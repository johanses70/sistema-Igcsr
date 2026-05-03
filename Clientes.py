from excepciones import ClienteError

class Cliente:
    def __init__(self, nombre, email):
        self.__nombre = nombre
        self.__email = email
        self.validar()

    def validar(self):
        if not self.__nombre:
            raise ClienteError("Nombre vacío")
        if "@" not in self.__email:
            raise ClienteError("Email inválido")

    def get_nombre(self):
        return self.__nombre
