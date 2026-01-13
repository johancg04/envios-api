from app.models.usuario import UsuarioCrear, Usuario, UsuarioLogin
from app.repositories.usuario_repository import usuario_repository


class UsuarioService:
    def __init__(self):
        pass

    def crear(self, usuario_crear: UsuarioCrear) -> Usuario | dict:
        nuevo_usuario = usuario_repository.insertar(usuario_crear)
        if nuevo_usuario:
            return nuevo_usuario
        else:
            return {"mensaje_error": "Error al crear usuario"}

    def listar(self) -> list[Usuario] | dict:
        lista_usuarios = usuario_repository.listar()
        if lista_usuarios is not None:
            return lista_usuarios
        else:
            return {"mensaje_error": "Error al listar usuarios"}

    def loguear(self, usuario_login: UsuarioLogin) -> dict:
        try:
            usuario_encontrado = usuario_repository.buscar(usuario_login)
            if usuario_encontrado:
                return {"mensaje": "Ingreso exitoso"}
            else:
                return {"mensaje_error": "Datos del usuario no son validos"}
        except:
            return {"mensaje_error": "Error en el login"}


usuario_service = UsuarioService()
