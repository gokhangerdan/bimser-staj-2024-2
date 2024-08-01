---
sidebar_position: 10
custom_edit_url: ""
---

# RadioList

Aynı gruba dahil birden çok Radio nesnesini liste halinde gösteren nesnedir. Forma birden çok Radio nesnesi koyup gruplandırmak yerine, aynı gruba dahil olan seçenekleri tek bir RadioList nesnesinin elemanları olarak eklemeye yarar.

Geliştirme arayüzünde aktif ekran form iken, Araç Kutusu panelinde form nesneleri listelenir. Nesne, araç kutusu panelinden sürükle/bırak yöntemi ile forma eklenir.

![RadioList](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7551afec-ef94-4550-87d5-3140dc7b98c3)

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

![RadioList](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8b62f004-f544-4124-ac98-31bc1fcb0d32)

</div>

Seçenek olarak **"Dinamik"** seçildiğinde; nesneye veriler, bir veri kaynağından dinamik olarak yüklenecek demektir. Dinamik seçeneği seçildiğinde Datasource alanında **Datasource** ve **Run at Server** özellikleri görünür olacaktır.

<div style={{textAlign: 'center'}}>

![RadioList](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9ef52d83-9b5e-4900-98a0-18591ec34e83)

</div>

Seçenek olarak **"Statik"** seçildiğinde ise, nesneye manuel eleman eklenecek demektir ve veri kaynağı alanında **Items** özelliği görünür olur.

<div style={{textAlign: 'center'}}>

![RadioList](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload06253705-3f72-4842-9477-bb767902256a)

</div>

:::note

Bu kısımdan itibaren nesnede type alanında **dinamik** değeri seçilirse nesne kullanımı açıklanacaktır. **Statik** kullanımdaki özellikleri görüntülemek için ilgili bölümü açabilirsiniz.

:::

<details>
  <summary>Dinamik kullanım detaylarını görüntülemek için tıklayın!</summary>
  <div>

`DataSource` - Nesnede, bir veri kaynağından gelen değerleri listeleyebilmek için kullanılacak alandır. Projede Çözüm Gezgini alanındaki DataSource bölümüne eklenmiş ve başarıyla derlenen veri kaynağı tanımı, nesnenin Datasource) kısmından seçilebilir olur.

![RadioList](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload62b14548-2174-4ca6-89b3-c579890961ea)

![RadioList](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada39f055e-3087-47d8-a490-2e0bc7cc6d36)

`RunAtServer` - Bu seçenek nesneye bağlanan sorgunun, sunucudan mı istemciden mi çalıştırılacağının belirlendiği seçenektir.

Bu seçenek aktif edilirse web arayüzünde forma tıklandığında, form açılmadan önce sorgu, sunucu tarafında çalıştırılır, form açıldığında nesneye sorgu sonucu yüklenmiş olarak gelir. Seçenek pasif yapıldığında web arayüzünde forma tıklandığında, form açıldıktan sonra nesneye sorgunun sonuç değerleri yüklenmeye başlar.

Sorgu sonucunun yüklenmesi için geçen bekleme süresi, bu özellik aktifken formun açılma anında, özellik pasifken form hızlı açıldıktan sonra nesneye verinin yüklenmesi anında etkili olur.

`Value Expression` - Veri Kaynağı kısmından bir veri kaynağı tanımı seçildiğinde bu alan görünür olur. Seçilen veri kaynağından dönen tüm kolonlar bu alanda listelenir. Kullanıcı arayüzden seçim yaptığında, yapılan seçimin kayıt alanının hangi kolon değeri olacağı bu alanda belirlenir.

Örneğin nesneye kullanıcıların listesini getiren bir sorgu bağlanmış olsun. Sorgudan ID (Kullanıcı Adı), FIRSTNAME (İsim), EMAIL (Mail Adresi) kolonları dönüyor olsun. Bu nesnenin amacı kullanıcı seçimi olduğu için seçilen kullanıcının benzersiz kayıt değeri ID kolonunda bulunduğundan, Değer İfadesi kısmında sorgudan dönen ID kolonu seçilmelidir.

![RadioList](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload457cb79f-e3e2-4316-961e-6488c0f04155)

`Display Expression` - Veri Kaynağı kısmından bir veri kaynağı tanımı seçildiğinde bu alan görünür olur. Seçilen veri kaynağından dönen tüm kolonlar bu alanda listelenir. Kullanıcı arayüzden seçim yaptığında, nesne içerisinde görünecek ifadenin hangi sorgu kolonundan geleceği bu alanda belirlenir.

![RadioList](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload18ccb8b3-e405-4679-9974-c2d8655c3d38)

Örneğin nesneye kullanıcıların listesini getiren bir sorgu bağlanmış olsun. Sorgudan ID (Kullanıcı Adı), FIRSTNAME (İsim), LASTNAME (Soyisim), EMAIL (Mail Adresi) kolonları dönüyor olsun. Bu nesnenin amacı kullanıcı seçimi olduğu için seçilen kullanıcının FIRSTNAME ve LASTNAME kolonlarından dönen değerleri nesne içinde görüntülenmek istenecektir. O yüzden Görünür İfadesi kısmında bu kolon değerleri seçilir.

![RadioList](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade3f24768-9fe3-4806-b989-bd59ea4a29f9)

`Display Format` - Görünüm İfadesi alanından seçilen kolon ya da kolonlar otomatik olarak bu alana da eklenir. Nesnede listelenecek eleman metinlerine görünüm formatı belirlemek için kullanılan alandır. Elemanların istenen bir formatta gösterilmesi için, ilgili format yapısı bu alanda belirtilebilir. Ve nesne seçimi sonrası nesnede görüntülenecek değerin web arayüzde uç kullanıcılara belirlenen formatta görünmesi sağlanabilir.

Formatlamada kullanılabilecek format tiplerine, alana odaklanıldığında çıkan bilgi mesajındaki linkten (https://shopify.github.io/liquid/) erişilebilir ve gerçekleştirilmek istenen format yapısı Görünüm Formatı alanında ilgili sütun için uygulanabilir.

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

![RadioList](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload093c8d12-5f52-4fb1-a329-caf5c0fba856)

Elemanlar alanına tıklandığında eleman ekleme penceresi açılır. Ekle butonuna tıklanarak nesneye yeni eleman kalemleri oluşturulur.

![RadioList](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfbe5f80d-fc74-4a77-98e6-f266f9d82c39)

Girilen elemanın **Value** ve **Title** alanları doldurulur. Ögenin Selected alanı aktif edilirse web ara yüzünde nesne içinde bu öge otomatik olarak seçilmiş gibi gösterilecektir. "Kaydet" butonuna basılarak nesneye eleman ekleme işlemi tamamlanır.

![RadioList](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd3bff03e-c33c-41d0-84c9-2bb37bf435e0)

Bu alana eklenmiş bir eleman düzenlenmek istendiğinde, ilgili eleman kaydına tıklanarak yan tarafta açılan eleman detayları penceresinden düzenleme yapılabilir. Mevcut bir eleman silinmek istendiğinde ise eleman detaylarındaki sil butonu kullanılır.

![RadioList](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddee24a61-8af7-4d15-9469-bfcee2780429)

Web arayüzde nesneye tıklandığında, Elemanlar alanında belirlenen eleman kayıtları, kullanıcının seçim yapması için listelenir.

RadioList nesnesinde görünüm;

![RadioList](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3e05dd9e-2343-4bc9-9f80-a9e62d07c5ee)

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

`Button Type` - Nesne elemanlarının düğme şeklinde mi yoksa buton şeklinde mi görüneceğinin ayarlandığı kısımdır. Bu alanda “Radio” ve “Button” seçenekleri listelenir.

<div style={{textAlign: 'center'}}>

![RadioList](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0f906098-63fd-4403-9d73-3b9979bddf4a)

</div>

`Direction` - Nesne elemanlarının Yatay ya da Dikey konumlandırılmasının sağlandığı kısımdır.

>Yapılabilecek Seçimler : Horizontal, Vertical

![RadioList](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade39aa194-780b-4eac-8ba5-4a2968cd5e15)

`Show Search` - Nesnenin değer verisinin tutulduğu alandır. Veritabanında nesne değeri bu alanda yazılan veri olarak tutulur.

### Behavior

`ReadOnly` - Nesnenin düzenleme modunda olup olmayacağının ayarlandığı kısımdır. Bu özellik aktif edildiğinde nesne veri girişine izin vermez, salt okunur modda olur. Nesneye veri girişine izin verilmesi için özelliğin pasif olması gerekir.

`Tab Index` - Bu alana sayısal değerler girilerek, tab butonuna basıldığında form nesneleri arasında hangi sıra ile odaklanılacağı belirlenir. Form doldurulurken imleci, veri girilmek istenen nesneye tıklamak yerine, tab butonuna basarak belirli bir sırayla indekslenmiş nesnelere direk odaklanılması sağlanmış olur. Bu da form doldurma hızını artıran bir özelliktir.

`Required` - Nesnede veri girişinin zorunlu olup olmayacağının belirlendiği alandır. Bu özellik aktif edildiğinde nesne içerisine veri girişi yapılmadan formun ilerletilmesi/kaydedilmesi gerçekleştirilemez.

`Value Type` - Nesne elemanlarının tipinin belirlendiği alandır. Burada belirlenen tipe göre, Elemanlar alanında eklenen satırın Değer alanı tipi değiştirilir. Aynı zamanda nesneye parametrik bir sorgu bağlandığında, parametre tipi ile Değer Tipi alanından seçilen tip değeri aynı olmalıdır. 

:::caution DİKKAT

Nesnenin Datasource alanında **Type : Statik** seçili ise ve eleman ekli ise Value Type alanı seçim yapılamaz durumuna geçer.

:::

### Data Definition Language

`Field Name` - Sistemin veri tabanında, nesne için oluşturacağı kolonun adının belirlendiği alandır. "İsim (Name)" kısmında nesneye başka bir isim verilip, veritabanı tablosunda nesne için oluşturulacak kolon adı farklı bir isim olarak yaratılabilir.

`Allow Null` - Nesne için oluşturulacak veritabanı alanının boş(null) değerlere izin verip vermeyeceği bu kısımdan belirtilir.

## Olaylar

Nesnenin sahip olduğu olaylar, Özellik Görüntüleyici panelindeki "Olaylar" sekmesinde yer almaktadır. Her bir olay, farklı çalışma anlarında tetiklenerek kendilerine özgü işlemleri gerçekleştirir. Bu olaylara geliştirici tarafından yazılan kodlar da ilgili olayın tetiklendiği anda çalıştırılır.

**"Client"** alanında bulunan olaylara çift tıklandığında ekran, TypeScript kodlamanın yapılabileceği **"Formadı.ts"** isimli form kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur.

**"Server"** alanında bulunan olaylara çift tıklandığında ekran, C# kodlamanın yapılabileceği **"Formadı.cs"** isimli form kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur.

Geliştirici bu methodlar içerisinde istediği kod bloğunu kurgulayabilir. Olaylar sekmesinden tıklanarak kod tarafında methodu oluşturulmuş olayın yanında, method adı bilgisi otomatik oluşturularak, olayla method arasındaki ilişki belirtilmiş olur.

![RadioList](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadad0d447e-bb59-47b5-8205-204cb1d8a5f2)

Oluşan methodlar;

![RadioList](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf81754b6-c5f5-4165-8407-c6c0e1465f63)

![RadioList](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc56e64ef-535d-4af0-9893-60984c658dcd)