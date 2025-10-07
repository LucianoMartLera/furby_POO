from classes.furby import Furby
from classes.furby_madre import Furby_Madre
from classes.furby_baby import Furby_baby
from os import system

def toca_para_continuar():
    input("Presione alguna tecla para continuar...")
    return

def validar_numero(mensaje: str, min: int, max: int):
    while True:
        num = input(mensaje)
        if not num.isdigit():
            print("Ingrese un valor numérico.")
            continue

        if int(num) < min or int(num) > max:
            print(f"Ingrese un valor válido entre {min} y {max}")
            continue
        break
    return int(num)

def crear_furby() -> Furby:
    nombre = input("Ingrese el nombre de su furby: ")
    color = input("Ingrese el color de su furby: ")
    energia = validar_numero("Ingrese la energía del furby (entre 0 y 100 %): ", min = 0, max = 100)
    pelo = input("Ingrese el estílo de pelo de su furby (puede ser liso, rizado, largo o corto): ")
    ojos = input("Ingrese el color de los ojos del furby: ")
    pico = input("Ingrese el tipo de pico de su furby (puede ser normal o afilado): ")
    furby = Furby(nombre, color, energia, pelo, ojos, pico)
    return furby

def crear_furby_bebe() -> Furby_baby:
    nombre = input("Ingrese el nombre de su furby bebé: ")
    color = input("Ingrese el color de su furby bebé: ")
    energia = validar_numero("Ingrese la energía del furby bebé (entre 0 y 100 %): ", min = 0, max = 100)
    pelo = input("Ingrese el estílo de pelo de su furby bebé (puede ser liso, rizado, largo o corto): ")
    ojos = input("Ingrese el color de los ojos del furby bebé: ")
    pico = input("Ingrese el tipo de pico de su furby bebé (puede ser normal o afilado): ")
    angustia = validar_numero("¿El furby bebé está angustiado?\n 1. Sí\n 2. No\n Su opción: ", min = 1, max = 2)
    angustia_bool = True if angustia == 1 else False
    furby_baby = Furby_baby(nombre, color, energia, pelo, ojos, pico, angustia_bool)
    return furby_baby

def crear_furby_madre() -> Furby_Madre:
    nombre = input("Ingrese el nombre de su madre furby: ")
    color = input("Ingrese el color de su madre furby: ")
    energia = validar_numero("Ingrese la energía de la madre furby (entre 0 y 100 %): ", min = 0, max = 100)
    pelo = input("Ingrese el estílo de pelo de su madre furby (puede ser liso, rizado, largo o corto): ")
    ojos = input("Ingrese el color de los ojos de la madre furby: ")
    pico = input("Ingrese el tipo de pico de su madre furby (puede ser normal o afilado): ")
    luchona = validar_numero("¿La madre furby es luchona?\n 1. Sí\n 2. No\n Su opción: ", min = 1, max = 2)
    luchona_bool = True if luchona == 1 else False
    furby_madre = Furby_Madre(nombre, color, energia, pelo, ojos, pico, luchona_bool)
    return furby_madre

