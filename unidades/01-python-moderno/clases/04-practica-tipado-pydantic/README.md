# Clase 4 - Práctica de tipado y Pydantic

La grabación dura cerca de 2 horas. Esta clase lleva a la práctica lo que se explicó al final de la clase anterior.

## Minutos que revisaría

- `00:20 a 09:57`: preparación de la notebook, objetivos y ejecución de mypy desde Python.
- `09:57 a 15:15`: ejercicio 1 sobre anotaciones sin cambiar el comportamiento.
- `15:15 a 26:57`: contratos de funciones, valores opcionales y corrección de errores de mypy.
- `26:57 a 44:30`: diferencias entre `list`, `Iterable`, `Any` y `object`.
- `45:11 a 1:03:19`: primeros modelos de Pydantic, modo estricto, `Field`, `Literal` y campos extra.
- `1:11:22 a 1:21:17`: normalización con `field_validator`.
- `1:21:17 a 1:37:36`: decoradores, métodos de clase y configuración de los modelos.
- `1:37:36 a 1:49:29`: ejercicios 4 y 5, casos límite y configuración antes de procesar.
- `1:49:41 a 1:54:37`: `EmailStr`, `SecretStr`, exclusión de contraseñas y roles con `Literal`.
- `1:54:56 a 1:56:06`: indicaciones sobre lo que falta en la notebook y el módulo `.py`.

## mypy y anotaciones

Las anotaciones no cambian cómo se ejecuta Python. mypy las lee para encontrar inconsistencias antes de correr el programa.

En la notebook se ejecuta mypy mediante su API, aunque normalmente se utiliza desde la terminal. El resultado incluye mensajes y un código de salida: cero significa que no encontró errores.

### Tipos de colecciones

Conviene pedir el tipo más general que realmente necesita una función:

- `list[float]` permite operaciones propias de una lista, como acceder por índice.
- `Iterable[float]` acepta listas, tuplas, conjuntos y otros objetos recorribles, pero no garantiza longitud ni acceso por índice.

### `Any` y `object`

- `Any` hace que mypy deje pasar prácticamente cualquier operación.
- `object` acepta cualquier objeto como entrada, pero obliga a comprobar su tipo antes de usar operaciones específicas.

`object` conserva más seguridad; `Any` es útil cuando de verdad no se conoce la forma del dato, pero puede esconder errores.

## Modelos de Pydantic

Un modelo hereda de `BaseModel` y declara sus campos mediante anotaciones. `model_validate` recibe los datos y devuelve una instancia válida o genera `ValidationError`.

Pydantic puede convertir valores compatibles. Por ejemplo, el texto `"0.9"` puede convertirse a `float`. Si no se quieren conversiones automáticas se utiliza validación estricta.

Herramientas vistas:

- `Field`: agrega restricciones como mínimo, máximo o longitud.
- `Literal`: limita un campo a un conjunto de valores conocidos.
- `ConfigDict(extra="forbid")`: rechaza claves que no pertenecen al modelo.
- `validate_assignment`: vuelve a validar cuando se modifica un atributo.
- `field_validator`: permite normalizar o validar un campo con reglas propias.

## Normalización

El ejemplo limpia espacios y convierte textos a minúsculas antes de aplicar el resto de las validaciones. Esto permite aceptar entradas como `" Positivo "` y almacenarlas de forma consistente.

El validador recibe `object` porque se ejecuta antes de conocer el tipo definitivo. Primero comprueba si el valor es una cadena y luego la normaliza.

La entrada original no debe modificarse. Pydantic construye un nuevo objeto con los datos ya validados.

## Datos sensibles y serialización

- `EmailStr` verifica el formato de un correo.
- `SecretStr` evita mostrar directamente una contraseña.
- `exclude=True` impide incluir un campo al serializar.
- `model_dump` produce un diccionario y `model_dump_json` produce JSON.

El profesor comentó que este tipo de validación se usa en APIs, configuraciones de entrenamiento y respuestas estructuradas de modelos de lenguaje.

## Ejercicios y estado

Durante la clase se trabajaron en pantalla los primeros cinco ejercicios:

1. Anotar `select_scores` sin cambiar su comportamiento.
2. Corregir un contrato y conseguir que mypy termine sin errores.
3. Diferenciar campos ausentes, nulos e inválidos.
4. Detectar espacios, booleanos, `nan` y valores fuera de rango.
5. Validar la configuración antes de procesar un lote.

Quedaron para continuar:

6. Serializar y reconstruir un reporte.
7. Comprobar lotes vacíos, rechazados y mayores al máximo.
8. Crear `count_labels`, ejecutar mypy y generar el reporte JSON.

Los ocho ejercicios quedaron resueltos posteriormente en la [carpeta de la tarea](../../tareas/sesion-02-tipado-pydantic/).

## Lo que no fue tarea

Al terminar, un alumno pidió una idea adicional para practicar. El profesor sugirió investigar FastAPI y Model Context Protocol. Fue una recomendación individual y opcional, no parte de la entrega de la sesión.

## Materiales

- [Notebook en Colab](https://colab.research.google.com/drive/1iVbFAxw1VvEI4aB-9CsQUfdbp8QzPZSR)
- [Carpeta oficial de la sesión](https://github.com/oscarnavmac/programacion_ai/tree/main/unidad-01-python-moderno/sesion-02-tipado-pydantic)
- [Instrucciones de la práctica](https://github.com/oscarnavmac/programacion_ai/blob/main/unidad-01-python-moderno/sesion-02-tipado-pydantic/PRACTICA.md)
