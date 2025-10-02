from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
# Habilita o CORS para permitir que o frontend React se comunique com esta API
CORS(app)

# Dados de exemplo que a API irá fornecer
livros_exemplo = [
    {"id": 1, "titulo": "O Senhor dos Anéis", "autor": "J.R.R. Tolkien"},
    {"id": 2, "titulo": "O Guia do Mochileiro das Galáxias", "autor": "Douglas Adams"},
    {"id": 3, "titulo": "Duna", "autor": "Frank Herbert"}
]

# Rota da API que retorna a lista de livros em formato JSON
@app.route("/api/books")
def get_books():
    return jsonify(livros_exemplo)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
