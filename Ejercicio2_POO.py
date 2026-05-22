"""
Ejercicio2_POO.py

Sistema de figuras geométricas con Programación Orientada a Objetos avanzada
y Programación Estructurada.

Propósito:
    Calcular área y perímetro de distintas figuras geométricas aplicando
    abstracción, herencia, polimorfismo, validación de datos, manejo de
    excepciones, logging, reporte en consola y graficación básica.

Conceptos aplicados:
    - Clase base abstracta.
    - Métodos abstractos.
    - Herencia.
    - Polimorfismo.
    - Encapsulación mediante propiedades.
    - Factory Method para creación de figuras.
    - Programación estructurada: secuencia, selección, iteración y excepciones.
    - Logging, reporte en consola y gráfica de resultados.
"""

from __future__ import annotations

import logging
import math
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any

import matplotlib.pyplot as plt


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


class Figura(ABC):
    """
    Clase base abstracta para representar figuras geométricas.

    Attributes:
        _nombre: Nombre asignado a la figura.
    """

    def __init__(self, nombre: str) -> None:
        """
        Inicializa el nombre de una figura.

        Args:
            nombre: Nombre descriptivo de la figura.

        Raises:
            ValueError: Si el nombre está vacío.
        """
        if not nombre.strip():
            raise ValueError("El nombre de la figura no puede estar vacío.")
        self._nombre = nombre.strip()

    @property
    def nombre(self) -> str:
        """
        Devuelve el nombre de la figura.

        Returns:
            Nombre de la figura.
        """
        return self._nombre

    @abstractmethod
    def calcular_area(self) -> float:
        """
        Calcula el área de la figura.

        Returns:
            Área calculada.
        """

    @abstractmethod
    def calcular_perimetro(self) -> float:
        """
        Calcula el perímetro de la figura.

        Returns:
            Perímetro calculado.
        """

    @abstractmethod
    def obtener_tipo(self) -> str:
        """
        Devuelve el tipo de figura.

        Returns:
            Cadena con el tipo de figura.
        """

    def generar_resumen(self) -> str:
        """
        Genera una línea de reporte para la figura.

        Returns:
            Texto con nombre, tipo, área y perímetro.
        """
        return (
            f"{self.nombre:<20} | "
            f"{self.obtener_tipo():<14} | "
            f"{self.calcular_area():>12.4f} | "
            f"{self.calcular_perimetro():>12.4f}"
        )


class Rectangulo(Figura):
    """
    Representa un rectángulo.

    Attributes:
        base: Medida de la base.
        altura: Medida de la altura.
    """

    def __init__(self, nombre: str, base: float, altura: float) -> None:
        """
        Inicializa un rectángulo.

        Args:
            nombre: Nombre de la figura.
            base: Base del rectángulo.
            altura: Altura del rectángulo.

        Raises:
            ValueError: Si base o altura son menores o iguales que cero.
        """
        super().__init__(nombre)
        if base <= 0:
            raise ValueError("La base del rectángulo debe ser mayor que cero.")
        if altura <= 0:
            raise ValueError("La altura del rectángulo debe ser mayor que cero.")
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        """
        Calcula el área del rectángulo.

        Returns:
            Área del rectángulo.
        """
        return self.base * self.altura

    def calcular_perimetro(self) -> float:
        """
        Calcula el perímetro del rectángulo.

        Returns:
            Perímetro del rectángulo.
        """
        return 2 * (self.base + self.altura)

    def obtener_tipo(self) -> str:
        """
        Devuelve el tipo de figura.

        Returns:
            Tipo de figura.
        """
        return "Rectángulo"


class Circulo(Figura):
    """
    Representa un círculo.

    Attributes:
        radio: Radio del círculo.
    """

    def __init__(self, nombre: str, radio: float) -> None:
        """
        Inicializa un círculo.

        Args:
            nombre: Nombre de la figura.
            radio: Radio del círculo.

        Raises:
            ValueError: Si el radio es menor o igual que cero.
        """
        super().__init__(nombre)
        if radio <= 0:
            raise ValueError("El radio del círculo debe ser mayor que cero.")
        self.radio = radio

    def calcular_area(self) -> float:
        """
        Calcula el área del círculo.

        Returns:
            Área del círculo.
        """
        return math.pi * self.radio ** 2

    def calcular_perimetro(self) -> float:
        """
        Calcula la circunferencia del círculo.

        Returns:
            Perímetro del círculo.
        """
        return 2 * math.pi * self.radio

    def obtener_tipo(self) -> str:
        """
        Devuelve el tipo de figura.

        Returns:
            Tipo de figura.
        """
        return "Círculo"


class Triangulo(Figura):
    """
    Representa un triángulo.

    Attributes:
        lado_a: Primer lado del triángulo.
        lado_b: Segundo lado del triángulo.
        lado_c: Tercer lado del triángulo.
    """

    def __init__(self, nombre: str, lado_a: float, lado_b: float, lado_c: float) -> None:
        """
        Inicializa un triángulo validando la desigualdad triangular.

        Args:
            nombre: Nombre de la figura.
            lado_a: Primer lado.
            lado_b: Segundo lado.
            lado_c: Tercer lado.

        Raises:
            ValueError: Si algún lado es inválido o no cumple la desigualdad triangular.
        """
        super().__init__(nombre)
        lados = [lado_a, lado_b, lado_c]
        for lado in lados:
            if lado <= 0:
                raise ValueError("Todos los lados del triángulo deben ser mayores que cero.")
        if not self._es_triangulo_valido(lado_a, lado_b, lado_c):
            raise ValueError("Los lados indicados no forman un triángulo válido.")
        self.lado_a = lado_a
        self.lado_b = lado_b
        self.lado_c = lado_c

    @staticmethod
    def _es_triangulo_valido(lado_a: float, lado_b: float, lado_c: float) -> bool:
        """
        Verifica la desigualdad triangular.

        Args:
            lado_a: Primer lado.
            lado_b: Segundo lado.
            lado_c: Tercer lado.

        Returns:
            True si los lados forman un triángulo válido; False en caso contrario.
        """
        return (
            lado_a + lado_b > lado_c
            and lado_a + lado_c > lado_b
            and lado_b + lado_c > lado_a
        )

    def calcular_area(self) -> float:
        """
        Calcula el área del triángulo mediante la fórmula de Herón.

        Returns:
            Área del triángulo.
        """
        semiperimetro = self.calcular_perimetro() / 2
        return math.sqrt(
            semiperimetro
            * (semiperimetro - self.lado_a)
            * (semiperimetro - self.lado_b)
            * (semiperimetro - self.lado_c)
        )

    def calcular_perimetro(self) -> float:
        """
        Calcula el perímetro del triángulo.

        Returns:
            Perímetro del triángulo.
        """
        return self.lado_a + self.lado_b + self.lado_c

    def obtener_tipo(self) -> str:
        """
        Devuelve el tipo de figura.

        Returns:
            Tipo de figura.
        """
        return "Triángulo"


@dataclass
class ResultadoFiguras:
    """
    Representa los resultados agregados del análisis de figuras.

    Attributes:
        total_figuras: Cantidad de figuras procesadas.
        area_total: Suma de áreas.
        perimetro_total: Suma de perímetros.
        area_promedio: Área promedio.
        perimetro_promedio: Perímetro promedio.
    """
    total_figuras: int
    area_total: float
    perimetro_total: float
    area_promedio: float
    perimetro_promedio: float


def crear_figura_desde_registro(registro: dict[str, Any]) -> Figura:
    """
    Crea una figura geométrica a partir de un registro de datos.

    Esta función implementa el patrón Factory Method, centralizando la
    creación de objetos concretos a partir del valor de la clave 'tipo'.

    Args:
        registro: Diccionario con los datos necesarios para crear una figura.

    Returns:
        Instancia concreta de Figura.

    Raises:
        ValueError: Si el tipo de figura no es soportado.
        KeyError: Si faltan claves requeridas.
    """
    tipo = str(registro["tipo"]).lower().strip()
    nombre = str(registro["nombre"]).strip()

    if tipo == "rectangulo":
        return Rectangulo(nombre, float(registro["base"]), float(registro["altura"]))
    if tipo == "circulo":
        return Circulo(nombre, float(registro["radio"]))
    if tipo == "triangulo":
        return Triangulo(
            nombre,
            float(registro["lado_a"]),
            float(registro["lado_b"]),
            float(registro["lado_c"]),
        )
    raise ValueError(f"Tipo de figura no soportado: {tipo}")


def crear_figuras_demo() -> list[Figura]:
    """
    Crea una lista de figuras de demostración.

    Returns:
        Lista de figuras concretas creadas mediante Factory Method.
    """
    registros = [
        {"tipo": "rectangulo", "nombre": "Rectángulo A", "base": 10, "altura": 5},
        {"tipo": "rectangulo", "nombre": "Rectángulo B", "base": 7.5, "altura": 3.2},
        {"tipo": "circulo", "nombre": "Círculo A", "radio": 4},
        {"tipo": "circulo", "nombre": "Círculo B", "radio": 2.8},
        {"tipo": "triangulo", "nombre": "Triángulo A", "lado_a": 3, "lado_b": 4, "lado_c": 5},
        {"tipo": "triangulo", "nombre": "Triángulo B", "lado_a": 6, "lado_b": 7, "lado_c": 8},
    ]

    figuras: list[Figura] = []
    for registro in registros:
        figuras.append(crear_figura_desde_registro(registro))

    logging.info("Se crearon %d figuras de demostración.", len(figuras))
    return figuras


def calcular_resultado_figuras(figuras: list[Figura]) -> ResultadoFiguras:
    """
    Calcula resultados agregados de las figuras.

    Args:
        figuras: Lista de figuras a procesar.

    Returns:
        ResultadoFiguras con totales y promedios.

    Raises:
        ValueError: Si la lista está vacía.
    """
    if not figuras:
        raise ValueError("No existen figuras para calcular resultados.")

    area_total = 0.0
    perimetro_total = 0.0

    for figura in figuras:
        area_total += figura.calcular_area()
        perimetro_total += figura.calcular_perimetro()

    total_figuras = len(figuras)

    return ResultadoFiguras(
        total_figuras=total_figuras,
        area_total=area_total,
        perimetro_total=perimetro_total,
        area_promedio=area_total / total_figuras,
        perimetro_promedio=perimetro_total / total_figuras,
    )


def imprimir_reporte_figuras(figuras: list[Figura], resultado: ResultadoFiguras) -> None:
    """
    Imprime en consola el reporte detallado de figuras.

    Args:
        figuras: Lista de figuras procesadas.
        resultado: Resultados agregados del análisis.

    Returns:
        None
    """
    print("\n" + "=" * 72)
    print("REPORTE DE FIGURAS GEOMÉTRICAS - EJERCICIO2_POO")
    print("=" * 72)
    print(f"{'Figura':<20} | {'Tipo':<14} | {'Área':>12} | {'Perímetro':>12}")
    print("-" * 72)

    for figura in figuras:
        print(figura.generar_resumen())

    print("-" * 72)
    print(f"Total de figuras procesadas : {resultado.total_figuras}")
    print(f"Área total                  : {resultado.area_total:.4f}")
    print(f"Perímetro total             : {resultado.perimetro_total:.4f}")
    print(f"Área promedio               : {resultado.area_promedio:.4f}")
    print(f"Perímetro promedio          : {resultado.perimetro_promedio:.4f}")
    print("=" * 72)


def generar_grafica_areas(figuras: list[Figura], ruta_salida: str) -> None:
    """
    Genera una gráfica de barras con el área de cada figura.

    Args:
        figuras: Lista de figuras procesadas.
        ruta_salida: Ruta del archivo de imagen que se generará.

    Returns:
        None
    """
    nombres: list[str] = []
    areas: list[float] = []

    for figura in figuras:
        nombres.append(figura.nombre)
        areas.append(figura.calcular_area())

    plt.figure(figsize=(10, 6))
    plt.bar(nombres, areas)
    plt.title("Áreas calculadas por figura")
    plt.xlabel("Figura")
    plt.ylabel("Área calculada")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(ruta_salida)
    plt.close()

    logging.info("Gráfica de áreas guardada en: %s", ruta_salida)


def probar_validacion_triangulo() -> None:
    """
    Ejecuta una prueba controlada de validación de triángulo inválido.

    Returns:
        None
    """
    try:
        Triangulo("Triángulo inválido", 1, 2, 10)
    except ValueError as error:
        logging.info("Prueba controlada de validación: %s", error)


def main() -> None:
    """
    Controla la ejecución principal del programa.

    Secuencia general:
        1. Configura logging.
        2. Crea figuras de demostración mediante Factory Method.
        3. Calcula áreas y perímetros usando polimorfismo.
        4. Imprime un reporte en consola.
        5. Genera una gráfica de áreas.
        6. Ejecuta una prueba controlada de validación.
        7. Maneja errores de ejecución.

    Returns:
        None
    """
    configurar_logging()

    try:
        logging.info("Inicio del programa Ejercicio2_POO.")
        figuras = crear_figuras_demo()
        resultado = calcular_resultado_figuras(figuras)
        imprimir_reporte_figuras(figuras, resultado)
        generar_grafica_areas(figuras, "Ejercicio2_POO_areas.png")
        probar_validacion_triangulo()
        logging.info("Ejecución finalizada correctamente.")

    except (ValueError, KeyError) as error:
        logging.error("Error de validación o datos incompletos: %s", error)
        print(f"Error de validación o datos incompletos: {error}")

    except Exception as error:
        logging.exception("Error inesperado durante la ejecución.")
        print(f"Error inesperado: {error}")


if __name__ == "__main__":
    main()
