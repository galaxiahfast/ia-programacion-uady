# Clase 13 - Neo4j y LangGraph

Esta clase corresponde al 13 de octubre. La primera parte presenta bases de datos orientadas a grafos con Neo4j; la segunda usa LangGraph para organizar un flujo de trabajo con estado, nodos y rutas.

## Minutos que revisaría

- `00:19 a 23:00`: nodos, relaciones, propiedades y consultas básicas con Cypher.
- `27:30 a 50:10`: casos de uso, `MATCH`, `MERGE`, consultas desde Python y borrado de nodos.
- `1:17:40 a 1:36:30`: diferencia entre un grafo de conocimiento y un flujo; estado, nodos, aristas, `START` y `END`.
- `1:42:30 a 1:58:30`: construcción de un flujo, actualización del estado y rutas condicionales.

## Neo4j

En Neo4j los datos se representan mediante nodos y relaciones. Ambos pueden tener propiedades. Cypher usa patrones visuales: los nodos se escriben entre paréntesis y las relaciones entre corchetes y flechas.

`MATCH` busca patrones existentes. `MERGE` encuentra un nodo o relación y lo crea solamente cuando no existe, mientras que `CREATE` siempre intenta crear uno nuevo. Neo4j resulta útil cuando las relaciones y los recorridos entre entidades son parte central del problema.

La instalación y práctica de Neo4j son opcionales; no hay un entregable obligatorio de esa notebook.

## LangGraph

En LangGraph un nodo es una función y una arista indica qué paso se ejecuta después. El estado es un diccionario tipado que conserva la información compartida entre los pasos.

Un flujo puede seguir una secuencia fija o escoger una ruta según el estado. En el ejemplo se normaliza un tema, se seleccionan documentos y después se produce un resumen o un mensaje sin resultados. Los ejercicios añaden un filtro mínimo de páginas y un nodo que calcula la media.

## Actividades

La Unidad 3 sí se entrega. Los dos ejercicios mostrados están resueltos en [la sesión de LangGraph](../../tareas/sesion-02-langgraph/). La práctica de SQLite de la clase anterior también está completa. Todo sigue pendiente de envío al formulario.
