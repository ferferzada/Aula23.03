def calculo(x):
    calculo = x*x + (x*2)-4
    return print(f"Calculo da equação é {calculo:.2f}")


if __name__ == "__main__":    
    x = float(input("Diga o valor de x: "))
    calculo(x)