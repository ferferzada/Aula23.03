def pessoas():
    pessoas = int(input("Quantas pessoas são?"))
    sexo = int(input("Quantas homens são?"))
    return media(pessoas,sexo)

def media(pes,sexo):
    mulheres= pes - sexo
    homens = sexo


    print(f"os Homens vão comer {homens*400} gramas de carne e beber {homens*5} de latinhas de cerveja")
    print(f"os Mulheres vão comer { mulheres* 300} gramas de carne e beber {mulheres * 2} de latinhas de cerveja")

pessoas()
