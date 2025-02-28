from abc import ABC, abstractmethod

class Empleado(ABC):
    @abstractmethod
    def calcular_sueldo(self):
        pass

    @abstractmethod
    def mostrar_info(self):
        pass