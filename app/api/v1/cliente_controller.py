from fastapi import APIRouter

from app.models.cliente import ClienteCrear, Cliente
from app.repositories.cliente_repository import cliente_repository
from app.services.cliente_service import cliente_service

router = APIRouter()

@router.post('/v1/clientes', response_model=None)
async def crear_cliente(cliente: ClienteCrear) -> Cliente | dict:
    return cliente_service.crear(cliente)

@router.get('/v1/clientes', response_model=None)
async def listar_clientes() -> list[Cliente] | dict:
    return cliente_service.listar()
