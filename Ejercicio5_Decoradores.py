"""
Ejercicio5_Decoradores.py

Decorador personalizado y parametrizado para validar argumentos numéricos.

Propósito:
    Implementar y aplicar un decorador avanzado que valide argumentos
    numéricos antes de ejecutar funciones matemáticas o financieras.
    El decorador extiende el comportamiento de las funciones decoradas
    sin modificar su lógica interna.

Conceptos aplicados:
    - Funciones como objetos de primera clase.
    - Decorador personalizado parametrizado.
    - Funciones anidadas.
    - Uso de *args y **kwargs.
    - functools.wraps para conservar metadatos.
    - Programación estructurada: secuencia, selección, iteración y excepciones.
    - Logging.
    - Reporte en consola.
    - Pruebas funcionales y prueba de error controlado.
"""

from __future__ import annotations

import logging
from collections.abc import Callable
from functools import wraps
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


def validar_numericos(
    *,
    permitir_cero: bool = False,
    minimo: float | None = None,
    maximo: float | None = None,
) -> Callable[[Callable[..., T]], Callable[..., T]]:
    """
    Decorador parametrizado para validar argumentos numéricos.

    Args:
        permitir_cero: Indica si el valor cero será aceptado.
        minimo: Valor mínimo permitido. Si es None, no se aplica límite inferior.
        maximo: Valor máximo permitido. Si es None, no se aplica límite superior.

    Returns:
        Decorador que envuelve la función original con validación previa.

    Raises:
        ValueError: Si la configuración del decorador es inconsistente.
    """
    if minimo is not None and maximo is not None and minimo > maximo:
        raise ValueError("El valor mínimo no puede ser mayor que el valor máximo.")

    def decorador(funcion: Callable[..., T]) -> Callable[..., T]:
        """
        Recibe la función que será decorada.

        Args:
            funcion: Función objetivo.

        Returns:
            Función envuelta con validación numérica.
        """

        @wraps(funcion)
        def wrapper(*args: Any, **kwargs: Any) -> T:
            """
            Valida argumentos numéricos antes de ejecutar la función original.

            Args:
                *args: Argumentos posicionales de la función decorada.
                **kwargs: Argumentos nombrados de la función decorada.

            Returns:
                Resultado original de la función decorada.
            """
            valores_a_validar: list[tuple[str, Any]] = []

            for indice, valor in enumerate(args):
                valores_a_validar.append((f"args[{indice}]", valor))

            for nombre, valor in kwargs.items():
                valores_a_validar.append((nombre, valor))

            for nombre, valor in valores_a_validar:
                if isinstance(valor, bool):
                    raise TypeError(
                        f"El argumento '{nombre}' es booleano y no se acepta como número."
                    )

                if isinstance(valor, (int, float)):
                    if not permitir_cero and valor == 0:
                        raise ValueError(f"El argumento '{nombre}' no puede ser cero.")

                    if valor < 0 and minimo is None:
                        raise ValueError(f"El argumento '{nombre}' no puede ser negativo.")

                    if minimo is not None and valor < minimo:
                        raise ValueError(
                            f"El argumento '{nombre}' debe ser mayor o igual que {minimo}."
                        )

                    if maximo is not None and valor > maximo:
                        raise ValueError(
                            f"El argumento '{nombre}' debe ser menor o igual que {maximo}."
                        )

            logging.info(
                "Validación numérica aprobada para función '%s'.",
                funcion.__name__,
            )
            return funcion(*args, **kwargs)

        return wrapper

    return decorador


@validar_numericos(permitir_cero=False, minimo=0.01)
def calcular_descuento(precio: float, porcentaje_descuento: float) -> float:
    """
    Calcula el precio final después de aplicar un descuento.

    Args:
        precio: Precio original del producto.
        porcentaje_descuento: Porcentaje de descuento expresado de 0 a 100.

    Returns:
        Precio final con descuento aplicado.

    Raises:
        ValueError: Si el porcentaje es mayor que 100.
    """
    if porcentaje_descuento > 100:
        raise ValueError("El porcentaje de descuento no puede ser mayor que 100.")

    descuento = precio * (porcentaje_descuento / 100)
    return precio - descuento


@validar_numericos(permitir_cero=False, minimo=1)
def calcular_promedio(*valores: float) -> float:
    """
    Calcula el promedio de un conjunto de valores positivos.

    Args:
        *valores: Valores numéricos a promediar.

    Returns:
        Promedio de los valores recibidos.

    Raises:
        ValueError: Si no se reciben valores.
    """
    if not valores:
        raise ValueError("Debe proporcionarse al menos un valor.")

    total = 0.0

    for valor in valores:
        total += valor

    return total / len(valores)


@validar_numericos(permitir_cero=True, minimo=0, maximo=1)
def calcular_indice_ponderado(
    precision: float,
    cobertura: float,
    peso_precision: float = 0.6,
    peso_cobertura: float = 0.4,
) -> float:
    """
    Calcula un índice ponderado a partir de métricas normalizadas.

    Args:
        precision: Métrica de precisión entre 0 y 1.
        cobertura: Métrica de cobertura entre 0 y 1.
        peso_precision: Peso asignado a la precisión.
        peso_cobertura: Peso asignado a la cobertura.

    Returns:
        Índice ponderado entre 0 y 1.

    Raises:
        ValueError: Si la suma de pesos no es igual a 1.
    """
    suma_pesos = peso_precision + peso_cobertura

    if round(suma_pesos, 6) != 1:
        raise ValueError("La suma de los pesos debe ser igual a 1.")

    return (precision * peso_precision) + (cobertura * peso_cobertura)


def ejecutar_pruebas() -> None:
    """
    Ejecuta pruebas funcionales del decorador validar_numericos.

    Returns:
        None
    """
    print("\\n" + "=" * 86)
    print("PRUEBAS DEL DECORADOR validar_numericos - EJERCICIO5_DECORADORES")
    print("=" * 86)

    precio_final = calcular_descuento(1500.0, 15.0)
    print(f"Precio final con descuento: ${precio_final:,.2f}")

    print("-" * 86)

    promedio = calcular_promedio(80, 90, 100, 95)
    print(f"Promedio calculado: {promedio:.2f}")

    print("-" * 86)

    indice = calcular_indice_ponderado(
        precision=0.92,
        cobertura=0.85,
        peso_precision=0.7,
        peso_cobertura=0.3,
    )
    print(f"Índice ponderado calculado: {indice:.4f}")

    print("=" * 86)


def ejecutar_pruebas_error_controlado() -> None:
    """
    Ejecuta pruebas controladas de error.

    Returns:
        None
    """
    print("\\n" + "=" * 86)
    print("PRUEBAS CONTROLADAS DE ERROR")
    print("=" * 86)

    casos = [
        ("Descuento con precio cero", lambda: calcular_descuento(0, 10)),
        ("Promedio con valor negativo", lambda: calcular_promedio(80, -5, 90)),
        (
            "Índice con precisión fuera de rango",
            lambda: calcular_indice_ponderado(
                precision=1.25,
                cobertura=0.80,
                peso_precision=0.5,
                peso_cobertura=0.5,
            ),
        ),
        ("Argumento booleano inválido", lambda: calcular_promedio(True, 90)),
    ]

    for nombre_caso, funcion_prueba in casos:
        try:
            funcion_prueba()

        except (ValueError, TypeError) as error:
            print(f"{nombre_caso}: excepción controlada -> {error}")
            logging.info("%s: excepción controlada -> %s", nombre_caso, error)

    print("=" * 86)


def main() -> None:
    """
    Controla la ejecución principal del programa.

    Returns:
        None
    """
    configurar_logging()

    try:
        logging.info("Inicio del programa Ejercicio5_Decoradores.")
        ejecutar_pruebas()
        ejecutar_pruebas_error_controlado()
        logging.info("Ejecución finalizada correctamente.")

    except Exception as error:
        logging.exception("Error inesperado durante la ejecución principal.")
        print(f"Error inesperado en el programa principal: {error}")


if __name__ == "__main__":
    main()
