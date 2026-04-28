# dime si un alumno esta suspenso

# el condicional simple con secuencia de escape el else es la salida a un valor no esperado. 

nota = 12
# ERROR - puede generar ambiguedad
if nota >= 5 and nota <= 10:
    print('aprobado')
else:
    print('suspenso')
    
# podemos usarlo cuando resultado sabemos a ciencia cierta que es binario

numero = 14
# correcto por que no genera ambiguedad
if numero % 2 == 0:
    print('par')
else:
    print('impar')