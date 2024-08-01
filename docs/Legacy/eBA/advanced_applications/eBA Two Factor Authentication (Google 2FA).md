# eBA Two Factor Authentication (Google 2FA) İmplementasyonu
eBA Mobil uygulamasına kullanıcı girişi yapılırken Google 2FA altyapısı kullanılmak istendiğinde aşağıdaki yönergelerin takip edilmesi gerekmektedir.
## Sunucu Tarafında Yapılacaklar
- eBA güncel sürümlerinde geçerlidir. 
- eBAConfiguration Editor > Advanced > Security tabına aşağıda belirtilen anahtarlar eklenmeli.

CustomMFA alanı oluşturulmalı ve MFAMode bilgisi Google olarak belirlenmelidir.
![](https://docsbimser.blob.core.windows.net/imagecontainer/1-96484903-21e7-47c6-89aa-428b3d78f582.png)
Resim 1 eBA Configuration Editor Yapılandırması
- eBA Arayüzü > Doküman Yönetimi > system/settings/2FA mail templates klasörlerinde Turkish.txt ve English.txt dosyaları bulunmalı. Bu dosyalar ilgili setup/update dosyalarıyla birlikte gelmekte.

eBA System Manager üzerinden **Multi Factor Authentication Enable  ve Multi Factor Auth Activated **adında Resim 2’de belirtilen özellikler tanımlanmalıdır. Bu özellik tanımlandıktan sonra Kullanıcı Özelliği olarak seçilmelidir.
![](https://docsbimser.blob.core.windows.net/imagecontainer/2-9b0a8377-a6f2-42e3-96e3-37f67bd4483a.png)
Resim 2 Kullanıcı Özelliği Tanımlama

eBA System Manager > Property Definitions > Properties 

![](https://docsbimser.blob.core.windows.net/imagecontainer/3-852decf2-0c3e-4556-8ee1-8d54b6f0d262.png)

**MultiFactorAuthEnable** işlemlerin aktif olması için gereken özelliktir. 
**MultiFactorAuthActivated **ise kullanıcı için barcode bilgilerini içeren mail işlemleri için gereklidir.
Bu özellik ayarların yapıldığı anda pasif durumda olmalıdır. Tüm ayarlar yapıldıktan sonra kullanıcı login işlemini gerçekleştirmek istediğinde barcode bilgilerinin olduğu bir mail alır.
Mail kullanıcıya iletildiği anda bu özellik otomatik olarak aktif duruma geçer ve her giriş anında mail atılması engellenir.
Eğer kullanıcıya tekrar mail gitmesi isteniyorsa bu özellik System Manager da kullanıcı ayarlarında pasife çekilmelidir.(Hesap Sıfırlama/Kurtarma işlemlerinde detaylı bilgi mevcut)

![](https://docsbimser.blob.core.windows.net/imagecontainer/4-6d8c31ff-9780-4855-80f1-d67e9075fa40.png)

Resim 3 SystemManager kurulum ayarları.

## İstemci Tarafında Yapılacaklar
- Google Play ve/veya Apple Store platformlarından indirilebilen eBA Mobil uygulamasının güncel versiyonu mobil cihazda yüklü olmalı.
- Yine aynı platformlardan indirilebilen Google Authenticator uygulaması mobil cihazda yüklü olmalı.

## Örnek Kullanım Senaryosu
Mobil cihazından eBA’ya giriş yapmaya çalışan kullanıcıya 2FA Doğrulama Anahtarı sorulur. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5-3fb26333-057e-496e-a225-0ac4236c3d62.png)

Resim 4 eBA Mobil Arayüz
İlk giriş anında bu kodu kullanabilmek için, kullanıcının mail adresine gönderilen QR kodu mobil cihazına yüklediği Google Authenticator uygulamasına taratması gerekmektedir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/6-be548d14-2a43-4235-8df8-290b55827af2.png)

Resim 5 Gelen Mail İçeriği
Tarattığı bu QR kod sayesinde Google Authenticator uygulaması periyodik zaman aşımlarıyla Doğrulama Anahtarları türetecektir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/7-4f338df9-5960-453b-81e4-62b521f8e11a.png)

Resim 6 Üretilen Doğrulama Anahtarı
Mobil cihazından eBA’ya giriş yapmaya çalışan kullanıcı o anki doğrulama anahtarını kullanarak eBA’ya giriş yapmış olur.
## Hesap Sıfırlama/Kurtarma
Kullanıcı Google Authenticator uygulamasını cihazından silerse, cihazını değiştirirse vb. QR kodu okutarak tanımladığı anahtarı kaybettiği herhangi bir durumda, hesabı için oluşturulan QR kodu tekrar tanımlayabilmek için ilk gönderilen maili saklıyorsa onu kullanabilir. 
Maili saklamadıysa, sistemin tekrar mail ile QR kodu göndermesi için; eBA System Manager üzerinden kullanıcı için tanımlı olan **Multi Factor Auth Activated** özelliğinin işareti kaldırılarak, kullanıcının ilk giriş denemesinde tekrar mail gönderilir.
eBA System Manager > Organization Management > Users > User Details

![](https://docsbimser.blob.core.windows.net/imagecontainer/8-a098f246-b80e-4d56-9aed-ff44265b480c.png)
