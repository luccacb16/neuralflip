import pytz
import datetime

from .db import db
class Models(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    state_dict = db.Column(db.PickleType, nullable=False)
    norm_params = db.Column(db.PickleType, nullable=True)
    createdAt = db.Column(db.DateTime, nullable=False)
    report = db.Column(db.PickleType, nullable=False)
    
def saveModel(modelo: object, report: dict) -> None:
    modelo_state_dict = modelo.state_dict()
    modelo_norm_params = modelo.norm_params
    
    modelo = Models(state_dict=modelo_state_dict, norm_params=modelo_norm_params, createdAt=getDatetime(), report=report)
    db.session.add(modelo)
    db.session.commit()
    
    print('Modelo salvo com sucesso!')
    
def checkForModel() -> bool:
    return Models.query.first() is not None
    
def getModel(id: int = None) -> tuple:
    if id:
        modelo = Models.query.get(id)
    else:
        modelo = Models.query.order_by(Models.createdAt.desc()).first()
    
    return modelo.id, modelo.state_dict, modelo.norm_params, modelo.createdAt, modelo.report

def getDatetime(timezone="America/Sao_Paulo"):
    return pytz.timezone(timezone).localize(datetime.datetime.now())

def getModelsReportsAndDates() -> list:
    models = Models.query.order_by(Models.createdAt.desc()).all()
    
    modelsReportsAndDates = []
    for modelo in models:
        modelsReportsAndDates.append((modelo.report, modelo.createdAt))
    
    return modelsReportsAndDates