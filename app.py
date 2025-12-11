from flask import Flask, jsonify, request
from flask_cors import CORS
from generate import gerar_password
import os

app = Flask(__name__)
CORS(app)  m

@app.route("/gerar", methods=["GET"])
def gerar():

    tamanho = request.args.get("tamanho")
    if tamanho is None:
        return jsonify({"erro": "O parâmetro 'tamanho' é obrigatório."}), 400

    try:
        tamanho = int(tamanho)
    except ValueError:
        return jsonify({"erro": "Tamanho inválido, envie um número."}), 400

    use_upper   = request.args.get("maiuscula") == "true"
    use_lower   = request.args.get("minuscula") == "true"
    use_number  = request.args.get("numero") == "true"
    use_special = request.args.get("especial") == "true"

    if not (use_upper or use_lower or use_number or use_special):
        return jsonify({"erro": "Selecione pelo menos uma opção!"}), 400

    password = gerar_password(
        qnt=tamanho,
        use_upper=use_upper,
        use_lower=use_lower,
        use_number=use_number,
        use_special=use_special
    )

    return jsonify({"password": password})

@app.route("/")
def home():
    return "API Gerador de Senhas funcionando!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
