def ler (pag:int ,pagLen ):
    return print(f"Demora {pag/pagLen:.0f} dias para ler TUDO")


x= int(input("QUANTAS PAGINAS TEM O LIVRO: "))
y= int(input("QUANTAS VOCE LE POR DIA: "))


ler(x,y)