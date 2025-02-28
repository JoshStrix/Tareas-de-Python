class Transformador:
    @staticmethod
    def transformar(datos, factor=None):
        if factor is None:
            return sum(datos)
        return [dato * factor for dato in datos]