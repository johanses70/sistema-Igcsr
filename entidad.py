from abc import ABC, abstractmethod
from datetime import datetime

class Entidad(ABC):
    def __init__(self, id):
        self._id = id
        self._fecha_creacion = datetime.now()

    # Encapsulación (getter)
    def get_id(self):
        return self._id

    def get_fecha_creacion(self):
        return self._fecha_creacion

    # Método abstracto obligatorio
    @abstractmethod
    def mostrar_info(self):
        pass
