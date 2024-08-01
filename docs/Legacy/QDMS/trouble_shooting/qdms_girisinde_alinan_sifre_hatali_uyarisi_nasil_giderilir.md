# QDMS girişinde alınan kullanıcı adı ve şifre hatalı problemini nasıl giderilir.

## Örnek Hata

![](https://docsbimser.blob.core.windows.net/imagecontainer/hata-61afb7f1-d0d5-4e2e-8621-1f8b35c8224d.png)

### Tek bir kullanıcıda bir problem var ise aşağıdaki adımların kontrol edilmesi gerekmemektedir.

-Sistem Yöneticisi bir kullanıcı Personel Tanımlama ekranından kullanıcının aktif-pasif durumunu kontrol etmeli,

-Eğer kullanıcı aktif ise yine personel tanımlamadan değiştire tıklayarak kullanıcı logon username bilgisi LDAP-Active Directory tarafıyla karşılaştırılmalı,

-Username bigisi de doğru eşleşiyorsa, kullanıcı üzerine Active Directory tarafında LogonTo ayarı yapılmış olabilir, bu ayarın yapılmaması gerekmektedir.

-Kullanıcının active directory şifresi expired olmuş olabilir , bunun kontrolünün sağlanması gerekmektedir .

-2. , 3. ve 4 . madde için Bilgi İşlem ile iletişime geçerek kontrolleri sağlayabilirsiniz.
