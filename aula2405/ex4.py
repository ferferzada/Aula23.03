import sys 

maior = -sys.maxsize
menor = sys.maxsize

for i  in range(10):
    num  =  int(input('informe um numerio inteiro: '))
    if maior < num:
        maior = num
    if menor > num:
        menor = num 

print(f"o maior numero informado foi {maior}")
print(f"o menor numero informado foi {menor}")