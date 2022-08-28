from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify

from flask_cors import CORS, cross_origin # para que no genere errores de CORS al hacer peticiones

from backend.models.curso_del_estudiante_model import CursoDelEstudianteModel

curso_del_estudiante_blueprint = Blueprint('curso_del_estudiante_blueprint', __name__)

model = CursoDelEstudianteModel()

#Ruta para crear cursos en la tabla cursos del estudiante
@curso_del_estudiante_blueprint.route('/curso_del_estudiante/create_curso_del_estudiante', methods=['POST'])
@cross_origin()
def create_curso_del_estudiante():
    content = model.create_curso_del_estudiante(int(request.json['cui']), request.json['curso1'],request.json['curso2'],request.json['curso3'],request.json['curso4'],request.json['curso5'] )    
    return jsonify(content)


#Ruta para borrar cursos en la tabla cursos del estudiante
@curso_del_estudiante_blueprint.route('/curso_del_estudiante/delete_curso_del_estudiante', methods=['POST'])
@cross_origin()
def delete_curso_del_estudiante():
    return jsonify(model.delete_curso_del_estudiante(int(request.json['cui'])))

#Ruta para crear cursos de un solo estudiante en la tabla cursos del estudiante
@curso_del_estudiante_blueprint.route('/curso_del_estudiante/get_curso_del_estudiante', methods=['POST'])
@cross_origin()
def curso_del_estudiante():
    return jsonify(model.get_curso_del_estudiante(int(request.json['cui'])))

#Ruta para retornar todos los cursos de todos los estudiantes en la tabla cursos del estudiante
@curso_del_estudiante_blueprint.route('/curso_del_estudiante/get_all_curso_del_estudiante', methods=['POST'])
@cross_origin()
def all_curso_del_estudiante():
    return jsonify(model.get_all_curso_del_estudiante())

