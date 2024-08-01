# Custom Login

## eBA uygulamasına giriş yapılırken istenilen validasyonları ve işlemleri yapabilmeye olanak sağlayan custom login özelliği bulunmaktadır.

eBA login esnasında hazırlanan bir dll'deki metod sayesinde, login olmaya çalışan kullanıcını için bazı şartlara göre login olabilmesini sağlar.
Örneğin kullanıcı id yerine mail adresi ile giriş yapmak için de bu işlemler uygulanabilir, alınan mail adresi değeri osusers'da karşılaştırılarak şifre doğruysa true döndürülebilir.

___

Burada önemli olan husus kullanıcı tanımlarında ExternalUsername bilgisinin esas alınıyor olmasıdır.

___

eBA uygulamasının konfigurasyonlarının yapıldığı eBAConfigurationEditor içerisindeki 'Advanced' sekmesinde solda yer alan "Security" altında gerekli tanımlamlar yapılmalıdır.

```
<Security>
    <key name="AuthenticationMode">custom</key>
    <key name="AuthenticationType">DLL</key>
    <AuthenticationDLL>
        <key name="Path">C:\BimserCozum\eBA\Common\eBACustomAuthentication.dll</key>
        <key name="TypeName">eBACustomAuthentication.Authentication</key>
    </AuthenticationDLL>
    <key name="LoginMode">external</key>
    <key name="ExternalUserMatch">equal</key>
</Security>
```

![](https://docsbimser.blob.core.windows.net/imagecontainer/Security-5bb0ffdc-e7aa-4aad-8ecd-bafe2a9c9abb.png)

eBAConfigurationEditor içerisinde Security altında yapılan tanımlarda hazırlanan harici DLL'in dosya yolu ve ismi gibi tanımlamalar yapılmıştır. Bu örnekte DLL kullanılacak metod ismi Authenticate olarak yer almaktadır.

Authenticate metodu kullanıcı login yapıldığında çağrılır. Amaç login esnasında bazı şartlara uygun olarak giriş yapıp yapamayacağını kontrol etmek yani validasyon yapmaktır.
Bu metod içerisinde dilediğiniz kontrolü yaptırabilirsiniz. true değeri döndürdüğünüzde kullanıcı login olurken, false değeri döndürdüğünüz durumda login olamayacaktır.


___

Hazırlanması gereken harici DLL için örnek;

```
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace eBACustomAuthentication
{
    public class Authentication : eBAAuthenticationInterface.IeBAAuthentication
    {
        public bool Authenticate(string userid, string password)
        {
            //referanslardaki eBAAuthenticationInterface dll i eba.net\common dizininde bulunmaktadır. 
            //Kendi server ınızdaki dll i referans olarak göstermelisiniz.
            if (userid == "adogru" && password == "0")
            {
                return true;
            }
            else if (userid == "hkar" && password == "0")
            {
                return true;
            }
            else if (userid == "okara@bimser.com.tr" && password == "0")
            {
                userid = "hkar";
                return true;
            }
            else
            {
                return false;
            }
        }
    }
}
```

