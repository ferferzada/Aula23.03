qtde_internet = int(input('Informe o consumo de internet: '))
qtde_local = int(input('Informe o consumo de ligações locais: '))
qtde_interurbano = int(input('Informe o consumo de ligações interurbanas: '))
qtde_torpedo = int(input('Informe o consumo de torpedos: '))

valor_internet = qtde_internet * 0.5
valor_local = qtde_local * 0.35
valor_interurbano = qtde_interurbano * 0.6
valor_torpedo = qtde_torpedo * 0.2

total_sem_desconto = valor_internet + valor_local + valor_interurbano + valor_torpedo
print(f'Total da fatura sem desconto: R$ {total_sem_desconto:.2f}')

desconto = 0
tipo_desconto = ''

if qtde_internet > 50:
    desconto = valor_internet * 0.05
    tipo_desconto = 'internet'

if qtde_local > 200:
    desconto_local = valor_local * 0.1
    if desconto_local > desconto:
        desconto = desconto_local
        tipo_desconto = 'ligação local'

if qtde_interurbano > 150:
    desconto_interurbano = valor_interurbano * 0.1
    if desconto_interurbano > desconto:
        desconto = desconto_interurbano
        tipo_desconto = 'ligação interurbana'

if qtde_torpedo > 50:
    desconto_torpedo = valor_torpedo * 0.2
    if desconto_torpedo > desconto:
        desconto = desconto_torpedo
        tipo_desconto = 'torpedos'

if desconto != 0:
    print(f"O desconto será sobre o serviço: {tipo_desconto}")
    print(f"O valor do desconto será de R$ {desconto:.2f}")

    total_com_desconto = total_sem_desconto - desconto
    print(f"O total com desconto será R$ {total_com_desconto:.2f}")
else:
    print('Não haverá desconto')