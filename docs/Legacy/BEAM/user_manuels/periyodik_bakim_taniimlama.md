# Periyodik Bakım Nasıl Oluşturulur?

Tanım: Periyodik bakım kendisine ait tanımları olan bir alt modüldür. Her planlı bakımda olduğu gibi bu bakımı gerçekleştirmek için de iş adımları (checklist) bulunur. Periyodik bakımın başlıca tanımları şunlardır;

- İş Adımları (Zorunlu)
- Bakım Planları (Zorunlu)
- Ölçüm Paketleri (Zorunlu Değil)
- Periyodik Bakım Tanımları (Zorunlu)


Bu tanımları yapabilmek için aşağıdaki yolu izleyiniz;
- Malzeme Yönetimi > Periyodik Bakım 

![](https://docsbimser.blob.core.windows.net/imagecontainer/21-b13333a5-9eb3-4305-a8cc-807f2af56eef.png)

## 1) İş Adımları

### 1.1) Genel Bilgiler

İş adımı kodu: Uygun bir kod belirleyiniz.

İş adımı tanımı: Yapılması gereken iş adımını detaylı şekilde giriniz. 

## 2) Bakım Planı

### 2.1) Genel Bilgiler

Bakım planı kodu: Uygun bir kod belirleyiniz.

Bakım planı tanımı: Uygun bir tanımlama yapınız. Periyodik Bakım tanımı değildir, bir bakım birden fazla periyodik bakımda kullanılabilir. Bu nedenle seçilecek iş adımlarının topladığımız bir pakete isim veriyor gibi düşünebilirsiniz.

### 2.2) İş adımları

![](https://docsbimser.blob.core.windows.net/imagecontainer/4-e8ef1646-cd31-4fb8-9004-92b05c2aa6b1.png)

İş adımları arayüzünde oluşturduğunuz gerekli iş adımlarını buraya giriniz.
Çoklu seçim özelliği ile iş adımlarını tek seferde seçerek ekleyebilirsiniz.

## 3) Ölçüm Paketleri

### 3.1) Genel Bilgiler

![](https://docsbimser.blob.core.windows.net/imagecontainer/5-22d0691a-cc0e-4d00-abcb-7d266bed5be0.png)

Ölçüm Paketi Kodu ve tanımını giriniz. Standart ve birimini belirledikten sonra toleranstan belirlenecek ise tolerans bilgisini girdikten sonra seçeneği işaretleyiniz.
Eğer alt ve üst değer ile ölçüm sonucu kontrol edilecek ise tolerans seçeneği işaretlemenize gerek yoktur.


### 3.2) İş Emri Bilgileri

![](https://docsbimser.blob.core.windows.net/imagecontainer/7-8d3fd0bc-b331-444a-bc7c-7d613721d50f.png)

- Kabul edilebilir değerler dışına çıkıldığında İş Emri oluştur.
İş emri kapatıldığında, belirlenen alt ve üst değer (veya Tolerans) Dışına çıkıldığında bu durumla alakalı olarak, yeni bir iş emri oluşturur.
Oluşturulan bu iş emrinin ayarları aşağıdaki bölmelerde seçilerek ayarlanır.

## 4) Periyodik Bakım Tanımları

- Hazırlanan planı hangi varlıkta uygulanacak,
- Hangi periyotlar ile iş emri oluşturulacak
- Oluşturulan bu iş emrinde iş tipi, talep açıklaması ve benzeri bilgilerin düzenlendiği bir alandır.


### 4.1) Periyodik Bakım Bilgileri

![](https://docsbimser.blob.core.windows.net/imagecontainer/1-1fa8c395-7135-449d-a3e4-41e7bd201c7e.png)

1) Varlık: Periyodik bakımın yapılacağı varlığı seçiniz.
2) Bakım/Arıza Kodu: Bakım kodu olarak daha detaylı şekilde tanımlama yapılması önerilir. Örneğin: Periyodik Bakım yerine 3 Aylık Periyodik Bakım
3) Tarihten Takibi Yap: Belirlenmiş tarihler arasında tekrarlanmasını istediğiniz bir tekrarlama metodunu buradaki kutucuğu işaretledikten sonra bilgilerini giriniz. Tolerans, periyodik bakımın kaç gün önceden iş emri sayfasında oluşturulacağı(bildiriliş tarihi) bilgisidir. Örneğin: Bakım yapılacak tarih: 15 Nisan ise ve Tolerans 3 Gün olarak belirlendiyse 12 Nisan’da iş emri sayfasında oluşur.
4) Sayaçtan Takip Yap: İşaretlenirse oluşturulan periyodik bakım artırılacak sayaçlar üzerinden takip edilir ve sayaç periyodunu geçtikten sonra devreye girer.
5) Bakım Tarihi Hesap Tipi: Eğer sabit seçilirse, oluşturulan bakımın tarihinden önce Periyodik Bakım Tanımları sayfasından bakım seçilip Yeni İş Emri Oluştur seçilerek el ile aktif edilirse, bakım periyodu erkenden bakım yapılmasına rağmen değişmez. Eğer dinamik seçilirse, el ile iş emrini oluşturduğumuzda periyodik bakım yapılacak tarih hesaplaması yenilenir.
Örnek Senaryo: 15 nisan’da yapmam gereken haftalık bakımı bir nedenden ötürü 12 nisanda gerçekleştirmek istersem;
Periyodik Bakım Tanımları sayfasına gelirim ve tanımladığım periyodik bakımı yeni iş emri oluştur seçeneğini seçerek iş emrini oluştururum. Eğer bu periyodik bakımın ayarı sabit ise bir sonraki iş emrini 15 nisanda bakımı yapmama rağmen oluşacaktır. Eğer dinamik ise, 12+7=19 Nisanda oluşacak şekilde güncellenir. Bu durumun gerçekleşmesi için iş emrinin kapanması gerekmektedir.


### 4.2) Periyodik Bakım Tanımları içerisindeki Diğer Sekmeler

- İş Emri Bilgileri
Üretim Durumu: Periyodik bakım devreye girdiğinde üretim durumu otomatik değişmesi için kullanılır.
İş Emri Türü, İş Tipi ve Bakım Önceliği, Bakım Süresi bilgilerini giriniz.
- Açıklamalar: İş Emri oluştuğunda içeride yazacak Talep açıklamasını giriniz.
- Malzemeler: Kullanılması kesin olan iş emrine otomatik olarak kayıtlı gelmesini istediğiniz malzemeyi ekleyiniz.
- Bakım Planı: Uygun bakım planını seçiniz.
- Ölçüm Paketleri: Uygun Ölçün Planı var ise ekleyiniz.
- Özel Durumlar: Periyodik bakımın aktif olmaması gereken zamanı ay bazında seçebilirsiniz.
- Bağlı Dökümanlar: Bakım ile alakalı dosya var ise ekleyebilirsiniz.


