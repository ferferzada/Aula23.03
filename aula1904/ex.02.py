def calculo(x):
    if x > 0:
        print(f"{x**2:.2f}")
    else:
        print(f'{x **(1/2)}')

x = int(input("DIgite um  numero"))

calculo(x)