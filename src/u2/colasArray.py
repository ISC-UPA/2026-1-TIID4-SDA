# Colas 
class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def encolar(self, item):
        self.items.append(item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        else:
            raise IndexError("La cola está vacía")

    def tamano(self):
        return len(self.items)

    def frente(self):
        if not self.esta_vacia():
            return self.items[0]
        else:
            raise IndexError("La cola está vacía")
    def __str__(self):
         return "Cola: " + str(self.items)

# Ejemplo de uso
if __name__ == "__main__":
    cola = Cola()
    cola.encolar(1)
    cola.encolar(2)
    cola.encolar(3)
    print(cola)  # Cola: [1, 2, 3]
    print("Frente de la cola:", cola.frente())  # Frente de la cola: 1
    print("Tamaño de la cola:", cola.tamano())  # Tamaño de la cola: 3
    print("Desencolando:", cola.desencolar())  # Desencolando: 1
    print(cola)  # Cola: [2, 3]
    print("¿La cola está vacía?", cola.esta_vacia())  # ¿La cola está vacía? False
    print("Desencolando:", cola.desencolar())  # Desencolando: 2
    print("Desencolando:", cola.desencolar())  # Desencolando: 3
    print("¿La cola está vacía?", cola.esta_vacia())  # ¿La cola está vacía? True   

   # usando colas propias de python    
    from collections import deque

    cola_deque = deque()
    cola_deque.append(1)
    cola_deque.append(2)
    cola_deque.append(3)
    print("Cola usando deque:", list(cola_deque))  # Cola usando deque: [1, 2, 3]
    print("Desencolando con deque:", cola_deque.popleft())  # Desencolando con deque: 1
    print("Cola después de desencolar con deque:", list(cola_deque))  # Cola después de desencolar con deque: [2, 3]

    print(cola_deque)

    