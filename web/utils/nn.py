import torch

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

load = torch.load('./utils/modelo.pt')
nn.load_state_dict(load['state_dict'])
nn.norm_params = load['norm_params']

def _predict(features):
    nn.eval()
    
    input = torch.tensor(features, dtype=torch.float32).to(device)
        
    with torch.no_grad():
        output = nn(input)
        
        conf = output.cpu().numpy()
        pred = (conf[0] > 0.5).astype(int)
        
        # Mapeamento da predição
        classmap = {0: 'Máquina', 1: 'Humana'}
        pred = classmap[pred]
        
        return pred, '{:.2f}'.format(float(max(conf[0], 1-conf[0]) * 100))