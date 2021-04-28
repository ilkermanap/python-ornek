Modüller
========

__name__ Değişkeni
------------------

Çoğu python uygulamasında, en altta aşağıdakine benzer bir blok görürsünüz:

    if __name__ == '__main__':
       ...

Bir python uygulamasını çalıştırdığınızda, adını vererek çağırdığınız uygulama için __name__ değişkeni __main__ değerini alır.

Eğer uygulamanız başka bir python dosyasını da import ediyorsa, örneğin modul.py olsun; modul.py icinde __name__ değişkeni 'modul' değerini alacaktır.

