#encoding: utf-8


#** Escreva um programa que imprima os números inteiros de 1 a 100. 
#Para múltiplos de três imprima "Fizz" ao ivés do número, e para os múltiplos de cinco imprima "Buzz". 
#Para números que são múltiplos de três e cinco imprima "FizzBuzz". **

lista = [n for n in range(0 ,101)]
print(lista)

for num in lista:
    if num % 3 == 0 and  num % 5 == 0:
        print('FizzBuzz', num)
    elif num % 5 == 0:
        print('Buzz',num)
    elif num % 3 == 0:
        print('Fizz', num)
    else:
        print(num)
print(lista)
print('=====--FIM--====')
