from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

from .db import db
from .routes import routes

def create_app():
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = os.urandom(24)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        
    db.init_app(app)

    with app.app_context():
        db.create_all()

    routes(app)
    
    # Manter o backend online
    from .utils.keep_online import keep_online
    keep_online()

    return app
