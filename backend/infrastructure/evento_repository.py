from backend.infrastructure.connection_pool import MySQLPool

# from backend.models.evento import EventoModel

# Clase Repositorio para la lectura y manipulacion en la BD
class EventoRepository:
    
    # Estableciendo conexion con la BD a traves de un atributo de pool
    def __init__(self):
        self.mysql_pool = MySQLPool()

    # Obtener un evento por id
    def get(self, id):
        params = {'id': id}
        rv = self.mysql_pool.execute("SELECT * FROM evento WHERE evento.idEvento = %(id)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id': result[0], 'id_ponente': result[1], 'nombre': result[2], 'detalles': result[3], 'link': result[4]}
            data.append(content)
            content = {}
        return data

    # Obtener todos los eventos
    def get_all(self):
        rv = self.mysql_pool.execute("SELECT * FROM Evento ORDER BY idEvento")
        data = []
        content = {}
        for result in rv:
            content = {'id': result[0], 'id_ponente': result[1], 'id_lista': result[2], 'nombre': result[3], 'detalles': result[4], 'link': result[5]}
            data.append(content)
            content = {}
        return data

    # Crear evento con todos sus parametros
    def create(self, id, id_ponente, nombre, detalles, link):
        params = {
            'id' : id,
            'id_ponente' : id_ponente,
            'nombre' : nombre,
            'detalles' : detalles,
            'link' : link
        }
        query = "insert into evento(%(id)s, %(id_ponente)s, %(nombre)s, %(detalles)s, %(link)s)"
        self.mysql_pool.execute(query, params, commit=True)
        data = {'result : 1'}
        return data
        
    # Borrar un evento por id
    def delete(self, id):
        params = {'id' : id}      
        query = "delete from evento where id = %(id)s"    
        self.mysql_pool.execute(query, params, commit=True)   
        data = {'result': 1}
        return data
