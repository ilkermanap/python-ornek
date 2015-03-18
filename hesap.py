#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Yukaridaki iki satir, kod icinde turkce harfler kullandigimiz 
zaman problem cikmamasini saglar. 
"""

import sys

"""
sys modulunu, programa verilen parametreleri okuyabilmek icin kullanacagiz
"""


import toplama

"""
toplama modulu, ayni dizinde bulunan toplama.py dosyasindan kullanilacak
import toplama dedigimizde,  toplama.py icindeki fonksiyonlara 

  toplama.topla(3,5) 

gibi erisiriz..

eger  

from toplama import topla

dersek o zaman 
  topla(3,5) 
diyebiliriz.

"""

sayi1 = float(sys.argv[1])
sayi2 = float(sys.argv[2])

sonuc = toplama.topla(sayi1,sayi2)

print sonuc


from toplama import topla

sonuc2 = topla(sayi1, sayi2)
print sonuc2


"""
simdi, islem.py icinden nesne kullanacagiz.
"""

print "Asagisi islem.py icindeki Islem nesnesini kullanarak hesap yapacak"

from islem import Islem

h = Islem(sayi1, sayi2)

print "toplama %0.2f" % h.topla()
print "cikarma %0.2f" % h.cikar()
print "carpma  %0.2f" % h.carp()
print "bolme   %0.2f" % h.bol()
