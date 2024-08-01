---
sidebar_position: 6
custom_edit_url: ""
---

# TagBox

Bir veri kaynağından gelen değerleri ya da geliştiricinin eleman olarak eklediği değerleri, web arayüzünde kullanıcıya liste şeklinde sunan ve bu veriler arasından çoklu eleman seçtirmeye yarayan nesnedir.

Geliştirme arayüzünde aktif ekran form iken, Araç Kutusu panelinde form nesneleri listelenir. Nesne, araç kutusu panelinden sürükle/bırak yöntemi ile forma eklenir.

![TagBox](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfa82ab92-ca1a-43ab-9f93-40f27faaa104)

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

<div style={{textAlign: 'center'}}>

![TagBox](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6a89ca53-746d-48a2-a01e-276b8e51d34c)

</div>

Seçenek olarak **"Dinamik"** seçildiğinde; nesneye veriler, bir veri kaynağından dinamik olarak yüklenecek demektir. Dinamik seçeneği seçildiğinde Datasource alanında **Datasource** ve **Run at Server** özellikleri görünür olacaktır.

<div style={{textAlign: 'center'}}>

![TagBox](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5ed27d66-dd4e-45b0-8d3d-f37f20eb6310)

</div>

Seçenek olarak **"Statik"** seçildiğinde ise, nesneye manuel eleman eklenecek demektir ve veri kaynağı alanında **Items** özelliği görünür olur.

<div style={{textAlign: 'center'}}>

![TagBox](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbf67a7cb-c41f-4531-a394-a480890665be)

</div>

:::note NOT

Bu kısımdan itibaren nesnede type alanında **dinamik** değeri seçilirse nesne kullanımı açıklanacaktır. **Statik** kullanımdaki özellikleri görüntülemek için ilgili bölümü açabilirsiniz.

:::

<details>
  <summary>Dinamik kullanım detaylarını görüntülemek için tıklayın!</summary>
  <div>

`DataSource` - Nesnede, bir veri kaynağından gelen değerleri listeleyebilmek için kullanılacak alandır. Projede Çözüm Gezgini alanındaki DataSource bölümüne eklenmiş ve başarıyla derlenen veri kaynağı tanımı, nesnenin Datasource) kısmından seçilebilir olur.

![TagBox](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada3b96ed2-7523-4b81-9f5a-849f1ab9d25a)

![TagBox](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1b837d17-3f43-47dc-bf3c-1b4413477af3)

`RunAtServer` - Bu seçenek nesneye bağlanan sorgunun, sunucudan mı istemciden mi çalıştırılacağının belirlendiği seçenektir.

Bu seçenek aktif edilirse web arayüzünde forma tıklandığında, form açılmadan önce sorgu, sunucu tarafında çalıştırılır, form açıldığında nesneye sorgu sonucu yüklenmiş olarak gelir. Seçenek pasif yapıldığında web arayüzünde forma tıklandığında, form açıldıktan sonra nesneye sorgunun sonuç değerleri yüklenmeye başlar.

Sorgu sonucunun yüklenmesi için geçen bekleme süresi, bu özellik aktifken formun açılma anında, özellik pasifken form hızlı açıldıktan sonra nesneye verinin yüklenmesi anında etkili olur.

`Value Expression` - Veri Kaynağı kısmından bir veri kaynağı tanımı seçildiğinde bu alan görünür olur. Seçilen veri kaynağından dönen tüm kolonlar bu alanda listelenir. Kullanıcı arayüzden seçim yaptığında, yapılan seçimin kayıt alanının hangi kolon değeri olacağı bu alanda belirlenir.

Örneğin nesneye kullanıcıların listesini getiren bir sorgu bağlanmış olsun. Sorgudan ID (Kullanıcı Adı), FIRSTNAME (İsim), EMAIL (Mail Adresi) kolonları dönüyor olsun. Bu nesnenin amacı kullanıcı seçimi olduğu için seçilen kullanıcının benzersiz kayıt değeri ID kolonunda bulunduğundan, Değer İfadesi kısmında sorgudan dönen ID kolonu seçilmelidir.

![TagBox](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfe47a1a3-283b-47ae-af87-8fb7f31afee7)

`Display Expression` - Veri Kaynağı kısmından bir veri kaynağı tanımı seçildiğinde bu alan görünür olur. Seçilen veri kaynağından dönen tüm kolonlar bu alanda listelenir. Kullanıcı arayüzden seçim yaptığında, nesne içerisinde görünecek ifadenin hangi sorgu kolonundan geleceği bu alanda belirlenir.

Örneğin nesneye kullanıcıların listesini getiren bir sorgu bağlanmış olsun. Sorgudan ID (Kullanıcı Adı), FIRSTNAME (İsim), LASTNAME (Soyisim), EMAIL (Mail Adresi) kolonları dönüyor olsun. Bu nesnenin amacı kullanıcı seçimi olduğu için seçilen kullanıcının FIRSTNAME ve LASTNAME kolonlarından dönen değerleri nesne içinde görüntülenmek istenecektir. O yüzden Görünür İfadesi kısmında bu kolon değerleri seçilir.

![TagBox](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5130bf49-8229-4231-86a7-6457606bbee4)

`Display Format` - Görünüm İfadesi alanından seçilen kolon ya da kolonlar otomatik olarak bu alana da eklenir. Nesnede listelenecek eleman metinlerine görünüm formatı belirlemek için kullanılan alandır. Elemanların istenen bir formatta gösterilmesi için, ilgili format yapısı bu alanda belirtilebilir. Ve nesne seçimi sonrası nesnede görüntülenecek değerin web arayüzde uç kullanıcılara belirlenen formatta görünmesi sağlanabilir.

Formatlamada kullanılabilecek format tiplerine, alana odaklanıldığında çıkan bilgi mesajındaki linkten (https://shopify.github.io/liquid/) erişilebilir ve gerçekleştirilmek istenen format yapısı Görünüm Formatı alanında ilgili sütun için uygulanabilir.

![TagBox](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload76767edd-d150-417c-b2a4-2f5401d3c6ed)

:::note NOT

Görünüm Formatı örnek uygulamaları için **[Display Format Örnekleri](code-samples/liquid-display-format.md)** dokümanını inceleyebilirsiniz.

:::

  </div>
</details>

:::note

Bu kısımdan itibaren nesnede type alanında **statik** değeri seçilirse nesne kullanımı açıklanacaktır. **Dinamik** kullanımdaki özellikleri görüntülemek için ilgili bölümü açabilirsiniz.

:::

<details>
  <summary>Statik kullanım detaylarını görüntülemek için tıklayın!</summary>
  <div>

`Items` - Nesnede, bir veri kaynağından gelen kayıtlar değil, geliştirme anında manuel eklenen elemanlar listelenmek istendiğinde, eleman tanımlama işlemi bu alandan yapılır. Liste elemanlarının belirlendiği kısımdır. Bu alandan nesneye yeni eleman eklenebilir, mevcut bir eleman silinebilir veya düzenlenebilir.

![TagBox](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2d449135-217f-47dd-ab30-d8224f98ae61)

Elemanlar alanına tıklandığında eleman ekleme penceresi açılır. Ekle butonuna tıklanarak nesneye yeni eleman kalemleri oluşturulur.

![TagBox](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload43b392e7-b9de-46b8-9270-2736ca392328)

Girilen elemanın **Value** ve **Title** alanları doldurulur. Ögenin Selected alanı aktif edilirse web ara yüzünde nesne içinde bu öge otomatik olarak seçilmiş gibi gösterilecektir. "Kaydet" butonuna basılarak nesneye eleman ekleme işlemi tamamlanır.

![TagBox](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7fb34e49-cd1f-4965-a9d6-a0065b5ac1e7)

Bu alana eklenmiş bir eleman düzenlenmek istendiğinde, ilgili eleman kaydına tıklanarak yan tarafta açılan eleman detayları penceresinden düzenleme yapılabilir. Mevcut bir eleman silinmek istendiğinde ise eleman detaylarındaki sil butonu kullanılır.

![TagBox](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc92b086d-3a33-4231-8ea8-d9ec376f682c)

Web arayüzde nesneye tıklandığında, Elemanlar alanında belirlenen eleman kayıtları, kullanıcının seçim yapması için listelenir.

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

`Allow Clear` - Nesnede seçilen değeri temizlemek için kullanılan özelliktir. Bu özellik aktif edildiğinde web arayüzünde kullanıcı nesneden bir seçim yaptığında, nesne kenarında × (Çarpı) işareti belirir. Çarpı işaretine basılarak seçilen değer silinip, başka bir nesne elemanının seçimi sağlanabilir.

`Placeholder` - Nesne içine uç kullanıcı tarafından girilmesi istenen veri bilgisini, nesne içerisinde bilgi amaçlı göstermek için kullanılan özelliktir. Uç kullanıcı nesneyi görüntülediğinde bu alana yazılan yönlendirici metni görür, nesneye odaklandığında ve değer girmeye başladığında yönlendirici metin kaybolur.

### Behavior

`ReadOnly` - Nesnenin düzenleme modunda olup olmayacağının ayarlandığı kısımdır. Bu özellik aktif edildiğinde nesne veri girişine izin vermez, salt okunur modda olur. Nesneye veri girişine izin verilmesi için özelliğin pasif olması gerekir.

`Tab Index` - Bu alana sayısal değerler girilerek, tab butonuna basıldığında form nesneleri arasında hangi sıra ile odaklanılacağı belirlenir. Form doldurulurken imleci, veri girilmek istenen nesneye tıklamak yerine, tab butonuna basarak belirli bir sırayla indekslenmiş nesnelere direk odaklanılması sağlanmış olur. Bu da form doldurma hızını artıran bir özelliktir.

`Required` - Nesnede veri girişinin zorunlu olup olmayacağının belirlendiği alandır. Bu özellik aktif edildiğinde nesne içerisine veri girişi yapılmadan formun ilerletilmesi/kaydedilmesi gerçekleştirilemez.

`Value Type` - Nesne elemanlarının tipinin belirlendiği alandır. Burada belirlenen tipe göre, Elemanlar alanında eklenen satırın Değer alanı tipi değiştirilir. Aynı zamanda nesneye parametrik bir sorgu bağlandığında, parametre tipi ile Değer Tipi alanından seçilen tip değeri aynı olmalıdır. 

:::caution DİKKAT

Nesnenin Datasource alanında **Type : Statik** seçili ise ve eleman ekli ise Value Type alanı seçim yapılamaz durumuna geçer.

:::

`Text Seperator` - Bu alan, kodlama anında nesne elemanlarının metin ifadelerine erişilmek istendiğinde, değerler arasına konulan ayrıştırıcı ifadenin belirlendiği kısımdır. Örneğin Text Seperator alanında virgül (,) karakteri yazılıp, nesnede TagItemText1 ve TagItemText2 olan iki öge nesne içinde seçilirse **TagItemText1,TagItemText2** olarak veri gelecektir.

`Value Seperator` - Bu alan, kodlama anında nesne elemanlarının değer ifadelerine erişilmek istendiğinde, değerler arasına konulan ayrıştırıcı ifadenin belirlendiği kısımdır. Örneğin Value Seperator alanında virgül (,) karakteri yazılıp, nesnede TagItemValue1 ve TagItemValue2 olan iki öge nesne içinde seçilirse **TagItemValue1,TagItemValue2** olarak veri gelecektir.

`Show Search` - Özellik aktif edildiğinde, web arayüz ekranında nesne içine veri girilebiliyor olur ve girilen karakterler nesne elemanları arasında otomatik aratılarak, kullanıcının girdiği veri ile eşleşen nesne elemanları seçenek olarak sunulur. Nesne içerisindeki elemanları, veri girerek otomatik filtreleme ile bulmayı sağlayan özelliktir.

![TagBox](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload10204e7a-0f8a-40f0-98af-6b9cc42626e0)

### Data Definition Language

`Field Name` - Sistemin veri tabanında, nesne için oluşturacağı kolonun adının belirlendiği alandır. "İsim (Name)" kısmında nesneye başka bir isim verilip, veritabanı tablosunda nesne için oluşturulacak kolon adı farklı bir isim olarak yaratılabilir.

`Allow Null` - Nesne için oluşturulacak veritabanı alanının boş(null) değerlere izin verip vermeyeceği bu kısımdan belirtilir.

## Olaylar

Nesnenin sahip olduğu olaylar, Özellik Görüntüleyici panelindeki "Olaylar" sekmesinde yer almaktadır. Her bir olay, farklı çalışma anlarında tetiklenerek kendilerine özgü işlemleri gerçekleştirir. Bu olaylara geliştirici tarafından yazılan kodlar da ilgili olayın tetiklendiği anda çalıştırılır.

"Client" alanında bulunan olaylara çift tıklandığında ekran, TypeScript kodlamanın yapılabileceği "Formadı.ts" isimli form kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur.

"Server" alanında bulunan olaylara çift tıklandığında ekran, C# kodlamanın yapılabileceği "Formadı.cs" isimli form kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur.

Geliştirici bu methodlar içerisinde istediği kod bloğunu kurgulayabilir. Olaylar sekmesinden tıklanarak kod tarafında methodu oluşturulmuş olayın yanında, method adı bilgisi otomatik oluşturularak, olayla method arasındaki ilişki belirtilmiş olur.

![TagBox](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4e2f321d-3297-4d60-8f1c-6b29a2d67a74)

Oluşan methodlar;

![TagBox](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7f02d00b-54a4-4673-a16f-f629f137dd72)

![TagBox](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3ba26c66-0bc4-415e-abfd-7b344be76afa)