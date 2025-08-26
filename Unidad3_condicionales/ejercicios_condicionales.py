#Entrada
fecha = input("Ingrese la fecha con el siguiente formato Día, Día(número)/mes: ")
fecha = fecha.split(",")
dia = fecha[0]
dia = dia.capitalize()
aux = fecha[1].strip().split("/")
dd = int(aux[0])
mm = int(aux[1])
total_alumnos = (None)
tomaron_examen = (None)
alumnos_aprobados = (None)
alumnos_desaprobados = (None)
porcentaje_aprobados = (None)
porcentaje_asistencia = (None)
arancel_alumno = (None)
ingresos_totales =(None)

# Proceso/Salida
# Validación de fecha

if mm > 12 or mm < 1:
    print()
    print("Se produjo un error")
    exit()
elif mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12:
        if dd < 1 or dd > 31:
            print()
            print("Se produjo un error")
            exit()
        else:
             print()
             print(f"Hoy es: {dia}, {dd} del {mm} ")
elif mm == 4 or mm == 5 or mm == 9 or mm == 11:
     if dd < 1 or dd > 30:
          print()
          print("Se produjo un error")
          exit()
     else:
        print()
        print(f"Hoy es: {dia}, {dd} del {mm} ")
else:
    if dd < 1 or dd > 29:
          print()
          print("Se produjo un error")
          exit()
    else:
         print()
         print(f"Hoy es: {dia}, {dd} del {mm} ")

# Acciones según el día

if dia == "Lunes" or dia == "Martes" or dia == "Miércoles":
     tomaron_examen = input(f"En el día {dia}, {dd}/{mm} ¿se tomaron los examenes?, 1.SI, 2.NO: ")
     if tomaron_examen == "1":
          print()
          alumnos_aprobados = int(input("Ingrese la cantidad de alumnos aprobados: "))
          alumnos_desaprobados = int(input("Ingrese la cantidad de alumnos desaprobados: "))
          total_alumnos = alumnos_aprobados + alumnos_desaprobados
          porcentaje_aprobados = (alumnos_aprobados / total_alumnos) * 100
          print(f"Aprobo el {porcentaje_aprobados}% de los alumnos")
elif dia == "Jueves":
    print()
    porcentaje_asistencia = int(input("Ingrese elporcentaje de asistencia a clase: "))
    if porcentaje_asistencia > 50:
        print("Asistió la mayoría")
    else:
         print("No asistió la mayoría")
elif dia == "Viernes" and dd == 1 and mm == 1 or dia == "Viernes" and dd == 1 and mm == 7:
    print()
    print("Comienzo de nuevo ciclo")
    total_alumnos = int(input("Ingrese la cantidad total de alumnos del nuevo ciclo: "))
    arancel_alumno = float(input("Ingrese la cuota en pesos que debera abonar cada alumno: "))
    ingresos_totales = arancel_alumno * total_alumnos
    print(f"En total ingresarían: ${ingresos_totales} pesos")
