# DSClient application is not found hatası ve çözüm önerileri

![](https://docsbimser.blob.core.windows.net/imagecontainer/DsClientHata-eef3cef1-6d5a-4a9b-89be-11b3b9d0f200.png)

Dsclient ekranında E-imzalama işlemi yapılacakken görüntülenen bu hatanın birden fazla sebebi olabilir.

Bu hatanın çözümü için öncelikle ,
E-imza atılmaya çalışılan Bilgisayarda/Sunucuda Dsclient.exe çalışıyormu  kontrol edilmeli.
Ardından aşşağıdaki linkte ilettiğimiz alanlar eksiksiz olarak kurulumu sağlanmışmıdır kontrol edilmelidir.


https://docs.bimser.net/docs/Others/DIGITALSIGNATURE/Kurulum/Windows_installation
https://docs.bimser.net/docs/Others/DIGITALSIGNATURE/Kurulum/Macos_installation
https://docs.bimser.net/docs/category/linux-kurulum


İlgili uygulamaların ve DSclientin kurulumunda ve çalışmasında problem yok ise aşağıdaki şekilde çözüm sağlanabilir

Genellikle eBA Version güncelleştirmelerinden sonra alınan bu hata eba.net>web.config dosyasının içerisindeki content  security policy alanının değişmesiyle oluşmaktadır.
Problemin çözümü için eba.net>web.config  içerisindeki content  security policy kısımını




```
<add name="Content-Security-Policy" value="default-src 'self' http://localhost:3638; style-src 'self' 'unsafe-inline'; script-src 'self' 'unsafe-inline' 'unsafe-eval'; img-src 'self' data:" />
```

yukarıdaki şekilde düzenleyiniz eğer düzelmez ise content  security policy kısımını
  açıklama satırına alınarak  problemin çözümünü sağlayabilirsiniz.

![](https://docsbimser.blob.core.windows.net/imagecontainer/cozum-0b36c481-0b71-450a-a248-a8155900c391.png)

