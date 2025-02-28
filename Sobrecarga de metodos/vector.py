class Vector:
    @staticmethod
    def calcular_norma(x, y, z=None):
        if z is None:
            return (x**2 + y**2) ** 0.5
        return (x**2 + y**2 + z**2) ** 0.5