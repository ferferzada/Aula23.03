from fatorial import *
x = 0
while x != 3:
    x = menu()
if x == 1:
    tratar_combinacoes()
elif x == 2:
    tratar_arranjos()
elif x == 3:
    print("opcao invalidaa")
