---
sidebar_position: 5
custom_edit_url: ""
---

# RelatedDocuments

RelatedDocuments nesnesi; form üzerine, yerel dizinde veya Doküman Yönetim Sistemi’nde bulunan dosyaların yüklenmesini sağlayan nesnedir.

Nesneye dosya yükleme işlemi, **sürükle/bırak yöntemi** ile veya yüklenecek dosyanın seçimi yapılarak gerçekleştirilebilir. Birden çok dosyanın seçimi yapılara, **toplu dosya yükleme** işlemi gerçekleştirilebilir.

Nesneye yüklenmesi için seçilen dosyaların **yüklenme durumu**, ekranın sağ üst köşesinde izlenebilir, dosya yüklemesi arka planda devam ederken kullanıcı, form üzerindeki diğer alanları doldurma işlemine devam edebilir.

Nesneye yüklenen dosya detaylarından **“Dosyayı Görüntüle”** seçeneğine tıklanarak, yan panelde dosya önizleme ekranının açılması sağlanır. Böylece yüklenen dosya web arayüzünde görüntülenebilmiş olur.

![RelatedDocuments](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade8fec0a8-1364-43f9-b57d-b89a03ef4f6d)

Nesnenin üzerine tıklandığında Özellik Görüntüleyici panelinde “Genel” ve “Olaylar” sekmeleri yer alır ve nesneye ait özellikler görüntülenip, düzenlenebilir. Nesne özelliklerinin aktarıldığı kalıtım şeması aşağıdaki gibidir;

## Genel

### Design

`Name` - Nesnenin sistem tarafında kullanılacak ismidir. Başka bir nesnenin içinde ve kod tarafında nesneye, isim alanında yazan değerle erişim sağlanır.

### Caption

`Title` - Nesnenin etiket metninin düzenlendiği kısımdır.

`Position` - Nesne etiketinin, nesnenin solunda mı, sağında mı yoksa üzerinde mi konumlandırılacağının düzenlendiği kısımdır.

>Yapılabilecek Seçimler : Left, Right, Top, Bottom

`Width` - Etiket alanının genişliğinin ayarlandığı kısımdır.

`Height` - Etiket alanının yüksekliğinin ayarlandığı kısımdır.

`Font` - Etiket alanındaki metnin font, yazı tipi, yazı boyutu ve renginin ayarlandığı kısımdır.

`Ellipsis` - Etiket metninin, etiket alanına sığmadığı durumlarda, metnin sığmayan kısmı için üç nokta (…) ifadesinin görünüp görünmeyeceğinin ayarlandığı kısımdır.

`Visible` - Etiket alanının gizli ya da görünür ayarlarının yapıldığı kısımdır.

`Show Colon` - Etiket metninin yanında iki nokta (:) ifadesinin görünüp görünmeyeceğinin ayarlandığı kısımdır.

`Horizontal Align` - Etiket metnini; sağa yasla, sola yasla ya da ortala ayarlarının gerçekleştirildiği kısımdır.

>Yapılabilecek Seçimler : Left, Center, Right

`Vertical Align` - Etiket metnini; yukarı yasla, aşağı yasla ya da ortala ayarlarının gerçekleştirildiği kısımdır.

>Yapılabilecek Seçimler : Top, Middle, Bottom

`Mark Char` - Nesneyi belirginleştirmek için, etiket metnine *, ! gibi karakterlerin girilebileceği alandır.

`Mark Position` - İşaret karakteri olarak belirlenen karakterin, etiket metninin başında mı yoksa sonunda mı gösterilmesinin ayarlandığı kısımdır.

>Yapılabilecek Seçimler : AtFirst, AtLast

### Appearance

`Visible` - Nesnenin gizlenip, görünür yapılma ayarlarının gerçekleştirildiği kısımdır. Bu alan aktifken, nesne form üzerinde görünür durumdadır. Alan pasif yapıldığında nesne görünmez olur.

`Client Visible` - Form ilk açıldığında nesne görünmesin, belirli bir şart sağlandığında nesne görünür olsun gibi bir işlem yapılmak istendiğinde, nesnenin istemci tarafında görünmez olması için bu alan pasif yapılır. Kodla ya da Kural Yöneticisi ile belirlenen şart sağlandığında nesne tekrar görünür hale getirilebilir. Sunucu görünürlüğü aktif değilken, istemci müdahale edemez ancak istemci görünürlüğü aktif değilken sunucu müdahale edebilir.

`Enabled` - Nesnenin etkin modu bu alandan ayarlanır. Bu özellik aktifken nesneye veri girişi sağlanabilir ve nesne düzenlenebilir. Özellik pasifken, nesne düzenlenemez moddadır ve pasif görünür.

`Client Enabled` - Form ilk açıldığında nesne etkin olmasın, belirli bir şart sağlandığında etkin olsun gibi bir işlem yapılmak istendiğinde, nesnenin istemci tarafında etkin olmaması için bu alan pasif yapılır. Kodla ya da Kural Yöneticisi ile belirlenen şart sağlandığında nesne tekrar etkin hale getirilebilir. Sunucu etkinliği aktif değilken, istemci müdahale edemez ancak istemci etkinliği aktif değilken sunucu müdahale edebilir.

`Background Color` - Nesneye arka plan rengi vermek için kullanılan alandır.

`Title` - Form arayüzde açıkken imleç ile nesne üzerine gelindiğinde, bu alanda yazılan metin, ipucu olarak gösterilir. Nesne ile ilgili detay bilgi verilmek istendiğinde kullanılan, uç kullanıcıyı yönlendirme amaçlı bir özelliktir.

`ClassName` - Forma ait CSS dosyası içinde yazılmış bir class'ın tanımlanarak nesne görünürlüğünün değiştirilebildiği alandır.

### Behavior

`ReadOnly` - Nesnenin düzenleme modunda olup olmayacağının ayarlandığı kısımdır. Bu özellik aktif edildiğinde nesne veri girişine izin vermez, salt okunur modda olur. Nesneye veri girişine izin verilmesi için özelliğin pasif olması gerekir.

### File Settings

`Add New File Enable` - Nesne üzerine yeni dosya ekleme işleminin yapılıp yapılamayacağının belirlendiği özelliktir. Aktif edildiğinde Adding Mode alanında izin verilen yükleme türlerine ait buton/butonlar gösterilerek nesneye yeni dosya eklenebilmektedir. Özellik pasif yapıldığında dosya ekleme butonları da pasif olur ve nesneye dosya eklenemez.

![RelatedDocuments](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb78144f2-edf3-4c5d-9659-91007b0ec097)

`Delete File Enable` - Nesneye yüklenen dosyanın nesne üzerinden kaldırılabilmesinin yapılıp yapılamayacağının belirlendiği özelliktir. Aktif edildiğinde ek dosyanın yanındaki **üç noktaya (...)** tıklanarak açılan pop-up'ta **Kaldır** butonu ile silme işlemi gerçekleşir.

:::caution DİKKAT

Delete File Enable özelliği dosyayı Doküman Yönetimi üzerinde yüklendiği dizinden silmez, nesne içindeki bağlantı kaldırılır.

:::

![RelatedDocuments](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb706c6e7-8006-4616-9728-b008b4dc3788)

`View File` - Nesneye yüklenen dosyanın nesne üzerinde görüntüleme işleminin yapılıp yapılamayacağının belirlendiği özelliktir. Aktfi edildiğinde nesnedeki üç noktaya tıklanarak açılan pop-up'ta Görüntüle butonu tıklanır durumda olur.

![RelatedDocuments](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload35e0fed4-b478-4bb5-a2c6-1fdef308bb02)

`Show Category Description` - Bu özellik aktif edildiğinde, Categories alanında ekli kategoriye girilen açıklama nesnede görünür olur.

![RelatedDocuments](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadda5dcdcf-07f1-4fa9-b2d6-4e7cdbd4c364)

`Show File Description` - Nesneye eklenen dosyanın açıklama metni, nesnede gösterilmek istenirse bu özellik aktif edilir. Eklenen dosyaya açıklama girmek için dosyanın (…) “Daha Fazla” ikonuna tıklandığında çıkan “Açıklama Gir” butonuna tıklanarak dosyaya açıklama metni eklenebilir ve nesnede bu açıklamanın görünmesi sağlanabilir.

`File Description Required` - Show File Description özelliğinin aktif edilmesi ile görünür olur. Yüklenen dosyada açıklamanın zorunlu olup olmayacağını belirlemek için kullanılır. Bu özellik aktifken, uç kullanıcı eklenen dosyaya açıklama girmeden formu ilerletemez.

:::caution DİKKAT

Zorunluluk kontrolünün yapılması için akışta ilgili nesnedeki Eventslerde olaydaki Validate seçeneğinin veya formun Toolbar Button alanına eklenecek butondaki Validate özelliğinin aktif olması gereklidir.

:::

`Show Content For Image Files` - Nesneye resim türünde dosya eklendiğinde, dosyanın uzantı ikonunun yerine küçük resim olarak gösterilmesi istenirse özellik aktif edilmelidir.

Nesneye bir resim dosyası eklenmişse ve bu özellik açıksa, eklenen resim dosyasının küçük bir önizlemesi nesne üzerinde gösterilir. Böylece, kullanıcı resmi görmek için “Dosyayı Görüntüle” butonuna tıklamak zorunda kalmamış olur.

:::note BİLGİ

Bu özelliğin kullanılması için Show File Extension özelliğinin aktif olması gereklidir.

:::

`Show Create Date` - Dosyanın eklenme tarihini nesnede göstermeye yarayan özelliktir.

![RelatedDocuments](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload40273400-995c-41b1-a82a-f0b5a4e2dd95)

`Show Path of File` - Yüklenen dosyanın sistem üzerindeki yol bilgisini nesnede göstermeye yarayan özelliktir.

![RelatedDocuments](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8a30ac63-fe35-48ac-b48d-459f59373b6c)

`Show Creator` - Dosya yükleyen kullanıcının, kullanıcı adı bilgisinin nesnede gösterilmesini sağlayan özelliktir.

![RelatedDocuments](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload06ebbd69-91d2-438d-9687-8cc155d3b8c9)

`Show File Extension` - Nesnede dosya yükendiğinde, dosya türüne ait ikonun gösterilmesini sağlayan özelliktir.

`Adding Mode` - Nesneye nereden dosya seçilebilerek yükleneceğinin belirlendiği alandır. Listelenen ögeler Bilgisayardan Seçilebilir, Doküman Yönetimi'nden Seçilebilir ve Hepsi olmak üzere üç farklı seçimden bir tanesi tercih edilebilmektedir.
  - `Bilgisayardan Seçilebilir` - Adding Mode üzerinde bu seçenek seçilirse Bilgisayardan Seçilebilir ikonu gözükür. Nesneye sadece uç kullanıcı cihazındaki dosyalar kullanılarak yükleme işlemi yapılacaktır.
  ![RelatedDocuments](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbfee1e3f-53c5-4d13-8afb-e168d4661bae)
  - `Doküman Yönetimi'nden Seçilebilir` - Adding Mode üzerinde bu seçenek seçilirse Doküman Yönetimi'nden Seçilebilir ikonu gözükür. Nesneye sadece sistemde Doküman Yönetimi üzerinden seçim gerçekleştirilerek nesneye dosya yükleme işlemi yapılacaktır. Doküman Yönetimi üzerinde dosya seçimi işleminde görüntülenecek depo/klasörler uç kullanıcıların yetkilerine bağlı değişebilir.
  ![RelatedDocuments](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1a5d332c-e94d-434b-a55e-696d3014c44b)
  - `Hepsi` - Adding Mode üzerinde bu seçenek seçilirse Bilgisayardan Seçilebilir ve Doküman Yönetimi'nden Seçilebilir ikonları gözükür. Nesneye uç kullanıcı cihazından veya Doküman Yönetimi üzerinden seçilerek dosya yükleme işlemi yapılacaktır.
  ![RelatedDocuments](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload48c88b09-90fb-48a0-b48f-60bab5668406)

`View Type` - Nesnenin görünümünü değiştirmek için kullanılan alandır. Listelenen ögeler Kart Görünümü, Liste Görünümü, Küçültülmüş Görünüm olmak üzere üç farklı seçimden bir tanesi tercih edilebilmektedir.
  - `Kart Görünümü` - View Type alanında varsayılan seçim olarak gelmektedir, nesnede yüklenen dosyalar kartlar şeklinde gösterilecektir.
  ![RelatedDocuments](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0e6ea89f-3751-4ff4-8a1d-bc7919736cd3)
  - `Liste Görünümü` - View Type alanında üzerinde bu seçenek seçilirse nesnede yüklenen dosyalar liste şeklinde gösterilecektir.
  ![RelatedDocuments](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadef298e81-ef20-48b6-bfa8-957a8cd7f437)
  - `Küçültülmüş Görünüm` - View Type alanında üzerinde bu seçenek seçilirse nesne daha kompakt oalcak şekilde gösterilecektir.


`Save Path (DM)` - Nesneye eklenen dosyalar, doküman yönetiminde belirlenen bir dizinde saklanır. Bu alandan, nesneye eklenecek dosyaların hangi dizinde tutulacağının seçimi yapılır.

Save Path alanına tıklandığında, doküman yönetim yapısı pencere olarak açılacaktır. Buradan dosyaların tutulması istenen dizin seçilerek “Tamam” butonuna tıklanır. Böylece kullanıcı, arayüzünde nesneye eklenen dosyaların DM de saklandığı dizini belirlenmiş olur.

![RelatedDocuments](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload163c5718-9f07-434c-b744-4082564adaed)

Alanda yapılacak seçim varsayılan dosya yükleme dizini olup, Categories alanında yeni kategori eklenip özelleşirilme yapılmadıysa, kategorilere eklenen dosyalar Save Path (DM) alanında seçilen dizine yüklenecektir.

:::tip İPUCU

İstenirse Save Path (DM) alanında seçim yapmadan Categories alanında tanımlı **kategorilerdeki Save Path (DM) alanını** kullanarak dosyanın yükleneceği dizini seçebilirsiniz.

:::

:::info BİLGİ

Doküman Yönetimi'nden seçilen dosyalar Save Path (DM) alanında seçtiğiniz dizine taşınmaz, seçilen dosyalar bulundukları dizinde kalmaya devam eder.

:::

`Categories` - Kullanıcıların, tasarlanmış olan forma hangi kategoride dosya ekleyebileceğinin belirlendiği alandır. 

Nesneye eklenen dosyalar, belirli bir kategoriye dahil olmalıdır. Varsayılan olarak nesneye **“Varsayılan”** isimli kategori ekli olarak gelir. Geliştirici tarafından nesne kategori tanımlarına müdahale edilmezse, arayüzde nesneye eklenen dosyalar bu Varsayılan kategorisine eklenmiş olur. 

Mevcut kategori tanımında değişiklik yapmak için veya nesneye yeni kategoriler eklemek ve düzenleme yapmak için Categories alanına tıklanır.

![RelatedDocuments](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload379a2e77-c57d-4ea2-a263-8a6375a555ff)

Kategoriler alanına tıklandığında ekrana, kategori düzenleme penceresi açılacaktır. Bu ekrandan mevcut kategori alanları düzenlenebilir, var olan bir kategori tanımı silinebilir veya nesneye yeni bir kategori tanımı eklenebilir. 

![RelatedDocuments](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6d64698d-8c0c-44e2-a1e8-646590871e0b)

Sıfırla butonunu kullanarak kategori üzerinde yaptığınız özelleştirilmeler paneli açtığınızdaki haline getirilir, örneğin yeni bir kategori ekleyip mevcut kategorinin bazı alanlarını özelleştirilerek işlem yapıldı ama bu işlemden vazgeçerek panelin açıldığı haline geri dönmek istenildiğinde kullanılabilmektedir. **Sıfırlama işlemi panel içeriği kaydedilmediyse çalışır,** kaydedilen kategori özelliklerinde sıfırlama işlemi uygulanamaz. 

Ekle butonu kullanarak nesne içine yeni kategori eklenirken, Kaydet butonu kullanarak panel içinde yapılan değişiklikler kaydedilmektedir.

Kategori tanımlarının "General" sekmesinde kategori adı (Category Name), kategori açıklaması (Description), kategoriye yüklenen dosyaların Doküman Yönetimi'nde saklanacağı dizin (Save Path (DM)), ve aktiflik durumu (Active) bilgileri yer alır. 

:::info BİLGİ

Kategorideki Save Path (DM) alanı, nesnedeki Save Path (DM) seçimi yapıldıysa nesne üzerinden dizin bilgisini almaktadır. İstenirse kategori üzerindeki Save Path (DM) alanı özelleştirilerek nesnede seçilenden farklı bir dizine yüklenmesi yapılabilir.

:::

“Properties” sekmesinde ise;
  - `Min File Count` - İlgili kategoriye eklenecek minimum dosya sayısının belirlenebileceği alandır.
  - `Max File Count` - İlgili kategoriye eklenecek maksimum dosya sayısının belirlenebileceği alandır.
  - `Max File Size` - İlgili kategoriye eklenecek dosyaların maksimum boyut sınırı değerinin girilebileceği alandır. Alanda dosya boyutu için değer girişi yapılıp, değerin KB (KiloByte), MB (MegaByte) veya GB (GigaByte) olarak mı limitleneceğinin seçimi yapılmalıdır.
  - `Supported Extensions` - İlgili kategoriye hangi dosya uzantılarının eklenmesine izin verileceğinin belirlenebildiği alandır.

![RelatedDocuments](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4b6a4eb8-63d1-4062-b701-2fa9539d6e45)

### Data Definition Language

`Field Name` - Sistemin veri tabanında, nesne için oluşturacağı kolonun adının belirlendiği alandır. “Name” kısmında nesneye başka bir isim verilip, veritabanı tablosunda nesne için oluşturulacak kolon adı farklı bir isim olarak yaratılabilir.

## Olaylar

Nesnenin sahip olduğu olaylar, Özellik Görüntüleyici panelindeki “Olaylar” sekmesinde yer almaktadır. Her bir olay, farklı çalışma anlarında tetiklenerek kendilerine özgü işlemleri gerçekleştirir. Bu olaylara geliştirici tarafından yazılan kodlar da ilgili olayın tetiklendiği anda çalıştırılır.

“Client” alanında bulunan olaylara çift tıklandığında ekran, TypeScript kodlamanın yapılabileceği “Formadı.ts” isimli form kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur.

“Server” alanında bulunan olaylara çift tıklandığında ekran, C# kodlamanın yapılabileceği “Formadı.cs” isimli form kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur.

Geliştirici bu methodlar içerisinde istediği kod bloğunu kurgulayabilir. Olaylar sekmesinden tıklanarak kod tarafında methodu oluşturulmuş olayın yanında, method adı bilgisi otomatik oluşturularak, olayla method arasındaki ilişki belirtilmiş olur.

![RelatedDocuments](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1d87b4f6-3e08-479c-85a4-c14065104f92)

Oluşan methodlar;

![RelatedDocuments](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload74e41590-531a-4492-8a20-bc98bc0447c0)

![RelatedDocuments](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9ddb6fba-02df-4768-b5a1-68d73670da2b)