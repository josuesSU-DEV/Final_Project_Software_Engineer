# from crypt import methods
import requests

from flask import Flask, session, redirect, g
from flask import request
from flask import jsonify
from flask import render_template,url_for
from flask_cors import CORS, cross_origin # para que no genere errores de CORS al hacer peticiones

from backend.blueprints.evento_blueprint import evento_blueprint
from backend.blueprints.asistente_blueprint import asistente_blueprint

from backend.models.evento import EventoModel

app = Flask(__name__,template_folder='frontend/templates',static_folder='frontend/static')

app.secret_key= "averysecretkey"


app.register_blueprint(evento_blueprint)
app.register_blueprint(asistente_blueprint)


cors = CORS(app)


@app.route('/', methods=['GET'])
def Index():
    response = requests.post("http://127.0.0.1:5000/api/evento/get_all").json() # Testing API
    eventos = []
    for result in response:
        evento = EventoModel(response[0]['id'], response[0]['id_ponente'], response[0]['id_lista'], response[0]['nombre'], response[0]['detalles'], response[0]['link'])
        eventos.append(evento)
    # evento = EventoModel(response[0].get_id(), response[0].get_id_ponente(), response[0].get_nombre(), response[0].get_detalles(), response[0].get_link())
    print(eventos[0].get_nombre())
    # print(response[0].get_detalles())
    # print(response[0]['detalles'])
    return render_template('evento.html')

# @app.route('/evento', methods=['GET'])
# def evento():
#     response = request.post("").json()

@app.route('/login', methods=['GET','POST'])
def Login():
    #if request.method == 'POST':

    return render_template('login.html')

@app.route('/evento', methods=['GET'])
def Evento():
    
    return render_template('evento.html')

@app.route('/profile', methods=['GET'])
def Profile():
    return render_template('profile.html')

if __name__ == "__main__":
    app.run(debug=True)