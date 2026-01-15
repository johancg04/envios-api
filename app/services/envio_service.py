from datetime import datetime

from app.models.envio import EnvioCrear, Envio, EnvioInfo, EnvioVer
from app.repositories.envio_repository import envio_repository


class EnvioService:
    def __init__(self):
        pass

    def crear(self, envio_crear: EnvioCrear) -> Envio | dict:
        fecha_envio = datetime.now()
        nuevo_envio = envio_repository.insertar(envio_crear, fecha_envio)
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


    def ver_detalle(self, id_envio: int) -> EnvioVer | dict:
        envio = envio_repository.obtener(id_envio)
        if envio is not None:
            return envio
        else:
            return {"mensaje_error": "Error al ver envio"}


envio_service = EnvioService()
