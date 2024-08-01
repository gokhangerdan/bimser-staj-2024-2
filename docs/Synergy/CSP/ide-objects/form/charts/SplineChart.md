---
sidebar_position: 3
custom_edit_url: ""
---

# SplineChart

SplineChart nesnesi form üzerinde, uç kullanıcılara veri kaynağından getirilen sonuçları eğri çizgi görselleri ile zenginleştirerek ifade etmek için kullanılır. Bu nesne ile kullanıcının, bir çok bilgiyi doğrudan görüntülemesi yerine, aynı anda özetle görüntülemesi sağlanır.

Geliştirme arayüzünde aktif ekran form iken, Araç Kutusu panelinde form nesneleri listelenir. Nesne, araç kutusu panelinden sürükle/bırak yöntemi ile forma eklenir.

![SplineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload179b312a-ebd5-43ea-bc5b-fe31d5e31c5a)

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

SplineChart nesnesinde kullanılacak sorgularda Insert ve Update sorguları kullanılmaz.

:::

![SplineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9e225bc5-1eab-4645-91bd-1be29199029a)

![SplineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6809cc26-6bb1-40dc-822e-59b198be2e99)

`RunAtServer` - Bu seçenek nesneye bağlanan sorgunun, sunucudan mı istemciden mi çalıştırılacağının belirlendiği seçenektir.

Bu seçenek aktif edilirse web arayüzünde forma tıklandığında, form açılmadan önce sorgu, sunucu tarafında çalıştırılır, form açıldığında nesneye sorgu sonucu yüklenmiş olarak gelir. Seçenek pasif yapıldığında web arayüzünde forma tıklandığında, form açıldıktan sonra nesneye sorgunun sonuç değerleri yüklenmeye başlar.

Sorgu sonucunun yüklenmesi için geçen bekleme süresi, bu özellik aktifken formun açılma anında, özellik pasifken form hızlı açıldıktan sonra nesneye verinin yüklenmesi anında etkili olur.

### Charts and Activation

`Chart items` - Nesnede gösterilmek istenen grafik tipinin seçildiği alandır. Chart Items kısmına tıklandığında, nesnede gösterilecek chart tipinin seçileceği ve seçilen chart özelliklerinin düzenleneceği bir pencere açılır. 

![SplineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload46b518d9-cc4e-4f46-86ec-00632c7d3c53)

Açılan penceredeki “Ekle” butonuna tıklandığında, Chart nesnesinde gösterilmek istenen chart tipleri listelenir. Nesneye aşağıdaki tiplerde chartlar eklenebilir;

> Spline Chart (Eğri Grafiği)

![SplineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd8e45624-f1a0-4e31-8878-56d0be922d81)

Ekle butonuna tıklanıp bir çizgi grafik eklendiğinde, pencerenin sol tarafındaki Grafikler sekmesine grafik tanımı eklenir. Sağ tarafta ise grafik bilgilerinin girildiği alan bulunmaktadır.

![SplineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf42699d9-809e-4458-a33a-233292c385ce)

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Name 	| Grafiğe verilecek isim bu alana yazılır. 	|
| Argument Field 	| İlgili alanlar içinde seçilebilecek olan değerler, grafiğin datasource seçeneğinde eklenmiş olan sorgudaki alanlardan gelmektedir. Argument Field alanına grafikte kullanılması istenen açıklama alanı kolonu seçilir. 	|
| Value Field 	| İlgili alanlar içinde seçilebilecek olan değerler, grafiğin datasource seçeneğinde eklenmiş olan sorgudaki alanlardan gelmektedir. Value Field alanına grafikte kullanılması istenen değer kolonu seçilir. 	|
| Color 	| Grafik renginin seçimi yapılmaktadır. Renk seçimi paneli rgb kodunun solunda bulunan renge tıklanıldığında gösterilmektedir. Palet üzerinde fare işaretçisiyle veya kullanılmak istenen RGB kodu ya da HEX kodu girilerek renk seçimi yapılabilir. RGB kodunun sağında bulunan A ifadesi Alfa Kanalı’nı belirtmekte olup opaklığı ayarlamak için kulanılmaktadır ve değer aralığı 0 ile 100 arasındadır. Bu seçenekler haricinde varsayılan olarak gelen 15 renkten birisi de seçilebilmektedir.![SplineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload09453931-cbcf-4181-8f36-06736fa808be) 	|

Verilerin girişi yapıldıktan sonra penceredeki “Kaydet” butona basılarak chart kaydedilmelidir.

`Rotate enabled` - Nesnede verilerin gösterildiği X ve Y eksenlerinin yerlerini değiştirmektedir. Varsayılan durum pasif olarak gelmektedir. Pasif durumda iken argüman alanı X ekseninde, değer alanı Y ekseninde gösterilmektedir. Aktif hale getirildiğinde bu eksenler yer değiştirip argüman alanı Y eksenine, değer alanı X ekseninde gösterilmektedir.

> *Rotate Enabled seçeneği pasif iken grafiğin gösterimi*
![SplineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaa62d796-9eff-41cf-9f77-6bcf2485d0f9)
> *Rotate Enabled aktif iken grafiğin gösterimi*
![SplineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3a0de556-b4ae-4b4f-acfd-e629019312b1)

`Animation enabled` - Aktif iken form açıldığında chart nesnesindeki verilerin animasyon şeklinde yüklenmesini sağlar. Kapalı olduğunda veriler yüklü şekilde gelir, açık olduğunda gif gibi hareket halinde yüklenir ve yüklü duruma geçer.

`Selection enabled` - Chart üzerinde her hangi bir verinin seçilmesini sağlar.Bu seçenek açıkken fare imleci veri üzerine gelince el şeklinde olur seçim yapıldığında ilgili alan seçili duruma geçer.

`Hover enabled` - Fare imleci ile veri üzerine gelindiğinde o bölgenin stil değişikliğini sağlar; gölgeli hale gelir.

`Tooltip enabled` - Verinin üzerine geldiğinde değerin gösterilmesini sağlar.Örneğin departmana göre kullanıcı sayısı grafiğinde, fare imleci argüman eksenindeki Yazılım departmanı üzerine getirildiğinde kullanıcı sayısını gösterebilir.

### Legend

`Enabled` - Chart içinde gösterilen grafiklerde hangi grafiğin neyi gösterdiğini belirtmek için kullanılmaktadır. Enabled seçeneği aktif hale getirildiğinde chartın yanında bir tooltip içinde bunlar belirtilmektedir.

> *Legend seçeneği aktif değilken chart görünümü*
![SplineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd3e937ba-94e5-42c2-8e15-145b3e6c72d1)
> *Legend seçeneği aktif hale getirildiğinde charttaki görünüm, sol tarafa hangi renk hangi chartı ifade eder bilgisi gösterilir*
![SplineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadea97c122-2063-457d-bf77-39d21a71e227)

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
![SplineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload157ec29a-0331-4de5-864b-8a10aa609c80)
> *Aktif iken argüman eksenindeki başlıklar görünür hale gelir*
![SplineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload50dbf707-1392-41f4-b43c-607799311b2f)

`Show tick` - Argument Axis içindeki Enabled özelliği aktifken görünen özelliktir. Argüman eksenindeki başlıklardan chart dışına doğru bir işaretçi çizgi çıkarmakta değer girilen Tick Size alanını aktif hale getirmek için kullanılır. Çizgi uzunluğu Tick size ile ayarlanmaktadır.

`Tick size` - Show tick özelliği aktifken görünen özelliktir. Argüman eksenindeki başlıklardan chart dışına doğru bir işaretçi çizgi çıkarmak için kullanılır.

> *Tick Size 0 (sıfır) iken argüman ekseninden çıkan bir çizgi gözükmez*
![SplineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7bd08053-dca8-48df-8658-5bd9ee11df4b)
> *Tick Size için örnek bir değer olarak 50 girildiğinde argüman ekseninden işaretçi çizgiler çıkmıştır*
![SplineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload691b474b-e0c5-4390-81d6-58fe1f0d76c4)

`Indent from axis` - Argument Axis Enabled özelliği aktifken görünen özelliktir.  Grafiğin alt kısmı ile argüman başlıkları arasındaki boşlukları belirlemek için kullanılır.

> *Indent from axis için örnek olarak 50 değeri girilmiş olup, bu değere göre başlıklar ve grafiğin alt kısmı arasındaki boşluk ayarlanabilmektedir*
![SplineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload51e657c7-3152-4c40-8487-8e7318d53c33)

`Position` - Argument Axis Enabled özelliği aktifken görünen özelliktir. Listelenen özellikler Top ve Bottom’dır. Arguman ekseninin Bottom (altta) veya Top (üstte) görünmesini sağlar.

>Yapılabilecek Seçimler : Top, Bottom

> *Bottom seçildiğindeki görünümü*
![SplineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4b7054b6-dbd8-4c33-8f55-80664a339108)
> *Top seçeneği seçildiğinde görünüm*
![SplineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfff7cd82-df39-47d5-8fe2-5956237bbc37)

`Show grid` - Argument Axis Enabled özelliği aktifken görünen özelliktir. Seçili iken argüman başlıklarından chart içine doğru gösterilen kılavuz çizgiler görünür hale gelir.

> *Show Grid seçili iken görünüm*
![SplineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6f1362c7-9dc3-4d11-9654-e2678ee27f6e)
> *Show Grid seçili değilken görünüm*
![SplineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3f248492-481f-4827-b300-edf2400afe8d)

`Show line` - Argument Axis Enabled özelliği aktifken görünen özelliktir. Seçili olduğu durumda orijin noktasından argüman ekseni boyunca devam eden bir çizgi gösterilir. Seçili değilse bu çizgi görünmez.

> *Show line seçili iken orijin noktasından çıkan çizgi görünür durumdadır.*
![SplineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1f2fbca5-b519-4278-ac67-056d5e129233)
> *Show line seçili olmadığında orijin noktasından çıkan çizgi kaldırılır.*
![SplineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload85b450c5-4b8c-4277-a24b-4c71695b204c)

`Show labels` - Argument Axis Enabled özelliği aktifken görünen özelliktir.  Seçili ise argüman eksenindeki başlıklar görünür halde gelir.

> *Show Label seçili iken argüman eksenindeki başlıklar görünür haldedir.*
![SplineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload332aa21b-c0e9-4d20-9639-395cf212f48d)
> *Show Label seçili değilse bu başlıklar görünmeyecektir*
![SplineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload50c511ca-5920-414b-93a4-6c9a831cac80)

### Value Axis

`Enabled` - Aktif iken değer eksenindeki başlıklar grafik içinde gösterilmektedir. Kapatıldığı durumda bu eksendeki başlıklar getirilmeyecektir.

> *Enabled seçili iken value eksenindeki değerler görünür olarak getirilir*
![SplineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd5d909b2-7855-40b8-bb9c-d33e2d414753)
> *Enabled seçeneği kapatıldığında value eksenindeki değer gösterilmeyecektir*
![SplineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload77cb776a-bfde-4d87-8d44-90e3ccf83686)

`Show tick` - Value Axis içindeki Enabled özelliği aktifken görünen özelliktir. Value eksenindeki başlıklardan chart dışına doğru bir işaretçi çizgi çıkarmakta değer girilen Tick Size alanını aktif hale getirmek için kullanılır. Çizgi uzunluğu Tick size ile ayarlanmaktadır.

`Tick size` - Show tick özelliği aktifken görünen özelliktir. Değer eksenindeki başlıklardan chart dışına doğru bir işaretçi çizgi çıkarmak için kullanılır.

> *Tick Size 0 iken değer ekseninden çıkan bir çizgi gözükmez*
![SplineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0a64be41-3276-4905-8b48-f41db968659b)
> *Tick Size için örnek bir değer 50 girildiğinde değer ekseninden işaretçi çizgiler çıkmıştır*
![SplineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5cb90010-b47d-40e6-9175-1c249811bc5d)

`Indent from axis` - Value Axis Enabled özelliği aktifken görünen özelliktir.  Grafiğin sol kısmı ile değer başlıkları arasındaki boşlukları belirlemek için kullanılır.

> *Indent from axis için örnek olarak 50 değeri girilmiş olup, bu değere göre başlıklar ve grafiğin sol kısmı arasındaki boşluk ayarlanabilmektedir*
![SplineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload82e2e6b2-c00d-4123-ad5a-f205f53aee2e)

`Position` - Value Axis Enabled özelliği aktifken görünen özelliktir. Listelenen özellikler Left ve Right’dır. Değer ekseninin Left (solda) veya Right (sağda) görünmesini sağlar.

>Yapılabilecek Seçimler : Left, Right

> *Left seçildiğindeki görünüm*
![SplineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddabdc759-a30f-4a79-8ea2-7fb5ea4330d6)
> *Right seçildiğindeki görünüm*
![SplineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd2b153aa-633e-4ac5-9cb9-3443d6219b29)

`Show grid` - Value Axis Enabled özelliği aktifken görünen özelliktir. Seçili iken value başlıklarından chart içine doğru gösterilen kılavuz çizgiler görünür hale gelir.

> *Show Grid seçili iken görünüm*
![SplineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2513171f-f18a-4be3-90f2-749cd1842583)
> *Show Grid seçili değilken görünüm*
![SplineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcc290578-4df7-43fb-8bd4-8bc1212a8760)

`Show line` - Value Axis Enabled özelliği aktifken görünen özelliktir. Seçili olduğu durumda orijin noktasından değer ekseni boyunca devam eden bir çizgi gösterilir. Seçili değilse bu çizgi görünmez.

> *Show line seçili iken orijin noktasından çıkan çizgi görünür durumdadır.*
![SplineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc31caf43-3314-4e9d-8afb-f783a147ca8d)
> *Show line seçili olmadığında orijin noktasından çıkan çizgi kaldırılır.*
![SplineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7fe1cbbc-5bda-444a-8069-2758d5f331da)

`Show labels` - Value Axis Enabled özelliği aktifken görünen özelliktir. Seçili olduğu durumda orijin noktasından değer ekseni boyunca devam eden bir çizgi gösterilir. Seçili değilse bu çizgi görünmez.

> *Show Label seçili iken argüman eksenindeki başlıklar görünür haldedir*
![SplineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2436f2f6-0394-4e7d-9b6d-36aad8d75173)
> *Show Label seçili değilse bu başlıklar görünmeyecektir*
![SplineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1c00d429-f169-4a44-8e33-e0e4a8b3de8d)

## Olaylar

Nesnenin sahip olduğu olaylar, Özellik Görüntüleyici panelindeki "Olaylar" sekmesinde yer almaktadır. Her bir olay, farklı çalışma anlarında tetiklenerek kendilerine özgü işlemleri gerçekleştirir. Bu olaylara geliştirici tarafından yazılan kodlar da ilgili olayın tetiklendiği anda çalıştırılır.

"Client" alanında bulunan olaylara çift tıklandığında ekran, TypeScript kodlamanın yapılabileceği "Formadı.ts" isimli form kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur.

"Server" alanında bulunan olaylara çift tıklandığında ekran, C# kodlamanın yapılabileceği "Formadı.cs" isimli form kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur.

Geliştirici bu methodlar içerisinde istediği kod bloğunu kurgulayabilir. Olaylar sekmesinden tıklanarak kod tarafında methodu oluşturulmuş olayın yanında, method adı bilgisi otomatik oluşturularak, olayla method arasındaki ilişki belirtilmiş olur.

![SplineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7c0c18cd-f926-4bfa-af50-f9d2ab12e7eb)