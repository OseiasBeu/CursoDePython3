#encoding: utf-8

#Strings
print('This is String!')

s= 'STRING'
print('Temos uma %s auxíliar.' %(s))


n= 123
print('Temos uma %s auxíliar.' %(n))

#Pontos Flutuantes

print('Floating point numbers: %10.2f' %(13.144))
#print('Flutuantes: %f' %(13,141516))

a1 = 'string'
a2 = 12345
print('Temos uma string aqui: %s.\nTemos um inteiro aqui: %r' %(a1,a2))

#Métodos de strings
#.format()

a3 = 'One:{a}, Two:{b}, Three:{c}'
print(a3)

a4 = 'One:{a}, Two:{b}, Three:{c}'.format(a=1,b='two',c = 12.3)
print(a4)