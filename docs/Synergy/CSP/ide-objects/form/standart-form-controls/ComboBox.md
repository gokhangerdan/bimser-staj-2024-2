---
sidebar_position: 5
custom_edit_url: ""
---

# ComboBox

Bir veri kaynağından gelen değerleri ya da geliştiricinin eleman olarak eklediği değerleri, web arayüzünde kullanıcıya liste şeklinde sunan ve bu veriler arasından eleman seçtirmeye yarayan nesnedir.

Geliştirme arayüzünde aktif ekran form iken, Araç Kutusu panelinde form nesneleri listelenir. Nesne, araç kutusu panelinden sürükle/bırak yöntemi ile forma eklenir.

![ComboBox](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3f4d2c04-4e52-4b09-8e16-8a381d887609)

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

`Type` - Nesneye hangi tipte veri ekleneceğinin seçimi bu alandan yapılır. Tip alanında **"Dinamik"** ve **"Statik"** olarak iki seçenek listelenir. Seçim yapılan tipe göre veri kaynağı bölümünde görünen özellikler değişiklik gösterecektir.

<div style={{textAlign: 'center'}}>

![ComboBox](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload571d5730-892c-4b35-85dd-1353926a4788)

</div>

Seçenek olarak **"Dinamik"** seçildiğinde; nesneye veriler, bir veri kaynağından dinamik olarak yüklenecek demektir. Dinamik seçeneği seçildiğinde Datasource alanında **Datasource** ve **Run at Server** özellikleri görünür olacaktır.

<div style={{textAlign: 'center'}}>

![ComboBox](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload849d64e7-f842-44cc-9027-a240c42720d3)

</div>

Seçenek olarak **"Statik"** seçildiğinde ise, nesneye manuel eleman eklenecek demektir ve veri kaynağı alanında **Items** özelliği görünür olur.

<div style={{textAlign: 'center'}}>

![ComboBox](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload85c46a9b-50f2-47de-9437-fd489e7ee94c)

</div>

:::note NOT

Bu kısımdan itibaren nesnede type alanında **dinamik** değeri seçilirse nesne kullanımı açıklanacaktır. **Statik** kullanımdaki özellikleri görüntülemek için ilgili bölümü açabilirsiniz.

:::

<details>
  <summary>Dinamik kullanım detaylarını görüntülemek için tıklayın!</summary>
  <div>

`DataSource` - Nesnede, bir veri kaynağından gelen değerleri listeleyebilmek için kullanılacak alandır. Projede Çözüm Gezgini alanındaki DataSource bölümüne eklenmiş ve başarıyla derlenen veri kaynağı tanımı, nesnenin Datasource) kısmından seçilebilir olur.

![ComboBox](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9f38c2e7-42f6-4b43-a2c7-6b145fc9942f)

<div style={{textAlign: 'center'}}>

![ComboBox](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7018661c-6de1-40b9-81ad-5984e48384e6)

</div>

`RunAtServer` - Bu seçenek nesneye bağlanan sorgunun, sunucudan mı istemciden mi çalıştırılacağının belirlendiği seçenektir.

Bu seçenek aktif edilirse web arayüzünde forma tıklandığında, form açılmadan önce sorgu, sunucu tarafında çalıştırılır, form açıldığında nesneye sorgu sonucu yüklenmiş olarak gelir. Seçenek pasif yapıldığında web arayüzünde forma tıklandığında, form açıldıktan sonra nesneye sorgunun sonuç değerleri yüklenmeye başlar.

Sorgu sonucunun yüklenmesi için geçen bekleme süresi, bu özellik aktifken formun açılma anında, özellik pasifken form hızlı açıldıktan sonra nesneye verinin yüklenmesi anında etkili olur.

`Value Expression` - Veri Kaynağı kısmından bir veri kaynağı tanımı seçildiğinde bu alan görünür olur. Seçilen veri kaynağından dönen tüm kolonlar bu alanda listelenir. Kullanıcı arayüzden seçim yaptığında, yapılan seçimin kayıt alanının hangi kolon değeri olacağı bu alanda belirlenir.

Örneğin nesneye kullanıcıların listesini getiren bir sorgu bağlanmış olsun. Sorgudan ID (Kullanıcı Adı), FIRSTNAME (İsim), EMAIL (Mail Adresi) kolonları dönüyor olsun. Bu nesnenin amacı kullanıcı seçimi olduğu için seçilen kullanıcının benzersiz kayıt değeri ID kolonunda bulunduğundan, Değer İfadesi kısmında sorgudan dönen ID kolonu seçilmelidir.

![ComboBox](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5c9e06d5-7d85-456e-b631-52fe3592698b)

`Display Expression` - Veri Kaynağı kısmından bir veri kaynağı tanımı seçildiğinde bu alan görünür olur. Seçilen veri kaynağından dönen tüm kolonlar bu alanda listelenir. Kullanıcı arayüzden seçim yaptığında, nesne içerisinde görünecek ifadenin hangi sorgu kolonundan geleceği bu alanda belirlenir.

Örneğin nesneye kullanıcıların listesini getiren bir sorgu bağlanmış olsun. Sorgudan ID (Kullanıcı Adı), FIRSTNAME (İsim), LASTNAME (Soyisim), EMAIL (Mail Adresi) kolonları dönüyor olsun. Bu nesnenin amacı kullanıcı seçimi olduğu için seçilen kullanıcının FIRSTNAME ve LASTNAME kolonlarından dönen değerleri nesne içinde görüntülenmek istenecektir. O yüzden Görünür İfadesi kısmında bu kolon değerleri seçilir.

![ComboBox](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6415a813-3d47-4f9a-8e6b-71266c06a39f)

`Display Format` - Görünüm İfadesi alanından seçilen kolon ya da kolonlar otomatik olarak bu alana da eklenir. Nesnede listelenecek eleman metinlerine görünüm formatı belirlemek için kullanılan alandır. Elemanların istenen bir formatta gösterilmesi için, ilgili format yapısı bu alanda belirtilebilir. Ve nesne seçimi sonrası nesnede görüntülenecek değerin web arayüzde uç kullanıcılara belirlenen formatta görünmesi sağlanabilir.

Formatlamada kullanılabilecek format tiplerine, alana odaklanıldığında çıkan bilgi mesajındaki linkten (https://shopify.github.io/liquid/) erişilebilir ve gerçekleştirilmek istenen format yapısı Görünüm Formatı alanında ilgili sütun için uygulanabilir.

![ComboBox](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc57cc69b-5f9a-401b-8888-728be3db03e2)

:::note NOT

Görünüm Formatı örnek uygulamaları için **[Display Format Örnekleri](code-samples/liquid-display-format.md)** dokümanını inceleyebilirsiniz.

:::

  </div>
</details>

:::note NOT

Bu kısımdan itibaren nesnede type alanında **statik** değeri seçilirse nesne kullanımı açıklanacaktır. **Dinamik** kullanımdaki özellikleri görüntülemek için ilgili bölümü açabilirsiniz.

:::

<details>
  <summary>Statik kullanım detaylarını görüntülemek için tıklayın!</summary>
  <div>

`Items` - Nesnede, bir veri kaynağından gelen kayıtlar değil, geliştirme anında manuel eklenen elemanlar listelenmek istendiğinde, eleman tanımlama işlemi bu alandan yapılır. Liste elemanlarının belirlendiği kısımdır. Bu alandan nesneye yeni eleman eklenebilir, mevcut bir eleman silinebilir veya düzenlenebilir.

![ComboBox](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4e60a926-d530-41dd-a9d2-1005a85f021a)

Elemanlar alanına tıklandığında eleman ekleme penceresi açılır. Ekle butonuna tıklanarak nesneye yeni eleman kalemleri oluşturulur.

![ComboBox](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload03dcf635-2232-4995-8759-c3cb0d5d73a5)

Girilen elemanın **Value** ve **Title** alanları doldurulur. Elemanın ikona sahip olması istenirse Icons alanı içindeki ikon kütüphanesinden seçim yapılabilir. Ögenin Selected alanı aktif edilirse web ara yüzünde nesne içinde bu öge otomatik olarak seçilmiş gibi gösterilecektir. "Kaydet" butonuna basılarak nesneye eleman ekleme işlemi tamamlanır.

![ComboBox](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload40ad77c9-993c-4deb-8539-e729b2feb6c9)

Bu alana eklenmiş bir eleman düzenlenmek istendiğinde, ilgili eleman kaydına tıklanarak yan tarafta açılan eleman detayları penceresinden düzenleme yapılabilir. Mevcut bir eleman silinmek istendiğinde ise eleman detaylarındaki sil butonu kullanılır.

![ComboBox](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1da82692-1aa0-4572-8a62-d5bf7855e541)

Web arayüzde nesneye tıklandığında, Elemanlar alanında belirlenen eleman kayıtları, kullanıcının seçim yapması için listelenir.

ComboBox nesnesinde görünüm:

![ComboBox](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload978b7f58-0851-4f10-91e4-ddf0ed7b27bb)

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

`Icon Expression` - Datasource alanında Type: Dinamik seçilip, Datasource seçimi yapıldığında görünen alandır. Açılır menü ile veri kaynağındaki bir kolon alanda seçilmelidir.

`Icon Matchers` - Icon Expression alanında tanımlı veri kaynağındaki kolon seçimi yapıldığında gözüken alandır. Alandaki 3 nokta ifadesine tıklandığında Value ve Icon tanımlama paneli gösterilmektedir. Ekleme butonuna tıklandığında Icon Expression alanında seçilen kolondaki bir değere karşılık hangi ikonun gösterileceği seçilmelidir. 

Örneğin nesneye kullanıcıların listesini getiren bir sorgu bağlanmış olsun. Sorgudan ID (Kullanıcı Adı), FIRSTNAME (İsim), LASTNAME (Soyisim), EMAIL (Mail Adresi) kolonları dönüyor olsun. Icon Expression alanında ID kolonu seçilirse, Icon Matchers alanında ID kolonundaki değerlere göre ikon gösterimi tanımı yapılacaktır. Value alanında 1 - Icon alanında approve ikonu seçilip kaydedilirse, web ara yüzünde nesnede 1 ID'sine sahip kullanıcı tanımlanan ikon ile gösterilirken, diğer ögeler ikon olmadan gösterilecektir. Alanda birden fazla Icon Matchers tanımlanması mümkündür.

`Placeholder` - Nesne içine uç kullanıcı tarafından girilmesi istenen veri bilgisini, nesne içerisinde bilgi amaçlı göstermek için kullanılan özelliktir. Uç kullanıcı nesneyi görüntülediğinde bu alana yazılan yönlendirici metni görür, nesneye odaklandığında ve değer girmeye başladığında yönlendirici metin kaybolur.

### Behavior

`ReadOnly` - Nesnenin düzenleme modunda olup olmayacağının ayarlandığı kısımdır. Bu özellik aktif edildiğinde nesne veri girişine izin vermez, salt okunur modda olur. Nesneye veri girişine izin verilmesi için özelliğin pasif olması gerekir.

`Tab Index` - Bu alana sayısal değerler girilerek, tab butonuna basıldığında form nesneleri arasında hangi sıra ile odaklanılacağı belirlenir. Form doldurulurken imleci, veri girilmek istenen nesneye tıklamak yerine, tab butonuna basarak belirli bir sırayla indekslenmiş nesnelere direk odaklanılması sağlanmış olur. Bu da form doldurma hızını artıran bir özelliktir.

`Required` - Nesnede veri girişinin zorunlu olup olmayacağının belirlendiği alandır. Bu özellik aktif edildiğinde nesne içerisine veri girişi yapılmadan formun ilerletilmesi/kaydedilmesi gerçekleştirilemez.

`Value Type` - Nesne elemanlarının tipinin belirlendiği alandır. Burada belirlenen tipe göre, Elemanlar alanında eklenen satırın Değer alanı tipi değiştirilir. Aynı zamanda nesneye parametrik bir sorgu bağlandığında, parametre tipi ile Değer Tipi alanından seçilen tip değeri aynı olmalıdır. 

:::caution DİKKAT

Nesnenin Datasource alanında **Type : Statik** seçili ise ve eleman ekli ise Value Type alanı seçim yapılamaz durumuna geçer.

:::

`Allow Clear` - Nesnede seçilen değeri temizlemek için kullanılan özelliktir. Bu özellik aktif edildiğinde web arayüzünde kullanıcı nesneden bir seçim yaptığında, nesne kenarında × (Çarpı) işareti belirir. Çarpı işaretine basılarak seçilen değer silinip, başka bir nesne elemanının seçimi sağlanabilir.

![ComboBox](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadba5fbf09-0678-4cb6-a713-58a6ef708a16)

`Show Search` - Özellik aktif edildiğinde, web arayüz ekranında nesne içine veri girilebiliyor olur ve girilen karakterler nesne elemanları arasında otomatik aratılarak, kullanıcının girdiği veri ile eşleşen nesne elemanları seçenek olarak sunulur. Nesne içerisindeki elemanları, veri girerek otomatik filtreleme ile bulmayı sağlayan özelliktir.

Tüm liste;

![ComboBox](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc13eeca9-7113-4ed8-aa3a-537cfa9c22e0)

Girilen veriye göre arama yapılıyor;

![ComboBox](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb303bb04-a4d0-43e7-99b5-6bb3f4b9033e)

`Size Type` - Nesne seçim alanı boyutunun ayarlandığı kısımdır.

>Yapılabilecek Seçimler : Small, Middle, Large

### Data Definition Language

`Field Name` - Sistemin veri tabanında, nesne için oluşturacağı kolonun adının belirlendiği alandır. "İsim (Name)" kısmında nesneye başka bir isim verilip, veritabanı tablosunda nesne için oluşturulacak kolon adı farklı bir isim olarak yaratılabilir.

`Allow Null` - Nesne için oluşturulacak veritabanı alanının boş(null) değerlere izin verip vermeyeceği bu kısımdan belirtilir.

## Olaylar

Nesnenin sahip olduğu olaylar, Özellik Görüntüleyici panelindeki "Olaylar" sekmesinde yer almaktadır. Her bir olay, farklı çalışma anlarında tetiklenerek kendilerine özgü işlemleri gerçekleştirir. Bu olaylara geliştirici tarafından yazılan kodlar da ilgili olayın tetiklendiği anda çalıştırılır.

**"Client"** alanında bulunan olaylara çift tıklandığında ekran, TypeScript kodlamanın yapılabileceği **"Formadı.ts"** isimli form kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur.

**"Server"** alanında bulunan olaylara çift tıklandığında ekran, C# kodlamanın yapılabileceği **"Formadı.cs"** isimli form kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur.

Geliştirici bu methodlar içerisinde istediği kod bloğunu kurgulayabilir. Olaylar sekmesinden tıklanarak kod tarafında methodu oluşturulmuş olayın yanında, method adı bilgisi otomatik oluşturularak, olayla method arasındaki ilişki belirtilmiş olur.

![ComboBox](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9781c8c8-d5b4-4aaf-8f3e-2fc52eaa08ef)

Oluşan methodlar;

![ComboBox](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada246c6ec-8770-4c98-a6f4-d8d297a70647)

![ComboBox](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaded2bdc6e-0904-4177-af4c-a185b6a3f16c)