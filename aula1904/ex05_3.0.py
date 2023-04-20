num1 = int(input("digite um numero: "))
num2 = int(input("digite outro numero: "))
num3 = int(input("digite outro numero: "))


if num1 < num2 and num1 < num3:
    menorNum=num1
elif num2< num1 and num2< num3:
     menorNum=num2
else:
     menorNum=num3

if menorNum % 2 == 0:
    print(f"numero {menorNum} é par")
else:
    print(f"numero {menorNum} é impar")