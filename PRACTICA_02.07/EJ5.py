def lista_cuadrados(numeros):
    """Función que toma una lista de números y devuelve una lista con sus cuadrados
    Parámetros:

        - numeros: Es la lista de números que introduce el usuario.
    Salida:
        Una lista con los cuadrados de los números introducidos por el usuario.
    """
    lista = []
    for i in numeros:
        lista.append(i**2)
    return lista


