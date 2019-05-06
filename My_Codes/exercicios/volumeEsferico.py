#encoding: utf-8

#Escreva uma função que calcula o volume de uma esfera dado seu raio.
#V = (4/3) π r3, onde r é o raio da esfera e π é a constante pi (3,14)

def vol(rad):
  return  (4.0/3)*(3.14)*(rad **3)

v = vol(5)
print('%10.2f cm cubicos'%(v))