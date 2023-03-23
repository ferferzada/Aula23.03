
def tempoVida(anos):
    dias = anos * 365
    horas = dias * 24
    return print(f"Ele viveu {dias} dias, e {horas} horas")

if __name__ == "__main__":
    anos = int(input("Diga quantos anos vc tem: "))
    tempoVida(anos)

