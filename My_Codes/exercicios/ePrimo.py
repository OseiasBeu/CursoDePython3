#encoding: utf-8

def ePrimo(num):
    for n in range(2,num):
        if num % n == 0:
            print('Não é primo')
            break
        else:
            print('É primo')

#ePrimo(2)
ePrimo(4)

