from app.models.seguiminento import SeguimientoCrear, Seguimiento
from app.repositories.seguimiento_repository import seguimiento_repository


class SeguimientoService:
    def __init__(self):
        pass

    def crear(self, seguimiento_crear: SeguimientoCrear) -> Seguimiento | dict:
      nuevo_seguimiento = seguimiento_repository.insertar(seguimiento_crear)
      if nuevo_seguimiento:
          return nuevo_seguimiento
      else:
          return {"mensaje_error": "Error al crear seguimiento"}

seguimiento_service = SeguimientoService()
