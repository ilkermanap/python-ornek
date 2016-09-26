from ogrenci import Ogrenci
from sinif import Sinif

class Okul:
    def __init__(self, okuladi):
        self.adi = okuladi
        self.siniflar = {}

    def sinif_ekle(self, sinif):
        if sinif.adi not in self.siniflar.keys():
            self.siniflar[sinif.adi] = sinif

    def ogrenci_ekle(self, sinif, ogrenci):
        self.sinif_ekle(sinif)
        self.siniflar[sinif.adi].ogrenci_ekle(ogrenci)

    def rapor(self, sinifadi=None):
        print "*" * 50
        print "  %s Okulu Siniflar Raporu" % self.adi
        if sinifadi is None:
            for sinif in self.siniflar.values():
                sinif.rapor()
            print "" 
            print ""
        else:
            if sinifadi in self.siniflar.keys():
                self.siniflar[sinifadi].rapor()
            else:
                print "Hatali sinif adi"
