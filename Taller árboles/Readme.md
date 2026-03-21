Generación de datos

Se crean registros con:

id único
nombre aleatorio
promedio entre 0 y 10

Cantidad típica: 10,000 registros.

Estructuras usadas
Lista

Almacena los datos de forma secuencial.
La búsqueda recorre todos los elementos.

Complejidad: O(n)

Árbol Binario de Búsqueda (ABB)

Organiza los datos según el id.
Permite búsquedas más rápidas que la lista.

Complejidad:

Promedio: O(log n)
Peor caso: O(n)
Árbol B+

Estructura balanceada que mantiene múltiples claves por nodo.
Optimizada para búsquedas eficientes en grandes volúmenes de datos.

Complejidad: O(log n)

Pruebas de rendimiento

Se realizan búsquedas aleatorias con:

100 búsquedas
1000 búsquedas
3000 búsquedas

Se mide el tiempo total de ejecución en cada estructura.

Objetivo

Comparar el rendimiento de búsqueda entre diferentes estructuras de datos y observar sus diferencias en la práctica.
