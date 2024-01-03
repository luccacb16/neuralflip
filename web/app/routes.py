from flask import render_template, request, redirect, url_for, jsonify, session
from random import choices

from .utils.features import extract_features
from .utils.nn import _predict, validate

from . import db
from .db import Sequences, checkRetrain

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
            return jsonify({ 'erro': 'Sequência inválida' }), 400
        
        # Extração das features
        features = extract_features(seq)
            
        # Predição e Confiança
        pred, conf = _predict(features)
        
        predLanguageMap = {
            'pt-br': 'MÁQUINA' if pred == 0 else 'HUMANO',
            'en-us': 'MACHINE' if pred == 0 else 'HUMAN'
        }
        
        predtxt = predLanguageMap[session['language']]
                
        return jsonify({ 'predtxt': predtxt, 'pred': pred, 'conf': conf }), 200
    
    @app.post('/feedback')
    def feedback():
        data = request.get_json()
        seq = data.get('seq')
        label = data.get('label')
        
        # Adiciona a sequência ao banco de dados
        sequence = Sequences(seq=seq, label=label)
        db.session.add(sequence)
        db.session.commit()

        return jsonify({ 'seq': seq, 'label': label, 'msg': 'Feedback enviado com sucesso!' }), 200
    
    @app.get('/retrain')
    def retrain():
        tempo, loss = checkRetrain()
        
        if tempo == 0 and loss == 0:
            return jsonify({ 'msg': 'Não há tuplas suficientes para retreinar a rede' }), 400
        
        return jsonify({ 'msg': 'Retreinamento concluído', 'tempo': tempo, 'loss': loss }), 200

    '''
    gerar

    Função que gera uma sequência aleatória.

    Returns:
        - seq (str): sequência aleatória
    '''
    @app.get('/gerar')
    def gerar() -> str:
        return jsonify({ 'seq': ''.join(choices('01', k=50)) })
    
    @app.get('/ping')
    def ping():
        return {'status': 'Online'}, 200