from cola import Cola


class PedidoRepository:
    """Repository que administra los pedidos mediante una cola."""

    def __init__(self):
        self.__cola = Cola()
        self.__ids = set()

    def agregar_pedido(self, pedido):
        """Registra un pedido nuevo."""
        if pedido.id_pedido in self.__ids:
            raise ValueError("Ya existe un pedido pendiente con ese ID.")

        self.__cola.encolar(pedido)
        self.__ids.add(pedido.id_pedido)

    def atender_pedido(self):
        """Retira y devuelve el siguiente pedido pendiente."""
        pedido = self.__cola.desencolar()
        self.__ids.remove(pedido.id_pedido)
        return pedido

    def obtener_siguiente(self):
        """Consulta el próximo pedido sin retirarlo."""
        return self.__cola.ver_siguiente()

    def esta_vacio(self):
        """Verifica si no existen pedidos pendientes."""
        return self.__cola.esta_vacia()

    def cantidad_pedidos(self):
        """Devuelve la cantidad de pedidos pendientes."""
        return self.__cola.cantidad()

    def listar_pedidos(self):
        """Devuelve todos los pedidos pendientes."""
        return self.__cola.listar_elementos()
