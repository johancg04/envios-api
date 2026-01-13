from app.models.cliente import ClienteCrear, Cliente
from app.repositories.cliente_repository import cliente_repository


class ClienteService:
    def __init__(self):
        pass

    def crear(self, cliente_crear: ClienteCrear) -> Cliente | dict:
        try:
            if cliente_repository.buscar_dni(cliente_crear.dni):
                return {"mensaje_error": f"Ya existe un cliente con el DNI: {cliente_crear.dni}"}
            else:
                nuevo_cliente = cliente_repository.insertar(cliente_crear)
                return nuevo_cliente
        except:
            return {"mensaje_error": "Error al crear cliente"}

    def listar(self) -> list[Cliente] | dict:
        lista_clientes = cliente_repository.listar()
        if lista_clientes is not None:
            return lista_clientes
        else:
            return {"mensaje_error": "Error al listar clientes"}


cliente_service = ClienteService()
