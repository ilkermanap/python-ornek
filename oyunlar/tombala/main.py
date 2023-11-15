from tombala import Kart
from random import choice


k = Kart()

sayilar = range(100)

for i in range(300):
    sayi = choice(sayilar)
    print(sayi)
    print(k.sayicek(sayi))

    
