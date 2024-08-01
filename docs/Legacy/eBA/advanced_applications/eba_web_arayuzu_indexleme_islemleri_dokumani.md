# eBA Web Ara Yüzü İndeksleme İşlemleri Dokümanı

## 1.Doküman Yönetiminde İndekslemenin Aktif Hale Getirilmesi

eBA web ara yüzünde Doküman Yönetimi modülü içerisinde barındırılan dokümanların, doküman içeriklerinde arama yapılabilmesi işleminin gerçekleştirilebilmesi için kütüphane seviyesinde veya klasör seviyesinde indeksleme seçeneği aktif hale getirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/1-142a0a6a-9cc2-4030-865f-98ffcace7db3.png)

Seçilen dizinde indeks işlemini başlatılabilmesi için eBA web ara yüzüne giriş yapılıp, Doküman Yönetimi içerisinde işlemin çalıştırılacağı dizin (kütüphane veya klasör) seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/2-e431154f-bbce-4a05-9564-e179d8ae01d7.png)

Dizin seçildiğinde araç çubuğunda, seçilen dizinle ilgili yapılabilecek işlemlere ait butonlar görünür hale gelir. Araç çubuğundaki “Özellikler” butonuna (Şekil 3, 2 numaralı alan) tıklanılarak, seçilmiş dizinin özelliklerine erişim sağlanır. Şekil 3’te görüleceği üzere açılan Özellikler panelinde,
Yönetim (3 numara ile işaretlenmiş alan) alanı içerisindeki İndeksleme seçeneği Evet seçilip, paneldeki
Kaydet butonuna tıklanılarak seçili kütüphanede indeksleme işlevi aktif hale getirilir.

Not: İndeksleme işlemi kütüphane seviyesinde aktif hale getirilirse, kütüphane içindeki bütün klasörlerde de indeksleme aktif hale gelecektir. Eğer bütün kütüphane içeriğinin indekslenmesi istenmiyorsa, belirli bir klasörde bu işlem uygulanmalıdır.


![](https://docsbimser.blob.core.windows.net/imagecontainer/3-34c521ae-3c40-487c-b843-2f0103a28681.png)

Ayarların kaydedilmesi sonrasında indeksleme işleminin aktif hale getirildiği dizin seçilerek, araç çubuğundaki “Index Yenileme” butonuna (Şekil 4) tıklanılır. Butona tıklanıldığında dizin içerisindeki dokümanların indekslenme işleminin başladığına dair uyarı mesajı gösterilmektedir (Şekil 5) ve dizin
içeriğindeki dosyalar indeksleme işleminin yapılması için sıraya alınır.

Not: Index Yenileme butonuna İndeksleme özelliği açılmış ana dizinde, sadece bir kere yapılması
yeterlidir. Dizin içerisine yeni klasör veya dosya konulduğunda indeks yenileme işlemini açık olan üst dizinden almaktadır.


![](https://docsbimser.blob.core.windows.net/imagecontainer/4-a9210669-b5ae-4b32-ab33-74728be8cbe9.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/5-3519d915-094d-4c44-ac6b-a18335f84bce.png)

İndeksleme için bekleyen dosyalarda, dosya görüntülenirken İçerikler panelindeki İndeks durumu kolonunda “Yeniden indekslenmek için bekliyor” şeklinde gösterim yapılmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/6-1bd9325a-8980-4772-a77a-db2dbab8cfa6.png)

Dosya içeriği sistem tarafından indekslendiğinde, kolonda gösterilen bilgi “İndekslenmiş” olarak
görünecektir.


![](https://docsbimser.blob.core.windows.net/imagecontainer/7-3990c50d-5a0c-421f-a7a4-64de0c1927f0.png)

## 2.	Doküman Yönetiminde İndekslemesi Aktif Bir Dizinde Arama Yapılması

Doküman Yönetimi bölümünde dosya içeriğinde arama yapabilmek için, Doküman Yönetimindeki bir
dizinde indeksleme işlemi başlatılmış ve dizindeki dosya içerikleri indekslenmiş olmalıdır. Sistem
üzerinde İndeks durumu “İndekslenmiş” olan dosyaların içeriklerinde arama yapılabilmektedir.

Arama işlemini gerçekleştirme için araç çubuğunda “İçerikte Ara” seçeneği işaretlenir ve Arama
alanına dosya içerisinde olabilecek bir kelime yazılıp (Şekil 8) arama işlemi başlatılır.


![](https://docsbimser.blob.core.windows.net/imagecontainer/8-4b1e5c06-8dc8-498f-95ae-53bc4f751b0d.png)

Aramada kullanılan bilgiyi içeren dosya veya dosyalar, sonuç ekranında Şekil 9’daki gibi listelenecektir. Arama sonuçlarında dosyanın bulunduğu dizin, aranan kelimenin bulunduğu cümle ve dosyayı oluşturan kişi gibi bilgiler gösterilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/9-ce6e4260-3bb0-4748-bad8-df99faeaad00.png)

## 3.	İndeksleme İşlemi Sonrası Lisans Kontrolü

Doküman Yönetiminde indeksleme işlemi için ayrıca OCR aktif hale getirildiyse, ABBYY klasörü
içerisindeki LicenseManager uygulaması çalıştırılarak, ay için kalan sayfa sayısı görüntülenebilmektedir.


![](https://docsbimser.blob.core.windows.net/imagecontainer/10-c2ba1520-a847-4c12-8125-afc15013a1db.png)