import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY=os.urandom(24),
        SQLALCHEMY_DATABASE_URI='sqlite:///db.sqlite'
    )

    db.init_app(app)

    from .main import main_bp as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth_bp as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app
