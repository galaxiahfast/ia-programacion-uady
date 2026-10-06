# Clase 2 - Funciones, errores y objetos

Esta clase continúa la primera notebook. La grabación dura aproximadamente 1 hora con 41 minutos.

## Lo importante

No dejaron una tarea nueva. La entrega sigue siendo la misma de la sesión 1:

- terminar los 11 ejercicios de la notebook del curso acelerado;
- resolver el ejercicio de la notebook del Zen de Python;
- entregar las dos notebooks el **7 de octubre de 2026**.

Las copias para trabajar están en la carpeta de [tareas](../../tareas/sesion-01-curso-acelerado/).

## Minutos que vale la pena revisar

- `09:23 a 18:42`: funciones, parámetros, `return`, `assert` y ejercicio del promedio.
- `21:00 a 26:00`: diferencia entre `sort` y `sorted`, criterio de ordenamiento y funciones `lambda`.
- `29:20 a 41:10`: `defaultdict`, `Counter`, agrupaciones y promedio por grupo.
- `49:22 a 1:02:14`: excepciones, `try`, `except`, `raise` y lectura de mensajes de error.
- `1:02:22 a 1:21:09`: clases, objetos, `self`, atributos de instancia y estado compartido.
- `1:21:35 a 1:34:03`: caso final del lote de predicciones y comprobación del contrato.
- `1:37:54 a 1:40:25`: presentación de la siguiente notebook sobre el Zen de Python.

## Apuntes

### Funciones

Las funciones se definen con `def`. Pueden recibir parámetros y devolver un resultado con `return`. Si se llama una función sin los argumentos requeridos, Python genera un error.

`assert` sirve para comprobar que una condición que esperamos sea verdadera realmente se cumpla. En los ejercicios se usa para verificar resultados y casos límite.

### Ordenamiento y agrupaciones

- `lista.sort()` modifica la lista original y no devuelve una lista nueva.
- `sorted(lista)` crea una lista ordenada sin modificar la original.
- El argumento `key` indica el dato que se usará para ordenar.
- Una función `lambda` sirve para expresar una operación pequeña sin definir una función aparte.
- `defaultdict` ayuda a agrupar elementos sin comprobar manualmente si ya existe cada clave.
- `Counter` cuenta cuántas veces aparece cada valor.

### Errores

Los mensajes de error indican el tipo, la línea y lo que ocurrió. Se mostraron ejemplos de `ValueError`, `IndexError`, `KeyError`, `TypeError` y `AssertionError`.

Conviene capturar errores concretos con `try` y `except`; usar una excepción demasiado general puede ocultar problemas. `raise` permite lanzar un error cuando los datos no cumplen lo esperado.

### Clases y objetos

Una clase funciona como el plano para crear objetos. `__init__` establece el estado inicial y `self` se refiere a la instancia actual.

Los datos propios de cada objeto deben crearse dentro de `__init__` usando `self`. Si una lista se declara directamente en la clase, puede terminar compartida por todas las instancias.

Asignar otro nombre al mismo objeto no crea una copia. Ambos nombres siguen apuntando a la misma instancia.

### Caso final

La clase `LotePredicciones` guarda registros y genera un resumen con:

- cantidad de registros;
- conteo por etiqueta;
- promedio de los scores;
- `None` como promedio cuando el lote está vacío.

El último ejercicio comprueba ese comportamiento con `assert`. A eso se refiere la notebook cuando habla del contrato: las condiciones que el código debe cumplir.

## Qué quedó pendiente

- [x] Revisar que los 11 ejercicios de la primera notebook estén completos.
- [x] Resolver el ejercicio de refactorización de la notebook del Zen.
- [x] Reiniciar el kernel y ejecutar ambas notebooks completas.
- [ ] Subirlas al [formulario de la Unidad 1](https://docs.google.com/forms/d/e/1FAIpQLSdTJ2vU04VfIpw1Tst_T_0g0tlbE-n6ZI81nrG0RQJMReAtaQ/viewform?usp=publish-editor).

## Algo que mencionó al final

La notebook del Zen repasa las 19 reglas de Python y busca que el código sea más claro, explícito y fácil de mantener. Solo tiene un ejercicio final de refactorización.
