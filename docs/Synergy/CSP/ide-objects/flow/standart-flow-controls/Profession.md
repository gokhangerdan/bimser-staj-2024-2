---
sidebar_position: 7
custom_edit_url: ""
---

# Unvan

Unvan nesnesi, akış içerisinde bir unvan değerini saklamak için kullanılan nesnedir. İçeriği sabit olarak belirlenebileceği gibi akış sırasında dinamik olarak da değiştirilebilir.

Unvan nesnesi içeriğine değer atamak için **[Atama](./Assignment.md)** nesnesi, unvan nesnesindeki değeri karşılaştırmak için **[Karşılaştırma](./Compare.md)** nesnesi ile birlikte kullanılabilir.

Akış tasarımında Unvan nesnesinden ok çıkarılmaz veya başka bir nesneden çıkan ok Unvan nesnesine bağlanmaz. Unvan nesnesi sadece unvan bilgisini saklamak amacı ile kullanılır.

Akış tasarım ekranında bulunan nesneye tıklandığında, Özellik Görüntüleyici panelinde, nesne özellikleri görünür.

![Unvan](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade91417d2-032d-48f4-a0f7-45b101d3e58f)

Unvan nesnesine tıklandığında Özellik Görüntüleyici panelinde "Appearance", "Properties" ve "Events" sekmeleri bulunmaktadır.

## Appearance

### Text Configs

`Object Name` - Nesnenin sistem tarafında kullanılacak ismidir. Kod tarafında nesneye, nesne adı alanında yazan değerle erişim sağlanır.

`Caption` - Nesnenin başlık metninin girildiği alandır.

`Is Lock` - Tasarım anında nesnenin yeri değiştirilmesin isteniyorsa bu alan aktif edilir.

`Size` - Nesnenin genişlik ve yükseklik ayarlarının yapıldığı kısımdır.

## Properties
 
### Value

Unvan nesnesinin başlangıç değerinin ayarlanacağı sekmedir. Bu sekmede, unvan nesnesine sabit bir değer verilebilir.

`Type` - Unvan nesnesinde tutulacak unvan değerinin seçildiği alandır. Tip alanında **“Sabit unvan”** ve **“Akış Başlatan Unvanı”** olarak iki seçenek listelenmektedir.

![Unvan](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload248fabe7-7d8e-45e6-9b68-3a2829bbd296)

Type alanından **“Sabit Unvan”** seçeneği seçildiğinde, sistemde tanımlı tüm unvan kayıtlarının listelendiği bir unvan seçimi alanı, Constant Title, açılacaktır. Bu alandan seçilen unvan tanımı, Unvan nesnesinde saklanmış olur.

Type alanından **“Akış Başlatan Unvanı”** seçeneği seçildiğinde, Unvan nesnesi, akışı başlatan kullanıcının unvanını saklamış olur.

:::info BİLGİ

Nesne üzerinde ekli özelliklerin doğru olduğu sistem tarafından kontrol edilmektedir. Eksik bir özellik bulunduğunda nesne üzerinde kırmızı ünlem ikonu gösterilerek, fare işaretçisi ile ikon üzerine gelindiğinde nelerin eksik veya hatalı olduğu görüntülenebilmektedir.

![Unvan](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3f561d9e-4f04-4f53-baac-6b3498cb04ee)

:::

## Events

Unvan nesnesinin sahip olduğu olaylar, Özellik Görüntüleyici panelindeki "Events" sekmesinde yer almaktadır. Her bir olay, farklı çalışma anlarında tetiklenerek kendilerine özgü işlemleri gerçekleştirir. Bu olaylara geliştirici tarafından yazılan kodlar da ilgili olayın tetiklendiği anda çalıştırılır. Herhangi bir olaya kod yazmak için, Events sekmesinden ilgili olay satırına çift tıklanır. Ekran, “Akışadı.cs” isimli akış kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur. Geliştirici bu method içerisinde istediği kod bloğunu kurgulayabilir. Events sekmesinden tıklanarak kod tarafında methodu oluşturulmuş olayın yanında, method adı bilgisi otomatik oluşturularak, olayla method arasındaki ilişki belirtilmiş olur.

![Unvan](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload04e7c55d-a2b9-45f9-870e-ece57c7059e9)