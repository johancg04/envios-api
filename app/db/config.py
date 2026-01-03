import psycopg2

def crear_conexion_windows():
    credenciales = {}
    with open('C:\\envios-api\\db.properties', 'r', encoding='utf8') as fh:
        for linea in fh:
            partes = linea.rstrip('\n').split('=')
            credenciales[partes[0]] = partes[1]
    conn = psycopg2.connect(**credenciales)
    print("Conectado a PostgreSQL Windows")
    return conn

def crear_conexion_macos():
    credenciales = {}
    with open('/Users/user/envios-api/db.properties', 'r', encoding='utf8') as fh:
        for linea in fh:
            partes = linea.rstrip('\n').split('=')
            credenciales[partes[0]] = partes[1]
    conn = psycopg2.connect(**credenciales)
    print("Conectado a PostgreSQL MacOS")
    return conn

def crear_conexion():
    # TODO usar variables de entorno para leer la configuracion de DB
    try:
        return crear_conexion_windows()
    except Exception as e:
        return crear_conexion_macos()

try:
    conn = crear_conexion()
    cursor = conn.cursor()

    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    print(f"Conectado a PostgreSQL version: {db_version[0]}")

    cursor.close()
    conn.close()

except psycopg2.Error as e:
    print(f"Error al conectar: {e}")

except Exception as e:
    print(f"Error general: {e}")
