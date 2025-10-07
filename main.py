from funciones import crear_furby, crear_furby_bebe, crear_furby_madre, validar_numero, toca_para_continuar
from os import system
from mensajes import mensaje_de_bienvenida, opciones_de_furbys, opciones_de_furby_bebe, opciones_de_furby_madre

def main() -> None:
    # Toda esta parte fue para probar el código
    # furby = Furby("Vegetta", "Violeta", 100, "Rizado", "Verdes", "Normal")
    # print(furby.encender())
    # print(furby)
    # print(furby.info_bateria())
    # print(furby.modo_satanico())
    system("clear")
    print(mensaje_de_bienvenida)
    opcion = validar_numero("Ingrese una opción: ", min = 1,max = 4)
    while True:

        if opcion == 1:
            system("clear")
            furby = crear_furby()
            print("El furby se creó con éxito. Ahora, ¿Qué quiere hacer con su nuevo furby?")
            while True:
                system("clear")
                print(opciones_de_furbys)
                opcion_furby = validar_numero("Su opción: ", min = 1, max = 6)
                if opcion_furby == 1:
                    print(furby.encender())
                    toca_para_continuar()
                    continue
                elif opcion_furby == 2:
                    print(furby)
                    toca_para_continuar()
                    continue
                elif opcion_furby == 3:
                    print(furby.info_bateria())
                    toca_para_continuar()
                    continue
                elif opcion_furby == 4:
                    print(furby.modo_satanico())
                    toca_para_continuar()
                    continue
                elif opcion_furby == 5:
                    print(furby.apagar())
                    toca_para_continuar()
                    continue
                elif opcion_furby == 6:
                    print("Gracias por usar el creador de furbys. ¡Hasta luego!")
                    toca_para_continuar()
                    break
            return
        elif opcion == 2:
            system("clear")
            furby_bebe = crear_furby_bebe()
            while True:
                print("El furby bebé se creó con éxito. Ahora, ¿Qué quiere hacer con su nuevo furby?")
                print(opciones_de_furby_bebe)
                opcion_furby = validar_numero("Su opción: ", min = 1, max = 7)
                if opcion_furby == 1:
                    print(furby_bebe.encender())
                    toca_para_continuar()
                    continue
                elif opcion_furby == 2:
                    print(furby_bebe)
                    toca_para_continuar()
                    continue
                elif opcion_furby == 3:
                    print(furby_bebe.info_bateria())
                    toca_para_continuar()
                    continue
                elif opcion_furby == 4:
                    print(furby_bebe.modo_satanico())
                    toca_para_continuar()
                    continue
                elif opcion_furby == 5:
                    print(furby_bebe.angustiarse())
                    toca_para_continuar()
                    continue
                elif opcion_furby == 6:
                    print(furby_bebe.apagar())
                    toca_para_continuar()
                    continue
                elif opcion_furby == 7:
                    print("Gracias por usar el creador de furbys. ¡Hasta luego!")
                    toca_para_continuar()
                    break
            return
        elif opcion == 3:
            system("clear")
            madre_furby = crear_furby_madre()
            while True:
                opcion_madre_furby = validar_numero("Su opción: ", min = 1, max = 7)
                print("La madre furby se creó con éxito. Ahora, ¿Qué quiere hacer con su nuevo furby?")
                print(opciones_de_furby_madre)
                if opcion_madre_furby == 1:
                    print(madre_furby.encender())
                    toca_para_continuar()
                elif opcion_madre_furby == 2:
                    print(madre_furby)
                    toca_para_continuar()
                elif opcion_madre_furby == 3:
                    print(madre_furby.info_bateria())
                    toca_para_continuar()
                elif opcion_madre_furby == 4:
                    print(madre_furby.modo_satanico())
                    toca_para_continuar()
                elif opcion_madre_furby == 5:
                    print(madre_furby.fatigarse())
                    toca_para_continuar()
                elif opcion_madre_furby == 6:
                    print(madre_furby.apagar())
                    toca_para_continuar()
                    continue
                elif opcion_madre_furby == 7:
                    print("Gracias por usar el creador de furbys. ¡Hasta luego!")
                    toca_para_continuar()
                    break
            return
        elif opcion == 4:
            break
        return




if __name__ == "__main__":
    main()



