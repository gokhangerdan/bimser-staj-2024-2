---
sidebar_position: 4
custom_edit_url: ""
---

# Senkronize Edici 

Senkronize Edici nesnesi, iki doküman nesnesi arasında dokümanların bağlı olduğu formlar üzerindeki alanları, formlar üzerindeki tablo, detaylar ve detay tablo nesnelerini birbirleriyle senkronize eden bir nesnedir.

Araç kutusu panelinden Senkronize Edici nesnesi sürüklenip akış üzerine bırakılır. Akış tasarım ekranında bulunan nesneye tıklandığında, Özellik Görüntüleyici panelinde, nesne özellikleri görünür.

Senkronize Edici nesnesine tıklandığında Özellik Görüntüleyici panelinde "Appearance", "Properties" ve "Events" sekmeleri bulunmaktadır.

![Senkronize Edici](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf292e12b-982e-4d5c-b25b-eee04de2e94f)

## Appearance

### Text Configs

`Object Name` - Nesnenin sistem tarafında kullanılacak ismidir. Kod tarafında nesneye, nesne adı alanında yazan değerle erişim sağlanır.

`Caption` - Nesnenin başlık metninin girildiği alandır.

`Is Lock` - Tasarım anında nesnenin yeri değiştirilmesin isteniyorsa bu alan aktif edilir.

`Size` - Nesnenin genişlik ve yükseklik ayarlarının yapıldığı kısımdır.

## Properties

### Value

`Type` - Senkronize Edici nesnesinin tipinin alfa numerik mi, numerik mi yoksa lojik bir değer mi olacağı bilgisi bu sekmeden ayarlanır. Tip alanında; Metin, Tam sayı, Ondalık sayı, Tarih, Para ve Doğru/Yanlış tipleri listelenmektedir.

`Value Type` - Sabit bir değer verilmek isteniyorsa değer türü olarak “Sabit değer” seçeneği seçilmektedir.

`Value` - Value Type alanında seçilen Sabit değerin tanımlandığı alandır.

### Action

`Continue If Error Occurs` - Süreç Senkronize Edici nesnesinden geçtiğinde nesne metodunun içinde yazılan kod bloğu çalıştırılıp, bu kodda herhangi bir hata ile karşılaşıldığında, web ara yüzünde sürecin hata vermeden devam etmesi isteniyorsa işaretlenir.

`Error Description Object` - Senkronize Edici nesnesi kodlarında bir hata ile karşılaşıldığında, hatanın detaylı metninin atandığı bir Değişken nesnesi bu alandan seçilmektedir.

### Synchronization


`Source Type` - Hangi veri türünün senkronizasyon işleminde kaynak olarak kullanılacağının seçiminin yapıldığı alandır. Listelenen öge Doküman seçeneğidir.

- Source Type olarak Doküman seçiminde, form üzerindeki verilerin senkronize edileceği anlamına gelmektedir.

`Source Document` - Akış üzerindeki hangi form kaynak olarak kullanılmak isteniyorsa seçildiği alandır.

`Target Type` - Alanda, kaynak kısmında seçilen verilerin aktarılacağı hedef belirlenmektedir. Listelenen öge Doküman seçeneğidir..

- Target Type olarak seçeneği, form üzerindeki verilerin senkronize edileceği anlamına gelmektedir.

`Target Document` - Akış üzerindeki hangi form hedef olarak kullanılmak isteniyorsa, bunun seçildiği alandır.

`Fields` - Kaynak ve Hedef alanlarında belirtilen alanların ilişkilendirilmesi bu bölümden yapılır. Kaynaktaki alanlar, hedefteki hangi alana denk geldiği tanımı yapılarak, alan eşleştirmeleri gerçekleştirilir.

![Senkronize Edici](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc828dae6-d73f-4756-9df8-e4e4d19b3acf)

:::info BİLGİ

Nesne üzerinde ekli özelliklerin doğru olduğu sistem tarafından kontrol edilmektedir. Eksik bir özellik bulunduğunda nesne üzerinde kırmızı ünlem ikonu gösterilerek, fare işaretçisi ile ikon üzerine gelindiğinde nelerin eksik veya hatalı olduğu görüntülenebilmektedir.

![Senkronize Edici](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload637ae9dd-12e0-4b83-a845-0b4174544b5f)

:::

## Events

### Events

Senkronize Edici nesnesinin sahip olduğu olaylar, Özellik Görüntüleyici panelindeki "Events" sekmesinde yer almaktadır. Her bir olay, farklı çalışma anlarında tetiklenerek kendilerine özgü işlemleri gerçekleştirir. Bu olaylara geliştirici tarafından yazılan kodlar da ilgili olayın tetiklendiği anda çalıştırılır. Herhangi bir olaya kod yazmak için, Olaylar sekmesinden ilgili olay satırına çift tıklanır. Ekran, “Akışadı.cs” isimli akış kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur. Geliştirici bu method içerisinde istediği kod bloğunu kurgulayabilir. Olaylar sekmesinden tıklanarak kod tarafında methodu oluşturulmuş olayın yanında, method adı bilgisi otomatik oluşturularak, olayla method arasındaki ilişki belirtilmiş olur.

![Senkronize Edici](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadda4e9b3f-ab45-4917-ae15-f1fba6e2d9b8)