---
sidebar_position: 15
custom_edit_url: ""
---

# NumberBox

Sayısal bir veri girişi yapılmak istendiğinde kullanılacak nesnedir. Ondalık (decimal) ve tamsayı (integer) veri girişlerini destekler ve sayısal ifadeler için kullanılabilecek özel ayarları özellik olarak barındırır.

Geliştirme arayüzünde aktif ekran form iken, Araç Kutusu panelinde form nesneleri listelenir. Nesne, araç kutusu panelinden sürükle/bırak yöntemi ile forma eklenir.

![NumberBox](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload366bbfaf-ac20-4e63-ae71-e313b2ce83e6)

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

`Placeholder` - Nesne içine uç kullanıcı tarafından girilmesi istenen veri bilgisini, nesne içerisinde bilgi amaçlı göstermek için kullanılan özelliktir. Uç kullanıcı nesneyi görüntülediğinde bu alana yazılan yönlendirici metni görür, nesneye odaklandığında ve değer girmeye başladığında yönlendirici metin kaybolur.

![NumberBox](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5c2bfb57-bb05-4308-9bf8-5049b0d3282d)

![NumberBox](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9b9ca511-d92a-4914-bee4-ef01bac45e1d)

`TextAlign` - Nesne içine girilen ifadenin hizalanacağı yerin belirlenmesi için kullanılan alandır. Sola hizala, merkeze hizala, sağa hizala seçimleri yapılabilir.

>Yapılabilecek Seçimler : Left, Center, Right

`Size Type` - Nesne boyutunun belirlenebileceği alandır.

>Yapılabilecek Seçimler : Small, Middle, Large

### Behavior

`ReadOnly` - Nesnenin düzenleme modunda olup olmayacağının ayarlandığı kısımdır. Bu özellik aktif edildiğinde nesne veri girişine izin vermez, salt okunur modda olur. Nesneye veri girişine izin verilmesi için özelliğin pasif olması gerekir.

`Tab Index` - Bu alana sayısal değerler girilerek, tab butonuna basıldığında form nesneleri arasında hangi sıra ile odaklanılacağı belirlenir. Form doldurulurken imleci, veri girilmek istenen nesneye tıklamak yerine, tab butonuna basarak belirli bir sırayla indekslenmiş nesnelere direk odaklanılması sağlanmış olur. Bu da form doldurma hızını artıran bir özelliktir.

`Required` - Nesnede veri girişinin zorunlu olup olmayacağının belirlendiği alandır. Bu özellik aktif edildiğinde nesne içerisine veri girişi yapılmadan formun ilerletilmesi/kaydedilmesi gerçekleştirilemez.

`Max` - Nesneye girilebilecek maksimum değerin belirlendiği alandır.

`Min` - Nesneye girilebilecek minimum değerin belirlendiği alandır.

`Step` - Nesne değerinin kaçar kaçar artıp azalacağının belirlendiği alandır. Artırma ve azaltma işlemleri nesne yanındaki ok butonları ile gerçekleştirilir. Bu alana girilen sayı değerince nesne verisi, ok tuşları kullanılarak step alanına girilen değer kadar artıp azalır.

![NumberBox](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload10e03d19-ef96-465b-9778-ee7780085195)

`Precision` - Virgülden sonra kaç karakter olacağının belirlendiği alandır. Virgülden sonra yazılan değeri aşağı ya da yukarı yuvarlayarak verilen karakter sayısına göre otomatik düzenler. 

Örneğin precision değeri olarak 2 verilmiş olsun. Ara yüzde kullanıcı bu nesneye “112” değeri girerek formdaki başka bir alana tıkladığında nesnedeki değer otomatik olarak “112.00” olacaktır. 

![NumberBox](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0fa6d8ec-c9c2-4551-8930-f9c30deeeaa6)

Nesneye, “112.454” değeri yazıldığında, hassasiyet 2 belirlendiği için, virgülden sonra 2 rakam sayılır, 3. rakam kontrol edilir. 3. rakamın değeri (bu örnek için ‘4’), 5 den küçükse bu rakam direkt olarak atılır ve nesnede “112.45” değeri yazar.

Ancak virgülden sonra “112.456” değeri yazsa idi, virgülden sonraki 3. rakamın değeri (bu örnek için ‘6’), 5 ve 5’den büyük olduğu için sayı yukarı yuvarlanacak ve nesnede “112.46” değeri yazılacaktı.

`Use Thousand Seperator` - Nesneye girilen değere otomatik binlik ayracı eklenmesini sağlayan özelliktir.

### Data Definition Language

`Field Name` - Sistemin veri tabanında, nesne için oluşturacağı kolonun adının belirlendiği alandır. “Name” kısmında nesneye başka bir isim verilip, veritabanı tablosunda nesne için oluşturulacak kolon adı farklı bir isim olarak yaratılabilir.

`Allow Null` - Nesne için oluşturulacak veritabanı alanının boş(null) değerlere izin verip vermeyeceği bu kısımdan belirtilir.

`Size` - Nesnenin veritabanı alanında tutacağı boyut bu alanda belirlenir. Max alanında ve varsa Precision alanında tanımlanan değerler toplamına göre hesaplanır.

`Precision` - Nesnenin veritabanı alanında tutacağı boyut bu alanda belirlenir. Precision alanına girilen değeri otomatik alır.

## Olaylar

Nesnenin sahip olduğu olaylar, Özellik Görüntüleyici panelindeki “Olaylar” sekmesinde yer almaktadır. Her bir olay, farklı çalışma anlarında tetiklenerek kendilerine özgü işlemleri gerçekleştirir. Bu olaylara geliştirici tarafından yazılan kodlar da ilgili olayın tetiklendiği anda çalıştırılır.

“Client” alanında bulunan olaylara çift tıklandığında ekran, TypeScript kodlamanın yapılabileceği “Formadı.ts” isimli form kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur.

“Server” alanında bulunan olaylara çift tıklandığında ekran, C# kodlamanın yapılabileceği “Formadı.cs” isimli form kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur.

Geliştirici bu methodlar içerisinde istediği kod bloğunu kurgulayabilir. Olaylar sekmesinden tıklanarak kod tarafında methodu oluşturulmuş olayın yanında, method adı bilgisi otomatik oluşturularak, olayla method arasındaki ilişki belirtilmiş olur.

![NumberBox](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada1f12b1f-3901-4a46-b44c-fcb46a6d2441)

Oluşan methodlar;

![NumberBox](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfec33f36-b2ff-4b39-a432-1525e12f8f58)

![NumberBox](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada4a70907-b172-48cb-bf66-bfeed1f594c6)