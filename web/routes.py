from flask import render_template, request, redirect, url_for, jsonify, session
from random import choices

from utils.features import extract_features
from utils.nn import _predict, validate

def routes(app):
    # Index
    @app.route('/')
    def home():
        language = session.get('language', 'pt-br')
        session['language'] = language
        
        return render_template('home_' + language + '.html')

    # Linguagem
    @app.post('/language')
    def language():
        data = request.get_json()
        language = data.get('language')
        
        session['language'] = language
        
        return redirect(url_for('home'))

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
        
        predLanguageMap = {
            'pt-br': 'MÁQUINA' if pred == 0 else 'HUMANO',
            'en-us': 'MACHINE' if pred == 0 else 'HUMAN'
        }
        
        pred = predLanguageMap[session['language']]
                
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