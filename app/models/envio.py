from datetime import datetime

from pydantic import BaseModel


class EnvioCrear(BaseModel):
    id_cliente: int
    id_usuario: int
    origen: str
    destino: str
    peso: float
    importe: float
    dni_destinatario: str
    nombre_destinatario: str
    telefono_destinatario: str


class Envio(BaseModel):
    id_envio: int
    id_cliente: int
    id_usuario: int
    codigo_envio: str
    origen: str
    destino: str
    peso: float
    importe: float
    fecha_envio: datetime
    dni_destinatario: str
    nombre_destinatario: str
    telefono_destinatario: str

class EnvioDetalle(BaseModel):
    id_envio: int
    codigo_envio: str
    nombre_cliente: str
    nombre_destinatario: str
    origen: str
    destino: str
    fecha_envio: datetime

class EnvioVer(BaseModel):
    id_envio: int
    fecha_envio: datetime
    peso: float
    importe: float
    dni: str
    nombre: str
    telefono: str
    correo: str
    dni_destinatario: str
    nombre_destinatario: str
    telefono_destinatario: str
