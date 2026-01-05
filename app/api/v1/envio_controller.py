from fastapi import APIRouter

from app.models.envio import EnvioCrear, Envio
from app.services.envio_service import envio_service

router = APIRouter()

@router.post('/v1/envios', response_model=None)
async def crear_envio(envio_crear: EnvioCrear) -> Envio | dict:
    return envio_service.crear(envio_crear)
