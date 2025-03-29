============================================
GESTIÓN DE EQUIPOS Y JUGADORES DE ESPORTS
============================================

Este proyecto permite gestionar equipos y jugadores de una liga de eSports mediante operaciones CRUD (Crear, Leer, Actualizar, Eliminar) usando PostgreSQL y Python.

-------------------------
REQUISITOS PREVIOS
-------------------------
1. **PostgreSQL**: Instalado y en ejecución.
2. **Python 3.x**: Descargar desde https://www.python.org/.
3. **psycopg3**: Librería para conectar Python con PostgreSQL.
4. **Git** (opcional): Para clonar el repositorio.

-------------------------
INSTALACIÓN Y CONFIGURACIÓN
-------------------------

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/JoshStrix/Tareas-de-Python/tree/257dcbe16bbd7b451bf7a554f80e6ba63a3d366e/CRUD%20Python
   cd esports-crud

2. Crear la base de datos:

Abre PostgreSQL (pgAdmin o psql) y ejecuta:
CREATE DATABASE esports_db;

3. Configurar credenciales:

Edita el archivo esports.py y modifica los valores en la función conectar():

conexion = psycopg.connect(
    host="localhost",
    dbname="esports_db",
    user="postgres",       # Usuario de tu PostgreSQL
    password="tu_contraseña" # Contraseña de tu PostgreSQL
)

4. Instalar dependencias (usar entorno virtual recomendado):

python -m venv venv

# Windows:
.\venv\Scripts\activate

# Linux/macOS:
source venv/bin/activate

#instalar esta libreria despues de tener el entorno virtual activado:
pip install psycopg[binary]

====================================================================================================

EJECUCION DE LA APLICACION

1. Iniciar el programa:
python esports.py

2. Menu de opciones:

--- Gestión de eSports ---
1. Crear equipo
2. Crear jugador
3. Mostrar equipos
4. Mostrar jugadores
5. Actualizar nombre de equipo
6. Eliminar equipo
7. Salir

INSTRUCCIONES DE USO
Crear equipo (Opción 1):

Ingresa un ID único, nombre, país y entrenador.
Ejemplo:

ID del equipo: 101
Nombre del equipo: Team Phoenix
País: España
Entrenador: Ana López

Crear jugador (Opción 2):

Proporciona nickname, rol y ID del equipo existente.
Ejemplo:

Nickname: Shadow
Rol: Sniper
ID del equipo: 101

Mostrar equipos/jugadores (Opciones 3 y 4):

Lista todos los registros almacenados.

Actualizar equipo (Opción 5):

Ingresa el ID del equipo y su nuevo nombre.
Ejemplo:

ID del equipo a actualizar: 101
Nuevo nombre: Team Dragon

Eliminar equipo (Opción 6):

Elimina un equipo y sus jugadores asociados.
Ejemplo:

ID del equipo a eliminar: 101

SOLUCIÓN DE PROBLEMAS COMUNES
Error de autenticación:

Verifica la contraseña en esports.py y configura pg_hba.conf para usar md5 (ver guía anterior).

Tablas no creadas:

Ejecuta manualmente en PostgreSQL:

CREATE TABLE equipos (...); 

IDs duplicados:

Asegúrate de que los IDs de equipos sean únicos.


