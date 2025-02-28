from empleado_abstracto import Empleado

class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, sueldo_mensual):
        self.nombre = nombre
        self.sueldo_mensual = sueldo_mensual

    def calcular_sueldo(self):
        return self.sueldo_mensual()
    
    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Sueldo: {self.sueldo_mensual}"