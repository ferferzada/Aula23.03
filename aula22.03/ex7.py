def multaDup(preco,tempo):
    multa = preco * 0.05 * tempo
    return print(f"O Preço com a multa fica {preco + multa}")
    


if __name__ == "__main__":
    preco = float(input("Diga o preço: "))
    tempo = int(input("Diga o tempo: "))
    multaDup(preco,tempo)