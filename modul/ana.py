from modul1 import toplama
from modul2 import carpma
import sys

yardim = """
toplama icin 
   python3 ana.py toplama 3 5

carpma icin 
   python3 ana.py carpma 3 5

"""
if __name__ == "__main__":
    argc = len(sys.argv)
    if argc  != 4:
        print("Parametre sayisi yanlis.")
        print(yardim)
    else:
        sayi1 = float(sys.argv[2])
        sayi2 = float(sys.argv[3])
        islem = sys.argv[1]
        if islem == "toplama":
            print(toplama(sayi1, sayi2))
        elif islem == "carpma":
            print(carpma(sayi1, sayi2))
        else:
            print("Hatali islem secilmis : %s" % islem)
            print(yardim)
