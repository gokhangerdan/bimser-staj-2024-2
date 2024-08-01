---
sidebar_position: 1
custom_edit_url: ""
---

# Zamanlayıcı

Zamanlayıcı nesnesi, belirlenen bir süre sonunda akışın üzerinde istenilen işlemin yapılmasını sağlamaktadır. Nesne, diğer akış nesneleri olan "**[Zamanlayıcı Başlat](./TimerStarter.md)**" ve "**[Zamanlayıcı Bitir](./TimerStoppper.md)**" nesneleriyle birlikte kullanılır. Akış ekranına konulduğunda, bu nesneye başka bir akış nesnesinden ok bağlanmamaktadır. Ancak, zaman aşımı olduğunda akışın nereye yönlendirileceğinin belirtilmesi için, Zamanlayıcı nesnesinden "Time Out" oku çıkartılmalıdır.

Araç kutusu panelinden Zamanlayıcı nesnesi sürüklenip akış üzerine bırakılır. Akış tasarım ekranında bulunan nesneye tıklandığında, Özellik Görüntüleyici panelinde, nesne özellikleri görünür.

Zamanlayıcı nesnesine tıklandığında Özellik Görüntüleyici panelinde "Appearance", "Properties" ve "Events" sekmeleri bulunmaktadır.

![Zamanlayıcı](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfc952d60-bc53-458e-b7bb-dacf973807be)

## Appearance

### Text Configs

`Object Name` - Nesnenin sistem tarafında kullanılacak ismidir. Kod tarafında nesneye, nesne adı alanında yazan değerle erişim sağlanır.

`Caption` - Nesnenin başlık metninin girildiği alandır.

`Is Lock` - Tasarım anında nesnenin yeri değiştirilmesin isteniyorsa bu alan aktif edilir.

`Size` - Nesnenin genişlik ve yükseklik ayarlarının yapıldığı kısımdır.

## Properties

### Time Out

`Day` - Zaman aşımı için belirlenen gün sayısının girildiği alandır.

`Hour` - Zaman aşımı için belirlenen saat sayısının girildiği alandır.

`Minute` - Zaman aşımı belirlenen dakika sayısının girildiği alandır.

`Calculate Using Working Hours` - Zaman aşımı hesaplanırken sistem ayarlarında belirtilen çalışma saatleri dikkate alınması isteniyorsa işaretlenmelidir.

`Calculate Using Holidays` - Zaman aşımı hesaplamalarında tatil olarak belirtilen günlerin dikkate alınması isteniyorsa işaretlenmelidir.

:::tip İPUCU

Örneğin aşağıdaki resimdeki senaryoda süreç başlatıldığında, Zamanlayıcı Başlat nesnesinden geçerek kullanıcı onayına gelir. Zamanlayıcı Başlat nesnesi Zamanlayıcı nesnesini tetiklemekte ve nesne içinde tanımlanmış 1 günlük Time Out sayacını başlatır. 1 gün içinde "Kullanıcı Amiri" başlıklı pozsiyondaki kullanıcı süreçte herhangi bir aksiyon almaz ise süre tamamlandığında Zamanlayıcı nesnesindeki ZamanAşımı kolu üzerinden süreç ilerler.

![Zamanlayıcı](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadefbe21c8-c45b-4aa3-bb74-d10d23788f96)

:::

## Events

### Events

Zamanlayıcı nesnesinin sahip olduğu olaylar, Özellik Görüntüleyici panelindeki "Events" sekmesinde yer almaktadır. Her bir olay, farklı çalışma anlarında tetiklenerek kendilerine özgü işlemleri gerçekleştirir. Bu olaylara geliştirici tarafından yazılan kodlar da ilgili olayın tetiklendiği anda çalıştırılır. Herhangi bir olaya kod yazmak için, Olaylar sekmesinden ilgili olay satırına çift tıklanır. Ekran, “Akışadı.cs” isimli akış kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur. Geliştirici bu method içerisinde istediği kod bloğunu kurgulayabilir. Olaylar sekmesinden tıklanarak kod tarafında methodu oluşturulmuş olayın yanında, method adı bilgisi otomatik oluşturularak, olayla method arasındaki ilişki belirtilmiş olur.

![Zamanlayıcı](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfc952d60-bc53-458e-b7bb-dacf973807be)