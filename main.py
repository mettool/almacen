from almacen import Almacen
from producto import Producto
from menu import Menu

obj_almacen = Almacen()
obj_menu = Menu(obj_almacen)
obj_menu.ejecutar_menu()