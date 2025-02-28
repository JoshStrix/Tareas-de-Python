from desarrollador import Desarrollador
from diseñador import Diseñador
from gerente import Gerente

def mostrar_trabajo(empleados):
    for empleado in empleados:
        print(empleado.trabajar())

empleados = [
    Desarrollador(),
    Diseñador(),
    Gerente()
]

mostrar_trabajo(empleados)