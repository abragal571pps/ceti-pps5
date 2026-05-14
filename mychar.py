#!/usr/bin/env python3
"""
Python 3.11.9
---------------------
mychar.py

Este programa obtiene la cadena de texto más larga a partir de una
lista de palabras introducidas por el usuario.

Si varias palabras tienen la misma longitud máxima, se devuelve la
primera según el orden alfabético (A–Z).

El código está estructurado en los siguientes bloques:
- Entrada de datos.
- Lógica de procesamiento.
- Control de flujo y gestión de errores.
"""


def cadena_mas_larga(cadenas):
    """
    Recibe una lista de cadenas y devuelve la más larga.

    Reglas:
    - La entrada debe ser una lista.
    - Todos los elementos deben ser cadenas de texto.
    - Si la lista está vacía, devuelve "".
    - En caso de empate, devuelve la primera alfabéticamente.
    """

    # La entrada debe ser una lista
    if not isinstance(cadenas, list):
        raise TypeError("La entrada debe ser una lista.")

    # Lista vacía
    if len(cadenas) == 0:
        return ""

    # Todos los elementos deben ser cadenas
    for elemento in cadenas:
        if not isinstance(elemento, str):
            raise TypeError("Todos los elementos deben ser cadenas de texto.")

    # Cálculo de la longitud máxima
    longitud_maxima = max(len(cadena) for cadena in cadenas)

    # Selección de las cadenas con longitud máxima
    cadenas_maximas = [
        cadena for cadena in cadenas if len(cadena) == longitud_maxima
    ]

    # Resolución del empate por orden alfabético
    return sorted(cadenas_maximas)[0]


def pedir_palabras(cantidad):
    """
    Solicita al usuario un número determinado de palabras y las
    devuelve en forma de lista.
    """

    palabras = []

    for i in range(cantidad):
        palabra = input("Introduce la palabra " + str(i + 1) + ": ")
        palabras.append(palabra.strip())

    return palabras


def ejecutar_programa():
    """
    Coordina la ejecución del programa sin gestionar excepciones,
    delegando esta responsabilidad en la función principal.
    """

    palabras = pedir_palabras(10)
    return cadena_mas_larga(palabras)


def main():
    """
    Punto de entrada del programa.

    Se encarga exclusivamente de la gestión de errores y de la
    interacción final con el usuario.
    """

    try:
        resultado = ejecutar_programa()

        print("\nResultado:")
        print("La cadena más larga es:", resultado)

    except KeyboardInterrupt:
        print("\nEl programa ha sido interrumpido por el usuario.")

    except EOFError:
        print("\nError en la entrada de datos.")

    except Exception as error:
        print("\nHa ocurrido un error inesperado:")
        print(error)


# Bloque de ejecución principal
if __name__ == "__main__":
    main()
