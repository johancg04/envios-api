import psycopg2

from app.db.config import crear_conexion

class Cliente:
    def __init__(self, nombre, dni, telefono, correo):
        self.nombre = nombre
        self.dni = dni
        self.telefono = telefono
        self.correo = correo

class ClienteRepository:
    def __init__(self):
        pass

    def insertar(self, cliente: Cliente):
        sql = """INSERT INTO cliente(nombre, dni, telefono, correo) VALUES(%s,%s,%s,%s)"""
        conn = None
        try:
            conn = crear_conexion()
            with conn.cursor() as cursor:
                cursor.execute(sql, (cliente.nombre, cliente.dni, cliente.telefono, cliente.correo))
            conn.commit()
        except(Exception, psycopg2.DatabaseError) as error:
            print(f"error: {error}")
            if conn:
                conn.rollback()
        finally:
            if conn:
                conn.close()
