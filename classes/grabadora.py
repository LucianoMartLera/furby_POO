class Grabadora:
    def __init__(self, almacenamiento: float | int, resolucion: int):
        self._almacenamiento = almacenamiento
        self._resolucion = resolucion
    
    def grabar(self):
        return "La grabadora empieza a grabar y lo guarda en almacenamiento"
    
    def detener(self):
        return "Se detiene la grabacion"

    def __str__(self):
        return f"La grabadora tiene {self._almacenamiento}gb de almacenamiento y una resolución de {self._resolucion} megapixeles"
