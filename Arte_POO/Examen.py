class Artista:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.obras = []

    def crear_obra(self, obra):
        if not isinstance(obra, ObraDeArte):
            raise TypeError("La obra debe ser una instancia de ObraDeArte o sus subclases.")
        self.obras.append(obra)
        obra.artista = self

class ObraDeArte:
    def __init__(self, titulo, año_creacion, valor):
        self.titulo = titulo
        self.año_creacion = año_creacion
        self.valor = valor
        self.artista = None

    def mostrar_info(self):
        info = f"Título: {self.titulo}\nAño: {self.año_creacion}\nValor: ${self.valor:,}"
        if self.artista:
            info += f"\nArtista: {self.artista.nombre}"
        return info

class Pintura(ObraDeArte):
    def __init__(self, titulo, año_creacion, valor, tecnica):
        super().__init__(titulo, año_creacion, valor)
        self.tecnica = tecnica

    def mostrar_info(self):
        return super().mostrar_info() + f"\nTécnica: {self.tecnica}"

class Escultura(ObraDeArte):
    def __init__(self, titulo, año_creacion, valor, material):
        super().__init__(titulo, año_creacion, valor)
        self.material = material

    def mostrar_info(self):
        return super().mostrar_info() + f"\nMaterial: {self.material}"

class Fotografia(ObraDeArte):
    def __init__(self, titulo, año_creacion, valor, tamano_mpx):
        super().__init__(titulo, año_creacion, valor)
        self.tamano_mpx = tamano_mpx

    def mostrar_info(self):
        return super().mostrar_info() + f"\nTamaño: {self.tamano_mpx} MPX"

class ObraMaestra(ObraDeArte):
    def __init__(self, titulo, año_creacion, valor, tecnica, material, reconocimiento):
        super().__init__(titulo, año_creacion, valor)
        self.tecnica = tecnica
        self.material = material
        self.reconocimiento = reconocimiento

    def mostrar_info(self):
        base_info = super().mostrar_info()
        return f"{base_info}\nTécnica: {self.tecnica}\nMaterial: {self.material}\nReconocimientos: {self.reconocimiento}"

class Exposicion:
    def __init__(self, nombre, fecha_inicio, fecha_fin):
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.obras = []

    def agregar_obra(self, obra):
        if not isinstance(obra, ObraDeArte):
            raise TypeError("La obra debe ser una instancia de ObraDeArte o sus subclases.")
        self.obras.append(obra)

    def calcular_valor_total(self):
        return sum(obra.valor for obra in self.obras)

    def mostrar_info(self):
        info = f"Exposición: {self.nombre}\nFecha: {self.fecha_inicio} - {self.fecha_fin}"
        info += f"\nValor total: ${self.calcular_valor_total():,}\nObras:"
        for obra in self.obras:
            info += f"\n\n{obra.mostrar_info()}"
        return info

if __name__ == "__main__":
    # Crear artistas
    van_gogh = Artista("Vincent van Gogh", "Holandés")
    michelangelo = Artista("Michelangelo", "Italiano")
    picasso = Artista("Pablo Picasso", "Español")
    frida = Artista("Frida Kahlo", "Mexicana")
    dali = Artista("Salvador Dalí", "Español")
    da_vinci = Artista("Leonardo da Vinci", "Italiano")
    rodin = Artista("Auguste Rodin", "Francés")
    ansel_adams = Artista("Ansel Adams", "Estadounidense")

    # Crear obras de arte
    noche_estrellada = Pintura("La noche estrellada", 1889, 1000000, "Óleo")
    david = Escultura("David", 1504, 5000000, "Mármol")
    guernica = Pintura("Guernica", 1937, 200000000, "Óleo sobre lienzo")
    demoiselles = Pintura("Les Demoiselles d'Avignon", 1907, 150000000, "Óleo")
    las_dos_fridas = Pintura("Las dos Fridas", 1939, 10000000, "Óleo sobre lienzo")
    autorretrato = Pintura("Autorretrato con collar de espinas", 1940, 5000000, "Óleo")
    persistencia = Pintura("La persistencia de la memoria", 1931, 150000000, "Óleo")
    sueno_abeja = Pintura("Sueño causado por el vuelo de una abeja", 1944, 80000000, "Óleo")
    mona_lisa = Pintura("La Mona Lisa", 1503, 860000000, "Óleo sobre álamo")
    ultima_cena = Pintura("La última cena", 1498, 450000000, "Témpera sobre yeso")
    pensador = Escultura("El Pensador", 1904, 15000000, "Bronce")
    yosemite = Fotografia("Clearing Winter Storm, Yosemite", 1937, 1500000, 50.3)
    
    # Obra Maestra
    gioconda_escultura = ObraMaestra(
        "La Gioconda en Mármol",
        2020,
        25000000,
        "Óleo y cincelado",
        "Mármol de Carrara",
        "Premio UNESCO a la Innovación Artística"
    )

    # Asignar obras a artistas
    van_gogh.crear_obra(noche_estrellada)
    michelangelo.crear_obra(david)
    picasso.crear_obra(guernica)
    picasso.crear_obra(demoiselles)
    frida.crear_obra(las_dos_fridas)
    frida.crear_obra(autorretrato)
    dali.crear_obra(persistencia)
    dali.crear_obra(sueno_abeja)
    da_vinci.crear_obra(mona_lisa)
    da_vinci.crear_obra(ultima_cena)
    da_vinci.crear_obra(gioconda_escultura)
    rodin.crear_obra(pensador)
    ansel_adams.crear_obra(yosemite)

    # Crear exposiciones
    expo_renacimiento = Exposicion("Arte del Renacimiento", "2025-05-01", "2025-12-31")
    expo_modernismo = Exposicion("Vanguardias del Siglo XX", "2025-06-01", "2025-12-31")

    # Agregar obras a exposiciones
    obras_renacimiento = [noche_estrellada, david, mona_lisa, ultima_cena, gioconda_escultura]
    for obra in obras_renacimiento:
        expo_renacimiento.agregar_obra(obra)
    
    obras_modernismo = [guernica, demoiselles, persistencia, las_dos_fridas, pensador, yosemite]
    for obra in obras_modernismo:
        expo_modernismo.agregar_obra(obra)

    # Mostrar información
    print("=== Artistas y sus Obras ===")
    artistas = [van_gogh, michelangelo, picasso, frida, dali, da_vinci, rodin, ansel_adams]
    for artista in artistas:
        print(f"\n{artista.nombre} ({artista.nacionalidad})")
        for obra in artista.obras:
            print(f"- {obra.titulo} ({obra.__class__.__name__})")

    print("\n=== Obras Destacadas ===")
    print(gioconda_escultura.mostrar_info())
    print("\n" + yosemite.mostrar_info())
    print("\n" + pensador.mostrar_info())

    print("\n=== Exposiciones ===")
    print(expo_renacimiento.mostrar_info())
    print("\n" + expo_modernismo.mostrar_info())