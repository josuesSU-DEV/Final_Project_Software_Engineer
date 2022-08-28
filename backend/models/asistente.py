from backend.models.usuario import UsuarioModel

class AsistenteModel(UsuarioModel):
    def __init__(self, id_, nombre_, apellido_, correo_):
        UsuarioModel.__init__(self, id_, nombre_, apellido_, correo_)