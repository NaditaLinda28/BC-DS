from productos import Producto

class Inventario:
    """Clase que representa el inventario de productos."""

    def __init__(self):
        """Inicializa un objeto Inventario."""
        self.productos = {}

    def agregar_producto(self, producto):
        """
        Agrega un producto al inventario.

        Args:
            producto (Producto): El producto a agregar al inventario.
        """
        self.productos[producto.id] = producto

    def eliminar_producto(self, id):
        """
        Elimina un producto del inventario.

        Args:
            id (str): El ID del producto a eliminar.

        Raises:
            ValueError: Si el producto no existe en el inventario.
        """
        if id in self.productos:
            del self.productos[id]
        else:
            raise ValueError("El producto no existe en el inventario")

    def actualizar_producto(self, id, nuevo_producto):
        """
        Actualiza la información de un producto en el inventario.

        Args:
            id (str): El ID del producto a actualizar.
            nuevo_producto (Producto): El nuevo objeto Producto con la información actualizada.

        Raises:
            ValueError: Si el producto no existe en el inventario.
        """
        if id in self.productos:
            self.productos[id] = nuevo_producto
        else:
            raise ValueError("El producto no existe en el inventario")

    def buscar_producto_por_id(self, id):
        """
        Busca un producto en el inventario por su ID.

        Args:
            id (str): El ID del producto a buscar.

        Returns:
            Producto or None: El objeto Producto si se encuentra, None si no se encuentra.
        """
        if id in self.productos:
            return self.productos[id]
        else:
            return None

    def listar_productos(self):
        """
        Lista todos los productos en el inventario.

        Returns:
            str: La información de todos los productos en el inventario.
        """
        total_cantidad = sum(producto.cantidad for producto in self.productos.values())
        total_valor = sum(producto.cantidad * producto.precio for producto in self.productos.values())
        productos_info = "\n".join([producto.obtener_informacion() for producto in self.productos.values()])
        return f"Total de productos: {total_cantidad}\nValor total del inventario: {total_valor}\n\n{productos_info}"
