from flask import request, jsonify
from app import send_email

def init_routes(app):
    @app.route('/send-email', methods=['POST'])
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
