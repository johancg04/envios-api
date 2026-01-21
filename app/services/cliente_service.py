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

    def buscar(self, dni: str) -> Cliente | dict:
        cliente = cliente_repository.buscar_dni(dni)
        if cliente is not None:
            return cliente
        else:
            return {"mensaje_error": f"Cliente con DNI: {dni} no encontrado"}


cliente_service = ClienteService()
