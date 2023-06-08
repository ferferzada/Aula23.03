indice = float(input("Informe o indice de poluição medido: "))

if indice >= 0.05 and indice <= 0.25:
    print("O indici de poluição está dentro do aceitavel!")

elif indice >= 0.25 and indice <= 0.3:
    print("Indústrias do 1º grupo devem suspender suas atividades! ")

elif indice > 0.3 and indice <= 0.4:
    print("Indústrias do 1º e 2º grupo devem suspender suas atividades! ")

elif indice > 0.41:
    print("Todos os grupos devem suspender suas atividades! ")

else:
    print("O índice de poluição informado ou é menor de 0.05 ou é inválido.")
