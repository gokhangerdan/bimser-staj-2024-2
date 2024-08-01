---
sidebar_position: 16
custom_edit_url: ""
---

# DateTimePicker

Tarih veya tarih ve saat girişleri yapılmak istendiğinde kullanılacak nesnedir.

Geliştirme arayüzünde aktif ekran form iken, Araç Kutusu panelinde form nesneleri listelenir. Nesne, araç kutusu panelinden sürükle/bırak yöntemi ile forma eklenir.

![DateTimePicker](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf21e6be4-c8f3-4609-b835-6fd7c259a1b4)

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

`Value` - Form web ara yüzünde açıldığında varsayılan bir tarih ile gelmesi istendiğinde, seçim yapılacak alandır.

`Placeholder` - Nesne içine uç kullanıcı tarafından girilmesi istenen veri bilgisini, nesne içerisinde bilgi amaçlı göstermek için kullanılan özelliktir. Uç kullanıcı nesneyi görüntülediğinde bu alana yazılan yönlendirici metni görür, nesneye odaklandığında ve değer girmeye başladığında yönlendirici metin kaybolur.

![DateTimePicker](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload86b5d0bd-a9ea-46db-a1f7-0d02a29b4560)

![DateTimePicker](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3ec11310-2ecc-434b-a38f-881304097dfc)

`TextAlign` - Nesne içine girilen ifadenin hizalanacağı yerin belirlenmesi için kullanılan alandır. Sola hizala, merkeze hizala, sağa hizala seçimleri yapılabilir.

>Yapılabilecek Seçimler : Left, Center, Right

`Size Type` - Nesne boyutunun belirlenebileceği alandır.

>Yapılabilecek Seçimler : Small, Middle, Large

### Behavior

`ReadOnly` - Nesnenin düzenleme modunda olup olmayacağının ayarlandığı kısımdır. Bu özellik aktif edildiğinde nesne veri girişine izin vermez, salt okunur modda olur. Nesneye veri girişine izin verilmesi için özelliğin pasif olması gerekir.

`Tab Index` - Bu alana sayısal değerler girilerek, tab butonuna basıldığında form nesneleri arasında hangi sıra ile odaklanılacağı belirlenir. Form doldurulurken imleci, veri girilmek istenen nesneye tıklamak yerine, tab butonuna basarak belirli bir sırayla indekslenmiş nesnelere direk odaklanılması sağlanmış olur. Bu da form doldurma hızını artıran bir özelliktir.

`Required` - Nesnede veri girişinin zorunlu olup olmayacağının belirlendiği alandır. Bu özellik aktif edildiğinde nesne içerisine veri girişi yapılmadan formun ilerletilmesi/kaydedilmesi gerçekleştirilemez.

`Format` - Tarih ve saat gösterim formatının belirlendiği alandır. Varsayılan olarak tarih formatı: “YYYY-MM-DD”, tarih ve saat formatı: “YYYY-MM-DD HH:mm” şeklinde tanımlıdır. Gösterilmek istenen farklı format yapıları bu alanda belirtilebilir.

`Show Time` - Nesnede saat bilgisinin gösterilip gösterilmeyeceğinin belirlendiği alandır. Bu alan aktif değilken nesnede sadece tarih bilgisi gösterilir, alan aktif edildiğinde hem tarih hem saat bilgisi nesnede görünür olur. Bu özellik aktifken, arayüzde nesneye tıklandığında tarih seçim alanının yanında saat seçim alanı da görünür olur.

![DateTimePicker](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8c455c30-b2d1-40a3-861b-0d548729cf2f)

`Show Today` - Nesne içerisinde tarih seçimi yaparken, seçim ekranının altında “Bugün” isimli butonun çıkmasını sağlayan özelliktir. Bu butona tıklandığında günün tarihi nesneye seçilmiş olarak yansır. Özellik kapatıldığında seçim ekranında “Bugün” butonu görünmeyecektir.

![DateTimePicker](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2bf49f90-9c04-42f7-8be3-4fc7270827de)

`Set Today As Default` - Bu özellik aktif edildiğinde nesnede varsayılan olarak bugünün tarihi görünür olur. Uç kullanıcı arayüzde formu ilk açtığında, nesne içerisinde günün tarihini görür, isterse başka bir tarih seçimi ile bu değeri değiştirebilir.

`Allow Clear` - Özellik aktif edildiğinde, web ara yüzünde nesnede yapılan tarih seçiminin istenirse kaldırılabilmesi sağlanır.

`Disable before` - Aktif edildiğinde günümüzden itibaren geçmişte bir nokta öncesindeki tarih seçimlerinin engellenmesi için ayarlar (gün, ay ve yıl değerleri tanımı) devreye girecektir.
  `Disable before years` - Girilen değere göre, günümüzden itibaren **x** yıl öncesine kadar tarih seçimi aktif olacaktır. **x yıl + 1 gün** öncesine gidildiğinde seçim yapılamayacaktır.
  `Disable before months` - Girilen değere göre, günümüzden itibaren **x** ay öncesine kadar tarih seçimi aktif olacaktır. **x ay + 1 gün** öncesine gidildiğinde seçim yapılamayacaktır.
  `Disable before days` - Girilen değere göre, günümüzden itibaren **x** gün öncesine kadar tarih seçimi aktif olacaktır. **x gün + 1 gün** öncesine gidildiğinde seçim yapılamayacaktır.

`Disable after` - Aktif edildiğinde günümüzden itibaren gelecekte bir nokta sonrasındaki tarih seçimlerinin engellenmesi için ayarlar (gün, ay ve yıl değerleri tanımı) devreye girecektir.
  `Disable after years` - Girilen değere göre, günümüzden itibaren **x** yıl geleceğe kadar tarih seçimi aktif olacaktır. **x yıl + 1 gün** ilerisine gidildiğinde seçim yapılamayacaktır.
  `Disable after months` - Girilen değere göre, günümüzden itibaren **x** ay geleceğe kadar tarih seçimi aktif olacaktır. **x ay + 1 gün** ilerisine gidildiğinde seçim yapılamayacaktır.
  `Disable after days` - Girilen değere göre, günümüzden itibaren **x** gün geleceğe kadar tarih seçimi aktif olacaktır. **x gün + 1 gün** ilerisine gidildiğinde seçim yapılamayacaktır.

### Data Definition Language

`Field Name` - Sistemin veri tabanında, nesne için oluşturacağı kolonun adının belirlendiği alandır. “Name” kısmında nesneye başka bir isim verilip, veritabanı tablosunda nesne için oluşturulacak kolon adı farklı bir isim olarak yaratılabilir.

`Allow Null` - Nesne için oluşturulacak veritabanı alanının boş(null) değerlere izin verip vermeyeceği bu kısımdan belirtilir.

## Olaylar

Nesnenin sahip olduğu olaylar, Özellik Görüntüleyici panelindeki “Olaylar” sekmesinde yer almaktadır. Her bir olay, farklı çalışma anlarında tetiklenerek kendilerine özgü işlemleri gerçekleştirir. Bu olaylara geliştirici tarafından yazılan kodlar da ilgili olayın tetiklendiği anda çalıştırılır.

“Client” alanında bulunan olaylara çift tıklandığında ekran, TypeScript kodlamanın yapılabileceği “Formadı.ts” isimli form kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur.

“Server” alanında bulunan olaylara çift tıklandığında ekran, C# kodlamanın yapılabileceği “Formadı.cs” isimli form kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur.

Geliştirici bu methodlar içerisinde istediği kod bloğunu kurgulayabilir. Olaylar sekmesinden tıklanarak kod tarafında methodu oluşturulmuş olayın yanında, method adı bilgisi otomatik oluşturularak, olayla method arasındaki ilişki belirtilmiş olur.

![DateTimePicker](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9af74421-eb2c-492f-aec1-0552c1bdf96a)

Oluşan methodlar;

![DateTimePicker](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfc777c2b-a9bd-4c1a-9e55-0d262a57adfd)

![DateTimePicker](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbafb8239-5f50-4485-ba35-50bd7578e12f)