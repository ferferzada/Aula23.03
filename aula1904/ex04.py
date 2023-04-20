num1 = float(input("digite um numero: "))
num2 = float(input("digite outro numero"))
num3 = float(input("digite outro numero"))

if num1 > num2 and num1 > num3:
    print(f"o numero {num1} é maior que outros")
elif num2> num1 and num2> num3:
    print(f"o numero {num2} é maior que outros")
else:
    print(f"o numero {num3} é maior que outros")