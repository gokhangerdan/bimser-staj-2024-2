# FormViewer
FormViewer nesnesi, bir form içerisinde başka bir formun görüntülenebilmesi ve düzenlenebilmesini sağlayan nesnedir. 
Geliştirme arayüzünde aktif ekran form iken, Araç Kutusu panelinde form nesneleri listelenir. Nesne, araç kutusu panelinden sürükle/bırak yöntemi ile forma eklenir.

## Genel[​](https://docs.bimser.net/docs/Synergy/CSP/ide-objects/form/advanced-form-controls/FormViewer#genel "Başlığa doğrudan bağlantı")

### Design[​](https://docs.bimser.net/docs/Synergy/CSP/ide-objects/form/advanced-form-controls/FormViewer#design "Başlığa doğrudan bağlantı")

`Name`  - Nesnenin sistem tarafında kullanılacak ismidir. Başka bir nesnenin içinde ve kod tarafında nesneye, isim alanında yazan değerle erişim sağlanır.

### Caption[​](https://docs.bimser.net/docs/Synergy/CSP/ide-objects/form/advanced-form-controls/FormViewer#caption "Başlığa doğrudan bağlantı")

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

### Appearance[​](https://docs.bimser.net/docs/Synergy/CSP/ide-objects/form/advanced-form-controls/FormViewer#appearance "Başlığa doğrudan bağlantı")

`Visible`  - Nesnenin gizlenip, görünür yapılma ayarlarının gerçekleştirildiği kısımdır. Bu alan aktifken, nesne form üzerinde görünür durumdadır. Alan pasif yapıldığında nesne görünmez olur.

`Client Visible`  - Form ilk açıldığında nesne görünmesin, belirli bir şart sağlandığında nesne görünür olsun gibi bir işlem yapılmak istendiğinde, nesnenin istemci tarafında görünmez olması için bu alan pasif yapılır. Kodla ya da Kural Yöneticisi ile belirlenen şart sağlandığında nesne tekrar görünür hale getirilebilir. Sunucu görünürlüğü aktif değilken, istemci müdahale edemez ancak istemci görünürlüğü aktif değilken sunucu müdahale edebilir.

`Title`  - Form arayüzde açıkken imleç ile nesne üzerine gelindiğinde, bu alanda yazılan metin, ipucu olarak gösterilir. Nesne ile ilgili detay bilgi verilmek istendiğinde kullanılan, uç kullanıcıyı yönlendirme amaçlı bir özelliktir.

`ClassName`  - Forma ait CSS dosyası içinde yazılmış bir class'ın tanımlanarak nesne görünürlüğünün değiştirilebildiği alandır.

### Behavior[​](https://docs.bimser.net/docs/Synergy/CSP/ide-objects/form/advanced-form-controls/FormViewer#behavior "Başlığa doğrudan bağlantı")

`Project`  - Nesnede açılması istenen formun bulunduğu projenin seçileceği alandır.

`Form`  - Seçilen projeden nesnede açılması istenen formun seçildiği alandır.
:::info Bilgi
FormViewer nesnesinin bulunduğu form kaydedildiğinde, nesneye eklenen form eğer parametreli form ise formda yapılan değişiklikler de kaydedilebilmektedir. 
:::

`View`  - Seçilen formun hangi view'ının nesneye ekleneceğinin seçildiği alandır.

`Height` - Nesne yüksekliğinin tanımlandığı alandır. Girilen değere göre nesnenin piksel türünde yüksekliği değişecektir. 

### Data Definition Language[​](https://docs.bimser.net/docs/Synergy/CSP/ide-objects/form/advanced-form-controls/FormViewer#data-definition-language "Başlığa doğrudan bağlantı")

`Field Name`  - Sistemin veri tabanında, nesne için oluşturacağı kolonun adının belirlendiği alandır. “Name” kısmında nesneye başka bir isim verilip, veritabanı tablosunda nesne için oluşturulacak kolon adı farklı bir isim olarak yaratılabilir.



## Olaylar[​](https://docs.bimser.net/docs/Synergy/CSP/ide-objects/form/advanced-form-controls/FormViewer#olaylar "Başlığa doğrudan bağlantı")

Nesnenin sahip olduğu olaylar, Özellik Görüntüleyici panelindeki “Olaylar” sekmesinde yer almaktadır. Her bir olay, farklı çalışma anlarında tetiklenerek kendilerine özgü işlemleri gerçekleştirir. Bu olaylara geliştirici tarafından yazılan kodlar da ilgili olayın tetiklendiği anda çalıştırılır.

“Client” alanında bulunan olaylara çift tıklandığında ekran, TypeScript kodlamanın yapılabileceği “Formadı.ts” isimli form kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur.

“Server” alanında bulunan olaylara çift tıklandığında ekran, C# kodlamanın yapılabileceği “Formadı.cs” isimli form kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur.

Geliştirici bu methodlar içerisinde istediği kod bloğunu kurgulayabilir. Olaylar sekmesinden tıklanarak kod tarafında methodu oluşturulmuş olayın yanında, method adı bilgisi otomatik oluşturularak, olayla method arasındaki ilişki belirtilmiş olur.
![formView](https://docsbimser.blob.core.windows.net/imagecontainer/FormView-3bacdbde-9108-4007-bf50-6d97aeced7c8.png)

Oluşan methodlar;
![FormViewTs](https://docsbimser.blob.core.windows.net/imagecontainer/FormViewTs-7bd5c24b-9167-4833-88a6-e1426dd0b263.png)

![FormViewCs](https://docsbimser.blob.core.windows.net/imagecontainer/FormViewCS-e323e905-ffb1-412c-a91e-0e2d3a1f457b.png)
