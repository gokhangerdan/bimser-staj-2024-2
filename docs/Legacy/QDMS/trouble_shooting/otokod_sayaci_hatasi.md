# Otokod sayacı hatalıdır, lütfen sayacı kontrol ediniz

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc4be5fd2-2274-4642-ab69-b214fe59579e)

Risk  tabanlı modüller de toplu bir aktarım yapıldığında risk sayacının güncellenmesi kullanıcı tarafından atlanabiliyordu ya da risk ana form sayacı geri kaldığında sistem aynı RDFD kodunu tanımlayabiliyordu. Bu durumun önüne geçebilmek adına mevcut versiyonda bir düzenleme  yapıldı.

Almış olduğunuz uyarının çözümü için aşağıda ilettiğim işlem adımlarını bir kez uygulamanız yeterli olacaktır;

EYS > İlgili Risk Modülü > Risk Değerlendirme Formu Tanımlama menüsüne gelerek uyarıyı aldığınız ana formu seçiniz ve detaylar butonuna basınız.
Açılan ekranda risk detay formunuzun en son hangi kodu aldığını kontrol ediniz. Yani en büyük RDFD kodunu kontrol etmeniz gerekecek. Örneğin bu değerin RD.003.0050 olduğunu varsayalım. Yani sayaç son olarak 50 değerinde kalmış diye yorumlayabiliriz.

Ardından;
EYS > İlgili Risk Modülü > Risk Değerlendirme Formu Tanımlama ilgili ana formu seçiniz ve "Güncelle" butonuna basınız.
Son olarak açılan ekranda "Otomatik Kod Sayacı" alanına 50 yazarak kaydet butonuna basmanız yeterli olacaktır.


Ek olarak sorunu olay bildirim, sapma yönetimi vb yapıda çalışan modüllerde yaşıyorsanız ;

Entegre yönetim sistemi > İlgili Modül > Tüm Kayıtlar (menü adı sizin ortamınızda değişiklik gösterebilir) menüsüne geliniz.
Açılan ekranda kayıtların en son hangi kodu aldığını kontrol ediniz. Yani en büyük RDFD kodunu kontrol etmeniz gerekecek. Örneğin bu değerin 4400.0151 olduğunu varsayalım. Yani sayaç son olarak 151 değerinde kalmış diye yorumlayabiliriz.

Ardından;
SAT > BSAT > Konfigürasyon Ayarları > Parametreler menüsüne gelerek ilgili modülünü seçiniz ve arama butonuna basınız.

4 numaralı "Olay Bildirim Detayı Sayac" parametre değerine not aldığınız 151 değerini yazınız.

Bu işlemin ardından otomatik kod sayıcı kaldığı yerden devam edecektir.