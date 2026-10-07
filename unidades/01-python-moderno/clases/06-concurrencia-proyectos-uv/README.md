# Clase 6 - Concurrencia y proyectos reproducibles con uv

La clase dura cerca de 1 hora con 56 minutos. Primero termina la práctica de concurrencia y después presenta la última sesión de la Unidad 1: cómo organizar un proyecto que otra persona pueda instalar y ejecutar.

## Minutos que revisaría

- `00:30 a 06:18`: repaso de `async`, `await`, `gather` y `TaskGroup`.
- `06:18 a 10:35`: ejercicio 3, dos lecturas concurrentes con distinta duración.
- `11:03 a 19:48`: timeouts, cancelación, limpieza con `finally` y ejercicio 4.
- `20:44 a 30:45`: qué hace reproducible a un proyecto y para qué sirve uv.
- `30:45 a 43:08`: `pyproject.toml`, `uv.lock`, `.python-version`, `.venv` y comandos principales.
- `43:13 a 59:35`: creación de un proyecto con `uv init` y primera ejecución.
- `1:00:00 a 1:35:00`: recorrido del catálogo de cursos y reproducción del entorno.
- `1:35:00 a 1:52:00`: dependencias, servidor MCP local y archivos que se entregan.
- `1:52:00 a 1:55:30`: aclaración de las cuatro prácticas y del formulario de la Unidad 1.

## Cierre de concurrencia

En el ejercicio 3 se crean dos tareas dentro de un `TaskGroup`. Las dos comienzan sin esperar a que termine la otra. La lectura `west`, que espera un segundo, termina antes que `north`, que espera tres; aun así se conservan ambos resultados.

`TaskGroup` espera todas las tareas al salir del bloque. Si una falla, cancela las que siguen activas y agrupa los errores. Esto da una estructura más clara que crear tareas sueltas.

En el ejercicio 4, `asyncio.timeout` limita el tiempo disponible. Cuando se vence, cancela la corrutina que estaba esperando y produce `TimeoutError`. El bloque `finally` se ejecuta incluso durante la cancelación, por lo que ahí debe colocarse la limpieza de recursos. Con un límite de un segundo una espera de tres se cancela; con un límite de tres segundos una espera de uno termina normalmente.

## Proyectos reproducibles con uv

La idea de reproducibilidad es que otra persona pueda obtener el proyecto, reconstruir su entorno y ejecutar los mismos comandos. Los archivos principales son:

- `pyproject.toml`: describe el proyecto, la versión de Python y sus dependencias.
- `uv.lock`: fija las versiones exactas resueltas, incluidas las dependencias indirectas.
- `.python-version`: indica la versión de Python elegida para trabajar.
- `.venv`: es el entorno local generado; no se entrega porque se reconstruye.

Comandos importantes de la clase:

```bash
uv init --no-package --python 3.13 --vcs none course-catalog
uv add "pydantic>=2,<3"
uv add "mcp>=2,<3"
uv tree
uv lock
uv sync --locked
uv run --locked python main.py python
```

`uv add` modifica la declaración y el lockfile. `uv sync --locked` reconstruye el entorno sin permitir que cambie la resolución. `uv run` ejecuta dentro del entorno administrado por uv; no hace falta activar `.venv` manualmente.

## Catálogo y servidor MCP

El proyecto de la sesión empieza como una función que busca cursos en un JSON. Después separa responsabilidades:

- `catalog/search.py` contiene el modelo y la búsqueda;
- `main.py` recibe argumentos y muestra resultados;
- `server.py` publica la búsqueda como herramienta MCP por stdio;
- `client.py` inicia el servidor, descubre la herramienta y la invoca;
- `tests/` comprueba la búsqueda y la comunicación real.

Importar `main.py` no ejecuta la consulta gracias a `if __name__ == "__main__"`. De la misma manera, importar `server.py` registra la herramienta, pero no inicia el transporte. Mientras el servidor usa stdio, stdout queda reservado para el protocolo y los diagnósticos deben ir a stderr mediante logging.

## Tareas detectadas

La entrega de la Unidad 1 reúne cuatro trabajos:

1. Notebooks de curso acelerado y Zen de Python.
2. Notebook, módulo y reporte JSON de tipado y Pydantic.
3. Notebook con cuatro ejercicios de iteración, archivos y concurrencia.
4. Proyecto reproducible del catálogo: cinco ejercicios de aplicación y cuatro de calidad.

La fecha actualizada es el **12 de octubre de 2026**. Los cuatro trabajos quedaron resueltos y comprobados en este repositorio, pero **no se ha enviado nada al formulario**. La entrega formal queda a cargo del alumno.

## Materiales

- [Sesión 4 en el repositorio oficial](https://github.com/oscarnavmac/programacion_ai/tree/main/unidad-01-python-moderno/sesion-04-reproducibilidad)
- [Práctica del catálogo](https://github.com/oscarnavmac/programacion_ai/blob/main/unidad-01-python-moderno/sesion-04-reproducibilidad/PRACTICA.md)
- [Bloque de calidad](https://github.com/oscarnavmac/programacion_ai/blob/main/unidad-01-python-moderno/sesion-04-reproducibilidad/CALIDAD.md)
- [Presentación](https://drive.google.com/file/d/1L7z6CxmTSq6CT-fPHlxq593WCAa2HRcI/view?usp=drivesdk)

