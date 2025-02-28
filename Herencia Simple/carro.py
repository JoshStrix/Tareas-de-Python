from vehiculo import Vehiculo

class Carro(Vehiculo):
    def arrancar(self):
        return "El carro esta arrancando."
    
    def parar(self):
        return "El carro se esta deteniendo."