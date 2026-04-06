README
Descripción

Este proyecto contiene dos scripts en Python relacionados con funciones hash SHA-256:

Fuerza bruta de hash
Búsqueda de orden en un árbol de Merkle
1. Fuerza bruta de SHA-256
Objetivo

Encontrar una secuencia de 10 dígitos (del 0 al 9) cuyo hash SHA-256 coincida con un valor dado.

Cómo funciona
Se generan todos los números desde 0000000000 hasta 9999999999
Cada número se convierte a string con 10 dígitos
Se calcula su hash SHA-256
Se compara con el hash objetivo
Código clave
for i in range(10_000_000_000):
    s = f"{i:010d}"
    h = hashlib.sha256(s.encode()).hexdigest()
Limitaciones
Espacio de búsqueda: 10^10 combinaciones
Extremadamente lento en CPU (puede tardar días o más)
No es práctico sin optimización (GPU, paralelización, etc.)
2. Búsqueda de orden en árbol de Merkle
Objetivo

Dado:

un hash raíz (root)
un conjunto de transacciones

Encontrar el orden de las transacciones que genera ese root.

Cómo funciona
Se generan todas las permutaciones posibles de las transacciones
Para cada orden:
Se construye el árbol de Merkle
Se calcula el hash raíz
Se compara con el hash objetivo
Construcción del árbol de Merkle
Cada transacción se hashea
Se agrupan de a pares
Se concatenan y se vuelven a hashear
Si hay un número impar, el último nodo se "sube" sin combinar
Código clave
xs = [h(x.encode()) for x in xs]

while len(xs) > 1:
    xs = [h((xs[i]+xs[i+1]).encode()) if i+1 < len(xs) else xs[i]
          for i in range(0, len(xs), 2)]
Búsqueda
for p in itertools.permutations(t):
    if merkle(p) == root:
        print("Orden encontrado:", p)
Limitaciones
Complejidad factorial: n!
Solo funciona si:
El hash fue generado con el mismo método
Las transacciones son correctas
El orden es el único válido
Conclusión
El primer código resuelve un problema de preimagen de hash
El segundo resuelve un problema de reconstrucción de orden en estructuras hash
Ambos usan fuerza bruta, por lo que escalan mal con el tamaño del problema
