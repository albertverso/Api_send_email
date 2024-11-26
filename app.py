from flask import Flask
from flask_mail import Mail
from config.config import Config
from app.routes import init_routes

app = Flask(__name__)

# Carrega as configurações da classe Config
app.config.from_object(Config)

# Inicializa a instância do Flask-Mail
mail = Mail(app)

# Inicializa as rotas
init_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
