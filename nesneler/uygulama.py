from okul import Okul
from sinif import Sinif
from ogrenci import Ogrenci
from okullar import Okullar

if __name__ == "__main__":
    import sys, os
    yenimahalle = Okullar("Yenimahalle")
    fname = sys.argv[1]
    if os.path.isfile(fname):
        for satir in open(fname, "r"):
            if satir.strip().startswith("#"):
                pass
            else:
                sira, ogrno, adi, sinifadi,okulu  = satir.strip().split(",")
                ogr = Ogrenci(adi, ogrno)
                yenimahalle.ogrenci_ekle(okulu, sinifadi, ogr)

        yenimahalle.rapor()
            
            # 1,1211,ilker manap,1E,Mevlana Ilkokulu
