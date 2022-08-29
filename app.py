from urllib import response
import requests

from flask import Flask, session, redirect, g
from flask import request
from flask import jsonify
from flask import render_template,url_for
from flask_cors import CORS, cross_origin # para que no genere errores de CORS al hacer peticiones

from backend.blueprints.evento_blueprint import evento_blueprint
from backend.blueprints.ponente_blueprint import ponente_blueprint

from backend.models.evento import EventoModel
from backend.models.ponente import PonenteModel

app = Flask(__name__,template_folder='frontend/templates',static_folder='frontend/static')

app.secret_key= "averysecretkey"


app.register_blueprint(evento_blueprint)
app.register_blueprint(ponente_blueprint)

cors = CORS(app)


@app.route('/', methods=['GET'])
def Index():
    response = requests.post("http://127.0.0.1:5000/api/evento/get_all").json()
    return render_template('home.html', eventos=response)


@app.route('/login', methods=['GET','POST'])
def Login():
    #if request.method == 'POST':
    return render_template('login.html')

@app.route('/registro', methods=['GET'])
def Registro():
    return render_template('registrar.html')

@app.route('/evento/<int:id>', methods=['GET'])
def Evento(id):
    query = {"id" : id}
    resp = requests.post("http://127.0.0.1:5000/api/evento/get", json=query).json()
    #evento = EventoModel(resp['id'], resp['ponente'], resp['id_lista'], resp['nombre'], resp['detalles'], resp['link'])
    return render_template('evento.html', evento=resp)

@app.route('/profile/<int:id>', methods=['GET'])
def Profile(id):
    query = {"id" : id}
    resp = requests.post("http://127.0.0.1:5000/api/ponente/get", json=query).json()
    return render_template('profile.html', ponente=resp)

if __name__ == "__main__":
    app.run(debug=True)