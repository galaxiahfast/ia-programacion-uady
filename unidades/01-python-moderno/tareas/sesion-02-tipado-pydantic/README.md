# Sesión 2 - Tipado y Pydantic

Usé la notebook oficial para resolver los ocho ejercicios. También están el módulo y el reporte JSON que pide la práctica.

## Archivos

- `u1_n3_tipado_pydantic.ipynb`: notebook completa y ejecutada.
- `lesson_models.py`: modelos, procesamiento de lotes y `count_labels`.
- `reporte_ejercicio_8.json`: reporte serializado y reconstruido en el ejercicio 8.
- `requirements.txt`: versiones indicadas en el material del profesor.

## Comprobaciones

Ejecuté la notebook completa con Python 3.12.3 y sus 36 celdas de código terminaron sin errores.

```text
code_cells=36 executed=36 errors=0
accepted=2 issues=4
```

También ejecuté la comprobación de mypy que pide el ejercicio:

```bash
python -m mypy --strict lesson_models.py
```

```text
Success: no issues found in 1 source file
```

El registro con dos campos inválidos genera dos errores en la misma posición, pero cuenta como un solo registro rechazado. El reporte se guarda en JSON y se puede volver a cargar.

## Estado

**Terminada y probada; todavía no enviada al formulario.**
