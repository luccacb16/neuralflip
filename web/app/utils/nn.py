import torch
from torch.utils.data import DataLoader, TensorDataset
import os
import time

from .features import extract_features

device = 'cpu'

class NeuralNetwork(torch.nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        
        self.norm_params = None
        self.batch_size = None
        self.epochs = None
        
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

dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(dir, 'modelo.pt')

load = torch.load(path, map_location=device)
nn.load_state_dict(load['state_dict'])
nn.norm_params = load['norm_params']

# Parâmetros
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
    
def _retrain(optimizer, loss_function, train_loader):
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
    
def retrain(seqs: list, labels: list):
    start = time.time()
    
    # Extrai as features
    features = [torch.tensor(extract_features(seq), dtype=torch.float32) for seq in seqs]
    
    # Normaliza as features
    features = [nn.normalize(f) for f in features]
    
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
    loss = _retrain(optimizer, loss_function, train_loader)
    
    end = time.time()
    
    tempo = '{:.2f}'.format(end - start)
    
    print(f'Retreinamento concluído em {tempo} segundos')
    print(f'Loss: {loss:.4f}\n')
    
    return tempo, loss
    
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