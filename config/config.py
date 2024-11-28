import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Configurações do servidor de e-mail
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv('EMAIL')  # Carregado do arquivo .env
    MAIL_PASSWORD = os.getenv('PASSWORD')  # Carregado do arquivo .env