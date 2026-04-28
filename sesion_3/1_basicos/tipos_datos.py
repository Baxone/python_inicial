# variable es una reserva de un espacio en memoria. debe tener un nombre, y este ser significativo de lo que almacene
nombre_estudiante = "Juan Antonio"
print(nombre_estudiante)
# simulacion de constante que no existe python
NOMBRE_ALUMNO = 'alberto'
print(NOMBRE_ALUMNO)

#nombre_estudiante = 33
#print(nombre_estudiante)
edad = 44
# tipos datos básicos: 
# string - cadenas de caracteres
nombre_ciudad = "Madrid"
apellidos = 'Pérez'
nombre_completo = nombre_estudiante + " " + apellidos
#nombre_edad = nombre_estudiante + str(edad)
nombre_edad = f'El estudiante se llama {nombre_estudiante} y tiene {edad} años'
print(nombre_edad)
# numeros - int - float 

edad = 33 #int
precio = 39.90 # float - racional
temperatura = -20 # negativos

# booleanos
estado = True
activo = False

# conversiones

numero1 = int(39.90) # 39
numero2 = float(39) # 39.0
numero_texto = float('39.30')
texto = str(numero2)
print(texto)
print(numero_texto * 2)

numero3 = float(input('Dime numero: '))
print(type(numero3))
print( numero3 + numero2 )

numero4 = 39.909095
print(round(numero4, 2))


