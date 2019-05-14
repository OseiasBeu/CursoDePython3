#encoding: utf-8

my_file = open('/home/oseiasbeu/Documents/pyhton/cursoDeP3/Python Completo/My_Codes/Texto.txt')

print(my_file)

print(my_file.read())

print(my_file.readline())

my_file.seek(0)
print(my_file.readline())

#Fazendo o loop para ler caractere  à caractere
for car  in my_file.readline():
  print(car)

#Fazendo o loop para ler linha a linha
for line  in my_file:
  print(line)

