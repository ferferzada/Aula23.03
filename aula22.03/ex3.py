def calcular_Celsius_Fahren(C):
    f = (C*1.8) + 32
    return print(f"fica em Farenheit {f:.1f}")

if __name__ == "__main__":
     c = float(input("Diga a temperatura em Celsius: "))
     calcular_Celsius_Fahren(c)
