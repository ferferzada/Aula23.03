funcao = input("Informe a sua função, sendo elas testador, analise de testes, programador, analista de sistemas, DBA: ")
horas_trabalhadas = float(input("Informe a quantidade de horas trabalhadas: "))

if funcao == ("testador"):
    salario = horas_trabalhadas * 20.00

elif funcao == ("analise de teste"):
    salario = horas_trabalhadas * 35.00

elif funcao == ("programador"):
    salario = horas_trabalhadas * 45.00

elif funcao == ("analista de sistemas"):
    salario = horas_trabalhadas * 40.00

elif funcao == "DBA":
    salario = horas_trabalhadas * 50.00
else:
    salario = None

if salario == None:
    print("É invalida")
else:

 print(f"A função de {funcao} depois de {horas_trabalhadas} horas trabalhadas vai receber um salario de R$:{salario:.2f}")

