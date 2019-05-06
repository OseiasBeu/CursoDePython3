#encoding: utf-8

#Listas são mutáveis diferente das strings

my_list = [1,2,3,4,5,6,7]
print(my_list)

my_list2 = [1,2,3,3, 'string']
print(my_list2)

my_list2[0]
print(my_list[2:])
print(my_list2[4])
print(my_list2[-1])

print(my_list + my_list2)

my_list = my_list + ['mais um item']
print(my_list)


#Métodos de Listas
print(type(my_list))

print(len(my_list))

my_list.append('outro item') #adiciona um item no final da lista
print(my_list)

var = my_list.pop() #Remove o último item da lista
print(var) #itém removido
print(my_list)

my_list.pop(3) #Remove  o itém da posição passada
print(my_list)

new_list = ['a','e','x','b','c']
print(new_list)
new_list.reverse() #Inverte a ordem da lista
print(new_list)

new_list.sort() #Ordena a lista
print(new_list[::-1]) #Reverse utilizando indexação

print(new_list)


#Listas dentro de listas = Alinhamento
lst_1=[1,2,3]
lst_2=[4,5,6]
lst_3=[7,8,9]

matrix = [lst_1,lst_2,lst_3]
print(matrix)

print(len(matrix))

print(len(matrix[0]))

res=matrix[1][2]

print(res)


#Compreensão de listas

first_col = [row[0] for row in matrix]
print(first_col)


nova_lista = first_col = [matrix[0][0],matrix[1][0],matrix[2][0]]
print(nova_lista)