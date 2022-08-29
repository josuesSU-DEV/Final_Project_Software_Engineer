from backend.infrastructure.connection_pool import MySQLPool

class PonenteRepository:
    def __init__(self):
        self.mysql_pool = MySQLPool()

    def get(self, id):
        params = {'id':id}
        rv = self.mysql_pool.execute("SELECT * FROM usuario u INNER JOIN ponente p on p.idPonente = u.idUsuario WHERE u.idUsuario = %(id)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {
                'id': result[0], 
                'nombre': result[1], 
                'apellido': result[2], 
                'correo': result[3], 
                'numEventos': result[5], 
                'descripcion': result[6]
            }
            data.append(content)
            content = {}
        return data[0]

    def get_all(self):
        rv = self.mysql_pool.execute("SELECT * FROM usuario u INNER JOIN ponente p on p.idPonente = u.idUsuario ORDER BY idUsuario")
        data = []
        content = {}
        for result in rv:
            content = {
                'id': result[0], 
                'nombre': result[1], 
                'apellido': result[2], 
                'correo': result[3], 
                'numEventos': result[5], 
                'descripcion': result[6]
            }
            data.append(content)
            content = {}
        return data

    def create(self, id, nombre, apellido, correo, numEventos, descripcion):
        params = {
            'id' : id,
            'nombre' : nombre,
            'apellido' : apellido,
            'correo' : correo,
            'numEventos' : numEventos,
            'descripcion' : descripcion
        }
        query = "insertarPonente(%(id)s, %(nombre)s, %(apellido)s, %(correo)s, %(numEventos)s, %(descripcion)s)"
        self.mysql_pool.execute(query, params, commit=True)
        data = {'result : 1'}
        return data

        
    def delete(self, id):
        params = {'id' : id}      
        query = "DELETE FROM ponente WHERE id = %(id)s\nDELETE FROM usuario WHERE id = %(id)s"    
        self.mysql_pool.execute(query, params, commit=True)   
        data = {'result': 1}
        return data
