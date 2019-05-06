#encoding: utf-8
# ** Escreva uma função Python que aceita uma string e calcule o número de maiúsculas e minúsculas. **

#  Exemplo de Cadeia: 'Olá Sr. Rogers, como você está bem, terça-feira?'
#  Saída esperada:
#  Número de caracteres maiúsculas: 4
#  Número de caracteres minúsculos: 33
# Se você se sentir ambicioso, explore o módulo de Coleções para resolver esse problema!

frase = []
frase = [letter for letter in 'Olá Sr. Rogers, como você está bem, Terça-feira?']
print(frase)

def upLow(texto):
  lC = []
  uC = []
  for l in texto:
    if l.isupper():
      uC.append(l)
      print(l)
    elif l.islower():
      lC.append(l)
      print(l)
  
  print('Número de caracteres maiúsculas: %i' %(len(uC)))
  print('Número de caracteres minúsculos: %i' %(len(lC)))

upLow(frase)