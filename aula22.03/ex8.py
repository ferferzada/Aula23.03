def tempoVida(anos):
    dias = anos * 365
    horas = dias * 24
    print(f"Ele viveu {dias} dias, e {horas} horas")

if __name__ == "__main__":
    
    anos = -1
    
    while anos <= 0:
        try:
            anos = int(input("Digite sua idade em anos: "))
            if anos <= 0:
                raise ValueError("A idade não pode ser negativa, ou zero")
            else:
                tempoVida(anos)
        except ValueError as error:
            print(f"Valor inválido: {error}")
            print("Por favor, digite um valor positivo para a idade.")
