

class Islem:
  def __init__(self, x,y ):
    self.x = x
    self.y = y

  def topla(self):
    return (self.x + self.y)
  
  def cikar(self):
    return (self.x - self.y)

  def carp(self):
    return (self.x * self.y)

  def bol(self):
    if self.y != 0:
      return (self.x / self.y)
    else:
      return None
