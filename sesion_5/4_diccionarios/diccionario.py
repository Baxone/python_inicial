# Diccionario: lista de elementos que en otros lenguajes de programacion se conoce como array asociativo. Se elimina el concepto de posicion para introducir el concepto clave:valor

alumno = {
    'nombre': 'Juan Antonio',
    'edad': 42,
    'estado': True,
    'dni': '345678X'
} 

print(alumno['nombre'])
# getters
print(alumno.get('dni'))


# como recorremos algo que no tiene posicion
print( alumno.values()) 
print( alumno.keys()) 
print( alumno.items()) 
print( "=" * 20)


for key in alumno.keys():
    print(key)
    
print( "=" * 20)

for value in alumno.values():
    print(value)
    
print( "=" * 20)

for key, value in alumno.items():
    print(f"{key}: {value}")
    
# modificable
alumno['nombre'] = 'Almudena'
print(alumno)

# insertar otros valores.
alumno['direccion'] = 'Calle numero piso y puerta'
print(alumno)

# eliminar un contenido por su clave
alumno.pop('direccion')
print(alumno)

#vaciar el diccionario
alumno.clear()
print(alumno)

#borrar el diccionario
del(alumno)



