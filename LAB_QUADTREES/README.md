# **Documentación: Quadtree para Gestión Logística**

## **Introducción**
Este proyecto implementa y optimiza una estructura de datos **Quadtree** desde cero para la gestión eficiente de puntos de entrega en un sistema logístico. Simulamos un entorno con **10.000 a 100.000 puntos** en un plano bidimensional para resolver problemas críticos de distribución, como la identificación de destinos dentro de un radio de entrega y la localización del punto más cercano.

## **Descripción de la Estructura**
El **Quadtree** es una estructura de árbol donde cada nodo interno tiene exactamente cuatro hijos. Se utiliza para particionar un espacio bidimensional dividiendo la región en cuatro cuadrantes (NW, NE, SW, SE). 

### **Componentes Clave:**
*   **Punto:** Representa las coordenadas (x, y) de una entrega.
*   **Rectángulo:** Define los límites geográficos de cada nodo y permite validar intersecciones.
*   **Capacidad:** En este notebook, hemos configurado una capacidad de **1 punto por nodo** para maximizar la segmentación espacial y observar el comportamiento de la estructura en su estado más granular.

## **Funcionalidades Implementadas**
1.  **Construcción Dinámica:** Inserción de miles de puntos con subdivisión automática de nodos.
2.  **Búsqueda por Radio (Range Search):** Localización ultra rápida de todos los puntos dentro de una distancia específica.
3.  **Búsqueda de Vecino Cercano:** Identificación del punto de entrega más próximo a una coordenada objetivo.
4.  **Visualización Espacial:** Generación de mapas de puntos y validación visual mediante círculos de colisión y zoom.
5.  **Benchmarking Comparativo:** Pruebas de estrés contra el método de **Fuerza Bruta**.

## **Análisis de Rendimiento: Quadtree vs. Fuerza Bruta**
Tras ejecutar múltiples escenarios, los resultados arrojan conclusiones clave para la toma de decisiones en software logístico:

*   **Búsqueda por Radio:** El Quadtree es el ganador indiscutible. Gracias a la poda espacial (descartar regiones enteras que no interesan), es hasta **~34 veces más rápido** que la fuerza bruta en cargas masivas.
*   **Vecino más Cercano:** En la implementación actual, la fuerza bruta mantiene una ligera ventaja debido al overhead de recursividad y la falta de un algoritmo de poda por distancia mínima en el Quadtree.
*   **Escalabilidad:** Se identificó que a partir de **10.000 puntos**, la eficiencia del Quadtree crece exponencialmente, siendo la única opción viable para datasets de gran escala (100.000+ puntos).

## **Contenido del Notebook**
1.  **Estructura del Quadtree:** Clases base y lógica de subdivisión.
2.  **Generación y Consulta:** Creación de datos aleatorios y pruebas de búsqueda.
3.  **Visualización:** Gráficos con `matplotlib` para verificar la precisión.
4.  **Pruebas Unitarias:** Validación de la lógica de distancia e inserción.
5.  **Comparativa Técnica:** Tablas y gráficos de tiempo de ejecución en escala logarítmica.
6.  **Análisis de Carga Masiva:** Prueba final con 100.000 puntos.

---
