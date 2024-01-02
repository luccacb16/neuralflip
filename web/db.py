from flask_sqlalchemy import SQLAlchemy

from app import app

db = SQLAlchemy(app)

class Sequence(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sequence = db.Column(db.String(50), nullable=False)
    label = db.Column(db.Integer, nullable=False)
    
db.create_all()