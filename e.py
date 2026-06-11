def mostrar_encabezado():
    print("=================================")
    print("| | sistema de Admsión Escolar...")
    print("=================================")

def solicitar_datos():

    estudiante = {}
    estudiante["rut"] = input("| | Ingrese el rut del estudiante: ")
    estudiante["nombre"] = input("| | Ingrese El Nombre Del Estudiante: ")
    estudiante["carrera"] = input("| | Que Carrera Esta Cursando: ")

    while True:
        try:
            estudiante["semestre"] = int(input("| | Ingrese el semestre que cursa: "))
            if estudiante["semestre"] < 1 or estudiante["semestre"] > 4:
                print("Debe ser del 1 al 4")
            else:
                break
        except ValueError:
            print("Debe ingresar un numero")
    return estudiante

def mostrar_datos(alumnos):

    print("==========================================================")
    print(f"| | Nombre De Estudiante: {alumnos["nombre"]}")
    print("==========================================================")
    print(f"| | RUN Del Estudiante: {alumnos["rut"]}")
    print("==========================================================")
    print(f"| | Carrera Cursante Del estudiante: {alumnos["carrera"]}")
    print("==========================================================")
    print(f"| | Semestre Del Estudiante: {alumnos["semestre"]}")
    print("==========================================================")

datos = solicitar_datos()
mostrar_encabezado()
mostrar_datos(datos)
















    









