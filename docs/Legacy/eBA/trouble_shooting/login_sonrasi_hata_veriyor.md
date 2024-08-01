# Input string was not in a correct format. Login sonrası hata veriyor.

Kullanıcı login yaptığında ana sayfaya erişemiyor. Sol menüden ana sayfaya tıkladığında da resimdeki gibi uyarı alıyorsa, çözüm için şunlar yapılmalıdır;

![](https://docsbimser.blob.core.windows.net/imagecontainer/hata1-dca72f7d-14bf-47e0-addb-11af48440f55.png)

Çözüm olarak veritabanındaki  DASHBOARDUSERSETTINGS tablosunda parametre alanı kontrol edilir. Örneğin resimdeki gibi (,Uygulamalar) alanın başında fazladan "," işreti varsa bu işret kaldırılır.
 Sadece virgülü kaldırınca düzelmezse DASHBOARDUSERSETTINGS tablosundaki "NULL" alanlar silinir ve sistem restart edilerek sorun giderilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/hata3-405fb207-21cd-45ca-bc07-e7b983f51493.png)

