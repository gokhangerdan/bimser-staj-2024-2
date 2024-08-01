# Form İndeksleme ve Doküman Verisi Arama
Proje Yönetimi üzerinden seçilen bir projedeki Formu Indeksle özelliği kullanılarak ilgilli projenin içerisinde seçilen bir formun seçilen bir alanı üzerinde indeksleme sağlanır. Bu sayede Web Arayüzdeki Arama Çubuğu üzerinde seçilen alana girilen değerler aranarak ilgili dokümanlara ulaşılabilir.

::: note NOT Bu özelliğin kullanılabilmesi için uygulama veritabanında CONFIGURATIONS tablosunda indeksleme işlemleri için kullanılan işlemci(processors) ve indeksleme sağlayıcı(Elasticsearch,Solr) bilgilerinin yapılandırılması gerekmektedir. :::


1.Adım
Proje Yönetimi üzerinden ilgili proje özellikleri açılır. Formu İndeksle butonuna tıklanır.
![formIndeksle](https://docsbimser.blob.core.windows.net/imagecontainer/formIndeksProjectManagement-7306e2c5-a624-4418-adcf-a27d15bf972d.png)

2.Adım
Proje içerisinde hangi formdaki hangi alanların indeksleneceği seçilir.
![formIndeksAlanSecimi](https://docsbimser.blob.core.windows.net/imagecontainer/formIndeksAlanSecimi-f116cd26-0ea2-457f-84c5-c2c8a5b9fb98.png)

İndeksleme öncesindeki veya sonrasındaki alanlara girilen veriler bu sayede indekslenmiş olur.

3.Adım 
Web Arayüzünde sağ üst köşede bulunan Arama Çubuğu üzerinden doküman üzerinde indekslenmiş alanlara girilen herhangi bir metin aratılır. Metnin geçtiği dokümanlar alt tarafta listelenir. 
![MetinAramaFormIndeks](https://docsbimser.blob.core.windows.net/imagecontainer/MetinAramaFormIndeks-3a0ded1f-6099-4247-bf00-3c79041d8953.png)

Listenen formlardan seçim yapılarak aratılan metne sahip bu dokümanın görüntülenmesi sağlanır.
![ideksDokumaniBul](https://docsbimser.blob.core.windows.net/imagecontainer/DokumaniBul-b6aa1863-c3a9-4e9c-9e2e-066c99ff7abd.png)
