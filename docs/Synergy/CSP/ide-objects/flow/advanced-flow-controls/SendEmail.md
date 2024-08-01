---
sidebar_position: 4
custom_edit_url: ""
---

# Eposta Gönder

Eposta Gönder nesnesi, sürecin herhangi bir anında, sistemde tanımlı kişilere veya organizasyon dışından kişilere mail göndermek için kullanılır.

Araç kutusu panelinden Eposta Gönder nesnesi sürüklenip akış üzerine bırakılır. Akış tasarım ekranında bulunan nesneye tıklandığında, Özellik Görüntüleyici panelinde, nesne özellikleri görünür. 

Eposta Gönder nesnesine tıklandığında Özellik Görüntüleyici panelinde "Appearance", "Properties" ve "Events" sekmeleri bulunmaktadır.

![Eposta Gönder](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd3c53131-633c-4d0b-86eb-3ead107a0a15)

## Appearance

### Text Configs

`Object Name` - Nesnenin sistem tarafında kullanılacak ismidir. Kod tarafında nesneye, nesne adı alanında yazan değerle erişim sağlanır.

`Caption` - Nesnenin başlık metninin girildiği alandır.

`Is Lock` - Tasarım anında nesnenin yeri değiştirilmesin isteniyorsa bu alan aktif edilir.

`Size` - Nesnenin genişlik ve yükseklik ayarlarının yapıldığı kısımdır.

## Properties

### Çalışma

`Continue If Error Occurs` - Süreç Eposta Gönder nesnesinden geçtiğinde nesne metodunun içinde yazılan kod bloğu çalıştırılıp, bu kodda herhangi bir hata ile karşılaşıldığında, web ara yüzünde sürecin hata vermeden devam etmesi isteniyorsa işaretlenir.

`Error Description Object` - Eposta Gönder nesnesi kodlarında bir hata ile karşılaşıldığında, hatanın detaylı metninin atandığı bir Değişken nesnesi bu alandan seçilmektedir.

### Value

`Type` - Eposta Gönder nesnesinin tipinin alfanumerik mi, numerik mi yoksa lojik bir değer mi olacağı bilgisi bu sekmeden ayarlanır. Type alanında; Metin, Tam sayı, Ondalık sayı, Tarih, Para ve Doğru/Yanlış tipleri listelenmektedir.

`Value Type` - Sabit bir değer verilmek isteniyorsa Value Type olarak “Sabit Değer” seçeneği seçilmektedir.

`Value` - Value Type alanında seçilen Sabit değerin tanımlandığı alandır.

### Mail From

`Read Information` - Gönderilen mail okunduğunda gönderen mail adresine okundu bilgisi iletilmesi istenildiği durumda seçilir.

### Mail To

`Mail to List` - Mail gönderilecek kişi ya da kişilerin mail adreslerinin belirlendiği alandır. Alana tıklandığında, mail gönderilecek adreslerin eklenebileceği  bir pencere açılır. Penceredeki Ekle butonuna basıldığında eklenen satır seçildiğinde, satır özelliklerinde Source Type seçeneği listelenir. Source Type alanına tıklandığında akış tasarımında kulanılabilecek liquid değişken verileri listelenir.

![Eposta Gönder](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload51310eaf-457f-4625-a4a8-d9efe930d6de)

### Mail CC

`Mail CC List` - Mailde CC ye eklenecek mail adresinin belirlendiği kısımdır. Mail adresi ekleme yapısı Şu Adrese Postala seçeneğindeki Listeye Postala ile aynıdır.

### Mail BCC

`Mail BCC List` - Mailde BCC ye eklenecek mail adresinin belirlendiği kısımdır. Mail adresi ekleme yapısı Şu Adrese Postala seçeneğindeki Listeye Postala ile aynıdır.

### Mail Content

`Subject Value` - Alanda mail konu metninin nereden besleneceği seçilir. Alana tıklandığında akış tasarımında kulanılabilecek liquid değişken verileri listelenir veya alana sabir veri girişi de yapılabilmektedir.

`Message Value` - Konu Tipi Sabit veya Fonksiyondan Elde Et olarak seçilirse görünür hale gelir. Bu alana gönderilecek olan maildeki konu yazılmalıdır. Alana tıklandığında akış tasarımında kulanılabilecek liquid değişken verileri listelenir veya alana sabir veri girişi de yapılabilmektedir.

`Is HTML Message` - Mail mesajının HTML yapıda gönderilmesi isteniyorsa bu alan işaretlenir.

### Mail Attachments

`Edit Attachments` - Gönderilecek maile ek eklemek için kullanılacak alandır.

![Eposta Gönder](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd490e5e4-e737-4c33-a870-fcff9178afdb)

Atttachments alanına tıklandığında, gönderilecek e-postaya eklenmek istenen ek türünün seçileceği tanımlanacağı ekran açılır.

![Eposta Gönder](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0eadf0c5-7b19-4813-a026-3d57adf0ce79)

Attachments düzenleme penceresinde **“Ekle”** butonu ile Bilgilendirme nesnesinde kişiye gönderilecek e-postaya ek eklenmesi için tanım yapılabilir, yapılmış tanımda satır üzerine tıklanarak ek ayarlarında değişiklik yapılabilir ya da ek satırı detaylarında beliren çöp kutusu ikonuna basılıp olay, nesne üzerinden kaldırılabilir.

![Eposta Gönder](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade4388958-2f55-4fe1-bb50-7ea2b09985ac)

- Type alanı ek dosyanın nerede bulunduğunun seçildiği alandır. DM, Flow, RelatedDocuments seçimleri yapılabilir.
    - Type:DM seçildiğinde panelde Value alanı içinde Doküman Yönetimi içinde seçim yapılır.
    - Type:Flow seçildiğinde ek olarak eklenecek dosyanın Id bilgisinin bulunduğu nesne liquid olarak seçilebilir veya statik veri yazılabilir. ({{ Document1.DocumentId }}, {{ Variable1.Value }}, 56669)
    - Type:RelatedDocuments seçildiğinde Document alanı gözükerek kullanılacak RelatedDocuments nesnesinin bulunduğu formu içeren Doküman nesnesi seçilir. Seçim yapılması ile panelde Related Documents alanı gözükerek seçilen nesne içindeki **Related Documents** nesneleri listelenerek seçim yapılır.

![Eposta Gönder](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload29b0cb0a-6a05-4112-9e25-5e14187ff026)

:::info BİLGİ

Nesne üzerinde ekli özelliklerin doğru olduğu sistem tarafından kontrol edilmektedir. Eksik bir özellik bulunduğunda nesne üzerinde kırmızı ünlem ikonu gösterilerek, fare işaretçisi ile ikon üzerine gelindiğinde nelerin eksik veya hatalı olduğu görüntülenebilmektedir.

![Eposta Gönder](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadecd18395-e00b-4928-a2f3-d5d758422f7a)

:::

## Events

### Events

Eposta Gönder nesnesinin sahip olduğu olaylar, Özellik Görüntüleyici panelindeki "Events" sekmesinde yer almaktadır. Her bir olay, farklı çalışma anlarında tetiklenerek kendilerine özgü işlemleri gerçekleştirir. Bu olaylara geliştirici tarafından yazılan kodlar da ilgili olayın tetiklendiği anda çalıştırılır. Herhangi bir olaya kod yazmak için, Olaylar sekmesinden ilgili olay satırına çift tıklanır. Ekran, “Akışadı.cs” isimli akış kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur. Geliştirici bu method içerisinde istediği kod bloğunu kurgulayabilir. Olaylar sekmesinden tıklanarak kod tarafında methodu oluşturulmuş olayın yanında, method adı bilgisi otomatik oluşturularak, olayla method arasındaki ilişki belirtilmiş olur.

![Eposta Gönder](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload51ce82ce-ccc4-479c-b246-8993ac35f229)

:::tip İPUCU

OnBeforeExecution eventi içinde nesne içinde gönderilecek eposta içeriğine müdahale edebilirsiniz.

```csharp
public void SendMail1_OnBeforeExecution(object sender,OnBeforeExecutionArguments args)
{
    SendMail1.Subject = "CSP üzerinden email gönderimi hk.";
    SendMail1.Message = "Bu emailde CSP'den email gönderim örneğine ait kod paylaşımı yapılmıştır.";
    SendMail1.DisplayName = "Bimser Synergy";
    SendMail1.FromAddress = "no-reply@bimser.com.tr";

    SendMail1.ErrorDescriptionObjectName = "Variable1";
    SendMail1.ResumeOnError = true;
    SendMail1.IsHtml = true;
    SendMail1.ReadNotification = false;

    SendMail1.AddTO("mailbox1@bimser.com.tr");
    SendMail1.AddCC("mailbox2@bimser.com.tr");
    SendMail1.AddBCC("mailbox3@bimser.com.tr");
}
```
:::