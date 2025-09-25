class Bateria:
    def __init__(self,duracion,voltaje):
        self._duracion = duracion
        self._voltaje = voltaje 
    
    def cargar(self):
        return "La bateria se cargo al %100"
    def descarga(self):
        return "Cargue el Furby"