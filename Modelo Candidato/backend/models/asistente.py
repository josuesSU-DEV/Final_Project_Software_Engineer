from backend.models.connection_pool import MySQLPool
class AsistenteModel:
    def __init__(self):
        self.mysql_pool = MySQLPool()

    def get_asistente(self, id):
        params = {'id': id}
        rv = self.mysql_pool.execute("SELECT * from usuario INNER JOIN asistente ON where asistente.id%(id)s=usuario.id%(id)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id': result[0], 'nombre': result[1], 'apellido': result[2], 'correo': result[3]}
            data.append(content)
            content = {}
        return data
    def get_all_asistentes(self):
        rv = self.mysql_pool.execute("select * from usuario")
        data = []
        content = {}
        

    def create_asistente(self, id, nombre, apellido, correo):

    def delete_asistente(self, id)