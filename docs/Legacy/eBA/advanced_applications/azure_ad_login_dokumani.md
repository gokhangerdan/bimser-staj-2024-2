# eBA Azure AD ile Login

## Kurulması Gerekenler:

- Node.js
- https://aka.ms/dotnet-core-applaunch?framework=Microsoft.NETCore.App&framework_version=5.0.17&arch=x64&rid=win10-x
- https://aka.ms/dotnet-core-applaunch?framework=Microsoft.AspNetCore.App&framework_version=5.0.0&arch=x64&rid=win10-x

## Ayarlanması Gerekenler:

**eBAConfiguration**

![](https://docsbimser.blob.core.windows.net/imagecontainer/configurationManager-878eb4e3-3e44-42c8-aaed-4b82be802ce3.png)

- **Security>Ouath20** kırılımı eklenmeli.
- **BaseUrl** : Default eBA adresi tanımlanmalı.
- **Enabled** : AzureAD logini aktif eden parametre.
- **Port** : Node.js tarafında çalışacak port bilgisi.


eBAConfiguration tarafında yapılacak tanımlamalar sonrasında eBAServer.exe.config dosyasının
içeriği düzenlenmelidir.

**eBAServer.exe.config**

![](https://docsbimser.blob.core.windows.net/imagecontainer/ebaServerexeConfig-0bc68ab6-2a85-457c-9e3d-9a75e538bbe1.png)

- **eBAGRPServiceEnabled** : Arka planda çalışacak servisi aktif eden parametre.
- **eBAWebAddress** : eBAConfiguration Web kısmındaki url bilgisi.
- **ValidaterPayload** : Buradaki değer email olarak sabit. ExternalUsername bilgisini bu
    değer üzerinden alıyoruz.
- **ValidaterValidAudiences** : ClientID bilgisi.
- **eBAGrpcServicePort** : Grpc servisin çalışacağı port bilgisi. Sistemde kullanılmayan bir
    port tanımlanabilir.
- **eBAOAUTH20PORT** : Azure tarafında tanımlanmış port.
- **AuthJSPath** : eBA dizininde authentication-oath\synergy-auth klasörü içindeki app.js
    yolu verilmeli. (C:\BimserCozum\authentication-oath\synergy-auth\app.js)

**AuthVariables** :

INTERNALAPISERVICEADDRESS= **localhost:50052** |OAUTH20_PORT= **4006** |OAUTH20_URL= **[http:/](http:/)
/localhost:4006** |OAUTH20_AUTHORIZEURL=https://login.microsoftonline.com/ **3462e409-
ac7a-457a-
8bd0**************** /oauth2/v2.0/authorize|OAUTH20_TOKENURL=https://login.microsofton
line.com/ **3462e409-*************** /oauth2/v2.0/token|OAUTH20_CLIENTID= **168d55bf-83c6-
************** |OAUTH20_CLIENTSECRET= **XKc8Q~u2urzy78LPO67JV~************** |OAUTH
_SCOPE=openid profile email user.read|OAUTH20_SCOPESEPARATOR=
|OAUTH20_USERPROFILEURL=https://graph.microsoft.com/v1.0/me|OAUTH20_ENABLED=true|CERTIFICATE_FILE_PATH=C:\SSL\fullchain.pem|PRIVATEKEY_FILE_PATH=C:\SSL\server.key
"/>

- Configte pem ve key dosyaları bulunmaktadır. Bu dosyalar ilgili dizine atılmalıdır.(Örnekte C:\SSL\ dizinindedir) Azure AD login'in SSL ile uyumlu çalışabilmesi için bu dosyalar gereklidir.

- Authvariables kısmı bir bütün olarak yer alıyor. Değişiklik yapılması gereken yerleri
    renklendirdim.
- **ClientID** ve **ClientSecret** haricinde **YEŞİL** renklendirdiğim kısım TenantID değeri.
    Müşterilerin azure ortamına tanımlı olan tenantID bilgisinin bu kısımlara girilmesi
    gerekiyor.


## SystemManager:

- Örneğin adogru@bimser.com hesabı olan bir kullanıcı için ilgili kullanıcının
    externalusername bilgisine adogru değeri girilmelidir.

## Kullanımı:

![](https://docsbimser.blob.core.windows.net/imagecontainer/AzureAdLogin-3dc6ce0a-6bb7-47cb-b067-9607778ea5fe.png)

- Ayarlamalar yapıltıktan sonra eBA login ekranında Azure AD giriş butonu görünür hale gelir.

- Tıklandığında microsoft login ekranına yönlendirilir ve kullanıcı login olduktan sonra otomatik olarak ilgili kullanıcıya login edilir.


## Dikkat Edilmesi Gerekenler:

- eBAGRPService in çalıştığını gözlemlemek için TaskManager > Details kısmına bakılabilir.

 Bu servis eBA servisleriyle beraber ayağa kalkan bir servis.

![](https://docsbimser.blob.core.windows.net/imagecontainer/grpcService-4b7ca80c-780e-466c-89ef-d2ff9c7a0a66.png)

- Azure ile login işlemi gerçekleştirildikten sonra kullanıcıya login olunması yerine
    tekrardan login ekranına yönlendiriliyorsa aşağıdaki ayar yapılmalıdır.

eba.net > Web.config dosyası içeriğindeki SessionState kısmında “cookieSameSite="Strict"
şeklinde yer alan değeri **Lax** olarak değiştirerek testler gerçekleştirilebilir.

- Bunun dışında tespit edilemeyen bir hata ile karşılaşıldığında Windows > Event Viewer
    kısmı incelenebilir.


