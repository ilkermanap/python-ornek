import sys



class Kelime:
    def __init__(self, kelime):
        self.kelime = kelime
        self.bulunan = []

    def kontrol(self):
        for harf in self.kelime:
            if harf not in self.bulunan:
                return False
        return True
        
    def tahmin(self, harf):
        harf = harf[0]
        if harf not in self.bulunan:
            if harf in self.kelime:
                self.bulunan.append(harf)
                return True
            return False
        else:
            print("%s zaten soylenmis" % harf)
            return True

    def __str__(self):
        s = ""
        for harf in self.kelime:
            if harf in self.bulunan:
                s += harf
            else:
                s += "_"
        return s

class Oyuncu:
    def __init__(self, adi, max_hata):
        self.adi = adi
        self.hata = 0
        self.max_hata = max_hata
        
    def cevap(self, durumu):
        if durumu == False:
            self.hata += 1
        if self.hata == self.max_hata:
            return False
        return True
    
    def kalan(self):
        return self.max_hata - self.hata
    
class Oyun:
    def __init__(self, oyuncu, kelime):
        self.oyuncu = oyuncu
        self.kelime = kelime
        self.bitti = False

    def sor(self, harf):
        if self.oyuncu.cevap(self.kelime.tahmin(harf)) == False:
            print("Kaybettin")
            self.bitti = True
        else:
            print(self.oyuncu.kalan(), " hakkin kaldi")
        print(str(self.kelime))
        if self.kelime.kontrol() == True:
            print("Bildin")
            sys.exit()
            
if __name__ == "__main__":
    oyuncu = Oyuncu("ilker", 5)
    kelime = Kelime("Deneme")
    oyun = Oyun(oyuncu, kelime)
    while not oyun.bitti:
        harf = input("Harf gir ")
        oyun.sor(harf)
