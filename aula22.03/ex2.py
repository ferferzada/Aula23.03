def calculo(x):
    calculo = x*x + (x*2)-4
    print(f"Calculo da equação é {calculo:.2f}")

if __name__ == "__main__":
    x = None

    while not isinstance(x, float):
        try:
            x = input("Diga o valor de x: ")
            x = float(x)
        except ValueError:
            print("Entrada inválida. Digite um número.")

    calculo(x)
    