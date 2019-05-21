#encoding: utf-8


#PROBLEM 1
# try:
#   for i in ['a','b','c']:
#     print(i**2)
# except (RuntimeError, TypeError, NameError):
#   print('deu ruim!!!')  
  
# class B(Exception):
#   pass

# class C(B):
#     pass

# class D(C):
#     pass

# for cls in [B, C, D]:
#     try:
#         raise cls()
#     except D:
#         print("D")
#     except C:
#         print("C")
#     except B:
#         print("B")


#PROBLEM 2
# X = 5
# Y = 0  
# try:
#   Z =Y/X
# except ZeroDivisionError:
#   print('deu ruim')
# finally:
#   print('tente de novo mané')

### Problema 3
# Escreva uma função que solicite um número inteiro e imprima o quadrado dele. 
# Use um loop while com  um try, except e else para contabilizar as entradas incorretas.

def sqrt_(i):
  sqrtI = i**2
  return sqrtI


try:
  a = sqrt_(2)
  print(a)
except:
  print('Deu ruim')