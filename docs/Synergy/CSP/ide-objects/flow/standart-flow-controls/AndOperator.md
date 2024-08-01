---
sidebar_position: 12
custom_edit_url: ""
---
# Ve Operatörü

Ve operatörü nesnesi, birden fazla pozisyonun onayına gönderildiği veya kollara ayrılarak farklı işlem adımlarının paralel yapılmasının ardından, hepsinin sonuçları döndükten sonra akışın devam etmesinin istendiği durumlarda kullanılan bir nesnedir. Akış tasarımında kollara ayrılmış işlem adımlarının tek bir kolda birleştirmek için kullanılır.

Ve Operatörü **kendisine bağlanan tüm akış adımlarından bir sonuç dönmesini** beklemektedir. Akış, ancak Ve Operatörüne bağlı tüm kollardan bir sonuç döndüğünde ilerletilir ve sonraki adımlara geçer aksi taktirde akış tüm işlem adımlarındaki işlemlerin tamamlanması için nesne üzerinde beklemede kalır. Ve operatörüne **n adet bağlantı kolu bağlanılabilir** ancak nesneden **sadece bir adet ok** çıkarılabilir.

Akış tasarım ekranında bulunan nesneye tıklandığında, Özellik Görüntüleyici panelinde, nesne özellikleri görünür.

![Ve Operatörü](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbacb9a47-aa54-4f46-bf6c-2dff564454cd)

Ve Operatörü nesnesine tıklandığında Özellik Görüntüleyici panelinde "Appearance" ve "Events" sekmeleri bulunmaktadır.

## Appearance

### Text Configs

`Object Name` - Nesnenin sistem tarafında kullanılacak ismidir. Kod tarafında nesneye, nesne adı alanında yazan değerle erişim sağlanır.

`Caption` - Nesnenin başlık metninin girildiği alandır.

`Is Lock` - Tasarım anında nesnenin yeri değiştirilmesin isteniyorsa bu alan aktif edilir.

`Size` - Nesnenin genişlik ve yükseklik ayarlarının yapıldığı kısımdır.

:::info BİLGİ

Nesne üzerinde ekli özelliklerin doğru olduğu sistem tarafından kontrol edilmektedir. Eksik bir özellik bulunduğunda nesne üzerinde kırmızı ünlem ikonu gösterilerek, fare işaretçisi ile ikon üzerine gelindiğinde nelerin eksik veya hatalı olduğu görüntülenebilmektedir.

![Ve Operatörü](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb999d314-854b-4e4a-bb22-bba7c7a70421)

:::

## Events

Ve Operatörü nesnesinin sahip olduğu olaylar, Özellik Görüntüleyici panelindeki "Events" sekmesinde yer almaktadır. Her bir olay, farklı çalışma anlarında tetiklenerek kendilerine özgü işlemleri gerçekleştirir. Bu olaylara geliştirici tarafından yazılan kodlar da ilgili olayın tetiklendiği anda çalıştırılır. Herhangi bir olaya kod yazmak için, Events sekmesinden ilgili olay satırına çift tıklanır. Ekran, “Akışadı.cs” isimli akış kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur. Geliştirici bu method içerisinde istediği kod bloğunu kurgulayabilir. Events sekmesinden tıklanarak kod tarafında methodu oluşturulmuş olayın yanında, method adı bilgisi otomatik oluşturularak, olayla method arasındaki ilişki belirtilmiş olur.

![Ve Operatörü](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3f89f785-7f93-44df-b741-98e4fb8f95b3)