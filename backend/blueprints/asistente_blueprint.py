from flask import Blueprint
from flask import request
from flask import jsonify

from flask_cors import cross_origin # para que no genere errores de CORS al hacer peticiones

from backend.models.asistente import AsistenteModel
from backend.infrastructure.asistente_repository import AsistenteRepository

asistente_blueprint = Blueprint('asistente_blueprint', __name__)

repo = AsistenteRepository()

@asistente_blueprint.route('/api/asistente/create', methods=['POST']) # Verificar si se encuentra en la base de datos
@cross_origin()
def create_asistente():
    content = repo.create(int(request.json['id']), request.json['nombre'], request.json['apellido'], request.json['correo'])    
    return jsonify(content)

@asistente_blueprint.route('/api/asistente/get', methods=['POST']) # Verificar si se encuentra en la base de datos
@cross_origin()
def get_asistente():
    content = repo.get(int(request.json['id']))    
    return jsonify(content)

@asistente_blueprint.route('/api/asistente/create', methods=['POST']) # Verificar si se encuentra en la base de datos
@cross_origin()
def get_all_asistente():
    content = repo.get_all() 
    return jsonify(content)

@asistente_blueprint.route('/api/asistente/create', methods=['POST']) # Verificar si se encuentra en la base de datos
@cross_origin()
def delete_asistente():
    content = repo.delete(int(request.json['id']))    
    return jsonify(content)