## BARKOD HAZIRLAMA YÖNTEMLERİ

### Varlık Barkodları:

Varlık Yönetimi -\> Varlıklar -\> Ekle / Değiştir / Kopyala -\> Genel Bilgiler

Varlıklar için barkod tanımlamasında varlık detay sayfası içerisinde yer alan “Barkod Kodu” alanı kullanılmaktadır.

![Resim1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5eb40c2b-921b-4a03-b438-33ab6e9f0c84)

### Varlık Barkod Kodu alan özellikleri:

Barkod Kodu alanı “String” türünde bir alan olup varsayılan olarak “20” karakter girişine izin vermektedir.

String alan olması nedeniyle “harf,rakam,sembol” içeriklerine sahip olabilmektedir.

![Resim2](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4d94d1c9-61be-4016-8e69-fe79ac59b0e0)

“Karakter sınırı kullanıcılarımızın ihtiyaç ve talepleri doğrultusunda artırılabilinmektedir.”

## Barkod Kodlarının Varlıklarla eşleştirilmesi

Beam uygulaması içerisinde tanımlı olan varlıkları için barkod bilgisi eklemek isteyen müşterilerimiz; hazırladıkları bir barkod düzeni var ise, Varlık kodu & Barkod Kodu eşleştirmelerini içeren bir excel hazırlayıp bimser destek sistemi üzerinden ileterek bu eşleştirmeleri sisteme uygulatabilirler.

Beam uygulamasına ilk kez eklenecek varlıklar için barkod kodu bilgisi eklemek isteyen kullanıcılarımız ise kendilerine iletilmiş olan “Varlık Şablonu” excel’i içerisine “Barkod” isminde bir sütun ekleyerek hazırlayabilirler.

## Barkod Kodu Hazırlama

Kullanıcılarımızın varlıkları üzerinde mevcut bir barkod sistemi bulunmuyor ve ilk kez oluşturulmak isteniyor ise barkod kodu hazırlamak için şu yöntemler izlenebilir:

1.  Varlık kodlarını aynı zamanda barkod kodu olarak tanımlamak:

    Varlık kodlaması için oluşturulmuş mevcut bir kodlama hiyerarşisini aynı zamanda barkod kodu için de uygulanabilir.

2.  Seri Numarasını aynı zamanda barkod kodu olarak tanımlamak:

    Varlıkların kendilerine ait seri numaraları varsa ve bunlar kullanıcımızın elinde bulunuyor ise bu seri numaraları barkod kodu olarak kullanılabilir.

3.  Varlığa detaylarına ait kısaltmalar içeren yeni bir kod sistemi oluşturmak:

    A blok daire 1 de bulunan 1200 devirlik bir kurutma kurutma makinası için örnek vermek gerekirse “Krt-Mak-1200dvr-Ablok-D1”

### Barkod kodlarından Etiket Oluşturmak

Beam uygulaması içerisine varlıklar ve barkod kodları eşleştirilmiş bir şeklide eklendikten sonra bu barkod kodlarına ait varlıklara yapıştırılacak etiketler oluşturmak için:

Varlık Yönetimi -\> Raporlar -\> 01 Varlık Barkod Listesi

Raporunu kullanarak, varlıkların “IR Barcod” veya “QR barcod” raporlarını hazırlayabilirler:

Varsayılan Barkod Raporu: “Barkod Tipi: Code-128”

![Resim3](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload06f30dd8-7c9a-48a7-8b14-3d21b0d02dfe)


Varsayılan Barkod Raporu: “Barkod Tipi: QRcode”

![Resim4](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb71ea5b2-4e61-4073-8fb5-ccc98e1af669)


Örneklerde görmüş olduğunuz etiket tasarımları müşteri talebi doğrultusunda düzenlenebilmektedir.

Müşterimiz talep ettiği etiket tasarımına ait ölçü ve içerik detaylarını içeren bir şablon hazırlayıp bimser destek sistemi üzerinden bildirebilir.

Beam uygulaması içerisinde barkod bilgileri tanımlanan varlıklar için “Varlık Barkod Listesi” raporu ile etiketleri içeren raporlar çekilir. Sonrasında kullanıcı bu raporları barkod yazıcıdan baskı alarak ilgili varlıklara etiketleyerek kullanıma hazır duruma getirir.

## 

## 

## Malzeme Barkodları:

Malzeme Yönetimi -\> Malzemeler -\> Ekle / Değiştir / Kopyala -\> Genel Bilgiler

Malzemeler için barkod tanımlamasında malzeme detay sayfası içerisinde yer alan “Barkod Kodu” alanı kullanılmaktadır.


![Resim5](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8ce34aad-640d-4cc5-be83-3f30f96592a8)


### Malzeme Barkod Kodu alan özellikleri:

Barkod Kodu alanı “String” türünde bir alan olup varsayılan olarak “100” karakter girişine izin vermektedir.

String alan olması nedeniyle “harf,rakam,sembol” içeriklerine sahip olabilmektedir.

![Resim6](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload19c0cdb4-f891-4afb-9e25-61c0385c543d)



“Karakter sınırı kullanıcılarımızın ihtiyaç ve talepleri doğrultusunda artırılabilinmektedir.”

## Barkod Kodlarının Malzemeler ile Eşleştirilmesi

Beam uygulaması içerisinde tanımlı olan malzemeler için barkod bilgisi eklemek isteyen müşterilerimiz; hazırladıkları bir barkod düzeni var ise, Malzeme kodu & Barkod Kodu eşleştirmelerini içeren bir excel hazırlayıp bimser destek sistemi üzerinden ileterek bu eşleştirmeleri sisteme uygulatabilirler.

Beam uygulamasına ilk kez eklenecek malzemeler için barkod kodu bilgisi eklemek isteyen kullanıcılarımız ise kendilerine iletilmiş olan “Malzeme Şablonu” excel’i içerisine “Barkod” isminde bir sütun ekleyerek hazırlayabilirler.

## Barkod Kodu Hazırlama

Kullanıcılarımızın varlıkları üzerinde mevcut bir barkod sistemi bulunmuyor ve ilk kez oluşturulmak isteniyor ise barkod kodu hazırlamak için şu yöntemler izlenebilir:

1.  Malzeme kodlarını aynı zamanda barkod kodu olarak tanımlamak:

    Malzeme kodlaması için oluşturulmuş mevcut bir kodlama hiyerarşisini aynı zamanda barkod kodu için de uygulanabilir.

2.  Seri Numarasını aynı zamanda barkod kodu olarak tanımlamak:

    Malzemelerin kendilerine ait seri numaraları varsa ve bunlar kullanıcımızın elinde bulunuyor ise bu seri numaraları barkod kodu olarak kullanılabilir.

3.  Malzeme detaylarına ait kısaltmalar içeren yeni bir kod sistemi oluşturmak:

    çalışma masası için örnek vermek gerekirse: Cal-Masa-MDF

## Barkod kodlarından Etiket Oluşturmak

Beam uygulaması içerisine varlıklar ve barkod kodları eşleştirilmiş bir şeklide eklendikten sonra bu barkod kodlarına ait malzemelere yapıştırılacak etiketler oluşturmak için:

Malzeme Yönetimi -\> Raporlar -\> 04 Barkod Listesi ve Yazdırma

Raporunu kullanarak, malzemelerin “IR Barcod” veya “QR barcod” raporlarını hazırlayabilirler:

Varsayılan Malzeme Barkod Raporu: “Barkod Tipi: Code93Extended”


![Resim7](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload845597a5-e668-4ea8-98cf-9183e8f74e87)


Varsayılan Malzeme Barkod Raporu: “Barkod Tipi: QRcode”


![Resim8](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5c2f84b3-8533-41e7-b688-8a9203d9c654)


Örneklerde görmüş olduğunuz etiket tasarımları müşteri talebi doğrultusunda düzenlenebilmektedir.

Müşterimiz talep ettiği etiket tasarımına ait ölçü ve içerik detaylarını içeren bir şablon hazırlayıp bimser destek sistemi üzerinden bildirebilir.

Beam uygulaması içerisinde barkod bilgileri tanımlanan malzemeler için “Barkod Listesi ve Yazdırma” raporu ile etiketleri içeren raporlar çekilir. Sonrasında kullanıcı bu raporları barkod yazıcıdan baskı alarak ilgili varlıklara etiketleyerek kullanıma hazır duruma getirir.


## BARKOD OKUYUCU KULLANIMI

## Barkod Okuyucu Özelliğinin Sağladığı Avantajlar

Barkod okuyucu fonksiyonu varlık seçimlerinde ve malzeme seçimlerinde ciddi faydalar sağlamaktadır.

Sağlayacağı başlıca faydalar;

-   Arıza tespit edilen varlığın kodunu sistemde manuel olarak aramak ile uğraşılmayacak.
-   Bakım personeli, yakınında olan bir varlık için açılmış talepleri veya emirleri kontrol edebilecek.
-   Bakım personeli, iş emrinde kullanmakta olduğu malzemeleri hızlıca sisteme ekleyebilecek.
-   Varlık taşıma işlemi yapıldığında taşınan varlık kolayca seçilecek.
-   Varlık taşıma sonrası, varlığın bağlandığı sahip varlık varsa kolayca seçim yapılabilinecek.
-   Malzeme hareketi oluşturulurken, ilgili malzemeler hızlıca seçilebilinecek.

Bu işlemlerin barkod okuyucu ile yapılması saha ortamlarında personellerin işlerini ciddi anlamda hızlandıracak ve kolaylaştıracaktır.

Barkod okuyucu fonksiyonunun kullanıldığı bütün alanların listesi [sonraki sayfada](#_QR_Kod_&) detaylı şekilde listelenmiştir.

## QR Kod & Barkod Okuyucu Kullanıldığı Yerler

Uygulama içerisinde varlık ve malzeme seçimi gerektiren her türlü alanda barkod okuma fonksiyon kullanılmaktadır.

Bu yerler şunlardır;

1.  VARLIKLAR -\> VARLIK EKLE -\> BAĞLI OLDUĞU VARLIK
2.  VARLIKLAR -\> FİLTRELE -\> VARLIK SEÇİMİ
3.  VARLIK SAYIMI -\> FİLTRELE -\> VARLIK SEÇİMİ
4.  VARLIK SAYIMI -\> EKLE -\> VARLIK SEÇİMİ
5.  VARLIK TAŞIMA -\> EKLE -\> VARLIK SEÇİMİ
6.  VARLIK TAŞIMA -\> EKLE -\> YENİ SAHİP VARLIK
7.  VARLIK TAŞIMA -\> FİLTRELE -\> VARLIK SEÇİMİ
8.  VARLIK TARİHÇESİ -\> -\>
9.  İŞ TALEPLERİ -\> EKLE -\> VARLIK SEÇİMİ
10. İŞ TALEPLERİ -\> DÜZENLE -\> VARLIK SEÇİMİ
11. İŞ TALEPLERİ -\> FİLTRELE -\> VARLIK SEÇİMİ
12. İŞ EMİRLERİ -\> EKLE -\> VARLIK SEÇİMİ
13. İŞ EMİRLERİ -\> DÜZENLE -\> VARLIK SEÇİMİ
14. İŞ EMİRLERİ -\> FİLTRELE -\> VARLIK SEÇİMİ
15. İŞ EMİRLERİ -\> EKLE -\> KULLANILAN MALZEME SEÇİMİ
16. İŞ EMİRLERİ -\> DÜZENLE -\> KULLANILAN MALZEME SEÇİMİ
17. MALZEME HAREKETİ -\> EKLE -\> MALZEME SEÇİMİ
18. MALZEME HAREKETİ -\> DEĞİŞTİR -\> MALZEME SEÇİMİ
19. MALZEME HAREKETİ -\> FİLTRELE -\> MALZEME SEÇİMİ
20. MALZEME SAYIMI -\> EKLE -\> MALZEME SEÇİMİ
21. MALZEME SAYIMI -\> DEĞİŞTİR -\>MALZEME SEÇİMİ
22. MALZEME SAYIMI -\> FİLTRELE -\> MALZEME SEÇİMİ


![Resim9](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc0b0cdb5-0fdf-45cf-a002-fcc6d0bc14e1)

## **Barkod Okuyucu Örneği ( Varlık Tarihçesi )**

Ana ekranda varlık tarihçesi tıklandığında barkod okuma ekranı açılacaktır.

![Resim10](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3397a971-7aee-46cb-9003-da2d3d35dbd3)

![Resim11](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3bc4d711-0cb8-43ed-aad1-7c1018c86607)


Açılan barkod okuma ekranına sisteme tanımlanmış bir varlığın barkodu okutulduğunda, o barkoda sahip varlığın bilgileri, ilgili varlık için açılmış iş emirleri ve iş talepleri sistem tarafından listelenmektedir.

![Resim12](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload294f04a5-444a-4b9b-9058-4d3bee0a2e80)

![Resim13](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb47ed328-bcd1-46c7-946b-c89a439bb696)

![Resim14](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload715e2798-480f-4260-bbe7-433a90b31e35)


