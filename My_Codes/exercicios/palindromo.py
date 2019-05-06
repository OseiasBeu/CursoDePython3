#encoding: utf-8
#** Escreva uma função Python que verifica se uma string passada é palindrome ou não. **

#Nota: Um palíndromo é palavra, frase ou seqüência que lê o mesmo para trás.
#
a = 'Roma me tem amor.'
b = 'Socorram-me, subi no ônibus em Marrocos!'
c = 'A mala nada na lama.'
d =  'A grama é amarga.'
e = 'A Rita, sobre vovô, verbos atira.'
f = 'Olé! Maracujá, caju, caramelo!'
g = 'Rir, o breve verbo rir.'
h = 'Anotaram a data da maratona.'

teste = [t1 for t1 in 'abcdefgh']
print(teste)

# s = s.replace(' ','') # Isso substitui todos os espaços "" sem espaço ". (Soluciona problemas com strings que têm espaços)

# def palindromo(pal):
#   pal = pal.replace(' ')
#   normal = []
#   reverse = []
#   for p in pal:
#     normal.append(p)
#   print(normal)
#   reverse = normal[::-1]
#   print(reverse)
#   if normal[0] == reverse[0] and normal[len(normal)-1] == reverse[len(reverse)-1]:
#     print('Está palavra é um palíndromo')
#   else:
#     print(normal[0])
#     print(reverse[0])
#     print('Está palavra não é um palíndromo')


# def testaFunc(lista):
#   for t in lista:
#     palindromo(t)

# testaFunc(teste)

def palindromo(s):
  s = s.replace(' ','')
  s = s.replace('.','')
  s = s.replace(',','')
  s = s.replace('-','')
  s = s.replace('_','')
  s = s.replace('!','')
  s = s.replace('^','')
  s = s.lower()
  print(s)
  if s == s[::-1]:
    print('É um palíndromo')

palindromo(e) 
