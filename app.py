import re
from flask import Flask, jsonify, render_template
from functions import numero_extenso


def create_app():
    app = Flask(__name__)

    @app.route('/')
    @app.route('/home')
    def home():
        return render_template('home.html'), 200

    @app.route('/scanapi')
    def scanapi():
        return render_template('tests-report.html')

    @app.route('/extenso/<num>', methods=['GET'])
    def main(num: str) -> dict:
        # checar se o valor é um valor válido.
        # Se não for, retorna mensagem de erro e status code 400 (bad request)
        if re.search(r'[^0-9|-]', num) != None:
            return jsonify(
                mensagem="O valor fornecido não é válido. Informe um valor inteiro entre [-99999,99999]."
            ), 400

        # checar se o valor é negativo
        num_out = "menos " if int(num) < 0 else ""

        # transforma o valor para o seu valor absoluto
        num = str(abs(int(num)))

        # se valor informado tiver 3 ou menos algarismos
        if len(num) <= 3:
            num_out += numero_extenso(num)
        # se o valor informado tiver mais de 4 e menos de 6 algarismos
        elif len(num) > 3 and len(num) < 6:
            milhares = numero_extenso(num[:-3])
            num_out += "mil" if milhares == "um" else milhares+" mil"
            unidades = numero_extenso(num[-3:])
            num_out += "" if unidades == "" else " e "+unidades
        # se tiver 6 ou mais algarismos
        else:
            return jsonify(
                mensagem="O valor informado se encontra fora do intervalo de [-99999,99999]"
            ), 400

        # se a variável tiver valor "", então o número é 0 (zero)
        num_out = "zero" if num_out == "" else num_out

        # retorna o número em extenso
        return jsonify(extenso=num_out), 200

    # retorna o app
    return app
