---
sidebar_position: 2
custom_edit_url: ""
---

# LineChart

LineChart nesnesi form üzerinde, uç kullanıcılara veri kaynağından getirilen sonuçları çizgi görselleri ile zenginleştirerek ifade etmek için kullanılır. Bu nesne ile kullanıcının, bir çok bilgiyi doğrudan görüntülemesi yerine, aynı anda özetle görüntülemesi sağlanır.

Geliştirme arayüzünde aktif ekran form iken, Araç Kutusu panelinde form nesneleri listelenir. Nesne, araç kutusu panelinden sürükle/bırak yöntemi ile forma eklenir.

![LineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb36a1730-cbf8-4e65-901d-60425bfd706b)

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

LineChart nesnesinde kullanılacak sorgularda Insert ve Update sorguları kullanılmaz.

:::

![LineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade7b84833-980f-446f-baa9-10d15b68be90)

![LineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada64fa0d8-d70d-4652-a590-4c7a03b34d71)

`RunAtServer` - Bu seçenek nesneye bağlanan sorgunun, sunucudan mı istemciden mi çalıştırılacağının belirlendiği seçenektir.

Bu seçenek aktif edilirse web arayüzünde forma tıklandığında, form açılmadan önce sorgu, sunucu tarafında çalıştırılır, form açıldığında nesneye sorgu sonucu yüklenmiş olarak gelir. Seçenek pasif yapıldığında web arayüzünde forma tıklandığında, form açıldıktan sonra nesneye sorgunun sonuç değerleri yüklenmeye başlar.

Sorgu sonucunun yüklenmesi için geçen bekleme süresi, bu özellik aktifken formun açılma anında, özellik pasifken form hızlı açıldıktan sonra nesneye verinin yüklenmesi anında etkili olur.

### Charts and Activation

`Chart items` - Nesnede gösterilmek istenen grafik tipinin seçildiği alandır. Chart Items kısmına tıklandığında, nesnede gösterilecek chart tipinin seçileceği ve seçilen chart özelliklerinin düzenleneceği bir pencere açılır.

![LineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload947f5eb8-60b7-4542-9db4-26ce562536ba)

Açılan penceredeki “Ekle” butonuna tıklandığında, Chart nesnesinde gösterilmek istenen chart tipleri listelenir. Nesneye aşağıdaki tiplerde chartlar eklenebilir;

> Line Chart (Çizelge Grafiği)

![LineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload96dac7fc-d80a-427b-8d0b-61df71d40c40)

Ekle butonuna tıklanıp bir çizgi grafik eklendiğinde, pencerenin sol tarafındaki Grafikler sekmesine grafik tanımı eklenir. Sağ tarafta ise grafik bilgilerinin girildiği alan bulunmaktadır.

![LineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8aa3910a-d8ca-43bd-a347-eeb6c9c8dae4)

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Name 	| Grafiğe verilecek isim bu alana yazılır. 	|
| Argument Field 	| İlgili alanlar içinde seçilebilecek olan değerler, grafiğin datasource seçeneğinde eklenmiş olan sorgudaki alanlardan gelmektedir. Argument Field alanına grafikte kullanılması istenen açıklama alanı kolonu seçilir. 	|
| Value Field 	| İlgili alanlar içinde seçilebilecek olan değerler, grafiğin datasource seçeneğinde eklenmiş olan sorgudaki alanlardan gelmektedir. Value Field alanına grafikte kullanılması istenen değer kolonu seçilir. 	|
| Color 	| Grafik renginin seçimi yapılmaktadır. Renk seçimi paneli rgb kodunun solunda bulunan renge tıklanıldığında gösterilmektedir. Palet üzerinde fare işaretçisiyle veya kullanılmak istenen RGB kodu ya da HEX kodu girilerek renk seçimi yapılabilir. RGB kodunun sağında bulunan A ifadesi Alfa Kanalı’nı belirtmekte olup opaklığı ayarlamak için kulanılmaktadır ve değer aralığı 0 ile 100 arasındadır. Bu seçenekler haricinde varsayılan olarak gelen 15 renkten birisi de seçilebilmektedir. ![LineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4fdb848b-f118-4814-a79a-b415af74642a) 	|

Verilerin girişi yapıldıktan sonra penceredeki “Kaydet” butona basılarak chart kaydedilmelidir.

`Rotate enabled` - Nesnede verilerin gösterildiği X ve Y eksenlerinin yerlerini değiştirmektedir. Varsayılan durum pasif olarak gelmektedir. Pasif durumda iken argüman alanı X ekseninde, değer alanı Y ekseninde gösterilmektedir. Aktif hale getirildiğinde bu eksenler yer değiştirip argüman alanı Y eksenine, değer alanı X ekseninde gösterilmektedir.

> *Rotate Enabled seçeneği pasif iken grafiğin gösterimi*
![LineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0cc48e7c-458e-4e1e-a160-0e84baba2955)
> *Rotate Enabled aktif iken grafiğin gösterimi*
![LineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2410bfd3-1206-43d4-a0ed-4bdb0d68e735)

`Animation enabled` - Aktif iken form açıldığında chart nesnesindeki verilerin animasyon şeklinde yüklenmesini sağlar. Kapalı olduğunda veriler yüklü şekilde gelir, açık olduğunda gif gibi hareket halinde yüklenir ve yüklü duruma geçer.

`Selection enabled` - Chart üzerinde her hangi bir verinin seçilmesini sağlar.Bu seçenek açıkken fare imleci veri üzerine gelince el şeklinde olur seçim yapıldığında ilgili alan seçili duruma geçer.

`Hover enabled` - Fare imleci ile veri üzerine gelindiğinde o bölgenin stil değişikliğini sağlar; gölgeli hale gelir.

`Tooltip enabled` - Verinin üzerine geldiğinde değerin gösterilmesini sağlar.Örneğin departmana göre kullanıcı sayısı grafiğinde, fare imleci argüman eksenindeki Yazılım departmanı üzerine getirildiğinde kullanıcı sayısını gösterebilir.

### Legend

`Enabled` - Chart içinde gösterilen grafiklerde hangi grafiğin neyi gösterdiğini belirtmek için kullanılmaktadır. Enabled seçeneği aktif hale getirildiğinde chartın yanında bir tooltip içinde bunlar belirtilmektedir.

> *Legend seçeneği aktif değilken chart görünümü*
![LineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd58e38e5-b481-4cfd-9ce9-153d968f2b89)
> *Aktif hale getirildiğinde charttaki görünüm, sol tarafa hangi renk hangi chartı ifade eder bilgisi gösterilir*
![LineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload438da522-79d6-4586-9e2c-b0ed37234cb9)

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
![LineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc1cb7c99-9db2-4ffb-a128-2382c6066abf)
> *Aktif iken argüman eksenindeki başlıklar görünür hale gelir*
![LineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload48648ee3-56e2-4747-9120-a45899e56cf4)

`Show tick` - Argument Axis içindeki Enabled özelliği aktifken görünen özelliktir. Argüman eksenindeki başlıklardan chart dışına doğru bir işaretçi çizgi çıkarmakta değer girilen Tick Size alanını aktif hale getirmek için kullanılır. Çizgi uzunluğu Tick size ile ayarlanmaktadır.

`Tick size` - Show tick özelliği aktifken görünen özelliktir. Argüman eksenindeki başlıklardan chart dışına doğru bir işaretçi çizgi çıkarmak için kullanılır.

> *Tick Size 0 (sıfır) iken argüman ekseninden çıkan bir çizgi gözükmez*
![LineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf6c89a75-63a9-4945-8a8f-2298dd67a6dd)
> *Tick Size için örnek bir değer olarak 50 girildiğinde argüman ekseninden işaretçi çizgiler çıkmıştır*
![LineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaf1022db-8c91-4edf-b5f7-db66d0ea7284)

`Indent from axis` - Argument Axis Enabled özelliği aktifken görünen özelliktir.  Grafiğin alt kısmı ile argüman başlıkları arasındaki boşlukları belirlemek için kullanılır.

> *Indent from axis için örnek olarak 50 değeri girilmiş olup, bu değere göre başlıklar ve grafiğin alt kısmı arasındaki boşluk ayarlanabilmektedir*
![LineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload33c2e807-1936-4152-a21b-3003cd711336)

`Position` - Argument Axis Enabled özelliği aktifken görünen özelliktir. Listelenen özellikler Top ve Bottom’dır. Arguman ekseninin Bottom (altta) veya Top (üstte) görünmesini sağlar.

>Yapılabilecek Seçimler : Top, Bottom

> *Bottom seçildiğindeki görünümü*
![LineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf3e738d0-d441-4d87-a077-656f6527a13a)
> *Top seçeneği seçildiğinde görünüm*
![LineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfb200408-0503-40aa-86bd-2f83bdd600e0)

`Show grid` - Argument Axis Enabled özelliği aktifken görünen özelliktir. Seçili iken argüman başlıklarından chart içine doğru gösterilen kılavuz çizgiler görünür hale gelir.

> *Show Grid seçili iken görünüm*
![LineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf9e7d75d-1ab1-492f-af11-f581775c997e)
> *Show Grid seçili değilken görünüm*
![LineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade3e99b83-53c8-43bf-b46f-8ecf36d0520d)

`Show line` - Argument Axis Enabled özelliği aktifken görünen özelliktir. Seçili olduğu durumda orijin noktasından argüman ekseni boyunca devam eden bir çizgi gösterilir. Seçili değilse bu çizgi görünmez.

> *Show line seçili iken orijin noktasından çıkan çizgi görünür durumdadır.*
![LineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload42d18a2e-e6d0-4359-91e1-4cb6d642e92a)
> *Show line seçili olmadığında orijin noktasından çıkan çizgi kaldırılır.*
![LineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddd7ae578-0830-4c56-b2c1-b0430113b9dd)

`Show labels` - Argument Axis Enabled özelliği aktifken görünen özelliktir.  Seçili ise argüman eksenindeki başlıklar görünür halde gelir.

> *Show Label seçili iken argüman eksenindeki başlıklar görünür haldedir.*
![LineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload67d8a0ff-a387-4cb2-8be0-652746157593)
> *Show Label seçili değilse bu başlıklar görünmeyecektir*
![LineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0feb8bdb-1775-41df-867b-c786806e4eb3)

### Value Axis

`Enabled` - Aktif iken değer eksenindeki başlıklar grafik içinde gösterilmektedir. Kapatıldığı durumda bu eksendeki başlıklar getirilmeyecektir.

> *Enabled seçili iken value eksenindeki değerler görünür olarak getirilir*
![LineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade84b66a9-35b0-409d-898c-c5b68822b278)
> *Enabled seçeneği kapatıldığında value eksenindeki değer gösterilmeyecektir*
![LineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7e7f5c82-a34f-4f04-90e3-e4a1894fab7b)

`Show tick` - Value Axis içindeki Enabled özelliği aktifken görünen özelliktir. Value eksenindeki başlıklardan chart dışına doğru bir işaretçi çizgi çıkarmakta değer girilen Tick Size alanını aktif hale getirmek için kullanılır. Çizgi uzunluğu Tick size ile ayarlanmaktadır.

`Tick size` - Show tick özelliği aktifken görünen özelliktir. Değer eksenindeki başlıklardan chart dışına doğru bir işaretçi çizgi çıkarmak için kullanılır.

> *Tick Size 0 iken değer ekseninden çıkan bir çizgi gözükmez*
![LineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8e4dc7ce-5cdb-4be4-91d8-3b0cce4a5b73)
> *Tick Size için örnek bir değer 50 girildiğinde değer ekseninden işaretçi çizgiler çıkmıştır*
![LineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload40af7d9e-f1cb-4864-98e7-9075b6ffe0b1)

`Indent from axis` - Value Axis Enabled özelliği aktifken görünen özelliktir.  Grafiğin sol kısmı ile değer başlıkları arasındaki boşlukları belirlemek için kullanılır.

> *Indent from axis için örnek olarak 50 değeri girilmiş olup, bu değere göre başlıklar ve grafiğin sol kısmı arasındaki boşluk ayarlanabilmektedir*
![LineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf3e2b7e5-fc67-4029-9b90-45a86e4c78e5)

`Position` - Value Axis Enabled özelliği aktifken görünen özelliktir. Listelenen özellikler Left ve Right’dır. Değer ekseninin Left (solda) veya Right (sağda) görünmesini sağlar.

>Yapılabilecek Seçimler : Left, Right

> *Left seçildiğindeki görünüm*
![LineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload694006a7-6e15-423f-a8ac-5aa7a869be91)
> *Right seçildiğindeki görünüm*
![LineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload33d355ce-d74a-408a-abb0-004e816db30e)

`Show grid` - Value Axis Enabled özelliği aktifken görünen özelliktir. Seçili iken value başlıklarından chart içine doğru gösterilen kılavuz çizgiler görünür hale gelir.

> *Show Grid seçili iken görünüm*
![LineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload230f5cf6-ffd3-421d-873a-2a724a032672)
> *Show Grid seçili değilken görünüm*
![LineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload78f63cd4-25d8-4d6c-9710-21ae75834a55)

`Show line` - Value Axis Enabled özelliği aktifken görünen özelliktir. Seçili olduğu durumda orijin noktasından değer ekseni boyunca devam eden bir çizgi gösterilir. Seçili değilse bu çizgi görünmez.

> *Show line seçili iken orijin noktasından çıkan çizgi görünür durumdadır.*
![LineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload160f6018-979b-49ad-b7b9-a05f03d76d2c)
> *Show line seçili olmadığında orijin noktasından çıkan çizgi kaldırılır.*
![LineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload924b6e1d-b30d-41b3-809e-62e65535c672)

`Show labels` - Value Axis Enabled özelliği aktifken görünen özelliktir. Seçili olduğu durumda orijin noktasından değer ekseni boyunca devam eden bir çizgi gösterilir. Seçili değilse bu çizgi görünmez.

> *Show Label seçili iken argüman eksenindeki başlıklar görünür haldedir*
![LineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd3cc6c21-cd87-419d-8642-6832e908ceb9)
> *Show Label seçili değilse bu başlıklar görünmeyecektir*
![LineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d3ebd0b-7e1e-4ceb-a102-bed933cf25e7)

## Olaylar

Nesnenin sahip olduğu olaylar, Özellik Görüntüleyici panelindeki "Olaylar" sekmesinde yer almaktadır. Her bir olay, farklı çalışma anlarında tetiklenerek kendilerine özgü işlemleri gerçekleştirir. Bu olaylara geliştirici tarafından yazılan kodlar da ilgili olayın tetiklendiği anda çalıştırılır.

"Client" alanında bulunan olaylara çift tıklandığında ekran, TypeScript kodlamanın yapılabileceği "Formadı.ts" isimli form kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur.

"Server" alanında bulunan olaylara çift tıklandığında ekran, C# kodlamanın yapılabileceği "Formadı.cs" isimli form kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur.

Geliştirici bu methodlar içerisinde istediği kod bloğunu kurgulayabilir. Olaylar sekmesinden tıklanarak kod tarafında methodu oluşturulmuş olayın yanında, method adı bilgisi otomatik oluşturularak, olayla method arasındaki ilişki belirtilmiş olur.

![LineChart](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada1f3e9de-fd4a-480a-9e26-c84c002a9b53)