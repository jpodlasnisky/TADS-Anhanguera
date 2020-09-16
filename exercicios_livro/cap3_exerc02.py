# Author João Pedro Podlasnisky
# Date 16/set/2020
# 

#  Teste 1
def teste1():
    a = int(input('Digite A: '))
    b = int(input('Digite B: '))
    c = int(input('Digite C: '))
    return a < b and a < c

#  Teste 2
def teste2():
    a = int(input('Digite A: '))
    b = int(input('Digite B: '))
    c = int(input('Digite C: '))
    return a < b or a < c

#  Teste 3
def teste3():
    a = int(input('Digite A: '))
    b = int(input('Digite B: '))
    c = int(input('Digite C: '))
    return a >= 0 and b == c

#  Teste 4
def teste4():
    a = int(input('Digite A: '))
    b = int(input('Digite B: '))
    c = int(input('Digite C: '))
    return a >= 0 and b == c

#  Teste 5
def teste5():
    a = int(input('Digite A: '))
    b = int(input('Digite B: '))
    c = int(input('Digite C: '))
    return a >= 0 or b == c

#  Teste 6
def teste6():
    a = int(input('Digite A: '))
    b = int(input('Digite B: '))
    c = int(input('Digite C: '))
    return a >= 0 or b == c

#  Teste 7
def teste7():
    a = int(input('Digite A: '))
    b = int(input('Digite B: '))
    c = int(input('Digite C: '))
    return b is not 0 and a is not c

#  Teste 8
def teste8():
    a = int(input('Digite A: '))
    b = int(input('Digite B: '))
    c = int(input('Digite C: '))
    return b is not 0 and a is not c
    

#  Teste 9
def teste9():
    a = int(input('Digite A: '))
    b = int(input('Digite B: '))
    c = int(input('Digite C: '))
    return b is not 0 or a is not c

#  Teste 10
def teste10():
    a = int(input('Digite A: '))
    b = int(input('Digite B: '))
    c = int(input('Digite C: '))
    return b is not 0 or a is not c

# Pedindo as entradas e mostrando os resultados    

print(teste1())
print(teste2())
print(teste3())
print(teste4())
print(teste5())
print(teste6())
print(teste7())
print(teste8())
print(teste9())
print(teste10())