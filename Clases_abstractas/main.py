from empleado_tp import EmpleadoTiempoCompleto
from empleado_mt import EmpleadoMedioTiempo

empleado1 = EmpleadoTiempoCompleto("Ana Maria", 5000)
empleado2 = EmpleadoMedioTiempo("Jose Luis", 40, 20)

print(empleado1.mostrar_info())
print(empleado2.mostrar_info())