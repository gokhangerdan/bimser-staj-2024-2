# YIL GEÇİŞLERİ SONRASI İŞ EMRİ OLUŞMAMA SORUNU VE ÇÖZÜMÜ

## Problemin Sebebi

İş Emri numaraları iş emri türü ve yıl bazında tutulmaktadır. İş Emri Türleri detay ekranında “Tek yıl başlangıç sayaç – tek yıl sayaç & çift yıl başlangıç sayaç – çift yıl sayaç” alanları bulunmaktadır. Her takvim yılı geçişi sonrası sistem çalışma yılı bilgisini güncellemekte ve “Tek yıl sayaç – çift yıl sayaç” isimli 2 alanı başlangıç sayaçlarındaki değere geri çekmektedir. Bu sıfırlama sonrası otomatik oluşan (periyodik bakım) iş emirleri ile numara sayaçları tekrar ilerlemektedir. 

Yıl geçişi sonrası sisteme ilk kez oturum açıldığında sıfırlama işlemi 2. Kez yapılmaktadır. Bu 2. Sıfırlama sonucu otomatik oluşan iş emirlerine verilen numaralar sistemde bulunurken, iş emri türü içinde tekrar başa dönüyor. Ve sonraki günlerde tekrar iş emri oluşturulmak istendiğinde de kayıt sistemde tanımlı (dublicate) hatası ortaya çıkıyor.

## Problemin Çözümü 

Bakım yönetimi > İş Emirleri sayfasından: Yeni geçilen yıla ait her iş emri türündeki en büyük iş emri numaraları bulunmalı ve not alınmalıdır.

Bakım yönetimi > İş Emri Türleri sayfasına girilerek, ilgili iş emri türlerindeki “Çift Yıl Sayaç – Tek Yıl Sayaç” alanları, not alınan en büyük numara ile güncellenir. Bu işlem sonrasında yaşanan problem düzelecek ve sistem girilen numaradan devam ederek iş emri numaraları üretmeye devam edecektir.


![](https://docsbimser.blob.core.windows.net/imagecontainer/09_HATA-ada97283-5a24-4a66-9473-1b17e6e5f952.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/07_ORDERNUMBER-7dadb7b9-7ae3-48c9-8420-67eb68e27e3b.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/08_ORDERNUBER_V-79cc0084-63b9-4af5-943c-1acb17ce5d42.png)

