def F_para_C(F):
    C = (F-32)*1.8
    return print(f"Em Celsius fica {C:.1f}")

if __name__ == "__main__":
    F = float(input("Digite a temperatura em fireCELTAS: "))
    F_para_C(F)  