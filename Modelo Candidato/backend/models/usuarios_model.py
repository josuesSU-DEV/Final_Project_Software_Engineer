from backend.models.connection_pool import MySQLPool

class UsuariosModel:
    def __init__(self): 
        self.mysql_pool = MySQLPool()

    def get_usuarios(self, cui):    
        params = {'cui' : cui}      
        rv = self.mysql_pool.execute("SELECT * from usuarios where cui=%(cui)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'cui': result[0], 'nombres': result[1], 'apellidos': result[2], 'escuela': result[3], 'correo': result[4], 'imagen': result[5]}
            data.append(content)
            content = {}
        return data

    def get_all_usuarios(self):  
        rv = self.mysql_pool.execute("SELECT * from usuarios order by cui")  
        data = []
        content = {}
        for result in rv:
            content = {'cui': result[0], 'nombres': result[1], 'apellidos': result[2], 'escuela': result[3], 'correo': result[4], 'imagen': result[5]}
            data.append(content)
            content = {}
        return data

    def create_usuarios(self,cui,nombres,apellidos,escuela,correo,imagen):    
        params = {
            'cui' : cui,
            'nombres' : nombres,
            'apellidos' : apellidos,
            'escuela' : escuela,
            'correo' : correo,
            'imagen' : imagen
        }  
        query = """insert into usuarios (cui,nombres,apellidos,escuela,correo,imagen) 
            values (%(cui)s, %(nombres)s, %(apellidos)s, %(escuela)s, %(correo)s, %(imagen)s)"""    
        cursor = self.mysql_pool.execute(query, params, commit=True)   

        data = {'cui' : cui, 'nombres' : nombres,'apellidos' : apellidos,'escuela' : escuela,'correo' : correo,'imagen' : imagen}
        return data

    def delete_usuarios(self, cui):    
        params = {'cui' : cui}      
        query = """delete from usuarios where cui = %(cui)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data

if __name__ == "__main__":    
    usm = UsuariosModel()     

    #print(tm.get_task(1))
    #print(tm.get_tasks())
    #print(tm.delete_task(67))
    #print(tm.get_tasks())
    #print(tm.create_task('prueba 10', 'desde python'))