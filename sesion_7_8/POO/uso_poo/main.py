from calculadora import Calculadora

def main():
    tipo = input('Que tipo de calculadora quieres: normal, cientifica: ')
    if tipo != 'normal' and tipo != 'cientifica':
        print('opcion no validada')
        main()
    else:
        casio = Calculadora(tipo)

    menu = f"""Bienvenido a mi calculadora {tipo}"""
    
    if tipo == 'normal':
        menu += """
[1]. sumar
[2]. restar
[3]. multiplicar
[x]. salir
        """
    else:
        menu += """
[1]. sumar
[2]. restar
[3]. multiplicar
[4]. potencia
[x]. salir
""" 
    print(menu)
    option = input('¿Qué opcion eliges?: ')
    
    if option == '1':
        n1 = float(input('dame un numero: '))
        n2 = float(input('dame otro numero: '))
        print(casio.sumar(n1, n2))
    elif option == '2':
        n1 = float(input('dame un numero: '))
        n2 = float(input('dame otro numero: '))
        print(casio.restar(n1,n2))
    elif option == '3':
        n1 = float(input('dame un numero: '))
        n2 = float(input('dame otro numero: '))
        n3 = float(input('dame otro numero: '))
        print(casio.multiplicar(n1,n2, n3))
    elif option == '4' and tipo == 'cientifica':
        base = float(input('dame la base: '))
        exponente = float(input('dame el exponente: '))
        print(casio.potencia(base, exponente))
    elif option == 'x':
        print('hasta pronto')
    else:
        print('opcion no valida')
        main()


main()