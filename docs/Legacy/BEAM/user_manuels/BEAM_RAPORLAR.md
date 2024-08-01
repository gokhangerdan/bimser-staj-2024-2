# BEAM Raporlar

## Bakım

### Analiz Raporları

#### Varlık Tarihçe Raporu

Rapor, [varlık](#_Varlıklar) bazında gruplama yaparak ilgili [varlık](#_Varlıklar) için açılmış olan [iş emirlerini](#_İş_Emri) listeler.

Rapor filtre ekranında, [varlık](#_Varlıklar) kodu filtreleme alanına değer girilirse ve “Alt ve Üst Varlıkları Dâhil Et” seçeneği işaretlenirse ilgili rapor filtrede seçilen [varlık](#_Varlıklar) kaydına bağlı olan tüm [varlıkları](#_Varlıklar) listeler.

![Resim1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1d968957-c3b7-4e3d-bd70-ae49342a5d4d)

Rapor filtre sayfasında bulunan “Talep Açıklaması Büyüyebilir” seçeneği işaretlenirse, rapor ön izlemesinde talep açıklamasının bulunduğu sütun aşağıya göre gerektiği kadar otomatik büyüyecektir.

![Resim2](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade9c2321b-48a9-43c5-9841-7216e9c670c0)

Rapor verisi istenirse ham olarak excel ortamına aktarılabilinir. Aktarma işlemi için rapor filtre sayfasında bulunan 
![Resim3](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload85a24f3d-e877-4c83-9489-93e43d94b9fa) simgeli butona tıklamak yeterlidir.

![Resim4](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc654d7a7-a1bf-44fd-9d7e-8c1ccb5bdc40)

#### Arıza Nedenleri Analizi

En çok bakıma neden olan [arıza nedenlerinin](#_Arıza_Nedenleri) analiz edilmesi için kullanılır. Rapor arıza nedeni bazında gruplama yaparak [iş emri](#_İş_Emri) sayısı, toplam maliyet ve toplam bakım süreleri değerlerini verir.

![Resim5](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload867034c3-4238-4da7-98b7-f4d83eab942d)

#### Arıza Nedeni Bazında Arıza Nedeni Analizi

Rapor, arıza nedeni bazında gruplama yaparak bir arıza nedeni kaydının en çok tekrarladığı [varlıkları](#_Varlıklar) listeler.

Bu rapor sayesinde bir arıza nedeninin en çok tekrarladığı [varlıkları](#_Varlıklar) tespit edebilirsiniz.

![Resim6](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload00890e87-87ea-4e8d-a009-4cda0d45ddb6)

#### Varlık Bazında Arıza Nedeni Analizi

[Varlık](#_Varlıklar) bazında gruplama yaparak ilgili varlıkta en fazla meydana gelen [arıza nedenlerini](#_Arıza_Nedenleri) listeler.

Bu rapor sayesinde bir [varlık](#_Varlıklar) kaydında en çok bakıma neden olan arızaları analiz edebilirsiniz.

![Resim7](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7365aca1-0f47-4ea8-b12d-801ab358c707)

#### Varlıklarda En Çok Tekrarlayan Arıza Nedenleri

Bu rapor, [arıza nedenlerini](#_Arıza_Nedenleri) [varlıklarda](#_Varlıklar) tekrarlama sayılarına göre sıralayarak, gruplama yapmadan, en çok tekrarlayandan en az tekrarlayana göre listeler.

Bu rapor sayesinde [varlık](#_Varlıklar) bazında en çok tekrarlayan [arıza nedenlerini](#_Arıza_Nedenleri) analiz edebilirsiniz.

![SNAGHTML15056056.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5311d405-ebd7-4004-acc7-028c91213003)

#### İş Emri Takip Formu

Sistemde bulunan [iş emirlerinin](#_İş_Emri) özet bilgisinin yeraldığı bir rapordur.

![SNAGHTML1ab28d4d.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc5bb0aa6-91c1-446a-b5f6-c08e99cc02f8)

#### Personel Performans Analizi

Bakımda çalışan [personellerin](#_Kaynaklar_/_Personeller) performansının ölçüldüğü rapordur. Raporun esas amacı [personelin](#_Kaynaklar_/_Personeller) çalışması gereken sürenin ne kadarının bakımda harcadığının tespit edilmesidir.

Rapor filtresinde [personellerin](#_Kaynaklar_/_Personeller) çalışması gerektiği süre hesaplanırken;

-   Tatil günlerinin hesaplamadan çıkarılması isteniyorsa “Şirket Hafta Sonlarını Toplam Mesaiden Çıkar” seçeneği işaretlenmelidir.
-   Şirketin çalışmadığı özel günlerin hesaplamadan çıkartılması isteniyorsa “Şirket Özel Günlerini Toplam Mesaiden Çıkar” seçeneği işaretlenmelidir.
-   [Personellerin](#_Kaynaklar_/_Personeller) çalışmadığı ya da izinli oldukları günlerin hesaplamadan çıkartılması isteniyorsa “Personellerin Çalışmadığı Günleri Toplam Mesaiden Çıkar” seçeneği işaretlenmelidir.

![SNAGHTML1ab84a64.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9929987e-b5d1-4c77-b3e3-8cc29d4e677f)

#### Mesai (Vardiya) Detaylı Personel Performans Raporu

Bakımda çalışan [personellerin](#_Kaynaklar_/_Personeller) performansının ölçüldüğü rapordur.Personel Performans Raporundan farklı olarak personellerin vardiya bazında çalışma süreleri gösterilmektedir.

Rapor filtresinde [personellerin](#_Kaynaklar_/_Personeller) çalışması gerektiği süre hesaplanırken;

-   Tatil günlerinin hesaplamadan çıkarılması isteniyorsa “Şirket Hafta Sonlarını Toplam Mesaiden Çıkar” seçeneği işaretlenmelidir.
-   Şirketin çalışmadığı özel günlerin hesaplamadan çıkartılması isteniyorsa “Şirket Özel Günlerini Toplam Mesaiden Çıkar” seçeneği işaretlenmelidir.
-   [Personellerin](#_Kaynaklar_/_Personeller) çalışmadığı ya da izinli oldukları günlerin hesaplamadan çıkartılması isteniyorsa “Personellerin Çalışmadığı Günleri Toplam Mesaiden Çıkar” seçeneği işaretlenmelidir.

![SNAGHTML70924c6.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload46d7f489-f97f-4c51-a472-23d3e54ce398)

#### Personel Çalışma Süreleri Raporu

Bakım [personelinin](#_Kaynaklar_/_Personeller) [iş emirlerinde](#_İş_Emri) çalıştığı sürelerin gösterildiği rapordur.

Rapor [personel](#_Kaynaklar_/_Personeller) bazında gruplama yaparak [iş emri](#_İş_Emri) detay bilgisini vermektedir.

![SNAGHTML1abe9a96.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb2c88983-c375-4ee1-984a-bcbc45fb1a08)

#### İş Emri Türlerinin İş Tiplerine Dağılımı

Rapor, hangi [iş tipinde](#_İş_Tipleri) hangi [iş emri türüne](#_İş_Emri_Türleri) ait kaç adet [iş emri](#_İş_Emri) açıldığını ve bu [iş emirlerindeki](#_İş_Emri) toplam bakım süresi ile kapatılma oranlarını vermektedir.

Rapor [iş tipi](#_İş_Tipleri) bazında gruplama yapıp detay bilgide de ilgili [iş tipi](#_İş_Tipleri) için oluşturulan [iş emirlerinin](#_İş_Emri), [iş emri türlerini](#_İş_Emri_Türleri) gruplayarak listelemektedir.

![SNAGHTML1abfbe4b.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8e6ff789-2d23-4d1f-9179-6427610760ce)

#### Açık İş Emirlerinin Varlıklara Dağılımı

Açık durumda bekleyen [iş emirlerinin](#_İş_Emri) [varlık](#_Varlıklar) bazında listelenebildiği rapordur.

Rapor, [varlık](#_Varlıklar) bazında gruplama yapıp açık [iş emirlerini](#_İş_Emri) detay kısımda listelemektedir.

![SNAGHTML1ac33c9e.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload953e2396-7293-4639-bae1-f2c192d76eb8)

#### Varlık Bazında Bakım Değerlendirme Raporu

[Varlık](#_Varlıklar) için yapılan bakımları ve bu bakımlarda gerçekleşen iş tiplerinin listelendiği rapordur.

![SNAGHTML1ac5feb5.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8a6d3179-2e74-4c10-b2c2-4637136c3a76)

#### Bakım / Arıza Kodu Bazında Bakım Değerlendirme Raporu

Bakım / Arıza kodu bazında toplam sürelerin, sayılan ve maliyetlerin verildiği rapordur.

![SNAGHTML1afaa2e0.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload81a10d77-451f-44b6-833c-5c39da2cbc91)

#### Kısım Bazında Bakım Durum Raporu

[Kısım](#_Kısımlar) bazında hangi [iş emri türünden](#_İş_Emri_Türleri) kaç adet [iş emri](#_İş_Emri) açıldığı ve bunların durumlara göre toplamlarının verildiği rapordur.

Bu raporda [kısım](#_Kısımlar) ve [iş emri türü](#_İş_Emri_Türleri) bazında toplam müdahale zamanı da verilmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6ebf76b7-fc4d-4767-9caf-ef32ea57abf7)

#### Bakım Özeti

Yapılan bakımlar ile ilgili excel formatında bilgi veren bir rapordur.

Bu raporda verilen bilgiler (excel sayfaları) şu şekildedir;

-   Personel İş Yükü
-   Bildirilen Arıza
-   İş Emri Kapatma Süreleri
-   Birim İş Hacmi
-   Tespit Edilen Arıza
-   Arıza Noktalarına Göre İş Yükü
-   [Arıza Çözümü](#_Arıza_Çözümleri)

#### Kısım Bazında MTBF Raporu

[Kısım](#_Kısımlar) bazında MTBF ve MTTR değerlerinin alındığı rapordur.

Rapor filtre ekranında girilen “Günlük Çalışma Saati” değeri rapora etki eden her bir [varlığın](#_Varlıklar) günlük çalışma süresidir.

“Ayda Ortalama Çalışılmayan Gün Sayısı” alanına ise [varlıkların](#_Varlıklar) ayda çalışmadığı gün sayısı girilmektedir.

![SNAGHTML1b2b1a61.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload212c1a6f-10be-4915-a46d-90fd8fa9f866)

#### Varlık Bazında Aylık MTBF

[Varlık](#_Varlıklar) bazında MTBF ve MTTR değerlerinin aylık olarak alındığı rapordur.

Rapor filtre ekranında girilen “Günlük Çalışma Saati” değeri rapora etki eden her bir [varlığın](#_Varlıklar) günlük çalışma süresidir.

“Ayda Ortalama Çalışılmayan Gün Sayısı” alanına ise [varlıkların](#_Varlıklar) ayda çalışmadığı gün sayısı girilmektedir.

![SNAGHTML1b2cddb0.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1d700c3d-f34c-42df-8ee2-cfa5421cb1d7)

#### Bakım Noktalarına Göre İş Emri Analizi

İş emri içerisinde girilen bakım noktalarının analizinin yapıldığı rapordur.

Rapor, bakım noktası bazında gruplama yaparak detay bölümde ilgili [iş emirlerini](#_İş_Emri) listelemektedir. Bu sayede bir bakım noktasına yapılan bakımlar analiz edilebilinir.

![SNAGHTML1b401505.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadde8c2804-1470-4a33-a18a-a4107c3a9f44)

#### Varlık Bazında Bakım Noktaları Analizi

Bir [varlık](#_Varlıklar) üzerinde bulunan bakım noktalarına yapılan bakımların analiz edilmesi için kullanılır.

Rapor, [varlık](#_Varlıklar) bazında gruplanır ve detay bölümde [iş emri](#_İş_Emri) genel bilgileri ile bakım yapılan noktaların bilgisi yer alır.

![SNAGHTML1b415b09.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc78c78e5-ef4e-4076-975c-a4018074dc9b)

#### Varlık Bazında Bakım Noktası Özeti

Detay bilgi olmadan [varlık](#_Varlıklar) üzerinde bulunan bakım noktalarına yapılan bakımların analiz edildiği rapordur.

![SNAGHTML1b433b0b.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7adcc39f-fd4c-470a-8163-d38179fc65c4)

#### En Çok Kullanılan Bakım Noktaları

Rapor, en çok bakım yapılan bakım noktalarını [varlık](#_Varlıklar) bazında listeler.

![SNAGHTML1b455bc5.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8c622084-09d5-4ce7-bab3-3eb47011be9c)

#### Varlık Sökme / Takma Raporu

İş emri içerisinde yapılan [varlık](#_Varlıklar) sökme/takma işlemlerinin listelendiği ve analiz edildiği rapordur.

Bu rapor sayesinde [varlıkların](#_Varlıklar) dolaşma tarihçesi de analiz edilebilinir.

![SNAGHTML1b4b84a8.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc1a72a10-9762-400a-9d44-cf2cd7e03df0)

#### İş Günlüğü Raporu

İş emri içerisinde “İş Günlüğü” sekmesinde girilen değerlerin raporlanması ve analizi için kullanılır.

![SNAGHTML1b4d86ab.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload25e85afd-9246-41b0-8eff-7473879f1091)

#### İş Emri Sayıları ve Oranları

Bu rapor [iş emri](#_İş_Emri) sayıları ve oranlarını, filtre sayfasında seçilen “Grup Kodu” seçeneğine göre gruplayarak listelemektedir.

Bu raporda kullanılabilecek grup kodları şöyledir;

-   [Bakım / Arıza Kodu](#_Bakım_/_Arıza)
-   [Sarf Yeri](#_Sarfyerleri)
-   [Kısım](#_Kısımlar)
-   [Arıza Nedeni](#_Arıza_Nedenleri)
-   [İş Tipi](#_İş_Tipleri)
-   [İş Emri Türü](#_İş_Emri_Türleri)
-   Ay

![SNAGHTML1b51d6cd.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload57443c76-3a34-4a0f-b17c-5aba1f10aa40)

#### Arıza Giderme Süreleri

Açılan [iş emirlerinin](#_İş_Emri) kapatılma sürelerinin gün bazında analiz edildiği rapordur.

Gün periyotları şu şekildedir;

-   1\. Günde Giderilen Arızalar
-   2-5 Günde Giderilen Arızalar
-   6-10 Günde Giderilen Arızalar
-   11-30 Günde Giderilen Arızalar
-   30 Günden Uzun Süren Arızalar
-   İlk Üç Günde Giderilen Arızalar

![SNAGHTML1b52e35b.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb5834102-10f1-4462-9554-463577652f4c)

#### İş Emri Kapatma Günleri Oranı

İş emirlerinin gün bazında açık kalma sürelerinin [iş emri türüne](#_İş_Emri_Türleri) göre sayılarının analiz edildiği rapordur.

![SNAGHTML1b56d567.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload49989c10-91b3-4134-b4ba-b537fa1f4c71)

#### Fiili ve Standart Ortalama Bakım Süreleri Karşılaştırma

İş emrinde oluşan bakım sürelerinin, standart bakım süresi ile karşılaştırıldığı rapordur.

Rapor [varlık](#_Varlıklar) bazında gruplama yapıp detay bölümünde de bakım / arıza kodu bazında ortalama değerleri karşılaştırmaktadır.

![SNAGHTML1b58b78b.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload91ee4f7b-e81f-4cba-8d31-829259212991)

#### Fiili ve Azami Müdahale Süreleri Karşılaştırma

Fiili olarak bakıma başlama (müdahale) süresinin, [varlık](#_Varlıklar) üzerinde tanımlı olan azami müdahale süresi ile karşılaştırıldığı rapordur.Rapor, [varlık](#_Varlıklar) bazında listelenmektedir.

![SNAGHTML1b5b3532.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcc3abea1-3e27-4889-810e-27ca0d837bcd)

#### Fiili ve Standart Ortalama İşçilik Süreleri Karşılaştırma

İş emrinde oluşan işçilik sürelerinin, standart bakım süresi ile karşılaştırıldığı rapordur.

Rapor [varlık](#_Varlıklar) bazında gruplama yapıp detay bölümünde de bakım / arıza kodu bazında ortalama değerleri karşılaştırmaktadır.

![SNAGHTML1b5e71e4.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadca52c3d5-fa45-4811-8f20-9fb36b702ee4)

#### Aylık Servis Raporu

Aylık bazda gruplama yaparak [iş emirlerinin](#_İş_Emri) [hizmet](#_Hizmetler) bilgilerinin ve maliyetlerinin analiz edilmesi için kullanılan rapordur.

Rapor, ay bazında gruplama yaptıktan sonra detay bölümünde ilgili aya ait bakım yapılan [varlıkları](#_Varlıklar) ve ilgili [varlık](#_Varlıklar) için verilen veya alınan [hizmetleri](#_Hizmetler) listeler.

![SNAGHTML1b5fbbde.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload71b4d8c7-fc14-46b8-b993-77ac87bdea83)

#### Varlık Bazında Aylık İş Emri Sayıları

[Varlık](#_Varlıklar) bazında aylık açılan [iş emri](#_İş_Emri) sayılarının analiz edildiği rapordur. Raporda her [varlık](#_Varlıklar) için bir önceki yıla ait ortalama [iş emri](#_İş_Emri) sayısı da verilmektedir.

![SNAGHTML1b62a024.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0add8b67-3f56-40f9-a77f-7296120d0f44)

#### Arıza Nedeni Bazında Duruş Analizi

Duruş olan [iş emirlerin](#_İş_Emri)in arıza nedeni bazında analizinin yapıldığı rapordur.

![C:\\Users\\aanac\\AppData\\Local\\Temp\\SNAGHTML71f1cfa.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada0fb7257-92ee-4d13-8f08-c8d9525f808f)

#### Duruş Sınıf Listesi Detay

Duruş olan [iş emirlerindeki](#_İş_Emri) [duruş sınıf](#_Duruş_Sınıfları) analizinin yapıldığı rapordur.

![SNAGHTML1b68f40e.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6f9c4053-e47d-4ad0-85d9-4bf29f7a7d05)

#### Duruş Sınıf Listesi (Özet)

[Duruş sınıfı](#_Duruş_Sınıfları) bazında [iş emri](#_İş_Emri) sayılarının ve genele oranlarının listelendiği rapordur.

![SNAGHTML1b7edcd7.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload619031cd-ed03-4fbf-96fd-b07e0193715e)

#### Neden Analizi Aksiyon Listesi

İş emrine bağlı oluşturulan aksiyon [iş emirlerinin](#_İş_Emri) listelendiği excel tabanlı rapordur.

![SNAGHTML1b9169ca.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload079e9461-b5d8-42ed-9778-9bc66bc6ff67)

#### İş Emri Grup Özellikleri Listesi

[Varlık](#_Varlıklar) kayıtlarında bulunan grup özelliklerine, iş emirleri içerisinde atanan grup özellik değerlerinin listelendiği rapordur.

Rapor [iş emri](#_İş_Emri) bazlı listeleme yapıp detayında grup özellik değerlerini göstermektedir.

![SNAGHTML1b968e3b.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadba4990e9-7dea-49a9-a75c-31849c62b625)

#### İş Emri Excel Listesi

İş emirlerinin liste olarak gösterildiği excel tabanlı rapor.

![SNAGHTML1b9c864f.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8fb1a0dc-cc04-4126-9005-f0345dff12e4)

#### İş Emri Süreleri Raporu

İş emri içerisinde oluşan sürelerin, [iş emri](#_İş_Emri) bazında listelendiği rapordur.

![SNAGHTML1ba21f72.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload05691c4a-bbcb-4550-a7f5-8d2dfed4ab9e)

#### Kullanıcının İş Emri ve İş Talebi Sayıları Analizi

Kullanıcıların oluşturdukları [iş emri](#_İş_Emri) ve [iş talebi](#_İş_Talebi) sayılarının listelendği rapordur.

Raporda [iş emri](#_İş_Emri) ve [iş talebi](#_İş_Talebi) ile ilgili sayıların dışında kullanıcının oturum açma sayıları da verilmektedir.

![SNAGHTML1ba655fd.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0ee6103d-0c74-469d-aea0-b87b15f66171)

#### Kullanıcı Bazlı İş Talebi ve İş Emri Sayıları Analizi

Kullanıcı bazında, açılan [iş emri](#_İş_Emri) ve [iş taleplerinin](#_İş_Talebi) gruplanarak listelendiği rapordur.

Bu rapor sayesinde bir kullanıcının kaç adet MEKANİK BAKIM iş tipli talepte bulunduğu analiz edilebilinir.

Rapor gruplama türü, filtre sayfasında bulunan “Grup Kodu” başlıklı alanda belirlenir.

Raporda kullanılabilecek gruplama türleri şu şekildedir;

-   [Bakım / Arıza Kodu](#_Bakım_/_Arıza)
-   [Sarf Yeri](#_Sarfyerleri)
-   [Kısım](#_Kısımlar)
-   [Arıza Nedeni](#_Arıza_Nedenleri)
-   [İş Tipi](#_İş_Tipleri)
-   [İş Emri Türü](#_İş_Emri_Türleri)
-   Ay

![SNAGHTML1bad3ed5.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload94fea51b-412f-4595-8303-9b265b10678a)

#### Kullanıcı Bazında İş Emri Listesi

Kullanıcı bazında gruplama yaparak detay kısmında ilgili kullanıcının oluşturmuş olduğu [iş emirlerinin](#_İş_Emri) listelendiği rapordur.

![SNAGHTML1bbf02cf.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload62f62653-cc80-41aa-8486-ddea92fd9d16)

#### İş Emri Kapatma Performansı Detayı

İş emirlerinin açık kaldığı gün sayısının listelendiği rapordur.

![SNAGHTML1bb128a6.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb098fdc4-e125-4581-b98b-b03ecb681038)

#### Süreç Performansı

Bakım sürecinin performansının ölçülmesinde kullanılan rapordur.

Rapor alınmadan önce filtre sayfasında bazı parametrelerin girilmesi gerekir. Bu parametreler şu şekildedir;

-   **Varlık Çalışma Süresi (Günlük):** Dakika cinsinden bir [varlığın](#_Varlıklar) günlük çalışma süresidir.
-   **Çalışılan Gün Sayısı:** Rapor tarih aralığında işletmenin çalıştığı gün sayısıdır.
-   **Toplam Varlık Sayısı:** Hesaplamalarda kullanılacak toplam [varlık](#_Varlıklar) sayısıdır. Sıfır (0) bırakılması durumunda uygulama kendisi [varlık](#_Varlıklar) sayısını hesaplar.
-   **Toplam Kritik Varlık Sayısı:** Hesaplamalarda kullanılacak toplam kritik [varlık](#_Varlıklar) sayısıdır. Sıfır (0) bırakılması durumunda uygulama kendisi kritik [varlık](#_Varlıklar) sayısını hesaplar.
-   **Kritik Varlık Önceliği:** Kritik olarak işaretlenmiş olan [varlıkların](#_Varlıklar) öncelik değerleridir. Uygulama bu şekilde kritik [varlıkları](#_Varlıklar) tespit etmektedir.
-   **Periyodik Bakım İş Emri Türü:** [Periyodik bakım](#_Periyodik_Bakım_Tanımlama) [iş emri](#_İş_Emri) için belirlenmiş olan [iş emri türü](#_İş_Emri_Türleri) kodudur.

![SNAGHTML1bb70040.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8c371197-3c45-42f9-a571-e41c4217873f)

#### Kullanıcı Bazında İş Talebi Doğruluk Analizi

Kullanıcının açmış olduğu taleplerdeki [iş emri türü](#_İş_Emri_Türleri), [iş tipi](#_İş_Tipleri) ve [bakım / arıza kodu](#_Bakım_/_Arıza) değerlerinin [iş emrindeki](#_İş_Emri) değişme oranıdır.

Bu rapor kullanıcının ne doğrulukta talepte bulunduğunun analiz edilmesinde kullanılır.

![SNAGHTML1bc15c44.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9fc5ca8c-8a64-4ebe-b536-46aabb6242d8)

### Mesai (Vardiya) Raporları

#### Mesai (Vardiya) Listesi Raporu

[Varlık grubu](#_Varlık_Grupları) bazında günlük olarak yapılan işlerin listesinin alınabileceği rapordur.

![SNAGHTML1c2bf163.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload681aded8-ddf7-435b-bdbd-d77415e28a6a)

#### Mesai (Vardiya) Raporu

[Kısım](#_Kısımlar) kodu bazında günlük yapılan işlerin listesinin alınabileceği rapordur.

![SNAGHTML1c2d5959.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload81663e67-a51b-410f-b3f1-2e9b068320be)

#### Mesai (Vardiya) Raporu Ölçüm Değerli

Günlük yapılan işlerin ölçüm detaylı olarak listesinin alınabileceği rapordur.

![SNAGHTML1c2f0a12.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb55b495f-eb26-4d1f-8c72-717290f3e33e)

#### Tarih Bazında Detaylı Mesai (Vardiya) Raporu

Günlük yapılan işlerin, yapılan işin açıklaması ve çalışan [personel](#_Kaynaklar_/_Personeller) detayını içerecek şekilde listesinin alınabileceği rapordur.

![SNAGHTML1c30e42a.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc0e4374b-e9e6-41ec-91a7-c3db3c3bedcd)

#### Günlük Mesai (Vardiya) Raporu

Günlük olarak, yapılan işlerin detaylı bir şekilde listesinin alınabileceği rapordur.

Bu raporun içeriğinde [iş emrinin](#_İş_Emri) açıldığı [varlık](#_Varlıklar) kaydının üst sahip [varlık](#_Varlıklar) kaydı bilgisi de mevcuttur. Rapor filtre sayfasında tarih ve saat birleştirilerek filtreleme yapılabilmektedir. Bu sayede bir [vardiyada](#_Mesailer) yapılan işlerin analizinde de kullanılabilinir.

![SNAGHTML1c32a132.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload14b2874c-dd1e-4e81-8d5e-f978ef09a7f7)

#### Haftalık Mesai (Vardiya) Raporu

Yapılan bakımların haftalık bazda detaylı listesinin alınabildiği rapordur.

Bu raporun içeriğinde [iş emrinin](#_İş_Emri) açıldığı [varlık](#_Varlıklar) kaydının üst sahip [varlık](#_Varlıklar) kaydı bilgisi de mevcuttur. Rapor filtre sayfasında tarih ve saat birleştirilerek filtreleme yapılabilmektedir. Bu sayede bir [vardiyada](#_Mesailer) yapılan işlerin analizinde de kullanılabilinir.

![SNAGHTML1c33da99.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload06824b67-523f-4839-a326-1b1eee34438b)

#### Üst Varlık Bazında Mesai (Vardiya) Raporu

Günlük olarak, yapılan işlerin detaylı bir şekilde listesinin alınabileceği rapordur.

Bu raporun içeriğinde [iş emrinin](#_İş_Emri) açıldığı [varlık](#_Varlıklar) kaydının üst sahip [varlık](#_Varlıklar) kaydı bilgisi de mevcuttur. Rapor verisi ham olarak, filtre sayfasında bulunan excel’e aktarma butonu ile dış ortama aktarılabilinir.

![SNAGHTML1c34f837.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload83e0c123-7c18-45b1-90ee-2256cffc4165)

### Koruyucu Bakım Raporları

#### Koruyucu Bakım Listesi

[Periyodik bakım](#_Periyodik_Bakım_Tanımlama) tanımlarının listesinin alınabileceği rapordur.

![SNAGHTML1c50d1c4.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2feec12e-5695-49d5-a5cc-307dcba17675)

#### Günlük Koruyucu Bakım Raporu

[Varlık](#_Varlıklar) bazında [periyodik bakım](#_Periyodik_Bakım_Tanımlama) planının günlük olarak listelendiği rapordur.

Rapor, [varlık](#_Varlıklar) bazında gruplama yaparak ilgili [varlık](#_Varlıklar) için hangi ayın hangi gününde [periyodik bakım](#_Periyodik_Bakım_Tanımlama) yapılması gerektiğini detay kısmında listelemektedir.

Bu rapordaki tarihler, bakımların zamanında yapılacağını kabul ederek bakım periyotlarına göre hesaplanmaktadır. Sayaçtan takip edilen bakımların hangi tarihte bakım sayaçlarının dolacağı bilinemediğinden rapor içerisinde görünmemektedirler.

![SNAGHTML1c51a670.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbad81a44-6939-4a0f-831f-9e7c974e54ae)

#### Haftalık Koruyucu Bakım Planı

[Varlık](#_Varlıklar) bazında [periyodik bakım](#_Periyodik_Bakım_Tanımlama) planının haftalık olarak listelendiği rapordur.

Rapor, [varlık](#_Varlıklar) bazında gruplama yaparak ilgili [varlık](#_Varlıklar) için hangi haftalarda [periyodik bakım](#_Periyodik_Bakım_Tanımlama) yapılması gerektiğini detay kısmında listelemektedir.

Bu rapordaki haftalar, bakımların zamanında yapılacağını kabul ederek bakım periyotlarına göre hesaplanmaktadır. Sayaçtan takip edilen bakımların hangi tarihte bakım sayaçlarının dolacağı bilinemediğinden rapor içerisinde görünmemektedirler.

![SNAGHTML1c569a9e.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc5ec35d1-c281-47b4-84ca-de8ccfb94645)

#### Günlük Bazda Gerçekleşecek Periyodik Bakım Sayıları Raporu

Hangi hafta gününe kaç adet [periyodik bakımın](#_Periyodik_Bakım_Tanımlama) denk geldiğinin listelendiği rapordur. Rapor [iş emri türü](#_İş_Emri_Türleri) bazında gruplama yaparak bu bilgiyi vermektedir.

Sayaçtan takip edilen bakımların hangi tarihte bakım sayaçlarının dolacağı bilinemediğinden rapor içerisinde görünmemektedirler.

![SNAGHTML1c60e582.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0ea918f5-b09b-4088-9832-f6e582a699bd)

#### Haftalık Bazda Gerçekleşecek Periyodik Bakım Sayıları Raporu

Hangi haftaya kaç adet [periyodik bakımın](#_Periyodik_Bakım_Tanımlama) denk geldiğinin listelendiği rapordur. Rapor [iş emri türü](#_İş_Emri_Türleri) bazında gruplama yaparak bu bilgiyi vermektedir.

Sayaçtan takip edilen bakımların hangi tarihte bakım sayaçlarının dolacağı bilinemediğinden rapor içerisinde görünmemektedirler.

![SNAGHTML1c63b204.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadddfc1230-661c-4741-ab97-7bf930ccfdad)

#### Aylık Bazda Gerçekleşecek Periyodik Bakım Sayıları Raporu

Hangi aya kaç adet [periyodik bakımın](#_Periyodik_Bakım_Tanımlama) denk geldiğinin listelendiği rapordur. Rapor [iş emri türü](#_İş_Emri_Türleri) bazında gruplama yaparak bu bilgiyi vermektedir.

Sayaçtan takip edilen bakımların hangi tarihte bakım sayaçlarının dolacağı bilinemediğinden rapor içerisinde görünmemektedirler.

![SNAGHTML1c64d5ca.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfde2fef9-ab7d-4096-8c1e-d222de3d437f)

#### Periyodik Bakım Planları

[Periyodik bakım](#_Periyodik_Bakım_Tanımlama) tanımlarında kullanılan [bakım planlarının](#_Bakım_Planları) adımları ile beraber listelendiği rapordur.

![SNAGHTML1c6703db.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload979ae1eb-ca69-4295-bc85-bb4939b539da)

#### Periyodik Bakım İhtiyaç Planlaması

Yapılacak [periyodik bakımlarda](#_Periyodik_Bakım_Tanımlama), hangi [malzemelere](#_Malzemeler) ve hangi kaynak sınıfına ait [personellerden](#_Kaynaklar_/_Personeller) kaç adam/saatlik ihtiyaç olduğuna dair ihtiyaç belirleme raporudur.

Rapor ihtiyaç olunan miktarların yanında mevcut miktarları da göstermektedir.

![SNAGHTML1c6aea15.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6f7f6c92-cea9-4ab8-9aae-224a59344d26)

#### Ölçüm Değerleri Analiz Raporu

İş emirlerinde [ölçüm paketi](#_Ölçüm_Paketleri) kullanılarak yapılan ölçümlerin aylık zaman dilimlerinde çizelge olarak alındığı excel tabanlı rapordur.

![SNAGHTML2590f3e4.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade9d3aaa9-4e98-4615-a133-5cba24e8543c)

#### Ölçüm Değerleri Analizi (Grafikli)

Tek bir [varlık](#_Varlıklar) için, [iş emirlerinde](#_İş_Emri) [ölçüm paketi](#_Ölçüm_Paketleri) kullanılarak yapılan ölçümlerdeki değerlerin analiz edildiği excel tabanlı rapordur.

Rapor hazırlama sayfasında, raporun hangi [varlık](#_Varlıklar) için çalıştırılacağı belirtilmelidir.

![SNAGHTML25941089.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1f2bd659-95f7-4906-bd62-a8dc81c5e45b)

[Varlık](#_Varlıklar) seçildikten sonra, ilk sekmenin alt bölümünde [varlık](#_Varlıklar) ile ilgili daha önce ölçümlerde kullanılan [ölçüm paketleri](#_Ölçüm_Paketleri) listelenir.

Rapor içerisinde referans değerlerinin de olması isteniyorsa, referans değerleri ile ilgili seçenekler işaretlenmelidir.

![SNAGHTML2598debf.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8e4e3e9e-f63e-4b45-96a0-231a84eff3fd)

Rapor içerisinde yer alacak [ölçüm paketleri](#_Ölçüm_Paketleri), satır içerisinde bulunan seçme kutucuğu işaretlenerek seçilmelidir.

![SNAGHTML2596914c.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4de89eee-5de3-499d-abdb-e13dcaa6efc9)

![SNAGHTML259a3c98.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload22306b73-7bc1-47f3-b6e7-7ddca6863f8c)

#### Planlanan Ölçüm Değerleri

[Periyodik bakım](#_Periyodik_Bakım_Tanımlama) tanımlarında ilişkilendirilen [ölçüm paketlerini](#_Ölçüm_Paketleri) temel alarak, gelecek zamanlarda [periyodik bakım](#_Periyodik_Bakım_Tanımlama) [iş emirleri](#_İş_Emri) içerisinde yapılacak ölçüm işlemlerini listeleyen excel tabanlı rapordur.

![SNAGHTML259bfa4b.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1dfd7125-a245-4d5d-a0eb-de2ddec927cb)

#### Ölçüm Değerli İş Emirleri

[Ölçüm paketi](#_Ölçüm_Paketleri) kullanılarak ölçüm yapılan [iş emirlerinin](#_İş_Emri) ölçüm değerleri ile beraber liste halinde verildiği excel tabanlı rapordur.

![SNAGHTML259de055.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcd36c29e-8a93-4fef-b8c5-7c56d3ed18a7)

#### Periyodik Bakım Performans Raporu

[Periyodik bakımların](#_Periyodik_Bakım_Tanımlama), tanımlarına uygun olarak zamanında oluşturulma ve bakımın yapılıp yapılmadığının takip edildiği, gecikmelerin analiz edildiği rapordur.

![SNAGHTML1c7356eb.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada9b2225b-d0da-4970-a8d1-299b0b1ab311)

### Maliyet Raporları

#### Bakım Maliyetleri

Bakımlarda oluşan maliyetlerin [varlık](#_Varlıklar) bazında gruplanarak ve [iş emri](#_İş_Emri) detaylı şekilde listelendiği rapordur.

Grup toplamı olarak [varlıkların](#_Varlıklar) toplam maliyet bilgisi de alınabilinir.

![SNAGHTML1c757d9d.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7755cfb1-6d33-429f-a8fc-816ba874fbf1)

#### Varlıkta Kullanılan Malzemeler

[Varlık](#_Varlıklar) için bakım sırasında kullanılan [malzemelerin](#_Malzemeler) ve maliyetlerinin listelendiği rapordur.

Rapor, [varlık](#_Varlıklar) bazında gruplama yaparak detay bölümünde ilgili [varlık](#_Varlıklar) için kullanılan [malzemeleri](#_Malzemeler) [iş emri](#_İş_Emri) bilgisi ile beraber listeler.

![SNAGHTML1c78123d.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload21ea0794-221d-41ff-94f4-66e01843eab4)

#### Malzeme Kullanım Raporu

Hangi [malzemeden](#_Malzemeler) bakımlarda kaç adet kullanıldığının ve toplam maliyetinin listelendiği rapordur.

![SNAGHTML1c78d0ac.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcd0e9346-6821-4cea-9bcf-759cfbfad919)

#### Sarf Yeri Maliyet Raporu

[Sarf yeri](#_Sarfyerleri) bazında, bakımlar sırasında oluşan toplam maliyet ile [sarf yerinin](#_Sarfyerleri) bütçesinin karşılaştırıldığı rapordur.

![SNAGHTML1c79c556.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4505b6e0-ae85-4e4b-a4d1-4826b5689f1d)

#### Aylık Maliyet Raporu

Aylık bazda [iş emrinde](#_İş_Emri) oluşan her tür maliyetin ([hizmet](#_Hizmetler), işçilik, [malzeme](#_Malzemeler) ve [personel](#_Kaynaklar_/_Personeller)) tek tek listelendiği rapordur.

![SNAGHTML1c7a91e8.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload728f0969-cd09-4cc8-aeb5-5d0ea4d66f29)

#### Varlık Maliyet ve Yenileme Maliyet Oranı Raporu

[Varlık](#_Varlıklar) bazında oluşan bakım maliyetlerinin listelendiği ve [varlık](#_Varlıklar) satın alma fiyatına oranlandığı rapordur.

Bu rapor analiz edilerek ilgili [varlığın](#_Varlıklar) hurdaya ayrılıp ayrılmayacağına karar verilebilinir.

![SNAGHTML1c7b77f2.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7014a654-adec-41f3-9c4d-2319c11c93a5)

#### Malzeme Kullanım Raporu (Detay)

[Malzeme](#_Malzemeler) bazında gruplama yapılarak, ilgili [malzemenin](#_Malzemeler) hangi iş emirlerinde kullanıldığının listelendiği rapordur.

[Malzeme](#_Malzemeler) bazında dip toplam verilerek, toplam [malzeme](#_Malzemeler) maliyeti de görülebilinir.

![SNAGHTML1c7c4510.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload63ac0e46-b25b-48a3-adc0-7c29cac9b05a)

#### Varlık Maliyet ve Yenileme Maliyet Oranı Raporu (İş Emri Türü Karşılaştırmalı)

[Varlık](#_Varlıklar) bazında oluşan bakım maliyetlerinin listelendiği ve [varlık](#_Varlıklar) satın alma fiyatına oranlandığı rapordur. Bu raporda maliyet bilgileri istenilen iki adet [iş emri türüne](#_İş_Emri_Türleri) göre karşılaştırılmalı verilmektedir.

Rapor içerisinde karşılaştırmalı olarak verilecek iki adet [iş emri türü](#_İş_Emri_Türleri), rapor filtre sayfasında belirlenmektedir.

Bu rapor analiz edilerek ilgili [varlığın](#_Varlıklar) hurdaya ayırılıp ayırılmayacağına karar verilebilinir.

![SNAGHTML1c7d6be1.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6e92f18d-3dcb-4c8f-b6b4-37732e2e68e9)

#### Varlık Bazında Üretim Duruş Maliyeti

Varlık, bakım sırasında veya arızaya geçerek durduğu zaman üretim kaybından dolayı oluşan maliyetlerin [varlık](#_Varlıklar) bazında listelendiği rapordur.

![SNAGHTML1c7f4cae.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6cf95b86-1c57-446f-bc93-53701d25f9ae)

#### Aylık Bazda Varlık Duruş Maliyeti

Varlık, bakım sırasında veya arızaya geçerek durduğu zaman üretim kaybından dolayı oluşan maliyetlerin [varlık](#_Varlıklar) bazında aylık olarak listelendiği rapordur.

![SNAGHTML1c806482.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5a8e1a1f-7c66-4176-b2ac-57ae93a7b858)

#### Aylık Bazda Üretim Duruş Maliyeti

Varlık, bakım sırasında veya arızaya geçerek durduğu zaman üretim kaybından dolayı oluşan toplam maliyetlerin aylık bazda listelendiği rapordur.

![SNAGHTML1c81516f.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd6591b69-7b33-4f6f-912c-b0264b0be442)

## Varlık

### Varlık Barkod Listesi

[Varlıkların](#_Varlıklar) barkod numaralarının listelendiği rapordur.

![SNAGHTML1c8e4fda.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4d5c134e-83a1-444a-8e11-0f325b5ba514)

### Varlık Grubu Bazında Varlık Listesi

[Varlıkların](#_Varlıklar) gruplarına göre listelendiği rapordur.

Rapor, [varlık grubu](#_Varlık_Grupları) bazında gruplanarak detay bölümde ilgili [varlık grubuna](#_Varlık_Grupları) ait olan [varlıklar](#_Varlıklar) listelenir.

Bu rapor sayesinde [varlık](#_Varlıklar) gruplarının maliyetleri de analiz edilebilinir.

![SNAGHTML1c8edc6f.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3df5e644-3466-4d4f-80bf-5144c391713b)

### Varlık Durumu Raporu

Hangi [varlık durumunda](#_Varlık_Durumları) kaç adet [varlık](#_Varlıklar) olduğunun sayısını liste ve grafik olarak veren rapordur.

![SNAGHTML1c90c19f.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload216b188c-2796-488f-bdc1-fa25a073dc4e)

### Varlık Durumu Tarihçesi

[Varlık](#_Varlıklar) bazında, ilgili [varlığın](#_Varlıklar) [varlık durumunun](#_Varlık_Durumları) değişme tarihçesinin verildiği rapordur. Bu rapor sayesinde [varlıkların](#_Varlıklar) hangi tarihte hangi durumda oldukları analiz edilebilinir.

![SNAGHTML1c92e1bc.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6b1734d9-2723-4520-9981-9cb6bd3a4967)

### Varlık Durumu Değişimleri Raporu

Verilen tarihler arasında varlıkların, [Varlık durum](#_Varlık_Durumları)larının değişim sayısının verildği rapordur.

![C:\\Users\\aanac\\AppData\\Local\\Temp\\SNAGHTML751d22e.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc8f0bb00-c5f6-4cb1-8219-3846bf25192b)

### Varlık Listesi

[Varlıkların](#_Varlıklar) genel bilgileri ile listelendiği rapordur.

![SNAGHTML1c950dcb.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload565034cf-ffa7-434c-b48a-a1f1b42481d1)

### Varlık Grup Özellikleri Listesi

[Varlıkların](#_Varlıklar), [varlık grubuna](#_Varlık_Grupları) ait olan özellikler (özel alanlar) için girilen değerlerinin listelendiği rapordur.

![SNAGHTML1c95eca5.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload38eb9d2e-94fc-4a65-b605-8842a5ffc12a)

### Varlık Malzeme Listesi

[Varlık](#_Varlıklar) üzerinde bulunan veya [varlık](#_Varlıklar) için [iş emrinde](#_İş_Emri) sarf edilen [malzeme](#_Malzemeler) listesinin, [varlık](#_Varlıklar) bazında gruplanarak verildiği rapordur.

![SNAGHTML1c977dbd.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada7939806-fe36-4580-9766-aa55c2aac22b)

## Malzeme

### Ambar Hareketleri

[Ambar](#_Ambarlar) bazında gruplayarak, ilgili [ambar](#_Ambarlar) için gerçekleşmiş olan her türlü stok hareketinin detaylı olarak listelendiği rapordur.

![SNAGHTML1c9c6434.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada328ea49-1ab1-4dd8-b459-414e614738ab)

### Ambar Özeti

[Ambar](#_Ambarlar) bazında gruplama yaparak, detay bölümde ilgili [ambarda](#_Ambarlar) bulunan [malzemelerin](#_Malzemeler) miktar, fiyat ve giriş-çıkış bilgilerinin listelendiği rapordur.

![SNAGHTML1c9d1164.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload62623bc9-9bef-4f86-895e-b0a410cc2c73)

### Malzeme Barkod Listesi

[Malzemelerin](#_Malzemeler) barkod bilgilerinin listelendiği rapordur.

![SNAGHTML1c9db041.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8704ac36-413a-47db-8701-272b814d8d0d)

### Barkod Listesi Ve Yazdırma

[Malzemelerin](#_Malzemeler) barkod bilgilerinin yazıcıdan yazdırılması amacı ile listelendiği rapordur.

![SNAGHTML1c9eaa29.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf96e1f79-f8a3-43f1-b7cb-776e9e4412b8)

### Hareket Görmeyen Malzemeler Listesi

[Sarf yeri](#_Sarfyerleri) ve [kısım](#_Kısımlar) bazında gruplanarak, belirli tarihler arasında, uygulama içerisinde tanımlı olduğu halde stok hareketi olmayan [malzemelerin](#_Malzemeler) listelendiği rapordur.

![SNAGHTML1c9fac3c.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3eebf626-ddd5-4a3c-bfcd-a253ed216a81)

### Malzeme Çıkış Raporu

[Malzeme](#_Malzemeler) çıkışlarının listelendiği excel tabanlı liste rapordur.

![SNAGHTML1ca096c8.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2b2e2c64-8134-497c-8a87-a8d8a6c6fddb)

### Malzeme Giriş Raporu

[Malzeme](#_Malzemeler) girişlerinin listelendiği excel tabanlı liste rapordur.

![SNAGHTML1ca14a6e.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload720b8ae3-cf84-4510-b918-5dcc9f119afa)

### Malzeme Stok Analizi

[Malzemelerin](#_Malzemeler) stok miktar analizinin yapıldığı rapordur. Bu raporda [malzeme](#_Malzemeler) miktarlarının yanı sıra ilgili [ambar](#_Ambarlar) için tanımlanmış olan asgari, azami ve güvenli stok miktarları da gösterilmektedir.

Asgari stok altına düşen malzmelerin listesi bu rapor ile alınabilinir. Bu işlem için rapor filtre sayfasında bulunan “Minimum Stok Miktarının altındaki Malzemeler” seçeneği işaretlenmelidir.

![SNAGHTML1ca1f369.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload24e8e386-5c43-4ac9-a8a1-ec4b48063b4b)

### Malzeme Borç Listesi

Malzeme talebi sonucunda transfer işlemi gerçekleşirse, talep eden [ambarın](#_Ambarlar) borçlu olduğu kabul edilir. [Ambarların](#_Ambarlar) taleplerinden dolayı borçlu oldukları [malzemelerin](#_Malzemeler) listesinin, talep detayları ile beraber listelendiği rapordur.

![SNAGHTML1ca28f59.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada1962855-4d0b-44c8-946c-2474401a1b84)

### Malzeme Talep Süreci Detayı

Malzeme taleplerinin onay süreçlerinin listelendiği ve analiz edildiği rapordur. Rapor talep bazında gruplanarak, onay adımları detay bölümde listelenmektedir.

![SNAGHTML1ca32ef2.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd6736ccb-0c1f-4873-93f7-aaa1c244b015)

## Enerji

### Rüzgâr Enerjisi Üretim Analizi

Uygulmaya girilen rüzgâr enerjisi üretim değerlerinin analiz edildiği excel tabanlı rapordur. Bu raporda üretim değerleri yıl ve aya göre saat gruplu toplam olarak verilmektedir.

![SNAGHTML2bb3037e.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf23d1a97-0a1f-4892-a755-0096318c3e19)

### Tüketim Analizi

Girilen tüketim değerlerinin [tüketim türüne](#_Tüketim_Türü) göre gruplanarak toplamlarının verildiği rapordur.

Bu raporda, tüketimlerin tep değerleri ile beraber karbon salınımı da gösterilmektedir. Tüketilen enerji kaynaklarından hangisinin işletme için daha uygun olacağına karar verilirken bu bilgilerden faydalanılabilinir.

![SNAGHTML2bb5af85.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4085f8b3-c17e-4e0a-a130-7499d5c532e1)

### Planlanan - Gerçekleşen Tüketim Analizi

Planlanan ve gerçekleşen tüketimlerin karşılaştırıldığı rapordur. Rapor bu karşılaştırmayı [kısım](#_Kısımlar) ve [enerji merkezi](#_Enerji_Merkezi) bazında yapabilmektedir.

![SNAGHTML2bb872b5.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload44fafa30-1423-42a8-929e-605a6b67607a)

### Pano Tüketim Analizi

[Dağıtım panosu](#_Dağıtım_Panosu) bazında girilen tüketim değerlerinin [kısım](#_Kısımlar) ve [enerji merkezi](#_Enerji_Merkezi) bazında gruplanarak gösterildiği rapordur.

![SNAGHTML2bb9a2f8.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8ecdeaea-d366-4752-bc2b-f258a16415b0)

# Grafikler

Uygulamada toplanan verilerin grafiksel olarak, kullanıcının daha kolay analiz işlemi yapabilmesini sağlamak amacıyla görsel olarak sunulduğu fonksiyonlardır.

Grafikler X ve Y eksenlerinden oluşur.

X Ekseni

X eksenine yatay eksen de denilebilir. X ekseninde genellikle kod veya tanım bilgileri yer alır. X ekseninin görevi, grafikte gösterilen değerleri gruplamaktır. Grafiklerin x ekseninde her zaman tek bir gruplama değer türü olabilir.

Y Ekseni

Y eksenine dikey eksen de denilebilir. Y ekseninde her zaman sayısal değerler olmalıdır. Y ekseni kullanıcının görmek istediği değerleri x ekseninde bulunan gruplama değer türüne göre toplam olarak gösterir.

![SNAGHTML1f67b36b.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload678df0e6-467c-47dc-b048-59ac9f1084be)

Grafik Ayarları

Hazırlanan Grafik ile ilgili görsel ayarların yapıldığı yerdir.

![SNAGHTML1f50adcf.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd863e763-65c2-450c-92b4-4ae8160704d0)

Bu ayarlar şu şekildedir;

| Başlıkları Göster           | Bu seçenek işaretli olursa grafik serisi üzerinde ilgili serinin değeri gösterilir.                                                                               |
|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Başlık Değer Gösterim Şekli | Grafik serisi üzerinde gösterilen başlığın içerik türü belirlenir.  Bu alanda seçilebilinecek türler aşağıdaki gibidir; Açıklama Açıklama ve Değer Seri Adı Değer |
| Seri Açıklamasını Göster    | Bu seçenek işaretli olursa grafiğin varsayılan olarak sağ tarafında bulunan seri ismini gösterir. Seri ismi genellikle Y ekseninde gösterilen değer türüdür.      |
| X Ekseni Başlık Açısı       | X ekseninde gösterilecek başlıkların x eksenine göre yazılma açısıdır.                                                                                            |
| İlk                         | Büyükten küçüğe doğru sıralanmış değerler arasından, grafik içerisinde gösterilmesi istenen ilk (n) kayıt.                                                        |
| Mod                         | Değerlerin toplam içerisinde gösterim türüdür.                                                                                                                    |
| Diğerlerini Göster          | Seçili olursa, grafikte gösterilecek ilk (n) kayıt arasına girmeyen değerlerin toplamını tek bir seri olarak grafik içerisinde gösterir.                          |
| Diğer Başlığı               | Grafik içerisinde gösterilen diğer serinin başlığıdır.                                                                                                            |
| Grafik Yüksekliği           | Hazırlanacak grafiğin pixel ölçü tipindeki yükseklik değeridir. 0 (sıfır) olarak bırakılırsa sayfa yüksekliğine göre otomatik hesaplanır.                         |
| Grafik Genişliği            | Hazırlanacak grafiğin pixel ölçü tipindeki genişlik değeridir. 0 (sıfır) olarak bırakılırsa sayfa genişliğine göre otomatik hesaplanır.                           |
| X Ekseni Değer Tipi         | X ekseninde gösterilecek değerin türüdür. İki değer alabilir; Kod Ad                                                                                              |
| Sıralama Türü               | Grafikteki serilerin değerlerine göre sıralanma türüdür. Dört değer alabilir; Değer-Artan Tanım-Artan Değer-Azalan Tanım-Azalan                                   |
| Değer Ölçek Tipi            | Grafikte gösterilen değerlerin veri tipidir. Dört değer alabilir; Qualitative: Sayılamayan Numerical: Sayısal / Sayılabilen DateTime: Tarih Auto: Otomatik        |
| Ondalık Bölüm               | Grafik değerlerinde gösterilecek sayısıal ifadenin ondalık kısmı uzunluğudur.                                                                                     |
| Grafik Başlığı              | Hazırlanan grafiğin üst bölümünde bulunacak başlık bilgisidir.                                                                                                    |

Grafik Araç Çubuğu

Hazırlanan grafiğin gösterildiği bölümde, grafiğin üst bölümünde bulunan ve ilgili grafik üzerinde bazı görsel ayarların yapılmasına olanak tanıyan araç çubuğudur.

![SNAGHTML1f52f24e.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3588aaec-70cb-4ef4-8852-201be012990d)

Bu araç çubuğındaki fonksiyonların kullanımı şu şekildedir;

-   ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf56c2968-9ef6-49a1-9447-20cfb08af038) : Hazırlanan grafiği yazıcıya gönderir.
-   ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4e83f2f5-804b-4ca2-a154-0f9ab3b40498) : Hazırlanan grafiği seçilen formatta dışa aktarır ve sürücüye kaydeder.
-   ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade7f7cf4a-e0e1-494a-966b-a5e04d19df47) : Hazırlanan grafiği seçilen formatta dışa aktarır ve farklı bir sayfada açar.
-   ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada4b148a4-3e31-4582-a897-ba582463f624) : Hazırlanan grafiğin dışa aktarım formatıdır.

    ![SNAGHTML1f564222.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadad7e21f6-9305-4919-91d4-f49ce7e4329a)

-   **Grafik Tipi:** Hazırlanan grafiğin türünü değiştirir.

    ![SNAGHTML1f57ab60.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf145c03d-f995-40db-aa94-523a9a001f53)

-   **Grafik Görünümü:** Grafik arka zemin görünümünü değiştirir.

    ![SNAGHTML1f5a0f50.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf41900e0-71c7-433b-a993-40a5645714e5)

-   **Grafik Renk Paleti:** Grafik serilerinde kullanılacak renk paletleridir.

    ![SNAGHTML1f5cd1d3.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3101a31d-7a6a-4613-a9cc-9401a1b438b8)

## Bakım

### En Çoklar Analizi

İş emirlerinde oluşan süre, maliyet ve sayılar ile ilgili değerlerin çeşitli gruplama özellikleri ile grafiksel olarak görüntülenebildiği ve analiz edilebildiği fonksiyondur.

En çoklar analizinde grafik hazırlama işlemi sırasıyla dört adımdan oluşur;

1.  **Yatay(X) Eksende Gösterilecek Gruplama Türünün Belirlenmesi (Ne Bazda?):** Grafiğin yatay ekseninde gösterilecek ve grafikte gösterilecek değerleri gruplayacak değer türü seçilir.

    Varlık, [sarf yeri](#_Sarfyerleri), [kısım](#_Kısımlar), [iş tipi](#_İş_Tipleri), arıza nedeni gibi seçenekler bu eksende seçilebilecek değer türlerine örnek gösterilebilinir.

    ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload59c61a8a-d18e-43a8-80a6-07d663b57044)

2.  **Değerler(Y) Ekseninde Gösterilecek Sayısal Değerlerin Belirlenmesi (Neyi?):** Grafiklenecek sayısal değerler bu sekmede belirlenir. Bu sekmede seçeceğiniz değerler yatay eksende seçmiş olduğunuz değer tipine göre gruplanıp toplam değerleri grafikte gösterilecektir.

    ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddf31a0f7-7095-4ba7-81b0-3f1aee745d18)

    Bir grafikte birden fazla grafiklenecek değer türü seçebilirsiniz. Bu durumda uygulama seçilen her grafikleme değer türü için bir dizi oluşturacak ve hepsini aynı grafik içerisinde gösterecektir.

    Grafiğin değer kısmını oluşturabilecek değer türleri aşağıda ki resimde gösterilmiştir.

3.  **Filtrenin Belirlenmesi (Hangi İş Emrileri?):** Grafik çiziminde kullanılacak [iş emirlerini](#_İş_Emri), bu sekmedeki filtreleme seçeneklerini kullanarak kısıtlayabilirsiniz.

    ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d67a8d8-065b-4d00-b348-e324b0eb4dce)

4.  **Grafik Ayarları (Nasıl?):** Gösterilecek grafik ile ilgili görsel ayarların yapılabildiği sekmedir.

    ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade4d5d440-2962-472a-8861-0bf6292ae849)

    Bu sekmede bulanan seçeneklerin ne işe yaradığı ve nasıl kullanılacağı [Grafikler](#grafikler) ana başlığı altında anlatılmıştır.

Bu dört adım geçildikten sonra grafik ön izleme için hazır demektir. En çoklar analizi sayfasındaki “Grafik” başlıklı sekmeye geçiş yaptığınızda grafiğin hazırlandığını görebilirsiniz ve kısa bir süre sonra grafik hazır olacaktır.

![SNAGHTML1f21983c.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade476514b-97bd-48d8-a901-04833729b11a)

Grafik hazırlanırken kullanılan veri, görüntülenmek veya dış ortama aktarmak istenirse, “Grafik Verisi” başlıklı sekmeyi açmak yeterli olacaktır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload905790e3-baae-45e3-9856-7d9233bdb70b)

Örnek Grafikler:

-   En Fazla Bakım Yapılan Varlıklar Grafiği:

| X Ekseni        | Varlık           |
|-----------------|------------------|
| Y Ekseni        | İş Emri Sayıları |
| Filtre          | \<İsteğe Bağlı\> |
| Grafik Ayarları | \<İsteğe Bağlı\> |

![SNAGHTML1f6bf1b3.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadddb0f180-d423-42b5-ad4d-5e15fcf88092)

-   En Fazla Duruşa Neden Olan Arıza Nedenleri Grafiği:

| X Ekseni        | Arıza Kodu                          |
|-----------------|-------------------------------------|
| Y Ekseni        | İş Emri Sayıları                    |
| Filtre          | Üretim Durumu = “Üretimi Durdurdum” |
| Grafik Ayarları | \<İsteğe Bağlı\>                    |

![SNAGHTML1f6ceac0.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1713fc77-3440-48e5-98ce-9f016e141c77)

-   En Fazla Bakım Maliyeti Oluşturan Varlık Grafiği:

| X Ekseni        | Varlık           |
|-----------------|------------------|
| Y Ekseni        | Toplam Maliyet   |
| Filtre          | \<İsteğe Bağlı\> |
| Grafik Ayarları | \<İsteğe Bağlı\> |

![SNAGHTML1f702273.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0eec95a4-9742-4ec0-bcf8-46cd3abbc7ce)

### Mtbf / Mttr Analizi

Mtbf ve Mttr değerlerinin çeşitli gruplama özellikleri ile grafiksel olarak görüntülenebildiği ve analiz edilebildiği fonksiyondur.

Mtbf / Mttr analizinde grafik hazırlama işlemi sırasıyla beş adımdan oluşur;

1.  **Grafik Zaman Ölçeği:** Gösterilecek mtbf ve mttr değerlerinin hangi zaman dönemleri için hesaplanacağı ve gösterileceği belirlenir.

    ![SNAGHTML1f85baac.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3ca747be-e870-4ae0-8075-412f408a9fd8)

2.  **Yatay (X) Ekseni:** Yatay eksende kullanılacak gruplama türüdür. Mtbf ve Mttr değerleri bu bölümde seçeceğiniz değer türüne göre tek tek hesaplanacak ve grafiklenecektir.

    Bu bölümde seçme işlemi yapabilmek için “Alt Grup Kullan” seçeneğini işaretlemelisiniz.

    ![SNAGHTML1f875d03.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload773be45d-0613-41ac-a634-e036b0b8d95d)

    Örneğin, [varlık](#_Varlıklar) bazında hesaplama yapılmak isteniyorsa bu bölümde “Varlık”, [sarf yeri](#_Sarfyerleri) bazında hesaplama yaptırılmak isteniyorsa “Sarf Yeri” seçili olmalıdır.

3.  **Değerler (Y) Ekseni:** Grafiğin hazırlanmasında kullanılacak hesaplama türleri seçilmelidir. Bu bölümde “MTBF”, “MTTR” ve “Arıza Oranı” başlıklı seçeneklerden en az birisi seçili olmalıdır aksi durumda grafik çizilemeyecektir.

    ![SNAGHTML1f8b8ead.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload626e623c-7fc0-4435-99a4-5cf8a1841d66)

    Bu sekmede mtbf ve mttr hesaplamalarında kullanılacak “Günlük Çalışma Saati” ve grafik tarih aralığındaki “Çalışılmayan Gün Sayısı” değerleri de girilmelidir.

4.  **Filtre:** Grafik çiziminde kullanılacak [iş emirlerini](#_İş_Emri), bu sekmedeki filtreleme seçeneklerini kullanarak kısıtlayabilirsiniz.

    ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d67a8d8-065b-4d00-b348-e324b0eb4dce)

5.  **Grafik Ayarları:** Gösterilecek grafik ile ilgili görsel ayarların yapılabildiği sekmedir.

    ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade4d5d440-2962-472a-8861-0bf6292ae849)

    Bu sekmede bulanan seçeneklerin ne işe yaradığı ve nasıl kullanılacağı [Grafikler](#grafikler) ana başlığı altında anlatılmıştır.

Bu beş adım geçildikten sonra grafik ön izleme için hazır demektir. Mtbf / Mttr analizi sayfasındaki “Grafik” başlıklı sekmeye geçiş yaptığınızda grafiğin hazırlandığını görebilirsiniz ve kısa bir süre sonra grafik hazır olacaktır.

![SNAGHTML1fc6b4b5.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd5b01717-2ca6-40a3-91a4-d96dd81f1ff1)

Grafik hazırlanırken kullanılan veri, görüntülenmek veya dış ortama aktarmak istenirse, “Grafik Verisi” başlıklı sekmeyi açmak yeterli olacaktır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadce465907-571d-451e-9cc0-10e372c9dd48)

### Ölçüm Değerleri Analizi

İş emirlerinde, [ölçüm paketleri](#_Ölçüm_Paketleri) ile yapılan ölçümlerin grafiksel olarak analiz edildiği fonksiyondur.

Ölçüm değerleri analizinde grafik hazırlama işlemi sırasıyla üç adımdan oluşur;

1.  **Grafik Zaman Ölçeği:** Grafik aynı anda sedece tek bir [varlık](#_Varlıklar) için çizdirilebilinir. Bu nedenle bu sekmede ölçüm değerleri grafiklenecek [varlık](#_Varlıklar) seçilmelidir.

    ![SNAGHTML257d0e76.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload49ad7d76-09b9-43b7-b30d-aa63898e7805)

    [Varlık](#_Varlıklar) seçildiği zaman alt bölümde bulunan listede ilgili [varlık](#_Varlıklar) için daha önce ölçümü yapılmış olan [ölçüm paketleri](#_Ölçüm_Paketleri) listelenir.

    ![SNAGHTML25833beb.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3d16374a-8791-48e9-a50f-9e8bc6ea7c67)

    Listelenen [ölçüm paketlerinden](#_Ölçüm_Paketleri) hangisi için girilen ölçüm değerlerinin analiz edileceği de belirtilmelidir.

    Seçme işlemi için satırda bulunan seçenek işaretlenmelidir.

    ![SNAGHTML25820948.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload40c2a8bf-9d95-436c-ae35-6cb273900d84)

    Değerlerin hangi zaman birimi bazında gösterileceği de bu sekmede belirlenir.

    ![SNAGHTML257e7968.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd8055c39-8c37-45f2-8d0d-e049a04cff09)

    Grafik içerisinde, ölçüm sırasında girilen referans değerlerinin ayrı bir seri olarak gösterilmesi isteniyorsa, gösterilmesi istenen referans değeri ile ilgili seçenek işaretlenmelidir.

    ![SNAGHTML257fd4d0.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload81c75668-f027-44aa-9f5a-9ce7f62a7431)

2.  **Filtre:** Grafik çiziminde kullanılacak [iş emirlerini](#_İş_Emri), bu sekmedeki filtreleme seçeneklerini kullanarak kısıtlayabilirsiniz.

    ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d67a8d8-065b-4d00-b348-e324b0eb4dce)

3.  **Grafik Ayarları:** Gösterilecek grafik ile ilgili görsel ayarların yapılabildiği sekmedir.

    ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade4d5d440-2962-472a-8861-0bf6292ae849)

    Bu sekmede bulanan seçeneklerin ne işe yaradığı ve nasıl kullanılacağı [Grafikler](#grafikler) ana başlığı altında anlatılmıştır.

Bu üç adım geçildikten sonra grafik ön izleme için hazır demektir. Ölçüm değerleri analizi sayfasındaki “Grafik” başlıklı sekmeye geçiş yaptığınızda grafiğin hazırlandığını görebilirsiniz ve kısa bir süre sonra grafik hazır olacaktır.

### Hedef Analizi

[Sarf yeri](#_Sarfyerleri), [kısım](#_Kısımlar) veya [varlık](#_Varlıklar) için tanımlanmış olan [hedeflerin](#_Hedefler_(Sarfyeri,_Kısım,), fiili gerçekleşme değerleri ile karşılaştırıldığı grafiklerdir.

Grafik hazırlama üç adımdan oluşmaktadır;

1.  **Tercihler:** Bu sekmede grafik hazırlanırken kullanılacak paremeterler belirlenmektedir. Sekme içinde üç adet başlık bulunmaktadır.
2.  **Hedef Analiz Türü:** Hangi bazda tanımlanan [hedeflerin](#_Hedefler_(Sarfyeri,_Kısım,) grafikleneceği belirlenir.

    Üç seçenek vardır;

    -   Varlık: [Varlık](#_Varlıklar) bazında hedef analizi yapılacaksa seçilmelidir.
        -   Kısım: [Kısım](#_Kısımlar) bazında hedef analizi yapılacaksa seçilmelidir.
        -   Sarf Yeri: [Sarf yeri](#_Sarfyerleri) bazında hedef analizi yapılacaksa seçilmelidir.

            ![SNAGHTML1fed51a0.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf90f7e37-43db-43c1-9ff9-cc8e93aa8ee8)

3.  **Filtre:** Hedef analiz türü belirlendikten sonra, belirlenen tür içerisinde filtreleme yapılmak isteniyorsa kullanılmalıdır.

    Örneğin hedef analizi türü olarak [varlık](#_Varlıklar) seçildikten sonra sadece belirli bir [varlık](#_Varlıklar) kaydına ait [hedefler](#_Hedefler_(Sarfyeri,_Kısım,) analiz edilmek isteniyorsa filtre bölümünde [varlık](#_Varlıklar) filtresi kullanılmalıdır.

    ![SNAGHTML1fdb7fb1.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7fca32fe-dd36-4171-95e6-8df66bf7b0e0)

    Aynı şekilde sadece belirli tarihler arasında girilen hedef değerleri analiz edilecekse “Yıl”, ve “Ay Aralığı” filtre seçenekleri kullanılmalıdır.

    MTBF ve MTTR ile ilgili [hedefler](#_Hedefler_(Sarfyeri,_Kısım,) analiz edilecekse, mtbf ve mttr fiili değer hesaplamalarında kullanılmak üzere “Çalışılmayan Gün Sayısı” ve “Günlük Çalışma Saati” değerleri de girilmelidir.

4.  **Grafik Serileri:** Grafiği çizdirilecek ve analiz edilecek [hedefler](#_Hedefler_(Sarfyeri,_Kısım,) seçilmelidir. Bu bölümde hedef tanımlaması yaptığınız değer türleri listelenmektedir.

    ![SNAGHTML1fdc0e49.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload22e1e426-1ed8-4e8a-9b08-dee88d562e59)

    Aynı anda birden fazla hedefi analiz edebilirsiniz fakat bu durum grafiğin okunmasını ve analiz işlemini zorlaştıracaktır.

5.  **Filtre:** Grafik çiziminde kullanılacak [iş emirlerini](#_İş_Emri), bu sekmedeki filtreleme seçeneklerini kullanarak kısıtlayabilirsiniz.

    ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d67a8d8-065b-4d00-b348-e324b0eb4dce)

6.  **Grafik Ayarları:** Gösterilecek grafik ile ilgili görsel ayarların yapılabildiği sekmedir.

    ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade4d5d440-2962-472a-8861-0bf6292ae849)

    Bu sekmede bulanan seçeneklerin ne işe yaradığı ve nasıl kullanılacağı [Grafikler](#grafikler) ana başlığı altında anlatılmıştır.

Bu üç adım geçildikten sonra grafik ön izleme için hazır demektir. Hedef analizi sayfasındaki “Grafik” başlıklı sekmeye geçiş yaptığınızda grafiğin hazırlandığını görebilirsiniz ve kısa bir süre sonra grafik hazır olacaktır.

![SNAGHTML1feb0516.PNG](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb3075403-a3eb-48f2-bd68-571af0b5d3b1)

Grafik hazırlanırken kullanılan veri, görüntülenmek veya dış ortama aktarmak istenirse, “Grafik Verisi” başlıklı sekmeyi açmak yeterli olacaktır.
