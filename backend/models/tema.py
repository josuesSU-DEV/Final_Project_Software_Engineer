class Tema:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
    
    def set_id(self, id_):
        self.id = id_
    def get_id(self):
        return self.id

    def set_nombre(self, nombre_):
        self.nombre = nombre_
    def get_nombre(self):
        return self.nombre