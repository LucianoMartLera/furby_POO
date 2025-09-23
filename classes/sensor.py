class Sensor:
    def __init__(self,alcanze,sensibilidad,presicion):
        self._alcanze=alcanze
        self._sensibilidad=sensibilidad
        self._presicion=presicion

    def escaneo(self):
        return f"el sensor escanea {self._alcanze}mt de frente"
        