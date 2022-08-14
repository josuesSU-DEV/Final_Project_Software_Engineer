#!/usr/bin/python
#-*- coding: utf-8 -*-

from Ponente import Ponente
from Asistente import Asistente

class Usuario(Ponente, Asistente):
    def __init__(self):
        self.id = None
        self.nombre = None
        self.correo = None

