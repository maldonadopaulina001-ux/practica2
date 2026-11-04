from abc import ABC, abstractmethod


# ---------------------------------------------------------------
# Clase Order (equivalente a Order.java)
# ---------------------------------------------------------------
class Order:
    def __init__(self, qtty, customer):
        self._customer = customer
        self._qtty = qtty

    def print(self):
        print("     Customer: " + str(self.get_customer()))
        print("     Quantity: " + str(self.get_qtty()))
        print("     ------------")

    def get_qtty(self):
        return self._qtty

    def get_customer(self):
        return self._customer


# ---------------------------------------------------------------
# Interfaz QueueInterface
# ---------------------------------------------------------------
class QueueInterface(ABC):
    @abstractmethod
    def size(self):
        """Devuelve el número de elementos de la cola."""

    @abstractmethod
    def is_empty(self):
        """True si la cola está vacía, False si no."""

    @abstractmethod
    def front(self):
        """Devuelve el primer elemento SIN eliminarlo. None si está vacía."""

    @abstractmethod
    def enqueue(self, info):
        """Añade un nuevo elemento al final de la cola."""

    @abstractmethod
    def dequeue(self):
        """Devuelve el primer elemento Y lo elimina. None si está vacía."""


# ---------------------------------------------------------------
# Clase Node: cada nodo guarda el objeto (info) y el siguiente nodo (next)
# ---------------------------------------------------------------
class Node:
    def __init__(self, info, next_node=None):
        self._info = info
        self._next = next_node

    def get_info(self):
        return self._info

    def set_info(self, info):
        self._info = info

    def get_next(self):
        return self._next

    def set_next(self, next_node):
        self._next = next_node


# ---------------------------------------------------------------
# Clase Queue basada en lista enlazada
#   top  -> cabeza de la cola (por donde se extrae)
#   tail -> último nodo (por donde se inserta)
# ---------------------------------------------------------------
class Queue(QueueInterface):
    def __init__(self):
        self._top = None
        self._tail = None
        self._size = 0

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def front(self):
        if self.is_empty():
            return None
        return self._top.get_info()

    def enqueue(self, info):
        new_node = Node(info)
        if self.is_empty():
            self._top = new_node
        else:
            self._tail.set_next(new_node)
        self._tail = new_node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        info = self._top.get_info()
        self._top = self._top.get_next()
        if self._top is None:      # la cola quedó vacía
            self._tail = None
        self._size -= 1
        return info

    # Apartado 1: mostrar el contenido de la cola
    def print_info(self):
        print("********* QUEUE DUMP *********")
        print("   Size: " + str(self._size))
        node = self._top
        i = 1
        while node is not None:
            print("   ** Element " + str(i))
            node.get_info().print()      # usa Order.print()
            node = node.get_next()
            i += 1
        print("******************************")

    # Apartado 2: n-ésimo elemento (posición 1 = primero), sin borrarlo
    def get_nth(self, pos):
        if pos < 1 or pos > self._size:
            return None
        node = self._top
        for _ in range(pos - 1):
            node = node.get_next()
        return node.get_info()


# ---------------------------------------------------------------
# TestQueue (equivalente al main)
# ---------------------------------------------------------------
def main():
    q = Queue()

    print(">>> Cola vacía")
    q.print_info()

    # Al menos 3 pedidos
    print(">>> enqueue de 3 pedidos")
    q.enqueue(Order(20, "cust1"))
    q.print_info()
    q.enqueue(Order(30, "cust2"))
    q.print_info()
    q.enqueue(Order(40, "cust3"))
    q.print_info()

    # front: no elimina
    print(">>> front (no elimina)")
    primero = q.front()
    primero.print()
    q.print_info()

    # dequeue: elimina
    print(">>> dequeue (elimina el primero)")
    extraido = q.dequeue()
    extraido.print()
    q.print_info()

    # Apartado 2: getNth con cuatro elementos
    print(">>> Apartado 2: cuatro elementos y obtener el tercero")
    q2 = Queue()
    q2.enqueue(Order(20, "cust1"))
    q2.enqueue(Order(30, "cust2"))
    q2.enqueue(Order(40, "cust3"))
    q2.enqueue(Order(50, "cust4"))
    q2.print_info()

    tercero = q2.get_nth(3)
    print("Elemento 3:")
    tercero.print()

    print("Posición no válida (0 y 9):", q2.get_nth(0), q2.get_nth(9))
    q2.print_info()   # la cola sigue intacta


if __name__ == "__main__":
    main()
