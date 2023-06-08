from function.inform import *
def areaQuadrado(largura:float)->float:
    return largura ** 2

def areaCirculo(raio:float)->float:
    return (3.14*(raio**2))

def areaTriangulo(base:float,altura:float)->float:
    return (base*altura)/2
def validar_opcao(opcao:int)->bool:
    return opcao in (1,2,3)

def obter_opcao()->int:
    opcao = 0
    while not validar_opcao(opcao):
            print('** menu de opção**\n'
            '1 - Area do quadrado\n'
              '2 - Area do Circulo\n'
              '3 - Area do Triangulo ')
            opcao = informInt("===>")
            if opcao not in (1,2,3):
                print("** Opção invalidada, tente novamente")
    return opcao



def definirArea(opcao:int):
    if opcao == 1:
        num1 = informFloat("Informe a largura:")
        return print(f"a area do quadrado é {areaQuadrado(num1)}")
    elif opcao == 2:
        raio = informFloat("Informe o raio do circulo:")
        return print(f"a area do circulo é {areaCirculo(raio)}")
    elif opcao == 3:
        base = informFloat("informe a base triangulo:")
        altura = informFloat("informe a altura do triangulo:")
        return print(f"a area do trinagulo é {areaTriangulo(base, altura)}")
