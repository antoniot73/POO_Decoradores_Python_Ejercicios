"""
Ejercicio1_POO.py

Sistema de nómina con Programación Orientada a Objetos avanzada
combinada con Programación Estructurada.

Objetivo del ejercicio:
    Demostrar el dominio de conceptos avanzados de Programación Orientada a
    Objetos (POO) mediante un caso de cálculo de nómina con distintos tipos
    de empleados. El diseño aplica herencia, polimorfismo, abstracción, clase
    base abstracta y un Factory Method simple para crear objetos desde
    registros de entrada.

Decisiones de diseño:
    1. Se define la clase abstracta Empleado como contrato común. Esta clase
       no debe instanciarse directamente; obliga a que toda subclase implemente
       calcular_pago() y obtener_tipo().
    2. Se crean tres subclases concretas: EmpleadoTiempoCompleto,
       EmpleadoPorHoras y EmpleadoComisionista. Cada una sobrescribe
       calcular_pago() porque cada tipo de empleado tiene una regla de negocio
       distinta.
    3. Se usa un Factory Method en crear_empleado_desde_registro() para separar
       la creación de objetos de la lógica principal del programa. Esto reduce
       el acoplamiento y permite agregar nuevos tipos de empleados sin modificar
       el flujo principal de ejecución.
    4. Se mantiene Programación Estructurada dentro del programa mediante
       secuencia, selección, iteración, manejo de excepciones, funciones
       auxiliares, logging, reporte en consola y graficación.

Conceptos aplicados:
    - Clases, atributos y métodos.
    - Encapsulación mediante propiedades.
    - Clase base abstracta y métodos abstractos.
    - Herencia y sobrescritura de métodos.
    - Polimorfismo mediante una lista de objetos Empleado.
    - Factory Method para creación de objetos.
    - Programación estructurada: secuencia, selección e iteración.
    - Manejo de excepciones y logging.
    - Reporte en consola y generación de gráfica.

Requisitos:
    pip install matplotlib

Ejecución:
    python Ejercicio1_POO.py
"""

from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt


def configurar_logging() -> None:
    """
    Configura la bitácora de eventos del programa.

    La bitácora permite registrar eventos relevantes del flujo de ejecución:
    inicio del programa, creación de objetos, cálculo de nómina, generación
    de gráfica y errores controlados.

    Returns:
        None.
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
    )


class Empleado(ABC):
    """
    Clase base abstracta para representar empleados.

    Esta clase define el contrato técnico que deben cumplir todos los tipos
    de empleados. La existencia de métodos abstractos garantiza que cada
    subclase implemente su propia regla de cálculo de pago.

    Attributes:
        _nombre: Nombre completo del empleado.
        _identificador: Identificador único del empleado.
    """

    def __init__(self, nombre: str, identificador: str) -> None:
        """
        Inicializa los atributos comunes de cualquier empleado.

        Args:
            nombre: Nombre completo del empleado.
            identificador: Código o identificador único del empleado.

        Raises:
            ValueError: Si nombre o identificador están vacíos.
        """
        if not nombre.strip():
            raise ValueError("El nombre del empleado no puede estar vacío.")

        if not identificador.strip():
            raise ValueError("El identificador del empleado no puede estar vacío.")

        self._nombre = nombre.strip()
        self._identificador = identificador.strip()

    @property
    def nombre(self) -> str:
        """
        Obtiene el nombre del empleado.

        Returns:
            Nombre completo del empleado.
        """
        return self._nombre

    @property
    def identificador(self) -> str:
        """
        Obtiene el identificador del empleado.

        Returns:
            Identificador único del empleado.
        """
        return self._identificador

    @abstractmethod
    def calcular_pago(self) -> float:
        """
        Calcula el pago del empleado.

        Este método es abstracto porque la regla de cálculo depende de la
        subclase concreta: tiempo completo, por horas o comisionista.

        Returns:
            Pago calculado.
        """

    @abstractmethod
    def obtener_tipo(self) -> str:
        """
        Obtiene la categoría del empleado.

        Returns:
            Tipo de empleado como cadena de texto.
        """

    def generar_resumen(self) -> str:
        """
        Genera una línea formateada para el reporte de nómina.

        Returns:
            Cadena con identificador, nombre, tipo y pago calculado.
        """
        return (
            f"{self.identificador:<8} | "
            f"{self.nombre:<25} | "
            f"{self.obtener_tipo():<20} | "
            f"${self.calcular_pago():>12,.2f}"
        )


class EmpleadoTiempoCompleto(Empleado):
    """
    Representa un empleado con salario mensual fijo y bono.

    El pago se calcula como salario mensual más bono. Esta clase demuestra
    herencia porque reutiliza los atributos comunes definidos en Empleado,
    y polimorfismo porque sobrescribe calcular_pago().
    """

    def __init__(
        self,
        nombre: str,
        identificador: str,
        salario_mensual: float,
        bono: float,
    ) -> None:
        """
        Inicializa un empleado de tiempo completo.

        Args:
            nombre: Nombre completo del empleado.
            identificador: Código único del empleado.
            salario_mensual: Salario mensual base.
            bono: Bono adicional.

        Raises:
            ValueError: Si salario_mensual o bono son negativos.
        """
        super().__init__(nombre, identificador)

        if salario_mensual < 0:
            raise ValueError("El salario mensual no puede ser negativo.")

        if bono < 0:
            raise ValueError("El bono no puede ser negativo.")

        self.salario_mensual = salario_mensual
        self.bono = bono

    def calcular_pago(self) -> float:
        """
        Calcula el pago de un empleado de tiempo completo.

        Returns:
            Suma de salario mensual y bono.
        """
        return self.salario_mensual + self.bono

    def obtener_tipo(self) -> str:
        """
        Obtiene el tipo de empleado.

        Returns:
            Texto descriptivo del tipo de empleado.
        """
        return "Tiempo completo"


class EmpleadoPorHoras(Empleado):
    """
    Representa un empleado pagado por horas trabajadas.

    Si el empleado trabaja más de 40 horas, las horas adicionales se pagan
    con factor extra de 1.5. Esta regla de negocio se encapsula en la
    subclase para evitar condicionales externos en el programa principal.
    """

    def __init__(
        self,
        nombre: str,
        identificador: str,
        horas_trabajadas: float,
        tarifa_hora: float,
    ) -> None:
        """
        Inicializa un empleado por horas.

        Args:
            nombre: Nombre completo del empleado.
            identificador: Código único del empleado.
            horas_trabajadas: Total de horas trabajadas.
            tarifa_hora: Pago por hora.

        Raises:
            ValueError: Si horas_trabajadas o tarifa_hora son negativas.
        """
        super().__init__(nombre, identificador)

        if horas_trabajadas < 0:
            raise ValueError("Las horas trabajadas no pueden ser negativas.")

        if tarifa_hora < 0:
            raise ValueError("La tarifa por hora no puede ser negativa.")

        self.horas_trabajadas = horas_trabajadas
        self.tarifa_hora = tarifa_hora

    def calcular_pago(self) -> float:
        """
        Calcula el pago del empleado por horas.

        Returns:
            Pago total considerando horas normales y horas extra.
        """
        horas_normales = 40.0
        factor_extra = 1.5

        # Selección estructurada: regla distinta si existen horas extra.
        if self.horas_trabajadas <= horas_normales:
            return self.horas_trabajadas * self.tarifa_hora

        horas_extra = self.horas_trabajadas - horas_normales
        pago_normal = horas_normales * self.tarifa_hora
        pago_extra = horas_extra * self.tarifa_hora * factor_extra

        return pago_normal + pago_extra

    def obtener_tipo(self) -> str:
        """
        Obtiene el tipo de empleado.

        Returns:
            Texto descriptivo del tipo de empleado.
        """
        return "Por horas"


class EmpleadoComisionista(Empleado):
    """
    Representa un empleado con salario base y comisión sobre ventas.

    El cálculo combina un pago fijo con un porcentaje sobre ventas. La clase
    encapsula la validación de la comisión para asegurar que se encuentre
    entre 0 y 1.
    """

    def __init__(
        self,
        nombre: str,
        identificador: str,
        salario_base: float,
        ventas: float,
        porcentaje_comision: float,
    ) -> None:
        """
        Inicializa un empleado comisionista.

        Args:
            nombre: Nombre completo del empleado.
            identificador: Código único del empleado.
            salario_base: Sueldo fijo del empleado.
            ventas: Total de ventas generadas.
            porcentaje_comision: Comisión expresada como decimal.

        Raises:
            ValueError: Si los valores numéricos no cumplen las reglas.
        """
        super().__init__(nombre, identificador)

        if salario_base < 0:
            raise ValueError("El salario base no puede ser negativo.")

        if ventas < 0:
            raise ValueError("Las ventas no pueden ser negativas.")

        if porcentaje_comision < 0 or porcentaje_comision > 1:
            raise ValueError("La comisión debe estar entre 0 y 1.")

        self.salario_base = salario_base
        self.ventas = ventas
        self.porcentaje_comision = porcentaje_comision

    def calcular_pago(self) -> float:
        """
        Calcula el pago del empleado comisionista.

        Returns:
            Salario base más comisión sobre ventas.
        """
        return self.salario_base + (self.ventas * self.porcentaje_comision)

    def obtener_tipo(self) -> str:
        """
        Obtiene el tipo de empleado.

        Returns:
            Texto descriptivo del tipo de empleado.
        """
        return "Comisionista"


@dataclass
class ResultadoNomina:
    """
    Estructura de datos para almacenar resultados agregados de nómina.

    Attributes:
        total_empleados: Cantidad de empleados procesados.
        total_nomina: Suma de todos los pagos calculados.
        pago_promedio: Pago promedio por empleado.
    """

    total_empleados: int
    total_nomina: float
    pago_promedio: float


def obtener_numero(registro: dict[str, Any], clave: str) -> float:
    """
    Obtiene y valida un valor numérico desde un registro.

    Args:
        registro: Diccionario con datos del empleado.
        clave: Nombre del campo que se desea extraer.

    Returns:
        Valor convertido a float.

    Raises:
        ValueError: Si la clave no existe o no puede convertirse a float.
    """
    if clave not in registro:
        raise ValueError(f"Falta el campo requerido: {clave}")

    try:
        return float(registro[clave])
    except (TypeError, ValueError) as error:
        raise ValueError(f"El campo {clave} debe ser numérico.") from error


def crear_empleado_desde_registro(registro: dict[str, Any]) -> Empleado:
    """
    Crea un empleado concreto a partir de un registro de entrada.

    Esta función aplica un Factory Method simple. El programa principal no
    instancia directamente subclases; delega la decisión de creación a esta
    función, reduciendo acoplamiento.

    Args:
        registro: Diccionario con los datos necesarios del empleado.

    Returns:
        Instancia concreta de una subclase de Empleado.

    Raises:
        ValueError: Si el tipo de empleado no es soportado o faltan datos.
    """
    tipo = str(registro.get("tipo", "")).strip().lower()
    nombre = str(registro.get("nombre", "")).strip()
    identificador = str(registro.get("identificador", "")).strip()

    # Selección estructurada: según el tipo se construye una subclase concreta.
    if tipo == "tiempo_completo":
        return EmpleadoTiempoCompleto(
            nombre=nombre,
            identificador=identificador,
            salario_mensual=obtener_numero(registro, "salario_mensual"),
            bono=obtener_numero(registro, "bono"),
        )

    if tipo == "por_horas":
        return EmpleadoPorHoras(
            nombre=nombre,
            identificador=identificador,
            horas_trabajadas=obtener_numero(registro, "horas_trabajadas"),
            tarifa_hora=obtener_numero(registro, "tarifa_hora"),
        )

    if tipo == "comisionista":
        return EmpleadoComisionista(
            nombre=nombre,
            identificador=identificador,
            salario_base=obtener_numero(registro, "salario_base"),
            ventas=obtener_numero(registro, "ventas"),
            porcentaje_comision=obtener_numero(registro, "porcentaje_comision"),
        )

    raise ValueError(f"Tipo de empleado no soportado: {tipo}")


def obtener_registros_demo() -> list[dict[str, Any]]:
    """
    Define registros de prueba para crear empleados.

    Returns:
        Lista de diccionarios con datos de empleados.
    """
    return [
        {
            "tipo": "tiempo_completo",
            "nombre": "Ana Torres",
            "identificador": "E001",
            "salario_mensual": 25000,
            "bono": 3000,
        },
        {
            "tipo": "tiempo_completo",
            "nombre": "Luis Ramírez",
            "identificador": "E002",
            "salario_mensual": 28000,
            "bono": 2500,
        },
        {
            "tipo": "por_horas",
            "nombre": "María López",
            "identificador": "E003",
            "horas_trabajadas": 45,
            "tarifa_hora": 350,
        },
        {
            "tipo": "por_horas",
            "nombre": "Carlos Pérez",
            "identificador": "E004",
            "horas_trabajadas": 38,
            "tarifa_hora": 320,
        },
        {
            "tipo": "comisionista",
            "nombre": "Sofía Herrera",
            "identificador": "E005",
            "salario_base": 12000,
            "ventas": 85000,
            "porcentaje_comision": 0.08,
        },
        {
            "tipo": "comisionista",
            "nombre": "Jorge Medina",
            "identificador": "E006",
            "salario_base": 10000,
            "ventas": 65000,
            "porcentaje_comision": 0.10,
        },
    ]


def crear_empleados(registros: list[dict[str, Any]]) -> list[Empleado]:
    """
    Crea una lista de empleados usando el Factory Method.

    Args:
        registros: Lista de diccionarios con datos de empleados.

    Returns:
        Lista de objetos Empleado.

    Raises:
        ValueError: Si no se crea ningún empleado válido.
    """
    empleados: list[Empleado] = []

    # Iteración estructurada: cada registro se transforma en un objeto.
    for registro in registros:
        empleado = crear_empleado_desde_registro(registro)
        empleados.append(empleado)
        logging.info(
            "Empleado creado: %s | %s",
            empleado.identificador,
            empleado.obtener_tipo(),
        )

    if not empleados:
        raise ValueError("No se creó ningún empleado.")

    return empleados


def calcular_resultado_nomina(empleados: list[Empleado]) -> ResultadoNomina:
    """
    Calcula los resultados agregados de la nómina.

    Args:
        empleados: Lista de empleados.

    Returns:
        ResultadoNomina con total de empleados, total de nómina y promedio.

    Raises:
        ValueError: Si la lista está vacía.
    """
    if not empleados:
        raise ValueError("No existen empleados para procesar.")

    total_nomina = 0.0

    # Iteración polimórfica: cada objeto ejecuta su propia versión de calcular_pago().
    for empleado in empleados:
        total_nomina += empleado.calcular_pago()

    total_empleados = len(empleados)
    pago_promedio = total_nomina / total_empleados

    return ResultadoNomina(
        total_empleados=total_empleados,
        total_nomina=total_nomina,
        pago_promedio=pago_promedio,
    )


def imprimir_reporte_nomina(empleados: list[Empleado], resultado: ResultadoNomina) -> None:
    """
    Imprime en consola el reporte detallado de nómina.

    Args:
        empleados: Lista de empleados procesados.
        resultado: Datos agregados de la nómina.

    Returns:
        None.
    """
    print("\n" + "=" * 84)
    print("REPORTE DE NÓMINA - EJERCICIO1_POO")
    print("=" * 84)
    print(f"{'ID':<8} | {'Empleado':<25} | {'Tipo':<20} | {'Pago':>13}")
    print("-" * 84)

    for empleado in empleados:
        print(empleado.generar_resumen())

    print("-" * 84)
    print(f"Total de empleados procesados : {resultado.total_empleados}")
    print(f"Total de nómina               : ${resultado.total_nomina:,.2f}")
    print(f"Pago promedio                 : ${resultado.pago_promedio:,.2f}")
    print("=" * 84)


def generar_grafica_nomina(empleados: list[Empleado], ruta_salida: str) -> None:
    """
    Genera una gráfica de barras con el pago de cada empleado.

    Args:
        empleados: Lista de empleados procesados.
        ruta_salida: Ruta del archivo PNG que será generado.

    Returns:
        None.
    """
    nombres: list[str] = []
    pagos: list[float] = []

    for empleado in empleados:
        nombres.append(empleado.nombre)
        pagos.append(empleado.calcular_pago())

    plt.figure(figsize=(10, 6))
    plt.bar(nombres, pagos)
    plt.title("Ejercicio1_POO - Pagos calculados por empleado")
    plt.xlabel("Empleado")
    plt.ylabel("Pago calculado")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(ruta_salida)
    plt.close()

    logging.info("Gráfica generada correctamente: %s", ruta_salida)


def main() -> None:
    """
    Ejecuta el flujo principal del programa.

    Secuencia:
        1. Configurar logging.
        2. Obtener registros de prueba.
        3. Crear empleados mediante Factory Method.
        4. Calcular la nómina usando polimorfismo.
        5. Imprimir reporte en consola.
        6. Generar una gráfica como evidencia.
        7. Manejar errores de validación o ejecución.

    Returns:
        None.
    """
    configurar_logging()

    try:
        logging.info("Inicio de Ejercicio1_POO.")

        registros = obtener_registros_demo()
        empleados = crear_empleados(registros)
        resultado = calcular_resultado_nomina(empleados)

        imprimir_reporte_nomina(empleados, resultado)

        ruta_grafica = str(Path("Ejercicio1_POO_nomina.png"))
        generar_grafica_nomina(empleados, ruta_grafica)

        print(f"\nArchivo gráfico generado: {ruta_grafica}")
        logging.info("Ejecución finalizada correctamente.")

    except ValueError as error:
        logging.error("Error de validación: %s", error)
        print(f"Error de validación: {error}")

    except Exception as error:
        logging.exception("Error inesperado durante la ejecución.")
        print(f"Error inesperado: {error}")


if __name__ == "__main__":
    main()
