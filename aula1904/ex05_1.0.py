num1 = int(input("digite um numero: "))
num2 = int(input("digite outro numero: "))
num3 = int(input("digite outro numero: "))

def mensagemPar(x):
    print(f"o {x} par, ele é o menor numeros entre os 3")

def mensagemImpar(x):
     print(f"o {x} é ímpar, ele é o menor numeros entre os 3")

if num1 < num2 and num1 < num3:
    if num1 % 2 == 0:
        mensagemPar(num1)
    else:
        mensagemImpar(num1)
elif num2< num1 and num2< num3:
    if num2 % 2 == 0:
        mensagemPar(num2)
    else:
        mensagemImpar(num2)
else:
    if num3 % 2 == 0:
        mensagemPar(num3)
    else:
        mensagemImpar(num3)