# SAP.Middleware.Connector.RfcParameterMetada.Direction hatası

![](https://docsbimser.blob.core.windows.net/imagecontainer/Ekran%20Alıntısı%20Bilkom.png-abd50828-0296-4b26-9fe3-6691d1208d79.png)

Sorun:" SAP servisi çalışıyor görünüyor. SAP 7.20 yüklü. SAP GUI üzerinden RFC sorunsuz çalıştırılabiliyor. System manager üzerinden eBASAPApi ile açılan bağlantılar Not Responding de kalıyor çalışmıyor. eBA SAP 3 üzerinden açılan bağlantılar hata veriyor."

Çözüm: "SAP entegrasyon ayarları kontrol edilir sonrasında SAP servisi çalıştıran kullanıcı local admin yetkisinde olması gerekiyor. Bu hata yetkiden kaynaklı olarak alınmıştır.