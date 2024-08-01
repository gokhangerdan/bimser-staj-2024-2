# FishBone

FishBone nesnesi, balık kılçığı diyagramı ya da bir başka ismiyle sebep sonuç diyagramına karşılık gelmektedir.
Sonuçları ortaya çıkaran sebepleri ortaya koymak, görselleştirmek ve üzerinde çalışmak için bu nesneden yararlanılır. Karşılaşılan problemi oluşturan bütün sebepler, bir takım birbirinden farklı sıkıntı kaynakları nedeniyle ortaya çıkar.
Bu nesne ile probleme götüren sebepler, genel olarak bu kaynakları tespit edebilmek maksadıyla, ana kategorilerine ayrılarak dallandırılır.
Geliştirme arayüzünde aktif ekran form iken, Araç Kutusu panelinde form nesneleri listelenir. Nesne, araç kutusu panelinden sürükle/bırak yöntemi ile forma eklenir.


## Genel[​](https://docs.bimser.net/docs/Synergy/CSP/ide-objects/form/advanced-form-controls/FishBone#genel "Başlığa doğrudan bağlantı")

### Design[​](https://docs.bimser.net/docs/Synergy/CSP/ide-objects/form/advanced-form-controls/FishBone#design "Başlığa doğrudan bağlantı")

`Name`  - Nesnenin sistem tarafında kullanılacak ismidir. Başka bir nesnenin içinde ve kod tarafında nesneye, isim alanında yazan değerle erişim sağlanır.

### Caption[​](https://docs.bimser.net/docs/Synergy/CSP/ide-objects/form/advanced-form-controls/FishBone#caption "Başlığa doğrudan bağlantı")

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

### DataSource[​](https://docs.bimser.net/docs/Synergy/CSP/ide-objects/form/advanced-form-controls/FishBone#dataSource "Başlığa doğrudan bağlantı")

`Type`  - Nesneye hangi tipte veri ekleneceğinin seçimi bu alandan yapılır. Tip alanında “Dinamik” ve “Statik” olarak iki seçenek listelenir.
Seçim yapılan tipe göre veri kaynağı bölümünde görünen özellikler değişiklik gösterecektir.
> Yapılabilecek Seçimler : Dinamik, Statik
![datasource-type](https://docsbimser.blob.core.windows.net/imagecontainer/FishBoneDataSource-4d5a9386-f65e-40a3-aae4-34224e636903.png)

Seçenek olarak **“Dinamik”** seçildiğinde; Datasource alanında projede tanımlı bir sorgu seçildiğinde nesneye veriler, bir veri kaynağından dinamik olarak yüklenebilir.
Seçenek olarak **"Statik"** seçildiğinde ise, nesneye manuel eleman eklenecek demektir ve veri kaynağı alanında **Items** özelliği görünür olur.

:::note NOT
Bu kısımdan itibaren nesnede type alanında  **dinamik**  değeri seçilirse nesne kullanımı açıklanacaktır.  **Statik**  kullanımdaki özellikleri görüntülemek için ilgili bölümü açabilirsiniz.
:::

<details>
<summary>Dinamik kullanım detaylarını görüntülemek için tıklayın!</summary>
<div>
  
`DataSource` - Nesnede, bir veri kaynağından gelen değerleri listeleyebilmek için kullanılacak alandır. Projede Çözüm Gezgini alanındaki DataSource bölümüne eklenmiş ve başarıyla derlenen veri kaynağı tanımı, nesnenin Datasource kısmından seçilebilir olur.  

![DataSource-Dinamik](https://docsbimser.blob.core.windows.net/imagecontainer/FishBoneDataSource-Dinamik-8f175156-051b-49ac-86a3-e9063e008994.png)

<div style={{textAlign: 'center'}}>

![kullanicilarigetir](https://docsbimser.blob.core.windows.net/imagecontainer/FishBoneKullanicilariGetir-ec53ebad-cb84-49d8-85a8-b3219f683604.png)

</div>


`Value Expression` - Veri Kaynağı kısmından bir veri kaynağı tanımı seçildiğinde bu alan görünür olur. Seçilen veri kaynağından dönen tüm kolonlar bu alanda listelenir. Kullanıcı arayüzden seçim yaptığında, yapılan seçimin kayıt alanının hangi kolon değeri olacağı bu alanda belirlenir.

Örneğin nesneye kullanıcıların listesini getiren bir sorgu bağlanmış olsun. Sorgudan ID (Kullanıcı Adı), FIRSTNAME (İsim), LASTNAME (Soyisim) kolonları dönüyor olsun. Bu nesnenin amacı kullanıcı seçimi olduğu için seçilen kullanıcının benzersiz kayıt değeri ID kolonunda bulunduğundan, Değer İfadesi kısmında sorgudan dönen ID kolonu seçilmelidir.

![FishBone-Dinamik-value](https://docsbimser.blob.core.windows.net/imagecontainer/FishBone-Dinamik-Value-2ffe6f1c-059e-4aa2-aca5-82e80fbf3ee4.png)

`Display Expression` - Veri Kaynağı kısmından bir veri kaynağı tanımı seçildiğinde bu alan görünür olur. Seçilen veri kaynağından dönen tüm kolonlar bu alanda listelenir. Kullanıcı arayüzden seçim yaptığında, nesne içerisinde görünecek ifadenin hangi sorgu kolonundan geleceği bu alanda belirlenir.

Örneğin nesneye kullanıcıların listesini getiren bir sorgu bağlanmış olsun. Sorgudan ID (Kullanıcı Adı), FIRSTNAME (İsim), LASTNAME (Soyisim), EMAIL (Mail Adresi) kolonları dönüyor olsun. Bu nesnenin amacı kullanıcı seçimi olduğu için seçilen kullanıcının FIRSTNAME ve LASTNAME kolonlarından dönen değerler nesne içinde görüntülenmek istenecektir. O yüzden Görünür İfadesi kısmında bu kolon değerleri seçilir.
  

![FishBone-Dinamik-Display](https://docsbimser.blob.core.windows.net/imagecontainer/FishBone-Dinamik-Display-92839bd5-fca3-4f98-8e3d-d8a7f5d4c2b8.png)

  
`Display Format` - Görünüm İfadesi alanından seçilen kolon ya da kolonlar otomatik olarak bu alana da eklenir. Nesnede listelenecek eleman metinlerine görünüm formatı belirlemek için kullanılan alandır. Elemanların istenen bir formatta gösterilmesi için, ilgili format yapısı bu alanda belirtilebilir. Ve nesne seçimi sonrası nesnede görüntülenecek değerin web arayüzde uç kullanıcılara belirlenen formatta görünmesi sağlanabilir.

Formatlamada kullanılabilecek format tiplerine, alana odaklanıldığında çıkan bilgi mesajındaki linkten ([https://shopify.github.io/liquid/)](https://shopify.github.io/liquid/) "https://shopify.github.io/liquid/)") erişilebilir ve gerçekleştirilmek istenen format yapısı Görünüm Formatı alanında ilgili sütun için uygulanabilir.

![FishBone-Dinamik-DisplayFormat](https://docsbimser.blob.core.windows.net/imagecontainer/FishBone-Dinamik-DisplayFormat-ccde0dc3-142e-4fc3-b08c-3c06675a4278.png)

Ana nedenlerde bulunan alanlar artık bu dinamik sorgudan gelen değerlerden seçilebilir.


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

`Items` - Nesnede, bir veri kaynağından gelen kayıtlar değil, geliştirme anında manuel eklenen elemanlar listelenmek istendiğinde, eleman tanımlama işlemi bu alandan yapılır. Liste elemanlarının belirlendiği kısımdır. Bu alandan nesneye yeni eleman eklenebilir, mevcut bir eleman silinebilir veya düzenlenebilir. Items alanındaki değerler **Ana Sebep**'lere(Main Reason),  altında bulunan alanlar ise **Alt Sebep**'lere(Sub Reason) karşılık gelmektedir.

![FishBoneStatik](https://docsbimser.blob.core.windows.net/imagecontainer/FishBone%20Static-6c659724-5dc7-4bbf-868c-fc30840d8cba.png)

Nesnenin statik elemanlarında varsayılan olarak Ekipman, Çevre, Yönetim, Materyal, İnsanlar, Süreç olmak üzere 6 alan gelmektedir. Bu alanlar silinebilir ve düzenlenebilir.

Elemanlar alanına tıklandığında eleman ekleme penceresi açılır. Ekle butonuna tıklanarak nesneye yeni eleman kalemleri oluşturulur.

Açılan pencerenin sağ tarafında **Main Reason** bölümünün altında girilen elemanın **Key** ve **Title** alanları doldurulur. Elemanın ikona sahip olması istenirse **Icon** alanı içindeki ikon kütüphanesinden seçim yapılabilir. **Selected Index** alanında bulunduğu sıra numarası verilir.

![FishBone Static Items](https://docsbimser.blob.core.windows.net/imagecontainer/FishBone%20Static%20Items-9d641e06-f190-4a9f-bc3e-70aebbf66489.png)

:::info Bilgi
**Reasons** alanındaki **Sub Reason Text** özelliği pasif duruma çekildiğinde **Main Reason** kısmının altında **Data Source** alanı da açılır. Uç kullanıcı dilerse Ana Sebep başlıklarının altında bulunan alt sebeplerde dinamik bir veri kaynağından gelen veriler üzerinden seçim yapabilir. 
:::

Web arayüzde nesneye tıklandığında, Elemanlar alanında belirlenen eleman kayıtları, kullanıcının seçim yapması için listelenir.
FishBone nesnesinde **Sub Reason** alanı pasif olduğundaki görünüm:
![SubReasonFalse](https://docsbimser.blob.core.windows.net/imagecontainer/FishBone-Sub%20Reason%20Text%20kapal%C4%B1-de4d996c-6770-4a10-a662-8b910bd156af.png)

Web arayüzde nesneye tıklandığında, Elemanlar alanında belirlenen eleman kayıtları, kullanıcının seçim yapması için listelenir.
FishBone nesnesinde **Sub Reason** alanı aktif olduğundaki görünüm:
![SubReasonTrue](https://docsbimser.blob.core.windows.net/imagecontainer/FishBone-Sub%20Reason%20Text%20A%C3%A7%C4%B1k-a8808a02-c1f3-47b1-9f08-bb76f57640ec.png)
:::info Bilgi
Alt sebeplere girilen alanlar kaldırılabilir veya Gerçek Sebep olarak işaretlenebilir. Gerçek Sebep olarak işaretlendiğinde alanın sol tarafında bir ünlem işareti konumlandırılır.
:::
</div>
</details>

### Appearance[​](https://docs.bimser.net/docs/Synergy/CSP/ide-objects/form/advanced-form-controls/FishBone#appearance "Başlığa doğrudan bağlantı")

`Visible`  - Nesnenin gizlenip, görünür yapılma ayarlarının gerçekleştirildiği kısımdır. Bu alan aktifken, nesne form üzerinde görünür durumdadır. Alan pasif yapıldığında nesne görünmez olur.

`Client Visible`  - Form ilk açıldığında nesne görünmesin, belirli bir şart sağlandığında nesne görünür olsun gibi bir işlem yapılmak istendiğinde, nesnenin istemci tarafında görünmez olması için bu alan pasif yapılır. Kodla ya da Kural Yöneticisi ile belirlenen şart sağlandığında nesne tekrar görünür hale getirilebilir. Sunucu görünürlüğü aktif değilken, istemci müdahale edemez ancak istemci görünürlüğü aktif değilken sunucu müdahale edebilir.

`Enabled`  - Nesnenin etkin modu bu alandan ayarlanır. Bu özellik aktifken nesneye veri girişi sağlanabilir ve nesne düzenlenebilir. Özellik pasifken, nesne düzenlenemez moddadır ve pasif görünür.

`Client Enabled`  - Form ilk açıldığında nesne etkin olmasın, belirli bir şart sağlandığında etkin olsun gibi bir işlem yapılmak istendiğinde, nesnenin istemci tarafında etkin olmaması için bu alan pasif yapılır. Kodla ya da Kural Yöneticisi ile belirlenen şart sağlandığında nesne tekrar etkin hale getirilebilir. Sunucu etkinliği aktif değilken, istemci müdahale edemez ancak istemci etkinliği aktif değilken sunucu müdahale edebilir.

`Background Color`  - Nesneye arka plan rengi vermek için kullanılan alandır.

`Title`  - Form arayüzde açıkken imleç ile nesne üzerine gelindiğinde, bu alanda yazılan metin, ipucu olarak gösterilir. Nesne ile ilgili detay bilgi verilmek istendiğinde kullanılan, uç kullanıcıyı yönlendirme amaçlı bir özelliktir.

`ClassName`  - Forma ait CSS dosyası içinde yazılmış bir class'ın tanımlanarak nesne görünürlüğünün değiştirilebildiği alandır.

`Problem` - FishBone nesnesinin sebep kırılımlarının bağlandığı orta gövdede bulunan Problem başlığının belirlendiği alandır.

### Reasons[​](https://docs.bimser.net/docs/Synergy/CSP/ide-objects/form/advanced-form-controls/FishBone#reasons "Başlığa doğrudan bağlantı")

`Main Reason No` - Ana sebeplerin sayısının belirlendiği alandır. Sebep sayısı 6'nın üzerine çıkmamaktadır.

`Sub Reason No` - Alt sebeplerin sayısının belirlendiği alandır. Alt sebeplerin sayısı da 10'un üzerine çıkmamaktadır.

`Sub Reason Text` - Alt sebeplerin kullanıcı tarafından eklenip eklenememesinin kontrol edildiği alandır. Aktif edildiğinde uç kullanıcılar alt sebepler ekleyebilmekte, pasif duruma getirildiğinde ise ekleyememektedir.

### Behavior[​](https://docs.bimser.net/docs/Synergy/CSP/ide-objects/form/advanced-form-controls/FishBone#behavior "Başlığa doğrudan bağlantı")

`Readonly` - Nesnenin düzenleme modunda olup olmayacağının ayarlandığı kısımdır. Bu özellik aktif edildiğinde nesne veri girişine izin vermez, salt okunur modda olur. Nesneye veri girişine izin verilmesi için özelliğin pasif olması gerekir.

### Data Definition Language[​](https://docs.bimser.net/docs/Synergy/CSP/ide-objects/form/advanced-form-controls/FishBone#data-definition-language "Başlığa doğrudan bağlantı")

`Field Name` - Sistemin veri tabanında, nesne için oluşturacağı kolonun adının belirlendiği alandır. "İsim (Name)" kısmında nesneye başka bir isim verilip, veritabanı tablosunda nesne için oluşturulacak kolon adı farklı bir isim olarak yaratılabilir.

## Olaylar[​](https://docs.bimser.net/docs/Synergy/CSP/ide-objects/form/advanced-form-controls/FishBone#olaylar "Başlığa doğrudan bağlantı")

Nesnenin sahip olduğu olaylar, Özellik Görüntüleyici panelindeki “Olaylar” sekmesinde yer almaktadır. Her bir olay, farklı çalışma anlarında tetiklenerek kendilerine özgü işlemleri gerçekleştirir. Bu olaylara geliştirici tarafından yazılan kodlar da ilgili olayın tetiklendiği anda çalıştırılır.

“Client” alanında bulunan olaylara çift tıklandığında ekran, TypeScript kodlamanın yapılabileceği “Formadı.ts” isimli form kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur.

“Server” alanında bulunan olaylara çift tıklandığında ekran, C# kodlamanın yapılabileceği “Formadı.cs” isimli form kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur.

Geliştirici bu methodlar içerisinde istediği kod bloğunu kurgulayabilir. Olaylar sekmesinden tıklanarak kod tarafında methodu oluşturulmuş olayın yanında, method adı bilgisi otomatik oluşturularak, olayla method arasındaki ilişki belirtilmiş olur.
![fishboneolaylar](https://docsbimser.blob.core.windows.net/imagecontainer/FishBoneOlaylar-744ca249-d5ce-4e0c-897b-8364240a2ee1.png)

Oluşan methodlar;
![FishBoneTs](https://docsbimser.blob.core.windows.net/imagecontainer/FishBoneTS-17e263a1-8d10-4adb-ad45-584e043f67e1.png)

![FishBoneCS](https://docsbimser.blob.core.windows.net/imagecontainer/FishBoneCS-7763b99c-8642-446f-88ef-9650f9f47dac.png)
