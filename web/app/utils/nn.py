from torch.utils.data import DataLoader, TensorDataset
import torch.nn.functional as F
from torch import nn
import torch
import os

from .metrics import getTestSetMetricsReport
from .features import extract_features
from ..db.models import getModel, saveModel, checkForModel

dir = os.path.dirname(os.path.abspath(__file__))
device = 'cpu'
class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        
        # Salvar os parâmetros de normalização
        self.norm_params = None
        
        self.batch_size = None
        self.epochs = None

        '''
        Arquitetura:
        - Fully Connected
        - n_features x 64 com Normalização de Lote e Dropout de 0.1 e LeakyReLU
        - 64 x 32 com Normalização de Lote e Dropout de 0.1 e LeakyReLU
        - 32 x 16 com Normalização de Lote e Dropout de 0.1 e LeakyReLU
        - 16 x 1 com Sigmoid (para obter a probabilidade/confiança)
        '''
        
        self.fc1 = nn.Linear(23, 64)
        # Batch Normalization: Normalizar os dados para evitar overfitting
        self.bn1 = nn.BatchNorm1d(64)

        self.fc2 = nn.Linear(64, 32)
        self.bn2 = nn.BatchNorm1d(32)
        
        self.fc3 = nn.Linear(32, 16)
        self.bn3 = nn.BatchNorm1d(16)

        self.fc4 = nn.Linear(16, 1)

        # Dropout: Desligar neurônios aleatoriamente para evitar overfitting
        self.dropout = nn.Dropout(0.1)
        
        # Inicialização dos pesos e bias com Kaiming Uniform
        self.apply(self.init_weights)

    # Feed Forward
    def forward(self, x):
        if self.norm_params is not None:
            x = self.normalize(x)
            
        x = self.dropout(F.leaky_relu(self.bn1(self.fc1(x))))
        x = self.dropout(F.leaky_relu(self.bn2(self.fc2(x))))
        x = self.dropout(F.leaky_relu(self.bn3(self.fc3(x))))

        x = torch.sigmoid(self.fc4(x))
        return x
    
    def normalize(self, x):
        min_vals, max_vals = zip(*self.norm_params)
        
        min_vals = torch.tensor(min_vals, dtype=torch.float32).to(x.device)
        max_vals = torch.tensor(max_vals, dtype=torch.float32).to(x.device)
                
        return (x - min_vals) / (max_vals - min_vals)
    
    # Inicialização dos pesos e bias com Kaiming Uniform
    def init_weights(self, m):
        if isinstance(m, nn.Linear):
            nn.init.kaiming_uniform_(m.weight, mode='fan_in', nonlinearity='relu')
            if m.bias is not None:
                nn.init.zeros_(m.bias)

model = NeuralNetwork().to(device)

def loadModel():
    if checkForModel(): # Verifica se há um modelo salvo no BD
        # Carregando o modelo
        id, model_state_dict, model_norm_params, createdAt, _ = getModel()
        model.load_state_dict(model_state_dict)
        model.norm_params = model_norm_params
        # Hiperparâmetros
        model.batch_size = 16
        model.epochs = 16
        
        print(f'Modelo {id} - {createdAt} carregado')
    else:
        # Carrega o modelo do arquivo
        path = os.path.join(dir, 'modelo.pt')
        load = torch.load(path)
        
        model.load_state_dict(load['state_dict'])
        model.norm_params = load['norm_params']
        
        # Hiperparâmetros
        model.batch_size = 16
        model.epochs = 24
        print('Nenhum modelo no BD - carregado do arquivo')
    
        # Salva o modelo no BD
        report, _ = getTestSetMetricsReport(model)
        saveModel(model, report)

def _predict(features):
    model.eval()
    
    input = torch.tensor(features, dtype=torch.float32).to(device) # Converte para tensor
    input = input.unsqueeze(0) # Adiciona uma dimensão
                
    with torch.no_grad():
        output = model(input)
        
        conf = output.cpu().numpy()
        pred = (conf[0] > 0.5).astype(int)
        
        return int(pred), '{:.2f}'.format(float(max(conf[0], 1-conf[0]) * 100))
    
def _train(optimizer, loss_function, train_loader):
    # Faz uma cópia da rede
    nn_copy = NeuralNetwork().to(device)
    nn_copy.load_state_dict(model.state_dict())
    nn_copy.norm_params = model.norm_params
    
    nn_copy.train()
    for epoch in range(model.epochs):
        epoch_loss = 0
        for x, y in train_loader:
            optimizer.zero_grad()
            output = nn_copy(x)
            output = output.squeeze()
            loss = loss_function(output, y)
            loss.backward()
            optimizer.step()
            
            epoch_loss += loss.item()
    
        epoch_loss /= len(train_loader)
            
    # Atualiza a rede
    model.load_state_dict(nn_copy.state_dict())
    model.norm_params = nn_copy.norm_params
    
    return epoch_loss

def updateMinMax(features):  
    for i, (min, max) in enumerate(model.norm_params):
        if features[i] < min: # Novo valor mínimo
            model.norm_params[i] = (features[i], max)
            
        if features[i] > max: # Novo valor máximo
            model.norm_params[i] = (min, features[i])
            
def train(seqs: list, labels: list):
    # Extrai as features
    features = [extract_features(seq) for seq in seqs]
    
    # Verifica novos valores mínimos e máximos
    for feature in features:
        updateMinMax(feature)
        
    # Converte as features e labels para tensor
    features_tensor = [torch.tensor(feature, dtype=torch.float32) for feature in features]
    features = torch.stack(features_tensor).to(device)
    labels = torch.tensor(labels, dtype=torch.float32).to(device)
    
    # Cria um DataLoader
    train_data = TensorDataset(features, labels)
    train_loader = DataLoader(train_data, batch_size=model.batch_size, shuffle=True)
    
    # Cria o otimizador
    optimizer = torch.optim.Adam(model.parameters())
    loss_function = torch.nn.BCELoss()
    
    # Retreina a rede
    loss = _train(optimizer, loss_function, train_loader)
    
    return loss
    
'''
validate

Função que recebe a sequência e retorna se a sequência é válida ou não.

Args:
    - seq (str): sequência
    
Returns:
    - valid (bool): True se a sequência é válida, False caso contrário
'''
def validate(seq: str):
    return len(seq) == 50 and all([n in '01' for n in seq])