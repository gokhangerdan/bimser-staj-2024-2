---
sidebar_position: 1
custom_edit_url: ""
---

# UserMetadata

Web arayüzünde formu oluşturan kullanıcının, sistemde kayıtlı kullanıcı bilgilerini otomatik olarak form üzerinde göstermeye yarayan nesnedir.

Nesne içerisinde kullanıcıya ait tüm İnsan Kaynakları tanımları listelenir, seçilen IK tanımına göre web arayüzünde formu oluşturan kişinin ilgili tanım değeri nesnede otomatik olarak görüntülenmiş olur.

![UserMetadata](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload80d2cc7d-34e1-4297-9905-76632569b39b)

Nesne geliştirme arayüzünde form tasarım ekranına yerleştirildikten sonra, nesne içinde gösterilmek istenen kullanıcı bilgisi Özellikler panelinden seçilir. Bu işlemden sonra menüdeki Çalıştır başlığı altından projenin başarıyla **derlenmesi** ve **yayınlanması** gerekmektedir. Proje başarıyla yayınlandığında, web arayüze kullanıcı adı ve şifre ile giriş yapılarak ilgili form menüden açılır ve kullanıcının seçilen bilgisinin nesneye otomatik geldiği görülür.

![UserMetadata](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9dafd350-cde8-46ab-ba48-69c4a5d6bc69)

Nesnenin üzerine tıklandığında Özellik Görüntüleyici panelinde "Genel" ve "Olaylar" sekmeleri yer alır ve nesneye ait özellikler görüntülenip, düzenlenebilir. Nesne özelliklerinin aktarıldığı kalıtım şeması aşağıdaki gibidir;

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

`Title` - Form arayüzde açıkken imleç ile nesne üzerine gelindiğinde, bu alanda yazılan metin, ipucu olarak gösterilir. Nesne ile ilgili detay bilgi verilmek istendiğinde kullanılan, uç kullanıcıyı yönlendirme amaçlı bir özelliktir.

`ClassName` - Forma ait CSS dosyası içinde yazılmış bir class'ın tanımlanarak nesne görünürlüğünün değiştirilebildiği alandır.

`Size Type` - Nesne seçim alanı boyutunun ayarlandığı kısımdır.

>Yapılabilecek Seçimler : Small, Middle, Large

### Behavior

`ReadOnly` - Nesnenin düzenleme modunda olup olmayacağının ayarlandığı kısımdır. Bu özellik aktif edildiğinde nesne veri girişine izin vermez, salt okunur modda olur. Nesneye veri girişine izin verilmesi için özelliğin pasif olması gerekir.

`Select Metadata Type` - Nesnede görünmesi istenen kullanıcı verisi bu alandan seçilir. Bu nesnede sistemde tanımlı kullanıcıların kullanıcı bilgileri listelenir. Akışı başlatan kullanıcının nesnede gösterilmek istenen değeri bu alandan seçilmelidir.

Özellikte listelenen değerler;

| **Özellik Tipi** 	| **Açıklama** 	|
|---	|---	|
| NameAndSurname 	| Akışı başlatan kullanıcının isim ve soyisim bilgilerinin nesnede gösterilmesi için seçilen değerdir. 	|
| UserId 	| Akışı başlatan kullanıcının kullanıcı numarası (UserId) bilgisinin nesnede gösterilmesi için seçilen değerdir. 	|
| UserName 	| Akışı başlatan kullanıcının kullanıcı adı (UserName) bilgisinin nesnede gösterilmesi için seçilen değerdir. 	|
| Position 	| Akışı başlatan kullanıcının pozisyon bilgisinin nesnede gösterilmesi için seçilen değerdir. 	|
| PositionId 	| Akışı başlatan kullanıcının pozisyon bilgisinin kodunun (PositionId) nesnede gösterilmesi için seçilen değerdir. 	|
| Department 	| Akışı başlatan kullanıcının departman bilgisinin nesnede gösterilmesi için seçilen değerdir. 	|
| DepartmentId 	| Akışı başlatan kullanıcının departman bilgisi kodunun (DepartmentId) nesnede gösterilmesi için seçilen değerdir. 	|
| Profession 	| Akışı başlatan kullanıcının unvan bilgisinin nesnede gösterilmesi için seçilen değerdir. 	|
| ProfessionId 	| Akışı başlatan kullanıcının unvan bilgisi kodunun (ProfessionId) nesnede gösterilmesi için seçilen değerdir. 	|
| EmailAddress 	| Akışı başlatan kullanıcının mail adres bilgisinin nesnede gösterilmesi için seçilen değerdir. 	|
| Custom 	| Web arayüzde İnsan Kaynakları menüsü altındaki Özellik Tanımları alanında Kullanıcı Özellikleri için tanımlanmış özellik kayıtlarından birinin bu nesnede görünmesi isteniyorsa Select Metadata Type alanında Custom seçeneği seçilip, Custom Metadata Field Name alanında istenilen özellik seçilebilmektedir. 	|

### Data Definition Language

`Field Name` - Sistemin veri tabanında, nesne için oluşturacağı kolonun adının belirlendiği alandır. "Name" kısmında nesneye başka bir isim verilip, veritabanı tablosunda nesne için oluşturulacak kolon adı farklı bir isim olarak yaratılabilir.

`Allow Null` - Nesne için oluşturulacak veritabanı alanının boş(null) değerlere izin verip vermeyeceği bu kısımdan belirtilir.

`Size` - Nesnenin veritabanı alanında tutacağı boyut bu alanda belirlenir.

## Olaylar

Nesnenin sahip olduğu olaylar, Özellik Görüntüleyici panelindeki "Olaylar" sekmesinde yer almaktadır. Her bir olay, farklı çalışma anlarında tetiklenerek kendilerine özgü işlemleri gerçekleştirir. Bu olaylara geliştirici tarafından yazılan kodlar da ilgili olayın tetiklendiği anda çalıştırılır.

"Client" alanında bulunan olaylara çift tıklandığında ekran, TypeScript kodlamanın yapılabileceği "Formadı.ts" isimli form kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur.

"Server" alanında bulunan olaylara çift tıklandığında ekran, C# kodlamanın yapılabileceği "Formadı.cs" isimli form kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur.

Geliştirici bu methodlar içerisinde istediği kod bloğunu kurgulayabilir. Olaylar sekmesinden tıklanarak kod tarafında methodu oluşturulmuş olayın yanında, method adı bilgisi otomatik oluşturularak, olayla method arasındaki ilişki belirtilmiş olur.

![UserMetadata](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload221692c5-8d1e-4ca5-a5db-d9888c1704c5)

Oluşan methodlar;

![UserMetadata](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb7bfe6c4-ee2e-416f-a0f1-79869d8c1cc3)

![UserMetadata](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload57a4919a-d4d3-47a3-8363-b0ef14fde635)