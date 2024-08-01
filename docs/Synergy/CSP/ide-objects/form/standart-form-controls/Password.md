---
sidebar_position: 3
custom_edit_url: ""
---

# Password

Form üzerine şifre ya da herkese açık olması istenmeyen bir bilgi girilmesi gerektiğinde tercih edilen nesnedir. Nesneye girilen karakterler nokta(**.**) ifadesi ile görselleştirilerek gizlenmiş olur.

Geliştirme arayüzünde aktif ekran form iken, Araç Kutusu panelinde form nesneleri listelenir. Nesne, araç kutusu panelinden sürükle/bırak yöntemi ile forma eklenir.

![Password](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadeb68d609-75c2-47f6-9ca1-7d2c5757b51b)

Nesnenin üzerine tıklandığında Özellik Görüntüleyici panelinde "Genel" ve "Olaylar" sekmeleri yer alır ve nesneye ait özellikler görüntülenip, düzenlenebilir.

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

`Text` - Nesnenin içerik değeridir. Form web arayüzde açıldığında bu alanda yazılan metin, nesne içinde varsayılan metin olarak görünür.

`Placeholder` - Nesne içine uç kullanıcı tarafından girilmesi istenen veri bilgisini, nesne içerisinde bilgi amaçlı göstermek için kullanılan özelliktir. Uç kullanıcı nesneyi görüntülediğinde bu alana yazılan yönlendirici metni görür, nesneye odaklandığında ve değer girmeye başladığında yönlendirici metin kaybolur.

`TextAlign` - Nesne içine girilen ifadenin hizalanacağı yerin belirlenmesi için kullanılan alandır. Sola hizala, merkeze hizala, sağa hizala seçimleri yapılabilir.

>Yapılabilecek Seçimler : Left, Center, Right

`Visibility Toggle` - Nesne özelliği gereği, nesneye girilen karakterler, noktalı olarak gizlenir. Hem girişi yapan kullanıcının girdiği değeri kontrol etme ihtiyacından dolayı hem de girilen metni görmesi gereken kullanıcının gizlenmiş karakterleri görünür yapma ihtiyacından dolayı nesnede, "karakterleri göster" fonksiyonunun kullanılıp kullanılmayacağı bu alandan ayarlanır.

![Password](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3bd99c3f-8dba-4f5d-84d2-b54a00a596cd)

![Password](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc6884ae5-e49d-49c8-9728-98e8c72b27f1)

VisibilityToggle özelliği aktif ise, nesnenin yanında karakterleri gösteren fonksiyon görünür olacaktır. Bu özellik pasif yapıldığında karakterleri gösteren fonksiyon nesnede görünmez olur.

Web arayüz kullanımında, nesneye veri girecek kullanıcının, girdiği veriyi görmesi isteniyorsa ancak kişi formu gönderdiğinde bir sonraki kişinin ya da akışta yetkisi olmayan başka bir kullanıcının bu nesneye girilen değeri görmesi istenmiyorsa, VisibilityToggle özelliği tasarım anında aktif edilir, akışta ilgili adımlarda kodla nesnenin bu özelliği kapatılabilir.

`Size Type` - Nesne boyutunun belirlenebileceği alandır.

>Yapılabilecek Seçimler : Small, Middle, Large

### Data Definition Language

`Field Name` - Sistemin veri tabanında, nesne için oluşturacağı kolonun adının belirlendiği alandır. “Name” kısmında nesneye başka bir isim verilip, veritabanı tablosunda nesne için oluşturulacak kolon adı farklı bir isim olarak yaratılabilir.

`Allow Null` - Nesne için oluşturulacak veritabanı alanının boş(null) değerlere izin verip vermeyeceği bu kısımdan belirtilir.

`Size` - Nesnenin veritabanı alanında tutacağı boyut bu alanda belirlenir.

## Olaylar

Nesnenin sahip olduğu olaylar, Özellik Görüntüleyici panelindeki “Olaylar” sekmesinde yer almaktadır. Her bir olay, farklı çalışma anlarında tetiklenerek kendilerine özgü işlemleri gerçekleştirir. Bu olaylara geliştirici tarafından yazılan kodlar da ilgili olayın tetiklendiği anda çalıştırılır.

**“Client”** alanında bulunan olaylara çift tıklandığında ekran, TypeScript kodlamanın yapılabileceği **“Formadı.ts”** isimli form kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur.

**“Server”** alanında bulunan olaylara çift tıklandığında ekran, C# kodlamanın yapılabileceği **“Formadı.cs”** isimli form kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur.

Geliştirici bu methodlar içerisinde istediği kod bloğunu kurgulayabilir. Olaylar sekmesinden tıklanarak kod tarafında methodu oluşturulmuş olayın yanında, method adı bilgisi otomatik oluşturularak, olayla method arasındaki ilişki belirtilmiş olur.

![Password](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddfc3667e-2286-4c1a-9e46-300c1a6c9ae0)

Oluşan methodlar;

![Password](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2a4209d3-c976-498c-ab4f-396c2a7a3826)

![Password](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload37cb2cd4-cc98-441e-94b6-ed48d4137f0f)