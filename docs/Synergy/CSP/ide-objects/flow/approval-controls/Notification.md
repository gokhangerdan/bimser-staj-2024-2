---
sidebar_position: 4
custom_edit_url: ""
---

# Bilgilendirme

Bilgilendirme nesnesi, sürecin herhangi bir anında, sistemde tanımlı kişilere bilgilendirme maili göndermek için kullanılan nesnedir.

Bilgilendirme nesnesi genel olarak süreç içerisinde geçen kullanıcılara ya da süreçle ilgili bilgilendirilmesi gereken kullanıcılara bilgilendirme maili göndermek için kullanılır.

Bilgilendirme nesnesinin içeriği statik olarak tanımlanabileceği gibi kod ile de doldurulabilir.

Akış tasarım ekranında bulunan nesneye tıklandığında, Özellik Görüntüleyici panelinde, nesne özellikleri görünür.

Bilgilendirme nesnesine tıklandığında Özellik Görüntüleyici panelinde "Appearance", "Properties" ve "Events" sekmeleri bulunmaktadır.

![Bilgilendirme](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadeca26ba3-2acc-4af4-a704-754b05ab3e57)

## Appearance

### Text Configs

`Object Name` - Nesnenin sistem tarafında kullanılacak ismidir. Kod tarafında nesneye, nesne adı alanında yazan değerle erişim sağlanır.

`Caption` - Nesnenin başlık metninin girildiği alandır.

`Is Lock` - Tasarım anında nesnenin yeri değiştirilmesin isteniyorsa bu alan aktif edilir.

`Size` - Nesnenin genişlik ve yükseklik ayarlarının yapıldığı kısımdır.

## Properties

### Group Content

`Group Content` - Bu alandan bilgilendirme mailinin gideceği kişi ya da kişileri seçmek için Bilgilendirme nesnesinin içeriği doldurulur. Grup içeriği alanına tıklandığında, Bilgilendirme nesnesine eklenecek kişileri seçmek için "İçerikler" butonu, seçilmiş kişileri nesne içinde oluşturmak için "Oluştur" ve eklenmiş kayıtları gruptan kaldırmak için “Sil” butonunun bulunduğu bir ekran açılacaktır.

![Bilgilendirme](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddf58688a-f8f3-413c-bb53-07d9aa172193)

"İçerikler" butonuna basıldığında, Bilgilendirme nesnesine hangi tipte içerik ekleneceğinin belirtileceği seçim alanı açılacaktır. Alanda; **[Pozisyon](#members-position)**, **[Pozisyon grupları](#members-position-groups)** ve **[Doküman üzerindeki nesne](#members-documents)** olarak 3 seçenek listelenir.

![Bilgilendirme](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload089b1afa-2aac-4948-9ffa-b2d25b40b53b)

#### Pozisyon seçimi yapılırsa {#members-position}

Pozisyon seçeneği seçildiğinde yeni pop-up açılır ve bu alanda; Sabit Pozisyon, Kullanıcı, Değişken Pozisyon ve Akışı Başlatan seçenekleri listelenir.

- Sabit pozisyon seçeneği seçildiğinde, ekrana sistemde bulunan tüm pozisyon kayıtları listelenir. Bu listeden bir ya da birden çok pozisyon kaydı seçilerek "Oluştur" butonuna basıldığında, Bilgilendirme nesnesine seçilen pozisyon kayıtları eklenmiş olur. Geliştirici isterse tekrar "İçerikler" butonuna basarak alan içeriğini doldurmaya devam edebilir.

![Bilgilendirme](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload558c97a7-262e-4389-b356-09ccff304435)

![Bilgilendirme](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6aa81d8b-7884-4f62-8ec0-e96f700f1157)

- Kullanıcı seçeneği seçildiğinde, ekrana sistemde bulunan tüm kullanıcı kayıtları listelenir. Bu listeden bir ya da birden çok kullanıcı kaydı seçilerek "Oluştur" butonuna basıldığında, Bilgilendirme nesnesine seçilen kullanıcılar eklenmiş olur. Geliştirici isterse tekrar "İçerikler" butonuna basarak grup içeriğini doldurmaya devam edebilir.

![Bilgilendirme](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4fd19a4c-041e-4571-b6f2-2c4e3163e83c)

![Bilgilendirme](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd85466b6-2905-4f63-9a3d-5ae1bb3a87c2)

- Değişken pozisyon seçeneği seçildiğinde, ekrana akış tasarımında bulunan tüm Pozisyon nesneleri ve Akışı Başlatan nesnesi listelenir. Bilgilendirme nesnesine akıştaki, hangi pozisyondaki kişi veya pozisyon eklenmek isteniyorsa o kişi veya pozisyonu temsil eden Pozisyon nesneleri seçimi bu alandan yapılır. "Oluştur" butonuna basıldıktan sonra geliştirici isterse tekrar "İçerikler" butonuna basarak grup içeriğini doldurmaya devam edebilir.

![Bilgilendirme](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload212906bc-2d27-49a4-b9dc-2e0b524576b9)

![Bilgilendirme](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5a4456a3-c2f8-4f12-87f0-0f659b034fb9)

- Akışı Başlatan seçeneği seçildiğinde, Bilgilendirme nesnesine akışı başlatan kullanıcı eklenmiş olur. Geliştirici isterse tekrar "İçerikler" butonuna basarak grup içeriğini doldurmaya devam edebilir.

![Bilgilendirme](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7bcb5a66-95d4-445e-a951-287db51a7179)

![Bilgilendirme](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7419b310-025c-49ad-ad33-b201f96fe103)

#### Pozisyon grupları seçimi yapılırsa {#members-position-groups}

Bilgilendirme nesnesinde Group Content alanı içinde Pozisyon Grupları seçeneği seçildiğinde yeni pop-up açılır ve bu alanda; Belge onaylayanlar/reddedenler, Unvana göre kullanıcı grubu, Departmana göre kullanıcı grubu ve Kullanıcı grupları seçenekleri listelenir.

- Belge onaylayanlar/reddedenler seçeneği, ilgili akış tasarımında akış, Bilgilendirme nesnesine gelene kadar kimler aksiyonda bulunmuşsa o kişileri Bilgilendirme nesnesine eklemek için kullanılan seçenektir. Geliştirici isterse tekrar "İçerikler" butonuna basarak grup içeriğini doldurmaya devam edebilir.

![Bilgilendirme](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc91bc11b-9a88-46ae-b48c-7542a44ca43a)

![Bilgilendirme](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb40a556e-20c8-4fc1-8c58-bae177e03d5c)

- Unvana göre kullanıcı grubu seçeneği, Bilgilendirme nesnesine belirli bir unvan tanımına sahip kullanıcıları eklemek için kullanılan seçenektir. "İçerikler" alanından bu seçenek seçildiğinde ekrana, sistemde tanımlı tüm unvan kayıtları listelenir.

![Bilgilendirme](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2b70c59e-49fe-40b1-aa2a-c1c278f911a2)

![Bilgilendirme](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload905e7aec-e687-44bc-babf-97bcca0a093e)

Aşağıdaki ekran görüntüsünde yapılan seçime göre “Project Manager” unvanlı kullanıcılar eklenecek demektir. Geliştirici isterse tekrar "İçerikler" butonuna basarak grup içeriğini doldurmaya devam edebilir.

![Bilgilendirme](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf753414c-8c2d-4a10-b815-db506bef8e09)

![Bilgilendirme](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf48ed8ea-46cd-40b5-948e-11d089a29091)

- Departmana göre kullanıcı grubu seçeneği, Bilgilendirme nesnesine belirli bir departmanda bulunan kullanıcıları eklemek için kullanılan seçenektir. "İçerikler" alanından bu seçenek seçildiğinde ekrana, sistemde tanımlı tüm departman kayıtları listelenir.

![Bilgilendirme](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf4b4875c-aa2e-46c9-9370-15f5d4cf0ae8)

![Bilgilendirme](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8fc68f95-f760-4620-910b-e6dad0141205)

Aşağıdaki ekran görüntüsünde yapılan seçime göre Bilgilendirme nesnesine, "Product Management" departmanındaki kullanıcılar eklenecek demektir. Geliştirici isterse tekrar "İçerikler" butonuna basarak grup içeriğini doldurmaya devam edebilir.

![Bilgilendirme](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload691cfe28-770e-48f2-8f28-5fc5259cb7f5)

![Bilgilendirme](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload567ba060-cf69-48bb-a40d-fe3d61e28951)

- Kullanıcı grupları seçeneği seçildiğinde ekrana, kullanıcı arayüzünde bulunan İnsan Kaynakları başlığı altında tanımlanmış **[Kullanıcı Grupları](web/human-resources/user-groups.md)** listelenir. Geliştirici bu listeden kullanıcı grubu seçimi yaptığında, Bilgilendirme nesnesine seçilen kullanıcı grubunun içine tanımlı kullanıcılar eklenmiş olur. İnsan Kaynakları bölümünden ilgili kullanıcı grubuna yeni kullanıcılar eklendiğinde ya da gruptan kişi çıkarıldığında, bu kullanıcı grubunun seçildiği Bilgilendirme nesnesine gelen akış, kullanıcı grubunun son güncel haliyle içinde bulunan kişilere bilgilendirme gönderilmiş olur.

![Bilgilendirme](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada5893063-a589-4c2e-b605-a56295a38182)

![Bilgilendirme](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload19dd4b9b-8336-426d-b358-782611b3f0e8)

![Bilgilendirme](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddf952a3b-5dfe-4a8a-bf39-e122b0d7e2d1)

![Bilgilendirme](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd33abe4d-84c6-404f-94b5-a80aec24e4c8)

#### Dokuman üzerindeki nesne seçimi yapılırsa {#members-documents}

- Doküman üzerindeki nesne seçeneği seçildiğinde form üzerindeki bir [DataGrid](form/advanced-form-controls/DataGrid.md) nesnesinde seçilen kullanıcı veya pozisyonları, Bilgilendirme nesnesine eklemek için kullanılır. Alanda kişi ekleme işlemi pozisyon bazlı veya kullanıcı bazlı yapılabilmektedir.

Eğer form üzerindeki DataGrid nesnesinde seçilen kişiler, kullanıcı bazlı olarak alana eklenmek isteniyorsa, tablo nesnelerinin “Kullanıcı Adı(sicil no)” bilgisini barındıran bir ID kolonuna sahip olması gerekir.

Eğer form üzerindeki DataGrid nesnesinde seçilen kişiler, pozisyon bazlı olarak alana eklenmek isteniyorsa, tablo nesnelerinin “Pozisyon id” bilgisini barındıran bir ID kolonuna sahip olması gerekir.

İçerikler alanından “Doküman üzerindeki nesne” seçeneği seçildiğinde ekrana aşağıdaki alanlar gelecektir;

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Document 	| Bu alanda akış tasarımında bulunan tüm Doküman nesneleri listelenir. Hangi form üzerindeki DataGrid nesnesinin verilerine erişilmek isteniyorsa, o formun tanımlı olduğu Doküman nesnesi bu alandan seçilir. 	|
| Data type 	| “Kullanıcı” ve “Pozisyon” seçenekleri listelenir. Bilgilendirme nesnesine eklenecek kayıtlar kullanıcı bazlı eklenecekse bu alandan “Kullanıcı”, pozisyon bazlı eklenecekse bu alandan “Pozisyon” seçeneği seçilmelidir. 	|
| Table / Details 	| Documents alanında eklenen form üzerindeki hangi DataGrid nesneden seçilen kişiler Bilgilendirme nesnesine eklenecekse, ilgili nesnenin seçimi yapılır. 	|
| Field 	| Bu alanda, DataGrid nesnesinin kolonları listelenir. Data type olarak “Kullanıcı” seçilmişse bu alanda, kullanıcı id lerinin bulunduğu kolonun seçimi yapılmalıdır. Data type olarak “Pozisyon” seçilmişse bu alanda, pozisyon id lerinin bulunduğu kolonun seçimi yapılmalıdır. 	|

### Documents

`Documents` - Bu alanda, Bilgilendirme nesnesindeki kullanıcının hangi formu ve formun hangi görünümünü (view) görebileceği ayarlanır. Projeye dahil olan formlar akış tarafında Doküman nesnesi içerisinde tutulur. Doküman nesnesi, kendisine bağlanan formu ve form üzerindeki verileri temsil eder. Akış üzerinde birden çok, farklı formları temsil eden Doküman nesneleri bulunabilir. Bilgilendirme nesnesindeki kullanıcının hangi formu görmesi isteniyorsa, bu alandan, ilgili formun bağlı olduğu Doküman nesnesinin seçimi yapılıp gerekli ayarları belirlenir.

Dokümanlar kısmına tıklandığında, akış üzerinde bulunan tüm Doküman nesneleri listelenir.

![Bilgilendirme](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfbaae866-18db-4ce1-8074-3d34b5460262)

Bilgilendirme nesnesinde tanımlı kullanıcıya web arayüzünde görmesi için birden fazla Doküman nesnesi de eklenebilir. Documents kısmına tıklandığında açılan ekranda kullanıcının görmesi istenen bir ya da birden çok Doküman nesnesi “Ekle” butonu ile eklenip, doküman üzerinde yapılabilecek düzenlemelerin ayarları belirlenir.

![Bilgilendirme](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade3ed5b35-818c-47fc-b06c-490dc3f0c813)

**Properties sekmesi özellikleri**

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Document 	| Akış tasarımı üzerindeki tüm Doküman nesnelerinin listelendiği alandır. Bilgilendirme nesnesindeki kişiye gösterilmek istenen formun bağlı olduğu Doküman nesnesi bu alandan seçilir. 	|
| View 	| “Doküman” alanından seçilen Doküman nesnesinin bağlı olduğu formun görünümleri (view) bu alanda listelenir. Bilgilendirme içindeki kullanıcı formu açtığında hangi form görünümünü görmesi isteniyorsa bu alandan seçimi yapılmalıdır. Görünüm alanından herhangi bir seçim yapılmazsa kullanıcı, “default” görünümü görecektir. 	|
| Panel Size 	| Web arayüzünde tanımlanan doküman nesnesinin hangi genişlikte açılabileceğinin belirlendiği alandır. 1-2-3 değerlerinden birisi seçilerek açılan panel boyutu seçilen değer genişliğinde açılacaktır. 	|

### Message

`Send Mail` - Akış adımı ilgili Bilgilendirme nesnesine düştüğünde, sistem otomatik olarak nesnedeki kişiye, bilgisine bir süreç düşürüldüğünün bilgisini mail olarak gönderir. İlgili nesnede bilgilendirme maili gönderilmesi istenmiyorsa, Send Mail alanının işareti kaldırılabilir. Bu durum genelde test amaçlı akış senaryosu denemelerinde kişilere mail gitmemesi için kullanılır.

:::tip İPUCU

Nesneler içinde gezerek e-posta gönderimini kapatmaya ek olarak akış genelinde de e-posta gönderimini engellemek mümkündür. **[Flow Properties->General](index.mdx#general)** içindeki **Disable Email Sending** özellği aktif edilerek e-posta gönderimi akış genelinde kapatılabilir.

:::

`Caption` - Bilgilendirme nesnesindeki kullanıcılara gönderilecek bilgi mailinin başlık bilgisidir. Başlık bilgisinde varsayılan olarak gelen “ProcessCaption“, “FirstName” ve “LastName” parametreleri bulunur. Bu parametreler sistemin kendi parametreleridir ve mailin gönderildiği sürecin başlığı, mailin gönderildiği kişinin adı ve soyadı bilgileri otomatik olarak sistem tarafından doldurulur. Varsayılan olarak gelen mail başlığı yapısı aşağıdaki gibidir. Geliştirici isterse bu mail başlığını değiştirebilir.

> *Bimser Synergy {{ProcessCaption}} onayı ({{FirstName}} {{LastName}})*

`Message` - Bilgilendirme nesnesindeki kullanıcılara gönderilecek mailin mesaj metin kısmı bu alanda yer alır. Varsayılan olarak gelen mesaj metni, isteğe bağlı olarak değiştirilebilir.

`Attachments` - Bilgilendirme nesnesindeki kullanıcılara gönderilecek mail içinde ek dosya gönderilmek istenirse bu alandan tanımlanır.

![Bilgilendirme](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload987eedbd-509d-4eb4-9c00-28cbee825ff9)

Atttachments alanına tıklandığında, gönderilecek e-postaya eklenmek istenen ek türünün seçileceği tanımlanacağı ekran açılır.

![Bilgilendirme](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload29a16141-ad1a-4531-8825-7f28bbca37a5)

Attachments düzenleme penceresinde **“Ekle”** butonu ile Bilgilendirme nesnesinde kişiye gönderilecek e-postaya ek eklenmesi için tanım yapılabilir, yapılmış tanımda satır üzerine tıklanarak ek ayarlarında değişiklik yapılabilir ya da ek satırı detaylarında beliren çöp kutusu ikonuna basılıp olay, nesne üzerinden kaldırılabilir.

![Bilgilendirme](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload47d3ac0d-18da-48ca-a837-da176f5b8cae)

- Type alanı ek dosyanın nerede bulunduğunun seçildiği alandır. DM, Flow, RelatedDocuments seçimleri yapılabilir.
    - Type:DM seçildiğinde panelde Value alanı içinde Doküman Yönetimi içinde seçim yapılır.
    - Type:Flow seçildiğinde ek olarak eklenecek dosyanın Id bilgisinin bulunduğu nesne liquid olarak seçilebilir veya statik veri yazılabilir. ({{ Document1.DocumentId }}, {{ Variable1.Value }}, 56669)
    - Type:RelatedDocuments seçildiğinde Document alanı gözükerek kullanılacak RelatedDocuments nesnesinin bulunduğu formu içeren Doküman nesnesi seçilir. Seçim yapılması ile panelde Related Documents alanı gözükerek seçilen nesne içindeki **Related Documents** nesneleri listelenerek seçim yapılır.

![Bilgilendirme](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload996811e4-16d9-4b4c-8487-dfd2a69feeea)

`Edit Message Source` - Bilgilendirme nesnesindeki kişilere gönderilecek mesajın, sistem varsayılanı olarak değil, özelleştirilmiş bir mesaj şablonu olarak gönderilmesi isteniyorsa bu özellik aktif edilir. Özellik aktif edildiğinde “Source Message” isimli alan görünür olacaktır.

`Source Message` - Varsayılan mail şablonunun html formatta görüntülenerek, üzerinde değişiklik yapılmasına izin veren ekran, bu alandan açılır. Tasarlanan mail şablonu, önizleme penceresinde anlık olarak görüntülenebilir.

Elektronik postada belli bir dil düzenlenmek istenirse panel içindeki dil seçeneği değiştirilerek, seçilen dile ait e-posta kodları ve önizlemesi yapılabilir.

![Bilgilendirme](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0ee198a0-9505-44b0-a2ad-c6e4ba705312)

:::info BİLGİ

Kullanıcıların sistemde hangi dilde e-posta alacakları, İnsan Kaynakları bölümünde her kullanıcıdaki **Varsayılan Dil** alanında yapılan seçime göre belirlenmektedir.

<div style={{textAlign: 'center'}}>

![Bilgilendirme](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9fb584ac-9013-4bed-a02f-61061603ded8)

</div>

:::

### Push Notification

:::caution DİKKAT

Push Notification mobil uygulama üzerinden Bimser Synergy CSP uygulamasına giriş yapmış ve bildirimlere izin vermiş kişi/kişilerin cihazlarına gönderilir.

:::

`Send Push Notification` - Bilgilendirme nesnesindeki kişilerin mobil cihazında bildirim gönderilmek istenirse alan aktif edilir.

`Caption` - Bilgilendirme nesnesindeki kişilere gönderilecek mobil bildirimin başlık bilgisidir. Başlık bilgisinde varsayılan olarak gelen “ProcessCaption“, “FirstName” ve “LastName” parametreleri bulunur. Bu parametreler sistemin kendi parametreleridir ve bilgilendirmenin gönderildiği sürecin başlığı, mailin gönderildiği kişinin adı ve soyadı bilgileri otomatik olarak sistem tarafından doldurulur. Varsayılan olarak gelen mail başlığı yapısı aşağıdaki gibidir. Geliştirici isterse bu mail başlığını değiştirebilir.

> *Bimser Synergy {{ProcessCaption}} onayı ({{FirstName}} {{LastName}})*

`Message` - Bilgilendirme nesnesindeki kişiye gönderilecek bilgilendirme mesaj metin kısmı bu alanda yer alır. Varsayılan olarak gelen mesaj metni, isteğe bağlı olarak değiştirilebilir.

### Action

`Continue If Error Occurs` - Özellik aktif edildiğinde Bilgilendirme nesnesine ait Continue bağlantına okuna ek olarak ContinueIfErrorOccured bağlantı okunun kullanılması sağlanır. Nesne içinde yanlış tasarım, atama bilgisinin bulunmaması vb. gibi durumlar sebebiyle atama işlemi yapılamadığında sürecin uç kullanıcı tarafında hata vermesi yerine bu ok üzerinden ilerleyerek, hata oluştuğunda sürecin farklı bir işlem yapması sağlanabilmektedir.

:::info BİLGİ

Nesne üzerinde ekli özelliklerin doğru olduğu sistem tarafından kontrol edilmektedir. Eksik bir özellik bulunduğunda nesne üzerinde kırmızı ünlem ikonu gösterilerek, fare işaretçisi ile ikon üzerine gelindiğinde nelerin eksik veya hatalı olduğu görüntülenebilmektedir.

![Bilgilendirme](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf4ca4f69-522f-4620-a23a-41cfea24951e)

:::

## Events

Bilgilendirme nesnesinin sahip olduğu olaylar, Özellik Görüntüleyici panelindeki "Events" sekmesinde yer almaktadır. Her bir olay, farklı çalışma anlarında tetiklenerek kendilerine özgü işlemleri gerçekleştirir. Bu olaylara geliştirici tarafından yazılan kodlar da ilgili olayın tetiklendiği anda çalıştırılır. Herhangi bir olaya kod yazmak için, Olaylar sekmesinden ilgili olay satırına çift tıklanır. Ekran, “Akışadı.cs” isimli akış kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur. Geliştirici bu method içerisinde istediği kod bloğunu kurgulayabilir. Olaylar sekmesinden tıklanarak kod tarafında methodu oluşturulmuş olayın yanında, method adı bilgisi otomatik oluşturularak, olayla method arasındaki ilişki belirtilmiş olur.

![Bilgilendirme](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload769856b5-0de4-4440-9b3f-40c8ce71c634)