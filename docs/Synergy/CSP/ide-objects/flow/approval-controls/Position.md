---
sidebar_position: 2
custom_edit_url: ""
---

# Pozisyon

Pozisyon nesnesi, akış içerisinde yer alan kullanıcı aksiyon adımlarını temsil eder.

Akış tasarımına yerleştirilen her bir pozisyon nesnesinde tanımlı uç kullanıcıdan sistem tarafından bir aksiyon yapılması beklenmektedir. Temel olarak bu nesne, bir iş sürecini kişinin onayına sunmak için kullanılır. Sistem varsayılan olarak akış tasarımı üzerine koyulan her bir “Pozisyon” nesnesi için ilgili uç kullanıcıya bir onay maili göndermekte, ayrıca bu iş sürecinin Web arabiriminde kullanıcının “Onaylar” listesine yerleşmesini sağlamaktadır.

Pozisyon nesnesinin içeriği tasarım sırasında statik olarak verilebileceği gibi çeşitli yöntemler ile dinamik olarak değiştirilebilir. Bu yöntemlerden en geneli **[“Atama”](standart-flow-controls/Assignment.md)** nesnesini kullanmaktır. Bu nesne yardımıyla, ilgili iş süreci adımında yer alan kullanıcı, dinamik olarak bulunarak içerik, akış sırasında değiştirilebilir. Pozisyon nesnesine kod ile de kullanıcı ya da pozisyon bazlı kişi ataması yapılabilir.

Akış tasarım ekranında bulunan nesneye tıklandığında, Özellik Görüntüleyici panelinde, nesne özellikleri görünür.

Pozisyon nesnesine tıklandığında Özellik Görüntüleyici panelinde "Appearance", "Properties" ve "Events" sekmeleri bulunmaktadır.

![Pozisyon](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada7c52220-b687-4d5f-b4d3-2aa7d26ae94e)

## Appearance

### Text Configs

`Object Name` - Nesnenin sistem tarafında kullanılacak ismidir. Kod tarafında nesneye, nesne adı alanında yazan değerle erişim sağlanır.

`Caption` - Nesnenin başlık metninin girildiği alandır.

`Is Lock` - Tasarım anında nesnenin yeri değiştirilmesin isteniyorsa bu alan aktif edilir.

`Size` - Nesnenin genişlik ve yükseklik ayarlarının yapıldığı kısımdır.

## Properties

### Value

`Type` -  Pozisyon nesnesinin hangi kullanıcı ya da pozisyonu temsil edeceği bu alandan belirlenir. Type alanından seçilen atama türüne göre Pozisyon nesnesine tanımlanacak değer listeleri değişecektir.

- **Type:Sabit pozisyon** seçimi; Pozisyon nesnesine, sistemde tanımlı bir pozisyon kaydını seçmek için kullanılır. Akış bu Pozisyon nesnesine geldiğinde, seçilen pozisyon kaydına sahip kullanıcıya onay isteği düşürülecektir. Tip alanından “Sabit Pozisyon” değeri seçildiğinde, “Değer” alanında sistemde tanımlı tüm pozisyon kayıtları listelenir. Değer alanından seçilen pozisyon tanımı, Pozisyon nesnesine set edilmiş olur ve artık bu Pozisyon nesnesi ilgili pozisyonu temsil eder.
- **Type:Sabit kullanıcı** seçimi; Pozisyon nesnesine, sistemde tanımlı bir kullanıcı kaydını seçmek için kullanılır. Akış bu Pozisyon nesnesine geldiğinde, seçilen kullanıcıya onay isteği düşürülecektir. Tip alanından “Sabit Kullanıcı” değeri seçildiğinde, “Değer” alanında sistemde tanımlı tüm kullanıcı kayıtları listelenir. Değer alanından seçilen kullanıcı tanımı, Pozisyon nesnesine set edilmiş olur ve artık bu Pozisyon nesnesi ilgili kullanıcıyı temsil eder.
- **Type:Akışı başlatan** seçimi; Akışı başlatan kullanıcıyı, Pozisyon nesnesine atamak için kullanılır. Akışı kim başlatmışsa, pozisyon nesnesine bu kişi otomatik atanır. Akış bu Pozisyon nesnesine geldiğinde onay, akışı başlatan kullanıcıya düşürülmüş olur.

### Message

`Send Mail` -  Akış adımı ilgili Pozisyon nesnesine düştüğünde, sistem otomatik olarak nesnedeki kişiye, onayına bir süreç düşürüldüğünün bilgisini mail olarak gönderir. İlgili nesnede aksiyon düştüğünde mail gönderilmesi istenmiyorsa, Send Mail alanının işareti kaldırılabilir. Bu durum genelde test amaçlı akış senaryosu denemelerinde kişilere mail gitmemesi için kullanılır.

:::tip İPUCU

Nesneler içinde gezerek e-posta gönderimini kapatmaya ek olarak akış genelinde de e-posta gönderimini engellemek mümkündür. **[Flow Properties->General](index.mdx#general)** içindeki **Disable Email Sending** özellği aktif edilerek e-posta gönderimi akış genelinde kapatılabilir.

:::

`Caption` -  Pozisyon nesnesindeki kullanıcıya gönderilecek onay mailinin başlık bilgisidir. Başlık bilgisinde varsayılan olarak gelen “ProcessCaption“, “FirstName” ve “LastName” parametreleri bulunur. Bu parametreler sistemin kendi parametreleridir ve mailin gönderildiği sürecin başlığı, mailin gönderildiği kişinin adı ve soyadı bilgileri otomatik olarak sistem tarafından doldurulur. Varsayılan olarak gelen mail başlığı yapısı aşağıdaki gibidir. Geliştirici isterse bu mail başlığını değiştirebilir.

> *Bimser Synergy {{ProcessCaption}} onayı ({{FirstName}} {{LastName}})*

`Message` -  Pozisyona gönderilecek mailin mesaj metin kısmı bu alanda yer alır. Varsayılan olarak gelen mesaj metni, isteğe bağlı olarak değiştirilebilir.

`Attachments` - Pozisyona gönderilecek mail içinde ek dosya gönderilmek istenirse bu alandan tanımlanır.

![Pozisyon](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada475cde9-564b-4f32-ace2-6182fb965b03)

Atttachments alanına tıklandığında, gönderilecek e-postaya eklenmek istenen ek türünün seçileceği tanımlanacağı ekran açılır.

![Pozisyon](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload86a50f04-0f22-419a-8f72-199fcf854f11)

Attachments düzenleme penceresinde **“Ekle”** butonu ile Pozisyon nesnesinde kişiye gönderilecek e-postaya ek eklenmesi için tanım yapılabilir, yapılmış tanımda satır üzerine tıklanarak ek ayarlarında değişiklik yapılabilir ya da ek satırı detaylarında beliren çöp kutusu ikonuna basılıp olay, nesne üzerinden kaldırılabilir.

![Pozisyon](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6dcba93f-f344-410a-9763-e8e02b9217d0)

- Type alanı ek dosyanın nerede bulunduğunun seçildiği alandır. DM, Flow, RelatedDocuments seçimleri yapılabilir.
    - Type:DM seçildiğinde panelde Value alanı içinde Doküman Yönetimi içinde seçim yapılır.
    - Type:Flow seçildiğinde ek olarak eklenecek dosyanın Id bilgisinin bulunduğu nesne liquid olarak seçilebilir veya statik veri yazılabilir. ({{ Document1.DocumentId }}, {{ Variable1.Value }}, 56669)
    - Type:RelatedDocuments seçildiğinde Document alanı gözükerek kullanılacak RelatedDocuments nesnesinin bulunduğu formu içeren Doküman nesnesi seçilir. Seçim yapılması ile panelde Related Documents alanı gözükerek seçilen nesne içindeki **Related Documents** nesneleri listelenerek seçim yapılır.

![Pozisyon](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3ae354da-4260-4679-9c28-4ff36cf96564)

`Edit Message Source` -  Pozisyon nesnesindeki kişiye gönderilecek mesajın, sistem varsayılanı olarak değil, özelleştirilmiş bir mesaj şablonu olarak gönderilmesi isteniyorsa bu özellik aktif edilir. Özellik aktif edildiğinde “Source Message” isimli alan görünür olacaktır.

`Source Message` -  Varsayılan mail şablonunun html formatta görüntülenerek, üzerinde değişiklik yapılmasına izin veren ekran, bu alandan açılır. Tasarlanan mail şablonu, önizleme penceresinde anlık olarak görüntülenebilir.

Elektronik postada belli bir dil düzenlenmek istenirse panel içindeki dil seçeneği değiştirilerek, seçilen dile ait e-posta kodları ve önizlemesi yapılabilir.

![Pozisyon](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload739c43d2-dcf2-469c-9b08-2cb0e38d0d5a)

:::info BİLGİ

Kullanıcıların sistemde hangi dilde e-posta alacakları, İnsan Kaynakları bölümünde her kullanıcıdaki **Varsayılan Dil** alanında yapılan seçime göre belirlenmektedir.

<div style={{textAlign: 'center'}}>

![Pozisyon](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada2d120d1-1d91-4b9d-b2e2-c9fbee67df23)

</div>

:::

### Push Notification

:::caution DİKKAT

Push Notification mobil uygulama üzerinden Bimser Synergy CSP uygulamasına giriş yapmış ve bildirimlere izin vermiş kişi/kişilerin cihazlarına gönderilir.

:::

`Send Push Notification` - Pozisyon nesnesindeki kişinin mobil cihazında bildirim gönderilmek istenirse alan aktif edilir.

`Caption` -  Pozisyon nesnesindeki kişiye gönderilecek mobil bildirimin başlık bilgisidir. Başlık bilgisinde varsayılan olarak gelen “ProcessCaption“, “FirstName” ve “LastName” parametreleri bulunur. Bu parametreler sistemin kendi parametreleridir ve bilgilendirmenin gönderildiği sürecin başlığı, mailin gönderildiği kişinin adı ve soyadı bilgileri otomatik olarak sistem tarafından doldurulur. Varsayılan olarak gelen mail başlığı yapısı aşağıdaki gibidir. Geliştirici isterse bu mail başlığını değiştirebilir.

> *Bimser Synergy {{ProcessCaption}} onayı ({{FirstName}} {{LastName}})*

`Message` -  Pozisyon nesnesindeki kişiye gönderilecek bilgilendirme mesaj metin kısmı bu alanda yer alır. Varsayılan olarak gelen mesaj metni, isteğe bağlı olarak değiştirilebilir.

### Documents

`Documents` - Bu alanda, pozisyon nesnesindeki kullanıcının hangi formu ve formun hangi görünümünü (view) görebileceği ayarlanır. Projeye dahil olan formlar akış tarafında Doküman nesnesi içerisinde tutulur. Doküman nesnesi, kendisine bağlanan formu ve form üzerindeki verileri temsil eder. Akış üzerinde birden çok, farklı formları temsil eden Doküman nesneleri bulunabilir. Pozisyon nesnesindeki kullanıcının hangi formu görmesi isteniyorsa, bu alandan, ilgili formun bağlı olduğu Doküman nesnesinin seçimi yapılıp gerekli ayarları belirlenir.

![Pozisyon](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2557b2e8-8fa0-482c-abdd-829049c8fda3)

Pozisyon nesnesinde tanımlı kullanıcıya web arayüzünde görmesi için birden fazla Doküman nesnesi de eklenebilir. Documents kısmına tıklandığında açılan ekranda kullanıcının görmesi istenen bir ya da birden çok Doküman nesnesi “Ekle” butonu ile eklenip, doküman üzerinde yapılabilecek düzenlemelerin ayarları belirlenir.

![Pozisyon](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2c9da3b1-979d-451c-9e74-38380b4e1b1a)

**Properties sekmesi özellikleri**

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Document 	| Akış tasarımı üzerindeki tüm Doküman nesnelerinin listelendiği alandır. Pozisyon nesnesindeki kişiye gösterilmek istenen formun bağlı olduğu Doküman nesnesi bu alandan seçilir. 	|
| View 	| “Doküman” alanından seçilen Doküman nesnesinin bağlı olduğu formun görünümleri (view) bu alanda listelenir. Pozisyondaki kullanıcı formu açtığında hangi form görünümünü görmesi isteniyorsa bu alandan seçimi yapılmalıdır. Görünüm alanından herhangi bir seçim yapılmazsa kullanıcı, “default” görünümü görecektir. 	|
| Panel Size 	| Web arayüzünde tanımlanan doküman nesnesinin hangi genişlikte açılabileceğinin belirlendiği alandır. 1-2-3 değerlerinden birisi seçilerek açılan panel boyutu seçilen değer genişliğinde açılacaktır. 	|
| Editable 	| Pozisyon nesnesindeki kullanıcının, doküman üzerinde düzenleme yapıp, yapamayacağı bu alandan belirlenir. Düzenle alanı işaretli olmayan bir doküman, kullanıcıya web arayüzünde salt okunur modunda açılır ve kişi formu düzenleyemez. Form üzerinde düzenleme yapılması isteniyorsa bu alan işaretlenmelidir. 	|
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

### Events

`Events` - Pozisyon nesnesindeki kullanıcının, web arayüzünde form için alabileceği aksiyon olaylarının tanımlandığı kısımdır. Bu alanda tanımlanan olaylar, web arayüzünde form üzerinde aksiyon butonları olarak görünür. Kullanıcı hangi olay butonuna tıklarsa süreç, dizayn anında o olaya ait bağlantı okunun bağlandığı akış adımına ilerler.

Nesneye Events alanından kaç tane olay eklenmişse, akış tasarım ekranında nesneden, her bir olayı temsil edecek bağlantı okları çıkarılmalı ve ilgili olaya tıklandığında akışın nereye gitmesi isteniyorsa bu oklar oraya bağlanmalıdır.

Events alanına tıklandığında, nesneye eklenecek olayların seçilebileceği ve bu olaylar için düzenlemelerin yapılabileceği bir pencere açılacaktır. Burada olay kayıtları olarak, **[Flow Properties->Events](index.mdx#events)** tabında tanımlanmış olaylar listelenir. Varsayılan olarak Pozisyon nesnesinde **"Onayla"** ve **"Reddet"** olayları ekli olarak gelir. Mevcut olaylar üzerinde değişiklik yapmak, yeni olay eklemek ya da mevcut olayı nesneden kaldırmak için Events alanına tıklanarak olay düzenleme penceresi açılır.

![Pozisyon](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf9f647dd-2206-47eb-a3ca-13aa1d26f1b3)

Events düzenleme penceresinde **“Ekle”** butonu ile Pozisyon nesnesine yeni bir olay eklenebilir, ekli olaylar için olay satırı üzerine tıklanarak olay ayarlarında değişiklik yapılabilir ya da ekli olay satırı detaylarında beliren çöp kutusu ikonuna basılıp olay, nesne üzerinden kaldırılabilir.

![Pozisyon](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload294f57f7-ccb8-426a-b0cb-ea75d36634b6)

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

:::caution DİKKAT

Nesne içeriğine eklenmiş bir olayın ayarları, **Flow Properties->Events** kısmından değiştirilmişse, nesne içeriğindeki ekli olay kaydı bu değişiklikten etkilenmemiş olabilir. Değişiklik sonrası ilgili olayı kullanan nesneler kontrol edilerek, Olaylar alanından değişikliğin yapıldığı olayın kaldırılıp tekrar eklenmesi gerekebilir.

:::

:::caution DİKKAT

Nesneye eklenmiş bir olay, **Flow Properties->Events** alanından silinirse, bu olayı kullanan nesneler kontrol edilerek, nesne içindeki ilgili ekli olay kaydının da silinmesi gerekir.

:::

### Options

`Hide the Approver` - Akış tarihçesinde, pozisyondaki kullanıcının adını * * * * şeklinde gizli göstermeye yarayan özelliktir.

`Show in the Flow History` - İlgili akış adımının akış tarihçesinde gösterilip gösterilmeyeceğinin ayarlandığı kısımdır.

### Flow Control

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

`If Document(s) is/are Changed Then Request is Needed` - Biraz önceki senaryomuzu biraz daha detaylandıralım ve müdür onayı ile IK müdürü onayı arasına bir başka pozisyon onayı olduğunu varsayalım. IK personeli belgeyi doldurduğunda öncelikli olarak müdürüne –yani burada müdür IK müdürü oluyor- daha sonra iş sürecinde yer alan diğer Pozisyon onayına gidecektir. Diğer pozisyon onayından sonra da “If Processed Before Do Not Send Request” seçeneğinden dolayı IK müdürüne tekrar uğramadan süreç tamamlanacaktır. Ancak şayet senaryomuzda yer alan Pozisyon nesnesi belgede herhangi bir değişiklik yaptıysa, yani belge IK müdürünün ilk onayından farklı bir hale geldiyse, IK müdürü ikinci kez bu belgeyi görmeden süreç tamamlanacaktır. Bu gibi durumları ortadan kaldırmak için ikinci bir seçenek olarak sisteme “If Document(s) is/are Changed Then Request is Needed” seçeneği eklenmiştir. Böylelikle bu seçeneği kullanarak yukarıda anlatılan senaryoda yer alan IK müdürüne ilgili belgenin tekrar gitmesi sağlanabilir.

### Forwarding Options

`Enabled` - Pozisyon nesnesindeki kullanıcıya gönderilen sürecin, kullanıcı tarafından akış tasarımında Members alanına eklenen kişilere sürecin yönlendirilmesi için kullanılmaktadır. Özellik aktif olduğunda yönlendirme işleminin yapılması için web ara yüzünde Event butonlarının yanında Forwarding olayı gözükür. 

Örneğin bir Satın Alma sürecinde kullanıcının onayına sürecin geldiğini ve Forwarding seçeneğinin aktif olduğunu varsayalım. Kullanıcı süreç içeriğini incelediğinde kendisi ile ilgili olmadığını, aynı departmanda X kişisinin bu işi yapması gerektiğini fark etsin. Süreci akışı başlatan kullanıcıya geri gönderip doğru kişinin seçilmesi veya sistem yöneticisi ile görüşerek bunun düzeltilmesi yerine; Forwarding eventi'ne tıklanarak süreç seçilen kullanıcıya işlem yapması için gönderilir.

:::caution DİKKAT

Forwarding işleminde onayın yönlendirildiği kişi tekrardan farklı bir kişiye süreci gönderemez. Farklı kişiye gönderilmesi istenirse, sürecin yönlendirme işlemini yapan kullanıcıya geri gönderilmesi ve kullanıcının yönlendirme işlemini tekrar yapması gereklidir.

:::

`Members` - Bu alandan Pozisyon nesnesinde yönlendirme işlemini yapacak kullanıcılar tanımlanır. Alana tıklandığında, Forwarding içine eklenecek kişileri seçmek için "İçerikler" butonu ve eklenmiş kayıtları kaldırmak için “Sil” butonunun bulunduğu bir ekran açılacaktır.

![Pozisyon](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload93c1c794-f921-4b6a-ade1-81b52f781b80)

"İçerikler" butonuna basıldığında, hangi tipte içerik ekleneceğinin belirtileceği seçim alanı açılacaktır. Alanda; **[Pozisyon](#members-position)**, **[Pozisyon grupları](#members-position-groups)** ve **[Doküman üzerindeki nesne](#members-documents)** olarak 3 seçenek listelenir.

![Pozisyon](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb1b98c65-c2a0-4997-a2da-5901a70110fe)

#### Pozisyon seçimi yapılırsa {#members-position}

Pozisyon seçeneği seçildiğinde yeni pop-up açılır ve bu alanda; Sabit Pozisyon, Kullanıcı, Değişken Pozisyon ve Akışı Başlatan seçenekleri listelenir.

- Sabit pozisyon seçeneği seçildiğinde, ekrana sistemde bulunan tüm pozisyon kayıtları listelenir. Bu listeden bir ya da birden çok pozisyon kaydı seçilerek "Oluştur" butonuna basıldığında, Members alanı içine seçilen pozisyon kayıtları eklenmiş olur. Geliştirici isterse tekrar "İçerikler" butonuna basarak alan içeriğini doldurmaya devam edebilir.

![Pozisyon](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload99228dbd-9f66-4531-aa76-2e53ff400e8e)

![Pozisyon](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload67c0ebff-8bd3-4173-8354-3ed7ec55728a)

- Kullanıcı seçeneği seçildiğinde, ekrana sistemde bulunan tüm kullanıcı kayıtları listelenir. Bu listeden bir ya da birden çok kullanıcı kaydı seçilerek "Oluştur" butonuna basıldığında, Members alanı içine seçilen kullanıcılar eklenmiş olur. Geliştirici isterse tekrar "İçerikler" butonuna basarak grup içeriğini doldurmaya devam edebilir.

![Pozisyon](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4eca46e6-9c2c-49bc-80a2-5c2e88979165)

![Pozisyon](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d7f8772-980c-4c7b-b9ba-89bac5cfc1c6)

- Değişken pozisyon seçeneği seçildiğinde, ekrana akış tasarımında bulunan tüm Pozisyon nesneleri ve Akışı Başlatan nesnesi listelenir. Members alanı içine akıştaki, hangi pozisyondaki kişi veya pozisyon eklenmek isteniyorsa o kişi veya pozisyonu temsil eden Pozisyon nesneleri seçimi bu alandan yapılır. "Oluştur" butonuna basıldıktan sonra geliştirici isterse tekrar "İçerikler" butonuna basarak grup içeriğini doldurmaya devam edebilir.

![Pozisyon](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9742f5e5-108c-44fa-a829-812e2aee8e89)

![Pozisyon](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada265dc55-b813-4ca0-92d4-8b94e9f27334)

- Akışı Başlatan seçeneği seçildiğinde, Members alanı içine akışı başlatan kullanıcı eklenmiş olur. Geliştirici isterse tekrar "İçerikler" butonuna basarak grup içeriğini doldurmaya devam edebilir.

![Pozisyon](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7752d6fe-bb8c-448a-b65d-48461274518b)

![Pozisyon](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d39c1c7-7691-431a-a458-211f22b54757)

#### Pozisyon grupları seçimi yapılırsa {#members-position-groups}

Members alanı içinde Pozisyon Grupları seçeneği seçildiğinde yeni pop-up açılır ve bu alanda; Belge onaylayanlar/reddedenler, Unvana göre kullanıcı grubu, Departmana göre kullanıcı grubu ve Kullanıcı grupları seçenekleri listelenir.

- Belge onaylayanlar/reddedenler seçeneği, ilgili akış tasarımında akış, Pozisyon nesnesine gelene kadar kimler aksiyonda bulunmuşsa o kişileri Members alanına eklemek için kullanılan seçenektir. Geliştirici isterse tekrar "İçerikler" butonuna basarak grup içeriğini doldurmaya devam edebilir.

![Pozisyon](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7959b70d-9f19-47e3-84f8-e2d5e8e904c1)

![Pozisyon](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4f286b65-d53b-4f93-83f3-ae14c01dd38a)

- Unvana göre kullanıcı grubu seçeneği, Members alanına belirli bir unvan tanımına sahip kullanıcıları eklemek için kullanılan seçenektir. "İçerikler" alanından bu seçenek seçildiğinde ekrana, sistemde tanımlı tüm unvan kayıtları listelenir.

![Pozisyon](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload09e5ebeb-f54a-4996-b38e-408da4d7d33f)

![Pozisyon](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd6f5de10-479b-497d-9cc9-4a9c29ed207a)

Aşağıdaki ekran görüntüsünde yapılan seçime göre “Project Manager” unvanlı kullanıcılar eklenecek demektir. Geliştirici isterse tekrar "İçerikler" butonuna basarak grup içeriğini doldurmaya devam edebilir.

![Pozisyon](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7297c082-a90f-4238-9000-55ce4a060504)

![Pozisyon](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload48140cc3-7664-4872-a295-972ef57444b1)

- Departmana göre kullanıcı grubu seçeneği, belirli bir departmanda bulunan kullanıcıları eklemek için kullanılan seçenektir. "İçerikler" alanından bu seçenek seçildiğinde ekrana, sistemde tanımlı tüm departman kayıtları listelenir.

![Pozisyon](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8b75477f-717c-4251-9f5c-1bff2334c9f1)

![Pozisyon](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada50e4840-d52f-423b-8bc2-06841fe21151)

Aşağıdaki ekran görüntüsünde yapılan seçime göre Members alanına, "Product Management" departmanındaki kullanıcılar eklenecek demektir. Geliştirici isterse tekrar "İçerikler" butonuna basarak grup içeriğini doldurmaya devam edebilir.

![Pozisyon](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7168ffb7-2301-4b31-abbf-b7fd7ec7f0e2)

![Pozisyon](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload59c8b49e-65ad-4790-87dd-a56fcc1e4729)

- Kullanıcı grupları seçeneği seçildiğinde ekrana, kullanıcı arayüzünde bulunan İnsan Kaynakları başlığı altında tanımlanmış **[Kullanıcı Grupları](web/human-resources/user-groups.md)** listelenir. Geliştirici bu listeden kullanıcı grubu seçimi yaptığında, Members alanına seçilen kullanıcı grubunun içine tanımlı kullanıcılar eklenmiş olur. İnsan Kaynakları bölümünden ilgili kullanıcı grubuna yeni kullanıcılar eklendiğinde ya da gruptan kişi çıkarıldığında, bu kullanıcı grubunun seçildiği Members alanında akış, kullanıcı grubunun son güncel haliyle içinde bulunan kişiler Forwording listesinde gözükür.

![Pozisyon](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2485ceda-833a-472d-9456-01294360839c)

![Pozisyon](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload87d87d3b-a5b9-42be-809f-3a972a3f2ac1)

![Pozisyon](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload33a0674a-3b6f-4b9e-8d31-725766ff049c)

![Pozisyon](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload53b8b2de-9b97-4afc-adf6-641eaf7748a2)

#### Dokuman üzerindeki nesne seçimi yapılırsa {#members-documents}

- Doküman üzerindeki nesne seçeneği seçildiğinde form üzerindeki bir [DataGrid](form/advanced-form-controls/DataGrid.md) nesnesinde seçilen kullanıcı veya pozisyonları, Members alanına eklemek için kullanılır. Alanda kişi ekleme işlemi pozisyon bazlı veya kullanıcı bazlı yapılabilmektedir.

Eğer form üzerindeki DataGrid nesnesinde seçilen kişiler, kullanıcı bazlı olarak alana eklenmek isteniyorsa, tablo nesnelerinin “Kullanıcı Adı(sicil no)” bilgisini barındıran bir ID kolonuna sahip olması gerekir.

Eğer form üzerindeki DataGrid nesnesinde seçilen kişiler, pozisyon bazlı olarak alana eklenmek isteniyorsa, tablo nesnelerinin “Pozisyon id” bilgisini barındıran bir ID kolonuna sahip olması gerekir.

İçerikler alanından “Doküman üzerindeki nesne” seçeneği seçildiğinde ekrana aşağıdaki alanlar gelecektir;

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Document 	| Bu alanda akış tasarımında bulunan tüm Doküman nesneleri listelenir. Hangi form üzerindeki DataGrid nesnesinin verilerine erişilmek isteniyorsa, o formun tanımlı olduğu Doküman nesnesi bu alandan seçilir. 	|
| Data type 	| “Kullanıcı” ve “Pozisyon” seçenekleri listelenir. Members alanına eklenecek kayıtlar kullanıcı bazlı eklenecekse bu alandan “Kullanıcı”, pozisyon bazlı eklenecekse bu alandan “Pozisyon” seçeneği seçilmelidir. 	|
| Table / Details 	| Documents alanında eklenen form üzerindeki hangi DataGrid nesneden seçilen kişiler Members alanına eklenecekse ilgili nesnenin seçimi yapılır. 	|
| Field 	| Bu alanda, DataGrid nesnesinin kolonları listelenir. Data type olarak “Kullanıcı” seçilmişse bu alanda, kullanıcı id lerinin bulunduğu kolonun seçimi yapılmalıdır. Data type olarak “Pozisyon” seçilmişse bu alanda, pozisyon id lerinin bulunduğu kolonun seçimi yapılmalıdır. 	|

`Use Referred User As Actual Value` - Akış tasarımında Atama vb nesnelerde kaynak olarak Forwarding özelliğinin aktif olduğu Pozisyon nesnesi seçildiğinde, sürecin yönlendirildiği kişi bilgisinin bundan sonra akış üzerinde kullanılmasını belirleyen özelliktir.

### Time Out

Bu kısım, pozisyon nesnesine zaman aşımı aksiyonu eklemek için kullanır. Akış, pozisyon nesnesine düştüğünde, belirli bir süre içerisinde, pozisyondaki kişi herhangi bir aksiyon almamışsa, isteğin zaman aşımına uğraması ve akışın herhangi bir yerinden, işlemin devam etmesi istenirse, bu bölümde bulunan kısımlar doldurulur. Zaman Aşımı bölümünde bulunan alanlar dolu ise ve Pozisyon nesnesinden, “Zaman Aşımı” bağlantısı çıkarılmışsa, belirlenen süre sonunda istek zaman aşımına uğrar ve akış, “Zaman Aşımı” kolunun bağlandığı yerden ilerler.

`Day` - Pozisyondan beklenen aksiyonun, belirli bir gün sonunda zaman aşımına uğraması isteniyorsa, bu alanda zaman aşımı gün bilgisi yazılır.

`Hour` - Pozisyondan beklenen aksiyonun, belirli bir saat sonunda zaman aşımına uğraması isteniyorsa, bu alanda zaman aşımı saat bilgisi yazılır.

`Minute` - Pozisyondan beklenen aksiyonun, belirli bir dakika sonunda zaman aşımına uğraması isteniyorsa, bu alanda zaman aşımı dakika bilgisi yazılır.

`Calculate Using Working Hours` - Zaman aşımı süresini, sistemde tanımlı çalışma saatleri hesaplanarak çalıştırmak için bu alan işaretlenir.

`Calculate Using Holidays` - Zaman aşımı süresini, sistemde tanımlı tatil günleri hesaplanarak çalıştırmak için bu alan işaretlenir.

:::info BİLGİ

Nesne üzerinde ekli özelliklerin doğru olduğu sistem tarafından kontrol edilmektedir. Eksik bir özellik bulunduğunda nesne üzerinde kırmızı ünlem ikonu gösterilerek, fare işaretçisi ile ikon üzerine gelindiğinde nelerin eksik veya hatalı olduğu görüntülenebilmektedir.

![Pozisyon](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade38e425e-13ea-47eb-85a3-7dc0941b7e63)

:::

## Events

Pozisyon nesnesinin sahip olduğu olaylar, Özellik Görüntüleyici panelindeki "Events" sekmesinde yer almaktadır. Her bir olay, farklı çalışma anlarında tetiklenerek kendilerine özgü işlemleri gerçekleştirir. Bu olaylara geliştirici tarafından yazılan kodlar da ilgili olayın tetiklendiği anda çalıştırılır. Herhangi bir olaya kod yazmak için, Olaylar sekmesinden ilgili olay satırına çift tıklanır. Ekran, “Akışadı.cs” isimli akış kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur. Geliştirici bu method içerisinde istediği kod bloğunu kurgulayabilir. Olaylar sekmesinden tıklanarak kod tarafında methodu oluşturulmuş olayın yanında, method adı bilgisi otomatik oluşturularak, olayla method arasındaki ilişki belirtilmiş olur.

![Pozisyon](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload274b68a1-291c-47f7-a6dc-915ce3b5a126)