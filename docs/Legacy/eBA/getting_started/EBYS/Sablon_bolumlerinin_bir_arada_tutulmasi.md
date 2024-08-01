# EBYS Şablon Bölümlerinin Bir Arada Tutulması

## GİRİŞ

Şablon alanlarının sayfa üzerinde bir sonraki alan ile birlikte hareket etmesi parametreye bağlanmıştır. 
ResmiYazisma projesindeki EBYPRM.VWPRP formuna “KPWTHNXT” isimli “Sonrakiyle Bir Arada Tutulması İstenen Şablon Bölümleri” başlıklı bir metin alanı eklenmelidir.

Bu alanda yazılan değerler DM'de bulunan (/system/ebys/eyazisma/templates/...) üst yazı dokümanında yer alan değerler ile aynı olmalıdır. 

Parametre aktif edildikten sonra yazı oluştururken yazdığımız parametre değerlerine ait bölümler sayfaya sığmadığı durumda aynı anda bir sonraki sayfaya kayacaktır.


## Parametrelerin Eklenmesi

Workflow Studio açılır ve ResmiYazisma projesinin EBYPRM.VWPRP formuna aşağıdaki metin alanı eklenir ve proje derlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/eybs_sonrakiyle_bir_arada_tut-34c2e652-85bc-4932-9765-55b0bdade0c3.png)


## Parametrelerin aktif edilmesi

eBA Web üzerinden EBYS/Üst Yazı Görünüm Tanımları menüsüne gidilir ve bir sonraki şablon bölümü ile bir arada tutulması istenen alanlar 
virgül ile ayrılarak eklenmelidir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/ebys_sonrakiyle_bir_arada_tut_tanim-768f8873-063e-4dca-85b7-061af44a01bf.png)


