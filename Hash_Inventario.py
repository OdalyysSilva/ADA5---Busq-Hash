class Inventario:
    def __init__(self):
        self.tabla = {}  # Diccionario como tabla hash

    def agregar_producto(self, producto, cantidad):
        """
        Agrega un producto al inventario o actualiza su cantidad.
        """
        if producto in self.tabla:
            self.tabla[producto] += cantidad
            print(f"Se actualizó el producto '{producto}' con {cantidad} más. Total: {self.tabla[producto]}")
        else:
            self.tabla[producto] = cantidad
            print(f"Producto '{producto}' agregado con cantidad: {cantidad}")

    def consultar_producto(self, producto):
        """
        Consulta la cantidad disponible de un producto.
        """
        if producto in self.tabla:
            return f"El producto '{producto}' tiene {self.tabla[producto]} unidades disponibles."
        else:
            return f"El producto '{producto}' no está en el inventario."

    def eliminar_producto(self, producto):
        """
        Elimina un producto del inventario.
        """
        if producto in self.tabla:
            del self.tabla[producto]
            print(f"Producto '{producto}' eliminado del inventario.")
        else:
            print(f"El producto '{producto}' no se encuentra en el inventario.")

    def mostrar_inventario(self):
        """
        Muestra todo el inventario.
        """
        if not self.tabla:
            print("El inventario está vacío.")
        else:
            print("\nInventario actual:")
            for producto, cantidad in self.tabla.items():
                print(f"{producto}: {cantidad} unidades")


# Programa principal
inventario = Inventario()

while True:
    print("\nMenú de Inventario:")
    print("1. Agregar producto")
    print("2. Consultar producto")
    print("3. Eliminar producto")
    print("4. Mostrar inventario")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        producto = input("Ingrese el nombre del producto: ")
        cantidad = int(input(f"Ingrese la cantidad de '{producto}': "))
        inventario.agregar_producto(producto, cantidad)
    elif opcion == "2":
        producto = input("Ingrese el nombre del producto a consultar: ")
        print(inventario.consultar_producto(producto))
    elif opcion == "3":
        producto = input("Ingrese el nombre del producto a eliminar: ")
        inventario.eliminar_producto(producto)
    elif opcion == "4":
        inventario.mostrar_inventario()
    elif opcion == "5":
        print("¡Saliendo del programa!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción del menú.")
