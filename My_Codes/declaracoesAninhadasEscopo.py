#encoding: utf-8
"""
Essa idéia de scope em seu código é muito importante para entender para atribuir e chamar nomes de variáveis ​​adequadamente.

Em termos simples, a idéia de scope pode ser descrita por 3 regras gerais:

1. As atribuições de nomes criam ou alteram nomes locais por padrão.
2. Existem 4 possíveis scopes. São eles:
    * local
    * enclosing functions
    * global
    * built-in
3. Os nomes declarados em declarações globais e não locais mapeiam nomes atribuídos para preencher módulos e escopos de função.


A declaração em #2 acima pode ser definida pela regra LEGB.

** Regra LEGB. **

L: Local - Nomes atribuídos de qualquer forma dentro de uma função (def ou lambda)) e declarações não globais nessa função.

E: Enclosing function locals - Nome no escopo local de todas e quaisquer funções enclapsuladas (def ou lambda), de dentro para fora.

G: Global (módulo) - Nomes atribuídos no nível superior de um arquivo de módulo, ou declarados como *global* em uma def dentro do arquivo.

B: Built-in (Python) - Nomes pré-atribuídos no módulo: open, range, SyntaxError, ...

"""
# x é local aqui:
f = lambda x:x**2

name = 'This is a global name'

def greet():
    name = 'Sammy'

    def hello():
        print('Hello '+name)

    hello()

greet()
print(name)


#global

x = 50

def func():
    global x
    print('This function is now using the global x!')
    print('Because of global x is: ', x)
    x = 2
    print('Ran func(), changed global x to', x)

print('Before calling func(), x is: ', x)
func()
print('Value of x (outside of func()) is: ', x)
