#encoding: utf-8
#Existem dois outros tipos de objetos em pyhton Sets(conjuntos) e Booleanos

#Set = um conjunto de dados; sua única diferença entre listas e dicionários é que os sets só permitem valores únicos

x = set()
print(type(x))
print(x)
#para adicionar elementos
x.add(1)
x.add(2)
print(x)

l = [1,1,2,2,3,4,5,6,1,1]
print(l)
set_lista = set(l)
print(set_lista)