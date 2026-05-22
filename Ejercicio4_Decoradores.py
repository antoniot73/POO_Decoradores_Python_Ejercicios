"""
Ejercicio4_Decoradores.py

Decorador personalizado para medir tiempo de ejecución de funciones.

Propósito:
    Implementar y aplicar un decorador avanzado que mida el tiempo de
    ejecución de funciones en Python, sin modificar directamente la lógica
    interna de las funciones decoradas.

Conceptos aplicados:
    - Funciones como objetos de primera clase.
    - Decorador personalizado.
    - Función anidada wrapper.
    - Uso de *args y **kwargs.
    - functools.wraps para conservar metadatos.
    - Programación estructurada: secuencia, selección, iteración y excepciones.
    - Logging.
    - Reporte en consola.
    - Pruebas funcionales.
"""

from __future__ import annotations

import logging
from collections.abc import Callable
from functools import wraps
from time import perf_counter
from typing import Any, TypeVar

T = TypeVar("T")


def configurar_logging() -> None:
    """
    Configura la bitácora de eventos del programa.

    Returns:
        None
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
    )


def medir_tiempo(funcion: Callable[..., T]) -> Callable[..., T]:
    """
    Decorador personalizado para medir el tiempo de ejecución de una función.

    Args:
        funcion: Función que será decorada.

    Returns:
        Función envolvente que conserva el resultado original y reporta
        el tiempo de ejecución.
    """

    @wraps(funcion)
    def wrapper(*args: Any, **kwargs: Any) -> T:
        """
        Ejecuta la función original midiendo su duración.

        Args:
            *args: Argumentos posicionales de la función decorada.
            **kwargs: Argumentos nombrados de la función decorada.

        Returns:
            Resultado original de la función decorada.
        """
        inicio = perf_counter()

        try:
            resultado = funcion(*args, **kwargs)
            fin = perf_counter()
            duracion = fin - inicio

            print(
                f"Función '{funcion.__name__}' ejecutada en "
                f"{duracion:.6f} segundos."
            )
            logging.info(
                "La función '%s' finalizó correctamente en %.6f segundos.",
                funcion.__name__,
                duracion,
            )
            return resultado

        except Exception as error:
            fin = perf_counter()
            duracion = fin - inicio

            logging.exception(
                "La función '%s' falló después de %.6f segundos.",
                funcion.__name__,
                duracion,
            )
            print(
                f"Error en función '{funcion.__name__}' "
                f"después de {duracion:.6f} segundos: {error}"
            )
            raise

    return wrapper


@medir_tiempo
def calcular_primos(hasta: int) -> list[int]:
    """
    Calcula números primos menores que un límite dado.

    Args:
        hasta: Límite superior no incluido para calcular números primos.

    Returns:
        Lista de números primos menores que el límite.

    Raises:
        ValueError: Si el límite es menor que 2.
    """
    if hasta < 2:
        raise ValueError("El límite debe ser mayor o igual que 2.")

    primos: list[int] = []

    for numero in range(2, hasta):
        es_primo = True

        for divisor in range(2, int(numero ** 0.5) + 1):
            if numero % divisor == 0:
                es_primo = False
                break

        if es_primo:
            primos.append(numero)

    return primos


@medir_tiempo
def sumar_rango(inicio: int, fin: int) -> int:
    """
    Suma los valores enteros contenidos en un rango.

    Args:
        inicio: Valor inicial del rango.
        fin: Valor final del rango, no incluido.

    Returns:
        Suma total de los valores del rango.

    Raises:
        ValueError: Si el valor inicial es mayor o igual que el valor final.
    """
    if inicio >= fin:
        raise ValueError("El valor inicial debe ser menor que el valor final.")

    total = 0

    for numero in range(inicio, fin):
        total += numero

    return total


@medir_tiempo
def filtrar_pares(numeros: list[int]) -> list[int]:
    """
    Filtra los números pares de una lista de enteros.

    Args:
        numeros: Lista de números enteros.

    Returns:
        Lista con los números pares.

    Raises:
        ValueError: Si la lista está vacía.
    """
    if not numeros:
        raise ValueError("La lista de números no puede estar vacía.")

    pares: list[int] = []

    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)

    return pares


def ejecutar_pruebas() -> None:
    """
    Ejecuta pruebas funcionales del decorador medir_tiempo.

    Returns:
        None
    """
    print("\n" + "=" * 80)
    print("PRUEBAS DEL DECORADOR medir_tiempo - EJERCICIO4_DECORADORES")
    print("=" * 80)

    primos = calcular_primos(50000)
    print(f"Cantidad de primos encontrados: {len(primos)}")
    print(f"Primeros 10 primos: {primos[:10]}")

    print("-" * 80)

    suma = sumar_rango(1, 1000000)
    print(f"Suma del rango 1 a 999999: {suma}")

    print("-" * 80)

    numeros = list(range(1, 101))
    pares = filtrar_pares(numeros)
    print(f"Cantidad de números pares entre 1 y 100: {len(pares)}")
    print(f"Números pares encontrados: {pares}")

    print("=" * 80)


def ejecutar_prueba_error_controlado() -> None:
    """
    Ejecuta una prueba controlada de error.

    Returns:
        None
    """
    print("\n" + "=" * 80)
    print("PRUEBA CONTROLADA DE ERROR")
    print("=" * 80)

    try:
        calcular_primos(1)

    except ValueError as error:
        print(f"Excepción controlada capturada: {error}")

    print("=" * 80)


def main() -> None:
    """
    Controla la ejecución principal del programa.

    Returns:
        None
    """
    configurar_logging()

    try:
        logging.info("Inicio del programa Ejercicio4_Decoradores.")
        ejecutar_pruebas()
        ejecutar_prueba_error_controlado()
        logging.info("Ejecución finalizada correctamente.")

    except Exception as error:
        logging.exception("Error inesperado durante la ejecución principal.")
        print(f"Error inesperado en el programa principal: {error}")


if __name__ == "__main__":
    main()
