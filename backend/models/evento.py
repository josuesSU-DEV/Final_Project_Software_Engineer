class EventoModel:
    def __init__(self, id_, id_ponente_, id_lista_, nombre_, detalles_, link_):
        self.id = id_
        self.id_ponente = id_ponente_
        self.id_lista = id_lista_
        self.nombre = nombre_
        self.detalles = detalles_
        self.link = link_

    def set_id(self, id_):
        self.id = id_
    def get_id(self):
        return self.id

    def set_id_ponente(self, id_ponente_):
        self.id_ponente = id_ponente_
    def get_id_ponente(self):
        return self.id_ponente

    def set_id_lista(self, id_lista_):
        self.id_lista = id_lista_
    def get_id_lista(self):
        return self.id_lista

    def set_nombre(self, nombre_):
        self.nombre = nombre_
    def get_nombre(self):
        return self.nombre

    def set_detalles(self, detalles_):
        self.detalles = detalles_
    def get_detalles(self):
        return self.detalles

    def set_link(self, link_):
        self.link = link_
    def get_link(self):
        return self.link