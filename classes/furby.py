from .robot import Robot 
from .bateria import Bateria
from .grabadora import Grabadora
from .sensor import Sensor

class Furby(Robot):
    def __init__(self, nombre: str, color: str, energia: int, pelo: str, color_ojos: str, pico: str) -> None:
        super().__init__(nombre, color, energia)

        self._pelo = pelo.lower()
        self._color_ojos = color_ojos.lower()
        self._pico = pico.lower()
        self._bateria = Bateria(energia, 12, 1.5)
        self._grabadora = Grabadora(120, 30)
        self._sensor = Sensor(10, "Alta", "Alta")

    def modo_satanico(self) -> str:
        message = f"{self._nombre} activó su modo satánico, sus ojos pasaron de {self._color_ojos} a rojos"
        self._color_ojos = "rojo"
        return message

    def info_bateria(self) -> str:
        return self._bateria.__str__()

    def __str__(self) -> str:
        return f"Mi furby se llama {self._nombre}, es de color {self._color}, tiene un pelo {self._pelo}, unos ojos color {self._color_ojos}, su pico es {self._pico} y {self._bateria.mostrar_porcentaje()}."
