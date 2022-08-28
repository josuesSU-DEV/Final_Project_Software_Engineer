class Nombre:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def full(self):
        return "{} {}".format(self.nombre, self.apellido)
        
class UsuarioModel:
    def __init__(self, id, nombre, apellido, correo):
        self.id = id
        self.nombre_completo = Nombre(nombre,apellido)
        self.correo = correo


if __name__ == "__main__":    
    usm = UsuarioModel()     



