from flask_mail import Message
from app import mail
from config.config import Config

def send_email(subject, to, message):
    try:
        msg = Message(
            subject=subject,
            sender=Config.MAIL_USERNAME,  # Substitua pelo seu e-mail
            recipients=[to],
            body=message
        )
        mail.send(msg)
        return {"message": "E-mail enviado com sucesso!"}, 200
    except Exception as e:
        return {"error": str(e)}, 500
