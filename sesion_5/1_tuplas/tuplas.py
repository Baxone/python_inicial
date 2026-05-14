#una tupla es una lista de valores inmutable, no se pueden ni añadir ni modificar nada. Proteger los datos que hay dentro.

# una tupla se usa para guardar informacion como los datos de conexion a una BBDD o una API o un ruta a un carpeta. Tambien se usa mucho en devolución de funciones.


tupla = ('Juan', 44, True)
frutas = ('naranjas', 'manzanas', 'peras', 'platanos')
tupla_unica = ('juan',)

print(tupla)
print(frutas)
print(tupla_unica)

#longitud
print(len(tupla)) # 3
print(len(frutas)) # 4
print(len(tupla_unica)) #1

#imprimir cualquier valor de la tupla
print( frutas[2] ) # peras
print( frutas[-1] ) # platanos

#copias tuplas
otra_tupla = frutas[0:2]
otra_tupla2 = tupla

print(otra_tupla)
print(otra_tupla2)

print( frutas[0:3:2] )  # naranjas, peras

for i in range(0, len(frutas)):
    print(frutas[i])

print('------------')

for fruta in frutas:
    print(fruta)
    
# ERROR intentar modificar la tupla tanto en longitud como en valores.
# fruta[0] = 'Mandarina'

# eliminar 
del frutas
#print(frutas)

def recoger_datos():
    nombre = input('Dime tu nombre:' )
    edad = int( input('Dime tu edad: ') )
    return nombre, edad

print(recoger_datos())