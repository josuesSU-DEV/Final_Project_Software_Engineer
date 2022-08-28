from backend.models.usuario import UsuariosModel

class PonenteModel(UsuariosModel):
    def __init__(self, id, nombre, apellido, correo):
        UsuariosModel.__init__(self, id, nombre, apellido, correo)