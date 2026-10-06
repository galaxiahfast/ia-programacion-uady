# Clase 5 - Cierre de Pydantic, generadores y concurrencia

La grabación dura cerca de 2 horas. Primero termina la práctica de Pydantic y después comienza la notebook de iteración, recursos y concurrencia.

## Minutos que revisaría

- `00:05 a 02:36`: explicación de dónde están las tareas, qué se entrega y dónde aparece la fecha límite.
- `02:36 a 11:45`: creación de `lesson_models.py`, modelos reutilizables y comprobación con mypy.
- `11:45 a 24:17`: ejercicios 7 y 8 de Pydantic; el ejercicio 8 queda como actividad independiente.
- `24:17 a 37:40`: ejemplo de FastAPI usando modelos de Pydantic para validar peticiones y respuestas.
- `37:53 a 49:51`: introducción a iterables, iteradores, generadores y context managers.
- `50:07 a 1:21:45`: práctica detallada de `iter`, `next`, expresiones generadoras y `yield`.
- `1:26:25 a 1:40:48`: archivos con `with`, cierre aun cuando ocurre un error y creación de context managers.
- `1:41:15 a 1:48:15`: concurrencia, corrutinas, `async`, `await`, `TaskGroup` y tiempos límite.
- `1:48:15 a 2:00:01`: `to_thread`, tareas en segundo plano, `gather` y comportamiento de `TaskGroup` cuando falla una tarea.

## Cierre de la práctica de Pydantic

El profesor aclaró que las tareas se describen en el `PRACTICA.md` de cada sesión y se suben mediante el formulario indicado en la unidad.

La notebook puede generar `lesson_models.py` usando `%%writefile`. Este módulo contiene los modelos de Pydantic y permite:

- reutilizarlos fuera de la notebook;
- ejecutar `mypy --strict` sobre código real;
- importar los modelos desde otras aplicaciones;
- separar la definición de datos de las pruebas y ejemplos.

Se repasó el ejercicio 7, que comprueba el procesamiento de lotes y casos límite. El ejercicio 8 queda del lado del alumno: agregar `count_labels`, comprobarlo con mypy y conservar un reporte JSON que pueda reconstruirse.

### FastAPI

La demostración muestra que un modelo de Pydantic puede utilizarse como entrada de una ruta. FastAPI recibe JSON, lo valida y solo llama a la función cuando los datos cumplen el modelo. También puede validarse el modelo de respuesta.

## Iterable, iterador y generador

- Un **iterable** es un objeto que se puede recorrer, como una lista, tupla o conjunto.
- Un **iterador** conserva la posición del recorrido y entrega un elemento cada vez mediante `next`.
- `iter(objeto)` crea un iterador a partir de un iterable.
- Un **generador** es un tipo de iterador producido por una función con `yield` o por una expresión generadora.

Cada iterador conserva su propia posición. Cuando se agota produce `StopIteration`; para volver a empezar hay que crear uno nuevo.

### Por qué usar generadores

Una lista guarda todos sus elementos en memoria. Un generador calcula cada valor cuando se solicita, por lo que es útil para archivos, secuencias grandes o resultados que se consumen poco a poco.

`yield` se parece a `return`, pero conserva el punto en el que quedó la función. La siguiente llamada continúa desde ahí.

## Context managers

`with` delimita el tiempo durante el que se utiliza un recurso. Al salir del bloque se ejecuta la limpieza correspondiente, incluso si ocurrió un error.

El ejemplo principal es un archivo: se abre dentro del bloque y queda cerrado al salir. También aplica a conexiones, directorios temporales, sesiones y otros recursos.

Es posible crear un context manager con `@contextmanager`, `yield` y un bloque `try/finally`. Lo que está antes de `yield` prepara el recurso y lo que está en `finally` lo libera.

## Concurrencia con asyncio

La concurrencia permite avanzar en otra tarea mientras una operación espera entrada o salida. No es lo mismo que ejecutar cálculos en paralelo.

- `async def` define una corrutina.
- `await` espera un resultado sin bloquear innecesariamente el event loop.
- `create_task` inicia una corrutina como tarea.
- `TaskGroup` administra varias tareas y espera que terminen al salir del bloque.
- `asyncio.timeout` limita cuánto se puede esperar.
- `asyncio.to_thread` permite llamar una función síncrona sin bloquear el event loop.
- `gather` espera varias corrutinas y conserva sus resultados.

En una notebook se puede usar `await` directamente porque Jupyter ya tiene un event loop. En un archivo `.py` normalmente se utiliza `asyncio.run(main())`.

## Tareas detectadas

### Pydantic

En esta clase se explicaron los ejercicios 7 y 8; el octavo fue indicado expresamente como trabajo independiente. La práctica completa quedó resuelta posteriormente en la [carpeta de la tarea](../../tareas/sesion-02-tipado-pydantic/).

### Iteración, recursos y concurrencia

La nueva notebook contiene cuatro ejercicios:

1. Crear `even_numbers(stop)` con `yield`.
2. Comprobar el cierre de un archivo, incluso cuando ocurre `ValueError`.
3. Ejecutar dos lecturas concurrentes mediante `TaskGroup`.
4. Comprobar la limpieza de una corrutina cancelada por un timeout.

En esta grabación se explican los ejercicios 1 y 2. La parte de concurrencia continúa en la siguiente clase. Los cuatro ejercicios quedaron resueltos posteriormente en la [carpeta de la tarea](../../tareas/sesion-03-iteracion-recursos-concurrencia/).

## Materiales

- [Notebook de iteración, recursos y concurrencia en Colab](https://colab.research.google.com/drive/1HKRCn91Q5ZGxFq--79Xwow3G692LyyuM)
- [Carpeta oficial de la sesión](https://github.com/oscarnavmac/programacion_ai/tree/main/unidad-01-python-moderno/sesion-03-iteracion-recursos-concurrencia)
- [Instrucciones de la práctica](https://github.com/oscarnavmac/programacion_ai/blob/main/unidad-01-python-moderno/sesion-03-iteracion-recursos-concurrencia/PRACTICA.md)
- [Presentación](https://drive.google.com/file/d/1gMZ1HGejLwIAsZf80W7OjOz9Ktkw5Arz/view?usp=drivesdk)
