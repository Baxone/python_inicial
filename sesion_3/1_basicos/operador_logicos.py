# operadores logicos tb devuelven Treu a False

# AND (y), OR (o), NOT (negación)

# AND quiero encontrar un movil que tenga un precio 200 y de marca apple
precio = 400
marca = "apple"

resultado = precio <= 200 and marca == 'apple'
print(resultado)
#AND
# FALSE and FALSE => FALSE
# FALSE and TRUE => FALSE
# TRUE and FALSE => FALSE
# TRUE and TRUE => TRUE

print('--------')
# OR quiero encontrar un movil que tenga un precio 200 ó de la marca apple
resultado = precio <= 200 or marca == 'apple'
print(resultado)
#OR
# FALSE or FALSE => FALSE
# FALSE or TRUE => TRUE
# TRUE or FALSE => TRUE
# TRUE or TRUE => TRUE
print('--------')
# not negacion sirve para negar una afirmacion o activar un negacion
estado_activo = True
print(estado_activo)
print(not estado_activo)

