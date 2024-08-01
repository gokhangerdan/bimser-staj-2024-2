---
sidebar_position: 1
custom_edit_url: ""
---

# Fonksiyon

Fonksiyon nesnesi, süreç adımlarının herhangi bir aşamasında gerçekleştirilmek istenen işlemlerin kodunu çalıştırmak için kullanılan, akış kod kısmına kendi methodunu açarak içerisine kod yazılan nesnedir.

Süreç işleyişinde akışın fonksiyon nesnesinden geçtiği adımlarda, fonksiyon nesnesi içinde yazılmış olan kod çalıştırılır ve geliştiricinin kod bloğu ile yaptırmak istediği işlemler gerçekleştirilmiş olur. Harici bir ortama veya veri tabanına veri atma, web servisten veri okuma, akış ya da formdaki verilere erişme veya güncelleme gibi birçok amaçla kullanılmak istenen kodu, akışın istenen adımında gerçekleştirmeyi sağlayan nesnedir.

Akış tasarım ekranında bulunan nesneye tıklandığında, Özellik Görüntüleyici panelinde, nesne özellikleri görünür.

Fonksiyon nesnesine tıklandığında Özellik Görüntüleyici panelinde "Appearance", "Properties" ve "Events" sekmeleri bulunmaktadır.

![Fonksiyon](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload06749b68-135f-4ca9-934f-c44cb4bf2291)

## Appearance

### Text Configs

`Object Name` - Nesnenin sistem tarafında kullanılacak ismidir. Kod tarafında nesneye, nesne adı alanında yazan değerle erişim sağlanır.

`Caption` - Nesnenin başlık metninin girildiği alandır.

`Is Lock` - Tasarım anında nesnenin yeri değiştirilmesin isteniyorsa bu alan aktif edilir.

`Size` - Nesnenin genişlik ve yükseklik ayarlarının yapıldığı kısımdır.

## Properties

### Value

`Type` - Geri dönüş değerine sahip fonksiyon nesnesinin dönüş değerinin alfanumerik mi, numerik mi yoksa lojik bir değer mi olacağı bilgisi bu sekmeden ayarlanır. Type alanında; Metin, Tam sayı, Ondalık sayı, Tarih, Para ve Doğru/Yanlış tipleri listelenir.

`Value Type` - Fonksiyondan dönen geri dönüş değerine sabit bir değer verilmek isteniyorsa bu alandan “Sabit değer” seçeneği seçilir.

`Value` - Value Type alanında Sabit değer seçeneği seçildiğinde kullanılacak alandır. “Value” alanına, sabit değer verisi girilebilir.

### Action

`Continue If Error Occurs` - Akış, fonksiyon nesnesinden geçtiğinde fonksiyonun içine yazılan kod bloğu çalıştırılır. Bu kod bloğunda herhangi bir hata ile karşılaşıldığında, akışın hata vermeden devam etmesi isteniyorsa bu alan işaretlenir. Fonksiyon nesnesinden çıkarılan ilk bağlantı kolu, akış fonksiyon nesnesindeki kodu başarıyla çalıştırıp sonraki adıma ilerleyeceği nesneye bağlanır. Fonksiyon nesnesinden çıkarılan ikinci bağlantı kolu ise “ContinueWhenErrorOccurs” koludur. Fonksiyonda herhangi bir hata olduğunda akış “ContinueWhenErrorOccurs” kolunun bağlandığı akış nesnesinden devam edecektir.

`Error Description Object` - Fonksiyonda bir hata ile karşılaşıldığında, hatanın detaylı metninin atandığı bir Değişken nesnesi bu alandan seçilebilir. Böylece hata mesajı, geliştiricinin kendi belirlediği ve anlaması kolay bir metin olmuş olacaktır.

:::info BİLGİ

Nesne üzerinde ekli özelliklerin doğru olduğu sistem tarafından kontrol edilmektedir. Eksik bir özellik bulunduğunda nesne üzerinde kırmızı ünlem ikonu gösterilerek, fare işaretçisi ile ikon üzerine gelindiğinde nelerin eksik veya hatalı olduğu görüntülenebilmektedir.

![Fonksiyon](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadca577a65-f2ae-458a-8c90-69a12f69ae39)

:::

## Olaylar

Fonksiyon nesnesinin amacı; akış sırasında fonksiyon çağrıldığında “Execute” olayını tetiklemek ve geliştirici kullanıcıların bu olay altına yazmış oldukları kod bloğu işlevini yerine getirmektir.

Olaylar sekmesinden “Execute” olayına çift tıklandığında ekran, “Akışadı.cs” isimli akış kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur. Geliştirici bu method içerisinde istediği kod bloğunu kurgulayabilir. Olaylar sekmesinden tıklanarak kod tarafında methodu oluşturulmuş olayın yanında, method adı bilgisi otomatik oluşturularak, olayla method arasındaki ilişki belirtilmiş olur.

![Fonksiyon](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5f0345ec-1317-43c4-a8cc-1f89eb2f34ad)