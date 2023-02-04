def decimal_binario(decimal):
    """Función que convierte un número decimal introducido por el usuario en binario
    Parámetros:

        - decimal: Es un número en formato decimal introducido por el usuario.
    Salida:
        Un número binario correspondiente al decimal introducido por el usuario.
    """
    binario = []
    while decimal > 0:
        binario.append(str(decimal % 2))
        decimal //= 2
    binario.reverse()
    return binario

def binario_decimal(numero):
    """Función que convierte un número binario introducido por el usuario en decimal
    Parámetros:

        - binario: Es un número en formato binario introducido por el usuario.
    Salida:
        Un número decimal correspondiente al binario introducido por el usuario.
    """
    numero = list(numero)
    numero.reverse()
    decimal = 0
    for i in range(len(numero)):
        decimal += int(numero[i]) * 2 ** i
    return decimal
