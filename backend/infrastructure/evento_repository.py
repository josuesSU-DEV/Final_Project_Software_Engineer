from backend.infrastructure.connection_pool import MySQLPool
from backend.infrastructure.ponente_repository import PonenteRepository

repo_ponente = PonenteRepository()
# Clase Repositorio para la lectura y manipulacion en la BD
class EventoRepository:
    # Estableciendo conexion con la BD a traves de un atributo de pool
    def __init__(self):
        self.mysql_pool = MySQLPool()

    # Obtener un evento por id
    def get(self, id):
        params = {'id': id}
        rv = self.mysql_pool.execute("select * from evento where evento.idEvento = %(id)s", params)

        # Obteniendo informacion del ponente
        ponente = repo_ponente.get(rv[0][1])
        
        data = []
        content = {}
        for result in rv:
            content = {'id': result[0], 'ponente': ponente[0], 'idLista' : result[2], 'nombre': result[3], 'detalles': result[4], 'link': result[5]}
            data.append(content)
            content = {}
        return data

    # Obtener todos los eventos
    def get_all(self):
        rv = self.mysql_pool.execute("select * from Evento order by idEvento")
        data = []
        content = {}
        for result in rv:

            ponente = repo_ponente.get(result[1])
            content = {'id': result[0], 'ponente': ponente[0], 'idLista': result[2], 'nombre': result[3], 'detalles': result[4], 'link': result[5]}
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
