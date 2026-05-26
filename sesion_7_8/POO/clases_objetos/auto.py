class Auto:
    # propiedades o caracteristicas del auto
    color = ""
    precio = 0
    combustible = ""
    motorizacion = ""
    matricula = ""
    estado = ""
    velocidad = 0
        
    # funcionalidades del auto - metodos o acciones
    # funcion inicializa el objeto es la que usamos para dar valores a las propiedades anterios.
    # a todas sin excepcion las funciones de objetos se les pasa como parametro el propio objeto
    def __init__(self, color, precio, matricula, combustible, motorizacion="100cv"):
        # inicializar los valores de las propiedades en función de los parametros.
        self.color = color
        self.precio = precio
        self.__matricula = matricula
        self.combustible = combustible
        self.motorizacion = motorizacion
        self.estado = 'apagado'
        
    def arrancar(self):
        self.estado = 'encendido'
        print('BRRRRRRRRRRRR vamos a darle beluga al buga')

    # getter o setter que son funciones dentro de mi clase que me permiten o bin visualizar la propiedad protegida o bien modificarla. Se puede solo visualizar y no modificar.
    def get_matricula(self):
        return self.__matricula

    def set_matricula(self, matricula):
        self.__matricula = matricula
        
    def acelerar(self, velocidad):
        self.velocidad += velocidad
        

ferrari = Auto('rojo', 75000, '2445-NHL', 'gasolia', '300cv')
fiat = Auto('vino',  1500, 'M-78654-DF', 'diesel', '55cv')

ferrari.set_matricula('6666-MAC')
print(ferrari.get_matricula())

fiat.arrancar()
print(fiat.estado)

fiat.acelerar(100)
print(fiat.velocidad)