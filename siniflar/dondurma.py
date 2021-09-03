

class Dondurma:
    def __init__(self, tur, topsayisi = 100):
        self.tur = tur
        self.miktar = topsayisi # 100 top 

    def satis(self, topsayisi):
        if self.miktar > topsayisi:
            self.miktar -= topsayisi
            print("BASARILI    %s %d top satildi, %d top kaldi" % (self.tur, topsayisi, self.miktar))
            return True
        else:
            print("SATAMADIK   %s %d top istendi, elde %d kadar var" % (self.tur, topsayisi, self.miktar))
            return False

    def rapor(self):
        print("%s\t%d" % (self.tur, self.miktar))
        
class Dondurmalar:
    def __init__(self):
        self.liste = {}

    def ekle(self, turu, topsayisi=100):
        self.liste[turu] = Dondurma(turu, topsayisi=topsayisi)
        

    def rapor(self):
        print("Envanter")
        for dondurma in self.liste.values():
            dondurma.rapor()
            

    def satis(self, tur, topsayisi):
        # iki boolean doner, birincisi tur var mi, ikincisi yeterli top varmi
        if tur in self.liste:
            return True, self.liste[tur].satis(topsayisi)
        else:
            return (False, False)


if __name__ == "__main__":
    d = Dondurmalar()
    d.ekle("Limon", 200)
    d.ekle("Visne", 50)
    d.ekle("Karadut", 20)
    d.rapor()

    d.satis("Limon", 198)
    d.satis("Visne", 4)
    d.satis("Limon", 3)
    d.rapor()
