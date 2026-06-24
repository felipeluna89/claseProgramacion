import ejercicio3 as ej
import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

opcion = 0
lista_reserva = []

import ejercicio3 as ej
import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

opcion = 0
lista_reserva = []

while opcion != 6:
    limpiar_pantalla()  # Limpia antes de mostrar el menú

    ej.mostrar_menu()
    opcion = ej.ingresar_opcion()

    if opcion == 1:
        ej.agregar_reserva(lista_reserva)

    elif opcion == 2:
        nombre = input("Ingrese el nombre del huesped a buscar: ")
        pos = ej.buscar_reserva(lista_reserva, nombre)

        if pos != -1:
            print(f"| | Nombre de Huesped: {lista_reserva[pos]['huesped']}")
            print(f"| | Numero de habitacion: {lista_reserva[pos]['habitacion']}")
            print(f"| | Noches de Hospedaje: {lista_reserva[pos]['noches']}")
            estado = "CONFIRMADO" if lista_reserva[pos]['confirmada'] else "PENDIENTE"
            print(f"| | Estado: {estado}")
        else:
            print(f"El Huesped {nombre} no ha sido encontrado")

        input("\nPresione ENTER para continuar...")

    elif opcion == 3:
        input("\nPresione ENTER para continuar...")
        nombre = input("Ingrese el nombre del huesped a buscar: ")
        pos = ej.buscar_reserva(lista_reserva, nombre)
        if pos != -1:
            lista_reserva.pop(pos)
            print("La reserva ha sido eliminada.")
        else:
            print(f"El huesped {nombre} no ha sido encontrado")

    elif opcion == 4:
        ej.confirmar_reserva(lista_reserva)

    elif opcion == 5:
        ej.confirmar_reserva(lista_reserva)
        ej.mostrar_reservas(lista_reserva)
        
    elif opcion == 6:
        print("Gracias por usar el programa")
