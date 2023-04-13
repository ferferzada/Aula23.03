clientesiso = 80 #int(input("Digite a quantidade de clientes com pendencias"))
clientesPar = 30 #int(input("Clientes com parcelas em dia: "))
clientesAtr = 40 #int(input("Cliente com atraso"))

somaClientes = clientesAtr + clientesiso + clientesPar
print(somaClientes)
iso = int(clientesiso *100/somaClientes)
print(iso)
atr = int(clientesAtr *100/somaClientes)
print(atr)
par = int(clientesPar*100/somaClientes)
print(par)

print(atr + par + iso)
