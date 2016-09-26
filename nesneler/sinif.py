class Sinif:
    def __init__(self, sinifadi):
        self.adi = sinifadi
        self.ogrenciler = {}

    def ogrenci_ekle(self, ogrenci):
        if ogrenci.numara not in self.ogrenciler.keys():
            self.ogrenciler[ogrenci.numara] = ogrenci
            
    def rapor(self):
        print "-" * 50
        print "%s Sinifi Ogrenci Listesi " % self.adi
        for ogrno, ogr in sorted(self.ogrenciler.items()):
            print "%7s %s" % (ogrno, ogr.adi)

            
