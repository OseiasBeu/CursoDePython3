#encoding: utf-8

print(type('olá'))

print(type(3))

print('Olá, mundo!')

#quebra de linha com \n e espaço com \t
print('Olá \n mundo!')
print('Olá \t mundo!')

#método len() conta a quantidade de caracteres que minha variável tem
print(len('Olá, mundo!'))

s = 'O Senhor é meu Pastor e nada me faltara!'
print(s)
qtd = len(s)
print(qtd)

#acessando determinadas posições dentro de uma variável string
print(s[:])

print(s[0]) #o elemento de indice 0 na variável s
print(s[2]) #o elemento de indice 2 na variável s
print(s[4]) #o elemento de indice 4 na variável s

print(s[2:8])#quero começar a leitura a partir do indice 2 e terminar no índice 8
print(s[:-2])


#Indexação com espaçamentos
print(s[::1])
print(s[::2])
print(s[::3])
print(s[::-1]) #inverte todos os caracteres
print(s[::-2])


#Propriedades de strings
#Strings são imutáveis (seus elementos de forma indicidual não são alteráveis)
#São concatenáveis

s = s+'-Salmos'
print(s)

#repetição de elementos

print(s* 10)


#Métodos embutidos em strings
print(s.upper)
print(s.lower)
print(s.split())
print(s.split(','))
print(s.casefold())