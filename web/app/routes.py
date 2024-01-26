from flask import render_template, request, redirect, url_for, jsonify, session
from random import choices
import time
import os

from .utils.features import extract_features
from .utils.nn import _predict, validate, train, nn
from .utils.metrics import saveMetrics, getTestSetMetricsReport, metrics_img_dir, plotModelEvolution

from .db.sequences import addSequenceToDB, checkRetrain, getSequences
from .db.models import saveModel
    
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
    @app.route('/sobre')
    def sobre():
        language = session.get('language', 'pt-br')
        session['language'] = language
        
        return render_template('sobre_' + language + '.html')
    
    # Página Métricas
    @app.route('/metricas')
    def metricas():
        language = session.get('language', 'pt-br')
        session['language'] = language
        
        # Obtendo as métricas
        imgs = ['accprecrecf1', 'confusionmatrix', 'precision', 'recall']
        
        if not all([os.path.isfile(metrics_img_dir + img + '_' + language + '.png') for img in imgs]):
            report, cm = getTestSetMetricsReport(nn)
            saveMetrics(report, cm)
            
        # Evolução dos modelos
        evolution_html = plotModelEvolution(language)
        
        return render_template('metricas_' + language + '.html', evolution_plot=evolution_html)

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
        addSequenceToDB(seq, label)

        return jsonify({ 'seq': seq, 'label': label, 'msg': 'Feedback enviado com sucesso!' }), 200
    
    @app.get('/retrain')
    def retrain():
        if checkRetrain(8):            
            # Salva o modelo no BD
            report, _ = getTestSetMetricsReport(nn)
            saveModel(nn, report)
    
            seqs, labels = getSequences()
            
            start = time.time()
            loss = train(seqs, labels)
            end = time.time()
            
            tempo = '{:.2f}'.format(end - start)
            
            # Atualiza as imagens das métricas
            report, cm = getTestSetMetricsReport(nn)
            saveMetrics(report, cm, session['language'])
            
            print(f'Tempo de retreinamento: {tempo} segundos - Loss: {loss:.4f}')
            return jsonify({ 'msg': 'Retreinamento concluído', 'tempo': tempo, 'loss': loss }), 200

        return jsonify({ 'msg': 'Não há tuplas suficientes para retreinar a rede' }), 400

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