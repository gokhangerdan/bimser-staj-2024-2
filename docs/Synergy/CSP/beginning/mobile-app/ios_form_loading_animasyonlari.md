# CSP iOS Uygulamamızda Form Ekranlarında Loading Animasyonu Yönetimi Hk.

CSP iOS uygulamamızda form ekranlarında 2 adet loading animasyonu bulunmakta. Bu animasyonların bir tanesi ekranı kilitlerken kullanıcı aksiyonlarını engeller, diğeri de ekranı kilitlemez ve kullanıcı aksiyonlarına izin verir.

### 1- Ekranı Kilitlemeyen Loading Animasyonu

Formdaki nesnelerin yüklenmesi esnasında çalışır. Bu aşamada ekranın kilitlenmeme sebebi; kullanıcının yanlış bir form açmış olabileceği ve formun yüklenmesini beklemeden sayfadan çıkış işlemini gerçekleştirebilmesi için tasarlanmıştır. Burada kullanıcı geri butonuna basarak bir önceki sayfaya formun yüklenmesini beklemeden geri dönebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/Ekranı%20Kilitlemeyen%20Loading%20Animasyonu-01416759-2da1-4746-9350-f1b559970635.png)

### 2- Ekranı Kilitleyen Loading Animasyonu

İhtiyaca göre web tarafından toggleLoading methodu ile tetiklenir ya da uygulama içinde belirlenmiş bölümlerde otomatik olarak çalışır. Veri alış-verişi sırasında olası hataları engellemek için tüm ekran kilitlenir, kullanıcı herhangi bir aksiyon alamaz. Zaman aşımı yaşandığında animasyonun sonlandırılabilmesi için 30 saniye geçtikten sonra ekranın sağ üst bölümünde bir çarpı butonu belirir. Bu çarpı butonu ile animasyon sonlandırılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/Ekranı%20Kilitleyen%20Loading%20Animasyonu-6cf9dd82-19f4-4b3c-9424-5b44b9f80e73.png)

