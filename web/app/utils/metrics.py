import matplotlib.pyplot as plt
from flask import session
import seaborn as sns
import pandas as pd
import torch
import os

from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay

device = 'cpu'

# Diretório atual
dir = os.path.dirname(os.path.abspath(__file__))

testset = pd.read_csv(os.path.join(dir, 'test.csv'))

metrics_img_dir = os.path.join(dir, '../static/img/metrics/')

figsize = (10, 6)

def getTestSetMetricsReport(modelo: object) -> dict:
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
        
        cm = confusion_matrix(y.cpu().numpy(), pred)
        
    return report, cm

def saveMetrics(report, cm): 
    # Accuracy, Precision, Recall, F1-Score
    saveAccPrecRecF1(report, 'pt-br')
    saveAccPrecRecF1(report, 'en-us')
    
    # Matriz de Confusão
    saveConfusionMatrix(cm, 'pt-br')
    saveConfusionMatrix(cm, 'en-us')
    
    # Precisão e Recall
    savePrecision(report, 'pt-br')
    savePrecision(report, 'en-us')
    
    saveRecall(report, 'pt-br')
    saveRecall(report, 'en-us')
    
def saveAccPrecRecF1(report, language):
    # Weighted Avg
    acc = report['accuracy']                        # Vermelho
    prec = report['weighted avg']['precision']      # Amarelo
    rec = report['weighted avg']['recall']          # Verde
    f1 = report['weighted avg']['f1-score']         # Azul
    
    languageMap = {
        'pt-br': 
            ['Acurácia', 'Precisão', 'Recall', 'F1-Score'], 
        'en-us': 
            ['Accuracy', 'Precision', 'Recall', 'F1-Score']
    }
    
    # Plot das métricas
    plt.figure(figsize=figsize)
    plt.bar(languageMap[language], [acc, prec, rec, f1], color=['#ff0000', '#ffff00', '#00ff00', '#0000ff'])
    plt.ylim(0, 1)
    for i, v in enumerate([acc, prec, rec, f1]):
        plt.text(i-0.1, v+0.01, '{:.4f}'.format(v))
    plt.savefig(metrics_img_dir + f'accprecrecf1_{language}.png', bbox_inches='tight', transparent=True)
    plt.close()

def saveConfusionMatrix(cm, language):
    # Matriz de Confusão
    languageMap = {
        'pt-br': 
            ['Máquina', 'Humano'], 
        'en-us': 
            ['Machine', 'Human']
    }
    
    cm = ConfusionMatrixDisplay(cm, display_labels=languageMap[language])
    cm.plot(cmap='Blues', values_format='d')
    plt.savefig(metrics_img_dir + f'confusionmatrix_{language}.png', bbox_inches='tight', transparent=True)
    plt.close()
    
def savePrecision(report, language):
    maquina = report['0.0']['precision']
    humano = report['1.0']['precision']
    
    languageMap = {
        'pt-br': 
            ['Máquina', 'Humano'], 
        'en-us': 
            ['Machine', 'Human']
    }
    
    # Plot das métricas
    plt.figure(figsize=figsize)
    plt.bar(languageMap[language], [maquina, humano], color=['#ff0000', '#0000ff'])
    plt.ylim(0, 1)
    for i, v in enumerate([maquina, humano]):
        plt.text(i-0.1, v+0.01, '{:.4f}'.format(v))
    plt.savefig(metrics_img_dir + f'precision_{language}.png', bbox_inches='tight', transparent=True)
    plt.close()
    
def saveRecall(report, language):
    maquina = report['0.0']['recall']
    humano = report['1.0']['recall']
    
    languageMap = {
        'pt-br': 
            ['Máquina', 'Humano'], 
        'en-us': 
            ['Machine', 'Human']
    }
    
    # Plot das métricas
    plt.figure(figsize=figsize)
    plt.bar(languageMap[language], [maquina, humano], color=['#ff0000', '#0000ff'])
    plt.ylim(0, 1)
    for i, v in enumerate([maquina, humano]):
        plt.text(i-0.1, v+0.01, '{:.4f}'.format(v))
    plt.savefig(metrics_img_dir + f'recall_{language}.png', bbox_inches='tight', transparent=True)
    plt.close()