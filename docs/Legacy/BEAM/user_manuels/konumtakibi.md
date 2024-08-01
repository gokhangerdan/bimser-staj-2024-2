# BEAM Konum Takibi

İçerik 
1. Giriş

1.1. Amaç

1.2. Kapsam

2. Modül Kullanımı:

2.1. Tanımlamalar: 

2.1.1. Sistem Tanımlamaları: 

2.2. Mobil Cihazlar Konfigürasyonları: 

2.2.1. IOS Cihazlarda Konum Bilgi Aktif Etme 

2.2.2. Android Cihazlarda Konum Bilgi Aktif Etme

2.3. Konum Bilgisinin Kullanımı ve Raporlama İçeriği: 



## 1. Giriş 

### 1.1. Amaç

Özellikle dağınık yapıda demirbaş yapısına sahip işletmelerde ekipman ister arızi ister periyodik 
bakımlar olsun bakım için çalışan personellerinin ekipmanın bulunduğu lokasyonda mı yoksa farklı 
bir noktadan mı ilgili bakım faaliyetlerini yaptıklarını kontrol edebilmek amacı ile mobil cihazlardaki 
konum bilgisinin kontrol edilmesi sağlanmıştır.

### 1.2. Kapsam 

Saha çalışması bulunan personellerin ekipmanlara bakım yaparken konum bilgilerinin saklanarak 
raporlarının alınması


## 2. Modül Kullanımı:

### 2.1. Tanımlamalar:

### 2.1.1. Sistem Tanımlamaları: 

• Beam ana menü “Varlık Yönetimi” modülü içerisinde varlıklara ait “Harita Bilgileri” ekranın üzerinde
varlık ’a ait X ve Y koordinat bilgilerinin tanımlanmış olması gerekmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/1-9f7b32f6-56ca-4146-909d-eda1a6a3d2c1.png)

• Beam ana menü içerisinde bulunan “Sistem” sekmesi tıklanır. Sonrasında “Kullanıcılar” sayfası seçilir 
ardından Kullanıcı parametreleri sekmesinden “İş Emri, Başladım/Tamamladım İşleminde Konum Bilgisini 
Kullan” seçeneği İşaretlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/2-219906cc-3d18-44d0-b228-7288c2ae4767.png)

• Beam ana menü içerisinde bulunan “Sistem” sekmesi tıklanır. Sonrasında “Kullanıcılar Grupları” 
sayfası seçilir ardından Menu yetkilerinden→Bakım Yönetimi→Raporlar→Analiz Raporları 
içerisindeki “Çalışan Personel Konum Raporu” işaretlenir ve kaydetme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3-21e6a0aa-7de6-4f4b-8faa-dc015765d9e5.png)

• Kayıt işlemi sonrasında Beam ana menü içerisindeki Bakım Yönetimi-→Raporlar→Analiz 
Raporları →”93 Çalışan Personel Konum Raporu” erişim sağlanabilir.


![](https://docsbimser.blob.core.windows.net/imagecontainer/4-c2af5a05-2e53-4426-962a-8077c587a01d.png)

### 2.2. Mobil Cihazlar Konfigürasyonları: 

### 2.2.1. IOS Cihazlarda Konum Bilgi Aktif Etme

• IOS cihazlar üzerinden konum bilgisini aktif edebilmek için Ana menü→Ayarlar kısmında arama alanına 
“Beam” yazılır. Açılan sayfada Konum işaretlenir ve konum bilgisini her zaman veya Uygulamayı 
Kullanırken seçilerek ana ekrana dönülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5-46398cb9-19bb-4de3-88f2-3cd8d2bd3fee.png)

### 2.2.2. Android Cihazlarda Konum Bilgi Aktif Etme 

• Android cihazlar üzerinden konum bilgisini aktif edebilmek için Ana menü→Uygulamalar→Uygulamalar 
kısmında “Beam” uygulaması seçilir. Açılan sayfada İzinler→Konum işaretlenir ve “Yalnızca uygulamayı 
kullanırken izin ver” seçilerek ana ekrana dönülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/6-86902eef-25a8-40fc-b2ff-d1f701bf8084.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/7-ad4f616e-2102-4a32-aae1-d2115c53037b.png)

### 2.3. Konum Bilgisinin Kullanımı ve Raporlama İçeriği: 

### 2.3.1. Mobil Uygulama Konum Bilgisi Kullanımı 

• BEAM Mobil uygulamasına giriş yapıldıktan sonra Ana menü üzerinden veya yan taraftaki menü 
ağacı üzerinden “İş Emirleri” modülüne giriş yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/8-f50849b1-5f79-4143-9ebc-fda703f18950.png)

• İş emri liste sayfasında çalışma yapılacak olan iş emirlerinden bir seçilerek ilgili iş emrinin üzerinden (long 
press) basıldığında açılan Başladım veya Tamamladım şeklinde seçimler yapıldığında mobil uygulamaya 
login olan kullanıcı ait X ve Y koordinat bilgileri sistem üzerinde kaydedilir.

• Sistem her Başladım denildiğinde başladım denilen konum bilgisi, Tamamladım dediğinde de tamamladım 
denilen konum bilgisi saklamaktadır. Varlık üzerinde tanımlı olan X ve Y koordinatlarına sistem metre 
cinsinden hesaplama yapmaktadır.


![](https://docsbimser.blob.core.windows.net/imagecontainer/9-974a1a70-140e-4dde-a012-83306cf9bed1.png)

### 2.3.2. Raporlama:

Beam ana menü içerisindeki Bakım Yönetimi-→Raporlar→Analiz Raporları →93 Çalışan Personel Konum 
Raporu ile rapor içeriğinde aşağıdaki kriterler göre raporlama yapılabilmektedir.


• Arıza Oluşma Tarihi
• Bildiriliş Tarihi
• Bitiş Tarihi
• Devreye Alma Tarihi
• İşe Başlama Tarihi
• Tamamladım Tarihi
• İş Emri No
• Çalışan Personel
• Varlık Kodu
• Varlık Tanımı
• Arıza Oluşma Tarihi
• Başlangıç Tarihi (İş Emri Başlangıç Tarihi)
• Bitiş Tarihi (İş Emri Bitiş Tarihi)
• Çalışan Personel Kodu
• Süre (Çalışan Personel Çalışma Süresi)


• Varlık Koordinat/ Başladım Mesafesi (M) 
**Varlık Konumu ile Başladım Konumu Arasındaki Uzaklık

• Varlık Koordinat/Bitirdim Mesafesi (M) 
**Varlık Konumu ile Tamamladım Konumu Arasındaki Uzaklık

![](https://docsbimser.blob.core.windows.net/imagecontainer/10-3f72b6a5-6f97-4979-ab79-6b1d97f0da84.png)

