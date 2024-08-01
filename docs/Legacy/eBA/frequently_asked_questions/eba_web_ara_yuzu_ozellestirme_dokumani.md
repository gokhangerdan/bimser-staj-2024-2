# eBA Web Ara Yüzü  Özelleştirme Nasıl Yapılır?

eBA web ara yüzünde kurulum ile gelen varsayılan görünüm dışında, firmalarınuygulama üzerinde 
kendi markalaşmalarını yapmasısağlanmakta, ara yüzde özelleştirme yapılabilmektedir. Bu dokümanda 
web ara yüzünde yapılabilecek özelleştirmeler ve bu özelleştirilmelerin nasıl gerçekleştirileceği
açıklanmaktadır.

### 1. Web Tarayıcısı İkonunun Değiştirilmesi

Web ara yüzüne giriş ekranında,tarayıcı penceresindeki sekmede gösterilen ikonun (1 numaralı 
işaretli alan) değiştirilmesi için dosya özellikleri 
• Çözünürlük: 16x16 piksel
• Dosya ismi: favicon
• Dosya uzantısı: ico
olacak şekilde yeni ikon dosyası hazırlanmalıdır. Değiştirilmek istenen örnek bir ikon dosyası Şekil 
2’de görünebilir.


![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9744fa9b-11fb-415f-bc10-9a7e3d16ac98)

Tasarlanan ikon dosyası, sunucuda eBA’nın kurulu olduğu klasör içeresinde bulunan iki farklı 
klasör yolundaki “favicon.ico” dosyası ile değiştirilir. Değiştirilecek dosyaların bulunduğu dizinler
• C:\BimserCozum\eBA\eba.netiçerisinde favicon.ico dosyası
• C:\BimserCozum\eBA\eba.net\Desktop\Images\Design\Theme içerisinde favicon.ico 
dosyası olarak barındırılmaktadır.
Dikkat: favicon.ico dosyası için belirtilen dizinler, eBA uygulaması dizininin kurulumda değiştirilmediği, 
kurulum ile gelen varsayılan dosya yolu ile kurulduğu dikkate alınarak yazılmıştır. Eğer bu dosya yolu 
değiştirildiyse, belirtilen klasör dizinleri sunucudaki dizine göre düzenlenmelidir. 
Sistemde bu iki dosya yolundaki favicon’un değiştirilmesi sonrasındaeBA servisleri yeniden 
başlatılmalıdır. Servisi yeniden başlatmak için sunucudaki .bat uzantılı servisleri yeniden başlatmayı 
sağlayan dosya, yönetici olarak çalıştırılır.
Dikkat: bat uzantılı dosya çalıştırıldığında, sisteme giriş yapmış tüm kullanıcılar otomatik olarak çıkış
işlemi gerçekleştirilmektedir. 
Web ara yüzünde yeniden giriş yapıldığında tarayıcı sekmesindeki ikon, değiştirilmiş ikon olarak 
gelecektir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb52e074d-bc5d-48ff-bfec-dae5a8ed2714)

### 2. Giriş Sayfasında Logoların Değiştirilmesi

### 2.1 Giriş bilgileri bölümünde bulunan logonun değiştirilmesi

Web ara yüzünde giriş ekranında, kullanıcı bilgilerinin üzerinde bulunan logo değiştirilmek 
isteniyorsa, yeni resim dosyasının özellikleri
• Çözünürlük: 198x74 piksel 
• Dosya ismi: ebalogo
• Dosya uzantısı: png 
olacak şekilde hazırlanmalıdır. Hazırlanan yeni logo, 
“C:\BimserCozum\eBA\eba.net\Desktop\Images\Design\HeaderText” içerisindeki ebalogo.png
dosyası ile değiştirilir. 
Dikkat: Belirtilen dizin, eBA uygulaması dizininin kurulumda değiştirilmediği, kurulum ile gelen 
varsayılan dosya yolu ile kurulduğu dikkate alınarak yazılmıştır. Eğer bu dosya yolu değiştirildiyse, 
belirtilen klasör dizinleri sunucudaki dizine göre düzenlenmelidir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc73f9aac-672b-42f1-8dac-7971373dab49)

Logonun değiştirilmesi sonrası eBA servisleri yeniden başlatılmalıdır. Servisi yeniden başlatmak için 
sunucudaki .bat uzantılı servisleri yeniden başlatmayı sağlayan dosya, yönetici olarak çalıştırılır.
Dikkat: bat uzantılı dosya çalıştırıldığında, sisteme giriş yapmış tüm kullanıcılar otomatik olarak çıkış
işlemi gerçekleştirilmektedir.
İşlemler sonrası web ara yüzünde yeniden giriş yapıldığında giriş sayfasında giriş bilgileri üzerindeki logo
yeni logo olarak görünür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc0d9fec9-cff4-4c10-b3e8-299e18984afd)

### 2.2 Giriş sayfasında sol üst köşede bulunan logonun değiştirilmesi

Web ara yüzünde giriş sayfasının sol üst köşesindeki logonun değiştirilmesi isteniyorsa
(resimdeki işaretli alan) Doküman Yönetiminde system kütüphanesi içine customstyle isminde bir 
klasör(Şekil 8) oluşturulmalıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada060a038-a0df-4a3d-9dd7-caff58cc61e5)

Oluşturulan klasör içerisine, customstyle.cssisimli stil dosyası ve tasarlanan son üst logosu eklenir. 
Yüklenen dosya içindeki css kodu Şekil 7’deki gibi görünmektedir.
Not: .startupHeader sınıfı içindeki background-image özelliğine yazılmış toplogo.png adlandırılması,
değiştirilecek yeni logonun ismini belirmektedir. toplogo ifadesi yerine farkı bir isim yazılabilir ancak 
yazılan isim yüklenecek resim dosyası ile aynı olmalıdır.
Not: Bu örnekte kullanılan logo çözünürlüğü 196x75 pikseldir.


![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3d965068-d109-4446-a3bc-6d52d1d33762)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload91cd9926-c146-4827-b692-e809d74da420)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload683e52f7-4d54-424c-80b0-188139b48776)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadeab22c44-8c25-4c42-8c6b-9e3f242fed80)

Logonun değiştirilmesi sonrası eBA servisleri yeniden başlatılmalıdır. Servisi yeniden başlatmak için 
sunucudaki .bat uzantılı servisleri yeniden başlatmayı sağlayan dosya, yönetici olarak çalıştırılır.
Dikkat: bat uzantılı dosya çalıştırıldığında, sisteme giriş yapmış tüm kullanıcılar otomatik olarak çıkış
işlemi gerçekleştirilmektedir.
İşlemler sonrası web ara yüzünde yeniden giriş yapıldığında, giriş sayfasının sol üst köşesinde yeni logo
gelmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3df7244e-4362-49b9-aa27-36ac21d561d3)

### 3. Arka Plan Resminin Değiştirilmesi

Web ara yüzünde arkaplanda gösterilen vektörel resim yerine farklı bir resim kullanılmak isteniyorsa
Doküman Yönetiminde system kütüphanesi içine customstyle isminde bir klasör (Şekil 12) oluşturulur.
Oluşturulan yeni klasör içerisine, customstyle.css ve tasarlanan arka plan resmi eklenir. Yüklenen 
CSS dosyası içine Şekil 1’de belirtilen kod yazılır.
Not: Background satırında url parantezi içerisindeki water_background.jpg ismi, örnek için kullanılan 
arka plan resmine ait olup, istenilen şekilde değiştirilebilmektedir.(water_background.jpg isimli 
dosyanın çözünürlüğü 1920x1080 pikseldir.)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload35eb3af7-7129-4824-a23a-15937ea620e4)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc19501cf-5430-4b7e-b104-abf682b4eb53)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc5620c57-9d1b-46a5-a1da-b6d818bc2f91)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfd380723-563a-4ce5-91d7-9939f37f1a95)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload61e701e4-f81f-4bd4-ba78-bee35872ffd8)

### 4. Giriş Sonrası Tarayıcı Sekmesindeki Yazının Değiştirilmesi

Tarayıcı sekmesinde gösterilen yazının değiştirilmesi isteniyorsa aşağıda belirtilen işlemler
uygulanabilir. Bu işlemle giriş yapıldıktan sonra tarayıcıdaki başlık bilgisi değişmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb5d23deb-cfb3-4107-a4da-863113d4341d)

eBA’nın sunucuda kurulu olduğu dizin içerisinde (varsayılan kurulum yolu C:\BimserCozum\eBA’dır, bu 
yol değişkenlik gösterebilir) Languages klasörü içindeki Server klasöründe bulunan xml dosyalarında, 
başlığın değiştirileceği dile ait dosya xml görüntüleme uygulaması ile açılır. Dosya içeriğindeki 
170appname isimli satırdaki ait değer, değiştirmek istenilen başlık bilgisi ile değiştirilir. 
Not: Başlık bilgisi hangi dillerde değiştirilmek isteniyorsa, o dillere ait xml dosyalarında 170appname 
satırında değişiklik yapılmalıdır.


![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload93987dc1-8b0f-4214-8f84-58d369a32f8b)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2004a252-383a-49bf-84b4-c8fd8531bb5e)

XML dosyasında yapılan değişiklik ardından, eBA servisleri yeniden başlatılmalıdır. Servisi yeniden 
başlatmak için sunucudaki .bat uzantılı servisleri yeniden başlatmayı sağlayan dosya, yönetici olarak 
çalıştırılır.
Dikkat: bat uzantılı dosya çalıştırıldığında, sisteme giriş yapmış tüm kullanıcılar otomatik olarak çıkış
işlemi gerçekleştirilmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf869a5e6-a0fa-47de-a1e9-40eb6abdffdc)

### 5. Giriş Öncesi Tarayıcı Sekmesindeki ve Giriş Bilgileri Üstündeki Yazının Değiştirilmesi

Web ara yüzünde giriş yapılmadan önce tarayıcı sekmesinde ve kullanıcı girişi alanı üzerinde
gösterilen yazıların değiştirilmesi isteniyorsa aşağıda belirtilen işlemler uygulanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5ebf3002-7851-495b-aebc-ed107766cbe7)

eBA’nın sunucuda kurulu olduğu dizin içerisinde (varsayılan kurulum yolu 
C:\BimserCozum\eBA’dır, bu yol değişkenlik gösterebilir) Common klasörü içinde bulunan eBA
Configuration Editor uygulaması çalıştırılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8b30d1ee-8141-49da-a562-30490f70e017)

eBA Configuration Editor içindeki Advanced sekmesine tıklanılarak (1 numaralı işaretli alan)
sekmeye geçiş yapılır. Listelenen değerlerde Web sekmesine tıklanıp (2 numaralı işaretli alan) uygulama 
içerisindeki küçük yeşil artı işaretine (3 numaralı işaretli alan) tıklanarak yeni değer sekmesi eklenir.


![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd65c67cb-a661-447f-a6fa-e87d9b23bfe4)

Yeni değer eklendiğindeki “Node Text” ifadesi “ApplicationCaptions” olarak değiştirilir

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1f3f1ee5-486d-4c6d-855c-bf2d4b3154ed)

Eklenen değer alanı başlığının değiştirilmesi sonrasında ApplicationCaptions alanı seçili iken, Key 
alanına gösterim yapılacak dilin ismi (Turkish, English, Russian, French vb.)yazılmalıdır. Value alanına ise 
o dile ait başlık bilginin karşılığı tanımlanmalıdır.
Not: Şekil 23’de tanımlama yapılan sistemde beş farklı dil aktif olduğundan her bir dile ait karşılıklar 
yazılmıştır. eBA uygulamasında aktif olan dillere göre key ve value karşılıkları yazılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9a735da5-f1bf-47f1-a512-5dcb1c0c4740)

ApplicationCaptions içerisinde diller ve karşılıklarının girişisonrasında, eBA Configuration 
Editor’da File butonuna tıklanarak açılan panelde Save seçeneğine tıklanır. Değişikliklerin kaydedilmesi 
sonrasında eBA servisleri yeniden başlatılmalıdır. Servisi yeniden başlatmak için sunucudaki .bat uzantılı 
servisleri yeniden başlatmayı sağlayan dosya, yönetici olarak çalıştırılır.
Dikkat: bat uzantılı dosya çalıştırıldığında, sisteme giriş yapmış tüm kullanıcılar otomatik olarak çıkış
işlemi gerçekleştirilmektedir.


![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcadc67d3-4fa1-495e-8204-9548cd3a9362)