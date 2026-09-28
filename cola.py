class Nodo:
    """Nodo utilizado por la cola para almacenar un pedido."""

    def __init__(self, pedido):
        self.pedido = pedido
        self.siguiente = None


class Cola:
    """Implementación manual de una cola FIFO mediante nodos enlazados."""

    def __init__(self):
        self.__frente = None
        self.__final = None
        7

        self.__cantidad = 0

    def encolar(self, pedido):
        """Agrega un pedido al final de la cola."""
        nuevo_nodo = Nodo(pedido)

        if self.esta_vacia():
            self.__frente = nuevo_nodo
            self.__final = nuevo_nodo
        else:
            self.__final.siguiente = nuevo_nodo
            self.__final = nuevo_nodo

        self.__cantidad += 1

    def desencolar(self):
        """Retira y devuelve el primer pedido de la cola."""
        if self.esta_vacia():
            raise IndexError("No hay pedidos pendientes.")

        pedido = self.__frente.pedido
        self.__frente = self.__frente.siguiente
        self.__cantidad -= 1

        if self.__frente is None:
            self.__final = None

        return pedido

    def ver_siguiente(self):
        """Consulta el primer pedido sin eliminarlo."""
        if self.esta_vacia():
            raise IndexError("No hay pedidos pendientes.")

        return self.__frente.pedido

    def esta_vacia(self):
        """Verifica si la cola está vacía."""
        return self.__frente is None

    def cantidad(self):
        """Devuelve la cantidad de pedidos almacenados."""
        return self.__cantidad

    def listar_elementos(self):
        """Devuelve los pedidos en el orden en que fueron registrados."""
        pedidos = []
        actual = self.__frente

        while actual is not None:
            pedidos.append(actual.pedido)
            actual = actual.siguiente

        return pedidos
