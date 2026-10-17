# Clase 14 - LangGraph y agentes

Esta clase corresponde al 15 de octubre. Primero completa LangGraph con paralelismo, reductores y subgrafos. Después presenta los componentes de un agente construido con LangChain y muestra cómo conectarlo con herramientas de un servidor MCP.

## Minutos que revisaría

- `00:23 a 11:55`: ejecución paralela, actualización simultánea del estado y reductores.
- `12:00 a 16:00`: `Command`, actualización del estado y saltos entre nodos.
- `16:04 a 22:45`: subgrafos, flujo padre y ejecución paralela de flujos hijos.
- `27:00 a 39:15`: ciclo de un agente, modelo, herramientas, mensajes y patrón ReAct.
- `40:09 a 52:10`: middleware, límites y controles alrededor del modelo y las herramientas.
- `52:30 a 1:17:30`: creación de herramientas y agente de demostración sin depender de una API externa.
- `1:34:45 a 1:38:30`: conexión de un servidor MCP con un agente.

## LangGraph avanzado

Dos nodos pueden salir del mismo punto y ejecutarse en paralelo. Si cada uno modifica una parte distinta del estado no hay conflicto. Cuando ambos actualizan la misma clave se necesita un reductor que indique cómo combinar los resultados.

`Command` permite que un nodo actualice el estado y decida directamente cuál será el siguiente paso. Los subgrafos sirven para encapsular flujos completos y utilizarlos como nodos dentro de un grafo mayor.

## Agentes y herramientas

Un agente combina un modelo, herramientas y un ciclo de decisión. El modelo recibe la solicitud, decide si necesita llamar una herramienta, observa el resultado y continúa hasta completar la tarea.

Las herramientas se describen con nombre, parámetros y propósito. LangChain convierte sus resultados en mensajes que el modelo puede relacionar con cada llamada. El middleware permite limitar llamadas, validar entradas o intervenir antes y después del modelo o de una herramienta.

Un servidor MCP expone herramientas mediante un protocolo común. El agente puede descubrirlas y utilizarlas sin duplicar la lógica del servidor. La demostración final usa de esta forma las herramientas del proyecto de productos.

## Actividades

No se dejó una práctica nueva. La sesión de agentes es material opcional y no requiere API key para la entrega de la Unidad 3. Las dos prácticas obligatorias de esa unidad ya están resueltas y siguen pendientes de envío.
