def mostrar_menu():
    print("********* MENÚ PRINCIPAL *********")
    print("1.- Agregar Reserva    | |")
    print(" ")
    print("2.- Buscar Reserva     | |")
    print(" ")
    print("3.- Eliminar Reserva   | |")
    print(" ")
    print("4.- Confirmar Reservas | |")
    print(" ")
    print("5.- Mostrar Reservas   | |")
    print(" ")
    print("6.- Salir              | |")
    print(" ")
    print("**********************************")

def ingresar_opcion():
    while True:
        try:
            op = int(input("Seleccione una opción: "))
            if op < 1 or op > 6:
                raise ValueError
            else:
                return op
        except ValueError:
            print("Debe ingresar un numero del 1 al 6.")

def agregar_reserva(lista_r):
    nombre_completo = input("| | Ingrese su nombre completo: ")
    correcto = validar_huesped(nombre_completo)
    if not correcto: 
        print("El nombre no puede estar vacio.")
        return
    
    numero_habitacion = input("| | Ingrese la cantidad de habitaciones a reservar: ")
    correcto = validar_habitacion(numero_habitacion)
    if not correcto:
        print("La habitacion debe ser un numero entero entre 1 y 200.")
        return
    
    cant_noches = input("| | Ingrese la cantidad de noches a hospedar: ")
    correcto = validar_noches(cant_noches)

    if not correcto:
        print("La cantidad de noches debe ser mayor a cero.")
        return
    
    reserva = { 
        "huesped": nombre_completo,
        "habitacion": int(numero_habitacion),
        "noches": int(cant_noches),
        "confirmada": False
    }
    lista_r.append(reserva)
    print("Reserva agregada correctamente.")
  
def buscar_reserva(lista_r, huesped):
    for x in range(len(lista_r)):
        if huesped == lista_r[x]["huesped"]:
            return x
    return -1

def confirmar_reserva(lista_r):
    for i in lista_r:
        if i["noches"] >= 2:
            i["confirmada"] = True
        else:
            i["confirmada"] = False

def mostrar_reservas(lista_r):
    print("| | Lista De Reservas ------")
    for i in lista_r:
        print(f"Nombre de Huesped: {i["huesped"]}")
        print(f"Numero de habitacion: {i["habitacion"]}")
        print(f"Noches de Hospedaje: {i["noches"]}")
        if i["confirmada"]:
            print("Estado: CONFIRMADO")
        else:
            print("Estado: PENDIENTE")
        print("****************************")


def validar_huesped(nombre):
    return nombre.strip() != ""

def validar_habitacion(hab):
    if hab.isdigit():
         val = int(hab)
         return val >= 1 and val <= 200
    return False

def validar_noches(noche):
    if noche.isdigit():
        val = int(noche)
        return val > 0
    return False
    