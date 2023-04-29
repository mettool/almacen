# Clase producto
# - Nombre del producto <- string
# - Descripcion <- string
# - Precio <- float
# - Fecha de vencimiento <- string
# Tendra solo 1 metodo que devolvera la descripcion del producto

class Producto:
    def __init__(self, nombre, descripcion, precio, vencimiento):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.vencimiento = vencimiento

    def __str__(self):
        return f"{self.nombre} - {self.descripcion} - {self.precio} - {self.vencimiento}"