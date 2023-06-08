populacao = int(input('DIgite sua população: '))

taxa = float(input('Informe o aumento de PUPULIZAO: '))

for i in range(1, 16):
    populacao += int(populacao *( taxa / 100))
    print(f"No {i} ano apos a pesquisa teve a {populacao}  de populacao")

    