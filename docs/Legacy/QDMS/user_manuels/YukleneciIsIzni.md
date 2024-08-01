---
title: Yüklenici İş İzni Takibi
description: Yüklenici İş İzni Takibi Modülü Yardım Dokümanı
sidebar_position: 46
---

:::tip Bilgi

İlgili konu başlığına sağ tarafta bulunan navigasyon yardımıyla hızlı bir şekilde ulaşabilirsiniz.

:::


**Yüklenici İş İzni Takibi Modülü(v.5.24) Kullanıcı Yardım Dokümanı**

Modül Versiyonu: 5.24



**1.GİRİŞ**: Yüklenici İş İzni Takibi Sistemi; bir kuruluşta potansiyel olarak tehlikeli olan rutin ve rutin olmayan faaliyetlerin güvenli şartlar altında gerçekleştirilmesinin sağlanması için oluşturulmuş standart bir prosedürdür. Yüklenici İş İzni Talep formu pek çok bakım onarım faaliyeti için güvenli çalışma sistemlerinin önemli bir parçasıdır. Yüklenici İş İzni Talep formları kullanıldığında işin gerekli güvenlik önlemleri altında yapılması sağlanır ve formlar sayesinde yapılacak işle ilgili tüm öngörülebilir tehlikelerin dikkate alınmış olduğunun net kaydı da tutulmuş olur.

**2.AMAÇ**: Bu yardım kılavuzunun amacı, QDMS kullanan kuruluşların Yüklenici İş İzni Takibi (Taşeron Yönetimi) Modülünün implementasyonu sırasında ve sonrasında izleyeceği yolu belirlemektir.

**3.SORUMLULUKLAR**: İşyeri Hekimi, İş Güvenliği Uzmanı, İnsan Kaynakları, İdari İşler Sorumlusu, İşveren.

**4.KISALTMALAR**:

QDMS: Kalite Dokümanları Yönetim Sistemi “ Quality Document Management System”

İSG: İş Sağlığı ve Güvenliği

İK: İnsan Kaynakları

# **5.YÜKLENİCİ İŞ İZNİ TAKİBİ MODÜLÜ**

Yüklenici firmaların kurum içerisindeki çalışmalarının takibi ve kontrolü, Yüklenici firmaların gerekli evraklarının takibi, Yüklenici İş İzin formlarının hazırlanması ve onaylanması, İş izni verilen personel listesinin Yüklenici firmaya e-mail ile gönderilmesi, Yüklenici firmalar tarafından çalışma yapılan yerlerin anlık gösterimi, Yüklenici firma bazlı, yapılacak iş türüne göre yetki verebilmesi, ihtiyaca yönelik faklı akışlar tasarlanması ve farklı alanlar tanımlanmasının sağlandığı modüldür.

## **5.1.Sistem Altyapı Tanımları/Yüklenici İş İzni Takibi**

Yüklenici İş İzni Takibi Modülü altyapısında oluşturulacak tanımlamaların yapıldığı kısımdır. Alan Tanımlama, Fonksiyon Dizayner, E-Posta Ayarları, Evrak Tanımlama ve İş Tipi Tanımlama gibi altyapı tanımlamalarının yapıldığı menülerdir. Bu menülerde Evrak Tanımlama ve İş Tipi Tanımlama Modülü kapsamında kullanmak için zorunludur. Alan tanımlama ve Fonksiyon Dizayner ise ekstra alan gereksinimi olduğunda kullanılabilir. E-Posta Ayarları menüsü ise ilgili rollere mail göndermek için kullanılmaktadır. Anket Soru Listeleri menüsü ise Anket İşlemleri Modülündeki Anket şablonu ekranında olduğu gibi bu modülde ilgili fonksiyonlar için Anket şablonu tasarlaması amacıyla kullanılmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc7409744-6447-47eb-9b57-15cf3195bce6)


### **5.1.1.Alan Tanımlama**

**Menü Adı**: Sistem Altyapı Tanımları/ Yüklenici İş İzni Takibi/ Alan Tanımlama

Yüklenici İş İzni Takibi Modülünün yer alacak bütün alanların tanımlandığı menüdür. Burada oluşturulan alanlar, alan havuzuna kaydedilir. Buradaki alan tanımlama özelliği, QDMS’in risk Modüllerindeki alan tanımlama özellikleri ile aynıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb0523e3d-5a65-4c79-afc4-98f7b929f675)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada110947d-b4eb-45ad-92e0-3866bf82ac5a): Yeni bir alan eklenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload20089354-0725-4d66-a276-f40b9c0c1e2a):Var olan alanda değişiklik yapılmak istenirse kullanılır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload805d1143-6659-44ab-b1d9-356f0cbe6450): İlgili alanı silmek için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4e48d709-d858-49b2-8158-08b92f279808): Alanın değerleri tanımlanır.

Alan Tanımlama ekranına yeni bir Alan eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9c17e3c6-0372-4ca6-b441-019b6826472a)(yeni) butonu tıklanarak Alan Tanımlama/ Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadec0da973-f914-457b-a92e-7297f93f6698)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Alan Kodu:** Alan Kodu bilgisi girilir.

**Alan Adı:** Alan Adı bilgisi girilir.

**Başlık Notu:** Alanın Başlık Notu bilgisi girilir.

**Giriş Tipi:** Alanın Giriş tipinin Hesaplanan veya Veri Girişi tipi bilgisi seçilir. Giriş Tipi seçeneği oluşturulan alanın manuel olarak veri girişi ile mi yoksa hesaplama yöntemi ile mi belirleneceğini gösterir.

**Alan Tipi**: Alan tipinin bilgisi seçilebilir. Alan Tipi ise oluşturulan alanın metin, numerik, tarih, liste vb. tiplerinden hangisi olduğunu gösterir.

**Görünme Şartı:** Alanın Görünme Şartı bilgisi girilir. Liste tipli bir alanın değerlerine göre oluşturulan alanın görüntülenmesini sağlar.

**Durum:** Alanın durumun Aktif veya Pasif olarak bilgisi seçilebilir.

**Genişlik:** Alanın kolon genişliği bilgisi girilir.

Alan adı ve Alan kodu bilgisi girilir. Giriş Tipi Veri Girişi ve Alan tipi Personel seçilir. Durum kısmı Aktif seçilir. Alan Tanımlama ekranında gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada0467968-7156-47a8-88d3-93ca5429e04b) (kaydet) butonu tıklanarak Alan Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf7ca76f3-5f42-46a8-9097-a8c0865cfb42)

Eğer havuza eklenen alanlar Liste, Puanlı Liste ya da Arama Özellikli Liste gibi Liste türlerinden biriyse ve ilgili alan seçildiği takdirde ekranın sağ üst köşesindeki butonlar arasında ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7920a6b3-8b30-4034-b17c-23fad239d533) (Değerler ) butonu ortaya çıkmaktadır. Bu buton yardımıyla eklenen liste biçimindeki alanın değerleri tanımlanır.

**Sistemde mevcut bulunan alan tiplerinin tam listesi aşağıda belirtilmiştir;**

**Metin:** Text kutucuğu ekler.

**Metin Çok Satırlı:** Çok satırlı text kutucuğu ekler.

**Nümerik:** Sayısal olarak veri girişi yaptırır.

**Nümerik-Parasal:** Parasal değer olarak nümerik giriş yaptırır.

**Nümerik-Birim:** Birim olarak nümerik giriş yaptırır.

**Tarih:** Takvim alanı ekler.

**Liste:** Birden fazla liste elemenanı arasından tek seçim yaptırır.

**Puanlı Liste:** Açılır menüden tekli seçim yaptırır, liste elemanlarının puan değerleri mevcuttur.

**Arama Özellikli Liste:** Açılır menü altından birden fazla seçim yapılmasını sağlar.

**Ağaç Liste:** Ağaç dallanması şeklinde menü altından birden fazla seçim yapılmasını sağlar.

**Personel:** QDMS Personel veri tabanından kişi bilgisi seçilebilmesini sağlar.

**Departman:** QDMS Departman veri tabanından departman bilgisi seçilebilmesini sağlar.

**Unvan:** QDMS Unvan veri tabanından unvan bilgisi seçilebilmesini sağlar.

**Doküman:** QDMS Doküman veri tabanından doküman seçilebilmesini sağlar.

**Süreç:** QDMS Süreç veri tabanından süreç seçilebilmesini sağlar.

**Yönetim Sistemi:** QDMS Yönetim Sistemi veri tabanından yönetim sistemi bilgisi seçilebilmesini sağlar.

**Müşteri:** QDMS Müşteri veri tabanından müşteri bilgisi seçilebilmesini sağlar.

**Tedarikçi:** QDMS Tedarikçi veri tabanından tedarikçi bilgisi seçilebilmesini sağlar.

**Ürün Grubu:** QDMS Ürün Grubu veri tabanından ürün grubu bilgisinin seçilebilmesini sağlar.

**Ürün:** QDMS Ürün veri tabanından ürün bilgisinin seçilebilmesini sağlar.

**Şirket Profili:** QDMS Şirket Profili veri tabanından şirket profili bilgisi seçilebilmesini sağlar.

**Başlık:** Risk formuna ya da detay ekranına başlık ekler.

**Dosya:** Dosya ekler.

**Resim:** Resim ekler.

**Resim Liste:** Resim listesinden seçim sağlar.

**Çoklu Resim:** Çoklu resim seçilmesini sağlar.

**Tablo:** Tablo verilerinin kullanılmasını sağlar.

**Sorgu:** Sorgulama şeklinde seçim sağlar.

**Sorgu Ağaç:** Ağaç dallanması şeklinde sorgu yapılmasını sağlar.

**Sekme:** Aktif sekme haricinde alanların ilişki kurularak içerisinde görülebileceği yeni bir sekme oluşturur.

**Onay Kutusu Liste:** Tekli veya çoklu seçim yaptırılacak tipte bir liste tipli alandır.

**Risk:** Risk tabanlı modüllerden değerlerin seçilebilmesini sağlar. Bu tip bir alan eklendikten sonra hangi modülden değerlerin geleceği alan tanımlama ekranında seçilmesi gereklidir.

**Açıklamalı Liste:** Seçilen liste değerinin yanına açıklama yazabilme imkanı sağlayan alan tipidir. Alan Tanımlama menüsünde alan değerleri tanımlanırken her değer için açıklama kutucuğunun aktif olup olmayacağının seçilmesi gerekir. Burada yapılan seçime göre Entegre Yönetim Sistemi menüsü altında bu alanın görüleceği menüde ilgili seçim yapıldığında alan değerinin yanına kullanıcının açıklama yazabilmesi için kutucuk açılmış olur.

**Pozisyon:** QDMS pozisyon veri tabanından pozisyon bilgisi seçilebilmesini sağlar.

**Saat:** Saat tipli alan ekler.

### **5.1.2.Fonksiyon Dizayner**

**Menü Adı**: Sistem Altyapı Tanımları/ Yüklenici İş İzni Takibi/ Fonksiyon Dizayner

Fonksiyon Dizayner özelliği ile alan havuzuna eklenen alanlar Yüklenici İş İzni Takibi Modülünün istenilen sayfaları ile ilişkilendirilebilir. Bunun için Yüklenici İş İzni Takibi Modülünün Sistem Altyapı Tanımları altından Fonksiyon Dizayner menüsüne gelinir. Açılan ekranda Yüklenici İş İzni Takibi Modülünün alan eklenebilecek fonksiyonları sıralanacaktır. Bu ekranda “Yüklenici İş İzni Talep Formu”, “Çalışma Yapılabilecek Personeller” ve “Yüklenici Personel Seçimi” fonksiyonlarında kullanılacak alanlar ve bunların sıralaması ile onay işlemlerindeki hiyerarşi detayı tanımlanır. Alan havuza eklenen alanlar![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload35cc4675-984e-431c-872d-536be0fca9de)(Alanlar) butonu yardımıyla 1, 2 ve 3 numaraları fonksiyonların sayfaları eklenerek bu fonksiyonları sayfalarında tanımlanan alanların görüntülenmesi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload07eddaa0-1abd-48bb-8ee5-2952906b0a98)

Hangi fonksiyona alan eklemesi yapılmak isteniyorsa o fonksiyon seçilerek sağ üstteki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload35cc4675-984e-431c-872d-536be0fca9de) (alanlar) butonu tıklanır ve alan fonksiyona eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd69b71ad-41d1-4c4f-a7ef-84ac79b64ca1)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada110947d-b4eb-45ad-92e0-3866bf82ac5a): Yeni bir Fonksiyon tanımlar.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload20089354-0725-4d66-a276-f40b9c0c1e2a): Listede seçili Fonksiyon bilgisi ile ilgili herhangi bir düzeltme, değişiklik veya güncelleme yapılır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload805d1143-6659-44ab-b1d9-356f0cbe6450): Listede seçili Fonksiyon bilgisi silinebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2bac49bf-717f-4a55-afb4-e4887c0559cc) : Önceki ekrana geri dönülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload35cc4675-984e-431c-872d-536be0fca9de)(Alanlar) butonu ile açılan ekranda seçili fonksiyonda kullanılacak alanlar ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9c17e3c6-0372-4ca6-b441-019b6826472a) Yeni kayıt butonuna tıklanarak belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb261edfd-ca7a-419f-951c-a02a1e46f8c7) ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload877f0ede-d227-4d71-881e-610b1a4c0051)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Alan Adı:** Alan adı bilgisi seçilir.

**Zorunluluk Mesajı:** Seçilen alanın Zorunluluk Mesajı bilgisi girilir. Zorunlu alanlar doldurulmadığında verilecek uyarı mesajı bilgisi yazılır.

**Sıra No:** Seçilen Alanın Sıra No bilgisi girilir.

**Varsayılan Rol:** İlgili alanın değeri daha önce tanımlanmış bir üst formdan ya da kaydı giren kişinin adı soyadı, pozisyonu, unvanı, departmanı, iş yeri gibi verileri ise bunlar için tanımlanmış rol seçilebilir.

**Varsayılan Değer Değiştirilmesin:** Seçilen alan varsayılan olarak bir değer getiriyorsa getirdiği değerin değiştirmemesini sağlar.

**Gridde göster:** Alanın Gridde gösterilmesi aktif edilmek istenirse ilgili check box işaretlenir.

**Satır Sayısı:** Seçilen alanın satır sayısı bilgisi belirlenir.

**Kolon Genişliği:** Seçilen alanın kolon genişliği bilgisi belirlenir.

**Aktif Statü:** Seçilen alanın aktif statüsü bilgisi ilgili seçeneklerden seçilir.

**Görünür Statü:** Seçilen alanın görünür statüsü bilgisi ilgili seçeneklerden seçilir.

**Zorunlu Statü:** Seçilen alanın zorunlu statü bilgisi ilgili seçeneklerden seçilebilir.

Fonksiyon menüsünden, ilgili alanın hangi ekranlarda kullanılacağı seçilir. Daha sonra seçilen Fonksiyonun statü durumları belirlenir. Aktif statü kısmında alanın hangi statüde görülmesi isteniliyorsa bu statü işaretlenir. Görünür statü kısmında alanın hangi statüde görülmesi isteniliyorsa bu statü işaretlenir. Eğer alanın zorunlu olması isteniyorsa zorunlu olacağı statü seçilir. Mesaj alanı, eğer seçilen alan zorunlu tutulduysa ekranda gösterilecek mesajın yazıldığı yerdir. Sıra no ise alanın ilgili ekranda kaçıncı sırada gösterileceğini belirtmektedir. Gridde gösterilip gösterilmeyeceği, kolon genişliği belirlenir. Gerekli tüm alanlar doldurulduktan sonra ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadec5762b7-d968-4829-b340-b7176b9afadd)(kaydet) butonuyla, ilgili alan için ilgili fonksiyon tanımlama işlemi gerçekleştirilmiş olur. Bu şekilde Yüklenici İş İzni Takibi Modülünde hangi alanların nerede yer alacağı belirlenmiş olur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade11582bc-ccdf-4972-bda2-c8ee41b1e19b)

Yüklenici İş İzni Takibi Modülü sayfalarıyla ilişkilendirilen alan, Entegre Yönetim Sistemi/ Yüklenici İş İzni Takibi /Yüklenici İş İzni Talep Formu ekranında görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2b7bf269-eb8e-4c25-814e-46e09e0f67a0)

### **5.1.3.E-Posta Ayarları**

**Menü Adı**: Sistem Altyapı Tanımları/ Yüklenici İş İzni Takibi/ E-Posta Ayarları

E-Posta ayarları ekranında, Yüklenici İş İzni Takibi Modülü sürecinin hangi aşamasında kimlere mail gönderimi yapılacağı belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9dd64dc1-8595-4b8d-9599-3f42831c7da1)Bildirim ayarı yapılacak değerin üzerine gelinip ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2e4a4950-c7db-46ff-8e32-8b51556e38fe) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload45fc14bb-d5de-45b2-8a74-b8d410580bd6)

Açılan ekranda, sol tarafta Roller sütunu bulunur. Bu, E-Posta bildirimimin gideceği rolü yani kişiyi göstermektedir. Kime E-Posta gitmesi isteniyorsa, o rolle ilgili E-Posta Gitsin Mi? check box’ı işaretlenir. Daha sonra gönderilecek E-Posta’ daki mesaj gövdesi, Kullanılacak Mesaj Gövdesi kutucuğu vasıtasıyla listeden seçilir. Bütün bu işlemlerden sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddaf23f05-9d9d-4d65-b28e-6588bae9184e) (kaydet) butonu ile yapılan ayarlar kaydedilmiş olur.

### **5.1.4.Evrak Tanımlama**

**Menü Adı**: Sistem Altyapı Tanımları/ Yüklenici İş İzni Takibi/ Evrak Tanımlama

Yüklenici İş İzni Takibi Modülünde çalışma izni için gerekli evrakların tanımlandığı menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload16e4665c-8681-472e-9e45-01badf2c078c)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada110947d-b4eb-45ad-92e0-3866bf82ac5a):Yeni bir evrak tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload20089354-0725-4d66-a276-f40b9c0c1e2a): Listede seçili evrak bilgisi güncellenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload805d1143-6659-44ab-b1d9-356f0cbe6450): Listede seçili evrak bilgisi silinebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc31d644c-a320-4eaa-91a7-b1fa59b3b4ff): Veriler Excel’ e aktarılabilir.

Evrak Tanımlama ekranından yeni bir Evrak eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9c17e3c6-0372-4ca6-b441-019b6826472a)(yeni) butonu tıklanarak Evrak Tanımlama/ Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload04e04b2d-3c7d-4741-a5ed-de953f68d3c3)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Evrak Adı:** Evrak Adı bilgisi girilir.

**Geçerlilik Süresi:** Evrağın Geçerlilik Süresi bilgisi girilir.

**Geçerlilik Süre Tip :** Evrağın Geçerlilik Süre Tipinin gün, ay ve yıl seçeneklerin seçilebilir.

**Açıklama:** Evrakla ilgili Açıklama bilgisi girilir.

**Evrak Türü Liste Değerleri:**Evrak Türü liste değerlerinden Personel ve Ekipman seçeneklerinde seçim yapılır.

**Alt Evrak Eklenecek mi? :** Alt Evrak Eklenecekse ilgili check box işaretlenir. Alt Evrak Eklenecek mi alanı aktif edilirse Alt Evraklar adı altında bir alan çıkar.

**Alt Evraklar:** Alt Evraklar bilgisi eklenir.

**Tüm iş tiplerinde zorunlu olsun mu?:** Tüm iş tiplerinde zorunlu bu evrağın zorunlu olması isteniyorsa ilgili check box işaretlenir.

Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada0467968-7156-47a8-88d3-93ca5429e04b) (kaydet) butonu tıklanarak Evrak Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade734c3e0-0c81-42c7-8234-136b5c572cea)

Alt Evraklara örnek; Alt evrak seçim ekranında da daha önceden tanımlanmış evraklar seçilir. Kaynakçı belgesi, ustalık belgesi vs. Bu şekilde yapılan bir seçimin amacı; evrak kümesi oluşturmaktır. Bu şekilde kümelenmiş evraklardan yüklenicinin herhangi bir evrak için personel ataması yeterli olacaktır. Bir evrağın ilişkilendirilmiş tüm alt evrakları için personel atamasına ihtiyaç olmayacaktır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc9025c7c-a8ba-4e2d-9889-c8f9ef9b7cf4)

Evrak Tanımlama ekranında gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada0467968-7156-47a8-88d3-93ca5429e04b) (kaydet) butonu tıklanarak Evrak Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade0db1ad3-c092-4d89-bd57-961587ec937d)

### **5.1.5.İş Tipi Tanımlama**

**Menü Adı**: Sistem Altyapı Tanımları/ Yüklenici İş İzni Takibi/ İş Tipi Tanımlama

Yüklenici İş İzni Takibi Modülünde çalışma yapılacak İş Tiplerinin tanımlamalarının yapıldığı menüdür. Yüklenici ile de İş Tipi İlişkisi kurulabilir. Yüklenici ile olan bu bağlantı parametreden aktif veya pasif yapılarak kullanılabilir. **Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Parametreler** menüsüne gelinir. Filtreden Yüklenici Yüklenici İş İzni Takibi Modülü seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4b3e16f0-1d4d-4511-a2db-446107bb654b)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1d08dcdf-b6c8-44d9-adb9-273f88f0aea6)

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload20089354-0725-4d66-a276-f40b9c0c1e2a)(Değiştir) butonu tıklanarak 20 numaralı parametre olan “İş Tipi Tanımlama Sayfasında Yükleniciler Seçilebilsin mi?” değeri “evet” olarak değiştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload040344ef-3a77-4a8b-a95e-e377f47b60e2)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadeb80ab67-7130-457e-b2cc-cb85d1b13a9e)

Parametre değeri “Evet” seçilerek parametre aktif edildiğinde İş Tipi Tanımlama alanında Yükleniciler alanı görüntülenir. Görüntülen yükleniciler alanı ile İş Tipi ile Yükleniciler ilişkilendirilir. Yüklecilerin hangi çalışmalarda bulunacakları iş Tipi tanımlama ekranında ilişkilendirilerek gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload23dba492-e37f-4ad1-8805-b9670d0f74bf)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada110947d-b4eb-45ad-92e0-3866bf82ac5a): Yeni bir İş Tipi tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload20089354-0725-4d66-a276-f40b9c0c1e2a): Listede seçili İş Tipi bilgisi güncellenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload805d1143-6659-44ab-b1d9-356f0cbe6450): Listede seçili İş Tipi bilgisi silinebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc31d644c-a320-4eaa-91a7-b1fa59b3b4ff): Veriler Excel’ e aktarılabilir.

İş Tipi Tanımlama ekranına yeni bir İş Tipi eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9c17e3c6-0372-4ca6-b441-019b6826472a)(yeni) butonu tıklanarak İş Tipi Tanımlama/ Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload99ada879-e662-4660-a468-68de7492a73e)

**Açılan ekranda ilgili alanlar tanımlanır:**

**İş Tipi Adı:** İş Tipi Tanımlama ekranında İş Tipi adı bilgisi girildiği alandır.

**Evrak Tipi:** İş Tipi Tanımlama ekranında Evrak Tipi bilgisi sistemde tanımlı olan Belge Listesinden gerekli belgelerin seçildiği alandır.

**Yükleniciler:** İş Tipi Tanımlama ekranında Yüklenici ve iş tipinin ilişkinin kurulduğu alandır. Bu alanda sistemde tanımlı yükleniciler listesinde yada yeni bir Yüklenici tanımlama işlemi yapılarak tanımlanan yüklenicinin seçim yapılır. Yüklenici İş İzni Takibi parametrelerin 20 numaralı “İş tipi Tanımlama sayfasında yükleniciler seçilebilsin mi?” parametre değeri “Evet” seçilerek parametre aktif edildikten sonra görüntülenen alandır.

**İş Tipi Yüklenici ve İç İzni modülleri için kullanılacak mı?:** İş Tipi Tanımlama ekranında Yüklenici ve İç İzni modüllerinde bu iş tipinin kullanılması isteniyorsa ilgili check box işaretlenir.

**Statü:** İş Tipi Tanımlama ekranında İş tipinin Aktif ve Pasif durumun seçilebildiği alandır. Pasif durumundaki iş tipleri iş tipinin seçildiği ekranlarda görüntülenmez ve seçilemez.

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3554c0cf-508a-4bfa-9b55-1257be88d67e)**:**Önceki ekrana geri dönülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload297ed6cb-d953-4704-9f10-0c212d66c0ea)**:**İş tipi ile ilgili gerekli evrak veya dosyaların yüklenmesi işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb22f8163-a421-491d-8941-6dd321754e5b):İş tipi ile ilgili yüklenen gerekli evrak veya dosyanın görüntülenmesi işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9544a598-33b4-49d5-a873-ee1fb9efe181):İş Tipi ile ilgili yüklenen gerekli olan evrak ve dosyaların silinme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6db30afb-e84f-471a-84ca-b799ff7c32db)(Ekle) butonu tıklanarak

Yeni butonu tıklanarak Yeni bir Tedarikçi tanımlama işlemi yapılır yada sistemde tanımlı tedarikçi seçilerek ekleme işlemi yapılır..

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload00ea5518-9573-4a8d-9bc4-d964234fdec2)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb6624a25-5512-456c-bda4-6911ef0bc5c3)

İş tipleri tanımlanır. İş tipi ile gerekli evraklar Evrak listesinde seçimi yapılır. İş tipi yüklenici ilişkisi kurulur ve gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada0467968-7156-47a8-88d3-93ca5429e04b) (kaydet) butonu tıklanarak İş Tipi Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9e18a724-a570-4d70-b2db-1ed7690a63ab)

### **5.1.6.Onay Akışı Tanımlama**

Yüklenici İş İzni Modülü için onay akışı kurgulandıktan sonra Yüklenici İş izinleri onaya gönderilebilir.

1-Açılış

Yüklenici İş İzni verilerinin girildiğine dair açılış bilgisidir.

2-Açma onayı

Yüklenici İş İzni Takibi modülünde akış olarak, Yüklenici iş izni açılırken kullanılması istenen Yüklenici iş izni açma onayını sağlayan kısımdır.

3-IK Değerlendirme

Yüklenici İş İzni Takibi modülünde akış olarak, IK değerlendirmesi istenilirse kullanılan onay kısmıdır.

4-Yüklenici Personel Belirleme (Talepte seçilmiş yükleniciye işe uygun personel belirleme için görev düşer. (SAT/BSAT/Tanımlar/Müşteri-Tedarikçi Tanımlama menüsüne tanımlanmış Tedarikçi tipli Yüklenicilerin mail adresi, sorumlu ve dil alanı bilgisi girilmelidir).Yüklenici Personel Havuzu menüsünde Yüklenici Firma için Yüklenici Personel ve Evrak tanımlama işlemi yapılarak yüklenici Personel Havuza eklenir. Yüklenici Personel Seçimi (17 nolu parametre Evet olduğunda bu onay kullanılır)

**Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Parametreler** menüsüne gelinir. Filtreden Yüklenici İş İzni Takibi Modülü seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadba92132f-b5e9-4d94-bb9f-4b002b069b03)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2d31c718-ae52-4abb-8be3-20f8421a4099)(Ara) butonu tıklanarak liste sekmesinde Yüklenici İş İzni Takibi Modülü ile ilgili parametreler listenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload769f216d-8f28-412e-97f7-150b30f41c6f)

Yüklenici İş İzni Takibi Modülü parametrelerinde 17 numaralı “Yüklenici Personel Seçimi Yüklenici tarafından yapılsın mı?” parametresi seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload20270201-b7c7-453b-bdb7-6ff55a9d89b2)

Parametre seçili iken ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload20089354-0725-4d66-a276-f40b9c0c1e2a)(Değiştir) butonu tıklanarak Parametreler ekranında parametrenin parametre değeri “Evet” seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade67edb88-3e09-4a92-98b2-c88102630d0e)

Parametreler ekranında parametre değeri “Evet” seçilerek parametre aktif edildikten sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc96719a7-cc29-41cc-bad4-a5856f1b00a6)(Kaydet) butonu tıklanarak kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6067e5b0-4d6d-49a3-8bd4-01372edd0d7e)

Yüklenici İş İzni Takibi Modülünde 17 numaralı parametre aktif edildikten sonra IK Değerlendirmesi onayında sonra “Yüklenici Personel Seçimi” aşamasıyla onay devam eder. Öncelikle Entegre Yönetim Sistem/Yüklenici İş İzni Takibi/Yüklenici Personel Havuzu menüsü tıklanılır. Açılan Yüklenici Personel Havuzu ekranında İlgili Yüklenici seçilerek firma için çalışma yapacak Yüklenici Personellerin ve personellere ait evrakların tanımlaması yapılarak havuza ekleme işlemi yapılır. 17 numaralı parametrenın parametre değeri “Hayır” ise IK Değerlendirmesi onayında sonra “Yüklenici Personel Seçimi” aşaması devre dışı kalır. Akış “ISG Değerlendirme” aşaması şeklinde sırasıyla devam eder.

5.Entegre Yönetim Sistem/Yüklenici İş İzni Takibi/Yüklenici Personel Seçimi ekranında Yüklenici Personel Havuzuna eklenen Yüklenici firma için çalışma yapacak personellerin seçimi yapılır.

6-ISG Değerlendirme

Yüklenici İş İzni Takibi modülünde akış olarak, ISG değerlendirmesi istenilirse kullanılan onay kısmıdır.

7-Son Risk Değerlendirme

Yüklenici İş İzni Takibi modülünde akış olarak, son risk değerlendirmesi istenilirse kullanılan onay kısmıdır

8-Açık

Yüklenici İş İzni Takibi modülünde akış olarak, iş izninin açıldığına dair kullanılan onay kısmıdır.

9- Kapalı

Yüklenici İş izninin bitiş tarihi gelince kapatma onayına gönderilir.

Akış tanımlarını **SAT/ BSAT/ Konfigürasyon Ayarları/ Akış Tanımlama** ekranından kontrol edilmeli, yoksa akışları tanımlanmalıdır. Belirtilen akışlar Akış Tanımlama menüsünde tanımlanmalıdır.

**SAT/ BSAT/ Konfigürasyon Ayarları/ Rol Tanımlama** ekranından onay akışları için rol tanımlamaları yapılır. Tanımlanan Roller akışlarla ilişkilendirilmedir.

**SAT/ Tanımlar/ Mesaj Gövdesi Tanımlama** ekranından Yüklenici İş İzni Takibi Modülü için yeni mesaj tanımlamaları yapılır.Tanımlanan mesaj gövdeleri akışlarla ilişkilendirilmesi yapılmalıdır.

**SAT/BSAT/ Konfigürasyon Ayarları/ Alt Modüle Tanımlama** ekranından da akışları kontrol edilmelidir. Alt Modül Tanımlanan menüsünde tanımlanan akışların ilişkilendirilmesi yapılmadır. (Bkz: BSAT Kullanıcı Yardım Dokümanı)

**SAT/ BSAT/ Konfigürasyon Ayarları/ Rol Tanımlama** ekranından onay akışları için rol tanımlamaları yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6fb5a189-377c-49cc-a2f8-390c91acd185)

**Ekranındaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada110947d-b4eb-45ad-92e0-3866bf82ac5a): Yeni bir Rol tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload20089354-0725-4d66-a276-f40b9c0c1e2a): Listede seçili Rol bilgisi güncellenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload805d1143-6659-44ab-b1d9-356f0cbe6450): Listede seçili Rol bilgisi silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d37f646-b90f-4919-b1fb-e18bf923ddd2): Kayıtlar filtrelenerek arama yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc31d644c-a320-4eaa-91a7-b1fa59b3b4ff): Veriler Excel’ e aktarılabilir.

**Rol Tanımı:** İSG Değerlendirmecisi seçili iken ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload20089354-0725-4d66-a276-f40b9c0c1e2a)(Değiştir) butonu tıklanarak Rol Tanımlama/Kayıt Güncelleme ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2fbbf65e-81ac-45ae-9ed5-5ffaa632037d)

**SAT/ Tanımlar/ Mesaj Gövdesi Tanımlama** ekranından Yüklenici İş İzni Takibi Modülü için yeni mesaj tanımlamaları yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload483588b1-f861-4b50-86ea-9636a76676c7)

**Ekranındaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada110947d-b4eb-45ad-92e0-3866bf82ac5a): Yeni bir Mesaj Gövdesi tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload20089354-0725-4d66-a276-f40b9c0c1e2a): Listede seçili Mesaj Gövdesi bilgisi güncellenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload805d1143-6659-44ab-b1d9-356f0cbe6450):Listede seçili Mesaj Gövdesi bilgisi silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d37f646-b90f-4919-b1fb-e18bf923ddd2): Kayıtlar filtrelenerek arama yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc31d644c-a320-4eaa-91a7-b1fa59b3b4ff): Veriler Excel’ e aktarılabilir.

Mesaj Gövdesi seçili iken ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload20089354-0725-4d66-a276-f40b9c0c1e2a)(Değiştir) butonu tıklanarak Mesaj Gövdesi Tanımlama/Kayıt Güncelleme ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfcee94dc-a12c-448c-87b5-4652096413fb)

**SAT/ BSAT/ Konfigürasyon Ayarları/ AkışTanımlama** menüsünden Yüklenici İş İzni Takibi Modülü için akış tanımlamaları yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0032da25-a1f8-4f30-84fd-1c4d3e296b01)

**Ekranındaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada110947d-b4eb-45ad-92e0-3866bf82ac5a): Yeni bir Akış tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload20089354-0725-4d66-a276-f40b9c0c1e2a): Listede seçili Akış bilgisi güncellenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload805d1143-6659-44ab-b1d9-356f0cbe6450):Listede seçili Akış bilgisi silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d37f646-b90f-4919-b1fb-e18bf923ddd2): Kayıtlar filtrelenerek arama yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc31d644c-a320-4eaa-91a7-b1fa59b3b4ff): Veriler Excel’ e aktarılabilir.

Akış Tanımı seçili iken ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload20089354-0725-4d66-a276-f40b9c0c1e2a)(Değiştir) butonu tıklanarak Akış Tanımlama/ Kayıt Güncelleme ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload10ae440f-637b-4db9-83ef-aee570c05dfc)

**Ayrıca SAT/BSAT/ Konfigürasyon Ayarları/ Alt Modüle Tanımlama** ekranından da akışları kontrol edilmelidir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadba962f13-1761-4aff-a509-b473dd2baa0f)

Alt Modül Tanımlama seçili iken ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload20089354-0725-4d66-a276-f40b9c0c1e2a) (Değiştir) butonu tıklanarak Alt Modül Tanımlama ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload18263c2e-1f5f-472f-b7e7-5dc52b8410a0)

### **5.1.7.Anket Soru Listeleri**

**Menü Adı**: Sistem Altyapı Tanımları/ Yüklenici İş İzni Takibi/ Anket Soru Listeleri

Yüklenici İş İzni Takibi Modülü için Anket Soru listelerin ilgili fonksiyonlar için hazırlandığı menüdür. Anket işlemleri Modülü olmayan kullanıcıların Anket işlemleri modülünde açılan Anket şablonu ekranında olduğu gibi bu modülde ilgili fonksiyon için Anket şablonu tasarlaması amacıyla kullanılmaktadır. Bu fonksiyon “İş İzni Kapatma” fonksiyonudur. Anket Soru Listeleri (Yüklenici İş İzni Takibi ) ekranında fonksiyon olarak “İş İzni Kapatma” fonksiyonu seçildiğinde sağ üstteki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc7adc25f-82fd-4991-a5f4-d941e181874a)(sorular) butonu tıklanarak Tedarikçi Değerlendirme modülü mantığında sistemde şablon anketler bu menüde tasarlanıp kaydedilmesi sağlanmaktadır. Şablon anketler tasarlandıktan sonra Yüklenici İş İzni Takibi modülün 1. fonksiyonla ilgili parametresi olan 16 numaralı “Yüklenici İş İzni Formu Şablon Anket Kodu”parametresinin parametre değeri boş ise sistem otomatik olarak anket kodunu parametre değerine tanımlamaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcf56e893-a742-4f43-b17b-7df7225eb171)

**Ekranda bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc7adc25f-82fd-4991-a5f4-d941e181874a):Tanımlanacak ankete soru ekleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc7adc25f-82fd-4991-a5f4-d941e181874a)(Sorular) butonu tıklanarak Anket işlemleri Modülün yapısındaki soru ekleme işlemin yapıldı ekran gibi Yüklenici İş İzni Takibi modülü için ilgili fonksiyon için soru ekleme ekranı görüntülenerek soru seçeneklerinden soru ekleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada50fc8e4-debc-402c-bc29-c27206d22ccc)

Yüklenici İş İzni Takibi Parametrelerinden 16 numaralı “Yüklenici İş İzni Formu Şablon Anket Kodu parametresinin parametre değerine herhangi bir parametre kodu tanımlı olmadığında sistem “Yeni bir anket oluşturulacaktır. Onaylıyor musunuz?” uyarı mesajına tamam butonu tıklanarak anket soruları ekranı görüntülenir. Anket Soruları ekranında soru seçenekleri kullanılarak bir şablon Anket tasarlanır.Şayet parametreye sistemde bir anket kodu tanımlı ise tanımlı olan anketin sorular ekranı güncelleme modunda açılır. Anket Soruları ekranı açılarak sorular ilgili düzenleme, güncelleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7b29c561-3b79-4dae-b926-8311c972f649)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3554d04e-5bdf-4a4d-9df0-ac7f41142d66)**: Geri Butonu:** Bir önceki sayfaya geçişi sağlar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1be84e5e-5f69-470c-8eb9-f5dc92507fe3)**: Yazdır Butonu:** Sorularınızı yazdırmaya sağlayan butondur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddceb63bb-a6c3-4046-8f76-12cd64edf864)**: Başlık Ekle Butonu:** Anketi bölümlendirerek başlık eklemek istenilirse bu buton kullanılır. Her başlık ayıracından sonra tanımlanan sorunun numarası 1 olarak gelir. Butona tıklanıldığında açılan sayfa aşağıdaki gibidir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb0694e49-3499-45a0-b013-1f534e1aa5b3) : **Bilgi Girişi Ekle Butonu:** Anketi dolduran kişilere, serbest bilgi girilmesi gereken sorular sorulduğunda, kullanılan soru tipidir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0ec869e4-83d1-49f9-86a0-1d1a5b9ade07)**: Seçenek Ekle Butonu:** Verilen cevapların belirtilen seçenekler içinden seçilmesi durumunda kullanılır.

**![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload46bc3501-26f5-48e6-91b7-6889bb04a462): Sıralama Ekle Butonu:** Bir sorunun seçeneklerinden tüm seçeneklerin tercih edilip, öncelik sırasına göre listelendiği durumda kullanılır. Seçenekler çoktan\>aza veya azdan\>çoğa doğru sıralanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb2797392-c4f6-4347-87ae-9d477b1d9e3b): **Çoklu Seçim Listesi Ekle Butonu:** Oluşturmak istenilen soruda çok fazla şık mevcutsa ve bunların check list gibi seçilmesi gerekiyor ise, çoklu seçim listesi tipinde soru eklenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddaeb722c-6153-4727-a8c5-41a58f2039b8)**: Açılır Liste Ekle Butonu:** Sorulan sorunun açılır listeden tek cevap seçilmesi durumunda kullanılacak soru tipidir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7bdc768e-d678-4345-9968-91fee386fb50)**:Ön Tanımlı Seçim Ekle butonu:** Bu soru tipi QDMS’de tanımlı personel, müşteri, departman ve ürün alanlarındaki listelerin seçilmesini sağlar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4a4973f8-22d1-4b3e-aa97-f22c40b02777):**Tarih Ekle butonuna:** Tıklanarak açılan ekranda, kullanıcıya tarih seçtirilecek soru eklenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbb2902f8-ed03-4bc6-b43b-2761b5699c4d)**:Ek Dosya Ekle Botunu:** Ankete Ek dosya ekleme işlemi için Ek Dosya alanı oluşturur.

**Örnek Soru seçenekleri ekleme;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddceb63bb-a6c3-4046-8f76-12cd64edf864) (Başlık Ekle) butonu tıklanarak Anket bölümlendirilerek başlık eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1857fe8e-85d3-448d-9abf-566b79077692)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7d9b23b5-c0e5-4943-b6d6-5a4a5dcb9666)

Başlık Metni alanına ilgili başlık bilgisi girilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload26f84685-bf0c-4b4a-a76b-6886940b9d00) (kaydet) butonuyla kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload54d7365b-1432-4224-9e9a-a4a12e711b03)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb0694e49-3499-45a0-b013-1f534e1aa5b3) (Bilgi Girişi Ekle) butonu tıklanarak serbest bilgi girilmesi için tanımlanacak soru tanımlanır. Bir metin alanı oluşturulur ve bu metin alanın kaç satırdan oluşacağında soru tanımlama ekranında ayarlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc25b42b9-3a4b-4c42-938c-1639630bffc2)

**Soru Metni:** Sorulacak soru metni, Türkçe alana yazılır. Diğer dillerde kullanım olması durumunda ilgili dillerin olduğu alana sorulacak soru verisi girilir.

**Satır Sayısı:** Satır sayısı, metnin büyüklüğünü belirlemek için kullanılır. 0 veya 1 olması durumunda cevap verilecek alan tek satır olarak görülür.

Sorulacak sorunun cevap verme zorunluluğu bu alandan belirlenir. Cevap zorunluluğu var ise soru cevaplanmadığında kaydetmeye izin verilmez, uyarı mesajı verilir.

**İlişkili Soru/Seçenek:** Bir sorunun, seçeneklerinden biri ile ilişki kurulduğunda, ilişkili sorunun çıkması istenilirse ilişkili soru/seçenek kısmından bağlantı sağlanır.

Sorulacak soru metni Türkçe alana yazılırak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload26f84685-bf0c-4b4a-a76b-6886940b9d00) (kaydet) butonuyla kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3e5e86f5-6291-44ef-82ad-a9727fe6f9ea)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0ec869e4-83d1-49f9-86a0-1d1a5b9ade07) **(**Seçenek Ekle) butonu tıklanarak verilen cevapların belirtilen seçeneklerden seçilme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0a5c4159-2d48-4cfa-8083-4959b17bc8c5)

**Soru Metni:** Sorulacak soru metni, Türkçe alana yazılır. Diğer dillerde kullanım olması durumunda ilgili dillerin olduğu alana sorulacak soru verisi girilir.

**Seçenek/Puan:** Bu alana sorunun seçenekleri girilir. Eğer anket, puanlı bir anket olacaksa, girilen seçenekler için puan da yazılmalıdır.

Sorulacak sorunun cevap verme zorunluluğu bu alandan belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload591ef729-1d11-460a-ae5e-f05292f02520)

Seçeneklerden 1 veya 1’den fazlasının seçilebilmesi bu alandaki check box’a göre belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0fba1395-fd75-4004-9191-4560405ce1bb)

Seçeneklerin yan yana (Tek Satırlı) veya alt altta (Çok Satırlı) dizili olarak görülmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload425910d9-0b60-4fdf-9d8f-3aa8a64a4adf)

Eğer çok satırlı seçeneği işaretlenirse kolon sayısı diye bir alan çıkar ve sorunun seçenekleri belirlenen değer kadar, kolonda görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload16780bda-4330-4a59-b147-7a2e3d1d8bcd)

**Hesaplama Yöntemi:** Anketin puanlı anket olması durumunda, bu sorunun seçeneklerine verilen puanların hangi yöntemle hesaplanılacağının belirlendiği alandır. Örneğin; 10 kişinin cevaplayacağı anketteki bir sorunun 4 seçeneği ve her bir seçeneğin kendine has puanları vardır. İlk seçeneğin puanının 5 olduğunu varsayarsak, 10 kullanıcının ilk seçeneği seçmesi halinde, bu puanlar toplanarak mı (50) veya ortalaması alınarak mı (5) anketin ortalama puanına dahil edilme durumu belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb5f098a0-6bd2-4e7e-bad5-def6ff97d89b)

**Ağırlıklı Puan:** Anketin puanlı anket olması durumunda sorunun anket içindeki ağırlığının belirlendiği alandır. Tüm sorular eş değer ağırlıktaysa 1 değeri yazılmalıdır. 0 olarak yazıldığı durumda anket puanı hesaplanmaz.

**İlişkili Soru/ Seçenek:** Bir sorunun başka bir sorunun seçeneğindeki şarta bağlı olarak görünmesi istenirse ilişkili soru/seçenek mantığı kullanılır.

İlgili alanlar doldurulduktan sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload26f84685-bf0c-4b4a-a76b-6886940b9d00) (kaydet) butonu tıklanarak kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8b445777-0fed-4fff-bcde-537cf3eb51f5)

Anket Soru Listeleri(Yüklenici İş İzni Takibi ) menüsünde İlgili fonksiyon seçili iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc7adc25f-82fd-4991-a5f4-d941e181874a)(Sorular) butonu tıklanarak açılan Anket soruları ekranında örnek olarak birkaç soru seçeneği tanımlanarak Anket Soru Listeleri(Yüklenici İş İzni Takibi ) tanımlama işlemi yapılır. Diğer soru seçeneklerin tanımlama işlemi Anket İşlemleri Modülünün soru tanımlama ekranındaki aynı şekilde yapılmaktadır. Soru tanımlama işlemi yapıldıktan sonra Anket Soru Listeleri (Yüklenici İş İzni Takibi) menüsü ilgili modülün ilgili parametresi olan 16 numaralı “Yüklenici İş İzni Formu Şablon Anket Kodu” parametresine sistem otomatik olarak anket kodu tanımlar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb3959aff-06eb-4e7a-b730-b7f28d0d99f7)

Anket Soru Listeleri(Yüklenici İş İzni Takibi) menüsü için olduğu gibi sistemde Sistem Altyapı Tanımları/ İlgili Modüller (DÖF, Dış-İç Müşteri Şikayetleri, Denetim, Öneri , Eğitim, İç İş İzni, Aksiyon Yönetimi ) modüllerinde menü yetkilendirmesi yapıldığında içeriğinde bu modüllerin bulunmaktadır. Açılan menüde ilgili fonksiyon seçilerek sağ üstteki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc7adc25f-82fd-4991-a5f4-d941e181874a)(Sorular) butonu tıklanır. Eğer bu fonksiyon için daha önceden ilgili parametreye bir anket kodu verilmişse ve bu anket sistemde mevcutsa, o anketin soru listesi güncelleme modunda açılır ve sorular düzenlenebilir. Diğer durumlarda yeni bir anket oluşturulur, anket kodu ilgili parametreye yazılır. Ondan sonra yine bu yeni oluşturulan anketin soruları güncelleme modunda açılır ve sorular düzenlenebilir.

Bu parametreleri uygulama içinde kullanan yerler, daha önceden olduğu gibi aynı şekilde çalışmaya devam ederler. Anket Modülü satın almamış kullanıcıların anket kullanan modüller için anket oluşturabilmeleri sağlanmıştır.

İlgili Modüller için Modüller içerisinde Anket lisanslı olmasa bile Anket tanımlanabilir. Bu amaçla kullanılan menünün menü yetkisi verildiğinde Qdms Modüllerin ilgili fonksiyonları ve ilgili modüllerin sistemde tanımlı parametrelerinin numaraları aşağıdaki tabloda yer almaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaded02da5a-77e0-4390-985f-7df003a29fc7)

### **5.1.8.Yüklenici İş İzni Takibi Modülü Parametrleri**

**Menü Adı:** Sistem Altyapı Tanımları/ BSAT / Konfigürasyon Ayarları/Parametreler

Yüklenici İş İzni Takibi Modülünün kullanıcının istek ve ihtiyaçlarına göre sistemsel ayarlarının yapıldığı ve bunlara göre parametreleri belirlendiği menüdür. SAT/BSAT/Konfigürasyon Ayarlar/ Parametreler menüsü tıklanılır. Açılan Parametreler ekranında Filtre sekmesinde Modüller alanında Yüklenici İş İzni Takibi Modülü seçillir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada11fe708-5440-488e-bb77-9732d122a804)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload20089354-0725-4d66-a276-f40b9c0c1e2a): Listede seçili parametre değiştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d37f646-b90f-4919-b1fb-e18bf923ddd2): Kayıtlar filtrelenerek arama yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc31d644c-a320-4eaa-91a7-b1fa59b3b4ff): Veriler Excel’ e aktarılabilir.

Modüller alanında Yüklenici İş İzni Takibi Modülü seçildikten sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2d31c718-ae52-4abb-8be3-20f8421a4099)(Ara) butonu tıklanarak Liste sekmesinde Yüklenici İş İzni Takibi Modülü ile ilgili parametrelerin listelenmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload959b648a-9938-4d11-959b-fc26b5647d7e)

Parametreler ekranında listenen parametrelerle ilgili parametre seçili iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2e4a4950-c7db-46ff-8e32-8b51556e38fe)(Değiştir) butonu tıklanarak parametre değeri “Evet” seçili yapılarak parametre aktif edilme, parametre değeri “Hayır” seçili yapılarak parametre değeri pasif edilme veya parametre değerindeki bilgi girişi ile ilgili değiştirme işlemleri yapılır.

## **5.2.Entegre Yönetim Sistemi/Yüklenici İş İzni Takibi**

Yüklenici İş İzni Takibi Modülü Entegre Yönetim Sistemi menüsü altında Yüklenici İş İzni Talep Formu İşlemleri, Yüklenici Personel Havuzu, Yüklenici Personel Seçimi , Çalışma Yapılacak Personeller, Saha Görünümü işlemleri ile Raporların görüntülenmesi gerçekleştirildiği kısımdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload220be8bc-4dfc-45e0-95d8-fb511aee5312)

### **5.2.1.İş İzni Talep Formu İşlemleri**

**Menü Adı**: Entegre Yönetim Sistemi/ Yüklenici İş İzni Takibi/ Yüklenici İş İzni Talep Formu İşlemleri

Yüklenici İş İzinlerinin Taleplerinin tanımlandığı menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload349fb043-dd82-4754-9c6c-440f4134a9bb)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada110947d-b4eb-45ad-92e0-3866bf82ac5a): Yeni bir Yüklenici İş İzni Talep formu tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload20089354-0725-4d66-a276-f40b9c0c1e2a): Listede seçili Yüklenici İş İzni Talep formu bilgisi güncellenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload805d1143-6659-44ab-b1d9-356f0cbe6450): Listede seçili Yüklenici İş İzni Talep formu bilgisi silinebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload097cc1db-5417-4694-a413-119b86f95e1c): Listede seçili Yüklenici İş İzni Talep Formu Pdf formatına görüntüler ve yazdırır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc31d644c-a320-4eaa-91a7-b1fa59b3b4ff):Veriler Excel’ e aktarılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d37f646-b90f-4919-b1fb-e18bf923ddd2): Kayıtlar filtrelenerek arama yapılabilir.

Yüklenici İş İzni Talep Formu İşlemleri ekranına yeni bir Yüklenici İş İzni Talep Formu eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9c17e3c6-0372-4ca6-b441-019b6826472a)(yeni) butonu tıklanarak Yüklenici İş İzni Talep Formu İşlemleri /Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5ed1a3ef-1788-42e5-a060-2a82be5ce9ad)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Form Kodu:** Yüklenici İş İzni Talep Formu kodu bilgisinin sistem tarafından otomatik verildiği alandır. Form Kodu Yüklenici İş İzni Takibi Modülün parametrelerinden 1 numaralı “Form Kodu Şablonu” parametresine tanımlı şablona göre otamatik olarak gelmektedir. Ör:IZIN.\#\#\# Ayrıca sayaç değerinde Yüklenici İş İzni Takibi Modülü parametrelerinde 2 numaralı “Form Kodu Şablonu Sayac” parametresindeki parametre değerindeki sayac değeri göre sistem otomatik olarak şablona atamaktadır. Sayaç Değeri :0 ise Form kodu IZIN.001, IZIN.002 şeklinde sistem form kodları otomatik verilmektedir. Sayaçdaki değere göre form kodları 1 artırılmaktadır.

**Talebi Yapan Tipi:** Yüklenici İş İzni Talep Formunun Talebi Yapan Tipi Departman mı İşyeri mi bilgisinin seçilebildiği alandır. Talebi yapan Tipi Departman seçildiğinde sistemde tanımlı Departman Listesi görüntülenir ve Departman listesinde seçim yapılır.Talebi yapan işyeri seçildiğinde sistemde tanımlı işyeri listesi görüntülenir ve işyeri listesinde seçim yapılır.

**İş Tipi:** Yüklenici İş İzni Talep Formunun İş Tipi bilgisi sistemde tanımlı olan İş Tipi Listesinde seçilebildiği alandır. İş Tipi ve Yüklenici eşleşmesi doğru olmalıdır. İş Tipi Tanımlama menüsünde Yükleniciler alanında tanımlı olan Yüklenici firmanın seçilen iş tiplerini ile ilişkinlendirilmesi alt yapıda yapılmaktadır.

**Yüklenici:**Yüklenici İş İzni Talep formunda Sistem Altyapı Tanımları/Yüklenici İş İzni Takibi/İş Tipi menüsünde İş tipi ve yüklenici eşleşmesi yapılan yüklenicileri listesinde seçim yapılan alandır. İş Tipi ve yüklenici eşleşmesi yapılmadığı takdirde sistem “İş Tipi ve Yüklenici eşleşmesi hatalıdır” uyarı mesajını verir. İş Tipi Tanımlama menüsünde 20 numaralı parametre aktif iken yükleniciler alanı görüntülenir ve bu alanda yüklenici seçim yapılarak İş Tipi ve Yükleniciler eşleşmesi yapılır.

**Planlanan Baş. Tar. :** Yüklenici İş İzni Talep Formunun Planlanan Başlangıç Tarihi bilgisinin takvim alanında belirlendiği alandır.

**Planlanan Bitiş. Tar. :** Yüklenici İş İzni Talep Formunun Planlanan Bitiş Tarihi bilgisi takvim alanında belirlendiği alandır.

**Sorumlu Yönetici:** Alan tanımlama menüsünde tanımlanıp, Fonksiyon Dizanyer sayfasında ilgili fonksiyonun sayfaları ile ilişkilendirilen sistemde tanımlı personel listesinden seçim yapılan personel tipli parametrik kulanıcı tanımlı alandır. Personel listesinde seçim yapılan alandır.

Form sekmesinden departman veya işyeri bazında talebi yapan tipi seçilir. Talebi yapan tipine göre ilgili departman veya işyeri seçilir. İşin planlanan başlangıç ve bitiş tarihleri seçilir. İş tipi seçilir.İş tipi Sistem Altyapı Tanımları / Yüklenici İş İzni Takibi/ İş Tipi Tanımlama menüsünde tanımlanan İş Tipi listesinde seçim yapılır. Yükleniciler alanında Yüklenici seçimi yapılır.Çalışma yapılacak harita sekmesinde departmanın veya işyerinin haritası karşımıza çıkar. Yapılacak işin nerde olduğunu harita üzerinde işaretlenir.

**Departman** **İçin Çalışma yapılacak harita bilgisinin eklenmesi:**

**Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları** menüsünde Modül Sistem Altyapı Tanımları seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload51e5d03e-814c-44e8-91ba-43cc6a3d555a)

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload20089354-0725-4d66-a276-f40b9c0c1e2a)(Güncelle) butonu tıklanarak Dil Ayarları ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3e96cf9c-7190-4e40-be79-abb8f633d044)

Açılan Dil ayarların ekranında Değeri alanına Harita bilgi girişi girilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada0467968-7156-47a8-88d3-93ca5429e04b) (kaydet) butonu tıklanarak alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade26d81eb-7e95-467e-b8b4-d971cd54357d)

**Sistem Altyapı Tanımları/ BSAT/ Tanımlar/ Departman Tanımla** menüsünde İş yerinin Haritası eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfba92c4b-5cfe-41e0-a7aa-4f9b937abb3f)

DepartmanTanımlama/ Yeni Kayıt ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload762a8e99-db55-4d13-91d1-00865618616d) (ekle) butonu yardımıyla tanımlanan Departmanı Haritası eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade8e9f9b2-8988-4423-913c-ebefdc6b3082)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2834571f-5389-42e2-90fd-c5443f0a2a59)

Gerekli alanlar doldurulduktan sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc96719a7-cc29-41cc-bad4-a5856f1b00a6)(Kaydet) butonu tıklanarak Departman Tanımlama işleminde İlgili Departmanın işyeri haritası sisteme yüklenir.

**İş Yeri İçin Çalışma yapılacak harita bilgisinin eklenmesi:**

**Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları** menüsünde Modül Sistem Altyapı Tanımları seçilir. İşyeri için “lblIsyeriHarita” label seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade7cfb82b-7972-4b69-93c9-c43c0c2a99bd)

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload20089354-0725-4d66-a276-f40b9c0c1e2a) (Güncelle) butonu tıklanarak Dil Ayarları ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0edf9ddd-5a10-4610-95f1-4a6f2214df51)

Değeri alanına Harita bilgi girişi girilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada0467968-7156-47a8-88d3-93ca5429e04b) (kaydet) butonu tıklanarak alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload97388ab5-0317-4f81-a49f-94efb581d13d)

**Sistem Altyapı Tanımları/ BSAT/ Tanımlar/ İşyeri Tanımlama** menüsünde İş yerinin Haritası eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfc6b5213-f4da-4a9f-8ab1-69ee66f44e49)

İş yeri Tanımlama/ Kayıt Güncelle ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload762a8e99-db55-4d13-91d1-00865618616d) (ekle) butonu yardımıyla İş yeri Harita eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0930b093-d68b-4f1f-b7af-074017ee7663)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc176257a-1f8e-45b3-88a9-9daa29155932)

**Çalışma Yapılacak Harita sekmesi:** Çalışma yapılacak Harita bilgisinin görüntülendiği sekmedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload980de2d4-acd5-4ac1-bd54-ed607e3bc61a)

Çiz butonu tıklanarak haritada çalışma yapılacak yerler işaretlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload53cd6b53-e355-42d9-876e-1083c2c20a65)

Sil butonu ile çalışma yapılacak işaretli yerler silinir. Güncelle butonu tıklanarak harita ile ilgili herhangi bir düzeltme veya değişiklik yapılır. Kaydet butonu ile Harita üzerinde yapılan değişikler kaydedilir. (+) ve (–) butonları ile harita boyutu büyütülüp küçültülür.

Yüklenici İş iznini Talep Formu oluşturup ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadef7704c4-979a-4e9d-839f-0696921f8aa8) (kaydet) butonuna bastığımız zaman açma onaycısına Yüklenici İş İzni Açma onayına gider.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2eb6e34e-5a97-45f4-ad0d-6bc9f73fc822)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadffadaf91-984d-4919-b6a2-a407a8d5ae97)

Yüklenici İş İzni bekleyen işlerime **“Açma Onayı Bekleyen İş İzinleri Listesi”** görev olarak iş düşecektir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload42e0c76c-0ad2-4c8c-882c-d43b6c603b9b)

İlgili Yüklenici İş İzninin kodu tıklanarak Yüklenici İş İzni onaylama sayfasına ulaşılır. Bu sayfada reddet, Onayla, iptal butonları bulunmaktadır.

**Form sekmesi;**

Form ile ilgili alanlar görüntülenir ve düzenleme yapılacak alanlar üzerinde düzenleme yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada9e29ae2-64a2-48a9-ac40-67d6fd7e593f)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcab7c6da-e1c5-4de8-809a-7fe313dd84af): Önceki ekrana dönülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload516a4ba5-301e-47e0-b8b7-fab1693e3c76): Yüklenici İş İzni talep formu onaylanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaf0b3d85-203f-42c6-a9db-21e7ed6e4b76): Yüklenici İş İzni talep formu reddedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb4632a94-5518-426c-8e55-850b10dcc076): Yüklenici İş İzni talep formu iptal edilir.

**Yüklenici İş İzni Talep formu ekranında bu aşamada yapılacak işlemler:** ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaf0b3d85-203f-42c6-a9db-21e7ed6e4b76) (Reddet) butonu tıkanırsa bu aşamada ret nedeni yazılarak Yüklenici İş İzni Talep Formu reddedilebilir. ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb4632a94-5518-426c-8e55-850b10dcc076)(İptal) butonu tıklanarak bu aşamada İç İş İzni Talep Formu iptal edilebilir. ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload516a4ba5-301e-47e0-b8b7-fab1693e3c76)(Onayla) butonu tıklanılarak bu aşamada Yüklenici İş İzni Talep Formu onaylanır.

**Çalışmaya Yapılacak Harita sekmesi;**

Bu sekmede çalışma yapılacak yerler görünülenir. İstenirse çalışma yapılacak harita üzerinde butonlar yardımıyla düzenleme, güncelleme ve değişiklik yapılıp kaydedilir. Sil butonu ile çalışma yapılacak işaretli yerler silinir. Güncelle butonu tıklanarak harita ile ilgili herhangi bir düzeltme veya değişiklik yapılır. Kaydet butonu ile Harita üzerinde yapılan değişikler kaydedilir. (+) ve (–) butonları ile harita boyutu büyütülüp küçültülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5086a30f-ae98-47b7-b47d-3bdcff7e900c)

Açma Onay aşmasında onaydaki kişi tarafından ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload516a4ba5-301e-47e0-b8b7-fab1693e3c76) (Onayla ) butonu tıklanarak Yüklenici İş İzni Talep Formu onaylanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4a6f26ee-7fb8-4018-9bb3-20317c337ca1)

Açma Onay akışındaki aşamada Yüklenici İş İzni Talep formu onaylanarak “Yüklenici İş İzni İK Onay “aşamasına gönderilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaa0e548c-e5f9-443f-b50b-5293ce03725b)

Yüklenici İş izni Talep Formu ilgili kişinin bekleyen işlerime **“IK Onayı Bekleyen Yüklenici İş İzinleri Listesi”** görev olarak iş düşecektir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadee17777a-12f8-42d2-9f45-ffdfbbc926fd)

İlgili Yüklenici İş İzninin kodu tıklanarak Yüklenici İş İzni onaylama sayfasına ulaşılır. Bu sayfada reddet, Onayla, iptal butonları bulunmaktadır.

**Form sekmesi;**

Form ile ilgili alanlar görüntülenir ve düzenleme yapılacak alanlar üzerinde düzenleme yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb2e09907-585b-46ba-9302-cfba8c286b54)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcab7c6da-e1c5-4de8-809a-7fe313dd84af): Önceki ekrana dönülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload516a4ba5-301e-47e0-b8b7-fab1693e3c76): Yüklenici İş İzni Talep Formu onaylanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaf0b3d85-203f-42c6-a9db-21e7ed6e4b76): Yüklenici İş İzni Talep Formu reddedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb4632a94-5518-426c-8e55-850b10dcc076): Yüklenici İş İzni Talep Formu iptal edilir.

**Yüklenici İş İzni Talep formu ekranında bu aşamada yapılacak işlemler:** İK onayı aşamasında ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaf0b3d85-203f-42c6-a9db-21e7ed6e4b76) (Reddet) butonu tıkanırsa bu aşamada ret nedeni yazılarak Yüklenici İş İzni Talep Formu reddedilebilir. ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb4632a94-5518-426c-8e55-850b10dcc076)(İptal) butonu tıklanarak bu aşamada Yüklenici İş İzni Talep Formu iptal edilebilir. ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload516a4ba5-301e-47e0-b8b7-fab1693e3c76)(Onayla) butonu tıklanılarak bu aşamada Yüklenici İş İzni Talep Formu onaylanır.

**Çalışmaya Yapılacak Harita sekmesi;**

Bu sekmede çalışma yapılacak yerler görünülenir. İstenirse çalışma yapılacak harita üzerinde butonlar yardımıyla düzenleme, güncelleme ve değişiklik yapılıp kaydedilir. Sil butonu ile çalışma yapılacak işaretli yerler silinir. Güncelle butonu tıklanarak harita ile ilgili herhangi bir düzeltme veya değişiklik yapılır. Kaydet butonu ile Harita üzerinde yapılan değişikler kaydedilir. (+) ve (–) butonları ile harita boyutu büyütülüp küçültülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc26b7d69-8788-4a52-a65e-35fea45d0a98)

İK onayı aşamasında onaydaki kişi tarafından ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload516a4ba5-301e-47e0-b8b7-fab1693e3c76) (Onayla) butonu tıklanarak Yüklenici İş İzni Talep Formu onaylanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade64dac41-434e-483e-952b-aa60dc2eb647)

Onaylanan Yüklenici İş İzni Talep formu “Yüklenici Personel Seçimi” aşamasına gelir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload344ead9c-d0d5-4415-8d6a-ae7d8503f272)

Yüklenici İş İzni Takibi Modülünde Yüklenici Personel Seçimi yapılması için öncelikle Yüklenici Personel Havuzu menüsünde çalışma yapacak Personellerin eklenmesi gerekir. Yüklenici Personel Havuzunda personel eklemesi yapılan çalışma yapacak personeller Yüklenici Personel Seçim menüsünde seçim aşaması gerçekleştirilir. Bu aşamaların gerçekleştirilmesi için öncelikle Entegre Yönetim Sistemi/Yüklenici İş İzni Takibi/Yüklenici Personel Havuzu menüsü tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc77a30a-7cff-4770-a93a-5fe699e6d42e)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc8ed4950-df31-413d-8c71-5a58d515e34e):Yüklenici Personel ekleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc8ed4950-df31-413d-8c71-5a58d515e34e)(Yüklenici Personeller) butonu tıklanarak Yüklenici Personel havuzuna eklenecek personel ekleme ekranın açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5248e077-5366-4947-99cb-e4b7842b616f)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada110947d-b4eb-45ad-92e0-3866bf82ac5a): Yeni bir yüklenici personel eklenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload20089354-0725-4d66-a276-f40b9c0c1e2a): Seçili yüklenici personel bilgisi günceller.

Yüklenici Personel ekranına yeni bir Yüklenici Personel eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9c17e3c6-0372-4ca6-b441-019b6826472a)(Yeni) butonu tıklanarak Yüklenici Personel/ Yeni Kayıt ekranı görüntülenir.

Yüklenici Personel Tanımlama yeni kayıt ekranında Kişi/ Ekipman tanımı bilgisi girilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload975f1624-cd3d-46df-bae2-75bcc842f5f4)

Yüklenici Personel Tanımlama yapıldıktan sonra Evraklar sekmesi tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadacce4c45-fc1d-4dc5-9b40-073905d6e6c9)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada110947d-b4eb-45ad-92e0-3866bf82ac5a): Yeni bir Evrak tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload20089354-0725-4d66-a276-f40b9c0c1e2a): Listede seçili Evrak bilgisi günceller.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload805d1143-6659-44ab-b1d9-356f0cbe6450): Listede seçili Evrak bilgisi silinebilir.

Yeni bir Evrak eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9c17e3c6-0372-4ca6-b441-019b6826472a)(yeni) butonu tıklanarak Evrak Tanımlama/ Yeni Kayıt ekranı görüntülenir.

**Ör:**Adli Sicil Kaydı

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7a89011e-10aa-48a0-ad65-958d9d80bcc6)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Evrak Türü:** Evrak türü bilgisi sistemde tanımlı olan evrak listesinden seçilebilir.

**Başlangıç Tarihi:** Evrağın başlangıç tarihi bilgisi girilir.

**Not:** Evrağın not bilgisi girilir.

**Ek Dosyalar:** Evrakla ilgili varsa ek dosyanın yüklendiği kısımdır.

**Ör:**Kaynakçılık Belgesi

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1713b883-a7d3-4795-b18c-0bac1c06fa0e)

Başlangıç Tarihi bilgisi seçilir. Ek dosyalar kısmında eklenecek dosya varsa sistemden eklenir. Geçerlilik tarihi dolmuş evraklar kırmızı olarak kayıt altına alınacaktır. Gerekli bilgiler girildikten sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload04faabbf-1aa1-4df5-9d12-bb65ef592a50) (kaydet) butonu tıklanarak Evrak Tanımlama kayıt işlemi gerçekleştirilir

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload36290660-a861-47f0-8fd4-398b66872ac4)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload914ab8a2-9840-4e23-a3d5-aa1568423642)

Sistem tarafında Yüklenici personellerin onaylama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaa8a3872-2c49-47bd-bd43-98e448cf67d6)

Yüklenici Personel onaylama işleminde sonra Entegre Yönetim Sistemi/Yüklenici İş İzni Takibi/Yüklenici Personel menüsü tıklanarak Yüklenici Personel seçimi işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf4831352-bc68-41ee-93e7-6bbfbe0fd8ce)

Yüklenici firma seçilir. ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc9048be6-863f-4f6d-8d45-b83a649cb9bf)(İleri) butonu tıklanrak Yüklenici personelleri ekranı açılarak Yüklenici personel seçimi yapılır. Bu ekranda Yüklenici firmanın beklenen evraklar listesi Beklenen Evraklar alanında görüntülenir.Diğer alanlar sekmesinde alan tanımlamada tanımlanıp alan havuzuna eklenen alanların Fonksiyon Dizanyer menüsünde 3 numaralı “Yüklenici Personel Seçimi” fonksiyonla varsa ilişkilendirilmiş alanlar görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada8a8ef9a-3f5f-490a-90b7-7ea1c53a135b)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadce0e7cb3-c424-4b84-8cb8-2991819e5c68):Yeni bir Kişi/Ekipman eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8b7a9994-e2e2-4c51-bc46-2ab3374e8299):Listede seçili Kişi/Ekipman bilgisi silinebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload849cfdcd-6757-4f7c-94ba-f8ef233c7778):Kişi/Ekipman Listesinin tümünü siler.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8a20b399-39a8-4083-85a8-be003011f974):Listede seçili Kişi/Ekipman bilgisi onaylanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload500977af-1d25-4767-972e-5d6cd49a07a4):Yüklenici Evrak bilgisi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb132d79c-c616-4b61-86fd-75a0db4978ee):Önceki ekrana dönülür.

Yüklenici Personelleri ekranına yeni bir Kişi/ Ekipman eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadce0e7cb3-c424-4b84-8cb8-2991819e5c68) (Kişi/Ekipman ekle) butonu tıklanır. Açılan Yüklenici Personel ekranına yeni bir Yüklenici Personel eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload529a147c-81a3-483f-9187-d6ba4beceecc)

Yüklenici Personellerin hangi iş tipinde çalışacakları işaretlenir. Çalışacakların iş tipi ile ilgili check box’lar işaretlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7fb7e8cd-1953-42af-877b-65698cea65f0)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload500977af-1d25-4767-972e-5d6cd49a07a4)(Görüntüle) butonu tıklanarak Yüklenici Evrak bilgisi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7371f83f-81e8-4dc3-a8eb-fde623b526c2)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8a20b399-39a8-4083-85a8-be003011f974) (Onayla) butonu tıklanarak listede seçili Kişi/Ekipman bilgisi onaylanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2723338e-156d-4c9f-94b1-73027e635941)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload86ea6a7f-0ee1-436d-8f46-482ec2754b2e)

Yükleni Personel Seçimi işlemi onaylandıktan sonra akış “İSG Değerlendirme Onayı” aşamasıyla devam edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload046f7188-3370-4d3c-8a13-50270970600e)

Onay bekleyen yüklenici Personeli onaylandıktan sonra Yüklenici İş izni formu bekleyen işlerime **“İSG Onayı Bekleyen Yüklenici İş İzinleri Listesi”** görev olarak iş düşecektir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload22c8fbf8-7149-4207-9492-bc4289647b79)

İlgili Yüklenici İş İzninin kodu tıklanarak Yüklenici iş izni onaylama sayfasına ulaşılır. Bu sayfada reddet, Onayla, iptal ve yüklenici personel seçimine dön butonları bulunmaktadır.

**Fom sekmesi;**

Form ile ilgili alanlar görüntülenir ve düzenleme yapılacak alanlar üzerinde düzenleme yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0e3f052a-36f6-4d85-800c-91e8c6dbc4ed)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcab7c6da-e1c5-4de8-809a-7fe313dd84af): Önceki ekrana dönülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload516a4ba5-301e-47e0-b8b7-fab1693e3c76): Yüklenici İş İzni Talep formu onaylanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaf0b3d85-203f-42c6-a9db-21e7ed6e4b76): Yüklenici İş İzni Talep formu reddedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb4632a94-5518-426c-8e55-850b10dcc076): Yüklenici İş İzni Talep formu iptal edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc4e053f-cced-419a-9954-9cec5518d1b6):Yüklenici Personel seçimine dönülür.

**Yüklenici İş İzni Talep formu ekranında bu aşamada yapılacak işlemler:** ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaf0b3d85-203f-42c6-a9db-21e7ed6e4b76) (Reddet) butonu tıkanırsa bu aşamada ret nedeni yazılarak Yüklenici İş İzni Talep Formu reddedilebilir. ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb4632a94-5518-426c-8e55-850b10dcc076)(İptal) butonu tıklanarak bu aşamada Yüklenici İş İzni Talep Formu iptal edilebilir. ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload516a4ba5-301e-47e0-b8b7-fab1693e3c76)(Onayla) butonu tıklanılarak bu aşamada Yüklenici İş İzni Talep Formu onaylanır. ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc4e053f-cced-419a-9954-9cec5518d1b6)(Yüklenici Personel Seçimine Dön) butonu ile Yüklenici Personel seçimine dönülür.

**Çalışmaya Yapılacak Harita sekmesi;**

Bu sekmede çalışma yapılacak yerler görünülenir. İstenirse çalışma yapılacak harita üzerinde butonlar yardımıyla düzenleme, güncelleme ve değişiklik yapılıp kaydedilir. Sil butonu ile çalışma yapılacak işaretli yerler silinir. Güncelle butonu tıklanarak harita ile ilgili herhangi bir düzeltme veya değişiklik yapılır. Kaydet butonu ile Harita üzerinde yapılan değişikler kaydedilir. (+) ve (–) butonları ile harita boyutu büyütülüp küçültülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb9ae623d-24c9-44a2-9b90-e735e8469106)

Çalışma yapacak Kişiler sekmesinde Çalışma yapılacak kişilerin listesi yer alır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc9e3b146-9748-4929-883e-2705afa5d7ff)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada110947d-b4eb-45ad-92e0-3866bf82ac5a):Yeni bir İş tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload20089354-0725-4d66-a276-f40b9c0c1e2a):Listede seçili İş Tanımlama bilgisi güncellenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload805d1143-6659-44ab-b1d9-356f0cbe6450):Listede seçili İş Tanımlama bilgisi silinebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7f23a9ef-f9da-4cc8-87b6-5cc6fb11ae57):Yüklenici Personellerin çalışma saatleri ayarlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7f23a9ef-f9da-4cc8-87b6-5cc6fb11ae57)(Çalışma saatlerini ayarla) butonu tıklanarak Yüklenici Personellerin çalışma tarihleri düzenlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4f2a505b-8b04-46ea-8556-2f7fd4f8206f)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload22101e9d-c280-43ef-8652-18a88722c1f9):Yüklenici Personelin çalışma tarihleri ve saatleri ayarlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload00986001-f52e-4f8b-a583-d70e80b8bd8f):Kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcaf1a13a-bd9b-4df9-b669-1a7141f9bdcf):Çalışma tarihleri düzenleme ekranı kapatılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload22101e9d-c280-43ef-8652-18a88722c1f9) (Çalışma tarihleri oluştur) butonu tıklanarak Yüklenici Personelleri Çalışma Tarihleri düzenleme ekranı açılır. Açılan ekranda çalışma tarihleri, başlama saati, bitiş saati bilgileri düzenlenir. Tüm kullanıcılara uygula check box işaretlenerek Çalışma Tarihleri düzenleme işlemi Tüm Kullanıcılara uygulanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload23c5be45-6501-4ce5-8fff-c856a9721ae2)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload22101e9d-c280-43ef-8652-18a88722c1f9) (Çalışma tarihleri oluştur) butonu tıklanarak tüm Yüklenici Personelleri Çalışma Tarihleri ve saatleri düzenlenir. ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload00986001-f52e-4f8b-a583-d70e80b8bd8f)(Kaydet) butonu tıklanarak Yüklenici Personeli çalışma saatleri düzenleme kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5ace640e-dd18-4f68-a1ac-d9f1e337df63)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload516a4ba5-301e-47e0-b8b7-fab1693e3c76)( Onayla) butonu tıklanarak Yüklenici İş İzni Talep formu onaylanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadeebb34af-98c4-4fc6-ad23-78af87627428)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload42f76353-369f-480b-b27a-df5d412afe51)

İSG Onayı işlemi tamamlandıktan sonra akışlarda Son Risk değerlendirme akışı kurgulanmışsa, Yüklenici İş İzni bekleyen işlerime **“Son Risk Değerlendirme Onayı bekleyen Yüklenici İş İzinleri Listesi ”** görev olarak iş düşecektir. Son risk değerlendirme akışı olmadığı durumda form onaylandığında açık statüsüne gelebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfeb80d58-6f6e-4ed4-8ea2-9875dbb7320f)

İlgili Yüklenici İş İzninin kodu tıklanarak İş İzni onaylama sayfasına ulaşılır. Bu sayfada reddet ve Onayla butonları bulunmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9f29deb1-8c79-4ef6-b52e-4bd52b360ed1)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcab7c6da-e1c5-4de8-809a-7fe313dd84af): Önceki ekrana dönülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload516a4ba5-301e-47e0-b8b7-fab1693e3c76): Yüklenici İş İzni onaylanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaf0b3d85-203f-42c6-a9db-21e7ed6e4b76): Yüklenici İş İzni reddedilir.

**Yüklenici İş İzni Talep formu ekranında bu aşamada yapılacak işlemler:** ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaf0b3d85-203f-42c6-a9db-21e7ed6e4b76) (Reddet) butonu tıkanırsa bu aşamada ret nedeni yazılarak Yüklenici İş İzni Talep formu reddedilebilir.. ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload516a4ba5-301e-47e0-b8b7-fab1693e3c76)(Onayla) butonu tıklanılarak bu aşamada Yüklenici İş İzni Talep Formu onaylanır.

**Çalışmaya Yapılacak Harita sekmesi;** Bu sekmede çalışma yapılacak yerler görünülenir. İstenirse çalışma yapılacak harita üzerinde butonlar yardımıyla düzenleme, güncelleme ve değişiklik yapılıp kaydedilir. Sil butonu ile çalışma yapılacak işaretli yerler silinir. Güncelle butonu tıklanarak harita ile ilgili herhangi bir düzeltme veya değişiklik yapılır. Kaydet butonu ile Harita üzerinde yapılan değişikler kaydedilir. (+) ve (–) butonları ile harita boyutu büyütülüp küçültülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb5446543-7d13-41e6-b94d-54681f590af3)

**Çalışma Yapılacak Kişiler sekmesi;** Yüklenici İş İzni Talep formunda çalışma yapılacak kişilerin ve uygunluk durumu bilgileri yer alır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbcd56683-7593-41ca-8309-0fae2f330288)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload516a4ba5-301e-47e0-b8b7-fab1693e3c76) (Onayla) butonu tıklanarak Yüklenici İş İzni Talep formu onaylanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload56942472-76bc-475d-b9fc-c4b9a50eaa0b)

Yüklenici İş İzni kaydına onay verildikten sonra kayıt açık statüsüne gelecektir. Kapanış tarihi geldiğinde Yüklenici İş İzni kaydı kapama için onaya gidecektir. Kapanış tarihi gelince otomatik olarak kapatma onayına gönderilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload62c55de2-105f-40e8-9086-44289014559c)

### **5.2.2.Çalışma Yapabilecek Personeller**

**Menü Adı**: Entegre Yönetim Sistemi/ Yüklenici İş İzni Takibi/ Çalışma Yapabilecek Personeller

Gün içerisinde çalışma yapacak personellerin listesini belirleyen menüdür. Bu menüde çalışma yapacak personellerin çalışma tarihleri düzenlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfcf9500e-14ee-45bf-8fda-4a00660db698)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7f23a9ef-f9da-4cc8-87b6-5cc6fb11ae57):Çalışma yapacak kişilerin çalışma saatleri ayarlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload22101e9d-c280-43ef-8652-18a88722c1f9): Güncelleme işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7f23a9ef-f9da-4cc8-87b6-5cc6fb11ae57):Çalışma saatlerini ayarla butonu tıklanarak çalışma yapacak personellerin çalışma saatleri düzenlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf9c8f91d-90ae-4998-91aa-df191c1ae71d)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload22101e9d-c280-43ef-8652-18a88722c1f9):Çalışma yapacak kişilerin çalışma saatleri ayarlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload00986001-f52e-4f8b-a583-d70e80b8bd8f):Kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcaf1a13a-bd9b-4df9-b669-1a7141f9bdcf):Çalışma tarihleri düzenleme ekranı kapatılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload22101e9d-c280-43ef-8652-18a88722c1f9)(Çalışma tarihleri oluştur) butonu tıklanarak çalışma yapacak personellerin çalışma tarihleri düzenleme ekranı açılır. Açılan ekranda çalışma tarihleri, başlama saati, bitiş saati bilgileri düzenlenir. Tüm kullanıcılara uygula check box işaretlenerek çalışma tarihleri düzenleme işlemi tüm kullanıcılara uygulanır. Sil butonu ile çalışma tarihi silinebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload22101e9d-c280-43ef-8652-18a88722c1f9) Çalışma tarihleri oluştur butonu tıklanarak çalışma yapacak personellerin çalışma tarihleri ve saatleri düzenlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload165754dc-b499-4dd0-8c0b-0868848edd23)

Çalışma saatlerinin bulunduğu satır çift tıklanarak çalışma saatleri üzerinde değişiklik, güncelleme ve düzenleme yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade54d45f8-4c6f-4980-b448-3cc87b92a59f)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload00986001-f52e-4f8b-a583-d70e80b8bd8f)Kaydet butonu tıklanarak Çalışma Yapacak Kişilerin çalışma saatleri düzenleme kayıt işlemi gerçekleştirilir.

### **5.2.3.Saha Görünümü**

**Menü Adı**: Entegre Yönetim Sistemi/ Yüklenici İş İzni Takibi/ Saha Görünümü

Haritadaki çalışmaların göründüğü rapordur. İşyeri haritası üzerinde giriş yapılan firmaların hangi bölgede çalıştığının gözlemlenmesine yarayan bir rapordur. Bir işyeri için birden fazla iş olması durumunda işlerin tümünün görüntülenmesi sağlanır. Filtre sekmesine gelindiğinde Form Kodu, Talep eden, Talebi Yapan Tipi, Talebi Yapan Departman, Yüklenici, Statü, Planlanan Baş. Tar. ve Planlanan Bit. Tar. gibi alanlar doldurularak bu kriterlere göre filtreleme işlemi gerçekleştirilerek kroki üzerinde yapılmış çalışmaların bilgisi verilebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1940f90c-bf91-4110-8780-249daa906672)Filtre sekmesi tıklanarak örneğin Talebi Yapan Departman alanı Departman listesinden Departman seçilerek ve Yüklenici alanında yüklenici firman seçilerek bu kriterlere göre filtreleme işlemi gerçekleştirilerek Çalışma Yapılacak Harita sekmesinde harita üzerinde yapılmış departman bazlı çalışmalar görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload11f0fa6a-36d7-4d87-adc1-ab941f50c7b3)

### **5.2.4.Sahada Çalışanların Raporu**

**Menü Adı**: Entegre Yönetim Sistemi/ Yüklenici İş İzni Takibi/ Sahada Çalışanların Raporu

Yüklenici İş İzni Takibi Modülünde girişi yapılan tüm Taşeronlar için, çalışan kişi, işe başlangıç – bitiş tarihi, talep eden birim gibi bilgilerin gösterildiği rapordur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc542bb27-2258-489c-b329-76c05df73a96)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4442f68e-834a-456b-8470-b511c493d087)**:**Form seç ekranı açar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload05083185-7dbb-40eb-851d-bda71e0b85b8):Yüklenici Evrak görüntüler.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d37f646-b90f-4919-b1fb-e18bf923ddd2): Kayıtlar filtrelenerek arama yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc31d644c-a320-4eaa-91a7-b1fa59b3b4ff): Veriler Excel’ e aktarılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4995f9ed-58b7-4a39-afe4-c7e171e1ae12)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4442f68e-834a-456b-8470-b511c493d087)(Yeni) butonu tıklanarak Form seç ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6904699a-4d38-4903-9a3f-1bcc9163655a)

Yüklenici İş İzni kaydı listede seçili iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2bb677b8-85b3-41c7-b736-a11aedf0e61d) seç butonu tıklanarak Yüklenici Personellerin listesi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5d13f17f-f0e8-4a9a-a917-eb255038e0e3)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada110947d-b4eb-45ad-92e0-3866bf82ac5a): Yeni bir çalışma yapacak kişi tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload20089354-0725-4d66-a276-f40b9c0c1e2a): Listede seçili çalışma yapacak kişi bilgisi güncellenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload805d1143-6659-44ab-b1d9-356f0cbe6450): Listede seçili çalışma yapacak kişi bilgisi silinebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc09d4562-43b1-4cb2-80f8-8032bc1992f0):Çalışma yapacak kişinin çalışma saatlerin ayarlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6fedc2a6-4ac3-405a-aeed-2c64b49445da):Çalışma Yapacak Kişiler ekranı kapatır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload500977af-1d25-4767-972e-5d6cd49a07a4)(Görüntüle) butonu tıklanarak Yüklenici Evrak bilgisi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf42ae84e-3b92-4540-a76f-339a0d587c4b)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf07296a4-b6a3-43b9-b912-2c6d3b34ac6e)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfb32958b-2b2b-4155-81ce-cd6e6f84b98e) (Excel’e aktar) butonuna basılırsa, sistem otomatik olarak Sahada Çalışanlar Raporunu oluşturup kullanıcıya Excel formatında sunmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6b22d844-1d93-4626-a279-678673332578)

### **5.2.5.Tedarikçi Personelleri Raporu**

**Menü Adı**: Entegre Yönetim Sistemi/ Yüklenici İş İzni Takibi/ Tedarikçi Personelleri Raporu

Tedarikçilerin mevcut çalıştırabileceği personellerini ve bu personellerin bilgilerini gösteren rapordur. Bu raporda hangi Tedarikçinin hangi çalışanının olduğunu, geçerlilik tarihini ve evrak bilgilerinden evrak durumları listelenerek görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd415e98e-061a-4dba-93c8-cb70f2145835)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc31d644c-a320-4eaa-91a7-b1fa59b3b4ff): Veriler Excel’ e aktarılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d37f646-b90f-4919-b1fb-e18bf923ddd2): Kayıtlar filtrelenerek arama yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload500977af-1d25-4767-972e-5d6cd49a07a4):Yüklenici Evrak bilgisi görüntülenir.

Filtre sekmesi tıklanarak örneğin Yüklenici alanı doldurularak bu kritere göre filtreleme işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf6c9fa16-8d46-4ea1-9fd5-df808bd33b7f)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload500977af-1d25-4767-972e-5d6cd49a07a4)(Görüntüle) butonu tıklanarak listede seçili Yüklenici Personelin Yüklenici Evrak bilgisi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7a9396bb-4a4c-4b97-92be-76d2f1d6e9f5)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5ddf55ba-620f-449f-bbe6-758de7d74d77)(Excel’e aktar) butonu tıklanarak Excel formatında Tedarikçi Personelleri Raporu görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7475c2b9-90ce-46ca-900d-e255ae1e5d59)

### **5.2.6.Yüklenici Personel Havuzu**

**Menü Adı**: Entegre Yönetim Sistemi/ Yüklenici İş İzni Takibi/ Yüklenici Personel Havuzu

Yüklenici Personel Belirleme (Talepte seçilmiş yükleniciye işe uygun personel belirleme işlemin yapıldığı menüdür. Müşteri Tedarikçi Tanımlama menüsüne tanımlanmış Tedarikçi tipli Yüklenicilerin mail adresi, sorumlu ve dil alanı bilgisi girildikten sonra tanımlanan bu Tedarikçiler yüklenici personel havuzu menüsünde listede yer alır. Bu menüde Yüklenici İş İzni Talep formda seçilmiş yükleniciye işe uygun personellerin ve Evraklarının tanımlama işlemi yapılır.Tanımlama işleminde sonra yüklenici personel onaylanır. Yükleci Personel Havuzunda Yüklenici Personelin Onaylama işleminden sonra Yükleci Personel Seçimi menüsünde Yükleneci Personel seçimi aşama gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc77a30a-7cff-4770-a93a-5fe699e6d42e)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc8ed4950-df31-413d-8c71-5a58d515e34e):Yüklenici Personel ekleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc8ed4950-df31-413d-8c71-5a58d515e34e)(Yüklenici Personeller) butonu tıklanarak Yüklenici Personel havuzuna eklenecek personel ekleme ekranın açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5248e077-5366-4947-99cb-e4b7842b616f)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada110947d-b4eb-45ad-92e0-3866bf82ac5a): Yeni bir yüklenici personel eklenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload20089354-0725-4d66-a276-f40b9c0c1e2a): Seçili yüklenici personel bilgisi günceller.

Yüklenici Personel ekranına yeni bir Yüklenici Personel eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9c17e3c6-0372-4ca6-b441-019b6826472a)(yeni) butonu tıklanarak Yüklenici Personel/ Yeni Kayıt ekranı görüntülenir.

Yüklenici Personel Tanımlama yeni kayıt ekranında Kişi/ Ekipman tanımı bilgisi girilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload975f1624-cd3d-46df-bae2-75bcc842f5f4)

Yüklenici Personel Tanımlama yapıldıktan sonra Evraklar sekmesi tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadacce4c45-fc1d-4dc5-9b40-073905d6e6c9)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada110947d-b4eb-45ad-92e0-3866bf82ac5a): Yeni bir evrak tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload20089354-0725-4d66-a276-f40b9c0c1e2a): Listede seçili evrak bilgisi günceller.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload805d1143-6659-44ab-b1d9-356f0cbe6450): Listede seçili evrak bilgisi silinebilir.

Yeni bir Evrak eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9c17e3c6-0372-4ca6-b441-019b6826472a)(yeni) butonu tıklanarak Evrak Tanımlama/ Yeni Kayıt ekranı görüntülenir.

**Ör:**Adli Sicil Kaydı

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7a89011e-10aa-48a0-ad65-958d9d80bcc6)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Evrak Türü:** Evrak türü bilgisi sistemde tanımlı olan evrak listesinden seçilebilir.

**Başlangıç Tarihi:** Evrağın başlangıç tarihi bilgisi girilir.

**Not:** Evrağın not bilgisi girilir.

**Ek Dosyalar:** Evrakla ilgili varsa ek dosyanın yüklendiği kısımdır.

**Ör:**Kaynakçılık Belgesi

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1713b883-a7d3-4795-b18c-0bac1c06fa0e)

Başlangıç Tarihi bilgisi seçilir. Ek dosyalar kısmında eklenecek dosya varsa sistemden eklenir. Geçerlilik tarihi dolmuş evraklar kırmızı olarak kayıt altına alınacaktır. Gerekli bilgiler girildikten sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload04faabbf-1aa1-4df5-9d12-bb65ef592a50) (kaydet) butonu tıklanarak Evrak Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload36290660-a861-47f0-8fd4-398b66872ac4)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload914ab8a2-9840-4e23-a3d5-aa1568423642)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaa8a3872-2c49-47bd-bd43-98e448cf67d6)

### **5.2.7.Yükleneci Personel Seçimi**

Yükleneci Personel Havuzu menüsünde tanımlanan Firma için çalışacak Yüklenicilerin Yüklenici Personel Listesinde seçim yapılan menüdür. Açılan Yüklenici Personel Seçimi ekranında Yüklenici Firmalar listenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf4831352-bc68-41ee-93e7-6bbfbe0fd8ce)

Listenen Yüklenici Firmalar listesinden Yüklenici firma seçilir. ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc9048be6-863f-4f6d-8d45-b83a649cb9bf)(İleri) butonu tıklanrak Yüklenici personelleri ekranı açılarak Yüklenici personel seçimi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada8a8ef9a-3f5f-490a-90b7-7ea1c53a135b)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadce0e7cb3-c424-4b84-8cb8-2991819e5c68):Yeni bir Kişi/Ekipman eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8b7a9994-e2e2-4c51-bc46-2ab3374e8299): Listede seçili Kişi/Ekipman bilgisi silinebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload849cfdcd-6757-4f7c-94ba-f8ef233c7778):Kişi/Ekipman Listesinin tümünü siler.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8a20b399-39a8-4083-85a8-be003011f974): Listede seçili Kişi/Ekipman bilgisi onaylanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload500977af-1d25-4767-972e-5d6cd49a07a4): Yüklenici Evrak bilgisi görüntülenir.

Yüklenici Personelleri ekranına yeni bir Kişi/ Ekipman eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadce0e7cb3-c424-4b84-8cb8-2991819e5c68) (Kişi/Ekipman ekle) butonu tıklanır. Açılan Yüklenici Personel ekranına yeni bir Yüklenici Personel eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload529a147c-81a3-483f-9187-d6ba4beceecc)

Eklenen Yüklenici Personelleri yapılacaklar çalışmalar işaretlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7fb7e8cd-1953-42af-877b-65698cea65f0)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload500977af-1d25-4767-972e-5d6cd49a07a4)(Görüntüle) butonu tıklanarak Yüklenici Evrak bilgisi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7371f83f-81e8-4dc3-a8eb-fde623b526c2)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8a20b399-39a8-4083-85a8-be003011f974) (Onayla) butonu tıklanarak listede seçili Kişi/Ekipman bilgisi onaylanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2723338e-156d-4c9f-94b1-73027e635941)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload86ea6a7f-0ee1-436d-8f46-482ec2754b2e)

Onay bekleyen yüklenici Personeli onaylandıktan sonra Yüklenici İş izni formu bekleyen işlerime **“İSG Onayı bekleyenYüklenici İş İzinleri Listesi”** olarak iş düşer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload046f7188-3370-4d3c-8a13-50270970600e)

.
