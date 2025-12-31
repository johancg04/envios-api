from app.models.cliente import ClienteCrear, Cliente
from app.repositories.cliente_repository import cliente_repository


class ClienteService:
    def __init__(self):
        pass

    def agregar(self, cliente_crear: ClienteCrear) -> Cliente | dict:
        nuevo_cliente = cliente_repository.insertar(cliente_crear)
        if nuevo_cliente:
            return nuevo_cliente
        else:
            return {"mensaje_error": "Error al agregar cliente"}

    def mostrar_cliente(self) -> list | dict:
        print(cliente_repository.mostrar())
        mostrar = cliente_repository.mostrar()
        if mostrar:
            return mostrar
        else:
            return {"mensaje_error": "Error al mostrar cliente"}

cliente_service = ClienteService()
