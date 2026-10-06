# Proyecto final - Búsqueda de productos con MCP

Servidor local para buscar, analizar y comparar productos de Amazon Reviews 2023. Usa los 600 productos y 6,992 reseñas de Electronics proporcionados por el profesor.

## Qué hace

- `search_products(query, top_k=5)` busca por similitud semántica.
- `analyze_product(product_id)` calcula conteos, proporciones, media y mediana de las reseñas seleccionadas.
- `compare_products(product_ids)` compara dos o más productos y toma el primero como referencia.

La búsqueda representa cada producto con dos fuentes: 50 % del texto del catálogo y 50 % del promedio de sus reseñas. Cada parte se normaliza antes de combinarla y el resultado se normaliza otra vez. El modelo es `sentence-transformers/all-MiniLM-L6-v2` y se carga desde `config.json`.

## Preparación

Se necesita Python 3.12 y `uv`.

```bash
uv sync --locked
```

La primera ejecución descarga el modelo. Los pesos quedan en la caché del equipo y no forman parte de la entrega.

## Ejecutar

En una terminal, desde esta carpeta:

```bash
uv run --locked python server.py
```

El servidor queda disponible en `http://127.0.0.1:8000/mcp`. En otra terminal:

```bash
uv run --locked python main.py
```

El cliente descubre las tres herramientas y ejecuta búsquedas, análisis, comparación, un producto desconocido y un caso inválido. La llamada posterior al error comprueba que la conexión sigue funcionando.

## Comprobaciones

```bash
uv run --locked python -m pytest
uv run --locked mypy --strict server.py client.py main.py support tests
uv run --locked ruff check server.py client.py main.py support tests
uv run --locked ruff format --check server.py client.py main.py support tests
```

Resultado verificado: **11 pruebas aprobadas**, Ruff sin observaciones y mypy estricto sin errores.

## Resultados observados

Consulta: `A portable waterproof Bluetooth speaker`

1. Altec Lansing Mini H2O (`B0B786PFYJ`), similitud 0.7942.
2. EDUPLINK Waterproof Portable Bluetooth Speaker (`B0BNY1L4JP`), similitud 0.7896.
3. Bose SoundLink Micro (`B09WWG19YS`), similitud 0.7580.

Los tres resultados mencionan explícitamente portabilidad, Bluetooth y resistencia al agua. Es una coincidencia coherente con la intención de la consulta, pero la puntuación expresa cercanía entre vectores: no es una probabilidad ni una calificación de calidad.

Consulta: `Comfortable headphones with good sound`

1. Sony MDR7506 (`B07CQMZVZ6`), similitud 0.7294.
2. OneOdio Over Ear Headphone (`B091K4WYD1`), similitud 0.7166.

Aquí se recuperan audífonos aunque los títulos no contengan todas las palabras de la consulta. La representación combinada permite aprovechar también lo expresado en las reseñas.

Como ejemplo de análisis, el JBL Charge 5 (`B0BCTJMN63`) tiene siete reseñas seleccionadas: tres de cuatro estrellas y cuatro de cinco, con media 4.5714 y mediana 5. Al compararlo con el JBL Flip 5 (`B09MMWM2Y8`), la media del segundo es 0.2214 puntos menor.

## Alcance y limitaciones

- Los conteos describen únicamente las reseñas incluidas; el máximo de 30 por producto impide usarlos como medida de popularidad en Amazon.
- La selección es por conveniencia y no representa toda la categoría Electronics.
- El modelo está orientado al inglés y trunca textos largos a 256 tokens de su tokenizador.
- `top_k` siempre devuelve los productos más cercanos disponibles, aun cuando una consulta sea poco pertinente.

## Organización

- `server.py`: servidor MCP y registro de herramientas.
- `client.py` y `main.py`: demostración HTTP.
- `support/data.py`: lectura y validación de los archivos comprimidos.
- `support/encoder.py`: adaptación del modelo de embeddings.
- `support/search.py`: combinación de vectores, búsqueda y estadísticas.
- `tests/`: pruebas con un codificador pequeño y comprobaciones del dataset real.
- `preparacion_datos.ipynb`: exploración proporcionada por el profesor.
- `DATASET.md`, `GUIA.md` y `MCP_HTTP.md`: material oficial de referencia.

## Estado de la entrega

- [x] Datos y configuración incluidos.
- [x] Embeddings combinados en proporción 50/50.
- [x] Tres herramientas disponibles por Streamable HTTP.
- [x] Entradas inválidas y productos desconocidos controlados.
- [x] Pruebas, Ruff y mypy estricto aprobados.
- [x] Cliente HTTP probado contra el servidor local.
- [ ] Envío al formulario; no realizado.
