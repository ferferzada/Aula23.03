clientesiso = int(input("Digite a quantidade de clientes com pendencias"))
clientesPar = int(input("Clientes com parcelas em dia: "))
clientesAtr = int(input("Cliente com atraso"))

somaClientes = clientesAtr + clientesiso + clientesPar
print(somaClientes)
iso = int(clientesiso *100/somaClientes)
print(iso)
atr = int(clientesAtr *100/somaClientes)
print(atr)
par = int(clientesPar*100/somaClientes)
print(par)

print(atr + par + iso)
