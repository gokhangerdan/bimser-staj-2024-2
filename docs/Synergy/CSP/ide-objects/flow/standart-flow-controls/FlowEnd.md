---
sidebar_position: 2
custom_edit_url: ""
---
# Akış Bitişi

Akış bitişi nesnesi, tasarlanan sürecin bittiği adımı belirten nesnedir. Akış tasarımında akışın sonlanması istenen yerlere bu nesne yerleştirilir.

Akış tasarım ekranında bulunan nesneye tıklandığında, Özellik Görüntüleyici panelinde, nesne özellikleri görünür.

![Akış Bitişi](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbc108115-d668-421b-80b9-2a5682975278)

Akış Bitişi nesnesine tıklandığında Özellik Görüntüleyici panelinde "Appearance", "Properties" ve "Events" sekmeleri bulunmaktadır.

## Appearance

### Text Configs 

`Object Name` - Nesnenin sistem tarafında kullanılacak ismidir. Kod tarafında nesneye, nesne adı alanında yazan değerle erişim sağlanır.

`Caption` - Nesnenin başlık metninin girildiği alandır.

`Is Lock` - Tasarım anında nesnenin yeri değiştirilmesin isteniyorsa bu alan aktif edilir.

`Size` - Nesnenin genişlik ve yükseklik ayarlarının yapıldığı kısımdır.


## Properties

### Status

`Update Flow Status as Finished` -  Akış bittiğinde akışın durum bilgisinin **“Bitti”** olarak set edilmesini sağlar. Bu bölüm işaretli iken, Akış Bitişi nesnesinden önce **[Akış Durumu](./FlowState.md)** nesnesi kullanılarak akış durumu değiştirildiyse, bu değişiklik ezilir ve durum, **“Bitti”** olarak güncellenir. Eğer akış bitse dahi **Akış Durumu nesnesi ile set edilen durum ezilmesin isteniyorsa **bu seçenek işaretlenmemelidir**.

`Set Flow Status as Deleted` -  Akışın sistemde silindi olarak set edilmesini sağlar. Genelde, iptal edilerek bitirilen ve sistemde **“Silindi”** olarak görünmesi istenen adımlar için kullanılır. Sürecin, onay adımlarından ilerlemiş ve normal olarak bitirilecek kolu, bu özelliğin işaretli olduğu Akış Bitiş nesnesine bağlanmamalıdır.

:::tip İPUCU

Silindi olarak set edilen akış ve forma ait veriler sistemden silinmez.

:::

:::info BİLGİ

Nesne üzerinde ekli özelliklerin doğru olduğu sistem tarafından kontrol edilmektedir. Eksik bir özellik bulunduğunda nesne üzerinde kırmızı ünlem ikonu gösterilerek, fare işaretçisi ile ikon üzerine gelindiğinde nelerin eksik veya hatalı olduğu görüntülenebilmektedir.

![Akış Bitişi](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload07f4b5bd-d3d2-4b21-af61-b7ac0d940a13)

:::

## Events

Akış Bitişi nesnesinin sahip olduğu olaylar, Özellik Görüntüleyici panelindeki "Events" sekmesinde yer almaktadır. Her bir olay, farklı çalışma anlarında tetiklenerek kendilerine özgü işlemleri gerçekleştirir. Bu olaylara geliştirici tarafından yazılan kodlar da ilgili olayın tetiklendiği anda çalıştırılır. Herhangi bir olaya kod yazmak için, Events sekmesinden ilgili olay satırına çift tıklanır. Ekran, “Akışadı.cs” isimli akış kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur. Geliştirici bu method içerisinde istediği kod bloğunu kurgulayabilir. Events sekmesinden tıklanarak kod tarafında methodu oluşturulmuş olayın yanında, method adı bilgisi otomatik oluşturularak, olayla method arasındaki ilişki belirtilmiş olur.

![Akış Bitişi](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf2503586-9b39-45b5-b074-4e7fc9e9c219)