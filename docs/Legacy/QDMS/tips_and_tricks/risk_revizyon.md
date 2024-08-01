# Risk Modülleri Üzerinde Revizyon Özelliği

Burada iki farklı işlem adımıyla ilerleyebilirsiniz.

1- Manuel takip

Bu durumda aksiyonlarınız tamamlandıktan sonra genel olarak risk kaydını açan kullanıcı;

Entegre Yönetim Sistemi > İlgili Risk Modülü > Risk Değerlendirme Formu Tanımlama > Detaylar  menüsünde sağ üstte yer alan "Revizyon" butonuna basarak ilgili risk kaydında bir revizyon başlatabilir ve riskin değerlerini güncelleyebilir. Bu işlemin ardından yine menüde yer alan "Eski Revizyonlar" butonu yardımıyla da riskin daha önceki revizyonlarda hangi değerlere sahip olduğu bilgisi görüntülenebilir.


Sistem alt yapı tanımları>İlgili risk modülü>İlgili risk modülü parametreleri üzerinde bulunan 80 numaralı parametre "Revizyon kullanılacak mı? parametresi evet yapıldığında buton aktif olacaktır. 


![](https://docsbimser.blob.core.windows.net/imagecontainer/Revizyon%2080%20numaralı%20parametre.png-50aa1567-ee13-41cf-95f4-31d52b4a006e.png)

2- Aksiyon üzerinden takip

İlgili risk modülü parametrelerinden;

"Tüm önlemler tamamlanınca risk değerlendirme aksiyonu açılsın" parametre değeri "Evet" ise, tüm aksiyonlar tamamlandığında risk kaydını açan kullanıcıya sistem tarafından otomatik bir aksiyon açılır. Bunun amacı açılan aksiyon ile risk kaydını açan kullanıcının ilgili risk kaydı için revizyon başlatmasını sağlamak.

![](https://docsbimser.blob.core.windows.net/imagecontainer/Tüm%20önlemler%20tamamlanınca%20Risk%20Değerlendirme%20aksiyonu%20açılsın.png-65bea22e-bd75-4a02-be29-e96e14dbe63a.png)

İlgili özelliğin çalışması için parametre evet yapıldıktan sonra bir çok parametre üzerinde değer ataması yapılmalıdır.

"Risk Değerlendirme Talebinde Kullanılacak Ana Aksiyon Kodu ?"   = EYS > Aksiyon > Planlama menüsünde yer alan, risk talebi aksiyonlarınızın hangi ana aksiyon planı altında yer alacağını belirlediğiniz parametre. Bu parametre değerine EYS > Aksiyon > Planlama menüsünde yer alan ana aksiyon plan numarası yazmalısınız.

"Risk Değerlendirme Talebinde Kullanılacak Aksiyon Süresi ?"  = Örneğin bu parametreye 3 yazdığınızı varsayalım. Bu durumda sistem risk talebi için oluşturulacak aksiyonu, işlem yapılan tarihin üzerinde 3 ekleyerek bitiş tarihini hesaplayıp otomatik olarak aksiyonu açacaktır.

"Risk Değerlendirme Talebinde Kullanılacak Aksiyonun Tip Kodu ?" = SAT > Aksiyon > Aksiyon Kalem Tipi Tanımlama menüsünde tanımlı olan bir aksiyon kalem tipinin kodunu yazmalısınız.

"Risk değernedirme talebinde kullanılacak aksiyon açıklaması"  = açılan otomatik aksiyonun tanımında hangi ifadenin yazdığının belirlendiği parametre.

Yukarıda ilettiğim parametrelere bağlı olarak risk kaydını açan kullanıcıya risk kaydındaki tüm önlemler tamamlandığında otomatik bir aksiyon açılır ve kullanıcının ilgili risk kaydı için bir revizyon başlatması beklenir.


![](https://docsbimser.blob.core.windows.net/imagecontainer/Risk%20değerlendirme%20parametreleri.png-1cc04e75-9217-415f-8ce5-2b973959fd9b.png)

