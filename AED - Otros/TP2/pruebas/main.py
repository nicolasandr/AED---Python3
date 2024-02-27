import random


def add_in_order(p, v):
    izq, der, pos = 0, len(v) - 1, 0
    n=0
    while izq <= der:
        medio = (izq + der) // 2
        if p == v[medio]:
            pos = medio
            print('entro en if')
            break
        elif p <= v[medio]:
            der = medio - 1
            print('entro en elif')
        else:
            izq = medio + 1
            print('entro en else')

    if izq > der:
        pos = izq
        print('entro en izq > der')
    v[pos:pos] = [p]
    n += 1
    print('vuelta ',n,' completa')

def principal():
    v = []
    print(len(v)-1)
    for i in range(5):
        pos = random.randint(0, 5)
        add_in_order(pos, v)

    for i in range(len(v)):
        print(v[i])

if __name__ == '__main__':
    principal()
