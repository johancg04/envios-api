import psycopg2

from app.db.config import crear_conexion
from app.models.seguiminento import SeguimientoCrear, Seguimiento


class SeguimientoRepository:
    def __init__(self):
        pass

    def insertar(self, seguimiento_crear: SeguimientoCrear) -> Seguimiento | None:
        sql = """ INSERT INTO seguimiento(id_envio, origen, destino, fecha_salida, fecha_llegada, estatus)
                  VALUES (%s, %s, %s, %s, %s,
                          %s) RETURNING id_seguimiento, id_envio, origen, destino, fecha_salida, fecha_llegada, estatus """
        conn = None
        seguimiento_nuevo = None
        try:
            conn = crear_conexion()
            with conn.cursor() as cursor:
                cursor.execute(sql, (seguimiento_crear.id_envio, seguimiento_crear.origen, seguimiento_crear.destino,
                                     seguimiento_crear.fecha_salida, seguimiento_crear.fecha_llegada,
                                     seguimiento_crear.estatus))
                resultado = cursor.fetchone()
                seguimiento_nuevo = Seguimiento(id_seguimiento=resultado[0], id_envio=resultado[1], origen=resultado[2],
                                                destino=resultado[3], fecha_salida=resultado[4],
                                                fecha_llegada=resultado[5], estatus=resultado[6])

            conn.commit()
            return seguimiento_nuevo
        except (Exception, psycopg2.DatabaseError) as error:
            print(f"error: {error}")
            if conn:
                conn.rollback()
        finally:
            if conn:
                conn.close()


seguimiento_repository = SeguimientoRepository()
