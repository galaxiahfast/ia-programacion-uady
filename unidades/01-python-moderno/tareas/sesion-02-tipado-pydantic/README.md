# Sesión 2 - Tipado y Pydantic

Práctica resuelta a partir de la notebook oficial. Contiene los ocho ejercicios, el módulo reutilizable y el reporte JSON solicitado.

## Archivos

- `u1_n3_tipado_pydantic.ipynb`: notebook completa y ejecutada.
- `lesson_models.py`: modelos, procesamiento de lotes y `count_labels`.
- `reporte_ejercicio_8.json`: reporte serializado y reconstruido en el ejercicio 8.
- `requirements.txt`: versiones indicadas en el material del profesor.

## Comprobaciones realizadas

La notebook se ejecutó completa con Python 3.12.3. Sus 36 celdas de código terminaron sin errores.

```text
code_cells=36 executed=36 errors=0
accepted=2 issues=4
```

El módulo también pasó el análisis estático solicitado:

```bash
python -m mypy --strict lesson_models.py
```

```text
Success: no issues found in 1 source file
```

La notebook también comprueba que un registro con dos campos inválidos produce dos incidencias en la misma posición. El archivo JSON conserva el reporte principal de la práctica y su reconstrucción se verifica correctamente.

## Estado

**Resuelta y verificada; no enviada al formulario.**
