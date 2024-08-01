---
sidebar_position: 1
custom_edit_url: ""
---

# Doküman

Doküman nesnesi, tasarlanan süreçte tasarlanmış formların ve form üzerindeki bilgilerin tutulduğu nesnedir. Doküman nesnesi, akışa eklendiğinde bağlantı oku ile herhangi başka bir nesneye bağlanamaz ya da başka bir nesnenin oku Doküman nesnesine bağlamamaktadır. Nesne akış içinde; pozisyon, pozisyon grubu, bilgilendirme vb. gibi nesnelere doküman olarak eklenerek ilgili adımda doküman nesnesinin bağlı olduğu proje formunun görüntülenmesi sağlanır.

Akış tasarım ekranında bulunan nesneye tıklandığında, Özellik Görüntüleyici panelinde, nesne özellikleri görünür.

Doküman nesnesine tıklandığında Özellik Görüntüleyici panelinde "Appearance", "Properties" ve "Events" sekmeleri bulunmaktadır.

![Doküman](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0d2efda2-1ba3-4785-975c-65be0a9bb632)

## Appearance

### Text Configs

`Object Name` - Nesnenin sistem tarafında kullanılacak ismidir. Kod tarafında nesneye, nesne adı alanında yazan değerle erişim sağlanır.

`Caption` - Nesnenin başlık metninin girildiği alandır.

`Is Lock` - Tasarım anında nesnenin yeri değiştirilmesin isteniyorsa bu alan aktif edilir.

`Size` - Nesnenin genişlik ve yükseklik ayarlarının yapıldığı kısımdır.

## Properties

### Document

`Document Type` - Doküman nesnesinde tutulacak belgenin türü seçimi yapılır. Alanda **["Sabit belge"](#static-document)** ve **["Mevcut belge"](#existing-document)** seçenekleri listelenmektedir.

#### Sabit belge seçilirse {#static-document}

`Process` - Document Type alanında Sabit belge seçildi ise Süreç alanı görünür hale gelir. Hangi sürece ait doküman oluşturulmak isteniyorsa, listeden o süreç seçilmelidir.

`Form` - Document Type alanında Sabit Belge seçildi ise Süreç alanı görünür hale gelir. Süreç alanında seçilen sürecin içindeki formlar listelenmektedir.

`View` - Document Type alanında Sabit Belge seçildi ise Süreç alanı görünür hale gelir. Form alanında seçilen formun içinde bulunan görünümler listelenmektedir.

`Panel Size` - Seçilen formun web ara yüzünde görüntülenirken form panel tipinde açıldığında, panelin genişliğini belirlemek için kullanılır.

:::info BİLGİ

Panel genişliğindeki 1 değerini ekranın 1/3'ünü kaplayacak şekilde panel açılması, 2 değerini ekranın 2/3'ünü kaplayacak şekilde panel açılması, 3 değerini ise ekranın 3/3'ünü kaplayacak (tamamı) şekilde panel açılması anlamına gelir.

:::

`Parameters` - Seçilen proje-form içerine parametre değer gönderilerek form içinde bu parametrelerin kullanılması için tanımlama yapılan alandır.

Örneğin Documents nesnesinde tanımlı forma parametreler tanımlanarak akış tarafında Pozisyon, Pozisyon Grubu gibi nesnede tanımlı bir event için, Form alanında parametrenin tanımlandığı Doküman nesnesinin içerdiği forma nesneden veya sabit bir değer şeklinde parametre aktarımı yapılabilmektedir.

:::info BİLGİ

Documents nesnesi üzerinde forma gönderilen parametrelerin form içinde kullanılması için ResponseParameters (Client veya Server) metodu kullanılmalıdır.

Örnek server tarafı kullanımı;

```csharp
void Form1_OnLoad(object sender, LoadEventArgs e)
{
    if (ResponseParameters.TryGetValue("ParametreAdı", out object parametreValue))
    {
        //
    }
}
```

:::

#### Mevcut belge seçilirse {#existing-document}

`Path` - Doküman nesnesinde sistemde kayıtlı bir form tutulmak istenildiği durumda, alana tıklanarak, Doküman Yönetim Sistemi yapısından ilgili form dizini seçimi yapılır. Bu sayede sistem üzerinde daha önceden oluşturulmuş bir süreç formu Doküman nesnesinde tutulabilir.

`Panel Size` - Seçilen belgenin web ara yüzünde görüntülenirken form panel tipinde açıldığında, panelin genişliğini belirlemek için kullanılır.

:::info BİLGİ

Panel genişliğindeki 1 değerini ekranın 1/3'ünü kaplayacak şekilde panel açılması, 2 değerini ekranın 2/3'ünü kaplayacak şekilde panel açılması, 3 değerini ise ekranın 3/3'ünü kaplayacak (tamamı) şekilde panel açılması anlamına gelir.

:::

`Parameters` - Seçilen proje-form içerine parametre değer gönderilerek form içinde bu parametrelerin kullanılması için tanımlama yapılan alandır.

Örneğin Documents nesnesinde tanımlı forma parametreler tanımlanarak akış tarafında Pozisyon, Pozisyon Grubu gibi nesnede tanımlı bir event için, Form alanında parametrenin tanımlandığı Doküman nesnesinin içerdiği forma nesneden veya sabit bir değer şeklinde parametre aktarımı yapılabilmektedir.

:::info BİLGİ

Nesne üzerinde ekli özelliklerin doğru olduğu sistem tarafından kontrol edilmektedir. Eksik bir özellik bulunduğunda nesne üzerinde kırmızı ünlem ikonu gösterilerek, fare işaretçisi ile ikon üzerine gelindiğinde nelerin eksik veya hatalı olduğu görüntülenebilmektedir.

![Doküman](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload741ded6b-d0e6-48c0-a4d0-21c59cca982c)

:::

## Events

### Events

Doküman nesnesinin sahip olduğu olaylar, Özellik Görüntüleyici panelindeki "Events" sekmesinde yer almaktadır. Her bir olay, farklı çalışma anlarında tetiklenerek kendilerine özgü işlemleri gerçekleştirir. Bu olaylara geliştirici tarafından yazılan kodlar da ilgili olayın tetiklendiği anda çalıştırılır. Herhangi bir olaya kod yazmak için, Olaylar sekmesinden ilgili olay satırına çift tıklanır. Ekran, “Akışadı.cs” isimli akış kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur. Geliştirici bu method içerisinde istediği kod bloğunu kurgulayabilir. Olaylar sekmesinden tıklanarak kod tarafında methodu oluşturulmuş olayın yanında, method adı bilgisi otomatik oluşturularak, olayla method arasındaki ilişki belirtilmiş olur.

![Doküman](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload741ded6b-d0e6-48c0-a4d0-21c59cca982c)