---
sidebar_position: 1
custom_edit_url: ""
---

# Akışı başlatan

Akışı başlatan nesnesi, web arayüzden ya da kod ile bir süreç başlatıldığında, süreci başlatan kişiyi temsil eden akış nesnesidir. 

:::danger UYARI

Akış başlatan nesnesi eski akış şablonunda kullanılan bir nesnedir. Yeni akış şablonu Akış Başlangıcı, Akış Bitişi ve Doküman nesnelerini kullanarak oluşmaktadır.

> *Yeni akış şablonu*
![Akışı başlatan](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc312ab85-f7ec-4104-9220-299c0f34b15a)
> *Eski akış şablonu*
![Akışı başlatan](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload651d5e6e-7592-4bd3-b793-56b0bcb24c13)

Yeni akış şablonunda Doküman süreç başlatılmadan oluşmayacağından veri tabanı üzerinden kayıt oluşmaz. Eski şablonda menüden tıklandığında Doküman Oluştur nesnesinden geçeceği için veri tabanında kayıt oluşur.

:::

Bu akış şablonunda Akış Başlangıcı ve Doküman Oluştur nesnelerinden sonra Akışı Başlatan nesnesi konumlandırılmıştır. Bu tasarımın amacı, web arayüzünden menüye ekli olan proje düğümüne tıklanarak başlatılan bir sürecin Akışı Başlatan kişisi olarak işlemi tetikleyen kişi olarak atanmasını sağlamaktır.

:::caution DİKKAT

Akışı başlatan nesnesi kullanıldığında, akışı başlatan kullanıcı süreci Taslaklara kaydetme işlemini yapamamaktadır.

:::

Akışı başlatan nesnesi sadece akışın başlangıcında bir kez kullanılmalıdır ve akışın ilerleyen adımlarında bu nesneye geri dönüş oku bağlanmamalıdır. Sonrasında sürecin tekrar akışı başlatana geri dönmesi gerekiyorsa ya da süreç adımlarında tekrar akışı başlatan kişiye onay gidecekse, ilgili adıma Akışı Başlatan nesnesi değil, Pozisyon nesnesi konulmalı ve pozisyon nesnesi içerisinde değer olarak “Akışı Başlatan” seçilmelidir.

Akış tasarım ekranında bulunan nesneye tıklandığında, Özellik Görüntüleyici panelinde, nesne özellikleri görünür.

Akışı başlatan nesnesine tıklandığında Özellik Görüntüleyici panelinde "Appearance", "Properties" ve "Events" sekmeleri bulunmaktadır.

## Appearance

### Text Configs

`Object Name` - Nesnenin sistem tarafında kullanılacak ismidir. Kod tarafında nesneye, nesne adı alanında yazan değerle erişim sağlanır.

`Caption` - Nesnenin başlık metninin girildiği alandır.

`Is Lock` - Tasarım anında nesnenin yeri değiştirilmesin isteniyorsa bu alan aktif edilir.

`Size` - Nesnenin genişlik ve yükseklik ayarlarının yapıldığı kısımdır.

## Properties

### Documents

`Documents` - Bu alanda, akışı başlatan kullanıcının hangi formu ve formun hangi görünümünü (view) görebileceği ayarlanır. Projeye dahil olan formlar akış tarafında Doküman nesnesi içerisinde tutulur. Doküman nesnesi, kendisine bağlanan formu ve form üzerindeki verileri temsil eder. Akış üzerinde birden çok, farklı formları temsil eden Doküman nesneleri bulunabilir. Akışı başlatan nesnesindeki kullanıcının hangi formu görmesi isteniyorsa, bu alandan, ilgili formun bağlı olduğu Doküman nesnesinin seçimi yapılıp gerekli ayarları belirlenir.

![Akışı başlatan](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5a8976b9-dec9-477c-becb-1469ac5186d8)

Akışı başlatan nesnesinde, süreci başlatan kullanıcının web arayüzünde görmesi için birden fazla Doküman nesnesi de eklenebilir. Documents kısmına tıklandığında açılan ekranda kullanıcının görmesi istenen bir ya da birden çok Doküman nesnesi “Ekle” butonu ile eklenip, doküman üzerinde yapılabilecek düzenlemelerin ayarları belirlenir.

![Akışı başlatan](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadba258d66-3fa6-4526-999e-efd21d16bd52)

**Properties sekmesi özellikleri**

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Document 	| Akış tasarımı üzerindeki tüm Doküman nesnelerinin listelendiği alandır. Pozisyon nesnesindeki kişiye gösterilmek istenen formun bağlı olduğu Doküman nesnesi bu alandan seçilir. 	|
| View 	| “Doküman” alanından seçilen Doküman nesnesinin bağlı olduğu formun görünümleri (view) bu alanda listelenir. Pozisyondaki kullanıcı formu açtığında hangi form görünümünü görmesi isteniyorsa bu alandan seçimi yapılmalıdır. Görünüm alanından herhangi bir seçim yapılmazsa kullanıcı, “default” görünümü görecektir. 	|
| Panel Size 	| Web arayüzünde tanımlanan doküman nesnesinin hangi genişlikte açılabileceğinin belirlendiği alandır. 1-2-3 değerlerinden birisi seçilerek açılan panel boyutu seçilen değer genişliğinde açılacaktır. 	|
| Editable 	| Akışı başlatan kullanıcının, doküman üzerinde düzenleme yapıp, yapamayacağı bu alandan belirlenir. Düzenle alanı işaretli olmayan bir doküman, kullanıcıya web arayüzünde salt okunur modunda açılır ve kişi formu düzenleyemez. Form üzerinde düzenleme yapılması isteniyorsa bu alan işaretlenmelidir. 	|
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

`Events` - Akışı başlatan kullanıcının, web arayüzünde form için alabileceği aksiyon olaylarının tanımlandığı kısımdır. Bu alanda tanımlanan olaylar, web arayüzünde form üzerinde aksiyon butonları olarak görünür. Kullanıcı hangi olay butonuna tıklarsa süreç, dizayn anında o olaya ait bağlantı okunun bağlandığı akış adımına ilerler.

Nesneye Events alanından kaç tane olay eklenmişse, akış tasarım ekranında nesneden, her bir olayı temsil edecek bağlantı okları çıkarılmalı ve ilgili olaya tıklandığında akışın nereye gitmesi isteniyorsa bu oklar oraya bağlanmalıdır.

Events alanına tıklandığında, nesneye eklenecek olayların seçilebileceği ve bu olaylar için düzenlemelerin yapılabileceği bir pencere açılacaktır. Burada olay kayıtları olarak, **[Flow Properties->Events](index.mdx#events)** tabında tanımlanmış olaylar listelenir. Varsayılan olarak Akışı başlatan nesnesine **"Gönder"** ve **"İptal"** olayı ekli olarak gelir. Mevcut olaylar üzerinde değişiklik yapmak, yeni olay eklemek ya da mevcut olayı nesneden kaldırmak için Events alanına tıklanarak olay düzenleme penceresi açılır.

![Akışı başlatan](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6c1d606c-22a7-4336-8734-c222a49cc780)

Events düzenleme penceresinde **“Ekle”** butonu ile Akışı başlatan nesnesine yeni bir olay eklenebilir, ekli olaylar için olay satırı üzerine tıklanarak olay ayarlarında değişiklik yapılabilir ya da ekli olay satırı detaylarında beliren çöp kutusu ikonuna basılıp olay, nesne üzerinden kaldırılabilir.

![Akışı başlatan](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf2c9f203-593b-4119-a800-f1294bcfcf39)

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

`Hide the Approver` - Akış tarihçesinde, akışı başlatan kullanıcının adını * * * * şeklinde gizli göstermeye yarayan özelliktir.

`Auto Open Approval Option` - Akış senaryosuna göre art arda olan akış adımları aynı kişiye geliyorsa, ilk aksiyon adımı için kişi formu açıp gerekli işlemleri yaparak aksiyon butonuna bastığında, ekranda “İş Akışı Tekrar Size Gelmiştir” bilgisi verilir. "Auto Open Approval Option" seçeneğinde "Otamatik aç" seçili ise, kullanıcı ilk aksiyonu aldığında ikinci aksiyon için form direk olarak kullanıcının önünde açılır. "Otomatik açma" seçili ise, ilk aksiyon adımından sonra ekran akış tarihçesi sayfasına yönlenir. Kişinin ikinci aksiyonu da almak için Onaylar sayfasına giderek ilgili süreci bulup formu tekrar açması gerekecektir.

`Show in the Flow History` - İlgili akış adımının akış tarihçesinde gösterilip gösterilmeyeceğinin ayarlandığı kısımdır.

### Message

`Send Mail` -  Akış adımı ilgili Akışı başlatan nesnesine düştüğünde, sistem otomatik olarak nesnedeki kişiye, onayına bir süreç düşürüldüğünün bilgisini mail olarak gönderir. İlgili nesnede aksiyon düştüğünde mail gönderilmesi istenmiyorsa, Send Mail alanının işareti kaldırılabilir. Bu durum genelde test amaçlı akış senaryosu denemelerinde kişilere mail gitmemesi için kullanılır.

:::tip İPUCU

Nesneler içinde gezerek e-posta gönderimini kapatmaya ek olarak akış genelinde de e-posta gönderimini engellemek mümkündür. **[Flow Properties->General](index.mdx#general)** içindeki **Disable Email Sending** özellği aktif edilerek e-posta gönderimi akış genelinde kapatılabilir.

:::

`Caption` -  Akışı başlatana gönderilecek onay mailinin başlık bilgisidir. Başlık bilgisinde varsayılan olarak gelen “ProcessCaption“, “FirstName” ve “LastName” parametreleri bulunur. Bu parametreler sistemin kendi parametreleridir ve mailin gönderildiği sürecin başlığı, mailin gönderildiği kişinin adı ve soyadı bilgileri otomatik olarak sistem tarafından doldurulur. Varsayılan olarak gelen mail başlığı yapısı aşağıdaki gibidir. Geliştirici isterse bu mail başlığını değiştirebilir.

> *Bimser Synergy {{ProcessCaption}} onayı ({{FirstName}} {{LastName}})*

`Message` -  Akışı başlatana gönderilecek mailin mesaj metin kısmı bu alanda yer alır. Varsayılan olarak gelen mesaj metni, isteğe bağlı olarak değiştirilebilir.

`Attachments` - Akışı başlatana gönderilecek mail içinde ek dosya gönderilmek istenirse bu alandan tanımlanır. 

![Akışı başlatan](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb2b44017-9c53-4a1f-8c26-6ce625ec2bfd)

Atttachments alanına tıklandığında, gönderilecek e-postaya eklenmek istenen ek türünün seçileceği tanımlanacağı ekran açılır.

![Akışı başlatan](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb81205f6-3d05-40e7-8229-ec97f1dabed4)

Attachments düzenleme penceresinde **“Ekle”** butonu ile Akışı başlatan nesnesinde kişiye gönderilecek e-postaya ek eklenmesi için tanım yapılabilir, yapılmış tanımda satır üzerine tıklanarak ek ayarlarında değişiklik yapılabilir ya da ek satırı detaylarında beliren çöp kutusu ikonuna basılıp olay, nesne üzerinden kaldırılabilir.

![Akışı başlatan](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcfb0c9fc-a1de-467c-9d07-64034c92a660)

- Type alanı ek dosyanın nerede bulunduğunun seçildiği alandır. DM, Flow, RelatedDocuments seçimleri yapılabilir.
    - Type:DM seçildiğinde panelde Value alanı içinde Doküman Yönetimi içinde seçim yapılır.
    - Type:Flow seçildiğinde ek olarak eklenecek dosyanın Id bilgisinin bulunduğu nesne liquid olarak seçilebilir veya statik veri yazılabilir. ({{ Document1.DocumentId }}, {{ Variable1.Value }}, 56669)
    - Type:RelatedDocuments seçildiğinde Document alanı gözükerek kullanılacak RelatedDocuments nesnesinin bulunduğu formu içeren Doküman nesnesi seçilir. Seçim yapılması ile panelde Related Documents alanı gözükerek seçilen nesne içindeki **Related Documents** nesneleri listelenerek seçim yapılır.

![Akışı başlatan](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9635a3e6-7e1a-4300-8498-ac76eb679115)

`Edit Message Source` -  Akışı başlatan kişiye gönderilecek mesajın, sistem varsayılanı olarak değil, özelleştirilmiş bir mesaj şablonu olarak gönderilmesi isteniyorsa bu özellik aktif edilir. Özellik aktif edildiğinde “Source Message” isimli alan görünür olacaktır.

`Source Message` -  Varsayılan mail şablonunun html formatta görüntülenerek, üzerinde değişiklik yapılmasına izin veren ekran, bu alandan açılır. Tasarlanan mail şablonu, önizleme penceresinde anlık olarak görüntülenebilir.

Elektronik postada belli bir dil düzenlenmek istenirse panel içindeki dil seçeneği değiştirilerek, seçilen dile ait e-posta kodları ve önizlemesi yapılabilir.

![Akışı başlatan](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2d5bbc80-376a-4e38-b0d8-3def338c2b85)

:::info BİLGİ

Kullanıcıların sistemde hangi dilde e-posta alacakları, İnsan Kaynakları bölümünde her kullanıcıdaki **Varsayılan Dil** alanında yapılan seçime göre belirlenmektedir.

<div style={{textAlign: 'center'}}>

![Akışı başlatan](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb5091715-a713-49cc-8691-d2aaf9ad67d1)

</div>

:::

### Push Notification

:::caution DİKKAT

Push Notification mobil uygulama üzerinden Bimser Synergy CSP uygulamasına giriş yapmış ve bildirimlere izin vermiş kişi/kişilerin cihazlarına gönderilir.

:::

`Send Push Notification` - Akışı başlatan kişinin mobil cihazında bildirim gönderilmek istenirse alan aktif edilir.

`Caption` -  Akışı başlatana gönderilecek mobil bildirimin başlık bilgisidir. Başlık bilgisinde varsayılan olarak gelen “ProcessCaption“, “FirstName” ve “LastName” parametreleri bulunur. Bu parametreler sistemin kendi parametreleridir ve bilgilendirmenin gönderildiği sürecin başlığı, mailin gönderildiği kişinin adı ve soyadı bilgileri otomatik olarak sistem tarafından doldurulur. Varsayılan olarak gelen mail başlığı yapısı aşağıdaki gibidir. Geliştirici isterse bu mail başlığını değiştirebilir.

> *Bimser Synergy {{ProcessCaption}} onayı ({{FirstName}} {{LastName}})*

`Message` -  Akışı başlatana gönderilecek bilgilendirme mesaj metin kısmı bu alanda yer alır. Varsayılan olarak gelen mesaj metni, isteğe bağlı olarak değiştirilebilir.

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

### Time Out

Bu kısım, nesneye zaman aşımı aksiyonu eklemek için kullanır. Akış, nesneye düştüğünde, belirli bir süre içerisinde, pozisyondaki kişi herhangi bir aksiyon almamışsa, isteğin zaman aşımına uğraması ve akışın herhangi bir yerinden, işlemin devam etmesi istenirse, bu bölümde bulunan kısımlar doldurulur. Time Out bölümünde bulunan alanlar dolu ise ve nesneden, “Time Out” bağlantısı çıkarılmışsa, belirlenen süre sonunda istek zaman aşımına uğrar ve akış, “Time Out” kolunun bağlandığı yerden ilerler.

`Day` -  Nesneden beklenen aksiyonun, belirli bir gün sonunda zaman aşımına uğraması isteniyorsa, bu alanda zaman aşımı gün bilgisi yazılır.

`Hour` -  Nesneden beklenen aksiyonun, belirli bir saat sonunda zaman aşımına uğraması isteniyorsa, bu alanda zaman aşımı saat bilgisi yazılır.

`Minute` - Nesneden beklenen aksiyonun, belirli bir dakika sonunda zaman aşımına uğraması isteniyorsa, bu alanda zaman aşımı dakika bilgisi yazılır.

`Calculate Using Working Hours` - Zaman aşımı süresini, sistemde tanımlı çalışma saatleri hesaplanarak çalıştırmak için bu alan işaretlenir.

`Calculate Using Holidays` - Zaman aşımı süresini, sistemde tanımlı tatil günleri hesaplanarak çalıştırmak için bu alan işaretlenir.

## Events

Akışı başlatan nesnesinin sahip olduğu olaylar, Özellik Görüntüleyici panelindeki "Events" sekmesinde yer almaktadır. Her bir olay, farklı çalışma anlarında tetiklenerek kendilerine özgü işlemleri gerçekleştirir. Bu olaylara geliştirici tarafından yazılan kodlar da ilgili olayın tetiklendiği anda çalıştırılır. Herhangi bir olaya kod yazmak için, Events sekmesinden ilgili olay satırına çift tıklanır. Ekran, “Akışadı.cs” isimli akış kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur. Geliştirici bu method içerisinde istediği kod bloğunu kurgulayabilir. Events sekmesinden tıklanarak kod tarafında methodu oluşturulmuş olayın yanında, method adı bilgisi otomatik oluşturularak, olayla method arasındaki ilişki belirtilmiş olur.

![Akışı başlatan](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf2c55eee-53e1-4c2d-b1a5-ce6f5de7f590)