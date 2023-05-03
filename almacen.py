from producto import Producto
import random

class Almacen:
    def __init__(self):
        self.lista_productos = {}


    # Funciones
    def listar_producto(self):
        for sku, item in self.lista_productos.items():
            print(f"{sku}: {item}")

    def agregar_producto(self, item):
        sku = random.randint(1000, 1999)
        self.lista_productos[sku] = item

    def buscar_producto(self, item):
        productos_encontrados = {}
        for sku, abarrote in self.lista_productos.items():
            if abarrote.nombre == item:
                productos_encontrados[sku] = abarrote
        return productos_encontrados
    
    def eliminar_producto(self, item):
        #Utilizo la funcion ya existente para buscar
        resultado_busqueda = self.buscar_producto(item)
        if len(resultado_busqueda) == 0:
            print("No se encontraron productos.")
        else:
            for sku, item in resultado_busqueda.items():
                print(f"Se ha eliminado el producto {sku}: {self.lista_productos.pop(sku)}")
                

    def modificar_producto(self, item):
        #Utilizo la funcion ya existente para buscar
        resultado_busqueda = self.buscar_producto(item)
        if len(resultado_busqueda) == 0:
            print("No se encontraron productos.")
        else:
            for sku, item in resultado_busqueda.items():
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
                print(f"El producto se ha modificado a: {sku}: {item}")

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