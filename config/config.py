import os

class Config:
    # Configurações do servidor de e-mail
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')  # Carregado do arquivo .env
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')  # Carregado do arquivo .env
