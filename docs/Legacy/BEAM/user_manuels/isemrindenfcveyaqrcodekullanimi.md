# İş Emrinde NFC veya QR code Kullanımı

## İçerik

1. Giriş

	1.1. Amaç 

2. Kullanımı

	2.1. Tanımlayıcılar 

                2.1.1. NFC veya QR Code Tanımlamaları

		2.1.2. Tüm İş Emirleri ve Kullanıcılar İçin NFC veya QR Code Kullanımı

		2.1.3. Kullanıcı Bazlı NFC veya QR Code Kullanımı 

		2.1.4. İş Emri Türü Bazlı NFC veya QR Code Kullanımı

## 1. Giriş

### 1.1 Amaç

NFC veya QR Code ile takip özelliğimiz sayesinde dağınık yapıya sahip ekipmanlara ve ekiplere sahip olan müşterilerimizin işleyişlerini kolaylaştırmak adına eklediğimiz özelliklerden biridir. Ekipmanların üzerinde NFC Tag veya QR Code etiketlenmesi yapılmış ise ilgili personel ekipmanın yanına geldiği zaman ilgili Tag’ı veya Code'u okutmadan ilgili ekipman üzerinde işlem yapmaya başlayamaz ve işlem bitiminde yine aynı işleyişe göre ilgili Tag’ı veya Code'u okutmadan ilgili iş emrini tamamlayamaz.
Bu da sistem üzerinden ekipman yanına gitmeden masa başında bakım yapılarak ilgili iş emirlerinin kapatılmasını engellemektedir.


## 2. Kullanımı

### 2.1 Tanımlamalar

2.1.1. NFC veya QR Code Tanımlamaları:

Beam ana menü “Sistem” modülü içerisinde “Sistem Parametreleri” sayfasına giriş yapılır. Ekle denilerek Anahtar Değeri alanına “Workorderassetvalidationmode” parametresi eklenir. Değer alanına NFC, QR veya boş olarak bir değer atanır.


![](https://docsbimser.blob.core.windows.net/imagecontainer/NFC1-aa7188da-cc35-4c31-90b8-683baeb0818d.png)

Workorderassetvalidationmode parametresi değeri QR olarak seçilir ise BEAM Mobil uygulamasında İş emirleri sayfasında ilgili iş emrinin üzerinde long press basıldığında açılan popup içerisindeki Başladım- Tamamladım-Devreye Aldım seçeneklerinden biri seçildiğinde kamera açılarak ilgili ekipman üzerindeki QR Code okutulması gerekmektedir.

Workorderassetvalidationmode parametresi değeri NFC olarak seçilir ise BEAM Mobil uygulamasında İş emirleri sayfasında ilgili iş emrinin üzerinde long press basıldığında açılan popup içerisindeki Başladım- Tamamladım-Devreye Aldım seçeneklerinden biri seçildiğinde NFC Tag okutulması gerekmektedir.

Workorderassetvalidationmode parametresi değeri boş olarak seçilir ise BEAM Mobil uygulamasında İş emirleri sayfasında ilgili iş emrinin üzerinde long press basıldığında açılan popup içerisindeki Başladım- Tamamladım-Devreye Aldım seçeneklerinden biri seçildiğinde eski çalışma şeklinde devam etmektedir.

2.1.2 Tüm İş Emirleri ve Kullanıcılar İçin NFC veya QR Code Kullanımı

BEAM ana menüden Bakım Yönetimi→Tanımlamalar→İş Emri Türleri→Diğer Bilgiler içerisindeki “İş Emri Bakım Durumu Değiştirilirken NFC veya QR Code Kullanımı Yapamaz.” seçeneği işaretlenmemelidir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/NFC2-dc189ea3-6258-4063-999b-a3a1fb135f9e.png)

BEAM ana menüden Sistem→Kullanıcılar→Kullanıcı Parametreleri içerisindeki İş Emri Bakım Durumu Değiştirilirken NFC veya QR Code Kullanımı Yapamaz” seçeneği işaretlenmemelidir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/NFC3-4080d957-6e1a-4e21-92ad-2c069d068711.png)

Bu kullanım modeli seçilmesi durumda Mobil uygulama üzerinden İş Emirlerine sayfasına gelindiğinde ilgili İş Emri üzerinde Uzun Basılıp (Long Press) çıkan pencerede “Başladım – Tamamladım – Devreye Aldım seçeneklerinden biri seçildiğinde sisteme giriş yapan kullanıcı için NFC veya QR Code açılacaktır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/NFC4-ac09061a-5acb-4533-9a01-756b5b6ce32c.png)

2.1.3. Kullanıcı Bazlı NFC veya QR Code Kullanımı

BEAM ana menüden Bakım Yönetimi→Tanımlamalar→İş Emri Türleri→Diğer Bilgiler içerisindeki “İş Emri Bakım Durumu Değiştirilirken NFC veya QR Code Kullanımı Yapamaz.” seçeneği işaretlenmemelidir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/NFC5-4c813ae7-6405-40df-9d2f-437cc3006e59.png)

BEAM ana menüden Sistem→Kullanıcılar→Kullanıcı Parametreleri içerisindeki İş Emri Bakım Durumu Değiştirilirken NFC veya QR Code Kullanımı Yapamaz” seçeneği işaretlenmelidir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/NFC7-6b3b4b1a-abe3-40c9-b0d4-1589c1d60580.png)

Bu kullanım modeli seçilmesi durumda Mobil uygulama üzerinden İş Emirlerine sayfasına gelindiğinde ilgili İş Emri üzerinde Uzun Basılıp (Long Press) çıkan pencerede “Başladım – Tamamladım – Devreye Aldım seçeneklerinden biri seçildiğinde sisteme giriş yapan kullanıcı için NFC veya QR Code açılmayacaktır. İş emrine direk olarak Başladım – Tamamladım – Devreye Aldım yapılabilecektir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/NFC8-a601ab81-4834-41a7-bd50-9064128465a2.png)

NOT:
a) Sistem > Sistem Parametrelerine Workorderassetvalidationmode Parametresi Eklenir QR Veya NFC Değerleri Girilir.
b) Web Uygulaması Yan Menüsünden Bakım Yönetimi > Tanımlar > İş Emri Türleri > Diğer Bilgiler > İş Emri Bakım Durumu Değiştirilirken NFC Ve QR
Kod Kullanımı Yapamaz İşaretlenir.
c) Web Uygulaması Yan Menüsünden Sistem Kullanıcılar > Kullanıcı Parametreleri > İş Emri Bakım Durumu Değiştirilirken NFC Ve QR Kod Kullanımı
Yapamaz İşaretlenir.
**Bu Tarz Kullanımda Kullanıcı Üzerindeki Parametre İş Emri Türü Parametresini Etkisiz Kalcaktır. Mobil Uygulama Üzerinden İş Emirlerine Gelindiğinde İlgili İş Emri Üzerine Uzun Basılıp (Long Press) Yapılıp Başladım – Tamamladım – Devreye Aldım İşlemleri Yapılmak İstendiğinde İlgili Kullanıcı İçin NFC Veya QR Açılmayacaktır. İş Emrine Direk Olarak Başladım – Tamamladım – Devreye Aldım Yapılabilecektir.

