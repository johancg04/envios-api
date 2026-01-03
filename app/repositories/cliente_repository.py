from typing import Any

import psycopg2

from app.db.config import crear_conexion
from app.models.cliente import Cliente, ClienteCrear


class ClienteRepository:
    def __init__(self):
        pass

    def insertar(self, cliente_crear: ClienteCrear) -> Cliente | None:
        sql = """ INSERT INTO cliente(nombre, dni, telefono, correo)
                  VALUES (%s, %s, %s, %s) RETURNING id_cliente, nombre, dni, telefono, correo """
        conn = None
        cliente_nuevo = None
        try:
            conn = crear_conexion()
            with conn.cursor() as cursor:
                cursor.execute(sql,
                               (cliente_crear.nombre, cliente_crear.dni, cliente_crear.telefono, cliente_crear.correo))
                result = cursor.fetchone()
                cliente_nuevo = Cliente(id=result[0],
                                        nombre=result[1],
                                        dni=result[2],
                                        telefono=result[3],
                                        correo=result[4])
            conn.commit()
            return cliente_nuevo
        except(Exception, psycopg2.DatabaseError) as error:
            print(f"error: {error}")
            if conn:
                conn.rollback()
        finally:
            if conn:
                conn.close()

    def listar(self) -> list[Cliente] | None:
        sql = """ SELECT id_cliente, nombre, dni, telefono, correo
                  FROM cliente """
        conn = None
        lista_clientes = []
        try:
            conn = crear_conexion()
            with conn.cursor() as cursor:
                cursor.execute(sql)
                results = cursor.fetchall()
                for result in results:
                    cliente = Cliente(id=result[0],
                                      nombre=result[1],
                                      dni=result[2],
                                      telefono=result[3],
                                      correo=result[4])
                    lista_clientes.append(cliente)
            conn.commit()
            return lista_clientes
        except(Exception, psycopg2.DatabaseError) as error:
            print(f"error: {error}")
            if conn:
                conn.rollback()
        finally:
            if conn:
                conn.close()


cliente_repository = ClienteRepository()
