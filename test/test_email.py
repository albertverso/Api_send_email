from flask_mail import Mail, Message
from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('EMAIL')
app.config['MAIL_PASSWORD'] = os.getenv('PASSWORD')

mail = Mail(app)

with app.app_context():
    try:
        msg = Message(subject="Teste de E-mail",
                      sender=app.config['MAIL_USERNAME'],
                      recipients=['alsguert@gmail.com'],
                      body="Este é um teste de envio de e-mail.")
        mail.send(msg)
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {str(e)}")