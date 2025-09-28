def mapear_nombre(nombre: str) -> str:
    # Esta función va a mapear el nombre de algo, o sea transformar la primera letra a mayúscula y dejando las demás en minúsculas para que al mostrarse el nombre en pantalla se vea bien.
    nombre_mapeado: str = nombre[0].upper()

    for i in range(len(nombre) - 1):
        nombre_mapeado += nombre[i + 1].lower()

    return nombre_mapeado
