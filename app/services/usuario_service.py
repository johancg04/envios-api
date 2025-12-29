from app.models.usuario import UsuarioCrear, Usuario
from app.repositories.usuario_repository import usuario_repository


class UsuarioService:
    def __init__(self):
        pass

    def agregar(self, usuario_crear: UsuarioCrear) -> Usuario | dict:
        nuevo_usuario = usuario_repository.insertar(usuario_crear)
        if nuevo_usuario:
            return nuevo_usuario
        else:
            return {"mensaje_error":"Error al agregar usuario"}

usuario_service = UsuarioService()
