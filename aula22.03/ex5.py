def mestre_obras(metros):
    argamassa =  metros / 5
    rejunte =  metros / 3
    return print(f"A casa usara {argamassa} de Argamassa, e de rejunte é {rejunte} ")

if __name__ == "__main__":
    metros = float(input("Diga em Metros Quadrados o tamanho da casa: "))
    mestre_obras(metros)