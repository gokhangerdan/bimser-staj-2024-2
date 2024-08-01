---
sidebar_position: 18
custom_edit_url: ""
---

# Scheduler

Uç kullanıcının bir takvim üzerinde belli bir tarih/tarih aralığındaki toplantı, etkinlik, randevu gibi türleri ekleyip, görsel olarak listelenmesini sağlayan nesnedir.

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

`DataSource` - Nesnede, bir veri kaynağından gelen değerleri listeleyebilmek için kullanılacak alandır. Projede Çözüm Gezgini alanındaki DataSource bölümüne eklenmiş ve başarıyla derlenen veri kaynağı tanımı, nesnenin Datasource) kısmından seçilebilir olur.

`RunAtServer` - Bu seçenek nesneye bağlanan sorgunun, sunucudan mı istemciden mi çalıştırılacağının belirlendiği seçenektir.

Bu seçenek aktif edilirse web arayüzünde forma tıklandığında, form açılmadan önce sorgu, sunucu tarafında çalıştırılır, form açıldığında nesneye sorgu sonucu yüklenmiş olarak gelir. Seçenek pasif yapıldığında web arayüzünde forma tıklandığında, form açıldıktan sonra nesneye sorgunun sonuç değerleri yüklenmeye başlar.

Sorgu sonucunun yüklenmesi için geçen bekleme süresi, bu özellik aktifken formun açılma anında, özellik pasifken form hızlı açıldıktan sonra nesneye verinin yüklenmesi anında etkili olur.

:::info BİLGİ

Nesnede data source tanımlı olduğunda value/display expression alanları aktif olmayacaktır. Data Source kolonlarına uygun verinin gösterimi Columns alanı içinde yapılacaktır.

:::

:::danger DİKKAT!

Nesneye Data Source eklediğinizde, tanımladığınız veri kaynağının **mutlaka** Id, Başlık, Başlangıç Tarihi ve Bitiş Tarihi kolonları döndürdüğünden emin olunuz. Nesnenin veri kaynağı ile birlikte kullanımı için listenen 4 kolon zorunludur.

:::

### Editing

`Enabled` - Nesnede editleme özelliklerinden herhangi bir tanesi kullanılacaksa alan aktif edilmelidir.

`Addable` - Nesnede öge ekleme işlemi aktif edilmesi istenirse alan aktif edilmelidir. Enable alanının da aktif olması zorunludur.

`Deletable` - Nesnede ekli ögenin silinebilmesi işlemi aktif edilmesi istenirse alan aktif edilmelidir. Enable alanının da aktif olması zorunludur.

`Editable` - Nesnede ekli ögenin düzenlenebilmesi işlemi aktif edilmesi istenirse alan aktif edilmelidir. Enable alanının da aktif olması zorunludur.

### Appearance

`Visible` - Nesnenin gizlenip, görünür yapılma ayarlarının gerçekleştirildiği kısımdır. Bu alan aktifken, nesne form üzerinde görünür durumdadır. Alan pasif yapıldığında nesne görünmez olur.

`Client Visible` - Form ilk açıldığında nesne görünmesin, belirli bir şart sağlandığında nesne görünür olsun gibi bir işlem yapılmak istendiğinde, nesnenin istemci tarafında görünmez olması için bu alan pasif yapılır. Kodla ya da Kural Yöneticisi ile belirlenen şart sağlandığında nesne tekrar görünür hale getirilebilir. Sunucu görünürlüğü aktif değilken, istemci müdahale edemez ancak istemci görünürlüğü aktif değilken sunucu müdahale edebilir.

`Enabled` - Nesnenin etkin modu bu alandan ayarlanır. Bu özellik aktifken nesneye veri girişi sağlanabilir ve nesne düzenlenebilir. Özellik pasifken, nesne düzenlenemez moddadır ve pasif görünür.

`Client Enabled` - Form ilk açıldığında nesne etkin olmasın, belirli bir şart sağlandığında etkin olsun gibi bir işlem yapılmak istendiğinde, nesnenin istemci tarafında etkin olmaması için bu alan pasif yapılır. Kodla ya da Kural Yöneticisi ile belirlenen şart sağlandığında nesne tekrar etkin hale getirilebilir. Sunucu etkinliği aktif değilken, istemci müdahale edemez ancak istemci etkinliği aktif değilken sunucu müdahale edebilir.

`Background Color` - Nesneye arka plan rengi vermek için kullanılan alandır.

`Title` - Form arayüzde açıkken imleç ile nesne üzerine gelindiğinde, bu alanda yazılan metin, ipucu olarak gösterilir. Nesne ile ilgili detay bilgi verilmek istendiğinde kullanılan, uç kullanıcıyı yönlendirme amaçlı bir özelliktir.

`ClassName` - Forma ait CSS dosyası içinde yazılmış bir class'ın tanımlanarak nesne görünürlüğünün değiştirilebildiği alandır.

`Columns` - Nesne üzerindeki ögelerde gösterilecek alanların tasarlandığı bölümdür. Varsayılan olarak No, Başlık, Başlangıç tarihi, Bitiş tarihi kolonları gelmektedir. Varsayılan kolonlarda `No` kolonu birincil anahtar, `Başlık` kolonu ögenin Scheduler üzerinde gösterilecek başlığı ve `Başlangıç/Bitiş tarihi` kolonları Sheduler'da ögenin gösterileceği aralığı belirlemekte kullanılmaktadır.

Columns alanında Boolean, Date, Date Time, Number, Select, Text, Time tiplerinde kolon eklenebilmektedir.

Tiplerin özellikleri hakkında bilgi almak için, aşağıdan her tipin kendisine ait paneli açarak inceleyebilirsiniz.

<details>
  <summary>Boolean türünde kolon özellikleri için tıklayın</summary>
  <div>

**General**

| **Özellik**  	| **Açıklama**                                                                                                                                             	|
|--------------	|----------------------------------------------------------------------------------------------------------------------------------------------------------	|
| Column Name  	| Nesnede eklenen kolonun adının tanımlandığı alandır.                                                                                                     	|
| Column Title 	| Nesne eklenen kolonun web ara yüzünde gösterileceği başlığın tanımlandığı alandır.                                                                       	|
| Source       	| Nesnede Data Source alanında bir veri kaynağı seçili olduğunda aktif olur. Veri kaynağındaki kolonun nesnedeki kolon ile eşleştirilmesi için kullanılır. 	|
| Width        	| Kolon genişliğinin ayarlandığı özelliktir, piksel değerinden giriş yapılması gereklidir.                                                                 	|
| Visible      	| Kolonun web ara yüzünde görünüp görünmeyeceğinin belirlendiği alandır.                                                                                   	|
| Edit Type    	| Kolon türünün (boolean, text, date vb.) gösterildiği özelliktir.                                                                                         	|
| Align        	| Kolonda girilecek verinin hizalanma yönünün seçildiği özelliktir.                                                                                        	|
| Primary Key  	| Kolon birincil anahtar olarak işaretlenmesi gerekiyorsa bu seçenek aktif edilmelidir..                                                                   	|
| Editable     	| Kolonda değişiklik yapılıp yapılamayacağının belirlendiği özelliktir.                                                                                    	|

**Control Properties**

| **Özellik**  	| **Açıklama**                                                                                                                                             	|
|--------------	|----------------------------------------------------------------------------------------------------------------------------------------------------------	|
| Column Name  	| Nesnede eklenen kolonun adının tanımlandığı alandır.                                                                                                     	|
| Column Title 	| Nesne eklenen kolonun web ara yüzünde gösterileceği başlığın tanımlandığı alandır.                                                                       	|
| Source       	| Nesnede Data Source alanında bir veri kaynağı seçili olduğunda aktif olur. Veri kaynağındaki kolonun nesnedeki kolon ile eşleştirilmesi için kullanılır. 	|
| Width        	| Kolon genişliğinin ayarlandığı özelliktir, piksel değerinden giriş yapılması gereklidir.                                                                 	|
| Visible      	| Kolonun web ara yüzünde görünüp görünmeyeceğinin belirlendiği alandır.                                                                                   	|
| Edit Type    	| Kolon türünün (boolean, text, date vb.) gösterildiği özelliktir.                                                                                         	|
| Align        	| Kolonda girilecek verinin hizalanma yönünün seçildiği özelliktir.                                                                                        	|
| Primary Key  	| Kolon birincil anahtar olarak işaretlenmesi gerekiyorsa bu seçenek aktif edilmelidir..                                                                   	|
| Editable     	| Kolonda değişiklik yapılıp yapılamayacağının belirlendiği özelliktir.                                                                                    	|

  </div>
</details>

<details>
  <summary>Date türünde kolon özellikleri için tıklayın</summary>
  <div>

**General**

| **Özellik**  	| **Açıklama**                                                                                                                                             	|
|--------------	|----------------------------------------------------------------------------------------------------------------------------------------------------------	|
| Column Name  	| Nesnede eklenen kolonun adının tanımlandığı alandır.                                                                                                     	|
| Column Title 	| Nesne eklenen kolonun web ara yüzünde gösterileceği başlığın tanımlandığı alandır.                                                                       	|
| Source       	| Nesnede Data Source alanında bir veri kaynağı seçili olduğunda aktif olur. Veri kaynağındaki kolonun nesnedeki kolon ile eşleştirilmesi için kullanılır. 	|
| Width        	| Kolon genişliğinin ayarlandığı özelliktir, piksel değerinden giriş yapılması gereklidir.                                                                 	|
| Visible      	| Kolonun web ara yüzünde görünüp görünmeyeceğinin belirlendiği alandır.                                                                                   	|
| Edit Type    	| Kolon türünün (boolean, text, date vb.) gösterildiği özelliktir.                                                                                         	|
| Align        	| Kolonda girilecek verinin hizalanma yönünün seçildiği özelliktir.                                                                                        	|
| Primary Key  	| Kolon birincil anahtar olarak işaretlenmesi gerekiyorsa bu seçenek aktif edilmelidir..                                                                   	|
| Editable     	| Kolonda değişiklik yapılıp yapılamayacağının belirlendiği özelliktir.                                                                                    	|

**Control Properties**

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Visible 	| Kolonun görünürlüğünün belirlendiği özelliktir, sunucu tarafında çalışır. 	|
| Client Visible 	| Kolonun görünürlüğünün belirlendiği özelliktir, istemci tarafında çalışır. 	|
| Enabled 	| Kolonun aktif olup olmayacağının belirlendiği özelliktir, sunucu tarafında çalışır. 	|
| Client Enabled 	| Kolonun aktif olup olmayacağının belirlendiği özelliktir, istemci tarafında çalışır. 	|
| Background Color 	| Kolonun arka plan renginin değiştirildiği özelliktir. 	|
| Title 	| Web ara yüzünde kolon üzerine fare işaretçisi ile gelindiğinde, ipucu ifadesinin içeriğinde gösterilecek bilgi belirlenmesi için kullanılır.  	|
| ClassName 	| Kolonda forma ait CSS dosyası içinde yazılmış bir class'ın tanımlanarak nesne görünürlüğünün değiştirilebildiği alandır. 	|
| Value 	| Kolonda değerin ne olacağının belirlendi alandır, aktif edildiğinde web ara yüzünde kolon seçilmiş olarak gözükecektir. 	|
| Placeholder 	| Kolon içine uç kullanıcı tarafından girilmesi istenen veri bilgisini, nesne içerisinde bilgi amaçlı göstermek için kullanılan özelliktir. 	|
| Text Align 	| Kolon içine girilen ifadenin hizalanacağı yerin belirlenmesi için kullanılan alandır. Sola hizala, merkeze hizala, sağa hizala seçimleri yapılabilir. 	|
| Size Type 	| Kolon boyutunun belirlenebileceği alandır. 	|
| ReadOnly 	| Kolonun düzenleme modunda olup olmayacağının ayarlandığı kısımdır. Aktif edildiğinde kolonda veri girişi gerçekleştirilmez, salt okunur durumunda çalışır.  	|
| Tab Index 	| Alana sayısal değerler girilerek, tab butonuna basıldığında form nesneleri arasında hangi sıra ile odaklanılacağı belirlenir. 	|
| Required 	| Kolonda veri girişinin zorunlu olup olmayacağının belirlendiği alandır. 	|
| Format 	| Tarih ve saat gösterim formatının belirlendiği alandır. Varsayılan olarak tarih formatı: “YYYY-MM-DD”, tarih ve saat formatı: “YYYY-MM-DD HH:mm” şeklinde tanımlıdır. Gösterilmek istenen farklı format yapıları bu alanda belirtilebilir. 	|
| Show Time 	| Kolonda saat bilgisinin gösterilip gösterilmeyeceğinin belirlendiği alandır. Bu özellik aktifken, ara yüzde nesneye tıklandığında tarih seçim alanının yanında saat seçim alanı da görünür olur. 	|
| Show Today 	| Kolon içerisinde tarih seçimi yaparken, seçim ekranının altında “Bugün” isimli butonun çıkmasını sağlayan özelliktir. 	|
| Show Today As Default 	| Özellik aktif edildiğinde kolonda varsayılan olarak bugünün tarihi görünür olur. 	|
| Allow Clear 	| Özellik aktif edildiğinde, web ara yüzünde kolonda yapılan tarih seçiminin istenirse kaldırılabilmesi sağlanır. 	|
| Disable before 	| Aktif edildiğinde günümüzden itibaren geçmişte bir nokta öncesindeki tarih seçimlerinin engellenmesi için ayarlar (gün, ay ve yıl değerleri tanımı) devreye girecektir.<br/> **Disable before years:** Girilen değere göre, günümüzden itibaren **x** yıl öncesine kadar tarih seçimi aktif olacaktır. **x yıl + 1 gün** öncesine gidildiğinde seçim yapılamayacaktır.<br/> **Disable before months:** Girilen değere göre, günümüzden itibaren **x** ay öncesine kadar tarih seçimi aktif olacaktır. **x ay + 1 gün** öncesine gidildiğinde seçim yapılamayacaktır.<br/> **Disable before days:** Girilen değere göre, günümüzden itibaren **x** gün öncesine kadar tarih seçimi aktif olacaktır. **x gün + 1 gün** öncesine gidildiğinde seçim yapılamayacaktır.<br/> 	|
| Disable after 	| Aktif edildiğinde günümüzden itibaren gelecekte bir nokta sonrasındaki tarih seçimlerinin engellenmesi için ayarlar (gün, ay ve yıl değerleri tanımı) devreye girecektir.<br/> **Disable after years:** Girilen değere göre, günümüzden itibaren **x** yıl geleceğe kadar tarih seçimi aktif olacaktır. **x yıl + 1 gün** ilerisine gidildiğinde seçim yapılamayacaktır.<br/> **Disable after months:** Girilen değere göre, günümüzden itibaren **x** ay geleceğe kadar tarih seçimi aktif olacaktır. **x ay + 1 gün** ilerisine gidildiğinde seçim yapılamayacaktır.<br/> **Disable after days:** Girilen değere göre, günümüzden itibaren **x** gün geleceğe kadar tarih seçimi aktif olacaktır. **x gün + 1 gün** ilerisine gidildiğinde seçim yapılamayacaktır. 	|
| Field Name 	| Sistemin veri tabanında, alan için oluşturacağı SQL kolon adının belirlendiği alandır. 	|
| Allow Null 	| Kolon için oluşturulacak veri tabanı alanının boş(null) değerlere izin verip vermeyeceği bu kısımdan belirtilir. 	|

  </div>
</details>

<details>
  <summary>Date Time türünde kolon özellikleri için tıklayın</summary>
  <div>

**General**

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Column Name 	| Nesnede eklenen kolonun adının tanımlandığı alandır. 	|
| Column Title 	| Nesne eklenen kolonun web ara yüzünde gösterileceği başlığın tanımlandığı alandır. 	|
| Source 	| Nesnede Data Source alanında bir veri kaynağı seçili olduğunda aktif olur. Veri kaynağındaki kolonun nesnedeki kolon ile eşleştirilmesi için kullanılır. 	|
| Width 	| Kolon genişliğinin ayarlandığı özelliktir, piksel değerinden giriş yapılması gereklidir. 	|
| Visible 	| Kolonun web ara yüzünde görünüp görünmeyeceğinin belirlendiği alandır. 	|
| Edit Type 	| Kolon türünün (boolean, text, date vb.) gösterildiği özelliktir. 	|
| Align 	| Kolonda girilecek verinin hizalanma yönünün seçildiği özelliktir. 	|
| Primary Key 	| Kolon birincil anahtar olarak işaretlenmesi gerekiyorsa bu seçenek aktif edilmelidir.. 	|
| Editable 	| Kolonda değişiklik yapılıp yapılamayacağının belirlendiği özelliktir. 	|

**Control Properties**

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Visible 	| Kolonun görünürlüğünün belirlendiği özelliktir, sunucu tarafında çalışır. 	|
| Client Visible 	| Kolonun görünürlüğünün belirlendiği özelliktir, istemci tarafında çalışır. 	|
| Enabled 	| Kolonun aktif olup olmayacağının belirlendiği özelliktir, sunucu tarafında çalışır. 	|
| Client Enabled 	| Kolonun aktif olup olmayacağının belirlendiği özelliktir, istemci tarafında çalışır. 	|
| Background Color 	| Kolonun arka plan renginin değiştirildiği özelliktir. 	|
| Title 	| Web ara yüzünde kolon üzerine fare işaretçisi ile gelindiğinde, ipucu ifadesinin içeriğinde gösterilecek bilgi belirlenmesi için kullanılır.  	|
| ClassName 	| Kolonda forma ait CSS dosyası içinde yazılmış bir class'ın tanımlanarak nesne görünürlüğünün değiştirilebildiği alandır. 	|
| Value 	| Kolonda değerin ne olacağının belirlendi alandır, aktif edildiğinde web ara yüzünde kolon seçilmiş olarak gözükecektir. 	|
| Placeholder 	| Kolon içine uç kullanıcı tarafından girilmesi istenen veri bilgisini, nesne içerisinde bilgi amaçlı göstermek için kullanılan özelliktir. 	|
| Text Align 	| Kolon içine girilen ifadenin hizalanacağı yerin belirlenmesi için kullanılan alandır. Sola hizala, merkeze hizala, sağa hizala seçimleri yapılabilir. 	|
| Size Type 	| Kolon boyutunun belirlenebileceği alandır. 	|
| ReadOnly 	| Kolonun düzenleme modunda olup olmayacağının ayarlandığı kısımdır. Aktif edildiğinde kolonda veri girişi gerçekleştirilmez, salt okunur durumunda çalışır.  	|
| Tab Index 	| Alana sayısal değerler girilerek, tab butonuna basıldığında form nesneleri arasında hangi sıra ile odaklanılacağı belirlenir. 	|
| Required 	| Kolonda veri girişinin zorunlu olup olmayacağının belirlendiği alandır. 	|
| Format 	| Tarih ve saat gösterim formatının belirlendiği alandır. Varsayılan olarak tarih formatı: “YYYY-MM-DD”, tarih ve saat formatı: “YYYY-MM-DD HH:mm” şeklinde tanımlıdır. Gösterilmek istenen farklı format yapıları bu alanda belirtilebilir. 	|
| Show Time 	| Kolonda saat bilgisinin gösterilip gösterilmeyeceğinin belirlendiği alandır. Bu özellik aktifken, ara yüzde nesneye tıklandığında tarih seçim alanının yanında saat seçim alanı da görünür olur. 	|
| Show Today 	| Kolon içerisinde tarih seçimi yaparken, seçim ekranının altında “Bugün” isimli butonun çıkmasını sağlayan özelliktir. 	|
| Show Today As Default 	| Özellik aktif edildiğinde kolonda varsayılan olarak bugünün tarihi görünür olur. 	|
| Allow Clear 	| Özellik aktif edildiğinde, web ara yüzünde kolonda yapılan tarih seçiminin istenirse kaldırılabilmesi sağlanır. 	|
| Disable before 	| Aktif edildiğinde günümüzden itibaren geçmişte bir nokta öncesindeki tarih seçimlerinin engellenmesi için ayarlar (gün, ay ve yıl değerleri tanımı) devreye girecektir.<br/> **Disable before years:** Girilen değere göre, günümüzden itibaren **x** yıl öncesine kadar tarih seçimi aktif olacaktır. **x yıl + 1 gün** öncesine gidildiğinde seçim yapılamayacaktır.<br/> **Disable before months:** Girilen değere göre, günümüzden itibaren **x** ay öncesine kadar tarih seçimi aktif olacaktır. **x ay + 1 gün** öncesine gidildiğinde seçim yapılamayacaktır.<br/> **Disable before days:** Girilen değere göre, günümüzden itibaren **x** gün öncesine kadar tarih seçimi aktif olacaktır. **x gün + 1 gün** öncesine gidildiğinde seçim yapılamayacaktır.<br/> 	|
| Disable after 	| Aktif edildiğinde günümüzden itibaren gelecekte bir nokta sonrasındaki tarih seçimlerinin engellenmesi için ayarlar (gün, ay ve yıl değerleri tanımı) devreye girecektir.<br/> **Disable after years:** Girilen değere göre, günümüzden itibaren **x** yıl geleceğe kadar tarih seçimi aktif olacaktır. **x yıl + 1 gün** ilerisine gidildiğinde seçim yapılamayacaktır.<br/> **Disable after months:** Girilen değere göre, günümüzden itibaren **x** ay geleceğe kadar tarih seçimi aktif olacaktır. **x ay + 1 gün** ilerisine gidildiğinde seçim yapılamayacaktır.<br/> **Disable after days:** Girilen değere göre, günümüzden itibaren **x** gün geleceğe kadar tarih seçimi aktif olacaktır. **x gün + 1 gün** ilerisine gidildiğinde seçim yapılamayacaktır. 	|
| Field Name 	| Sistemin veri tabanında, alan için oluşturacağı SQL kolon adının belirlendiği alandır. 	|
| Allow Null 	| Kolon için oluşturulacak veri tabanı alanının boş(null) değerlere izin verip vermeyeceği bu kısımdan belirtilir. 	|

  </div>
</details>

<details>
  <summary>Number türünde kolon özellikleri için tıklayın</summary>
  <div>

**General**

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Column Name 	| Nesnede eklenen kolonun adının tanımlandığı alandır. 	|
| Column Title 	| Nesne eklenen kolonun web ara yüzünde gösterileceği başlığın tanımlandığı alandır. 	|
| Source 	| Nesnede Data Source alanında bir veri kaynağı seçili olduğunda aktif olur. Veri kaynağındaki kolonun nesnedeki kolon ile eşleştirilmesi için kullanılır. 	|
| Width 	| Kolon genişliğinin ayarlandığı özelliktir, piksel değerinden giriş yapılması gereklidir. 	|
| Visible 	| Kolonun web ara yüzünde görünüp görünmeyeceğinin belirlendiği alandır. 	|
| Edit Type 	| Kolon türünün (boolean, text, date vb.) gösterildiği özelliktir. 	|
| Align 	| Kolonda girilecek verinin hizalanma yönünün seçildiği özelliktir. 	|
| Primary Key 	| Kolon birincil anahtar olarak işaretlenmesi gerekiyorsa bu seçenek aktif edilmelidir.. 	|
| Editable 	| Kolonda değişiklik yapılıp yapılamayacağının belirlendiği özelliktir. 	|
| Summary Type 	| Alanda seçilen işlem tanımları (Sum, Max, Min, Avg, Count) web arayüzde kolonun altında belirerek, ilgili kolondaki sayısal değerlerin işlem sonuçlarını gösterilir. 	|
| Auto increment 	| Kolon değerinin otomatik artıp artmayacağının belirlenmesi için kullanılır. 	|

**Control Properties**

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Visible 	| Kolonun görünürlüğünün belirlendiği özelliktir, sunucu tarafında çalışır. 	|
| Client Visible 	| Kolonun görünürlüğünün belirlendiği özelliktir, istemci tarafında çalışır. 	|
| Enabled 	| Kolonun aktif olup olmayacağının belirlendiği özelliktir, sunucu tarafında çalışır. 	|
| Client Enabled 	| Kolonun aktif olup olmayacağının belirlendiği özelliktir, istemci tarafında çalışır. 	|
| Background Color 	| Kolonun arka plan renginin değiştirildiği özelliktir. 	|
| Title 	| Web ara yüzünde kolon üzerine fare işaretçisi ile gelindiğinde, ipucu ifadesinin içeriğinde gösterilecek bilgi belirlenmesi için kullanılır.  	|
| ClassName 	| Kolonda forma ait CSS dosyası içinde yazılmış bir class'ın tanımlanarak nesne görünürlüğünün değiştirilebildiği alandır. 	|
| Value 	| Kolonda değerin ne olacağının belirlendi alandır, aktif edildiğinde web ara yüzünde kolon seçilmiş olarak gözükecektir. 	|
| Placeholder 	| Kolon içine uç kullanıcı tarafından girilmesi istenen veri bilgisini, nesne içerisinde bilgi amaçlı göstermek için kullanılan özelliktir. 	|
| Text Align 	| Kolon içine girilen ifadenin hizalanacağı yerin belirlenmesi için kullanılan alandır. Sola hizala, merkeze hizala, sağa hizala seçimleri yapılabilir. 	|
| Size Type 	| Kolon boyutunun belirlenebileceği alandır. 	|
| ReadOnly 	| Kolonun düzenleme modunda olup olmayacağının ayarlandığı kısımdır. Aktif edildiğinde kolonda veri girişi gerçekleştirilmez, salt okunur durumunda çalışır.  	|
| Tab Index 	| Alana sayısal değerler girilerek, tab butonuna basıldığında form nesneleri arasında hangi sıra ile odaklanılacağı belirlenir. 	|
| Required 	| Kolonda veri girişinin zorunlu olup olmayacağının belirlendiği alandır. 	|
| Max 	| Kolona girilebilecek maksimum değerin belirlendiği alandır. 	|
| Min 	| Kolona girilebilecek minimum değerin belirlendiği alandır. 	|
| Step 	| Kolon değerinin kaçar kaçar artıp azalacağının belirlendiği alandır. Artırma ve azaltma işlemleri nesne yanındaki ok butonları ile gerçekleştirilir. 	|
| Precision 	| Virgülden sonra kaç karakter olacağının belirlendiği alandır. Virgülden sonra yazılan değeri aşağı ya da yukarı yuvarlayarak verilen karakter sayısına göre otomatik düzenler. 	|
| Use Thousand Seperator 	| Kolona girilen değere otomatik binlik ayracı eklenmesini sağlayan özelliktir. 	|
| Field Name 	| Sistemin veri tabanında, alan için oluşturacağı SQL kolon adının belirlendiği alandır. 	|
| Allow Null 	| Kolon için oluşturulacak veri tabanı alanının boş(null) değerlere izin verip vermeyeceği bu kısımdan belirtilir. 	|
| Size 	| Kolonun veri tabanı alanında tutacağı boyut bu alanda belirlenir. Size ve Precision alanındaki değerlere göre SQL'de kolon büyüklüğü oluşturulur. 	|
| Precision 	| Kolonun veri tabanı alanında tutacağı boyut bu alanda belirlenir. Size ve Precision alanındaki değerlere göre SQL'de kolon büyüklüğü oluşturulur. 	|

  </div>
</details>

<details>
  <summary>Select türünde kolon özellikleri için tıklayın</summary>
  <div>

**General**

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Column Name 	| Nesnede eklenen kolonun adının tanımlandığı alandır. 	|
| Column Title 	| Nesne eklenen kolonun web ara yüzünde gösterileceği başlığın tanımlandığı alandır. 	|
| Source 	| Nesnede Data Source alanında bir veri kaynağı seçili olduğunda aktif olur. Veri kaynağındaki kolonun nesnedeki kolon ile eşleştirilmesi için kullanılır. 	|
| Width 	| Kolon genişliğinin ayarlandığı özelliktir, piksel değerinden giriş yapılması gereklidir. 	|
| Visible 	| Kolonun web ara yüzünde görünüp görünmeyeceğinin belirlendiği alandır. 	|
| Edit Type 	| Kolon türünün (boolean, text, date vb.) gösterildiği özelliktir. 	|
| Align 	| Kolonda girilecek verinin hizalanma yönünün seçildiği özelliktir. 	|
| Primary Key 	| Kolon birincil anahtar olarak işaretlenmesi gerekiyorsa bu seçenek aktif edilmelidir.. 	|
| Editable 	| Kolonda değişiklik yapılıp yapılamayacağının belirlendiği özelliktir. 	|

**Control Properties**

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Type 	| Kolonda hangi tipte veri ekleneceğinin seçimi bu alandan yapılır. Alanda "Dinamik" ve "Statik" olarak iki seçenek listelenir. Seçim yapılan tipe göre veri kaynağı bölümünde görünen özellikler değişiklik gösterecektir. **Type=Dinamik** seçildiğinde **DataSource, Run At Server, Value Expression, Display Expression ve Display Format** alanları gözükürken, **Type=Statik** seçilirse Items alanı gözükecektir. 	|
| Data Source 	| Type alanında **Dinamik** seçildiğinde görünür duruma geçer. Bir veri kaynağından gelen değerleri listeleyebilmek için kullanılacak alandır. Alanda Çözüm Gezgini alanındaki DataSource bölümüne eklenmiş ve başarıyla derlenen veri kaynağı tanımı, kolonun Datasource) kısmından seçilebilir olur. 	|
| Run At Server 	| Type alanında **Dinamik** seçildiğinde görünür duruma geçer. Kolona bağlanan sorgunun, sunucudan mı istemciden mi çalıştırılacağının belirlendiği seçenektir. 	|
| Value Expression 	| Type alanında **Dinamik** seçildiğinde görünür duruma geçer. Veri Kaynağı kısmından bir veri kaynağı tanımı seçildiğinde bu alan görünür olur. Seçilen veri kaynağından dönen tüm kolonlar bu alanda listelenir. Kullanıcı ara yüzden seçim yaptığında, seçilen ögenin değeri olarak ne ttuyapılan seçimin kayıt alanının hangi kolon değeri olacağı bu alanda belirlenir. 	|
| Display Expression 	| Type alanında **Dinamik** seçildiğinde görünür duruma geçer. Veri Kaynağı kısmından bir veri kaynağı tanımı seçildiğinde bu alan görünür olur. Seçilen veri kaynağından dönen tüm kolonlar bu alanda listelenir. Kullanıcı ara yüzden seçim yaptığında, kolon içerisinde görünecek ifadenin hangi sorgu kolonundan geleceği bu alanda belirlenir. 	|
| Display Format 	| Type alanında **Dinamik** seçildiğinde görünür duruma geçer. Display Expression alanından seçilen kolon ya da kolonlar otomatik olarak bu alana da eklenir. Nesnede listelenecek eleman metinlerine görünüm formatı belirlemek için kullanılan alandır. Elemanların istenen bir formatta gösterilmesi için, ilgili format yapısı bu alanda belirtilebilir. Nesne seçimi sonrası kolonda görüntülenecek değerin web arayüzde uç kullanıcılara belirlenen formatta görünmesi sağlanabilir. Formatlamada kullanılabilecek format tiplerine, alana odaklanıldığında çıkan bilgi mesajındaki linkten (https://shopify.github.io/liquid/) erişilebilir 	|
| Items 	| Type alanında **Statik** seçildiğinde görünür duruma geçer. Veri kaynağından gelen kayıtlar değil, geliştirme anında manuel eklenen elemanlar listelenmek istendiğinde, eleman tanımlama işlemi bu alandan yapılır. Items alanına tıklandığında eleman ekleme penceresi açılır. Ekle butonuna tıklanarak nesneye yeni eleman kalemleri oluşturulur. Girilen elemanın **Value** ve **Title** alanları doldurulur. Elemanın ikona sahip olması istenirse Icons alanı içindeki ikon kütüphanesinden seçim yapılabilir. Ögenin Selected alanı aktif edilirse web ara yüzünde nesne içinde bu öge otomatik olarak seçilmiş gibi gösterilecektir. "Kaydet" butonuna basılarak nesneye eleman ekleme işlemi tamamlanır. Web arayüzde nesneye tıklandığında, Elemanlar alanında belirlenen eleman kayıtları, kullanıcının seçim yapması için listelenir. 	|
| Visible 	| Kolonun görünürlüğünün belirlendiği özelliktir, sunucu tarafında çalışır. 	|
| Client Visible 	| Kolonun görünürlüğünün belirlendiği özelliktir, istemci tarafında çalışır. 	|
| Enabled 	| Kolonun aktif olup olmayacağının belirlendiği özelliktir, sunucu tarafında çalışır. 	|
| Client Enabled 	| Kolonun aktif olup olmayacağının belirlendiği özelliktir, istemci tarafında çalışır. 	|
| Background Color 	| Kolonun arka plan renginin değiştirildiği özelliktir. 	|
| Title 	| Web ara yüzünde kolon üzerine fare işaretçisi ile gelindiğinde, ipucu ifadesinin içeriğinde gösterilecek bilgi belirlenmesi için kullanılır.  	|
| ClassName 	| Kolonda forma ait CSS dosyası içinde yazılmış bir class'ın tanımlanarak nesne görünürlüğünün değiştirilebildiği alandır. 	|
| Icon Expression 	| Type alanında **Dinamik** seçildiğinde görünür duruma geçer. Kolonda veri kaynağına ait kolonlar seçilerek, seçilen kolondaki verilerin belli şartlara göre veri ile beraber ikonda gösterilmesi için kullanılmaktadır. 	|
| Icon Matchers 	| Type alanında **Dinamik** seçildiğinde görünür duruma geçer. Icon Expression alanında seçilen kolondaki veride, hangi veriye göre hangi ikonun gösterilmesi gerektiğinin tanımlandığı alandır. 	|
| Placeholder 	| Kolon içine uç kullanıcı tarafından girilmesi istenen veri bilgisini, nesne içerisinde bilgi amaçlı göstermek için kullanılan özelliktir. 	|
| ReadOnly 	| Kolonun düzenleme modunda olup olmayacağının ayarlandığı kısımdır. Bu özellik aktif edildiğinde veri girişine izin verilmez, salt okunur modda olur. 	|
| Tab Index 	| Alana sayısal değerler girilerek, tab butonuna basıldığında hangi sıra ile odaklanılacağı belirlenir. İmleci, veri girilmek istenen nesneye tıklamak yerine, tab butonuna basarak belirli bir sırayla indekslenmiş nesnelere direk odaklanılması sağlanmış olur. 	|
| Required 	| Kolonda veri girişinin zorunlu olup olmayacağının belirlendiği alandır. Bu özellik aktif edildiğinde nesne içerisine veri girişi yapılmadan formun ilerletilmesi/kaydedilmesi gerçekleştirilemez. 	|
| Value Type 	| Kolon elemanlarının tipinin belirlendiği alandır. Burada belirlenen tipe göre, Elemanlar alanında eklenen satırın Değer alanı tipi değiştirilir. Aynı zamanda nesneye parametrik bir sorgu bağlandığında, parametre tipi ile Değer Tipi alanından seçilen tip değeri aynı olmalıdır. Datasource alanında **Type : Statik** seçili ve statik eleman eklendiğinde Value Type alanı seçim yapılamaz durumuna geçer. 	|
| Allow Clear 	| Kolonda seçilen değeri temizlemek için kullanılan özelliktir. Aktif edildiğinde web arayüzünde kullanıcı bir seçim yaptığında, × (Çarpı) işareti belirir. İşarete basılarak seçilen değer silinip, başka bir nesne elemanının seçimi sağlanabilir. 	|
| Show Search 	| Özellik aktif edildiğinde kolon içerisindeki elemanları, veri girerek otomatik filtreleme ile bulmayı sağlayan özelliktir. 	|
| Size Type 	| Nesne seçim alanı boyutunun ayarlandığı kısımdır. 	|
| Field Name 	| Sistemin veri tabanında, alan için oluşturacağı SQL kolon adının belirlendiği alandır. 	|
| Allow Null 	| Kolon için oluşturulacak veri tabanı alanının boş(null) değerlere izin verip vermeyeceği bu kısımdan belirtilir. 	|

  </div>
</details>

<details>
  <summary>Text türünde kolon özellikleri için tıklayın</summary>
  <div>

**General**

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Column Name 	| Nesnede eklenen kolonun adının tanımlandığı alandır. 	|
| Column Title 	| Nesne eklenen kolonun web ara yüzünde gösterileceği başlığın tanımlandığı alandır. 	|
| Source 	| Nesnede Data Source alanında bir veri kaynağı seçili olduğunda aktif olur. Veri kaynağındaki kolonun nesnedeki kolon ile eşleştirilmesi için kullanılır. 	|
| Width 	| Kolon genişliğinin ayarlandığı özelliktir, piksel değerinden giriş yapılması gereklidir. 	|
| Visible 	| Kolonun web ara yüzünde görünüp görünmeyeceğinin belirlendiği alandır. 	|
| Edit Type 	| Kolon türünün (boolean, text, date vb.) gösterildiği özelliktir. 	|
| Align 	| Kolonda girilecek verinin hizalanma yönünün seçildiği özelliktir. 	|
| Primary Key 	| Kolon birincil anahtar olarak işaretlenmesi gerekiyorsa bu seçenek aktif edilmelidir.. 	|
| Editable 	| Kolonda değişiklik yapılıp yapılamayacağının belirlendiği özelliktir. 	|

**Control Properties**

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Visible 	| Kolonun görünürlüğünün belirlendiği özelliktir, sunucu tarafında çalışır. 	|
| Client Visible 	| Kolonun görünürlüğünün belirlendiği özelliktir, istemci tarafında çalışır. 	|
| Enabled 	| Kolonun aktif olup olmayacağının belirlendiği özelliktir, sunucu tarafında çalışır. 	|
| Client Enabled 	| Kolonun aktif olup olmayacağının belirlendiği özelliktir, istemci tarafında çalışır. 	|
| Background Color 	| Kolonun arka plan renginin değiştirildiği özelliktir. 	|
| Title 	| Web ara yüzünde kolon üzerine fare işaretçisi ile gelindiğinde, ipucu ifadesinin içeriğinde gösterilecek bilgi belirlenmesi için kullanılır.  	|
| ClassName 	| Kolonda forma ait CSS dosyası içinde yazılmış bir class'ın tanımlanarak nesne görünürlüğünün değiştirilebildiği alandır. 	|
| Placeholder 	| Kolon içine uç kullanıcı tarafından girilmesi istenen veri bilgisini, nesne içerisinde bilgi amaçlı göstermek için kullanılan özelliktir. 	|
| Text Align 	| Alan içine girilen ifadenin hizalanacağı yerin belirlenmesi için kullanılan alandır. Sola hizala, merkeze hizala, sağa hizala seçimleri yapılabilir. 	|
| Enable Multilanguage 	| Çoklu dilde veri girişinin yapılabilmesini sağlandığı alandır. Aktif edilmesi ile çoklu dil butonu gösterilerek kullanıcının birden fazla dil için veri girişi yapabilmesi sağlanır. 	|
| Text 	| Kolonun içerik değeridir. Form web arayüzde açıldığında bu alanda yazılan metin, alan içinde varsayılan metin olarak görünür. Enable Multilanguage Text özelliği ile birlikte çalışır, özellik aktif ise Text özelliğinde çoklu dil ifadesi yazılması için buton gözükecektir. 	|
| Show Character Count 	| Alanda yazılmış ifadenin kaç karakter uzunluğunda olduğu gösterilmek istenirse aktif edilir. Aktif edildiğinde girilen ifade/nesnede girilebilecek maksimum limitin ne olduğunu gösteren bir sayaç görünür durumda olur. 	|
| Size Type 	| Alan boyutunun belirlenebileceği alandır. 	|
| ReadOnly 	| Kolonun düzenleme modunda olup olmayacağının ayarlandığı kısımdır. Bu özellik aktif edildiğinde veri girişine izin verilmez, salt okunur modda olur. 	|
| Tab Index 	| Alana sayısal değerler girilerek, tab butonuna basıldığında hangi sıra ile odaklanılacağı belirlenir. İmleci, veri girilmek istenen nesneye tıklamak yerine, tab butonuna basarak belirli bir sırayla indekslenmiş nesnelere direk odaklanılması sağlanmış olur. 	|
| Required 	| Kolonda veri girişinin zorunlu olup olmayacağının belirlendiği alandır. Bu özellik aktif edildiğinde nesne içerisine veri girişi yapılmadan formun ilerletilmesi/kaydedilmesi gerçekleştirilemez. 	|
| Max Lenght 	| Nesneye girilecek karakter sayısının maksimum değeri bu alanda belirlenir. Bu alanda verilen sayısal değer ile, nesneye girilen karakter sayısı sınırlandırılabilir. 	|
| Field Name 	| Sistemin veri tabanında, alan için oluşturacağı SQL kolon adının belirlendiği alandır. 	|
| Allow Null 	| Kolon için oluşturulacak veri tabanı alanının boş(null) değerlere izin verip vermeyeceği bu kısımdan belirtilir. 	|
| Size 	| Kolonun veri tabanı üzerinde tutacağı boyut bu alanda belirlenir. 	|

  </div>
</details>

<details>
  <summary>Time türünde kolon özellikleri için tıklayın</summary>
  <div>

**General**

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Column Name 	| Nesnede eklenen kolonun adının tanımlandığı alandır. 	|
| Column Title 	| Nesne eklenen kolonun web ara yüzünde gösterileceği başlığın tanımlandığı alandır. 	|
| Source 	| Nesnede Data Source alanında bir veri kaynağı seçili olduğunda aktif olur. Veri kaynağındaki kolonun nesnedeki kolon ile eşleştirilmesi için kullanılır. 	|
| Width 	| Kolon genişliğinin ayarlandığı özelliktir, piksel değerinden giriş yapılması gereklidir. 	|
| Visible 	| Kolonun web ara yüzünde görünüp görünmeyeceğinin belirlendiği alandır. 	|
| Edit Type 	| Kolon türünün (boolean, text, date vb.) gösterildiği özelliktir. 	|
| Align 	| Kolonda girilecek verinin hizalanma yönünün seçildiği özelliktir. 	|
| Primary Key 	| Kolon birincil anahtar olarak işaretlenmesi gerekiyorsa bu seçenek aktif edilmelidir.. 	|
| Editable 	| Kolonda değişiklik yapılıp yapılamayacağının belirlendiği özelliktir. 	|

**Control Properties**



  </div>
</details>

`Show today button` - Alan aktif edilerek nesne üzerinde **Bugün** butonu gösterilir. Nesnede tarih aralığında gezinirken günümüze dönülmek istenirse aktif edilmelidir.

`Show date navigator` - Nesnede tarihler arasında gezinme yapılabilmesi istenirse alan aktif edilir. Alan aktif edilerek nesnedeki tarih aralıkları arasında gezinmeyi sağlayan sağ ok-sol ok-tarih aralığına tıklanınca açılan takvimler gösterilir. Kapalı durumda iken Supported view'da seçilen ögeye göre sadece bulunulan gün/hafta veya ay içeriği gösterilir.

`Show all day panel` - Alan aktif edildiğinde bütün günü kapsayan etkinlik bulunabildiğinde (en az 24 saat olmalıdır) aktif edilmesi gereken özelliktir. Aktif edilerek nesnede Tüm Gün satırı gösterilir ve tüm günü kaplayan etkinlik varsa burada gösterilir.

`Show tooltip` - Özellik aktif ise nesne üzerinde ekli ögelerde bir kere tıklandığında pop-up açılarak içinde ögeye ait tanımlı bilgiler gösterilmektedir. Pop-up içinde başlık, tarihi, bulunduğu saat aralığı ve yetkisi bulunuyorsa düzenleme/silme ikonları gösterilecektir.

`Show view switcher` - Nesnede takvimin gösterim şeklinin değiştirilebileceği alandır. Aktif edildiğinde nesnede **Supported views** alanında ekli ögelerin seçilebileceği aşağıya açılır liste görünür olur. Listede yapılan seçime göre (Day: Takvim günlük görünümde, Week: Takvim haftalık görünümde, Month: Takvim aylık görünümde) nesne takvimi görünümü değişecektir.

`Supported views` - Takvim görünümünde hangi tiplerin kullanabileceğini belirlemek için ögelerin seçildiği alandır. Bir veya birden fazla seçim yapılabilmektedir. Birden fazla seçim yapıldığında, yapılan seçimlere göre kullanıcının web ara yüzünde değiştirilebilmesine izin verilmesi istenirse **Show view switcher** özelliği aktif edilmelidir. 

>Yapılabilecek Seçimler : Day, Week, Month

`Default view` - Takvim web ara yüzünde açılırken hangi görünümle (Day/Week/Month) açılacağının belirlendiği alandır. Supported views alanında seçim yapıldığında, alanda seçilebilecek ögeler listelenmektedir.

`Start hour` - Takvim gösteriminde başlangıç saatinin belirlendiği alandır. Yapılan seçime göre nesne içinde saat dilimleri gösterilmektedir.

`End hour` - Takvim gösteriminde bitiş saati çizgisinin belirlendiği alandır. Yapılan seçime göre nesne içinde saat dilimleri gösterilmektedir.

### Behavior

`ReadOnly` - Nesnenin düzenleme modunda olup olmayacağının ayarlandığı kısımdır. Bu özellik aktif edildiğinde nesne veri girişine izin vermez, salt okunur modda olur. Nesneye veri girişine izin verilmesi için özelliğin pasif olması gerekir.

### Data Definition Language

`Field Name` - Sistemin veri tabanında, nesne için oluşturacağı kolonun adının belirlendiği alandır. “Name” kısmında nesneye başka bir isim verilip, veritabanı tablosunda nesne için oluşturulacak kolon adı farklı bir isim olarak yaratılabilir.

## Olaylar

Nesnenin sahip olduğu olaylar, Özellik Görüntüleyici panelindeki “Olaylar” sekmesinde yer almaktadır. Her bir olay, farklı çalışma anlarında tetiklenerek kendilerine özgü işlemleri gerçekleştirir. Bu olaylara geliştirici tarafından yazılan kodlar da ilgili olayın tetiklendiği anda çalıştırılır.

“Client” alanında bulunan olaylara çift tıklandığında ekran, TypeScript kodlamanın yapılabileceği “Formadı.ts” isimli form kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur.

“Server” alanında bulunan olaylara çift tıklandığında ekran, C# kodlamanın yapılabileceği “Formadı.cs” isimli form kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur.

Geliştirici bu methodlar içerisinde istediği kod bloğunu kurgulayabilir. Olaylar sekmesinden tıklanarak kod tarafında methodu oluşturulmuş olayın yanında, method adı bilgisi otomatik oluşturularak, olayla method arasındaki ilişki belirtilmiş olur.