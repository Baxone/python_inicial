# dime si un alumno esta suspenso

nota = 20

if nota >= 0 and nota < 5:
    print('suspenso')
    
if nota >= 5 and nota <= 10:
    print('aprobados')
    
if nota < 0 or nota > 10:
    print('valor no valido')