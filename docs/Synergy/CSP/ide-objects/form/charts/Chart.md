---
sidebar_position: 1
custom_edit_url: ""
---

# Chart

Chart nesnesi form üzerinde, uç kullanıcılara veri kaynağından getirilen sonuçların görsellik ile zenginleştirilerek ifade edilmesi için kullanılır. Bu nesne ile kullanıcının, bir çok bilgiyi doğrudan görüntülemesi yerine, aynı anda özetle görüntülemesi sağlanır.

Geliştirme arayüzünde aktif ekran form iken, Araç Kutusu panelinde form nesneleri listelenir. Nesne, araç kutusu panelinden sürükle/bırak yöntemi ile forma eklenir.

![Chart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload199ddbfe-edc9-47d1-93cb-e27c5bbd74bd)

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

### Appearance

`Visible` - Nesnenin gizlenip, görünür yapılma ayarlarının gerçekleştirildiği kısımdır. Bu alan aktifken, nesne form üzerinde görünür durumdadır. Alan pasif yapıldığında nesne görünmez olur.

`Client Visible` - Form ilk açıldığında nesne görünmesin, belirli bir şart sağlandığında nesne görünür olsun gibi bir işlem yapılmak istendiğinde, nesnenin istemci tarafında görünmez olması için bu alan pasif yapılır. Kodla ya da Kural Yöneticisi ile belirlenen şart sağlandığında nesne tekrar görünür hale getirilebilir. Sunucu görünürlüğü aktif değilken, istemci müdahale edemez ancak istemci görünürlüğü aktif değilken sunucu müdahale edebilir.

`Enabled` - Nesnenin etkin modu bu alandan ayarlanır. Bu özellik aktifken nesneye veri girişi sağlanabilir ve nesne düzenlenebilir. Özellik pasifken, nesne düzenlenemez moddadır ve pasif görünür.

`Client Enabled` - Form ilk açıldığında nesne etkin olmasın, belirli bir şart sağlandığında etkin olsun gibi bir işlem yapılmak istendiğinde, nesnenin istemci tarafında etkin olmaması için bu alan pasif yapılır. Kodla ya da Kural Yöneticisi ile belirlenen şart sağlandığında nesne tekrar etkin hale getirilebilir. Sunucu etkinliği aktif değilken, istemci müdahale edemez ancak istemci etkinliği aktif değilken sunucu müdahale edebilir.

`Background Color` - Nesneye arka plan rengi vermek için kullanılan alandır.

`Title` - Form arayüzde açıkken imleç ile nesne üzerine gelindiğinde, bu alanda yazılan metin, ipucu olarak gösterilir. Nesne ile ilgili detay bilgi verilmek istendiğinde kullanılan, uç kullanıcıyı yönlendirme amaçlı bir özelliktir.

`ClassName` - Forma ait CSS dosyası içinde yazılmış bir class'ın tanımlanarak nesne görünürlüğünün değiştirilebildiği alandır.

### Datasource

`DataSource` - Nesnede, bir veri kaynağından gelen değerleri listeleyebilmek için kullanılacak alandır. Projede Çözüm Gezgini alanındaki DataSource bölümüne eklenmiş ve başarıyla derlenen veri kaynağı tanımı, nesnenin Datasource) kısmından seçilebilir olur.

:::danger UYARI

Chart nesnesinde kullanılacak sorgularda Insert ve Update sorguları kullanılmaz.

:::

![Chart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload13ba228e-0c5e-44cf-bf24-5d81eb72a4b4)

![Chart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload48abccb8-c6a7-42e5-8d11-3cacced1e6c8)

`RunAtServer` - Bu seçenek nesneye bağlanan sorgunun, sunucudan mı istemciden mi çalıştırılacağının belirlendiği seçenektir.

Bu seçenek aktif edilirse web arayüzünde forma tıklandığında, form açılmadan önce sorgu, sunucu tarafında çalıştırılır, form açıldığında nesneye sorgu sonucu yüklenmiş olarak gelir. Seçenek pasif yapıldığında web arayüzünde forma tıklandığında, form açıldıktan sonra nesneye sorgunun sonuç değerleri yüklenmeye başlar.

Sorgu sonucunun yüklenmesi için geçen bekleme süresi, bu özellik aktifken formun açılma anında, özellik pasifken form hızlı açıldıktan sonra nesneye verinin yüklenmesi anında etkili olur.

### Charts and Activation

`Chart items` - Nesnede gösterilmek istenen grafik tipinin seçildiği alandır. Chart Items kısmına tıklandığında, nesnede gösterilecek chart tipinin seçileceği ve seçilen chart özelliklerinin düzenleneceği bir pencere açılır. 

![Chart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8a180ade-f843-4ea5-b5b0-4419fba5fb63)

Açılan penceredeki “Ekle” butonuna tıklandığında, Chart nesnesinde gösterilmek istenen chart tipleri listelenir. Nesneye aşağıdaki tiplerde chartlar eklenebilir;

> Area Chart (Alan Grafiği)
> Bar Chart (Sütun Grafiği)
> Line Chart (Çizelge Grafiği)
> Pie Chart (Dairesel Grafik)
> Scatter Chart (Serpilme Grafiği)
> Spline Chart (Eğri Grafiği)

:::info BİLGİ

Pie chart ögesi diğer ögelerle birlikte kullanılamaz.

:::

![Chart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload568ea565-f884-48ad-9872-1715a6ab8dbc)

Ekle butonuna tıklanıp bir grafik seçimi yapıldığında pencerenin sol tarafındaki Grafikler sekmesine seçilen grafik eklenir. Sağ tarafta ise grafik bilgilerinin girildiği alan bulunmaktadır.

![Chart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5da6ecba-7de8-4270-b338-ec7b72840ec2)

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Name 	| Grafiğe verilecek isim bu alana yazılır. 	|
| Argument Field 	| İlgili alanlar içinde seçilebilecek olan değerler, grafiğin datasource seçeneğinde eklenmiş olan sorgudaki alanlardan gelmektedir. Argument Field alanına grafikte kullanılması istenen açıklama alanı kolonu seçilir. 	|
| Value Field 	| İlgili alanlar içinde seçilebilecek olan değerler, grafiğin datasource seçeneğinde eklenmiş olan sorgudaki alanlardan gelmektedir. Value Field alanına grafikte kullanılması istenen değer kolonu seçilir. 	|
| Color 	| Grafik renginin seçimi yapılmaktadır. Renk seçimi paneli rgb kodunun solunda bulunan renge tıklanıldığında gösterilmektedir. Palet üzerinde fare işaretçisiyle veya kullanılmak istenen RGB kodu ya da HEX kodu girilerek renk seçimi yapılabilir. RGB kodunun sağında bulunan A ifadesi Alfa Kanalı’nı belirtmekte olup opaklığı ayarlamak için kulanılmaktadır ve değer aralığı 0 ile 100 arasındadır. Bu seçenekler haricinde varsayılan olarak gelen 15 renkten birisi de seçilebilmektedir. ![Chart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload28ea121d-3c74-4726-99eb-0421800c1ab2)	|

Verilerin girişi yapıldıktan sonra penceredeki “Kaydet” butona basılarak chart kaydedilmelidir.

`Rotate enabled` - Nesnede verilerin gösterildiği X ve Y eksenlerinin yerlerini değiştirmektedir. Varsayılan durum pasif olarak gelmektedir. Pasif durumda iken argüman alanı X ekseninde, değer alanı Y ekseninde gösterilmektedir. Aktif hale getirildiğinde bu eksenler yer değiştirip argüman alanı Y eksenine, değer alanı X ekseninde gösterilmektedir.

> *Rotate Enabled seçeneği pasif iken grafiğin gösterimi*
![Chart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada4d01068-cb41-4e8c-ac8b-33b66452114a)
> *Rotate Enabled seçeneği aktif iken grafiğin gösterimi*
![Chart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload97f5eef9-1f60-447c-b333-0b8d779a0a62)

`Animation enabled` - Aktif iken form açıldığında chart nesnesindeki verilerin animasyon şeklinde yüklenmesini sağlar. Kapalı olduğunda veriler yüklü şekilde gelir, açık olduğunda gif gibi hareket halinde yüklenir ve yüklü duruma geçer.

> *Soldaki chartta Animation Enabled aktif iken sağdaki chartta aynı özellik pasif durumdadır*
![Chart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload94acfd22-b512-4fd7-8453-665e9d9d7628)

`Selection enabled` - Chart üzerinde her hangi bir verinin seçilmesini sağlar.Bu seçenek açıkken fare imleci veri üzerine gelince el şeklinde olur seçim yapıldığında ilgili alan seçili duruma geçer.

`Hover enabled` - Fare imleci ile veri üzerine gelindiğinde o bölgenin stil değişikliğini sağlar; gölgeli hale gelir.

`Tooltip enabled` - Verinin üzerine geldiğinde değerin gösterilmesini sağlar.Örneğin departmana göre kullanıcı sayısı grafiğinde, fare imleci argüman eksenindeki Yazılım departmanı üzerine getirildiğinde kullanıcı sayısını gösterebilir.

### Legend

`Enabled` - Chart içinde gösterilen grafiklerde hangi grafiğin neyi gösterdiğini belirtmek için kullanılmaktadır. Enabled seçeneği aktif hale getirildiğinde chartın yanında bir tooltip içinde bunlar belirtilmektedir.

> *Legend özelliği aktif değilken chart görünümü*
![Chart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbcb39a5a-8018-4a84-b886-de2dc1ca9005)
> *Legend özelliği aktifken chart görünümü*
![Chart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1f2bdf94-cd2e-472d-a5be-3571a8492364)

`Position` - Enabled özelliği aktifken bilgilerin grafiğin neresinde görüneceğinin seçilmesi için açılan özelliktir. Listelenen seçenekler Left (solda), Right (sağda) ve Bottom (altta) ve Top (üstte)’dır.

>Yapılabilecek Seçimler : Left, Right, Bottom, Top

### Stack

`Enabled` - Chart nesnesi içinde birden fazla Chart items ögesi eklendiyse bunları gösterimini sağlamak için kullanılır.

`Series` - Enabled özelliği aktifken görünen özelliktir. Charts and Activation içindeki Chart Items’da oluşturulan grafiklerin seçildiği özelliktir. Listedeki grafiklerden seçim yapılarak chart üzerinde birden fazla grafik gösterilir.

### Zoom and Pan

`Enabled` - Chart içinde değerlere yakınlaştırma ve uzaklaştırma işlemlerini yapabilmek için kullanılmaktadır. Aktif olduğu durumda buna bağlı üç özellik daha aktif hale gelmektedir.

`Interaction with arguments` - Zoom And Pan içindeki Enabled özelliği aktifken görünen özelliktir. Argüman alanındaki verilere göre her ikisi (both), hiçbiri (none), uzaklaşma (pan) ve yakınlaştırma (zoom) işlemleri yapılabilir. Both seçiliyse argüman ekseninde hem yakınlaştırma (Zoom) hem de kaydırma (Pan) özelliği aktif hale gelir. None seçeneğinde bu eksenle ilgili bir işlem yapılması engellenir. Pan seçili ise argüman ekseni boyunca grafik sağa ya da sola doğru kaydırılabilir. Zoom seçili ise grafik yaklaştırıldığında değer ekseni sabit kalacak şekilde argüman ekseni boyunca yakınlaştırılır.

>Yapılabilecek Seçimler : Both, None, Pan, Zoom

`Interaction with values` - Zoom And Pan içindeki Enabled özelliği aktifken görünen özelliktir. Değer alanındaki verilere göre her ikisi (both), hiçbiri (none), uzaklaşma (pan) ve yakınlaştırma (zoom) işlemleri yapılabilir. Both seçiliyse değer ekseninde hem yakınlaştırma (Zoom) hem de kaydırma (Pan) özelliği aktif hale gelir. None seçeneğinde bu eksenle ilgili bir işlem yapılması engellenir. Pan seçili ise değer ekseni boyunca grafik sağa ya da sola doğru kaydırılabilir. Zoom seçili ise grafik yaklaştırıldığında argüman ekseni sabit kalacak şekilde değer ekseni boyunca yakınlaştırılır.

>Yapılabilecek Seçimler : Both, None, Pan, Zoom

`Zoom region key` - Zoom And Pan içindeki Enabled özelliği aktifken görünen özelliktir. Listelenen ögelerde seçilecek tuş, klavye üzerindeki tuşa basılı tutulup grafik üzerindeki bir alan fare ile seçilerek yakınlaştırma yapılabilir. Shift, Alt veya Ctrl seçenekleri seçilebilir.

>Yapılabilecek Seçimler : Shift, Alt, Ctrl

### Argument Axis

`Enabled` - Aktif iken argüman eksenindeki başlıklar grafik içinde gösterilmektedir. Kapatıldığı durumda bu eksendeki başlıklar getirilmeyecektir.

> *Argument Axis özelliği aktif değilken argüman eksenindeki değerler gizlenir*
![Chart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload497f7f17-276a-4edd-9ced-4922e13d0ef6)
> *Argument Axis özelliği aktifken argüman eksenindeki başlıklar görünür hale gelir*
![Chart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade219104c-71f9-4dc0-aa98-74792432e604)

`Show tick` - Argument Axis içindeki Enabled özelliği aktifken görünen özelliktir. Argüman eksenindeki başlıklardan chart dışına doğru bir işaretçi çizgi çıkarmakta değer girilen Tick Size alanını aktif hale getirmek için kullanılır. Çizgi uzunluğu Tick size ile ayarlanmaktadır.

`Tick size` - Show tick özelliği aktifken görünen özelliktir. Argüman eksenindeki başlıklardan chart dışına doğru bir işaretçi çizgi çıkarmak için kullanılır.

> *Tick Size 0 iken argüman ekseninden çıkan bir çizgi gözükmez*
![Chart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada3a29a1a-1da0-467f-b5b3-140b2df67b55)
> *Tick Size için örnek bir değer 50 girildiğinde argüman ekseninden işaretçi çizgiler çıkmıştır*
![Chart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6e23ff2b-c954-4ed5-a89a-6ebd459ceca8)

`Indent from axis` - Argument Axis Enabled özelliği aktifken görünen özelliktir.  Grafiğin alt kısmı ile argüman başlıkları arasındaki boşlukları belirlemek için kullanılır.

> *Indent from axis için örnek olarak 50 değeri girilmiş olup, bu değere göre başlıklar ve grafiğin alt kısmı arasındaki boşluk ayarlanabilmektedir*
![Chart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc5b3af2b-be64-4203-b2bc-b7fb8072cd73)

`Position` - Argument Axis Enabled özelliği aktifken görünen özelliktir. Listelenen özellikler Top ve Bottom’dır. Arguman ekseninin Bottom (altta) veya Top (üstte) görünmesini sağlar.

>Yapılabilecek Seçimler : Top, Bottom

> *Bottom seçildiğindeki görünümü*
![Chart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload492ad47b-d9d2-4bd5-accc-052a6a5b4fd2)
> *Top seçildiğindeki görünüm*
![Chart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7bc83a29-7f82-43f5-a809-1167d4cb0c48)

`Show grid` - Argument Axis Enabled özelliği aktifken görünen özelliktir. Seçili iken argüman başlıklarından chart içine doğru gösterilen kılavuz çizgiler görünür hale gelir.

> *Show Grid seçili iken görünüm*
![Chart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb560a963-ed5c-400b-8359-a9c31d440dfb)
> *Show Grid seçili değilken görünüm*
![Chart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1a064e9f-34fb-4a38-8616-8ab1d855eb1a)

`Show line` - Argument Axis Enabled özelliği aktifken görünen özelliktir. Seçili olduğu durumda orijin noktasından argüman ekseni boyunca devam eden bir çizgi gösterilir. Seçili değilse bu çizgi görünmez.

> *Show line seçili iken orijin noktasından çıkan çizgi görünür durumdadır*
![Chart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload915cef98-9cec-45ad-9365-e2a26a7ace26)
> *Show line seçili olmadığında orijin noktasından çıkan çizgi kaldırılır*
![Chart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload48318873-41ac-4ce7-bc4a-4bdd7ca046af)

`Show labels` - Argument Axis Enabled özelliği aktifken görünen özelliktir.  Seçili ise argüman eksenindeki başlıklar görünür halde gelir.

> *Show Label seçili iken argüman eksenindeki başlıklar görünür haldedir*
![Chart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf38d41a7-f6c1-4255-a6d6-f77c98fd1999)
> *Show Label seçili değilse bu başlıklar görünmeyecektir*
![Chart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaf3960ff-2be9-492a-937c-9f2858a9e13a)

### Value Axis

`Enabled` - Aktif iken değer eksenindeki başlıklar grafik içinde gösterilmektedir. Kapatıldığı durumda bu eksendeki başlıklar getirilmeyecektir.

> *Enabled seçili iken value eksenindeki değerler görünür olarak getirilir*
![Chart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload63bfc87c-47f3-45ef-ab14-9222edcc1ab5)
> *Enabled seçeneği kapatıldığında value eksenindeki değer gösterilmeyecektir*
![Chart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5ba37f5b-e0fd-427e-b4b9-1eae74d5da1a)

`Show tick` - Value Axis içindeki Enabled özelliği aktifken görünen özelliktir. Value eksenindeki başlıklardan chart dışına doğru bir işaretçi çizgi çıkarmakta değer girilen Tick Size alanını aktif hale getirmek için kullanılır. Çizgi uzunluğu Tick size ile ayarlanmaktadır.

`Tick size` - Show tick özelliği aktifken görünen özelliktir. Değer eksenindeki başlıklardan chart dışına doğru bir işaretçi çizgi çıkarmak için kullanılır.

> *Tick Size 0 iken değer ekseninden çıkan bir çizgi gözükmez*
![Chart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload212e7628-bc5d-47c7-8321-13fb8bfd8b66)
> *Tick Size için örnek bir değer 50 girildiğinde değer ekseninden işaretçi çizgiler çıkmıştır*
![Chart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload92b269f7-3532-4eba-859d-56649afee800)

`Indent from axis` - Value Axis Enabled özelliği aktifken görünen özelliktir.  Grafiğin sol kısmı ile değer başlıkları arasındaki boşlukları belirlemek için kullanılır.

> *Indent from axis için örnek olarak 50 değeri girilmiş olup, bu değere göre başlıklar ve grafiğin sol kısmı arasındaki boşluk ayarlanabilmektedir*
![Chart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3a33c238-4905-4570-99ff-0cefc6b9e418)

`Position` - Value Axis Enabled özelliği aktifken görünen özelliktir. Listelenen özellikler Left ve Right’dır. Değer ekseninin Left (solda) veya Right (sağda) görünmesini sağlar.

>Yapılabilecek Seçimler : Left, Right

> *Left seçildiğindeki görünüm*
![Chart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5b905967-e2e4-4ab2-b360-a7e7dd9ef3a1)
> *Right seçildiğindeki görünüm*
![Chart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddd17090e-b82e-4466-9f2c-e729fea2cc37)

`Show grid` - Value Axis Enabled özelliği aktifken görünen özelliktir. Seçili iken value başlıklarından chart içine doğru gösterilen kılavuz çizgiler görünür hale gelir.

> *Show Grid seçili iken görünüm*
![Chart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload50beeb67-178c-4e39-8167-1b680e7cfb2a)
> *Show Grid seçili değilken görünüm*
![Chart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload34f07e7e-0e2d-4f26-a358-2dd77c699f70)

`Show line` - Value Axis Enabled özelliği aktifken görünen özelliktir. Seçili olduğu durumda orijin noktasından değer ekseni boyunca devam eden bir çizgi gösterilir. Seçili değilse bu çizgi görünmez.

> *Show line seçili iken orijin noktasından çıkan çizgi görünür durumdadır.*
![Chart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd9b3cfe0-a060-41ad-9a5a-50d0ffde19ca)
> *Show line seçili olmadığında orijin noktasından çıkan çizgi kaldırılır.*
![Chart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadca560695-683f-41ae-b3a4-c8f3a49d9012)

`Show labels` - Value Axis Enabled özelliği aktifken görünen özelliktir. Seçili olduğu durumda orijin noktasından değer ekseni boyunca devam eden bir çizgi gösterilir. Seçili değilse bu çizgi görünmez.

> *Show Label seçili iken argüman eksenindeki başlıklar görünür haldedir*
![Chart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada29a0e5c-9e01-4981-b07f-0a4080c1bc0c)
> *Show Label seçili değilse bu başlıklar görünmeyecektir*
![Chart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddab8fc3d-fcf8-4a45-8047-504729a618cb)

## Olaylar

Nesnenin sahip olduğu olaylar, Özellik Görüntüleyici panelindeki "Olaylar" sekmesinde yer almaktadır. Her bir olay, farklı çalışma anlarında tetiklenerek kendilerine özgü işlemleri gerçekleştirir. Bu olaylara geliştirici tarafından yazılan kodlar da ilgili olayın tetiklendiği anda çalıştırılır.

"Client" alanında bulunan olaylara çift tıklandığında ekran, TypeScript kodlamanın yapılabileceği "Formadı.ts" isimli form kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur.

"Server" alanında bulunan olaylara çift tıklandığında ekran, C# kodlamanın yapılabileceği "Formadı.cs" isimli form kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur.

Geliştirici bu methodlar içerisinde istediği kod bloğunu kurgulayabilir. Olaylar sekmesinden tıklanarak kod tarafında methodu oluşturulmuş olayın yanında, method adı bilgisi otomatik oluşturularak, olayla method arasındaki ilişki belirtilmiş olur.

![Chart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadac4c8b90-6f51-42e1-9516-6019b54af9ab)