from furby import Furby

class furby_baby(Furby):
    def __init__(self, nombre, color, energia, pelo, color_ojos, pico,angustia):
        super().__init__(angustia)
        self.angustia=angustia
    def angustiarse(self):
        return f"comienza a llorar para llamar la atencion de su madre"