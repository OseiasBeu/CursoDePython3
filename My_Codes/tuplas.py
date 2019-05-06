#encoding: utf-8

#Tupla é um tipo de dado em pyhton bastante semelhante a listas.
#pode-se criar uma tupla com múltiplos elementos
#também podemos trabalhar com múltiplos tipos de dados
#uma tupla é imutável, portando não pode ser modificada
#não possuí o método append(),portanto não podemos incluir nada dentro dela

t = (1,2,3,4,4,4,4,4,4)
print(type(t))

print(t[2])

#Métodos de tuplas
t1 = t.index(2) #Passo o valor e ela me retorna a posição do valor
print(t1)

t2 = t.count(4) #Passo um elemento e ela me retornar a quantidade de repetições desse elemento
print(t2)

