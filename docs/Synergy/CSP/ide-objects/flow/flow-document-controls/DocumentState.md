---
sidebar_position: 3
custom_edit_url: ""
---

# Belge Durumu

Belge Durumu nesnesi, akış tasarımında bulunan Doküman nesnelerinin durumlarını, akış üzerinde istenilen bir noktada değiştirmek amacı ile kullanılır.

Araç kutusu panelinden Belge Durumu nesnesi sürüklenip akış üzerine bırakılır. Akış tasarım ekranında bulunan nesneye tıklandığında, Özellik Görüntüleyici panelinde, nesne özellikleri görünür. 

Belge Durumu nesnesine tıklandığında Özellik Görüntüleyici panelinde "Appearance", "Properties" ve "Events" sekmeleri bulunmaktadır.

![Belge Durumu](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfb789b77-80fa-475f-bb19-482824f89836)

## Appearance

### Text Configs

`Object Name` - Nesnenin sistem tarafında kullanılacak ismidir. Kod tarafında nesneye, nesne adı alanında yazan değerle erişim sağlanır.

`Caption` - Nesnenin başlık metninin girildiği alandır.

`Is Lock` - Tasarım anında nesnenin yeri değiştirilmesin isteniyorsa bu alan aktif edilir.

`Size` - Nesnenin genişlik ve yükseklik ayarlarının yapıldığı kısımdır.

## Properties

### Status and Position

`Position` -  Alanda akış tasarımında bulunan Akışı Başlatan nesnesi ve Pozisyon nesneleri listelenir. Belgedeki durum değişikliğini kimin yaptığı gösterilmek isteniyorsa bu sekmeden bir Pozisyon seçilmesi gereklidir.

`Status List` - Alanda durumu değiştirilecek Doküman nesneleri ve bu Doküman nesnelerinin yeni durumları seçilir. Bu sekmede bulunan listeye birden fazla satır eklemek yani birden fazla Doküman durumunu değiştirmek mümkündür.

:::info BİLGİ

Nesne üzerinde ekli özelliklerin doğru olduğu sistem tarafından kontrol edilmektedir. Eksik bir özellik bulunduğunda nesne üzerinde kırmızı ünlem ikonu gösterilerek, fare işaretçisi ile ikon üzerine gelindiğinde nelerin eksik veya hatalı olduğu görüntülenebilmektedir.

![Belge Durumu](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb84f0c5c-f457-4e40-9a4e-608f40907409)

:::

## Events

### Events

Belge Durumu nesnesinin sahip olduğu olaylar, Özellik Görüntüleyici panelindeki "Events" sekmesinde yer almaktadır. Her bir olay, farklı çalışma anlarında tetiklenerek kendilerine özgü işlemleri gerçekleştirir. Bu olaylara geliştirici tarafından yazılan kodlar da ilgili olayın tetiklendiği anda çalıştırılır. Herhangi bir olaya kod yazmak için, Olaylar sekmesinden ilgili olay satırına çift tıklanır. Ekran, “Akışadı.cs” isimli akış kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur. Geliştirici bu method içerisinde istediği kod bloğunu kurgulayabilir. Olaylar sekmesinden tıklanarak kod tarafında methodu oluşturulmuş olayın yanında, method adı bilgisi otomatik oluşturularak, olayla method arasındaki ilişki belirtilmiş olur.

![Belge Durumu](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8749178b-4c09-43df-ab8d-20ee1fa6f790)