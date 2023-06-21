from importacao.inform import *

def menu():
    print("Qual das opções quer seguir \n"
          "Opção 1 ==>Pizza normal \n"
          "Opção 2 ==>Pizza Gourmet\n"
          "Opção 3 ==>Pizza Premium")
    return verificiar(informInt("Qual opção você quer: "))

def verificiar(x:int):

            if x == 1:
                return pizza_normal()
            elif x == 2:
                return pizza_gourmet()
            elif x == 3:
                return pizza_premium()
            elif x > 3:
                print("Entrada inválida. Por favor, informe um número válido.")
                return menu()

def decidir_tamanho(x:str)->str:
    print("Tamanho grande?\n"
          "**ou**\n"
          "tamanho gigante?\n")
    while True:
        try:
            t = input("Qual tamanho?")
            tamanho = (t.lower()).strip()
            if tamanho == "grande":
                custo = x * 0.2
                preco = x + custo
                return print(f"O preço da pizza vai {preco:.2f}")
            elif tamanho == "gigante":
                custo = x * 0.2
                preco = x + custo
                return print(f"O preço da pizza vai {preco:.2f}")
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
