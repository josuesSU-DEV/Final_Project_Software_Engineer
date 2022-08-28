from backend.models.connection_pool import MySQLPool

class CursoDelEstudianteModel:
    def __init__(self):        
        self.mysql_pool = MySQLPool()

    def get_curso_del_estudiante(self, cui):    
        params = {'cui' : cui}      
        rv = self.mysql_pool.execute("SELECT * from `curso del estudiante` where cui=%(cui)s", params)
        data = []
        content = {}
        for result in rv:
            content = {'cui': result[0], 'curso1': result[1], 'curso2': result[2], 'curso3': result[3], 'curso4': result[4], 'curso5': result[5]}
            data.append(content)
            content = {}
        return data

    def get_all_curso_del_estudiante(self):  
        rv = self.mysql_pool.execute("SELECT * from `curso del estudiante` order by cui")  
        data = []
        content = {}
        for result in rv:
            content = {'cui': result[0], 'curso1': result[1], 'curso2': result[2], 'curso3': result[3], 'curso4': result[4], 'curso5': result[5]}
            data.append(content)
            content = {}
        return data

    def create_curso_del_estudiante(self, cui, curso1, curso2, curso3, curso4, curso5):    
        params = {
            'cui' : cui,
            'curso1' : curso1,
            'curso2' : curso2,
            'curso3' : curso3,
            'curso4' : curso4,
            'curso5' : curso5,
        }  
        query = """insert into `curso del estudiante` (cui, curso1, curso2, curso3, curso4, curso5) 
            values (%(cui)s, %(curso1)s, %(curso2)s, %(curso3)s, %(curso4)s, %(curso5)s)"""    
        cursor = self.mysql_pool.execute(query, params, commit=True)   

        data = {'cui': cui, 'curso1': curso1, 'curso2': curso2, 'curso3': curso3, 'curso4': curso4, 'curso5': curso5}
        return data

    def delete_curso_del_estudiante(self, cui):    
        params = {'cui' : cui}      
        query = """delete from `curso del estudiante` where cui = %(cui)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data

if __name__ == "__main__":    
    tm = CursoDelEstudianteModel()     
