

class Insan:
    def __init__(self, adi, cinsiyeti, dogumyili):
        self.adi = adi
        self.cins = cinsiyeti
        self.dogumyili = dogumyili

class Calisan(Insan):
    def __init__(self, ad, cins, dy, maas):
        Insan.__init__(self, ad, cins, dy)
        self.maas = maas

    
