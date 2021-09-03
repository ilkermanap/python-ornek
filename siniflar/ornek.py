
"""
 skala dict, 
 { 
    0 : 0,         tecrube suresi : karsilik gelen maas artisi
    5 : 3000
    7 : 4000
    10: 6000
 }
  

"""
class Yetenek:
    def __init__(self, adi, skala = None):
        self.adi = adi
        self.skala = skala

    def katki(self, tecrube):
        ek = 0
        
        for i in sorted(self.skala.keys()):
            if tecrube >= i:
                ek = self.skala[i]
            else:
                return ek
        return ek

class Insan:
    def __init__(self, adi, soyadi, dogumyili):
        self.adi = adi
        self.soyadi = soyadi
        self.dogumyili = dogumyili

        
class Calisan(Insan):
    def __init__(self, adi, soyadi, dogumyili, taban_maas):
        Insan.__init__(self, adi, soyadi, dogumyili)
        self.yetenekler = {}
        self.taban_maas = taban_maas

    def yetenek_ekle(self, yetenek, tecrube):
        self.yetenekler[yetenek.adi] = (yetenek,tecrube)
            
    def maas(self):
        maas_ = self.taban_maas
        for yetenek, tecrube in self.yetenekler.values():
            maas_ += yetenek.katki(tecrube)
        return maas_

    
    def rapor(self, bordro=False):
        if bordro:
            s = "%s %s %f\n" % (self.adi, self.soyadi, self.taban_maas)
            for y,t in self.yetenekler.values():
                s += "  +  %s %f\n" % ( y.adi, y.katki(t))
            s += "   Toplam : %0.2f" % self.maas()
            return s
        else:
            print("%s %s" % (self.adi, self.soyadi))
            print("Taban maas %f" % self.taban_maas)
            for y,t in self.yetenekler.values():
                print("%s icin %d yil tecrube karsiligi %d katki" % (y.adi, t, y.katki(t)))
            print("-"*40)
            print("Toplam  %f" % self.maas()) 


class Isyeri:
    def __init__(self, adi):
        self.adi = adi
        self.calisanlar = []

    def calisan_ekle(self, calisan):
        self.calisanlar.append(calisan)


    def bordro(self):
        gider = 0
        print("%s isyeri bordrosu" % self.adi)
        for c in self.calisanlar:
            print(c.rapor(bordro=True))
            gider += c.maas()
        print("-"*40)
        print("Gider Toplami %f" % gider)
        
if __name__ == "__main__":


    isyeri = Isyeri("IMB")
    py = Yetenek("Python", {0:0, 3:1500, 5:2500, 10:4000})
    csharp = Yetenek("CSharp", {0:0, 3:1000, 5:1500, 10:3000})
    java = Yetenek("Java", {0:0, 3:500, 5:1500, 10:2000})
    c = Calisan("ilker", "manap", 1972, 3500)
    c.yetenek_ekle(py, 7)
    c.yetenek_ekle(csharp, 3)
    d = Calisan("Ahmet", "Mehmet", 1986, 2200)
    d.yetenek_ekle(py,1)
    d.yetenek_ekle(java, 6)

    isyeri.calisan_ekle(c)
    isyeri.calisan_ekle(d)

    isyeri.bordro()
    
