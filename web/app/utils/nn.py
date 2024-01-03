import torch
import os

device = 'cuda' if torch.cuda.is_available() else 'cpu'

class NeuralNetwork(torch.nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        
        self.norm_params = None
        
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

load = torch.load(path)
nn.load_state_dict(load['state_dict'])
nn.norm_params = load['norm_params']

def _predict(features):
    nn.eval()
    
    input = torch.tensor(features, dtype=torch.float32).to(device)
        
    with torch.no_grad():
        output = nn(input)
        
        conf = output.cpu().numpy()
        pred = (conf[0] > 0.5).astype(int)
        
        return int(pred), '{:.2f}'.format(float(max(conf[0], 1-conf[0]) * 100))
    
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