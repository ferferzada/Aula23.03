num1, num2, num3 = sorted(map(int, input("Digite três números separados por espaço: ").split()))

if num1 % 2 == 0:
    print(f"O {num1} é par, ele é o menor número entre os 3.")
else:
    print(f"O {num1} é ímpar, ele é o menor número entre os 3.")