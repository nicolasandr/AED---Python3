patente = input("Ingrese la patente del vehiculo: ").replace(" ", "")
tipo_de_vehiculo = int(input("Ingrese el tipo de vehiculo: (0: motocicleta, 1: automóvil, 2: camión): "))
forma_de_pago = int(input("ingrese tipo de pago: (1: manual, 2: telepeaje): "))
pais = int(input("Ingrese el pais donde se encuentra la cabina de peaje:\n(0: Argentina - 1: Bolivia - 2: Brasil - 3: Paraguay - 4: Uruguay).: "))
Distancia = int(input("Ingrese la distancia (en Km) que recorrio el vehiculo desde la ultima cabina.\nSi es la primer cabina agregue 0: "))
importe_base = 0
#se Obtiene el tamaño de la cadena
tamanio_de_cadena_patente = len(patente)

#filtramos patente por cantidad de digitos
if tamanio_de_cadena_patente == 7:
    #filtramos patente por pais
    if  patente[0:2].isalpha() and patente[2:5].isdigit() and patente[5:7].isalpha():
        patente = "Argentina"
    elif patente[0:3].isalpha() and patente[3].isdigit() and patente[4].isalpha() and patente[4:7]:
        patente = "Brasil"
    elif patente[0:2].isalpha() and patente[2:].isdigit():
        patente = "Bolivia"
    elif patente[0:4].isalpha() and patente[4:].isdigit():
        patente = "Paraguay"
    elif patente[0:3].isalpha() and patente[3:].isdigit():
        patente = "Uruguay"
    else:
        patente = "Otro"
else:
    patente = "Otro"

#Cargamos el importe base en funcion de encuentra ubicada la cabina de peaje:
if pais >= 0 and pais <= 4:
    if pais == 0:
        #Argentina
        importe_base = 300
    if pais == 1:
        #Bolivia
        importe_base = 200
    if pais == 2:
        #Brasil
        importe_base = 400
    if pais == 3:
        #Paraguay
        importe_base = 300
    if pais == 4:
        #Uruguay
        importe_base = 300
else:
    #para cualquier otro pais
    importe_base = 300

#Modificamos el importe base segun el tipo de vehiculo:
if tipo_de_vehiculo == 0:
    #motocicleta (descuento del 50%)
    importe_base = (importe_base * 0.5)
elif tipo_de_vehiculo == 2:
    #camion (recargo del 60%)
    importe_base = (importe_base * 1.6)

#Modificamos importe base en funcion de La forma de pago:
if forma_de_pago == 2:
    #telepeaje:(descuento del 10%)
    importe_base = importe_base - (importe_base * 0.1)

#Emision de ticket:

print("\nEmision de ticket: \nPais de procedencia del vehiculo:",patente)
print("Importe base a pagar:", importe_base)

# calculo de promedio por vehiculo
if Distancia == 0:
   promedio_abonado_por_km = "No hay valor promedio pagado ya que la distancia recorrida es 0 km."
   print("Valor promedio pagado:", promedio_abonado_por_km)
else:
   promedio_abonado_por_km = importe_base / Distancia
   print("Valor promedio pagado:", round(promedio_abonado_por_km, 2))