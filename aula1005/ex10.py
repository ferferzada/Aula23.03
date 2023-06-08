saldo_medio = float(input("Informe o saldo medio do ultimo ano: "))

if saldo_medio >= 0 and saldo_medio <=500:
    valor_credito = 0

elif saldo_medio >= 501 and saldo_medio <= 1000:
    valor_credito = 0.2

elif saldo_medio >= 1001 and saldo_medio <= 1600:
    valor_credito = 0.3

else:
    saldo_medio >= 1601
    valor_credito = 0.4

credito = saldo_medio * valor_credito

print (f"O saldo médio foi de R${saldo_medio:.2f}, e o valor de crédito foi de R${credito:.2f}! ")
print (f"Totalizando no valor de R${saldo_medio + credito:.2f}")