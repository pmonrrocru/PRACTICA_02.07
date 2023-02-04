def freq_palabras(cadena):
    """Función que muestra las palabras de una cadena con su frecuencia
    Parámetros:

        - cadena: Es un fragmento de texto introducido por el usuario.
    Salida:
        Un diccionario con las palabras del texto y su frecuencia.
    """
    cadena = cadena.split()
    palabras = {}
    for i in cadena:
        if i in palabras:
            palabras[i] += 1
        else:
            palabras[i] = 1
    return palabras
texto = input("Introduce el texto que quieras: ")
print(freq_palabras(texto))

