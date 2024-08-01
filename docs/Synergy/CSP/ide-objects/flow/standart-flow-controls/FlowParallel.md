---
sidebar_position: 11
custom_edit_url: ""
---
# Paralel Akış

Paralel akış nesnesi, süreç içinde akışın aynı anda birden fazla pozisyon veya pozisyon grubuna yönlendirilmesini sağlamak için kullanılır. Akış tasarımında sürecin kollara ayrılacağı yer veya yerlere bu nesne yerleştirilir.

Akış tasarım ekranında bulunan nesneye tıklandığında, Özellik Görüntüleyici panelinde, nesne özellikleri görünür.

![Paralel Akış](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbdd7d60a-bc7c-446b-b55b-6a7169d8d8e0)

Paralel Akış nesnesine tıklandığında Özellik Görüntüleyici panelinde "Appearance" ve "Events" sekmeleri bulunmaktadır.

> *Nesnenin örnek kullanımı*
![Paralel Akış](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd2b3bfa1-b6f8-4a4a-aee6-6e0c636791d2)

## Appearance

### Text Configs

`Object Name` - Nesnenin sistem tarafında kullanılacak ismidir. Kod tarafında nesneye, nesne adı alanında yazan değerle erişim sağlanır.

`Caption` - Nesnenin başlık metninin girildiği alandır.

`Is Lock` - Tasarım anında nesnenin yeri değiştirilmesin isteniyorsa bu alan aktif edilir.

`Size` - Nesnenin genişlik ve yükseklik ayarlarının yapıldığı kısımdır.

:::info BİLGİ

Nesne üzerinde ekli özelliklerin doğru olduğu sistem tarafından kontrol edilmektedir. Eksik bir özellik bulunduğunda nesne üzerinde kırmızı ünlem ikonu gösterilerek, fare işaretçisi ile ikon üzerine gelindiğinde nelerin eksik veya hatalı olduğu görüntülenebilmektedir.

![Paralel Akış](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload40c85a20-2670-48bd-8127-94708b865c08)

:::

## Events

Paralel Akış nesnesinin sahip olduğu olaylar, Özellik Görüntüleyici panelindeki "Events" sekmesinde yer almaktadır. Her bir olay, farklı çalışma anlarında tetiklenerek kendilerine özgü işlemleri gerçekleştirir. Bu olaylara geliştirici tarafından yazılan kodlar da ilgili olayın tetiklendiği anda çalıştırılır. Herhangi bir olaya kod yazmak için, Events sekmesinden ilgili olay satırına çift tıklanır. Ekran, “Akışadı.cs” isimli akış kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur. Geliştirici bu method içerisinde istediği kod bloğunu kurgulayabilir. Events sekmesinden tıklanarak kod tarafında methodu oluşturulmuş olayın yanında, method adı bilgisi otomatik oluşturularak, olayla method arasındaki ilişki belirtilmiş olur.

![Paralel Akış](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload380118b2-f961-47bc-ad1b-6145c6329d83)