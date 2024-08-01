# Müşteri Şikayeti  Kayıtları Çekmek için Web Servis Kullanımı Hk.

QDMS Müşteri Şikayetleri  Web servisimize Qdms giriş linki /QDMSNET/MSWs/Main.asmx yazarak ulaşabilirsiniz.
Örnek olarak "http://qdmsv523.bimser.local/QDMSNET/MSWs/Main.asmx" olacaktır. QDMS'te açılmış şikayetlerin bilgilerini görebilmek için kullanacağınız metot MSBul ya da GetMSDataTable metodlarıdır.  Bu metotlar ile filtreleme yaparak QDMS içerisinde açılmış kayıtları görebilirsiniz. 

5.23 QDMS versiyonu kullanıyorsanız bu versiyonlarda güvenlik  sebebiyle Servis otantikasyonu vardır ve bunun içinde ServiceAuth metodu kullanılarak token alınır. Ekte Web servis ile ilgili tüm dokümanlara ulaşabilirsiniz. Servis otantikasyonu için de yapılması gereken işlemler ilgili dokümanlarda iletilecektir.

