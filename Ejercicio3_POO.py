
"""
Ejercicio3_POO.py

Sistema de notificaciones con Programación Orientada a Objetos avanzada
y Programación Estructurada.

Propósito:
    Gestionar el envío simulado de notificaciones por distintos canales
    aplicando abstracción, herencia, polimorfismo, patrón Factory Method,
    validación de datos, manejo de excepciones, logging y reporte en consola.

Conceptos aplicados:
    - Clase base abstracta.
    - Métodos abstractos.
    - Herencia.
    - Polimorfismo.
    - Encapsulación mediante propiedades.
    - Factory Method para creación de notificadores.
    - Programación estructurada: secuencia, selección, iteración y excepciones.
    - Logging y reporte en consola.
"""

from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any


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


class Notificador(ABC):
    """
    Clase base abstracta para representar un canal de notificación.

    Attributes:
        _destinatario: Destinatario de la notificación.
    """

    def __init__(self, destinatario: str) -> None:
        """
        Inicializa el destinatario común del notificador.

        Args:
            destinatario: Identificador del destinatario.

        Raises:
            ValueError: Si el destinatario está vacío.
        """
        if not destinatario.strip():
            raise ValueError("El destinatario no puede estar vacío.")

        self._destinatario = destinatario.strip()

    @property
    def destinatario(self) -> str:
        """
        Devuelve el destinatario de la notificación.

        Returns:
            Destinatario de la notificación.
        """
        return self._destinatario

    @abstractmethod
    def enviar(self, mensaje: str) -> bool:
        """
        Envía una notificación.

        Args:
            mensaje: Contenido del mensaje.

        Returns:
            True si el envío fue exitoso; False en caso contrario.
        """

    @abstractmethod
    def obtener_tipo(self) -> str:
        """
        Devuelve el tipo de canal de notificación.

        Returns:
            Tipo de notificador.
        """

    def generar_resumen(self, mensaje: str, estado: bool) -> str:
        """
        Genera una línea de resumen del envío.

        Args:
            mensaje: Mensaje enviado.
            estado: Resultado del envío.

        Returns:
            Texto con canal, destinatario, mensaje y estado.
        """
        estado_texto = "Exitoso" if estado else "Fallido"
        return (
            f"{self.obtener_tipo():<15} | "
            f"{self.destinatario:<25} | "
            f"{mensaje:<35} | "
            f"{estado_texto:<10}"
        )


class NotificadorEmail(Notificador):
    """
    Representa un notificador por correo electrónico.

    Attributes:
        asunto: Asunto del correo.
    """

    def __init__(self, correo_destino: str, asunto: str) -> None:
        """
        Inicializa el notificador de correo.

        Args:
            correo_destino: Correo electrónico de destino.
            asunto: Asunto del mensaje.

        Raises:
            ValueError: Si el correo o el asunto son inválidos.
        """
        if "@" not in correo_destino:
            raise ValueError("El correo electrónico debe contener '@'.")

        if not asunto.strip():
            raise ValueError("El asunto del correo no puede estar vacío.")

        super().__init__(correo_destino)
        self.asunto = asunto.strip()

    def enviar(self, mensaje: str) -> bool:
        """
        Simula el envío de un correo electrónico.

        Args:
            mensaje: Mensaje a enviar.

        Returns:
            True si el mensaje es válido.
        """
        if not mensaje.strip():
            return False

        logging.info(
            "Correo enviado a %s con asunto '%s'.",
            self.destinatario,
            self.asunto,
        )
        return True

    def obtener_tipo(self) -> str:
        """
        Devuelve el tipo de notificador.

        Returns:
            Tipo de notificador.
        """
        return "Email"


class NotificadorSMS(Notificador):
    """
    Representa un notificador por SMS.

    Attributes:
        prefijo_pais: Prefijo telefónico del país.
    """

    def __init__(self, numero_telefono: str, prefijo_pais: str) -> None:
        """
        Inicializa el notificador SMS.

        Args:
            numero_telefono: Número telefónico de destino.
            prefijo_pais: Prefijo telefónico del país.

        Raises:
            ValueError: Si los datos telefónicos son inválidos.
        """
        numero_limpio = numero_telefono.replace(" ", "").replace("-", "")

        if not numero_limpio.isdigit():
            raise ValueError("El número telefónico solo debe contener dígitos.")

        if len(numero_limpio) < 10:
            raise ValueError("El número telefónico debe tener al menos 10 dígitos.")

        if not prefijo_pais.strip():
            raise ValueError("El prefijo de país no puede estar vacío.")

        super().__init__(numero_limpio)
        self.prefijo_pais = prefijo_pais.strip()

    def enviar(self, mensaje: str) -> bool:
        """
        Simula el envío de un SMS.

        Args:
            mensaje: Mensaje a enviar.

        Returns:
            True si el mensaje es válido y no supera 160 caracteres.
        """
        if not mensaje.strip():
            return False

        if len(mensaje) > 160:
            return False

        logging.info(
            "SMS enviado a %s%s.",
            self.prefijo_pais,
            self.destinatario,
        )
        return True

    def obtener_tipo(self) -> str:
        """
        Devuelve el tipo de notificador.

        Returns:
            Tipo de notificador.
        """
        return "SMS"


class NotificadorPush(Notificador):
    """
    Representa un notificador push para aplicación móvil.

    Attributes:
        app_nombre: Nombre de la aplicación.
    """

    def __init__(self, id_dispositivo: str, app_nombre: str) -> None:
        """
        Inicializa el notificador push.

        Args:
            id_dispositivo: Identificador del dispositivo.
            app_nombre: Nombre de la aplicación.

        Raises:
            ValueError: Si el dispositivo o la aplicación están vacíos.
        """
        if not id_dispositivo.strip():
            raise ValueError("El identificador del dispositivo no puede estar vacío.")

        if not app_nombre.strip():
            raise ValueError("El nombre de la aplicación no puede estar vacío.")

        super().__init__(id_dispositivo)
        self.app_nombre = app_nombre.strip()

    def enviar(self, mensaje: str) -> bool:
        """
        Simula el envío de una notificación push.

        Args:
            mensaje: Mensaje a enviar.

        Returns:
            True si el mensaje es válido.
        """
        if not mensaje.strip():
            return False

        logging.info(
            "Notificación push enviada al dispositivo %s desde %s.",
            self.destinatario,
            self.app_nombre,
        )
        return True

    def obtener_tipo(self) -> str:
        """
        Devuelve el tipo de notificador.

        Returns:
            Tipo de notificador.
        """
        return "Push"


@dataclass
class ResultadoEnvio:
    """
    Representa el resultado agregado del proceso de envío.

    Attributes:
        total_envios: Total de envíos procesados.
        envios_exitosos: Cantidad de envíos exitosos.
        envios_fallidos: Cantidad de envíos fallidos.
    """

    total_envios: int
    envios_exitosos: int
    envios_fallidos: int


def crear_notificador(registro: dict[str, Any]) -> Notificador:
    """
    Crea un notificador concreto a partir de un registro.

    Esta función implementa el patrón Factory Method, centralizando la
    creación de objetos según el canal indicado.

    Args:
        registro: Diccionario con los datos del notificador.

    Returns:
        Instancia concreta de Notificador.

    Raises:
        ValueError: Si el tipo de canal no es soportado.
        KeyError: Si faltan claves requeridas.
    """
    tipo = str(registro["tipo"]).lower().strip()

    if tipo == "email":
        return NotificadorEmail(
            correo_destino=str(registro["correo_destino"]),
            asunto=str(registro["asunto"]),
        )

    if tipo == "sms":
        return NotificadorSMS(
            numero_telefono=str(registro["numero_telefono"]),
            prefijo_pais=str(registro["prefijo_pais"]),
        )

    if tipo == "push":
        return NotificadorPush(
            id_dispositivo=str(registro["id_dispositivo"]),
            app_nombre=str(registro["app_nombre"]),
        )

    raise ValueError(f"Tipo de notificador no soportado: {tipo}")


def crear_notificadores_demo() -> list[Notificador]:
    """
    Crea una lista de notificadores de demostración.

    Returns:
        Lista de notificadores concretos creados mediante Factory Method.
    """
    registros = [
        {
            "tipo": "email",
            "correo_destino": "ana.torres@empresa.com",
            "asunto": "Aviso de nómina",
        },
        {
            "tipo": "email",
            "correo_destino": "luis.ramirez@empresa.com",
            "asunto": "Actualización de expediente",
        },
        {
            "tipo": "sms",
            "numero_telefono": "5512345678",
            "prefijo_pais": "+52",
        },
        {
            "tipo": "sms",
            "numero_telefono": "5587654321",
            "prefijo_pais": "+52",
        },
        {
            "tipo": "push",
            "id_dispositivo": "device-ABC-001",
            "app_nombre": "AppCorporativa",
        },
        {
            "tipo": "push",
            "id_dispositivo": "device-XYZ-002",
            "app_nombre": "AppCorporativa",
        },
    ]

    notificadores: list[Notificador] = []

    for registro in registros:
        notificadores.append(crear_notificador(registro))

    logging.info("Se crearon %d notificadores de demostración.", len(notificadores))
    return notificadores


def procesar_envios(notificadores: list[Notificador], mensajes: list[str]) -> ResultadoEnvio:
    """
    Procesa el envío de mensajes usando polimorfismo.

    Args:
        notificadores: Lista de notificadores disponibles.
        mensajes: Lista de mensajes a enviar.

    Returns:
        ResultadoEnvio con totales de éxito y fallo.

    Raises:
        ValueError: Si no existen notificadores o mensajes.
    """
    if not notificadores:
        raise ValueError("No existen notificadores para procesar.")

    if not mensajes:
        raise ValueError("No existen mensajes para enviar.")

    exitosos = 0
    fallidos = 0

    print("\\n" + "=" * 95)
    print("REPORTE DE NOTIFICACIONES - EJERCICIO3_POO")
    print("=" * 95)
    print(f"{'Canal':<15} | {'Destinatario':<25} | {'Mensaje':<35} | {'Estado':<10}")
    print("-" * 95)

    for indice, notificador in enumerate(notificadores):
        mensaje = mensajes[indice % len(mensajes)]
        estado = notificador.enviar(mensaje)

        if estado:
            exitosos += 1
        else:
            fallidos += 1

        print(notificador.generar_resumen(mensaje, estado))

    total_envios = exitosos + fallidos

    print("-" * 95)
    print(f"Total de envíos procesados : {total_envios}")
    print(f"Envíos exitosos            : {exitosos}")
    print(f"Envíos fallidos            : {fallidos}")
    print("=" * 95)

    return ResultadoEnvio(
        total_envios=total_envios,
        envios_exitosos=exitosos,
        envios_fallidos=fallidos,
    )


def probar_validacion_notificador() -> None:
    """
    Ejecuta una prueba controlada de validación de notificador inválido.

    Returns:
        None
    """
    try:
        crear_notificador(
            {
                "tipo": "email",
                "correo_destino": "correo_invalido",
                "asunto": "Prueba",
            }
        )
    except ValueError as error:
        logging.info("Prueba controlada de validación: %s", error)


def main() -> None:
    """
    Controla la ejecución principal del programa.

    Secuencia general:
        1. Configura logging.
        2. Crea notificadores mediante Factory Method.
        3. Procesa envíos usando polimorfismo.
        4. Imprime reporte en consola.
        5. Ejecuta una prueba controlada de validación.
        6. Maneja errores de ejecución.

    Returns:
        None
    """
    configurar_logging()

    try:
        logging.info("Inicio del programa Ejercicio3_POO.")

        notificadores = crear_notificadores_demo()
        mensajes = [
            "Su recibo está disponible.",
            "Se actualizó su información.",
            "Tiene una nueva alerta.",
        ]

        procesar_envios(notificadores, mensajes)
        probar_validacion_notificador()

        logging.info("Ejecución finalizada correctamente.")

    except (ValueError, KeyError) as error:
        logging.error("Error de validación o datos incompletos: %s", error)
        print(f"Error de validación o datos incompletos: {error}")

    except Exception as error:
        logging.exception("Error inesperado durante la ejecución.")
        print(f"Error inesperado: {error}")


if __name__ == "__main__":
    main()
