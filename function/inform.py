def informInt(mensagem: str) -> int:

    while True:
        try:
            numero = int(input(mensagem))
            return numero
        except ValueError:
            print("Entrada inválida. Por favor, informe um número inteiro.")

def informFloat(mensagem: str) -> float:
    while True:
        try:
            numero = float(input(mensagem))
            return numero
        except ValueError:
            print("Entrada inválida. Por favor, informe um número válido.")

