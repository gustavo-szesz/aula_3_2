from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

# Configuração do MongoDB
uri = "mongodb+srv://admin_gs:<SENHA>@cluster0.n8rvg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)
db = client['compradb']
collection = db['comprascol']

# Constantes 
HTTP_OK = 200
HTTP_NOT_FOUND = 404
HTTP_INTERNAL_SERVER_ERROR = 500
HTTP_NOT_IMPLEMENTED = 501
HTTP_BAD_GATEWAY = 502
  
# Rotas CRUD

# GET /produtos
@app.route('/produtos', methods=['GET'])
def get_produtos():  
    try:
        produtos = list(collection.find())
        for produto in produtos:
            produto['_id'] = str(produto['_id'])  # Converte ObjectId para string
        return jsonify(produtos), HTTP_OK
    except Exception as e:
        return jsonify({'error': str(e)}), HTTP_INTERNAL_SERVER_ERROR

# POST /produtos
@app.route('/produtos', methods=['POST'])
def add_produto():
    try:
        data = request.json
        produto = {
            "nome": data.get("nome"),
            "fornecedor": data.get("fornecedor"),
            "endereco_fornecedor": data.get("endereco_fornecedor"),
            "quantidade": data.get("quantidade"),
            "endereco": data.get("endereco"),
            "preco_unitario": data.get("preco_unitario")
        }
        result = collection.insert_one(produto)
        return jsonify({"message": "Produto adicionado", "id": str(result.inserted_id)}), HTTP_OK
    except Exception as e:
        return jsonify({'error': str(e)}), HTTP_INTERNAL_SERVER_ERROR

# PUT /produtos/:id: querystrring
# OBSERVAÇÃO: as IDs são geradas automaticamente pelo MongoDB e são hashes de 24 caracteres
# Para atualizar um produto, é necessário informar a ID gerada pelo MongoDB
@app.route('/produtos/<id>', methods=['PUT'])
def update_produto(id):
    try:
        data = request.json
        updated_data = {
            "nome": data.get("nome"),
            "fornecedor": data.get("fornecedor"),
            "endereco_fornecedor": data.get("endereco_fornecedor"),
            "quantidade": data.get("quantidade"),
            "endereco": data.get("endereco"),
            "preco_unitario": data.get("preco_unitario")
        }
        result = collection.update_one({"_id": ObjectId(id)}, {"$set": updated_data})
        if result.matched_count == 0:
            return jsonify({"error": "Produto não encontrado"}), HTTP_NOT_FOUND
        return jsonify({"message": "Produto atualizado"}), HTTP_OK
    except Exception as e:
        return jsonify({'error': str(e)}), HTTP_INTERNAL_SERVER_ERROR

# DELETE /produtos/:id: 
@app.route('/produtos/<id>', methods=['DELETE'])
def delete_produto(id):
    try:
        result = collection.delete_one({"_id": ObjectId(id)})
        if result.deleted_count == 0:
            return jsonify({"error": "Produto não encontrado"}), HTTP_NOT_FOUND
        return jsonify({"message": "Produto removido"}), HTTP_OK
    except Exception as e:
        return jsonify({'error': str(e)}), HTTP_INTERNAL_SERVER_ERROR




# Tratamentos de erros
@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify({"error": "Método não implementado"}), HTTP_NOT_IMPLEMENTED

@app.errorhandler(502)
def bad_gateway(e):
    return jsonify({"error": "Erro externo"}), HTTP_BAD_GATEWAY



if __name__ == '__main__':
    app.run(port=3000, debug=True)