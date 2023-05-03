from producto import Producto
import random
# Clase menu

class Menu:
    
    # Constructor para crear el menu
    def __init__(self, almacen):
        self.almacen = almacen
    
    # Funcion para el menu
    def ejecutar_menu(self):
        while True:
            print("1.- Agregar productos")
            print("2.- Listar productos")
            print("3.- Buscar productos")
            print("4.- Crear reporte de productos")
            print("5.- Cargar desde archivo")
            print("6.- Eliminar producto")
            print("7.- Modificar producto")
            print("8.- Salir")
            opcion = input("Ingrese una opcion: ")
            if opcion == "1":
                self.agregar_item()
            elif opcion == "2":
                self.listar_item()
            elif opcion == "3":
                self.buscar_por_nombre()
            elif opcion == "4":
                self.crear_reporte()
            elif opcion == "5":
                self.carga_masiva()
            elif opcion == "6":
                self.eliminar_item()
            elif opcion == "7":
                self.modificar_item()
            elif opcion == "8":
                break
            else:
                print("Opcion invalida.")

    def agregar_item(self):
        # Crear un objeto "producto"
        nombre = input("Ingrese el nombre del producto: ")
        descripcion = input("Ingrese descripcion: ")
        precio = input("Ingrese precio: ")
        vencimiento = input("Ingrese fecha de vencimiento: ")

        objeto_producto = Producto(nombre, descripcion, precio, vencimiento)
        self.almacen.agregar_producto(objeto_producto)
        print("Producto agregado.")

    def listar_item(self):
        self.almacen.listar_producto()
    
    def buscar_por_nombre(self):
        nombre_abarrote = input("Ingrese el producto a buscar: ")
        resultado_busqueda = self.almacen.buscar_producto(nombre_abarrote)
        if len(resultado_busqueda) == 0:
            print("No se encontraron productos.")
        else:
            print(f"Se encontro el producto {nombre_abarrote}")
            for sku, abarrote in resultado_busqueda.items():
                print(f"{sku}: {abarrote}")
    
    def crear_reporte(self):
        nombre_archivo = input("Ingrese el nombre de su reporte: ")
        with open(nombre_archivo + ".txt", "w") as f:
            f.write("************ REPORTE DE ABARROTES ************" + "\n")
            for sku, producto in self.almacen.lista_productos.items():
                f.write(f"{sku}: {producto}\n")

    def carga_masiva(self):
        nombre_archivo = input("Ingrese nombre de archivo: ")
        self.almacen.cargar_desde_archivo(nombre_archivo)

    def eliminar_item(self):
        nombre_abarrote = input("Ingrese el producto a eliminar: ")
        self.almacen.eliminar_producto(nombre_abarrote)

    def modificar_item(self):
        nombre_abarrote = input("Ingrese el producto a modificar: ")
        self.almacen.modificar_producto(nombre_abarrote)