#encoding: utf-8

#Funçẽos onde conseguimos definir com apenas uma linha e sua existência será temporária

def square(num): return num ** 2
#    result = num**2
#    return result
#    return num ** 2



squ = lambda  num: num ** 2

par = lambda x: x % 2 ==0

primeiroChar = lambda letra: letra[0]

invertString = lambda strin: strin[::-1]

print(invertString('olá mundo!!!'))

print(primeiroChar('Olá mundo!!!'))

print(par(10))

print(squ(4))

print(square(2))
