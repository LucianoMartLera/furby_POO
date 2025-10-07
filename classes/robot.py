from .functions import mapear_nombre

class Robot:
    _encendido: bool = False
    def __init__(self, nombre: str, color: str, energia: int):
        self._nombre = mapear_nombre(nombre)
        self._color = color.lower()
        self._energia = energia

    def encender(self):
        self._encendido = True
        return f"{self._nombre} se ha encendido, tiene {self._energia}% de energía."

    def apagar(self):
        self._encendido = False
        return f"{self._nombre} se ha apagado."
