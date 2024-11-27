from flask_mail import Message
from config.config import Config

def send_email(subject, to, message):
    from app import mail

    #print(f"emailll {Config.MAIL_USERNAME}")
    
    try:
        msg = Message(
            subject=subject,
            recipients=[to],
            body=message
        )
        mail.send(msg)
        return {"message": "E-mail enviado com sucesso!"}, 200
    except Exception as e:
        return {"error": str(e)}, 500