from flask import Flask, render_template, request, redirect, url_for, jsonify
from random import choices

from utils.features import extract_features
from utils.nn import _predict

app = Flask(__name__)

# Index
@app.route('/')
def home():
    return render_template('base.html')

# Página Sobre
@app.route('/sobre/')
def sobre():
    return render_template('sobre.html')

'''
predict

Endpoint que recebe a sequência e retorna a predição do modelo.

Args:
    - seq (str): sequência
    
Returns:
    - pred (str): predição da rede neural
'''
@app.get('/predict/<seq>')
def predict(seq: str):
    # Validação da sequência
    if not validate(seq):
        return jsonify({'erro': 'Sequência inválida'}), 400
    
    # Extração das features
    features = extract_features(seq)
        
    # Predição e Confiança
    pred, conf = _predict(features)
            
    return jsonify({'pred': pred, 'conf': conf}), 200

'''
gerar

Função que gera uma sequência aleatória.

Returns:
    - seq (str): sequência aleatória
'''
@app.get('/gerar')
def gerar() -> str:
    return jsonify({'seq': ''.join(choices('01', k=50))})

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