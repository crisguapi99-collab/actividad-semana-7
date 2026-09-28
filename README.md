# actividad-semana-7
Patrones de Diseño, Testing Unitario y Tipos de Datos Abstractos Lineales
### Descripción

Este proyecto implementa un sistema de gestión de pedidos desarrollado en Python.

El sistema permite registrar pedidos y procesarlos respetando el orden en que fueron registrados. Para esto se implementó manualmente una estructura de datos lineal tipo **cola**, utilizando el principio **FIFO (First In, First Out)**.

También se implementó el patrón de diseño **Repository**, encargado de separar la administración de los pedidos de la lógica principal de la aplicación.

Finalmente, se desarrollaron pruebas unitarias utilizando **pytest** para comprobar las principales operaciones de la cola y del Repository.

## Objetivos

- Implementar manualmente una cola sin utilizar una implementación de cola de una biblioteca.
- Aplicar las operaciones fundamentales de una cola.
- Implementar el patrón Repository.
- Integrar la cola con el Repository.
- Desarrollar pruebas unitarias con pytest.
- Crear una aplicación funcional de gestión de pedidos.

## Funcionalidades

1. Registrar un nuevo pedido.
2. Atender el siguiente pedido.
3. Consultar el siguiente pedido sin eliminarlo.
4. Mostrar todos los pedidos pendientes.
5. Consultar la cantidad de pedidos.
6. Verificar si existen pedidos pendientes.
7. Validar datos básicos de los pedidos.
8. Evitar IDs duplicados entre pedidos pendientes.

## Estructura de datos

La estructura utilizada es una **cola FIFO**.

FIFO significa que el primer pedido que entra es el primer pedido que sale.

La cola fue implementada manualmente mediante nodos enlazados. No se utilizó `queue.Queue` ni otra implementación de cola de una biblioteca.

Las operaciones principales son:

- `encolar()`: agrega un pedido al final.
- `desencolar()`: elimina y devuelve el pedido del frente.
- `ver_siguiente()`: consulta el pedido del frente sin eliminarlo.
- `esta_vacia()`: verifica si la cola está vacía.
- `cantidad()`: devuelve el número de pedidos.
- `listar_elementos()`: recorre los pedidos pendientes.

## Patrón Repository

La clase `PedidoRepository` funciona como una capa intermedia entre la aplicación y la estructura de datos.

La aplicación principal no manipula directamente los nodos de la cola. En su lugar, utiliza métodos del Repository como:

- `agregar_pedido()`
- `atender_pedido()`
- `obtener_siguiente()`
- `esta_vacio()`
- `cantidad_pedidos()`
- `listar_pedidos()`

De esta manera, se separa la administración de los datos de la lógica principal de la aplicación.

## Pruebas unitarias

Las pruebas fueron desarrolladas utilizando `pytest`.

Se prueban, entre otros aspectos:

- Estado inicial de la cola.
- Inserción de pedidos.
- Eliminación de pedidos.
- Orden FIFO.
- Consulta del siguiente pedido.
- Cantidad de elementos.
- Comportamiento de una cola vacía.
- Registro mediante Repository.
- Atención mediante Repository.
- Control de IDs duplicados.

## Requisitos

- Python 3
- pytest
- Visual Studio Code (opcional)

## Instalación

Abrir una terminal en la carpeta principal del proyecto y ejecutar:

```bash
python -m pip install -r requirements.txt
```

En Windows también puede utilizarse:

```bash
py -m pip install -r requirements.txt
```

## Ejecución

Para ejecutar el sistema:

```bash
python main.py
```

En Windows:

```bash
py main.py
```

## Ejecución de pruebas

Para ejecutar todas las pruebas:

```bash
python -m pytest -v
```

En Windows:

```bash
py -m pytest -v
```

## Autor

**Cristhian Guapi**

Actividad: Semana 7
