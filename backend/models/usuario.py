class UsuarioModel:
    def __init__(self, id_, nombre, apellido, correo_):
        self.id = id_
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo_
    def full(self):
        return "{} {} {} {}".format(self.id, self.nombre, self.apellido, self.correo)
    
    def set_id(self, id_):
        self.id = id_
    def get_id(self):
        return self.id

    def set_nombre(self, nombre_):
        self.nombre = nombre_
    def get_nombre(self):
        return self.nombre
    
    def set_apellido(self, apellido_):
        self.apellido = apellido_
    def get_apellido(self):
        return self.apellido
    
    def set_correo(self, correo_):
        self.correo = correo_
    def get_correo(self):
        return self.correo
        
# class UsuarioModel:
#     def __init__(self, id, nombre, apellido, correo):
#         self.id = id
#         self.nombre_completo = Nombre(nombre,apellido)
#         self.correo = correo


# if __name__ == "__main__":    
#     usm = UsuarioModel()     



