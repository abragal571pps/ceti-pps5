#!/usr/bin/env python3
"""
Programa de testing para la función cadena_mas_larga.

Incluye:
- Pruebas deterministas
- Casos límite
- Entradas no válidas
- Pruebas aleatorias

La salida por consola se personaliza para mostrar el nombre del test y
si ha sido correcto (OK) o el tipo de error en caso de fallo.
"""

import random
import string
import unittest

from mychar import cadena_mas_larga

NUM_PRUEBAS = 100


class TestCadenaMasLarga(unittest.TestCase):


    # ====================================================
    # ENTRADAS VALIDAS
    # ====================================================

    def test_a_ejemplo_enunciado(self):
        lista = ["a", "ab", "abc", "dddd", "abcd"]
        self.assertEqual(cadena_mas_larga(lista), "abcd")


    def test_a_una_sola_cadena(self):
        self.assertEqual(cadena_mas_larga(["hola"]), "hola")


    def test_a_empate_real_longitud(self):
        """
        Empate real: todas las cadenas tienen la misma longitud.
        Se devuelve la primera alfabéticamente.
        """
        lista = ["perro", "gatos", "raton"]
        self.assertEqual(cadena_mas_larga(lista), "gatos")


    def test_a_simbolos_y_numeros_como_texto(self):
        lista = ["abc", "1234", "!@#$", "abcd"]
        self.assertEqual(cadena_mas_larga(lista), "!@#$")


    def test_a_mayusculas_minusculas(self):
        lista = ["abcd", "Abcd"]
        self.assertEqual(cadena_mas_larga(lista), "Abcd")


    # ====================================================
    # CASOS LIMITE
    # ====================================================

    def test_b_lista_vacia(self):
        self.assertEqual(cadena_mas_larga([]), "")


    def test_b_cadenas_vacias(self):
        self.assertEqual(cadena_mas_larga(["", "", "a"]), "a")


    def test_b_cadenas_muy_largas(self):
        corta = "a" * 10
        larga = "b" * 1000
        self.assertEqual(cadena_mas_larga([corta, larga]), larga)


    # ====================================================
    # ENTRADAS NO VALIDAS
    # ====================================================

    def test_c_entrada_no_lista(self):
        with self.assertRaises(TypeError):
            cadena_mas_larga("no_es_lista")

        with self.assertRaises(TypeError):
            cadena_mas_larga(123)

        with self.assertRaises(TypeError):
            cadena_mas_larga(None)


    def test_c_elementos_no_cadena(self):
        with self.assertRaises(TypeError):
            cadena_mas_larga(["hola", 5, "adios"])

        with self.assertRaises(TypeError):
            cadena_mas_larga([True, "texto"])

        with self.assertRaises(TypeError):
            cadena_mas_larga(["ok", None])


    # ====================================================
    # TESTS ALEATORIOS
    # ====================================================

    def test_z_listas_aleatorias(self):
        """
        Genera listas aleatorias válidas y no válidas,
        mostrando el resultado de cada iteración y un
        resumen final de los casos ejecutados.
        """

        total_validas = 0
        total_invalidas = 0

        for i in range(NUM_PRUEBAS):

            tamaño = random.randint(1, 10)

            # Decidimos si este test será válido o no
            lista_valida = random.choice([True, False])
            lista = []

            for _ in range(tamaño):

                if lista_valida:
                    # Solo cadenas
                    longitud = random.randint(0, 10)
                    valor = "".join(
                        random.choice(string.ascii_lowercase)
                        for _ in range(longitud)
                    )
                else:
                    # Introducimos un valor no válido
                    tipo = random.choice(["int", "none", "bool"])

                    if tipo == "int":
                        valor = random.randint(0, 100)
                    elif tipo == "none":
                        valor = None
                    else:
                        valor = random.choice([True, False])

                lista.append(valor)

            with self.subTest(iteracion=i, datos=lista):

                if lista_valida:
                    total_validas += 1
                    resultado = cadena_mas_larga(lista)
                    print( f"[i {i:03d}] OK             -> {resultado} :: {lista}" )

                    self.assertIn(resultado, lista)

                else:
                    total_invalidas += 1
                    print( f"[i {i:03d}] ERROR ESPERADO -> TypeError :: {lista}" )

                    with self.assertRaises(TypeError):
                        cadena_mas_larga(lista)

        # Resumen final del test aleatorio
        print("\nResumen del test aleatorio:")
        print(f" - Total de iteraciones : {NUM_PRUEBAS}")
        print(f" - Casos válidos        : {total_validas}")
        print(f" - Casos no válidos     : {total_invalidas}\n")


# ======================================================
# PERSONALIZACION PARA SALIDA POR CONSOLA
# ======================================================

class CustomTestResult(unittest.TextTestResult):

    def addSuccess(self, test):
        super().addSuccess(test)
        print(f"{test._testMethodName} -> OK")


    def addFailure(self, test, err):
        super().addFailure(test, err)
        print(f"{test._testMethodName} -> FAIL ({err[0].__name__})")


    def addError(self, test, err):
        super().addError(test, err)
        print(f"{test._testMethodName} -> ERROR ({err[0].__name__})")


class CustomTestRunner(unittest.TextTestRunner):
    resultclass = CustomTestResult


if __name__ == "__main__":
    unittest.main(testRunner=CustomTestRunner(), verbosity=0)
