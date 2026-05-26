class Calculadora:
    marca = "Casio"
    tipo = ""  
    #como no tengo que inicializar ninguna propiedad no tengo obligacion de crear la funcion __init__ constructor. No es obligatoria en python
    def __init__(self, tipo = 'normal'):
        self.tipo = tipo
    
    def sumar(self, *numeros):
        suma = 0
        for numero in numeros:
            suma += numero
        return suma
    
    def restar(self, n1, n2):
        return n1 - n2 if n1 >= n2 else n2 - n1
    
    def multiplicar(self, n1, n2, n3):
        return n1 * n2 * n3
    
    
    def potencia(self, base, exp):
        if self.tipo == 'cientifica':
            return base ** exp
        else:
            return 'no es un calculadora cientifica no puedo hacer potencias'
    
    
