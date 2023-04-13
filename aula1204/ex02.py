prestacoes = int(input("Digite o numero de consorcios: "))
prestacoesPagas = int(input("Prestações pagas: "))
prestacoesPrecos = float(input("Prestações pagas: "))

i = (prestacoes - prestacoesPagas) * prestacoesPrecos

print(f"{i:.2f}")
