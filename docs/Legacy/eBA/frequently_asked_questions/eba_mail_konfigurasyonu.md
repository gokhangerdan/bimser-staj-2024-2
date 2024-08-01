# eBA Mail Konfigurasyonu Nasıl Değiştirilir?

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada7d9a1cb-6f35-41aa-a612-9d8cf9a185ad)

Şekil 1’de, 1 numaralı C:/eBA/Common dizinindeki eBAConfigurationEditor.exe çalıştırılır. Açılan pencerede Mail Settings sekmesine tıklanır. 4 numaralı alandaki alanlar sistem bilgilerine göre yazılır.

SMTP Host: Maillerin gönderileceği smtp server adı veya ip adresi alanıdır.

SMTP Port: Smtp serverın kullandığı portdur. Genelde 25. veya 587. portlar kullanılmaktadır.

Username: Eğer “Required Authentication” seçeneği işaretli ise smtp servera bağlanırken kullanılacak kullanıcı adı bilgisidir.

Password: Bağlantı kullanıcı şifresidir. Default Address: eBA tarafından gönderilen maillerde gönderen adresi boş ise varsayılan olarak maillerin gönderen adresi bu değer olarak ayarlanır.

Default Name: eBA tarafından gönderilen maillerin gönderen adı boş ise bu değer kullanılır

Try Count: Mailler gönderilirken hata oluşabilir. Bu hatanın sebebi olarak smtp server, network, mail adresi yanlışlığı gibi birçok neden olabilir. Mail server mailleri gönderirken hata olursa mailleri tekrar göndermeye çalışır. Try Count, Mail Server’ ın mailleri kaç kere göndermeyi deneyeceği sayıdır.

Mails per Session: Mail Server, mailleri göndermeye her başladığında kaç mailin atılacağını belirler.

Delete Mails: Mailler gönderildikten sonra veritabanında saklanılacak mı yoksa silinecek mi değeridir. Silinecekse kaç gün sonra sileneceği açılan kutucuğa yazılır.

Requires Authentication: Smtp servera bağlanılırken kullanıcı adı ve şifresi gerekliliğini belirtir.

Debug: Debug modda daha ayrıntılı loglama yapılmaktadır.

Requires SSL Encryption: Smtp server bağlantısı sırasında SSL şifreleme kullanımını belirtir.