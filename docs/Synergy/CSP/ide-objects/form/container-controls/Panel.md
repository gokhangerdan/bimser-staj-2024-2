---
sidebar_position: 1
custom_edit_url: ""
---

# Panel

Form nesnelerini gruplamak için kullanılan, nesne gruplarını gizleyip-gösterme opsiyonu sunun form tasarım nesnesidir.

Form üzerinde, işlev ya da anlam yönünden benzer nesneler panelin içine yerleştirilerek uç kullanıcılar için karmaşadan uzak, anlaşılır formlar tasarlamayı mümkün kılar. Ayrıca açılıp kapanma opsiyonu ile aynı panel içerisindeki nesneleri gizleme ve gösterme özelliği sağlanmış olur.

![Panel](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7d674cd2-ff47-46dc-8541-d094eb40aecd)

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

`Header Mode` - Nesne başlık yapısının ayarlandığı kısımdır. Nesnede başlık olmasın istenirse ***None***, nesne başlığı görünsün istenirse ***Titled***, arayüzde başlık kısmına tıklandığında nesne kapansın, tekrar tıklandığında açılsın istenirse ***Collapsible*** seçeneği seçilmelidir.

![Panel](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd5b12dd5-cf5b-4276-9abe-1d6139b2fb9c)

`Title Font` - Başlık alanındaki metnin font, yazı tipi, yazı boyutu ve renginin ayarlandığı kısımdır.

`Height` - Nesne yüksekliğinin ayarlandığı kısımdır. Nesne içerisine sığmayan elemanlar için arayüzde kaydırma çubuğu belirir ve nesne içindeki diğer elemanlar bu kaydırma çubuğu kullanılarak görülebilir.

![Panel](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcde791d4-952e-4fa9-9ae2-73f448df405b)

Kaydırma çubuğu çıkmasın, nesne içindeki tüm elemanlar görünür olsun istenirse, yükseklik kısmından nesne yüksekliği artırılabilir.

![Panel](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload231b8bab-2416-4358-b53e-c1a29299b7a7)

### Behavior

`ReadOnly` - Nesnenin düzenleme modunda olup olmayacağının ayarlandığı kısımdır. Bu özellik aktif edildiğinde nesne veri girişine izin vermez, salt okunur modda olur. Nesneye veri girişine izin verilmesi için özelliğin pasif olması gerekir.

## Olaylar

Nesnenin sahip olduğu olaylar, Özellik Görüntüleyici panelindeki "Olaylar" sekmesinde yer almaktadır. Her bir olay, farklı çalışma anlarında tetiklenerek kendilerine özgü işlemleri gerçekleştirir. Bu olaylara geliştirici tarafından yazılan kodlar da ilgili olayın tetiklendiği anda çalıştırılır.

"Client" alanında bulunan olaylara çift tıklandığında ekran, TypeScript kodlamanın yapılabileceği "Formadı.ts" isimli form kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur.

"Server" alanında bulunan olaylara çift tıklandığında ekran, C# kodlamanın yapılabileceği "Formadı.cs" isimli form kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur.

Geliştirici bu methodlar içerisinde istediği kod bloğunu kurgulayabilir. Olaylar sekmesinden tıklanarak kod tarafında methodu oluşturulmuş olayın yanında, method adı bilgisi otomatik oluşturularak, olayla method arasındaki ilişki belirtilmiş olur.

![Panel](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada91f79ef-4e3d-4a90-beb8-a0cdc7579958)

Oluşan methodlar;

![Panel](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload57d071fd-c591-4859-8bf4-fa9d948aff65)

![Panel](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload12231816-beee-4b85-8cad-6234f900839e)