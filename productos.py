class Producto:
    """Clase que representa un producto en el inventario."""

    def __init__(self, id, nombre, descripcion, cantidad, precio):
        """
        Inicializa un objeto Producto.

        Args:
            id (str): El ID del producto.
            nombre (str): El nombre del producto.
            descripcion (str): La descripción del producto.
            cantidad (int): La cantidad disponible del producto.
            precio (float): El precio unitario del producto.
        """
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.precio = precio

    def obtener_informacion(self):
        """
        Obtiene la información del producto.

        Returns:
            str: La información del producto formateada.
        """
        return f"ID: {self.id}, Nombre: {self.nombre}, Descripción: {self.descripcion}, Cantidad: {self.cantidad}, Precio: {self.precio}"

    def modificar_cantidad(self, cantidad):
        """
        Modifica la cantidad del producto.

        Args:
            cantidad (int): La nueva cantidad del producto.
        """
        self.cantidad = cantidad

    def modificar_precio(self, precio):
        """
        Modifica el precio del producto.

        Args:
            precio (float): El nuevo precio del producto.
        """
        self.precio = precio
