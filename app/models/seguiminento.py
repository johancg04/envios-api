from datetime import datetime

from pydantic import BaseModel


class SeguimientoCrear(BaseModel):
    id_envio: int
    origen: str
    destino: str
    fecha_salida: datetime
    fecha_llegada: datetime
    estatus: str

class Seguimiento(BaseModel):
    id_seguimiento:int
    id_envio: int
    origen: str
    destino: str
    fecha_salida: datetime
    fecha_llegada: datetime
    estatus: str