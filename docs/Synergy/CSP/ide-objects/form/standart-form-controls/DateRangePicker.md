---
sidebar_position: 17
custom_edit_url: ""
---

# DateRangePicker

Tarih veya zaman aralığı belirtmek için kullanılan nesnedir. Başlangıç ve bitiş tarihi mantığında aralık değeri belirtmek için kullanılır.

Geliştirme arayüzünde aktif ekran form iken, Araç Kutusu panelinde form nesneleri listelenir. Nesne, araç kutusu panelinden sürükle/bırak yöntemi ile forma eklenir.

![DateRangePicker](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload530a3cc2-8e9c-4553-962c-81f080ff9727)

Nesnenin üzerine tıklandığında Özellik Görüntüleyici panelinde “Genel” ve “Olaylar” sekmeleri yer alır ve nesneye ait özellikler görüntülenip, düzenlenebilir. Nesne özelliklerinin aktarıldığı kalıtım şeması aşağıdaki gibidir;

## Genel

### Design

`Name` - Nesnenin sistem tarafında kullanılacak ismidir. Başka bir nesnenin içinde ve kod tarafında nesneye, isim alanında yazan değerle erişim sağlanır.

### Start Date

`Allow empty` - Başlangıç tarihi alanının boş bırakılıp bırakılamayacağı bu alandan belirlenir. Bu özellik aktif edildiğinde başlangıç tarihi alanı boş bırakılabilir. Özellik pasifken başlangıç tarihi olarak bir değer seçilmesi zorunlu tutulur.

`Set today as default` - Özellik aktif edildiğinde, başlangıç tarihi alanında bugünün tarihi varsayılan seçili olarak görülür.

`Disabled hours` - Nesne özelliklerindeki **Show Time** özelliği aktifken, bu alanda belirtilen saatler nesnede pasif olarak görünür ve seçilemez.

Belirli bir saat aralığının seçilmesi istenmiyorsa, ilgili saat aralığı, saat değerleri arasına “–” işareti konularak yazılır. Örneğin; saat 12 ile 16 arası saatlerin seçilmesi istenmiyorsa, bu alana “12-16” değeri yazılır. Nesnede saat seçim alanında bu saat aralıkları pasif görünür.

![DateRangePicker](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadeb05f043-dd9b-4a43-a7d1-708f46aa8dd7)

![DateRangePicker](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9253adaf-a9e8-4ac8-8560-a0bc51e3b1e9)

Birden çok saat değerinin seçilememesi isteniyorsa, bu saat değerleri arasına “,” konularak bu alana yazılır. Örneğin; 01,03 ve 05 saatlerinin seçilememesi istenirse, bu alana “01,03,05” ifadesi yazılmalıdır.

![DateRangePicker](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadee6f0f63-8b4b-4fea-835a-478e5ac65ee0)

![DateRangePicker](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1250b23a-5b93-4a1d-8b7e-2c02bb3d5859)

`Disabled minutes` - Nesne özelliklerindeki **Show Time** özelliği aktifken, bu alanda belirtilen dakikalar, nesnede pasif olarak görünür ve seçilemez.

Belirli bir dakika aralığının seçilmesi istenmiyorsa, ilgili dakika aralığı, dakika değerleri arasına “–” işareti konularak yazılır. Örneğin; 20 ile 25 dakika arası pasif olsun istenirse, bu alana “20-25” değeri yazılır. Nesnede dakika seçim alanında bu dakika aralıkları pasif görünür.

![DateRangePicker](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd2cf1caf-16cc-4692-abb8-b27234932fee)

![DateRangePicker](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0e38297e-9847-46e6-aca3-0e198f46a680)

Birden çok dakika değerinin seçilememesi isteniyorsa, bu dakika değerleri arasına “,” konularak bu alana yazılır. Örneğin; 40 ve 45 dakikalarının seçilememesi istenirse, bu alana “40,45” ifadesi yazılmalıdır.

![DateRangePicker](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6d421863-dd54-402e-96c3-367a8139fe2d)

![DateRangePicker](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade286897f-e592-4deb-a74c-c3c54d17a6d9)

`Disabled seconds` - Nesne özelliklerindeki **Show Time** özelliği aktif edildiğinde, Format alanında varsayılan format “YYYY-MM-DD HH:mm” şeklinde gelir. Saniye değerinin de nesnede seçilebilmesi istenirse bu format, **YYYY-MM-DD HH:mm:ss** şeklinde düzenlenmelidir. Bu düzenlemeden sonra nesnede saniye değeri de görüntülenebilir olur. 

![DateRangePicker](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc9b666a3-68cb-4f25-bc0b-82aa219064c3)

Engelli Saniyeler alanında belirtilen saniyeler, nesnede pasif olarak görünür ve seçilemez.

Belirli bir saniye aralığının seçilmesi istenmiyorsa, ilgili saniye aralığı, saniye değerleri arasına “–” işareti konularak yazılır. Örneğin; 03 ile 07 saniye arası pasif olsun istenirse, bu alana “03-07” değeri yazılır. Nesnede saniye seçim alanında bu saniye aralıkları pasif görünür.

![DateRangePicker](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload39526b24-0a24-4db3-8802-f662d29efa3c)

![DateRangePicker](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1aa3604a-c207-4b89-9762-91753a47772e)

Birden çok saniye değerinin seçilememesi isteniyorsa, bu saniye değerleri arasına “,” konularak bu alana yazılır. Örneğin; 53, 55 ve 56 saniyelerinin seçilememesi istenirse, bu alana “53,55,56” ifadesi yazılmalıdır.

![DateRangePicker](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2a658c08-c9ab-4c64-8644-83ee137f958e)

![DateRangePicker](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd6762bc5-b1fb-4ec5-90b6-0ad055031c85)

`Value` - Başlangıç tarihi alanının değeri burada ifade edilir. Bu alanda seçilen tarih, başlangıç tarihi alanının varsayılan değeri olarak nesnede belirir.

`Placeholder` - Nesne içine uç kullanıcı tarafından girilmesi istenen veri bilgisini, nesne içerisinde bilgi amaçlı göstermek için kullanılan özelliktir. Uç kullanıcı nesneyi görüntülediğinde bu alana yazılan yönlendirici metni görür, nesneye odaklandığında ve değer girmeye başladığında yönlendirici metin kaybolur.

### End Date

`Allow empty` - Bitiş tarihi alanının boş bırakılıp bırakılamayacağı bu alandan belirlenir. Bu özellik aktif edildiğinde bitiş tarihi alanı boş bırakılabilir. Özellik pasifken bitiş tarihi olarak bir değer seçilmesi zorunlu tutulur.

`Set today as default` - Özellik aktif edildiğinde, bitiş tarihi alanında bugünün tarihi varsayılan seçili olarak görülür.

`Disabled hours` - Nesne özelliklerindeki **Show Time** özelliği aktifken, bu alanda belirtilen saatler nesnede pasif olarak görünür ve seçilemez.

Belirli bir saat aralığının seçilmesi istenmiyorsa, ilgili saat aralığı, saat değerleri arasına “–” işareti konularak yazılır. Örneğin; saat 12 ile 16 arası saatlerin seçilmesi istenmiyorsa, bu alana “12-16” değeri yazılır. Nesnede saat seçim alanında bu saat aralıkları pasif görünür.

![DateRangePicker](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadac58ef78-3387-4898-a39b-9c4a6022ae83)

![DateRangePicker](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada41c512a-7857-4c8a-98c9-5974dd481fc6)

Birden çok saat değerinin seçilememesi isteniyorsa, bu saat değerleri arasına “,” konularak bu alana yazılır. Örneğin; 01,03 ve 05 saatlerinin seçilememesi istenirse, bu alana “01,03,05” ifadesi yazılmalıdır.

![DateRangePicker](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload91e84f81-f99c-4d55-ada5-9bbc2713907d)

![DateRangePicker](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload06615b5a-a124-44f5-9056-97c234d539ad)

`Disabled minutes` - Nesne özelliklerindeki **Show Time** özelliği aktifken, bu alanda belirtilen dakikalar, nesnede pasif olarak görünür ve seçilemez.

Belirli bir dakika aralığının seçilmesi istenmiyorsa, ilgili dakika aralığı, dakika değerleri arasına “–” işareti konularak yazılır. Örneğin; 20 ile 25 dakika arası pasif olsun istenirse, bu alana “20-25” değeri yazılır. Nesnede dakika seçim alanında bu dakika aralıkları pasif görünür.

![DateRangePicker](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5f8d24d7-e27c-465e-972f-f21688efeb39)

![DateRangePicker](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddec8211c-b472-40e1-a3ab-89ff87d10b8d)

Birden çok dakika değerinin seçilememesi isteniyorsa, bu dakika değerleri arasına “,” konularak bu alana yazılır. Örneğin; 40 ve 45 dakikalarının seçilememesi istenirse, bu alana “40,45” ifadesi yazılmalıdır.

![DateRangePicker](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload26daa4c1-6aa5-4816-a17d-e82cc382ab55)

![DateRangePicker](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3e4dcc81-1d9e-4968-a534-71882e1dec85)

`Disabled seconds` - Nesne özelliklerindeki **Show Time** özelliği aktif edildiğinde, Format alanında varsayılan format “YYYY-MM-DD HH:mm” şeklinde gelir. Saniye değerinin de nesnede seçilebilmesi istenirse bu format, **YYYY-MM-DD HH:mm:ss** şeklinde düzenlenmelidir. Bu düzenlemeden sonra nesnede saniye değeri de görüntülenebilir olur. 

![DateRangePicker](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6da64c51-48f5-4f4e-a951-2868e0896feb)

Engelli Saniyeler alanında belirtilen saniyeler, nesnede pasif olarak görünür ve seçilemez.

Belirli bir saniye aralığının seçilmesi istenmiyorsa, ilgili saniye aralığı, saniye değerleri arasına “–” işareti konularak yazılır. Örneğin; 03 ile 07 saniye arası pasif olsun istenirse, bu alana “03-07” değeri yazılır. Nesnede saniye seçim alanında bu saniye aralıkları pasif görünür.

![DateRangePicker](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadeebdd294-8837-4bf6-b086-5e459eeda944)

![DateRangePicker](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb32d916d-2cb4-44a3-a745-bb13d8049803)

Birden çok saniye değerinin seçilememesi isteniyorsa, bu saniye değerleri arasına “,” konularak bu alana yazılır. Örneğin; 53, 55 ve 56 saniyelerinin seçilememesi istenirse, bu alana “53,55,56” ifadesi yazılmalıdır.

![DateRangePicker](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload46623951-b39c-4859-ac59-7548aa86fcb9)

![DateRangePicker](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload77de2179-9d0a-4664-b5e8-9540d0ca1330)

`Value` - Bitiş tarihi alanının değeri burada ifade edilir. Bu alanda seçilen tarih, bitiş tarihi alanının varsayılan değeri olarak nesnede belirir.

`Placeholder` - Nesne içine uç kullanıcı tarafından girilmesi istenen veri bilgisini, nesne içerisinde bilgi amaçlı göstermek için kullanılan özelliktir. Uç kullanıcı nesneyi görüntülediğinde bu alana yazılan yönlendirici metni görür, nesneye odaklandığında ve değer girmeye başladığında yönlendirici metin kaybolur.

![DateRangePicker](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload697de4dc-92c9-4e04-bcb8-1f27c2784d50)

![DateRangePicker](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload94339311-e8d5-4ecb-88f2-0d40dbcb9200)

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

`TextAlign` - Nesne içine girilen ifadenin hizalanacağı yerin belirlenmesi için kullanılan alandır. Sola hizala, merkeze hizala, sağa hizala seçimleri yapılabilir.

>Yapılabilecek Seçimler : Left, Center, Right

`Size Type` - Nesne boyutunun belirlenebileceği alandır.

>Yapılabilecek Seçimler : Small, Middle, Large

### Behavior

`ReadOnly` - Nesnenin düzenleme modunda olup olmayacağının ayarlandığı kısımdır. Bu özellik aktif edildiğinde nesne veri girişine izin vermez, salt okunur modda olur. Nesneye veri girişine izin verilmesi için özelliğin pasif olması gerekir.

`Tab Index` - Bu alana sayısal değerler girilerek, tab butonuna basıldığında form nesneleri arasında hangi sıra ile odaklanılacağı belirlenir. Form doldurulurken imleci, veri girilmek istenen nesneye tıklamak yerine, tab butonuna basarak belirli bir sırayla indekslenmiş nesnelere direk odaklanılması sağlanmış olur. Bu da form doldurma hızını artıran bir özelliktir.

`Required` - Nesnede veri girişinin zorunlu olup olmayacağının belirlendiği alandır. Bu özellik aktif edildiğinde nesne içerisine veri girişi yapılmadan formun ilerletilmesi/kaydedilmesi gerçekleştirilemez.

`Format` - Start ve End Date alanlarında görünecek olan tarih ve saat formatının belirlendiği kısımdır. Nesnede Show Time özelliği pasifken, varsayılan tarih formatı “YYYY-MM-DD” şeklindedir. Show Time özelliği aktifken, varsayılan format “YYYY-MM-DD HH:mm” şeklindedir. Nesnede gösterilmek istenen format yapısı bu alanda belirtilebilir.

`Mode` - Format alanı boş bırakıldığında aktif olan bir özelliktir. Nesnede gösterilecek değerin modunu ifade eder. Nesnenin start ve end date alanlarında; sadece yıl, sadece ay, sadece saat veya sadece gün bazlı seçim yapılmasını sağlamak için kullanılır.

![DateRangePicker](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadced031f0-faba-4906-8d10-24102cf4d137)

>Yapılabilecek Seçimler : Year, Month, Time, Date

`Show Time` - Nesnede saat değerinin gösterilmesi için bu özelliğin aktif edilmesi gerekir. Özellik aktif edildiğinde Format alanındaki varsayılan değer “YYYY-MM-DD HH:mm” şeklinde gösterilir.

`Show Today` - Nesnenin başlangıç ve bitiş tarihi alanlarında tarih seçimi ekranında “Bugün” seçeneğinin belirmesi için bu özellik aktif edilir. “Bugün” seçeneğine tıklandığında günün tarihi, nesneye otomatik olarak yansır.

![DateRangePicker](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1be18cfa-5d99-460b-840f-e6106b1a49c7)

`Date limit type` - Seçilecek tarih aralığında kısıtlama yapılmak istendiğinde, kısıtlama türünün belirlendiği alandır. Yapılan seçime göre nesne özelliğinde seçilmesi gereken alanlar değişecektir.

>Yapılabilecek Seçimler : Active Date Types, Disabled Date Types

`Active date type` - Date limit type alanında *Active Date Types* seçili olduğunda aktif olacak alandır. Alanda yapılacak öge seçimine göre seçim aralığının belirlenmesi aşağıdaki gibi olacaktır.
- `Range dates` - Seçimi yapıldığında nesnede **Disabled date** alanı seçilebilir duruma geçer. Disabled date içinde seçimi yapılacak tarih aralığına göre nesnede tarih seçimi yapılabilir, diğer tarihler seçilemez olacaktır.
![DateRangePicker](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5c300bc5-4720-46e0-aa36-73c605fcadef)
![DateRangePicker](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1aa43471-fb16-4fe0-81ef-621b1588d3eb)
- `In year` - Seçimi yapıldığında, sadece o anki yıldan bir tarih seçilebilir. Önceki veya sonraki yıllar seçilemez olacaktır.
- `In month` - Seçimi yapıldığında, sadece o anki ay içerisinden bir tarih seçilebilir. Önceki veya sonraki aylar pasif yani seçilemez olur.
![DateRangePicker](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2a4d2f0a-34de-4932-83e4-32d839933dd7)
- `In week` - Seçimi yapıldığında, sadece o anki hafta içerisinden bir tarih seçilebilir. Önceki ve sonraki haftalar pasif yani seçilemez olur.
![DateRangePicker](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload78bd735f-2e5b-48b9-8b31-ac05780d8b50)

`Disabled date type` - Date limit type alanında *Disabled Date Types* seçili olduğunda aktif olacak alandır. Alanda yapılacak öge seçimine göre seçim aralığının belirlenmesi aşağıdaki gibi olacaktır.

![DateRangePicker](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload613e95f6-68a8-41ec-9517-05934f7c809e)

- `Past disabled` - Seçimi yapıldığında, nesnede bugünden önceki tarihler seçilemez olarak görünür.
![DateRangePicker](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7af37645-700d-426b-86f4-d7b24b084956)
- `Before from date` - Seçimi yapıldığında nesnede **Disabled date** alanı seçilebilir duruma geçer. Disabled date içinde seçilecek tarih öncesinki tarihler nesne içerisinde seçilemez olarak gözükecektir.
![DateRangePicker](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d686c4e-7de8-4f5b-9c11-1e31337d2e81)
![DateRangePicker](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8feefd14-7e6e-4422-9f7a-8859111a90a7)
- `After from date` - Seçimi yapıldığında nesnede **Disabled date** alanı seçilebilir duruma geçer. Disabled date içinde seçilecek tarih sonrasındaki tarihler nesne içerisinde seçilemez olarak gözükecektir.
![DateRangePicker](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcfccdd2d-dc21-4a13-99b7-63942bed6b96)
![DateRangePicker](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0f2bab82-39da-4076-a3e8-d12d6295ffba)
- `Dynamic range` - Seçimi yapıldığında, nesne özelliklerindeki Disabled date range alanı aktif olur. Başlangıç tarihi alanı mevcut günden itibaren, burada yazılan sayısal değer kadar gün önce veya sonraya sabitlenir. Seçilebilen günler arasından seçilen başlangıç tarihine göre ise bitiş tarihi alanında, başlangıç tarihincen önceki bir gün seçilemeyeceği için aralık belirlenmiş olur.
![DateRangePicker](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadba53b3e0-0a86-4f42-a592-fadd85dc420b)
![DateRangePicker](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaded0295a1-557b-4197-ace9-2d4dfa169739)
![DateRangePicker](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload95f91aeb-0aac-46c6-8d31-a477ea47db3f)

`Allow Clear` - Nesne içinde yapılan seçimin kolaylıkla kaldırılabilmesi istenirse özellik aktif edilmelidir.

### Data Definition Language

`Field Name` - Sistemin veri tabanında, nesne için oluşturacağı kolonun adının belirlendiği alandır. “Name” kısmında nesneye başka bir isim verilip, veritabanı tablosunda nesne için oluşturulacak kolon adı farklı bir isim olarak yaratılabilir.

`Allow Null` - Nesne için oluşturulacak veritabanı alanının boş(null) değerlere izin verip vermeyeceği bu kısımdan belirtilir.

## Olaylar

Nesnenin sahip olduğu olaylar, Özellik Görüntüleyici panelindeki “Olaylar” sekmesinde yer almaktadır. Her bir olay, farklı çalışma anlarında tetiklenerek kendilerine özgü işlemleri gerçekleştirir. Bu olaylara geliştirici tarafından yazılan kodlar da ilgili olayın tetiklendiği anda çalıştırılır.

“Client” alanında bulunan olaylara çift tıklandığında ekran, TypeScript kodlamanın yapılabileceği “Formadı.ts” isimli form kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur.

“Server” alanında bulunan olaylara çift tıklandığında ekran, C# kodlamanın yapılabileceği “Formadı.cs” isimli form kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur.

Geliştirici bu methodlar içerisinde istediği kod bloğunu kurgulayabilir. Olaylar sekmesinden tıklanarak kod tarafında methodu oluşturulmuş olayın yanında, method adı bilgisi otomatik oluşturularak, olayla method arasındaki ilişki belirtilmiş olur.

![DateRangePicker](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5626addd-ab7f-4687-9f63-f3610b7ab6a4)