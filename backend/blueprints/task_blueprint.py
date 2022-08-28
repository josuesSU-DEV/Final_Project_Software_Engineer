from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify

from flask_cors import CORS, cross_origin # para que no genere errores de CORS al hacer peticiones

from backend.models.task_model import TaskModel

task_blueprint = Blueprint('task_blueprint', __name__)

model = TaskModel()

@task_blueprint.route('/task/create_task', methods=['POST'])
@cross_origin()
def create_task():
    content = model.create_task(request.json['title'], request.json['description'])    
    return jsonify(content)

@task_blueprint.route('/task/delete_task', methods=['POST'])
@cross_origin()
def delete_task():
    return jsonify(model.delete_task(int(request.json['id'])))

@task_blueprint.route('/task/get_task', methods=['POST'])
@cross_origin()
def task():
    return jsonify(model.get_task(int(request.json['id'])))

@task_blueprint.route('/task/get_tasks', methods=['POST'])
@cross_origin()
def tasks():
    return jsonify(model.get_tasks())

