# Un set es un conjunto ordenado de elementos UNICOS. Se utiliza para eleminar elementos duplicados de una lista.

lista = [1,1,1,2,2,2,2,3,3,4,5,6,7,6,3,8,6]
print(lista)
conjunto = set(lista)

lista_elementos_unicos = list(conjunto)
print(lista_elementos_unicos)

# frutas
frutas = {'melon', 'sandia', 'platano', 'pera', 'melon'}
print(frutas)

#  el orden del es aleatorio, esto complica mucho el manejo de estos elemento por posición

#agregar elementos a un set. OJO siempre que no este duplicados.
frutas.add('manzana')
print(frutas)

# borrar elementos dentro de un set que sepamos de forma segura que existen dentro de la lista.
frutas.remove('manzana')
print(frutas)

# discard me permite borrar un elemento del conjunto si existe si no existe no me da error
frutas.discard('sandia')
print(frutas)

##vaciar un set y eleminarlo
frutas.clear() #{}
del frutas # eliminarlo