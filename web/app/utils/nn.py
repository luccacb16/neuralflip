import torch
from torch.utils.data import DataLoader, TensorDataset
import os
from sklearn.metrics import classification_report
import pandas as pd

from .features import extract_features
from ..db.models import getModel

dir = os.path.dirname(os.path.abspath(__file__))
device = 'cpu'

class NeuralNetwork(torch.nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        
        self.norm_params: list = None
        self.batch_size: int = None
        self.epochs: int = None
        
        self.layer1 = torch.nn.Linear(17, 32)
        self.relu = torch.nn.ReLU()
        
        self.layer2 = torch.nn.Linear(32, 32)
        
        self.output = torch.nn.Linear(32, 1)
        self.sigmoid = torch.nn.Sigmoid()

    def forward(self, x):
        if self.norm_params is not None:
            x = self.normalize(x)
                    
        x = self.relu(self.layer1(x))
        x = self.relu(self.layer2(x))
        x = self.sigmoid(self.output(x))
        
        return x
    
    def normalize(self, x):
        min_vals, max_vals = zip(*self.norm_params)
        
        min_vals = torch.tensor(min_vals, dtype=torch.float32).to(x.device)
        max_vals = torch.tensor(max_vals, dtype=torch.float32).to(x.device)
                
        return (x - min_vals) / (max_vals - min_vals)

nn = NeuralNetwork().to(device)

'''path = os.path.join(dir, 'modelo.pt')
load = torch.load(path, map_location=device)
nn.load_state_dict(load['state_dict'])
nn.norm_params = load['norm_params']'''

def loadModel():
    # Carregando o modelo
    id, model_state_dict, model_norm_params, createdAt, _ = getModel()
        
    nn.load_state_dict(model_state_dict)
    nn.norm_params = model_norm_params

    print(f'Modelo {id} - {createdAt} carregado')

    # Hiperparâmetros
    nn.batch_size = 16
    nn.epochs = 341

def _predict(features):
    nn.eval()
    
    input = torch.tensor(features, dtype=torch.float32).to(device)
        
    with torch.no_grad():
        output = nn(input)
        
        conf = output.cpu().numpy()
        pred = (conf[0] > 0.5).astype(int)
        
        return int(pred), '{:.2f}'.format(float(max(conf[0], 1-conf[0]) * 100))
    
def _train(optimizer, loss_function, train_loader):
    # Faz uma cópia da rede
    nn_copy = NeuralNetwork().to(device)
    nn_copy.load_state_dict(nn.state_dict())
    
    nn_copy.train()
    
    for epoch in range(nn.epochs):
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
    nn.load_state_dict(nn_copy.state_dict())
    
    return epoch_loss

def updateMinMax(features):  
    for i, (min, max) in enumerate(nn.norm_params):
        if features[i] < min: # Novo valor mínimo
            nn.norm_params[i] = (features[i], max)
            
        if features[i] > max: # Novo valor máximo
            nn.norm_params[i] = (min, features[i])
            
def train(seqs: list, labels: list):
    # Extrai as features
    features = [extract_features(seq) for seq in seqs]
    
    # Verifica novos valores mínimos e máximos
    for feature in features:
        updateMinMax(feature)
    
    # Normaliza as features
    features = [nn.normalize(torch.tensor(f, dtype=torch.float32)) for f in features]
    
    # Converte as features e labels para tensor
    features = torch.stack(features).to(device)
    labels = torch.tensor(labels, dtype=torch.float32).to(device)
    
    # Cria um DataLoader
    train_data = TensorDataset(features, labels)
    train_loader = DataLoader(train_data, batch_size=nn.batch_size, shuffle=True)
    
    # Cria o otimizador
    optimizer = torch.optim.Adam(nn.parameters())
    loss_function = torch.nn.BCELoss()
    
    # Retreina a rede
    loss = _train(optimizer, loss_function, train_loader)
    
    return loss

def metricas(modelo: object) -> dict:
    testset = pd.read_csv(os.path.join(dir, 'test.csv'))
    
    X = testset.drop('Classe', axis=1)
    y = testset['Classe']
    
    X = torch.tensor(X.values, dtype=torch.float32).to(device)
    y = torch.tensor(y.values, dtype=torch.float32).to(device)
    
    modelo.eval()
    with torch.no_grad():
        pred = modelo(X)
        pred = pred.squeeze()
        pred = (pred > 0.5).cpu().int().numpy()
        
        report = classification_report(y.cpu().numpy(), pred, output_dict=True)
        
    return report
    
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