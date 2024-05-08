from inventario import Inventario
from productos import Producto

def mostrar_menu():
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por ID")
    print("5. Listar todos los productos")
    print("6. Salir")

def main():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            descripcion = input("Ingrese la descripción del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(id, nombre, descripcion, cantidad, precio)
            inventario.agregar_producto(producto)
            print("Producto agregado correctamente.\n")

        elif opcion == "2":
            id = input("Ingrese el ID del producto a eliminar: ")
            try:
                inventario.eliminar_producto(id)
                print("Producto eliminado correctamente.\n")
            except ValueError as e:
                print(e)

        elif opcion == "3":
            id = input("Ingrese el ID del producto a actualizar: ")
            if id in inventario.productos:
                nuevo_id = input("Ingrese el nuevo ID del producto: ")
                nombre = input("Ingrese el nuevo nombre del producto: ")
                descripcion = input("Ingrese la nueva descripción del producto: ")
                cantidad = int(input("Ingrese la nueva cantidad del producto: "))
                precio = float(input("Ingrese el nuevo precio del producto: "))
                nuevo_producto = Producto(nuevo_id, nombre, descripcion, cantidad, precio)
                try:
                    inventario.actualizar_producto(id, nuevo_producto)
                    print("Producto actualizado correctamente.\n")
                except ValueError as e:
                    print(e)
            else:
                print("El producto no existe en el inventario.\n")

        elif opcion == "4":
            id = input("Ingrese el ID del producto a buscar: ")
            producto = inventario.buscar_producto_por_id(id)
            if producto:
                print(producto.obtener_informacion())
            else:
                print("Producto no encontrado.\n")

        elif opcion == "5":
            print(inventario.listar_productos())

        elif opcion == "6":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.\n")

if __name__ == "__main__":
    main()
