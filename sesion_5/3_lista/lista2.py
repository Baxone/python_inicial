nombres = ['Juan antonio', 'Manuel', 'Marta', 'Lucia', 'Elena', 'Miguel']

# insertar varios a nombre a la vez
nombres.extend(['Maria', 'Joaquin'])

print(nombres)

# insertar en cualquier posicion
nombres.insert(2, 'Jorge')
print(nombres)


# eliminar por contenido, obviamente teniendo el tema mayusculas y minisculas.

nombres.remove('joaquin'.title())
print(nombres)

# recorrerlo una lista
for nombre in nombres:
    print(f'####. {nombre.title()} .####')