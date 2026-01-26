import hashlib

from app.models.usuario import UsuarioCrear, Usuario, UsuarioLogin
from app.repositories.usuario_repository import usuario_repository

def hashear_texto(texto : str) -> str:
    return hashlib.sha256(texto.encode('utf-8')).hexdigest()

class UsuarioService:
    def __init__(self):
        pass

    def crear(self, usuario_crear: UsuarioCrear) -> Usuario | dict:
        usuario_crear.contrasenia = hashear_texto(usuario_crear.contrasenia)
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
        usuario_login.contrasenia = hashear_texto(usuario_login.contrasenia)
        try:
            usuario_encontrado = usuario_repository.buscar(usuario_login)
            if usuario_encontrado:
                return {"mensaje": "Ingreso exitoso"}
            else:
                return {"mensaje_error": "Datos del usuario no son validos"}
        except:
            return {"mensaje_error": "Error en el login"}


usuario_service = UsuarioService()
