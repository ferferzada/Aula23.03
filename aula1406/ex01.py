poggers = []
from random import randint
def addlist(x):
    for i in range(10):
        x.append(randint(0,100))


def saber_par():
    for dados in range(0,len(poggers),2):

            print(dados)


addlist(poggers)
saber_par()