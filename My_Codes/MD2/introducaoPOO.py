#Crie um novo tipo de objet chamado Sample
class Sample(object):
  pass

#Instanciando Sample
x = Sample()
print(type(x))

#Atributos
# A sintaxe para criar um atributo é:
# self.attribute = something
# Existe um método especial chamado:
# init()
# Esse método é usado para inicializar os atributos de um objeto. Por exemplo:

class Dog(object):
  def __init__(self, raca):
    self.raca = raca
    
sam = Dog(raca = 'Lab')
thor = Dog(raca = 'Olimpo')

# Vamos descrever o que temos acima. O método especial
# init() é chamado automaticamente logo após o objeto ter sido criado:
# def init (self, raça): Cada atributo em uma definição de classe começa com uma referência ao objeto de
# instância. É convencionalmente chamado de self. A raça é o argumento. O valor é passado durante a
# instanciação da classe.
# self.breed = breed


print(sam.raca)
print(thor.raca)


# Em Python também existem atributos de objeto de classe. Esses atributos de objeto de classe são os
# mesmos para qualquer instância da classe. Por exemplo, podemos criar o atributo especie para a classe
# Dog. Os cães (independentemente da sua raça, nome ou outros atributos serão sempre mamíferos.
# Aplicamos essa lógica da seguinte maneira:

class Dog2(object):
  #Atributos de objetos de classe
  species =  'Mamíferos'
  
  def __init__(self,raca,nome):
    self.raca = raca
    self.nome = nome
    
jean = Dog2('Lab','Odin')
print(jean.nome, jean.raca, jean.species)


# Métodos
# Métodos são funções definidos dentro do corpo de uma classe. Eles são usados para executar operações
# com os atributos de nossos objetos. Os métodos são essenciais no conceito de encapsulamento em OOP.
# Isso é essencial para dividir as responsabilidades na programação, especialmente em grandes aplicações.
# Você pode basicamente pensar em métodos como funções que atuam em um Objeto que levam o próprio
# Objeto através de seu argumento self .
# Vamos passar por um exemplo de criação de uma classe Circle:

class Circle(object):
  pi = 3.14
  
  #Ocirculo é instanciado com um raio (o padrão é 1)
  def __init__(self, radius = 1):
    self.radius = radius
  
  #metodo de cálculo da área. Observe o uso de si mesmo:
  def area(self):
    return self.radius * self.radius * Circle.pi  
  
  #Método que redefie a área
  def setRadius(self, radius):
    self.radius = radius
    
  #Método para obter raio (Mesmo que apenas chamar radius)
  def getRadius(self):
    return self.radius
  
c = Circle()

c.setRadius(2)
print(c.getRadius())
print(c.area())


# Herança
# A herança é uma forma de formar novas classes usando classes que já foram definidas. As classes recém
# formadas são chamadas classes derivadas, as classes de que derivamos são chamadas de classes base.
# Os benefícios importantes da herança são a reutilização de códigos e a redução da complexidade de um
# programa. As classes derivadas (descendentes) substituem ou estendem a funcionalidade das classes base
# (ancestrais).
# Vejamos um exemplo incorporando nosso trabalho anterior na classe Dog:

class Animal(object):
  def __init__(self):
    print('Animal created')
  
  def whoAmI(self):
    print("Animal")
    
  def eat(self):
    print("Eating...")
  
class Dog3(Animal):
  def __init__(self):
    Animal.__init__(self)
    print("Dog Created")
    
    def whoAmI(self):
      print('dog')
      
    def barc(self):
      print('woof!')
      
d = Dog3()
print(d.whoAmI())

print(d.eat())

      

# Métodos especiais
# Finalmente, vamos dar uma olhada em métodos especiais. Classes em Python podem implementar
# determinadas operações com nomes de métodos especiais. Esses métodos não são realmente chamados
# diretamente, mas pela sintaxe de linguagem específica de Python. Por exemplo, crie uma classe de livro:

class Book(object):
  def __init__(self, title, author, pages):
    print("A book is created")
    self.title = title
    self.author = author
    self.pages = pages
  
  def __str__(self):
    return "Title:%s , author:%s, pages:%s " %(self.title, self.author, self.pages)
  
  def __len__(self):
    return self.pages

  def __del__(self):
    print("A book is destroyed")



book = Book("Python Rocks!", "Rodrigo Tadewald", 159)
# Métodos especiais
print(book)
print(len(book))
del book

# Os métodos init (), str (), len () e del (). Esses métodos especiais são definidos pelo uso de sublinhados.
# Eles nos permitem usar funções específicas do Python em objetos criados através da nossa classe.





