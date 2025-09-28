from classes.furby import Furby

def main() -> None:
    furby = Furby("Vegetta", "Violeta", 100, "Rizado", "Verdes", "Normal")
    print(furby.encender())
    print(furby)
    print(furby.info_bateria())
    print(furby.modo_satanico())

if __name__ == "__main__":
    main()



