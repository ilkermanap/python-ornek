
class Takim:
    def __init__(self, adi, max_yanlis=3):
        self.adi = adi
        self.puan = 0
        self.sayi = None
        self.yanlis_tahmin = 0
        self.sira = False
        self.max_yanlis = max_yanlis
        
    def tahmin(self, takim, sayi):
        #Karsi takimin sayisi tahmin ediliyor
        if takim.sayi == sayi:
            self.puan += 10
        
        else:
            self.yanlis_tahmin += 1
            if self.yanlis_tahmin == self.max_yanlis:
                self.sira = False

    def rapor(self):
        print("%s\t%d\t%d" % (self.adi,self.puan, self.yanlis_tahmin))

class Oyun:
    def __init__(self, adi):
        self.adi = adi
        self.takimlar = {}

    def takim_ekle(self, takim):
        self.takimlar[takim.adi] = takim

    def rapor(self):
        print("Adi\tPuan\tYanlis Tahmin\n-------------------------------------------")
        for adi, takim in self.takimlar.items():
            takim.rapor()

    def oyna(self):
        #to be implemented
        pass
    
if __name__ == "__main__":
    oyun = Oyun("Bizim Oyun")
    oyun.takim_ekle(Takim("Kirmizi", 123))
    oyun.takim_ekle(Takim("Mavi", 351))
    oyun.rapor()
                    
