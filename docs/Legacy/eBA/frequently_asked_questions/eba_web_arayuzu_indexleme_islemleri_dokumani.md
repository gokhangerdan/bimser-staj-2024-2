# eBA Doküman Yönetiminde Dokümanlar Nasıl Atif Edilir?

### 1. Doküman Yönetiminde İndekslemenin Aktif Hale Getirilmesi

eBA web ara yüzünde Doküman Yönetimi modülü içerisinde barındırılan dokümanların,
doküman içeriklerinde arama yapılabilmesi işleminin gerçekleştirilebilmesi için kütüphane
seviyesinde veya klasör seviyesinde indeksleme seçeneği aktif hale getirilir.
Seçilen dizinde indeks işlemini başlatılabilmesi için eBA web ara yüzüne giriş yapılıp,
Doküman Yönetimi içerisinde işlemin çalıştırılacağı dizin (kütüphane veya klasör) seçilir.


![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc36b2489-d4c0-45ed-ac46-ba8da292180a)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7d4d2904-20d4-4ecf-8f73-e8ffea0a5379)

Dizin seçildiğinde araç çubuğunda, seçilen dizinle ilgili yapılabilecek işlemlere ait butonlar
görünür hale gelir. Araç çubuğundaki “Özellikler” butonuna (Şekil 3, 2 numaralı alan) tıklanılarak,
seçilmiş dizinin özelliklerine erişim sağlanır. Şekil 3’te görüleceği üzere açılan Özellikler panelinde,
Yönetim (3 numara ile işaretlenmiş alan) alanı içerisindeki İndeksleme seçeneği Evet seçilip, paneldeki
Kaydet butonuna tıklanılarak seçili kütüphanede indeksleme işlevi aktif hale getirilir.
Not: İndeksleme işlemi kütüphane seviyesinde aktif hale getirilirse, kütüphane içindeki bütün
klasörlerde de indeksleme aktif hale gelecektir. Eğer bütün kütüphane içeriğinin indekslenmesi
istenmiyorsa, belirli bir klasörde bu işlem uygulanmalıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload460918c8-563d-4367-a34c-40590fea254f)

Ayarların kaydedilmesi sonrasında indeksleme işleminin aktif hale getirildiği dizin seçilerek, araç
çubuğundaki “Index Yenileme” butonuna (Şekil 4) tıklanılır. Butona tıklanıldığında dizin içerisindeki
dokümanların indekslenme işleminin başladığına dair uyarı mesajı gösterilmektedir (Şekil 5) ve dizin
içeriğindeki dosyalar indeksleme işleminin yapılması için sıraya alınır.
Not: Index Yenileme butonuna İndeksleme özelliği açılmış ana dizinde, sadece bir kere yapılması
yeterlidir. Dizin içerisine yeni klasör veya dosya konulduğunda indeks yenileme işlemini açık olan üst
dizinden almaktadır.


![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0aa4652a-48ec-4f2d-9948-5cf48567745f)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3e964fca-1c8e-4042-b0c2-1ec69c4b11ce)

Indeksleme için bekleyen dosyalarda, dosya görüntülenirken İçerikler panelindeki İndeks
durumu kolonunda “Yeniden indekslenmek için bekliyor” şeklinde gösterim yapılmaktadır.


![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload36735a42-bc9a-4b2a-bc2f-e7cb3cb0d418)

Dosya içeriği sistem tarafından indekslendiğinde, kolonda gösterilen bilgi “İndekslenmiş” olarak
görünecektir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5bd47f2a-4479-4c67-ade2-20ba2fdb42f6)

### 2. Doküman Yönetiminde İndekslemesi Aktif Bir Dizinde Arama Yapılması

Doküman Yönetimi bölümünde dosya içeriğinde arama yapabilmek için, Doküman Yönetimindeki bir
dizinde indeksleme işlemi başlatılmış ve dizindeki dosya içerikleri indekslenmiş olmalıdır. Sistem
üzerinde İndeks durumu “İndekslenmiş” olan dosyaların içeriklerinde arama yapılabilmektedir.
Arama işlemini gerçekleştirme için araç çubuğunda “İçerikte Ara” seçeneği işaretlenir ve Arama
alanına dosya içerisinde olabilecek bir kelime yazılıp (Şekil 8) arama işlemi başlatılır.


![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd89d4889-aa3a-4bc7-b86b-877591be7a04)

Aramada kullanılan bilgiyi içeren dosya veya dosyalar, sonuç ekranında Şekil 9’daki gibi
listelenecektir. Arama sonuçlarında dosyanın bulunduğu dizin, aranan kelimenin bulunduğu cümle ve
dosyayı oluşturan kişi gibi bilgiler gösterilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade702fa50-3999-44a1-961a-149784191f6c)

### 3. İndeksleme İşlemi Sonrası Lisans Kontrolü

Doküman Yönetiminde indeksleme işlemi için ayrıca OCR aktif hale getirildiyse, ABBYY klasörü
içerisindeki LicenseManager uygulaması çalıştırılarak, ay için kalan sayfa sayısı görüntülenebilmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd74ff82f-af6d-4d6c-9522-729ad79a02da)