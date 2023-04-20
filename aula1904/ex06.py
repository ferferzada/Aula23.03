lado1 = float(input("Digite um tamanho do primeiro lado: "))
lado2 = float(input("Digite um tamanho do segundo lado: "))
lado3 = float(input("Digite um tamanho do terceiro lado: "))

if lado1 == lado2 and lado1 == lado3:
    triangulo = "triângulo Equiláterio"
elif lado2 != lado1 and lado2 != lado3:
    triangulo = "Triângulo Escaleno"
else:
    triangulo = "Triângulo Isósceles"

if ((lado1 + lado2) > lado3) or ((lado1 + lado2)==lado3):
    print(f"Ele é um {triangulo}")
else:
    print("não é um triangulo")