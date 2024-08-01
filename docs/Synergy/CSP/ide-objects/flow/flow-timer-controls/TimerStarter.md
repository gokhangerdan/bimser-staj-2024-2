---
sidebar_position: 2
custom_edit_url: ""
---

# Zamanlayıcı Başlat

Zamanlayıcı Başlat nesnesi, akış üzerinde kullanılan Zamanlayıcı nesnesinin başlatılmasını sağlamaktadır. Nesne süreç içine eklendiğinde, akışı okları ile sürece dahil edilmelidir.

Araç kutusu panelinden Zamanlayıcı Başlat nesnesi sürüklenip akış üzerine bırakılır. Akış tasarım ekranında bulunan nesneye tıklandığında, Özellik Görüntüleyici panelinde, nesne özellikleri görünür.

Zamanlayıcı Başlat nesnesine tıklandığında Özellik Görüntüleyici panelinde "Appearance", "Properties" ve "Events" sekmeleri bulunmaktadır.

![Zamanlayıcı Başlat](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcff6b544-7e23-4610-8355-acf239d272f2)

## Appearance

### Text Configs

`Object Name` - Nesnenin sistem tarafında kullanılacak ismidir. Kod tarafında nesneye, nesne adı alanında yazan değerle erişim sağlanır.

`Caption` - Nesnenin başlık metninin girildiği alandır.

`Is Lock` - Tasarım anında nesnenin yeri değiştirilmesin isteniyorsa bu alan aktif edilir.

`Size` - Nesnenin genişlik ve yükseklik ayarlarının yapıldığı kısımdır.

## Properties

### Target

`Target Timer` -  Alanda akışta bulunan zamanlayıcı nesneleri listelenmekte olup, nesnenin hangi zamanlayıcı nesnesi ile ilişkilendirileceği seçilmektedir.

![Zamanlayıcı Başlat](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6b84fa86-e781-4fd3-aa34-ea75ecbbfdb6)

:::info BİLGİ

Nesne üzerinde ekli özelliklerin doğru olduğu sistem tarafından kontrol edilmektedir. Eksik bir özellik bulunduğunda nesne üzerinde kırmızı ünlem ikonu gösterilerek, fare işaretçisi ile ikon üzerine gelindiğinde nelerin eksik veya hatalı olduğu görüntülenebilmektedir.

![Zamanlayıcı Başlat](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9c08fae0-a9e2-4d75-ad7c-e44e57f82fb3)

:::

## Events

### Events

Zamanlayıcı Başlat nesnesinin sahip olduğu olaylar, Özellik Görüntüleyici panelindeki "Events" sekmesinde yer almaktadır. Her bir olay, farklı çalışma anlarında tetiklenerek kendilerine özgü işlemleri gerçekleştirir. Bu olaylara geliştirici tarafından yazılan kodlar da ilgili olayın tetiklendiği anda çalıştırılır. Herhangi bir olaya kod yazmak için, Olaylar sekmesinden ilgili olay satırına çift tıklanır. Ekran, “Akışadı.cs” isimli akış kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur. Geliştirici bu method içerisinde istediği kod bloğunu kurgulayabilir. Olaylar sekmesinden tıklanarak kod tarafında methodu oluşturulmuş olayın yanında, method adı bilgisi otomatik oluşturularak, olayla method arasındaki ilişki belirtilmiş olur.

![Zamanlayıcı Başlat](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd828b85d-c6c0-42a6-8854-7cbb780a234e)