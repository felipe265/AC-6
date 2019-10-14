import os
from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/')
def nao_entre_em_panico():
    for i in range(1, 550):
        divisores = 0
        for divisor in range(1, i+1):
            if i % divisor == 0:
                divisores += 1
        if divisores == 2:
            return i


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
