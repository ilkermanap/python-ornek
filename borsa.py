import requests
from bs4 import BeautifulSoup as bs
import os
import time

class Hisse:
    def __init__(self, adi):
        self.adi = adi
        self.fiyat = None
        self.alis = None
        self.satis = None
        self.enyuksek = None
        self.endusuk = None
        self.aort = None
        self.yuzde = None
        self.hacim_lot = None
        self.hacim_tl = None

    def guncelle(self, etiket, rakam):
        if etiket.find("fiyat_id") > -1:
            self.fiyat = rakam
        if etiket.find("alis_id") > -1:
            self.alis = rakam
        if etiket.find("satis_id") > -1:
            self.satis = rakam
        if etiket.find("yuksek_id") > -1:
            self.enyuksek = rakam
        if etiket.find("dusuk_id") > -1:
            self.dusuk = rakam
        if etiket.find("aort_id") > -1:
            self.aort = rakam
        if etiket.find("yuzde_id") > -1:
            self.yuzde = rakam
        if etiket.find("fiyat_id") > -1:
            self.fiyat = rakam

    def rapor(self, tarih):
        print "%s\t%s\t%02.2f\t%02.2f" % (tarih, self.adi, self.alis, self.satis)

class Sayfa:
    def __init__(self, icerik):
        self.icerik = icerik
        self.tarih = None
        self.soup = bs(self.icerik)
        self.li = self.soup.find_all("li")

        
        
class LokalSayfa(Sayfa):
    def __init__(self, fname):
        self.dosya = fname
        icerik = open(fname,"r").read()
        Sayfa.__init__(self, icerik)
        self.tarih = time.gmtime(os.stat(fname).st_ctime)

    def guncelle(self):
        icerik = open(self.dosya,"r").read()
        Sayfa.__init__(self, icerik)
        self.tarih = time.gmtime(os.stat(self.dosya).st_ctime)

class UzakSayfa(Sayfa):
    def __init__(self, url):
        self.url = url
        r = requests.get(url)
        icerik = r.text
        Sayfa.__init__(self, icerik)
        self.tarih = time.localtime()

    def guncelle(self):
        r = requests.get(self.url)
        icerik = r.text
        Sayfa.__init__(self, icerik)
        self.tarih = time.localtime()        

class Borsa:
    def __init__(self, adi, kaynak):
        self.adi = adi
        self.kaynak = kaynak
        self.veriler = {}
        
    def guncelle(self):
        self.kaynak.guncelle()
        if self.kaynak.tarih not in self.veriler.keys():
            hs = {}
            for listitem in self.kaynak.li:
                if ('class' in listitem.attrs.keys())  and  ('id' in listitem.attrs.keys()):
                    if listitem.attrs['class'][0] == 'cell048':
                        adi = listitem.attrs['id'].split("_")[-1]
                        etiket = listitem.attrs['id']
                        rakam = float(listitem.text.replace(",","."))
                        if adi not in hs.keys():
                            hs[adi] = Hisse(adi)
                        hs[adi].guncelle(etiket, rakam)
            self.veriler[self.kaynak.tarih] = hs


    def rapor(self, hisse=None):
        print "Tarih                     hisse  alis   satis"
        print "----------------------------------------------"
        for tr, v in self.veriler.items():
            tstr = time.strftime("%Y-%m-%d %H:%M:%S", tr)
            if hisse is None:
                for k, hs in sorted(v.items()):
                    hs.rapor(tstr)
            else:
                if hisse in v.keys():
                    v[hisse].rapor(tstr)
                else:
                    print hisse, " icin %s tarihinde veri  bulunamadi" % tstr
if __name__ == "__main__":
    s = LokalSayfa("bigpara.html")
    #u = UzakSayfa("http://www.bigpara.com/borsa/canli-borsa/")
    b = Borsa("IMKB",s)
    b.guncelle()
    b.rapor()
    b.rapor("ZOREN")
    b.rapor("ZOsdf")
