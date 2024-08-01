---
sidebar_position: 9
custom_edit_url: ""
---

# TreeView

TreeView (Ağaç Görünümü) nesnesi form üzerinde hiyerarşik bilgi görünümü sunan bir öğedir. Nesne ana ögeler ve bunların altında olabilecek çocuk ögelerden oluşmaktadır. Bu nesne ile kullanıcıya kırılım yapısında bir liste gösterilip seçim yapması sağlanabilir.

Geliştirme arayüzünde aktif ekran form iken, Araç Kutusu panelinde form nesneleri listelenir. Nesne, araç kutusu panelinden sürükle/bırak yöntemi ile forma eklenir.

![TreeView](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadadfbde7d-2de9-48a3-9c93-3006903c8f0e)

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

:::note NOT

Bu kısımdan itibaren nesnede type alanında **dinamik** değeri seçilirse nesne kullanımı açıklanacaktır. **Statik** kullanımdaki özellikleri görüntülemek için ilgili bölümü açabilirsiniz.

:::

<details>
  <summary>Dinamik kullanım detaylarını görüntülemek için tıklayın!</summary>
  <div>

`DataSource` - Nesnede, bir veri kaynağından gelen değerleri listeleyebilmek için kullanılacak alandır. Projede Çözüm Gezgini alanındaki DataSource bölümüne eklenmiş ve başarıyla derlenen veri kaynağı tanımı, nesnenin Datasource) kısmından seçilebilir olur.

![TreeView](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload90cc71b2-3129-4893-b83d-428a5d2f600f)

![TreeView](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload54717ce3-5c2d-4d15-ae38-bc3986bdbd9f)

`RunAtServer` - Bu seçenek nesneye bağlanan sorgunun, sunucudan mı istemciden mi çalıştırılacağının belirlendiği seçenektir.

Bu seçenek aktif edilirse web arayüzünde forma tıklandığında, form açılmadan önce sorgu, sunucu tarafında çalıştırılır, form açıldığında nesneye sorgu sonucu yüklenmiş olarak gelir. Seçenek pasif yapıldığında web arayüzünde forma tıklandığında, form açıldıktan sonra nesneye sorgunun sonuç değerleri yüklenmeye başlar.

Sorgu sonucunun yüklenmesi için geçen bekleme süresi, bu özellik aktifken formun açılma anında, özellik pasifken form hızlı açıldıktan sonra nesneye verinin yüklenmesi anında etkili olur.

`Value Expression` - Veri Kaynağı kısmından bir veri kaynağı tanımı seçildiğinde bu alan görünür olur. Seçilen veri kaynağından dönen tüm kolonlar bu alanda listelenir. Kullanıcı arayüzden seçim yaptığında, yapılan seçimin kayıt alanının hangi kolon değeri olacağı bu alanda belirlenir.

Örneğin nesneye kullanıcıların listesini getiren bir sorgu bağlanmış olsun. Sorgudan ID (Kullanıcı Adı), FIRSTNAME (İsim), EMAIL (Mail Adresi) kolonları dönüyor olsun. Bu nesnenin amacı kullanıcı seçimi olduğu için seçilen kullanıcının benzersiz kayıt değeri ID kolonunda bulunduğundan, Değer İfadesi kısmında sorgudan dönen ID kolonu seçilmelidir.

`Display Expression` - Veri Kaynağı kısmından bir veri kaynağı tanımı seçildiğinde bu alan görünür olur. Seçilen veri kaynağından dönen tüm kolonlar bu alanda listelenir. Kullanıcı arayüzden seçim yaptığında, nesne içerisinde görünecek ifadenin hangi sorgu kolonundan geleceği bu alanda belirlenir.

Örneğin nesneye kullanıcıların listesini getiren bir sorgu bağlanmış olsun. Sorgudan ID (Kullanıcı Adı), FIRSTNAME (İsim), LASTNAME (Soyisim), EMAIL (Mail Adresi) kolonları dönüyor olsun. Bu nesnenin amacı kullanıcı seçimi olduğu için seçilen kullanıcının FIRSTNAME ve LASTNAME kolonlarından dönen değerleri nesne içinde görüntülenmek istenecektir. O yüzden Görünür İfadesi kısmında bu kolon değerleri seçilir.

`Display Format` - Görünüm İfadesi alanından seçilen kolon ya da kolonlar otomatik olarak bu alana da eklenir. Nesnede listelenecek eleman metinlerine görünüm formatı belirlemek için kullanılan alandır. Elemanların istenen bir formatta gösterilmesi için, ilgili format yapısı bu alanda belirtilebilir. Ve nesne seçimi sonrası nesnede görüntülenecek değerin web arayüzde uç kullanıcılara belirlenen formatta görünmesi sağlanabilir.

Formatlamada kullanılabilecek format tiplerine, alana odaklanıldığında çıkan bilgi mesajındaki linkten (https://shopify.github.io/liquid/) erişilebilir ve gerçekleştirilmek istenen format yapısı Görünüm Formatı alanında ilgili sütun için uygulanabilir.

`Hierarcy Type` - Nesneye veri kaynağı tanımlandığında, veri kaynağında hangi tipe göre verilerin kırılımlı olacağının belirlendiği alandır. 

Örneğin nesneye bir REST sorgusu tanımlanıp, sorgu sonucunda listelenen ögelerin her birinde id ve hangi id'ye bağlı olduğunu belli eden parentid anahtarları içeriyorsa nesnede Hierarcy Type alanında Parent By seçilebilirken; REST sorugusu sonucundaki ögelerin içinde direkt olarak çocuk öge içeriyorsa Children By seçilmelidir.

Nesneye SQL sorgusu tanımlı ve sorguda ID, PARENTID ve TEXT gibi ögelerin birbirleri ile ilişkisini belli eder sonuçlar dönüyorsa, alanda Parent By seçilebilir.

***SQL Veri Kaynağı içeriği aşağıdaki gibi ise Parent By seçilmelidir.***

| **ID** 	| **PARENTID** 	| **TEXT** 	|
|---	|---	|---	|
| 1 	| 0 	| 1. Ana Öge 	|
| 2 	| 1 	| 1.1 Çocuk Başlık 	|
| 3 	| 1 	| 1.2 Çocuk Alt Başlık 	|
| 4 	| 3 	| 1.2.1 Çocuk Alt Başlık 	|
| 5 	| 0 	| 2. Ana Öge 	|
| 6 	| 5 	| 2.1 Çocuk Başlık 	|
| 7 	| 6 	| 2.1.1 Çocuk Alt Başlık 	|

***REST Veri Kaynağı içeriği aşağıdaki gibi ise Parent By seçilmelidir.***

```json

{
    "key": "1",
    "icon": null,
    "text": "Item1",
    "parentKey": null,
    "selected": true,
    "disabled": false,
    "expand": false
},
{
    "key": "2",
    "icon": null,
    "text": "Item2",
    "parentKey": "1",
    "selected": false,
    "disabled": false,
    "expand": false
},
{
    "key": "3",
    "icon": null,
    "text": "Item3",
    "parentKey": null,
    "selected": false,
    "disabled": false,
    "expand": false
}

```

***REST Veri Kaynağı içeriği aşağıdaki gibi ise Children By seçilmelidir.***

```json

{
    "id": "1",
    "icon": null,
    "text": "Item1",
    "childrenKey": [
        {
            "id": "2",
            "icon": null,
            "text": "Item2",
            "childrenKey": [],
            "selected": false,
            "disabled": false,
            "expand": false
        },
        {
            "id": "3",
            "icon": null,
            "text": "Item3",
            "childrenKey": [],
            "selected": false,
            "disabled": false,
            "expand": false
        }
    ],
    "selected": false,
    "disabled": false,
    "expand": false
}

```

>Yapılabilecek Seçimler : Parent By, Children By

`Not Recursive` - Nesne veri kaynağında seçili sorgu sonucunun özyinemeli (recursive) olup olmadığının seçildiği alandır. Nesneye bağlanan sorgu kırılımlı olarak listelenmiyorsa özellik aktif edililir. Aktif edildiğinde nesnede tanımlı sorguda kırılım bulunmuyor ama kırılımlı hale çevirmesini istenmiş olur.

`Parent Key` - Hierarcy Type alanında Parent By seçildiğinde gözüken alandır. DataSource üzerinden gelen veri özyinelemeli (recursive) olarak gelmediğinde, gelen veriyi nesne üzerinde düzgünce yansıtabilmek için manipüle edilmesi, iç içe bir kırılım yapısı oluşturulması gerekmektedir. Hierarcy Type alanında Parent By seçilmesi ile gelen bu veride yerleşimin mevcut ögenin bağlı olduğu ögesi (parent) bulunup bunun altına yerleştirilmesi ile meydana gelineceğini ifade edilir.

Örneğin yukarıdaki 1 numaralı alt alta öge içeren json örneği gibi sonuç geliyorsa Hierarchy Type alanında Parent By seçilip, Parent Key alanında parentkey özelliği seçilebilir. SQL sorgusu örneğinde ise Hierarchy Type alanında Parent By seçilip, Parent Key alanında PARENTID kolonu seçilebilir.

`Children Key` - Hierarcy Type alanında Children By seçildiğinde gözüken alandır. DataSource üzerinden gelen veri özyinelemeli (recursive) olarak gelmediğinde, gelen veriyi nesne üzerinde düzgünce yansıtabilmek için manipüle edilmesi, iç içe bir kırılım yapısı oluşturulması gerekmektedir. Hierarcy Type alanında Children By seçilmesi ile gelen bu veride yerleşimin mevcut ögenin altındaki çocukları (child) bulunup bunun altına yerleştirilmesi ile meydana gelineceğini ifade edilir.

Örneğin yukarıdaki 2 numaralı iç içe ögelerin listelendiği json örneği gibi sonuç geliyorsa, Hierarchy Type alanında Children By seçilip, Children Key alanında childrenkey özelliği seçilebilir. 

  </div>
</details>

:::note NOT

Bu kısımdan itibaren nesnede type alanında **statik** değeri seçilirse nesne kullanımı açıklanacaktır. **Dinamik** kullanımdaki özellikleri görüntülemek için ilgili bölümü açabilirsiniz.

:::

<details>
  <summary>Statik kullanım detaylarını görüntülemek için tıklayın!</summary>
  <div>

`Items` - Nesnede, bir veri kaynağından gelen kayıtlar değil, geliştirme anında manuel eklenen elemanlar listelenmek istendiğinde, eleman tanımlama işlemi bu alandan yapılır. Liste elemanlarının belirlendiği kısımdır. Bu alandan nesneye yeni eleman eklenebilir, mevcut bir eleman silinebilir veya düzenlenebilir. TreeView nesnesine elle eleman eklemek için 3 nokta ifadesine tıklanılır.

![TreeView](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9fc47ad4-5ebd-44fb-95ab-c059fb15e6a5)

Açılan pencerede “Ekle” butonuna tıklanarak nesnenin ana elemanlarını oluşturacak öge eklenebilir.

![TreeView](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada541a676-9b0b-49b4-ac5d-b9b0bbf73ea6)

Ana öge eklendiğinde pencerenin sol tarafındaki panelde ögeler listelenirken, sağ tarafta o nesnenin özellikleri bulunmaktadır.

![TreeView](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload79026538-c252-4073-be4e-b5af46b677aa)

`Key` - Ögeye verilecek anahtar değeri bu alana yazılır, ekli diğer ögelerdeki key alanlarında tanımlanmış değerlerden farklı olmalıdır, aynı değer yazılırsa ekleme işlemi yapılmaz.

`Title` - Ögeye verilecek isim bu alana yazılır.

`Checked` - Ögenin seçilmiş olarak gösteriminin ayarlandığı alandır. Seçili ise öge yanındaki CheckBox seçili olarak gözükecektir. Checked ile yapılan seçimin gözükmesi için, Selection Settings bölümündeki Type alanında **checkbox** seçimi yapılmalıdır.

`Selected` - Ögenin form üzerinde seçili halde gelmesi için kullanılır. Seçili olması istenen öge için aktif hale getirilir. Aktid edildiğinde öge, kendisi genişliğindeki görselle seçildiği gösterilir.  

`Expand` - Ögenin altında bulunan kırılımın açık olarak gelmesi için kullanılır. 

`Icon` - Ögenin öncesinde bir ikon gösterilmesi isteniyorsa ikon seçimindeki üç noktaya tıklanarak İkon Bulucu içinde gelen resimlerden seçim yapılabilir.

`Children Items` - Öge altında olması istenen başka bir eleman daha varsa Children Items’taki üç noktaya tıklanarak ekleme yapılabilir. Açılan pencerede ekle butonuna basıldığında gelen özellikler bir önceki pencere ile aynı olup, “Kaydet” butonuna tıklanarak çocuk elemanlar ana elemanın altına gelecek şekilde kaydedilir.

  </div>
</details>

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

`Show Search` - Özellik aktif edildiğinde, web arayüz ekranında nesne içine veri girilebiliyor olur ve girilen karakterler nesne elemanları arasında otomatik aratılarak, kullanıcının girdiği veri ile eşleşen nesne elemanları seçenek olarak sunulur. Nesne içerisindeki elemanları, veri girerek otomatik filtreleme ile bulmayı sağlayan özelliktir.

### Behavior

`ReadOnly` - Nesnenin düzenleme modunda olup olmayacağının ayarlandığı kısımdır. Bu özellik aktif edildiğinde nesne veri girişine izin vermez, salt okunur modda olur. Nesneye veri girişine izin verilmesi için özelliğin pasif olması gerekir.

`Text Seperator` - Bu alan, kodlama anında nesne elemanlarının metin ifadelerine erişilmek istendiğinde, değerler arasına konulan ayrıştırıcı ifadenin belirlendiği kısımdır. Örneğin Text Seperator alanında virgül (,) karakteri yazılıp, nesnede TreeViewText1 ve TreeViewText2 olan iki öge nesne içinde seçilirse **TreeViewText1,TreeViewText2** olarak veri gelecektir.

`Value Seperator` - Bu alan, kodlama anında nesne elemanlarının değer ifadelerine erişilmek istendiğinde, değerler arasına konulan ayrıştırıcı ifadenin belirlendiği kısımdır. Örneğin Value Seperator alanında virgül (,) karakteri yazılıp, nesnede TreeViewValue1 ve TreeViewValue2 olan iki öge nesne içinde seçilirse **TreeViewValue1,TreeViewValue2** olarak veri gelecektir.

### Selection Settings

`Mode` - Nesnede tek bir ögenin veya birden fazla ögenin seçilebileceğinin belirlendiği alandır. Alanda single seçimi yapılırsa nesnede listelen ögelerden bir tanesi seçilirken, multiple seçimi yapıldığında ise listenen ögeler arasında birden fazla seçim yapılması sağlanır.

`Type` - Nesnede seçim işleminin bir ögelerin yanında gösterilecek bir checkbox'tan mı yoksa ögeye tıklanarak öge boyunca bir seçim alanı ile mi yapılacağının belirlendiği alandır. Alanda **checkbox** seçildiğinde her ögenin yanında bir seçim kutusu gözükerek bu kutulara tıklanarak seçim yapılması beklenirken, **rowselect** seçildiğinde seçim işlemi ögelerin bulunduğu satıra tıklaranak gerçekleştirilmektedir.

### Data Definition Language

`Field Name` - Sistemin veri tabanında, nesne için oluşturacağı kolonun adının belirlendiği alandır. "İsim (Name)" kısmında nesneye başka bir isim verilip, veritabanı tablosunda nesne için oluşturulacak kolon adı farklı bir isim olarak yaratılabilir.

## Olaylar

Nesnenin sahip olduğu olaylar, Özellik Görüntüleyici panelindeki "Olaylar" sekmesinde yer almaktadır. Her bir olay, farklı çalışma anlarında tetiklenerek kendilerine özgü işlemleri gerçekleştirir. Bu olaylara geliştirici tarafından yazılan kodlar da ilgili olayın tetiklendiği anda çalıştırılır.

**"Client"** alanında bulunan olaylara çift tıklandığında ekran, TypeScript kodlamanın yapılabileceği **"Formadı.ts"** isimli form kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur.

**"Server"** alanında bulunan olaylara çift tıklandığında ekran, C# kodlamanın yapılabileceği **"Formadı.cs"** isimli form kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur.

Geliştirici bu methodlar içerisinde istediği kod bloğunu kurgulayabilir. Olaylar sekmesinden tıklanarak kod tarafında methodu oluşturulmuş olayın yanında, method adı bilgisi otomatik oluşturularak, olayla method arasındaki ilişki belirtilmiş olur.

![TreeView](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb592f494-4be4-49e2-82ee-153f624dfd5f)