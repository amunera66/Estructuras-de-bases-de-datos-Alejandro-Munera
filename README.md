**Árbol KD**
En esta sección se implementa la estructura de datos KD-Tree para organizar puntos en un espacio de k dimensiones. Se define una clase Nodo que almacena un punto, el eje de división y referencias a sus hijos izquierdo y derecho.
La función construir crea el árbol de manera recursiva. En cada nivel se selecciona un eje según la profundidad y se ordenan los puntos con respecto a ese eje. Luego se toma el elemento central de la lista ordenada como pivote, lo que permite dividir el conjunto en dos subconjuntos. Esto asegura un árbol balanceado en número de nodos, aunque no necesariamente una partición espacial homogénea si los datos no están distribuidos uniformemente.
La función distancia calcula la distancia euclidiana entre dos puntos en cualquier número de dimensiones.
La función buscar_radio recorre el árbol para encontrar todos los puntos dentro de un radio dado respecto a un punto objetivo. Utiliza poda para evitar explorar ramas que no pueden contener puntos válidos.
La función mas_cercano implementa la búsqueda del vecino más cercano. Explora primero la rama más prometedora y solo visita la otra si existe posibilidad de encontrar un punto más cercano, usando también poda.

**Ejemplo de uso**
En esta parte se genera un conjunto de puntos aleatorios en dos dimensiones dentro de un rango definido. Con estos puntos se construye el KD-Tree.
Luego se genera un punto objetivo también aleatorio. A partir de este punto se realizan dos operaciones principales: la búsqueda de todos los puntos dentro de un radio determinado y la búsqueda del vecino más cercano.
Finalmente se imprimen resultados básicos como el número total de puntos, el punto objetivo, la cantidad de puntos dentro del radio y el punto más cercano junto con su distancia.

**Gráficos en R2**
Aquí se representan los datos en el plano cartesiano para facilitar la interpretación visual. Se grafican todos los puntos generados, destacando en otro color aquellos que están dentro del radio de búsqueda.
También se marca el punto objetivo y se genera una segunda gráfica con zoom alrededor de este punto. En esta vista se dibuja además un círculo que representa el radio de búsqueda, lo que permite verificar visualmente qué puntos deberían ser incluidos.

**Árbol de los primeros 4 niveles**
Esta sección muestra una representación del KD-Tree como una estructura jerárquica. Se dibujan los nodos del árbol hasta una profundidad limitada (por ejemplo, 4 niveles) para evitar saturar la visualización.
Cada nodo se representa con sus coordenadas y se dibujan líneas hacia sus hijos. Esto permite entender cómo se organiza el árbol y cómo se distribuyen los puntos en cada nivel.

**Pruebas unitarias**
Se implementa un conjunto de pruebas simples utilizando assert para verificar el correcto funcionamiento de las funciones principales.
Las pruebas cubren la construcción del árbol, el cálculo de distancia, la búsqueda por radio y la búsqueda del vecino más cercano. También se incluyen casos límite como listas vacías, un solo punto y radios extremos.
Si todas las pruebas pasan, se muestra un mensaje de éxito con el tiempo de ejecución. Si alguna falla, se indica el nombre del test que produjo el error.

**Prueba vs fuerza bruta**
En esta sección se compara el rendimiento del KD-Tree con un enfoque de fuerza bruta. Se implementan versiones directas de búsqueda por radio y vecino más cercano que recorren todos los puntos sin optimización.
Se ejecutan pruebas en distintos escenarios, variando el número de puntos, el número de consultas y el tamaño del radio. Para cada caso se mide el tiempo de ejecución de ambos enfoques.
Esto permite observar en qué situaciones el KD-Tree ofrece ventajas y en cuáles la fuerza bruta puede ser comparable o incluso mejor.

**Gráficos KD-Tree vs fuerza bruta**
Finalmente, se grafican los resultados obtenidos en las pruebas de rendimiento. Se comparan los tiempos de ejecución del KD-Tree y la fuerza bruta para cada escenario.
Se utiliza una escala logarítmica para facilitar la visualización cuando hay diferencias grandes en los tiempos. Se generan dos gráficas: una para la búsqueda de vecino más cercano y otra para la búsqueda por radio.
Estas gráficas permiten analizar claramente el comportamiento de ambos algoritmos y entender en qué condiciones cada uno es más eficiente.
