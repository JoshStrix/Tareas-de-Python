import psycopg

# Función para conectar a la base de datos
def conectar():
    try:
        conexion = psycopg.connect(
            host="localhost",
            dbname="esports_db",
            user="postgres",
            password="root"
        )
        return conexion
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

# Crear tablas (si no existen)
def crear_tablas():
    conexion = conectar()
    if conexion:
        try:
            with conexion.cursor() as cursor:
                # Tabla equipos
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS equipos (
                        id INTEGER PRIMARY KEY,
                        nombre TEXT NOT NULL UNIQUE,
                        pais TEXT,
                        entrenador TEXT
                    )
                """)
                # Tabla jugadores con ON DELETE CASCADE
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS jugadores (
                        id SERIAL PRIMARY KEY,
                        nickname TEXT NOT NULL UNIQUE,
                        rol TEXT NOT NULL,
                        equipo_id INTEGER REFERENCES equipos(id) ON DELETE CASCADE
                    )
                """)
                conexion.commit()
                print("Tablas creadas exitosamente.")
        except psycopg.Error as e:
            print(f"Error al crear tablas: {e}")
        finally:
            conexion.close()

# Operaciones CRUD para equipos
def crear_equipo(id_equipo, nombre, pais, entrenador):
    conexion = conectar()
    if conexion:
        try:
            with conexion.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO equipos (id, nombre, pais, entrenador) VALUES (%s, %s, %s, %s)",
                    (id_equipo, nombre, pais, entrenador)
                )
                conexion.commit()
                print("Equipo creado exitosamente.")
        except psycopg.Error as e:
            print(f"Error al crear equipo: {e}")
        finally:
            conexion.close()

def leer_equipos():
    conexion = conectar()
    if conexion:
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT id, nombre, pais, entrenador FROM equipos")
                equipos = cursor.fetchall()
                if equipos:
                    print("\n--- Lista de Equipos ---")
                    for equipo in equipos:
                        print(f"ID: {equipo[0]} | Nombre: {equipo[1]} | País: {equipo[2]} | Entrenador: {equipo[3]}")
                else:
                    print("No hay equipos registrados.")
        except psycopg.Error as e:
            print(f"Error al leer equipos: {e}")
        finally:
            conexion.close()

def actualizar_equipo(id_equipo, nuevo_nombre):
    conexion = conectar()
    if conexion:
        try:
            with conexion.cursor() as cursor:
                cursor.execute(
                    "UPDATE equipos SET nombre = %s WHERE id = %s",
                    (nuevo_nombre, id_equipo)
                )
                conexion.commit()
                print("Equipo actualizado exitosamente.")
        except psycopg.Error as e:
            print(f"Error al actualizar equipo: {e}")
        finally:
            conexion.close()

def eliminar_equipo(id_equipo):
    conexion = conectar()
    if conexion:
        try:
            with conexion.cursor() as cursor:
                cursor.execute("DELETE FROM equipos WHERE id = %s", (id_equipo,))
                conexion.commit()
                print("Equipo eliminado exitosamente.")
        except psycopg.Error as e:
            print(f"Error al eliminar equipo: {e}")
        finally:
            conexion.close()

# Operaciones CRUD para jugadores
def crear_jugador(nickname, rol, equipo_id):
    conexion = conectar()
    if conexion:
        try:
            with conexion.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO jugadores (nickname, rol, equipo_id) VALUES (%s, %s, %s)",
                    (nickname, rol, equipo_id)
                )
                conexion.commit()
                print("Jugador creado exitosamente.")
        except psycopg.Error as e:
            print(f"Error al crear jugador: {e}")
        finally:
            conexion.close()

def leer_jugadores():
    conexion = conectar()
    if conexion:
        try:
            with conexion.cursor() as cursor:
                cursor.execute("""
                    SELECT j.nickname, j.rol, e.nombre 
                    FROM jugadores j 
                    LEFT JOIN equipos e ON j.equipo_id = e.id
                """)
                jugadores = cursor.fetchall()
                if jugadores:
                    print("\n--- Lista de Jugadores ---")
                    for jugador in jugadores:
                        print(f"Nickname: {jugador[0]} | Rol: {jugador[1]} | Equipo: {jugador[2]}")
                else:
                    print("No hay jugadores registrados.")
        except psycopg.Error as e:
            print(f"Error al leer jugadores: {e}")
        finally:
            conexion.close()


def menu():
    crear_tablas()
    while True:
        print("\n--- Gestión de eSports ---")
        print("1. Crear equipo")
        print("2. Crear jugador")
        print("3. Mostrar equipos")
        print("4. Mostrar jugadores")
        print("5. Actualizar nombre de equipo")
        print("6. Eliminar equipo")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_equipo = int(input("ID del equipo: "))
            nombre = input("Nombre del equipo: ")
            pais = input("País: ")
            entrenador = input("Entrenador: ")
            crear_equipo(id_equipo, nombre, pais, entrenador)
        elif opcion == "2":
            nickname = input("Nickname: ")
            rol = input("Rol: ")
            equipo_id = int(input("ID del equipo: "))
            crear_jugador(nickname, rol, equipo_id)
        elif opcion == "3":
            leer_equipos()
        elif opcion == "4":
            leer_jugadores()
        elif opcion == "5":
            id_equipo = int(input("ID del equipo a actualizar: "))
            nuevo_nombre = input("Nuevo nombre: ")
            actualizar_equipo(id_equipo, nuevo_nombre)
        elif opcion == "6":
            id_equipo = int(input("ID del equipo a eliminar: "))
            eliminar_equipo(id_equipo)
        elif opcion == "7":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()