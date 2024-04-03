# class Nodo:
#     def __init__(self, valor):
#         self.valor = valor
#         self.aristas = {}

# def agregarArista(nodo1, nodo2):
#     nodo1.aristas[nodo2.valor] = nodo2
#     nodo2.aristas[nodo1.valor] = nodo1

# # Función para crear un árbol a partir de los recorridos pre-orden, in-orden y post-orden
# def construirArbol(preorden, inorden, postorden):
#     if not preorden or not inorden or not postorden:
#         return None

#     raiz_valor = preorden[0]
#     raiz = Nodo(raiz_valor)

#     raiz_index_inorden = inorden.index(raiz_valor)
#     raiz_index_postorden = postorden.index(raiz_valor)

#     inorden_izquierda = inorden[:raiz_index_inorden]
#     inorden_derecha = inorden[raiz_index_inorden + 1:]

#     preorden_izquierda = preorden[1:1 + len(inorden_izquierda)]
#     preorden_derecha = preorden[1 + len(inorden_izquierda):]

#     postorden_izquierda = postorden[:len(inorden_izquierda)]
#     postorden_derecha = postorden[len(inorden_izquierda):-1]

#     raiz.izquierda = construirArbol(preorden_izquierda, inorden_izquierda, postorden_izquierda)
#     raiz.derecha = construirArbol(preorden_derecha, inorden_derecha, postorden_derecha)

#     return raiz

# # Función para agregar aristas al grafo basado en un recorrido en pre-orden del árbol
# def agregarAristasPreOrden(nodo, grafo):
#     if not nodo:
#         return

#     grafo[nodo.valor] = nodo  # Agregar el nodo al grafo
#     if nodo.izquierda:
#         agregarAristasPreOrden(nodo.izquierda, grafo)

#     if nodo.derecha:
#         agregarAristasPreOrden(nodo.derecha, grafo)

#     for vecino in (nodo.izquierda, nodo.derecha):
#         if vecino:
#             agregarArista(nodo, vecino)

# # Función para agregar aristas al grafo basado en un recorrido en in-orden del árbol
# def agregarAristasInOrden(nodo, grafo):
#     if not nodo:
#         return

#     if nodo.izquierda:
#         agregarAristasInOrden(nodo.izquierda, grafo)
#         agregarArista(nodo, nodo.izquierda)

#     grafo[nodo.valor] = nodo  # Agregar el nodo al grafo

#     if nodo.derecha:
#         agregarAristasInOrden(nodo.derecha, grafo)
#         agregarArista(nodo, nodo.derecha)

# # Función para agregar aristas al grafo basado en un recorrido en post-orden del árbol
# def agregarAristasPostOrden(nodo, grafo):
#     if not nodo:
#         return

#     if nodo.izquierda:
#         agregarAristasPostOrden(nodo.izquierda, grafo)

#     if nodo.derecha:
#         agregarAristasPostOrden(nodo.derecha, grafo)

#     for vecino in (nodo.izquierda, nodo.derecha):
#         if vecino:
#             agregarArista(nodo, vecino)

#     grafo[nodo.valor] = nodo  # Agregar el nodo al grafo

# # Función para imprimir el grafo
# def imprimirGrafo(nodo, visitados=None):
#     if visitados is None:
#         visitados = set()
#     visitados.add(nodo.valor)
#     print("Nodo", nodo.valor, ": ", end="")
#     print(", ".join(nodo.aristas.keys()))
#     for vecino in nodo.aristas.values():
#         if vecino.valor not in visitados:
#             imprimirGrafo(vecino, visitados)

# # Recorridos de ejemplo
# preorden = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# inorden = ['c', 'b', 'd', 'a', 'f', 'e', 'g']
# postorden = ['c', 'd', 'b', 'f', 'g', 'e', 'a']

# # Construir el árbol
# arbol = construirArbol(preorden, inorden, postorden)

# # Crear el grafo basado en los recorridos
# grafo_preorden = {}
# grafo_inorden = {}
# grafo_postorden = {}

# agregarAristasPreOrden(arbol, grafo_preorden)
# agregarAristasInOrden(arbol, grafo_inorden)
# agregarAristasPostOrden(arbol, grafo_postorden)

# # Imprimir el grafo para cada recorrido
# print("Grafo basado en recorrido en pre-orden:")
# imprimirGrafo(grafo_preorden[arbol.valor])

# print("\nGrafo basado en recorrido en in-orden:")
# imprimirGrafo(grafo_inorden[arbol.valor])

# print("\nGrafo basado en recorrido en post-orden:")
# imprimirGrafo(grafo_postorden[arbol.valor])





# class Nodo:
#     def __init__(self, valor):
#         self.valor = valor
#         self.conexiones = {}  # Un diccionario para almacenar las conexiones
#         self.visitado = False  # Para el recorrido del árbol

# class Grafo:
#     def __init__(self):
#         self.nodos = {}

#     def agregarNodo(self, valor):
#         if valor not in self.nodos:
#             self.nodos[valor] = Nodo(valor)

#     def agregarConexion(self, desde, hacia):
#         if desde in self.nodos and hacia in self.nodos:
#             self.nodos[desde].conexiones[hacia] = True
#             self.nodos[hacia].conexiones[desde] = True
#         else:
#             print("Uno o ambos nodos no existen en el grafo.")

#     def preorden(self, nodo):
#         if nodo:
#             print(nodo.valor, end=' ')
#             for conexion in nodo.conexiones:
#                 if not self.nodos[conexion].visitado:
#                     self.nodos[conexion].visitado = True
#                     self.preorden(self.nodos[conexion])

#     def inorden(self, nodo):
#         if nodo:
#             if len(nodo.conexiones) >= 1:
#                 conexion_izquierda = list(nodo.conexiones.keys())[0]
#             else:
#                 conexion_izquierda = None

#             if len(nodo.conexiones) >= 2:
#                 conexion_derecha = list(nodo.conexiones.keys())[1]
#             else:
#                 conexion_derecha = None

#             if conexion_izquierda is not None:
#                 self.inorden(self.nodos[conexion_izquierda])

#             print(nodo.valor, end=' ')

#             if conexion_derecha is not None:
#                 self.inorden(self.nodos[conexion_derecha])

#     def postorden(self, nodo):
#         if nodo:
#             self.postorden(self.nodos[nodo.valor].conexiones.get(list(nodo.conexiones.keys())[0], None))
#             self.postorden(self.nodos[nodo.valor].conexiones.get(list(nodo.conexiones.keys())[1], None))
#             print(nodo.valor, end=' ')

# # Ejemplo de uso
# grafo = Grafo()

# grafo.agregarNodo('A')
# grafo.agregarNodo('B')
# grafo.agregarNodo('C')
# grafo.agregarNodo('D')
# grafo.agregarNodo('E')

# grafo.agregarConexion('A', 'B')
# grafo.agregarConexion('A', 'C')
# grafo.agregarConexion('B', 'D')
# grafo.agregarConexion('B', 'E')

# print("Recorrido Preorden:")
# grafo.preorden(grafo.nodos['A'])
# print("\nRecorrido Inorden:")
# grafo.inorden(grafo.nodos['A'])
# print("\nRecorrido Postorden:")
# grafo.postorden(grafo.nodos['A'])

# class Solution:
#     def duplicates(self, arr, n):
#         conteo = {}
#         duplicados = []

#         for elemento in arr:
#             if elemento in conteo:
#                 conteo[elemento] += 1
#             else:
#                 conteo[elemento] = 1

#         for elemento, cantidad in conteo.items():
#             if cantidad > 1:
#                 duplicados.append(elemento)

#         return sorted(duplicados) if duplicados else [-1]


# if(__name__ == '__main__'):
#     t = int(input())
#     for i in range(t):
#         n = int(input())
#         arr = list(map(int,input().strip().split()))
#         res = Solution().duplicates(arr,n)
#         for i in res:
#             print(i,end =" ")




class Solution:
    def binarysearch(self, arr, n, k):
        salto = int(n**0.5) #Esta variable determina el tamaño del salto que se realiza en cada iteración de la búsqueda.
        #Al principio, se establece como la raíz cuadrada del tamaño del arreglo. Este valor se incrementa dinámicamente a medida que avanza la búsqueda.
        previo = 0 #Esta variable almacena el índice de inicio del bloque de búsqueda anterior. 
        #Se actualiza en cada iteración del bucle while para mantener un registro del punto de inicio del último bloque de búsqueda.
        
        while arr[min(salto, n) - 1] < k:
            previo = salto
            salto += int((n - previo)**0.5)
            if previo >= n:
                return -1
        
        for i in range(previo, min(salto, n)):
            if arr[i] == k:
                return i
        
        return -1
    
if(__name__ == '__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int,input().strip().split()))
        res = Solution().binarysearch(arr,n)
        for i in res:
            print(i,end =" ")