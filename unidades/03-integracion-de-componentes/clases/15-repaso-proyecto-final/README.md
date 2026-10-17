# Clase 15 - Repaso del proyecto final

Esta clase corresponde al 16 de octubre. Los temas del curso ya habían terminado, por lo que se dedicó el inicio a repasar el proyecto final y el resto a preguntas generales sobre agentes, herramientas y trabajo profesional con IA.

## Minutos que revisaría

- `00:08 a 04:30`: objetivo, estructura del proyecto, archivos que deben incluirse y dependencias.
- `04:30 a 08:15`: creación y combinación de embeddings de productos y reseñas.
- `08:15 a 12:20`: servidor MCP, sus tres herramientas y cliente de demostración.
- `12:37 a 18:20`: fecha, formato de entrega, criterios de evaluación y entradas inválidas.
- `19:20 a 33:30`: conversación opcional sobre ideas de portafolio y flujos de trabajo con agentes.

## Requisitos confirmados

El entregable es un archivo comprimido con el proyecto completo. Debe poder instalarse con `uv`, incluir `pyproject.toml`, `uv.lock`, configuración, datos, código y un README que explique cómo ejecutarlo.

Las tres herramientas obligatorias son:

- `search_products`, con búsqueda semántica mediante embeddings;
- `analyze_product`, para resumir un producto y sus reseñas;
- `compare_products`, para comparar dos o más productos.

La representación de búsqueda combina 50 % del vector del catálogo y 50 % del promedio de las reseñas. También deben controlarse casos como una consulta vacía, `top_k=0` o un producto inexistente.

Los ejemplos pueden mostrarse con capturas o con el texto de salida; las capturas no son obligatorias. La interpretación de resultados se escribe en lenguaje normal dentro del README.

## Evaluación y fechas

Lo más importante es que el proyecto sea reproducible, que las tres herramientas funcionen y que la búsqueda use embeddings. También se revisarán las anotaciones de tipo con mypy, aunque tienen menor peso.

- Unidades 2 y 3: **19 de octubre de 2026 al final del día**.
- Proyecto final: **26 de octubre de 2026 al final del día**.

No hubo cambios respecto de las fechas ya registradas.

## Estado del proyecto

No se asignó una actividad nueva. El [proyecto integrador](../../../../proyecto-integrador/) ya cumple los requisitos mencionados. Después de esta clase se verificó nuevamente: 11 pruebas aprobadas, mypy estricto sin errores y Ruff sin observaciones. Continúa pendiente de envío.
