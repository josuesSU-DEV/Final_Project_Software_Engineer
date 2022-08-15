from backend.models.connection_pool import MySQLPool

class EscuelaModel:
    def __init__(self):
        self.mysql_pool = MySQLPool()

    def get_escuela(self,idEscuela):
        params = {'idEscuela' : idEscuela}
        rv = self.mysql_pool.execute("SELECT * from escuela where idEscuela=%(idEscuela)s",params)
        data = []
        content = {}
        for result in rv:
            content = {'idEscuela': result[0], 'escuela':result[1], 'anio': result[2], 'numero_estudiantes': result[3]}
            data.append(content)
            content = {}
        return data

    def get_all_escuela(self):#Obtener todos los datos 
        rv = self.mysql_pool.execute("SELECT * from escuela")  
        data = []
        content = {}
        for result in rv:
            content = {'idEscuela': result[0], 'escuela': result[1], 'anio': result[2], 'numero_estudiantes': result[3]}
            data.append(content)
            content = {}
        return data

    def create_escuela(self, idEscuela, escuela, anio, numero_estudiantes):#Se envian los parametros a traves del formato JSON 
        params = {
            'idEscuela' : idEscuela,
            'escuela' : escuela,
            'anio' : anio,
            'numero_estudiantes' : numero_estudiantes
        }
        query = """insert into escuela (idEscuela, escuela,anio,numero_estudiantes)
            values (%(idEscuela)s,%(escuela)s,%(anio)s,%(numero_estudiantes)s)"""
        cursor = self.mysql_pool.execute(query, params, commit=True)

        data = {'idEscuela': cursor.lastrowid, 'escuela': escuela, 'anio': anio, 'numero_estudiantes': numero_estudiantes}
        return data

    def delete_escuela(self, idEscuela):#Se envia el IdEscuela con la que se identifica para eliminar no se necesita mas
        params = {'idEscuela': idEscuela}
        query = """delete from escuela where idEscuela = %(idEscuela)s"""    
        self.mysql_pool.execute(query, params, commit=True)  
        data = {'result': 1}
        return data

if __name__== "__main__":
    esm = EscuelaModel()
    #print(esm.get_task(1))
    #print(esm.get_tasks())
    #print(esm.delete_task(67))
    #print(esm.get_tasks())
    #print(esm.create_task('prueba 10', 'desde python'))
