from fastapi import APIRouter

from app.models.seguimiento import SeguimientoCrear, Seguimiento
from app.services.seguimiento_service import seguimiento_service

router = APIRouter()

@router.post('/v1/seguimientos', response_model=None)
async def crear_seguimiento(seguimiento_crear: SeguimientoCrear) -> Seguimiento | dict:
    return seguimiento_service.crear(seguimiento_crear)
