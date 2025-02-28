from empleado_abstracto import Empleado

class EmpleadoMedioTiempo(Empleado):
    def __init__(self, nombre, horas, pago_hora):
        self.nombre = nombre
        self.horas = horas
        self.pago_hora = pago_hora

    def calcular_sueldo(self):
        return self.horas * self.pago_hora
    
    def mostrar_info(self):
     return f"Nombre: {self.nombre}, Sueldo: {self.calcular_sueldo()}"