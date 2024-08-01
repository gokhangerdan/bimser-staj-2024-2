---
sidebar_position: 5
custom_edit_url: ""
---

# Akış Durdurucu

Akış Durdurucu nesnesi, akışın kodla tetikleme yapılana kadar bulunduğu adımda kalmasını sağlamaktadır. Kodla tetikleme sonucunda, nesnenin tetiklendiği parametre değerine göre akış istenilen şekilde yönlendirilir.

Araç kutusu panelinden Akış Durdurucu nesnesi sürüklenip akış üzerine bırakılır. Akış tasarım ekranında bulunan nesneye tıklandığında, Özellik Görüntüleyici panelinde, nesne özellikleri görünür.

Akış Durdurucu nesnesine tıklandığında Özellik Görüntüleyici panelinde "Appearance", "Properties" ve "Events" sekmeleri bulunmaktadır.

![Akış Durdurucu](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcf0a8499-5afd-4120-a8a6-1fc0706ebea2)

## Appearance

### Text Configs

`Object Name` - Nesnenin sistem tarafında kullanılacak ismidir. Kod tarafında nesneye, nesne adı alanında yazan değerle erişim sağlanır.

`Caption` - Nesnenin başlık metninin girildiği alandır.

`Is Lock` - Tasarım anında nesnenin yeri değiştirilmesin isteniyorsa bu alan aktif edilir.

`Size` - Nesnenin genişlik ve yükseklik ayarlarının yapıldığı kısımdır.

## Properties

### Events

`Olaylar` - Alanda, **[Flow Properties->Events](index.mdx#events)** sekmesinde bulunan tüm olaylar listelenmektedir. Akış Durdurucu nesnesi kullanılarak durdurulan süreç, durdurma işleminden hemen önce tetiklenen diğer süreç içerisinden bu sekmedeki değerle tekrar başlama konumuna alınabilir.

### Options

`Show in the Flow History` - Nesnenin akış tarihçesinde bir adım olarak gözükmesi isteniyorsa seçenek işaretlenmelidir. İşaretli olmadığı durumda, akış tarihçesinde akışın durdurulduğunu ifade eden Akış Durdurucu nesnesi ile ilgili satır görünmeyecektir.

### Time Out

`Day` - Nesnenin olaylar sekmesine eklenen Timeout olayı için belirlenen gün sayısının girildiği alandır.

`Hour` - Nesnenin olaylar sekmesine eklenen Timeout olayı için belirlenen saat sayısının girildiği alandır.

`Minute` - Nesnenin olaylar sekmesine eklenen Timeout olayı  için belirlenen dakika sayısının girildiği alandır.

`Calculate Using Working Hours` - Timeout olayı hesaplanırken sistem ayarlarında belirtilen çalışma saatleri dikkate alınması isteniyorsa işaretlenmelidir.

`Calculate Using Holidays` - Timeout olayı hesaplamalarında tatil olarak belirtilen günlerin dikkate alınması isteniyorsa işaretlenmelidir.

:::info BİLGİ

Nesne üzerinde ekli özelliklerin doğru olduğu sistem tarafından kontrol edilmektedir. Eksik bir özellik bulunduğunda nesne üzerinde kırmızı ünlem ikonu gösterilerek, fare işaretçisi ile ikon üzerine gelindiğinde nelerin eksik veya hatalı olduğu görüntülenebilmektedir.

![Akış Durdurucu](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload96921409-0a81-460d-a7d3-7f505f969045)

:::

## Events

### Events

Akış Durdurucu nesnesinin sahip olduğu olaylar, Özellik Görüntüleyici panelindeki "Events" sekmesinde yer almaktadır. Her bir olay, farklı çalışma anlarında tetiklenerek kendilerine özgü işlemleri gerçekleştirir. Bu olaylara geliştirici tarafından yazılan kodlar da ilgili olayın tetiklendiği anda çalıştırılır. Herhangi bir olaya kod yazmak için, Olaylar sekmesinden ilgili olay satırına çift tıklanır. Ekran, “Akışadı.cs” isimli akış kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur. Geliştirici bu method içerisinde istediği kod bloğunu kurgulayabilir. Olaylar sekmesinden tıklanarak kod tarafında methodu oluşturulmuş olayın yanında, method adı bilgisi otomatik oluşturularak, olayla method arasındaki ilişki belirtilmiş olur.

![Akış Durdurucu](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf2bfaf71-3fb4-4db7-832c-f517b39a27f4)