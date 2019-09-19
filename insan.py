

class Insan:
    def __init__(self, adi, cinsiyeti, dogumyili):
        self.adi = adi
        self.cins = cinsiyeti
        self.dogumyili = dogumyili

    def rapor(self):
        print("adi        :", self.adi)
        print("dogum yili :", self.dogumyili)

class Calisan(Insan):
    def __init__(self, ad, cins, dy, maas):
        Insan.__init__(self, ad, cins, dy)
        self.maas = maas

    def rapor(self):
        Insan.rapor(self)
        print("maasi :", self.maas)


a = Insan("ilker","e",1972)

b = Calisan("ilker","e",1972, 100)

a.rapor()
b.rapor()


