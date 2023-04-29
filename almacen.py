from producto import Producto

class Almacen:
    def __init__(self):
        self.lista_productos = []


    # Funciones
    def listar_producto(self):
        for item in self.lista_productos:
            print(item)

    def agregar_producto(self, item):
        self.lista_productos.append(item)

    def buscar_producto(self, item):
        productos_encontrados = []
        for abarrote in self.lista_productos:
            if abarrote.nombre == item:
                productos_encontrados.append(abarrote)
        return productos_encontrados
    
    def eliminar_producto(self, item):
        #Utilizo la funcion ya existente para buscar
        resultado_busqueda = self.buscar_producto(item)
        if len(resultado_busqueda) == 0:
            print("No se encontraron productos.")
        else:
            for item in resultado_busqueda:
                print(f"Se ha eliminado el producto {item}")
                self.lista_productos.remove(item)

    def modificar_producto(self, item):
        #Utilizo la funcion ya existente para buscar
        resultado_busqueda = self.buscar_producto(item)
        if len(resultado_busqueda) == 0:
            print("No se encontraron productos.")
        else:
            for item in resultado_busqueda:
                print(f"Seleccione el parametro a modificar del producto {item}")
                print("1.- Nombre")
                print("2.- Descripcion")
                print("3.- Precio")
                print("4.- Fecha de vencimiento")
                opcion = input("Ingrese una opcion: ")
                if opcion == "1":
                    parametro = input("Ingrese el nuevo nombre: ")
                    item.nombre = parametro
                elif opcion == "2":
                    parametro = input("Ingrese la nueva descripcion: ")
                    item.descripcion = parametro
                elif opcion == "3":
                    parametro = input("Ingrese el nuevo precio: ")
                    item.precio = parametro
                elif opcion == "4":
                    parametro = input("Ingrese la nueva fecha de vencimiento: ")
                    item.vencimiento = parametro
                else:
                    print("Opcion invalida.")
                print(f"El producto se ha modificado a:  {item}")

    def cargar_desde_archivo(self, nombre_archivo):
        with open(nombre_archivo, "r") as f:
            for linea in f:
                if linea != "\n":
                    campos = linea.strip().split(",")
                    nombre = campos[0]
                    descripcion = campos[1]
                    precio = campos[2]
                    vencimiento = campos[3]
                    objeto_producto = Producto(nombre, descripcion, precio, vencimiento)
                    self.agregar_producto(objeto_producto)