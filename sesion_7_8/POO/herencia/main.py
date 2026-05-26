from lib.producto import Producto
from lib.comida import Comida

def main():
    camisa = Producto('camisa', 12.90)
    camisa.mostrar_pvp(21)
    
    huevos = Comida('huevos', 3.5, '2026/06/12')
    huevos.mostrar_pvp(4)
    huevos.mostrar_info()
    

main()