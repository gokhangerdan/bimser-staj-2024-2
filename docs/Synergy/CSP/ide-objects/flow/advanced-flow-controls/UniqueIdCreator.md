---
sidebar_position: 3
custom_edit_url: ""
---

# Numaratör

Numaratör nesnesi, akış tasarımının istenen bir adımında, belirli bir formatta numara üretmeye yarayan nesnedir. Proje formları için Form Özelliklerindeki  Kimlik alanından belirlenen özel formatlı Form Id yapısında numaralar üretip, akıştaki başka bir nesnede bu ürettiği numarayı tutmaya yarar.

Akış tasarım ekranında bulunan nesneye tıklandığında, Özellik Görüntüleyici panelinde, nesne özellikleri görünür. 

Numaratör nesnesine tıklandığında Özellik Görüntüleyici panelinde "Appearance", "Properties" ve "Events" sekmeleri bulunmaktadır.

![Numaratör](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaf05117d-6229-4405-93cc-6128b7a3d6d9)

## Appearance

### Text Configs

`Object Name` - Nesnenin sistem tarafında kullanılacak ismidir. Kod tarafında nesneye, nesne adı alanında yazan değerle erişim sağlanır.

`Caption` - Nesnenin başlık metninin girildiği alandır.

`Is Lock` - Tasarım anında nesnenin yeri değiştirilmesin isteniyorsa bu alan aktif edilir.

`Size` - Nesnenin genişlik ve yükseklik ayarlarının yapıldığı kısımdır.

## Properties

### Identity

`Format` -   Biçim özelliğindeki üç noktaya basıldığında, sistemde tanımlı tüm formlar ve bu formlarda seçilmiş özel format id yapıları listelenir. Numaratör nesnesi ile hangi formun kimlik formatında numaralar üretilmek isteniyorsa buradan o format ve form seçimi yapılmalıdır.

`Target` -   Hedef kısmında, akış tasarımına eklenmiş nesneler listelenir. Üretilen numara hangi akış nesnesinde tutulacaksa, buradan o akış nesnesi seçimi yapılacaktır. 

Genel olarak üretilen numaralar, akışta bulunan **[Değişken](standart-flow-controls/Variable.md)** nesneleri üzerinde tutulur ve bu nesne üzerinden işlem yapılır. 

Akış, Numaratör nesnesinden geçtikten sonra içinde tanımlı formatta bir numara üretip seçilen hedef nesneye bu numara atanır. Hedef nesneye değer atamasının ardından **[Doküman No Atama](flow-document-controls/SetDocumentId.md)** nesnesi içinde Properties sekmesindeki "Type:From Variable Object" olarak seçilip, Format/Object alanında numaratör nesnesinde seçilen hedef nesne seçilmelidir.

:::info BİLGİ

Nesne üzerinde ekli özelliklerin doğru olduğu sistem tarafından kontrol edilmektedir. Eksik bir özellik bulunduğunda nesne üzerinde kırmızı ünlem ikonu gösterilerek, fare işaretçisi ile ikon üzerine gelindiğinde nelerin eksik veya hatalı olduğu görüntülenebilmektedir.

![Numaratör](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload11c00b2f-3128-4aac-a83d-0b4387d259f6)

:::

## Events

Numaratör nesnesinin sahip olduğu olaylar, Özellik Görüntüleyici panelindeki "Events" sekmesinde yer almaktadır. Her bir olay, farklı çalışma anlarında tetiklenerek kendilerine özgü işlemleri gerçekleştirir. Bu olaylara geliştirici tarafından yazılan kodlar da ilgili olayın tetiklendiği anda çalıştırılır. Herhangi bir olaya kod yazmak için, Olaylar sekmesinden ilgili olay satırına çift tıklanır. Ekran, “Akışadı.cs” isimli akış kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur. Geliştirici bu method içerisinde istediği kod bloğunu kurgulayabilir. Olaylar sekmesinden tıklanarak kod tarafında methodu oluşturulmuş olayın yanında, method adı bilgisi otomatik oluşturularak, olayla method arasındaki ilişki belirtilmiş olur.

![Numaratör](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7b72d6ca-b362-47f7-9e89-22f74850ecb7)