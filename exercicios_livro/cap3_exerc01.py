# Author João Pedro Podlasnisky
# Date 16/set/2020
# 

#  Teste 1
def teste1():
    a = int(input('Digite A: '))
    b = int(input('Digite B: '))
    return a > b

#  Teste 2
def teste2():
    x = int(input('Digite X: '))    
    return x <= 10.0

#  Teste 3
def teste3():
    a = int(input('Digite A: '))
    b = int(input('Digite B: '))
    return a-b >= 0

#  Teste 4
def teste4():
    a = int(input('Digite A: '))
    b = int(input('Digite B: '))
    n = int(input('Digite N: '))
    return a*b < n

#  Teste 5
def teste5():
    a = int(input('Digite A: '))
    b = int(input('Digite B: '))
    c = int(input('Digite C: '))
    return 10*a >= b*c

#  Teste 6
def teste6():
    a = int(input('Digite A: '))
    b = int(input('Digite B: '))
    c = int(input('Digite C: '))
    return 10*a >= b*c

#  Teste 7
def teste7():
    n = int(input('Digite N: '))
    return n % 2 == 0

#  Teste 8
def teste8():
    n = int(input('Digite N: '))
    return n % 2 == 0
    
#  Teste 9
def teste9():
    t = int(input('Digite T: '))
    return t == 'BANANA'

#  Teste 10
def teste10():
    t = int(input('Digite T: '))
    return t > 'BANANA'

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
