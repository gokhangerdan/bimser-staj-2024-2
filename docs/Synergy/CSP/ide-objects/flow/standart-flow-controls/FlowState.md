---
sidebar_position: 10
custom_edit_url: ""
---

# Akış Durumu

Akışın belirli aşamalarında, akış durumunu set etmek için, Akış Durumu nesnesi kullanılır. **[Flow Properties->Statuses](index.mdx#statuses)** sekmesinde belirlenen akış durum tanımları, Akış Durumu nesnesi içerisinden durum olarak seçilmektedir.

Nesnenin kullanımı, akışın hangi adımda olduğunu **takip etmeyi** ve süreç durumu bazlı **raporlar almayı** sağlar. Akışta istenilen adımdan sonra bu nesne kullanılarak, akışın o an hangi durumda olduğu, o akış için kayıtlı durumlar arasından seçilerek ayarlanabilir.

Akış tasarım ekranında bulunan nesneye tıklandığında, Özellik Görüntüleyici panelinde, nesne özellikleri görünür.

![Akış Durumu](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb1ceb6ba-231e-4f87-80c1-97bcf16025e3)

Akış Durumu nesnesine tıklandığında Özellik Görüntüleyici panelinde "Appearance", "Properties" ve "Events" sekmeleri bulunmaktadır.

## Appearance

### Text Configs

`Object Name` - Nesnenin sistem tarafında kullanılacak ismidir. Kod tarafında nesneye, nesne adı alanında yazan değerle erişim sağlanır.

`Caption` - Nesnenin başlık metninin girildiği alandır.

`Is Lock` - Tasarım anında nesnenin yeri değiştirilmesin isteniyorsa bu alan aktif edilir.

`Size` - Nesnenin genişlik ve yükseklik ayarlarının yapıldığı kısımdır.

## Properties
 
### Documents

`Status ` - Bu alanda Akış Özelliklerinde yer alan **"Statuses"** alanında kayıtlı akış durumları listelenir. Akış durumu nesnesinde akışın set edilmek istendiği durum tanımı, bu listeden seçilir. Akış, bu nesneden geçtiğinde akışın durumu, nesnede seçili durum olarak güncellenir. Web arayüzünde akış tarihçesi kısmında ve akış bilgileri alanında akışın durum bilgisi gösterilmektedir.

Akış özelliklerinde durumlar alanına “Sözleşme Onaylandı”, isimli bir durum ekleyelim.

![Akış Durumu](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload54ef78dd-33a6-4cd5-b4d8-09b55a40bde6)

Eklenen yeni durum, Akış Durumu nesnesine seçilebilir.

![Akış Durumu](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1e5ba4af-6cde-49d9-a123-61597c2cdf6f)

Böylece akış, bu Akış Durumu nesnesinden geçtiği anda, akışın durumu “Sözleşme Onaylandı” olarak güncellenecektir.

![Akış Durumu](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload59f2cabc-9646-4a3b-8d21-6581b5165a47)

`Show in the Flow History ` - Eklenen Akış Durumu nesnesinin web ara yüzünde akış tarihçesi üzerinde gözükmesi istenirse seçilmesi gereken alandır.

:::info BİLGİ

Nesne üzerinde ekli özelliklerin doğru olduğu sistem tarafından kontrol edilmektedir. Eksik bir özellik bulunduğunda nesne üzerinde kırmızı ünlem ikonu gösterilerek, fare işaretçisi ile ikon üzerine gelindiğinde nelerin eksik veya hatalı olduğu görüntülenebilmektedir.

![Akış Durumu](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8d493c20-2a86-4c76-8087-715cee7cb201)

:::

## Events

Akış Durumu nesnesinin sahip olduğu olaylar, Özellik Görüntüleyici panelindeki "Events" sekmesinde yer almaktadır. Her bir olay, farklı çalışma anlarında tetiklenerek kendilerine özgü işlemleri gerçekleştirir. Bu olaylara geliştirici tarafından yazılan kodlar da ilgili olayın tetiklendiği anda çalıştırılır. Herhangi bir olaya kod yazmak için, Events sekmesinden ilgili olay satırına çift tıklanır. Ekran, “Akışadı.cs” isimli akış kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur. Geliştirici bu method içerisinde istediği kod bloğunu kurgulayabilir. Events sekmesinden tıklanarak kod tarafında methodu oluşturulmuş olayın yanında, method adı bilgisi otomatik oluşturularak, olayla method arasındaki ilişki belirtilmiş olur.

![Akış Durumu](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadddee69bf-9a3c-48a7-ae7f-1693118a4f69)