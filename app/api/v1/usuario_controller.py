from fastapi import APIRouter

from app.models.usuario import UsuarioCrear, Usuario
from app.services.usuario_service import usuario_service

router = APIRouter()

@router.post('/v1/usuarios', response_model=None)
async def crear_usuario(usuario_crear: UsuarioCrear) -> Usuario | dict:
    return usuario_service.crear(usuario_crear)

@router.get('/v1/usuarios', response_model=None)
async def listar_usuarios() -> list[Usuario] | dict:
    return usuario_service.listar()
