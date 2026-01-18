from datetime import datetime

from app.models.envio import EnvioCrear, Envio, EnvioInfo, EnvioVer
from app.repositories.envio_repository import envio_repository

def completar_ceros(cantidad: int, numero: int) -> str:
    return ('0' * cantidad + str(numero))[len(str(numero)):]

def generar_codigo_envio(fecha_envio, codigo_envio_seq) -> str:
    anio = str(fecha_envio.year)[2:]
    mes = completar_ceros(2, fecha_envio.month)
    dia = completar_ceros(2, fecha_envio.day)
    seq = completar_ceros(4, codigo_envio_seq)
    return anio + mes + dia + seq


class EnvioService:
    def __init__(self):
        pass

    def crear(self, envio_crear: EnvioCrear) -> Envio | dict:
        fecha_envio = datetime.now()
        codigo_envio_seq = envio_repository.obtener_codigo_seq()
        codigo_envio = generar_codigo_envio(fecha_envio, codigo_envio_seq)
        nuevo_envio = envio_repository.insertar(envio_crear, fecha_envio, codigo_envio)
        if nuevo_envio:
            return nuevo_envio
        else:
            return {"mensaje_error": "Error al crear envio"}

    def buscar(self, identificador: str) -> list[EnvioInfo] | dict:
        lista_envios = envio_repository.buscar(identificador)
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
