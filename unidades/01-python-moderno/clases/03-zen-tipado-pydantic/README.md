# Clase 3 - Zen de Python, tipado y Pydantic

La grabación dura aproximadamente 1 hora con 50 minutos. La primera hora termina la notebook del Zen y el resto introduce anotaciones de tipo, mypy y Pydantic.

## Minutos que revisaría

- `03:12 a 18:00`: primeras reglas del Zen: claridad, código explícito y diferencia entre complejo y complicado.
- `20:33 a 30:20`: evitar demasiada anidación, mantener el código espaciado y priorizar legibilidad.
- `33:59 a 44:36`: manejo visible de errores, entradas ambiguas y espacios de nombres.
- `45:01 a 1:03:06`: explicación y solución del ejercicio de refactorización del Zen.
- `1:03:48 a 1:17:16`: PEP, historia de los type hints y sintaxis moderna de anotaciones.
- `1:17:16 a 1:23:43`: diferencia entre las anotaciones, mypy y la validación durante la ejecución.
- `1:23:43 a 1:41:15`: modelos de Pydantic, conversiones y `ValidationError`.
- `1:42:54 a 1:50:02`: ejemplos reales, restricciones con `Field` y uso de modelos en funciones y APIs.

## Zen de Python

No son reglas obligatorias ni optimizaciones de rendimiento. Son criterios para escribir código que otra persona pueda leer y mantener.

Las ideas que más se repitieron fueron:

- usar nombres que expliquen para qué sirve cada dato;
- hacer visibles las decisiones importantes;
- preferir una solución simple cuando resuelva bien el problema;
- aceptar la complejidad necesaria, pero evitar código innecesariamente complicado;
- reducir bloques anidados cuando una salida temprana deja el flujo más claro;
- no esconder errores con un `except` demasiado amplio;
- no adivinar cuando una entrada puede interpretarse de varias formas;
- conservar el nombre del módulo en llamadas como `math.sqrt` cuando ayuda a reconocer de dónde viene la función.

## Ejercicio del Zen

La tarea mostrada cerca del minuto `45:01` consiste en refactorizar una función con nombres poco claros, mucha anidación y un `except Exception` que oculta cualquier error.

El comportamiento no debe cambiar: recibe registros, acepta scores convertibles a números no negativos y devuelve el promedio o `None` si no hay valores válidos.

Este ejercicio ya está resuelto en la [notebook del Zen](../../tareas/sesion-01-curso-acelerado/u1_n2_zen_de_python.ipynb), pero todavía no se ha enviado.

## Anotaciones de tipo

Python sigue siendo un lenguaje de tipado dinámico. Escribir `precio: float` o indicar el retorno de una función no obliga a Python a respetar ese tipo durante la ejecución.

Las anotaciones sirven principalmente como documentación y permiten que herramientas como mypy detecten usos incompatibles antes de ejecutar el programa.

Ejemplos de sintaxis moderna:

```python
precio: float = 19.5
descuento: float | None = None

def saludar(nombre: str) -> str:
    return f"Hola, {nombre}"
```

## Diferencia entre mypy y Pydantic

- **mypy** revisa estáticamente las anotaciones. No ejecuta el programa ni valida datos que llegan desde fuera.
- **Pydantic** valida datos durante la ejecución y crea un objeto solamente cuando cumple el modelo.
- Si los datos no son válidos, Pydantic genera un `ValidationError`.
- `try` y `except` no realizan la validación; sirven para decidir qué hacer después de que ocurre el error.

Pydantic puede convertir algunos valores compatibles, como un texto numérico a `float`. Si se necesita evitar conversiones, se puede usar validación estricta.

También permite agregar reglas con `Field`, validar correos, restringir valores con `Literal` y construir modelos anidados. Esto resulta útil para APIs, respuestas de modelos de lenguaje y datos que vienen de archivos o bases de datos.

## Pendientes registrados

No los voy a resolver todavía; quedan guardados para revisarlos al final:

- [x] Refactorización del Zen de Python. Resuelta, no enviada.
- [ ] Ocho ejercicios de la notebook de tipado y Pydantic.
- [ ] Módulo `.py` con `count_labels` y comprobación de mypy sin errores.
- [ ] Reporte JSON del ejercicio 8 y comprobación de que puede reconstruirse.

## Materiales

- [Notebook de tipado y Pydantic en Colab](https://colab.research.google.com/drive/1iVbFAxw1VvEI4aB-9CsQUfdbp8QzPZSR)
- [Carpeta oficial de la sesión](https://github.com/oscarnavmac/programacion_ai/tree/main/unidad-01-python-moderno/sesion-02-tipado-pydantic)
- [Instrucciones de la práctica](https://github.com/oscarnavmac/programacion_ai/blob/main/unidad-01-python-moderno/sesion-02-tipado-pydantic/PRACTICA.md)
- [Presentación](https://drive.google.com/file/d/1_2Bp0DOJYRTTAVd6tD1gruzsVrnT5Bru/view?usp=drivesdk)
