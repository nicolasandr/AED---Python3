n = int(input("Ingrese el valor de n: "))
orbita=[n]
incremento=n

while n != 1:
    if n%2 == 0:
        n= n/2
        incremento += n
        orbita.append(round(n))
    else:
        n=(3*n)+1
        incremento +=n
        orbita.append(round(n))

#orbita(arreglo)
print("orbita",orbita)
#longitud de la orbita
longitud =len(orbita)
print("Longitud de la orbita:",longitud)
#promedio de todos los valores de la orbita
print("promedio:",round(incremento/longitud,1))
#mayor de los numeros de la orbita:
print("valor maximo:",max(orbita))