"""
Ejercicio6_Decoradores.py

Decorador avanzado de auditoría con logging y manejo de errores.

Propósito:
    Implementar y aplicar un decorador avanzado que registre auditoría
    de ejecución sobre funciones Python, incluyendo nombre de función,
    argumentos, resultado, tiempo de ejecución y errores.
"""

from __future__ import annotations

import logging
from collections.abc import Callable
from functools import wraps
from time import perf_counter
from typing import Any, TypeVar

T = TypeVar("T")


def configurar_logging() -> None:
    """Configura la bitácora de eventos del programa."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
    )


def auditar_ejecucion(funcion: Callable[..., T]) -> Callable[..., T]:
    """
    Decorador avanzado para auditar ejecución de funciones.

    Args:
        funcion: Función que será decorada.

    Returns:
        Función envuelta con auditoría avanzada.
    """

    @wraps(funcion)
    def wrapper(*args: Any, **kwargs: Any) -> T:
        """
        Ejecuta auditoría antes y después de la función decorada.

        Args:
            *args: Argumentos posicionales.
            **kwargs: Argumentos nombrados.

        Returns:
            Resultado original de la función decorada.
        """
        inicio = perf_counter()

        print("\n" + "=" * 80)
        print(f"INICIO AUDITORÍA -> {funcion.__name__}")
        print("=" * 80)
        print(f"Argumentos posicionales: {args}")
        print(f"Argumentos nombrados  : {kwargs}")

        logging.info(
            "Inicio de función '%s' con args=%s kwargs=%s",
            funcion.__name__,
            args,
            kwargs,
        )

        try:
            resultado = funcion(*args, **kwargs)
            duracion = perf_counter() - inicio

            print(f"Resultado obtenido    : {resultado}")
            print(f"Tiempo de ejecución   : {duracion:.6f} segundos")

            logging.info(
                "Función '%s' ejecutada correctamente en %.6f segundos.",
                funcion.__name__,
                duracion,
            )

            print("=" * 80)
            print(f"FIN AUDITORÍA -> {funcion.__name__}")
            print("=" * 80)

            return resultado

        except Exception as error:
            duracion = perf_counter() - inicio

            logging.exception(
                "Error en función '%s' después de %.6f segundos.",
                funcion.__name__,
                duracion,
            )

            print(f"Error detectado       : {error}")
            print(f"Tiempo hasta error    : {duracion:.6f} segundos")
            print("=" * 80)
            print(f"FIN AUDITORÍA -> {funcion.__name__}")
            print("=" * 80)

            raise

    return wrapper


@auditar_ejecucion
def calcular_factorial(numero: int) -> int:
    """
    Calcula el factorial de un número entero positivo.

    Args:
        numero: Número entero positivo.

    Returns:
        Factorial calculado.

    Raises:
        ValueError: Si el número es negativo.
    """
    if numero < 0:
        raise ValueError("El número no puede ser negativo.")

    factorial = 1

    for valor in range(1, numero + 1):
        factorial *= valor

    return factorial


@auditar_ejecucion
def convertir_temperatura(temperatura: float, origen: str, destino: str) -> float:
    """
    Convierte temperaturas entre Celsius y Fahrenheit.

    Args:
        temperatura: Valor de temperatura.
        origen: Unidad de origen.
        destino: Unidad destino.

    Returns:
        Temperatura convertida.

    Raises:
        ValueError: Si las unidades son inválidas.
    """
    origen = origen.upper().strip()
    destino = destino.upper().strip()

    if origen == destino:
        return temperatura

    if origen == "C" and destino == "F":
        return (temperatura * 9 / 5) + 32

    if origen == "F" and destino == "C":
        return (temperatura - 32) * 5 / 9

    raise ValueError("Conversión de temperatura no soportada.")


@auditar_ejecucion
def analizar_texto(texto: str) -> dict[str, int]:
    """
    Analiza estadísticas básicas de un texto.

    Args:
        texto: Texto a analizar.

    Returns:
        Diccionario con estadísticas del texto.

    Raises:
        ValueError: Si el texto está vacío.
    """
    if not texto.strip():
        raise ValueError("El texto no puede estar vacío.")

    palabras = texto.split()
    resultado = {"caracteres": len(texto), "palabras": len(palabras), "vocales": 0}
    vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"

    for caracter in texto:
        if caracter in vocales:
            resultado["vocales"] += 1

    return resultado


def ejecutar_pruebas() -> None:
    """Ejecuta pruebas funcionales del decorador."""
    print("\n" + "#" * 90)
    print("PRUEBAS DEL DECORADOR auditar_ejecucion - EJERCICIO6_DECORADORES")
    print("#" * 90)

    factorial = calcular_factorial(8)
    print(f"Factorial calculado: {factorial}")

    print("-" * 90)

    temperatura = convertir_temperatura(25, "C", "F")
    print(f"Temperatura convertida: {temperatura:.2f} °F")

    print("-" * 90)

    estadisticas = analizar_texto(
        "La programación orientada a objetos permite construir sistemas reutilizables."
    )
    print(f"Estadísticas del texto: {estadisticas}")

    print("#" * 90)


def ejecutar_pruebas_error_controlado() -> None:
    """Ejecuta pruebas controladas de error."""
    print("\n" + "#" * 90)
    print("PRUEBAS CONTROLADAS DE ERROR")
    print("#" * 90)

    casos = [
        ("Factorial negativo", lambda: calcular_factorial(-5)),
        ("Conversión inválida", lambda: convertir_temperatura(30, "K", "F")),
        ("Texto vacío", lambda: analizar_texto("")),
    ]

    for nombre_caso, prueba in casos:
        try:
            prueba()
        except Exception as error:
            print(f"{nombre_caso}: excepción controlada -> {error}")
            logging.info("%s: excepción controlada -> %s", nombre_caso, error)

    print("#" * 90)


def main() -> None:
    """Controla la ejecución principal del programa."""
    configurar_logging()

    try:
        logging.info("Inicio del programa Ejercicio6_Decoradores.")
        ejecutar_pruebas()
        ejecutar_pruebas_error_controlado()
        logging.info("Ejecución finalizada correctamente.")

    except Exception as error:
        logging.exception("Error inesperado durante la ejecución principal.")
        print(f"Error inesperado en el programa principal: {error}")


if __name__ == "__main__":
    main()
