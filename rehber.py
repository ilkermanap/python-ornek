

class Kisi:
    def __init__(self,tcno, adi,soyadi,sehir, meslek, tel, adres):
        self.tcno = tcno
        self.adi = adi
        self.soyadi = soyadi
        self.sehir = sehir
        self.meslek = meslek
        self.tel = tel
        self.adres = adres


    def rapor(self):
        print("Adi    :", self.adi)
        print("Soyadi :", self.soyadi)
        print("TC No  :", self.tcno)
        print("Sehir  :", self.sehir)
        print("Meslek :", self.meslek)
        print("Telefon:", self.tel)
        print("Adres  :", self.adres)

    def csv(self, ayirac = ";"):
        a = ayirac
        b = self.adi + a
        b += self.soyadi + a
        b += self.tcno + a
        b += self.sehir + a
        b += self.meslek + a
        b += self.tel + a
        b += self.adres 
        return b

class Rehber:
    def __init__(self, adi):
        self.adi = adi
        self.kisiler = {}

    def ekle(self, kisi):
        self.kisiler[kisi.tcno] = kisi


    def rapor(self):
        print("-" * 50)
        print(self.adi, "  Rehberi")
        print("-" * 50)
        for tcno, kisi in self.kisiler.items():
            kisi.rapor()
            print("-" * 50)

    def csv(self):
        print("adi;soyadi;tcno;sehir;meslek;tel;adres")
        for tcno, kisi in self.kisiler.items():
            print(kisi.csv())



if __name__ == "__main__":
    r = Rehber("Ev Telefon")
    a = Kisi("1", "Nurullah", "Caliskan", "Mugla","Ogrenci","0000","Mugla/Milas")
    b = Kisi("2", "Abdullah", "Caliskan", "Mugla","Ogrenci","0100","Mugla/Milas")
    c = Kisi("3", "Ilker", "Manap", "Stokholm","Muhendis","00230","Stokholm/Alvsjo")
    r.ekle(a)
    r.ekle(b)
    r.ekle(c)
    r.csv()
    r.rapor()
