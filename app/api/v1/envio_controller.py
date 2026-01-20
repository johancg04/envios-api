from fastapi import APIRouter

from app.models.envio import EnvioCrear, Envio, EnvioDetalle, EnvioVer
from app.services.envio_service import envio_service

router = APIRouter()

@router.post('/v1/envios', response_model=None)
async def crear_envio(envio_crear: EnvioCrear) -> Envio | dict:
    return envio_service.crear(envio_crear)

@router.get('/v1/envios', response_model=None)
async def buscar_envios(identificador: str) -> list[EnvioDetalle] | dict:
    return envio_service.buscar(identificador)

@router.get('/v1/envios/{id_envio}', response_model=None)
async def ver_detalle(id_envio) -> EnvioVer | dict:
    return envio_service.ver_detalle(id_envio)
