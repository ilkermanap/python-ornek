from random import choice

class Kart:
    def __init__(self):
        dizi = range(1,100)
        self.sayilar = []
        self.cinkolar = {1:[], 2:[], 3:[]}
        for cinko in range(15):
            sayi = choice(dizi)
            if sayi not in self.sayilar:
                self.sayilar.append(sayi)
            else:
                found = False
                while not found:
                    sayi = choice(dizi)
                    if sayi not in self.sayilar:
                        self.sayilar.append(sayi)
                        found = True


        i = 0
        for sayi in self.sayilar:
            cinko = int((i / 5)) + 1
            self.cinkolar[cinko].append(sayi)
            i+=1

    def sayicek(self, cekilen):
        for k, cinko in self.cinkolar.items():
            if cekilen in cinko:
                self.cinkolar[k].remove(cekilen)

        print(self.cinkolar)
        if len(self.cinkolar[1]) == 0:
            if len(self.cinkolar[2]) == 0:
                if len(self.cinkolar[3]) == 0:
                    return "TOMBALA"
                else:
                    return "Ikinci cinko"
            else:
                return "Birinci Cinko"
        else:
            return "Devam"

