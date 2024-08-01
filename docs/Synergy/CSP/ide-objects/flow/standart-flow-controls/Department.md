---
sidebar_position: 8
custom_edit_url: ""
---
# Departman

Departman nesnesi, akış içerisinde bir departman değerini saklamak için kullanılan nesnedir. İçeriği sabit olarak belirlenebileceği gibi akış sırasında dinamik olarak da değiştirilebilir.

Departman nesnesi içeriğine değer atamak için **[Atama](./Assignment.md)** nesnesi, departman nesnesindeki değeri karşılaştırmak için **[Karşılaştırma](./Compare.md)** nesnesi ile birlikte kullanılabilir.

Akış tasarımında Departman nesnesinden ok çıkarılmaz veya başka bir nesneden çıkan ok Departman nesnesine bağlanmaz. Departman nesnesi sadece departman bilgisini saklamak amacı ile kullanılır.

Akış tasarım ekranında bulunan nesneye tıklandığında, Özellik Görüntüleyici panelinde, nesne özellikleri görünür.

![Departman](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload29205566-40d9-4535-8557-b0eeadfed7b0)

Departman nesnesine tıklandığında Özellik Görüntüleyici panelinde "Appearance", "Properties" ve "Events" sekmeleri bulunmaktadır.

## Appearance

### Text Configs

`Object Name` - Nesnenin sistem tarafında kullanılacak ismidir. Kod tarafında nesneye, nesne adı alanında yazan değerle erişim sağlanır.

`Caption` - Nesnenin başlık metninin girildiği alandır.

`Is Lock` - Tasarım anında nesnenin yeri değiştirilmesin isteniyorsa bu alan aktif edilir.

`Size` - Nesnenin genişlik ve yükseklik ayarlarının yapıldığı kısımdır.

## Properties

### Value

Departman nesnesinin başlangıç değerinin ayarlanacağı sekmedir. Bu sekme yardımıyla departman nesnesine sabit bir değer verilebilir.

`Type` -   Departman nesnesinde tutulacak departman değerinin seçildiği alandır. Tip alanında “Sabit departman” ve “Akış başlatan departmanı” olarak iki seçenek listelenmektedir.

![Departman](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9e7b26e8-5287-4014-a9c3-11eebb84ec2b)

Type alanından **“Sabit departman”** seçeneği seçildiğinde, sistemde tanımlı tüm departman kayıtlarının listelendiği bir departman seçimi alanı, Select Department, açılacaktır. Bu alandan seçilen departman tanımı, Departman nesnesinde saklanmış olur.

Type alanından **“Akış Başlatanın Departmanı”** seçeneği seçildiğinde, Departman nesnesi, akışı başlatan kullanıcının departmanını saklamış olur.

:::info BİLGİ

Nesne üzerinde ekli özelliklerin doğru olduğu sistem tarafından kontrol edilmektedir. Eksik bir özellik bulunduğunda nesne üzerinde kırmızı ünlem ikonu gösterilerek, fare işaretçisi ile ikon üzerine gelindiğinde nelerin eksik veya hatalı olduğu görüntülenebilmektedir.

![Departman](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload59ea07b3-cb7f-44bf-9cd6-1d9ac96e3de4)

:::

## Events

Departman nesnesinin sahip olduğu olaylar, Özellik Görüntüleyici panelindeki "Events" sekmesinde yer almaktadır. Her bir olay, farklı çalışma anlarında tetiklenerek kendilerine özgü işlemleri gerçekleştirir. Bu olaylara geliştirici tarafından yazılan kodlar da ilgili olayın tetiklendiği anda çalıştırılır. Herhangi bir olaya kod yazmak için, Events sekmesinden ilgili olay satırına çift tıklanır. Ekran, “Akışadı.cs” isimli akış kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur. Geliştirici bu method içerisinde istediği kod bloğunu kurgulayabilir. Events sekmesinden tıklanarak kod tarafında methodu oluşturulmuş olayın yanında, method adı bilgisi otomatik oluşturularak, olayla method arasındaki ilişki belirtilmiş olur.

![Departman](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadafb4d706-a3b7-458a-a572-13e6946a404d)