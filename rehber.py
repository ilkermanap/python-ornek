

class Insan:
    def __init__(self,tcno, adi,soyadi,sehir, meslek, tel, adres):
        self.tcno = tcno
        self.adi = adi
        self.soyadi = soyadi
        self.sehir = sehir
        self.meslek = meslek
        self.tel = tel
        self.adres = adres


    def rapor(self):
        print "-" * 30
        print "Adi    :", self.adi
        print "Soyadi :", self.soyadi
        print "TC No  :", self.tcno
        print "Sehir  :", self.sehir
        print "Meslek :", self.meslek
        print "Telefon:", self.tel
        print "Adres  :", self.adres

    def csv(self, ayirac = ";"):
        a = ayirac
        b = self.adi + a
        b = self.adi + a
        b = self.adi + a
        b = self.adi + a


class Rehber:
    def __init__(self, adi):
        self.adi = adi
        self.kisiler = {}

    def ekle(self, kisi):
        self.kisiler[kisi.tcno] = kisi

