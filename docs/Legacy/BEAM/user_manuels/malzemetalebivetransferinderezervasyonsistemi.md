# BEAM Malzeme Talebi ve Transferinde Rezervasyon Kullanımı

## 1. Giriş

### 1.1. Amaç 

Birçok şirketin en önemli maliyetlerinin başında malzeme maliyetleri yer almaktadır ve malzeme 
maliyetleri kontrol etmek birçok işletme için kolay olmamaktadır. BEAM uygulaması içerisinde bulunan 
malzeme modülü ile dağınık yapıda ve süreçlerde olan kontrol edebilir ve takip edebilirsiniz. Bu
kapsamda Malzeme Rezervasyonu fonksiyonu sayesinde bir şekilde yönetilmesine olanak sağlar.

### 1.2. Kapsam

İşletmelerin ihtiyaç duyulan malzemeler kullanımı sırasında gerek kritik stoklar gerekse de öncelikli işler 
için stok bulunan malzemelerin rezerve ederek bu türdeki işler kullanılması önem arz etmektedir. Hem
web hem de mobil uygulama ile malzeme talep ve transfer süreçlerinde rezervasyon kurallarına göre 
malzeme hareketleri oluşturmayı hedeflemektedir.

## 2. Modül Kullanımı: 

### 2.1. Tanımlamalar:

### 2.1.1. Sistem Tanımlamaları:

 Beam ana menü içerisinde bulunan “Sistem” sekmesi tıklanır. Sonrasında “Şirketler” sayfası seçilir 
ardından şirket üzerinde parametreler sekmesinde “(BC429) - Malzeme Talebi ve Transferinde 
Rezervasyon Sistemi Kullanılsın” parametresi işaretlenir. Bu parametresinin aktif olduğu durumlarda 
çıkış ve transfer işlemlerinin malzeme hareketleri üzerinden değil sadece Malzeme Talebi ve 
Transferi modülü üzerinden sürdürülmelidir. Aksi halde Malzeme Talebi ve Transferi süreçleri 
içerisinde onay akışlarında rezerve edilen malzeme miktarı ile ilgili sorunlar yaşanabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/BeamMTalepveTransferRezervarson_p1-7873706c-ba93-4f52-ab5e-5e98d6e36075.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/BeamMTalepveTransferRezervarson_p2-4a680bfa-76fa-456f-993d-142e8a6d2083.png)

### 2.2. Rezervasyon Sisteminin Kullanımı ve Kontrolleri:

### 2.2.1. Web uygulama üzerinden kullanımı

 BEAM ana menü içerisinde bulunan “Malzeme Yönetimi→Malzeme Talebi ve Transferi” sekmesi 
tıklanır. Ardından açılan Malzeme Talebi ve Transferi sayfasından Ekle denilerek yapılmak istenilen 
“Çıkış veya Transfer” hareket türlerinden biri seçilerek Malzeme Hareket sayfasına erişim sağlanılır.
**Malzeme Talebi ve Transferi sayfasında rezervasyon işlemleri Çıkış Ve Transfer Türleri Üzerinden Yapılabilmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/BeamMTalepveTransferRezervarson_p3-75a70143-a449-495e-963d-92e6b9b775ba.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/BeamMTalepveTransferRezervarson_p4-f393749d-c8e1-4b46-8c76-cf8f94a3105c.png)

Açılan çıkış veya transfer hareketi sayfasından talep edilecek malzemeleri seçmek için “Malzemeler”
sekmesinden seçilir ve Malzeme Ekle/Çoklu Seçim veya Excel’den Aktar kullanılarak istenilen 
malzemelerin eklenilmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/BeamMTalepveTransferRezervarson_p5-58311932-b500-4c36-a0a2-dc15dd2d9495.png)

 Malzeme eklenildiğin veya çoklu seçimden malzeme eklenildiğinde malzemenin hangi ambarda kaç 
adet rezerve edildiğini “Rezerve Edilen Malzeme Miktarı “ alanında görüntülenebilir. Rezerve 
edilen malzeme miktarı alanı onayda bekleyen malzeme miktarını göstermektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/BeamMTalepveTransferRezervarson_p6-b31b0ad8-a2f9-4f83-9e80-22537a79197b.png)

Malzeme ekleme sırasında (Ekle – Çoklu Seçim – Excel’den Aktar) talep miktarı sistem üzerinde rezerve 
edilebilecek miktarı aşar ise sistem ”XX Malzemesine, YY Ambarında Rezervasyon Yapılabilecek Maksimum 
Miktar: ….” şeklinde bir uyarı ile kullanıcıları bilgilendirmekte ve bu neden ile sistem belirtilen miktardan 
daha fazla malzeme eklemeye izin vermemektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/BeamMTalepveTransferRezervarson_p7-84eda94e-f48e-4184-bc53-8bbe28352276.png)

 Malzemeler eklenmesi sonrasında kaydet ile ilgili malzemeler kaydedilmeye başlanıldığın da Rezervasyon 
talebi başlatılmış olup süreç içerisindeki ilgililerin onayına gönderim sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/BeamMTalepveTransferRezervarson_p8-09006215-0f8d-4fbe-8791-51392da9b318.png)

 Malzemeler eklenip rezervasyon talebi kaydedilirken malzemelerin ilgili ambarlarında rezervasyon 
miktarlarında anlık değişiklik olur ise uyarı verilecek kayıt işlemi yapılmayacaktır. Bu durumda malzemeler 
sekmesinde ilgili malzemelerin silinip istenilen malzemelerin tekrar eklenmesi gerekmektedir. Bu durumda ilgili 
kayıt yapan kullanıcının karşına aşağıdaki gibi çıkarılan uyarı ile durum hakkında bilgilendirme yapılmaktadır. 
”Kayıt Oluşturulurken Rezerve Edilen Malzeme Miktarlarında Değişiklik Oldu. Rezervasyon İçin Yeterli 
Miktarda Malzeme (ler) Bulunmamaktadır. Lütfen Malzemeler Sekmesindeki İlgili Kayıtları Tekrar Giriniz. … 
Malzemesine, … Ambarında Rezervasyon Yapılabilecek Maksimum Miktar: …”

![](https://docsbimser.blob.core.windows.net/imagecontainer/BeamMTalepveTransferRezervarson_p9-fe2cfaf1-178c-4f1b-b36e-a4919a645fdd.png)

### 2.2.2. Beam Mobil Uygulaması Üzerinde Kullanımı 

 Mobil uygulama üzerinde menü ağacı içerisinden veya ana menü içerisinde bulunan Malzeme Talebi ve 
Transferi modülü seçilerek ilgili modüle giriş sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/BeamMTalepveTransferRezervarson_p10-22f96158-7320-4e3e-9693-97850359acaf.png)

 Malzeme Talebi ve Transferi modülünde ekle denilerek “Çıkış veya Transfer” hareket türlerinden biri
seçilerek Malzeme Hareket sayfasına erişim sağlanılır. 
**Malzeme Talebi ve Transferi sayfasında rezervasyon işlemleri Çıkış Ve Transfer Türleri Üzerinden Yapılabilmektedir

![](https://docsbimser.blob.core.windows.net/imagecontainer/BeamMTalepveTransferRezervarson_p11-2af57c1c-cdcd-417e-8497-e2d6d15cf012.png)

 Açılan çıkış veya transfer hareketi sayfasından talep edilecek malzemeleri seçmek için “Malzemeler”
sekmesinden seçilir ve Malzeme Ekle kullanılarak istenilen malzemelerin eklenilmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/BeamMTalepveTransferRezervarson_p12-5ba6f224-4db0-48e4-b501-fed87d5ee8ca.png)

 Malzeme seçilip ardından ambar seçimi yapıldığında malzemenin hangi ambarda kaç adet rezerve edildiğini 
“Rezerve Edilen Malzeme Miktarı “ alanında görüntülenebilir. Rezerve edilen malzeme miktarı alanı onayda 
bekleyen malzeme miktarını göstermektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/BeamMTalepveTransferRezervarson_p13-28843bac-bb67-4070-9a50-90c8ebb158ec.png)

Malzeme ekleme sırasında talep miktarı sistem üzerinde rezerve edilebilecek miktarı aşar ise sistem 
”XX Malzemesine, YY Ambarında Rezervasyon Yapılabilecek Maksimum Miktar: ….” şeklinde bir 
uyarı ile kullanıcıları bilgilendirmekte ve bu nedenle ile sistem belirtilen miktardan daha fazla 
malzeme eklemeye izin vermemektedir.


 Malzemeler eklenmesi sonrasında kaydet ile ilgili malzemeler kaydedilmeye başlanıldığın da 
Rezervasyon talebi başlatılmış olup süreç içerisindeki ilgililerin onayına gönderilmiş sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/BeamMTalepveTransferRezervarson_p14-01f441de-64c1-4aba-b0e2-6b43d05b3645.png)

Malzemeler eklenip rezervasyon talebi kaydedilirken malzemelerin ilgili ambarlarında rezervasyon 
miktarlarında anlık değişiklik olur ise uyarı verilecek kayıt işlemi yapılmayacaktır. Bu durumda malzemeler 
sekmesinde ilgili malzemelerin silinip istenilen malzemelerin tekrar eklenmesi gerekmektedir. Bu durumda ilgili 
kayıt yapan kullanıcının karşına aşağıdaki gibi çıkarılan uyarı ile durum hakkında bilgilendirme yapılmaktadır. 

”. … Malzemesine, … Ambarında Rezervasyon Yapılabilecek Maksimum Miktar: …”

![](https://docsbimser.blob.core.windows.net/imagecontainer/BeamMTalepveTransferRezervarson_p15-e32e3f3c-e4f9-4de7-89b0-d00da830e44c.png)

