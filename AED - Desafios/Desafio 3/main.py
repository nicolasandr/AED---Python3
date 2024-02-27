import soporte


def Principal():
    num = []
    cont = []
    c = 300000 * [0]
    cant = 0
    v = soporte.vector_known_range(300000)

    for i in range(len(v)):
        x = v[i]
        c[x] += 1

    for i in c:
        if c[i] != 0:
            cant += 1
    print(cant)

    #v = [2,2,2,2,2,1,1,1,3,3,3,3,3,4,5,5,1]

    for i in range(len(v)):
        x = v[i]
        if x in num:
            i = num.index(x)
            cont[i] += 1
        else:
            num.append(x)
            cont.append(1)

    may = max(cont)
    #for i in cont:
     #   if cont[i] > cont[i+1]:
#
     #       else:
    #print(cont)
    print((len(cont)))
    #print(num)

    Hay_moda = False
    c = 0

    for i in cont:
        if may == i:
            c += 1

    if c == 1:
        for i in cont:
            indice = cont.index(may)
            Hay_moda = True

    if Hay_moda:
        moda = num[indice]
        print(moda)

if __name__ == '__main__':
    Principal()
