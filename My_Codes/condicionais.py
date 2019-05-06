#encoding: utf-8


# sintaxe:
# if case1:
#      executar ação1
#  elif case2:
#      execute ação2
#  else:
#      execute a ação 3

if True:
  print('It was true')


x = True
if x:
  print('X is true')
else:
  print('x is false')

i = 6 #indice do aluno

a = [10,9,9,8,5,10,7] #notas

if a[i] >= 9:
  print('Aprovado')
elif a[i] >= 7:
  print('Recuperação')
else:
  print('Reprovado')



p = 0
aluno = {'Oseias': 7, 'Gustavo':7,'Cristian': 9}
nomeAluno ='Oseias'

if aluno[nomeAluno] >= 9:
  print('O aluno: %s foi aprovado' %(aluno.keys()[0]))
elif aluno[nomeAluno] >=7:
  print('O aluno: %s está de recuperação' %(aluno.keys()[0]))
else:
  print('O aluno: %s está reprovado' %(aluno.keys()[0]))