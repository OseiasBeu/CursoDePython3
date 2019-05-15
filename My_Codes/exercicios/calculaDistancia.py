# Programação orientada a objetos - Tema de casa

# Problema 1
# Preencha os métodos da classe Line para aceitar coordenadas como um par de tuplas 
# e retornar a inclinação e a distância da linha.

# d = √((x2 - x1)2 + (y2 - y1)2
# (x1, y1) e (x2, y2) representam as coordenadas x e y dos dois pontos.

# Para calcular o coeficiente angular de uma reta utiliza-se a seguinte fórmula:
# m = tg α
# Sendo m um número real e α o ângulo de inclinação da reta.
# Para calcular o coeficiente angular de uma reta a partir de dois pontos devemos dividir a variação entre os eixos x e y:
# A(Xa, Ya); B(Xb, Yb)
# m = Yb - Ya/ Xb - Xa
# Atenção!
# Quando o ângulo é igual a 0º: m = tg 0 = 0
# Quando o ângulo α é agudo (menor que 90º): m = tg α > 0
# Quando o ângulo α é reto (90º): não é possível calcular o coeficiente angular, pois não existe a tangente de 90º
# Quando o ângulo α é obtuso (maior que 90º) : m = tg α < 0
# EX.:
# A (– 5, 4) ;B (3,2):
class Line(object):
  def __init__(self,coor1, coor2):
    self.coor1 = coor1
    self.coor2 = coor2
    print(coor1)
    print(coor2)
    print("Coordenadas capturadas!!!")

  def distace(self):
    x1,y1 = self.coor1 #Desempacotamento de Tuplas
    x2,y2 = self.coor2
    d = ((x2-x1)**2 + (y2-y1)**2)**0.5
    # d = (((self.coor1[1] - self.coor1[0])**2) + ((self.coor2[1] - self.coor2[0])**2))
    print('A distância dessa reta é de: %3.2f'%(d))
  
  
  def slope(self):
    x1,y1 = self.coor1 #Desempacotamento de Tuplas
    x2,y2 = self.coor2
    m = y2-y1 / x1-x2    
    # m = (self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[0])
    print('O coeficiênte angular possuí: %3.2fº'%(m))
  
li = Line((-2,3),(1,5))
li.distace()
li.slope()
