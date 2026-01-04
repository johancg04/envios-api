from app.models.envio import EnvioCrear, Envio
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

envio_service = EnvioService()
