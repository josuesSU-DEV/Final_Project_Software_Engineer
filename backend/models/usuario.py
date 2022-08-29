class Nombre:
    def __init__(self, nombre_, apellido_):
        self.nombre = nombre_
        self.apellido = apellido_

    def full(self):
        return "{} {}".format(self.nombre, self.apellido)

class UsuariosModel:
    def __init__(self, id_, nombre_, apellido_, correo_):
        self.id = id_
        self.nombre_completo = Nombre(nombre_, apellido_)
        self.correo = correo_
    
    def set_id(self, id_):
        self.id = id_
    def get_id(self):
        return self.id

    def set_nombre(self, nombre_, apellido_):
        self.nombre_completo = Nombre(nombre_,apellido_)
    def get_nombre(self):
        return self.nombre_completo.full()
    
    def set_correo(self, correo_):
        self.correo = correo_
    def get_correo(self):
        return self.correo

if __name__ == "__main__":    
    usm = UsuariosModel() 