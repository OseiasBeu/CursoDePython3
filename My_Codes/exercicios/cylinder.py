#encoding: utf-8
# Em um cilindro, consideramos as seguintes áreas:

# a) área lateral (AL)

# Podemos observar a área lateral de um cilindro fazendo a sua planificação;
# Assim, a área lateral do cilindro reto cuja altura é h e cujos raios dos círculos das bases são r é um retângulo de dimensões :
# Al = 2 * pi * r * h


# b) área da base (AB): área do círculo de raio r.
# Ab = pi*r²

# c) área total (AT): soma da área lateral com as áreas das bases.
# At = Al + 2*Ab = 2*pi*r*h + 2*pi*r² = 2*pi*r(h+r)



class Cylinder(object):
  def __init__(self,altura, raio):
    self.altura = altura
    self.raio = raio
    
  def AreaLateral(self):
    Al = 2 * 3.14 * self.raio * self.altura
    print('A área lateral desse cilindro é de:  %3.2f' %(Al))
    
  def AreaBase(self):
    Ab = 3.14 * (self.raio**2)
    print('A área base desse cilíndro é de: %3.2f' %(Ab))
    
  def AreaTotal(self):
    At = 2 * 3.14 * self.raio * self.altura + (2* 3.14 * (self.raio**2))
    print('A área total do cilíndro é de: %3.2f' %(At))
  
  def Volume(self):
    Vol = 3.14 * (self.raio**2) * self.altura
    print('O volume do cilíndro é: %3.2f' %(Vol))
    
cil = Cylinder(10,3)    
cil.AreaBase()
cil.AreaLateral()
cil.AreaTotal()
cil.Volume()
