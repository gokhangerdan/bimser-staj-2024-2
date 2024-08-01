---
sidebar_position: 3
custom_edit_url: ""
---

# Pozisyon Grubu

Pozisyon grubu nesnesi, akış adımlarında birden çok kişiye aksiyon düşürülmek istendiğinde kullanılan nesnedir. Pozisyon nesnesine yalnızca bir kullanıcı ya da pozisyon eklenebilirken, pozisyon grubu nesnesine birden çok kullanıcı, pozisyon, kullanıcı grubu, departman veya unvan bazlı kullanıcı eklemeleri yapılabilmektedir.

Akış, Pozisyon Grubu nesnesine geldiğinde, gruptaki herkese onay maili gönderilir ve gruptaki kullanıcılar kendi web arayüz sayfalarında bulunan Onaylar ekranından bu süreç kaydına erişebilir.

Pozisyon Grubu nesnesinin içeriği tasarım sırasında statik olarak verilebileceği gibi kodla da grup içeriği doldurulabilir. Akış tasarım ekranında bulunan nesneye tıklandığında, Özellik Görüntüleyici panelinde, nesne özellikleri görünür.

Pozisyon grubu nesnesine tıklandığında Özellik Görüntüleyici panelinde "Appearance", "Properties" ve "Events" sekmeleri bulunmaktadır.

![Pozisyon Grubu](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0f444a70-b041-416e-b37b-d6e72885ac70)

## Appearance

### Text Configs

`Object Name` - Nesnenin sistem tarafında kullanılacak ismidir. Kod tarafında nesneye, nesne adı alanında yazan değerle erişim sağlanır.

`Caption` - Nesnenin başlık metninin girildiği alandır.

`Is Lock` - Tasarım anında nesnenin yeri değiştirilmesin isteniyorsa bu alan aktif edilir.

`Size` - Nesnenin genişlik ve yükseklik ayarlarının yapıldığı kısımdır.

## Properties

### Group Content

`Group Content` - Bu alandan Pozisyon Grubu nesnesinin içeriği doldurulur. Grup içeriği alanına tıklandığında, Pozisyon Grubuna eklenecek kişileri seçmek için "İçerikler" butonu, seçilmiş kişileri nesne içinde oluşturmak için "Oluştur" ve eklenmiş kayıtları gruptan kaldırmak için “Sil” butonunun bulunduğu bir ekran açılacaktır.

![Pozisyon Grubu](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadec04b195-a586-4599-9f91-d38256d69be1)

"İçerikler" butonuna basıldığında, Pozisyon Grubuna hangi tipte içerik ekleneceğinin belirtileceği seçim alanı açılacaktır. Alanda; **[Pozisyon](#members-position)**, **[Pozisyon grupları](#members-position-groups)** ve **[Doküman üzerindeki nesne](#members-documents)** olarak 3 seçenek listelenir.

![Pozisyon Grubu](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd78dde34-2a95-473c-8b2b-0aa63ea17260)

#### Pozisyon seçimi yapılırsa {#members-position}

Pozisyon seçeneği seçildiğinde yeni pop-up açılır ve bu alanda; Sabit Pozisyon, Kullanıcı, Değişken Pozisyon ve Akışı Başlatan seçenekleri listelenir.

- Sabit pozisyon seçeneği seçildiğinde, ekrana sistemde bulunan tüm pozisyon kayıtları listelenir. Bu listeden bir ya da birden çok pozisyon kaydı seçilerek "Oluştur" butonuna basıldığında, Pozisyon Grubu nesnesine seçilen pozisyon kayıtları eklenmiş olur. Geliştirici isterse tekrar "İçerikler" butonuna basarak alan içeriğini doldurmaya devam edebilir.

![Pozisyon Grubu](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5b86a0a1-8af4-4335-bcd6-73a15fc6abd0)

![Pozisyon Grubu](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade5d8bcf4-b5b2-4205-861d-73dfc8e876f1)

- Kullanıcı seçeneği seçildiğinde, ekrana sistemde bulunan tüm kullanıcı kayıtları listelenir. Bu listeden bir ya da birden çok kullanıcı kaydı seçilerek "Oluştur" butonuna basıldığında, Pozisyon Grubu nesnesine seçilen kullanıcılar eklenmiş olur. Geliştirici isterse tekrar "İçerikler" butonuna basarak grup içeriğini doldurmaya devam edebilir.

![Pozisyon Grubu](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1519bccc-1fe3-453a-9a68-f6ea882d3854)

![Pozisyon Grubu](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc2b45295-d618-49fe-9bb7-697e14fc9c67)

- Değişken pozisyon seçeneği seçildiğinde, ekrana akış tasarımında bulunan tüm Pozisyon nesneleri ve Akışı Başlatan nesnesi listelenir. Pozisyon Grubu nesnesine akıştaki, hangi pozisyondaki kişi veya pozisyon eklenmek isteniyorsa o kişi veya pozisyonu temsil eden Pozisyon nesneleri seçimi bu alandan yapılır. "Oluştur" butonuna basıldıktan sonra geliştirici isterse tekrar "İçerikler" butonuna basarak grup içeriğini doldurmaya devam edebilir.

![Pozisyon Grubu](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload12308fc5-0341-44c2-bac6-74fd00cca4fa)

![Pozisyon Grubu](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload73e723e9-22b9-440a-a1fc-a9d6dce0f696)

- Akışı Başlatan seçeneği seçildiğinde, Pozisyon Grubuna akışı başlatan kullanıcı eklenmiş olur. Geliştirici isterse tekrar "İçerikler" butonuna basarak grup içeriğini doldurmaya devam edebilir.

![Pozisyon Grubu](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadafdb9f37-1b5b-4e17-b782-fe6f62894707)

![Pozisyon Grubu](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3573d74a-8110-4a26-9290-3ec72fbb633e)

#### Pozisyon grupları seçimi yapılırsa {#members-position-groups}

Pozisyon Grubu nesnesinde Group Content alanı içinde Pozisyon Grupları seçeneği seçildiğinde yeni pop-up açılır ve bu alanda; Belge onaylayanlar/reddedenler, Unvana göre kullanıcı grubu, Departmana göre kullanıcı grubu ve Kullanıcı grupları seçenekleri listelenir.

- Belge onaylayanlar/reddedenler seçeneği, ilgili akış tasarımında akış, Pozisyon Grubu nesnesine gelene kadar kimler aksiyonda bulunmuşsa o kişileri Pozisyon Grubuna eklemek için kullanılan seçenektir. Geliştirici isterse tekrar "İçerikler" butonuna basarak grup içeriğini doldurmaya devam edebilir.

![Pozisyon Grubu](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3c41c6fd-a82b-474c-9e88-ba2de9aa68ce)

![Pozisyon Grubu](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb0c18b5b-2a4e-4e2a-816f-5aa274255bdf)

- Unvana göre kullanıcı grubu seçeneği, Pozisyon Grubu nesnesine belirli bir unvan tanımına sahip kullanıcıları eklemek için kullanılan seçenektir. "İçerikler" alanından bu seçenek seçildiğinde ekrana, sistemde tanımlı tüm unvan kayıtları listelenir.

![Pozisyon Grubu](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbc4193f9-1446-4d32-be10-00a1d0768be2)

![Pozisyon Grubu](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbb30c426-c458-4c72-ba0a-733581ea145c)

Aşağıdaki ekran görüntüsünde yapılan seçime göre “Project Manager” unvanlı kullanıcılar eklenecek demektir. Geliştirici isterse tekrar "İçerikler" butonuna basarak grup içeriğini doldurmaya devam edebilir.

![Pozisyon Grubu](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcf36973e-7435-42e8-8cef-43ac88db04a0)

![Pozisyon Grubu](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadec83e4a3-5649-4643-ae55-f6181f024204)

- Departmana göre kullanıcı grubu seçeneği, Pozisyon Grubu nesnesine belirli bir departmanda bulunan kullanıcıları eklemek için kullanılan seçenektir. "İçerikler" alanından bu seçenek seçildiğinde ekrana, sistemde tanımlı tüm departman kayıtları listelenir.

![Pozisyon Grubu](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb32031ea-b705-4486-8341-6b5ac35e4552)

![Pozisyon Grubu](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbdf6626c-cc3c-40b7-a56c-aa2e5028c032)

Aşağıdaki ekran görüntüsünde yapılan seçime göre Pozisyon Grubu nesnesine, "Product Management" departmanındaki kullanıcılar eklenecek demektir. Geliştirici isterse tekrar "İçerikler" butonuna basarak grup içeriğini doldurmaya devam edebilir.

![Pozisyon Grubu](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5cb3031e-4892-4738-85da-daefc93393f4)

![Pozisyon Grubu](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb1062ba0-2fc2-4dc8-8003-5f9fe5c74dab)

- Kullanıcı grupları seçeneği seçildiğinde ekrana, kullanıcı arayüzünde bulunan İnsan Kaynakları başlığı altında tanımlanmış **[Kullanıcı Grupları](web/human-resources/user-groups.md)** listelenir. Geliştirici bu listeden kullanıcı grubu seçimi yaptığında, Pozisyon Grubu nesnesine seçilen kullanıcı grubunun içine tanımlı kullanıcılar eklenmiş olur. İnsan Kaynakları bölümünden ilgili kullanıcı grubuna yeni kullanıcılar eklendiğinde ya da gruptan kişi çıkarıldığında, bu kullanıcı grubunun seçildiği Pozisyon Grubu nesnesine gelen akış, kullanıcı grubunun son güncel haliyle içinde bulunan kişilere onaya gönderilmiş olur.

![Pozisyon Grubu](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadde3564c4-6ea2-47cd-abc8-e4726f571441)

![Pozisyon Grubu](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfa906b89-753a-43d8-967b-3814ca60f4e9)

![Pozisyon Grubu](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload25647cb5-bae3-4f52-ba98-93ef9d133e32)

![Pozisyon Grubu](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload627c0d12-c193-4e6e-988b-a7509da71833)

#### Dokuman üzerindeki nesne seçimi yapılırsa {#members-documents}

- Doküman üzerindeki nesne seçeneği seçildiğinde form üzerindeki bir [DataGrid](form/advanced-form-controls/DataGrid.md) nesnesinde seçilen kullanıcı veya pozisyonları, Pozisyon Grubu nesnesine eklemek için kullanılır. Alanda kişi ekleme işlemi pozisyon bazlı veya kullanıcı bazlı yapılabilmektedir.

Eğer form üzerindeki DataGrid nesnesinde seçilen kişiler, kullanıcı bazlı olarak alana eklenmek isteniyorsa, tablo nesnelerinin “Kullanıcı Adı(sicil no)” bilgisini barındıran bir ID kolonuna sahip olması gerekir.

Eğer form üzerindeki DataGrid nesnesinde seçilen kişiler, pozisyon bazlı olarak alana eklenmek isteniyorsa, tablo nesnelerinin “Pozisyon id” bilgisini barındıran bir ID kolonuna sahip olması gerekir.

İçerikler alanından “Doküman üzerindeki nesne” seçeneği seçildiğinde ekrana aşağıdaki alanlar gelecektir;

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Document 	| Bu alanda akış tasarımında bulunan tüm Doküman nesneleri listelenir. Hangi form üzerindeki DataGrid nesnesinin verilerine erişilmek isteniyorsa, o formun tanımlı olduğu Doküman nesnesi bu alandan seçilir. 	|
| Data type 	| “Kullanıcı” ve “Pozisyon” seçenekleri listelenir. Pozisyon Grubu alanına eklenecek kayıtlar kullanıcı bazlı eklenecekse bu alandan “Kullanıcı”, pozisyon bazlı eklenecekse bu alandan “Pozisyon” seçeneği seçilmelidir. 	|
| Table / Details 	| Documents alanında eklenen form üzerindeki hangi DataGrid nesneden seçilen kişiler Pozisyon Grubu nesnesine eklenecekse, ilgili nesnenin seçimi yapılır. 	|
| Field 	| Bu alanda, DataGrid nesnesinin kolonları listelenir. Data type olarak “Kullanıcı” seçilmişse bu alanda, kullanıcı id lerinin bulunduğu kolonun seçimi yapılmalıdır. Data type olarak “Pozisyon” seçilmişse bu alanda, pozisyon id lerinin bulunduğu kolonun seçimi yapılmalıdır. 	|

### Documents

`Documents` - Bu alanda, Pozisyon Grubu nesnesindeki kullanıcının hangi formu ve formun hangi görünümünü (view) görebileceği ayarlanır. Projeye dahil olan formlar akış tarafında Doküman nesnesi içerisinde tutulur. Doküman nesnesi, kendisine bağlanan formu ve form üzerindeki verileri temsil eder. Akış üzerinde birden çok, farklı formları temsil eden Doküman nesneleri bulunabilir. Pozisyon Grubu nesnesindeki kullanıcının hangi formu görmesi isteniyorsa, bu alandan, ilgili formun bağlı olduğu Doküman nesnesinin seçimi yapılıp gerekli ayarları belirlenir.

![Pozisyon Grubu](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload121cb870-5e3c-4a50-9b33-ddb69a534b4c)

Pozisyon Grubu nesnesinde tanımlı kullanıcıya web arayüzünde görmesi için birden fazla Doküman nesnesi de eklenebilir. Documents kısmına tıklandığında açılan ekranda kullanıcının görmesi istenen bir ya da birden çok Doküman nesnesi “Ekle” butonu ile eklenip, doküman üzerinde yapılabilecek düzenlemelerin ayarları belirlenir.

![Pozisyon Grubu](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1750c125-9cbc-40e2-b7c9-e74f72db9c84)

**Properties sekmesi özellikleri**

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Document 	| Akış tasarımı üzerindeki tüm Doküman nesnelerinin listelendiği alandır. Pozisyon Grubu nesnesindeki kişiye gösterilmek istenen formun bağlı olduğu Doküman nesnesi bu alandan seçilir. 	|
| View 	| “Doküman” alanından seçilen Doküman nesnesinin bağlı olduğu formun görünümleri (view) bu alanda listelenir. Pozisyon Grubu içindeki kullanıcı formu açtığında hangi form görünümünü görmesi isteniyorsa bu alandan seçimi yapılmalıdır. Görünüm alanından herhangi bir seçim yapılmazsa kullanıcı, “default” görünümü görecektir. 	|
| Panel Size 	| Web arayüzünde tanımlanan doküman nesnesinin hangi genişlikte açılabileceğinin belirlendiği alandır. 1-2-3 değerlerinden birisi seçilerek açılan panel boyutu seçilen değer genişliğinde açılacaktır. 	|
| Editable 	| Pozisyon Grubu nesnesindeki kullanıcıların, doküman üzerinde düzenleme yapıp, yapamayacağı bu alandan belirlenir. Düzenle alanı işaretli olmayan bir doküman, kullanıcıya web arayüzünde salt okunur modunda açılır ve kişi formu düzenleyemez. Form üzerinde düzenleme yapılması isteniyorsa bu alan işaretlenmelidir. 	|
| Show events 	| İlgili adımdaki kullanıcının, formu ilerletmek ve akışı devam ettirmek için aksiyon alacağı olay butonlarının form üzerinde gösterilip gösterilmeyeceğinin ayarlandığı alandır. Kullanıcının, ilgili doküman üzerinde işlem yapıp, bir iş akışına dahil etmesi için aksiyon butonlarını kullanması gerekiyorsa bu alan işaretli olmalıdır. Eğer doküman kullanıcıya bilgi amaçlı eklenmişse, aksiyon olay butonlarının bu dokümanda görünmesine gerek yoktur ve bu durumda "Show events" alanı işaretlenmemelidir. 	|
| Signature 	| Sistem, dijital imza altyapısını desteklemektedir. Dijital imza sağlayıcılarından sertifika alınmışsa, bu seçenek iş akışlarının ve belgelerin imzalı onayları için kullanılabilir.İmza alanında 4 seçenek listelenir;<br/> **No sign :** Belge üzerinde dijital imza kullanılmayacağını belirtmek için seçilir<br/> **Optional :** İsteğe bağlı olarak doküman üzerinde dijital imza kullanılacağı durumda seçilir. Süreç ilgili kullanıcıya geldiğinde belgenin dijital olarak imzalanıp imzalanmayacağı kullanıcıya bırakılmıştır.<br/> **Required :** Kullanıcının, sertifikası var mı yok mu ayırt etmeksizin, belgeyi bir dijital imza sertifikasıyla imzalamasını zorunlu kılar.<br/> **Required if possible :** Kullanıcı için bir dijital imza sertifikası varsa, sistem kullanıcıyı belgeyi onaylamak için dijital imza sertifikasını kullanmaya zorlar. Zorunluluk, yalnızca belirli bir sertifika varsa kullanıcıya uygulanır. 	|

**Signature sekmesi özellikleri**

Belge imzalama ayarlarıyla ilgili detaylı düzenlemelerin yapıldığı kısımdır.

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Signature 	| Belgenin CAdES veya PAdES türlerinden hangisi kullanılarak imzalandığının belirlendiği alandır. 	|
| Timestamp 	| Belge imzalanırken zaman dangası kullanılmak istendiğinde aktif edilen özelliktir. 	|

:::danger UYARI

Nesne içinde eklenen doküman nesnesinde imza ayarı yapıldıysa, imza atılmak istenen doküman nesnesi **belge (pdf vb. dokümanlar)** içermelidir ve imzalar belgeler üzerine atılmalıdır. **CSP formları üzerine imza atılamaz!**

:::

:::caution DİKKAT

Nesne içinde eklenen doküman nesnesinde imza ayarı yapıldıysa, imza işleminin web ara yüzünde başlatılabilmesi için aynı nesnede Events bölümünde ekli hangi olayda imza işleminin yapılacağı, olaydaki **Digital Signature Required** seçimi aktif edilmelidir.

:::

### Message

`Send Mail` - Akış adımı ilgili Pozisyon Grubu nesnesine düştüğünde, sistem otomatik olarak nesnedeki kişiye, onayına bir süreç düşürüldüğünün bilgisini mail olarak gönderir. İlgili nesnede aksiyon düştüğünde mail gönderilmesi istenmiyorsa, Send Mail alanının işareti kaldırılabilir. Bu durum genelde test amaçlı akış senaryosu denemelerinde kişilere mail gitmemesi için kullanılır.

:::tip İPUCU

Nesneler içinde gezerek e-posta gönderimini kapatmaya ek olarak akış genelinde de e-posta gönderimini engellemek mümkündür. **[Flow Properties->General](index.mdx#general)** içindeki **Disable Email Sending** özellği aktif edilerek e-posta gönderimi akış genelinde kapatılabilir.

:::

`Caption` - Pozisyon Grubu nesnesindeki kullanıcılara gönderilecek onay mailinin başlık bilgisidir. Başlık bilgisinde varsayılan olarak gelen “ProcessCaption“, “FirstName” ve “LastName” parametreleri bulunur. Bu parametreler sistemin kendi parametreleridir ve mailin gönderildiği sürecin başlığı, mailin gönderildiği kişinin adı ve soyadı bilgileri otomatik olarak sistem tarafından doldurulur. Varsayılan olarak gelen mail başlığı yapısı aşağıdaki gibidir. Geliştirici isterse bu mail başlığını değiştirebilir.

> *Bimser Synergy {{ProcessCaption}} onayı ({{FirstName}} {{LastName}})*

`Message` - Pozisyon Grubu nesnesindeki kullanıcılara gönderilecek mailin mesaj metin kısmı bu alanda yer alır. Varsayılan olarak gelen mesaj metni, isteğe bağlı olarak değiştirilebilir.

`Attachments` - Pozisyon Grubu nesnesindeki kullanıcılara gönderilecek mail içinde ek dosya gönderilmek istenirse bu alandan tanımlanır.

![Pozisyon Grubu](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade25bd6d5-6000-4007-8859-b779e30787c8)

Atttachments alanına tıklandığında, gönderilecek e-postaya eklenmek istenen ek türünün seçileceği tanımlanacağı ekran açılır.

![Pozisyon Grubu](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload326a75ac-a969-42c8-be50-74370a282046)

Attachments düzenleme penceresinde **“Ekle”** butonu ile Pozisyon Grubu nesnesinde kişiye gönderilecek e-postaya ek eklenmesi için tanım yapılabilir, yapılmış tanımda satır üzerine tıklanarak ek ayarlarında değişiklik yapılabilir ya da ek satırı detaylarında beliren çöp kutusu ikonuna basılıp olay, nesne üzerinden kaldırılabilir.

![Pozisyon Grubu](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf6fa8a71-b7bb-4d2b-8b6f-2e55a975a0f6)

- Type alanı ek dosyanın nerede bulunduğunun seçildiği alandır. DM, Flow, RelatedDocuments seçimleri yapılabilir.
    - Type:DM seçildiğinde panelde Value alanı içinde Doküman Yönetimi içinde seçim yapılır.
    - Type:Flow seçildiğinde ek olarak eklenecek dosyanın Id bilgisinin bulunduğu nesne liquid olarak seçilebilir veya statik veri yazılabilir. ({{ Document1.DocumentId }}, {{ Variable1.Value }}, 56669)
    - Type:RelatedDocuments seçildiğinde Document alanı gözükerek kullanılacak RelatedDocuments nesnesinin bulunduğu formu içeren Doküman nesnesi seçilir. Seçim yapılması ile panelde Related Documents alanı gözükerek seçilen nesne içindeki **Related Documents** nesneleri listelenerek seçim yapılır.

![Pozisyon Grubu](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6389d340-5597-496b-9150-8d8764cc9323)

`Edit Message Source` - Pozisyon Grubu nesnesindeki kişilere gönderilecek mesajın, sistem varsayılanı olarak değil, özelleştirilmiş bir mesaj şablonu olarak gönderilmesi isteniyorsa bu özellik aktif edilir. Özellik aktif edildiğinde “Source Message” isimli alan görünür olacaktır.

`Source Message` - Varsayılan mail şablonunun html formatta görüntülenerek, üzerinde değişiklik yapılmasına izin veren ekran, bu alandan açılır. Tasarlanan mail şablonu, önizleme penceresinde anlık olarak görüntülenebilir.

Elektronik postada belli bir dil düzenlenmek istenirse panel içindeki dil seçeneği değiştirilerek, seçilen dile ait e-posta kodları ve önizlemesi yapılabilir.

![Pozisyon Grubu](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload603e5b89-e2c4-49d2-942e-4f3c15bba4e8)

:::info BİLGİ

Kullanıcıların sistemde hangi dilde e-posta alacakları, İnsan Kaynakları bölümünde her kullanıcıdaki **Varsayılan Dil** alanında yapılan seçime göre belirlenmektedir.

<div style={{textAlign: 'center'}}>

![Pozisyon Grubu](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf8a6f7cd-631a-4030-b80e-6c6927e4abc2)

</div>

:::

### Push Notification

:::caution DİKKAT

Push Notification mobil uygulama üzerinden Bimser Synergy CSP uygulamasına giriş yapmış ve bildirimlere izin vermiş kişi/kişilerin cihazlarına gönderilir.

:::

`Send Push Notification` - Pozisyon Grubu nesnesindeki kişilerin mobil cihazında bildirim gönderilmek istenirse alan aktif edilir.

`Caption` - Pozisyon Grubu nesnesindeki kişilere gönderilecek mobil bildirimin başlık bilgisidir. Başlık bilgisinde varsayılan olarak gelen “ProcessCaption“, “FirstName” ve “LastName” parametreleri bulunur. Bu parametreler sistemin kendi parametreleridir ve bilgilendirmenin gönderildiği sürecin başlığı, mailin gönderildiği kişinin adı ve soyadı bilgileri otomatik olarak sistem tarafından doldurulur. Varsayılan olarak gelen mail başlığı yapısı aşağıdaki gibidir. Geliştirici isterse bu mail başlığını değiştirebilir.

> *Bimser Synergy {{ProcessCaption}} onayı ({{FirstName}} {{LastName}})*

`Message` - Pozisyon Grubu nesnesindeki kişiye gönderilecek bilgilendirme mesaj metin kısmı bu alanda yer alır. Varsayılan olarak gelen mesaj metni, isteğe bağlı olarak değiştirilebilir.

### Flow Control

`Empty Group Event` - Kodla doldurulan bir grup nesnesi için sorgudan kayıt dönmemesi, gruba tanımlı kullanıcı grubunun boş olması veya herhangi farklı bir senaryo ile grup içeriğinin boş kalması durumunda, akış Pozisyon Grubu nesnesine geldiğinde sistem tarafından “Grup Boş” hatası alınmaması için akış, grup nesnesinden bu alanda seçilen olay oku kolundan otomatik ilerletilir. Burada amaç akışın; grup içeriği boş olduğunda, varsayılan olarak seçilen olay kolundan ilerlemesini sağlayarak devam ettirmektir.

Bu alanda, Pozisyon Grubu nesnesine Olaylar alanından eklenen olaylar listelenmektedir. Grup boşken akışın hangi olay kolundan ilerlemesi isteniyorsa bu alandan ilgili olay seçilmelidir. Pozisyon Grubu nesnesi akış tasarım ekranına süreklendiğinde varsayılan olarak “Onayla” ve “Reddet” olayları ekli gelir. O yüzden değişiklik yapılmadığı durumda bu alanda da “Onayla” ve “Reddet” olayları listelenir.

:::caution DİKKAT

Pozisyon Grubu nesnesine tanımlı olaylar değiştirildiğinde, “Empty Group Event” alanında seçili olay da mevcut tanımlı olaylardan biri seçilerek değiştirilmelidir.

Örneğin; Pozisyon Grubu nesnesine “Onayla” olayı eklenmiş olsun ve “Empty Group Event” alanından da “Onayla” seçeneği seçilmiş olsun. Geliştirici, gruptan “Onayla” olayını kaldırıp yerine “Gönder” olayını eklemiş olsun. Bu durumda “Empty Group Event” alanında hala silinen olay olan “Onayla” olayı kalmış olacak ve süreç bu adıma geldiğinde hata verecektir. Olaylar alanından kaldırılan bir olay, “Empty Group Event” alanından da kaldırılmalı ve bu alanda, var olan bir olayın seçimi yapılmalıdır.

:::

`Conflict State Event` - Pozisyon Grubunda sürecin ilerleme şartı olarak “Çoğunluk” seçilmiş olsun. Burada; gruptaki kişilerden çoğunluğu onay verirse akış ilerlesin isteniyor. Grupta 4 kişi olduğu düşünülürse ve 2 kişi onaylayıp, 2 kişi reddederse çoğunluk şartı sağlanmamış olacak ve akış kararsız kalacaktır.

Bir başka senaryo olarak, Pozisyon Grubunda sürecin ilerleme şartı “Tümü” seçilmiş olsun. Gruptaki kişilerin hepsi onay verirse akış ilerlesin isteniyor. Ancak gruptan 1 kişi bile reddet olayına bastığında akış yine ilerleyememiş olacak ilerleme şartı sağlanamayıp kararsız bir durum yaşanacaktır.

Bu gibi çatışma durumlarında, akışın askıda kalmaması veya hata vermemesi için “Conflict State Event” alanından varsayılan bir olay seçilir ve grupta böyle bir kararsızlık yaşandığında akışın, seçilen olay kolundan ilerlemesi sağlanmış olur.

:::caution DİKKAT

Pozisyon Grubu nesnesine tanımlı olaylar değiştirildiğinde, “Conflict State Event” alanında seçili olay da mevcut tanımlı olaylardan biri seçilerek değiştirilmelidir.

Örneğin; Pozisyon Grubu nesnesine “Onayla” olayı eklenmiş olsun ve “Conflict State Event” alanından da “Onayla” seçeneği seçilmiş olsun. Geliştirici, gruptan “Onayla” olayını kaldırıp yerine “Gönder” olayını eklemiş olsun. Bu durumda “Conflict State Event” alanında hala silinen olay olan “Onayla” olayı kalmış olacak ve süreç bu adıma geldiğinde hata verecektir. Olaylar alanından kaldırılan bir olay, “Conflict State Event” alanından da kaldırılmalı ve bu alanda, var olan bir olayın seçimi yapılmalıdır.

:::

`If Processed Before Do Not Send Request` - Akış senaryosuna göre, bazı durumlarda işlem yapan bir kişiye akış tekrar gönderilebilir. Bu gibi durumlarda kullanıcının tekrar aksiyon yapmasına gerek olmadan sürecin devam etmesi istenilebilir.

Durumu bir örnek ile açıklamak gerekirse, tasarlanan bir İş Akışında kullanıcının müdür onayından sonra sürecin IK müdürü onayına gitmesi isteniyor olsun. Böyle bir senaryoda IK departmanından bir personel iş sürecini başlattığında müdürü olarak zaten IK müdürü süreci onaylayacağından tekrar belge kendisine gelecektir ve ikinci kez aynı belgeyi onaylamak durumunda kalacaktır. Bu gibi senaryolar ile karşılaşmamak için “If Processed Before Do Not Send Request” seçeneğinden faydalanılır.

“If Processed Before Do Not Send Request” seçeneği aktif edildiğinde "Before Processed Events" ve "If Document(s) is/are Changed Then Request is Needed" başlıklı yeni kontrol alanları görünür olacaktır.

`Before Processed Events` - Kullanıcı alan üzerinde tanımlı olaylardan biri ile daha önceden onay verdiyse, alanda ilgili event seçilerek sürecin otomatik olarak onaylanmasını sağlar.

Örneğin, tasarlanan bir İş Akışında kullanıcının müdür onayından sonra sürecin IK müdürü onayına gitmesi isteniyor ve her iki nesnede de "İzin Talebini Onayla" eventi olsun. Böyle bir senaryoda IK departmanından bir personel iş sürecini başlattığında müdürü olarak zaten IK müdürü süreci onaylayacağından tekrar belge kendisine gelecektir. Ancak alanda "İzin Talebini Onayla" eventi ekli olduğu ve IK müdürü halihazırda öncesinden bu eventi kullanarak onay verdiği için süreç otomatik olarak devam edecektir.

:::tip İPUCU

If Processed Before Do Not Send Request ve Before Processed Events kullanıcı daha önce süreci tanımlı event'i kullandıysa çalışır.

:::

:::caution DİKKAT

If Processed Before Do Not Send Request özelliği bir kere çalıştığında pasif durumuna geçer, yenien aktif etmek için API seviyesinde (nesne özelliğine akış içinde erişilerek) kod yazılabilir.

:::

`If Document(s) is/are Changed Then Request is Needed` - Biraz önceki senaryomuzu biraz daha detaylandıralım ve müdür onayı ile IK müdürü onayı arasına bir başka pozisyon onayı olduğunu varsayalım. IK personeli belgeyi doldurduğunda öncelikli olarak müdürüne –yani burada müdür IK müdürü oluyor- daha sonra iş sürecinde yer alan diğer Pozisyon onayına gidecektir. Diğer pozisyon onayından sonra da “If Processed Before Do Not Send Request” seçeneğinden dolayı IK müdürüne tekrar uğramadan süreç tamamlanacaktır. Ancak şayet senaryomuzda yer alan Pozisyon Grubu nesnesi belgede herhangi bir değişiklik yaptıysa, yani belge IK müdürünün ilk onayından farklı bir hale geldiyse, IK müdürü ikinci kez bu belgeyi görmeden süreç tamamlanacaktır. Bu gibi durumları ortadan kaldırmak için ikinci bir seçenek olarak sisteme “If Document(s) is/are Changed Then Request is Needed” seçeneği eklenmiştir. Böylelikle bu seçeneği kullanarak yukarıda anlatılan senaryoda yer alan IK müdürüne ilgili belgenin tekrar gitmesi sağlanabilir.

### Events

`Events` - Pozisyon Grubu üyesinin, web arayüzünde form için alabileceği aksiyon olaylarının tanımlandığı kısımdır. Bu alanda tanımlanan olaylar, web arayüzünde form üzerinde aksiyon butonları olarak görünür. Kullanıcı hangi olay butonuna tıklarsa süreç, dizayn anında o olaya ait bağlantı okunun bağlandığı akış adımına ilerler.

Nesneye Events alanından kaç tane olay eklenmişse, akış tasarım ekranında nesneden, her bir olayı temsil edecek bağlantı okları çıkarılmalı ve ilgili olaya tıklandığında akışın nereye gitmesi isteniyorsa bu oklar oraya bağlanmalıdır.

Events alanına tıklandığında, nesneye eklenecek olayların seçilebileceği ve bu olaylar için düzenlemelerin yapılabileceği bir pencere açılacaktır. Burada olay kayıtları olarak, **[Flow Properties->Events](index.mdx#events)** tabında tanımlanmış olaylar listelenir. Varsayılan olarak Pozisyon Grubu nesnesine “Onayla” ve “Reddet” olayları ekli olarak gelir. Mevcut olaylar üzerinde değişiklik yapmak, yeni olay eklemek ya da mevcut olayı nesneden kaldırmak için Events alanına tıklanarak olay düzenleme penceresi açılır.

![Pozisyon Grubu](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload13d7c5bd-0643-45e5-b5c6-4bfc7d0c6116)

Events düzenleme penceresinde “Ekle” butonu ile Pozisyon Grubu nesnesine yeni bir olay eklenebilir, ekli olaylar için olay satırı üzerine tıklanarak olay ayarlarında değişiklik yapılabilir ya da ekli olay satırına gelindiğinde beliren çöp kutusu ikonuna basılıp olay, nesne üzerinden kaldırılabilir.

![Pozisyon Grubu](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6455cf62-9c3e-4412-9e9b-6ed30a4b38e6)

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Identity 	| Olayı ifade eden id değeri bu kısımda görünür. Bu alan salt okunur moddadır ve değiştirilemez. 	|
| Description 	| Olayın metin kısmının göründüğü alandır. 	|
| Visible 	| Web arayüzünde ilgili olay butonunun görünmesi için bu özellik aktif edilmelidir. 	|
| Validate 	| Form dizayn anında nesne özelliklerinde verilen zorunluluk şartlarının ve formun validasyon Kural Yöneticisi kısmında yazılan kontrollerin çalışarak, istenen durumun sağlanmadığı veya zorunlu nesnelerin boş bırakıldığı durumlarda kullanıcıya uyarı mesajı verilmesi için, kullanıcının tıkladığı olay butonunda “Validate” alanının işaretli olması gerekir. 	|
| Reason 	| Sebep alanı işaretlenmiş bir olaya web arayüzünde tıklandığında, kullanıcının karşısına sebep açıklamasını girmesi için bir alan çıkarılır. Genelde Reddet olayı için kullanılır ve kişi Reddet butonuna basarak formu reddetmek istediğinde, red nedenini sebep alanına girmesi istenir. 	|
| Reason Title 	| Web ara yüzünde sebep açıklamasının gösterildiği alan başlığındaki ifadenin özelleştirilmesinin yapıldığı alandır. 	|
| Digital Signature Required 	| Dijital imza gerekli alanı işaretlenmiş bir olaya web arayüzünde tıklandığında kullanıcının E-imza işlemi gerçekleştirmesi için gerekli ekran açılacaktır. İmza işleminin başlaması için nesneye tanımlı doküman nesnesinde Signature ayarları yapılmış olmalıdır. 	|
| Form 	| Form alanından, akışta bulunan bütün Doküman nesneleri listelenir. Herhangi bir event için bu alandan bir Doküman nesnesi seçildiğinde, web arayüzünde bu olaya tıklandığında kullanıcının karşısına Form alanından seçilen Doküman nesnesi içindeki tanımlanmış formun ekranı açılır ve kullanıcının formdaki alanları doldurması beklenir. Kullanıcı açılan formu doldurup tamam dediğinde akış bir sonraki adıma ilerler. Doldurulan bu form, ilgili akış nesnesinin “Event Formu” olmuş olur. 	|
| Icon 	| Web arayüzünde formun üzerinde belirecek olan olay butonlarının ikonları bu alandan seçilir. Varsayılan olarak gelen olayların sistemde bulunan ikonları otomatik olarak ikon kolonunda belirtilmiş olur. 	|
| Condition 	| Bu alan, her bir olay için, akışın o olaydan ilerlemesinin bağlı olduğu koşulun seçildiği alandır. Koşul alanında seçenek olarak; Tümü, Sayı, Çoğunluk, Yüzde değerleri listelenir.<br/><br/> **Tümü :** Pozisyon grubu nesnesine gelen akışın ilerleyebilmesi için, grubun tüm üyelerinin, Condition alanında “Tümü” seçilen aksiyon olayına tıklamış olması beklenir.<br/>Örneğin; Pozisyon Grubuna olay olarak “Onayla” olayı eklenmiş ve Condition alanından “Tümü” seçilmişse, akışın ilerleyebilmesi için grup üyelerinin hepsinin “Onayla” butonuna basmış olması gerekir. Condition alanından “Tümü” seçilmişse, “Condition Value” alanı gösterilmez.<br/><br/>**Sayı :** Pozisyon grubu nesnesine gelen akışın ilerleyebilmesi için, belirtilen sayı kadar ilgili olay aksiyonunun alınmasının yeterli olduğu durumlarda kullanılır.<br/>Örneğin; Pozisyon Grubuna olay olarak “Onayla” olayı eklenmiş ve Condition alanından “Sayı” seçilmişse, “Condition Value” alanına yazılan sayı kadar grup üyesinin, “Onayla” butonuna basması, akışın ilerlemesi için yeterlidir. 5 kişinin bulunduğu bir gruptan yalnızca 1 kişinin onay vermesi yeterli gibi bir işlem yapılmak isteniyorsa, Condition alanından “Sayı” seçilmeli, Condition Value alanına 1 yazılmalıdır. Böylece gruptan 1 kişi Onayla butonuna bastığında akış diğer grup üyelerinin aksiyon almasını beklemez, diğer grup üyeleri üzerinde bekleyen işi kaldırır ve süreci bir sonraki adıma ilerletir.<br/><br/>**Yüzde :** Pozisyon grubu nesnesine gelen akışın ilerleyebilmesi için, grup üyelerinin belirli bir yüzdesinin ilgili aksiyonu almış olması gerekir.<br/>Örneğin; Pozisyon Grubuna olay olarak “Onayla” olayı eklenmiş ve Condition alanından “Yüzde” seçilmişse, “Condition Value” alanına yazılan sayının yüzdesi kadar (Condition Value alanına 30 yazılmışsa grubun %30 u aksiyon aldıysa demektir) grup üyesinin, “Onayla” butonuna basması, akışın ilerlemesi için yeterlidir.<br/><br/>**Çoğunluk :** Pozisyon grubu nesnesine gelen akışın ilerleyebilmesi için, grup üyelerinin çoğunluğunun ilgili aksiyon olayını almış olması gerekir. Burada sistem otomatik olarak %51 oranını baz alır. “Condition Value” alanı gözükmez. 	|

:::caution DİKKAT

Nesne içeriğine eklenmiş bir olayın ayarları, **Flow Properties->Events** kısmından değiştirilmişse, nesne içeriğindeki ekli olay kaydı bu değişiklikten etkilenmemiş olabilir. Değişiklik sonrası ilgili olayı kullanan nesneler kontrol edilerek, Olaylar alanından değişikliğin yapıldığı olayın kaldırılıp tekrar eklenmesi gerekebilir.

:::

:::caution DİKKAT

Nesneye eklenmiş bir olay, **Flow Properties->Events** alanından silinirse, bu olayı kullanan nesneler kontrol edilerek, nesne içindeki ilgili ekli olay kaydının da silinmesi gerekir.

:::

### Options

`Hide the Approver` - Akış tarihçesinde, pozisyondaki kullanıcının adını * * * * şeklinde gizli göstermeye yarayan özelliktir.

`Show in the Flow History` - İlgili akış adımının akış tarihçesinde gösterilip gösterilmeyeceğinin ayarlandığı kısımdır.

### Time Out

Bu kısım, Pozisyon Grubu nesnesine zaman aşımı aksiyonu eklemek için kullanır. Akış, pozisyon nesnesine düştüğünde, belirli bir süre içerisinde, pozisyondaki kişi herhangi bir aksiyon almamışsa, isteğin zaman aşımına uğraması ve akışın herhangi bir yerinden, işlemin devam etmesi istenirse, bu bölümde bulunan kısımlar doldurulur. Zaman Aşımı bölümünde bulunan alanlar dolu ise ve Pozisyon Grubu nesnesinden, “Zaman Aşımı” bağlantısı çıkarılmışsa, belirlenen süre sonunda istek zaman aşımına uğrar ve akış, “Zaman Aşımı” kolunun bağlandığı yerden ilerler.

`Day` - Pozisyon Grubu nesnesinde beklenen aksiyonun, belirli bir gün sonunda zaman aşımına uğraması isteniyorsa, bu alanda zaman aşımı gün bilgisi yazılır.

`Hour` - Pozisyon Grubu nesnesinde beklenen aksiyonun, belirli bir saat sonunda zaman aşımına uğraması isteniyorsa, bu alanda zaman aşımı saat bilgisi yazılır.

`Minute` - Pozisyon Grubu nesnesinde beklenen aksiyonun, belirli bir dakika sonunda zaman aşımına uğraması isteniyorsa, bu alanda zaman aşımı dakika bilgisi yazılır.

`Calculate Using Working Hours` - Zaman aşımı süresini, sistemde tanımlı çalışma saatleri hesaplanarak çalıştırmak için bu alan işaretlenir.

`Calculate Using Holidays` - Zaman aşımı süresini, sistemde tanımlı tatil günleri hesaplanarak çalıştırmak için bu alan işaretlenir.

:::info BİLGİ

Nesne üzerinde ekli özelliklerin doğru olduğu sistem tarafından kontrol edilmektedir. Eksik bir özellik bulunduğunda nesne üzerinde kırmızı ünlem ikonu gösterilerek, fare işaretçisi ile ikon üzerine gelindiğinde nelerin eksik veya hatalı olduğu görüntülenebilmektedir.

![Pozisyon Grubu](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddaa4719d-af29-45d2-9fb3-e2e1bf2b0109)

:::

## Events

Pozisyon Grubu nesnesinin sahip olduğu olaylar, Özellik Görüntüleyici panelindeki "Events" sekmesinde yer almaktadır. Her bir olay, farklı çalışma anlarında tetiklenerek kendilerine özgü işlemleri gerçekleştirir. Bu olaylara geliştirici tarafından yazılan kodlar da ilgili olayın tetiklendiği anda çalıştırılır. Herhangi bir olaya kod yazmak için, Olaylar sekmesinden ilgili olay satırına çift tıklanır. Ekran, “Akışadı.cs” isimli akış kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur. Geliştirici bu method içerisinde istediği kod bloğunu kurgulayabilir. Olaylar sekmesinden tıklanarak kod tarafında methodu oluşturulmuş olayın yanında, method adı bilgisi otomatik oluşturularak, olayla method arasındaki ilişki belirtilmiş olur.

![Pozisyon Grubu](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6f51052b-9f59-40b3-87bb-714d7a38cac6)