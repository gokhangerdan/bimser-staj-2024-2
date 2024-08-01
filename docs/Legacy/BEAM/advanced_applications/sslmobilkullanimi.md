# Mobil Uygulama SSL Geçişi

2.23.3 ve sonrası paketlerde sistem parametresine yeni bir alan eklendi.Bu parametrenin değerine müşterinin bağlantı uygulama linki yazılmalıdır.
Sistem Parametresi: MobileLocalizationServicePath
Value: http://localhost/BEAM
Value değerine müşterimizin BEAM uygulaması bağlantı linki yazılmalıdır.

Eğer müşteride IIS de 80 portu kapalıysa ve mobilde hata alınırsa yani (https://....com/BEAM/service/Reportservice.svc) Servise erişim yoksa Uygulama klasörü altında www klasöründeki web configden aşağıdaki düzenlemeleri yapmanız gerekmektedir.


```<serviceMetadata httpGetEnabled="true" httpsGetEnabled="true" />
<security mode="Transport" >
<transport clientCredentialType="None"/>
</security>
```

![](https://docsbimser.blob.core.windows.net/imagecontainer/SSL%20Web%20Config-0d6ab6a9-f4b9-4f7e-a4f9-54b623cf181a.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/SSL%20Web%20Config1-3e62799b-4e92-4da9-a620-7316ce7ccec7.png)

