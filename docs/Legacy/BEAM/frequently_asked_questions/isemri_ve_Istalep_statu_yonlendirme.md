# İş Emri ve İş Talebinde Statü Nasıl Yönlendirme Yapıyor?

Bir iş emri veya iş talebi oluşturulup bakım tamamlanana kadar geçen sürede ilgili kayıtlar birçok statü alabilirler. Her statü değiştiğinde uygulama ön tanımlı adreslere e-posta veya sms gönderebilmektedir. Bu ayarlar statü kaydı içerisinden yapılmaktadır.
İş emri ya da iş talebinde statü değiştiği zaman, uygulama, ilgili kaydın kısım, iş tipi, bakım / arıza kodu veya öncelik değeri ile uyuşan bir “E-Posta ve Sms Tablosu”  satırı olup olmadığını kontrol eder. Eğer uyuşan bir satır bulur ise ilgili satırdaki bildirim adreslerine bildirimde bulunur.


![](https://docsbimser.blob.core.windows.net/imagecontainer/Isemri_Istalep_statu_yonlendir-0e7da399-b46d-4f51-8bee-5033ef01ffc7.png)

Uygulama uygun satırı bulamadıkça bir sonraki koşulu sağlayan satır olup olmadığına bakar; Arama işlemi aşağıdaki sıra ile olur.


![](https://docsbimser.blob.core.windows.net/imagecontainer/Isemri_Istalep_statu_yonlendir1-51d961fb-f5e8-40ea-8b91-7311544b2ca3.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/Isemri_Istalep_statu_yonlendir3-48bdc0d0-493f-480a-874e-8a62b3c3b55e.png)

Uygulama uyuşan satırı bulduğu zaman aramayı durdurur yani bir seferde sadece tek bir satırdaki alıcılara bildirim işlemi yapılır.

