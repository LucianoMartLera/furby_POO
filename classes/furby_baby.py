from .furby import Furby

class Furby_baby(Furby):
    def __init__(self, nombre: str, color: str, energia: int, pelo: str, color_ojos: str, pico: str, angustia: bool):
        super().__init__(nombre, color, energia, pelo, color_ojos, pico)
        self._angustia = angustia

    def get_angustia(self):
        return self._angustia

    def set_angustia(self, esta_angustiado: bool):
        self._angustia = esta_angustiado

    def angustiarse(self):
        return f"{self._nombre} comienza a llorar para llamar la atencion de su madre" if self._angustia else "El bebé furby no está angustiado. ¿Quieres angustiarlo?\n 1. sí\n 2. no"
