# Excel Aktarımı Sırasında Login Ekranına Atma

Microsoft Access Database Engine 2016 64 Bit kurun.
Daha sonra 32 Bit'ini indirin ve CMD'yi açın. Ekran görüntüsündeki gibi dosya yolunu belirtip sonuna /quiet ekleyin ve çalıştırın. ---------- https://www.microsoft.com/en-us/download/details.aspx?id=54920


Örnek: C:\Users\eba\Downloads\accessdatabaseengine.exe /quiet

![](https://docsbimser.blob.core.windows.net/imagecontainer/excelloginhata1-62e1a646-113f-425c-99cd-1aa89e36b564.png)

Sonrasında PRODUCTION veya TEST, kısaca IIS'teki eBA'yı barındıran web site'ın altındaki eba.net applikasyonu hangi application pool'a bağlıysa o application pool'un user'ını ApplicationPoolIdentity'den LocalSystem'e çevirin ve servisleri restart edin.

![](https://docsbimser.blob.core.windows.net/imagecontainer/excelloginhata2-74fa45c4-0ef5-478c-b891-119748582479.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/excelloginhata3-1b733672-356d-44b5-ac78-a08ceb42f020.png)

