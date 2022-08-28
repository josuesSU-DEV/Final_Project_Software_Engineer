from backend.models.usuario import UsuarioModel

class PonenteModel(UsuarioModel):
    def __init__(self, id, nombre, apellido, correo):
        UsuarioModel.__init__(self, id, nombre, apellido, correo)