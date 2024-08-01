# İş Talebinde Bakım Onay Nedir? Nasıl Devreye Alabilirim?

Bakım onay tabiri iş talebi için kullanılır. Normal şartlarda bir iş talebi oluşturulduğu zaman ilgili talep bilgilerini de içeren bir iş emri oluşturulur. Bakım personeli de bu oluşturulan iş emrini görür ve ilgili bakımı yapar.
Bazı durumlarda yapılan iş talebinin hemen iş emrine dönüşüp bakımcı personelin iş emri listesinde görünmesi istenmeyebilinir. Bu tip durumlarda “Bakım Onay” tabiri devreye girmektedir. Bakım onay alanı “Evet” olmayan iş talepleri iş emrine dönüşmezler ve bakımcı personel tarafından iş emri listesinde görünmezler.


![](https://docsbimser.blob.core.windows.net/imagecontainer/Istalep_bakimonaypic1-9bbf93f3-d9af-40bf-9801-55e506a8e77c.png)

Bakım Onay sistemini devreye almak için;
1.	Şirket kaydı üzerindeki “Genel Bilgiler” sekmesinde bulunan “Varsayılan Onay Değeri” başlıklı alanda “Hayır” değeri seçilmelidir. Bu sayede oluşacak tüm iş taleplerinin ön tanımlı olarak(varsayılan) bakım onaysız oluşması sağlanır.
2.	Tüm talep açacak kullanıcılardan, iş talebi kaydı içerisindeki “Bakım Onayı” değerini değiştirme yetkisi alınmalıdır. Bu işlem için, bu kullanıcıların bağlı oldukları kullanıcı grubu kaydındaki “BCG1.005”  kodlu parametre pasif duruma getirilmelidir.
Bu sayede talep açan kullanıcılar, varsayılan bakım onay değeri “Hayır” olan iş taleplerinin bakım onay değerini “Evet” olarak değiştiremeyeceklerdir.
3.	Bakım onaysız açılan taleplerin, bakım onayını verecek ve iş emrine dönüştürecek kullanıcılara yetki verilmelidir. Bu işlem için onay verecek kullanıcıların bağlı oldukları kullanıcı grubu kaydı içerisinden “BCG1.005”  kodlu parametre aktif duruma getirilmelidir.


