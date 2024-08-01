---
sidebar_position: 6
custom_edit_url: ""
---
# Karşılaştırma

Karşılatırma nesnesi, tasarlanan süreç içinde bir değer göre süreç yönlendirmesinin yapıldığı nesnedir. Akış tasarımında süreçte hangi adımdan sonra karşılaştırma yapılması istenen yerlere bu nesne eklenmelidir.

Akış tasarım ekranında bulunan nesneye tıklandığında, Özellik Görüntüleyici panelinde, nesne özellikleri görünür.

![Karşılaştırma](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf6805614-8e55-4947-ad1c-578e74899480)

Karşılaştırma nesnesine tıklandığında Özellik Görüntüleyici panelinde "Appearance", "Properties" ve "Events" sekmeleri bulunmaktadır.

## Appearance

### Text Configs

`Object Name` - Nesnenin sistem tarafında kullanılacak ismidir. Kod tarafında nesneye, nesne adı alanında yazan değerle erişim sağlanır.

`Caption` - Nesnenin başlık metninin girildiği alandır.

`Is Lock` - Tasarım anında nesnenin yeri değiştirilmesin isteniyorsa bu alan aktif edilir.

`Size` - Nesnenin genişlik ve yükseklik ayarlarının yapıldığı kısımdır.

## Properties

### Compare

`Source Object` - Akış içindeki hangi nesneye göre karşılaştırmanın yapılacağının seçiminin yapılmasını sağlar. Kaynak nesne seçimi yapıldığında Sonuçlar kısmı aktif hale gelir.

Source Object alanında akıştaki **[Değişken](#source-variable)**, **[Akışı başlatan](#source-flow-starter)**, **[Pozisyon](#source-position)**, **[Departman](#source-department)** ve **[Unvan](#source-profession)** nesneleri kullanılabilmektedir.

![Karşılaştırma](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload64dc84de-247a-48d2-a3cc-7d6439b56036)

> *Aşağıdaki resimdeki 1 numaralı senaryoda Karşılaştırma nesnesi içinde Source Object alanında seçim yapılmadığından Results seçeneği gelmemektedir. 2 numaralı senaryoda Source Object seçildiği için Results alanı gelmektedir.*
![Karşılaştırma](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcd42cbda-7a2b-477c-a676-a150e6c62eee)

#### Source Object alanında **Değişken** nesnesi seçilirse {#source-variable}

`Özelliği kullan` - Karşılaştırma nesnesinde Source Object alanında akıştaki Değişken nesnesi seçildiğinde gözüken alandır. Değişken nesnesinde Doküman nesnesi seçilip, Source Object alanında formdaki bir nesne seçildiğinde, nesne içinde yapılan seçimin Text veya Value ifadelerine göre mi karşılaştırmanın yapılacağı belirlenebilmektedir. (Örneğin ComboBox ve Lookup nesnelerinde Value ve Text olarak farklı bilgiler bulunduğundan, ComboBox nesnesinde seçili ögenin Text'ine göre ilerlemesi sağlanabilir.)

> Yapılabilecek seçimler: Text, Value

`Results` - Karşılaştırma içinde gelen değerin hangi şart/şartlara göre değerlendirilip yönlendirileceğinin belirlendiği bölümdür. Üç noktaya tıklanarak Sonuçlar paneli açılır. Pencerede Ekle butonuna tıklanarak kural eklenebilir. Pencerenin sol tarafında eklenen şartlar bulunurken sağ tarafta o şartın özellikleri bulunmaktadır.

![Karşılaştırma](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0e1aab2c-3ce8-47d8-839f-0e79ae3f3306)

Karşılaştırma tipi alanı içindeki seçilebilecek ögeler, Karşılaştırma nesnesinde seçilen Değişken nesnesinin türüne göre değişiklik gösterecektir.

:::danger UYARI

Aşağıdaki tablo Karşılaştırma nesnesinde **Özelliği kullan** alanında **Value** seçildiyse geçerlidir. Alanda **Text** seçimi yapılırsa, Değişken tipi ne olursa olsun tablodaki Metin kolonunda listelenen seçimler (Eşittir, Eşit değildir, Boş, Boş değil, İçerir, İçermez, İle Başlar, İle Biter) Karşılaştırma tipi alanında gözükecektir.

:::

| **Tanımlanan Değişken Tipi** 	| **Karşılaştırma tipi alanında listelenen seçimler** 	|
|---	|---	|
| Metin 	| Eşittir, Eşit değildir, Boş, Boş değil, İçerir, İçermez, İle Başlar, İle Biter 	|
| Tam sayı 	| Eşittir, Eşit değildir, Boş, Boş değil, Daha büyük, Daha büyük veya eşit, Daha küçük, Daha küçük veya eşit, Arasında, Arasında olmayan 	|
| Ondalıklı sayı 	| Eşittir, Eşit değildir, Boş, Boş değil, Daha büyük, Daha büyük veya eşit, Daha küçük, Daha küçük veya eşit, Arasında, Arasında olmayan 	|
| Tarih 	| Eşittir, Eşit değildir, Boş, Boş değil, Daha büyük, Daha büyük veya eşit, Daha küçük, Daha küçük veya eşit, Arasında, Arasında olmayan 	|
| Para 	| Eşittir, Eşit değildir, Boş, Boş değil, Daha büyük, Daha büyük veya eşit, Daha küçük, Daha küçük veya eşit, Arasında, Arasında olmayan 	|
| Doğru/Yanlış 	| Eşittir, Eşit değildir 	|

- Result alanı içindeki tanımlama panelinde eklenen ögedeki Değer Türü alanında **Constant** ve **Liquid** seçenekleri bulunmaktadır. Constant seçildiğinde karşılaştırma sonucu sabit bir değer ile kontrol edilebilirken, Liquid seçildiğinde akıştaki liquid verileri kullanılarak veya darklı bir Değişken nesnesi içindeki değere göre karşılaştırma yapılması gerçekleştirilebilir.

> *Sabit değer ile karşılaştırma*
![Karşılaştırma](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4c44d972-e17d-4732-8976-99b70ba1c797)

> *Akıştaki farklı bir Değişken nesnesi içeriğini kullanarak karşılaştırma*
![Karşılaştırma](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcbf71d63-2461-47df-b7be-721c71502a3e)

:::info BİLGİ

Tarih tipindeki Değişken nesnesi tanımlandığında, Değişken'in içerdiği tarih değerini formatlama için Biçim alanı gözükür, Değer türü Constant seçildiyse Değer alanında tarih seçimi yapılmalıdır.

<div style={{textAlign: 'center'}}>

![Karşılaştırma](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload52362129-91cb-4007-9908-1c73abcc5a5d)

</div>

<div style={{textAlign: 'center'}}>

![Karşılaştırma](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload73754a81-e9b4-4b1a-92ba-f12f92bc9352)

</div>

:::

:::info BİLGİ

Boolean tipindeki Değişken nesnesi tanımlandığında, Değer türü Constant seçildiyse Değer alanında true/false ifadesinin karşılığı olan switch gözükecektir.

<div style={{textAlign: 'center'}}>

![Karşılaştırma](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload08518d55-5754-4beb-9a32-9c73a3862c17)

</div>

:::

Results alanınındaki tanımlı sonuçlar silinmek istenirse panel içinden veya alanda üç nokta ifadesinin yanındaki Sıfırla butonu kullanılabilir.

![Karşılaştırma](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload70239557-6ffe-406f-b3c2-f47b9f1c0fc5)

#### Source Object alanında **Pozisyon** nesnesi seçilirse {#source-position}

`Comparison value` - Karşılaştırma işleminin seçilen Pozisyon nesnesine göre Kod veya Kimlik bilgisinin mi kullanılacağının belirlendiği alandır.

> Yapılabilecek seçimler: Kod, Kimlik

`Collection type` - Karşılaştırma işleminin seçilen Pozisyon nesnesine göre, kullanıcı veya pozisyon bilgisine göre karşılaştırma işleminin yapılmasının belirlendiği alandır.

> Yapılabilecek seçimler: User, Position

`Results` - Karşılaştırma içinde gelen değerin hangi şart/şartlara göre değerlendirilip yönlendirileceğinin belirlendiği bölümdür. Üç noktaya tıklanarak Sonuçlar paneli açılır. Collection type alanında yapılacak seçime göre kullanıcı bilgisi veya pozisyon bilgisi listelenerek karşılaştırma işleminde kullanılacak veriler seçilir.

#### Source Object alanında **Departman** nesnesi seçilirse {#source-department}

`Comparison value` - Karşılaştırma işleminin seçilen Departman nesnesine göre Kod veya Kimlik bilgisinin mi kullanılacağının belirlendiği alandır.

> Yapılabilecek seçimler: Kod, Kimlik

`Results` - Karşılaştırma içinde gelen değerin hangi şart/şartlara göre değerlendirilip yönlendirileceğinin belirlendiği bölümdür. Üç noktaya tıklanarak Sonuçlar paneli açılır. Panel içinde listelenen departmanlar arasında seçim yapılarak karşılaştırma işleminde kullanılacak verilerin seçilir.

#### Source Object alanında **Unvan** nesnesi seçilirse {#source-profession}

`Comparison value` - Karşılaştırma işleminin seçilen Unvan nesnesine göre Kod veya Kimlik bilgisinin mi kullanılacağının belirlendiği alandır.

> Yapılabilecek seçimler: Kod, Kimlik

`Results` - Karşılaştırma içinde gelen değerin hangi şart/şartlara göre değerlendirilip yönlendirileceğinin belirlendiği bölümdür. Üç noktaya tıklanarak Sonuçlar paneli açılır. Panel içinde listelenen unvanlar arasında seçim yapılarak karşılaştırma işleminde kullanılacak verilerin seçilir.

#### Source Object alanında **Akışı başlatan** nesnesi seçilirse {#source-flow-starter}

`Collection type` - Karşılaştırma işleminin seçilen Akışı başlatan nesnesine göre, kullanıcı veya pozisyon bilgisine göre karşılaştırma işleminin yapılmasının belirlendiği alandır.

> Yapılabilecek seçimler: User, Position

`Results` - Karşılaştırma içinde gelen değerin hangi şart/şartlara göre değerlendirilip yönlendirileceğinin belirlendiği bölümdür. Üç noktaya tıklanarak Sonuçlar paneli açılır. Collection type alanında yapılacak seçime göre kullanıcı bilgisi veya pozisyon bilgisi listelenerek karşılaştırma işleminde kullanılacak veriler seçilir.

:::tip İPUCU

Karşılaştırma nesnesinde bağlantı oku çekilirken nesneye yanlış şart bağlandıysa, tüm okları silip yeniden bağlantıların oluşturulmasına gerek yoktur. Hatalı oka fare işaretçisi ile çift tıklandığında bağlantı düzenleme ve silme paneli açılır.

<div style={{textAlign: 'center'}}>

![Karşılaştırma](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7fd03fb4-c3f5-40ff-bbde-be30a6515ec2)

</div>

Panelde **Sil** seçeneği seçili iken Tamam butonuna tıklandığında oluşturulan bağlantı silinecektir. Değiştir seçeneği seçili olduğunda, değiştirilmesi istenen şart alttaki alanda seçilerek Tamam butonuna tıklanabilir.

:::

:::info BİLGİ

Nesne üzerinde ekli özelliklerin doğru olduğu sistem tarafından kontrol edilmektedir. Eksik bir özellik bulunduğunda nesne üzerinde kırmızı ünlem ikonu gösterilerek, fare işaretçisi ile ikon üzerine gelindiğinde nelerin eksik veya hatalı olduğu görüntülenebilmektedir.

![Karşılaştırma](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf9f7c608-a0cd-46f0-b815-48f9608cf919)

:::

## Events

Karşılaştırma nesnesinin sahip olduğu olaylar, Özellik Görüntüleyici panelindeki "Events" sekmesinde yer almaktadır. Her bir olay, farklı çalışma anlarında tetiklenerek kendilerine özgü işlemleri gerçekleştirir. Bu olaylara geliştirici tarafından yazılan kodlar da ilgili olayın tetiklendiği anda çalıştırılır. Herhangi bir olaya kod yazmak için, Events sekmesinden ilgili olay satırına çift tıklanır. Ekran, “Akışadı.cs” isimli akış kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur. Geliştirici bu method içerisinde istediği kod bloğunu kurgulayabilir. Events sekmesinden tıklanarak kod tarafında methodu oluşturulmuş olayın yanında, method adı bilgisi otomatik oluşturularak, olayla method arasındaki ilişki belirtilmiş olur.

![Karşılaştırma](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4bbe4248-ee58-4e91-a763-86b53ac97a33)