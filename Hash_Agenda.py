class AgendaTelefonica:
    def __init__(self):
        self.tabla = {}  # Diccionario como tabla hash

    def agregar_contacto(self, nombre, numero):
        """
        Agrega un contacto a la tabla hash.
        """
        if nombre in self.tabla:
            print(f"El contacto '{nombre}' ya existe. Actualizando número...")
        self.tabla[nombre] = numero
        print(f"Contacto agregado o actualizado: {nombre} -> {numero}")

    def buscar_contacto(self, nombre):
        """
        Busca un contacto en la tabla hash por nombre.
        """
        if nombre in self.tabla:
            return f"{nombre}: {self.tabla[nombre]}"
        else:
            return f"El contacto '{nombre}' no existe."

    def eliminar_contacto(self, nombre):
        """
        Elimina un contacto de la tabla hash por nombre.
        """
        if nombre in self.tabla:
            del self.tabla[nombre]
            print(f"El contacto '{nombre}' ha sido eliminado.")
        else:
            print(f"El contacto '{nombre}' no existe en la agenda.")

    def mostrar_contactos(self):
        """
        Muestra todos los contactos almacenados.
        """
        if not self.tabla:
            print("La agenda está vacía.")
        else:
            print("\nContactos en la agenda:")
            for nombre, numero in self.tabla.items():
                print(f"{nombre}: {numero}")

# Programa principal
agenda = AgendaTelefonica()

while True:
    print("\nMenú de Agenda Telefónica:")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Eliminar contacto")
    print("4. Mostrar todos los contactos")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del contacto: ")
        numero = input(f"Ingrese el número de teléfono de {nombre}: ")
        agenda.agregar_contacto(nombre, numero)
    elif opcion == "2":
        nombre = input("Ingrese el nombre del contacto a buscar: ")
        print(agenda.buscar_contacto(nombre))
    elif opcion == "3":
        nombre = input("Ingrese el nombre del contacto a eliminar: ")
        agenda.eliminar_contacto(nombre)
    elif opcion == "4":
        agenda.mostrar_contactos()
    elif opcion == "5":
        print("¡Saliendo de la agenda telefónica!")
        break
    else:
        print("Opción no válida. Por favor, intente nuevamente.")
