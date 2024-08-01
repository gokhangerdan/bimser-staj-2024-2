---
sidebar_position: 4
custom_edit_url: ""
---

# BarChart

BarChart nesnesi form üzerinde, uç kullanıcılara veri kaynağından getirilen sonuçlar bar şeklindeki grafiklerle ile zenginleştirerek ifade etmek için kullanılır. Bu nesne ile kullanıcının, bir çok bilgiyi doğrudan görüntülemesi yerine, aynı anda özetle görüntülemesi sağlanır.

Geliştirme arayüzünde aktif ekran form iken, Araç Kutusu panelinde form nesneleri listelenir. Nesne, araç kutusu panelinden sürükle/bırak yöntemi ile forma eklenir.

![BarChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6f607591-b511-4f7d-a970-100403db3170)

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

BarChart nesnesinde kullanılacak sorgularda Insert ve Update sorguları kullanılmaz.

:::

![BarChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcdd4dfea-e5d6-437f-8c07-47654e50b220)

![BarChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload771a5276-e84a-4b6d-abe2-479e24aae0fc)

`RunAtServer` - Bu seçenek nesneye bağlanan sorgunun, sunucudan mı istemciden mi çalıştırılacağının belirlendiği seçenektir.

Bu seçenek aktif edilirse web arayüzünde forma tıklandığında, form açılmadan önce sorgu, sunucu tarafında çalıştırılır, form açıldığında nesneye sorgu sonucu yüklenmiş olarak gelir. Seçenek pasif yapıldığında web arayüzünde forma tıklandığında, form açıldıktan sonra nesneye sorgunun sonuç değerleri yüklenmeye başlar.

Sorgu sonucunun yüklenmesi için geçen bekleme süresi, bu özellik aktifken formun açılma anında, özellik pasifken form hızlı açıldıktan sonra nesneye verinin yüklenmesi anında etkili olur.

### Charts and Activation

`Chart items` - Nesnede gösterilmek istenen grafik tipinin seçildiği alandır. Chart Items kısmına tıklandığında, nesnede gösterilecek chart tipinin seçileceği ve seçilen chart özelliklerinin düzenleneceği bir pencere açılır. 

![BarChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfd146cdc-fd38-483e-8e13-a9ece8a8e6aa)

Açılan penceredeki “Ekle” butonuna tıklandığında, Chart nesnesinde gösterilmek istenen chart tipleri listelenir. Nesneye aşağıdaki tiplerde chartlar eklenebilir;

> Bar Chart (Sütun Grafiği)

![BarChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc060a6f1-cf47-469e-8b98-7ec47c3253da)

Ekle butonuna tıklanıp bir çizgi grafik eklendiğinde, pencerenin sol tarafındaki Grafikler sekmesine grafik tanımı eklenir. Sağ tarafta ise grafik bilgilerinin girildiği alan bulunmaktadır.

![BarChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload80e1fea7-d868-406b-826d-88bbc6684b55)

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Name 	| Grafiğe verilecek isim bu alana yazılır. 	|
| Argument Field 	| İlgili alanlar içinde seçilebilecek olan değerler, grafiğin datasource seçeneğinde eklenmiş olan sorgudaki alanlardan gelmektedir. Argument Field alanına grafikte kullanılması istenen açıklama alanı kolonu seçilir. 	|
| Value Field 	| İlgili alanlar içinde seçilebilecek olan değerler, grafiğin datasource seçeneğinde eklenmiş olan sorgudaki alanlardan gelmektedir. Value Field alanına grafikte kullanılması istenen değer kolonu seçilir. 	|
| Color 	| Grafik renginin seçimi yapılmaktadır. Renk seçimi paneli rgb kodunun solunda bulunan renge tıklanıldığında gösterilmektedir. Palet üzerinde fare işaretçisiyle veya kullanılmak istenen RGB kodu ya da HEX kodu girilerek renk seçimi yapılabilir. RGB kodunun sağında bulunan A ifadesi Alfa Kanalı’nı belirtmekte olup opaklığı ayarlamak için kulanılmaktadır ve değer aralığı 0 ile 100 arasındadır. Bu seçenekler haricinde varsayılan olarak gelen 15 renkten birisi de seçilebilmektedir.![BarChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload97b7470b-3e0f-443a-80f0-39a8b8352a36) 	|

Verilerin girişi yapıldıktan sonra penceredeki “Kaydet” butona basılarak chart kaydedilmelidir.

`Rotate enabled` - Nesnede verilerin gösterildiği X ve Y eksenlerinin yerlerini değiştirmektedir. Varsayılan durum pasif olarak gelmektedir. Pasif durumda iken argüman alanı X ekseninde, değer alanı Y ekseninde gösterilmektedir. Aktif hale getirildiğinde bu eksenler yer değiştirip argüman alanı Y eksenine, değer alanı X ekseninde gösterilmektedir.

> *Rotate Enabled seçeneği pasif iken grafiğin gösterim*
![BarChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4e788795-1db6-4387-a00a-f9397bf8d8a2)
> *Rotate Enabled aktif iken grafiğin gösterimi*
![BarChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0cd8362c-63d0-4c96-8014-97e091839729)

`Animation enabled` - Aktif iken form açıldığında chart nesnesindeki verilerin animasyon şeklinde yüklenmesini sağlar. Kapalı olduğunda veriler yüklü şekilde gelir, açık olduğunda gif gibi hareket halinde yüklenir ve yüklü duruma geçer.

`Selection enabled` - Chart üzerinde her hangi bir verinin seçilmesini sağlar.Bu seçenek açıkken fare imleci veri üzerine gelince el şeklinde olur seçim yapıldığında ilgili alan seçili duruma geçer.

`Hover enabled` - Fare imleci ile veri üzerine gelindiğinde o bölgenin stil değişikliğini sağlar; gölgeli hale gelir.

`Tooltip enabled` - Verinin üzerine geldiğinde değerin gösterilmesini sağlar.Örneğin departmana göre kullanıcı sayısı grafiğinde, fare imleci argüman eksenindeki Yazılım departmanı üzerine getirildiğinde kullanıcı sayısını gösterebilir.

### Legend

`Enabled` - Chart içinde gösterilen grafiklerde hangi grafiğin neyi gösterdiğini belirtmek için kullanılmaktadır. Enabled seçeneği aktif hale getirildiğinde chartın yanında bir tooltip içinde bunlar belirtilmektedir.

> *Legend seçeneği aktif değilken chart görünümü*
![BarChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7e645c50-07da-469b-b524-37ca1f535f39)
> *Aktif hale getirildiğinde charttaki görünüm, sol tarafa hangi renk hangi chartı ifade eder bilgisi gösterilir*
![BarChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada7b225d9-e2f4-4ba3-89f2-5b8dfe0412e1)

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
![BarChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload14243f90-3681-48ae-8849-c723c86a47f8)
> *Aktif iken argüman eksenindeki başlıklar görünür hale gelir*
![BarChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1021f86e-8971-4bb3-9e50-b745e1b28922)

`Show tick` - Argument Axis içindeki Enabled özelliği aktifken görünen özelliktir. Argüman eksenindeki başlıklardan chart dışına doğru bir işaretçi çizgi çıkarmakta değer girilen Tick Size alanını aktif hale getirmek için kullanılır. Çizgi uzunluğu Tick size ile ayarlanmaktadır.

`Tick size` - Show tick özelliği aktifken görünen özelliktir. Argüman eksenindeki başlıklardan chart dışına doğru bir işaretçi çizgi çıkarmak için kullanılır.

> *Tick Size 0 (sıfır) iken argüman ekseninden çıkan bir çizgi gözükmez*
![BarChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0ddb44a3-92f2-4503-8ab9-ff9c182b907a)
> *Tick Size için örnek bir değer olarak 50 girildiğinde argüman ekseninden işaretçi çizgiler çıkmıştır*
![BarChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload42203923-2471-46e7-813b-830977732881)

`Indent from axis` - Argument Axis Enabled özelliği aktifken görünen özelliktir.  Grafiğin alt kısmı ile argüman başlıkları arasındaki boşlukları belirlemek için kullanılır.

> *Indent from axis için örnek olarak 50 değeri girilmiş olup, bu değere göre başlıklar ve grafiğin alt kısmı arasındaki boşluk ayarlanabilmektedir*
![BarChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5cd1ed5a-c6de-4db2-a97f-64600ec09634)

`Position` - Argument Axis Enabled özelliği aktifken görünen özelliktir. Listelenen özellikler Top ve Bottom’dır. Arguman ekseninin Bottom (altta) veya Top (üstte) görünmesini sağlar.

>Yapılabilecek Seçimler : Top, Bottom

> *Bottom seçildiğindeki görünümü*
![BarChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc1657533-0991-45c6-ba82-ed1ac1e3025b)
> *Top seçeneği seçildiğinde görünüm*
![BarChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade6edc8e4-3904-419e-b11e-56b3fdd0bd9a)

`Show grid` - Argument Axis Enabled özelliği aktifken görünen özelliktir. Seçili iken argüman başlıklarından chart içine doğru gösterilen kılavuz çizgiler görünür hale gelir.

> *Show Grid seçili iken görünüm*
![BarChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadda0c9a35-ad85-4900-ab77-1c79c408f13b)
> *Show Grid seçili değilken görünüm*
![BarChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload45d38b0b-181b-4a14-9cf7-0a3715c5786e)

`Show line` - Argument Axis Enabled özelliği aktifken görünen özelliktir. Seçili olduğu durumda orijin noktasından argüman ekseni boyunca devam eden bir çizgi gösterilir. Seçili değilse bu çizgi görünmez.

> *Show line seçili iken orijin noktasından çıkan çizgi görünür durumdadır.*
![BarChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7760b3e7-82d9-45b3-bbee-64cf53f3da46)
> *Show line seçili olmadığında orijin noktasından çıkan çizgi kaldırılır.*
![BarChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2b9e71a6-838c-4f12-9180-b5390c89ca32)

`Show labels` - Argument Axis Enabled özelliği aktifken görünen özelliktir.  Seçili ise argüman eksenindeki başlıklar görünür halde gelir.

> *Show Label seçili iken argüman eksenindeki başlıklar görünür haldedir.*
![BarChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaff31446-8ede-4009-a89b-616979b2f37f)
> *Show Label seçili değilse bu başlıklar görünmeyecektir*
![BarChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload12460598-e4f6-4830-b5f0-5f61d4f1f1f1)

### Value Axis

`Enabled` - Aktif iken değer eksenindeki başlıklar grafik içinde gösterilmektedir. Kapatıldığı durumda bu eksendeki başlıklar getirilmeyecektir.

> *Enabled seçili iken value eksenindeki değerler görünür olarak getirilir*
![BarChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade26dae07-b00c-412d-8994-1749de07e122)
> *Enabled seçeneği kapatıldığında value eksenindeki değer gösterilmeyecektir*
![BarChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1cca1efb-acea-4425-b7ea-ec2518853b4f)

`Show tick` - Value Axis içindeki Enabled özelliği aktifken görünen özelliktir. Value eksenindeki başlıklardan chart dışına doğru bir işaretçi çizgi çıkarmakta değer girilen Tick Size alanını aktif hale getirmek için kullanılır. Çizgi uzunluğu Tick size ile ayarlanmaktadır.

`Tick size` - Show tick özelliği aktifken görünen özelliktir. Değer eksenindeki başlıklardan chart dışına doğru bir işaretçi çizgi çıkarmak için kullanılır.

> *Tick Size 0 iken değer ekseninden çıkan bir çizgi gözükmez*
![BarChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada3c0c814-36ea-40f3-ab84-0906b4172bb0)
> *Tick Size için örnek bir değer 50 girildiğinde değer ekseninden işaretçi çizgiler çıkmıştır*
![BarChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade366618c-3fcd-48ce-a459-aa8fefb79033)

`Indent from axis` - Value Axis Enabled özelliği aktifken görünen özelliktir.  Grafiğin sol kısmı ile değer başlıkları arasındaki boşlukları belirlemek için kullanılır.

> *Indent from axis için örnek olarak 50 değeri girilmiş olup, bu değere göre başlıklar ve grafiğin sol kısmı arasındaki boşluk ayarlanabilmektedir*
![BarChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd15cc5d6-4edb-4077-ad3f-ba72dd7f52e6)

`Position` - Value Axis Enabled özelliği aktifken görünen özelliktir. Listelenen özellikler Left ve Right’dır. Değer ekseninin Left (solda) veya Right (sağda) görünmesini sağlar.

>Yapılabilecek Seçimler : Left, Right

> *Left seçildiğindeki görünüm*
![BarChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3241b16f-5a98-4c2d-b31f-b4ce9a9e841f)
> *Right seçildiğindeki görünüm*
![BarChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcf452d61-1215-4bb1-abb8-4135a89b873e)

`Show grid` - Value Axis Enabled özelliği aktifken görünen özelliktir. Seçili iken value başlıklarından chart içine doğru gösterilen kılavuz çizgiler görünür hale gelir.

> *Show Grid seçili iken görünüm*
![BarChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload355d8026-769a-4abd-813d-35cb8955fd2d)
> *Show Grid seçili değilken görünüm*
![BarChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7505f354-a244-4e1e-bd46-9522a01d58e7)

`Show line` - Value Axis Enabled özelliği aktifken görünen özelliktir. Seçili olduğu durumda orijin noktasından değer ekseni boyunca devam eden bir çizgi gösterilir. Seçili değilse bu çizgi görünmez.

> *Show line seçili iken orijin noktasından çıkan çizgi görünür durumdadır.*
![BarChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload88b4ba26-cab8-4b82-95cf-3124bcab978c)
> *Show line seçili olmadığında orijin noktasından çıkan çizgi kaldırılır.*
![BarChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadab5b9205-3763-408f-9740-335e27e16494)

`Show labels` - Value Axis Enabled özelliği aktifken görünen özelliktir. Seçili olduğu durumda orijin noktasından değer ekseni boyunca devam eden bir çizgi gösterilir. Seçili değilse bu çizgi görünmez.

> *Show Label seçili iken argüman eksenindeki başlıklar görünür haldedir*
![BarChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade4326ce2-5179-4292-8c43-98b8c29b3acf)
> *Show Label seçili değilse bu başlıklar görünmeyecektir*
![BarChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd024c07d-ba65-4896-879d-6022e9a31ce7)

## Olaylar

Nesnenin sahip olduğu olaylar, Özellik Görüntüleyici panelindeki "Olaylar" sekmesinde yer almaktadır. Her bir olay, farklı çalışma anlarında tetiklenerek kendilerine özgü işlemleri gerçekleştirir. Bu olaylara geliştirici tarafından yazılan kodlar da ilgili olayın tetiklendiği anda çalıştırılır.

"Client" alanında bulunan olaylara çift tıklandığında ekran, TypeScript kodlamanın yapılabileceği "Formadı.ts" isimli form kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur.

"Server" alanında bulunan olaylara çift tıklandığında ekran, C# kodlamanın yapılabileceği "Formadı.cs" isimli form kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur.

Geliştirici bu methodlar içerisinde istediği kod bloğunu kurgulayabilir. Olaylar sekmesinden tıklanarak kod tarafında methodu oluşturulmuş olayın yanında, method adı bilgisi otomatik oluşturularak, olayla method arasındaki ilişki belirtilmiş olur.

![BarChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2ebc5210-55b8-4dc4-b9ec-f8963b57170f)