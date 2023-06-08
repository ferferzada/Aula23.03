def obter_valor_obsoluto(x:int) ->int:
    if x < 0:
      return x * -1
    return x

x = int(input("Informe um número: "))

absoluto = obter_valor_obsoluto(x)
print(absoluto)


