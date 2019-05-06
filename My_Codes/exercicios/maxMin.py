#encoding: utf-8

#Escreva uma função que verifica se um número está em um determinado intervalo (inclusive o máximo e mínimo)

def maxMin(num, minimo, maximo):
  for n in range(minimo,maximo):
    if num < maximo and num > minimo:
      print('%i está no range' %(num))
      break
    else:
      print('O número não está dentro do range')
      break

maxMin(9,2,10)


def ran_ch(num, low,high):
  if num in list(range(low, high+1)):
    return True
  else:
    return False

print(ran_ch(5,6,60))