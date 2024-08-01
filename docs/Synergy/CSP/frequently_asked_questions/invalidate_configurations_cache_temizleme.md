# InvalidateConfigurationsCache Temizleme

CONFİGURATIONS tablosunda yapılan bir değişikliklerde postman üzerinden config cache temizleme ile sunucu restartı olmadan değişiklik yapabilirsiniz.

## Config cache temizleme işlemleri:

1) https://dnsadresi/api/web/cache/InvalidateConfigurationsCache
2) Authorization bölümüne bearer tokenı girilmelidir. Başındaki "Bearer" silinmelidir.
3) Headers alanına Bimser-Encrypted-Data ve Bimser-Language keyleri eklenerek value değerleri yazılır. 
4) Body kısmını tip olarak json seçip {} şeklinde boş gönderiniz.

Not: bearer tokenını ve headers alanına girilecek key value değerlerini csp sayfasına giriş yaptıktan sonra konsol ekranından ekte iletmiş olduğum görseldeki gibi alabilirsiniz. 


![](https://docsbimser.blob.core.windows.net/imagecontainer/c1-ee649738-8a2d-47e5-ab68-5c669139e4c2.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/c2-58996667-41a5-4e07-9cc4-285f1894f809.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/c3-34a86269-06d1-4d80-88b1-6fbe699aa612.png)