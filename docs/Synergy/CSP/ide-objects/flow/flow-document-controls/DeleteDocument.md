---
sidebar_position: 6
custom_edit_url: ""
---

# Doküman Silme

Doküman Silme nesnesi, proje formlarını sistemden silmek için kullanılır. Doküman silme nesnesi ile silinen dokümanlar sistemden kaldırıldıkları için bu nesne sadece atıl durumda olan, bir daha ulaşılması gerekmeyen formlar için tercih edilmelidir.

Araç kutusu panelinden Doküman Silme nesnesi sürüklenip akış üzerine bırakılır. Akış tasarım ekranında bulunan nesneye tıklandığında, Özellik Görüntüleyici panelinde, nesne özellikleri görünür. 

Doküman Silme nesnesine tıklandığında Özellik Görüntüleyici panelinde "Appearance", "Properties" ve "Events" sekmeleri bulunmaktadır.

![Doküman Silme](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada34c5a2c-a4f8-443a-b109-7783ae67a01b)

## Appearance

### Text Configs

`Object Name` - Nesnenin sistem tarafında kullanılacak ismidir. Kod tarafında nesneye, nesne adı alanında yazan değerle erişim sağlanır.

`Caption` - Nesnenin başlık metninin girildiği alandır.

`Is Lock` - Tasarım anında nesnenin yeri değiştirilmesin isteniyorsa bu alan aktif edilir.

`Size` - Nesnenin genişlik ve yükseklik ayarlarının yapıldığı kısımdır.

## Properties

### Documents

`Documents` -  Alanda akış tasarımındaki tüm Doküman nesneleri listelenir ve silinmek istenen formun bağlı olduğu Doküman nesnesinin seçimi bu alandan yapılmaktadır. Bir veya birden fazla doküman nesnesi seçilerek, bunları silmek mümkündür.

![Doküman Silme](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3a4e8890-745d-4589-a6a8-83b9978dc0de)

:::info BİLGİ

Nesne üzerinde ekli özelliklerin doğru olduğu sistem tarafından kontrol edilmektedir. Eksik bir özellik bulunduğunda nesne üzerinde kırmızı ünlem ikonu gösterilerek, fare işaretçisi ile ikon üzerine gelindiğinde nelerin eksik veya hatalı olduğu görüntülenebilmektedir.

![Doküman Silme](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload62012fc5-5793-468b-873a-1d8c62e2c37a)

:::

## Events

### Events

Doküman Silme nesnesinin sahip olduğu olaylar, Özellik Görüntüleyici panelindeki "Events" sekmesinde yer almaktadır. Her bir olay, farklı çalışma anlarında tetiklenerek kendilerine özgü işlemleri gerçekleştirir. Bu olaylara geliştirici tarafından yazılan kodlar da ilgili olayın tetiklendiği anda çalıştırılır. Herhangi bir olaya kod yazmak için, Olaylar sekmesinden ilgili olay satırına çift tıklanır. Ekran, “Akışadı.cs” isimli akış kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur. Geliştirici bu method içerisinde istediği kod bloğunu kurgulayabilir. Olaylar sekmesinden tıklanarak kod tarafında methodu oluşturulmuş olayın yanında, method adı bilgisi otomatik oluşturularak, olayla method arasındaki ilişki belirtilmiş olur.

![Doküman Silme](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6caabb54-2e77-4023-8aa9-72a985fcd93f)