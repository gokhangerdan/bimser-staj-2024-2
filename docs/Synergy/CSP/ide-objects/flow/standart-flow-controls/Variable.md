---
sidebar_position: 9
custom_edit_url: ""
---

# Değişken

Değişken nesnesi, tasarlanan süreç içinde form veya akış üzerindeki bir değerin saklanıp, akışın başka bir bölümünde kullanılmasını sağlayan nesnedir. Akış tasarımında sürükle bırak ile akışta bir alana nesne konulup, herhangi bir şekilde sürece bağlanmadan kullanılabilir.

Akış tasarım ekranında bulunan nesneye tıklandığında, Özellik Görüntüleyici panelinde, nesne özellikleri görünür.

![Değişken](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload26bfe09d-63e5-42b0-b281-c8f2a07716e5)

Değişken nesnesine tıklandığında Özellik Görüntüleyici panelinde "Appearance", "Properties" ve "Events" sekmeleri bulunmaktadır.

## Appearance

### Text Configs

`Object Name` - Nesnenin sistem tarafında kullanılacak ismidir. Kod tarafında nesneye, nesne adı alanında yazan değerle erişim sağlanır.

`Caption` - Nesnenin başlık metninin girildiği alandır.

`Is Lock` - Tasarım anında nesnenin yeri değiştirilmesin isteniyorsa bu alan aktif edilir.

`Size` - Nesnenin genişlik ve yükseklik ayarlarının yapıldığı kısımdır.

## Properties
 
### Variables

`Type` - Değişken içerisinde hangi türde veri tutulacağını belirlenmesi, tip seçeneği ile ayarlanmaktadır.  Listelenen seçenekler Metin, Tam Sayı, Ondalık Sayı, Tarih, Para ve Doğru/Yanlış’tır.

`Value Type ` - Değişken içinde bir değerin otomatik olarak atanması için kullanılmaktadır. Alanda Sabit değer seçimi yapılıldığında bu değerin girildiği alan (Value) görünür hale gelmektedir. Yeni Değişken nesnesi akışa eklendiğinde Sabit değer seçimi otomatik olarak gelmektedir.

`Value ` - Değişkene tanımlanacak bir sabit değerin girildiği alandır.

### Link

`General` - Değişkenin genel (public) veya gizli (private) türünde olması için kullanılmaktadır. General seçeneği işarelendiğinde nesne dışarıdan erişilebilir hale gelmektedir.

`Target Document` - Değişken içine form üzerinden bir değer alınmak isteniyorsa, bu değerin olduğu doküman nesnesinin seçildiği alandır.

`Target Object` - Target Document içinde seçilen formdaki hangi nesne içindeki değer alınması isteniyorsa, seçimi bu alanda yapılmaktadır.

## Events

Değişken nesnesinin sahip olduğu olaylar, Özellik Görüntüleyici panelindeki "Events" sekmesinde yer almaktadır. Her bir olay, farklı çalışma anlarında tetiklenerek kendilerine özgü işlemleri gerçekleştirir. Bu olaylara geliştirici tarafından yazılan kodlar da ilgili olayın tetiklendiği anda çalıştırılır. Herhangi bir olaya kod yazmak için, Events sekmesinden ilgili olay satırına çift tıklanır. Ekran, “Akışadı.cs” isimli akış kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur. Geliştirici bu method içerisinde istediği kod bloğunu kurgulayabilir. Events sekmesinden tıklanarak kod tarafında methodu oluşturulmuş olayın yanında, method adı bilgisi otomatik oluşturularak, olayla method arasındaki ilişki belirtilmiş olur.

![Değişken](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload163f7d3b-dc2f-4f98-9660-bbf5dc243f4c)