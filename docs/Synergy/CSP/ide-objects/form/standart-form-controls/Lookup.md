---
sidebar_position: 7
custom_edit_url: ""
---

# Lookup

Bir veri kaynağından gelen değerleri ya da geliştiricinin eleman olarak eklediği değerleri, web arayüzünde kullanıcıya tablo yapısı şeklinde sunan ve bu veriler arasından eleman seçtirmeye yarayan nesnedir.

Kaynaktan çok sayıda veri geliyorsa, ComboBox nesnesinde bu verileri liste şeklinde göstermek yerine, Lookup nesnesinde tablo yapısında göstermek tercih edilir.

Geliştirme arayüzünde aktif ekran form iken, Araç Kutusu panelinde form nesneleri listelenir. Nesne, araç kutusu panelinden sürükle/bırak yöntemi ile forma eklenir.

![Lookup](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload79089093-ade7-4d6d-a1b1-f9014c22888b)

Nesnenin üzerine tıklandığında Özellik Görüntüleyici panelinde "Genel" ve "Olaylar" sekmeleri yer alır ve nesneye ait özellikler görüntülenip, düzenlenebilir. Nesne özelliklerinin aktarıldığı kalıtım şeması aşağıdaki gibidir;

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

`DataSource` - Nesnede, bir veri kaynağından gelen değerleri listeleyebilmek için kullanılacak alandır. Projede Çözüm Gezgini alanındaki DataSource bölümüne eklenmiş ve başarıyla derlenen veri kaynağı tanımı, nesnenin Datasource) kısmından seçilebilir olur.

![Lookup](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0330d6e4-a88c-4add-bfed-e1b8a69d8910)

![Lookup](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload812d33f9-4730-4b92-9b20-9904a6531ecf)

`RunAtServer` - Bu seçenek nesneye bağlanan sorgunun, sunucudan mı istemciden mi çalıştırılacağının belirlendiği seçenektir.

Bu seçenek aktif edilirse web arayüzünde forma tıklandığında, form açılmadan önce sorgu, sunucu tarafında çalıştırılır, form açıldığında nesneye sorgu sonucu yüklenmiş olarak gelir. Seçenek pasif yapıldığında web arayüzünde forma tıklandığında, form açıldıktan sonra nesneye sorgunun sonuç değerleri yüklenmeye başlar.

Sorgu sonucunun yüklenmesi için geçen bekleme süresi, bu özellik aktifken formun açılma anında, özellik pasifken form hızlı açıldıktan sonra nesneye verinin yüklenmesi anında etkili olur.

`Value Expression` - Veri Kaynağı kısmından bir veri kaynağı tanımı seçildiğinde bu alan görünür olur. Seçilen veri kaynağından dönen tüm kolonlar bu alanda listelenir. Kullanıcı arayüzden seçim yaptığında, yapılan seçimin kayıt alanının hangi kolon değeri olacağı bu alanda belirlenir.

Örneğin nesneye kullanıcıların listesini getiren bir sorgu bağlanmış olsun. Sorgudan ID (Kullanıcı Adı), FIRSTNAME (İsim), EMAIL (Mail Adresi) kolonları dönüyor olsun. Bu nesnenin amacı kullanıcı seçimi olduğu için seçilen kullanıcının benzersiz kayıt değeri ID kolonunda bulunduğundan, Değer İfadesi kısmında sorgudan dönen ID kolonu seçilmelidir.

![Lookup](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload53a12ea2-23b0-401f-a23e-97181f5d75c0)

`Display Expression` - Veri Kaynağı kısmından bir veri kaynağı tanımı seçildiğinde bu alan görünür olur. Seçilen veri kaynağından dönen tüm kolonlar bu alanda listelenir. Kullanıcı arayüzden seçim yaptığında, nesne içerisinde görünecek ifadenin hangi sorgu kolonundan geleceği bu alanda belirlenir.

Örneğin nesneye kullanıcıların listesini getiren bir sorgu bağlanmış olsun. Sorgudan ID (Kullanıcı Adı), FIRSTNAME (İsim), LASTNAME (Soyisim), EMAIL (Mail Adresi) kolonları dönüyor olsun. Bu nesnenin amacı kullanıcı seçimi olduğu için seçilen kullanıcının FIRSTNAME ve LASTNAME kolonlarından dönen değerleri nesne içinde görüntülenmek istenecektir. O yüzden Görünür İfadesi kısmında bu kolon değerleri seçilir.

![Lookup](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload47162f36-bd63-4faa-a95f-2bb6ac143f4b)

`Display Format` - Görünüm İfadesi alanından seçilen kolon ya da kolonlar otomatik olarak bu alana da eklenir. Nesnede listelenecek eleman metinlerine görünüm formatı belirlemek için kullanılan alandır. Elemanların istenen bir formatta gösterilmesi için, ilgili format yapısı bu alanda belirtilebilir. Ve nesne seçimi sonrası nesnede görüntülenecek değerin web arayüzde uç kullanıcılara belirlenen formatta görünmesi sağlanabilir.

Formatlamada kullanılabilecek format tiplerine, alana odaklanıldığında çıkan bilgi mesajındaki linkten (https://shopify.github.io/liquid/) erişilebilir ve gerçekleştirilmek istenen format yapısı Görünüm Formatı alanında ilgili sütun için uygulanabilir.

![Lookup](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada8f17840-d58e-4c48-bf78-f4ecde6a6e5f)

:::note NOT

Görünüm Formatı örnek uygulamaları için **[Display Format Örnekleri](code-samples/liquid-display-format.md)** dokümanını inceleyebilirsiniz.

:::

### Appearance

`Visible` - Nesnenin gizlenip, görünür yapılma ayarlarının gerçekleştirildiği kısımdır. Bu alan aktifken, nesne form üzerinde görünür durumdadır. Alan pasif yapıldığında nesne görünmez olur.

`Client Visible` - Form ilk açıldığında nesne görünmesin, belirli bir şart sağlandığında nesne görünür olsun gibi bir işlem yapılmak istendiğinde, nesnenin istemci tarafında görünmez olması için bu alan pasif yapılır. Kodla ya da Kural Yöneticisi ile belirlenen şart sağlandığında nesne tekrar görünür hale getirilebilir. Sunucu görünürlüğü aktif değilken, istemci müdahale edemez ancak istemci görünürlüğü aktif değilken sunucu müdahale edebilir.

`Enabled` - Nesnenin etkin modu bu alandan ayarlanır. Bu özellik aktifken nesneye veri girişi sağlanabilir ve nesne düzenlenebilir. Özellik pasifken, nesne düzenlenemez moddadır ve pasif görünür.

`Client Enabled` - Form ilk açıldığında nesne etkin olmasın, belirli bir şart sağlandığında etkin olsun gibi bir işlem yapılmak istendiğinde, nesnenin istemci tarafında etkin olmaması için bu alan pasif yapılır. Kodla ya da Kural Yöneticisi ile belirlenen şart sağlandığında nesne tekrar etkin hale getirilebilir. Sunucu etkinliği aktif değilken, istemci müdahale edemez ancak istemci etkinliği aktif değilken sunucu müdahale edebilir.

`Background Color` - Nesneye arka plan rengi vermek için kullanılan alandır.

`Title` - Form arayüzde açıkken imleç ile nesne üzerine gelindiğinde, bu alanda yazılan metin, ipucu olarak gösterilir. Nesne ile ilgili detay bilgi verilmek istendiğinde kullanılan, uç kullanıcıyı yönlendirme amaçlı bir özelliktir.

`ClassName` - Forma ait CSS dosyası içinde yazılmış bir class'ın tanımlanarak nesne görünürlüğünün değiştirilebildiği alandır.

`Size Type` - Nesne seçim alanı boyutunun ayarlandığı kısımdır.

>Yapılabilecek Seçimler : Small, Middle, Large

`Placeholder` - Nesne içine uç kullanıcı tarafından girilmesi istenen veri bilgisini, nesne içerisinde bilgi amaçlı göstermek için kullanılan özelliktir. Uç kullanıcı nesneyi görüntülediğinde bu alana yazılan yönlendirici metni görür, nesneye odaklandığında ve değer girmeye başladığında yönlendirici metin kaybolur.

![Lookup](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload78873bc4-8250-4de2-8822-39ff5fcb3948)

![Lookup](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf54e2861-53a4-4d19-bfdb-e14bb6252e99)

`Text Align` - Nesne içinde seçilen ögede, ögeye ait yazının nesne içinde nasıl hizalanacağını belirlemek için kullanılır. 

>Yapılabilecek Seçimler : Left, Center, Right

### Behavior

`ReadOnly` - Nesnenin düzenleme modunda olup olmayacağının ayarlandığı kısımdır. Bu özellik aktif edildiğinde nesne veri girişine izin vermez, salt okunur modda olur. Nesneye veri girişine izin verilmesi için özelliğin pasif olması gerekir.

`Tab Index` - Bu alana sayısal değerler girilerek, tab butonuna basıldığında form nesneleri arasında hangi sıra ile odaklanılacağı belirlenir. Form doldurulurken imleci, veri girilmek istenen nesneye tıklamak yerine, tab butonuna basarak belirli bir sırayla indekslenmiş nesnelere direk odaklanılması sağlanmış olur. Bu da form doldurma hızını artıran bir özelliktir.

`Required` - Nesnede veri girişinin zorunlu olup olmayacağının belirlendiği alandır. Bu özellik aktif edildiğinde nesne içerisine veri girişi yapılmadan formun ilerletilmesi/kaydedilmesi gerçekleştirilemez.

`Columns` - Web arayüzünde seçim yapmak için nesneye tıklandığında açılacak tablonun sütunlarının belirlendiği ve düzenlendiği alandır. 

Sütunlar kısmına tıklandığında tablo sütunlarının belirleneceği ve düzenleneceği pencere açılır. Bu pencerede **“+ Ekle”** butonu ile tabloya manuel kolonlar eklenebilir. **“Kolonları Üret”** butonu ile, nesneye bağlanan sorgudan dönen kolonlar üretme penceri içinde tek tek veya tümü seçilerek direkt olarak bu alana eklenebilir.

![Lookup](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload13928698-78e7-4d74-8ed4-b6422534bbc2)

Eklenmiş kolonlardan herhangi birine tıklandığında, sağ tarafta o kolona ait özellikler listelenir. Kolon özellikleri düzenlenebilir veya tabloda ilgili kolon gösterilmek istenmiyorsa çöp kutusu ikonuna tıklanarak “Eklenmiş Kolonlar” alanından kaldırılabilir.

Kolon özelliklerinin listelendiği bölümde Genel sekmesinde bulunan alanlar:

:::note NOT

Aşağıdaki liste nesnede Text kolonu türüne göre yazılmıştır.

:::

- `Name` - Kolon adı alanıdır. Kolon, “Ekle” butonu ile manuel oluşturulduysa bu alan düzenlenebilir olarak gelir. Kolon, “Kolonları Üret” butonu ile bu alana eklenmiş, sorgudan dönen bir kolon ismi otomatik olarak gelir.
- `Caption` - Kolon başlığı alanıdır. Tabloda gösterilmek istenen sütun adı buradan ayarlanır.
- `Width` - Kolon genişliğinin ayarlandığı alandır.
- `Visible` - Kolonun web arayüzde görünüp görünmeyeceğinin ayrlandığı kısımdır.
- `Disable to Export` - Tablo dışa aktarıldığında, özelliğin aktif edildiği kolonun aktarılmasını önlemek için kullanılan ayardır.
- `Allow Hiding` - Kolonun tablo gösterimi esnasında gizlenebilmesine izin verilmek istenirse aktif edilen ayardır. Nesnedeki Show Column Chooser ayarı ile birlikte kullanılır.
- `Cell Type` -Kolon tipi değeri bu alanda tutulur. Kolon, “Kolonları Üret” butonu ile bu alana eklenmiş, sorgudan dönen bir kolonsa bu alan salt okunur yapıdadır. “Ekle” butonu ile manuel oluşturulmuş bir kolonsa bu alan düzenlenebilir moddadır. Hücre Tipi alanında listelenen seçenekler aşağıdaki gibidir;

- Seçilebilecek kolon tipleri: Text, Number, Boolean, Date, Time, DateTime, Select, Multilanguage, Action Button

  - `Text` - Kolonda, metin tipinde veri tutuluyor demektir. Hücre tipi Text iken, Kontrol sekmesinde kolonun, veri tabanında tutulacak alanının isim, boyut ve nullable özelliklerinin belirleneceği alanlar açılır.
  - `Number` - Kolonda number tipinde bir değer tutulacaksa bu hücre tipi seçilir. Number tipli kolon için Genel sekmesinde, **Toplam**, **Maksimum“**, **Minimum**, **Ortalama** ve **Sayı** seçeneklerinin listelendiği Summary Types alanı ve kolon değerinin otomatik artıp artmayacağının belirleneceği Auto Increment alanı görünür olur.
  ![Lookup](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc2796f9d-901a-4d70-b84c-8df5c1663d48)
  - `Boolean` - Kolonda doğru / yanlış tipinde değer tutuluyor demektir.
  - `Select` - Select tipindeki bir kolonda, bir veri kaynağından gelen veriler veya manuel eklenen elemanlar listelenebilir. Web arayüzünde kullanıcı, Select kolonuna tıkladığında listelenen değerlerden seçim yapabilir. Hücre tipi olarak Select seçildiğinde Kontrol sekmesinde DataSource isimli bir alan açılır. Bu alanda, bir veri kaynağından getirilen değerler kolonda listelenmek istenirse Type olarak “Dinamik“, manuel eklenen değerler kolonda listelenmek istenirse Type olarak “Statik” seçeneği seçilmelidir.
  ![Lookup](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload543fd3f0-24a1-486f-8580-91f9bc5830eb)
  - `Action Button` - Kolona, tıklandığında belirli bir işlemi yapmak üzere tasarlanmış bir aksiyon butonu eklemeye yarayan hücre tipidir. Hücre tipi olarak Action Button seçildiğinde ekranda Aksiyon Butonu isimli bir sekme belirecektir. Web arayüzünde, kolondaki bu butona tıklandığında hangi işlemin yapılacağı aksiyon butonu sekmesinde belirtilir. Aksiyon butonu sekmesinde Type alanında, aksiyon seçimi yapılmaktadır. Burada listelenen aksiyon seçeneklerine göre, web arayüzünde bu aksiyon butonuna tıklandığında, **Create a Form, Open a Form, Open a Process, Open a Selection Form, Execute Custom Action** işlemleri gerçekleştirilebilmektedir.
  ![Lookup](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload623d0167-2644-415e-a827-15fd79291a41)
  
  Seçilen her bir aksiyon tipine göre, Aksiyon Özellikleri bölümünde doldurulması gereken alanlar değişiklik gösterir.

  | **İşlem** 	| **Gerekli Bilgi** 	|
  |---	|---	|
  | Oluşturulacak formun 	| Proje Adı, Form Adı 	|
  | Açılacak formun 	| Doküman id değeri 	|
  | Açılacak sürecin 	| Süreç id ve Süreç İstek id değerleri 	|
  | Açılacak seçili formun 	| Değerlerini getirecek veri bağlantılarının tanımlanması 	|
  | Başlatılacak sürecin 	| Süreç adı ve Akış Adı değerleri 	|

  Eklenmiş kolonlar alanında listelenen kolonlardan, ilgili veriyi barındıran kolonun seçimi yapılarak doldurulmalıdır.

  - `Date` - İçinde tarih tipinde veri barındıran kolonların hücre tipi değeridir.
  - `Time` - İçinde saat tipinde veri barındıran kolonların hücre tipi değeridir.
  - `DateTime` - İçinde tarih ve saat tipinde veri barındıran kolonların  hücre tipi değeridir.

- `Align` - Kolonu sağa, sola veya ortaya hizalama ayarı bu alandan yapılır.
- `Allow Null` - Kolonda boş değere izin verilmek isteniyorsa bu alandan yapılır.
- `Icon Source Field` - Seçilen kolon adına göre, o kolondaki değer şartı sağlandığında özelliğin aktif olduğu kolonda ikon gösterimi sağlanır. Örneğin Kolon1 içinde alanda Kolon1 ve Kolon2 listelensin. Kolon1 seçildiğinde, bu kolon için oluşturulacak şartlara göre özelliğin aktif olduğu kolonda şartların sağlandığı değerlerde ikonlar gösterilecektir.
- `Icon Matchers` - Icon Source Field alanında seçilen kolondaki hangi değerde hangi ikonunun gösterileceği şartlarını oluşturmak için kullanılır.
- `Header Filter Enabled` - Kolonda, kolon başlığı filtresi ile kolondaki verileri seçerek filtrelemeyi aktif etmek için kullanılır.
- `Is Primary Key` - Eklenmiş kolonlar alanında bulunan kolonlardan en az biri birincil anahtar olarak seçilmelidir. Kayıtlar için benzersiz değer taşıyan kolon, birincil anahtar olarak işaretlenir. Eklenmiş kolonlar arasında benzersiz kolon bulunmuyorsa, “Ekle” butonu ile Number tipte bir kolon eklenip, otomatik artış özelliği aktif edilerek, her kayıt için benzersiz numara kolonu oluşturulup, bu kolon birincil anahtar olarak belirlenebilir.
- `Editing Enabled` - Kolonun düzenlenebilip düzenlenemeyeceği buradan ayarlanır.

:::info BİLGİ

Bu kısımdan itibaren kolon özellikleri açıklaması tamamlanmış olup, nesne özelliklerine devam edilecektir.

:::

`Allow Clear` - Nesnede seçilen değeri temizlemek için kullanılan özelliktir. Bu özellik aktif edildiğinde web arayüzünde kullanıcı nesneden bir seçim yaptığında, nesne kenarında × (Çarpı) işareti belirir. Çarpı işaretine basılarak seçilen değer silinip, başka bir nesne elemanının seçimi sağlanabilir.

![Lookup](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaf847c79-aeca-4cd6-94e1-4987109c3c91)

`Value Type` - Nesne elemanlarının tipinin belirlendiği alandır. Burada belirlenen tipe göre, Elemanlar alanında eklenen satırın Değer alanı tipi değiştirilir. Aynı zamanda nesneye parametrik bir sorgu bağlandığında, parametre tipi ile Değer Tipi alanından seçilen tip değeri aynı olmalıdır. 

>Yapılabilecek Seçimler : string, boolean, integer, decimal, date

### Column Settings

`Orderable` - Nesne içinde seçim panelindeki tablo kolonlarını sürükle – bırak yöntemi ile sıralamaya yarayan özelliktir. Kolon adına tıklanıp, istenilen yere bırakılarak kolonlar arası yer değiştirme yapılabilir.

`Show Column Chooser` - Nesne içinde seçim panelinde Allow Hiding özelliği açık olan tablo kolonları öge seçimi esnasında gizlenebilmesi istenirse, tablo üzerinde kolon seçici pop-up'ını aktif edecektir.

`Resizeable` - Sütun genişliğini büyütüp küçültmeye yarayan özelliktir.

### Filtering Settings

`Enabled` - Bu özellik aktif edildiğinde nesne içinde seçim panelindeki tablo kolonlarında, her bir kolonun altına filtre alanları açılır. Filtre alanına yazılan değer, kolon kayıtları arasında filtrelenerek, ilgili kayıtlar listelenir.

![Lookup](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbcaedbb9-a277-4e83-bb55-cb65c8d239fb)

### Paging Settings

`Enabled` - Tabloda listelenen verilerin sayfalar şeklinde gösterilip gösterilmeyeceğinin ayarlandığı özelliktir. Bu özellik pasif yapıldığında, tabloda ne kadar kayıt varsa alt alta listelenir. Özellik aktif edildiğinde veriler, sayfalar şeklinde gösterilir.

`Current Page` - Nesnenin, web arayüzünde açıldığında, burada belirtilen sayfadan açılmasını sağlamak için kullanılan özelliktir.

`Paging Size` - Sayfa başına kayıt sayısı gösterim ayarlarının yapıldığı özelliktir. Varsayılan olarak 10, 20, 30, 40 değerlerini alır. Bir sayfada kaç satır gösterilmek isteniyorsa bu alandan ayarlanabilir.

### Searching Settings

`Enabled` - Özellik aktif edildiğinde, tablo yapısının üzerinde arama çubuğu belirir. Ve bu arama çubuğuna yazılan değer, tablonun tüm kolonlarında aratılarak, eşleyen satırların listelenmesi sağlanır.

![Lookup](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload67b48d58-3277-41f4-81c5-06bd502e8f9a)

### Sorting Settings

`Mode` - Tablo kayıtları arasında sıralama yapılmasını sağlayan özelliktir. Herhangi bir kolona tıklandığında, kolon içindeki verilerin artan ya da azalan sıralamaya göre listelenmesini sağlar. 

>Yapılabilecek Seçimler : none, single, multiple

![Lookup](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb33143e2-7683-4788-a5a9-2ad4385fea27)

:::info BİLGİ

Mode alanında listelenen değerlerde, **None** seçeneği, sıralama yapılmayacak demektir. **Single** seçeneği ile sadece tek bir kolona göre sıralama yapılabilir. **Multiple** seçeneği ile birden fazla kolon sıralanabilir demektir.

:::

### Selection Settings

`Mode` - Tablo kayıtları arasında sadece bir öge veya birden fazla ögenin seçilebilmesini sağlayan özelliktir. Signle seçildiğinde sadece bir öge seçimi yapılabilirken, multiple seçildiğinde birden fazla öge seçilebilecektir.

>Yapılabilecek Seçimler : single, multiple

### Data Definition Language

`Field Name` - Sistemin veri tabanında, nesne için oluşturacağı kolonun adının belirlendiği alandır. “Name” kısmında nesneye başka bir isim verilip, veritabanı tablosunda nesne için oluşturulacak kolon adı farklı bir isim olarak yaratılabilir.

`Allow Null` - Nesne için oluşturulacak veritabanı alanının boş(null) değerlere izin verip vermeyeceği bu kısımdan belirtilir.

`Size` - Nesnenin veritabanı alanında tutacağı boyut bu alanda belirlenir. MaxLenght alanına girilen değeri otomatik alır.

## Olaylar

Nesnenin sahip olduğu olaylar, Özellik Görüntüleyici panelindeki “Olaylar” sekmesinde yer almaktadır. Her bir olay, farklı çalışma anlarında tetiklenerek kendilerine özgü işlemleri gerçekleştirir. Bu olaylara geliştirici tarafından yazılan kodlar da ilgili olayın tetiklendiği anda çalıştırılır.

**“Client”** alanında bulunan olaylara çift tıklandığında ekran, TypeScript kodlamanın yapılabileceği **“Formadı.ts”** isimli form kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur.

**“Server”** alanında bulunan olaylara çift tıklandığında ekran, C# kodlamanın yapılabileceği **“Formadı.cs”** isimli form kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur.

Geliştirici bu methodlar içerisinde istediği kod bloğunu kurgulayabilir. Olaylar sekmesinden tıklanarak kod tarafında methodu oluşturulmuş olayın yanında, method adı bilgisi otomatik oluşturularak, olayla method arasındaki ilişki belirtilmiş olur.

![Lookup](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload62c1d456-8572-4f2e-8f33-54be18d0be4f)

Oluşan methodlar;

![Lookup](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload82ec1bec-8c22-4de5-a2e7-c2e443e95231)

![Lookup](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload957bccb4-0075-4c68-a14b-061881172588)