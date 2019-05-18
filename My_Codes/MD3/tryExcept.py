#encoding: utf-8
# sintaxe:
# try:
#   Você tenta fazer algo aqui...
#   ...
  
# except ExceptionI:
#   Se causar a ExceptionI, roda isso.
#   ...
# else:
#   Se não causar excessões, roda isso.
#   ...
  
# Nós também podemos apenas verificar qualquer exceção apenas com except: 
# Para obter uma melhor compreensão de tudo isso, 
# vamos verificar um exemplo: 
# Vamos ver algum código que abre e grava um arquivo:

# try:
#     f = open('testfile','w')
#     f.write('Test write this')
# except IOError:
#     # Isso só irá verificar se há uma exceção IOError e, em seguida, executar esta declaração de impressão
#    print("Error: Could not find file or read data")
# else:
#    print("Content written successfully")
#    f.close()
   
# Agora, vamos ver o que aconteceria se não tivéssemos permissão de escrita (abrindo apenas com 'r'):
try:
    f = open('testfile','r')
    f.write('Test write this')
except IOError:
    # This will only check for an IOError exception and then execute this print statement
   print("Error: Could not find file or read data- Vacilão")
else:
   print("Content written successfully")
   f.close()
   
   
   
   
   
   
   
   
   
   
   
   
   
   