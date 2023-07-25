from random import randint

numeros = []


def addlist(x):
    for i in range(100):
        x.append(randint(0, 1000))


addlist(numeros)


def saber(numeros):
    menor = 0
    maior = 0
    menor100 = []
    par = []
    for i in range(len(numeros)):
        var = numeros[i]
        if menor <var:
            menor =var
        if maior < menor:
            maior = menor
        if var % 2 == 0:
            par.append(var)
        if numeros[i] < 100:
            menor100.append(var)

    print(f"O MAIOR NUMEROs É {maior}")
    print(f"Os NUMEROs pares é  {par}")
    print(f"e menor q 100 é {menor100}")


saber(numeros)
