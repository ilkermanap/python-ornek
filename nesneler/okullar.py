from okul import Okul
from sinif import Sinif
from ogrenci import Ogrenci


class Okullar:
    def __init__(self,ilcesi):
        self.ilce = ilcesi
        self.okullar = {}

    def okul_ekle(self, okul):
        print okul.adi
        if okul.adi not in self.okullar.keys():
            self.okullar[okul.adi] = okul
        print self.okullar

    def sinif_ekle(self, okuladi, sinif):
        self.okul_ekle(Okul(okuladi))
        self.okullar[okuladi].sinif_ekle(sinif)

    def ogrenci_ekle(self, okuladi, sinifadi, ogrenci):
        self.sinif_ekle(okuladi, Sinif(sinifadi))
        self.okullar[okuladi].siniflar[sinifadi].ogrenci_ekle(ogrenci)
            
    def rapor(self, okuladi=None):
        print "*" * 50
        print "  %s Ilcesi Okullar Raporu" % self.ilce
        if okuladi is None:
            for okulu in self.okullar.values():
                okulu.rapor()

        else:
            if okuladi in self.okullar.keys():
                self.okullar[okuladi].rapor()
            else:
                print "Hatali okul adi, ekli okullar asagida:"
                for k in self.okullar.keys():
                    print k
