

class Dondurma:
    def __init__(self, tur, topsayisi = 100, fiyat=5, maliyet=2):
        self.tur = tur
        self.miktar = topsayisi # 100 top 
        self.fiyat = fiyat
        self.maliyet = maliyet
        self.kar = fiyat - maliyet
        
    def satis(self, topsayisi):
        if self.miktar > topsayisi:
            self.miktar -= topsayisi
            print("BASARILI    %s %d top satildi, %d top kaldi" % (self.tur, topsayisi, self.miktar))
            return True
        else:
            print("SATAMADIK   %s %d top istendi, elde %d kadar var" % (self.tur, topsayisi, self.miktar))
            return False

    def rapor(self):
        print(f"{self.tur}\t{self.miktar}")
        
class Dukkan:
    def __init__(self):
        self.liste = {}
        self.satilan = []

    def ekle(self, turu, topsayisi=100, fiyat=5, maliyet=2):
        self.liste[turu] = Dondurma(turu, topsayisi=topsayisi, fiyat=fiyat, maliyet=maliyet)
        

    def satisrapor(self):
        print("------- Satis Raporu --------------")
        _ciro = 0
        _maliyet = 0
        _kar = 0
        for tur, top in self.satilan:
            t = self.liste[tur]
            _ciro += t.fiyat * top
            _maliyet += t.maliyet * top
            _kar += t.kar * top
            print(tur, top, " ciro : ", t.fiyat * top, "  maliyet : ", t.maliyet * top, "   kar : ", t.kar * top)

        print("-"*50)
        print(f"Toplam ciro : {_ciro}     Toplam maliyet : {_maliyet}   Toplam Kar : {_kar}")
            
    def rapor(self):
        print("-------  Envanter  -------------")
        for dondurma in self.liste.values():
            dondurma.rapor()
            

    def satis(self, tur, topsayisi):
        turdurum = tur in self.liste
        satisdurum = False
        if turdurum:
            satisdurum = self.liste[tur].satis(topsayisi)
            if satisdurum:
                self.satilan.append((tur, topsayisi))
        return turdurum, satisdurum


if __name__ == "__main__":
    d = Dukkan()
    d.ekle("Limon", topsayisi=200, fiyat=5, maliyet=2)
    d.ekle("Karadut", topsayisi=10, fiyat=7, maliyet=4)

    d.rapor()

    d.satis("Limon", 5)
    d.satis("Karadut",4)
    d.satis("Karadut",3)
    d.satis("Limon", 12)
    d.satis("Limon", 15)
    d.satis("Karadut",4)

    d.satisrapor()


    d.rapor()