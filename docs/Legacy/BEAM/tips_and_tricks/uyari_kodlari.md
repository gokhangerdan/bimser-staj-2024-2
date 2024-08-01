# Uyarı Kodları

Uyarı kodları bir iş emrine müdahale, bakımın devam etme süresi veya iş emrinin açık kalma süresi öngörülen sürenin üstüne çıkarsa belirlenen alıcılara e-posta veya sms ile uyarı gönderilmesi için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/uyarı%20kodları%20sayfası-5971cd22-6e1d-4a3b-907b-61dbd20b158d.png)

## Kurallar Bölümü

İlgili kayda ait uyarı kuralları “Kurallar” başlıklı sekmede yapılmaktadır. Temel olarak tanımlar “X dakikayı geçince Y alıcılarına Z içerikli e-posta ve/veya sms gönderilsin” şeklinde yapılmaktadır.
Bir kural satırı bir iş emri için bir defa uygulanmaktadır. Yani 10dk açık kalmış bir iş emri için kriterlere uygun bir uyarı satırı işletildiği zaman aynı iş emri için bir daha bu satır işletilmez. Bu durumda kuralları ilgili kaydın içerisine eklerken zaman koşulunu küçükten büyüğe doğru eklemek doğru olacaktır.
Birden fazla alıcı eklemek için ;
bir kişinin mail adresini girdikten sonra sonuna ";" koyarak diğer kullanıcının mail adresini girerek birden çok kullanıcıya uyarı gitmesini sağlayabilirsiniz.

![](https://docsbimser.blob.core.windows.net/imagecontainer/kurallar-24288954-7141-4e95-8ebb-8786e3f4dfa0.png)

Uyarma Tipi=Uyarı verilmek istenen süre tipi seçilir. 

Operatör=Seçilen Süre tipinden küçük,büyük ya da eşit olma durumları kontrol edilir

Değer=Kontrol edilmek istenen değer girilir.

SMS=Bu alan işaretli ise SMS gönderimi yapılır.

Mail=Bu alan işaretli ise Mail gönderimi yapılır.

Gsm Listesi=SMS gönderilmek istenen GSM numaraları girilir.

Mail Listesi=Mail gönderilmek istenen mail adresleri girilir.

Mail Formatı Kodu=Gö      nderilmek istenen mail formatı seçilir.

SMS Formatı Kodu=Gönderilmek istenen sms formatı seçilir.


## Filtre Bölümü

Filtre bölümü içerisinden verilecek olan uyarıyı daha fazla kişiselleştirip detaylı bir şekilde uyarı kontrolü sağlayabilirsiniz.

![](https://docsbimser.blob.core.windows.net/imagecontainer/filtre-0900688d-fc58-4390-b021-31c5af90ebcc.png)