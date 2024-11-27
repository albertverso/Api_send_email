from flask_mail import Mail
from flask import Flask
from config.config import Config
from flask_cors import CORS
from app.routes import routes_bp  # Importa o Blueprint

mail = Mail()

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Carrega as configurações
    app.config.from_object(Config)

    # Inicializa o Flask-Mail
    mail.init_app(app)

    # Registra o Blueprint
    app.register_blueprint(routes_bp)

    return app