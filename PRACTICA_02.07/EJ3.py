def area_circulo(radio):
    """Función que calcula el área de un círculo en función del radio
    Parámetros:

        - radio: La longitud del radio introducido por el usuario.
    Salida:
        El área del círculo.
    """
    area = 3.1415 * radio**2
    return area

def volumen_cilindro(radio, altura):
    """Función que calcula el area de un cilindro utilizando la función dek area del círculo
    Parámetros:

        - radio: La longitud del radio introducido por el usuario.
        - altura: La altura del cilindro introducido por el usuario.
    Salida:
        El área del cilindro:
    """
    cilindro = area_circulo(radio) * altura
    return cilindro




