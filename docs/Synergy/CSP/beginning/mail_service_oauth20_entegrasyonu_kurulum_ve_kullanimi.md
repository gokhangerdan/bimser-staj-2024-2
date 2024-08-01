# Mail Servis

Mail Servis uygulamasının çalışabilmesi için konfigurasyon ayarları mevcuttur. Bu ayarlar temelde 2 başlık altında toplanabilir. 

### Oauth2.0 Login Uygulaması ve  Parametreleri 

Oauth2.0  ile çalışabilmesi için OauthLogin uygulamasından giriş yapılması gerekmektedir. Bu Uygulama da bazı parametreler almaktadır. Uygulamanın parametreleri aşağıdaki gibidir.

```
{
  "ms": {
    "instance": "https://login.microsoftonline.com/",
    "clientId": "",
    "tenantId": "",
    "redirectUri": "https://localhost:7149/sample-oauth2/get-token",
    "scopes": [
      "email",
      "offline_access",
      "https://outlook.office.com/SMTP.Send",
      "https://outlook.office.com/IMAP.AccessAsUser.All",
      "https://outlook.office.com/POP.AccessAsUser.All",
      "https://outlook.office.com/EWS.AccessAsUser.All"
    ]
  },
  "google": {
    "clientId": "",
    "clientSecret": "",
    "userId": "ornekmail@gmail.com",
    "scopes": [
      "https://mail.google.com/"
    ]
  }
}
```

MS

Json da bulunan MS parametresi Microsoft u temsil etmektedir ve içerindeki değerler Outlook' için gerekli değerleri alır. Bu değerlerden clientId, tenantId lerin değiştirilmesi yeterlidir. Diğer Parametreler değiştirilebilir (redirectUri) hariç fakat buna ihtiyaç yoktur.
ClientId ve TenantId bilgilerini https://portal.azure.com/ üzerinden gerekli ayarları yapıp sağlayabilirsiniz.

![](https://docsbimser.blob.core.windows.net/imagecontainer/AzureBilgileri-80c70f38-d7b8-4843-bd0e-cf4f6d221bad.png)

Google

Json da bulunan Google parametresi içerindeki değerler Gmail' için gerekli değerleri alır. Bu değerlerden clientId, tenantId, userId lerin değiştirilmesi yeterlidir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/Google-f1d1560f-bd1e-4004-a324-f205a64b00d3.png)

OauthLogin Uygulaması için gerekli parametreler yukarıdaki gibi doldurulduktan sonra uygulama çalıştırılır.

### OauthLogin Uygulaması

Uygulama açıldıktan sonra aşağıdaki gibi bir ekran gelecektir. Bu ekranda hangi mailservisi için (outlook,gmail) giriş yapılacağı seçilecektir ve ardından oluşan RefreshTokenlar ConfigurationTablosuna veya Configuration Manager Uygulamasına eklenecektir. Uygulama içi görseller ve Örnek RefreshToken aşağıdaki görseldeki gibidir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/Uygulama-f25c539c-a5c7-472c-9d17-bad7576ab7f8.png)

Login With Microsoft seçildiğinde aşağıdaki gibi bir URL' i tarayıcınız yapıştırmanız ve ardından tarayıcıdan izinleri vermeniz gerekmektedir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/MS-126605d8-ac08-4e9b-9298-47ae7c5d1eb7.png)

İşlemler başarılı olduğu durumda Tarayıcı True değeri dönecek ve görseldeki gibi RefreshToken Bilgisini almış olacağız.

![](https://docsbimser.blob.core.windows.net/imagecontainer/MS-Token-be02ef1d-99e0-4ec8-bd42-39a1efd0694d.png)

Eğer Login With Google seçeneği seçilmişse tarayıcı otomatik olarak açılacak ve yine yukarıdaki görseldeki gibi refreshToken bilgisini console ekranına yazacaktır.

### Mail Servis Parametreleri ve Refresh Tokenların Kullanımı

Yukarıda aldığımız refreshTokenları ConfigurationManager veya Configuration tablolarımızda MailServis için oluşturulmuş Configlere  (OAuth2RefreshToken parametresi) eklememiz gerekecektir.  Bu Config detayları "Mail Servis - Configuration Parametreleri" dokumanında açıklanmıştır. 

## Basic Authentication

Basic Authentication için yapmamız gereken ayar sadece UserName ve UserPassword alanlarını girmek olacaktır. OAuth2RefreshToken, ClientId, ClientSecret, TenantId bilgileri boş bırakılabilir. 

Not: MailServis uygulaması öncelikle UserPassword parametreleri kontrol etmektedir. Bu parametreler boş ise daha sonra Oauth2.0 için gerekli olan OAuth2RefreshToken, ClientId, ClientSecret, TenantId gibi parametrelere bakmaktadır. Kısaca Oatuh2.0 ile çalışmak istiyorsanız UserPassword bilgisini boş bırakmanız gerekmektedir.

