# eBA HTTP-SSL Konfigürasyonu

eBA adresine Https linki üzerinden erişebilmek için öncelikli olarak müşterimizin IT birimi tarafından SSL seritifikası IIS'e eklenmelidir.
İlgili SSL sertifikanın yüklendiğine emin olmak için aşağıdaki görsellerde yer alan alanları kontrol edebilirsiniz.

![](https://docsbimser.blob.core.windows.net/imagecontainer/SSL3-c29cdec4-95c4-4f8b-95ba-ed1fbbd35700.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/SSL1-f12dee23-504c-4217-bd3b-3b8594341d26.png)

Bu alanlara ek olarak Server Certificate alanında ilgili SSL sertifikanın içerisinde  sertifikanın doğrulandığını teyid etmeniz gerekmektedir

### eBA Tarafında yapılacak işlemler:

eBAConfigurationEditor.exe>Web kırılımı altında Root URL ve URL alanları yeni Https'li link ile değiştirilmelidir

![](https://docsbimser.blob.core.windows.net/imagecontainer/SSl4-38fff3e7-6558-47e0-8e21-c23e4ece69cb.png)

Advanced>Config>WH keyinin value değerine ilgili Https'li link ile değiştirilmelidirörn:https://abctestxyz.com/eba.net.dm

![](https://docsbimser.blob.core.windows.net/imagecontainer/SSL5-fae1366d-5e4e-48f2-94bc-ee5097f6f6f6.png)

Advanced>DocumentManagement>Default > WebServiceAddress keyinin value değerine  ilgili Https'li link ile değiştirilmelidir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/ssl6-70fe7a88-9265-44f4-ac15-db45d11e7fc4.png)

Advanced>Web>SSL key'inin değeri "true" olarak değiştirilmeli ardından File>Save diyerek ilgili değişiklikler kaydedilmelidir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/ssl8-b197c0b2-eed3-41d9-a6f6-c20616435c0f.png)

Bu işlemlerden sonra BimserViewer ,BimserViewerService ve 
eBA Döküman Yönetimi>system/settings/dm altında bulunan viewers.config dosyaları Https'li olarak değiştirilmelidir.


Tüm bu işlemlerin ardından eBA Servislerini ve IIS'i yeniden başlatarak sisteminize Https'li link üzerinden erişebilirsiniz.



