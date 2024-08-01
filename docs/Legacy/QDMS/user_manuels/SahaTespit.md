---
title: Saha Tespit Yönetimi
description: Saha Tespit Yönetimi Yardım Dokümanı
sidebar_position: 51
---

:::tip Bilgi

İlgili konu başlığına sağ tarafta bulunan navigasyon yardımıyla hızlı bir şekilde ulaşabilirsiniz.

:::


**Saha Tespit Yönetimi Modülü(v.5.24) Kullanıcı Yardım Dokümanı**

Modül Versiyonu: 5.24



# **1.Saha Tespit Yönetimi**

Denetçiler herhangi bir zamanda bir saha turu yaptığından tespit ettiği uygunsuzluklar bağlı olarak o esnada bir bulgu açıp, denetimde soru tanımlayıp planlı yada plansız denetim gerçekleştiği modüldür. Saha Tespit Yönetimi Modülü Saha Denetimi ve Davranış Odaklı Güvenlik Yönetimi olmak üzere iki denetime ayrılmaktadır.Saha Denetimde Planlı ve Plansız Saha Denetimde yapılırken Denetim için önceden soru havuzuna eklenmiş sorular kullanılır. Soru eklenirken soru tanımının (Metin Çok Satırlı) yanı sıra olumlu cevap (Metin), Olumsuz cevap (Metin), nötr Cevap (Metin), ağırlık, puan gibi alanlar mevcuttur.Bu denetimde Sorusuz denetim de olabilir ve Denetim gerçekleştirirken soru varsa cevaplama bölümü dışında ek yorum alanı ve bulgular sekmesi yer almaktadır. Bulgulardan Saha Tespit Yönetimi Modülünün parametrelerinde 1 ve 2 numaralı parametrelerine göre DÖF ve aksiyon açılabilir. Davranış Odaklı Güvenlik Yönetimi Planlı ve Plansız Davranış Odaklı Güvenlik Yönetimi Denetimi yapılır. Aynı Saha Denetimde olduğu gibi Denetim için önceden soru havuzuna eklenmiş sorular kullanılmak zorundadır. Soru eklenirken soru tanımının (Metin Çok Satırlı) yanı sıra olumlu cevap (Metin), olumsuz cevap (Metin), nötr cevap (Metin), ağırlık, puan gibi alanlar Saha Denetimde olduğu gibi yer almaktadır.Saha Denetimde farklı olarak sorusuz denetim de olamaz. Denetim gerçekleştirirken sorunun cevaplama bölümü dışında ek yorum alanı mevcuttur ve ayrıca Bulgu sekmeside bu denetimde bulunmamaktadır.

## 1.1.Sistem Altyapı Tanımları/ Saha Tespit Yönetimi

Saha Tespit Yönetimi modülünü kapsamında alt yapısını oluşturacak tanımlamaların yapıldığı kısımdır. Yapılan tanımlamalara göre giriş ekranında veriler karşımıza çıkmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload320a1cf7-cf6e-4e6e-84af-f70b8400b8d1)



### **1.1.1.Soru Havuzu**

**Menü adı**: Sistem Altyapı Tanımları/ Saha Tespit Yönetimi/ **Soru Havuzu**

Saha Tespit Yönetimi modülünde sorulacak soruların oluşturulduğu menüdür.Tanımlanan sorunun olumlu, olumsuz ve nötr cevap bilgisinin girildiği soruya bir puan verilecekse ağırlık ve puan bilgisinin belirlendiği menüdür. Aynı zamanda sorunun aktif/ pasif özelliği bulunmakta, sorunun bir daha sorulmayacağı durumlarda soru pasife çekilebilmektedir. Böylece geçmişte sorunun sorulduğu denetim kayıtlarında soru kaybolmayacak, yeni denetimlerde ise aktif soru havuzunda yer almayacaktır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb4ddb076-1d0c-427e-89f9-71efbb076b5f)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload02c48cf3-7d02-44ea-abe9-2128db295db0)**: Yeni bir soru tanımlanır.**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload149c4901-7a7e-4084-aca6-af46c2eee3fd)**:Listede seçili** soru bilgisi **ile ilgili herhangi bir düzeltme, değişiklik veya güncelleme yapılır.**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7eda1f87-7000-408f-9570-4ccc685c9be1)**:Listede seçili** soru bilgisi **silinebilir.**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload458f81ee-bb58-4c44-8c80-3e3b40581493)**:**Kayıtlar filtrelenerek arama yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb7e6e75a-4a49-44c9-8164-a18c8ea0d337)**:**Veriler excel’ e aktarılabilir.

Soru havuzu ekranına yeni bir soru eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1fef5a8d-988d-4f5f-be51-2c981b2fc713) (yeni) butonu tıklanarak Soru Havuzu/ Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf2a3e2f6-b053-4f8d-9beb-516f1fc691ea)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Soru:** Soru bilgisi girilir.

**Olumlu Cevap:** Sorunun olumlu cevap bilgisi girilir.

**Olumsuz Cevap:** Sorunun olumsuz cevap bilgisi girilir.

**Nötr Cevap:** Sorunun nötr cevap bilgisi girilir.

**Ağırlık:** Sorunun ağırlık bilgisi girilir.

**Puan:** Sorunun Puan bilgisi girilir.

**Durum:** Sorunun aktif ve pasif durum bilgisi seçilir.

Açılan ekranda soru bilgisi yazılır. Olumlu cevap, olumsuz cevap ve nötr cevap bilgileri girilir. **G**erekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade59f23f4-1827-44e2-aac4-8d535f3be621) (kaydet) butonu tıklanarak soru tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadeb6d6bfc-54ae-48e0-9830-2ef827af6c42)

### **1.1.2.Soru Listesi Tanımlama**

**Menü adı**: Sistem Altyapı Tanımları /Saha Tespit Yönetimi/ **Soru Listesi Tanımlama**

Saha Tespit Yönetimi modülünde soru listesi tanımlama işleminin gerçekleştiği menüdür. Soru havuzunda tanımlanan sorular departman, yönetim sistemi, süreç ismi, zimmet işlemleri, faaliyet işleri gibi “Soru Listesi” oluşturularak kategorize edilebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload29925dae-5cb7-4d11-86e7-fb8972c99928)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf891ba37-18b6-4de1-9d30-4afcefcc1018): Yeni Soru Listesi oluşturulur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc69a2cee-fa84-470d-833a-be5fb72b9bf7): **Listede seçili** soru liste bilgisi **ile ilgili herhangi bir düzeltme, değişiklik veya güncelleme yapılır.**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadde607c47-b7e6-4a54-b305-226b10a91950): **Listede seçili** soru listesi bilgisi silinebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload77a3f434-8b27-434e-bbe4-60ccd47fcd0b): Soru listesine bağlı sorular seçilmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb7e6e75a-4a49-44c9-8164-a18c8ea0d337): Soru listesi verileri excel’e aktarılabilir.

Soru listesi tanımlama ekranına yeni bir soru listesi eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1fef5a8d-988d-4f5f-be51-2c981b2fc713) (yeni) butonu tıklanarak Soru Listesi Tanımlama/ Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6013d55d-e04c-4b00-8984-26a1cf1dd073)

Açılan ekranda liste no sistem tarafından verilir. Soru listesi tanımı bilgisi girilir. **G**erekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade59f23f4-1827-44e2-aac4-8d535f3be621) (kaydet) butonu tıklanarak soru listesi tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb7a171d2-1cdf-4cc4-80e6-66bd3a9cf132)

### **1.1.3.Bulgu Tipleri**

**Menü adı**: Sistem Altyapı Tanımları/ Saha Tespit Yönetimi/ **Bulgu Tipleri**

Saha Tespit Yöntemi modülünde tespit edilen bulguların başlıklarının tanımlanması işleminin gerçekleştiği menüdür. Majör, minör, gözlem vb. tanımlamalar yapılabilir. Belirlenen bulgu tiplerine göre DÖF veya aksiyon açılabilir ya da kullanıcı seçimli yapılabilir. Tanımlanan bir bulgu tipinde, işlem tipi kullanıcı seçimli seçilirse ilgili bulgu için DÖF veya Aksiyon açılması zorunlu tutulmamaktadır. Ancak bir bulgu tipi DÖF veya aksiyon ile ilişkilendirilirse denetim gerçekleştirme aşamasında denetçinin DÖF veya aksiyon açması zorunlu tutulur. Bu amaçlar doğrultusunda ilgili bulgu tipleri tanımlanır. Bu aşamalarda Bulgu Tipi için DÖF ve Aksiyon açılması Denetim Faaliyetleri Modülünde geçerlidir. Bu modülde belirlenen bulgu tipine göre DÖF ve Aksiyon açılması parametrelere göre açılır. Saha Tespit Yönetimi Modülü parametrelerinde 1ve 2 numaralı parametrelere bağlı olarak DÖF ve Aksiyon açılır. Bulgu Tipi menüsündeki İşlem Tipi alanın bu modülde işlevini yoktur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload59d0c877-2c94-429f-92b0-a5267d727ba4)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf891ba37-18b6-4de1-9d30-4afcefcc1018): Yeni bir bulgu tipi tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc69a2cee-fa84-470d-833a-be5fb72b9bf7): **Listede seçili** bulgu tipi bilgisi **ile ilgili herhangi bir düzeltme, değişiklik veya güncelleme yapılır.**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadde607c47-b7e6-4a54-b305-226b10a91950): **Listede seçili** bulgu tipi bilgisi silinebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb7e6e75a-4a49-44c9-8164-a18c8ea0d337) : Veriler excel’e aktarılabilir.

Bulgu tipi tanımlama ekranına yeni bir bulgu tipi eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1fef5a8d-988d-4f5f-be51-2c981b2fc713) (yeni) butonu tıklanarak Bulgu Tipi Tanımlama/ Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9a74b3a4-55d7-44da-977e-b57ed47bdf58)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Bulgu Tipi:** Bulgu tipi bilgisi girilir.

**İşlem Tipi:**İlgili seçeneklerden seçim yapılır. Ör. DÖF Açılsın

**Durum:** Bulgu tipinin aktif veya pasif durumu seçilir.

Açılan ekranda bulgu tipi bilgisi girilir. İşlem tipi seçeneklerinde seçim yapılarak ve Durum kısmı aktif seçilir. Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade59f23f4-1827-44e2-aac4-8d535f3be621) (kaydet) butonu tıklanarak bulgu tipi tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddcb19cb5-2300-41ea-81cd-800d346d05b7)

### **1.1.4.Saha Yönetimi Parametreleri**

**Menü adı**: Sistem Altyapı Tanımları/ Saha Tespit Yönetimi/ Saha Yönetimi Parametreleri

Saha Tespit Yönetimi modülü için kullanıcının istek ve ihtiyaçlarına göre çeşitli ayarlamaların yapılabildiği ve bunlara göre parametrelerin belirlendiği (seçilebildiği) menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcfb11c24-318f-411a-b375-3a164e80a684)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4966a52b-e508-4fc8-a07c-228cb42bcc7c): Listede seçili parametre değiştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload458f81ee-bb58-4c44-8c80-3e3b40581493): Kayıtlar filtrelenerek arama yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb7e6e75a-4a49-44c9-8164-a18c8ea0d337): Veriler excel’ e aktarılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8aecac2b-8665-47bc-ae07-a47095251f5e)

Açılan Saha Tespit Yönetimi Modülü parametreleri ekranında parametrelerle ilgili parametre değerinin “Evet” seçilerek aktif etme, parametre değerini “Hayır” seçilerek parametreyi pasif etme parametre değeri bilgisini girme ve girilen parametre değeri bilgisini değiştirme işlemleri yapılır.

Örnek; Parametre Aktifleme işlemi

Saha Tespit Yönetimi Modülü parametrelerinde 31 numaralı “Denetim ve Bulgu listelerinde yetki kontrollü yapılacak mı?” parametre seçili iken ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4966a52b-e508-4fc8-a07c-228cb42bcc7c)(Değiştir) butonu tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada7ee41cd-c745-4e32-b0d6-074af97bd397)

Açılan parametreler ekranında parametre değeri “ Evet” seçilir

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload29719b99-9d41-4b5c-bb9d-afd829b55d1a)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade59f23f4-1827-44e2-aac4-8d535f3be621)(Kaydet) butonu tıklanarak parametre aktif etme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb24beaaf-a2b6-44d5-a564-f1e6287f678a)

Aynı aşamalar yapılarak parametre değeri “Hayır” seçilerek parametre pasif etme işlemi yapılır ve parametre değerine yeni değeri girilerek parametre değeri bilgisi girilme işlemi yapılır. Yada parametre değeri bilgisi değiştirme işlemi yapılır.

### **1.1.5.Alan Tanımlama**

**Menü adı**: Sistem Altyapı Tanımları/ Saha Tespit Yönetimi/ Alan Tanımlama

Entegre Yönetim Sistemi ekranlarında kullanılması istenilen alanların tanımlandığı menüdür. Burada tanımlanan alanlar alan havuzuna eklenir.Tanımlanan alanlar Saha Tespit Yönetim modülün ilgili menülerin sayfalarıyla ilişkilendirilip, bu alanları menülerin sayfalarında görüntülenmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb0129a57-4a8f-4224-8bac-1c62b1e694d8)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0e8b88e6-046f-4e8d-a224-d2c077500fc4): Yeni bir alan tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbe4032be-3ada-432c-9faa-d89c7df9763a):**Listede seçili alan** bilgisi **ile ilgili herhangi bir düzeltme, değişiklik veya güncelleme yapılır.**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0085e811-7943-48a0-9fe3-289b577c6cf3):**Listede seçili alan** bilgisi **silinebilir.**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5f07eb56-d0c5-44ce-b44a-40ecafcf19fb): Değerler butonu yardımıyla eklenen liste biçimindeki alanının değerleri tanımlanır.

**Alan** tanımlama ekranına yeni bir **alan** eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1fef5a8d-988d-4f5f-be51-2c981b2fc713) (yeni) butonu tıklanarak **Alan** Tanımlama/ Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaaee52e7-6fae-4fa5-af38-393ab3e4f2b7)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Alan Kodu:** Alan kodu bilgisi girilir.

**Alan Adı:** Alan adı bilgisi girilir.

**Başlık Notu:** Alanın başlık notu bilgisi girilir.

**Giriş Tipi:** Alanın giriş tipinin hesaplanan veya veri girişi tipi bilgisi seçilir. Giriş tipi seçeneği oluşturulan alanın manuel olarak veri girişi ile mi yoksa hesaplama yöntemi ile mi belirleneceğini gösterir.

**Alan Tipi**: Alan tipinin bilgisi seçilir. Alan tipi ise oluşturulan alanın metin, nümerik, tarih, liste vb. tiplerinden hangisi olduğunu gösterir.

**Görünme Şartı:** Alanın görünme şartı bilgisi girilir. Liste tipli alanın değerlerine göre oluşturulan alanın görüntülenmesini sağlar.

**Durum:** Alanın durumunun aktif veya pasif olarak bilgisi seçilir.

Açılan ekranda alan kodu ve alan adı bilgisi girilir. Giriş tipi bilgisi, veri girişi ve Alan Tipi bilgisi, personel seçilir. Durum kısmı aktif seçilir. Alan tanımlama ekranında gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade59f23f4-1827-44e2-aac4-8d535f3be621) (kaydet) butonu tıklanarak alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2641695a-2e6a-43d4-8a56-d43c8b60596f)

**Sistemde mevcut bulunan alan tiplerinin tam listesi aşağıda belirtilmiştir;**

**Metin:** Text kutucuğu ekler.

**Metin Çok Satırlı:** Çok satırlı text kutucuğu ekler.

**Nümerik-Parasal:** Parasal değer olarak nümerik giriş yaptırır.

**Nümerik-Birim:** Birim olarak nümerik giriş yaptırır.

**Tarih:** Takvim alanı ekler.

**Liste:** Birden fazla element arasından tek seçim yaptırır.

**Puanlı Liste:** Açılır menüden tekli seçim yaptırır, liste elementlerinin puan değerleri mevcuttur.

**Arama Özellikli Liste:** Açılır menü altından birden fazla seçim yapılmasını sağlar.

**Ağaç Liste:** Ağaç dallanması şeklinde menü altından birden fazla seçim yapılmasını sağlar.

**Personel:** QDMS personel veri tabanından kişi bilgisi seçilebilmesini sağlar.

**Departman:** QDMS departman veri tabanından departman bilgisi seçilebilmesini sağlar.

**Unvan:** QDMS unvan veri tabanından unvan bilgisi seçilebilmesini sağlar.

**Doküman:** QDMS doküman veri tabanından doküman seçilebilmesini sağlar.

**Süreç:** QDMS süreç veri tabanından süreç seçilebilmesini sağlar.

**Yönetim Sistemi:** QDMS yönetim sistemi veri tabanından yönetim sistemi bilgisi seçilebilmesini sağlar.

**Müşteri:** QDMS müşteri veri tabanından müşteri bilgisi seçilebilmesini sağlar.

**Tedarikçi:** QDMS tedarikçi veri tabanından tedarikçi bilgisi seçilebilmesini sağlar.

**Ürün Grubu:** QDMS ürün grubu veri tabanından ürün grubu bilgisinin seçilebilmesini sağlar.

**Ürün:** QDMS ürün veri tabanından ürün bilgisinin seçilebilmesini sağlar.

**Şirket Profili:** QDMS şirket profili veri tabanından şirket profili bilgisi seçilebilmesini sağlar.

**Başlık:** Risk formuna ya da detay ekranına başlık ekler.

**Dosya:** Dosya ekler.

**Resim:** Resim ekler.

**Resim Liste:** Resim listesinden seçim sağlar.

**Çoklu Resim:** Çoklu resim seçilmesini sağlar.

**Tablo:** Tablo verilerinin kullanılmasını sağlar.

**Sorgu:** Sorgulama şeklinde seçim sağlar.

**Sorgu Ağaç:** Ağaç dallanması şeklinde sorgu yapılmasını sağlar.

### **1.1.6.Yetki Matrisi**

**Menü adı**: Sistem Altyapı Tanımları/ Saha Tespit Yönetimi/ Yetki Matrisi

Saha Tespit Yönetimi modülünde kullanımı ile alakalı rol bazlı veya kullanıcı grubu bazlı yetkilendirmelerin yapıldığı menüdür. Genel olarak rol ve kullanıcı gruplarına, denetim ekleme, güncelleme ve silme yetkisi verilebilir. Rolllere yetki vermek için ilgili check-box’lar işaretlenir. Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayaraları/Rol Tanımlama menüsünde Saha Tespit Yönetim Modülü için tanımlı Roller Yetki matrisi ekranında görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4edd33f6-f6f2-4ec2-be6e-c0d61fd3f8ce)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload42fda14a-fbc8-4a6e-bb23-c73976525227) : Kullanıcı grubu ekler.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload75c94402-4a86-437e-8fc7-484bdfef885e) : Kullanıcı grubunu siler.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1b9c2021-5197-4c07-8abf-b4bcf47d61f9) : Tüm kullanıcı gruplarını siler.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6be96480-82a3-4c79-9fc0-d1ecac329026) : Kayıt işlemi gerçekleştirilir.

Grup eklemek için ise ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload42fda14a-fbc8-4a6e-bb23-c73976525227) (Kullanıcı grubu ekle) butonuna basılır daha sonra yetkileri verilir. İstenirse Sistem Altyapı Tanımları/BSAT/Tanımlar/Kullanıcı Grubu Tanımlama menüsünde ilgili modül için Kullanıcı Grubu tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf642cef9-0a31-4c89-8e28-c7ca1ea1d5fb)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc20d987b-e855-48d1-9705-d6dacdb5f0d7) (Seç) butonu tıklanarak kullanıcı grubu eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcdaad36f-cae9-4a53-b364-02fde8e79055)

### **1.1.7.Fonksiyon Dizayner**

**Menü Adı**: Sistem Altyapı Tanımları/ Saha Tespit Yönetimi/ Fonksiyon Dizayner

Fonksiyon Dizayner özelliği ile alan havuzuna eklenen alanlar saha tespit yönetimi modülünün istenilen sayfaları ile ilişkilendirilebilir. Bunun için saha tespit yönetimi modülünün sistem alt yapı tanımları altından fonksiyon dizayner menüsüne gelinir. Açılan ekranda saha tespit yönetimi modülünün alan eklenebilecek fonksiyonları sıralanacaktır. Bu ekranda saha denetim gerçekleştirme, davranış odaklı denetim gerçekleştirme, bulgu tanımlama, saha denetimi tanımlama ve davranış odaklı denetim tanımlama fonksiyonlarında kullanılacak alanlar ve bunların sıralaması ile onay işlemlerindeki hiyerarşi detayı tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2adb0b44-375c-476c-85f6-a7c941fa77fb)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4c929590-98a9-4245-b570-37fc14cca961) (Alanlar) butonu tıklanarak formların detaylarında kullanılacak “Alanlar” belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb27e65ab-fab5-4f84-8e3a-770b8c712ffc)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload08ffc741-ea2f-4947-8bb7-e5d3c2118048): Yeni bir fonksiyon eklenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4966a52b-e508-4fc8-a07c-228cb42bcc7c): **Listede seçili** fonksiyon bilgisi **ile ilgili herhangi bir düzeltme, değişiklik veya güncelleme yapılır.**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0b82885f-6e29-4527-86ff-2b9a423285a5): **Listede seçili** fonksiyon bilgisi silinebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload95b37be9-e125-4d87-9d17-2b522807ad2d): Önceki ekrana geri dönülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4c929590-98a9-4245-b570-37fc14cca961)(Alanlar) butonu ile açılan ekranda seçili fonksiyonda kullanılacak alanlar ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf21d0b6a-db6d-4345-ad7e-6d3ab7f8f897)(Yeni) butonuna tıklanarak belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload32eb1473-e1a8-4ee3-bdaf-ebb3aa0d1899)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Alan Adı:** Alan Tanımlama/ Fonksiyonlar/ Yeni kayıt kısmından alan adı bilgisi seçilir.

**Zorunlu Mu? :** Alanın Zorunlu Mu? bilgisinin evet ya da hayır seçeneklerinden seçilir. Seçilen alanın zorunluğu sorgulatılıyor. Evet seçeneği seçildiğinde alan zorunlu olur.

**Zorunluluk Mesajı:** Seçilen alanın zorunluluk mesajı bilgisi girilir. Zorunlu alanlar doldurulmadığında verilecek uyarı mesajı bilgisi yazılır.

**Sıra No:** Seçilen alanın sıra no bilgisi girilir.

**Varsayılan Rol:** Seçilen alanın varsayılan rol bilgisi onaycı tanımları listesinden seçilebilir. Alanların içerisinde rol ekranında daha önce tanımlanmış bir rol ile getirilecek varsayılan rol alanı doldurulur.

**Varsayılan Değer Değiştirilmesin:** Seçilen alanın varsayılan değer değiştirilmesin bilgisi aktif edilmek istenirse ilgili check box işaretlenir. Seçilen alan varsayılan olarak bir değer getiriyorsa getirdiği değerin değiştirilmemesini sağlar.

**Gridde göster:** Seçilen alanın gridde gösterilmesi aktif edilmek istenirse ilgili check box işaretlenir.

**Satır Sayısı:** Seçilen alanın satır sayısının bilgisi belirlenir.

**Kolon Genişliği:** Seçilen alanın kolon genişliği bilgisi belirlenir.

**Aktif Statü:** Alanın sisteme tanımlanan statülerin hangilerinde aktif olacağını belirler. Bu alanda işaretlenen statülerde ilgili alanın tipine göre işlem gerçekleştirilebilir.

**Görünür Statü:** Alanın sisteme tanımlanan statülerin hangilerinde görüleceğini belirler. Aktif statüsü seçilen alanlar için aynı zamanda görünür statüde en az aktif statü alanında işaretlenen statüler olacak şekilde belirlenmelidir.

**Zorunlu Statü:** **:** Alanın sisteme tanımlanan statülerin hangilerinde zorunlu olacağını belirler.

Açılan ekranda alan bilgileri listeden seçilir, zorunlu bir alan ise kullanıcının bu alanı doldurmadığında çıkacak mesaj tanımlanır, sıra numarası belirlenir. Aktif statü, Görünür Statü ve Zorunlu Statü durumları seçilir. Zorunlu olup olmadığı, gridde gösterilip gösterilmeyeceği, kolon genişliği belirlenerek gerekli tüm alanlar doldurulduktan sonra ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd48a7c38-3d4a-42b7-8933-236eb398bc19) (Kaydet) butonu tıklanarak, ilgili alan için fonksiyon ile ilişkilendirme işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadac7bece2-740d-490c-94a8-741a4bc7729a)

### **1.1.8.E-Posta Ayarları**

**Menü Adı**: Sistem Altyapı Tanımları/ Saha Tespit Yönetimi/ E-Posta Ayarları

E-Posta ayarları ekranında, Saha Tespit Yönetimi Modülü süreçlerinin hangi aşamasında kimlere mail ve sms gönderimi yapılacağı belirlendiği menüdür. E-posta ayarlarından Saha Tespit Yönetimi Mdülünde yer alan “ Denetim Oluşturma Bildirimi’’ kimlere gönderilmesi gerektiği seçilerek, güncellenebilir. Bu işlem için![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb895b8e6-0edd-4050-9f6a-73480f8ebf78)(değiştir) butonu kullanılmalıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload88ca80fe-2361-425d-9f3d-7d221f3104b6)

İlgili roller seçilmek için E-Posta Gitsin mi? check box’ ı işaretlenir. Giden e-postada yazan mail içeriği kullanılacak mesaj gövdesi alanından ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload312f33b5-3ac0-454f-ae23-4c3cc612f37b)(seç) butonuyla seçilir, yanlış eklenen bir mesaj gövdesini silmek içinse ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8a1aa31c-68d1-4114-9c56-f845fbdff01f)(sil) butonu kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload10b52cd7-7bc9-414b-bb37-2fafca46012b)

Değişiklikler yapıldıktan sonra E-Posta ayarlarını kaydetmek için sağ üstte yer alan ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadad04b8a2-c995-40c9-bdcb-222a1916e03a)(Kaydet) butonu kullanılır. Hiçbir değişiklik yapmadan çıkmak için ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload04b0b8df-1a3a-4490-886e-5a1ef2369390)(geri) butonu kullanılır.

## 1.2.Entegre Yönetim Sistemi/Saha Tespit Yönetimi

Saha Tespit Yönetim Modülünde kapsamında Saha Denetimi, Davranış Odaklı Güvenlik Yönetimi Denetiminin gerçekleştiği ve Raporların görüntülendiği kısımdır.

### **1.2.1.Saha Denetimi**

**Menü Adı:** Entegre Yönetim Sistemi/ Saha Tespit Yönetimi/ Saha Denetimi

Saha Tespit Yönetimi modülünde saha denetimin gerçekleştirildiği menüdür. Saha tespit yönetimi planlı saha denetimi ve plansız saha denetimi olmak üzere ikiye ayrılır. Denetim için önceden soru havuza eklenmiş sorulardan seçim yapılır. Soru eklenirken soru tanımının (Metin Çok Satırlı) yanı sıra olumlu cevap (Metin), Olumsuz cevap (Metin), nötr Cevap (Metin), ağırlık, puan gibi alanlar bilgileri girilir.İstenirse sorusuz denetimde yapılalabilir. Denetim gerçekleştirirken soru varsa cevaplama bölümü dışında ek yorum alanı ve bulgular sekmesi ilgili alanların bilgileri girilir. Bulgulardan Saha Tespit Yönetimi Modülünün 1numaralı “DÖF açılabilsin mi?” ve 2 numaralı “Aksiyon açılabilsin mi?”parametrelerine göre DÖF ve aksiyon açılabilmesi sağlanır şeklinde denetim gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf5918a25-4e9a-42a3-84a1-dd01314d1d66)

**Ekrandaki bulunan butonlar yardımıyla**;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload29c200de-979c-4079-8f44-93ae1cbeca1f): Planlı denetim planlar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload91024c68-62f1-44c2-bad2-b9d41c6b26c1): Plansız denetim planlar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload458f81ee-bb58-4c44-8c80-3e3b40581493): Kayıtlar filtrelenerek arama yapılabilir.

**1.Planlı Saha Denetimi**

Planlı saha denetim işleminin gerçekleştiği ekrandır. ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5e470fb4-bde1-40de-9f20-2983ba2da92c)(Denetim Planlama) butonu tıklanarak planlı saha denetim işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload170ba828-a48e-4db7-b7a7-4616e6982d5d)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload08ffc741-ea2f-4947-8bb7-e5d3c2118048): Yeni bir planlı denetim tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4966a52b-e508-4fc8-a07c-228cb42bcc7c): Listede seçili planlı denetim bilgisi güncellenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0b82885f-6e29-4527-86ff-2b9a423285a5): Listede seçili planlı denetim bilgisi silinebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada9e79a9e-046c-4fdb-8a24-63cb7d8ae33f): Denetim soruları ekler.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload341bc115-1611-4c03-bbe8-3f6af412d54e): Denetimi gerçekleştir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload458f81ee-bb58-4c44-8c80-3e3b40581493): Kayıtlar filtrelenerek arama yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb7e6e75a-4a49-44c9-8164-a18c8ea0d337): Veriler excel’ e aktarılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload95b37be9-e125-4d87-9d17-2b522807ad2d): Önceki ekrana geri dönülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1a3f8f7c-1468-44da-84c5-cb5c86f71f44):Raporu alınır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload08ffc741-ea2f-4947-8bb7-e5d3c2118048) (Yeni) botunu tıklanarak denetim tanımlama ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1f905623-ed5a-457d-892b-3bc3056b4dae)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Denetim:** Denetimin adı bilgisi girilir.

**İş Yapacak:** Denetimde işi yapacak kişi bilgisi sistemde tanımlı personel listesinden seçilir.

**Yapılacak Tarih:** Denetim yapılacak tarih bilgisi girilir.

**Denetim Saati:** Denetim yapılacak saat bilgisi girilir.

**Periyodiklik:** Denetimde periyodiklik olup olmayacağı bilgisi seçilir.

**Tekrar Süresi:** Denetimde periyodiklik seçilirse tekrar süresi seçilir.

**Tekrar Periyodu:** Denetimde periyodiklik seçilirse tekrar periyodu bilgisi girilir.

**Bulgu Tipi:** Sistemde tanımlı bulgu tipi seçenekleri seçilir. Sistem Altyapı Tanımları/Saha Tespit Yönetimi/Bulgu Tipleri menüsünde tanımlı bulgu tiplerinde seçim yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload35be2aa0-fb85-40c3-941e-7d1ed12cd8be)

**2. Plansız Saha Denetimi**

Plansız saha denetim işleminin gerçekleştirildiği kısımdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload037ce772-4c23-4379-893d-f87b146f50f4)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload91024c68-62f1-44c2-bad2-b9d41c6b26c1) (Plansız denetim yap) butonu tıklanarak plansız saha denetim işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade6471bfa-6a4d-4c85-8c3f-cd7b279b7231)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Denetim:** Denetimin adı bilgisi girilir.

**Yapılacak Tarih:** Denetim yapılacak tarih bilgisi girilir.

**Denetim Saati:** Denetim yapılacak saat bilgisi girilir.

**Bulgu Tipi:** Sistemde tanımlı bulgu tipi seçeneklerinden seçilir. Sistem Altyapı Tanımları/Saha Tespit Yönetimi/Bulgu Tipleri menüsünde tanımlı bulgu tiplerinde seçim yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload63845f73-dbf5-414a-ab1c-ecbe3a8a6169) (İleri) butonu tıklanır. Denetim soruları ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload31994911-1aa4-4a04-b798-c9c1458a8ca2)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload37b1125b-8c6c-4f6a-a637-e8ae5e964a35): Önceki ekrana geri dönülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf1b20a5c-2ebd-4a59-9b8f-947b4ba3e940): Denetime soru eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2b6a665d-86a4-4a68-b8ae-043b1902be1d): Bir sonraki ekrana geçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf1b20a5c-2ebd-4a59-9b8f-947b4ba3e940)(Soru ekle) butonu tıklanarak soru seç listesi ekranı açılır. Sistem Altyapı Tanımları/Saha Tespit Yönetimi/Soru Havuzu menüsünde tanımlı sorulardan seçim yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadde5ddb4e-0b66-4405-9542-085603ec29da)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf1b20a5c-2ebd-4a59-9b8f-947b4ba3e940): Yeni bir soru tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4ecb6a23-09fd-4e69-9928-a89da00c2e0c): Soru seç listesinde soru seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload458f81ee-bb58-4c44-8c80-3e3b40581493): Kayıtlar filtrelenerek arama yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload37b1125b-8c6c-4f6a-a637-e8ae5e964a35): Önceki ekrana geri dönülür.

Soru seç listesi ekranında soru seçilerek denetime soru eklenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1b82edae-e08c-40ca-be92-b3ed83bb679c)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d892f70-fa8c-4e2c-8b10-2be6ae44ca53) (Seç) butonu tıklanarak seçilen sorular denetime eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb673712b-f2b2-43cd-a078-258d557b6a89)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload63845f73-dbf5-414a-ab1c-ecbe3a8a6169) (İleri) butonu tıklanır. Denetimi gerçekleştir ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4332b682-0421-49ad-bdb7-b118feda2a5d)

Denetim gerçekleştir ekranında zorunlu alan yorum kısmı doldurulur ve sorulara verilecek cevapların seçenekleri seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5fbdba8b-1d76-4ad4-bc5e-b8907ad16a54)

Bulgular sekmesi tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8798ff6e-8327-47c8-9f07-6f21d8c8240b)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload08ffc741-ea2f-4947-8bb7-e5d3c2118048): Yeni bir bulgu tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4966a52b-e508-4fc8-a07c-228cb42bcc7c): Listede seçili bulgu bilgisini güncellenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0b82885f-6e29-4527-86ff-2b9a423285a5): Listede seçili bulgu bilgisi silinebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb7e6e75a-4a49-44c9-8164-a18c8ea0d337): Veriler excel’ e aktarılabilir.

Bulgular sekmesinde ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload08ffc741-ea2f-4947-8bb7-e5d3c2118048)(Yeni) butonu tıklanarak bulgu tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2f203b12-8a0c-4bdf-87b6-ec3c16dd3f73)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Bulgu Özeti:** Bulgu hakkında özet bilgi girilir.

**Bulgu Detayı:** Bulgu hakkında detaylı bilgi girilir.

**Bulgu Tipi:** Bulgu tipleri; majör, minör vb. seçilebilir

**İlgili Soru:** Bulgu ile ilgili soru seçilebilir.

**DÖF Oluştur: :** Döf oluşturmak için ilgili check box işaretlenir.

**Aksiyon Oluştur:** Aksiyon oluşturmak için ilgili check box işaretlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade59f23f4-1827-44e2-aac4-8d535f3be621)(Kaydet) butonu tıklanarak bulgu tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload24f32eb3-6119-492b-916d-0db538e7948b)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade59f23f4-1827-44e2-aac4-8d535f3be621) (Kaydet) butonu tıklanarak denetim kapatma onayına gönderilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada59573ee-90b1-489a-afc7-7ed10251daf9)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc059a436-1659-47b2-82fb-29fa22993600)

#### **1.2.1.1.Saha Denetiminin Onaylama Aşaması**

Onayda bulunan kişinin bekleyen işlerimde “Onay Bekleyen Saha Denetimleri” olarak iş düşecektir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload735d1129-5f71-4e50-8ce7-eacde7b04443)

Onay bekleyen saha denetimleri listesinde denetim kodu üzerindeki link tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadad598910-02ce-4c4f-a8a1-a9991999eebe)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload40b3348c-41f0-49fc-868d-26e9b2e1a72b) : Onay/ Ret açıklama bilgisi girilerek denetim onaylanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload17af7257-f285-4edf-9621-04f70711349e): Onay/ Ret açıklama bilgisi girilerek denetim gerçekleştirilmez.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload458f81ee-bb58-4c44-8c80-3e3b40581493)**: Kayıtlar filtrelenerek arama yapılabilir.**

Denetim gerçekleştir ekranında Onay/ Ret açıklama bilgisi girilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfb248350-6d18-4bae-9838-ff15e2072053) (ret et) butonu tıklanarak denetim ret edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3d481750-c4f7-4c9b-a1e6-e2ea36099d74)

Denetim gerçekleştir ekranında Onay/ Ret açıklama bilgisi girilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload981b25a0-8000-41d4-b518-e9eee22fa84e) (onay) butonu tıklanarak denetim onaylanarak kapatılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd4f73c39-34c8-49c2-9d7e-ae3645b0030e)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf13e9344-5e92-4026-8865-d2845bd4b07f)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5096317c-6612-418b-9823-740ccf3d929f)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1a3f8f7c-1468-44da-84c5-cb5c86f71f44)(Rapor) butonu tıklanarak Saha Denetim Raporu alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0bd70a9e-3cb2-4820-8dca-2c5f3b4908ea)![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade51cdeaa-3aa5-47d2-89ba-2154a2ff78b8)![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload96f71d22-e090-46bb-a653-d41ec612ae59)

**Planlı ve Plansız Saha Denetimde;**

-   Denetim için önceden soru havuzuna eklenmiş sorular da kullanılabilir.
-   Soru eklenirken soru tanımının (Metin Çok Satırlı) yanı sıra olumlu cevap (Metin), Olumsuz cevap (Metin), nötr Cevap (Metin), ağırlık, puan gibi alanlar mevcuttur.
-   Sorusuz denetim de olabilir.
-   Denetim gerçekleştirirken soru varsa cevaplama bölümü dışında ek yorum alanı ve bulgular sekmesi mevcuttur.
-   Bulgulardan Saha Tespit Yönetimi Modülünün parametrelerinden 1 ve 2 numaralı parametrelerine göre DÖF ve aksiyon açılabilir.

### **1.2.2.Davranış Odaklı Güvenlik Yönetimi**

**Menü Adı:** Entegre Yönetim Sistemi/ Saha Tespit Yönetimi/ Davranış Odaklı Güvenlik Yönetimi

Saha Tespit Yönetimi modülünde iş sağlığı güvenliği kapsamında davranış odaklı güvenlik yönetimi denetimin gerçekleştiği menüdür. Sahada personelerin güvensiz davranışlarından kaynaklanan denetimlerdir. Davranış odaklı güvenlik yönetimi denetimi planlı ve plansız denetim olmak üzere ikiye ayrılır. Denetim için önceden soru havuzuna eklenmiş sorular seçim yapılır. Soru eklenirken soru tanımının (Metin Çok Satırlı) yanı sıra olumlu cevap (Metin), olumsuz cevap (Metin), nötr cevap (Metin), ağırlık, puan gibi alanların bilgileri girilir. Bu denetimde sorusuz Denetim gerçekleştirilmez. Denetim gerçekleştirirken sorunun cevaplama bölümü dışında ek yorum alanı bilgisi girilir ve denetim gerçekleştirilir. Saha denetimde olduğu gibi bu denetimde bulgu sekmesi bulunmamaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload74d9c454-4bd0-451f-aef9-2c7ebbc21cb0)

**Ekrandaki bulunan butonlar yardımıyla**;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload29c200de-979c-4079-8f44-93ae1cbeca1f): Planlı davranış odaklı yönetim denetimi planlar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload91024c68-62f1-44c2-bad2-b9d41c6b26c1): Plansız davranış odaklı yönetim denetimi planlar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload458f81ee-bb58-4c44-8c80-3e3b40581493): Kayıtlar filtrelenerek arama yapılabilir.

**1.Planlı Davranış Odaklı Yönetim Denetimi**

Planlı Davranış Odaklı Yönetim Denetimi işleminin gerçekleştiği ekrandır. ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5e470fb4-bde1-40de-9f20-2983ba2da92c)(Denetim Planlama) butonu tıklanarak Planlı Davranış Odaklı Yönetim Denetim işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload53f0a3bd-54b2-4fb2-b6b5-fdcc9db96503)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload08ffc741-ea2f-4947-8bb7-e5d3c2118048): Yeni bir planlı denetim tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4966a52b-e508-4fc8-a07c-228cb42bcc7c): Listede seçili planlı denetim bilgisi güncellenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0b82885f-6e29-4527-86ff-2b9a423285a5): Listede seçili planlı denetim bilgisi silinebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada9e79a9e-046c-4fdb-8a24-63cb7d8ae33f): Denetim soruları ekler.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload341bc115-1611-4c03-bbe8-3f6af412d54e): Denetimi gerçekleştir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload458f81ee-bb58-4c44-8c80-3e3b40581493): Kayıtlar filtrelenerek arama yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb7e6e75a-4a49-44c9-8164-a18c8ea0d337): Veriler excel’ e aktarılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload95b37be9-e125-4d87-9d17-2b522807ad2d): Önceki ekrana geri dönülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1a3f8f7c-1468-44da-84c5-cb5c86f71f44):Saha denetim raporu alınır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload08ffc741-ea2f-4947-8bb7-e5d3c2118048) (Yeni) botunu tıklanarak denetim tanımlama ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9ab75884-e3ef-4053-b1d4-f0c020cd9106)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Denetim:** Denetimin adı bilgisi girilir.

**İş Yapacak:** Denetimde işi yapacak kişi bilgisi sistemde tanımlı personel listesinden seçilir.

**Yapılacak Tarih:** Denetim yapılacak tarih bilgisi girilir.

**Denetim Saati:** Denetim yapılacak saat bilgisi girilir.

**Periyodiklik:** Denetimde periyodiklik olup olmayacağı bilgisi seçilir.

**Tekrar Süresi:** Denetimde periyodiklik seçilirse tekrar süresi seçilir.

**Tekrar Periyodu:** Denetimde periyodiklik seçilirse tekrar periyodu bilgisi girilir.

**Bulgu Tipi:** Sistemde tanımlı bulgu tipi seçenekleri seçilir. Sistem Altyapı Tanımları/Saha Tespit Yönetimi/Bulgu Tipleri menüsünde tanımlı bulgu tiplerinde seçim yapılır.

Denetim tanımlama ekranında gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade59f23f4-1827-44e2-aac4-8d535f3be621) (kaydet) butonu tıklanarak denetim tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8c4c8409-1525-4890-8c5a-4bf9e36b0c7b)

**2. Plansız Davranış Odaklı Yönetim Denetimi**

Plansız davranış odaklı yönetim denetimi işleminin gerçekleştiği kısımdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb7aa92fb-e184-4cd7-b4df-fa7f194d204c)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload91024c68-62f1-44c2-bad2-b9d41c6b26c1) (Plansız denetim yap) butonu tıklanarak plansız davranış odaklı yönetim denetimi işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfa5a7b2e-c5d1-4ea6-8e81-7c96c11e2b42)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Denetim:** Denetimin adı bilgisi girilir.

**Yapılacak Tarih:** Denetim yapılacak tarih bilgisi girilir..

**Denetim Saati:** Denetim yapılacak saat bilgisi girilir.

**Bulgu Tipi:** Sistemde tanımlı bulgu tipi seçenekleri seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload63845f73-dbf5-414a-ab1c-ecbe3a8a6169) (İleri) butonu tıklanır. Denetim soruları ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload67dcc3ac-4eb8-4495-9c90-7631a417b90c)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload37b1125b-8c6c-4f6a-a637-e8ae5e964a35): Önceki ekrana geri dönülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf1b20a5c-2ebd-4a59-9b8f-947b4ba3e940): Denetime soru eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6ae2bece-f738-4b1b-8ae4-136d4583004d): Denetime soru listesi eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2b6a665d-86a4-4a68-b8ae-043b1902be1d): Bir sonraki ekrana geçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf1b20a5c-2ebd-4a59-9b8f-947b4ba3e940)(Soru ekle) butonu tıklanarak soru seç listesi ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4799cd06-a1bc-475b-bfda-734e23c6de45)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf1b20a5c-2ebd-4a59-9b8f-947b4ba3e940):Yeni bir soru tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4ecb6a23-09fd-4e69-9928-a89da00c2e0c):Soru seç listesinde soru seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload458f81ee-bb58-4c44-8c80-3e3b40581493): Kayıtlar filtrelenerek arama yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload37b1125b-8c6c-4f6a-a637-e8ae5e964a35): Önceki ekrana geri dönülür.

Soru seç listesi ekranında soru seçilerek denetime soru eklenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload55f83e70-0c27-4617-b6dc-ace41880c826)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d892f70-fa8c-4e2c-8b10-2be6ae44ca53) Seç butonu tıklanarak seçilen sorular denetime eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb97c5de9-0389-4e4c-8732-d329d49c87fb)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload63845f73-dbf5-414a-ab1c-ecbe3a8a6169) (İleri) butonu tıklanır. Denetimi gerçekleştir ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload50b97751-ef2c-4315-a0c8-d6d83df6fe77)

Denetim gerçekleştir ekranında zorunlu alan yorum kısmı doldurulur ve sorulara verilecek cevapların seçenekleri seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3570b0bc-dd9f-42db-9e6d-4099d1f1be8c)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade59f23f4-1827-44e2-aac4-8d535f3be621) (Kaydet) butonu tıklanarak denetim kapatma onayına gönderilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf09c1a3c-e42a-42e1-9048-45e621c50c3f)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8f401e87-d23a-4f08-b2e0-8afa30cd08b1)

#### **1.2.2.1.Davranış Odaklı Güvenlik Yönetimi Denetimi Onaylama Aşaması**

Onayda bulunan kişinin bekleyen işlerimde “Onay Bekleyen Davranış Odaklı Güvenlik Yönetimi” olarak iş düşecektir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc50e3ee9-90e8-4d0d-afe5-d0d79a6364bc)

Onay Bekleyen Davranış Odaklı Güvenlik Yönetimi Listesinde denetim kodu üzerindeki link tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7a3cb2fd-588f-46d2-9fb4-3414527a98da)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload40b3348c-41f0-49fc-868d-26e9b2e1a72b):Onay/ Ret açıklama bilgisi girilerek denetim onaylanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload17af7257-f285-4edf-9621-04f70711349e): Onay/ Ret açıklama bilgisi girilerek denetim gerçekleştirilmez.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload458f81ee-bb58-4c44-8c80-3e3b40581493)**: Kayıtlar filtrelenerek arama yapılabilir.**

Denetim gerçekleştir ekranında Onay/ Ret açıklama bilgisi girilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfb248350-6d18-4bae-9838-ff15e2072053) (ret et) butonu tıklanarak denetim ret edilebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3d481750-c4f7-4c9b-a1e6-e2ea36099d74)

Denetim gerçekleştir ekranında Onay/ Ret açıklama bilgisi girilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload981b25a0-8000-41d4-b518-e9eee22fa84e) (onay) butonu tıklanarak denetim onaylanarak kapatılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1dd5559f-fae2-45cc-9707-b8432452a670)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadeb57dc15-3533-4f52-81f2-cdce755e0458)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadddfcd373-1385-4077-a9c0-a6b191972a91)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1a3f8f7c-1468-44da-84c5-cb5c86f71f44)(Rapor) butonu tıklanarak Davranış Odaklı Güvenlik Yönetimi Denetim Raporu alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaded0f4e7c-aa2e-4262-bc5a-6023f3968236) ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload024a395d-e34d-4c01-8d33-f686e0d4725b)

**Planlı ve Plansız Davranış Odaklı Güvenlik Yönetimi Denetimi**

-   Denetim için önceden soru havuzuna eklenmiş sorular kullanılmak zorundadır.
-   Soru eklenirken soru tanımının (Metin Çok Satırlı) yanı sıra olumlu cevap (Metin), olumsuz cevap (Metin), nötr cevap (Metin), ağırlık, puan gibi alanlar mevcuttur.
-   **Sorusuz denetim de olamaz.**
-   Denetim gerçekleştirirken soru varsa cevaplama bölümü dışında ek yorum alanı mevcuttur.
-   **Bulgu sekmesi bulunmamaktadır.**

### **1.2.3.Raporlar**

**Menü Adı:** Entegre Yönetim Sistemi/ Saha Tespit Yönetimi/ Raporlar

Saha Tespit Yönetimi modülünde raporların görüntülendiği kısımdır.

#### **1.2.3.1.Aksiyon Raporu**

**Menü Adı:** Entegre Yönetim Sistemi/ Saha Tespit Yönetimi/ Raporlar/ Aksiyon Raporu

Saha Tespit Yönetimi Modülü kapsamında denetimde açılmış aksiyonları listelendiği rapordur.(Aksiyon modülünün kalem detayındaki raporun alt yapısını kullanmaktadır.)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9713f709-aacf-46c0-883a-5a107cef3b53)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload458f81ee-bb58-4c44-8c80-3e3b40581493): Kayıtlar filtrelenerek arama yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb7e6e75a-4a49-44c9-8164-a18c8ea0d337): Veriler excel’ e aktarılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload275e26f2-081d-4ae6-bfe4-a4afd33ffc70): Aksiyon özet raporu alınabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcc5b67e7-f26f-43f8-8ed1-6ca0777812cd): Log görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc48b2340-9e16-478f-aa39-06967603f1d2): Aksiyon çizelge raporu alınabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload91042b46-c30c-41bd-aa87-3ab6dc3540d3)(Excel’e aktar) butonuna basılırsa, sistem otomatik olarak aksiyon raporu oluşturup kullanıcıya excel formatında sunmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfb43b099-9434-447c-a9ab-b225b0b2707f)

#### **1.2.3.2.Bulgu Raporu**

**Menü Adı:** Entegre Yönetim Sistemi/ Saha Tespit Yönetimi/ Raporlar/ Bulgu Raporu

Saha Tespit Yönetimi Modülü kapsamında denetimde açılmış olan bulguların görüntülendiği rapordur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload66ec28c4-0cba-4223-a19f-0f72d2f95825)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload458f81ee-bb58-4c44-8c80-3e3b40581493): Kayıtlar filtrelenerek arama yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb7e6e75a-4a49-44c9-8164-a18c8ea0d337): Veriler excel’ e aktarılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload91042b46-c30c-41bd-aa87-3ab6dc3540d3)(Excel’e aktar) butonuna basılırsa, sistem otomatik olarak bulgu raporu oluşturup kullanıcıya excel formatında sunmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaa6e0ea5-9e16-463a-a7af-d661b4b2abbc)

#### **1.2.3.3.Saha Denetim Raporu**

**Menü adı:** Entegre Yönetim Sistemi/ Saha Tespit Yönetimi/ Raporlar/ Saha Denetim Raporu

Bu rapor üzerinden ilgili denetimlerin tekli raporlarına da erişilebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0614eb5f-f15f-4134-a1a9-1fe21af96843)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload458f81ee-bb58-4c44-8c80-3e3b40581493): Kayıtlar filtrelenerek arama yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb7e6e75a-4a49-44c9-8164-a18c8ea0d337): Veriler excel’ e aktarılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadae8d6fe2-be6f-43d3-abd9-51c899f0cb86): Saha denetim raporu alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload91042b46-c30c-41bd-aa87-3ab6dc3540d3)(Excel’e aktar) butonuna basılırsa, sistem otomatik olarak saha denetim raporu oluşturup kullanıcıya excel formatında sunmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc760b6e6-75c6-415a-a513-8214fdd40d3d)

#### **1.2.3.4.Davranış Odaklı Denetim Raporu**

**Menü adı:** Entegre Yönetim Sistemi/ Saha Tespit Yönetimi/ Raporlar/ Davranış Odaklı Denetim Raporu

Bu rapor üzerinden ilgili denetimlerin tekli raporlarına da erişilebildiği menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8f19067b-ce10-4534-91ff-fc6531e3e43b)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload458f81ee-bb58-4c44-8c80-3e3b40581493): Kayıtlar filtrelenerek arama yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb7e6e75a-4a49-44c9-8164-a18c8ea0d337): Veriler excel’ e aktarılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadae8d6fe2-be6f-43d3-abd9-51c899f0cb86): Davranış odaklı denetim raporu alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload91042b46-c30c-41bd-aa87-3ab6dc3540d3)(Excel’e aktar) butonuna basılırsa, sistem otomatik olarak davranış odaklı denetim raporu oluşturup kullanıcıya excel formatında sunmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload82b09aba-2962-4cf0-baf9-7a5f5d7d7b3d)
