
class Nokta:
    def __init__(self, x,y):
        self.x = x
        self.y = y

class Daire(Nokta):
    def __init__(self, x,y, yaricap):
        Nokta.__init__(self, x,y)
        self.yaricap = yaricap
