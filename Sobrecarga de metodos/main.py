from vector import Vector
from transformador import Transformador

print("Norma 2D:", Vector.calcular_norma(3,4))
print("Norma 3D:", Vector.calcular_norma(1,2,2))
datos = [1,2,3]
print("Suma:", Transformador.transformar(datos))
print("Multiplicacion:", Transformador.transformar(datos, 2))