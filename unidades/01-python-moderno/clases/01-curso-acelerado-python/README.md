# Clase 01 · Introducción y curso acelerado de Python

> Duración de la grabación: **1 h 46 min**  
> Resumen actualizado: **6 de octubre de 2026**  
> Fuente: transcripción de la clase, diapositivas y repositorio oficial del profesor.

## Lo esencial en un minuto

- El curso no se centra en entrenar modelos: busca construir software de IA legible, reproducible y fácil de integrar.
- La primera sesión utilizó la notebook **Curso acelerado de Python para IA** y llegó hasta comprehensions y el ejercicio de temperaturas.
- Hay que entregar **dos notebooks completas**: 11 ejercicios del curso acelerado y uno del Zen de Python.
- La instrucción vigente del repositorio oficial fija la entrega de la Unidad 1 para el **7 de octubre de 2026**.
- Para esta sesión basta Google Colab; todavía no es necesario preparar un entorno local.

## Acción prioritaria

1. Abrir y guardar una copia de las dos notebooks en Google Drive.
2. Resolver los 12 ejercicios y conservar las predicciones, explicaciones y comprobaciones solicitadas.
3. Reiniciar el entorno y ejecutar todas las celdas antes de entregar.
4. Volver a comentar las líneas que provocan errores en el laboratorio correspondiente.
5. Enviar las copias mediante el formulario oficial antes de la fecha límite.

| Material | Enlace |
| --- | --- |
| Notebook 1 · Curso acelerado | [Abrir en Google Colab](https://colab.research.google.com/drive/1Q4dLL8eTF55DsSLiOXE2frOw3iFhuHkL) |
| Notebook 2 · Zen de Python | [Abrir en Google Colab](https://colab.research.google.com/drive/1MTMMN5ifsWDA2aLzHCqRdMRmhp51K0jM) |
| Instrucciones vigentes | [Práctica de la sesión](https://github.com/oscarnavmac/programacion_ai/blob/main/unidad-01-python-moderno/sesion-01-curso-acelerado-python/PRACTICA.md) |
| Entrega de Unidad 1 | [Formulario oficial](https://docs.google.com/forms/d/e/1FAIpQLSdTJ2vU04VfIpw1Tst_T_0g0tlbE-n6ZI81nrG0RQJMReAtaQ/viewform?usp=publish-editor) |

## Ruta rápida por la grabación

Si ya conoces Python, no hace falta ver toda la clase. Estos son los fragmentos de mayor valor:

| Minutos | Prioridad | Contenido |
| --- | --- | --- |
| `20:39–24:00` | Alta | Cómo localizar, abrir y guardar una copia de la notebook en Colab. |
| `44:46–53:35` | Alta | Mutabilidad, alias, copia superficial y estructuras anidadas. Es la explicación técnica más importante de la primera mitad. |
| `1:05:01–1:12:03` | Alta | Valores interpretados como falsos y diferencia entre `0` y `None`. |
| `1:28:02–1:31:19` | Alta | Qué esperaba el profesor de las notebooks. El medio y la fecha mencionados ahí ya fueron actualizados en el repositorio. |
| `1:32:19–1:40:38` | Alta | Comprehensions, `enumerate`, `zip` y ejercicio de conversión de temperaturas. |
| `1:15:10–1:27:42` | Opcional | Experiencia profesional del profesor: agentes, integración de modelos, MCP, A2A, LangGraph y despliegue. |
| `1:43:36–1:46:22` | Media | Cierre, contenido pendiente y recordatorio sobre guardar las notebooks. |

La ruta de prioridad alta dura aproximadamente **31 minutos**. Si los fundamentos de Python también son nuevos, conviene agregar estos bloques:

- `25:32–36:18`: variables, tipos, operadores, cadenas y primer ejercicio.
- `36:18–44:46`: listas, tuplas, diccionarios, conjuntos, índices y slicing.
- `54:20–1:04:42`: tuplas, diccionarios, conjuntos y conversiones entre colecciones.

## Qué explicó el profesor

### Enfoque de la asignatura

Programar consiste en expresar una tarea mediante reglas: identificar entradas, operaciones, salidas y casos en los que faltan datos. Python se utiliza por su legibilidad, su biblioteca estándar y su ecosistema para datos e inteligencia artificial.

Las primeras clases usan notebooks para practicar, pero el curso avanzará hacia proyectos de Python reales, reproducibles y ejecutables por otras personas.

### Notebooks y estado

Una notebook mantiene variables en memoria dentro de una sesión. Por eso, ejecutar celdas fuera de orden puede producir resultados engañosos. Antes de entregar hay que reiniciar el entorno y ejecutar todo desde arriba.

### Datos y colecciones

- Tipos básicos: cadenas, enteros, flotantes, booleanos y `None`.
- Colecciones: listas, tuplas, diccionarios y conjuntos.
- Las listas y los diccionarios son mutables; dos variables pueden apuntar al mismo objeto.
- Una copia superficial no duplica los objetos mutables anidados. Para independizarlos hay que copiarlos también o usar una copia profunda cuando corresponda.
- Los conjuntos eliminan duplicados y permiten intersección, unión y diferencia.

### Control de flujo

Python interpreta `False`, `None`, cero y las colecciones vacías como valores falsos. Esto no significa que sean equivalentes: cuando cero es un resultado válido, se debe comprobar explícitamente `is None` para distinguirlo de un dato ausente.

Se repasaron `if`, `for`, `while`, comprehensions, `enumerate` y `zip`. Las comprehensions son convenientes cuando la transformación sigue siendo breve y legible; un ciclo normal es preferible cuando la lógica crece.

### Aplicaciones de IA

El profesor distinguió dos caminos:

- **Desarrollar modelos:** entrenar y evaluar modelos con bases teóricas y herramientas como PyTorch.
- **Integrar modelos:** incorporar modelos existentes en aplicaciones, agentes, servidores y flujos de trabajo.

Como ejemplo profesional describió un sistema que recomienda componentes para robots industriales. También explicó MCP como un protocolo estándar para exponer herramientas a agentes y mencionó A2A y flujos representados como grafos.

## Lista de ejercicios de la sesión

### Notebook 1 · Curso acelerado

- [ ] 1. Una frase con datos.
- [ ] 2. Una lista dentro de otra.
- [ ] 3. Copiar sin compartir la lista.
- [ ] 4. Elegir una estructura.
- [ ] 5. Cero no es ausencia.
- [ ] 6. Transformar y filtrar.
- [ ] 7. Promedio sin inventar datos.
- [ ] 8. Resumir grupos.
- [ ] 9. Instancias y alias.
- [ ] 10. Estado independiente.
- [ ] 11. Comprobar el contrato.

### Notebook 2 · Zen de Python

- [ ] 1. Refactorización siguiendo el Zen.

## Lo dicho en clase frente a la instrucción vigente

Durante la grabación el profesor comentó que todavía no había definido la fecha ni el medio de entrega y que probablemente habría dos semanas o más. Esa información quedó desactualizada.

El repositorio oficial ahora indica:

- **fecha límite:** 7 de octubre de 2026;
- **medio:** formulario de Google enlazado arriba;
- **entregables:** las dos notebooks con los 12 ejercicios resueltos;
- **criterio de verificación:** reiniciar y ejecutar todas las celdas sin dejar activos los errores intencionales.

El profesor permitió usar asistentes de IA, con la condición de comprender y poder explicar el código generado.

## Qué continúa

La grabación terminó aproximadamente a la mitad de la primera notebook. Quedaron para estudio o sesiones posteriores las funciones, ordenamiento y agrupación, excepciones, `assert`, programación orientada a objetos, el caso integrador y la notebook completa del Zen de Python.

## Fuentes verificadas

- [Repositorio oficial del curso](https://github.com/oscarnavmac/programacion_ai)
- [Sesión 1 en el repositorio oficial](https://github.com/oscarnavmac/programacion_ai/tree/main/unidad-01-python-moderno/sesion-01-curso-acelerado-python)
- [Presentación de introducción](https://drive.google.com/file/d/1Ls0122l-Fyyb7-adEzKu6HVJqUk8rHun/view?usp=sharing)

La verificación del repositorio oficial se hizo el 6 de octubre de 2026 sobre el commit `27e3c2b`.
