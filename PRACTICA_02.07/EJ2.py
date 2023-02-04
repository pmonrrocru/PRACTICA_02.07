def factorial_iterativo(n):
   """Función que calcula el factorial de un número entero introducido por el usuario utilizando bucles

   Parámetros:

       - n: Un número entero introducido por el usuario
   Salida:
       El factorial del número introducido
   """
   if n == 0 or n == 1:
        resultado = 1
        return resultado
   else:
        resultado = n * factorial_iterativo(n-1)
        return resultado

def factorial_recursivo(n):
    """Función que calcula el factorial de un número entero introducido por el usuario de forma recursiva:

        - n: Un número entero introducido por el usuario.
    Salida:
        El factorial del número introducido
    """
    if n == 0:
        resultado = 1
        return resultado
    else:
        return n * factorial_recursivo(n-1)







