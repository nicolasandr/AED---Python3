import random
random.seed(11)

cant_divisible_x4 =  cant_divisible_x4yx8 = total1 = menoresAlPrimerNumGenerado = cantidad1 = 0
cantidad2 = 0
primerNumero = None
bandera = False

for i in range(1000):
    num = random.randint(1,2500)

    if primerNumero is None:
        primerNumero = num

    if (num % 4) == 0 and (num % 8) != 0:
        cant_divisible_x4 += 1
    if (num % 4) == 0 and (num % 8) == 0:
        cant_divisible_x4yx8 += 1
    #punto2
    if num > 2000:
        total1 += num
        cantidad1 += 1
    #punto3
    if primerNumero > num:
        cantidad2 += 1
        #falta calc el porcetnaje afuera
    #punto 4
    if num == 1 or num == 2500:
        bandera = True

#punto2
promedio1 = total1 / cantidad1
#punto3
porcentaje = (cantidad2 * 100)/1000

print("Divisibles por 4 y no por 8: ",cant_divisible_x4 )
print("cantidad divisible por ambos: ",cant_divisible_x4yx8)
print("Promedio de valores mayores a 2000: ",round(promedio1,2))
print("Cantidad de Numeros menores al primer valor generado: ",cantidad2,"porcentaje :",porcentaje)
if (bandera == True):
    print("Si aparecieron los valores extremos en la secuencia")
else:
    print("no aparecieron los valores extremos en la secuencia")