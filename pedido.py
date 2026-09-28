class Pedido:
    """Representa un pedido realizado por un cliente."""

    def __init__(self, id_pedido, cliente, producto, cantidad):
        if id_pedido <= 0:
            raise ValueError("El ID debe ser mayor que cero.")
        if not cliente.strip():
            raise ValueError("El nombre del cliente es obligatorio.")
        if not producto.strip():
            raise ValueError("El nombre del producto es obligatorio.")
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")

        self.__id_pedido = id_pedido
        self.__cliente = cliente.strip()
        self.__producto = producto.strip()
        self.__cantidad = cantidad

    @property
    def id_pedido(self):
        return self.__id_pedido

    @property
    def cliente(self):
        return self.__cliente

    @property
    def producto(self):
        return self.__producto

    @property
    def cantidad(self):
        return self.__cantidad

    def mostrar_informacion(self):
        return (
            f"Pedido #{self.__id_pedido} | "
            f"Cliente: {self.__cliente} | "
            f"Producto: {self.__producto} | "
            f"Cantidad: {self.__cantidad}"
        )
