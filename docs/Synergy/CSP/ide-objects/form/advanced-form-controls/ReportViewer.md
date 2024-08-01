# ReportViewer

ReportViewer, çözüm gezgininde Reports klasörü altında oluşturulmuş raporların form üzerinde görünmesini sağlayan nesnedir.
Geliştirme arayüzünde aktif ekran form iken, Araç Kutusu panelinde form nesneleri listelenir. Nesne, araç kutusu panelinden sürükle/bırak yöntemi ile forma eklenir.

## Genel[​](https://docs.bimser.net/docs/Synergy/CSP/ide-objects/form/advanced-form-controls/ReportViewer#genel "Başlığa doğrudan bağlantı")

### Design[​](https://docs.bimser.net/docs/Synergy/CSP/ide-objects/form/advanced-form-controls/ReportViewer#design "Başlığa doğrudan bağlantı")

`Name`  - Nesnenin sistem tarafında kullanılacak ismidir. Başka bir nesnenin içinde ve kod tarafında nesneye, isim alanında yazan değerle erişim sağlanır.

### Caption[​](https://docs.bimser.net/docs/Synergy/CSP/ide-objects/form/advanced-form-controls/ReportViewer#caption "Başlığa doğrudan bağlantı")

`Title`  - Nesnenin etiket metninin düzenlendiği kısımdır.

`Position`  - Nesne etiketinin, nesnenin solunda mı, sağında mı yoksa üzerinde mi konumlandırılacağının düzenlendiği kısımdır.

> Yapılabilecek Seçimler : Left, Right, Top, Bottom

`Width`  - Etiket alanının genişliğinin ayarlandığı kısımdır.

`Height`  - Etiket alanının yüksekliğinin ayarlandığı kısımdır.

`Font`  - Etiket alanındaki metnin font, yazı tipi, yazı boyutu ve renginin ayarlandığı kısımdır.

`Ellipsis`  - Etiket metninin, etiket alanına sığmadığı durumlarda, metnin sığmayan kısmı için üç nokta (…) ifadesinin görünüp görünmeyeceğinin ayarlandığı kısımdır.

`Visible`  - Etiket alanının gizli ya da görünür ayarlarının yapıldığı kısımdır.

`Show Colon`  - Etiket metninin yanında iki nokta (:) ifadesinin görünüp görünmeyeceğinin ayarlandığı kısımdır.

`Horizontal Align`  - Etiket metnini; sağa yasla, sola yasla ya da ortala ayarlarının gerçekleştirildiği kısımdır.

> Yapılabilecek Seçimler : Left, Center, Right

`Vertical Align`  - Etiket metnini; yukarı yasla, aşağı yasla ya da ortala ayarlarının gerçekleştirildiği kısımdır.

> Yapılabilecek Seçimler : Top, Middle, Bottom

`Mark Char`  - Nesneyi belirginleştirmek için, etiket metnine *, ! gibi karakterlerin girilebileceği alandır.

`Mark Position`  - İşaret karakteri olarak belirlenen karakterin, etiket metninin başında mı yoksa sonunda mı gösterilmesinin ayarlandığı kısımdır.

> Yapılabilecek Seçimler : AtFirst, AtLast

### Appearance[​](https://docs.bimser.net/docs/Synergy/CSP/ide-objects/form/advanced-form-controls/ReportViewer#appearance "Başlığa doğrudan bağlantı")

`Visible`  - Nesnenin gizlenip, görünür yapılma ayarlarının gerçekleştirildiği kısımdır. Bu alan aktifken, nesne form üzerinde görünür durumdadır. Alan pasif yapıldığında nesne görünmez olur.

`Client Visible`  - Form ilk açıldığında nesne görünmesin, belirli bir şart sağlandığında nesne görünür olsun gibi bir işlem yapılmak istendiğinde, nesnenin istemci tarafında görünmez olması için bu alan pasif yapılır. Kodla ya da Kural Yöneticisi ile belirlenen şart sağlandığında nesne tekrar görünür hale getirilebilir. Sunucu görünürlüğü aktif değilken, istemci müdahale edemez ancak istemci görünürlüğü aktif değilken sunucu müdahale edebilir.

`Enabled`  - Nesnenin etkin modu bu alandan ayarlanır. Bu özellik aktifken nesneye veri girişi sağlanabilir ve nesne düzenlenebilir. Özellik pasifken, nesne düzenlenemez moddadır ve pasif görünür.

`Client Enabled`  - Form ilk açıldığında nesne etkin olmasın, belirli bir şart sağlandığında etkin olsun gibi bir işlem yapılmak istendiğinde, nesnenin istemci tarafında etkin olmaması için bu alan pasif yapılır. Kodla ya da Kural Yöneticisi ile belirlenen şart sağlandığında nesne tekrar etkin hale getirilebilir. Sunucu etkinliği aktif değilken, istemci müdahale edemez ancak istemci etkinliği aktif değilken sunucu müdahale edebilir.

`Background Color`  - Nesneye arka plan rengi vermek için kullanılan alandır.

`Title`  - Form arayüzde açıkken imleç ile nesne üzerine gelindiğinde, bu alanda yazılan metin, ipucu olarak gösterilir. Nesne ile ilgili detay bilgi verilmek istendiğinde kullanılan, uç kullanıcıyı yönlendirme amaçlı bir özelliktir.

`ClassName`  - Forma ait CSS dosyası içinde yazılmış bir class'ın tanımlanarak nesne görünürlüğünün değiştirilebildiği alandır.

`Report` - Reports klasörünün altında tasarlanmış olan raporlardan nesneye eklenmesi istenen raporun seçildiği alandır.

`parameters` - Tasarlanan raporda oluşturulmuş parametrelerin listelendiği ve seçildiği alandır.
-   `Name`  - Report Designer üzerinde hazırlanan raporda oluşturulan parametre isminin göründüğü alandır. 
-   `Parameter Type`  - Report Designer üzerinde tasarlanan raporda oluşturulmuş parametrenin tipinin gösterildiği alandır. (static ya da dynamic olabilmektedir)
-   `Type`  -  Report Designer üzerinde parametrenin belirlenen veri tipinin gösterildiği alandır. 
-   `Allow Null` - Parametre değeri için boş(null) değerlere izin verilip verilmediğinin gösterildiği alandır.
-   `Alan` - Parametre değerinin form üzerindeki hangi alandan alınacağının belirlendiği alandır. 

`Height` -  Nesne yüksekliğinin tanımlandığı alandır. Girilen değere göre nesnenin piksel türünde yüksekliği değişecektir.

## Olaylar[​](https://docs.bimser.net/docs/Synergy/CSP/ide-objects/form/advanced-form-controls/ReportViewer#olaylar "Başlığa doğrudan bağlantı")

Nesnenin sahip olduğu olaylar, Özellik Görüntüleyici panelindeki “Olaylar” sekmesinde yer almaktadır. Her bir olay, farklı çalışma anlarında tetiklenerek kendilerine özgü işlemleri gerçekleştirir. Bu olaylara geliştirici tarafından yazılan kodlar da ilgili olayın tetiklendiği anda çalıştırılır.

“Client” alanında bulunan olaylara çift tıklandığında ekran, TypeScript kodlamanın yapılabileceği “Formadı.ts” isimli form kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur.

“Server” alanında bulunan olaylara çift tıklandığında ekran, C# kodlamanın yapılabileceği “Formadı.cs” isimli form kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur.

Geliştirici bu methodlar içerisinde istediği kod bloğunu kurgulayabilir. Olaylar sekmesinden tıklanarak kod tarafında methodu oluşturulmuş olayın yanında, method adı bilgisi otomatik oluşturularak, olayla method arasındaki ilişki belirtilmiş olur.

![ReportViewer](https://docsbimser.blob.core.windows.net/imagecontainer/ReportViewer-0febf810-ad62-460c-b2e8-96e05d999ba3.png)

Oluşan methodlar;
![ReportDesignerTS](https://docsbimser.blob.core.windows.net/imagecontainer/ReportViewerTS-a41bfcaf-8643-4cc6-82ac-8c4fb232a9ef.png)
![ReportDesignerCS](https://docsbimser.blob.core.windows.net/imagecontainer/ReportDesignerCs-09e8b47d-d6e1-4b6e-a594-3daffe051c4a.png)
