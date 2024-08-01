---
sidebar_position: 2
custom_edit_url: ""
---

# MaskInput

MaskInput nesnesi, uç kullanıcıya belirli formatta bir değer girdirilmek istendiğinde kullanılan nesnedir. Karakter sayısı belli olan; Tc kimlik numarası, telefon numarası, IBAN gibi bilgilerin uygun formatta girilmesini sağlayan özel bir veri girişi nesnedir.

Geliştirme arayüzünde aktif ekran form iken, Araç Kutusu panelinde form nesneleri listelenir. Nesne, araç kutusu panelinden sürükle/bırak yöntemi ile forma eklenir.

![MaskInput](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload09943b7e-1efb-49ff-a722-8dd7b745a2fb)

Nesnenin üzerine tıklandığında Özellik Görüntüleyici panelinde "Genel" ve "Olaylar" sekmeleri yer alır ve nesneye ait özellikler görüntülenip, düzenlenebilir.

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

`ClassName` - Forma ait CSS dosyası içinde yazılmış bir class'ın tanımlanarak nesne görünürlüğünün değiştirilebildiği alandır

`Value` - Alana girilecek değer ile nesnede varsayılan veri gösterimi ayarlanabilir. 

`Placeholder` - Nesne içine uç kullanıcı tarafından girilmesi istenen veri bilgisini, nesne içerisinde bilgi amaçlı göstermek için kullanılan özelliktir. Uç kullanıcı nesneyi görüntülediğinde bu alana yazılan yönlendirici metni görür, nesneye odaklandığında ve değer girmeye başladığında yönlendirici metin kaybolur.

![MaskInput](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload757781b9-a442-4360-abc7-c2c6d5ed4b0b)

![MaskInput](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf818e165-078b-45f4-89d8-f2fcd4dfefbf)

`TextAlign` - Nesne içine girilen ifadenin hizalanacağı yerin belirlenmesi için kullanılan alandır. Sola hizala, merkeze hizala, sağa hizala seçimleri yapılabilir.

>Yapılabilecek Seçimler : Left, Center, Right

`Size Type` - Nesne boyutunun belirlenebileceği alandır.

>Yapılabilecek Seçimler : Small, Middle, Large

### Behavior

`ReadOnly` - Nesnenin düzenleme modunda olup olmayacağının ayarlandığı kısımdır. Bu özellik aktif edildiğinde nesne veri girişine izin vermez, salt okunur modda olur. Nesneye veri girişine izin verilmesi için özelliğin pasif olması gerekir.

`Tab Index` - Bu alana sayısal değerler girilerek, tab butonuna basıldığında form nesneleri arasında hangi sıra ile odaklanılacağı belirlenir. Form doldurulurken imleci, veri girilmek istenen nesneye tıklamak yerine, tab butonuna basarak belirli bir sırayla indekslenmiş nesnelere direk odaklanılması sağlanmış olur. Bu da form doldurma hızını artıran bir özelliktir.

`Required` - Nesnede veri girişinin zorunlu olup olmayacağının belirlendiği alandır. Bu özellik aktif edildiğinde nesne içerisine veri girişi yapılmadan formun ilerletilmesi/kaydedilmesi gerçekleştirilemez.

`Mask` - Nesneye girilmesi istenen formatın belirlendiği alandır. Bu alanda, “Maske Format Karakteri” alanında tanımlanan formatın karakteri girilerek, nesneye istenen veri giriş yapısının belirtilmesi sağlanmış olur.

> Örneğin; **"(0262) 341 43 14"**  Formatında bir telefon numarası bu alana girdirilmek istendiğinde; Maske alanına **"(0262) 999 99 99"** ifadesi yazılır. Burada bulunan 9 ifadesi, 0-9 arası bir rakam girilecek demektir.

![MaskInput](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadabafbb65-d900-4ce4-8f77-af32caea6a2e)

Maske bu şekilde tanımlanıp, Araç Çubuğundan "Önizleme" butonuna tıklanarak ya da web arayüzünde ilgili form açılarak nesneye tıklanır. Nesneye tıklandığında sabit verilen “(0262)” ifadesi görünür olur, bu ifade silinemez ve değiştirilemez. Uç kullanıcıdan telefon numarasının geri kalan rakamları girilmesi beklenir.

![MaskInput](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload689b5684-85f0-4ac3-bac9-ca50b9ac8325)

> **"TR11 1111 1111 1111 1111 1111 11"** Formatında bir Iban numarası girilmesi istendiğinde; Maske alanına **"TR99 9999 9999 9999 9999 9999 99"** ifadesi yazılır.

![MaskInput](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada15df41f-eef3-4dfe-998f-fd3263fc8d38)

Maske bu şekilde tanımlanıp, Araç Çubuğundan “Önizleme” butonuna tıklanarak ya da web arayüzünde ilgili form açılarak nesneye tıklanır. Nesneye tıklandığında sabit verilen “TR” ifadesi görünür olur, bu ifade silinemez ve değiştirilemez. Uç kullanıcıdan Iban bilgisinin geri kalan rakamları girilmesi beklenir.

![MaskInput](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcf8d8d52-8145-464d-b83f-12ce8eb76cf7)

:::info BİLGİ

Eğer sabit verilecek ifadede 9 rakamı yer alıyorsa; örneğin sadece 2019 yılına ait bir tarih girilmesi istendiğinde, maske alanına 0-9 arası rakam girilmesi istenen karakterlere yazılan “9” ifadesi ile sabit verilmek istenen "9" karakterinin karışmaması için, sabit karakter olan 9 un önüne "\" konulur.

:::

> **"11-11-2019"** Formatında, sadece 2019 yılına ait bir tarih girişi yaptırılmak istendiğinde; Maske alanına **"99-99-201\9"** ifadesi yazılır.

![MaskInput](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1c65fbc2-c71c-45c2-a461-4e47077bd405)

Maske bu şekilde tanımlanıp, Araç Çubuğundan "Önizleme" butonuna tıklanarak ya da web arayüzünde ilgili form açılarak nesneye tıklanır. Nesneye tıklandığında ilk 2 rakam sonunda "-" sonraki iki rakam sonunda da "-2019" ifadeleri görünür olur, bu ifadeler silinemez ve değiştirilemez.

![MaskInput](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0df208ba-0617-4a2b-ab4f-38776ac51da3)

`Mask Format Char` Maske alanında kullanılmak üzere formatlar ve bu formatları ifade eden karakter tanımlarının yapıldığı alandır. Burada tanımlı formatı ifade eden Maske Karakteri, Maske alanında kullanılır.

Varsayılan olarak sistem tarafından sunulan formatlar;

| Maske karakteri | Format      | Açıklama                                                                                                                                                                                |
|-----------------|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 9               | [0-9]       | Nesneye sadece 0-9 arası rakam girilmesine izin veren formattır.<br/>Maske alanına kaç defa “9” yazılırsa, o kadar 0-9 arası rakam girişi bekleniyor demektir.                           |
| a               | [A-Za-z]    | Nesneye sadece harf girilmesine izin veren formattır. Hem büyük hem küçük harf girişine izin verilir.<br/>Maske alanına kaç defa “a” yazılırsa, o kadar harf girişi bekleniyor demektir. |
| *               | [A-Za-z0-9] | Nesneye, büyük-küçük harf ve rakam girişine izin veren formattır.<br/>Maske alanına kaç defa “*” yazılırsa, o kadar harf veya rakam girişi bekleniyor demektir.                          |

![MaskInput](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada3cbc693-b634-4af9-b9ce-7b7452f6230d)

### Data Definition Language

`Field Name` - Sistemin veri tabanında, nesne için oluşturacağı kolonun adının belirlendiği alandır. “Name” kısmında nesneye başka bir isim verilip, veritabanı tablosunda nesne için oluşturulacak kolon adı farklı bir isim olarak yaratılabilir.

`Allow Null` - Nesne için oluşturulacak veritabanı alanının boş(null) değerlere izin verip vermeyeceği bu kısımdan belirtilir.

`Size` - Nesnenin veritabanı alanında tutacağı boyut bu alanda belirlenir.

:::caution DİKKAT

**Text** ve **Size** özellikleri, nesne yapısı gereği arayüzde bulunmamaktadır.

:::

## Olaylar

Nesnenin sahip olduğu olaylar, Özellik Görüntüleyici panelindeki “Olaylar” sekmesinde yer almaktadır. Her bir olay, farklı çalışma anlarında tetiklenerek kendilerine özgü işlemleri gerçekleştirir. Bu olaylara geliştirici tarafından yazılan kodlar da ilgili olayın tetiklendiği anda çalıştırılır.

**“Client”** alanında bulunan olaylara çift tıklandığında ekran, TypeScript kodlamanın yapılabileceği **“Formadı.ts”** isimli form kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur.

**“Server”** alanında bulunan olaylara çift tıklandığında ekran, C# kodlamanın yapılabileceği **“Formadı.cs”** isimli form kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur.

Geliştirici bu methodlar içerisinde istediği kod bloğunu kurgulayabilir. Olaylar sekmesinden tıklanarak kod tarafında methodu oluşturulmuş olayın yanında, method adı bilgisi otomatik oluşturularak, olayla method arasındaki ilişki belirtilmiş olur.

![MaskInput](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc41288c1-3661-4f07-86ec-fd03ebc769ac)

Oluşan methodlar;

![MaskInput](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload778a8f61-2acd-430a-9c6b-03cddd66abca)

![MaskInput](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaed287c4-a913-4857-8abe-5468507454a9)