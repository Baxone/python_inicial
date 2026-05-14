# lista son un cojunto de elementos casi siempre del mismo tipo 
lista_nombres = ['Carlos', 'Pedro', 'Juan']
lista = ['Carlos', 32, True]

#longitud
print( len(lista) ) #3

#imprimir un valor
print( lista_nombres[1] ) # Pedro

nombre_nuevo = 'Maria'
lista_nombres.append(nombre_nuevo)
print(lista_nombres)

# modificar un elemento
lista_nombres[0] = 'Santiago'

print(lista_nombres)

# añadir elementos en cualquier posicion
lista_nombres.insert(1, 'Natalia')
print(lista_nombres)

# borrar, funcion o efecto pringle. pop()
valor = lista_nombres.pop()
print(valor)
print(lista_nombres)

# borrar en cualquier posicion pop(2)
valor2 = lista_nombres.pop(2)
print(valor2)
print(lista_nombres)

print(lista_nombres[2])
print(lista_nombres[0:2])

# pasos por valor y por referencia

# paso por valor una variable le paso su espacio a en memoria a otra
nombre = 'Juan'
otro_nombre = nombre
nombre = 'Natalia'
print(nombre, otro_nombre)

# paso por referencia
lista1 = ['pepe','juan','teresa']
lista2 = lista1
lista1[1] = 'mac'
print(lista1)
print(lista2)

# romper esta paso por referencia y crear una copia
lista1 = ['pepe','juan','teresa']
lista2 = lista1.copy() # lista2 = lista1[:]
lista1[1] = 'mac'
print(lista1)
print(lista2)


# copiar parte de la lista
lista3 = lista1[0:2]
lista1[0]='maria'
print(lista3)
print(lista1)