
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "D’YHANY está en línea."

@app.route('/hablar', methods=['POST'])
def hablar():
    data = request.get_json()
    texto_usuario = data.get("texto", "")
    return jsonify({"respuesta": f"Recibí tu mensaje: {texto_usuario}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
