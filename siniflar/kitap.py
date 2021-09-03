
class Kitap:
    def __init__(self, isbn, yazar, adi, yayinevi):
        self.isbn = isbn
        self.yazar = yazar
        self.adi = adi
        self.yayinevi = yayinevi
        self.veri = {"isbn":isbn, "yazar":yazar, "adi":adi, "yayinevi":yayinevi}

    def __str__(self):
        return "%s\t%s\t%s\t%s" % (self.isbn, self.yazar, self. adi, self.yayinevi)
        
    def arama(self, anahtar, deger):
        if anahtar not in self.veri.keys():
            return False
        else:
            if self.veri[anahtar] == deger:
                return True
            return False
        return False
        
class Kitaplik:
    def __init__(self, adi):
        self.adi = adi
        self.kitaplar = {}

    def arama(self, anahtar, deger):
        sonuc = []
        for k in self.kitaplar.values():
            
            if k.arama(anahtar, deger):
                sonuc.append(k)
        return sonuc
        
    def ekle(self, k):
        if k.isbn not in self.kitaplar.keys():
            self.kitaplar[k.isbn] = k

if __name__ == "__main__":
    k = Kitaplik("Kutuphanem")
    k.ekle(Kitap("1234","Maksim Gorki", "Ekmegimi Kazanirken", "Is Bankasi"))
    k.ekle(Kitap("2345","Tolstoy", "Itiraflarim", "Antik"))
    k.ekle(Kitap("3456","Ahmet Izzet Pasa", "Feryadim", "Timas"))
    k.ekle(Kitap("3556","Maksim Gorki", "Benim Universitelerim", "Roman Yayinlari"))

    sonuc = k.arama("yazar", "Maksim Gorki")

    for kitap in sonuc:
        print(kitap)
