---
sidebar_position: 2
custom_edit_url: ""
---

# Doküman Oluştur

Doküman Oluştur nesnesi istenilen formun bir örneğini yaratarak akış üzerindeki Doküman nesnesine atamaya yarar. Bu nesne bağlantı kolları ile diğer akış nesnelerine bağlanarak akışa dahil edilir. Akış adımı Doküman Oluştur nesnesinden geçtiği anda, içinde tanımlı olan Doküman nesnesinin bağlı olduğu form, sistemde oluşturulmuş olur.

:::caution DİKKAT

Doküman Oluştur nesnesi eski akış şablonunda doküman nesnesinde tanımlı formu oluşturmak için kullanılan bir nesnedir. Yeni akış şablonunda Akış Başlangıcı nesnesi içine Doküman eklendiğinde, süreç bir sonraki adıma gönderildiğinde form oluşmaktadır. Doküman Oluştur nesnesini akışı dallandırdığınız ve farklı yerlerde dokümanının oluşturulması için kullanabilirsiniz.

> *Yeni akış şablonu*
![Doküman Oluştur](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1b189a23-9437-4527-af97-4b1c5adb77cc)
> *Eski akış şablonu*
![Doküman Oluştur](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd8b13279-ac18-41cd-8428-abbaf49ee5d2)

Yeni akış şablonunda Doküman süreç başlatılmadan oluşmayacağından veri tabanı üzerinden kayıt oluşmaz. Eski şablonda menüden tıklandığında Doküman Oluştur nesnesinden geçeceği için veri tabanında kayıt oluşur.

:::

İçerisinde Doküman nesnesi tanımlanabilen Pozisyon, Pozisyon Grubu, Bilgilendirme gibi nesnelerden önce, içlerinde tanımlanmış olan Doküman nesnesinin, Doküman Oluştur nesnesi kullanılarak yaratılması gerekmektedir. Aksi taktirde Doküman nesnesinin ekli olduğu diğer akış nesneleri ilgili dokümanı görüntüleyemez ve sistem tarafından hata alınır.

Araç kutusu panelinden Doküman Oluştur nesnesi süreklenip form üzerine bırakılır. Doküman Oluştur nesnesine tıklandığında Özellik Görüntüleyici panelinde nesnesinin sahip olduğu özellikler listelenecektir.

Doküman Oluştur nesnesine tıklandığında Özellik Görüntüleyici panelinde "Appearance", "Properties" ve "Events" sekmeleri bulunmaktadır.

![Doküman Oluştur](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadeb3b648c-3c20-40c3-906f-83830799d832)

## Appearance

### Text Configs

`Object Name` - Nesnenin sistem tarafında kullanılacak ismidir. Kod tarafında nesneye, nesne adı alanında yazan değerle erişim sağlanır.

`Caption` - Nesnenin başlık metninin girildiği alandır.

`Is Lock` - Tasarım anında nesnenin yeri değiştirilmesin isteniyorsa bu alan aktif edilir.

`Size` - Nesnenin genişlik ve yükseklik ayarlarının yapıldığı kısımdır.

## Properties

### Documents

`Document` - Alanda akış tasarımında bulunan tüm Doküman nesneleri listelenir. Hangi Doküman nesnesinde tanımlı form, Doküman Oluştur nesnesi ile ilişkilendirilmek isteniyorsa buradan ilgili Doküman nesnesi seçimi yapılacaktır.

![Doküman Oluştur](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd80e5d6a-150e-4fb7-b1b8-8fc2c07b5227)

`Type` - Doküman Oluştur nesnesi ile yeni bir doküman mı oluşturulacağı yoksa var olan bir dokümanın mı nesnede tanımlanacağı seçimi yapılır. Alanda "None", "Create new form", "Add existing document" şeklinde üç seçenek listelenir.

- Create new form seçeneği seçildiğinde; ekrana Creator, Process, Form, View, Create Id alanları belirir.

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Creator 	| Creator kısmında, akış tasarımında kullanılan Akışı Başlatan ve Pozisyon nesneleri listelenir. Belgenin akış üzerindeki hangi pozisyon adına oluşturulacağı bu alandan seçilir. 	|
| Project 	| Project kısmında, oluşturulacak formun dahil olduğu projenin adı seçilir. 	|
| Form 	| Form kısmında, oluşturulacak olan form seçilecektir. 	|
| View 	| Görünüm kısmında, formun hangi görünümünün (view) oluşturulacağı seçilir. Eğer Pozisyon gibi doküman gösterebilen diğer akış nesnelerinde ekstradan görünüm belirlenmemişse, kişilere varsayılan olarak burada yaratılan görünüm gösterilecektir. 	|
| Create Id 	| Create Id seçeneği işaretlenirse, oluşturulan forma bir form Id numarası atanır. Ayrıca Doküman No Set Etme nesnesi kullanımına gerek kalmaz. 	|
| Panel Size 	| Seçilen formun web ara yüzünde görüntülenirken form panel tipinde açıldığında, panelin genişliğini belirlemek için kullanılır. 	|

- Add existing document seçeneği seçildiğinde; ekrana Path Type, Path Source Type, Value alanları belirir

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Path Type 	| Sistemdeki formun Doküman Oluştur nesnesine hangi verisi ile tanıtılacağının seçimi yapılır. Bu alanda "Tam yol" ve "Form no" seçenekleri listelenir.<br/><br/>Tam Yol seçeneği seçildiğinde, Doküman Oluştur nesnesine tanımlanacak formun, Doküman Yönetim Sistemindeki yolu değer olarak verilmelidir.<br/>Form No seçilirse de ilgili formun Form Id (Global Id) numarasının nesneye verilmesi gerekir. 	|
| Path Source Type 	| Doküman Oluştur nesnesine tanıtılacak formun tam yol bilgisini veya form id bilgisini nereden alacağı bu kısımdan belirtilir. Bu alanda "Constant Path" ve "From Variable" seçenekleri listelenir.<br/><br/>Constant Path seçeneği seçildiğinde ve Değer alanına tıklandığında, Doküman Yönetim Sisteminden ilgili formun yolunun seçilebileceği bir pencere açılacaktır.<br/>From Variable seçeneği seçildiğinde ise Değer alanından, akış tasarımındaki Fonksiyon ve Değişken nesneleri listelenir. Doküman Oluştur nesnesine tanımlanacak formun tam yol ya da Form No bilgisini veren akış nesnesi bu alandan seçilir. 	|
| Value 	| Path Source Type alanında yapılan seçime göre Doküman Yönetimi içinde seçimin yapılacağı veya Değişken nesnesinin seçileceği alandır. 	|
| Panel Size 	| Seçilen formun web ara yüzünde görüntülenirken form panel tipinde açıldığında, panelin genişliğini belirlemek için kullanılır. 	|

### Relations

`Upper Document` - Doküman Oluştur nesnesinde seçilen dokümanın üst dokümanı varsa üst dokümanın bağlı olduğu Doküman nesnesinin seçimi bu alandan yapılır.

`Caption` - İlişkili dokümanın başlık bilgisinin tanımlandığı alandır.

:::info BİLGİ

Nesne üzerinde ekli özelliklerin doğru olduğu sistem tarafından kontrol edilmektedir. Eksik bir özellik bulunduğunda nesne üzerinde kırmızı ünlem ikonu gösterilerek, fare işaretçisi ile ikon üzerine gelindiğinde nelerin eksik veya hatalı olduğu görüntülenebilmektedir.

![Doküman Oluştur](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload36b5bb62-c1ef-442a-82bd-006cee26cc1b)

:::

## Events

### Events

Doküman Oluştur nesnesinin sahip olduğu olaylar, Özellik Görüntüleyici panelindeki "Events" sekmesinde yer almaktadır. Her bir olay, farklı çalışma anlarında tetiklenerek kendilerine özgü işlemleri gerçekleştirir. Bu olaylara geliştirici tarafından yazılan kodlar da ilgili olayın tetiklendiği anda çalıştırılır. Herhangi bir olaya kod yazmak için, Olaylar sekmesinden ilgili olay satırına çift tıklanır. Ekran, “Akışadı.cs” isimli akış kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur. Geliştirici bu method içerisinde istediği kod bloğunu kurgulayabilir. Olaylar sekmesinden tıklanarak kod tarafında methodu oluşturulmuş olayın yanında, method adı bilgisi otomatik oluşturularak, olayla method arasındaki ilişki belirtilmiş olur.

![Doküman Oluştur](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2bfe6877-0329-47a9-8dc1-379be0f79fdf)