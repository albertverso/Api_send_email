from flask import request, jsonify, Blueprint
from src.send_email import send_email

routes_bp = Blueprint('routes', __name__)

@routes_bp.route('/send-email', methods=['POST'])
def send_email_route():
    data = request.json
    subject = data.get('subject', 'Sem Assunto')
    to = data['to']
    message = data['message']

    # Chama a função que envia o e-mail
    try:
        send_email(subject, to, message)
        return jsonify({"message": "E-mail enviado com sucesso!"}), 200
    except Exception as e:
        return jsonify({"message": f"Erro ao enviar o e-mail: {str(e)}"}), 500


@routes_bp.route('/', methods=['GET'])
def index():
    return jsonify({"message": "API de envio de e-mail"}), 200
