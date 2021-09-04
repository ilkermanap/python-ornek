# Sınıf Örnekleri

## Dondurmacı

Bir dondurma dükkanını tanımlamak için en az iki nesne gerekir. Dondurma ve dükkan.

### Dondurma Nesnesi

Dondurma denince aklımıza türü gelir. Dondurma nesnemizi türü, toplam top sayısı, bir top maliyeti, bir top fiyatı  bilgilerini vererek oluştururuz.

Dondurma satışı için satis fonksiyonu var. Bu fonksiyona parametre olarak satılmak istenen top sayısı verilir. Satılmak istenen top sayısı eldeki miktardan az ise satış gerçekleşir ve satılan top sayısı o dondurma türünün toplam miktarından düşülür ve True değeri döndürülür.  Eğer satılmak istenen top sayısı eldeki miktardan az ise, satış gerçekleşmez, miktar aynı kalır ve False değeri döndürülür.


### Dükkan Nesnesi

Dükkan için önemli olan depo durumu ve satışlardır. Bu bilgileri saklayabilecek iki değişken kullandık, liste ve satılan.  

liste değişkeni dict tipindedir. Anahtar olarak dondurma türünü kullanır. O tür adı için Dondurma sınıfından türetilmiş bir değişken saklar.

satilan değişkeni, list tipindedir. Yapılan her başarılı satış için bu listeye satılan dondurma türü ve satılan top miktarı eklenir.

Envantere dondurma eklemek için ekle fonksiyonu kullanılır. Dondurma türü, toplam top sayısı, bir top fiyatı ve bir top maliyeti bilgileri verilir. Bu bilgiler kullanılarak Dondurma nesnesi oluşturulur ve dükkanın liste değişkenine eklenir.

Dükkandan satış için satis fonksiyonu yazılmıştır. Dondurma türü ve satılacak top sayısı verilir. Bu fonksiyon bize iki değer döndürür. Birincisi istenen dondurma türünün dükkanda olup olmadığı, ikincisi ise istenen dondurmadan elde yeterince olup olmadığıdır.

## Uygulama

Ana uygulamada önce boş bir dükkan tanımlayarak başlarız: 

    dukkan = Dukkan()

Dükkanımıza dondurmaları ekleriz:

    dukkan.ekle("Limon", topsayisi=200, fiyat=5, maliyet=2)

Bu satırla, dükkana bir topu 5 liraya satılacak olan 200 top limonlu dondurma ekledik. 

Yeni bir tür daha ekleyelim:

    dukkan.ekle("Karadut", topsayisi=10, fiyat=7, maliyet=4)

Böylece dükkana 200 top limonlu, 10 top karadutlu dondurma ekledik.

Envanteri görmek için dükkanın rapor fonksiyonunu çağırırız. 

    -------  Envanter  -------------
    Limon	200
    Karadut	10


Dondurma satışı için dükkanın satis foksiyonunu kullanırız.

    dukkan.satis("Limon", 5)
    dukkan.satis("Karadut",4)
    dukkan.satis("Karadut",3)
    dukkan.satis("Limon", 12)
    dukkan.satis("Limon", 15)
    dukkan.satis("Karadut",4)

Son satış hariç bütün satışlar başarılı olur.

    BASARILI    Limon 5 top satildi, 195 top kaldi
    BASARILI    Karadut 4 top satildi, 6 top kaldi
    BASARILI    Karadut 3 top satildi, 3 top kaldi
    BASARILI    Limon 12 top satildi, 183 top kaldi
    BASARILI    Limon 15 top satildi, 168 top kaldi
    SATAMADIK   Karadut 4 top istendi, elde 3 kadar var

Bir daha envanter durumu alırsak:

    dukkan.rapor()

    -------  Envanter  -------------
    Limon	168
    Karadut	3


Dükkanın satış ve parasal durumu için:

    ------- Satis Raporu --------------
    Limon 5  ciro :  25   maliyet :  10    kar :  15
    Karadut 4  ciro :  28   maliyet :  16    kar :  12
    Karadut 3  ciro :  21   maliyet :  12    kar :  9
    Limon 12  ciro :  60   maliyet :  24    kar :  36
    Limon 15  ciro :  75   maliyet :  30    kar :  45
    --------------------------------------------------
    Toplam ciro : 209     Toplam maliyet : 92   Toplam Kar : 117
 