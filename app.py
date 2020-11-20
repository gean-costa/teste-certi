from flask import Flask, jsonify
from functions import numero_extenso


def create_app():
    app = Flask(__name__)

    @app.route('/home')
    def home():
        return 'Olá, seja bem-vindo', 200

    @app.route('/<num>', methods=['GET'])
    def main(num):
        num_out = "menos " if int(num) < 0 else ""
        num = str(abs(int(num)))
        
        if len(num) <= 3:
            num_out += numero_extenso(num)
        elif len(num) > 3 and len(num)<6:
            milhares = numero_extenso(num[:-3])
            num_out += "mil" if milhares == "um" else milhares+" mil"
            unidades = numero_extenso(num[-3:])
            num_out += "" if unidades == "" else " e "+unidades
        else:
            return jsonify(status="erro", mensagem="Number out of range")

        num_out = "zero" if num_out == "" else num_out

        return jsonify(extenso=num_out), 200

    return app
