from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail

db = SQLAlchemy()
migrate = Migrate()
mail = Mail()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')

    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)

    from app.routes import api
    app.register_blueprint(api)

    return app
