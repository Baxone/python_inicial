# operador ternario o condicional abreviado

numero1 = 13
resultado = ""

if numero1 % 2 == 0:
    resultado = 'par'
else:
    resultado = 'impar'    
    
print(resultado)

# siempre que tenga un condicional con escape donde una variable cambia de valor, podemos convertirlo en un condicional abreviado.

otro_resultado = 'par' if numero1 % 2 == 0 else 'impar'
print(otro_resultado)

estado_factura = input('como esta la factura: ')
mensaje = 'te enviamos el pedido' if estado_factura == 'pagada' else 'debes proceeder al pago'
print( mensaje )