from .db import db

class Sequences(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    seq = db.Column(db.String(50), nullable=False)
    label = db.Column(db.Integer, nullable=False)
    
def checkRetrain(n: int):
    count0 = Sequences.query.filter_by(label=0).count()
    count1 = Sequences.query.filter_by(label=1).count()

    return count0 >= n and count1 >= n

def getSequences() -> list:
    # Obtém os ids das tuplas
    zeros_id = findSequencesIdsByLabel(0)    
    ones_id = findSequencesIdsByLabel(1)
    
    # Obtém as sequências
    zeros = [findSequenceById(id[0]) for id in zeros_id]
    ones = [findSequenceById(id[0]) for id in ones_id]
    
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
        deleteSequenceById(id[0])
    for id in ones_id:
        deleteSequenceById(id[0])
    db.session.commit()
    
    return seqs, labels
    
def addSequenceToDB(seq: str, label: int) -> None:
    sequence = Sequences(seq=seq, label=label)
    db.session.add(sequence)
    db.session.commit()    

def findSequenceById(id: int) -> Sequences:
    seq = Sequences.query.get(id)
    
    return seq.id, seq.seq, seq.label

def findSequencesIdsByLabel(label: int) -> list:
    return Sequences.query.filter_by(label=label).order_by(Sequences.id).limit(8).with_entities(Sequences.id)

def deleteSequenceById(id: int) -> None:
    Sequences.query.filter_by(id=id).delete(synchronize_session=False)