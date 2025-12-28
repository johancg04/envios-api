from fastapi import APIRouter

from app.models.cliente import ClienteCrear, Cliente
from app.services.cliente_service import cliente_service

router = APIRouter()

@router.post('/v1/clientes', response_model=None)
async def crear_cliente(cliente: ClienteCrear) -> Cliente | dict:
    return cliente_service.agregar(cliente)
