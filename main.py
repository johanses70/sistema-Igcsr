from cliente import Cliente
from servicio import Sala, Equipo, Asesoria
from reserva import Reserva

def main():
    try:
        c1 = Cliente("Juan", "juan@mail.com")
        s1 = Sala("Sala", 50)

        r1 = Reserva(c1, s1, 2)
        print("Costo:", r1.procesar())

        # ERROR CONTROLADO
        r2 = Reserva(c1, s1, -1)
        print(r2.procesar())

    except Exception as e:
        print("Error general:", e)

if __name__ == "__main__":
    main()
