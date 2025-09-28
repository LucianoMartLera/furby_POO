class Sensor:
    def __init__(self, alcance: int, sensibilidad: str, presicion: str):
        self._alcance = alcance
        self._sensibilidad = sensibilidad
        self._presicion = presicion

    def escaneo(self):
        return f"El sensor escanea {self._alcance}mt de frente"
        
