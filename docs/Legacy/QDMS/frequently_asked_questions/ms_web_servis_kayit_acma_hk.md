# Müşteri Şikayeti  Kayıt açmak  için Web Servis Kullanımı Hk.

QDMS Müşteri Şikayetleri  Web servisimize Qdms giriş linki /QDMSNET/MSWs/Main.asmx yazarak ulaşabilirsiniz.
Örnek olarak "http://qdmsv523.bimser.local/QDMSNET/MSWs/Main.asmx" olacaktır.
Yeni MS kaydı oluşturmak için YeniIcerik metdounu kullanabilirsiniz. Yeni bir döf kaydı oluşturmanız için minimum göndermeniz gereken alanlar MKOD(Müşteri kodu), SIKAYETG(Şikayeti Açan), SISTEMEKT(Şikayet Açma tarihi), ICDIS(İç Müşteri, Dış Müşteri Şikayeti).
5.23 QDMS versiyonu kullanıyorsanız bu versiyonlarda güvenlik  sebebiyle Servis otantikasyonu vardır ve bunun içinde ServiceAuth metodu kullanılarak token alınır. Destek ekibinden Web servis ile ilgili tüm dokümanları talep edebilirsiniz. Servis otantikasyonu için de yapılması gereken işlemler ilgili dokümanlarda iletilecektir.


