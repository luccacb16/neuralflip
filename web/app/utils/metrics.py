import matplotlib.pyplot as plt
import plotly.graph_objects as go
from flask import session
import seaborn as sns
import pandas as pd
import torch
import os

from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay

from ..db.models import getModelsReportsAndDates

device = 'cpu'

# Diretório atual
dir = os.path.dirname(os.path.abspath(__file__))

testset = pd.read_csv(os.path.join(dir, 'test.csv'))

metrics_img_dir = os.path.join(dir, '../static/img/metrics/')

figsize = (10, 6)
fontsize = 14

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
    prec = report['weighted avg']['precision']      # Azul
    rec = report['weighted avg']['recall']          # Verde
    f1 = report['weighted avg']['f1-score']         # Amarelo
    
    languageMap = {
        'pt-br': ['Acurácia', 'Precisão', 'Recall', 'F1-Score'], 
        'en-us': ['Accuracy', 'Precision', 'Recall', 'F1-Score']
    }
    
    # Plot das métricas
    plt.figure(figsize=figsize)
    bars = plt.bar(languageMap[language], [acc, prec, rec, f1], color=['#ff0000', '#0000ff', '#00ff00', '#ffff00'])
    plt.ylim(0, 1)

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.01, '{:.4f}'.format(yval), ha='center', fontdict={'fontsize': 14})

    plt.savefig(metrics_img_dir + f'accprecrecf1_{language}.png', bbox_inches='tight', transparent=True)
    plt.close()

def saveConfusionMatrix(cm, language):
    languageMap = {
        'pt-br': [['Máquina', 'Humano'], ['Rótulo Verdadeiro', 'Rótulo Predito']],
        'en-us': [['Machine', 'Human'], ['True Label', 'Predicted Label']]
    }

    plt.figure(figsize=figsize)
    sns.heatmap(cm, annot=True, fmt="d", cmap='Blues', cbar=False,
                xticklabels=languageMap[language][0], yticklabels=languageMap[language][0], annot_kws={"size": 20})
    
    plt.ylabel(languageMap[language][1][0])
    plt.xlabel(languageMap[language][1][1])

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
    plt.bar(languageMap[language], [maquina, humano], color=['#0364a1', '#023e63'])
    plt.ylim(0, 1)
    for i, v in enumerate([maquina, humano]):
        plt.text(i-0.1, v+0.01, '{:.4f}'.format(v), fontdict={'fontsize': fontsize})
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
    plt.bar(languageMap[language], [maquina, humano], color=['lightgreen', 'green'])
    plt.ylim(0, 1)
    for i, v in enumerate([maquina, humano]):
        plt.text(i-0.1, v+0.01, '{:.4f}'.format(v), fontdict={'fontsize': fontsize})
    plt.savefig(metrics_img_dir + f'recall_{language}.png', bbox_inches='tight', transparent=True)
    plt.close()

def plotModelEvolution(language='pt-br'):
    languageMap = {
        'pt-br': {
            'Accuracy': 'Acurácia', 
            'Precision': 'Precisão', 
            'Recall': 'Recall', 
            'F1-Score': 'F1-Score',
            'Data': 'Data',
        },
        'en-us': {
            'Accuracy': 'Accuracy', 
            'Precision': 'Precision', 
            'Recall': 'Recall', 
            'F1-Score': 'F1-Score',
            'Data': 'Date',
        }
    }

    reports = getModelsReportsAndDates()

    dates = [report[1] for report in reports]
    accuracies = [report[0]['accuracy'] for report in reports]
    precisions = [report[0]['weighted avg']['precision'] for report in reports]
    recalls = [report[0]['weighted avg']['recall'] for report in reports]
    f1_scores = [report[0]['weighted avg']['f1-score'] for report in reports]

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=dates, 
        y=accuracies, 
        mode='lines+markers', 
        name=languageMap[language]['Accuracy'],
        hoverinfo='text',
        text=[
            f'{languageMap[language]["Accuracy"]}: {a:.4f}<br>'
            f'{languageMap[language]["Precision"]}: {p:.4f}<br>'
            f'{languageMap[language]["Recall"]}: {r:.4f}<br>'
            f'{languageMap[language]["F1-Score"]}: {f:.4f}' 
            for a, p, r, f in zip(accuracies, precisions, recalls, f1_scores)
        ]
    ))

    fig.update_layout(
        xaxis_title=languageMap[language]['Data'],
        yaxis_title=languageMap[language]['Accuracy'],
        hovermode='closest',
        width=800,
        height=400,
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(t=0, l=0, b=0, r=0),
        yaxis=dict(range=[0, 1])
    )

    return fig.to_html(full_html=False)