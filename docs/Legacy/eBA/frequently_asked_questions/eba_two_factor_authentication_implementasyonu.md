# eBA Mobil Uygulamada 2FA Kullanılabilir mi?

eBA Mobil uygulamasına kullanıcı girişi yapılırken Google 2FA altyapısı kullanılmak istendiğinde aşağıdaki yönergelerin takip edilmesi gerekmektedir.

### 1)	Sunucu Tarafında Yapılacaklar

-	eBA güncel sürümlerinde geçerlidir. 
-	eBAConfiguration Editor > Advanced > Security tabına aşağıda belirtilen anahtarlar eklenmeli.
-	CustomMFA alanı oluşturulmalı ve MFAMode bilgisi Google olarak belirlenmelidir.


![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload01be9893-ba4a-4188-8a8f-988da40a3f7f)

-	eBA Arayüzü > Doküman Yönetimi > system/settings/2FA mail templates klasörlerinde Turkish.txt ve English.txt dosyaları bulunmalı. Bu dosyalar ilgili setup/update dosyalarıyla birlikte gelmekte.
-	eBA System Manager üzerinden Multi Factor Authentication Enable  ve Multi Factor Auth Activated adında Resim 2’de belirtilen özellikler tanımlanmalıdır. Bu özellik tanımlandıktan sonra Kullanıcı Özelliği olarak seçilmelidir.


![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9b701c99-5102-4dee-97cc-46b961713b0b)

eBA System Manager > Property Definitions > Properties 

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7f2c371f-a979-427c-9d45-7876813952eb)

MultiFactorAuthEnable işlemlerin aktif olması için gereken özelliktir. 
MultiFactorAuthActivate ise kullanıcı için barcode bilgilerini içeren mail işlemleri için gereklidir.
Bu özellik ayarların yapıldığı anda pasif durumda olmalıdır. Tüm ayarlar yapıldıktan sonra kullanıcı login işlemini gerçekleştirmek istediğinde barcode bilgilerinin olduğu bir mail alır.
Mail kullanıcıya iletildiği anda bu özellik otomatik olarak aktif duruma geçer ve her giriş anında mail atılması engellenir.
Eğer kullanıcıya tekrar mail gitmesi isteniyorsa bu özellik System Manager da kullanıcı ayarlarında pasife çekilmelidir.(Hesap Sıfırlama/Kurtarma işlemlerinde detaylı bilgi mevcut)


![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload84715e2f-ea6b-4836-bc55-0542b8126071)

### 2)	İstemci Tarafında Yapılacaklar

-	Google Play ve/veya Apple Store platformlarından indirilebilen eBA Mobil uygulamasının güncel versiyonu mobil cihazda yüklü olmalı.
-	Yine aynı platformlardan indirilebilen Google Authenticator uygulaması mobil cihazda yüklü olmalı.


### 3)	Örnek Kullanım Senaryosu

Mobil cihazından eBA’ya giriş yapmaya çalışan kullanıcıya 2FA Doğrulama Anahtarı sorulur. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc0a7bce5-a621-4cbb-8391-90bcdbfae1a5)

İlk giriş anında bu kodu kullanabilmek için, kullanıcının mail adresine gönderilen QR kodu mobil cihazına yüklediği Google Authenticator uygulamasına taratması gerekmektedir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcf44c2c0-24cf-426e-9b0e-be51676b70d7)

Tarattığı bu QR kod sayesinde Google Authenticator uygulaması periyodik zaman aşımlarıyla Doğrulama Anahtarları türetecektir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb6bb3fa4-cfe4-4a23-af5e-dacd9f54f222)

Mobil cihazından eBA’ya giriş yapmaya çalışan kullanıcı o anki doğrulama anahtarını kullanarak eBA’ya giriş yapmış olur.

### 4)	Hesap Sıfırlama/Kurtarma

Kullanıcı Google Authenticator uygulamasını cihazından silerse, cihazını değiştirirse vb. QR kodu okutarak tanımladığı anahtarı kaybettiği herhangi bir durumda, hesabı için oluşturulan QR kodu tekrar tanımlayabilmek için ilk gönderilen maili saklıyorsa onu kullanabilir. 
Maili saklamadıysa, sistemin tekrar mail ile QR kodu göndermesi için; eBA System Manager üzerinden kullanıcı için tanımlı olan Multi Factor Auth Activated özelliğinin işareti kaldırılarak, kullanıcının ilk giriş denemesinde tekrar mail gönderilir.

eBA System Manager > Organization Management > Users > User Details


![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaf68563c-8977-4567-a8fb-3125f35b0edd)