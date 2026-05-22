# POO_Decoradores_Python_Ejercicios

Programación Orientada a Objetos y Decoradores en Python

## 📋 Descripción General

Este conjunto de ejercicios desarrolla conceptos avanzados de:

* 🏗️ Programación Orientada a Objetos (POO)
* 🎯 Decoradores personalizados
* 📐 Programación estructurada en Python
* 🛡️ Manejo de excepciones
* 🪵 Logging y auditoría
* 🧪 Validación de datos
* 🧩 Modularización y buenas prácticas

Todos los ejercicios fueron desarrollados bajo principios de ingeniería de software orientados a:

* 📑 claridad estructural,
* ♻️ reutilización,
* 🔧 mantenibilidad,
* 🔍 trazabilidad,
* 📖 documentación técnica,
* ✂️ separación de responsabilidades.

---

## 🗂️ Estructura de los ejercicios

| Ejercicio | Tema Principal | Nivel |
| :--- | :--- | :--- |
| 📄 `Ejercicio1_POO.py` | 💼 Sistema de nómina con POO avanzada | 📈 Intermedio |
| 📄 `Ejercicio2_POO.py` | 📐 Figuras geométricas y polimorfismo | 📈 Intermedio |
| 📄 `Ejercicio3_POO.py` | 📣 Sistema de notificaciones con *Factory Method* | 🚀 Avanzado |
| 📄 `Ejercicio4_Decoradores.py` | ⏱️ Decorador para medición de tiempo | 📈 Intermedio |
| 📄 `Ejercicio5_Decoradores.py` | 🎛️ Decorador parametrizado de validación | 🚀 Avanzado |
| 📄 `Ejercicio6_Decoradores.py` | 🪵 Decorador de auditoría y *logging* | 🚀 Avanzado |

---

## 🛠️ Requisitos Técnicos

* **Versión recomendada:** 🐍 Python 3.11+
* **Bibliotecas utilizadas:** Todas pertenecen a la biblioteca estándar de Python:
  * `logging`
  * `abc`
  * `dataclasses`
  * `functools`
  * `typing`
  * `collections.abc`
  * `time`

⚠️ *No se requieren dependencias externas.*

---

## 🎓 Objetivos Académicos

Los ejercicios buscan demostrar dominio en:

### 🏗️ Programación Orientada a Objetos
* Clases y objetos
* Herencia
* Polimorfismo
* Encapsulación
* Abstracción
* Clases abstractas
* *Factory Method*
* Tipado estático con *type hints*

### 🎯 Decoradores
* Funciones como objetos de primera clase
* Funciones anidadas
* Clausuras (*closures*)
* Decoradores personalizados
* Decoradores parametrizados
* Uso de `*args` y `**kwargs`
* Uso de `functools.wraps`

### 📐 Programación estructurada
Todos los ejercicios incluyen:
* Modularización mediante funciones
* Secuencia clara de ejecución
* Selección (`if`/`elif`/`else`)
* Iteración (`for`/`while`)
* Manejo de excepciones
* *Logging*
* Reportes en consola
* *Docstrings* completos

---

## 🔍 Detalle de los Ejercicios

### 💼 Ejercicio 1 — Sistema de Nómina
* **Archivo:** `Ejercicio1_POO.py`
* **Propósito:** Modelar un sistema de empleados utilizando herencia, polimorfismo, encapsulación y clases abstractas.
* **Conceptos aplicados:**
  * Clase abstracta `Empleado`
  * Métodos abstractos
  * Subclases: Tiempo completo, Medio tiempo, Por horas
  * Polimorfismo en cálculo de pagos
  * Validaciones y *Logging*


### 📐 Ejercicio 2 — Figuras Geométricas

* **Archivo:** `Ejercicio2_POO.py`
* **Propósito:** Aplicar polimorfismo y abstracción en figuras geométricas.
* **Conceptos aplicados:**
* Clase abstracta `Figura`
* Métodos abstractos
* Herencia y sobrescritura
* Polimorfismo
* Cálculo de áreas


### 📣 Ejercicio 3 — Sistema de Notificaciones

* **Archivo:** `Ejercicio3_POO.py`
* **Propósito:** Simular un sistema multicanal de notificaciones usando POO avanzada.
* **Conceptos aplicados:**
* Clase abstracta `Notificador`
* Encapsulación con `@property`
* Herencia y polimorfismo
* *Factory Method*
* *Logging* y manejo de excepciones
* Validación de datos
* **Canales implementados:** 📧 Email, 📱 SMS, 🔔 Push notifications


### ⏱️ Ejercicio 4 — Decorador de Medición de Tiempo

* **Archivo:** `Ejercicio4_Decoradores.py`
* **Propósito:** Crear un decorador capaz de medir el tiempo de ejecución.
* **Conceptos aplicados:** Decoradores, *Wrapper functions*, `*args`, `kwargs`, `functools.wraps`, *Logging* y manejo de excepciones.
* **Funciones decoradas:** Cálculo de primos, Suma de rangos, Filtrado de pares.


### 🎛️ Ejercicio 5 — Decorador Parametrizado

* **Archivo:** `Ejercicio5_Decoradores.py`
* **Propósito:** Construir un decorador reutilizable para validación numérica.
* **Conceptos aplicados:** Decoradores parametrizados, Clausuras, Validación dinámica, `*args`, `kwargs`, *Type checking* y *Logging*.
* **Validaciones implementadas:** Rangos mínimos y máximos, Valores negativos, Valores booleanos, Restricción de cero.


### 🪵 Ejercicio 6 — Decorador de Auditoría

* **Archivo:** `Ejercicio6_Decoradores.py`
* **Propósito:** Implementar auditoría avanzada de funciones.
* **Conceptos aplicados:** Decoradores avanzados, *Logging* estructurado, Registro de argumentos, resultados, tiempos y errores, junto a un manejo robusto de excepciones.
* **Funciones auditadas:** Factorial, Conversión de temperatura, Análisis de texto.


---

## ⚙️ Características de Ingeniería Aplicadas

Todos los ejercicios incorporan de manera consistente:

* 🪵 **Logging:**
```python
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

```


* 📑 **Docstrings completos:** Cada función incluye propósito, parámetros, retorno y excepciones.
* 🏷️ **Tipado estático:** Uso consistente de `list[int]`, `dict[str, Any]`, `Callable[..., T]`.
* 🛡️ **Manejo de errores:** Uso estructural de bloques `try/except/raise`.

---

## 🚀 Ejecución Recomendada

Ejecutar individualmente cada módulo en la terminal:

```bash
python Ejercicio1_POO.py
python Ejercicio2_POO.py
python Ejercicio3_POO.py
python Ejercicio4_Decoradores.py
python Ejercicio5_Decoradores.py
python Ejercicio6_Decoradores.py

```

📊 **Resultados Esperados:** Cada programa imprime resultados en consola, registra eventos mediante *logging*, valida entradas de forma defensiva, captura errores controlados y muestra pruebas funcionales.

---

## 💎 Buenas Prácticas Aplicadas

* ✂️ Separación de responsabilidades
* 🧩 Diseño modular
* ♻️ Reutilización de código
* 🔗 Bajo acoplamiento y alta cohesión
* 🛡️ Validación defensiva
* 📐 Programación estructurada
* 📖 Documentación técnica

---

## 👨‍💻 Autor

**Antonio Nicolás Toro González** 🎓 *Maestría en Inteligencia Artificial para la Transformación Digital* 🏫 Instituto Internacional de Aguascalientes

👨‍🏫 **Tutor Académico:** Dr. Jonás Velasco Álvarez

### 📜 Licencia Académica

Material desarrollado con fines educativos y de formación avanzada en: Python, Programación Orientada a Objetos, Decoradores, Ingeniería de Software, Ciencia de Datos e Inteligencia Artificial.

```

```
