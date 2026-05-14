productos = [
    {
        'nombre': 'Leche desnatada',
        'precio': 2,
        'cantidad': 12
    },
    {
        'nombre': 'Cereales',
        'precio': 8,
        'cantidad': 2
    },
    {
        'nombre': 'Pescado',
        'precio': 22,
        'cantidad': 1
    },
]

#print( len(productos) )

#print(productos[0]) # diccionario completo
#print(productos[0]['nombre']) # leche


def pintar_lista(lista):
    for producto in lista:
        print('-' * 30)
        print(f"{producto['nombre']} => precio: {producto['precio'] * producto['cantidad']} euros")
    

pintar_lista(productos)

# añadais tres productos a lista, y filtreis una lista con todo los producto cuya cantidad se mayor que 0.