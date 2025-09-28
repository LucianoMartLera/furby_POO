from furby import Furby

class Furby_Madre(Furby):
    def __init__(self, nombre: str, color: str, energia: int, pelo: str, color_ojos: str, pico: str, luchona: bool) -> None:
        super().__init__(nombre, color, energia, pelo, color_ojos, pico)

        self._luchona = luchona

    def fatigarse(self):
        return f"La mamá furby {self._nombre} se cansó" if not self._luchona else f"La mamá furby {self._nombre} se cansó de tanto cuidar al furby bebé"


# Esta parte es para probar el código
if __name__ == "__main__":
    madre = Furby_Madre("Martha", "naranja", 100, "rizado", "verdes", "normal", False)

    print(madre.fatigarse())
