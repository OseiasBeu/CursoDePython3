x = []

for i in range(0,30):
    x +=[i]
#x.append(i)
print(x)
#Compreensã em lista nos permite criar a mesma lista de várias formas diferentes.

x2 = [i for i in range(0,30)]
print(x2)

#Criação de listas em pares

x3 = []

for i in range(0,30):
    if i % 2 == 0:
        x3 += [i]
print(x3)

x4 = [i for i in range(0,30) if i % 2 == 0]
print(x4)

x5 = []
x5 = [letter for letter in 'word']
print(x5)

#Conversão de temperatura de Celsius para Fahrenheit

celsius = [0,10,15,20,30,40,100]
fahrenheit = [(temp * ( 9/5 ) + 32 ) for temp in celsius]
print(celsius)
print(fahrenheit)
