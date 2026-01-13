from app.models.envio import EnvioCrear, Envio, EnvioInfo
from app.repositories.envio_repository import envio_repository


class EnvioService:
    def __init__(self):
        pass

    def crear(self, envio_crear: EnvioCrear) -> Envio | dict:
        nuevo_envio = envio_repository.insertar(envio_crear)
        if nuevo_envio:
            return nuevo_envio
        else:
            return {"mensaje_error": "Error al crear envio"}

    def buscar(self) -> list[EnvioInfo] | dict:
        lista_envios = envio_repository.buscar()
        if lista_envios is not None:
            return lista_envios
        else:
            return {"mensaje_error": "Error al listar envios"}


envio_service = EnvioService()
