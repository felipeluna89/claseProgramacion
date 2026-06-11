def conversion_notas(puntaje, puntaje_total):
    nota = (puntaje * 6 / puntaje_total) + 1
    return round(nota,1)


while True:
    try:
        p = float(input("Ingresa la nota del estudiante: "))
        if p < 0:
            print("Debe ser una nota positiva")
        else:
            break
    except ValueError:
        print("Debe ingresar un numero")
while True:
    try:
        pt = float(input("ingrese la nota total de la evualación: "))
        if pt < 0:
            print("Debe ser una nota positiva")
        else:
            break
    except ValueError:
        print("Debe ingresar un numero")

calificacion = conversion_notas(p, pt)
print(f"la nota es de: {calificacion}")