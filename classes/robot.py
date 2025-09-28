from .functions import mapear_nombre

class Robot:
    def __init__(self, nombre: str, color: str, energia: int):
        self._nombre = mapear_nombre(nombre)
        self._color = color.lower()
        self._energia = energia

    def encender(self):
        return f"{self._nombre} se ha encendido, tiene {self._energia}% de energía."
