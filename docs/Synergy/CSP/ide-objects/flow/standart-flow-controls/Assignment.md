---
sidebar_position: 5
custom_edit_url: ""
---

# Atama

Atama nesnesi, akış üzerindeki bir çok nesneye değer set etmek için kullanılabilen bir nesnedir. Atama işlemi sonucunda set edilen nesne hangi akış adımında kullanılacaksa, atama nesnesinin o adımdan önce kullanılması gerekir.

Akış tasarım ekranında bulunan nesneye tıklandığında, Özellik Görüntüleyici panelinde, nesne özellikleri görünür.

![Atama](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload17376ca5-f2e7-4670-ae9e-136f72cd002b)

Atama nesnesine tıklandığında Özellik Görüntüleyici panelinde "Appearance", "Properties" ve "Events" sekmeleri bulunmaktadır.

## Appearance

### Text Configs

`Object Name` - Nesnenin sistem tarafında kullanılacak ismidir. Kod tarafında nesneye, nesne adı alanında yazan değerle erişim sağlanır.

`Caption` - Nesnenin başlık metninin girildiği alandır.

`Is Lock` - Tasarım anında nesnenin yeri değiştirilmesin isteniyorsa bu alan aktif edilir.

`Size` - Nesnenin genişlik ve yükseklik ayarlarının yapıldığı kısımdır.

## Properties
 
### Status

Atama işlemi için; hangi nesneye, hangi türde, hangi değerin atanacağının belirlendiği kısımdır.

`Target Object` - Hangi akış nesnesine atama yapılmak isteniyorsa o nesne bu alandan seçilir. Atama nesnesinde hedef nesne olarak kullanılabilecek nesneler; Pozisyon, Değişken, Departman ve Unvan nesneleridir. Seçilen hedef nesneye göre bu nesneye ne tür değer atanabileceği değişiklik gösterir.

![Atama](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload520e50ab-9be9-4869-a4a8-c94ba498ade8)

- Target Object olarak **Pozisyon** nesnesi seçilirse;

Target Object kısmından Pozisyon nesnesi seçildiğinde, bu pozisyon nesnesine yapılacak atamanın Source Type değerleri ve seçilen kaynak tipine göre hangi değerin atanacağı Kaynak Değeri bilgileri aşağıdaki tabloda açıklanmıştır.

![Atama](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8d019b28-c158-4443-aa66-c989807ed516)

| **Hedef Nesne** 	| **Kaynak Tipi** 	| **Kaynak Tipi Açıklaması** 	| **Kaynak Verisi** 	|
|---	|---	|---	|---	|
| Pozisyon 	| Sabit pozisyon 	| Seçilen hedef nesneye, sistemde tanımlı pozisyon tanımlarından birini atamak için kullanılır 	| Kaynak verisi olarak, sistemdeki pozisyon tanımlarını listeleyen bir seçim alanı açılır. Geliştirici, hedef nesneye atayacağı pozisyon bilgisini bu listeden seçer 	|
| Pozisyon 	| Sabit kullanıcı 	| Seçilen hedef nesneye, sistemde tanımlı kullanıcı tanımlarından birini atamak için kullanılır 	| Kaynak verisi olarak, sistemdeki kullanıcı tanımlarını listeleyen bir seçim alanı açılır. Geliştirici, hedef nesneye atayacağı kullanıcı bilgisini bu listeden seçer 	|
| Pozisyon 	| Değişken pozisyon 	| Seçilen hedef nesneye, akışta bulunan “Akışı Başlatan” ve diğer “Pozisyon” nesnelerinde bulunan kişiyi atamak için kullanılır 	| Kaynak verisi olarak, akış tasarımında bulunan tüm pozisyon nesneleri ve akışı başlatan nesnesi listelenir. Geliştirici, hangi akış nesnesindeki kişiyi hedef nesneye kişi olarak atamak istiyorsa bu listeden ilgili nesneyi seçer 	|
| Pozisyon 	| Akışı başlatan 	| Seçilen hedef nesneye, akışı başlatan kullanıcı atanmak isteniyorsa kullanılır 	|  	|
| Pozisyon 	| Akışı başlatanın yöneticisi 	| Seçilen hedef nesneye, akışı başlatan kullanıcının yöneticisi atanmak isteniyorsa kullanılır 	| Sistemde bir kullanıcının birden çok yönetici tanımı bulunabilir. Bu yöneticiler farklı yönetici profilleri ile tanımlıdır (bir kişinin teknik amiri ve idari amiri olarak iki yöneticiye sahip olması gibi).Source Type alanında Akışı Başlatanın Yöneticisi seçildiğinde atama yapılacak yönetici profilinin seçileceği bir “Profil” alanı açılır. Burada kişinin hangi profil amirininin atanacağı seçilir.<br/><br/>Akışı başlatanın yöneticisi seçildiğinde yönetici bulunmadığı senaryo için nesnede oluşan **NoManager** bağlantısı kullanılmalıdır.  	|
| Pozisyon 	| Kullanıcı yöneticisi 	| Seçilen hedef nesneye, akışta bulunan herhangi bir pozisyon nesnesindeki ya da akışı başlatan nesnesindeki kişinin yöneticisini atamak için kullanılır 	| Sistemde bir kullanıcının birden çok yönetici tanımı bulunabilir. Bu yöneticiler farklı yönetici profilleri ile tanımlıdır (bir kişinin teknik amiri ve idari amiri olarak iki yöneticiye sahip olması gibi).<br/><br/>Kaynak verisi olarak önce atama yapılacak yönetici profilinin seçileceği bir “Profil” alanı açılır. Burada kişinin hangi profil amirininin atanacağı seçilir. Sonrasında kaynak verisi kısmından akışta bulunan “Akışı Başlatan” ve diğer “Pozisyon” nesneleri listesinden, hangi kullanıcının yöneticisi hedef nesneye atanmak isteniyorsa ilgili nesnenin seçimi yapılır 	|
| Pozisyon 	| Departman yöneticisi 	| Seçilen hedef nesneye, akışta bulunan ve sistemde tanımlı departman bilgilerinden birini tutan “Departman” nesnesinin yöneticisini atamak için kullanılır 	| Kaynak verisi olarak, akış tasarımında kullanılan **“Departman”** nesneleri listelenir. Hangi departman nesnesinde tanımlı departmanın yöneticisi hedef nesneye atanmak isteniyorsa bu alandan ilgili nesne seçilir 	|
| Pozisyon 	| Değişken değerden pozisyon 	| Seçilen hedef nesneye, akıştaki bir “Değişken” nesnesinde bulunan pozisyon kodu değerini veya akışta geri dönüş değeri olarak pozisyon kodu gönderen bir “Fonksiyon” nesnesinden dönen değeri atamak için kullanılır 	| Kaynak verisi olarak, akış tasarımında kullanılan “Değişken” ve “Fonksiyon” nesneleri listelenir. Hangi nesnedeki pozisyon tanımı hedef nesneye atanmak isteniyorsa o nesne bu listeden seçilecektir.<br/><br/>Değişken nesnesinde, pozisyon kodu tutuluyor olması gerekir. Fonksiyon nesnesi ise geri dönüş değeri olarak bir pozisyon kodu göndermelidir. 	|
| Pozisyon 	| Değişken değerden kullanıcı 	| Seçilen hedef nesneye, akıştaki bir “Değişken” nesnesinde bulunan kullanıcı kodu değerini veya akışta geri dönüş değeri olarak kullanıcı kodu gönderen bir “Fonksiyon” nesnesinden dönen değeri atamak için kullanılır 	| Kaynak verisi olarak, akış tasarımında kullanılan **“Değişken”** ve **“Fonksiyon”** nesneleri listelenir. Hangi nesnedeki kullanıcı tanımı hedef nesneye atanmak isteniyorsa o nesne bu listeden seçilecektir.<br/><br/>Değişken nesnesinde, kullanıcı kodu tutuluyor olması gerekir. Fonksiyon nesnesi ise geri dönüş değeri olarak bir kullanıcı kodu göndermelidir. 	|
| Pozisyon 	| Unvana göre üst pozisyon 	| Seçilen hedef nesneye, akıştaki bir Pozisyon nesnesinin veya akışı başlatanın, belirlenen unvanlı yöneticisini atamak için kullanılır. 	| Kaynak verisi olarak, akış tasarımında kullanılan **“Pozisyon”** ve **“Akışı Başlatan”** nesneleri listelenir. Ayrıca unvan seçimi için akışta kullanılan **“Unvan”** nesneleri veya sabit unvan tanımı verilmek isteniyorsa sistemdeki unvanların listesi gelmektedir. Kullanıcının hangi profil tanımlı amirinin atanacağı Profil alanı da bulunmaktadır.<br/><br/>Seçilen kaynak pozisyonun, seçilen unvan tanımlı yöneticisi, hedef nesneye atanmış olur. 	|
| Pozisyon 	| Oturum açan kullanıcı 	| Yerine işlem ve vekaleten gerçekleştirilen işlemlerde hedef nesneye, işlemi yapmak için oturum açan kullanıcının ataması yapılır 	|  	|
| Pozisyon 	| Oturum açan asıl kullanıcı 	| Yerine işlem ve vekaleten gerçekleştirilen işlemlerde hedef nesneye, yerine geçen veya vekaleten işlem yapan kişinin ataması yapılır 	|  	|

- Target Object olarak **Değişken** nesnesi seçilirse;

![Atama](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8950bc82-8bb7-4e6d-adbb-b7e0a54afd02)

Target Object kısmından Değişken nesnesi seçildiğinde, bu değişken nesnesine yapılacak atamanın Kaynak Tipi değerleri ve seçilen kaynak tipine göre hangi değerin atanacağı Kaynak Değeri bilgileri aşağıdaki tabloda açıklanmıştır. Kaynak Tipi alanı, değişken nesnesinin “Source Type” değerine göre farklılık gösterir.

| **Hedef Nesne** 	| **Değişken Türü** 	| **Kaynak Tipi** 	| **Kaynak Tipi Açıklaması** 	| **Kaynak Verisi** 	|
|---	|---	|---	|---	|---	|
| Değişken 	| Metin 	| Sabit değer 	| Değişken nesnesine sabit bir metin değeri atamak için kullanılır 	| Değişken nesnesine atanacak sabit değerin girilebileceği bir **“Değer”** alanı açılır 	|
| Değişken 	| Metin 	| Değişken değer 	| Akışta kullanılan bir nesnenin değerini değişken nesnesine atamak için kullanılır 	| Kaynak verisi olarak, akıştaki **Pozisyon**, **Akışı Başlatan**, **Değişken**, **Departman**, **Unvan** ve **Fonksiyon** nesneleri listelenir. Hangi nesnenin verisi değişkene atanmak isteniyorsa o nesne buradan seçilecektir.<br/><br/>Fonksiyon nesnesinin değişkene atanacak bir dönüş değeri göndermesi gerekir. 	|
| Metin 	| Metin 	| Proje adı 	| Proje adını değişken nesnesine atamak için kullanılır 	|  	|
| Değişken 	| Tamsayı 	| Sabit değer 	| Akışta kullanılan bir nesnenin değerini değişken nesnesine atamak için kullanılır 	| Değişken nesnesine atanacak sabit değerin girilebileceği bir **“Değer”** alanı açılır 	|
| Değişken 	| Tamsayı 	| Değişken değer 	| Akışta kullanılan bir nesnenin değerini değişken nesnesine atamak için kullanılır 	| Kaynak verisi olarak, akıştaki **Pozisyon**, **Akışı Başlatan**, **Değişken**, **Departman**, **Unvan** ve **Fonksiyon** nesneleri listelenir. Hangi nesnenin verisi değişkene atanmak isteniyorsa o nesne buradan seçilecektir.<br/><br/>Fonksiyon nesnesinin değişkene atanacak bir dönüş değeri göndermesi gerekir. 	|
| Değişken 	| Tamsayı 	| Arttır 	| Değişken nesnesindeki değeri 1 artırır 	|  	|
| Değişken 	| Tamsayı 	| Azalt 	| Değişken nesnesindeki değeri 1 azaltır 	|  	|

- Target Object olarak **Departman** nesnesi seçilirse;

![Atama](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb9256b9d-275c-4c20-80c2-4e46a5e19fb5)

Target Object kısmından Departman nesnesi seçildiğinde, bu departman nesnesine yapılacak atamanın Source Type değerleri ve seçilen kaynak tipine göre hangi değerin atanacağı Kaynak Değeri bilgileri aşağıdaki tabloda açıklanmıştır.

| **Hedef Nesne** 	| **Kaynak Tipi** 	| **Kaynak Tipi Açıklaması** 	| **Kaynak Verisi** 	|
|---	|---	|---	|---	|
| Departman 	| Sabit departman 	| Departman nesnesine sistemde tanımlı bir departmanı atamak için kullanılır 	| Kaynak verisi olarak, sistemde tanımlı tüm departmanlar listelenir. Departman nesnesine atanmak istenen departman tanımı bu listeden seçilir 	|
| Departman 	| Değişken departmanı 	| Akışta kullanılan başka bir departman nesnesindeki departman değerini atamak için kullanılır 	| Kaynak verisi olarak, akış tasarımında kullanılan tüm departman nesneleri listelenir. Hangi departman nesnesinde tutulan kayıt atanmak isteniyorsa bu listeden seçilir 	|
| Departman 	| Pozisyon departmanı 	| Akışta kullanılan bir pozisyon nesnesindeki kullanıcının ya da akışı başlatan kullanıcının departman bilgisi, departman nesnesine atanmak istenirse kullanılır 	| Kaynak verisi olarak, akışta kullanılan tüm pozisyon nesneleri ve akışı başlatan nesnesi listelenir 	|
| Departman 	| Akış başlatıcı departmanı 	| Akışı başlatan kullanıcının departman bilgisi nesneye atanmak isteniyorsa kullanılır 	|  	|
| Departman 	| Değişken değer 	| Akışta kullanılan bir nesnenin değerini departman nesnesine atamak için kullanılır 	| Kaynak verisi olarak, akıştaki **Değişken** ve **Fonksiyon** nesneleri listelenir. Hangi nesnenin verisi departman nesnesine atanmak isteniyorsa o nesne buradan seçilecektir.<br/><br/>Fonksiyon nesnesinin departman nesnesine atanacak bir dönüş değeri göndermesi gerekir. 	|
| Departman 	| Yönetici departmanı 	| Akışta kullanılan başka bir departman nesnesindeki departmanın üst departmanını atamak için kullanılır 	| Kaynak verisi olarak, akış tasarımında kullanılan tüm departman nesneleri listelenir. Hangi departman nesnesinde tutulan departman değerinin üst departmanı atanmak isteniyorsa bu listeden seçilir 	|

- Target Object olarak **Unvan** nesnesi seçilirse;

![Atama](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2b79ebd1-c60e-4dbc-bc6c-673138a654fe)

Target Object kısmından Unvan nesnesi seçildiğinde, bu unvan nesnesine yapılacak atamanın Source Type değerleri ve seçilen kaynak tipine göre hangi değerin atanacağı Kaynak Değeri bilgileri aşağıdaki tabloda açıklanmıştır.

| **Hedef Nesne** 	| **Kaynak Tipi** 	| **Kaynak Tipi Açıklaması** 	| **Kaynak Verisi** 	|
|---	|---	|---	|---	|
| Unvan 	| Sabit unvan 	| Ünvan nesnesine, sistemde tanımlı bir ünvan değeri atanmak istendiğinde kullanılır 	| Kaynak verisi olarak sistemdeki tüm ünvan kayıtları listelenir. Nesneye atanmak istenen ünvan bu listeden seçilir 	|
| Unvan 	| Değişken unvan 	| Akışta kullanılan başka bir ünvan nesnesindeki ünvan değerini atamak için kullanılır 	| Kaynak verisi olarak, akış tasarımında kullanılan tüm ünvan nesneleri listelenir. Hangi ünvan nesnesinde tutulan kayıt atanmak isteniyorsa bu listeden seçilir 	|
| Unvan 	| Görev unvanı 	| Akışta kullanılan bir pozisyon nesnesindeki kullanıcının ya da akışı başlatan kullanıcının ünvan bilgisi, ünvan nesnesine atanmak istenirse kullanılır 	| Kaynak verisi olarak, akışta kullanılan tüm pozisyon nesneleri ve akışı başlatan nesnesi listelenir 	|
| Unvan 	| Akış başlatıcı unvanı 	| Akışı başlatan kullanıcının ünvan bilgisi nesneye atanmak isteniyorsa kullanılır 	|  	|
| Unvan 	| Değişken değer 	| Akışta kullanılan bir nesnenin değerini ünvan nesnesine atamak için kullanılır 	| Kaynak verisi olarak, akıştaki **Değişken** ve **Fonksiyon** nesneleri listelenir. Hangi nesnenin verisi ünvan nesnesine atanmak isteniyorsa o nesne buradan seçilecektir.<br/><br/>Fonksiyon nesnesinin ünvan nesnesine atanacak bir dönüş değeri göndermesi gerekir. 	|

:::info BİLGİ

Nesne üzerinde ekli özelliklerin doğru olduğu sistem tarafından kontrol edilmektedir. Eksik bir özellik bulunduğunda nesne üzerinde kırmızı ünlem ikonu gösterilerek, fare işaretçisi ile ikon üzerine gelindiğinde nelerin eksik veya hatalı olduğu görüntülenebilmektedir.

![Atama](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcac76617-7e19-4ecf-b852-226b9a91afe9)

:::

### Action

`Continue If Error Occurs` - Özellik aktif edildiğinde Atama nesnesine ait Contunie bağlantına okuna ek olarak ContinueIfErrorOccured bağlantı okunun kullanılması sağlanır. Nesne içinde yanlış tasarım, atama bilgisinin bulunmaması vb. gibi durumlar sebebiyle atama işlemi yapılamadığında sürecin uç kullanıcı tarafında hata vermesi yerine bu ok üzerinden ilerleyerek, hata oluştuğunda sürecin farklı bir işlem yapması sağlanabilmektedir.

![Atama](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaded5f194c-cd87-4530-bb08-9dc85bcc45f7)

`Error Description Object` - Nesnede Continue If Error Occurs özelliği aktif olduğunda gözüken alandır. Nesne içinde hata oluştuğunda hata mesajının akıştaki Değişken nesnesine aktarılması istendiğinde kullanılmalıdır.

## Events

Atama nesnesinin sahip olduğu olaylar, Özellik Görüntüleyici panelindeki "Events" sekmesinde yer almaktadır. Her bir olay, farklı çalışma anlarında tetiklenerek kendilerine özgü işlemleri gerçekleştirir. Bu olaylara geliştirici tarafından yazılan kodlar da ilgili olayın tetiklendiği anda çalıştırılır. Herhangi bir olaya kod yazmak için, Events sekmesinden ilgili olay satırına çift tıklanır. Ekran, “Akışadı.cs” isimli akış kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur. Geliştirici bu method içerisinde istediği kod bloğunu kurgulayabilir. Events sekmesinden tıklanarak kod tarafında methodu oluşturulmuş olayın yanında, method adı bilgisi otomatik oluşturularak, olayla method arasındaki ilişki belirtilmiş olur.

![Atama](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1fe07d26-bc1a-4c25-929d-6b88d6dfaa6c)