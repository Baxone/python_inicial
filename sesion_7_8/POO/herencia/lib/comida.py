from .producto import Producto

# herencia, lo que representa esto es que Comida tiene todas las propiedas y funciones de producto
class Comida(Producto):
    fecha_caducidad = '0000/00/00'
    
    def __init__(self, nombre, precio, fecha_caducidad):
        super().__init__(nombre, precio) ## llamando a la funcion constructor del padre Producto
        self.fecha_caducidad = fecha_caducidad
        
    def mostrar_info(self):
        print(f"Producto: {self.nombre}, precio: {self.precio}€ y fecha de caducidad: {self.fecha_caducidad}")
        