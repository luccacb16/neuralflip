from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Sequences(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    seq = db.Column(db.String(50), nullable=False)
    label = db.Column(db.Integer, nullable=False)