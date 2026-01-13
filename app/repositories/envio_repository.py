import psycopg2

from app.db.config import crear_conexion
from app.models.envio import EnvioCrear, Envio, EnvioInfo


class EnvioRepository:
    def __init__(self):
        pass

    def insertar(self, envio_crear: EnvioCrear) -> Envio | None:
        sql = """ INSERT INTO envio(id_cliente, id_usuario, codigo_envio, origen, destino, peso, importe, fecha_envio,
                                    dni_destinatario, nombre_destinatario, telefono_destinatario)
                  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id_envio, id_cliente, id_usuario, codigo_envio, origen, destino, peso, importe, fecha_envio,
                                    dni_destinatario, nombre_destinatario, telefono_destinatario """
        conn = None
        envio_nuevo = None
        try:
            conn = crear_conexion()
            with conn.cursor() as cursor:
                cursor.execute(sql, (envio_crear.id_cliente, envio_crear.id_usuario, envio_crear.codigo_envio,
                                     envio_crear.origen, envio_crear.destino, envio_crear.peso, envio_crear.importe,
                                     envio_crear.fecha_envio, envio_crear.dni_destinatario,
                                     envio_crear.nombre_destinatario, envio_crear.telefono_destinatario))
                resultado = cursor.fetchone()
                envio_nuevo = Envio(id_envio=resultado[0], id_cliente=resultado[1], id_usuario=resultado[2],
                                    codigo_envio=resultado[3], origen=resultado[4], destino=resultado[5],
                                    peso=resultado[6], importe=resultado[7], fecha_envio=resultado[8],
                                    dni_destinatario=resultado[9], nombre_destinatario=resultado[10],
                                    telefono_destinatario=resultado[11])
            conn.commit()
            return envio_nuevo
        except (Exception, psycopg2.DatabaseError) as error:
            print(f"error: {error}")
            if conn:
                conn.rollback()
        finally:
            if conn:
                conn.close()

    def buscar(self) -> list[EnvioInfo] | None:
        sql = """ SELECT codigo_envio, cli.nombre, nombre_destinatario, origen, destino, fecha_envio
                  FROM envio env
                           INNER JOIN cliente cli ON env.id_cliente = cli.id_cliente """
        conn = None
        lista_envios = []
        try:
            conn = crear_conexion()
            with conn.cursor() as cursor:
                cursor.execute(sql)
                results = cursor.fetchall()
                for result in results:
                    envio = EnvioInfo(codigo_envio=result[0],
                                      nombre_cliente = result[1],
                                      nombre_destinatario=result[2],
                                      origen=result[3],
                                      destino=result[4],
                                      fecha_envio=result[5])
                    lista_envios.append(envio)
            return lista_envios
        except (Exception, psycopg2.DatabaseError) as error:
            print(f"error: {error}")
        finally:
            if conn:
                conn.close()


envio_repository = EnvioRepository()
