from flask_sqlalchemy import SQLAlchemy
import numpy as np

from .utils.nn import retrain

db = SQLAlchemy()

class Sequences(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    seq = db.Column(db.String(50), nullable=False)
    label = db.Column(db.Integer, nullable=False)
    
def checkRetrain():
    count0 = Sequences.query.filter_by(label=0).count()
    count1 = Sequences.query.filter_by(label=1).count()

    # Early return se não há tuplas suficientes
    if not (count0 >= 8 and count1 >= 8):
        return 0, 0
    
    # Obtém os ids das tuplas
    zeros_id = findIdsByLabel(0)    
    ones_id = findIdsByLabel(1)
    
    # Obtém as sequências
    zeros = [findById(id[0]) for id in zeros_id]
    ones = [findById(id[0]) for id in ones_id]
    
    # Separa as sequências das labels
    zeros_seqs = [seq[1] for seq in zeros]
    zeros_labels = [seq[2] for seq in zeros]
    ones_seqs = [seq[1] for seq in ones]
    ones_labels = [seq[2] for seq in ones]
    
    # Une os pares
    seqs = zeros_seqs + ones_seqs
    labels = zeros_labels + ones_labels
    
    # Deleta as tuplas
    for id in zeros_id:
        deleteById(id[0])
        
    for id in ones_id:
        deleteById(id[0])
    
    # Retreina
    tempo, loss = retrain(seqs, labels)
    
    return tempo, loss
    
def findById(id: int) -> Sequences:
    seq = Sequences.query.get(id)
    
    return seq.id, seq.seq, seq.label

def findIdsByLabel(label: int) -> list:
    return Sequences.query.filter_by(label=label).order_by(Sequences.id).limit(8).with_entities(Sequences.id)

def deleteById(id: int) -> None:
    Sequences.query.filter_by(id=id).delete(synchronize_session=False)
    db.session.commit()