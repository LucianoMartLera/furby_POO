class Bateria:
    def __init__(self, carga: int, duracion: int, voltaje: float):
        self._carga = carga
        self._duracion = duracion
        self._voltaje = voltaje 
    
    def __str__(self) -> str:
        return f"""
        Descripción de la batería:
            • Carga actual: {self._carga}
            • Duración aproximada: {self._duracion}
            • Voltaje: {self._voltaje}
        """

    def cargar(self) -> str:
        return "La bateria se cargó al %100"

    def descarga(self) -> str:
        return "La batería se descargó"

    def mostrar_porcentaje(self) -> str:
        return f"El porcentaje de batería es de {self._carga}%"
