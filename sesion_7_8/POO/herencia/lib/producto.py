class Producto:
    nombre = ""
    precio = 0
    
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        
    def mostrar_pvp(self, iva):
        impuesto = iva / 100  # 0.21
        precio_final = self.precio * (1 + impuesto)
        print(f'El precio del {self.nombre} con IVA es: {round(precio_final, 2)}€')