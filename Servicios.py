from abc import ABC, abstractmethod
from excepciones import ServicioError

class Servicio(ABC):
    def __init__(self, nombre, tarifa):
        if tarifa <= 0:
            raise ServicioError('Tarifa inválida')
        self.nombre = nombre
        self.tarifa = tarifa

    @abstractmethod
    def calcular_costo(self, cantidad, impuesto=0, descuento=0):
        pass

class ServicioSala(Servicio):
    def calcular_costo(self, horas, impuesto=0, descuento=0):
        subtotal = self.tarifa * horas
        return subtotal * (1 + impuesto - descuento)

class ServicioEquipo(Servicio):
    def calcular_costo(self, dias, impuesto=0, descuento=0):
        subtotal = self.tarifa * dias
        return subtotal * (1 + impuesto - descuento)

class ServicioAsesoria(Servicio):
    def calcular_costo(self, sesiones, impuesto=0, descuento=0):
        subtotal = self.tarifa * sesiones
        return subtotal * (1 + impuesto - descuento)
