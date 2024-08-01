---
sidebar_position: 15
custom_edit_url: ""
---

# Yorum

Yroum nesnesi, akış okunabilirliğini arttıran bir nesnedir. Nesne kullanılarak akış içinde belli bir kısım hakkında veya bir fonksiyon içinde yapılan işlemleri tasarım üzerinde açıklamalar eklenebilir.

Akış tasarım ekranında bulunan nesneye tıklandığında, Özellik Görüntüleyici panelinde, nesne özellikleri görünür.

![Yorum](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb3be2ff2-a2c4-489c-966f-2789a9bbf01a)

Yorum nesnesine tıklandığında Özellik Görüntüleyici panelinde "Appearance" ve "Events" sekmeleri bulunmaktadır.

## Appearance

### Text Configs

`Object Name` - Nesnenin sistem tarafında kullanılacak ismidir. Kod tarafında nesneye, nesne adı alanında yazan değerle erişim sağlanır.

`Caption` - Nesnenin başlık metninin girildiği alandır.

`Is Lock` - Tasarım anında nesnenin yeri değiştirilmesin isteniyorsa bu alan aktif edilir.

`Size` - Nesnenin genişlik ve yükseklik ayarlarının yapıldığı kısımdır.

## Events

Yorum nesnesinin sahip olduğu olaylar, Özellik Görüntüleyici panelindeki "Events" sekmesinde yer almaktadır. Her bir olay, farklı çalışma anlarında tetiklenerek kendilerine özgü işlemleri gerçekleştirir. Bu olaylara geliştirici tarafından yazılan kodlar da ilgili olayın tetiklendiği anda çalıştırılır. Herhangi bir olaya kod yazmak için, Events sekmesinden ilgili olay satırına çift tıklanır. Ekran, “Akışadı.cs” isimli akış kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur. Geliştirici bu method içerisinde istediği kod bloğunu kurgulayabilir. Events sekmesinden tıklanarak kod tarafında methodu oluşturulmuş olayın yanında, method adı bilgisi otomatik oluşturularak, olayla method arasındaki ilişki belirtilmiş olur.

![Yorum](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload52189f88-e197-40b7-8f51-af0860981db3)