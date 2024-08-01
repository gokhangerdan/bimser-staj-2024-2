# Import / Export
Synergy ortamları arasında proje transferleri, aktarım sırasındaki gerekli düzenlemeleri de sağlayarak kolaylıkla gerçekleştirilebilmektedir.

## Dışa Aktarma
Projenizi dışarıya aktarmak için IDE ekranına geçilir, Üst kısımdaki Araçlar menüsü altından Proje Yöneticisi açılır.

![ideProjeYoneticisi](https://docsbimser.blob.core.windows.net/imagecontainer/ideProjeYoneticisi-1e13faaa-6512-4e91-8c34-67f577da41f2.png)

 Dışarıya aktarılmak istenen proje aratılır ve seçilir, Dışa Aktar butonuna tıklanarak proje sıkıştırılmış dosyası(tar.gz uzantılı) cihaza indirilir.
 
![Export](https://docsbimser.blob.core.windows.net/imagecontainer/Export-43c2332b-a75f-4b48-9de2-73f0c2c0511a.png)

## İçe Aktarma
 Dışarıya aktarılan projenin istenen ortama taşınması için taşınacak ortamda Proje Yöneticisine gidilir ve İçe Aktar butonuna Tıklanır. Ardından adım adım projenin aktarım aşamaları takip edilir.

**1.Adım: Proje Kaynağı Seçimi**
Cihazdan ya da Doküman yönetiminden seçilmek üzere dışa aktarılmış olan projenin tar.gz uzantılı sıkıştırılmış dosyası seçilir.

![ImportAdim1](https://docsbimser.blob.core.windows.net/imagecontainer/Import1-dd42ab83-ecb9-4e5b-89be-ab6a29fb2639.png)
 
**2.Adım: Hedef Dizin Seçimi**
 Projenin ortamdaki mevcut bir proje ya da yeni bir proje olmasına göre ilerlenir, eğer kaynakta seçilen proje ismi hedefte mevcutsa otomatik olarak *mevcut projenin üzerine yazılacak* seçeneği seçili olarak gelir. Eğer mevcut değilse *yeni bir proje olarak aktar* seçilir ve hedef ortamda Doküman yönetimi üzerinde proje klasörünün hangi dizine kaydedileceğinin seçimi yapılır.
 
![importAdım2Hedef](https://docsbimser.blob.core.windows.net/imagecontainer/importAd%C4%B1m2Hedef-c5ed09e1-4463-4a4b-a016-ae9db1270e61.png)
 
**3.Adım: Analiz**
Sol taraftaki kırılımlı yapıda Projenin hangi dosyalarında ne türde değişiklik olduğu bilgisi yer alır. Sağ tarafta ise projenin kapsadığı öğeler listelenir.

![ImportAdim3Analiz](https://docsbimser.blob.core.windows.net/imagecontainer/ImportAdim3Analiz-b1b9e768-d2a8-4153-bff4-d3552558a5db.png)

**4.Adım: DM Dizin Değişiklikleri**
Projenin kaynak ortamdaki dizininde barınan nesnelerin hedef ortamda hangi dizinde tutulacağının değişikliği yapılır. Kaynak yolunda geçen dizinin sağ tarafındaki bilgilendirme ikonunun (🛈) üzerine gelindiğinde bu nesnenin projede nerede kullanıldığının bilgisi bulunur. 
Örneğin: /Forms/MasrafDetayFormu/MasrafDetayFormu.eaf - RdMasrafDokumanlari 
Bu örnek, projedeki MasrafDetayFormu'nun formunun RdMasrafDokumanlari isimli ilişkili doküman nesnesindeki dizin bilgisini göstermektedir. 
Bu sayede DM dizin değişiklikleri aktarım sırasında sağlanarak proje nesneleri hedef ortama uyumlu hale gelmiş olur. 

![ImportAdim4DM](https://docsbimser.blob.core.windows.net/imagecontainer/ImportAdim4DM-062c5a7a-35d5-4f36-90a4-df2739c31e27.png)

**5.Adım: Bağlantılar**
Projenin kaynak ortamında DataSource altında bulunan sorguların hangi türde Bağlantı bilgisi içerdiği ve bağlantı kaynağının adı *Kaynak bağlantısı* altında listelenir. Bilgilendirme ikonunun (🛈) üzerine gelindiğinde ise sorguların hangileri olduğu gösterilir. 
Örneğin: /DataSource/MasrafTipleriGetir.mssqlds - MasrafTipleriGetir, /DataSource/MasrafBeyanSurecArsivi_DataSource.mssqlds - MasrafBeyanSurecArsivi_DataSource
Örnekteki 2 sorgu da Kaynaktaki *Danismanlik* bağlantısını kullanmaktadır.
Eşleşen bağlantı üzerinden de ilgili bağlantıların hedef ortamda hangi bağlantı kaynağı ile yapılacağı seçilir. 
Bağlantı kaynaklarının taşınması ile projelerdeki dinamik kaynaklı nesneler Test ortamdan Canlı ortama geçişte kolay bir şekilde uyumlu hale gelmiş olur.
![ImportAdim5Baglantilar](https://docsbimser.blob.core.windows.net/imagecontainer/ImportAdim5Baglantilar-f15056cf-45a5-458f-8575-3dca6a9c009d.png)

**6.Adım: HR**
Kaynak ortamda projenin Akış tarafında kullanılan Pozisyon,Ünvan,Departman, Pozisyon Grubu gibi nesnelerin İnsan Kaynaklarındaki verileri ile Hedef ortamdaki İnsan Kaynakları verileri arasında eşleştirilme yapılır.

![ImportAdim6HR](https://docsbimser.blob.core.windows.net/imagecontainer/ImportAdim6HR-bd12a4d4-d85b-47ab-b064-ab60f5d3f3e8.png)
 
 **7.Adım: Form**
 Kaynak ortamdaki Proje,Form ve viewlar ile Hedef ortamdakiler arasında eşleştirme yapılması sağlanır.
 ![importAdım7Form](https://docsbimser.blob.core.windows.net/imagecontainer/importAd%C4%B1m7Form-342564d4-f7d2-4179-b61b-42088d9c1b1a.png)

**8.Adım:  Akış**
 Kaynak ortamdaki Proje ve Akışlar ile Hedef ortamdakiler arasında eşleştirme yapılması sağlanır.

**9.Adım: PAT(Personal Access Token)**
Projenin Schedules bölümünde herhangi bir İş tanımlı ise bu işe tanımlanan Erişim anahtarının(Personal access token) hedef ortamdaki karşılığının belirtilmesi gerekir. Kaynak pat'daki bilgilendirme ikonunun (🛈) üzerine gelindiğinde hangi Schedule İş'inin olduğu bilgisi görünür.
Örneğin: /Schedules/Test.sch - İş1
Örnekteki iş için gereken erişim anahtarı yerine hedef ortamdaki erişim anahtarının girildiği alandır.
![ImportAdim9PAT](https://docsbimser.blob.core.windows.net/imagecontainer/ImportAdim9PAT-a3c06857-6990-453c-b195-50f5d6bd3cb6.png)

**10.Adım: İçe Aktar**
Son adımda Projenin içe aktarma işlemi gerçekleştirilir. Eğer aktarım gerçekleştikten sonra uygulamanın yayınlanması isternirse ilgili kutucuk işaretlenir ve yayınlamanın Major ya da Minor olarak hangi versiyon türünde yapılacağı seçilir. Deploy agent seçimi de yapılarak alt taraftaki İçe aktar butonuna tıklanır ve ardından Aktarım ve Yayınlama işlemleri başlar. Aşamalar Çıktı ekranında gösterilir.

![ImportAdim10SONDeploy](https://docsbimser.blob.core.windows.net/imagecontainer/ImportAdim10SONDeploy-a12b5f7e-341b-46c3-8d2f-264dd1166015.png) 
