---
sidebar_position: 2
custom_edit_url: ""
---

# Tabs

Farklı form görünümleri olarak tasarlanmış ekranlar arasında geçiş yapmayı sağlayan nesnedir. Birden çok sekmenin her biri, farklı tasarımlarla diğer form nesneleri sürüklenerek dizayn edilebilir ve sekmeler arası geçiş yapılarak aktif sekmedeki nesneler düzenlenebilir.

![Tabs](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0287a006-7ce9-42bb-ae19-6dc8b8478310)

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

`Items` - Nesne sekmelerinin belirlendiği alandır. Nesnede kaç sekme olacağı, sekme isimleri ve özellikleri bu alandan yönetilir. 

![Tabs](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1b654c60-cb92-40e6-96d3-a3f7f3d3197a)

Elemanlar kısmına tıklandığında ekrana, Sekme Ekleme penceresi açılır. Panel içindeki Ekle butonuna tıklanıldığında nesneye yeni sekmeler eklenebilir ve sekme özellikleri düzenlenebilir. 

![Tabs](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload357d25de-67ab-4001-afc7-fe5030c35c63)

Eklenen sekme kaydına tıklandığında sağ tarafta sekme özellikleri listelenir. Bu özellikler düzenlenerek sekme özelleştirilebilir.

![Tabs](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload868356f2-f94e-45d2-b2d7-7e12c931d5db)

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Key 	| Ögenin benzersiz anahtarının tanımlandığı alandır. Nesne içindeki diğer ögelerden farklı olacak şekilde key alanının değeri yazılır. 	|
| Title 	| Sekme adının düzenlendiği alandır. Buradaki Çoklu Dil Desteği özelliği ile sekme adının diğer dillerdeki karşılıkları tanımlanabilir. Sisteme giriş yapılan dile göre sekme adı ilgili dil tanımında görülecektir. 	|
| Selected 	| Selected alanı aktif edilen sekme, nesne arayüzde açıldığı anda varsayılan olarak tıklanmış şekilde açık gelir. Uç kullanıcı için, form açıldığı anda nesnede hangi sekmenin açık gelmesi isteniyorsa o sekmede bu özellik aktif edilir. Nesneye eklenen hiçbir sekmede bu özellik aktif edilmezse, ilk eklenen sekme açık olarak gelecektir. 	|
| Enabled 	| Sekmenin açılabilme durumunun etkin olup olmayacağının belirlendiği özelliktir. Enabled alanı pasif yapılan bir sekme, web arayüzünde tıklanıp, açılamamaktadır. Bu özellik genelde, kullanıcı bazlı sekme görünürlüklerinin yönetilmesi istenen durumlarda, yetkisi olmayan kullanıcıların ilgili sekmeyi görememesi işlemleri için kullanılır. 	|
| Icon 	| Sekme ikonunun belirlendiği kısımdır. Bu alana tıklandığında ikon bulucu ekranı açılır. Bu ekrandan seçilen ikon ilgili sekmede gösterilen ikon olarak belirlenebilir. 	|

`Tab Position` - Nesnedeki sekmelerin yukarıda (top), sağda (right), aşağıda (bottom) veya solda (left) konumlandırılacağının seçildiği kısımdır.

![Tabs](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload914747a5-cc2d-41fa-9e1d-f5b84655d161)

`Height` - Nesne yüksekliğinin ayarlandığı kısımdır. Nesne içerisine sığmayan elemanlar için arayüzde kaydırma çubuğu belirir ve nesne içindeki diğer elemanlar bu kaydırma çubuğu kullanılarak görülebilir. 

![Tabs](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload342c4568-e506-49a7-8cb0-e5a499da628f)

Kaydırma çubuğu çıkmasın, nesne içindeki tüm elemanlar görünür olsun istenirse, yükseklik kısmından nesne yüksekliği artırılabilir. Böylece nesne yüksekliği, içindeki eleman sayısına göre düzenlenebilmiş olur.

![Tabs](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload75940c8e-01fc-429c-a6bc-770c8a14a913)

`Has Scroll Bar` - Özellik aktifken, nesne içine eklenen elemanların mevcut yüksekliğe sığmadığı durumlarda nesnede kaydırma çubuğu belirir. Bu özellik pasif yapıldığında nesne yüksekliği içinde bulunan elemanlara göre optimize edilir ve kaydırma çubuğu çıkarılmaz.

## Olaylar

Nesnenin sahip olduğu olaylar, Özellik Görüntüleyici panelindeki "Olaylar" sekmesinde yer almaktadır. Her bir olay, farklı çalışma anlarında tetiklenerek kendilerine özgü işlemleri gerçekleştirir. Bu olaylara geliştirici tarafından yazılan kodlar da ilgili olayın tetiklendiği anda çalıştırılır.

"Client" alanında bulunan olaylara çift tıklandığında ekran, TypeScript kodlamanın yapılabileceği "Formadı.ts" isimli form kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur.

"Server" alanında bulunan olaylara çift tıklandığında ekran, C# kodlamanın yapılabileceği "Formadı.cs" isimli form kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur.

Geliştirici bu methodlar içerisinde istediği kod bloğunu kurgulayabilir. Olaylar sekmesinden tıklanarak kod tarafında methodu oluşturulmuş olayın yanında, method adı bilgisi otomatik oluşturularak, olayla method arasındaki ilişki belirtilmiş olur.

![Tabs](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload11582f49-9623-443f-ba3a-aabefbffe34d)

Oluşan methodlar;

![Tabs](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload61005c8c-1a16-49ea-b1f6-886b24059e9b)

![Tabs](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1b9beb2c-a387-4b31-804b-192fef3cf951)