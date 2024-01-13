from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

from .routes import routes
from .db.db import db
from .utils.nn import loadModel

def create_app():
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = os.urandom(24)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        
    db.init_app(app)

    with app.app_context():
        db.create_all()
        loadModel()

    routes(app)
    
    # Manter o backend online
    if (os.environ.get('PING') == 'True'):
        from .utils.keep_online import keep_online
        keep_online()

    return app