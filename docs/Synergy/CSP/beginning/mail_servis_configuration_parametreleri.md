# MAIL Servis Konfigürasyon Parametreleri

___

### MailService.Section-sys.CertificateCheckAlwaysCorrect:

SMTP istemcisinin sunucu sertifikası doğrulama geri çağırmasını ayarlar. Bu satırın işlevi, sunucu sertifikası doğrulamasını her zaman doğru/yanlış olarak kabul etmektir.


___

### MailService.Section-sys.DefaultProfile

Mail Servis e gelen isteklerde hangi profilin kullanılacağı belirtilmemişse bu configürasyondaki profil bilgisi varsayılan olarak kullanılır.


___

### MailService.Section-sys.TemplatePath



___

### MailService.Section-sys.Profiles

Bu Configürasyon mail servisimizin mail atarken kullanacağı mail adresleri ve bu adres için gerekli bilgilerini tutmaktadır. Örn: 



```
 "BimserSynergy-Outlook": {
		"Server": "smtp.office365.com",
		"Port": 587,
		"UserName": "synergytest@bimser.com.tr",
		"UserPassword": "sifre",
		"SecureSocketOption": 3,
		"DisplayName": "Synergy Application Test Dev",
		"OAuth2RefreshToken": "Q9RiMbT5CTGgBnY8",
		"ClientId": "2d74b95d-5c45-12a2-b0a6-3a0dd5d8f201",
		"ClientSecret": "",
		"TenantId": "3462e409-a12r-457a-8po0-8qe246c31d62",
		"OAuth2Provider": 1
}


```

 Yukarıdaki örnek Outlook Profilinde; 

### BimserSynergy-Outlook

Profilin adıdır.  İçerisinde bulunan bilgilere ulaşmak için bu ad kullanılmaktadır.

### Server

Outlook mailler için smtp server bilgisidir.

### Port

Outlook mailler için port bilgisidir.

### UserName

Mailleri atmakta kullanacağımız (maillerin hangi adresten gönderildiği) adresimiz.

### UserPassword

UserName bilgisindeki mail adresimizin şifresidir.

### SecureSocketOption

Bağlantı için kullanılması gereken SSL ve/veya TLS şifrelemesini belirtmenin bir yolunu sağlar. None,Auto,SslOnConnect,StartTls,StartTlsWhenAvailable gibi değerler alır.

### DisplayName

Bu parametreyi örnek ile açılayacağız, Örneğin Synergy Platformdan Mail geldiğini düşünelim. Bu mail adresi synergy@bimser.com.tr olsun. Gelen mail adresinde görünen adı  "synergy@bimser.com.tr" değil de "TURKCELL" şeklinde gözüküyor.

![](https://docsbimser.blob.core.windows.net/imagecontainer/DisplayName-84dbf2e7-bcac-4aa5-b3d1-eb588fd0a7aa.png)

### OAuth2RefreshToken

Oauth2 ile mail adresine login olunduğunda alınan refreshToken bilgisi (bu parametre ile işlem yapılacaksa UserPassword bilgisi girilmesine gerek yoktur.)

### ClientId

Oauth2 login için gerekli Client bilgisi

### ClientSecret

Oauth2 login için gerekli Tenant bilgisi

### TenantId

Oauth2 login için gerekli Tenant bilgisi

### OAuth2Provider

Profil bilgisinin Outlook veya Gmail mi olduğunu belirtir. 1 Outlook, 2 Gmail değerlerini alır.

___

Not: TenantId, ClientSecret, TenantId gibi bilgiler mail ayarları yapılırken size Google veya Microsoft tarafından sağlanacaktır.



___

