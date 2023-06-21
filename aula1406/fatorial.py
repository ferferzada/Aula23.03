from importacao.inform import *

def menu():
    print("Qual das funções quer seguir \n"
          "Opção 1 ==>Calcular combinações \n"
          "Opção 2 ==>Calcular arranjo \n"
          "Opção 3 ==>sair")
    return verificar(informInt("Qual opção você quer: "))


def verificar(x):
    x = 0
    while x !=3:
        x = menu()
    if x== 1:
       tratar_combinacoes()
    elif x==2:
        tratar_arranjos()
    elif x == 3:
        print("opcao invalidaa")

def tratar_combinacoes():
     n = informInt('Informe o numero de elementos(n):')
     p = informInt('informe o tamanho dos agrupamentos(n)')
     result = calcular_combinacoes(n,p)
     print(f"o total de combinações é{result:.1f}")


def tratar_arranjos():
    n = informInt('Informe o numero de elementos(n):')
    p = informInt('informe o tamanho dos agrupamentos(n)')
    result = calcular_arranjos(n, p)
    print(f"o total de arranjos é{result:.1f}")



def saber_acao(x):
    if x == 1:
        num = informInt("Qual numero para o saber o primeiro numero para arranjos")
        num2 = informInt("Qual numero para o saber o primeiro segundo para arranjos")
        result = calcular_arranjos(num, num2)
    elif x == 2:
        num = informInt("Qual numero para  combinações")
        num2 = informInt("Qual outro numero para  o combinações")
        result = calcular_combinacoes(num, num2)
    else:
        result = "poggers"
    return result


def calcular_fatorial(num:int)->int:
    if num==1:
        return 1
    return num * calcular_fatorial(num-1)

def calcular_arranjos(n: int,p:int)->float:
    return calcular_fatorial(n) / calcular_fatorial(n-p)

def calcular_combinacoes(n:int,p:int)->float:
    return calcular_fatorial(n)/calcular_fatorial(p) * calcular_fatorial(n-p)