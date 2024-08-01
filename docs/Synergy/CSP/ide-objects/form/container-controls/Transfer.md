---
sidebar_position: 5
custom_edit_url: ""
---

# Transfer

Bir veri kaynağından gelen değerleri ya da geliştiricinin eleman olarak eklediği değerleri, kaynak kolonunda kullanıcıya liste şeklinde sunan ve bu veriler arasından eleman seçtirerek hedef kolonuna transfer etmeye yarayan nesnedir.

Kaynak ve hedef yapısında, çoklu eleman seçmek için kullanılan bir seçim kontrolüdür. Kaynak kolonunda listelenen elemanlardan seçilmek istenen kayıtlar işaretlenir, ok butonu ile hedef kolonuna aktarılarak seçim işlemi gerçekleştirilir. Tam tersi olarak hedef kolonunda seçilmiş veriler işaretlenerek ok butonu ile kaynak kolonuna geri gönderilebilir, böylece yapılan seçim geri alınmış olur.

![Transfer](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbafd5a2c-a3b2-4a55-bcc2-2058e190d439)

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

`Type` - Nesneye hangi tipte veri ekleneceğinin seçimi bu alandan yapılır. Tip alanında **"Dinamik"** ve **"Statik"** olarak iki seçenek listelenir. Seçim yapılan tipe göre veri kaynağı bölümünde görünen özellikler değişiklik gösterecektir.

<div style={{textAlign: 'center'}}>

![Transfer](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb03a7f9c-c258-48a5-8b63-e8e95d16ceda)

</div>

Seçenek olarak **"Dinamik"** seçildiğinde; nesneye veriler, bir veri kaynağından dinamik olarak yüklenecek demektir. Dinamik seçeneği seçildiğinde Datasource alanında **Datasource** ve **Run at Server** özellikleri görünür olacaktır.

<div style={{textAlign: 'center'}}>

![Transfer](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload22fa103b-536c-4395-bc7a-4c510b1388df)

</div>

Seçenek olarak **"Statik"** seçildiğinde ise, nesneye manuel eleman eklenecek demektir ve veri kaynağı alanında **Items** özelliği görünür olur.

<div style={{textAlign: 'center'}}>

![Transfer](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5f5d3b8f-23ff-42db-93d5-dd2958664683)

</div>

:::note NOT

Bu kısımdan itibaren nesnede type alanında **dinamik** değeri seçilirse nesne kullanımı açıklanacaktır. **Statik** kullanımdaki özellikleri görüntülemek için ilgili bölümü açabilirsiniz.

:::

<details>
  <summary>Dinamik kullanım detaylarını görüntülemek için tıklayın!</summary>
  <div>

`DataSource` - Nesnede, bir veri kaynağından gelen değerleri listeleyebilmek için kullanılacak alandır. Projede Çözüm Gezgini alanındaki DataSource bölümüne eklenmiş ve başarıyla derlenen veri kaynağı tanımı, nesnenin Datasource) kısmından seçilebilir olur.

![Transfer](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4d89bffb-e4f0-489d-8ad6-10ebd0b2bbb7)

![Transfer](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload469a5e47-c22f-4af7-a041-6a3bc0577afd)

`RunAtServer` - Bu seçenek nesneye bağlanan sorgunun, sunucudan mı istemciden mi çalıştırılacağının belirlendiği seçenektir.

Bu seçenek aktif edilirse web arayüzünde forma tıklandığında, form açılmadan önce sorgu, sunucu tarafında çalıştırılır, form açıldığında nesneye sorgu sonucu yüklenmiş olarak gelir. Seçenek pasif yapıldığında web arayüzünde forma tıklandığında, form açıldıktan sonra nesneye sorgunun sonuç değerleri yüklenmeye başlar.

Sorgu sonucunun yüklenmesi için geçen bekleme süresi, bu özellik aktifken formun açılma anında, özellik pasifken form hızlı açıldıktan sonra nesneye verinin yüklenmesi anında etkili olur.

`Value Expression` - Veri Kaynağı kısmından bir veri kaynağı tanımı seçildiğinde bu alan görünür olur. Seçilen veri kaynağından dönen tüm kolonlar bu alanda listelenir. Kullanıcı arayüzden seçim yaptığında, yapılan seçimin kayıt alanının hangi kolon değeri olacağı bu alanda belirlenir.

Örneğin nesneye kullanıcıların listesini getiren bir sorgu bağlanmış olsun. Sorgudan ID (Kullanıcı Adı), FIRSTNAME (İsim), EMAIL (Mail Adresi) kolonları dönüyor olsun. Bu nesnenin amacı kullanıcı seçimi olduğu için seçilen kullanıcının benzersiz kayıt değeri ID kolonunda bulunduğundan, Değer İfadesi kısmında sorgudan dönen ID kolonu seçilmelidir.

![Transfer](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload70e5848c-2334-4314-b6df-8d93de441a8d)

`Display Expression` - Veri Kaynağı kısmından bir veri kaynağı tanımı seçildiğinde bu alan görünür olur. Seçilen veri kaynağından dönen tüm kolonlar bu alanda listelenir. Kullanıcı arayüzden seçim yaptığında, nesne içerisinde görünecek ifadenin hangi sorgu kolonundan geleceği bu alanda belirlenir.

Örneğin nesneye kullanıcıların listesini getiren bir sorgu bağlanmış olsun. Sorgudan ID (Kullanıcı Adı), FIRSTNAME (İsim), LASTNAME (Soyisim), EMAIL (Mail Adresi) kolonları dönüyor olsun. Bu nesnenin amacı kullanıcı seçimi olduğu için seçilen kullanıcının FIRSTNAME ve LASTNAME kolonlarından dönen değerleri nesne içinde görüntülenmek istenecektir. O yüzden Görünür İfadesi kısmında bu kolon değerleri seçilir.

![Transfer](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload253d467d-8250-4b66-9d06-0171891f03ef)

`Display Format` - Görünüm İfadesi alanından seçilen kolon ya da kolonlar otomatik olarak bu alana da eklenir. Nesnede listelenecek eleman metinlerine görünüm formatı belirlemek için kullanılan alandır. Elemanların istenen bir formatta gösterilmesi için, ilgili format yapısı bu alanda belirtilebilir. Ve nesne seçimi sonrası nesnede görüntülenecek değerin web arayüzde uç kullanıcılara belirlenen formatta görünmesi sağlanabilir.

Formatlamada kullanılabilecek format tiplerine, alana odaklanıldığında çıkan bilgi mesajındaki linkten (https://shopify.github.io/liquid/) erişilebilir ve gerçekleştirilmek istenen format yapısı Görünüm Formatı alanında ilgili sütun için uygulanabilir.

![Transfer](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload511505b1-0cf6-47ad-924d-9b177dcb7270)

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

![Transfer](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2d4b919c-0f11-4085-b7b0-b34b6bfa373d)

Elemanlar alanına tıklandığında eleman ekleme penceresi açılır. Ekle butonuna tıklanarak nesneye yeni eleman kalemleri oluşturulur.

![Transfer](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf14859cc-a0ad-4796-98a4-9bc52d3e0f43)

Girilen elemanın **Value** ve **Title** alanları doldurulur. Ögenin Selected alanı aktif edilirse web ara yüzünde nesne içinde bu öge otomatik olarak seçilmiş gibi gösterilecektir. "Kaydet" butonuna basılarak nesneye eleman ekleme işlemi tamamlanır.

![Transfer](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload05a1ebef-543a-4dc3-862e-6493fdc07211)

Bu alana eklenmiş bir eleman düzenlenmek istendiğinde, ilgili eleman kaydına tıklanarak yan tarafta açılan eleman detayları penceresinden düzenleme yapılabilir. Mevcut bir eleman silinmek istendiğinde ise eleman detaylarındaki sil butonu kullanılır.

![Transfer](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload22711301-7c55-4a33-a23a-ae1a7d8310e8)

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

`Allow Select All` - Bu özellik aktif edildiğinde nesne üzerinde “Tümünü Seç” seçim kutusu aktif olur. Kullanıcı tek tek nesne elemanlarını seçmektense bu butona tıklayarak tüm nesne elemanlarını tek tıkla seçili yapabilir veya tüm nesne elemanlarının seçimini tek tıkla kaldırabilir.

<div style={{textAlign: 'center'}}>

![Transfer](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2f4c38ab-c7e2-4737-a46d-8d53b43fe785)

</div>

`Source Title` - Nesne içindeki kaynak bölümünde başlık tanımlanmak istenirse kullanılan alandır.

`Target Title` - Nesne içindeki hedef bölümünde başlık tanımlanmak istenirse kullanılan alandır.

### Behavior

`ReadOnly` - Nesnenin düzenleme modunda olup olmayacağının ayarlandığı kısımdır. Bu özellik aktif edildiğinde nesne veri girişine izin vermez, salt okunur modda olur. Nesneye veri girişine izin verilmesi için özelliğin pasif olması gerekir.

`Tab Index` - Bu alana sayısal değerler girilerek, tab butonuna basıldığında form nesneleri arasında hangi sıra ile odaklanılacağı belirlenir. Form doldurulurken imleci, veri girilmek istenen nesneye tıklamak yerine, tab butonuna basarak belirli bir sırayla indekslenmiş nesnelere direk odaklanılması sağlanmış olur. Bu da form doldurma hızını artıran bir özelliktir.

`Required` - Nesnede veri girişinin zorunlu olup olmayacağının belirlendiği alandır. Bu özellik aktif edildiğinde nesne içerisine veri girişi yapılmadan formun ilerletilmesi/kaydedilmesi gerçekleştirilemez.

`Value Type` - Nesne elemanlarının tipinin belirlendiği alandır. Burada belirlenen tipe göre, Elemanlar alanında eklenen satırın Değer alanı tipi değiştirilir. Aynı zamanda nesneye parametrik bir sorgu bağlandığında, parametre tipi ile Değer Tipi alanından seçilen tip değeri aynı olmalıdır. 

:::caution DİKKAT

Nesnenin Datasource alanında **Type : Statik** seçili ise ve eleman ekli ise Value Type alanı seçim yapılamaz durumuna geçer.

:::

`Text Seperator` - Bu alan, kodlama anında nesne elemanlarının metin ifadelerine erişilmek istendiğinde, değerler arasına konulan ayrıştırıcı ifadenin belirlendiği kısımdır. Örneğin Text Seperator alanında virgül (,) karakteri yazılıp, nesnede yazıları TransferItemText1 ve TransferItemText2 olan iki öge nesne içinde seçilirse **TransferItemText1,TransferItemText2** olarak veri gelecektir.

`Value Seperator` - Bu alan, kodlama anında nesne elemanlarının değer ifadelerine erişilmek istendiğinde, değerler arasına konulan ayrıştırıcı ifadenin belirlendiği kısımdır. Örneğin Value Seperator alanında virgül (,) karakteri yazılıp, nesnede değerleri TransferItemValue1 ve TransferItemValue2 olan iki öge nesne içinde seçilirse **TransferItemValue1,TransferItemValue2** olarak veri gelecektir.

`Show Search` - Özellik aktif edildiğinde, web arayüz ekranında nesne içine veri girilebiliyor olur ve girilen karakterler nesne elemanları arasında otomatik aratılarak, kullanıcının girdiği veri ile eşleşen nesne elemanları seçenek olarak sunulur. Nesne içerisindeki elemanları, veri girerek otomatik filtreleme ile bulmayı sağlayan özelliktir.

![Transfer](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada8dbb846-a612-44f7-9a9a-9606ffaa3268)

### Data Definition Language

`Field Name` - Sistemin veri tabanında, nesne için oluşturacağı kolonun adının belirlendiği alandır. "İsim (Name)" kısmında nesneye başka bir isim verilip, veritabanı tablosunda nesne için oluşturulacak kolon adı farklı bir isim olarak yaratılabilir.

`Allow Null` - Nesne için oluşturulacak veritabanı alanının boş(null) değerlere izin verip vermeyeceği bu kısımdan belirtilir.

## Olaylar

Nesnenin sahip olduğu olaylar, Özellik Görüntüleyici panelindeki "Olaylar" sekmesinde yer almaktadır. Her bir olay, farklı çalışma anlarında tetiklenerek kendilerine özgü işlemleri gerçekleştirir. Bu olaylara geliştirici tarafından yazılan kodlar da ilgili olayın tetiklendiği anda çalıştırılır.

"Client" alanında bulunan olaylara çift tıklandığında ekran, TypeScript kodlamanın yapılabileceği "Formadı.ts" isimli form kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur.

"Server" alanında bulunan olaylara çift tıklandığında ekran, C# kodlamanın yapılabileceği "Formadı.cs" isimli form kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur.

Geliştirici bu methodlar içerisinde istediği kod bloğunu kurgulayabilir. Olaylar sekmesinden tıklanarak kod tarafında methodu oluşturulmuş olayın yanında, method adı bilgisi otomatik oluşturularak, olayla method arasındaki ilişki belirtilmiş olur.

![Transfer](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc3876ee8-5d26-4c50-ad0d-17b31ae0d976)

Oluşan methodlar;

![Transfer](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfa7e1304-cbd9-4646-b9b4-b4f955895145)

![Transfer](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2d5dac48-e39d-41e9-8a6f-f6c569e2c222)