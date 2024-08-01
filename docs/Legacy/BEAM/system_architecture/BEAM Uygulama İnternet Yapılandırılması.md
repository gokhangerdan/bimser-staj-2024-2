

**DİKKAT!**

İş bu doküman ve içeriği tavsiye niteliğinde olup, internete açılmadan önce uygulama üzerinde kontrol edilmesi gereken işlemleri kapsamaktadır. Doküman içeriği ve firmanın uyguladığı güvenlik politikasına göre farklılık gösterebilir. Firma kendi şirketine ait IT güvenlik politikasını uygulamalıdır. BEAM’in çalışması için bazı ayarların farklı yapılması gerekebilir. Dokümandaki eksik ve/veya farklı bilgiden dolayı oluşabilecek durum/durumlardan Bimser Çözüm sorumlu tutulamaz.

# **BEAM Sunucusu İnternete Açılmadan Önce Yapılması Gerekenler**

Bu doküman içeriğinde BEAM bulunduğu sunucu internete açılmadan önce hangi ögelerin kontrol edilmesi gerektiği açıklanacaktır.

Kontrol edilecek olan maddeler sırası ile aşağıda belirtilmiştir. Bu maddelerin bazılarının müşteri tarafından yapılması gerekmekte olup, bu maddeler **“(Müşteri)”** ifadesi ile belirtilmiştir.

1.  Sunucu üzerinde çalışan Redis uygulamasında şifre tanımlama
2.  **(Müşteri)** Sunucu üzerinde çalışan Redis uygulamasının çalıştığı tanımlanan portun sunucu dışından erişime kapattırılması
3.  **(Müşteri)** BEAM sunucuna dış dünyadan erişim yapılabilmesi için DNS adresi kaydının tanımlanması
4.  **(Müşteri)** BEAM sunucusunda uygulama için tanımlanmış DNS adresine uygun SSL sertifikasının IIS'e yüklenmesi
5.  **(Müşteri)** Tanımlatılan yeni DNS adresinin IIS'te BEAM bulunduğu olduğu sitede https binding olarak eklenmesi, sertifika ve DNS bilgilerinin binding üzerine tanımlanması
6.  Admin şifresinin varsayılan şifre olarak bırakılmaması
7.  **(Müşteri)** Güvenlik testleri & sunucuların güvenliğinin sağlanması

## Sunucu üzerinde çalışan Redis uygulamasında şifre tanımlama

Redis uygulaması kurulduğunda, varsayılan olarak içinde şifre özelliği (requirepass) kapalı gelmektedir. Redis içindeki verilere ulaşılmasını önlemek amacı ile Redis uygulamasında şifre parametresi (requirepass) aktif hale getirilmelidir.

Aktif etmek için C:\Program Files\Redis (dizin Redis kurulumu esnasında farklılık gösterebilir) dizini içindeki **redis.windows-service.conf** dosyası açılır.

.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6c1f2869-6bfe-4588-b28e-a6a316f89711)

Dosya içinde SECURITY bölümü içinde bulunan requirepass alanına gelinir requirepass parametresinin başında bulunan kare (\#) işareti silinmelidir. İşaretin silinmesi ile şifre alanına yani foobared ifadesinin yerine kullanılması istenen şifre girilmelidir. Bu örnekte 16 karakterden oluşan alfa numerik bir şifre girilmiştir. Redis şifresi daha önceden kullanılmış ve/veya kolay tahmin edilebilen bir şifre olmamalıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb390d25c-80cc-4a53-bd66-8f8d12156c3b)

Şifre girildikten sonra **redis.windows-service.conf** dosyayı kaydedilir. Kaydetme işlemi ardından Windows servislerinde redis servisinin durdurulup, ardından başlatılması işlemi yapılmalıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadef43ffad-a938-435f-8d86-97f791c90fcd)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload06eda22b-4215-4cca-a96b-0bf34ac541a0)

1.  Redis’in çalıştığı portun dışarıdan erişime kapatılması

Redis uygulamasının çalıştığı portun bulunduğu sunucu dışından erişilmesi kapatılmalıdır. Bu işlem firmanın IT veya ilgili birimi tarafından yapılmalıdır.

Redis portunu öğrenmek için redis uygulamasının kurulu olduğu sunucuda C:\\Program Files\\Redis (dizin Redis kurulumu esnasında farklılık gösterebilir) dizini içindeki **redis.windows-service.conf** dosyası açılır.

Dosya içinde NETWORK bölümü içinde bulunan port alanına gelinerek redis’in çalıştığı port bilgisi öğrenilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade8d76f52-6988-4b8b-b96d-7a17eb385c05)

**Not:** BEAM uygulaması ve Redis uygulaması farklı sunucular üzerinde çalışıyorsa, Redis uygulamasının bulunduğu sunucuda BEAM sunucunun erişilebilmesi için istisna kuralı tanımlanmalıdır. Aynı istisna kuralı başka uygulamaların Redis’e bağlanması gerekiyorsa tanımlanabilir.

## BEAM Uygulamasına Erişim İçin DNS Kaydının Yapılması

Uygulamanın dış dünyaya açılabilmesi için BEAM’in DNS adresi tanımlaması yapılması ve bu adrese uygun olarak HTTPS üzerinden çalışması gerekmektedir.

DNS adresi tanımlaması yapılması firmanın IT veya ilgili birimi tarafından yapılmalıdır.

## DNS Adresine Uygun SSL Sertifikasının Yüklenmesi

BEAM sunucusuna erişim için gerekli DNS adresi tanımlaması yapıldıktan sonra, adresin HTTPS üzerinden çalışması için sunucuya SSL sertifikayı yüklenmelidir. İşlem firmanın IT veya ilgili birimi tarafından yapılmalıdır.

## ISS’te BEAM Uygulamasının Çalıştığı Web sitede https Binding Olarak Tanımlanması

DNS adresi tanımlaması ve IIS’e DNS adresini doğrulayacak SSL sertifikası yüklendikten sonra, BEAM’ın çalıştığı web sitesinde bulunan bindingler’de yeni https binding eklenir. Burada SSL ayarının yapılması için SSL sertifikası seçimi gibi HTTPS üzerinden çalışması için gerekecektir.

![Click Bindings](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload59995da3-1e6c-4d7d-a2dc-3a16a8b05e5b)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3d9a2466-20c4-4682-af2a-894089b2ea7f)

## Beam System Configuration Şifreleme:

BEAM uygulaması dış dünyaya açılmadan önce System configuration üzerinde bulunan alanların şifrele hale getirilmesi gerekmektedir. Bu kapsamda şifre içerikli anahtar değer lerine başına SK\_ eklentisi getirilmesi gerekmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload03e417bd-0721-488c-8887-d0bde3aa39b5)

İstenildiği takdirde sistem genelinde bir şifre gereksinimi kuralı (minimum uzunluk, büyük harf, küçük harf vb gibi) oluşturularak, kullanıcılar ilk girişlerini yaparken bu kurala uygun olarak yeni şifre oluşturmaları sağlanabilir.

## 1.7 Güvenlik Testleri & Sunucu(ların) Güvenliğinin Sağlanması

BEAM sunucusunda, Redis ayrı bir sunucuya kurulduysa Redis sunucusunda, Viewer ayrı bir sunucuya kurulduysa viewer sunucusunda, sistemin kullandığı veri tabanı ve veri tabanı sunucunun güvenliğinin sağlanmasından firmanın IT veya ilgili birimi sorumludur. Sunucuların firewall ile korunması, kimlerin nereden ve nasıl erişebileceği, DMZ gibi yapılar firma tarafından planlanmalı ve uygulanmalıdır.

Sunucular üzerinde güvenlik testi yapılması istenirse firma tarafında ilgili testler yapılmalıdır.

## 1.8 Sunucu Yapılandırması:

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcc9e039a-1f05-4bbd-ba2b-4b6bdd0565f1)
