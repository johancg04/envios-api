from pydantic import BaseModel


class UsuarioCrear(BaseModel):
    nombre: str
    correo: str
    rol: str
    estado: str
    usuario: str
    contrasenia: str

class Usuario(BaseModel):
    id: int
    nombre: str
    correo: str
    rol: str
    estado: str
    usuario: str
    contrasenia: str
