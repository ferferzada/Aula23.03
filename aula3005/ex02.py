def verMaior(x:int,y:int) ->int:
    return x if x > y else y
        
x = int(input("DIGITE PRIMEIRO NUMERO:"))

y = int(input("DIGITE SEGUNDO NUMERO:"))


print(f'o maior numero entre os 2 é zap {verMaior(x,y)}')