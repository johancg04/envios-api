from pydantic import BaseModel


class ClienteCrear(BaseModel):
    nombre: str
    dni: str
    telefono: str
    correo: str

class Cliente(BaseModel):
    id: int
    nombre: str
    dni: str
    telefono: str
    correo: str
