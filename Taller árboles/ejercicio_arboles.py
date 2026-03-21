import random
import time

# ------------------------------------
# CREACIÓN DE DATOS ALEATORIOS
# ------------------------------------
def crear_registros(cantidad=10000):
    lista_nombres = [
        "Ana", "Carlos", "Maria", "Juan", "Pedro", "Luisa", "Sofia",
        "Andres", "Camila", "David", "Laura", "Mateo", "Valentina",
        "Daniel", "Sara", "Miguel", "Paula", "Sebastian", "Elena"
    ]

    resultado = []
    identificadores = random.sample(range(1000, 100000), cantidad)  # IDs sin repetir

    for idx in range(cantidad):
        registro = {
            "id": identificadores[idx],
            "nombre": random.choice(lista_nombres),
            "promedio": round(random.uniform(0, 10), 2)
        }
        resultado.append(registro)

    return resultado


# ------------------------------------
# ALMACENAMIENTO EN LISTA
# ------------------------------------
def cargar_en_lista(datos):
    contenedor = []

    for item in datos:
        contenedor.append(item)

    return contenedor


# ------------------------------------
# IMPLEMENTACIÓN ÁRBOL BINARIO DE BÚSQUEDA
# ------------------------------------
class NodoBinario:
    def __init__(self, dato):
        self.dato = dato
        self.izq = None
        self.der = None


class ArbolBinarioBusqueda:
    def __init__(self):
        self.root = None

    def agregar(self, dato):
        if self.root is None:
            self.root = NodoBinario(dato)
        else:
            self._agregar_rec(self.root, dato)

    def _agregar_rec(self, actual, dato):
        if dato["id"] < actual.dato["id"]:
            if actual.izq is None:
                actual.izq = NodoBinario(dato)
            else:
                self._agregar_rec(actual.izq, dato)
        else:
            if actual.der is None:
                actual.der = NodoBinario(dato)
            else:
                self._agregar_rec(actual.der, dato)

    def encontrar(self, clave_id):
        return self._encontrar_rec(self.root, clave_id)

    def _encontrar_rec(self, nodo, clave_id):
        if nodo is None:
            return None

        if nodo.dato["id"] == clave_id:
            return nodo.dato

        if clave_id < nodo.dato["id"]:
            return self._encontrar_rec(nodo.izq, clave_id)
        else:
            return self._encontrar_rec(nodo.der, clave_id)


# ------------------------------------
# IMPLEMENTACIÓN ÁRBOL B+
# ------------------------------------
class NodoBMas:
    def __init__(self, es_hoja=False):
        self.es_hoja = es_hoja
        self.llaves = []
        self.ramas = []
        self.next = None  # enlace entre hojas


class ArbolBMas:
    def __init__(self, grado=3):
        self.root = NodoBMas(True)
        self.grado = grado

    def insertar(self, key, value):
        nodo_raiz = self.root

        # Si la raíz está llena, se divide
        if len(nodo_raiz.llaves) == (2 * self.grado) - 1:
            nueva = NodoBMas()
            nueva.ramas.append(nodo_raiz)

            self._split_child(nueva, 0)
            self._insert_non_full(nueva, key, value)

            self.root = nueva
        else:
            self._insert_non_full(nodo_raiz, key, value)

    def _insert_non_full(self, nodo, key, value):
        if nodo.es_hoja:
            pos = len(nodo.llaves) - 1
            nodo.llaves.append((None, None))

            while pos >= 0 and key < nodo.llaves[pos][0]:
                nodo.llaves[pos + 1] = nodo.llaves[pos]
                pos -= 1

            nodo.llaves[pos + 1] = (key, value)

        else:
            pos = len(nodo.llaves) - 1

            while pos >= 0 and key < nodo.llaves[pos][0]:
                pos -= 1

            pos += 1

            if len(nodo.ramas[pos].llaves) == (2 * self.grado) - 1:
                self._split_child(nodo, pos)

                if key > nodo.llaves[pos][0]:
                    pos += 1

            self._insert_non_full(nodo.ramas[pos], key, value)

    def _split_child(self, padre, indice):
        grado = self.grado
        nodo_actual = padre.ramas[indice]
        nuevo_nodo = NodoBMas(nodo_actual.es_hoja)

        padre.ramas.insert(indice + 1, nuevo_nodo)
        padre.llaves.insert(indice, nodo_actual.llaves[grado - 1])

        nuevo_nodo.llaves = nodo_actual.llaves[grado:(2 * grado) - 1]
        nodo_actual.llaves = nodo_actual.llaves[0:grado - 1]

        if not nodo_actual.es_hoja:
            nuevo_nodo.ramas = nodo_actual.ramas[grado:(2 * grado)]
            nodo_actual.ramas = nodo_actual.ramas[0:grado]

    def buscar(self, key, nodo=None):
        if nodo is None:
            nodo = self.root

        pos = 0
        while pos < len(nodo.llaves) and key > nodo.llaves[pos][0]:
            pos += 1

        if nodo.es_hoja:
            if pos < len(nodo.llaves) and nodo.llaves[pos][0] == key:
                return nodo.llaves[pos][1]
            return None

        return self.buscar(key, nodo.ramas[pos])


# ------------------------------------
# COMPARACIÓN DE TIEMPOS DE BÚSQUEDA
# ------------------------------------

def buscar_en_lista(lista, clave):
    for elemento in lista:
        if elemento["id"] == clave:
            return elemento
    return None


def medir_tiempos():
    # Generar datos
    datos = crear_registros(10000)

    # Estructuras
    estructura_lista = cargar_en_lista(datos)

    arbol_binario = ArbolBinarioBusqueda()
    arbol_bmas = ArbolBMas(grado=3)

    # Insertar datos en árboles
    for registro in datos:
        arbol_binario.agregar(registro)
        arbol_bmas.insertar(registro["id"], registro)

    # Cantidades de pruebas
    pruebas = [100, 1000, 3000]

    print("\n--- RESULTADOS DE TIEMPOS ---\n")

    for cantidad in pruebas:
        # Seleccionar IDs aleatorios existentes
        claves = random.sample([d["id"] for d in datos], cantidad)

        # LISTA
        inicio = time.time()
        for clave in claves:
            buscar_en_lista(estructura_lista, clave)
        fin = time.time()
        tiempo_lista = fin - inicio

        # ABB
        inicio = time.time()
        for clave in claves:
            arbol_binario.encontrar(clave)
        fin = time.time()
        tiempo_abb = fin - inicio

        # ÁRBOL B+
        inicio = time.time()
        for clave in claves:
            arbol_bmas.buscar(clave)
        fin = time.time()
        tiempo_bmas = fin - inicio

        print(f"Búsquedas: {cantidad}")
        print(f"Lista:     {tiempo_lista:.6f} segundos")
        print(f"ABB:       {tiempo_abb:.6f} segundos")
        print(f"Árbol B+:  {tiempo_bmas:.6f} segundos")
        print("-" * 40)


# Ejecutar prueba
if __name__ == "__main__":
    medir_tiempos()
