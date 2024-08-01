# eBA Office Online Viewer Nasıl Aktif Edilir?

BA Office Online Viewer Kurulum dokümanında, Doküman Yönetiminde office uzantılı dosyalar üzerinde 
düzenleme yapabilmek için Office Online Viewer kurulumunun nasıl yapıldığı anlatılmaktadır.

### 1.eBA Office Online Viewer Kurulumu

Doküman Yönetiminde office uzantılı dosyalar üzerinde düzenleme yapabilmek için Office Online Viewer 
kurulumu yapılır. Kuruluma başlamadan önce eBA Viewer kurulumunun yapılmış olması gerekmektedir. 
Viewer kurulum işlemi eBA Viewer Ekleme Dokümanı’nda anlatılmaktadır. 
eBA Office Online Viewer ile dokümanları web üzerinden düzenleyebilmek için Office Online Server’da 
düzenleme lisansına sahip olunması gerekmektedir. Aksi halde dokümanlar görüntülenir fakat üzerinde 
değişiklik yapılamaz.
Not: Kuruluma başlamadan önce Müşterinin Office Online Server’ının kurulu olduğu makinenin adı/IP 
adresi istenir.
Şekil 1’de, 1 numaralı alandaki eBA’nın kurulu olduğu dizin açılır. WopiHost_Publish klasörü bu dizinin 
altına kopyalanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade0f5f316-c37d-49ed-be79-11d78033e96a)

IIS üzerinde eBA’nın çalıştığı web site altında RestWopiHost uygulaması oluşturulur. Şekil 2’de, 1 numaralı 
alandaki Default Web Site üzerinde iken sağ tuş tıklanıp Add Aplication seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3154bc4b-fb9b-43be-9f48-2df4eb1dcdd0)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada0ac27c8-63a4-4ff7-a73b-91e7e801a746)

Şekil 3’te, 1 numaralı alana RestWopiHost ya da başka bir ad yazılır. 2 numaralı alanda eBA klasörüne 
kopyaladığımız WopiHost_Publish klasörü seçilir.

WopiHost_Publish dizini altında bulunan web.config dosyası içerisinde değişiklik yapılmalıdır. Şekil 4’teki 
gibi Web.config dosyası Notepad ile açılır.


![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc9580ef6-1f71-4adc-82e1-d841f263a8dd)

Şekil 5’te, 1 numaralı alanda belirtilen yer, Office Online Server’ının kurulu olduğu makinenin adı/IP Adresi 
ile değiştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8deb2ee6-3c54-4ce5-8a93-a7cbdd2c6b1b)

Not: IIS’te RestWopiHost adı yerine başka bir ad verildi ise Şekil 5’de, web.config dosyasında 
WopiApplicationName ve daha önce eklenen BimserViewer klasörü altındaki web.config dosyasında 
OfficeWopiHostApplicationPath değerinde yazan RestWopiHost, verilen ad ile değiştirilmelidir.
Dokümanın tamamında http:// ile başlayan satırlarda kırmızı ile işaretli alanlara makinanın IP adresi yazılıp 
dosya kaydedilir.


![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1e2f2a4f-1dde-47fc-903c-863afd362a2f)

Viewers.config dosyasında değişiklik yapılır. Şekil 7’da, dokümanın tamamında http:// ile başlayan 
satırlarda kırmızı ile işaretli alanlara makinanın IP adresi yazılıp dosya kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload93e0cd56-11cd-4e1f-8349-a0a426aaf089)

Doküman Yönetim sisteminde viewers.config dosyasında değişiklik yapılır

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb6756047-2e36-4c11-8e75-5d81517dce28)

Şekil 8’de, 1 numaralı alanda belirtilen dizin açılır. 2 numaralı alandaki viewers.config dosyası çift tıklanarak 
açılır.


![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8aec4cdf-a5cf-466e-9296-e1ae6b7b0afa)

Dosya üzerinde değişiklik yapmak için; Şekil 9’da, 1 numaralı alandaki Edit butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7e6091e7-7fe9-43fc-b06e-07e926751cc2)

Şekil 10’da, 1 numaralı alandaki tüm satırlar silinip Şekil 7’deki, viewers dosyasındaki tüm satırlar buraya 
kopyalanır. Değişiklikleri kaydetmek için 2 numaralı alandaki butona tıklanır.
Office Online ile görüntülenecek dosya uzantıları Şekil 11’de, 1 numaralı alanda belirtilmiştir. Var olan 
dosya uzantılarına ekleme ya da çıkarma yapılabilir.


![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadff883488-18b9-43fb-81aa-c159a540a6a9)

Yaptığımız tüm değişikliklerin uygulanması için IIS restart edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcccb6fc4-d661-4eb7-ba9b-cd6df8734ffd)

Şekil 12’de, 1 numaralı alana tıklanıp 2 numaralı alandaki Restart linkine tıklanarak restart işlemi yapılır.