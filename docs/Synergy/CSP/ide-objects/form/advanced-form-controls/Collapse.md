---
sidebar_position: 11
custom_edit_url: ""
---

# Collapse

Form üzerinde nesneleri gruplanarak, daraltılabilen ve genişletilebilen bir içerik alanı içeren nesnedir. Formda sayfayı temiz tutmak için karmaşık bölgeleri gruplamak veya gizlemek için kullanılabilmektedir.

Geliştirme arayüzünde aktif ekran form iken, Araç Kutusu panelinde form nesneleri listelenir. Nesne, araç kutusu panelinden sürükle/bırak yöntemi ile forma eklenir.

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

`Items` - Nesneye eklenecek panel ögelerinin tanımlandığı alandır. Elemanlar alanına tıklandığında eleman ekleme penceresi açılır. Bu alandan nesneye yeni eleman eklenebilir, mevcut bir eleman silinebilir veya düzenlenebilir. Ekle butonuna tıklanarak nesneye yeni eleman kalemleri oluşturulur.
  - `Key` - Ögeye verilecek anahtar değeri bu alana yazılır, ekli diğer ögelerdeki key alanlarında tanımlanmış değerlerden farklı olmalıdır, aynı değer yazılırsa ekleme işlemi yapılmaz.
  - `Title` - Ögeye verilecek isim bu alana yazılır.
  - `Expanded` - Ögenin otomatik olarak açık gelmesi istenirse alan aktif edilmelidir. Birden fazla Expanded seçimi yaparak birden fazla panelin açık gelmesi sağlanabilir. Özellik nesnedeki Accordion özelliği ile birlikte çalışmakta olup, Accordion özelliği **aktif** olduğunda **sadece bir ögenin Expanded özelliği aktif** olabilmektedir.
  - `Enabled` - Alan aktif edilerek ögenin ve içindeki nesnelerin gizlenmesi sağlanmaktadır. 

`Height` - Nesnenin yüksekliğinin piksel cinsinden tanımlandığı alandır.

`Has Scrollbar` - Alan aktif edildiğinde nesne içindeki panel açıldığında Height alanındaki limit geçildiyse panel içinde kaydırma çubuğunun gösterilmesi için kullanılmaktadır. Kapalı ise panel açıldığında içindeki bütün nesneler gösterilir.

`Toolbox Items` - Nesne üzerinde toolbar bölümüne butonlar eklenerek, butonlara tıklanınca işlem yapılması istenirse kullanılmaktadır. Toolbox Items alanına tıklandığında eleman ekleme penceresi açılır. Bu alandan nesnede toolbox içine yeni eleman eklenebilir, mevcut bir eleman silinebilir veya düzenlenebilir. Ekle butonuna tıklanarak nesneye yeni eleman kalemleri oluşturulur.
  - `Key` - Ögeye verilecek anahtar değeri bu alana yazılır, ekli diğer ögelerdeki key alanlarında tanımlanmış değerlerden farklı olmalıdır, aynı değer yazılırsa ekleme işlemi yapılmaz.
  - `Title` - Ögeye verilecek isim bu alana yazılır. Show text alanı aktif olduğunda girilen ifade gösterilir.
  - `Far Item` - Alan aktif edilerek ögenin toolbox içinde normal ögelerden ayrı bir grupta, sağa dayalı olarak gösterilmesi sağlanır. Birden fazla ögede Far Item özelliği seçili ise, seçili ögeler eklenme sıralarına göre toolbox içinde sağa yaslı olarak gösterilir.  
  > Örneğin ekli ögeler içinde ToolItem1'den 6'ya kadar sırası ile ekli ögelerde 3, 4 ve 5 için Far Item özelliği aktif edildiğinde 5 numaralı item en sağda olurken, 3 numaralı öge bu grubun en solunda olacaktır. 1,2 ve 6 numaralı ögeler ise Far Item ögelerinin solunda kendi içinde gruplanmış olarak gösterilecektir.
  - `Icon` - Ögeye ikon tanımlanmak istendiğinde bu alandan seçim yapılır.
  - `Show text` - Ögenin Title alanında girilen ifadenin gösterimi istenirse alan aktif edilmelidir.

### Behavior

`ReadOnly` - Nesnenin düzenleme modunda olup olmayacağının ayarlandığı kısımdır. Bu özellik aktif edildiğinde nesne veri girişine izin vermez, salt okunur modda olur. Nesneye veri girişine izin verilmesi için özelliğin pasif olması gerekir.

`Accordion` - Alan aktif edildiğinde nesnede aktif olarak sadece bir öge açılarak içerdiği nesnelere görüntülenir. Nesne içine eklenen ögelerden bir tanesi açıkken farklı bir öge görüntülenmek için açıldığında önceden açılmış ögenin otomatik olarak kapanması için kullanılır.

## Olaylar

Nesnenin sahip olduğu olaylar, Özellik Görüntüleyici panelindeki "Olaylar" sekmesinde yer almaktadır. Her bir olay, farklı çalışma anlarında tetiklenerek kendilerine özgü işlemleri gerçekleştirir. Bu olaylara geliştirici tarafından yazılan kodlar da ilgili olayın tetiklendiği anda çalıştırılır.

"Client" alanında bulunan olaylara çift tıklandığında ekran, TypeScript kodlamanın yapılabileceği "Formadı.ts" isimli form kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur.

"Server" alanında bulunan olaylara çift tıklandığında ekran, C# kodlamanın yapılabileceği "Formadı.cs" isimli form kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur.

Geliştirici bu methodlar içerisinde istediği kod bloğunu kurgulayabilir. Olaylar sekmesinden tıklanarak kod tarafında methodu oluşturulmuş olayın yanında, method adı bilgisi otomatik oluşturularak, olayla method arasındaki ilişki belirtilmiş olur.