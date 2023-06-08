import random
acertou = False
sorteio = random.randint(0,100)

for i in range(1,11):
    p = int(input("POGGERS: "))

    if p == sorteio:
        print("certo")
        acertou =  True
    else: 
        if p > sorteio:
            print("NUMERO Q VC DIGITO E MAIOR Q U SURTEIO")
        else:
            print("NUMERO Q VC DIGITO E menor Q U SURTEIO")
        print('erro')

if not acertou:
    print(f"VIOLENCIA  {sorteio