from classes.furby import Furby

def main() -> None:
    furby = Furby("Vegetta", "Violeta", 100, "Rizado", "Verdes", "Normal")
    print(furby.encender())
    print(furby)

if __name__ == "__main__":
    main()



