from flask import Flask, jsonify
from functions import numero_extenso

app = Flask(__name__)


@app.route('/<num>', methods=['GET'])
def main(num):
    num_out = "menos " if int(num)<0 else ""
    num = str(abs(int(num)))
    if len(num)<=3:
        num_out += numero_extenso(num)
    else:
        num_out += numero_extenso(num[:-3]) + " mil e "
        num_out += numero_extenso(num[-3:])
    
    return jsonify({"extenso": num_out})

