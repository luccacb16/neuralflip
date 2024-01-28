import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
import torch

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Plotar as métricas
def plot_metrics(metrics_dict, epochs, n=8):
    interval = epochs // n
    yy = [i * interval for i in range(n)] + [epochs]

    mean_acc = [np.mean(metrics_dict['acc'][:i+1]) if i != 0 else metrics_dict['acc'][0] for i in yy]
    mean_prec = [np.mean(metrics_dict['prec'][:i+1]) if i != 0 else metrics_dict['prec'][0] for i in yy]
    mean_rec = [np.mean(metrics_dict['rec'][:i+1]) if i != 0 else metrics_dict['rec'][0] for i in yy]
    mean_f1 = [np.mean(metrics_dict['f1'][:i+1]) if i != 0 else metrics_dict['f1'][0] for i in yy]

    return yy, mean_acc, mean_prec, mean_rec, mean_f1

# Plotar a loss
def plot_loss(losses, epochs):
    return list(range(epochs)), losses

# Plotar a matriz de confusão
def plot_confusion_matrix(y_true, y_pred):
    conf_matrix = confusion_matrix(y_true, y_pred)
    return conf_matrix

# Plotar todas as métricas
def plot_all(metrics_train, metrics_test, losses, y_true, y_pred, epochs):
    yy, mean_acc, mean_prec, mean_rec, mean_f1 = metrics_train
    yy_loss, losses = plot_loss(losses, epochs)
    conf_matrix = plot_confusion_matrix(y_true, y_pred)
    
    fig, axs = plt.subplots(1, 4, figsize=(32, 8))

    # Metrics Train
    axs[0].plot(yy, mean_acc, label='Accuracy')
    axs[0].plot(yy, mean_prec, label='Precision')
    axs[0].plot(yy, mean_rec, label='Recall')
    axs[0].plot(yy, mean_f1, label='F1')
    axs[0].set_title('Metrics Train')
    axs[0].set_xlabel('Épocas')
    axs[0].set_ylabel('Métricas')
    axs[0].legend()

    # Metrics Test
    yy, mean_acc, mean_prec, mean_rec, mean_f1 = metrics_test
    axs[1].plot(yy, mean_acc, label='Accuracy')
    axs[1].plot(yy, mean_prec, label='Precision')
    axs[1].plot(yy, mean_rec, label='Recall')
    axs[1].plot(yy, mean_f1, label='F1')
    axs[1].set_title('Metrics Test')
    axs[1].set_xlabel('Épocas')
    axs[1].set_ylabel('Métricas')
    axs[1].legend()

    # Loss
    axs[2].plot(yy_loss, losses)
    axs[2].set_xlim(0, 15)
    axs[2].set_title('Loss')
    axs[2].set_xlabel('Épocas')
    axs[2].set_ylabel('Loss')

    # Confusion Matrix
    sns.heatmap(conf_matrix, annot=True, ax=axs[3], cmap='Blues',
                xticklabels=['Máquina', 'Humana'],
                yticklabels=['Máquina', 'Humana'], fmt='d')
    axs[3].set_title('Confusion Matrix')
    axs[3].set_xlabel('Predicted Label')
    axs[3].set_ylabel('True Label')

    plt.tight_layout()
    plt.show()
    
def calculate_metrics(model, data_loader):
    model.eval()
    y_true = []
    y_pred = []

    with torch.no_grad():
        for X_batch, y_batch in data_loader:
            X_batch = X_batch.to(device)
            outputs = model(X_batch)
            predictions = outputs.round()
            y_true += y_batch.tolist()
            y_pred += predictions.tolist()

    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred, zero_division=0)
    recall = recall_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)
    return accuracy, precision, recall, f1

def MinMax(X, mins, maxes):
    return (X - mins) / (maxes - mins)