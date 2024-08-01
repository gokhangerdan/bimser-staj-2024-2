---
sidebar_position: 2
custom_edit_url: ""
---

# DocumentMetadata

Formun oluşturulma tarihi veya form numarası (formid) bilgilerini, web arayüzünde form açıldığı anda otomatik göstermeye yarayan nesnedir.

![DocumentMetadata](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbc4ea181-00d0-4697-a2ba-261bd4b74b05)

Nesne geliştirme arayüzünde form tasarım ekranına yerleştirildikten sonra, nesne içinde gösterilmek istenen bilgi, Özellikler panelinden seçilir. Bu işlemden sonra menüdeki Çalıştır başlığı altından projenin başarıyla **derlenmesi** ve **yayınlanması** gerekmektedir. Proje başarıyla yayınlandığında, web arayüze kullanıcı adı ve şifre ile giriş yapılarak ilgili form menüden açılır ve formun seçilen bilgisinin nesnede yapılan ayara göre otomatik geldiği görülebilir.

Nesnenin üzerine tıklandığında Özellik Görüntüleyici panelinde “Genel” ve “Olaylar” sekmeleri yer alır ve nesneye ait özellikler görüntülenip, düzenlenebilir. Nesne özelliklerinin aktarıldığı kalıtım şeması aşağıdaki gibidir;

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

`Title` - Form arayüzde açıkken imleç ile nesne üzerine gelindiğinde, bu alanda yazılan metin, ipucu olarak gösterilir. Nesne ile ilgili detay bilgi verilmek istendiğinde kullanılan, uç kullanıcıyı yönlendirme amaçlı bir özelliktir.

`ClassName` - Forma ait CSS dosyası içinde yazılmış bir class'ın tanımlanarak nesne görünürlüğünün değiştirilebildiği alandır.

`Size Type` - Nesne seçim alanı boyutunun ayarlandığı kısımdır.

>Yapılabilecek Seçimler : Small, Middle, Large

### Behavior

`ReadOnly` - Nesnenin düzenleme modunda olup olmayacağının ayarlandığı kısımdır. Bu özellik aktif edildiğinde nesne veri girişine izin vermez, salt okunur modda olur. Nesneye veri girişine izin verilmesi için özelliğin pasif olması gerekir.

`Select Metadata Type` - Nesnede, gösterilmek istenen forma ait bilgi bu alandan seçilir.

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Id 	| Forma sistem tarafından verilen form id değerinin nesnede gösterilmesi isteniyorsa bu seçenek seçilir. Id formatı formun kendi Özellik Görüntüleyicisi üzerindeki Identity Format oluşturulabilir. 	|
| CreateDate 	| Formun oluşturulduğu tarih bilgisinin nesnede görünmesi isteniyorsa bu seçenek seçilir. 	|

:::info BİLGİ

Bir form üzerine ikiden fazla DocumentMetadata nesnesi eklenmesi sistem tarafından engellenmektedir. İkinci DocumentMetadata nesnesinde Select Metadata Type alanındaki seçim otomatik olarak ekli olmayan özellik olarak ayarlı gelir. 

:::

`Pull Number On Start` - Form akışı başlatanda görüntülendiği anda numara verilmesi istenirse aktif edilen özelliktir. Özellik kapalı olduğunda süreç başlatıldığında forma numara verme işlemi gerçekleşmemektedir.

:::caution DİKKAT

Pull New Number özelliği aktif iken Pull Number On Start özelliği de aktif edilirse, Pull New Number özelliği kapalı durumuna geçer.

:::

`Pull New Number` - Özellik aktif edildiğinde nesne üzerinde yeni numara alma butonu görünür olur. Buton ile forma numara verme işlemi kullanıcı tarafından yapılır.

:::danger UYARI

Pull New Number özelliği aktif edilmesi ile nesne üzerinde gözükecek butona tıklanarak sürekli yeni numara çekilmesi mümkündür. Bu sebeple kullanıcı birden fazla kez tıkladığı senaryoda, her tıklama için yeni kimlik numarası üretileceğinden, üretilen eski kimlik numaraları kullanılamaz hale gelir.

:::

`Date Format` - Select Metadata Type alanında CreateDate seçildiğinde görünen alandır. Nesnede tarih ve saat gösterim formatının belirlendiği alandır.

### Data Definition Language

`Field Name` - Sistemin veri tabanında, nesne için oluşturacağı kolonun adının belirlendiği alandır. "Name" kısmında nesneye başka bir isim verilip, veritabanı tablosunda nesne için oluşturulacak kolon adı farklı bir isim olarak yaratılabilir.

`Allow Null` - Nesne için oluşturulacak veritabanı alanının boş(null) değerlere izin verip vermeyeceği bu kısımdan belirtilir.

`Size` - Nesnenin veritabanı alanında tutacağı boyut bu alanda belirlenir.

## Olaylar

Nesnenin sahip olduğu olaylar, Özellik Görüntüleyici panelindeki "Olaylar" sekmesinde yer almaktadır. Her bir olay, farklı çalışma anlarında tetiklenerek kendilerine özgü işlemleri gerçekleştirir. Bu olaylara geliştirici tarafından yazılan kodlar da ilgili olayın tetiklendiği anda çalıştırılır.

"Client" alanında bulunan olaylara çift tıklandığında ekran, TypeScript kodlamanın yapılabileceği "Formadı.ts" isimli form kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur.

"Server" alanında bulunan olaylara çift tıklandığında ekran, C# kodlamanın yapılabileceği "Formadı.cs" isimli form kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur.

Geliştirici bu methodlar içerisinde istediği kod bloğunu kurgulayabilir. Olaylar sekmesinden tıklanarak kod tarafında methodu oluşturulmuş olayın yanında, method adı bilgisi otomatik oluşturularak, olayla method arasındaki ilişki belirtilmiş olur.

![DocumentMetadata](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload94fc695e-2796-4dae-9082-3c1eec725b78)

Oluşan methodlar;

![DocumentMetadata](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd66e001d-4e70-4387-aa13-394dc42a7bec)

![DocumentMetadata](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload251c9360-d378-49c4-ba88-47f136e3fcb7)