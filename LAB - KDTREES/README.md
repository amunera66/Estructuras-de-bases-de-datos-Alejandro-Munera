**Introducción**

En este proyecto se aborda el problema de búsqueda eficiente en un conjunto de datos espaciales. Se trabaja con aproximadamente 10.000 puntos de entrega representados como coordenadas (x, y), simulando un sistema de logística en una ciudad. El objetivo es responder consultas espaciales de manera eficiente, como encontrar puntos cercanos a una ubicación o determinar el punto más próximo.

Para resolver este problema, se implementa desde cero un Árbol-KD (KD-Tree) y se compara su rendimiento frente a un enfoque de fuerza bruta.

**Descripción**

El Árbol-KD es una estructura de datos que organiza puntos en un espacio k-dimensional mediante particiones recursivas. En este caso se utiliza para datos en 2D (coordenadas x, y). El árbol permite reducir significativamente el número de comparaciones necesarias durante las búsquedas, gracias a técnicas de poda basadas en la geometría del espacio.

Por otro lado, el método de fuerza bruta consiste en recorrer todos los puntos en cada consulta, lo cual es simple pero poco eficiente para grandes volúmenes de datos.

**Funcionalidades**

- Construcción de un Árbol-KD a partir de un conjunto de puntos.
- Búsqueda de todos los puntos dentro de un radio dado (range search).
- Búsqueda del punto más cercano a una ubicación (nearest neighbor).
- Visualización de los puntos en el plano cartesiano.
- Visualización de los primeros niveles del árbol.
- Comparación de rendimiento entre KD-Tree y fuerza bruta.
- Ejecución de pruebas unitarias para validar el funcionamiento.

**Prueba vs Fuerza Bruta**

Se comparan ambos enfoques en distintos escenarios:

- Muchos puntos (10.000)
- Pocos puntos (10)
- Radio grande
- Muchas consultas

El análisis muestra que el KD-Tree es más eficiente en la mayoría de los casos, especialmente con grandes volúmenes de datos y múltiples consultas. Sin embargo, en conjuntos pequeños (por ejemplo, menos de ~16 puntos), la fuerza bruta puede ser más rápida.

Esto se debe a varios factores:
- El KD-Tree tiene un costo inicial de construcción.
- La recursión introduce sobrecarga adicional.
- La localidad de caché favorece a la fuerza bruta en datasets pequeños.
- El costo constante de recorrer pocos elementos es muy bajo.

**Gráficos**

Se incluyen visualizaciones que permiten:
- Ver todos los puntos generados.
- Identificar los puntos dentro de un radio.
- Mostrar el punto objetivo.
- Observar el comportamiento del KD-Tree en los primeros niveles.
- Comparar tiempos de ejecución entre KD-Tree y fuerza bruta (incluyendo escala logarítmica para mejor interpretación).

**Conclusiones**

El Árbol-KD es una solución eficiente para problemas de búsqueda espacial cuando se trabaja con grandes volúmenes de datos o múltiples consultas. Su principal ventaja radica en la poda de regiones irrelevantes, lo que reduce significativamente el número de comparaciones.

Sin embargo, no siempre es la mejor opción. En datasets pequeños o cuando el radio de búsqueda es muy grande, la fuerza bruta puede ser igual o incluso más eficiente debido a su simplicidad y menor sobrecarga.

En este proyecto se observa que el KD-Tree comienza a superar a la fuerza bruta aproximadamente a partir de 16 puntos, lo cual es coherente con el análisis teórico y práctico del comportamiento de ambos enfoques.

**Cómo ejecutar en Google Colab**

1. Abrir Google Colab.
2. Crear un nuevo notebook.
3. Copiar y pegar el código completo en una celda.
4. Ejecutar la celda.

El código generará:
- Resultados de búsquedas (vecino más cercano y búsqueda por radio).
- Gráficas de los puntos y consultas.
- Comparaciones de rendimiento.
- Visualización del árbol.
- Resultados de pruebas unitarias.

