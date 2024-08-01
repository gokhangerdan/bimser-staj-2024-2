---
sidebar_position: 5
custom_edit_url: ""
---

# Onay İptal Edici

Onay İptal Edici nesnesi ,iş sürecinin herhangi bir adımında yer alan aksiyon isteğini iptal  etmek amacıyla kullanılmaktadır. Temel kullanım amacı herhangi bir Onay Kontrolünde bekleyen İş süreci adımını iptal ederek akışı farklı bir yönde devam ettirmektir.

Örneğin; Akıştaki bir Pozisyon nesnesine onay gönderildiğinde, nesnedeki kişi belirli bir süre içerisinde süreci ilerletmezse, bu süre sonunda ilgili pozisyon nesnesinde aksiyon için bekleyen istek, Onay İptal Edici nesnesi kullanılarak iptal edilip, akışın devam etmesi sağlanabilir. Veya akış senaryosuna göre herhangi bir nesnede bekleyen aksiyon isteğine gerek kalmadığı durumlarda bekleyen istek bu nesne kullanılarak iptal edilebilir.

Akış tasarım ekranında bulunan nesneye tıklandığında, Özellik Görüntüleyici panelinde, nesne özellikleri görünür.

Onay İptal Edici nesnesine tıklandığında Özellik Görüntüleyici panelinde "Appearance", "Properties" ve "Events" sekmeleri bulunmaktadır.

![Onay İptal Edici](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2e4ef7e6-315e-4f8d-a32b-8652f9f56074)
 
## Appearance

### Text Configs

`Object Name` - Nesnenin sistem tarafında kullanılacak ismidir. Kod tarafında nesneye, nesne adı alanında yazan değerle erişim sağlanır.

`Caption` - Nesnenin başlık metninin girildiği alandır.

`Is Lock` - Tasarım anında nesnenin yeri değiştirilmesin isteniyorsa bu alan aktif edilir.

`Size` - Nesnenin genişlik ve yükseklik ayarlarının yapıldığı kısımdır.

## Properties

### Approval

`Target Type` - Bu alandan, bekleyen aksiyon kaydı reddedilmek istenen nesnenin seçimi yapılır. Bu alanda, akış tasarım ekranında bulunan **Grup, Akış Durdurucu, Pozisyon** gibi kendinden aksiyon beklenen nesne türü seçilmelidir. Yapılan seçim türüne göre Target Object alanı görünür hale geçer.

Ayrıca herhangi bir adım gözetmeksizin **“Tümü”** seçeneği kullanılarak, iş süreci o adımda hangi Onay Kontrolünde olursa olsun tüm bekleyen onayları iptal edip akışın, ilgili **“Onay İptal Edici”** nesnesinden devam etmesi sağlanabilir.

`Target Object` - Target Type alanında **Grup, Akış Durdurucu, Pozisyon** seçimlerinden biri yapıldığında görünen alandır. Target Type alanında seçilen türe göre akış nesneleri listelenir. Hangi nesnede bekleyen işlem iptal edilmek isteniyorsa ilgili nesnenin seçimi yapılır.

![Onay İptal Edici](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9b2c4eaa-000c-40ef-b201-73074e7375be)
![Onay İptal Edici](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload96cf4143-21af-44a6-9b4b-2b742c0e4b79)
![Onay İptal Edici](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcddde2e5-7607-4337-a748-e6e9cb408f32)

:::info BİLGİ

Nesne üzerinde ekli özelliklerin doğru olduğu sistem tarafından kontrol edilmektedir. Eksik bir özellik bulunduğunda nesne üzerinde kırmızı ünlem ikonu gösterilerek, fare işaretçisi ile ikon üzerine gelindiğinde nelerin eksik veya hatalı olduğu görüntülenebilmektedir.

![Onay İptal Edici](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6e6f5096-d7b7-4257-b7ef-b4afe0ffa21c)

:::

## Events

Onay İptal Edici nesnesinin sahip olduğu olaylar, Özellik Görüntüleyici panelindeki "Events" sekmesinde yer almaktadır. Her bir olay, farklı çalışma anlarında tetiklenerek kendilerine özgü işlemleri gerçekleştirir. Bu olaylara geliştirici tarafından yazılan kodlar da ilgili olayın tetiklendiği anda çalıştırılır. Herhangi bir olaya kod yazmak için, Olaylar sekmesinden ilgili olay satırına çift tıklanır. Ekran, “Akışadı.cs” isimli akış kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur. Geliştirici bu method içerisinde istediği kod bloğunu kurgulayabilir. Olaylar sekmesinden tıklanarak kod tarafında methodu oluşturulmuş olayın yanında, method adı bilgisi otomatik oluşturularak, olayla method arasındaki ilişki belirtilmiş olur.

![Onay İptal Edici](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc7b0eb5c-b2b9-4140-ac5f-e1b184458956)