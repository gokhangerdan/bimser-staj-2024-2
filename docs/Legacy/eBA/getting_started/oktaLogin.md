# Okta ile Login işlemi

![](https://docsbimser.blob.core.windows.net/imagecontainer/1-5196f1c0-0723-4ff8-9625-8e9865dea01e.png)
İlk olarak Okta bilgileri configuration kısmında tanımlanarak girilmelidir.
**ClientId** : Okta projesi oluşturulduğunda oluşan ClientId bilgisi.
**ClientSecret** : Okta projesi oluşturulduğunda oluşan ClientSecret bilgisi.
**Enable** : Okta ile login için butonun aktif-pasif edilme durumu.
**Okta Domain** : Müşteriye ait okta domain bilgisi.
**Redirect Url** : [https://localhost/eba.net](https://localhost/eba.net)
**SsoEnable** : Sso nun aktif-pasif edilme durumu.



![](https://docsbimser.blob.core.windows.net/imagecontainer/2-2510db3d-8fef-4b0a-8147-e56c64ecefb0.png)
- Müşterinin okta hesabında oluşturduğu uygulamadaki **ClientId** – **Client Secret **– **Domain** bilgileri bu sayfadan alınması gerekmektedir. Müşteriden bu bilgiler talep edilebilir.





![](https://docsbimser.blob.core.windows.net/imagecontainer/3-78b3c76a-816b-4051-b7f7-8ea37fba9734.png)
- Yine oluşturulan uygulama ayarlarında İmplict ( Hybrid) seçilerek IdToken ve AccessToken izinleri verilmelidir.
- Alt kısımda yer alan login işlemlerinde redirect url bilgilerine [https://localhost/eba.net/Default.aspx](https://localhost/eba.net/Default.aspx) bilgisi geçilmelidir.
- Bu işlemler müşteriye iletilerek bilgilerin eklenmesi sağlanabilir.



![](https://docsbimser.blob.core.windows.net/imagecontainer/4-b800f68f-c8c8-469c-920d-cba79f1ce13f.png)
- Tüm ayarlar yapıldıktan sonra login aşamasında Okta ile giriş butonu aktif olur.
- Okta ile giriş penceresi açılır ve kullanıcı okta bilgilerini girerek login işlemini gerçekleştirebilir.
- Kullanıcının okta mail bilgisiyle login olabilmesi için eBA kullanıcısında ExternalUsername olarak Okta mail adresi tanımlanmalıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5-d73f09cc-d1d7-4969-852e-65c44524c16f.png)
