#encoding: utf-8

lista = [1,2,3,45,6,7,8,9,12,34,56,76,88,99,11,45,18,46,95,75,24,57,97,0]

for num in lista:
  if num == 0:
    print('O número: %i é neutro.' %(num))
  elif num % 2 == 0:
    print('O número: %i é par.' %(num))    
  else:
    print('O número: %i é impar.' %(num))

sum_ = 0
for num in lista:
  sum_ += num
  print(num)
  print(sum_)

print('Soma total: %i' %(sum_))



string = 'Salmos 191'
for letra in string:
  print(letra)


#As tuplas tem uma característica em específico quando estamos iterando nelas:
#tuple banking
t = (1,2,3,4,5,6,7)
for p in t:
  print(p)

#Uma lista composta por tuplas:
l = [(1,2),(2,3),(3,4)]
print(type(l))
print(type(l[0]))
#podemos desembalar as tuplas da seguinte forma:
(t1,t2) = l[0]
print(t1)
print(t2)

for (t1,t2) in l:
  print(t1*t2)

#dicionario
d = {'c1':1,'c2':2,'c3': 3}
for item in d:
  print(item)

for item in d.items():
  print(item)

for (chave, valor) in d.items():
  print(chave, ':' ,valor)