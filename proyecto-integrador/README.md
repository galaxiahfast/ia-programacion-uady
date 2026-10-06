# Proyecto final - Buscador semántico de productos

La consigna definitiva del curso es construir un servidor MCP que permita buscar, analizar y comparar productos de Amazon mediante embeddings.

## Alcance confirmado

- Datos: Amazon Reviews 2023, categoría Electronics.
- Muestra preparada: 600 productos y 6,992 reseñas.
- Modelo: `sentence-transformers/all-MiniLM-L6-v2`.
- Transporte: MCP Streamable HTTP en `http://127.0.0.1:8000/mcp`.
- Fecha límite: **19 de octubre de 2026**.

El servidor tendrá las herramientas `search_products`, `analyze_product` y `compare_products`. El código debe ser modular, tener pruebas, pasar mypy en modo estricto y explicar instalación, uso y limitaciones.

Los archivos de trabajo se incorporarán en esta carpeta conforme se resuelva la consigna oficial. No se enviará nada al formulario sin autorización.

## Estado

- [x] Consigna y datos identificados.
- [ ] Notebook oficial ejecutada y entendida.
- [ ] Lógica separada en módulos.
- [ ] Servidor MCP y cliente HTTP funcionando.
- [ ] Pruebas, Ruff y mypy aprobados.
- [ ] Documentación y demostración terminadas.

## Referencia

- [Consigna oficial](https://github.com/oscarnavmac/programacion_ai/tree/main/proyecto-final)
