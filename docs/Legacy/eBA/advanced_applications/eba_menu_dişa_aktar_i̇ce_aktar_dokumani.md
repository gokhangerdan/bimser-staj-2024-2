# eBA İş Akışı ve Doküman Yönetimi Sistemi Menü Dışa Aktar-İçe Aktar Dokümanı

## 1. Menünün Dışa Aktarılması-İçe Aktarılması


eBA uygulamasında menüye öge eklenerek oluşturulan yapı, farklı bir sistemde aynı kırılım yapısı
tekrar elle tek tek oluşturulmasına ek olarak, menü ağacı dışarı aktarılıp yeni sistemde içe aktarımı yapılarak tasarlanmış menü yapısı kolaylıkla taşınabilmektedir. Bu dokümanda dışa aktarım ve içe aktarım işlemlerinin nasıl yapılacağı açıklanacaktır.


### 1.1 İşlemlerin Yapıldığı Menü Yöneticisi Önizleme Alanına Erişim Sağlama


Menü dışarı aktarım işlemi sisteme giriş yapılarak ulaşılabilmektedir. Üst araç çubuğundaki Ayarlar simgesine tıklandığında gözüken pop-up menüde Menü Yöneticisi Önizleme sekmesine tıklanarak dışa aktarma işleminin yapılacağı panel görüntülenir.


![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%201-f722ef59-b35a-4583-8529-864388baaac7.png)

Şekil 1

Pop-up’taki Menü Yöneticisi Önizleme ve Menü Yöneticisi sekmeleri işlem yapılan kullanıcıda System Manager’da Authorization Manager üzerinden webMenuDesign yetkisi verildi ise görünür olmaktadır. Giriş yapan kullanıcıda bu sekmeler gözükmüyor ise System Manager uygulamasından ilgili kullanıcıya, pozisyona gibi istenilen role yetki eklenmesi sonrası, kullanıcı sistem çıkış yapıp tekrardan giriş yaptığında sekmeler gözükecektir.
Örneğin Şekil 2’de Kullanıcı Rolü alanında Ali Doğru kişisi eklenip, kullanıcıya Web kırılımı altındaki webMenuDesigner yetkisi verildiğinde, kişi hesabına giriş yapınca Şekil 3’de görüldüğü üzere Ayarlar menüsünde sekmeler görünür halde olacaktır.


![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%202:%20Kullanıcı%20Rolünde%20Yetkinin%20Tanımlanması-69895932-9f99-417e-b857-240992c2022c.png)

Şekil 2: Kullanıcı Rolünde Yetkinin Tanımlanması


![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%203:%20Kullanıcıda%20Menü%20Yöneticisinin%20Gözükmesi-2b3e9ca3-105d-4622-8725-def1c5fe8c34.png)

Şekil 3: Kullanıcıda Menü Yöneticisinin Gözükmesi


### 1.2 Menünün Dışarı Aktarılması

Web ara yüzündeki Menü Yöneticisi Önizleme butonuna tıklanarak açılan panelde Dışa Aktar butonuna (Şekil 4) tıklanarak, sistemdeki menünün dışarı aktarılması işlemin yapılacağı panel (Şekil 5) açılır.


![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%204:%20Dışa%20Aktar%20butonu-4565458e-1897-46b9-ae22-3ebcbb9e2745.png)

Şekil 4: Dışa Aktar butonu


![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%205:%20Dışa%20Aktar%20işleminin%20yapılacağı%20panelin%20açılması-aadbf0bd-1766-421a-9bcc-e64635629cb6.png)

Şekil 5: Dışa Aktar işleminin yapılacağı panelin açılması

Panel açıkken menüdeki ana öge kırılımına fare ile tıklanıp sürükle-bırak işlemi yapılarak dışa aktar paneli içindeki alana taşınmalıdır. Örneğin Şekil 6’da Uygulamalar ana menüsü içeriği fare ile sürükleme işlemi ile okun gösterdiği yere doğru taşınarak Şekil 7’deki gibi gözükmektedir.


![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%206:%20Uygulamalar%20menüsünün%20sürüklenmesi%20işlemi-da3a1fe1-6b2d-4fda-b043-4035786a0ed1.png)

Şekil 6: Uygulamalar menüsünün sürüklenmesi işlemi


![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%207:%20Sürükleme%20işleminin%20tamamlanması%20ile%20oluşan%20görünüm-ba9fefa2-4023-4fa5-bb35-753d05856f3e.png)

Şekil 7: Sürükleme işleminin tamamlanması ile oluşan görünüm

Diyagram Önizleme ifadesinin yanındaki dışarı aktarma butonuna tıklanıldığında (Şekil 8) alan içindeki bütün menü kırılımları .json dosyayı olarak işlem yapan kullanıcı bilgisayarına (Şekil 9) indirilir.


![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%208:%20Dışa%20aktar%20işlemini%20başlatma-4f4f1b96-f6f9-451b-bb30-9151474db0de.png)

Şekil 8: Dışa aktar işlemini başlatma


![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%209:%20İşlemi%20yapan%20kullanıcıda%20menünün%20indirilmesi-945e7c08-c885-413c-9d19-47b7f1c9043e.png)

Şekil 9: İşlemi yapan kullanıcıda menünün indirilmesi



Menü içindeki bütün ögelerin dışarı aktarılması işleminin yapılabileceği gibi, istenirse taşınan ana kırılım içindeki ögeler kaldırılarak, sadece belli bir menü grubunun taşınması işlemini de
yapılabilmektedir.
Dışarı aktarılacak ögelerin kaldırılması işlemi için, Diyagram Önizleme alanında her menü ögesinin yanında fare işaretçisi ile gelindiğinde menünün yanında silme butonu (Şekil 10) gözükmektedir. Şekil 10’da fare işaretçisi ile Group Panel01 ögesinin üzerine gelindiğinde, ögede eksi butonu görünür durumunda olmaktadır.


![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%2010:%20Silme%20butonunun%20menü%20ögesinde%20gözükmesi-4215a485-c0cd-49e1-9c28-6bd0d2c3a9d5.png)

Şekil 10: Silme butonunun menü ögesinde gözükmesi

Group Panel01 ögesi yanındaki sil butonuna tıklanıldığında, panel ve içindeki ögeler dışarı aktarılacak menü listesinden çıkarılacaktır.


![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%2011:%20Dışa%20aktarda%20ögelerin%20silinmesi%20sonucunda%20yeni%20diyagram-4db3a4e9-0d5b-49d7-a64c-2451eae6f0d8.png)

Şekil 11: Dışa aktarda ögelerin silinmesi sonucunda yeni diyagram

Diyagram Önizleme ifadesinin yanındaki dışarı aktarma butonuna tıklanıldığında (Şekil 8) alan içindeki bütün menü kırılımları .json dosyayı olarak işlem yapan kullanıcı bilgisayarına (Şekil 9) indirilir.
Aktarılan dosyada, sistemdeki profiller ve menü ögeleri ilişkisi bilgisi saklanmaktadır. Bu sayede menünün aktarılacağı yeni sistemde, ögelerin alındığı sistemdeki isimle aynı menü profilleri oluşturulduğunda, oluşturulan profiller için menü ögeleri tekrardan seçilmesine gerek yoktur.
Örneğin X Firması-Test sisteminde Uygulamalar menüsü tasarlanmış ve InsanKaynaklari, BilgiIslem ve Hukuk olmak üzere üç farklı profil ve her profilde Uygulamalar içinde hangi ögelerin görüneceği seçilmiş olsun. Menü .json dosyası olarak dışarı aktarıldığında, aktarılan ögeler içinde hangi menü profillerinde gözükeceği bilgisi saklamaktadır. X Firması-PRODUCTION sistemine menü
dosyası içeri aktarıldığında, aktarılan sistemde de InsanKaynaklari, BilgiIslem ve Hukuk isimli menü profilleri halihazırda bulunuyorsa; dosya içeri aktarıldığında profil ve menü ögeleri sistem tarafından eşleştirilerek profilin tanımlı olduğu kullanıcılar menü ögelerini görebilecektir. Taşınma işlemi esnasında menü profilleri bulunmuyor ve sonradan oluşturulduğunda da profil-menü ögesi eşleştirilmesi yapılacaktır.
Not: Yukarıda anlatılan senaryodaki menü profili-menü ögesi eşleştirilmesinin yapılabilmesi için,
her iki sistemde de menü profili isimleri aynı olacak şekilde oluşturulmuş olmalıdır.


### 1.3 Menünün İçeri Aktarılması

Web ara yüzündeki Menü Yöneticisi Önizleme butonuna tıklanarak açılan panelde İçe Aktar butonuna (Şekil 12) tıklanarak, sistemdeki menünün içeri aktarılması işlemi için dışarı aktarılmış .json dosyasının seçileceği dizin penceresi (Şekil 13) açılır.



![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%2012:%20İçe%20Aktar%20işlemini%20başlatma-9571cc96-7dbb-4c3b-9368-39de84a1c510.png)

Şekil 12: İçe Aktar işlemini başlatma

![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%2013:%20Menü%20json%20dosyasının%20seçilmesi-33126748-03ae-4357-aed3-13f7b76171d0.png)

Şekil 13: Menü json dosyasının seçilmesi


Dosya seçilip Aç butonuna tıklanarak, seçilen dosya içeriği Diyagram Önizleme alanında listelenir.


![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%2014:%20İçe%20Aktarılan%20menü%20ögelerinin%20ön%20izlemesi-60b1daae-cdd0-4dc7-8394-bc5951c92fba.png)

Şekil 14: İçe Aktarılan menü ögelerinin ön izlemesi


Ögelerin listelendiği panelde, panel içeriğinin sistemdeki menüye eklenmesi için, öncelikle Diyagram Önizleme yanındaki butona tıklanmalıdır.


![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%2015:%20İçe%20aktarım%20işlemine%20başlama-c053b2c6-9961-4388-a877-1522f6c9e71d.png)

Şekil 15: İçe aktarım işlemine başlama

Butona tıklandığında ekranın altında Şekil 16’daki mesaj gösterilecektir.


![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%2016:%20Diyagram%20önizlemede%20butona%20tıklanarak%20mesajın%20alınması-ea8a4cb4-fdba-4bb9-8b25-818883eb1034.png)

Şekil 16: Diyagram önizlemede butona tıklanarak mesajın alınması

İşlemin tamamlanması için Menu Designer’daki Kaydet butonuna (Şekil 17) tıklanmalıdır.


![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%2017:%20Kaydet%20butonuna%20tıklayarak%20içe%20aktarılmak%20istenen%20ögelerin%20kaydedilmesi-e9599795-7a31-4b72-a61f-c4e9c0b0f6e0.png)

Şekil 17: Kaydet butonuna tıklayarak içe aktarılmak istenen ögelerin kaydedilmesi

İşlemlerin tamamlanması ile taşınan menü yeni sistemde görünür olacaktır.


![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%2018:%20İçe%20aktarılan%20menünün%20gösterilmesi-c9c21afa-3283-4057-96cb-80069ab94615.png)

Şekil 18: İçe aktarılan menünün gösterilmesi

Menü içeri aktarma işleminde, menü dışarı aktarda olduğu gibi istenmeye menülerin kaldırılması mümkündür. İçe aktar işlemi esnasında Şekil 15’teki butona tıklanmadan önce menü ögeleri
Diyagram Önizleme içinden kaldırılmalıdır.
İçe aktarılacak ögelerin kaldırılması işlemi, Diyagram Önizleme alanında her menü ögesinin
yanında fare işaretçisi ile gelindiğinde menünün yanında silme butonu (Şekil 19) gözükecektir. Şekil 19’da fare işaretçisi ile Group Panel01 ögesinin üzerine gelindiğinde, ögede eksi butonu görünür durumunda olmaktadır.


![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%2019:%20Menünün%20içe%20aktarımı%20yapmadan%20önce%20kaldırılması-c4ebc36a-1f20-43f2-8a61-0b6168e224a6.png)

Şekil 19: Menünün içe aktarımı yapmadan önce kaldırılması

Group Panel01 ögesi yanındaki sil butonuna tıklanıldığında, panel ve içindeki ögeler dışarı aktarılacak menü listesinden çıkarılacaktır.

Listeden çıkarma işlemi sonrasında içe aktar işlemi tamamlandığında menü yapısı Şekil 20’deki gibi gözükecektir.


![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%2020:%20İçe%20aktarma%20işlemi%20sonrasında%20silinmiş%20menü%20sonucu-a86a9ec9-b778-41a3-858e-61d2f881a3b5.png)

Şekil 20: İçe aktarma işlemi sonrasında silinmiş menü sonucu


