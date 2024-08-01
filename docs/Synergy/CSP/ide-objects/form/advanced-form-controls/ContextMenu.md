---
sidebar_position: 14
custom_edit_url: ""
---

# ContextMenu

DataGrid ve TreeView nesnelerinde farenin sağ tıklama işlemi ile bağlam menüsü açılıp, menüde Open A Process, Open A Form vb., özelleştirilmiş görevler tanımlanarak, sağ tık ile işlem yapmayı sağlayan nesnedir. Nesne geliştirme ortamında form üzerine eklendiğinde web ara yüzünde gözükmemektedir, nesnenin DataGrid veya TreeView nesnelerinde tanımlanarak kulanılmaktadır.

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

### Datasource

`Type` - Nesneye hangi tipte veri ekleneceğinin seçimi bu alandan yapılır. Tip alanında "Dinamik" ve "Statik" olarak iki seçenek listelenir. Seçim yapılan tipe göre veri kaynağı bölümünde görünen özellikler değişiklik gösterecektir.

Seçenek olarak "Dinamik" seçildiğinde; nesneye veriler, bir veri kaynağından dinamik olarak yüklenecek demektir. Dinamik seçeneği seçildiğinde Datasource alanında Datasource ve Run at Server özellikleri görünür olacaktır.

Seçenek olarak "Statik" seçildiğinde ise, nesneye manuel eleman eklenecek demektir ve veri kaynağı alanında Items özelliği görünür olur.

:::note

Bu kısımdan itibaren nesnede type alanında **dinamik** değeri seçilirse nesne kullanımı açıklanacaktır. **Statik** kullanımdaki özellikleri görüntülemek için ilgili bölümü açabilirsiniz.

:::

<details>
  <summary>Dinamik kullanım detaylarını görüntülemek için tıklayın!</summary>
  <div>

`DataSource` - Nesnede, bir veri kaynağından gelen değerleri listeleyebilmek için kullanılacak alandır. Projede Çözüm Gezgini alanındaki DataSource bölümüne eklenmiş ve başarıyla derlenen veri kaynağı tanımı, nesnenin Datasource) kısmından seçilebilir olur.

`RunAtServer` - Bu seçenek nesneye bağlanan sorgunun, sunucudan mı istemciden mi çalıştırılacağının belirlendiği seçenektir.

Bu seçenek aktif edilirse web arayüzünde forma tıklandığında, form açılmadan önce sorgu, sunucu tarafında çalıştırılır, form açıldığında nesneye sorgu sonucu yüklenmiş olarak gelir. Seçenek pasif yapıldığında web arayüzünde forma tıklandığında, form açıldıktan sonra nesneye sorgunun sonuç değerleri yüklenmeye başlar.

Sorgu sonucunun yüklenmesi için geçen bekleme süresi, bu özellik aktifken formun açılma anında, özellik pasifken form hızlı açıldıktan sonra nesneye verinin yüklenmesi anında etkili olur.

`Value Expression` - Veri Kaynağı kısmından bir veri kaynağı tanımı seçildiğinde bu alan görünür olur. Seçilen veri kaynağından dönen tüm kolonlar bu alanda listelenir. Kullanıcı arayüzden seçim yaptığında, yapılan seçimin kayıt alanının hangi kolon değeri olacağı bu alanda belirlenir.

Örneğin nesneye kullanıcıların listesini getiren bir sorgu bağlanmış olsun. Sorgudan ID (Kullanıcı Adı), FIRSTNAME (İsim), EMAIL (Mail Adresi) kolonları dönüyor olsun. Bu nesnenin amacı kullanıcı seçimi olduğu için seçilen kullanıcının benzersiz kayıt değeri ID kolonunda bulunduğundan, Değer İfadesi kısmında sorgudan dönen ID kolonu seçilmelidir.

`Display Expression` - Veri Kaynağı kısmından bir veri kaynağı tanımı seçildiğinde bu alan görünür olur. Seçilen veri kaynağından dönen tüm kolonlar bu alanda listelenir. Kullanıcı arayüzden seçim yaptığında, nesne içerisinde görünecek ifadenin hangi sorgu kolonundan geleceği bu alanda belirlenir.

Örneğin nesneye kullanıcıların listesini getiren bir sorgu bağlanmış olsun. Sorgudan ID (Kullanıcı Adı), FIRSTNAME (İsim), LASTNAME (Soyisim), EMAIL (Mail Adresi) kolonları dönüyor olsun. Bu nesnenin amacı kullanıcı seçimi olduğu için seçilen kullanıcının FIRSTNAME ve LASTNAME kolonlarından dönen değerleri nesne içinde görüntülenmek istenecektir. O yüzden Görünür İfadesi kısmında bu kolon değerleri seçilir.

`Display Format` - Görünüm İfadesi alanından seçilen kolon ya da kolonlar otomatik olarak bu alana da eklenir. Nesnede listelenecek eleman metinlerine görünüm formatı belirlemek için kullanılan alandır. Elemanların istenen bir formatta gösterilmesi için, ilgili format yapısı bu alanda belirtilebilir. Ve nesne seçimi sonrası nesnede görüntülenecek değerin web arayüzde uç kullanıcılara belirlenen formatta görünmesi sağlanabilir.

Formatlamada kullanılabilecek format tiplerine, alana odaklanıldığında çıkan bilgi mesajındaki linkten (https://shopify.github.io/liquid/) erişilebilir ve gerçekleştirilmek istenen format yapısı Görünüm Formatı alanında ilgili sütun için uygulanabilir.

`ItemsExpr` - Hangi veri alanının iç içe öğeleri içerdiğini belirtir.

`Parent Key` - Seçilen veri kaynağındaki bir üst öğenin (parent item) tanımlayıcısını belirtir.

  </div>
</details>

:::note

Bu kısımdan itibaren nesnede type alanında **statik** değeri seçilirse nesne kullanımı açıklanacaktır. **Dinamik** kullanımdaki özellikleri görüntülemek için ilgili bölümü açabilirsiniz.

:::

<details>
  <summary>Statik kullanım detaylarını görüntülemek için tıklayın!</summary>
  <div>

`Items` - Nesnede, bir veri kaynağından gelen kayıtlar değil, geliştirme anında manuel eklenen elemanlar listelenmek istendiğinde, eleman tanımlama işlemi bu alandan yapılır. Liste elemanlarının belirlendiği kısımdır. Bu alandan nesneye yeni eleman eklenebilir, mevcut bir eleman silinebilir veya düzenlenebilir. Elemanlar alanına tıklandığında eleman ekleme penceresi açılır. Ekle butonuna tıklanarak nesneye yeni eleman kalemleri oluşturulur.

`Key` - Ögeye verilecek anahtar değeri bu alana yazılır, ekli diğer ögelerdeki key alanlarında tanımlanmış değerlerden farklı olmalıdır, aynı değer yazılırsa ekleme işlemi yapılmaz.

`Text` - Ögeye verilecek isim bu alana yazılır.

`Title` - Ögeye fare işaretçisi ile gelindiğinde gösterilecek isim bu alana yazılır. 

`Icon` - Ögenin ikona sahip olması istenirse bu alandan seçim yapılmalıdır.

`Items` - Öge altında olması istenen başka bir eleman daha varsa Items’taki üç noktaya tıklanarak ekleme yapılabilir. Açılan pencerede ekle butonuna basıldığında gelen özellikler bir önceki pencere ile aynı olup, “Kaydet” butonuna tıklanarak çocuk elemanlar ana elemanın altına gelecek şekilde kaydedilir.

  </div>
</details>

### Appearance

`Visible` - Nesnenin gizlenip, görünür yapılma ayarlarının gerçekleştirildiği kısımdır. Bu alan aktifken, nesne form üzerinde görünür durumdadır. Alan pasif yapıldığında nesne görünmez olur.

`Client Visible` - Form ilk açıldığında nesne görünmesin, belirli bir şart sağlandığında nesne görünür olsun gibi bir işlem yapılmak istendiğinde, nesnenin istemci tarafında görünmez olması için bu alan pasif yapılır. Kodla ya da Kural Yöneticisi ile belirlenen şart sağlandığında nesne tekrar görünür hale getirilebilir. Sunucu görünürlüğü aktif değilken, istemci müdahale edemez ancak istemci görünürlüğü aktif değilken sunucu müdahale edebilir.

`Enabled` - Nesnenin etkin modu bu alandan ayarlanır. Bu özellik aktifken nesneye veri girişi sağlanabilir ve nesne düzenlenebilir. Özellik pasifken, nesne düzenlenemez moddadır ve pasif görünür.

`Client Enabled` - Form ilk açıldığında nesne etkin olmasın, belirli bir şart sağlandığında etkin olsun gibi bir işlem yapılmak istendiğinde, nesnenin istemci tarafında etkin olmaması için bu alan pasif yapılır. Kodla ya da Kural Yöneticisi ile belirlenen şart sağlandığında nesne tekrar etkin hale getirilebilir. Sunucu etkinliği aktif değilken, istemci müdahale edemez ancak istemci etkinliği aktif değilken sunucu müdahale edebilir.

`Background Color` - Nesneye arka plan rengi vermek için kullanılan alandır.

`Title` - Form arayüzde açıkken imleç ile nesne üzerine gelindiğinde, bu alanda yazılan metin, ipucu olarak gösterilir. Nesne ile ilgili detay bilgi verilmek istendiğinde kullanılan, uç kullanıcıyı yönlendirme amaçlı bir özelliktir.

`ClassName` - Forma ait CSS dosyası içinde yazılmış bir class'ın tanımlanarak nesne görünürlüğünün değiştirilebildiği alandır.

`Action Buttons` - ContextMenu içinde aksiyon butonu eklenerek Open A Form, Open A Process, Create A Form, Start A Process, Open A Selection Form, Execute Custom Action işlemlerinin yapılması istenildiğinde kullanılacak alandır.

- `Create A Form` - Tıklandığında butona tanımlanan sistemde yeni bir form oluşturulup uç kullanıcının işlem yapabileceği buton türüdür.

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

- `Open A Form` - Sistemdeki mevcut formun görüntülenmesi istenirse kullanılacak buton türüdür. Buton ile sadece form görüntülenmesi sağlanır, akış tarihçesi hakkında bilgi gösterilmesi istenirse Open A Process butonu kullanılmalıdır.

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

- `Open A Process` - Sistemdeki mevcut sürecin görüntülenmesi istenirse kullanılacak buton türüdür. Buton ile akış tarihçesi gibi bilgiler erişilebilir olmaktadır. Sadece formun görüntülenmesi istenirse Open A Form tipinde buton kullanılmalıdır.

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

- `Start A Process` - Tıklandığında butona tanımlanan sistemde yeni bir süreç oluşturulup uç kullanıcının işlem yapabileceği buton türüdür.

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

- `Open A Selection Form` - Tıklandığında butona tanımlanan veri kaynağına tanımlı bir seçim formunu açarak uç kullanıcının işlem yapabileceği buton türüdür.

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
| Mode 	| Sıralama modunu belirtir.<br/>none: Satırlarda sıralama işlemi yapılamaz<br/>single: Satırlar yalnızca tek bir sütunun değerlerine göre sıralanabilir.<br/>multple: Satırlar birkaç sütunun değerlerine göre sıralanabilir. 	|

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

## Olaylar

Nesnenin sahip olduğu olaylar, Özellik Görüntüleyici panelindeki “Olaylar” sekmesinde yer almaktadır. Her bir olay, farklı çalışma anlarında tetiklenerek kendilerine özgü işlemleri gerçekleştirir. Bu olaylara geliştirici tarafından yazılan kodlar da ilgili olayın tetiklendiği anda çalıştırılır.

“Client” alanında bulunan olaylara çift tıklandığında ekran, TypeScript kodlamanın yapılabileceği “Formadı.ts” isimli form kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur.

“Server” alanında bulunan olaylara çift tıklandığında ekran, C# kodlamanın yapılabileceği “Formadı.cs” isimli form kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur.

Geliştirici bu methodlar içerisinde istediği kod bloğunu kurgulayabilir. Olaylar sekmesinden tıklanarak kod tarafında methodu oluşturulmuş olayın yanında, method adı bilgisi otomatik oluşturularak, olayla method arasındaki ilişki belirtilmiş olur.