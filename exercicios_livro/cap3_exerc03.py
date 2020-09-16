# Author João Pedro Podlasnisky
# Date 16/set/2020
# 

#  Teste 1
def teste1():
    a = int(input('Digite A: '))
    b = int(input('Digite B: '))
    c = int(input('Digite C: '))
    return a < b and a < c or c != 0

#  Teste 2
def teste2():
    a = int(input('Digite A: '))
    b = int(input('Digite B: '))
    c = int(input('Digite C: '))
    return a < b and (a < c or c != 0)

#  Teste 3
def teste3():
    a = int(input('Digite A: '))
    b = int(input('Digite B: '))
    c = int(input('Digite C: '))
    return not (a>=0 and b == c)

#  Teste 4
def teste4():
    a = int(input('Digite A: '))
    b = int(input('Digite B: '))
    c = int(input('Digite C: '))
    return not (a >= 0) and not (b == c)

#  Teste 5
def teste5():
    a = int(input('Digite A: '))
    b = int(input('Digite B: '))
    c = int(input('Digite C: '))
    return (a >= 0 or b == c) and b > a

#  Teste 6
def teste6():
    a = int(input('Digite A: '))
    b = int(input('Digite B: '))
    c = int(input('Digite C: '))
    return not (a <= b) or c > b

#  Teste 7
def teste7():
    a = int(input('Digite A: '))
    b = int(input('Digite B: '))
    c = int(input('Digite C: '))
    return not (a <= 0 or c > b)

#  Teste 8
def teste8():
    a = int(input('Digite A: '))
    b = int(input('Digite B: '))
    c = int(input('Digite C: '))
    return a == 0 and b != 0 and c == 0
    

#  Teste 9
def teste9():
    a = int(input('Digite A: '))
    b = int(input('Digite B: '))
    c = int(input('Digite C: '))
    return a == 0 and b != 0 and c == 0

#  Teste 10
def teste10():
    a = int(input('Digite A: '))
    b = int(input('Digite B: '))
    c = int(input('Digite C: '))
    return a == 0 or b != 0 or c == 0

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