import psycopg2

from app.db.config import crear_conexion
from app.models.cliente import Cliente, ClienteCrear


class ClienteRepository:
    def __init__(self):
        pass

    def insertar(self, cliente_crear: ClienteCrear) -> Cliente | None:
        sql = """ INSERT INTO cliente(nombre, dni, telefono, correo)
                  VALUES (%s, %s, %s, %s) RETURNING id_cliente """
        conn = None
        id_cliente_nuevo = None
        try:
            conn = crear_conexion()
            with conn.cursor() as cursor:
                cursor.execute(sql, (cliente_crear.nombre, cliente_crear.dni, cliente_crear.telefono, cliente_crear.correo))
                result = cursor.fetchone()
                id_cliente_nuevo = result[0]
            conn.commit()
            cliente_nuevo = Cliente(id=id_cliente_nuevo,
                                    nombre=cliente_crear.nombre,
                                    dni=cliente_crear.dni,
                                    telefono=cliente_crear.telefono,
                                    correo=cliente_crear.correo)
            return cliente_nuevo
        except(Exception, psycopg2.DatabaseError) as error:
            print(f"error: {error}")
            if conn:
                conn.rollback()
        finally:
            if conn:
                conn.close()


cliente_repository = ClienteRepository()
