#pip install flask
from flask import Flask, jsonify, request
from generate import gerar_password

app = Flask(__name__)

@app.route("/gerar", methods=["GET"])
def gerar():
    try:
        tamanho = int(request.args.get("tamanho", 8))
    except ValueError:
        return jsonify({"erro": "Tamanho inválido"}), 400

    password = gerar_password(tamanho)
    return jsonify({"password": password})

@app.route("/")
def home():
    return "API Gerador de Senhas funcionando!"

if __name__ == "__main__":
    app.run()
