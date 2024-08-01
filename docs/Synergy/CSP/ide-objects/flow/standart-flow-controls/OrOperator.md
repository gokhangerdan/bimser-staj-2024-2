---
sidebar_position: 13
custom_edit_url: ""
---

# Veya Operatörü

Veya operatörü nesnesi, birden fazla pozisyonun onayına gönderildiği veya kollara ayrılarak farklı işlem adımlarının paralel yapılmasının ardından, herhangi bir koldan sonuç döndükten sonra akışın devam etmesinin istendiği durumlarda kullanılan bir nesnedir. Akış tasarımında kollara ayrılmış işlem adımlarının tek bir kolda birleştirmek için kullanılır.

Akış, **nesneye bağlı kollardan bir tanesinden sonuç döndüğünde** ilerletilir ve sonraki adımlara geçer, herhangi bir sonuç gelmediği sürece bir işlemin tamamlanıp sonuç gelene kadar nesne üzerinde beklemede kalır. Veya operatörüne n adet bağlantı kolu bağlanılabilir ancak nesneden sadece bir adet ok çıkarılabilir.

Akış tasarım ekranında bulunan nesneye tıklandığında, Özellik Görüntüleyici panelinde, nesne özellikleri görünür.

![Veya Operatörü](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9bf6ebab-8d0d-45b4-8fb2-fab4436cf433)

Veya Operatörü nesnesine tıklandığında Özellik Görüntüleyici panelinde "Appearance" ve "Events" sekmeleri bulunmaktadır.

## Appearance

### Text Configs

`Object Name` - Nesnenin sistem tarafında kullanılacak ismidir. Kod tarafında nesneye, nesne adı alanında yazan değerle erişim sağlanır.

`Caption` - Nesnenin başlık metninin girildiği alandır.

`Is Lock` - Tasarım anında nesnenin yeri değiştirilmesin isteniyorsa bu alan aktif edilir.

`Size` - Nesnenin genişlik ve yükseklik ayarlarının yapıldığı kısımdır.

:::info BİLGİ

Nesne üzerinde ekli özelliklerin doğru olduğu sistem tarafından kontrol edilmektedir. Eksik bir özellik bulunduğunda nesne üzerinde kırmızı ünlem ikonu gösterilerek, fare işaretçisi ile ikon üzerine gelindiğinde nelerin eksik veya hatalı olduğu görüntülenebilmektedir.

![Veya Operatörü](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbd9b636c-6784-44ba-936c-4c566a0fce3e)

:::

## Events

Veya Operatörü nesnesinin sahip olduğu olaylar, Özellik Görüntüleyici panelindeki "Events" sekmesinde yer almaktadır. Her bir olay, farklı çalışma anlarında tetiklenerek kendilerine özgü işlemleri gerçekleştirir. Bu olaylara geliştirici tarafından yazılan kodlar da ilgili olayın tetiklendiği anda çalıştırılır. Herhangi bir olaya kod yazmak için, Events sekmesinden ilgili olay satırına çift tıklanır. Ekran, “Akışadı.cs” isimli akış kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur. Geliştirici bu method içerisinde istediği kod bloğunu kurgulayabilir. Events sekmesinden tıklanarak kod tarafında methodu oluşturulmuş olayın yanında, method adı bilgisi otomatik oluşturularak, olayla method arasındaki ilişki belirtilmiş olur.

![Veya Operatörü](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade4cfd455-2d6c-4aee-b645-459f0d49c78d)