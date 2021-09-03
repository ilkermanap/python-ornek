
class Soru:
    def __init__(self, soru_metni, cevap, max_deneme=3):
        self.metin = soru_metni
        self.cevap = cevap.lower()
        self.max_deneme = max_deneme
        self.yanlis = 0

    def sor(self):
        for i in range(self.max_deneme):
            cevap = input(self.metin +  " :")
            if cevap.lower() == self.cevap:
                return True
            print("Yanlis cevap, %d hakkin kaldi" % (self.max_deneme - i -1))
            self.yanlis = i+1
        return False

    def rapor(self):
        durum = "bildiniz"
        if self.yanlis == self.max_deneme:
            durum = "bilemediniz"
        print(self.metin, " sorusunu %d denemede %s." % (self.yanlis, durum))

class Sinav:
    def __init__(self, baslik):
        self.baslik = baslik
        self.sorular = {}

    def soru_ekle(self, metin, cevap):
        son_soru = len(self.sorular.keys())
        self.sorular[son_soru +1 ] = Soru(metin, cevap)

    def sinav(self):
        print(self.baslik, " sinavi basladi")
        for i in sorted(self.sorular.keys()):
            self.sorular[i].sor()

        for i in sorted(self.sorular.keys()):
            self.sorular[i].rapor()

        
                  
if __name__ == "__main__":
    sinav = Sinav("Baskentler")
    sinav.soru_ekle("Turkiye","Ankara")
    sinav.soru_ekle("Bulgaristan","Sofya")
    sinav.soru_ekle("Yunanistan","Atina")

    sinav.sinav()
