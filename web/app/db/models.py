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
    
    model = Models(state_dict=modelo_state_dict, norm_params=modelo_norm_params, createdAt=getDatetime(), report=report)
    db.session.add(model)
    db.session.commit()
    
    print('Modelo salvo com sucesso!')
    
def getModel(id: int = None) -> tuple:
    if id:
        model = Models.query.get(id)
    else:
        model = Models.query.order_by(Models.createdAt.desc()).first()
    
    return model.id, model.state_dict, model.norm_params, model.createdAt, model.report

def getDatetime(timezone="America/Sao_Paulo"):
    return pytz.timezone(timezone).localize(datetime.datetime.now())