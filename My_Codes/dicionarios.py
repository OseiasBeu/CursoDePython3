#encoding: utf-8

# Dicionário é um tipo diferente de coleção. 
# Ele é um tipo de mapeamento nativo do Python. 
# Um mapa é uma coleção associativa desordenada.
# A associação, ou mapeamento, é feita a partir de uma chave, 
# que pode ser qualquer tipo imutável, para um valor, 
# que pode ser qualquer objeto de dados do Python.

#criando um dicionario  
my_dic = {'chav1':'value1','chav2':'value2'}
dic = type(my_dic)

print(dic)
print(my_dic)

#acessando valores a partir das chaves
print(my_dic['chav2'])


#é possível utilizar funções de strings e de números na saída de um dicinário
my_dic2 = {'chav1':'value1','chav2':'value2', 2:'string'}
print(my_dic2[2].upper())

#trabalhando com arrays dentro dos dicionários
my_dic3 = {'key1':123,'key2':[12,23,33,[0,9,8,7]],'key3':['item0','item1','item2']}
print(my_dic3['key3'])
print(my_dic3['key2'][3][2])

#insrindo novos itens no dicionário
d = {}
d['CHAVE1'] ='VALOR1'
print(d)

d['CHAVE2'] = 'VALOR2'
print(d)

#Métodos para trabalhar com dicionário
ret = my_dic3
print(ret.keys()) #retorna as chaves
print(ret.values()) #retorna os valores
print(ret.items()) #retorna todas as tuplas (todos os iténs de um dicionário)



e = {'k1':[{'nest_key':['this is deep',['hello']]}]}
e['k1'][0]['nest_key'][1]


# Esse é chato...
f = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
f['k1'][2]['k2'][1]['tough'][2][0]