def buscar_mascota(lista_m, nombre_m):
    for x in range(len(lista_m)):
        if nombre_m == lista_m[x]["nombre"]:
            return x
    return -1

def validar_nombre(name):
    return name.strip() != ""

def validar_especie(especie):
    especie_validas = ["perro", "gato", "ave"]
    return especie.strip().lower() in especie_validas

def validar_edad(edad):
    return edad.isdigit and int(edad) > 0

def mostrar_menu():
    print("=========== MENÚ PRINCIPAL ==========")
    print("1.- agregar mascota")
    print("2.- buscar mascota")
    print("3.- eliminar mascota")
    print("4.- marcar como vacunada")
    print("5.- mostrar mascota")
    print("6.- salir")
    print("=====================================")

def ingresar_opcion():
    while True:
        try:
            opcion = int(input("Seleccione una opcion: "))
            if opcion < 1 or opcion > 6:
                print("debe de ingresar un numero del 1 al 6")
            else:
                break
        except ValueError:
            print("debe ingresar un numero")
    return opcion

def agregar_mascota(lista):
    name = input("ingrese el nombre de la mascota: ")
    correcto = validar_nombre(name)
    if not correcto:
        print("el nombre no puede estar vacio")
        return
    
    especie = input("ingrese la especie de la mascota (perro, gato o ave): )")
    correcto =  validar_especie(especie)
    if not correcto:
        print("La especie solo puede ser perro, gato, ave")
        return
    
    edad = input("Ingrese la edad de la mascota: ")
    correcto = validar_edad(edad)
    if not correcto:
        print("la edad debe ser un numero entero y mayor a cero")
        return
    
    mascota = {
        "nombre": name.strip(),
        "especie": especie.strip(),
        "edad": int(edad),
        "vacunada": False
    }
    lista.append(mascota)
    print("Mascota agregada correctamente")

def actualizar_vacunas(lista_m):
    for m in lista_m:
        if m["edad"] >= 1:
            m["vacunada"] = True
        else:
            m["vacunada"] = False

lista_mascota = []

op = 0
while op != 6:
    mostrar_menu()
    op = ingresar_opcion()

    if op == 1:
        agregar_mascota(lista_mascota) 
    elif op == 2:
        print("*** buscar mascota ***")
        nombre = input("Ingrese el nombre del amascota: ")
        posicion = buscar_mascota(lista_mascota, nombre)
        if posicion != -1:
            print(f"La posicion encontrada es: {posicion + 1}")
            m = lista_mascota[posicion]
            print(f"nombre mascota: {m["nombre"]}")
            print(f"Especie Mascota: {m["especie"]}")
            print(f"edad mascota: {m["edad"]}")
            print(f"vacunada: {m["vacunada"]}")
        else:
            print("la mascota no se ha encontrado")
    elif op == 3:
        print("*** eliminar mascota ***")
        nombre = input("Ingrese el nombre del amascota: ")
        posicion = buscar_mascota(lista_mascota, nombre)
        if posicion != 1:
            lista_mascota.pop(posicion)
            print("la mascota ha sido removida del sistema")
        else:
            print(f"la mascota {nombre} no se encuentra en la lista")
    elif op == 4:
        actualizar_vacunas(lista_mascota)
        print("vacunas actualizadas")
        print()
    elif op == 5:
        actualizar_vacunas(lista_mascota)
        if len(lista_mascota) == 0:
            print("No hay mascotas en la lista")
        else:
            print("== Lista De Mascota ==")
            for m in lista_mascota:
                print(f"nombre mascota: {m["nombre"]}")
                print(f"Especie Mascota: {m["especie"]}")
                print(f"edad mascota: {m["edad"]}")
                estado = "AL DIA" if m["vacunada"] else "pendiente"
                print(f"Estado vacuna: {estado}")
                print("========================")
                print("")
    elif op == 6:
        print("Gracias por su visita")
