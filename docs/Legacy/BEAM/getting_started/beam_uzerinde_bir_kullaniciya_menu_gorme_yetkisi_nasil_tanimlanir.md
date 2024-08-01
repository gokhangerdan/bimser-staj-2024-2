# Beam Üzerinde Bir Kullanıcıya Menü Görme Yetkisi Nasıl  Tanımlanır?

•	BEAM sistemi üzerinde herhangi bir menü yetkisi verilebilmesi için izlenecek yol şu şekildedir: 
Ana menü -> Sistem -> Kullanıcı Grupları -> Kullanıcının yer aldığı kullanıcı grubu seçilir -> Değiştir butonu veya çift tıklama ile ilgili gruba girilir. -> Sol sekmelerde yer alan menü yetkileri alanına girilir -> Burada ilgili modüller sıralı halde gelir. Sıralı halde gelen modüllerin tamamını görmek istiyorsa modülün yanında yer alan onay kutucuğu (check-box) işaretlenir veya tamamının gözükmesi istenmiyorsa “+” butonuna basılıp spesifik olarak ilgili modüle ait alt menülerin görme yetkisi verilebilir.


![](https://docsbimser.blob.core.windows.net/imagecontainer/mupload-d9fbd0c0-81dc-49bc-803e-58c9c3dea16b.png)

Resim 1.1 – Varlık Yönetimi Açık Olmayan Test Kullanıcısı

![](https://docsbimser.blob.core.windows.net/imagecontainer/mupload-9818f400-50cd-4bd5-ab1e-3324be89eeac.png)

Resim 1.2 – Kullanıcı Grupları seçimi

![](https://docsbimser.blob.core.windows.net/imagecontainer/mupload-23a2651e-482c-49c7-ae09-3cd9938de798.png)

Resim 1.3 – Test kullanıcısının kullanıcı grubuna değiştir ile girilmesi

![](https://docsbimser.blob.core.windows.net/imagecontainer/mupload-5a55b033-d7bf-4993-8377-46423a419791.png)

Resim 1.4 – Sol sekmede yer alan Menü Yetkilerinin seçimi

![](https://docsbimser.blob.core.windows.net/imagecontainer/mupload-df7661e5-a9ce-492d-8711-c7db4b26a49e.png)

Resim 1.5 – Varlık Yönetimi modülünün tüm alt menülerinin verilmesi

![](https://docsbimser.blob.core.windows.net/imagecontainer/mupload-0cd54c6e-136b-4a09-80dd-c9ed13d22008.png)

Resim 1.5.1 – Varlık Yönetimi yanında yer alan “onay kutucuğu” işaretlendiğinde tüm alt menülerin aktifleşmesi

![](https://docsbimser.blob.core.windows.net/imagecontainer/mupload-8b58fbb6-0c21-41e8-8b3d-fd46c7529956.png)

Resim 1.6 – Varlık Yönetimi yanında yer alan “+” simgesine basılarak spesifik alt menülerin seçilme işlemi

![](https://docsbimser.blob.core.windows.net/imagecontainer/mupload-cbbec520-c0d4-4d2c-a9c1-0c7c6cafb297.png)

Resim 1.6.1 – Varlık Yönetimi yanında yer alan “+” simgesine basılıp spesifik istenilen menülerin aktifleştirilmesi işlemi

![](https://docsbimser.blob.core.windows.net/imagecontainer/mupload-ee420d40-574d-4fea-bdb3-41dff8626a90.png)

Resim 1.7 – İstenilen menü yetkileri tanımlandıktan sonra “kaydet” butonuna basılması

![](https://docsbimser.blob.core.windows.net/imagecontainer/mupload-c7a76471-b427-4764-83fb-1056be7987a7.png)

Resim 1.8 – Seçilen menü yetkilerine göre “test” kullanıcısının gördüğü modül ve alt menüleri

## Sistem Modülünde Kullanıcı Grupları Alt Menüsünü Göremiyorum Ne Yapmalıyım?

Sistem modülünde eğer kullanıcı grupları ilgili menü yetkisi vermek isteyen kullanıcı içerisinde gözükmüyorsa bu durum kullanıcı kartında yer alan “Yönetici mi?” onay kutucuğunun işaretli olmamasından kaynaklıdır.
Eğer ki ilgili kullanıcı sistemde “Yönetici” olarak tanımlanması gerekiyorsa, sistemde yönetici olarak tanımlı bir kullanıcıya durum bildirilir. Yönetici olan kullanıcınızın izleyeceği yol şu şekildedir:
Ana menü -> Sistem -> Kullanıcılar -> İlgili kullanıcı seçilir -> Değiştir veya çift tıklama ile girilir -> Genel Bilgiler sekmesinde yer alan “Yönetici mi?” kutucuğu işaretlenir -> “Kaydet” butonuna basılır.
Kullanıcı yönetici yapılmayacaksa, sistem üzerindeki “Yönetici” kullanıcıya durum bildirilir ve “BEAM Üzerinden Bir Kullanıcıya Nasıl Menü Yetkisi Tanımlanır?” başlığı altında bahsedilen yollar üzerinden ilgili kullanıcıya istenilen menü yetkisi, yönetici kullanıcı tarafından sağlanır.