from fastapi import APIRouter
from pydantic import BaseModel

from app.services.cliente_service import cliente_service


class ClienteCrear(BaseModel):
    nombre: str
    dni: str
    telefono: str
    correo: str


router = APIRouter()

@router.post('/v1/clientes', response_model=None)
async def crear_cliente(cliente: ClienteCrear) -> dict:
    cliente_service.agregar(cliente)
    return {'message': 'Cliente creado correctamente'}
