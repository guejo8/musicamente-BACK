from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Crea una función para establecer la conexión con MongoDB Atlas
def get_database_connection():
    uri = "mongodb+srv://root:swwaohTbDXF2Mf8Q@cluster0.xeild8p.mongodb.net/musicamente?retryWrites=true&w=majority"
    client = MongoClient(uri)
    return client["musicamente"]

# Obtiene una referencia a la colección
collection = get_database_connection()["lessons"]

@app.route('/')
def hello():
    return 'Hello from Flask!'

# CREATE: Insertar un nuevo documento en la colección
@app.route('/api/data', methods=['POST'])
def insertar_documento():
    nuevo_documento = request.json
    insert_result = collection.insert_one(nuevo_documento)
    return jsonify({"message": "Documento insertado con el ID:", "inserted_id": str(insert_result.inserted_id)}), 201

# READ: OBTENER TODOS los documentos
@app.route('/api/data', methods=['GET'])
def obtener_todos_documentos():
    documentos = list(collection.find({}))

    # Convertir ObjectId a cadena en cada documento
    for documento in documentos:
        documento["_id"] = str(documento["_id"])

    return jsonify(documentos)

# READ: OBTENER un documento por su ID
@app.route('/api/data/<string:documento_id>', methods=['GET'])
def obtener_documento_por_id(documento_id):
    documento_obtenido = collection.find_one({"_id": ObjectId(documento_id)})
    if documento_obtenido:
        documento_obtenido["_id"] = str(documento_obtenido["_id"])  # Convertir ObjectId a cadena
        return jsonify(documento_obtenido)
    else:
        return jsonify({"message": "Documento no encontrado"}), 404

# UPDATE: editar un documento por su ID
@app.route('/api/data/<string:documento_id>', methods=['PUT'])
def actualizar_documento_por_id(documento_id):
    nuevos_datos = request.json
    result = collection.update_one({"_id": ObjectId(documento_id)}, {"$set": nuevos_datos})
    if result.modified_count > 0:
        return jsonify({"message": "Documento actualizado correctamente"}), 200
    else:
        return jsonify({"message": "Documento no encontrado"}), 404

# DELETE: Borrar un documento por su ID
@app.route('/api/data/<string:documento_id>', methods=['DELETE'])
def eliminar_documento_por_id(documento_id):
    result = collection.delete_one({"_id": ObjectId(documento_id)})
    if result.deleted_count > 0:
        return jsonify({"message": "Documento eliminado correctamente"}), 200
    else:
        return jsonify({"message": "Documento no encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)
