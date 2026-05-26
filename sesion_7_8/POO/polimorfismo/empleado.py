class Empleado:
    def __init__(self, nombre, horas_trabajadas):
        self.nombre = nombre
        self.horas_trabajadas = horas_trabajadas

    def calcular_salario(self):
        print("Cada tipo de empleado debe implementar calcular_salario()")


class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, horas_trabajadas, precio_hora):
        super().__init__(nombre, horas_trabajadas)
        self.precio_hora = precio_hora
        
    def calcular_salario(self):
        return self.horas_trabajadas * self.precio_hora
    
class EmpleadoFijo(Empleado):
    def __init__(self, nombre, horas_trabajadas, salario_base, bonus_mensual):
        super().__init__(nombre, horas_trabajadas)
        self.salario_base = salario_base
        self.bonus_mensual = bonus_mensual

    def calcular_salario(self):
        return self.salario_base + self.bonus_mensual
    
class EmpleadoComisiones(Empleado):
    def __init__(self, nombre, horas_trabajadas, salario_base, ventas, porcentaje_comision):
        super().__init__(nombre, horas_trabajadas)
        self.salario_base = salario_base
        self.ventas = ventas
        self.porcentaje_comision = porcentaje_comision

    def calcular_salario(self):
        return self.salario_base + self.ventas * self.porcentaje_comision