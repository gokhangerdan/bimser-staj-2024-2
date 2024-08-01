# QDMS Harici Uygulama Üzerinden Giriş İşlemleri

## Harici Giriş İşlemleri Parametreleri

![](https://docsbimser.blob.core.windows.net/imagecontainer/EXTERNALLOGIN1-e66b6ad9-0341-4df4-b320-6b43acfe898a.png)

## Harici Giriş İşlemleri Örnek Kod Geliştirmeleri

### Android

Intent paket ismi “com.bimser.qdmsv2.SplashActivity.launchapp” şeklindedir. Java ve kotlin için örnek kodlar aşağıdaki gibidir :

![](https://docsbimser.blob.core.windows.net/imagecontainer/EXTERNALLOGINIMAGE2-8dd3c999-7ce4-4153-b3ea-13aae6b89e41.png)

### iOS

![](https://docsbimser.blob.core.windows.net/imagecontainer/EXTERNALLOGINIMAGE3-16bda6fd-4dff-4c38-8ce0-465377e5b2aa.png)

## Harici Giriş İşlemleri Result Değerleri

### Android

Uygulama hata alması durumunda Activity.RESULT_CANCELED değeri ile geri bildirim yapılmaktadır. Geri bildirim intenti içinde gelen “error” keyinde aşağıdaki hata kodları dönmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/EXTERNALLOGINIMAGE4-adb53eaf-94ff-458d-8331-1512a8247976.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/EXTERNALLOGINIMAGE5-003113d5-ca0a-42ae-ac11-2350cf0220e3.png)

### iOS

iOS tarafında geri bildirimler QDMS üzerinden uyarı paneliyle sağlanmaktadır.

