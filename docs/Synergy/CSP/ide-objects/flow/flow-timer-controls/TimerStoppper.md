---
sidebar_position: 3
custom_edit_url: ""
---

# Zamanlayıcı Bitir

Zamanlayıcı Bitir nesnesi, akış üzerinde kullanılan Zamanlayıcı nesnesinin sonlandırılmasını sağlamaktadır. Nesne süreç içine eklendiğinde, akışı okları ile sürece dahil edilmelidir.

Araç kutusu panelinden Zamanlayıcı Bitir nesnesi sürüklenip akış üzerine bırakılır. Akış tasarım ekranında bulunan nesneye tıklandığında, Özellik Görüntüleyici panelinde, nesne özellikleri görünür.

Zamanlayıcı Bitir nesnesine tıklandığında Özellik Görüntüleyici panelinde "Appearance", "Properties" ve "Events" sekmeleri bulunmaktadır.

![Zamanlayıcı Bitir](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade3b6e24d-1527-46ba-a8c3-efa588454c58)

## Appearance

### Text Configs

`Object Name` - Nesnenin sistem tarafında kullanılacak ismidir. Kod tarafında nesneye, nesne adı alanında yazan değerle erişim sağlanır.

`Caption` - Nesnenin başlık metninin girildiği alandır.

`Is Lock` - Tasarım anında nesnenin yeri değiştirilmesin isteniyorsa bu alan aktif edilir.

`Size` - Nesnenin genişlik ve yükseklik ayarlarının yapıldığı kısımdır.

## Properties

### Target

`Target Timer` - Alanda akışta bulunan zamanlayıcı nesneleri listelenmekte olup, nesnenin hangi zamanlayıcı nesnesi ile ilişkilendirileceği seçilmektedir.

![Zamanlayıcı Bitir](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb6ea1ee5-73e1-40f6-9059-1119930eafe7)

:::info BİLGİ

Nesne üzerinde ekli özelliklerin doğru olduğu sistem tarafından kontrol edilmektedir. Eksik bir özellik bulunduğunda nesne üzerinde kırmızı ünlem ikonu gösterilerek, fare işaretçisi ile ikon üzerine gelindiğinde nelerin eksik veya hatalı olduğu görüntülenebilmektedir.

![Zamanlayıcı Bitir](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3ec52d04-0526-407a-922d-cf57d5357f7a)

:::

## Events

### Events

Zamanlayıcı Bitir nesnesinin sahip olduğu olaylar, Özellik Görüntüleyici panelindeki "Events" sekmesinde yer almaktadır. Her bir olay, farklı çalışma anlarında tetiklenerek kendilerine özgü işlemleri gerçekleştirir. Bu olaylara geliştirici tarafından yazılan kodlar da ilgili olayın tetiklendiği anda çalıştırılır. Herhangi bir olaya kod yazmak için, Olaylar sekmesinden ilgili olay satırına çift tıklanır. Ekran, “Akışadı.cs” isimli akış kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur. Geliştirici bu method içerisinde istediği kod bloğunu kurgulayabilir. Olaylar sekmesinden tıklanarak kod tarafında methodu oluşturulmuş olayın yanında, method adı bilgisi otomatik oluşturularak, olayla method arasındaki ilişki belirtilmiş olur.

![Zamanlayıcı Bitir](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload91c67754-3266-4b1a-b5a4-f77abddb1309)