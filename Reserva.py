from excepciones import ReservaError
from logger_config import logger

class Reserva:
    def __init__(self, cliente, servicio, cantidad):
        self.cliente = cliente
        self.servicio = servicio
        self.cantidad = cantidad
        self.estado = 'pendiente'

    def confirmar(self):
        try:
            if self.cantidad <= 0:
                raise ValueError('Cantidad inválida')
        except ValueError as e:
            logger.error(str(e))
            raise ReservaError('No se pudo confirmar') from e
        else:
            self.estado = 'confirmada'
            logger.info('Reserva confirmada')
        finally:
            logger.info('Fin confirmación')

    def cancelar(self):
        self.estado = 'cancelada'
        logger.info('Reserva cancelada')

    def procesar_pago(self, monto):
        costo = self.servicio.calcular_costo(self.cantidad, impuesto=0.19)
        if monto < costo:
            raise ReservaError('Pago insuficiente')
        self.estado = 'pagada'
        logger.info('Pago exitoso')
        return round(monto - costo,2)
