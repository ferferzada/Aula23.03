

contaPagas = int(input("digite o valor que pagou: "))
conta = int(input("valor da conta: "))
troco = contaPagas- conta
print(f"o troco deu {troco}")
trocoCom100= int(troco / 100)
print(f"numero de nota de 100 são {(trocoCom100)}")
troco = troco -(trocoCom100*100)
print(troco)
trocoCom10 = int(troco / 10)
print(f"numero de notas de 10 são {(trocoCom10)}")
troco = int(troco-(trocoCom10*10))

print(f"numero de notas de 1 são {(troco)}")


