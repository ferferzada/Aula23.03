from importacao.inform import *

def menu():
    print("Qual das opções quer seguir \n"
          "Opção 1 ==>Pizza normal = R$ 15,00 \n"
          "Opção 2 ==>Pizza Gourmet = R$ 20,00\n"
          "Opção 3 ==>Pizza Premium = R$ 30,00")
    return verificiar(informInt("Qual opção você quer: "))

def verificiar(x:int):

            if x == 1:
                return pizza_normal()
            elif x == 2:
                return pizza_gourmet()
            elif x == 3:
                return pizza_premium()
            elif x > 3 or x < 1:
                print("Entrada inválida. Por favor, informe um numero do cardapio")
                return menu()

def decidir_tamanho(x:str)->str:
    print("Tamanho normal?\n"
          "**ou**\n"
          "tamanho grande \n"
          "**ou**\n"
          "tamanho gigante?\n")
    while True:
        try:
            t = input("Qual tamanho? ")
            tamanho = (t.lower()).strip()
            if tamanho == "grande":
                custo = x * 0.2
                preco = x + custo
                return print(f"O preço da pizza vai {preco:.2f}")
            elif tamanho == "gigante":
                custo = x * 0.4
                preco = x + custo
                return print(f"O preço da pizza vai {preco:.2f}")
            elif tamanho == "normal":
                return print(f"O preço da pizza vai {x:.2f}")

        except:
             print("Infomarção invalida, digite novamente")
def pizza_normal():
    x = 15.00
    decidir_tamanho(x)
def pizza_gourmet():
    x = 20.00
    decidir_tamanho(x)
def pizza_premium():
    x = 30.00
    decidir_tamanho(x)


