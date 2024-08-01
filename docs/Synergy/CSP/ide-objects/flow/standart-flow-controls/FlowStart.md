---
sidebar_position: 1
custom_edit_url: ""
---

# Akış Başlangıcı

Akış başlangıcı nesnesi, tasarlanan sürecin akışının başlangıç noktasını belirten nesnedir. Her akış tasarımının en başında bu nesne bulunmalıdır. Akış tasarımında kullanılacak diğer nesneler, bu akış başlangıcı nesnesinden sonra sıralanır ve birbirlerine bağlantı nesnesi ile ilişki kurarlar. Bir akış ekranında yalnızca 1 adet akış başlangıcı nesnesi kullanımına izin verilir.

Geliştirme arayüzünde aktif ekran akış iken, Araç Kutusu panelinde akış nesneleri listelenir. Araç kutusu panelinden Akış başlangıcı nesnesi süreklenip akış ekranı üzerine bırakıldığında akışa nesne eklenmiş olur. Akış başlangıcı nesnesine tıklandığında Özellik Görüntüleyici panelinde nesnenin sahip olduğu özellikler listelenecektir.

![Akış Başlangıcı](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6dbeb2bd-5a48-4da5-8438-987181209a43)

Akış Başlangıcı nesnesine tıklandığında Özellik Görüntüleyici panelinde "Appearance", "Properties" ve "Events" sekmeleri bulunmaktadır.

## Appearance

### Text Configs

`Object Name` - Nesnenin sistem tarafında kullanılacak ismidir. Kod tarafında nesneye, nesne adı alanında yazan değerle erişim sağlanır.

`Caption` - Nesnenin başlık metninin girildiği alandır.

`Is Lock` - Tasarım anında nesnenin yeri değiştirilmesin isteniyorsa bu alan aktif edilir.

`Size` - Nesnenin genişlik ve yükseklik ayarlarının yapıldığı kısımdır.

## Properties

### Documents

`Documents` - Bu alanda, akışı başlatan kullanıcının hangi formu ve formun hangi görünümünü (view) görebileceği ayarlanır. Projeye dahil olan formlar akış tarafında Doküman nesnesi içerisinde tutulur. Doküman nesnesi, kendisine bağlanan formu ve form üzerindeki verileri temsil eder. Akış üzerinde birden çok, farklı formları temsil eden Doküman nesneleri bulunabilir. Akış Başlangıcı nesnesindeki kullanıcının hangi formu görmesi isteniyorsa, bu alandan, ilgili formun bağlı olduğu Doküman nesnesinin seçimi yapılıp gerekli ayarları belirlenir.

![Akış Başlangıcı](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload27027fa2-1f41-4e2a-8846-dcf87b7bd2c0)

Akış Başlangıcı nesnesinde, süreci başlatan kullanıcının web arayüzünde görmesi için birden fazla Doküman nesnesi de eklenebilir. Documents kısmına tıklandığında açılan ekranda kullanıcının görmesi istenen bir ya da birden çok Doküman nesnesi “Ekle” butonu ile eklenip, doküman üzerinde yapılabilecek düzenlemelerin ayarları belirlenir.

![Akış Başlangıcı](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0bb11617-051e-4e2b-9941-88ad7d366c38)

**Properties sekmesi özellikleri**

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Document 	| Akış tasarımı üzerindeki tüm Doküman nesnelerinin listelendiği alandır. Akış Başlangıcı nesnesindeki kişiye gösterilmek istenen formun bağlı olduğu Doküman nesnesi bu alandan seçilir. 	|
| View 	| “Doküman” alanından seçilen Doküman nesnesinin bağlı olduğu formun görünümleri (view) bu alanda listelenir. Nesnedeki kullanıcı formu açtığında hangi form görünümünü görmesi isteniyorsa bu alandan seçimi yapılmalıdır. Görünüm alanından herhangi bir seçim yapılmazsa kullanıcı, “default” görünümü görecektir. 	|
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

Events alanına tıklandığında, nesneye eklenecek olayların seçilebileceği ve bu olaylar için düzenlemelerin yapılabileceği bir pencere açılacaktır. Burada olay kayıtları olarak, **[Flow Properties->Events](index.mdx#events)** tabında tanımlanmış olaylar listelenir. Varsayılan olarak Akış Başlangıcı nesnesine **"Gönder"** olayı ekli olarak gelir. Mevcut olaylar üzerinde değişiklik yapmak, yeni olay eklemek ya da mevcut olayı nesneden kaldırmak için Events alanına tıklanarak olay düzenleme penceresi açılır.

![Akış Başlangıcı](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload779edb32-8af1-4035-8c8c-853c1db4a3bd)

Events düzenleme penceresinde **“Ekle”** butonu ile Akış Başlangıcı nesnesine yeni bir olay eklenebilir, ekli olaylar için olay satırı üzerine tıklanarak olay ayarlarında değişiklik yapılabilir ya da ekli olay satırı detaylarında beliren çöp kutusu ikonuna basılıp olay, nesne üzerinden kaldırılabilir.

![Akış Başlangıcı](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4beb1ca0-d35c-4fd1-9b87-5c4097b1e2a3)

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

`Start Immediately` - Özellik aktif edildiğinde, yeni bir akış başlatılırken kullanıcı etkileşimine ihtiyaç duymadan akışın başlatılabilmesi işlemini gerçekleştirir. Özellik aktif edildiğinde nesne üzerinden çıkan event bağlantıları kaldırılır ve nesneden sadece Continue event bağlantısı çıkarılabilmektedir.

:::caution DİKKAT

Start Immediately özelliği aktif ve nesnede Documents alanında seçim yapılmadıysa, formun oluşması için akışta Doküman Oluştur nesnesi kullanılmalıdır.

:::

`Can Save As Draft` - Web ara yüzünde menüde akışı başlatan kullanıcının formu taslak olarak kaydedebilmesi istenirse aktif edilen özelliktir. Özellikle web ara yüzünde formda "Taslak Olarak Kaydet" butonu gösterilir, akışı başlatan kullanıcı butona tıklayarak formu kaydedebilir.

Kullanıcı taslak olarak kaydettiği formlarına İş Akış Yönetimi içerisinde Taslaklar bölümünden erişebilmektedir.

:::info BİLGİ

Süreçlerin taslak olarak kaydedilmesi proje bazında aktif edilmektedir. Özellik aktif edilmediyse akışı başlatan kullanıcı süreci ilerletmeden formu kapattığında form taslak olarak kaydedilmemektedir.

:::

:::caution DİKKAT

Web ara yüzünde süreç başlatıldığında form taslak olarak kaydedilmeden veya süreç başlatılmadan form verisi veri tabanına kaydedilmez.

:::

:::info BİLGİ

Nesne üzerinde ekli özelliklerin doğru olduğu sistem tarafından kontrol edilmektedir. Eksik bir özellik bulunduğunda nesne üzerinde kırmızı ünlem ikonu gösterilerek, fare işaretçisi ile ikon üzerine gelindiğinde nelerin eksik veya hatalı olduğu görüntülenebilmektedir.

![Akış Başlangıcı](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb37c03b3-2808-4523-b1f9-343484929597)

:::

## Events

Akış Başlangıcı nesnesinin sahip olduğu olaylar, Özellik Görüntüleyici panelindeki "Events" sekmesinde yer almaktadır. Her bir olay, farklı çalışma anlarında tetiklenerek kendilerine özgü işlemleri gerçekleştirir. Bu olaylara geliştirici tarafından yazılan kodlar da ilgili olayın tetiklendiği anda çalıştırılır. Herhangi bir olaya kod yazmak için, Events sekmesinden ilgili olay satırına çift tıklanır. Ekran, “Akışadı.cs” isimli akış kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur. Geliştirici bu method içerisinde istediği kod bloğunu kurgulayabilir. Events sekmesinden tıklanarak kod tarafında methodu oluşturulmuş olayın yanında, method adı bilgisi otomatik oluşturularak, olayla method arasındaki ilişki belirtilmiş olur.

![Akış Başlangıcı](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf9292dfd-2ebf-4b9b-aa33-7928fc6dbe47)