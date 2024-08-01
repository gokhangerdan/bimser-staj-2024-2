---
sidebar_position: 14
custom_edit_url: ""
---

# Düğüm Girişi & Düğüm Çıkışı

Düğüm Girişi nesnesi, akış tasarım ekranının anlaşılabilirliğini arttırmak için kullanılan bir nesnedir. Akışlar tasarlanırken bazı durumlarda bağlantı okları, nesnelerin yada birbirlerin üzerinden geçerek akış tasarımının görsel olarak anlaşılabilirliğini azaltır. Bu duruma önlem olarak geliştirilmiş giriş, çıkış düğümleri birlikte çalışarak, akış bir Düğüm Girişi ne yönlendirilir ve bağlantı oklarının nesnelerin üzerinden geçmesi engellenir.

Düğüm Girişi nesnesi, **Düğüm Çıkışı nesnesi ile birlikte** kullanılır. Akışa eklenen bir Düğüm Çıkışı nesnesine karşılık gelen bir tane de Düğüm Girişi nesnesi konur. Akış, bu Düğüm Girişine vardığında devam edeceği nokta, Düğüm Girişi nin bağlı olduğu Düğüm Çıkışıdır.

Akış tasarım ekranında bulunan nesneye tıklandığında, Özellik Görüntüleyici panelinde, nesne özellikleri görünür.

![Düğüm Girişi & Düğüm Çıkışı](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc5549e42-02a9-482c-81a2-b9e1e63ead62)

Düğüm Girişi nesnesine tıklandığında Özellik Görüntüleyici panelinde "Appearance", "Properties" ve "Events" sekmeleri bulunmaktadır.

:::caution DİKKAT

Düğüm Çıkışı nesnesine tıklandığında Özellik Görüntüleyici panelinde "Appearance" ve "Events" sekmeleri bulunmaktadır.

:::

## Appearance

### Text Configs

`Object Name` - Nesnenin sistem tarafında kullanılacak ismidir. Kod tarafında nesneye, nesne adı alanında yazan değerle erişim sağlanır.

`Caption` - Nesnenin başlık metninin girildiği alandır.

`Is Lock` - Tasarım anında nesnenin yeri değiştirilmesin isteniyorsa bu alan aktif edilir.

`Size` - Nesnenin genişlik ve yükseklik ayarlarının yapıldığı kısımdır.

## Properties

### Node In

`Node Name` - Bu alandan, ilgili Düğüm Girişi nesnesi ile birlikte çalışacak Düğüm Çıkışı nesnesi seçilir. Akış tasarım ekranına öncelikle Düğüm Çıkışı nesnesi eklenir ve bu düğüme bir ad verilir. Daha sonra akışa bir tane Düğüm Girişi nesnesi eklenir ve **Düğüm Girişi** nesnesinin “Düğüm Adı” alanında ilgili **Düğüm Çıkışı** nesnesinin adı seçilir.

Akış tasarım ekranında aynı Düğüm Çıkışına bağlı bir çok Düğüm Girişi bulunabilir. Ancak, aynı isimli Düğüm Çıkışı olamaz. Çünkü Düğüm Çıkışı akışın yönleneceği yeri bildirir bu yüzden tek olmalıdır. Düğüm Girişi ise akışın yönlendirilmek istendiği noktaya konulur. Akışın farklı adımlarında akışı aynı yere yönlendirme durumu olabileceği için aynı çıkışa bağlı Düğüm Girişi birden fazla olabilir. 

![Düğüm Girişi & Düğüm Çıkışı](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2aba091b-8c21-4fd4-9192-4c853d1bea87)

:::info BİLGİ

Nesne üzerinde ekli özelliklerin doğru olduğu sistem tarafından kontrol edilmektedir. Eksik bir özellik bulunduğunda nesne üzerinde kırmızı ünlem ikonu gösterilerek, fare işaretçisi ile ikon üzerine gelindiğinde nelerin eksik veya hatalı olduğu görüntülenebilmektedir.

![Düğüm Girişi & Düğüm Çıkışı](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload483e4313-afab-47ec-95a6-19970983e137)

:::

## Events

Düğüm Girişi & Düğüm Çıkışı nesnesinin sahip olduğu olaylar, Özellik Görüntüleyici panelindeki "Events" sekmesinde yer almaktadır. Her bir olay, farklı çalışma anlarında tetiklenerek kendilerine özgü işlemleri gerçekleştirir. Bu olaylara geliştirici tarafından yazılan kodlar da ilgili olayın tetiklendiği anda çalıştırılır. Herhangi bir olaya kod yazmak için, Events sekmesinden ilgili olay satırına çift tıklanır. Ekran, “Akışadı.cs” isimli akış kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur. Geliştirici bu method içerisinde istediği kod bloğunu kurgulayabilir. Events sekmesinden tıklanarak kod tarafında methodu oluşturulmuş olayın yanında, method adı bilgisi otomatik oluşturularak, olayla method arasındaki ilişki belirtilmiş olur.

![Düğüm Girişi & Düğüm Çıkışı](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload59ca62c8-1aaf-4f5e-a916-9a88a7aab745)

![Düğüm Girişi & Düğüm Çıkışı](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload96c9c033-edc6-4bb7-a9ab-bde83ae98675)