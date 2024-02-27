segundos = int(input("\nIngrese la cantidad de segundos: "))
minutos =int(segundos % 3600 / 60)
horas = int(segundos / 3600)
resto_segundos = (segundos % 3600) % 60

if horas > 24:
    print("Excedido")
else:
    print("El tiempo es: " + str(horas) + ":" + str(minutos) + ":" + str(resto_segundos))

#segunda parte:
horas = int(input("\nIngrese la cantidad de horas: "))
minutos = int(input("Ingrese la cantidad de minutos: "))
segundos = int(input("Ingrese la cantidad de segundos: "))
minutos_a_seg = minutos * 60
horas_a_seg = horas * 3600

segundos_totales = minutos_a_seg + horas_a_seg + segundos

print("\nLa cantidad de segundos totales es: ",segundos_totales)
