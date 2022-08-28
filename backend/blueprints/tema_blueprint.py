from flask import Blueprint
from flask import request
from flask import jsonify

from flask_cors import cross_origin # para que no genere errores de CORS al hacer peticiones

from backend.models.tema import Tema
from backend.infrastructure.tema_repository import TemaRepository

tema_blueprint = Blueprint('tema_blueprint', __name__)

repo = TemaRepository()

@tema_blueprint.route('/api/tema/create', methods=['POST']) # Verificar si se encuentra en la base de datos
@cross_origin()
def create_tema():
    content = repo.create(int(request.json['id']), request.json['nombre'])    
    return jsonify(content)

@tema_blueprint.route('/api/tema/get', methods=['POST']) # Verificar si se encuentra en la base de datos
@cross_origin()
def get_tema():
    content = repo.get(int(request.json['id']))    
    return jsonify(content)

@tema_blueprint.route('/api/tema/get_all', methods=['POST']) # Verificar si se encuentra en la base de datos
@cross_origin()
def get_all_tema():
    content = repo.get_all() 
    return jsonify(content)

@tema_blueprint.route('/api/tema/delete', methods=['POST']) # Verificar si se encuentra en la base de datos
@cross_origin()
def delete_tema():
    content = repo.delete(int(request.json['id']))    
    return jsonify(content)