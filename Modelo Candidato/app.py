from flask import Flask, session, redirect, g
from flask import request
from flask import jsonify
from flask import render_template,url_for
from flask_cors import CORS, cross_origin # para que no genere errores de CORS al hacer peticiones

from backend.blueprints.login_blueprint import login_blueprint
from backend.blueprints.usuarios_blueprint import usuarios_blueprint
from backend.blueprints.curso_del_estudiante_blueprint import curso_del_estudiante_blueprint
from backend.blueprints.escuela_blueprint import escuela_blueprint

from backend.models.login_model import LoginModel
from backend.models.usuarios_model import UsuariosModel
from backend.models.curso_del_estudiante_model import CursoDelEstudianteModel

app = Flask(__name__,template_folder='frontend2/templates',static_folder='frontend2/static')
app.secret_key= "hola"
app.register_blueprint(login_blueprint)
app.register_blueprint(usuarios_blueprint)
app.register_blueprint(curso_del_estudiante_blueprint)
app.register_blueprint(escuela_blueprint)

cors = CORS(app)

modelLogin = LoginModel()
modelUser = UsuariosModel()
modelCourse = CursoDelEstudianteModel()

class User:
    def __init__(self,id, cui, contrasenia, nombres, apellidos, escuela, correo, imagen, cursos):
        self.id = id
        self.cui = cui
        self.contrasenia = contrasenia
        self.nombres = nombres
        self.apellidos = apellidos
        self.escuela = escuela
        self.correo = correo
        self.imagen = imagen
        self.cursos = cursos
    def __repr__(self):
        return f'<User:  {self.cui}>'

users = []

list_log = modelLogin.get_all_usuario()
list_user = modelUser.get_all_usuarios()
list_course = modelCourse.get_all_curso_del_estudiante()


n = 1
for x, y, z in zip(list_log,list_user,list_course):
    users.append(User(id=n, cui=x.get('cui'), contrasenia=x.get('contrasenia'),nombres=y.get('nombres'),apellidos=y.get('apellidos'),escuela=y.get('escuela'),correo=y.get('correo'),imagen=y.get('imagen'),cursos=[z.get('curso1'),z.get('curso2'),z.get('curso3'),z.get('curso4'),z.get('curso5')]))
    n += 1


@app.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user

@app.route('/login', methods=['GET', 'POST'])
def Index():
    if request.method == 'POST':
        users.clear()
        modelLogin = LoginModel()
        modelUser = UsuariosModel()
        modelCourse = CursoDelEstudianteModel()

        list_log = modelLogin.get_all_usuario()
        list_user = modelUser.get_all_usuarios()
        list_course = modelCourse.get_all_curso_del_estudiante()

        n = 1
        for x, y, z in zip(list_log,list_user,list_course):
            users.append(User(id=n, cui=x.get('cui'), contrasenia=x.get('contrasenia'),nombres=y.get('nombres'),apellidos=y.get('apellidos'),escuela=y.get('escuela'),correo=y.get('correo'),imagen=y.get('imagen'),cursos=[z.get('curso1'),z.get('curso2'),z.get('curso3'),z.get('curso4'),z.get('curso5')]))
            n += 1
        session.pop('user_id', None)
        cui = request.form['cui']
        print(cui)
        contrasenia = request.form['contrasenia']
        user = [x for x in users if x.cui == cui][0]
        if user and user.contrasenia == contrasenia:
            session['user_id'] = user.id
            return redirect(url_for('Menu'))

        return redirect(url_for('Index'))
    return render_template('login.html')


@app.route('/usuarios')
def Menu():
    if not g.user:
        return redirect(url_for('Index'))
    return render_template("menu.html")

@app.route('/signup', methods=['GET','POST'])
def SignUp():
    if request.method == 'POST':
        cui = request.form['cui']
        contrasenia = request.form['contrasenia']
        nombres = request.form['nombres']
        apellidos = request.form['apellidos']
        correo = request.form['email']
        escuela = request.form['escuela']

        curso1 = ''
        curso2 = ''
        curso3 = ''
        curso4 = ''
        curso5 = ''

        if escuela == "Ciencia de la Computacion":
            curso1 = 'Arquitectura de Computadores'
            curso2 = 'Ciencia de la Computacion II'
            curso3 = 'Trabajo Interdisciplinar I'
            curso4 = 'Calculo en Varias Variab;es'
            curso5 = 'Desarrollo Basado en Plataformas'
        else:
            curso1 = 'Materiales'
            curso2 = 'Dibujo Arquitectonico'
            curso3 = 'Taller de diseno'
            curso4 = 'Teoria de la arquitectura'
            curso5 = 'Historia de la Arquitectura'

        modelUser.create_usuarios(cui,nombres,apellidos,"Ciencia de la Computacion",correo,"imagen01.png")
        modelLogin.create_usuario(cui,contrasenia)
        modelCourse.create_curso_del_estudiante(cui,curso1,curso2,curso3,curso4,curso5)

        return redirect(url_for('Index'))

    return render_template("singup.html")

@app.route('/register',methods=['GET'])
def Register():
    return render_template('asistencia.html')

if __name__ == "__main__":
    app.run(debug=True)
