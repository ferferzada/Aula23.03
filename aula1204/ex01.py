def equacao(x):
    x = x ** 2 + 10 * x - 5
    print(x)

if __name__ == "__main__":
    x = None
    while not isinstance(x, int):
        try:
            x = input("Diga o valor de x: ")
            x = int(x)
        except ValueError:
            print("Entrada inválida. Digite um número.")
    
    equacao(x)

