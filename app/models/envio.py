from datetime import date
from pydantic import BaseModel


class EnvioCrear(BaseModel):
    id_cliente: int
    id_usuario: int
    codigo_envio: str
    origen: str
    destino: str
    peso: float
    importe: float
    fecha_envio: date
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
    fecha_envio: date
    dni_destinatario: str
    nombre_destinatario: str
    telefono_destinatario: str
