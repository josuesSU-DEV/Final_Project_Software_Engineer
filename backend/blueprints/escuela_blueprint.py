from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify

from flask_cors import CORS, cross_origin # para que no genere errores de CORS al hacer peticiones

from backend.models.escuela_model import EscuelaModel

escuela_blueprint = Blueprint('escuela_blueprint', __name__)

model = EscuelaModel()

@escuela_blueprint.route('/escuela/create_escuela', methods=['POST'])
@cross_origin()
def create_escuela():
    content = model.create_escuela(int(request.json['idEscuela']),request.json['escuela'], int(request.json['anio']), int(request.json['numero_estudiantes']))    
    return jsonify(content)

@escuela_blueprint.route('/escuela/delete_escuela', methods=['POST'])
@cross_origin()
def delete_escuela():
    return jsonify(model.delete_escuela(int(request.json['idEscuela'])))

@escuela_blueprint.route('/escuela/get_escuela', methods=['POST'])
@cross_origin()
def escuela():
    return jsonify(model.get_escuela(int(request.json['idEscuela'])))

@escuela_blueprint.route('/escuela/get_all_escuela', methods=['POST'])
@cross_origin()
def all_escuela():
    return jsonify(model.get_all_escuela())