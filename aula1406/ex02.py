from ex01 import *

poggers = []

addlist(poggers)

duplo = []

print(poggers)
def teste():
    for dados in range(0,len(poggers), 2):
        x = poggers[dados] * 2
        duplo.append(x)

teste()
print(duplo)
add2 = []
def teste1():
    for dados in range(1,len(poggers),2):
        x = poggers[dados] * 3
        add2 .append(x)

teste1()
print(add2)