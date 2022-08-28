from backend.infrastructure.connection_pool import MySQLPool

# Clase Repositorio para la lectura y manipulacion en la BD
class AsistenteRepository:
    # Estableciendo la conexion con la BD en MYSQL
    def __init__(self):
        self.mysql_pool = MySQLPool()

    # Obtener un asistente por id
    def get(self, id):
        params = {'id':id}
        rv = self.mysql_pool.execute("select * from usuario where idUsuario = %(id)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id': result[0], 'nombre': result[1], 'apellido': result[2], 'correo': result[3]}
            data.append(content)
            content = {}
        return data

    # Obtener todos los asistentes
    def get_all(self):
        rv = self.mysql_pool.execute("select * from usuario u inner join asistente a on u.idUsuario = a.idAsistente order by idUsuario")
        data = []
        content = {}
        for result in rv:
            content = {'id': result[0], 'nombre': result[1], 'apellido': result[2], 'correo': result[3]}
            data.append(content)
            content = {}
        return data

    # Crear por todos los parametros
    def create(self, id, nombre, apellido, correo):
        params = {
            'id' : id,
            'nombre' : nombre,
            'apellido' : apellido,
            'correo' : correo,
        }
        # Necesario insertar primero en la tabla usuario
        # ya que tiene una llave foranea asociada
        query = "insertarAsistente(%(id)s, %(nombre)s, %(apellido)s, %(correo)s)"
        self.mysql_pool.execute(query, params, commit=True)
        data = {'result : 1'}
        return data

    # Borrar por id
    def delete(self, id):
        params = {'id' : id}
        # Necesario borrar primero de la tabla asistente
        # ya que tiene una llave foranea asociada
        query = "delete from asistente where id = %(id)s\ndelete from usuario where id = %(id)s"    
        self.mysql_pool.execute(query, params, commit=True)   
        data = {'result': 1}
        return data

