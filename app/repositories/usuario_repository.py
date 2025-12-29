import psycopg2

from app.db.config import crear_conexion
from app.models.usuario import UsuarioCrear, Usuario


class UsuarioRepository:
    def __init__(self):
        pass

    def insertar(self, usuario_crear: UsuarioCrear) -> Usuario | None:
        sql = """ INSERT INTO usuario(nombre, correo, usuario, contrasenia, rol, estado)
                  VALUES (%s, %s, %s, %s, %s,
                          %s) RETURNING id_usuario, nombre, correo, usuario, contrasenia, rol, estado """

        conn = None
        usuario_nuevo = None
        try:
            conn = crear_conexion()
            with conn.cursor() as cursor:
                cursor.execute(sql,
                               (usuario_crear.nombre, usuario_crear.correo, usuario_crear.usuario, usuario_crear.contrasenia,
                                usuario_crear.rol, usuario_crear.estado))
                result = cursor.fetchone()
                usuario_nuevo = Usuario(id=result[0],
                                        nombre=result[1],
                                        correo=result[2],
                                        usuario=result[3],
                                        contrasenia=result[4],
                                        rol=result[5],
                                        estado=result[6])
            conn.commit()
            return usuario_nuevo
        except (Exception, psycopg2.DatabaseError) as error:
            print(f"error: {error}")
            if conn:
                conn.rollback()
        finally:
            if conn:
                conn.close()


usuario_repository = UsuarioRepository()
