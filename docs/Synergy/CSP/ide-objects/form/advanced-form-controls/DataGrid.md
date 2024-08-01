---
sidebar_position: 2
custom_edit_url: ""
---

# DataGrid

Bir veri kaynağından gelen değerleri tablo yapısı şeklinde gösterebilen, satır satır veri eklenebilen, satırlara tıklandığında çeşitli aksiyonlar alınmasını sağlayan çok fonksiyonlu bir tablo nesnesidir.

Sistemde başlatılmış süreçlerin rapor ekranlarında, kaynaktan gelen tablo yapısındaki verilerin seçimi ve form üzerinde gösterilmesinde, satır bazlı işlemler yapılmasında veya farklı bir forma girilen verilerin tablo yapısı şeklinde gösterilmesi gibi birçok işlemin gerçekleştirilmesinde bu nesneden yararlanılır.

Geliştirme arayüzünde aktif ekran form iken, Araç Kutusu panelinde form nesneleri listelenir. Nesne, araç kutusu panelinden sürükle/bırak yöntemi ile forma eklenir.

![DataGrid](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbac431f7-649e-4937-b164-066e62a3d390)

![DataGrid](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb21f2d5e-6a98-4a0d-85df-31e3e3f11fed)

Nesnenin üzerine tıklandığında Özellik Görüntüleyici panelinde **“Genel”** ve **“Olaylar”** sekmeleri yer alır ve nesneye ait özellikler görüntülenip, düzenlenebilir. Nesne özelliklerinin aktarıldığı kalıtım şeması aşağıdaki gibidir;

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

### Datasource

`Type` - Nesneye hangi tipte veri ekleneceğinin seçimi bu alandan yapılır. Tip alanında “Dinamik” ve “İlişkili” olarak iki seçenek listelenir. Seçim yapılan tipe göre veri kaynağı bölümünde görünen özellikler değişiklik gösterecektir.

>Yapılabilecek Seçimler : Dinamik, İlişkili

<div style={{textAlign: 'center'}}>

![DataGrid](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload082fae9d-e7d3-4c21-896e-95d350eca222)

</div>

Seçenek olarak **“Dinamik”** seçildiğinde; Datasource alanında projede tanımlı bir sorgu seçildiğinde nesneye veriler, bir veri kaynağından dinamik olarak yüklenebilir veya Datasource alanında seçim yapılmazsa ve nesnede Show Add Button özelliği aktif edilirse nesneye manuel olarak veri eklenebilir.

<div style={{textAlign: 'center'}}>

![DataGrid](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc42fe828-b35d-4747-b0f1-ce7651ff8f08)

</div>

Seçenek olarak **“İlişkili”** seçildiğinde; nesne ile sistemdeki herhangi bir form ilişkilendirilecek demektir.

İlişkilendirilen formun üzerindeki nesnelere girilen değerler, DataGrid nesnesinde kolon olarak gösterilir. İlişkili seçeneği seçildiğinde, nesne özelliklerindeki **Columns** alanına, **“Doküman Kimliği”** ve **“Düzenle”** isimli iki adet kolon otomatik gelecektir. Yine nesne özelliklerinde bulunan **Toolbar Buttons** alanına da **“CREATERELATIONDOCUMENT”** isimli buton kaydı otomatik olarak eklenecektir.

`DataSource` - Nesnede, bir veri kaynağından gelen değerleri listeleyebilmek için kullanılacak alandır. Projede Çözüm Gezgini alanındaki DataSource bölümüne eklenmiş ve başarıyla derlenen veri kaynağı tanımı, nesnenin Datasource) kısmından seçilebilir olur.

<div style={{textAlign: 'center'}}>

![DataGrid](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload526dccf8-7383-463d-a340-3a99f96679ea)

</div>

<div style={{textAlign: 'center'}}>

![DataGrid](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload52847aa4-3443-4082-9cd6-4e3f056515d9)

</div>

`RunAtServer` - Bu seçenek nesneye bağlanan sorgunun, sunucudan mı istemciden mi çalıştırılacağının belirlendiği seçenektir.

Bu seçenek aktif edilirse web arayüzünde forma tıklandığında, form açılmadan önce sorgu, sunucu tarafında çalıştırılır, form açıldığında nesneye sorgu sonucu yüklenmiş olarak gelir. Seçenek pasif yapıldığında web arayüzünde forma tıklandığında, form açıldıktan sonra nesneye sorgunun sonuç değerleri yüklenmeye başlar.

Sorgu sonucunun yüklenmesi için geçen bekleme süresi, bu özellik aktifken formun açılma anında, özellik pasifken form hızlı açıldıktan sonra nesneye verinin yüklenmesi anında etkili olur.

### Appearance

`Visible` - Nesnenin gizlenip, görünür yapılma ayarlarının gerçekleştirildiği kısımdır. Bu alan aktifken, nesne form üzerinde görünür durumdadır. Alan pasif yapıldığında nesne görünmez olur.

`Client Visible` - Form ilk açıldığında nesne görünmesin, belirli bir şart sağlandığında nesne görünür olsun gibi bir işlem yapılmak istendiğinde, nesnenin istemci tarafında görünmez olması için bu alan pasif yapılır. Kodla ya da Kural Yöneticisi ile belirlenen şart sağlandığında nesne tekrar görünür hale getirilebilir. Sunucu görünürlüğü aktif değilken, istemci müdahale edemez ancak istemci görünürlüğü aktif değilken sunucu müdahale edebilir.

`Enabled` - Nesnenin etkin modu bu alandan ayarlanır. Bu özellik aktifken nesneye veri girişi sağlanabilir ve nesne düzenlenebilir. Özellik pasifken, nesne düzenlenemez moddadır ve pasif görünür.

`Client Enabled` - Form ilk açıldığında nesne etkin olmasın, belirli bir şart sağlandığında etkin olsun gibi bir işlem yapılmak istendiğinde, nesnenin istemci tarafında etkin olmaması için bu alan pasif yapılır. Kodla ya da Kural Yöneticisi ile belirlenen şart sağlandığında nesne tekrar etkin hale getirilebilir. Sunucu etkinliği aktif değilken, istemci müdahale edemez ancak istemci etkinliği aktif değilken sunucu müdahale edebilir.

`Background Color` - Nesneye arka plan rengi vermek için kullanılan alandır.

`Title` - Form arayüzde açıkken imleç ile nesne üzerine gelindiğinde, bu alanda yazılan metin, ipucu olarak gösterilir. Nesne ile ilgili detay bilgi verilmek istendiğinde kullanılan, uç kullanıcıyı yönlendirme amaçlı bir özelliktir.

`ContextMenu` - Forma eklenmiş ContextMenu nesnesinin seçildiği alandır.

`ContextMenuTarget` - ContextMenu alanında seçili ögenin, nesnenin hangi bölümüne tıklandığında çalışacağının belirlendiği alandır. Container seçimi yapıldığında nesne içeriğinin bulunduğu alan boyutunca fare ile sağ tıklandığında ContextMenu içeriği açılırken, alanda Row seçimi yapıldığında, nesnedeki ögelerde fare ile sağ tıklandığında tanımlanan ContextMenu açılır.

`ClassName` - Forma ait CSS dosyası içinde yazılmış bir class'ın tanımlanarak nesne görünürlüğünün değiştirilebildiği alandır.

`Columns` - Nesne sütunlarının belirlendiği ve düzenlendiği alandır. Sütunlar kısmına tıklandığında tablo sütunlarının belirleneceği ve düzenleneceği pencere açılır. Bu pencerede “+ Ekle” butonu ile tabloya manuel kolonlar eklenebilir. “Kolonları Üret” butonu ile, nesneye bağlanan sorgudan dönen kolonlar direkt olarak bu alana eklenir.

<div style={{textAlign: 'center'}}>

![DataGrid](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf813f18e-da8d-406c-8ca5-a9eb0fb1ae29)

</div>

Eklenmiş kolonlardan herhangi birine tıklandığında, sağ tarafta o kolona ait özellikler listelenir. Kolon özellikleri düzenlenebilir veya tabloda ilgili kolon gösterilmek istenmiyorsa kolonun yanındaki dikey üç nokta ikonuna tıklanarak “Eklenmiş Kolonlar” alanından kaldırılabilir.

:::tip BİLGİ

Text türündeki kolonda, metin tipinde veri tutuluyor demektir. Hücre tipi Text iken, Kontrol sekmesinde kolonun, veri tabanında tutulacak alanının isim, boyut ve nullable özelliklerinin belirleneceği alanlar açılır.

:::

<details>
  <summary>Text türünde kolon özellikleri için tıklayın</summary>
  <div>

![DataGrid](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb35d83d9-ef4c-41d0-b9a4-4e19ed3f212c)

**General**

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Name 	| Kolon adı alanıdır. Kolon, “Ekle” butonu ile manuel oluşturulduysa bu alan düzenlenebilir olarak gelir. Kolon, “Kolonları Üret” butonu ile bu alana eklenmiş, sorgudan dönen bir kolonsa bu alan salt okunur yapıdadır. 	|
| Caption 	| Kolon başlığı alanıdır. Tabloda gösterilmek istenen sütun adı buradan ayarlanır. 	|
| Width 	| Kolon genişliğinin ayarlandığı alandır. 	|
| Visible 	| Kolonun web arayüzde görünüp görünmeyeceğinin ayarlandığı kısımdır. 	|
| Disable to Export 	| Tablo dışa aktarıldığında, özelliğin aktif edildiği kolonun aktarılmasını önlemek için kullanılan ayardır. 	|
| Allow Hiding 	| Kolonun Sütun Seçici paneline (Show Column Chooser aktif edildiğinde gösterilen panel) eklenerek kullanıcı tarafından gizlenmesini sağlayan ayardır. 	|
| Cell Type 	| Kolon tipi değeri bu alanda tutulur. Kolon, “Kolonları Üret” butonu ile bu alana eklenmiş, sorgudan dönen bir kolonsa bu alan salt okunur yapıdadır. “Ekle” butonu ile manuel oluşturulmuş bir kolonsa bu alan düzenlenebilir moddadır. Hücre Tipi alanında listelenen seçenekler Ekle butonu içindeki seçenekler ile aynıdır. 	|
| Align 	| Kolonu sağa, sola veya ortaya hizalama ayarı bu alandan yapılır. 	|
| Allow Null 	| Kolonda veri eklenmesi zorunlu olup olmadığının ayarlandığı özelliktir. Alan aktif edildiğinde kolona veri girişi yapılmadan satır kaydedilmemektedir. 	|
| Icon Source Field 	| Kolonda, kendisine veya farklı bir kolondaki veriye göre karşılaştırma yapılıp eşleşme olduğunda hücredeki verinin yanında ikon gösterilmesi için kullanılan alandır. 	|
| Icon Matchers 	| Icon Source Field alanında kolon seçimi yapıldığında görünür duruma geçer. Seçilen kolondaki bulunan/bulunabilecek değerlere göre hangi ikonların gösterileceği tanımlanır.<br/>Örneğin Icon Source Field'da kolonun kendisi seçilip Matchers alanında kolonda bulunan bir değer girilip değere uygun ikon seçildiğinde, web ara yüzünde kolonda matchers'a yazılan değer bulunduğunda tanımlanan ikon ile gösterilecektir. 	|
| Headet Filter Enabled 	| Kolonda Header Filter (başlık filtresi) aktif edilmesinin ayarlandığı özelliktir. **Kolonda ve nesnedeki Header Filter Enabled özelliği aktif** ise başlık filteresi görünür olur. 	|
| Is Primary Key 	| Eklenmiş kolonlar alanında bulunan kolonlardan en az biri birincil anahtar olarak seçilmelidir. Kayıtlar için benzersiz değer taşıyan kolon, birincil anahtar olarak işaretlenir. Eklenmiş kolonlar arasında benzersiz kolon bulunmuyorsa, “Ekle” butonu ile Number tipte bir kolon eklenip, otomatik artış özelliği aktif edilerek, her kayıt için benzersiz numara kolonu oluşturulup, bu kolon birincil anahtar olarak belirlenebilir. 	|
| Editing Enabled 	| Kolonun düzenlenebilip düzenlenemeyeceği buradan ayarlanır. Nesnede Type:İlişkili seçili ise kolonda yapılan değişiklik tanımlı formdaki alanlardaki veriyi değiştirmemektedir. 	|

**Control**

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Field Name 	| Sistemin veri tabanında, alan için oluşturacağı SQL kolon adının belirlendiği alandır. 	|
| Allow Null 	| Kolon için oluşturulacak veri tabanı alanının boş(null) değerlere izin verip vermeyeceği bu kısımdan belirtilir. 	|
| Size 	| Kolonun veri tabanı üzerinde tutacağı boyut bu alanda belirlenir. 	|

  </div>
</details>

:::tip BİLGİ

Number türündeki kolonda number tipinde bir değer tutulacaksa bu hücre tipi seçilir. Number tipli kolon için Genel sekmesinde, **“Toplam“**, **“Maksimum“**, **“Minimum“**, **“Ortalama”** ve **“Sayı”** seçeneklerinin listelendiği Summary Types alanı ve kolon değerinin otomatik artıp artmayacağının belirleneceği **Auto Increment** alanı görünür olur.

:::

<details>
  <summary>Number türünde kolon özellikleri için tıklayın</summary>
  <div>

![DataGrid](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc86165c-ba13-49a0-bc9a-7ae907e49e70)

**General**

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Name 	| Kolon adı alanıdır. Kolon, “Ekle” butonu ile manuel oluşturulduysa bu alan düzenlenebilir olarak gelir. Kolon, “Kolonları Üret” butonu ile bu alana eklenmiş, sorgudan dönen bir kolonsa bu alan salt okunur yapıdadır. 	|
| Caption 	| Kolon başlığı alanıdır. Tabloda gösterilmek istenen sütun adı buradan ayarlanır. 	|
| Width 	| Kolon genişliğinin ayarlandığı alandır. 	|
| Visible 	| Kolonun web arayüzde görünüp görünmeyeceğinin ayarlandığı kısımdır. 	|
| Disable to Export 	| Tablo dışa aktarıldığında, özelliğin aktif edildiği kolonun aktarılmasını önlemek için kullanılan ayardır. 	|
| Allow Hiding 	| Kolonun Sütun Seçici paneline (Show Column Chooser aktif edildiğinde gösterilen panel) eklenerek kullanıcı tarafından gizlenmesini sağlayan ayardır. 	|
| Cell Type 	| Kolon tipi değeri bu alanda tutulur. Kolon, “Kolonları Üret” butonu ile bu alana eklenmiş, sorgudan dönen bir kolonsa bu alan salt okunur yapıdadır. “Ekle” butonu ile manuel oluşturulmuş bir kolonsa bu alan düzenlenebilir moddadır. Hücre Tipi alanında listelenen seçenekler aşağıdaki gibidir; 	|
| Align 	| Kolonu sağa, sola veya ortaya hizalama ayarı bu alandan yapılır. 	|
| Allow Null 	| Kolonda veri eklenmesi zorunlu olup olmadığının ayarlandığı özelliktir. Alan aktif edildiğinde kolona veri girişi yapılmadan satır kaydedilmemektedir. 	|
| Icon Source Field 	| Kolonda, kendisine veya farklı bir kolondaki veriye göre karşılaştırma yapılıp eşleşme olduğunda hücredeki verinin yanında ikon gösterilmesi için kullanılan alandır. 	|
| Icon Matchers 	| Icon Source Field alanında kolon seçimi yapıldığında görünür duruma geçer. Seçilen kolondaki bulunan/bulunabilecek değerlere göre hangi ikonların gösterileceği tanımlanır.<br/>Örneğin Icon Source Field'da kolonun kendisi seçilip Matchers alanında kolonda bulunan bir değer girilip değere uygun ikon seçildiğinde, web ara yüzünde kolonda matchers'a yazılan değer bulunduğunda tanımlanan ikon ile gösterilecektir. 	|
| Headet Filter Enabled 	| Kolonda Header Filter (başlık filtresi) aktif edilmesinin ayarlandığı özelliktir. **Kolonda ve nesnedeki Header Filter Enabled özelliği aktif** ise başlık filteresi görünür olur. 	|
| Formula 	| Kolon içindeki değerin formdaki alanlar, istatistik ve trigonometri fonksiyonları, operatörler kullanılarak bir formül ile hesaplanmasını sağlayan alandır. Alan içinde formül yazılıp kaydedilerek hesaplatma yaptırılır. 	|
| Is Primary Key 	| Eklenmiş kolonlar alanında bulunan kolonlardan en az biri birincil anahtar olarak seçilmelidir. Kayıtlar için benzersiz değer taşıyan kolon, birincil anahtar olarak işaretlenir. Eklenmiş kolonlar arasında benzersiz kolon bulunmuyorsa, “Ekle” butonu ile Number tipte bir kolon eklenip, otomatik artış özelliği aktif edilerek, her kayıt için benzersiz numara kolonu oluşturulup, bu kolon birincil anahtar olarak belirlenebilir. 	|
| Editing Enabled 	| Kolonun düzenlenebilip düzenlenemeyeceği buradan ayarlanır. Nesnede Type:İlişkili seçili ise kolonda yapılan değişiklik tanımlı formdaki alanlardaki veriyi değiştirmemektedir. 	|
| Summary Types 	| Alanda seçilen işlem tanımları (Sum, Max, Min, Avg, Count) web arayüzde kolonun altında belirerek, ilgili kolondaki sayısal değerlerin işlem sonuçlarını gösterilir. 	|
| Auto Increment 	| Kolon değerinin otomatik artıp artmayacağının belirlenmesi için kullanılır. 	|
| Precision 	| Virgülden sonra kaç karakter olacağının belirlendiği alandır. Virgülden sonra yazılan değeri aşağı ya da yukarı yuvarlayarak verilen karakter sayısına göre otomatik düzenler. 	|

**Control**

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Field Name 	| Sistemin veri tabanında, alan için oluşturacağı SQL kolon adının belirlendiği alandır. 	|
| Allow Null 	| Kolon için oluşturulacak veri tabanı alanının boş(null) değerlere izin verip vermeyeceği bu kısımdan belirtilir. 	|
| Size 	| Kolonun veri tabanı alanında tutacağı boyut bu alanda belirlenir. Size ve Precision alanındaki değerlere göre SQL'de kolon büyüklüğü oluşturulur. 	|
| Precision 	| Kolonun veri tabanı alanında tutacağı boyut bu alanda belirlenir. Size ve Precision alanındaki değerlere göre SQL'de kolon büyüklüğü oluşturulur. 	|

  </div>
</details>

:::tip BİLGİ

Boolean türünde kolonda doğru / yanlış tipinde değer tutuluyor demektir.

:::

<details>
  <summary>Boolean türünde kolon özellikleri için tıklayın</summary>
  <div>

**General**

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Name 	| Kolon adı alanıdır. Kolon, “Ekle” butonu ile manuel oluşturulduysa bu alan düzenlenebilir olarak gelir. Kolon, “Kolonları Üret” butonu ile bu alana eklenmiş, sorgudan dönen bir kolonsa bu alan salt okunur yapıdadır. 	|
| Caption 	| Kolon başlığı alanıdır. Tabloda gösterilmek istenen sütun adı buradan ayarlanır. 	|
| Width 	| Kolon genişliğinin ayarlandığı alandır. 	|
| Visible 	| Kolonun web arayüzde görünüp görünmeyeceğinin ayarlandığı kısımdır. 	|
| Disable to Export 	| Tablo dışa aktarıldığında, özelliğin aktif edildiği kolonun aktarılmasını önlemek için kullanılan ayardır. 	|
| Allow Hiding 	| Kolonun Sütun Seçici paneline (Show Column Chooser aktif edildiğinde gösterilen panel) eklenerek kullanıcı tarafından gizlenmesini sağlayan ayardır. 	|
| Cell Type 	| Kolon tipi değeri bu alanda tutulur. Kolon, “Kolonları Üret” butonu ile bu alana eklenmiş, sorgudan dönen bir kolonsa bu alan salt okunur yapıdadır. “Ekle” butonu ile manuel oluşturulmuş bir kolonsa bu alan düzenlenebilir moddadır. Hücre Tipi alanında listelenen seçenekler Ekle butonu içindeki seçenekler ile aynıdır. 	|
| Align 	| Kolonu sağa, sola veya ortaya hizalama ayarı bu alandan yapılır. 	|
| Allow Null 	| Kolonda veri eklenmesi zorunlu olup olmadığının ayarlandığı özelliktir. Alan aktif edildiğinde kolona veri girişi yapılmadan satır kaydedilmemektedir. 	|
| Icon Source Field 	| Kolonda, kendisine veya farklı bir kolondaki veriye göre karşılaştırma yapılıp eşleşme olduğunda hücredeki verinin yanında ikon gösterilmesi için kullanılan alandır. 	|
| Icon Matchers 	| Icon Source Field alanında kolon seçimi yapıldığında görünür duruma geçer. Seçilen kolondaki bulunan/bulunabilecek değerlere göre hangi ikonların gösterileceği tanımlanır.<br/>Örneğin Icon Source Field'da kolonun kendisi seçilip Matchers alanında kolonda bulunan bir değer girilip değere uygun ikon seçildiğinde, web ara yüzünde kolonda matchers'a yazılan değer bulunduğunda tanımlanan ikon ile gösterilecektir. 	|
| Headet Filter Enabled 	| Kolonda Header Filter (başlık filtresi) aktif edilmesinin ayarlandığı özelliktir. **Kolonda ve nesnedeki Header Filter Enabled özelliği aktif** ise başlık filteresi görünür olur. 	|
| Is Primary Key 	| Eklenmiş kolonlar alanında bulunan kolonlardan en az biri birincil anahtar olarak seçilmelidir. Kayıtlar için benzersiz değer taşıyan kolon, birincil anahtar olarak işaretlenir. Eklenmiş kolonlar arasında benzersiz kolon bulunmuyorsa, “Ekle” butonu ile Number tipte bir kolon eklenip, otomatik artış özelliği aktif edilerek, her kayıt için benzersiz numara kolonu oluşturulup, bu kolon birincil anahtar olarak belirlenebilir. 	|
| Editing Enabled 	| Kolonun düzenlenebilip düzenlenemeyeceği buradan ayarlanır. Nesnede Type:İlişkili seçili ise kolonda yapılan değişiklik tanımlı formdaki alanlardaki veriyi değiştirmemektedir. 	|

**Control**

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Field Name 	| Sistemin veri tabanında, alan için oluşturacağı SQL kolon adının belirlendiği alandır. 	|
| Allow Null 	| Kolon için oluşturulacak veri tabanı alanının boş(null) değerlere izin verip vermeyeceği bu kısımdan belirtilir. 	|

  </div>
</details>

:::tip BİLGİ

Date türünde kolon içinde tarih tipinde veri barındıran kolonların hücre tipi değeridir.

:::

<details>
  <summary>Date türünde kolon özellikleri için tıklayın</summary>
  <div>

**General**

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Name 	| Kolon adı alanıdır. Kolon, “Ekle” butonu ile manuel oluşturulduysa bu alan düzenlenebilir olarak gelir. Kolon, “Kolonları Üret” butonu ile bu alana eklenmiş, sorgudan dönen bir kolonsa bu alan salt okunur yapıdadır. 	|
| Caption 	| Kolon başlığı alanıdır. Tabloda gösterilmek istenen sütun adı buradan ayarlanır. 	|
| Width 	| Kolon genişliğinin ayarlandığı alandır. 	|
| Visible 	| Kolonun web arayüzde görünüp görünmeyeceğinin ayarlandığı kısımdır. 	|
| Disable to Export 	| Tablo dışa aktarıldığında, özelliğin aktif edildiği kolonun aktarılmasını önlemek için kullanılan ayardır. 	|
| Allow Hiding 	| Kolonun Sütun Seçici paneline (Show Column Chooser aktif edildiğinde gösterilen panel) eklenerek kullanıcı tarafından gizlenmesini sağlayan ayardır. 	|
| Cell Type 	| Kolon tipi değeri bu alanda tutulur. Kolon, “Kolonları Üret” butonu ile bu alana eklenmiş, sorgudan dönen bir kolonsa bu alan salt okunur yapıdadır. “Ekle” butonu ile manuel oluşturulmuş bir kolonsa bu alan düzenlenebilir moddadır. Hücre Tipi alanında listelenen seçenekler aşağıdaki gibidir; 	|
| Align 	| Kolonu sağa, sola veya ortaya hizalama ayarı bu alandan yapılır. 	|
| Allow Null 	| Kolonda veri eklenmesi zorunlu olup olmadığının ayarlandığı özelliktir. Alan aktif edildiğinde kolona veri girişi yapılmadan satır kaydedilmemektedir. 	|
| Icon Source Field 	| Kolonda, kendisine veya farklı bir kolondaki veriye göre karşılaştırma yapılıp eşleşme olduğunda hücredeki verinin yanında ikon gösterilmesi için kullanılan alandır. 	|
| Icon Matchers 	| Icon Source Field alanında kolon seçimi yapıldığında görünür duruma geçer. Seçilen kolondaki bulunan/bulunabilecek değerlere göre hangi ikonların gösterileceği tanımlanır.<br/>Örneğin Icon Source Field'da kolonun kendisi seçilip Matchers alanında kolonda bulunan bir değer girilip değere uygun ikon seçildiğinde, web ara yüzünde kolonda matchers'a yazılan değer bulunduğunda tanımlanan ikon ile gösterilecektir. 	|
| Format 	| Tarih ve saat gösterim formatının belirlendiği alandır. Varsayılan olarak tarih formatı: “YYYY-MM-DD”, tarih ve saat formatı: “YYYY-MM-DD HH:mm” şeklinde tanımlıdır. Gösterilmek istenen farklı format yapıları bu alanda belirtilebilir. 	|
| Is Primary Key 	| Eklenmiş kolonlar alanında bulunan kolonlardan en az biri birincil anahtar olarak seçilmelidir. Kayıtlar için benzersiz değer taşıyan kolon, birincil anahtar olarak işaretlenir. Eklenmiş kolonlar arasında benzersiz kolon bulunmuyorsa, “Ekle” butonu ile Number tipte bir kolon eklenip, otomatik artış özelliği aktif edilerek, her kayıt için benzersiz numara kolonu oluşturulup, bu kolon birincil anahtar olarak belirlenebilir. 	|
| Editing Enabled 	| Kolonun düzenlenebilip düzenlenemeyeceği buradan ayarlanır. Nesnede Type:İlişkili seçili ise kolonda yapılan değişiklik tanımlı formdaki alanlardaki veriyi değiştirmemektedir. 	|
| Precision 	| Virgülden sonra kaç karakter olacağının belirlendiği alandır. Virgülden sonra yazılan değeri aşağı ya da yukarı yuvarlayarak verilen karakter sayısına göre otomatik düzenler. 	|

**Control**

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Field Name 	| Sistemin veri tabanında, alan için oluşturacağı SQL kolon adının belirlendiği alandır. 	|
| Allow Null 	| Kolon için oluşturulacak veri tabanı alanının boş(null) değerlere izin verip vermeyeceği bu kısımdan belirtilir. 	|

  </div>
</details>

:::tip BİLGİ

Time türünde kolon içinde saat tipinde veri barındıran kolonların hücre tipi değeridir.

:::

<details>
  <summary>Time türünde kolon özellikleri için tıklayın</summary>
  <div>

**General**

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Name 	| Kolon adı alanıdır. Kolon, “Ekle” butonu ile manuel oluşturulduysa bu alan düzenlenebilir olarak gelir. Kolon, “Kolonları Üret” butonu ile bu alana eklenmiş, sorgudan dönen bir kolonsa bu alan salt okunur yapıdadır. 	|
| Caption 	| Kolon başlığı alanıdır. Tabloda gösterilmek istenen sütun adı buradan ayarlanır. 	|
| Width 	| Kolon genişliğinin ayarlandığı alandır. 	|
| Visible 	| Kolonun web arayüzde görünüp görünmeyeceğinin ayarlandığı kısımdır. 	|
| Disable to Export 	| Tablo dışa aktarıldığında, özelliğin aktif edildiği kolonun aktarılmasını önlemek için kullanılan ayardır. 	|
| Allow Hiding 	| Kolonun Sütun Seçici paneline (Show Column Chooser aktif edildiğinde gösterilen panel) eklenerek kullanıcı tarafından gizlenmesini sağlayan ayardır. 	|
| Cell Type 	| Kolon tipi değeri bu alanda tutulur. Kolon, “Kolonları Üret” butonu ile bu alana eklenmiş, sorgudan dönen bir kolonsa bu alan salt okunur yapıdadır. “Ekle” butonu ile manuel oluşturulmuş bir kolonsa bu alan düzenlenebilir moddadır. Hücre Tipi alanında listelenen seçenekler aşağıdaki gibidir; 	|
| Align 	| Kolonu sağa, sola veya ortaya hizalama ayarı bu alandan yapılır. 	|
| Allow Null 	| Kolonda veri eklenmesi zorunlu olup olmadığının ayarlandığı özelliktir. Alan aktif edildiğinde kolona veri girişi yapılmadan satır kaydedilmemektedir. 	|
| Icon Source Field 	| Kolonda, kendisine veya farklı bir kolondaki veriye göre karşılaştırma yapılıp eşleşme olduğunda hücredeki verinin yanında ikon gösterilmesi için kullanılan alandır. 	|
| Icon Matchers 	| Icon Source Field alanında kolon seçimi yapıldığında görünür duruma geçer. Seçilen kolondaki bulunan/bulunabilecek değerlere göre hangi ikonların gösterileceği tanımlanır.<br/>Örneğin Icon Source Field'da kolonun kendisi seçilip Matchers alanında kolonda bulunan bir değer girilip değere uygun ikon seçildiğinde, web ara yüzünde kolonda matchers'a yazılan değer bulunduğunda tanımlanan ikon ile gösterilecektir. 	|
| Format 	| Tarih ve saat gösterim formatının belirlendiği alandır. Varsayılan olarak saat formatı: “HH:mm”, saat ve saniye formatı: “HH:mm:ss” şeklinde tanımlıdır. Gösterilmek istenen farklı format yapıları bu alanda belirtilebilir. 	|
| Is Primary Key 	| Eklenmiş kolonlar alanında bulunan kolonlardan en az biri birincil anahtar olarak seçilmelidir. Kayıtlar için benzersiz değer taşıyan kolon, birincil anahtar olarak işaretlenir. Eklenmiş kolonlar arasında benzersiz kolon bulunmuyorsa, “Ekle” butonu ile Number tipte bir kolon eklenip, otomatik artış özelliği aktif edilerek, her kayıt için benzersiz numara kolonu oluşturulup, bu kolon birincil anahtar olarak belirlenebilir. 	|
| Editing Enabled 	| Kolonun düzenlenebilip düzenlenemeyeceği buradan ayarlanır. Nesnede Type:İlişkili seçili ise kolonda yapılan değişiklik tanımlı formdaki alanlardaki veriyi değiştirmemektedir. 	|
| Precision 	| Virgülden sonra kaç karakter olacağının belirlendiği alandır. Virgülden sonra yazılan değeri aşağı ya da yukarı yuvarlayarak verilen karakter sayısına göre otomatik düzenler. 	|

**Control**

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Field Name 	| Sistemin veri tabanında, alan için oluşturacağı SQL kolon adının belirlendiği alandır. 	|
| Allow Null 	| Kolon için oluşturulacak veri tabanı alanının boş(null) değerlere izin verip vermeyeceği bu kısımdan belirtilir. 	|

  </div>
</details>

:::tip BİLGİ

DateTime türünde kolon içinde tarih ve saat tipinde veri barındıran kolonların hücre tipi değeridir.

:::

<details>
  <summary>DateTime türünde kolon özellikleri için tıklayın</summary>
  <div>

**General**

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Name 	| Kolon adı alanıdır. Kolon, “Ekle” butonu ile manuel oluşturulduysa bu alan düzenlenebilir olarak gelir. Kolon, “Kolonları Üret” butonu ile bu alana eklenmiş, sorgudan dönen bir kolonsa bu alan salt okunur yapıdadır. 	|
| Caption 	| Kolon başlığı alanıdır. Tabloda gösterilmek istenen sütun adı buradan ayarlanır. 	|
| Width 	| Kolon genişliğinin ayarlandığı alandır. 	|
| Visible 	| Kolonun web arayüzde görünüp görünmeyeceğinin ayarlandığı kısımdır. 	|
| Disable to Export 	| Tablo dışa aktarıldığında, özelliğin aktif edildiği kolonun aktarılmasını önlemek için kullanılan ayardır. 	|
| Allow Hiding 	| Kolonun Sütun Seçici paneline (Show Column Chooser aktif edildiğinde gösterilen panel) eklenerek kullanıcı tarafından gizlenmesini sağlayan ayardır. 	|
| Cell Type 	| Kolon tipi değeri bu alanda tutulur. Kolon, “Kolonları Üret” butonu ile bu alana eklenmiş, sorgudan dönen bir kolonsa bu alan salt okunur yapıdadır. “Ekle” butonu ile manuel oluşturulmuş bir kolonsa bu alan düzenlenebilir moddadır. Hücre Tipi alanında listelenen seçenekler aşağıdaki gibidir; 	|
| Align 	| Kolonu sağa, sola veya ortaya hizalama ayarı bu alandan yapılır. 	|
| Allow Null 	| Kolonda veri eklenmesi zorunlu olup olmadığının ayarlandığı özelliktir. Alan aktif edildiğinde kolona veri girişi yapılmadan satır kaydedilmemektedir. 	|
| Icon Source Field 	| Kolonda, kendisine veya farklı bir kolondaki veriye göre karşılaştırma yapılıp eşleşme olduğunda hücredeki verinin yanında ikon gösterilmesi için kullanılan alandır. 	|
| Icon Matchers 	| Icon Source Field alanında kolon seçimi yapıldığında görünür duruma geçer. Seçilen kolondaki bulunan/bulunabilecek değerlere göre hangi ikonların gösterileceği tanımlanır.<br/>Örneğin Icon Source Field'da kolonun kendisi seçilip Matchers alanında kolonda bulunan bir değer girilip değere uygun ikon seçildiğinde, web ara yüzünde kolonda matchers'a yazılan değer bulunduğunda tanımlanan ikon ile gösterilecektir. 	|
| Format 	| Tarih ve saat gösterim formatının belirlendiği alandır. Varsayılan olarak tarih formatı: “YYYY-MM-DD”, tarih ve saat formatı: “YYYY-MM-DD HH:mm” şeklinde tanımlıdır. Gösterilmek istenen farklı format yapıları bu alanda belirtilebilir. 	|
| Is Primary Key 	| Eklenmiş kolonlar alanında bulunan kolonlardan en az biri birincil anahtar olarak seçilmelidir. Kayıtlar için benzersiz değer taşıyan kolon, birincil anahtar olarak işaretlenir. Eklenmiş kolonlar arasında benzersiz kolon bulunmuyorsa, “Ekle” butonu ile Number tipte bir kolon eklenip, otomatik artış özelliği aktif edilerek, her kayıt için benzersiz numara kolonu oluşturulup, bu kolon birincil anahtar olarak belirlenebilir. 	|
| Editing Enabled 	| Kolonun düzenlenebilip düzenlenemeyeceği buradan ayarlanır. Nesnede Type:İlişkili seçili ise kolonda yapılan değişiklik tanımlı formdaki alanlardaki veriyi değiştirmemektedir. 	|
| Precision 	| Virgülden sonra kaç karakter olacağının belirlendiği alandır. Virgülden sonra yazılan değeri aşağı ya da yukarı yuvarlayarak verilen karakter sayısına göre otomatik düzenler. 	|

**Control**

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Field Name 	| Sistemin veri tabanında, alan için oluşturacağı SQL kolon adının belirlendiği alandır. 	|
| Allow Null 	| Kolon için oluşturulacak veri tabanı alanının boş(null) değerlere izin verip vermeyeceği bu kısımdan belirtilir. 	|

  </div>
</details>

:::tip BİLGİ

Select tipindeki bir kolonda, bir veri kaynağından gelen veriler veya manuel eklenen elemanlar listelenebilir. Web arayüzünde kullanıcı, Select kolonuna tıkladığında listelenen değerlerden seçim yapabilir.

:::

<details>
  <summary>Select türünde kolon özellikleri için tıklayın</summary>
  <div>

![DataGrid](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade33be543-85e3-4aab-bce5-a95f00a8a75e)

**General**

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Name 	| Kolon adı alanıdır. Kolon, “Ekle” butonu ile manuel oluşturulduysa bu alan düzenlenebilir olarak gelir. Kolon, “Kolonları Üret” butonu ile bu alana eklenmiş, sorgudan dönen bir kolonsa bu alan salt okunur yapıdadır. 	|
| Caption 	| Kolon başlığı alanıdır. Tabloda gösterilmek istenen sütun adı buradan ayarlanır. 	|
| Width 	| Kolon genişliğinin ayarlandığı alandır. 	|
| Visible 	| Kolonun web arayüzde görünüp görünmeyeceğinin ayarlandığı kısımdır. 	|
| Disable to Export 	| Tablo dışa aktarıldığında, özelliğin aktif edildiği kolonun aktarılmasını önlemek için kullanılan ayardır. 	|
| Allow Hiding 	| Kolonun Sütun Seçici paneline (Show Column Chooser aktif edildiğinde gösterilen panel) eklenerek kullanıcı tarafından gizlenmesini sağlayan ayardır. 	|
| Cell Type 	| Kolon tipi değeri bu alanda tutulur. Kolon, “Kolonları Üret” butonu ile bu alana eklenmiş, sorgudan dönen bir kolonsa bu alan salt okunur yapıdadır. “Ekle” butonu ile manuel oluşturulmuş bir kolonsa bu alan düzenlenebilir moddadır. Hücre Tipi alanında listelenen seçenekler Ekle butonu içindeki seçenekler ile aynıdır. 	|
| Align 	| Kolonu sağa, sola veya ortaya hizalama ayarı bu alandan yapılır. 	|
| Allow Null 	| Kolonda veri eklenmesi zorunlu olup olmadığının ayarlandığı özelliktir. Alan aktif edildiğinde kolona veri girişi yapılmadan satır kaydedilmemektedir. 	|
| Icon Source Field 	| Kolonda, kendisine veya farklı bir kolondaki veriye göre karşılaştırma yapılıp eşleşme olduğunda hücredeki verinin yanında ikon gösterilmesi için kullanılan alandır. 	|
| Icon Matchers 	| Icon Source Field alanında kolon seçimi yapıldığında görünür duruma geçer. Seçilen kolondaki bulunan/bulunabilecek değerlere göre hangi ikonların gösterileceği tanımlanır.<br/>Örneğin Icon Source Field'da kolonun kendisi seçilip Matchers alanında kolonda bulunan bir değer girilip değere uygun ikon seçildiğinde, web ara yüzünde kolonda matchers'a yazılan değer bulunduğunda tanımlanan ikon ile gösterilecektir. 	|
| Headet Filter Enabled 	| Kolonda Header Filter (başlık filtresi) aktif edilmesinin ayarlandığı özelliktir. **Kolonda ve nesnedeki Header Filter Enabled özelliği aktif** ise başlık filteresi görünür olur. 	|
| Is Primary Key 	| Eklenmiş kolonlar alanında bulunan kolonlardan en az biri birincil anahtar olarak seçilmelidir. Kayıtlar için benzersiz değer taşıyan kolon, birincil anahtar olarak işaretlenir. Eklenmiş kolonlar arasında benzersiz kolon bulunmuyorsa, “Ekle” butonu ile Number tipte bir kolon eklenip, otomatik artış özelliği aktif edilerek, her kayıt için benzersiz numara kolonu oluşturulup, bu kolon birincil anahtar olarak belirlenebilir. 	|
| Editing Enabled 	| Kolonun düzenlenebilip düzenlenemeyeceği buradan ayarlanır. Nesnede Type:İlişkili seçili ise kolonda yapılan değişiklik tanımlı formdaki alanlardaki veriyi değiştirmemektedir. 	|

**Control**

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Type 	| Kolonda hangi tipte veri ekleneceğinin seçimi bu alandan yapılır. Alanda "Dinamik" ve "Statik" olarak iki seçenek listelenir. Seçim yapılan tipe göre veri kaynağı bölümünde görünen özellikler değişiklik gösterecektir. **Type=Dinamik** seçildiğinde **DataSource, Run At Server, Value Expression, Display Expression ve Display Format** alanları gözükürken, **Type=Statik** seçilirse Items alanı gözükecektir. 	|
| Data Source 	| Type alanında **Dinamik** seçildiğinde görünür duruma geçer. Bir veri kaynağından gelen değerleri listeleyebilmek için kullanılacak alandır. Alanda Çözüm Gezgini alanındaki DataSource bölümüne eklenmiş ve başarıyla derlenen veri kaynağı tanımı, kolonun Datasource) kısmından seçilebilir olur. 	|
| Run At Server 	| Type alanında **Dinamik** seçildiğinde görünür duruma geçer. Kolona bağlanan sorgunun, sunucudan mı istemciden mi çalıştırılacağının belirlendiği seçenektir. 	|
| Value Expression 	| Type alanında **Dinamik** seçildiğinde görünür duruma geçer. Veri Kaynağı kısmından bir veri kaynağı tanımı seçildiğinde bu alan görünür olur. Seçilen veri kaynağından dönen tüm kolonlar bu alanda listelenir. Kullanıcı ara yüzden seçim yaptığında, seçilen ögenin değeri olarak ne ttuyapılan seçimin kayıt alanının hangi kolon değeri olacağı bu alanda belirlenir. 	|
| Display Expression 	| Type alanında **Dinamik** seçildiğinde görünür duruma geçer. Veri Kaynağı kısmından bir veri kaynağı tanımı seçildiğinde bu alan görünür olur. Seçilen veri kaynağından dönen tüm kolonlar bu alanda listelenir. Kullanıcı ara yüzden seçim yaptığında, kolon içerisinde görünecek ifadenin hangi sorgu kolonundan geleceği bu alanda belirlenir. 	|
| Display Format 	| Type alanında **Dinamik** seçildiğinde görünür duruma geçer. Display Expression alanından seçilen kolon ya da kolonlar otomatik olarak bu alana da eklenir. Nesnede listelenecek eleman metinlerine görünüm formatı belirlemek için kullanılan alandır. Elemanların istenen bir formatta gösterilmesi için, ilgili format yapısı bu alanda belirtilebilir. Nesne seçimi sonrası kolonda görüntülenecek değerin web arayüzde uç kullanıcılara belirlenen formatta görünmesi sağlanabilir. Formatlamada kullanılabilecek format tiplerine, alana odaklanıldığında çıkan bilgi mesajındaki linkten (https://shopify.github.io/liquid/) erişilebilir 	|
| Items 	| Type alanında **Statik** seçildiğinde görünür duruma geçer. Veri kaynağından gelen kayıtlar değil, geliştirme anında manuel eklenen elemanlar listelenmek istendiğinde, eleman tanımlama işlemi bu alandan yapılır. Items alanına tıklandığında eleman ekleme penceresi açılır. Ekle butonuna tıklanarak nesneye yeni eleman kalemleri oluşturulur. Girilen elemanın **Value** ve **Title** alanları doldurulur. Elemanın ikona sahip olması istenirse Icons alanı içindeki ikon kütüphanesinden seçim yapılabilir. Ögenin Selected alanı aktif edilirse web ara yüzünde nesne içinde bu öge otomatik olarak seçilmiş gibi gösterilecektir. "Kaydet" butonuna basılarak nesneye eleman ekleme işlemi tamamlanır. Web arayüzde nesneye tıklandığında, Elemanlar alanında belirlenen eleman kayıtları, kullanıcının seçim yapması için listelenir. 	|
| Field Name 	| Sistemin veri tabanında, alan için oluşturacağı SQL kolon adının belirlendiği alandır. 	|
| Allow Null 	| Kolon için oluşturulacak veri tabanı alanının boş(null) değerlere izin verip vermeyeceği bu kısımdan belirtilir. 	|

  </div>
</details>

:::tip BİLGİ

Multilanguage tipindeki bir kolonda, alanda verinin birden fazla dil karşılığının girişi sağlanır. Örneğin Türkçe olarak "X bölgesine gitmesi gerekiyor" ifadesininin İngilizce karşılığının da girilmesi gerekiyorsa nesneye MultiLanguagekolonu eklenerek, kolonda Türkçe bilgi girilip, kolon içinde çoklu dil girişi alanında "It has to go to X zone" diyerek tek kolon içinde veri girişi sağlanabilmektedir.

:::

<details>
  <summary>MultiLanguage türünde kolon özellikleri için tıklayın</summary>
  <div>

**General**

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Name 	| Kolon adı alanıdır. Kolon, “Ekle” butonu ile manuel oluşturulduysa bu alan düzenlenebilir olarak gelir. Kolon, “Kolonları Üret” butonu ile bu alana eklenmiş, sorgudan dönen bir kolonsa bu alan salt okunur yapıdadır. 	|
| Caption 	| Kolon başlığı alanıdır. Tabloda gösterilmek istenen sütun adı buradan ayarlanır. 	|
| Width 	| Kolon genişliğinin ayarlandığı alandır. 	|
| Visible 	| Kolonun web arayüzde görünüp görünmeyeceğinin ayarlandığı kısımdır. 	|
| Disable to Export 	| Tablo dışa aktarıldığında, özelliğin aktif edildiği kolonun aktarılmasını önlemek için kullanılan ayardır. 	|
| Allow Hiding 	| Kolonun Sütun Seçici paneline (Show Column Chooser aktif edildiğinde gösterilen panel) eklenerek kullanıcı tarafından gizlenmesini sağlayan ayardır. 	|
| Cell Type 	| Kolon tipi değeri bu alanda tutulur. Kolon, “Kolonları Üret” butonu ile bu alana eklenmiş, sorgudan dönen bir kolonsa bu alan salt okunur yapıdadır. “Ekle” butonu ile manuel oluşturulmuş bir kolonsa bu alan düzenlenebilir moddadır. Hücre Tipi alanında listelenen seçenekler Ekle butonu içindeki seçenekler ile aynıdır. 	|
| Align 	| Kolonu sağa, sola veya ortaya hizalama ayarı bu alandan yapılır. 	|
| Allow Null 	| Kolonda veri eklenmesi zorunlu olup olmadığının ayarlandığı özelliktir. Alan aktif edildiğinde kolona veri girişi yapılmadan satır kaydedilmemektedir. 	|
| Icon Source Field 	| Kolonda, kendisine veya farklı bir kolondaki veriye göre karşılaştırma yapılıp eşleşme olduğunda hücredeki verinin yanında ikon gösterilmesi için kullanılan alandır. 	|
| Icon Matchers 	| Icon Source Field alanında kolon seçimi yapıldığında görünür duruma geçer. Seçilen kolondaki bulunan/bulunabilecek değerlere göre hangi ikonların gösterileceği tanımlanır.<br/>Örneğin Icon Source Field'da kolonun kendisi seçilip Matchers alanında kolonda bulunan bir değer girilip değere uygun ikon seçildiğinde, web ara yüzünde kolonda matchers'a yazılan değer bulunduğunda tanımlanan ikon ile gösterilecektir. 	|
| Headet Filter Enabled 	| Kolonda Header Filter (başlık filtresi) aktif edilmesinin ayarlandığı özelliktir. **Kolonda ve nesnedeki Header Filter Enabled özelliği aktif** ise başlık filteresi görünür olur. 	|
| Is Primary Key 	| Eklenmiş kolonlar alanında bulunan kolonlardan en az biri birincil anahtar olarak seçilmelidir. Kayıtlar için benzersiz değer taşıyan kolon, birincil anahtar olarak işaretlenir. Eklenmiş kolonlar arasında benzersiz kolon bulunmuyorsa, “Ekle” butonu ile Number tipte bir kolon eklenip, otomatik artış özelliği aktif edilerek, her kayıt için benzersiz numara kolonu oluşturulup, bu kolon birincil anahtar olarak belirlenebilir. 	|
| Editing Enabled 	| Kolonun düzenlenebilip düzenlenemeyeceği buradan ayarlanır. Nesnede Type:İlişkili seçili ise kolonda yapılan değişiklik tanımlı formdaki alanlardaki veriyi değiştirmemektedir. 	|

**Control**

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Field Name 	| Sistemin veri tabanında, alan için oluşturacağı SQL kolon adının belirlendiği alandır. 	|
| Allow Null 	| Kolon için oluşturulacak veri tabanı alanının boş(null) değerlere izin verip vermeyeceği bu kısımdan belirtilir. 	|
| Size 	| Kolonun veri tabanı üzerinde tutacağı boyut bu alanda belirlenir. 	|

  </div>
</details>

:::tip BİLGİ

Action Button kolonu, tıklandığında belirli bir işlemi yapmak üzere tasarlanmış bir aksiyon butonu eklemeye yarayan hücre tipidir. Hücre tipi olarak Action Button seçildiğinde ekranda Aksiyon Butonu isimli bir sekme belirecektir. Web arayüzünde, kolondaki bu butona tıklandığında hangi işlemin yapılacağı aksiyon butonu sekmesinde belirtilir. 

DataGrid nesnesinde actionButton kolonu eklenerek, Button Properties sekmesindeki Type alanında seçilen buton türüne göre Open A Form, Open A Process, Create A Form, Start A Process, Open A Selection Form, Execute Custom Action işlemlerinin yapılması sağlanabilmektedir. Örneğin Type:İlişkili olan datagrid nesnesinde otomatik olarak Open A Form tipinde buton eklenerek, kullanıcının formu geri açabilmesi için buton eklenmektedir.

:::

***Her bir Action Button Tipi için buton tipine ait akordiyon menüyü açarak detayları görüntüleyebilirsiniz. Aşağıdaki tabloda her Action Buttondaki Genaral özellikleri ortak olduğu için tek seferde tanımlanmıştır.***

**General**

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Name 	| Kolon adı alanıdır. Kolon, “Ekle” butonu ile manuel oluşturulduysa bu alan düzenlenebilir olarak gelir. Kolon, “Kolonları Üret” butonu ile bu alana eklenmiş, sorgudan dönen bir kolonsa bu alan salt okunur yapıdadır. 	|
| Caption 	| Kolon başlığı alanıdır. Tabloda gösterilmek istenen sütun adı buradan ayarlanır. 	|
| Width 	| Kolon genişliğinin ayarlandığı alandır. 	|
| Visible 	| Kolonun web arayüzde görünüp görünmeyeceğinin ayarlandığı kısımdır. 	|
| Disable to Export 	| Tablo dışa aktarıldığında, özelliğin aktif edildiği kolonun aktarılmasını önlemek için kullanılan ayardır. 	|
| Allow Hiding 	| Kolonun Sütun Seçici paneline (Show Column Chooser aktif edildiğinde gösterilen panel) eklenerek kullanıcı tarafından gizlenmesini sağlayan ayardır. 	|
| Cell Type 	| Kolon tipi değeri bu alanda tutulur. Kolon, “Kolonları Üret” butonu ile bu alana eklenmiş, sorgudan dönen bir kolonsa bu alan salt okunur yapıdadır. “Ekle” butonu ile manuel oluşturulmuş bir kolonsa bu alan düzenlenebilir moddadır. Hücre Tipi alanında listelenen seçenekler Ekle butonu içindeki seçenekler ile aynıdır. 	|
| Align 	| Kolonu sağa, sola veya ortaya hizalama ayarı bu alandan yapılır. 	|

![DataGrid](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd3439391-5d34-4289-935d-426d7b6619e9)

- `Create A Form` - Tıklandığında butona tanımlanan sistemde yeni bir form oluşturulup uç kullanıcının işlem yapabileceği buton türüdür.

<details>
<summary>Create A Form butonun özellikleri için tıklayın</summary>
<div>

**Button Properties**

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Type 	| Create A Form 	|
| Name 	| Action butonun adının tanımlandığı alandır. Alanda ekli diğer ögelerdeki name alanlarında tanımlanmış değerlerden farklı olmalıdır, aynı değer yazılırsa ekleme işlemi yapılmaz. 	|
| Text 	| Action butonun web ara yüzünde gösterileceği başlığın tanımlandığı alandır. 	|
| Title 	| Action butonun web ara yüzünde fare imleci ile üzerine gelindiğinde gösterilecek bilginin tanımlandığı alandır. 	|
| Icon 	| Action buton ikon ile birlikte gösterilmek istenirse, ikonun seçildiği alandır. 	|
| Visible 	| Action butonun web ara yüzünde görünürlüğünün belirlendiği seçenektir. 	|

**Action Type Properties**

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Project Name 	| Action buton ile açılması istenen formun bulunduğu projenin adının (**Name**) bilgisinin yazıldığı alandır. 	|
| Form Name 	| Action buton ile açılması istenen form adının (**Name**) yazıldığı alandır 	|
| Default View 	| Action buton ile açılacak formun, varsayılan olarak hangi görünüm (default, view1, muhasebe vb gibi ) ile açılması isteniyorsa tanımlandığı alandır. 	|
| Data Entry Form 	| Alan aktif edilirse, Action buton ile form açıldığında form üzerindeki yapılan işlemler kaydedildiğinde veri tanına kaydedilir ancak nesne üzerine eklenmez. 	|
| Parameters 	| Alan içine yazılacak değerlerle action butona tıklandığında açılacak forma parametre gönderilerek, gönderilen parametreler açılan form içinde ResponseParameters metodu ile karşılanarak parametreye göre işlem yapılması sağlanabilir. 	|
| Panel Size 	| Action buton ile açılacak formun boyutunun belirlendiği alandır 1-2 veya 3 değerleri seçilebilir. Seçilen değerler Show On özelliğinde Panel seçiminde etkili olacak olup, Modal veya Drawer seçildiğinde Panel Size'a girilen değer etki etmeyecektir. 	|
| Show On 	| Action buton ile açılacak formun tipte açılacağını belirlemek için kullanılır.<br/>Panel: Form panel görünümde açılmak istenirse seçilmelidir. Varsayılan açılma tipidir, panel büyüklüğü Panel Size alanında 1-2-3 değerleri seçilerek değiştirilebilmektedir.<br/>Modal: Form ekranın ortasında, ekranı kaplayacak şekilde açılması istenirse seçilmelidir. Panel Size alanında yapılan seçim modal ile açılmayı etkilemez.<br/>Drawer: Form ekranın sağından kayarak panelin gösterilmesi istenirse seçilmelidir. Açılan form mevcut sayfanın üstünde gösterilir. Panel Size alanında yapılan seçim drawer ile açılmayı etkilemez. 	|

</div>
</details>

- `Open A Form` - Sistemdeki mevcut formun görüntülenmesi istenirse kullanılacak buton türüdür. Buton ile sadece form görüntülenmesi sağlanır, akış tarihçesi hakkında bilgi gösterilmesi istenirse Open A Process butonu kullanılmalıdır.

<details>
<summary>Open A Form butonun özellikleri için tıklayın</summary>
<div>

**Button Properties**

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Type 	| Open A Form 	|
| Name 	| Action butonun adının tanımlandığı alandır. Alanda ekli diğer ögelerdeki name alanlarında tanımlanmış değerlerden farklı olmalıdır, aynı değer yazılırsa ekleme işlemi yapılmaz. 	|
| Text 	| Action butonun web ara yüzünde gösterileceği başlığın tanımlandığı alandır. 	|
| Title 	| Action butonun web ara yüzünde fare imleci ile üzerine gelindiğinde gösterilecek bilginin tanımlandığı alandır. 	|
| Icon 	| Action buton ikon ile birlikte gösterilmek istenirse, ikonun seçildiği alandır. 	|
| Visible 	| Action butonun web ara yüzünde görünürlüğünün belirlendiği seçenektir. 	|

**Action Type Properties**

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Document Id 	| Action buton ile açılması istenen formun **global id** bilginin yazıldığı alandır. 	|
| Default View 	| Action buton ile açılacak formun, varsayılan olarak hangi görünüm (default, view1, muhasebe vb gibi ) ile açılması isteniyorsa tanımlandığı alandır. 	|
| Editable 	| Action buton ile açılması istenen formda değişiklik işleminin yapılıp yapılmayacağının belirlendiği alandır. Formda değişiklik yapılması isteniyorsa alan aktif edilmelidir. 	|
| Parameters 	| Alan içine yazılacak değerlerle action butona tıklandığında açılacak forma parametre gönderilerek, gönderilen parametreler açılan form içinde ResponseParameters metodu ile karşılanarak parametreye göre işlem yapılması sağlanabilir. 	|
| Panel Size 	| Action buton ile açılacak formun boyutunun belirlendiği alandır 1-2 veya 3 değerleri seçilebilir. Seçilen değerler Show On özelliğinde Panel seçiminde etkili olacak olup, Modal veya Drawer seçildiğinde Panel Size'a girilen değer etki etmeyecektir. 	|
| Show On 	| Action buton ile açılacak formun tipte açılacağını belirlemek için kullanılır.<br/>Panel: Form panel görünümde açılmak istenirse seçilmelidir. Varsayılan açılma tipidir, panel büyüklüğü Panel Size alanında 1-2-3 değerleri seçilerek değiştirilebilmektedir.<br/>Modal: Form ekranın ortasında, ekranı kaplayacak şekilde açılması istenirse seçilmelidir. Panel Size alanında yapılan seçim modal ile açılmayı etkilemez.<br/>Drawer: Form ekranın sağından kayarak panelin gösterilmesi istenirse seçilmelidir. Açılan form mevcut sayfanın üstünde gösterilir. Panel Size alanında yapılan seçim drawer ile açılmayı etkilemez. 	|

</div>
</details>

- `Open A Process` - Sistemdeki mevcut sürecin görüntülenmesi istenirse kullanılacak buton türüdür. Buton ile akış tarihçesi gibi bilgiler erişilebilir olmaktadır. Sadece formun görüntülenmesi istenirse Open A Form tipinde buton kullanılmalıdır.

<details>
<summary>Open A Process butonun özellikleri için tıklayın</summary>
<div>

**Button Properties**

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Type 	| Open A Process 	|
| Name 	| Action butonun adının tanımlandığı alandır. Alanda ekli diğer ögelerdeki name alanlarında tanımlanmış değerlerden farklı olmalıdır, aynı değer yazılırsa ekleme işlemi yapılmaz. 	|
| Text 	| Action butonun web ara yüzünde gösterileceği başlığın tanımlandığı alandır. 	|
| Title 	| Action butonun web ara yüzünde fare imleci ile üzerine gelindiğinde gösterilecek bilginin tanımlandığı alandır. 	|
| Icon 	| Action buton ikon ile birlikte gösterilmek istenirse, ikonun seçildiği alandır. 	|
| Visible 	| Action butonun web ara yüzünde görünürlüğünün belirlendiği seçenektir. 	|

**Action Type Properties**

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Process Id 	| Action buton ile açılması istenen süreç numarası bilginin yazıldığı alandır. 	|
| Process Request Id 	| Action butonda açılacak sürecin hangi istek numarası ile açılacağını belirlemek için yazıldığı alandır. PROCESSREQUEST tablosunda ilgili süreç numarasının PROCESSREQUESTID kolonu verisi kullanılmaktadır. Tabloda süreç numarasının içermediği RequestId tanımırsa süreç görüntülenemez. 	|
| Parameters 	| Alan içine yazılacak değerlerle action butona tıklandığında açılacak forma parametre gönderilerek, gönderilen parametreler açılan form içinde ResponseParameters metodu ile karşılanarak parametreye göre işlem yapılması sağlanabilir. 	|
| Panel Size 	| Action buton ile açılacak formun boyutunun belirlendiği alandır 1-2 veya 3 değerleri seçilebilir. Seçilen değerler Show On özelliğinde Panel seçiminde etkili olacak olup, Modal veya Drawer seçildiğinde Panel Size'a girilen değer etki etmeyecektir. 	|
| Show On 	| Action buton ile açılacak formun tipte açılacağını belirlemek için kullanılır.<br/>Panel: Form panel görünümde açılmak istenirse seçilmelidir. Varsayılan açılma tipidir, panel büyüklüğü Panel Size alanında 1-2-3 değerleri seçilerek değiştirilebilmektedir.<br/>Modal: Form ekranın ortasında, ekranı kaplayacak şekilde açılması istenirse seçilmelidir. Panel Size alanında yapılan seçim modal ile açılmayı etkilemez.<br/>Drawer: Form ekranın sağından kayarak panelin gösterilmesi istenirse seçilmelidir. Açılan form mevcut sayfanın üstünde gösterilir. Panel Size alanında yapılan seçim drawer ile açılmayı etkilemez. 	|

</div>
</details>

- `Open A Selection Form` - Tıklandığında butona tanımlanan veri kaynağına tanımlı bir seçim formunu açarak uç kullanıcının işlem yapabileceği buton türüdür.

<details>
<summary>Open A Selection Form butonun özellikleri için tıklayın</summary>
<div>

**Button Properties**

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Type 	| Open A Selection Form 	|
| Name 	| Action butonun adının tanımlandığı alandır. Alanda ekli diğer ögelerdeki name alanlarında tanımlanmış değerlerden farklı olmalıdır, aynı değer yazılırsa ekleme işlemi yapılmaz. 	|
| Text 	| Action butonun web ara yüzünde gösterileceği başlığın tanımlandığı alandır. 	|
| Title 	| Action butonun web ara yüzünde fare imleci ile üzerine gelindiğinde gösterilecek bilginin tanımlandığı alandır. 	|
| Icon 	| Action buton ikon ile birlikte gösterilmek istenirse, ikonun seçildiği alandır. 	|
| Visible 	| Action butonun web ara yüzünde görünürlüğünün belirlendiği seçenektir. 	|

**Ok Button Properties**

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Text 	| Selection form panelindeki tamam butonu yanında yazılması istenen ifadenin tanımlandığı alandır. 	|
| Title 	| Selection form panelinde tamam butonu üzerine fare işaretçisi ile üzerine gelindiğinde gösterilecek bilginin tanımlandığı alandır. 	|
| Icon 	| Selection form panelinde tamam butonun ikonunun belirlendiği alandır. 	|

**Data Source**

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| DataSource 	| Selection form içinde gösterilecek verilerin bulunduğu projedeki veri kaynağının seçildiği alandır. 	|
| Columns 	| DataSource alanında seçilen veri kaynağına göre, veri kaynağından gelen kolonların üretildiği alandır. Alan içindeki Kolonları Üret botonuna tıklanarak, tanımlı veri kaynağında kolon tiplerine uygun kolonlar üretilecektir. Üretilen kolonlardan bir tanesinin birincil anahtar olarak işaretlenmesi, seçim işleminde aynı ögelerin olduğu satırlar bulunduğunda hepsinin seçilmesini önlemektedir. 	|
| Column Map 	| Nesne kolonları ve Columns alanında üretilen kolonların eşleştirildiği alandır. Nesne kolonlarında seçim yaparken Columns alanındaki uygun kolon tipi seçilebilir olacaktır. Örneğin nesnede kolon tipi text tipinde ise, seçim listesinde text tipindeki kolonlar listelenir. Diğer türdeki kolonlar listelenmez. 	|

**Columns Settings**

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Enabled 	| Columns Settings altındaki Orderable ve Resizeable özelliklerinin kullanılması için aktif edilmesi gereken özelliktir. 	|
| Orderable 	| Aktif edildiğinde selection formdaki kolonların kendi içinde sırasını değiştirilmesi istenirse özellik aktif edilmelidir. 	|
| Resizeable 	| Aktif edildiğinde selection formdaki kolonun sağa veya sola doğru genişletilip daraltılabilmesini sağlayan özelliktir. 	|

**Filtering Settings**

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Enabled 	| Alan aktif edilerek selection form içinde her kolon başlığında filtreleme özelliği kullanılabilir durumda olur. Kolon tipine göre filtre türleri değişiklik gösterebilir.  	|

**Paging Settings**

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Enabled 	| Selection formda listelenen verilerin sayfalar şeklinde gösterilip gösterilmeyeceğinin ayarlandığı özelliktir. Bu özellik pasif yapıldığında, bağlı olan data source içinde ne kadar kayıt varsa alt alta listelenir. Özellik aktif edildiğinde veriler, sayfalar şeklinde gösterilir. 	|
| Current Page 	| Selection form web arayüzünde açıldığında, burada belirtilen sayfadan açılmasını sağlamak için kullanılan özelliktir. 	|
| Paging Size 	| Sayfa başına kayıt sayısı gösterim ayarlarının yapıldığı özelliktir. Varsayılan olarak 10, 20, 30, 40 değerlerini alır. Bir sayfada kaç satır gösterilmek isteniyorsa bu alandan ayarlanabilir. 	|

**Seaching Settings**

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Enabled 	| Özellik aktif edildiğinde, selection form yapısının üzerinde arama çubuğu belirir. Ve bu arama çubuğuna yazılan değer, formun tüm kolonlarında aratılarak, eşleyen satırların listelenmesi sağlanır. 	|

**Selection Settings**

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Enabled 	| Selection formda tablo satırları içerisinden satır seçebilmek için bu özellik aktif edilmelidir. 	|
| Mode 	| Seçim modunun seçileceği alandır. "Single" ve "Multiple" seçeneklerini barındırır. Selection form içindeki ögelerde sadece tek bir satır seçilmek istenirse "Single", birden çok satırı seçilmek istenirse "Multiple" modu seçilmelidir. 	|
| Show Select All 	| Bu özellik aktif edildiğinde, sütun başlıklarının yanında tümünü seç butonu aktif olur. Eğer Mode alanında **multiple** seçili ise selection form içinde tümünü seç checkbox'ı görünür hale geçer. Tümünü Seç butonuna tıklandığında Select All Mode özelliğinde yapılan seçime göre sayfada veya bütün sayfalarda tüm satırlar seçili hale gelir. Butona tekrar tıklandığında satır seçimleri kaldırılır. 	|
| Select All Mode 	| Show Select All özelliği ile birlikte çalışır. **page** seçili ise Select All ile yapılan seçimle sadece görüntülenen sayfadaki ögeler seçilir, **allPage** seçili ise Tümünü Seç işleminde yapılan seçimde bütün sayfalardaki ögeler seçilir.  	|
| Show CheckBoxes Mode 	| Selection formda seçim sütununda ve satır seçimi işleminde checkbox'ların ne zaman görüntüleneceği belirler. Yapılan seçim mode alanında **multiple** seçili olduğunda geçerlidir.<br/>always: Tüm onay kutularını içeren seçim sütunu her zaman görünür durumdadır. Kullanıcı, onay kutusunu veya onay kutusunun bulunduğu hücreyi tıklayarak bir satırı seçebilir, ancak satırın kendisini tıklayarak seçim işlemini yapamaz.<br/>none: Tüm onay kutularını içeren seçim sütunu gizlenir. Kullanıcılar klavye kısayolları veya uzun dokunma (tıkla ve basılı tut) ile satırları seçebilir.<br/>onClick: Seçim sütunu her zaman gösterilir. Kullanıcı sütunu tıkladığında veya iki veya daha fazla satır seçildiğinde onay kutuları görünür. Satır seçimi iptal edildiğinde onay kutuları kaybolur.<br/>onLongTap: Tüm onay kutularını içeren seçim sütunu, satırlara uzun dokunulduğunda (tıklayın ve basılı tutun) görünür ve kaybolur. 	|

**Sorting Settings**

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Enabled 	| Selection formda tablo kolonları içinde sıralama işlemi yapılabilmesi için özellik aktif edilmelidir. 	|
| All Sorting Columns 	| Aktif olduğunda kolondaki sıralamanın diğer satırların da sırasını değiştirmesini sağlar. 	|
| Mode 	| Sıralama modunu belirtir.<br/>none: Satırlarda sıralama işlemi yapılamaz<br/>single: Satırlar yalnızca tek bir sütunun değerlerine göre sıralanabilir.<br/>multple: Satırlar birkaç sütunun değerlerine göre sıralanabilir. 	|

**Action Type Properties**

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Panel Size 	| Action buton ile açılacak formun boyutunun belirlendiği alandır 1-2 veya 3 değerleri seçilebilir. Seçilen değerler Show On özelliğinde Panel seçiminde etkili olacak olup, Modal veya Drawer seçildiğinde Panel Size'a girilen değer etki etmeyecektir. 	|
| Show On 	| Action buton ile açılacak formun tipte açılacağını belirlemek için kullanılır.<br/>Panel: Form panel görünümde açılmak istenirse seçilmelidir. Varsayılan açılma tipidir, panel büyüklüğü Panel Size alanında 1-2-3 değerleri seçilerek değiştirilebilmektedir.<br/>Modal: Form ekranın ortasında, ekranı kaplayacak şekilde açılması istenirse seçilmelidir. Panel Size alanında yapılan seçim modal ile açılmayı etkilemez.<br/>Drawer: Form ekranın sağından kayarak panelin gösterilmesi istenirse seçilmelidir. Açılan form mevcut sayfanın üstünde gösterilir. Panel Size alanında yapılan seçim drawer ile açılmayı etkilemez. 	|

</div>
</details>

- `Start A Process` - Tıklandığında butona tanımlanan sistemde yeni bir süreç oluşturulup uç kullanıcının işlem yapabileceği buton türüdür.

<details>
<summary>Start A Process butonun özellikleri için tıklayın</summary>
<div>

**Button Properties**

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Type 	| Start A Process 	|
| Name 	| Action butonun adının tanımlandığı alandır. Alanda ekli diğer ögelerdeki name alanlarında tanımlanmış değerlerden farklı olmalıdır, aynı değer yazılırsa ekleme işlemi yapılmaz. 	|
| Text 	| Action butonun web ara yüzünde gösterileceği başlığın tanımlandığı alandır. 	|
| Title 	| Action butonun web ara yüzünde fare imleci ile üzerine gelindiğinde gösterilecek bilginin tanımlandığı alandır. 	|
| Icon 	| Action buton ikon ile birlikte gösterilmek istenirse, ikonun seçildiği alandır. 	|
| Visible 	| Action butonun web ara yüzünde görünürlüğünün belirlendiği seçenektir. 	|

**Action Type Properties**

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Project Name 	| Action buton ile başlatılacak projenin adının (**Name**) bilgisinin yazıldığı alandır. 	|
| Flow Name 	| Action buton ile başlatılacak projenin hangi akış ile başlatılması isteniyorsa, akış adının (**Name**) yazıldığı alandır. 	|
| Parameters 	| Alan içine yazılacak değerlerle action butona tıklandığında açılacak forma parametre gönderilerek, gönderilen parametreler açılan form içinde ResponseParameters metodu ile karşılanarak parametreye göre işlem yapılması sağlanabilir. 	|
| Panel Size 	| Action buton ile açılacak formun boyutunun belirlendiği alandır 1-2 veya 3 değerleri seçilebilir. Seçilen değerler Show On özelliğinde Panel seçiminde etkili olacak olup, Modal veya Drawer seçildiğinde Panel Size'a girilen değer etki etmeyecektir. 	|
| Show On 	| Action buton ile açılacak formun tipte açılacağını belirlemek için kullanılır.<br/>Panel: Form panel görünümde açılmak istenirse seçilmelidir. Varsayılan açılma tipidir, panel büyüklüğü Panel Size alanında 1-2-3 değerleri seçilerek değiştirilebilmektedir.<br/>Modal: Form ekranın ortasında, ekranı kaplayacak şekilde açılması istenirse seçilmelidir. Panel Size alanında yapılan seçim modal ile açılmayı etkilemez.<br/>Drawer: Form ekranın sağından kayarak panelin gösterilmesi istenirse seçilmelidir. Açılan form mevcut sayfanın üstünde gösterilir. Panel Size alanında yapılan seçim drawer ile açılmayı etkilemez. 	|

</div>
</details>

- `Execute Custom Action` - Mevcut butonlar dışında formun .ts veya .cs alanlarında kod ile butona tıklanıldığında farklı işlemler yapılmak istendiğinde kullanılabilecek buton türüdür.

<details>
<summary>Execute Custom Action butonun özellikleri için tıklayın</summary>
<div>

**Button Properties**

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Type 	| Execute Custom Action 	|
| Name 	| Action butonun adının tanımlandığı alandır. Alanda ekli diğer ögelerdeki name alanlarında tanımlanmış değerlerden farklı olmalıdır, aynı değer yazılırsa ekleme işlemi yapılmaz. 	|
| Text 	| Action butonun web ara yüzünde gösterileceği başlığın tanımlandığı alandır. 	|
| Title 	| Action butonun web ara yüzünde fare imleci ile üzerine gelindiğinde gösterilecek bilginin tanımlandığı alandır. 	|
| Icon 	| Action buton ikon ile birlikte gösterilmek istenirse, ikonun seçildiği alandır. 	|
| Visible 	| Action butonun web ara yüzünde görünürlüğünün belirlendiği seçenektir. 	|

</div>
</details>

`Display Type` - Nesne yüksekliğinin içindeki verilere göre veya sabit boyut verilerek ayarlandığı özelliktir.

>Yapılabilecek Seçimler : Auto Grow, Auto Fill, Max Height, Fixed Height

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Auto Grow 	| Varsayılan seçimdir. Seçili olduğunda nesnenin içerdiği satır sayısına kadar satır alanı yüksekliği boyutlandırılır. 	|
| Auto Fill 	| Seçili olduğunda nesnenin tamamı form yüksekliği kadar yükseklik değerine sahip olarak içerdiği veriler gösterilir. 	|
| Max Height 	| Seçili olduğunda nesnenin özellik görüntüleyicisinde Height alanı görünür olur. Satır alanı yüksekliği en fazla Height alanında girilen değere kadar büyüyebilir. 	|
| Fixed Height 	| Seçili olduğunda nesnenin özellik görüntüleyicisinde Height alanı görünür olur. Satır alanı yüksekliği Height alanında girilen değer boyutunda gösterilir. 	|

`Height` - Display Type alanında Max Height veya Fixed Height seçildiğinde gözüken özelliktir. Alana girilen değere ve Display Type alanında yapılan seçime göre nesne yüksekliği görünümü değişmektedir.

`Virtual Scrolling` - Bu özellik aktif ve nesne içeriği doluyken; kolon başlıkları kısmı sabit kalır, sadece kaydırma çubuğu hareket eder. Nesnede paging özelliği aktif olsa bile nesnedeki tüm veriler tek sayfada kaydırma çubuğu kaydırıldıkça gösterilir. Özellik pasifken, kaydırma çubuğu ile birlikte kolon başlıkları da hareket eder.

`Alternate Color Enable` - Nesne satırlarını ayırt etmeyi kolaylaştırmak amacıyla, satırlardan biri beyaz, diğeri bu alandan seçilen renk olacak şekilde gösterilmesi istenirse aktif edilmelidir. Özellik aktif edildiğinde Alternate Color alanında seçilen renk ile diğer satır gösterilir. Özellik kapalı olduğunda bütün satırlar aynı renk ile gösterilir.

`Alternate Color` - Alternate Color Enable özelliği aktifse çalışır. Nesne satırlarını ayırt etmeyi kolaylaştırmak amacıyla, satırlardan biri beyaz, diğeri bu alandan seçilen renk olacak şekilde satır renklendirmeye yarayan özelliktir.

![DataGrid](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc2f336e7-9c7f-4ada-9d55-2e37541fea46)

`Export to Excel` - Özellik aktif edildiğinde, nesne üzerinde Excel’e Aktar butonu görünür olur. Bu butona tıklanarak, nesne verileri excele aktarılabilir.

![DataGrid](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload081a3cdf-95d7-4545-a091-3b17dd58b6a3)

`Grid Lines` - Nesne içindeki satırlarda, satırlar arası ayırma çizgilerinin nasıl görüneceğinin belirlendiği alandır.

>Yapılabilecek Seçimler : None, Horizontal, Vertical, Both

`Grid Border` - Nesne içindeki bölümlerde sınırların gösterimi için kullanılır. Aktif olduğunda nesne içindeki alanların sınırları çizgilerle belirtilir. Özellik kapatıldığında nesne görünümü formun arka planından beslenerek aynı olur.

`Column Vertical Border` - Kolonlarda dikey ayırma çizgilerinin gözükmesi istenirse özellik aktif edilmelidir. 

`Hover State Enabled` - Özellik aktif edildiğinde kullanıcı fare imlecini satır üzerine getirdiğinde, satırların vurgulanmasını sağlar.

`Hidden Row Column Name` - Nesnede kolon içindeki bir veriye göre, verinin bulunduğu satır gizlenmek istendiğinde kullanılan alandır. Alanda nesnede hangi kolona göre satırın gizlenmesini belirlemek için kolon seçilmelidir.

`Hidden Row Value Matchers` - Hidden Row Column Name alanında seçim yapılması ile görünür olur. Hidden Row Column Name alanında seçilen kolon içinde bulunabilecek/bulunan veriler Value Matchers alanında tanımlanır. Nesne içinde seçilen kolonda Value Matchers alanında girilen veri bulunursa, verinin bulunduğu satır otomatik olarak gizlenir.

### Behavior

`ReadOnly` - Nesnenin düzenleme modunda olup olmayacağının ayarlandığı kısımdır. Bu özellik aktif edildiğinde nesne veri girişine izin vermez, salt okunur modda olur. Nesneye veri girişine izin verilmesi için özelliğin pasif olması gerekir.

### Column Settings

`Orderable` - Nesne içindeki kolonların kendi içinde uç kullanıcı tarafından sırasının değiştirilmesi istenirse alan aktif edilmelidir.

`Show Column Chooser` - Alan aktif edildiğinde nesne üzerinde Sütun Seçici butonu gösterilerek, butona tıklanılınca kolon sürükle-bırak yöntemi ile açılan pop-up'a eklenerek, kolonun gizlenmesi sağlanır. Nesne üzerindeki kolonlardaki **Allow Hiding** özelliği ile birlikte çalışır. Eğer kolonda Allow Hiding özelliği devre dışı bırakılırsa kolon Sütun Seçici alanına eklenemez.

![DataGrid](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbe0cf739-917d-4658-a059-41a3e136c251)

![DataGrid](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload539d8edd-7bca-41f8-aa12-de22b6ddc837)

`Resizeable` - Kolon genişliği uç kullanıcı tarafından kolon sınırlarında sürükle ve bırak yöntemi ile genişletilip daraltılabilmesi istenirse alan aktif edilmelidir.

`Resizing Mode` - Resizeable özelliği aktif edildiğinde gözüken alandır. Yapılan seçime göre nesnedeki kolon genişletme daratma davranışları değişmektedir. **nextColumn** seçilirse, web ara yüzünde sütun boyutu değiştirilirken bitişik sütunu yeniden boyutlandırır; iki kolonun toplam bileşen genişliği değişmez. **widget** seçiminde web ara yüzünde sütun boyutu değiştirilirken nesnede toplam bileşen genişliği artar veya azalır; diğer tüm sütunlar genişliklerini korur.

>Yapılabilecek Seçimler : nextColumn, widget

### Editing Settings

`Mode` - Nesne üzerinde değişiklik yapılması istenildiğinde, nesnenin hangi durumda çalışacağının belirlendiği alandır. Nesnede Type:İlişkili seçildiğinde alan seçim yapılamaz durumuna geçer.

>Yapılabilecek Seçimler : cell, row, batch

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| cell 	| Bu modda nesne içindeki tüm satırlar düzenlenebilir durumunda olur. cell modunda, kullanıcı verileri hücre hücre düzenler. Bir hücre odağı kaybettiğinde değişiklikler kaydedilir veya bir kullanıcı Esc tuşuna basarsa atılır. Eklenen satır, yalnızca odak ondan kaydırıldığında kaydedilir. 	|
| row 	| Bu modda bir kullanıcı verileri satır satır düzenler. Bir kullanıcı bir "Düzenle" düğmesini tıkladığında, ilgili satır düzenleme durumuna girer ve düzenleme sütununda "Kaydet" ve "İptal" düğmeleri görünür. UI bileşeni, değişiklikleri yalnızca "Kaydet" düğmesi tıklandığında kaydeder. Bir kullanıcı başka bir satırı düzenlemeye başlarsa, verileri sıralar veya filtrelerse, değişiklikleri saymaz. 	|
| batch 	| batch modda, cell modunda olduğu gibi, kullanıcı verileri hücre hücre düzenler. Ancak, bu modda, bir kullanıcı değişiklikleri hemen kaydetmek yerine formu gönderene veya kaydedene kadar ön bellekte saklanır. Revert butonuna tıklanarak yapılan bütün değişiklikler geri alınabilir. 	|

row seçildiğinde görünüm;
![DataGrid](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload323a7eb6-5647-4e16-ab97-e13e89c11a27)

cell seçildiğinde görünüm;
<div style={{textAlign: 'center'}}>

![DataGrid](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0ff0f74a-2191-45ee-88c0-02ba9c8b21be)

</div>

:::tip İPUCU

batch tipindeki modu nesnede **datasource** alanında veri kaynağı tanımlı olduğunda kullanabilirsiniz. Yapmış olduğunuz değişiklikleri veri kaynağına geri yazmak için kod yazılmalıdır.

:::

:::caution DİKKAT

DataGrid nesnesi ilişkili tipinde kullanılığında editing setting alanında yapmış olduğunuz seçimler ile DataGrid nesnesi üzerinde nesneye tanımlı formdaki alanlar değiştirilemez. Alanları değiştirmek için formun üzerinde değişiklik yapılmalıdır.

:::

`Show Add Command` - Nesnede yeni satır eklenebilmesi istenirse aktif edilecek özelliktir. Nesnede Type:İlişkili seçildiğinde alan seçim yapılamaz durumuna geçer.

![DataGrid](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb0ffc4d8-7b68-44bb-a0a8-f8f14775c022)

`Show Delete Command` - Nesnede ekli satırın nesne üzerinden silinmesi istenirse aktif edilecek özelliktir.

![DataGrid](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload82f00188-8531-4940-b072-df05fad391e4)

`Show Edit Command` - Nesnede ekli satırdaki verilerde güncelleme yapılabilmesi istenirse aktif edilecek özelliktir. Nesnede **Type : İlişkili** seçildiğinde alan seçim yapılamaz durumuna geçer.

![DataGrid](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3432c4f7-5a39-4602-bca7-c8592b5e1446)

### Filtering Settings

`Row Filter Enabled` - Bu özellik aktif edildiğinde her bir kolonun altına filtre alanları açılır. Filtre alanına yazılan değer, kolon kayıtları arasında filtrelenerek, ilgili kayıtlar listelenir.

![DataGrid](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadeea1b309-3034-4d45-a06d-bfa147e36b3c)

`Show Operation Chooser` - Row Filter Enabled özelliği aktif edildiğinde gözükür. Filtre alanına yazılan metnin, kolon verileri arasındaki filtreleme seçeneklerini listeleyen özelliktir. Özellik aktif edildiğinde, her bir kolon için, kolon tipine uygun filtreleme seçenekleri listelenir.

![DataGrid](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb2fd400d-1316-4366-b4d0-de462eb075d5)

`Header Filter Enabled` - Header Filter, kullanıcının, tek bir sütundaki değerleri filtrelemesine olanak tanır. Aktif edildiğinde kolon başlığındaki simgesine tıklamak, tüm sütunun benzersiz değerlerini içeren bir açılır menüyü gösterir. Header Filter'ın kolonda gösterilmesi için **nesnedeki Header Filter Enabled** ve **kolonlardaki Header Filter Enabled** özelliğinin aktif edilmesi gereklidir.

### Paging Settings

`Enabled` - Tabloda listelenen verilerin sayfalar şeklinde gösterilip gösterilmeyeceğinin ayarlandığı özelliktir. Bu özellik pasif yapıldığında, tabloda ne kadar kayıt varsa alt alta listelenir. Özellik aktif edildiğinde veriler, sayfalar şeklinde gösterilir.

`Current Page` - Nesnenin, web arayüzünde açıldığında, burada belirtilen sayfadan açılmasını sağlamak için kullanılan özelliktir.

`Paging Size` - Sayfa başına kayıt sayısı gösterim ayarlarının yapıldığı özelliktir. Varsayılan olarak 10, 20, 30, 40 değerlerini alır. Bir sayfada kaç satır gösterilmek isteniyorsa bu alandan ayarlanabilir.

### Searching Settings

`Enabled` - Özellik aktif edildiğinde, tablo yapısının üzerinde arama çubuğu belirir. Ve bu arama çubuğuna yazılan değer, tablonun tüm kolonlarında aratılarak, eşleyen satırların listelenmesi sağlanır.

![DataGrid](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload29747462-e71b-4a33-b837-7e658123ffa8)

### Sorting Settings

`Mode` - Tablo kayıtları arasında sıralama yapılmasını sağlayan özelliktir. Herhangi bir kolona tıklandığında, kolon içindeki verilerin artan ya da azalan sıralamaya göre listelenmesini sağlar. 

>Yapılabilecek Seçimler : none, single, multiple

![DataGrid](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload60c54a24-f2f5-4fb4-8e63-9811e1ff394a)

:::tip İPUCU

Mode alanında listelenen değerlerde, **None** seçeneği, sıralama yapılmayacak demektir. **Single** seçeneği ile sadece tek bir kolona göre sıralama yapılabilir. **Multiple** seçeneği ile birden fazla kolon sıralanabilir demektir.

:::

### Selection Settings

`Enabled` - Nesnede satır seçilebilmesi istenirse aktif edilmesi gereken özlliktir.

`Mode` - Seçim modunun seçileceği alandır. "Single" ve "Multiple" seçeneklerini barındırır. Nesne içindeki satırlarda sadece tek bir satır seçilmek istenirse "Single", birden çok satırı seçilmek istenirse "Multiple" modu seçilmelidir.

`Show Select All` - Mode alanında multiple seçildiğinde görünen özelliktir. Bu özellik aktif edildiğinde, sütun başlıklarının yanında tümünü seç butonu aktif olur. Eğer Mode alanında **multiple** seçili ise DataGrid nesnesi içinde tümünü seç checkbox'ı görünür hale geçer. Tümünü Seç butonuna tıklandığında Select All Mode özelliğinde yapılan seçime göre sayfada veya bütün sayfalarda tüm satırlar seçili hale gelir. Butona tekrar tıklandığında satır seçimleri kaldırılır.

`Select All Mode` - Mode alanında multiple seçildiğinde görünen özelliktir. Show Select All özelliği ile birlikte çalışır. **page** seçili ise Select All ile yapılan seçimle sadece görüntülenen sayfadaki ögeler seçilir, **allPage** seçili ise Tümünü Seç işleminde yapılan seçimde bütün sayfalardaki ögeler seçilir.

`Show CheckBoxes Mode` - Mode alanında multiple seçildiğinde görünen özelliktir. DataGrid nesnesinde seçim sütununda ve satır seçimi işleminde checkbox'ların ne zaman görüntüleneceği belirler. Yapılan seçim Mode alanında **multiple** seçili olduğunda geçerlidir.

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| always 	| Tüm onay kutularını içeren seçim sütunu her zaman görünür durumdadır. Kullanıcı, onay kutusunu veya onay kutusunun bulunduğu hücreyi tıklayarak bir satırı seçebilir, ancak satırın kendisini tıklayarak seçim işlemini yapamaz. 	|
| none 	| Tüm onay kutularını içeren seçim sütunu gizlenir. Kullanıcılar klavye kısayolları veya uzun dokunma (tıkla ve basılı tut) ile satırları seçebilir. 	|
| onClick 	| Seçim sütunu her zaman gösterilir. Kullanıcı sütunu tıkladığında veya iki veya daha fazla satır seçildiğinde onay kutuları görünür. Satır seçimi iptal edildiğinde onay kutuları kaybolur. 	|
| onLongTap 	| Tüm onay kutularını içeren seçim sütunu, satırlara uzun dokunulduğunda (tıklayın ve basılı tutun) görünür ve kaybolur. 	|

### Execute Action

`Toolbar Buttons` - Bu alanda nesneye, bazı aksiyonları almak için butonlar eklenebilir. Form oluşturma, form açma, süreç açma, seçili formu açma veya süreç başlatma gibi işlemleri gerçekleştiren butonlar eklenerek, butona tıklandığında ilgili aksiyonun alınması sağlanabilir. Araç çubuğu butonları alanına tıklandığında, nesneye eklenecek aksiyon butonlarının tanımlanacağı ekran açılır.

![DataGrid](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada56c4a5c-4367-4e42-85c4-ff3d509ae2ba)

Açılan ekranda ekle butonuna tıklanarak, buton adı, metni ve başlığı girilip, butona tıklandığında hangi aksiyonu gerçekleştireceğinin seçimi yapılır.

<div style={{textAlign: 'center'}}>

![DataGrid](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6fd87482-e149-4d8b-bfe4-c1e5566435e1)

</div>

- `Create A Form` - Tıklandığında butona tanımlanan sistemde yeni bir form oluşturulup uç kullanıcının işlem yapabileceği buton türüdür. Hangi projenin hangi formunun oluşturulacağı bilgileri Aksiyon Özellikleri alanından seçilmelidir.

![DataGrid](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf5717154-e547-4e81-b201-bc6b3ef9a82b)

<details>
  <summary>Create A Form butonun özellikleri için tıklayın</summary>
  <div>

  **Button Properties**

  | **Özellik** 	| **Açıklama** 	|
  |---	|---	|
  | Name 	| Action butonun adının tanımlandığı alandır. Alanda ekli diğer ögelerdeki name alanlarında tanımlanmış değerlerden farklı olmalıdır, aynı değer yazılırsa ekleme işlemi yapılmaz. 	|
  | Text 	| Action butonun web ara yüzünde gösterileceği başlığın tanımlandığı alandır. 	|
  | Title 	| Action butonun web ara yüzünde fare imleci ile üzerine gelindiğinde gösterilecek bilginin tanımlandığı alandır. 	|
  | Icon 	| Action buton ikon ile birlikte gösterilmek istenirse, ikonun seçildiği alandır. 	|
  | Visible 	| Action butonun web ara yüzünde görünürlüğünün belirlendiği seçenektir. 	|

  **Action Type Properties**

  | **Özellik** 	| **Açıklama** 	|
  |---	|---	|
  | Project Name 	| Action buton ile açılması istenen formun bulunduğu projenin adının (**Name**) bilgisinin yazıldığı alandır. 	|
  | Form Name 	| Action buton ile açılması istenen form adının (**Name**) yazıldığı alandır 	|
  | Default View 	| Action buton ile açılacak formun, varsayılan olarak hangi görünüm (default, view1, muhasebe vb gibi ) ile açılması isteniyorsa tanımlandığı alandır. 	|
  | Data Entry Form 	| Alan aktif edilirse, Action buton ile form açıldığında form üzerindeki yapılan işlemler kaydedildiğinde veri tanına kaydedilir ancak nesne üzerine eklenmez. 	|
  | Parameters 	| Alan içine yazılacak değerlerle action butona tıklandığında açılacak forma parametre gönderilerek, gönderilen parametreler açılan form içinde ResponseParameters metodu ile karşılanarak parametreye göre işlem yapılması sağlanabilir. 	|
  | Panel Size 	| Action buton ile açılacak formun boyutunun belirlendiği alandır 1-2 veya 3 değerleri seçilebilir. Seçilen değerler Show On özelliğinde Panel seçiminde etkili olacak olup, Modal veya Drawer seçildiğinde Panel Size'a girilen değer etki etmeyecektir. 	|
  | Show On 	| Action buton ile açılacak formun tipte açılacağını belirlemek için kullanılır.<br/>Panel: Form panel görünümde açılmak istenirse seçilmelidir. Varsayılan açılma tipidir, panel büyüklüğü Panel Size alanında 1-2-3 değerleri seçilerek değiştirilebilmektedir.<br/>Modal: Form ekranın ortasında, ekranı kaplayacak şekilde açılması istenirse seçilmelidir. Panel Size alanında yapılan seçim modal ile açılmayı etkilemez.<br/>Drawer: Form ekranın sağından kayarak panelin gösterilmesi istenirse seçilmelidir. Açılan form mevcut sayfanın üstünde gösterilir. Panel Size alanında yapılan seçim drawer ile açılmayı etkilemez. 	|

  </div>
</details>

- `Open A Form` - Sistemdeki mevcut formun görüntülenmesi istenirse kullanılacak buton türüdür. Açtırılmak istenen formun form id (Document Id) değeri Aksiyon Özellikleri alanından seçilmelidir. Genelde, doküman arşiv oluştururken kullanılır. Buton ile sadece form görüntülenmesi sağlanır, akış tarihçesi hakkında bilgi gösterilmesi istenirse Open A Process butonu kullanılmalıdır.

![DataGrid](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload90032690-ca97-490f-94be-eb80e9abb425)

<details>
  <summary>Open A Form butonun özellikleri için tıklayın</summary>
  <div>

  **Button Properties**

  | **Özellik** 	| **Açıklama** 	|
  |---	|---	|
  | Name 	| Action butonun adının tanımlandığı alandır. Alanda ekli diğer ögelerdeki name alanlarında tanımlanmış değerlerden farklı olmalıdır, aynı değer yazılırsa ekleme işlemi yapılmaz. 	|
  | Text 	| Action butonun web ara yüzünde gösterileceği başlığın tanımlandığı alandır. 	|
  | Title 	| Action butonun web ara yüzünde fare imleci ile üzerine gelindiğinde gösterilecek bilginin tanımlandığı alandır. 	|
  | Icon 	| Action buton ikon ile birlikte gösterilmek istenirse, ikonun seçildiği alandır. 	|
  | Visible 	| Action butonun web ara yüzünde görünürlüğünün belirlendiği seçenektir. 	|

  **Action Type Properties**

  | **Özellik** 	| **Açıklama** 	|
  |---	|---	|
  | Document Id 	| Action buton ile açılması istenen formun **global id** bilginin yazıldığı alandır. 	|
  | Default View 	| Action buton ile açılacak formun, varsayılan olarak hangi görünüm (default, view1, muhasebe vb gibi ) ile açılması isteniyorsa tanımlandığı alandır. 	|
  | Editable 	| Action buton ile açılması istenen formda değişiklik işleminin yapılıp yapılmayacağının belirlendiği alandır. Formda değişiklik yapılması isteniyorsa alan aktif edilmelidir. 	|
  | Parameters 	| Alan içine yazılacak değerlerle action butona tıklandığında açılacak forma parametre gönderilerek, gönderilen parametreler açılan form içinde ResponseParameters metodu ile karşılanarak parametreye göre işlem yapılması sağlanabilir. 	|
  | Panel Size 	| Action buton ile açılacak formun boyutunun belirlendiği alandır 1-2 veya 3 değerleri seçilebilir. Seçilen değerler Show On özelliğinde Panel seçiminde etkili olacak olup, Modal veya Drawer seçildiğinde Panel Size'a girilen değer etki etmeyecektir. 	|
  | Show On 	| Action buton ile açılacak formun tipte açılacağını belirlemek için kullanılır.<br/>Panel: Form panel görünümde açılmak istenirse seçilmelidir. Varsayılan açılma tipidir, panel büyüklüğü Panel Size alanında 1-2-3 değerleri seçilerek değiştirilebilmektedir.<br/>Modal: Form ekranın ortasında, ekranı kaplayacak şekilde açılması istenirse seçilmelidir. Panel Size alanında yapılan seçim modal ile açılmayı etkilemez.<br/>Drawer: Form ekranın sağından kayarak panelin gösterilmesi istenirse seçilmelidir. Açılan form mevcut sayfanın üstünde gösterilir. Panel Size alanında yapılan seçim drawer ile açılmayı etkilemez. 	|

  </div>
</details>

- `Open A Process` - Sistemdeki mevcut sürecin görüntülenmesi istenirse kullanılacak buton türüdür. Açtırılmak istenen sürecin id si (Process Id) ve sürecin istek id si (Process Request Id) değerleri Aksiyon Özellikleri alanından seçilmelidir. Genelde, süreç arşiv oluştururken kullanılır. Buton ile akış tarihçesi gibi bilgiler erişilebilir olmaktadır. Sadece formun görüntülenmesi istenirse Open A Form tipinde buton kullanılmalıdır.

![DataGrid](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadda30c46e-09c7-4cf5-ae61-4fbfa2778aec)

<details>
  <summary>Open A Process butonun özellikleri için tıklayın</summary>
  <div>

  **Button Properties**

  | **Özellik** 	| **Açıklama** 	|
  |---	|---	|
  | Name 	| Action butonun adının tanımlandığı alandır. Alanda ekli diğer ögelerdeki name alanlarında tanımlanmış değerlerden farklı olmalıdır, aynı değer yazılırsa ekleme işlemi yapılmaz. 	|
  | Text 	| Action butonun web ara yüzünde gösterileceği başlığın tanımlandığı alandır. 	|
  | Title 	| Action butonun web ara yüzünde fare imleci ile üzerine gelindiğinde gösterilecek bilginin tanımlandığı alandır. 	|
  | Icon 	| Action buton ikon ile birlikte gösterilmek istenirse, ikonun seçildiği alandır. 	|
  | Visible 	| Action butonun web ara yüzünde görünürlüğünün belirlendiği seçenektir. 	|

  **Action Type Properties**

  | **Özellik** 	| **Açıklama** 	|
  |---	|---	|
  | Process Id 	| Action buton ile açılması istenen süreç numarası bilginin yazıldığı alandır. 	|
  | Process Request Id 	| Action butonda açılacak sürecin hangi istek numarası ile açılacağını belirlemek için yazıldığı alandır. PROCESSREQUEST tablosunda ilgili süreç numarasının PROCESSREQUESTID kolonu verisi kullanılmaktadır. Tabloda süreç numarasının içermediği RequestId tanımırsa süreç görüntülenemez. 	|
  | Parameters 	| Alan içine yazılacak değerlerle action butona tıklandığında açılacak forma parametre gönderilerek, gönderilen parametreler açılan form içinde ResponseParameters metodu ile karşılanarak parametreye göre işlem yapılması sağlanabilir. 	|
  | Panel Size 	| Action buton ile açılacak formun boyutunun belirlendiği alandır 1-2 veya 3 değerleri seçilebilir. Seçilen değerler Show On özelliğinde Panel seçiminde etkili olacak olup, Modal veya Drawer seçildiğinde Panel Size'a girilen değer etki etmeyecektir. 	|
  | Show On 	| Action buton ile açılacak formun tipte açılacağını belirlemek için kullanılır.<br/>Panel: Form panel görünümde açılmak istenirse seçilmelidir. Varsayılan açılma tipidir, panel büyüklüğü Panel Size alanında 1-2-3 değerleri seçilerek değiştirilebilmektedir.<br/>Modal: Form ekranın ortasında, ekranı kaplayacak şekilde açılması istenirse seçilmelidir. Panel Size alanında yapılan seçim modal ile açılmayı etkilemez.<br/>Drawer: Form ekranın sağından kayarak panelin gösterilmesi istenirse seçilmelidir. Açılan form mevcut sayfanın üstünde gösterilir. Panel Size alanında yapılan seçim drawer ile açılmayı etkilemez. 	|

  </div>
</details>

- `Start A Process` - Tıklandığında butona tanımlanan sistemde yeni bir süreç oluşturulup uç kullanıcının işlem yapabileceği buton türüdür. Hangi projenin hangi akışından süreç başlatılacağı bilgileri Aksiyon Özellikleri alanında belirtilmelidir.

![DataGrid](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8b403cc9-b18f-463e-b6d3-0cd7315672b5)

<details>
  <summary>Start A Process butonun özellikleri için tıklayın</summary>
  <div>

  **Button Properties**

  | **Özellik** 	| **Açıklama** 	|
  |---	|---	|
  | Name 	| Action butonun adının tanımlandığı alandır. Alanda ekli diğer ögelerdeki name alanlarında tanımlanmış değerlerden farklı olmalıdır, aynı değer yazılırsa ekleme işlemi yapılmaz. 	|
  | Text 	| Action butonun web ara yüzünde gösterileceği başlığın tanımlandığı alandır. 	|
  | Title 	| Action butonun web ara yüzünde fare imleci ile üzerine gelindiğinde gösterilecek bilginin tanımlandığı alandır. 	|
  | Icon 	| Action buton ikon ile birlikte gösterilmek istenirse, ikonun seçildiği alandır. 	|
  | Visible 	| Action butonun web ara yüzünde görünürlüğünün belirlendiği seçenektir. 	|

  **Action Type Properties**

  | **Özellik** 	| **Açıklama** 	|
  |---	|---	|
  | Project Name 	| Action buton ile başlatılacak projenin adının (**Name**) bilgisinin yazıldığı alandır. 	|
  | Flow Name 	| Action buton ile başlatılacak projenin hangi akış ile başlatılması isteniyorsa, akış adının (**Name**) yazıldığı alandır. 	|
  | Parameters 	| Alan içine yazılacak değerlerle action butona tıklandığında açılacak forma parametre gönderilerek, gönderilen parametreler açılan form içinde ResponseParameters metodu ile karşılanarak parametreye göre işlem yapılması sağlanabilir. 	|
  | Panel Size 	| Action buton ile açılacak formun boyutunun belirlendiği alandır 1-2 veya 3 değerleri seçilebilir. Seçilen değerler Show On özelliğinde Panel seçiminde etkili olacak olup, Modal veya Drawer seçildiğinde Panel Size'a girilen değer etki etmeyecektir. 	|
  | Show On 	| Action buton ile açılacak formun tipte açılacağını belirlemek için kullanılır.<br/>Panel: Form panel görünümde açılmak istenirse seçilmelidir. Varsayılan açılma tipidir, panel büyüklüğü Panel Size alanında 1-2-3 değerleri seçilerek değiştirilebilmektedir.<br/>Modal: Form ekranın ortasında, ekranı kaplayacak şekilde açılması istenirse seçilmelidir. Panel Size alanında yapılan seçim modal ile açılmayı etkilemez.<br/>Drawer: Form ekranın sağından kayarak panelin gösterilmesi istenirse seçilmelidir. Açılan form mevcut sayfanın üstünde gösterilir. Panel Size alanında yapılan seçim drawer ile açılmayı etkilemez. 	|

  </div>
</details>

- `Open A Selection Form` - Tıklandığında butona tanımlanan veri kaynağına tanımlı bir seçim formunu açarak uç kullanıcının işlem yapabileceği buton türüdür. Seçildiğinde, seçim yapılacak listenin veri bağlantılarının tanımlanması gerekmektedir. Ve bu alanda, seçim yapılacak tablo yapısının kolon, filtre, sayfalama, arama, seçim, sıralama gibi özellikleri de düzenlenebilir.

![DataGrid](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload89dbda8b-efd7-4057-a704-745bb46ea3fe)

<details>
  <summary>Open A Selection Form butonun özellikleri için tıklayın</summary>
  <div>

  **Button Properties**

  | **Özellik** 	| **Açıklama** 	|
  |---	|---	|
  | Name 	| Action butonun adının tanımlandığı alandır. Alanda ekli diğer ögelerdeki name alanlarında tanımlanmış değerlerden farklı olmalıdır, aynı değer yazılırsa ekleme işlemi yapılmaz. 	|
  | Text 	| Action butonun web ara yüzünde gösterileceği başlığın tanımlandığı alandır. 	|
  | Title 	| Action butonun web ara yüzünde fare imleci ile üzerine gelindiğinde gösterilecek bilginin tanımlandığı alandır. 	|
  | Icon 	| Action buton ikon ile birlikte gösterilmek istenirse, ikonun seçildiği alandır. 	|
  | Visible 	| Action butonun web ara yüzünde görünürlüğünün belirlendiği seçenektir. 	|

  **Ok Button Properties**

  | **Özellik** 	| **Açıklama** 	|
  |---	|---	|
  | Text 	| Selection form panelindeki tamam butonu yanında yazılması istenen ifadenin tanımlandığı alandır. 	|
  | Title 	| Selection form panelinde tamam butonu üzerine fare işaretçisi ile üzerine gelindiğinde gösterilecek bilginin tanımlandığı alandır. 	|
  | Icon 	| Selection form panelinde tamam butonun ikonunun belirlendiği alandır. 	|

  **Data Source**

  | **Özellik** 	| **Açıklama** 	|
  |---	|---	|
  | DataSource 	| Selection form içinde gösterilecek verilerin bulunduğu projedeki veri kaynağının seçildiği alandır. 	|
  | Columns 	| DataSource alanında seçilen veri kaynağına göre, veri kaynağından gelen kolonların üretildiği alandır. Alan içindeki Kolonları Üret botonuna tıklanarak, tanımlı veri kaynağında kolon tiplerine uygun kolonlar üretilecektir. Üretilen kolonlardan bir tanesinin birincil anahtar olarak işaretlenmesi, seçim işleminde aynı ögelerin olduğu satırlar bulunduğunda hepsinin seçilmesini önlemektedir. 	|
  | Column Map 	| Nesne kolonları ve Columns alanında üretilen kolonların eşleştirildiği alandır. Nesne kolonlarında seçim yaparken Columns alanındaki uygun kolon tipi seçilebilir olacaktır. Örneğin nesnede kolon tipi text tipinde ise, seçim listesinde text tipindeki kolonlar listelenir. Diğer türdeki kolonlar listelenmez. 	|

  **Columns Settings**

  | **Özellik** 	| **Açıklama** 	|
  |---	|---	|
  | Enabled 	| Columns Settings altındaki Orderable ve Resizeable özelliklerinin kullanılması için aktif edilmesi gereken özelliktir. 	|
  | Orderable 	| Aktif edildiğinde selection formdaki kolonların kendi içinde sırasını değiştirilmesi istenirse özellik aktif edilmelidir. 	|
  | Resizeable 	| Aktif edildiğinde selection formdaki kolonun sağa veya sola doğru genişletilip daraltılabilmesini sağlayan özelliktir. 	|

  **Filtering Settings**

  | **Özellik** 	| **Açıklama** 	|
  |---	|---	|
  | Enabled 	| Alan aktif edilerek selection form içinde her kolon başlığında filtreleme özelliği kullanılabilir durumda olur. Kolon tipine göre filtre türleri değişiklik gösterebilir.  	|

  **Paging Settings**

  | **Özellik** 	| **Açıklama** 	|
  |---	|---	|
  | Enabled 	| Selection formda listelenen verilerin sayfalar şeklinde gösterilip gösterilmeyeceğinin ayarlandığı özelliktir. Bu özellik pasif yapıldığında, bağlı olan data source içinde ne kadar kayıt varsa alt alta listelenir. Özellik aktif edildiğinde veriler, sayfalar şeklinde gösterilir. 	|
  | Current Page 	| Selection form web arayüzünde açıldığında, burada belirtilen sayfadan açılmasını sağlamak için kullanılan özelliktir. 	|
  | Paging Size 	| Sayfa başına kayıt sayısı gösterim ayarlarının yapıldığı özelliktir. Varsayılan olarak 10, 20, 30, 40 değerlerini alır. Bir sayfada kaç satır gösterilmek isteniyorsa bu alandan ayarlanabilir. 	|

  **Seaching Settings**

  | **Özellik** 	| **Açıklama** 	|
  |---	|---	|
  | Enabled 	| Özellik aktif edildiğinde, selection form yapısının üzerinde arama çubuğu belirir. Ve bu arama çubuğuna yazılan değer, formun tüm kolonlarında aratılarak, eşleyen satırların listelenmesi sağlanır. 	|

  **Selection Settings**

  | **Özellik** 	| **Açıklama** 	|
  |---	|---	|
  | Enabled 	| Selection formda tablo satırları içerisinden satır seçebilmek için bu özellik aktif edilmelidir. 	|
  | Mode 	| Seçim modunun seçileceği alandır. "Single" ve "Multiple" seçeneklerini barındırır. Selection form içindeki ögelerde sadece tek bir satır seçilmek istenirse "Single", birden çok satırı seçilmek istenirse "Multiple" modu seçilmelidir. 	|
  | Show Select All 	| Bu özellik aktif edildiğinde, sütun başlıklarının yanında tümünü seç butonu aktif olur. Eğer Mode alanında **multiple** seçili ise selection form içinde tümünü seç checkbox'ı görünür hale geçer. Tümünü Seç butonuna tıklandığında Select All Mode özelliğinde yapılan seçime göre sayfada veya bütün sayfalarda tüm satırlar seçili hale gelir. Butona tekrar tıklandığında satır seçimleri kaldırılır. 	|
  | Select All Mode 	| Show Select All özelliği ile birlikte çalışır. **page** seçili ise Select All ile yapılan seçimle sadece görüntülenen sayfadaki ögeler seçilir, **allPage** seçili ise Tümünü Seç işleminde yapılan seçimde bütün sayfalardaki ögeler seçilir.  	|
  | Show CheckBoxes Mode 	| Selection formda seçim sütununda ve satır seçimi işleminde checkbox'ların ne zaman görüntüleneceği belirler. Yapılan seçim mode alanında **multiple** seçili olduğunda geçerlidir.<br/>always: Tüm onay kutularını içeren seçim sütunu her zaman görünür durumdadır. Kullanıcı, onay kutusunu veya onay kutusunun bulunduğu hücreyi tıklayarak bir satırı seçebilir, ancak satırın kendisini tıklayarak seçim işlemini yapamaz.<br/>none: Tüm onay kutularını içeren seçim sütunu gizlenir. Kullanıcılar klavye kısayolları veya uzun dokunma (tıkla ve basılı tut) ile satırları seçebilir.<br/>onClick: Seçim sütunu her zaman gösterilir. Kullanıcı sütunu tıkladığında veya iki veya daha fazla satır seçildiğinde onay kutuları görünür. Satır seçimi iptal edildiğinde onay kutuları kaybolur.<br/>onLongTap: Tüm onay kutularını içeren seçim sütunu, satırlara uzun dokunulduğunda (tıklayın ve basılı tutun) görünür ve kaybolur. 	|

  **Sorting Settings**

  | **Özellik** 	| **Açıklama** 	|
  |---	|---	|
  | Enabled 	| Selection formda tablo kolonları içinde sıralama işlemi yapılabilmesi için özellik aktif edilmelidir. 	|
  | All Sorting Columns 	| Aktif olduğunda kolondaki sıralamanın diğer satırların da sırasını değiştirmesini sağlar. 	|
  | Mode 	| Sıralama modunu belirtir.<br/>none: Satırlarda sıralama işlemi yapılamaz<br/>single: Satırlar yalnızca tek bir sütunun değerlerine göre sıralanabilir.<br/>multiple: Satırlar birkaç sütunun değerlerine göre sıralanabilir. 	|

  **Action Type Properties**

  | **Özellik** 	| **Açıklama** 	|
  |---	|---	|
  | Panel Size 	| Action buton ile açılacak formun boyutunun belirlendiği alandır 1-2 veya 3 değerleri seçilebilir. Seçilen değerler Show On özelliğinde Panel seçiminde etkili olacak olup, Modal veya Drawer seçildiğinde Panel Size'a girilen değer etki etmeyecektir. 	|
  | Show On 	| Action buton ile açılacak formun tipte açılacağını belirlemek için kullanılır.<br/>Panel: Form panel görünümde açılmak istenirse seçilmelidir. Varsayılan açılma tipidir, panel büyüklüğü Panel Size alanında 1-2-3 değerleri seçilerek değiştirilebilmektedir.<br/>Modal: Form ekranın ortasında, ekranı kaplayacak şekilde açılması istenirse seçilmelidir. Panel Size alanında yapılan seçim modal ile açılmayı etkilemez.<br/>Drawer: Form ekranın sağından kayarak panelin gösterilmesi istenirse seçilmelidir. Açılan form mevcut sayfanın üstünde gösterilir. Panel Size alanında yapılan seçim drawer ile açılmayı etkilemez. 	|

  </div>
</details>

  - `Execute Custom Action` - Mevcut butonlar dışında formun .ts veya .cs alanlarında kod ile butona tıklanıldığında farklı işlemler yapılmak istendiğinde kullanılabilecek buton türüdür.

<details>
  <summary>Execute Custom Action butonun özellikleri için tıklayın</summary>
  <div>

  **Button Properties**

  | **Özellik** 	| **Açıklama** 	|
  |---	|---	|
  | Name 	| Action butonun adının tanımlandığı alandır. Alanda ekli diğer ögelerdeki name alanlarında tanımlanmış değerlerden farklı olmalıdır, aynı değer yazılırsa ekleme işlemi yapılmaz. 	|
  | Text 	| Action butonun web ara yüzünde gösterileceği başlığın tanımlandığı alandır. 	|
  | Title 	| Action butonun web ara yüzünde fare imleci ile üzerine gelindiğinde gösterilecek bilginin tanımlandığı alandır. 	|
  | Icon 	| Action buton ikon ile birlikte gösterilmek istenirse, ikonun seçildiği alandır. 	|
  | Visible 	| Action butonun web ara yüzünde görünürlüğünün belirlendiği seçenektir. 	|

  </div>
</details>

### Data Definition Language

`Field Name` - Sistemin veri tabanında, nesne için oluşturacağı kolonun adının belirlendiği alandır. "İsim (Name)" kısmında nesneye başka bir isim verilip, veritabanı tablosunda nesne için oluşturulacak kolon adı farklı bir isim olarak yaratılabilir.

## Olaylar

Nesnenin sahip olduğu olaylar, Özellik Görüntüleyici panelindeki "Olaylar" sekmesinde yer almaktadır. Her bir olay, farklı çalışma anlarında tetiklenerek kendilerine özgü işlemleri gerçekleştirir. Bu olaylara geliştirici tarafından yazılan kodlar da ilgili olayın tetiklendiği anda çalıştırılır.

"Client" alanında bulunan olaylara çift tıklandığında ekran, TypeScript kodlamanın yapılabileceği "Formadı.ts" isimli form kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur.

"Server" alanında bulunan olaylara çift tıklandığında ekran, C# kodlamanın yapılabileceği "Formadı.cs" isimli form kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur.

Geliştirici bu methodlar içerisinde istediği kod bloğunu kurgulayabilir. Olaylar sekmesinden tıklanarak kod tarafında methodu oluşturulmuş olayın yanında, method adı bilgisi otomatik oluşturularak, olayla method arasındaki ilişki belirtilmiş olur.

![DataGrid](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload15b50f46-9de2-46f2-8c82-5b65f73ee923)

![DataGrid](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1aa4873e-2755-4176-a644-cf069f2a37c2)

![DataGrid](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadeab95d76-d770-4cfd-aefe-716501633136)