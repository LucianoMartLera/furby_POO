import Robot from robot

class Furby(Robot):
    def __init__(self, pelo, color_ojos, pico):
        super().__init__(nombre, color, energia)

        self._pelo = pelo
        self._color_ojos = color_ojos
        self._pico = pico

    def modo_satanico(self):
        message = f"{self._nombre} activó su modo satánico, sus ojos pasaron de {self._color_ojos} a rojos"
        self._color_ojos = "rojo"
        return message

