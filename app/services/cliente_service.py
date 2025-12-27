from app.repositories.cliente_repository import cliente_repository

class ClienteService:
    def __init__(self):
        pass

    def agregar(self, cliente):
        cliente_repository.insertar(cliente)

cliente_service = ClienteService()
