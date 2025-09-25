class Bateria:
    def __init__(self, carga, duracion, voltaje):
        self._carga = carga
        self._duracion = duracion
        self._voltaje = voltaje 
    
    def cargar(self):
        return "La bateria se cargó al %100"

    def descarga(self):
        return "La batería se descargó"

    def mostrar_porcentaje(self):
        return f"El porcentaje de batería es de {self._carga}%"
