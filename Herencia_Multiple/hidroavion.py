from navegable import Navegable
from volador import Volador

class Hidroavion(Navegable, Volador):
    def navegar(self):
        return "El hidroavion esta navegando"
    
    def volar(self):
        return "El hidroavion esta volando"