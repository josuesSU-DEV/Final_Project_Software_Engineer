from flask.templating import render_template
from backend.models.connection_pool import MySQLPool

class LoginModel:
    def __init__(self): 
        self.mysql_pool = MySQLPool()

    def get_usuario(self, cui): #retorna el usuario dependiendo del CUI que se pasa a traves de json    
        params = {'cui' : cui}      
        rv = self.mysql_pool.execute("SELECT * from login where cui=%(cui)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'cui': result[0], 'contrasenia': result[1]}
            data.append(content)
            content = {}
        return data

    def get_all_usuario(self): #retorna todos los usuarios que existen en la tabla "login"
        rv = self.mysql_pool.execute("SELECT * from login order by cui")  
        data = []
        content = {}
        for result in rv:
            content = {'cui': result[0], 'contrasenia': result[1]}
            data.append(content)
            content = {}
        return data

    def create_usuario(self, cui, contrasenia): #crear usuario a traves de json    
        params = {
            'cui' : cui,
            'contrasenia' : contrasenia
        }  
        query = """insert into login(cui, contrasenia) 
            values (%(cui)s, %(contrasenia)s)"""    
        cursor = self.mysql_pool.execute(query, params, commit=True)   

        data = {'cui': cui, 'contrasenia': contrasenia}
        return data

    def delete_usuario(self, cui):#borra usuario de la base de datos  
        params = {'cui' : cui}      
        query = """delete from login where cui = %(cui)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data

if __name__ == "__main__":    
    um = LoginModel()     

    #print(tm.get_task(1))
    #print(tm.get_tasks())
    #print(um.delete_usuario(67))
    #print(um.get_tasks())
    #print(tm.create_task('prueba 10', 'desde python'))