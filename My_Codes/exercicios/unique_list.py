#encoding: utf-8
# ** Escreva uma função Python que recebe uma lista e retorna uma nova lista com elementos exclusivos da primeira lista. **

#  Lista de Amostras: [1,1,1,1,2,2,3,3,3,3,4,5]
#  Lista única: [1, 2, 3, 4, 5]

listaAmostral = [1,1,1,1,2,2,3,3,3,3,4,5]


def uniqueList(l):
  return list(dict.fromkeys(l))

a = uniqueList(listaAmostral)
print(a)


def unique_list(l):
  return list(set(l))

b = unique_list(listaAmostral)
print(b)