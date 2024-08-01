---
sidebar_position: 6
custom_edit_url: ""
---

# AreaChart

AreaChart nesnesi form üzerinde, uç kullanıcılara veri kaynağından getirilen sonuçlar alansal gösterimler ile zenginleştirerek ifade etmek için kullanılır. Bu nesne ile kullanıcının, bir çok bilgiyi doğrudan görüntülemesi yerine, aynı anda özetle görüntülemesi sağlanır.

Geliştirme arayüzünde aktif ekran form iken, Araç Kutusu panelinde form nesneleri listelenir. Nesne, araç kutusu panelinden sürükle/bırak yöntemi ile forma eklenir.

![AreaChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload962de785-a083-4b5b-b3e8-f200f1f83dc0)

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

AreaChart nesnesinde kullanılacak sorgularda Insert ve Update sorguları kullanılmaz.

:::

![AreaChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0766af43-b6b7-4e50-ad8c-ab94ce892aeb)

![AreaChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload61eee89c-4d3a-4f88-93c7-34f9ddc9712e)

`RunAtServer` - Bu seçenek nesneye bağlanan sorgunun, sunucudan mı istemciden mi çalıştırılacağının belirlendiği seçenektir.

Bu seçenek aktif edilirse web arayüzünde forma tıklandığında, form açılmadan önce sorgu, sunucu tarafında çalıştırılır, form açıldığında nesneye sorgu sonucu yüklenmiş olarak gelir. Seçenek pasif yapıldığında web arayüzünde forma tıklandığında, form açıldıktan sonra nesneye sorgunun sonuç değerleri yüklenmeye başlar.

Sorgu sonucunun yüklenmesi için geçen bekleme süresi, bu özellik aktifken formun açılma anında, özellik pasifken form hızlı açıldıktan sonra nesneye verinin yüklenmesi anında etkili olur.

### Charts and Activation

`Chart items` - Nesnede gösterilmek istenen grafik tipinin seçildiği alandır. Chart Items kısmına tıklandığında, nesnede gösterilecek chart tipinin seçileceği ve seçilen chart özelliklerinin düzenleneceği bir pencere açılır. 

![AreaChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5a48405f-1b0f-42cf-89e4-34928b2c845d)

Açılan penceredeki “Ekle” butonuna tıklandığında, Chart nesnesinde gösterilmek istenen chart tipleri listelenir. Nesneye aşağıdaki tiplerde chartlar eklenebilir;

> Area Chart (Alan Grafiği)

![AreaChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7bca9368-2025-4ac1-8423-67b5ef73f6c4)

Ekle butonuna tıklanıp bir çizgi grafik eklendiğinde, pencerenin sol tarafındaki Grafikler sekmesine grafik tanımı eklenir. Sağ tarafta ise grafik bilgilerinin girildiği alan bulunmaktadır.

![AreaChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload49d29971-d4c8-4b67-a944-f5765a27fafd)

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Name 	| Grafiğe verilecek isim bu alana yazılır. 	|
| Argument Field 	| İlgili alanlar içinde seçilebilecek olan değerler, grafiğin datasource seçeneğinde eklenmiş olan sorgudaki alanlardan gelmektedir. Argument Field alanına grafikte kullanılması istenen açıklama alanı kolonu seçilir. 	|
| Value Field 	| İlgili alanlar içinde seçilebilecek olan değerler, grafiğin datasource seçeneğinde eklenmiş olan sorgudaki alanlardan gelmektedir. Value Field alanına grafikte kullanılması istenen değer kolonu seçilir. 	|
| Color 	| Grafik renginin seçimi yapılmaktadır. Renk seçimi paneli rgb kodunun solunda bulunan renge tıklanıldığında gösterilmektedir. Palet üzerinde fare işaretçisiyle veya kullanılmak istenen RGB kodu ya da HEX kodu girilerek renk seçimi yapılabilir. RGB kodunun sağında bulunan A ifadesi Alfa Kanalı’nı belirtmekte olup opaklığı ayarlamak için kulanılmaktadır ve değer aralığı 0 ile 100 arasındadır. Bu seçenekler haricinde varsayılan olarak gelen 15 renkten birisi de seçilebilmektedir.![AreaChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfcb60b9a-9c20-4d78-9d97-7c6b43807416) 	|

Verilerin girişi yapıldıktan sonra penceredeki “Kaydet” butona basılarak chart kaydedilmelidir.

`Rotate enabled` - Nesnede verilerin gösterildiği X ve Y eksenlerinin yerlerini değiştirmektedir. Varsayılan durum pasif olarak gelmektedir. Pasif durumda iken argüman alanı X ekseninde, değer alanı Y ekseninde gösterilmektedir. Aktif hale getirildiğinde bu eksenler yer değiştirip argüman alanı Y eksenine, değer alanı X ekseninde gösterilmektedir.

> *Rotate Enabled seçeneği pasif iken grafiğin gösterimi*
![AreaChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd1e7a609-9359-4a4f-a35e-41aa36f7acff)
> *Rotate Enabled aktif iken grafiğin gösterimi*
![AreaChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf2f0f8d3-f77b-4a3c-9bf1-cc9ed77375b7)

`Animation enabled` - Aktif iken form açıldığında chart nesnesindeki verilerin animasyon şeklinde yüklenmesini sağlar. Kapalı olduğunda veriler yüklü şekilde gelir, açık olduğunda gif gibi hareket halinde yüklenir ve yüklü duruma geçer.

`Selection enabled` - Chart üzerinde her hangi bir verinin seçilmesini sağlar.Bu seçenek açıkken fare imleci veri üzerine gelince el şeklinde olur seçim yapıldığında ilgili alan seçili duruma geçer.

`Hover enabled` - Fare imleci ile veri üzerine gelindiğinde o bölgenin stil değişikliğini sağlar; gölgeli hale gelir.

`Tooltip enabled` - Verinin üzerine geldiğinde değerin gösterilmesini sağlar.Örneğin departmana göre kullanıcı sayısı grafiğinde, fare imleci argüman eksenindeki Yazılım departmanı üzerine getirildiğinde kullanıcı sayısını gösterebilir.

### Legend

`Enabled` - Chart içinde gösterilen grafiklerde hangi grafiğin neyi gösterdiğini belirtmek için kullanılmaktadır. Enabled seçeneği aktif hale getirildiğinde chartın yanında bir tooltip içinde bunlar belirtilmektedir.

> *Legend seçeneği aktif değilken chart görünümü*
![AreaChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload50bbaaa5-1790-4d89-9496-aa8e03a4194a)
> *Aktif hale getirildiğinde charttaki görünüm, sol tarafa hangi renk hangi chartı ifade eder bilgisi gösterilir*
![AreaChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload84bc1eaf-893e-4a26-aefc-1755b4b24859)

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

> *Pasif iken argüman eksenindeki değerler gizlenir*
![AreaChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0f8b6fb0-17ce-4210-b175-153a38e2dd80)
> *Aktif iken argüman eksenindeki başlıklar görünür hale gelir*
![AreaChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8f30cf06-7c9e-4dcb-99d7-3b4ef6cc392f)

`Show tick` - Argument Axis içindeki Enabled özelliği aktifken görünen özelliktir. Argüman eksenindeki başlıklardan chart dışına doğru bir işaretçi çizgi çıkarmakta değer girilen Tick Size alanını aktif hale getirmek için kullanılır. Çizgi uzunluğu Tick size ile ayarlanmaktadır.

`Tick size` - Show tick özelliği aktifken görünen özelliktir. Argüman eksenindeki başlıklardan chart dışına doğru bir işaretçi çizgi çıkarmak için kullanılır.

> *Tick Size 0 (sıfır) iken argüman ekseninden çıkan bir çizgi gözükmez*
![AreaChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0be4d1f0-7028-43f8-8aae-0c32851214b6)
> *Tick Size için örnek bir değer olarak 50 girildiğinde argüman ekseninden işaretçi çizgiler çıkmıştır*
![AreaChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb2d143a1-2a96-48c5-897e-3a55d4593fda)

`Indent from axis` - Argument Axis Enabled özelliği aktifken görünen özelliktir.  Grafiğin alt kısmı ile argüman başlıkları arasındaki boşlukları belirlemek için kullanılır.

> *Indent from axis için örnek olarak 50 değeri girilmiş olup, bu değere göre başlıklar ve grafiğin alt kısmı arasındaki boşluk ayarlanabilmektedir*
![AreaChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadac2457ee-2d0c-4644-a546-06ab7ef51812)

`Position` - Argument Axis Enabled özelliği aktifken görünen özelliktir. Listelenen özellikler Top ve Bottom’dır. Arguman ekseninin Bottom (altta) veya Top (üstte) görünmesini sağlar.

>Yapılabilecek Seçimler : Top, Bottom

> *Bottom seçildiğindeki görünümü*
![AreaChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0ab8129c-044d-4ad6-be90-ca341601239f)
> *Top seçeneği seçildiğinde görünüm*
![AreaChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload05be3407-cff7-42fc-a081-8637ae278441)

`Show grid` - Argument Axis Enabled özelliği aktifken görünen özelliktir. Seçili iken argüman başlıklarından chart içine doğru gösterilen kılavuz çizgiler görünür hale gelir.

> *Show Grid seçili iken görünüm*
![AreaChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload42c1ccf7-45b9-41d0-aa12-b3bcea007579)
> *Show Grid seçili değilken görünüm*
![AreaChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3d2f47a8-e661-46d5-9d72-596b5beeff05)

`Show line` - Argument Axis Enabled özelliği aktifken görünen özelliktir. Seçili olduğu durumda orijin noktasından argüman ekseni boyunca devam eden bir çizgi gösterilir. Seçili değilse bu çizgi görünmez.

> *Show line seçili iken orijin noktasından çıkan çizgi görünür durumdadır.*
![AreaChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc24fb598-2cc2-4346-86be-aebe3e3ade76)
> *Show line seçili olmadığında orijin noktasından çıkan çizgi kaldırılır.*
![AreaChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada4cdbdbe-f953-4b1f-aa86-b7e81342f7da)

`Show labels` - Argument Axis Enabled özelliği aktifken görünen özelliktir.  Seçili ise argüman eksenindeki başlıklar görünür halde gelir.

> *Show Label seçili iken argüman eksenindeki başlıklar görünür haldedir.*
![AreaChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5ad5b7c7-c487-4204-8600-383e066250bb)
> *Show Label seçili değilse bu başlıklar görünmeyecektir*
![AreaChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload003bae97-6887-49ed-a715-eabf75bee054)

### Value Axis

`Enabled` - Aktif iken değer eksenindeki başlıklar grafik içinde gösterilmektedir. Kapatıldığı durumda bu eksendeki başlıklar getirilmeyecektir.

> *Enabled seçili iken value eksenindeki değerler görünür olarak getirilir*
![AreaChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload703ab5de-2f2c-4fde-b607-75e015e98afa)
> *Enabled seçeneği kapatıldığında value eksenindeki değer gösterilmeyecektir*
![AreaChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload60a601d0-7f9a-4e35-b1fb-af54f757e61b)

`Show tick` - Value Axis içindeki Enabled özelliği aktifken görünen özelliktir. Value eksenindeki başlıklardan chart dışına doğru bir işaretçi çizgi çıkarmakta değer girilen Tick Size alanını aktif hale getirmek için kullanılır. Çizgi uzunluğu Tick size ile ayarlanmaktadır.

`Tick size` - Show tick özelliği aktifken görünen özelliktir. Değer eksenindeki başlıklardan chart dışına doğru bir işaretçi çizgi çıkarmak için kullanılır.

> *Tick Size 0 iken değer ekseninden çıkan bir çizgi gözükmez*
![AreaChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8bac2aad-9a25-4461-b62c-f603e09909dc)
> *Tick Size için örnek bir değer 50 girildiğinde değer ekseninden işaretçi çizgiler çıkmıştır*
![AreaChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload90248808-a487-4fd8-ac71-cde023265915)

`Indent from axis` - Value Axis Enabled özelliği aktifken görünen özelliktir.  Grafiğin sol kısmı ile değer başlıkları arasındaki boşlukları belirlemek için kullanılır.

> *Indent from axis için örnek olarak 50 değeri girilmiş olup, bu değere göre başlıklar ve grafiğin sol kısmı arasındaki boşluk ayarlanabilmektedir*
![AreaChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload73ec5604-1fa9-4f52-bf0d-aa04aa73aeed)

`Position` - Value Axis Enabled özelliği aktifken görünen özelliktir. Listelenen özellikler Left ve Right’dır. Değer ekseninin Left (solda) veya Right (sağda) görünmesini sağlar.

>Yapılabilecek Seçimler : Left, Right

> *Left seçildiğindeki görünüm*
![AreaChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload73ea03c4-4744-497d-a2f7-6337e25cae70)
> *Right seçildiğindeki görünüm*
![AreaChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload84f297cd-90d6-4154-a05b-33ec1d086bb2)

`Show grid` - Value Axis Enabled özelliği aktifken görünen özelliktir. Seçili iken value başlıklarından chart içine doğru gösterilen kılavuz çizgiler görünür hale gelir.

> *Show Grid seçili iken görünüm*
![AreaChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6ad24b86-9936-40a1-9f91-4ce264dd8376)
> *Show Grid seçili değilken görünüm*
![AreaChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada48a68df-a1cd-46aa-b1e2-ef991202aa01)

`Show line` - Value Axis Enabled özelliği aktifken görünen özelliktir. Seçili olduğu durumda orijin noktasından değer ekseni boyunca devam eden bir çizgi gösterilir. Seçili değilse bu çizgi görünmez.

> *Show line seçili iken orijin noktasından çıkan çizgi görünür durumdadır.*
![AreaChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddf5fb937-293a-46d1-b2c7-68b40028f818)
> *Show line seçili olmadığında orijin noktasından çıkan çizgi kaldırılır.*
![AreaChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5185d6da-04a4-48e4-96ad-2cc75367ea34)

`Show labels` - Value Axis Enabled özelliği aktifken görünen özelliktir. Seçili olduğu durumda orijin noktasından değer ekseni boyunca devam eden bir çizgi gösterilir. Seçili değilse bu çizgi görünmez.

> *Show Label seçili iken argüman eksenindeki başlıklar görünür haldedir*
![AreaChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada109f219-cf5b-4a45-85ef-5fd86e3a8ecd)
> *Show Label seçili değilse bu başlıklar görünmeyecektir*
![AreaChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5f8b592b-e13d-42bc-91e3-508d4260f492)

## Olaylar

Nesnenin sahip olduğu olaylar, Özellik Görüntüleyici panelindeki "Olaylar" sekmesinde yer almaktadır. Her bir olay, farklı çalışma anlarında tetiklenerek kendilerine özgü işlemleri gerçekleştirir. Bu olaylara geliştirici tarafından yazılan kodlar da ilgili olayın tetiklendiği anda çalıştırılır.

"Client" alanında bulunan olaylara çift tıklandığında ekran, TypeScript kodlamanın yapılabileceği "Formadı.ts" isimli form kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur.

"Server" alanında bulunan olaylara çift tıklandığında ekran, C# kodlamanın yapılabileceği "Formadı.cs" isimli form kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur.

Geliştirici bu methodlar içerisinde istediği kod bloğunu kurgulayabilir. Olaylar sekmesinden tıklanarak kod tarafında methodu oluşturulmuş olayın yanında, method adı bilgisi otomatik oluşturularak, olayla method arasındaki ilişki belirtilmiş olur.

![AreaChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0c9e52b5-68c4-47a3-ac45-dc86b75e33a3)