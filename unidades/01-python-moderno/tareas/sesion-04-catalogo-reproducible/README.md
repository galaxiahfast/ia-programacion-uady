# Catálogo de cursos reproducible con MCP

Proyecto de la sesión 4 con los nueve ejercicios resueltos: cinco sobre la aplicación y cuatro sobre calidad. La misma búsqueda se puede usar desde la terminal o como herramienta MCP local.

## Preparación

```bash
uv sync --locked
```

El proyecto se verificó con Python 3.12.3. No se incluye `.venv`: uv la reconstruye usando `pyproject.toml`, `uv.lock` y `.python-version`.

## Uso

Consulta directa:

```bash
uv run --locked python main.py python
uv run --locked python main.py astronomy
uv run --locked python main.py python --catalog data/extra_courses.json
```

Consulta por MCP:

```bash
uv run --locked python client.py python
uv run --locked python client.py astronomy
uv run --locked python client.py " "
```

El cliente inicia y detiene `server.py`; no hace falta abrir el servidor en otra terminal.

## Ejercicios de aplicación

### 1. Punto de entrada

`python -c "import main"` no consulta el catálogo porque al importar un archivo su `__name__` no es `"__main__"`. La misma condición al final de `server.py` impide iniciar el transporte durante el import.

El decorador `@mcp.tool()` registra `find_courses` al importar el módulo. Registrar la función solo la deja disponible para el servidor; `mcp.run(transport="stdio")` es la llamada que inicia el transporte.

### 2. Datos y argumentos

`data/extra_courses.json` agrega `PY03`, **Practical Python automation**. La consulta con `--catalog` devuelve `PY01`, `PY02` y `PY03` y termina con código 0. Una ruta inexistente termina con código 1 y no escribe resultados en stdout.

El servidor MCP conserva `data/courses.json` como catálogo predeterminado.

### 3. Niveles y destinos

- DEBUG muestra la ruta leída y el resumen de la búsqueda.
- INFO muestra solo el resumen.
- ERROR no muestra mensajes durante una consulta exitosa.

Con `--log-level ERROR --log-file logs/app.log`, la consola filtra DEBUG e INFO, pero el archivo los conserva porque su handler acepta mensajes desde DEBUG. Los resultados JSON salen por stdout y el logging usa stderr. Esto es indispensable en `server.py`, donde stdout pertenece al protocolo MCP.

### 4. Diagnóstico

El mensaje INFO ahora incluye coincidencias y total de cursos leídos:

```text
INFO | catalog.search | Search completed: 2 of 3 courses matched
```

La consulta directa y la herramienta MCP siguen devolviendo `PY01` y `PY02` para `python`.

### 5. Reproducción y llamada MCP

La herramienta descubierta es `find_courses`. Resultados comprobados:

| Consulta | Resultado | Código |
| --- | --- | ---: |
| `python` | `PY01` y `PY02` | 0 |
| `astronomy` | lista vacía válida | 0 |
| espacios | respuesta MCP con `is_error: true` | 1 |

Una lista vacía significa que la búsqueda fue válida pero no encontró coincidencias. La consulta en blanco es un error de entrada.

`pyproject.toml` declara el proyecto y las dependencias; `uv.lock` fija la resolución completa; `.python-version` selecciona Python 3.12. `.venv` no se entrega porque depende del equipo y se reconstruye con uv.

## Ejercicios de calidad

Se agregaron estas pruebas:

- un curso con horas negativas debe ser rechazado;
- una ejecución de consola con catálogo inexistente debe salir con código 1 y stdout vacío.

También se introdujo temporalmente un `import json` sin usar. Ruff señaló `F401`; después de quitarlo, el proyecto volvió a pasar completo.

```bash
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked mypy --strict main.py server.py client.py catalog
uv run --locked python -m pytest
```

Resultado final:

```text
All checks passed!
10 files already formatted
Success: no issues found in 6 source files
8 passed
```

Desde una copia limpia también se ejecutaron `uv sync --locked`, el cliente MCP y las cuatro comprobaciones. Todos terminaron con código 0.

## Estado

**Resuelto y verificado; no enviado al formulario.**
