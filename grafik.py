
class Nokta:
    def __init__(self, x,y):
        self.x = x
        self.y = y

class Daire(Nokta):
    def __init__(self, x,y, yaricap):
        Nokta.__init__(self, x,y)
        self.yaricap = yaricap


class Cizgi(Nokta):
    def __init__(self, x,y, x1,y1):
        Nokta.__init__(self, x,y)
        self.bitis = Nokta(x1,y1)



