# Rapor Zamanlayıcı

Rapor zamanlayıcısı, belirtilen sürede filtrelenmiş raporun istenilen mail adreslerine gönderilmesini sağlamaktadır.
Rapor hangi yönetimden hazırlanacak o yönetime girilir.
Raporlar alanından ilgili rapor seçilir.(Excel ile oluşturulan raporlarda zamanlayıcı bulunmamaktadır.)

Raporun hangi filtreler ile gelmesi isteniyorsa buna göre filtreleme işlemi yapılır.
(Örneğin: Sadece varlık tanımı xxx olan varlıklar raporla gelsin.)
Filtreleme işlemi sonrası ‘Zamanlayıcı’ butonuna basılır.
Yeni bir zamanlayıcı yapılıcak ise ‘Ekle’, olan düzeltilicek ise ‘Değiştir’, olan silinicek ise ‘Sil’ tuşana basılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/mupload-d3b5463e-b6e9-40b6-bccf-ac7f695a0c29.png)

img1.png

![](https://docsbimser.blob.core.windows.net/imagecontainer/mupload-0394f10d-85e6-47d6-867e-59981dfc21fc.png)

img2.png

## Genel Bilgiler Alanı Doldurulması Gereken Yerler

Kod alanı; bensersiz olmalıdır.
Açıklama alanı; istenilen açıklama yazılabilir.
Gönderim format alanı(mail için); gönderilen mailin açıklama alanı için yazılan formattır. Daha önceden oluşturulmuş bir gönderim formatı seçilmelidir.

Boş rapor gönderim format alanı; düzenlemiş olan rapordan belirtilen sürede bir veri gelmez ise eklenen mail adreslerine bunu belirten bir mail gitmesi için eklenebilir alandır.(Gönderim format alanındaki ile aynı olabilir.)

Çıktı biçimi alanı; iletilen raporun hangi formatta gelinmesi istenirsa ona göre seçim yapılır.
Atkif alanı;  zamanlayıcı kullanılıyor ise tikli, kullanılmak istenilemez ise tiki kaldırarak pasif hale getirilebilir.



![](https://docsbimser.blob.core.windows.net/imagecontainer/mupload-a34353ea-b0bc-4a14-b545-ee2861e85483.png)

img3.png

## Zamanlayıcı Alanı Doldurulması Gereken Yerler

 Hazırlama periyot tipi: Ne kadar sürede hazırlasın raporu
Hazırlama periyodu: Verilen periyotta kaç kere hazırlasın
Saat kaçta hazırla:(tikliyse) belirtilen saatte rapor gönderimi yapılır.
Periyodik olarak hazırla: (tikliyse) başlama ve bitiş saatlerinde belirtilen saat aralığında bir rapor göndermektedir.


![](https://docsbimser.blob.core.windows.net/imagecontainer/mupload-67b66a79-0ab6-4905-a325-6fdb1552f8b7.png)

img4.png

## Alıcı Alanı Doldurulması Gereken Yerler

Mail ile raporun gönderileceği kişiler bu alana eklenir.
Kullanıcı, kullanıcı grubu, bilgilendirme grubu yada mail adresi olarak bu alana adresler eklenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/mupload-f4ac0fe0-d251-445b-88fa-1c8d7014c136.png)

img5.png

## Filtre Alanı Doldurulması Gereken Yerler

Raporun kaç günlük veri ile rapor getirilmesi isteniyor ise ona göre gün sayısı belirtilir.(Örneğin: Beş günlük bir rapor isteniyor ise 5 – 0 olarak düzenlenir.)
İlk rapor gün sayısı geçmişten kaç gün, diğer rapor gün sayısı alanı ilerideki kaç günü raporda kapsayacağını belirtir.
(İşlem için zamanlayıcı oluşturulmadan önce tarih filtresi gerilmesi gerekmektedir.)
Özel tarih fitresi ile haftanın başından itibaren, ay başından itibaren yada yıl başından itibaren rapor gönderimi yapılmaya başlamaktadır.


![](https://docsbimser.blob.core.windows.net/imagecontainer/mupload-3bdb4f2b-870c-4d53-a5a2-ef166b719cb1.png)

img6.png