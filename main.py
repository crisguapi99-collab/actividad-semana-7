from pedido import Pedido
from pedido_repository import PedidoRepository


def mostrar_menu():
    print("\n" + "=" * 50)
    print("        SISTEMA DE GESTIÓN DE PEDIDOS")
    print("=" * 50)
    print("1. Registrar nuevo pedido")
    print("2. Atender siguiente pedido")
    print("3. Consultar siguiente pedido")
    print("4. Mostrar todos los pedidos")
    print("5. Consultar cantidad de pedidos")
    print("6. Verificar si hay pedidos pendientes")
    print("7. Salir")
    print("=" * 50)


def ejecutar():
    repositorio = PedidoRepository()
    siguiente_id = 1

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            try:
                cliente = input("Nombre del cliente: ").strip()
                producto = input("Nombre del producto: ").strip()
                cantidad = int(input("Cantidad: "))

                pedido = Pedido(
                    siguiente_id,
                    cliente,
                    producto,
                    cantidad
                )

                repositorio.agregar_pedido(pedido)
                print("\nPedido registrado correctamente.")
                print(pedido.mostrar_informacion())
                siguiente_id += 1

            except ValueError as error:
                print(f"\nError: {error}")

        elif opcion == "2":
            try:
                pedido = repositorio.atender_pedido()
                print("\nPedido atendido correctamente.")
                print(pedido.mostrar_informacion())
            except IndexError as error:
                print(f"\nError: {error}")

        elif opcion == "3":
            try:
                pedido = repositorio.obtener_siguiente()
                print("\nSiguiente pedido:")
                print(pedido.mostrar_informacion())
            except IndexError as error:
                print(f"\nError: {error}")

        elif opcion == "4":
            pedidos = repositorio.listar_pedidos()

            if not pedidos:
                print("\nNo hay pedidos pendientes.")
            else:
                print("\n--- PEDIDOS PENDIENTES ---")
                for pedido in pedidos:
                    print(pedido.mostrar_informacion())

        elif opcion == "5":
            print(f"\nPedidos pendientes: {repositorio.cantidad_pedidos()}")

        elif opcion == "6":
            if repositorio.esta_vacio():
                print("\nNo hay pedidos pendientes.")
            else:
                print("\nHay pedidos pendientes por atender.")

        elif opcion == "7":
            print("\nGracias por utilizar el sistema.")
            break

        else:
            print("\nOpción no válida. Intente nuevamente.")


if __name__ == "__main__":
    ejecutar()
