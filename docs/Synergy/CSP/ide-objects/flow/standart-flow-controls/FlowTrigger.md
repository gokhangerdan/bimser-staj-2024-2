---
sidebar_position: 4
custom_edit_url: ""
---

# Akış Tetikleyici

Akış Tetikleyici nesnesi, proje tasarlanırken belli bir aşamada sürecin farklı bir projenin başlatılması, aynı projede farklı bir akışın başlatılması gibi işlemine ihtiyaç duyulduğunda kod yazılmadan bu süreçlerin başlatılabilmesini sağlayan nesnedir.

Nesne kullanılarak bir veya birden fazla sürecin tetiklenmesi işlemi yapılabilmektedir. Bir tane süreç tetiklenmek istendiğinde nesnedeki Parameters alanına değerler tanımlanarak akış tetikleme işlemi yapılabilir. Birden fazla sürecin tetiklenmesi ise tetiklenecek süreç verileri form üzerindeki DataGrid nesnesi nesne üzerinde tanımlanarak yapılabilmektedir.

Akış tasarım ekranında bulunan nesneye tıklandığında, Özellik Görüntüleyici panelinde, nesne özellikleri görünür.

![Akış Tetikleyici](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddff2e255-ca02-4eaa-bdbf-b2d6e784031e)

Akış Bitişi nesnesine tıklandığında Özellik Görüntüleyici panelinde "Appearance", "Properties" ve "Events" sekmeleri bulunmaktadır.

## Appearance

### Text Configs

`Object Name` - Nesnenin sistem tarafında kullanılacak ismidir. Kod tarafında nesneye, nesne adı alanında yazan değerle erişim sağlanır.

`Caption` - Nesnenin başlık metninin girildiği alandır.

`Is Lock` - Tasarım anında nesnenin yeri değiştirilmesin isteniyorsa bu alan aktif edilir.

`Size` - Nesnenin genişlik ve yükseklik ayarlarının yapıldığı kısımdır.

## Properties

### Source

`Document` - Birden fazla süreç tetiklenmesi istendiğinde, tetikleme işleminde kullanılacak DataGrid nesnesini içeren **[Doküman](flow-document-controls/Document.md)** nesnesinin seçildiği alandır.

`Control Name` - Documents alanında yapılan seçimde, nesnede tanımlı formun içerdiği ve süreçler tetiklenirken kullanılacak DataGrid nesnesinin seçildiği alandır.

### Trigger

`Project` - Başlatılması istenen projenin seçildiği alandır.

`Flow` - Başlatılması istenen projenin hangi akışı tetiklenmesi isteniyorsa seçildiği alandır.

`Parent ProcessId` - Süreç tetiklendiğinde, tetiklenen süreç(ler) ve ana süreç arasında bağlantının kurulduğu kısımdır. Alana tanım yapıldığında süreç tetiklendiğinde akış tarihçesinde başlatılan diğer akışlar sürecin akış tarihçesinde kırılımlı olarak gösterilir. Statik, akıştaki bir değişkenin içerdiği veri ( **{{Degisken1.Value}}** ) veya sürecin kendi akış numarası verisi girilebilir.

:::tip İPUCU

Eğer sürece ait numaranın otomatik olarak kullanılmasını isterseniz Parent ProcessId alanına **{{ProcessId}}** yazabilirsiniz.

:::

`Show in Flow History` - Özellik aktif edildiğinde Akış Tetikleyici nesnesinin akış tarihçesinde gözükmesini sağlar.

`Starter User` - Akış tarihçesinde tetiklenen akışların hangi kullanıcı ile başladığını göstermek için tanımın yapıldığı alandır. Statik bir değer veya değişkenin içerdiği veri ( **{{Degisken1.Value}}** ) girilebilir. Starter User Type alanında yapılan seçimle birlikte çalışır. Starter User Type alanında yapılan seçime göre kullanıcının OSUSERS tablosundaki ID ve USERNAME değerleri girilmelidir.

`Starter User Type` - Starter User alanında girilen bilginin hangi türde olacağını belirlemek için kullanılan alandır. Akış tarihçesinde tetiklenen akışların, kullanıcı id’si (UserId) veya kullanıcı ismi (UserName) bilgilerinden bir tanesi ile tetiklenmesi isteniyorsa, hangi bilgiye göre tetiklemenin seçileceği alandır. 

>Yapılabilecek Seçimler : UserId, UserName

`Process Count Variable` - Akış Tetikleyici nesnesi üzerinden başlatılan akış sayısının akıştaki bir değişken nesnesine aktarıldığı alandır. Akışta bulunan bir değişken nesnesi seçilir.

### Parameters

`Parameters` - Akış Tetikleyici nesnesi üzerinde seçilmiş proje-akış üzerine gönderilecek değişken bilgilerinin girildiği alandır. 

![Akış Tetikleyici](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload08d26a26-5643-4619-8545-97a4446aafac)

Parameters alanına tıklandığında, başlatılacak akışlara gönderilecek parametre değerlerinin tanımlanacağı ekran açılır.

![Akış Tetikleyici](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4519b138-d2f0-4b50-bf03-4638f49eac02)

Açılan ekranda ekle butonuna tıklanarak, başlatılacak akıştaki verinin gönderileceği değişken adı, gönderilecek veri türü, gönderilecek verinin tanımı yapılır. 

![Akış Tetikleyici](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload450c3487-7246-4607-beac-6f6ab3031644)

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Name 	| Nesnede seçilen projeye ait akışta bulunan ve parametre değerini alacak değişken nesnesinin adının yazıldığı alandır. Örneğin nesnede proje olarak İzin Talep projesi seçilip, akış olarak Flow1 seçildiyse, name alanında Flow1'in içerdiği ve **General seçeneği aktif olarak Değişken nesneleri**nin adı yazılmalıdır.![Akış Tetikleyici](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade98aa59d-6cef-48d5-a511-2a2d0da96026) 	|
| Type 	| Gönderilecek veri tipinin seçildiği alandır. String, Number, Boolean, DateTime ve Control seçenekleri bulunmaktadır. Control seçeneğinin kullanılabilmesi için nesnenin Control Name alanında DataGrid seçimi yapılmış olmalıdır. 	|
| Value 	| Name alanında seçilen Değişken nesnesine gönderilecek parametre verisinin tanımlandığı alandır. Statik veriler veya akışta kullanılabilecek liquid verileri tanımlanabilir ({{Document1.DocumentId}}, {{ProcessId}} gibi). Eğer Type alanınca Control seçildiyse, alanda nesneye tanımlanmış DataGrid nesnesinin kolonları listenecektir. 	|

> *Örnek bir parameters tanımı*
![Akış Tetikleyici](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3bfa921f-0d4f-4b50-a9af-85c7318aed0f)

:::tip İPUCU

Aşağıdaki resimde Akış Tetikleyici nesnesinde Parameters alanında, nesnede tetiklenecek akıştaki UserId, ParentDocumentId ve ParentProcessId değişkenleri (Örnek bir parameters tanımı içinde belirtilen değerler) tanımlanmıştır.

![Akış Tetikleyici](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade26ef355-f039-4ba9-b8ca-3eb4792d7214)

![Akış Tetikleyici](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4c5a587f-8912-4493-9a49-9c7273d2b431)

:::

:::info BİLGİ

Nesne üzerinde ekli özelliklerin doğru olduğu sistem tarafından kontrol edilmektedir. Eksik bir özellik bulunduğunda nesne üzerinde kırmızı ünlem ikonu gösterilerek, fare işaretçisi ile ikon üzerine gelindiğinde nelerin eksik veya hatalı olduğu görüntülenebilmektedir.

![Akış Tetikleyici](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9f8d39d1-49f7-4056-8560-3b1d97ce3b81)

:::

## Events

Akış Tetikleyici nesnesinin sahip olduğu olaylar, Özellik Görüntüleyici panelindeki "Events" sekmesinde yer almaktadır. Her bir olay, farklı çalışma anlarında tetiklenerek kendilerine özgü işlemleri gerçekleştirir. Bu olaylara geliştirici tarafından yazılan kodlar da ilgili olayın tetiklendiği anda çalıştırılır. Herhangi bir olaya kod yazmak için, Events sekmesinden ilgili olay satırına çift tıklanır. Ekran, “Akışadı.cs” isimli akış kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur. Geliştirici bu method içerisinde istediği kod bloğunu kurgulayabilir. Events sekmesinden tıklanarak kod tarafında methodu oluşturulmuş olayın yanında, method adı bilgisi otomatik oluşturularak, olayla method arasındaki ilişki belirtilmiş olur.

![Akış Tetikleyici](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3cbf69b0-86fd-488e-969f-c0474994cb52)