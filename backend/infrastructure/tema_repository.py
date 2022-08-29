from backend.infrastructure.connection_pool import MySQLPool

class TemaRepository:
    def __init__(self):
        self.mysql_pool = MySQLPool()

    def get(self, id):
        params = {'id': id}
        rv = self.mysql_pool.execute("SELECT * FROM tema WHERE tema.id = %(id)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {
                'id': result[0], 
                'nombre': result[1]
            }
            data.append(content)
            content = {}
        return data

    def get_all(self):
        rv = self.mysql_pool.execute("SELECT * FROM tema ORDER BY id")
        data = []
        content = {}
        for result in rv:
            content = {
                'id': result[0], 
                'nombre': result[1]
            }
            data.append(content)
            content = {}
        return data

    def create(self, id, id_ponente, nombre, detalles, link):
        params = {
            'id' : id,
            'nombre' : nombre,
        }
        query = "INSERT INTO tema(%(id)s, %(nombre)s)"
        self.mysql_pool.execute(query, params, commit=True)
        data = {'result : 1'}
        return data
        
    def delete(self, id):
        params = {'id' : id}      
        query = "DELETE FROM tema WHERE id = %(id)s"    
        self.mysql_pool.execute(query, params, commit=True)   
        data = {'result': 1}
        return data