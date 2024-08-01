<h1>File Selector</h1>
FileSelector nesnesi; form üzerine, yerel dizinde veya Doküman Yönetim Sistemi’nde bulunan dosyaların yüklenmesini sağlayan nesnedir.

Nesneye dosya yükleme işlemi, alanın sağında bulunan üç nokta ifadesine tıklanarak yapılır. Bir ya da birden çok dosyanın seçimi yapılabilir. 


Nesneye yüklenmesi için seçilen dosyaların  **yüklenme durumu**, ekranın sağ üst köşesinde izlenebilir, dosya yüklemesi arka planda devam ederken kullanıcı, form üzerindeki diğer alanları doldurma işlemine devam edebilir.
![fileselectoruygulama](https://docsbimser.blob.core.windows.net/imagecontainer/fileselectoruygulama-122847a8-fe8e-4afa-921f-830449644898.png)

Nesneye yüklenen dosya üzerine tıklandığında, yan panelde dosya önizleme ekranının açılması sağlanır. Böylece yüklenen dosya web arayüzünde görüntülenebilmiş olur.



## Genel[​](https://docs.bimser.net/docs/Synergy/CSP/ide-objects/form/advanced-form-controls/FileSelector#genel "Başlığa doğrudan bağlantı")

### Design[​](https://docs.bimser.net/docs/Synergy/CSP/ide-objects/form/advanced-form-controls/FileSelector#design "Başlığa doğrudan bağlantı")

`Name`  - Nesnenin sistem tarafında kullanılacak ismidir. Başka bir nesnenin içinde ve kod tarafında nesneye, isim alanında yazan değerle erişim sağlanır.

### Caption[​](https://docs.bimser.net/docs/Synergy/CSP/ide-objects/form/advanced-form-controls/RelatedDocuments#caption "Başlığa doğrudan bağlantı")

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

### Appearance[​](https://docs.bimser.net/docs/Synergy/CSP/ide-objects/form/advanced-form-controls/FileSelector#appearance "Başlığa doğrudan bağlantı")

`Visible`  - Nesnenin gizlenip, görünür yapılma ayarlarının gerçekleştirildiği kısımdır. Bu alan aktifken, nesne form üzerinde görünür durumdadır. Alan pasif yapıldığında nesne görünmez olur.

`Client Visible`  - Form ilk açıldığında nesne görünmesin, belirli bir şart sağlandığında nesne görünür olsun gibi bir işlem yapılmak istendiğinde, nesnenin istemci tarafında görünmez olması için bu alan pasif yapılır. Kodla ya da Kural Yöneticisi ile belirlenen şart sağlandığında nesne tekrar görünür hale getirilebilir. Sunucu görünürlüğü aktif değilken, istemci müdahale edemez ancak istemci görünürlüğü aktif değilken sunucu müdahale edebilir.

`Enabled`  - Nesnenin etkin modu bu alandan ayarlanır. Bu özellik aktifken nesneye veri girişi sağlanabilir ve nesne düzenlenebilir. Özellik pasifken, nesne düzenlenemez moddadır ve pasif görünür.

`Client Enabled`  - Form ilk açıldığında nesne etkin olmasın, belirli bir şart sağlandığında etkin olsun gibi bir işlem yapılmak istendiğinde, nesnenin istemci tarafında etkin olmaması için bu alan pasif yapılır. Kodla ya da Kural Yöneticisi ile belirlenen şart sağlandığında nesne tekrar etkin hale getirilebilir. Sunucu etkinliği aktif değilken, istemci müdahale edemez ancak istemci etkinliği aktif değilken sunucu müdahale edebilir.

`Background Color`  - Nesneye arka plan rengi vermek için kullanılan alandır.

`Title`  - Form arayüzde açıkken imleç ile nesne üzerine gelindiğinde, bu alanda yazılan metin, ipucu olarak gösterilir. Nesne ile ilgili detay bilgi verilmek istendiğinde kullanılan, uç kullanıcıyı yönlendirme amaçlı bir özelliktir.

`ClassName`  - Forma ait CSS dosyası içinde yazılmış bir class'ın tanımlanarak nesne görünürlüğünün değiştirilebildiği alandır.

### Behavior[​](https://docs.bimser.net/docs/Synergy/CSP/ide-objects/form/advanced-form-controls/FileSelector#behavior "Başlığa doğrudan bağlantı")

`ReadOnly`  - Nesnenin düzenleme modunda olup olmayacağının ayarlandığı kısımdır. Bu özellik aktif edildiğinde nesne veri girişine izin vermez, salt okunur modda olur. Nesneye veri girişine izin verilmesi için özelliğin pasif olması gerekir.

`Allow Select Multiple` - Çoklu dosya seçimine izin verilip verilmeyeceğinin ayarlandığı özelliktir. Aktif edildiğinde birden fazla dosya seçilebilir ve Max Selection Count alanı aktif hale gelir.

`Max Selection Count` - Nesneye eklenecek maksimum dosya adedi bu alana yazılan değerle sınırlandırılır.

`Allow Remove` - Eklenen dosyaların kaldırılıp kaldırılamayacağının ayarlandığı özelliktir. Bu özellik aktif edildiğinde eklenen dosyalar kaldırılabilir hale gelir.

`Allow View` -  Bu özellik aktif edildiğinde eklenen dosyaların üzerine tıklandığında görüntülenebilmesi sağlanır.

`Selection Target` - Doküman yönetimi üzerinden nesneye doküman eklenmek istendiğinde kullanıcının karşısına ilk olarak bu alanda seçili olan klasör yönlendirilir.

`Upload Target` - Nesneye eklenen dosyaların kaydedileceği dosya yolunun verileceği alandır.

`Supported Extension` - Eklenen dosyalar için uzantı bilgisinin seçildiği alandır. Eklenecek dosyaların sadece bu alanda seçilen uzantı tiplerinde olması sağlanır.
![fileselector_extension](https://docsbimser.blob.core.windows.net/imagecontainer/FileSelector%20Supported%20Extensions-9edf0fca-862d-4cd2-a5c5-2f23028f8709.png)

### Data Definition Language[​](https://docs.bimser.net/docs/Synergy/CSP/ide-objects/form/advanced-form-controls/FileSelector#data-definition-language "Başlığa doğrudan bağlantı")

`Field Name`  - Sistemin veri tabanında, nesne için oluşturacağı kolonun adının belirlendiği alandır. “Name” kısmında nesneye başka bir isim verilip, veritabanı tablosunda nesne için oluşturulacak kolon adı farklı bir isim olarak yaratılabilir.

## Olaylar[​](https://docs.bimser.net/docs/Synergy/CSP/ide-objects/form/advanced-form-controls/RelatedDocuments#olaylar "Başlığa doğrudan bağlantı")

Nesnenin sahip olduğu olaylar, Özellik Görüntüleyici panelindeki “Olaylar” sekmesinde yer almaktadır. Her bir olay, farklı çalışma anlarında tetiklenerek kendilerine özgü işlemleri gerçekleştirir. Bu olaylara geliştirici tarafından yazılan kodlar da ilgili olayın tetiklendiği anda çalıştırılır.

“Client” alanında bulunan olaylara çift tıklandığında ekran, TypeScript kodlamanın yapılabileceği “Formadı.ts” isimli form kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur.

“Server” alanında bulunan olaylara çift tıklandığında ekran, C# kodlamanın yapılabileceği “Formadı.cs” isimli form kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur.

Geliştirici bu methodlar içerisinde istediği kod bloğunu kurgulayabilir. Olaylar sekmesinden tıklanarak kod tarafında methodu oluşturulmuş olayın yanında, method adı bilgisi otomatik oluşturularak, olayla method arasındaki ilişki belirtilmiş olur.

Oluşan methodlar;
![fileselectorclientevents](https://docsbimser.blob.core.windows.net/imagecontainer/FileSelector%20client%20event-21e277bd-6982-4536-9ed5-5e5f2ba153b7.png)
![fileselectorserverevents](https://docsbimser.blob.core.windows.net/imagecontainer/FileSelector%20server%20events-69f2222e-01fe-42d8-b962-59f135129576.png)
