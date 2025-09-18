class Robot:
    def __init__(self, nombre, color, energia):
        self._nombre = nombre
        self._color = color
        self._energia = energia

    def encender(self):
        return f"{self._nombre} se ha encendido, tiene {self._energia}% de energía."
