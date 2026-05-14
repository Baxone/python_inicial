lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

lista_numereritos = [12.4,13,56756,45,6778,78,435,6,78,89]

# sacar una lista de numeros impares

def filtra_lista_paridad(lista, tipo):
    lista_resultante = []
    for numero in lista:
        if numero % 2 != 0 and tipo == 'impar':
            lista_resultante.append(numero)
        elif numero % 2 == 0 and tipo == 'par':
            lista_resultante.append(numero)
    return lista_resultante
        
#lista_pares = filtra_lista_paridad(lista_numeros, 'par')
lista_pares = filtra_lista_paridad(lista_numereritos, 'par')

print(lista_pares)

        
        
def filtrar_pares(lista):
    lista_resultante = []
    for numero in lista:
        if numero % 2 == 0:
            lista_resultante.append(numero)
    return lista_resultante

    
def filtrar_impares(lista):
    lista_resultante = []
    for numero in lista:
        if numero % 2 != 0:
            lista_resultante.append(numero)
    return lista_resultante
        
        