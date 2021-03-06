from random import randint
MIN = 1
MAX = 20
COSTO = 0

def generarOrdenados(n):
    a =[randint(MIN, MAX)]
    for i in range (n - 1):
        a.append(a[-1] + randint(MIN, MAX))
    return a

def busquedaBinaria(a,e):
    global COSTO
    if len(a) == 0:
        return False
    mitad = len(a) // 2
    COSTO += 1
    if e == a[mitad]:
        return True
    else:
        COSTO += 1
        if e > a[mitad]:
            return busquedaBinaria(a[mitad + 1:], e)
        else:
            return busquedaBinaria(a[:mitad], e)

def busquedaNoOrdenada(a,e):
    global COSTO
    for i in a:
        COSTO += 1
        if i == e:
            return True
    return False

REPET = 50
MINL = 50
MAXL = 5000
for i in range(REPET):
    l = randint(MINL, MAXL)
    f = generarOrdenados(l)
    for n in f:
        COSTO = 0
        assert busquedaBinaria(f, n) == True
        print(COSTO, 'bin', l, True)
        COSTO = 0
        assert busquedaNoOrdenada(f, n) == True
        print(COSTO, 'wey', l, True)
    for n in range(l):
        e = randint(min(f) // 2, 2 * max(f))
        es = (e in f)
        COSTO = 0
        assert busquedaBinaria(f, e) == es
        print(COSTO, 'bin', l, es)
        COSTO = 0
        assert busquedaNoOrdenada(f, e) == es
        print(COSTO, 'wey', l, es)

