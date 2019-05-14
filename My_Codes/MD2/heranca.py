#encoding: utf-8

class Animal(object):
  def __init__(self):
    print("Aninal Criado")
    
  def quemSouEu(self):
    print("Eu sou um animal!!!")
  
  def comer(self):
    print("Comendoo...")
    
    
animal1 = Animal()

animal1.comer()
animal1.quemSouEu


class Cachorro(Animal):
  def __init__(self):
    print("Cachorro criado!")
  
  def __Animal__(self):
    print("Animal cachorro criado")
    
  def latir(sefl):
    print('Latindo')
  
  def raca(self, raca):
    self.raca = raca
    print(self.raca)
    
sam = Cachorro()

sam.comer()
sam.latir()
sam.raca('Labrador')


