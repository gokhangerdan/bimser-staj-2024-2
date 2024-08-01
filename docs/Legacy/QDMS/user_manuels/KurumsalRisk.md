---
title: Kurumsal Risk Değerlendirme
description: Kurumsal Risk Değerlendirme Yardım Dokümanı
sidebar_position: 26
---

:::tip Bilgi

İlgili konu başlığına sağ tarafta bulunan navigasyon yardımıyla hızlı bir şekilde ulaşabilirsiniz.

:::



**Kurumsal Risk Değerlendirme Modülü(v.5.24) Kullanıcı Yardım Dokümanı**

Modül Versiyonu: 5.24



**1.GİRİŞ:** Kurumsal Risk Değerlendirme Modülünün amacı, şirketin iş yapma şekilleri, hesap verebilme, sosyal sorumluluk, şeffaflık, yatırımcıların haklarının korunması, kurumsal ve kontrol, risk yönetimi gibi birçok yönetim kalitesi kriteri açısından en ideal ortamı elde etmesini sağlamaktır. Kurumsal Risk Değerlendirme Modülü risklerin belirlendiği, hangi risklerin öncelikli olarak çözümlenmesi gerektiğinin değerlendirildiği, risklerin yönetilmesi için stratejiler ve planların geliştirilerek uygulandığı sistematik bir süreçtir.

**2.AMAÇ:** Bu yardım kılavuzunun amacı, QDMS Kurumsal Risk Modülleri implementasyonu sırasında ve sonrasında risk formları ile bu risklerle ilgili alınacak önlemlerin planlanması aşamasında izleyeceği yolu belirlemektir.

**3.SORUMLULUKLAR:** Yönetim Sistemleri Temsilcisi

**4.KISALTMALAR:**

RDF: Risk Değerlendirme Formu

RDFD: Risk Değerlendirme Form Detayı

**5.İŞ AKIŞI:**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4ccbc87f-f555-4c52-8990-89b60cd3af39)



# **6.KURUMSAL RİSK DEĞERLENDİRME**

Kullanılmakta olan Kurumsal Risk Değerlendirme metodolojisinin dijital ortamda takibini sağlama, risk analiz tarihçesini oluşturma ve izleme, risk değerlendirme sonucunda önlemleri belirleme ve takip etme, mevcut risk formlarının sisteme aktarımı, risk formları üzerinde yetki kontrolünü sağlama ile yetkisiz erişimi engellemeyi sağlayan risk değerlendirme modülüdür.

## **6.1.Sistem Altyapı Tanımları/Kurumsal Risk Değerlendirme**

Kurumsal Risk Değerlendirme Modülünü kapsamında altyapısını oluşturmak amacıyla gerekli tanımlamaların yapıldığı kısımdır. Yapılan tanımlamalara göre Entegre Yönetim Sistemi menüsünden girişlerde bu veriler kullanılmakta ve görülmektedir.

### **6.1.1.Kontroller**

#### **6.1.1.1.Kontrol Tanımlama**

**Menü Adı**: Sistem Altyapı Tanımları/Kurumsal Risk Değerlendirme/ Kontroller/ Kontrol Tanımlama

Kontroller QDMS'te Risk Modüllerinde kullanılır. Kontroller 27001 EK A maddesinde geçen maddelerdir ve önlemler sekmesinde gelmektedir. Önlemler sekmesinde her bir risk için kontrol adımı seçebilebilir.Önlemler sekmesinde, seçtiğiniz kontrol maddeleri, QDMS ortamında raporlar başlığında SOA raporu almak istediğinizde karşınıza çıkacaktır.Kısaca Kontroller SOA raporunun hazırlanmasında kullanılmaktadır. 95 nolu parametre evet ise kontroller risk yeni kayıt ekranında sekme olarak karşımıza çıkar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8519bd8b-ec28-4c2d-8730-147ca16432a5)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9f362429-f90a-4625-a725-fbf7a6816676): Yeni bir Kontrol tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada0614f26-24d0-4b72-89e2-e20d74a780df): Listede seçili Kontrol bilgisi güncellenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2ae29da1-4327-419e-9458-8fb3f84dcf85): Listede seçili Kontrol bilgisi silinebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload076b70b0-75aa-467b-80d8-678df037e68d): Veriler Excel’ e aktarılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfcf033eb-a926-4c7d-a621-2f9bb3cd8e9b): Kayıtlar filtrelenerek arama yapılabilir.

Kontrol Tanımlama ekranına yeni bir Kontrol eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload607297d2-f9af-4677-acbd-eca4b368b7fd)(yeni) butonu tıklanarak Kontrol Tanımlama\\Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8356d7c5-7275-4116-9516-e58e3fafd214)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Kontrol Kodu:** Kontrol Tanımlama ekranında Kontrol Kodu bilgisinin girildiği alandır.

**Bağlı Olduğu Kontrol:** Oluşturulma aşamasında olan Üst Kontrol Kodu, bir kontrol kodu tanımının alt kırılımı olması halinde bu alan otomatik dolu gelir. Dolu olarak gelen alanda bağlı olduğu kontrol kodu tanımının adı yazar. Bağlı olduğu üst kırılım silinmek istenildiğinde sağ yanda bulunan ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6d58369d-3cfe-4b88-8d51-868a6f2f9220) (sil) butonu veya değiştirilmek istenildiğinde sağ yanda bulunan ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1625049a-f943-4b53-bbf3-91ba154774cc) (seç) butonu kullanılır. Bağlı olduğu bir üst kontrol yok ise bu alan boş gelir.

**Kontrol Tanımı:** Kontrol Tanımlama ekranında Kontrol Tanım bilgisinin girildiği alandır.

**Açıklama:** Kontrol Tanımlama ekranında Açıklama bilgisinin girildiği alandır.

**Durum:** Kontrol Tanımlama ekranında Aktif ve Pasif durum bilgisinin seçilebildiği alandır.

Kontrol Tanımlama ekranında gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb7126322-0d77-432e-b92a-92ea5055c29b) (kaydet) butonu tıklanarak Kontrol Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload22db39f4-86cd-48f0-bbde-99583d623a76)

### **6.1.2.Alan Tanımlama**

**Menü Adı**: Sistem Altyapı Tanımları/Kurumsal Risk Değerlendirme/ Alan Tanımlama

Kurumsal Risk Değerlendirme Modülünün risk formu ve risk detayı ekranlarında yer alacak bütün alanların tanımlandığı yerdir. Burada oluşturulan alanlar, alan havuzuna kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7a9ee5ad-883d-4555-ba25-7f998b74bd49)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9f362429-f90a-4625-a725-fbf7a6816676): Yeni bir alan eklenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada0614f26-24d0-4b72-89e2-e20d74a780df): Var olan alanda değişiklik yapılmak istenirse kullanılır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2ae29da1-4327-419e-9458-8fb3f84dcf85): İlgili alanı silmek için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload185f3252-343c-4633-881e-a754b1232c81): Liste biçiminde alanların elementleri tanımlanır.

Alan Tanımlama ekranına yeni bir alan eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload607297d2-f9af-4677-acbd-eca4b368b7fd)(yeni) butonu tıklanarak Alan Tanımlama\\Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8ebffdef-dff8-483a-90ff-e531330abf94)![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade52f2095-e5cd-4017-885c-adc263a97d09)  
**Açılan ekranda ilgili alanlar tanımlanır:**

**Alan Kodu:** Alan Tanımlama ekranında Alan Kodu bilgisinin girildiği alandır.

**Alan Adı:** Alan Tanımlama ekranında Alan Adı bilgisinin girildiği alandır.

**Başlık Notu:** Alan Tanımlama ekranında Başlık Notu bilgisinin girildiği alandır.

**Giriş Tipi:** Alan Tanımlama ekranında Giriş tipinin Hesaplanan veya Veri Girişi tipi bilgisinin seçilebildiği alandır. Giriş Tipi seçeneği oluşturulan alanın manuel olarak veri girişi ile mi yoksa hesaplama yöntemi ile mi belirleneceğini gösterir.

**Alan Tipi**: Alan Tanımlama ekranında alan tipinin bilgisinin seçilebildiği alandır. Alan Tipi ise oluşturulan alanın metin, numerik, tarih, liste vb. tiplerinden hangisi olduğunu gösterir.

**Görünme Şartı:** Alan Tanımlama ekranında Görünme Şartı bilgisinin girildiği alandır. Liste tipli alanın değerlerine göre oluşturulan alanın görüntülenmesini sağlar.

**Durum:** Alan Tanımlama ekranında durumun aktif veya pasif olarak bilgisinin seçilebildiği alandır.

Açılan ekranda alan kodu ve alan adı bilgisi girilir. Giriş Tipi Veri Girişi ve Alan Tipi Metin Çok Satırlı seçilir. Durum kısmı Aktif seçilir. Alan Tanımlama ekranında gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb7126322-0d77-432e-b92a-92ea5055c29b) (kaydet) butonu tıklanarak Alan Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload314cf943-46ef-4939-a282-4a1d5b450b1c)

Giriş Tipi olarak Veri girişi ve Hesaplanan olarak iki tür seçim mevcuttur. Hesaplama dışındaki her durum için Veri giriş tipi seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd8b99484-1082-49db-9d24-390401f05f32)

Eğer havuza eklenen alanlar Liste, Puanlı Liste, Arama Özellikli Liste ya da Puanlı Liste türlerinden biriyse ve ilgili alan seçildiği takdirde ekranın sağ üst köşesindeki butonlar arasında ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload185f3252-343c-4633-881e-a754b1232c81)(Değerler) butonu ortaya çıkacaktır. Bu buton yardımıyla eklenen liste biçimindeki alanın elementleri tanımlanır.

Örnek amacıyla puanlı liste tipinde Frekans alanı eklendi.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf6a27324-aea0-4c1b-a9b7-8fac37b77fa5)

Bu alan seçili iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload185f3252-343c-4633-881e-a754b1232c81)(değerler) butonu tıklanırsa, Frekans alanının liste elemanlarının tanımlanacağı ekrana ulaşılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadeb4b5b4c-f248-4217-976a-69c9f97ddd61)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9f362429-f90a-4625-a725-fbf7a6816676): Alanın yeni değeri tanımlar.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada0614f26-24d0-4b72-89e2-e20d74a780df): Listede seçili değer bilgisi güncellenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2ae29da1-4327-419e-9458-8fb3f84dcf85): Listede seçili değer bilgisi silinebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload076b70b0-75aa-467b-80d8-678df037e68d): Veriler Excel’ e aktarılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade354c077-0a5b-445f-ba37-f23516bb3eb3):Değer aktarım şablonu indirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7b6fed35-81d0-49ed-82a8-3978d32ba481): Şablon yüklenilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfcf033eb-a926-4c7d-a621-2f9bb3cd8e9b): Kayıtlar filtrelenerek arama yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5ac9de4a-2e37-4995-ac88-e6f03ab89151): Önceki ekrana geri dönülür.

Değerler tanımlama ekranına yeni bir değer eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload607297d2-f9af-4677-acbd-eca4b368b7fd)(yeni) butonu tıklanarak Değerler Tanımlama\\Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd1822d96-28a9-478d-a73f-66147d2e157f)![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7a5e71a0-50ea-4a64-b075-ac9fe572431e)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Tanım:** Değerler ekranında Değer adının bilgisinin girildiği alandır.

**Açıklama:** Değerler ekranında Açıklama bilgisinin girildiği alandır.

**Değer:** Değerler ekranında değerin puanın bilgisinin girildiği alandır.

**Durum:** Değerler ekranında Değerin Aktif ve Pasif durumun bilgisinin seçilebildiği alandır.

**Varsayılan:** Değerler ekranında Varsayılan bilgisi aktif edilecekse ilgili check box işaretlenir. Liste değeri alanların değerlerinde varsayılan olarak seçili gelmesi istenen alan için işaretlenir.

**Önlem Zorunlu Mu?** : Değerler ekranında Önlem Zorunlu Mu? bilgisi aktif edilecekse ilgili check box işaretlenir. Alanın Liste değeri seçildiğinde mutlaka önlem aldırılmasını sağlayan alandır.

Açılan ekranda değerin tanım ve puan bilgisi girilir. Durum kısmı Aktif seçilir. Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb7126322-0d77-432e-b92a-92ea5055c29b) (kaydet) butonu tıklanarak Değerler kayıt işlemi gerçekleştirilir

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload65e93ac3-f2f5-4a62-9d6f-5accbecbe308)

Sistemde mevcut bulunan alan tiplerinin tam listesi aşağıda belirtilmiştir;

-   **Metin:** Text kutucuğu ekler.
-   **Metin Çok Satırlı:** Çok satırlı text kutucuğu ekler.
-   **Nümerik-Parasal:** Parasal değer olarak nümerik giriş yaptırır.
-   **Nümerik-Birim:** Birim olarak nümerik giriş yaptırır.
-   **Tarih:** Takvim alanı ekler.
-   **Liste:** Birden fazla element arasından tek seçim yaptırır.
-   **Puanlı Liste:** Açılır menüden tekli seçim yaptırır, liste elementlerinin puan değerleri mevcuttur.
-   **Arama Özellikli Liste:** Açılır menü altından birden fazla seçim yapılmasını sağlar.
-   **Ağaç Liste:** Ağaç dallanması şeklinde menü altından birden fazla seçim yapılmasını sağlar.
-   **Personel:** QDMS Personel veri tabanından kişi bilgisi seçilebilmesini sağlar.
-   **Departman:** QDMS Departman veri tabanından departman bilgisi seçilebilmesini sağlar.
-   **Ünvan:** QDMS Unvan veri tabanından ünvan bilgisi seçilebilmesini sağlar.
-   **Doküman:** QDMS Doküman veri tabanından doküman seçilebilmesini sağlar.
-   **Süreç:** QDMS Süreç veri tabanından süreç seçilebilmesini sağlar.
-   **Yönetim Sistemi:** QDMS Yönetim Sistemi veri tabanından yönetim sistemi bilgisi seçilebilmesini sağlar.
-   **Müşteri:** QDMS Müşteri veri tabanından müşteri bilgisi seçilebilmesini sağlar.
-   **Tedarikçi:** QDMS Tedarikçi veri tabanından tedarikçi bilgisi seçilebilmesini sağlar.
-   **Ürün Grubu:** QDMS Ürün Grubu veri tabanından ürün grubu bilgisinin seçilebilmesini sağlar.
-   **Ürün:** QDMS Ürün veri tabanından ürün bilgisinin seçilebilmesini sağlar.
-   **Şirket Profili:** QDMS Şirket Profili veri tabanından şirket profili bilgisi seçilebilmesini sağlar.
-   **Başlık:** Risk formuna ya da detay ekranına başlık ekler.
-   **Dosya:** Dosya ekler.
-   **Resim:** Resim ekler.
-   **Resim Liste:** Resim listesinden seçim sağlar.
-   **Çoklu Resim:** Çoklu resim seçilmesini sağlar.
-   **Tablo:** Tablo verilerinin kullanılmasını sağlar.
-   **Sorgu:** Sorgulama şeklinde seçim sağlar.
-   **Sorgu Ağaç:** Ağaç dallanması şeklinde sorgu yapılmasını sağlar.

### **6.1.3.Fonksiyon Dizayner**

**Menü Adı**: Sistem Altyapı Tanımları/Kurumsal Risk Değerlendirme/ Fonksiyon Dizayner

Fonksiyon Dizayner özelliği ile alan havuzuna eklenen alanlar Kurumsal Risk Değerlendirme Modülünün istenilen sayfaları ile ilişkilendirilebilir. Bunun için Kurumsal Risk Değerlendirme Modülünün sistem altyapı tanımları altından Fonksiyon Dizayner menüsüne gelinir.Açılan ekranda Kurumsal Risk Değerlendirme Modülünün alan eklenebilecek fonksiyonları sıralanacaktır. Bu ekranda Kaynak Grubu Tanımlama, Kaynak Tanımlama, Risk Değerlendirme Form Tanımlama, Risk Değerlendirme Detay, Önlem Tanımlama ve Kontrol Tanımlama fonksiyonlarında kullanılacak alanlar ve bunların sıralaması ile onay işlemlerindeki hiyerarşi detayı tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4ce7aeac-d524-4e58-a756-1a3d36173812)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb19c6748-c7f4-43a7-9069-14439f5c882f)(Alanlar) butonu ile formların detaylarında kullanılacak “Alanlar” belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5056d758-5f95-43a3-b449-a2b8480c8bff)

**Ekranındaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9f362429-f90a-4625-a725-fbf7a6816676): Yeni bir Fonksiyon tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada0614f26-24d0-4b72-89e2-e20d74a780df): Listede seçili Fonksiyon bilgisi güncellenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2ae29da1-4327-419e-9458-8fb3f84dcf85): Listede seçili Fonksiyon bilgisi silinebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5ac9de4a-2e37-4995-ac88-e6f03ab89151): Önceki ekrana geri dönülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb19c6748-c7f4-43a7-9069-14439f5c882f)(Alanlar) butonu ile açılan ekranda seçili Fonksiyonda kullanılacak alanlar ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload607297d2-f9af-4677-acbd-eca4b368b7fd) (Yeni) butonuna tıklanarak belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf4de8976-c552-4d87-bb3c-4f5633a8e4cf) ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7646d5b9-c6e2-42a7-bd13-3d3f661ffcab)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Alan Adı:** Alan Tanımlama/Fonksiyonlar ekranında Alan Adı Bilgisinin seçilebildiği alandır.

**Zorunlu Mu? :** Alan Tanımlama/Fonksiyonlar ekranında Zorunlu Mu? bilgisinin Evet ya da Hayır seçeneklerinden seçilebildiği alandır. Alanın zorunluğu sorgulanıyor. Evet seçildiğinde alan zorunlu oluyor.

**Zorunluluk Mesajı:** Alan Tanımlama/Fonksiyonlar ekranında Zorunluluk Mesajı bilgisinin girildiği alandır. Zorunlu alanlar doldurulmadığında verilecek uyarı mesajı yazılır.

**Sıra No:** Alan Tanımlama/Fonksiyonlar ekranında Sıra No bilgisinin girildiği alandır.

**Gridde göster:** Alan Tanımlama/Fonksiyonlar ekranında Gridde Göster aktif edilmek istenirse ilgili check box işaretlenir. RDF ve RDFD’de tanımlama ekranlarında hangi alanların gösterileceğini belirler.

**Seçimde Göster:** Alan Tanımlama/Fonksiyonlar ekranında Seçimde Göster aktif edilmek istenirse ilgili check box işaretlenir. Riskte oluşturulan alanın başka modüllerle ilişkisi kurulduğunda gösterilecek alanları belirler.

**Satır Sayısı:** Alan Tanımlama/Fonksiyonlar ekranında satır sayısının bilgisinin belirlendiği alandır.

**Kolon Genişliği:** Alan Tanımlama/Fonksiyonlar ekranında Kolon Genişliği bilgisinin belirlendiği alandır.

**İlişkili Sekme:** Alan Tanımlama/Fonksiyonlar ekranında İlişkili sekmede ilgili sekme seçildiği alandır.

Açılan ekranda alan Adı seçilir. Zorunlu mu? bilgisi Hayır seçeneği tıklanır. Sıra no ve kolon genişliği bilgisi girilir. Gridde göster bilgisi ilgili check box işaretlenir. Gerekli tüm alanlar doldurulduktan sonra ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaf47b321-2a29-4c20-98b1-e6ef53b95c9d)(kaydet) butonuyla, ilgili alan için ilgili fonksiyon tanımlama işlemi gerçekleştirilmiş olur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4d1f1d4d-0797-4782-8fc9-c4428e6e4d4d)

### **6.1.4.Risk Dağılım Matrisi Tanımlama**

**Menü Adı**: Sistem Altyapı Tanımları/Kurumsal Risk Değerlendirme/ Risk Dağılım Matrisi Tanımlama

Risk Dağılım Matrisi Tanımlamadaki amaç, belirlenen parametrelere göre risk dağılımın hangi aralıklarda daha yoğun olduğunu tespit etmektir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadac96aefe-27be-4f46-a0af-b4794ac384d5)

**Ekranındaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9f362429-f90a-4625-a725-fbf7a6816676): Yeni Risk Dağılım Matrisi tanımlar.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada0614f26-24d0-4b72-89e2-e20d74a780df): Listede seçili Risk Dağılım Matrisi bilgisi günceller.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2ae29da1-4327-419e-9458-8fb3f84dcf85): Listede seçili Risk Dağılım Matrisi bilgisini siler.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload092aa2b3-f96d-4330-b932-8f40b8a1d0d4):Risk Dağılım Matrisini renklendirir.

Risk Dağılım Matrisi Tanımlama ekranına yeni bir Risk Dağılım Matrisi eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload607297d2-f9af-4677-acbd-eca4b368b7fd)(yeni) butonu tıklanarak Risk Dağılım Matrisi Tanımlama \\Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload94cca6b1-10fc-4bb3-82e2-ce1807fe0284)![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2dbd8988-08ff-4475-817e-c2bc5a50f9bb)

Yeni butonu ile açılan ekranda “Grafik Adı” belirlenir. X ve Y eksenindeki parametreler için risk karşılaştırmasında kullanılacak alanlar belirlenir. Bu alanların alan tanımlama menüsündeki formülleri “X Formülü” ve “Y Formülü” kısımlarına yazılır. “X Aralıkları” ve “Y Aralıkları” kısımlarına ise alanların değerleri girilir. İşlemler tamamlandıktan sonra kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload897efae2-9062-4fe9-80e5-e84f4738f491)

Risk Dağılım Matrisini kullanılan yönteme uygun olarak renklendirmek için Risk Dağılım Matrisi tanımlama ekranındaki sağ üst köşede bulunan ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3596a696-60b9-413f-9a16-322fc93b483c) (Renklendir) butonuyla oluşturulan matris açılır. Ekrandaki her kutucuğun üzerine tıklanarak kutucuklar renklendirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6a482aa8-42c6-4cfe-80bb-7573971b6ad3)

### **6.1.5.Onay Akışı**

Kurumsal Risk Değerlendirme Modülü için onay akışı kurgulandıktan sonra riskler onaya gönderilebilir.

**Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Parametreler** menüsüne gelinir. Filtreden Kurumsal Risk Değerlendirme Modülü seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbba8eb39-ff8e-465e-8e8c-2ab4b40ff756)

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada0614f26-24d0-4b72-89e2-e20d74a780df)(Değiştir) butonu ile 22 numaralı parametre olan “Statü kullanılacak mı?” değeri “evet” olarak değiştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddd40b9ec-366b-405c-bea3-9f485ad62f9b)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0f1ef261-326d-4897-959b-67eb90bf8504)

**SAT/ BSAT/ Konfigürasyon Ayarları/ Rol Tanımlama** ekranından onay akışları için rol tanımlamaları yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload247ba83c-bb35-4424-9a0b-00ca82e06163)

**Sistem Altyapı Tanımları/ BSAT/ Tanımlar/ Mesaj Gövdesi Tanımlama** ekranından Modül için yeni mesaj gövdesi tanımlamaları yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb20dc304-f339-4a6c-9180-3e1b6fa05809)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload68467ddc-cfe2-47a5-b592-27ab393cae37)

**Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Akış Tanımlama** ekranından akış tanımlamaları yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload33f192e3-f0b6-463c-944a-dd58c8ac4ed3)

Fonksiyon Dizayner menüsüne gelinir. Statü ve Butonlar adında iki farklı işlem butonu Risk Değerlendirme Form Tanımlama ve Risk Değerlendirme Detay fonksiyonları için menüye gelecektir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2d9ddd50-f1d6-415b-897b-e217a4b8c51a)

**Ekranındaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9da06d63-7dcd-407f-80d7-987364a9d409): Statü tanımlamak için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbb981c0a-4f34-41dc-a30c-0f8d84d865b8): Butonlar tanımlamak için kullanılır.

Fonksiyon dizayner menüsünden ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf8d42c3b-2277-41f6-8887-9c7f31da3efc) (statüler) butonu ile statüler tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload76f3f50d-8d3a-4d7b-9d64-e2ee5a0025ea)

**Ekranındaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9f362429-f90a-4625-a725-fbf7a6816676):Yeni statü tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada0614f26-24d0-4b72-89e2-e20d74a780df): Listede seçili statü bilgisi güncellenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2ae29da1-4327-419e-9458-8fb3f84dcf85): Listede seçili statü bilgisi silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3441981c-31d9-46ee-90a7-65cf4f1bacbb):Önceki ekrana geri dönülür.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9f362429-f90a-4625-a725-fbf7a6816676) (Yeni) butonu ile yeni statü tanımlama ekranına gelinir. Açılan ekranda statü kodu, statü adı, akışın başlatılıp başlatılmayacağı, yeni statü, durum, akış tanımı, onay talep mesajı, onay tamam mesajı ve onay red mesajı girişleri yapılarak kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1663e6d6-57ac-4593-a6d1-82b7a1849f97)

Fonksiyon dizaynerdan ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcf745dde-cbc9-4037-8443-be84d8d2fbd8) (Butonlar) butonu ile butonlar tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6e312e76-f34e-4c5e-8286-5c1a7ab52ae8)

Yeni bir buton tanımlamak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload607297d2-f9af-4677-acbd-eca4b368b7fd) (Yeni) butonu ile kullanılır. Açılan ekranda buton kodu, buton adı belirlenir. Buton tipi ve resmi belirlenir. Görünür statüsü, yeni statü ve durum girişi yapılır. Gerekli alanlar doldurulduktan sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb412234-f80c-4cd2-a416-6147a15f7b5e)( kaydet) butonuyla kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc39a3ca0-a8bc-41b7-8165-2af60c8a44d5)

Buton ekleme işleminde görünür statü seçeneği ile oluşturulan butonun hangi statüde görüleceği belirlenir. Oluşturulan butona göre olay ekranında işlem gerçekleştirildikten sonra, olayın hangi statüye gideceği ve nerede görüleceği “yeni statü” seçimi ile belirlenir.

Fonksiyon dizaynerdan ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7a80c8d1-ae6f-45a6-b1a2-33f8b4781661) (alanlar) botonuyla alanlar tanımlanır.

Sisteme tanımlanan bütün alanların hangi sayfada görüleceği alanlar butonu ile gerçekleştirilir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9f362429-f90a-4625-a725-fbf7a6816676) (Yeni) butonu ile yeni statü tanımlama ekranına gelinir. Açılan ekranda alan seçilir, aktif statü-görünür statü-zorunlu statü durumları seçilerek bu alanın hangi statülerde görüleceği belirlenmiş olur.

### **6.![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb35ee986-a248-448b-af0d-b6fc786779eb)![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3e49dc35-5eaf-4ad2-aa11-bdd47e7358d9)1.6.Alan Menüsü Tanımlama**

**Menü Adı**: Sistem Altyapı Tanımları/Kurumsal Risk Değerlendirme/ Alan menüsü Tanımlama

Liste tipli alanlara değer eklenmesi için Entegre Yönetim Sistemi altında menü oluşturulmasını sağlayan menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc0d567e1-ed3b-4f69-9480-8a9a802c4469)

**Ekranındaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9f362429-f90a-4625-a725-fbf7a6816676): Yeni Menü tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada0614f26-24d0-4b72-89e2-e20d74a780df): Listede seçili Menü bilgisi değiştirilir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2ae29da1-4327-419e-9458-8fb3f84dcf85): Listede seçili Menü bilgisi silinir.

Listeye yeni bir Menü eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload607297d2-f9af-4677-acbd-eca4b368b7fd) (yeni) butonu tıklanarak Menü Tanımlama\\ Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload83f4035b-215b-494c-8ba0-5ee8972e0b0e)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Menü Adı:** Menü Tanımlama ekranında Menü adı bilgisinin girildiği alandır.

**Alan:** Menü Tanımlama ekranında Alan bilgisinin seçilebildiği alandır.

**Sıra No:** Menü Tanımlama ekranında Sıra No bilgisinin girildiği alandır.

Açılan ekranda Menü Adı ve Sıra No bilgisi girilir. Alan bilgisi seçilir. Menü Tanımlama ekranında gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb7126322-0d77-432e-b92a-92ea5055c29b) (kaydet) butonu tıklanarak Menü Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfe406dab-ad6d-4b86-9a19-2e4a8b605196)

### **6.1.7.Kurumsal Risk Değerlendirme Parametreleri**

**Menü Adı**: Sistem Altyapı Tanımları/Kurumsal Risk Değerlendirme/ Kurumsal Risk Değerlendirme Parametreleri

Kurumsal Risk Değerlendirme Modülünün kullanıcının istek ve ihtiyaçlarına göre sistemsel ayarlarının yapıldığı ve bunlara göre parametreleri belirlendiği menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7aae65d1-0373-4fa7-b6d4-2a4d832f3436)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada0614f26-24d0-4b72-89e2-e20d74a780df): Listede seçili parametre güncellenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfcf033eb-a926-4c7d-a621-2f9bb3cd8e9b): Kayıtlar filtrelenerek arama yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload076b70b0-75aa-467b-80d8-678df037e68d): Veriler Excel’ e aktarılabilir.

### **6.1.8.E-Posta Ayarları**

**Menü Adı**: Sistem Altyapı Tanımları/Kurumsal Risk Değerlendirme/ E-Posta Ayarları

E-Posta ayarları ekranında, Kurumsal Risk Değerlendirme Modülü sürecinin hangi aşamasında kimlere mail gönderimi yapılacağı belirlenir.

Bildirim ayarı yapılacak değerin üzerine gelinip ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5daca06b-2d43-4761-9c2c-423b0c6180fc) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload37cd0845-d2ff-447b-899f-258b9063224f)

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload041d433c-9dd5-4a28-aa0d-0fe91ba47c0c)(Değiştir) butonu ile değerin içine girdikten sonra, rollere göre uygun mesaj gövdesi seçilir ve E-posta gitsin mi check-box‘ ı işaretlenerek kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload735c2512-8522-45df-82e4-df28b66e0f9d)

### **6.1.9.Tekrar Eden Kayıtlar Raporu Şablonu**

**Menü Adı**: Sistem Altyapı Tanımları/Kurumsal Risk Değerlendirme/ Tekrar Eden Kayıtlar Raporu Şablonu

Sistemde bir kullanıcı için istenen konularda tekrar eden kayıtları gösteren menüdür. İlk olarak Sistem Altyapı Tanımları/ Kurumsal Risk Değerlendirme /Tekrar Eden Kayıtlar Raporu Şablonu menüsünden raporda çekilecek alanlar seçilir.

Daha sonra Entegre Yönetim Sistemi/ Kurumsal Risk Değerlendirme /Raporlar/Tekrar Eden Kayıtlar raporundan ilgili rapora ulaşılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadeaf1fb43-b0c3-4767-82c5-a36840b1c6d4)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload86cde9b8-fd83-4d4c-a810-9ac62df10863): Yeni Tekrar Eden Kayıtlar Şablonu tanımlanır

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4499312d-136c-47bc-9a93-4950d2b2c69b): Listede seçili Tekrar Eden Kayıtlar Şablonu bilgisi güncellenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb29dc9af-e1f5-41dc-98a0-b877b2c05c6c): Listede seçili Tekrar Eden Kayıtlar Şablonu bilgisi silinebilir.

Tekrar Eden Kayıtlar Raporu Şablonları ekranına yeni bir Tekrar Eden Kayıtlar Raporu Şablonları eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload607297d2-f9af-4677-acbd-eca4b368b7fd)(yeni) butonu tıklanarak Tekrar Eden Kayıtlar Raporu Şablonları \\Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload09da1a5c-f6aa-4a2c-ba99-7912ecc80da8)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Tanım:** Tekrar Eden Kayıtlar Raporu Şablonları ekranında Tekrar Eden Kayıtlar Raporu Şablonları tanım bilgisinin girildiği alandır.

**Kolanlar:** Tekrar Eden Kayıtlar Raporu Şablonları ekranında Kolanlar bilgisinin seçilebildiği alandır.

Açılan ekranda Tekrar Eden Kayıtlar Raporu tanım bilgisi girilir. İlgili Kolanlar seçilir. Tekrar Eden Kayıtlar Raporu Şablonları ekranında gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb7126322-0d77-432e-b92a-92ea5055c29b) (kaydet) butonu tıklanarak Tekrar Eden Kayıtlar Raporu Şablonları kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd653dbab-8cc6-430f-b982-358ef00e1db5)

Entegre Yönetim Sistemi/ Kurumsal Risk Değerlendirme /Raporlar/Tekrar Eden Kayıtlar raporundan ilgili rapor şablonu seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload44868c31-c6c5-46b7-a389-d5062c98c952)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfcf033eb-a926-4c7d-a621-2f9bb3cd8e9b) Ara butonu ile kayıtlar filtrelenerek arama yapılabilir ve ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload076b70b0-75aa-467b-80d8-678df037e68d)( Excel aktar) botunu ile veriler Excel’ e aktarılabilir.

### **6.1.10.Rapor Formatları**

**Menü Adı**: Sistem Altyapı Tanımları/Kurumsal Risk Değerlendirme/Rapor Formatları

Kurumsal Risk Değerlendirme metotlarına göre farklı rapor formatları oluşturmak için Rapor Formatları menüsü kullanılabilir. Bunun için öncelikle SAT/BSAT/Konfigürasyon Ayarları/Rapor Formatları Düzenleme menüsüne oluşturacağımız rapor formatlarının tümü tanımlanmalıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5f64b3c7-3f46-45c6-9256-e68fea191bad)

Açılan menüde ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload607297d2-f9af-4677-acbd-eca4b368b7fd) (Yeni) butonuna tıklanarak rapor formatı eklemesi yapılır ve rapor formatının adı uzantısıyla beraber kopyalanır.

Daha sonra, SAT/Kurumsal Risk Değerlendirme/Rapor Formatları menüsü açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada73540c6-f3d4-400f-9b11-1b848681e115)

**Ekranındaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9f362429-f90a-4625-a725-fbf7a6816676): Yeni Rapor Formatı tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada0614f26-24d0-4b72-89e2-e20d74a780df): Listede seçili Rapor Formatı bilgisi güncellenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2ae29da1-4327-419e-9458-8fb3f84dcf85): Listede seçili Rapor Formatı bilgisi silinir.

Listeye yeni bir Rapor Formatı eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload607297d2-f9af-4677-acbd-eca4b368b7fd) (yeni) butonu tıklanarak Rapor Formatları\\ Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8b394201-8267-40d4-bbbc-3709fcf4e8ab)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Rapor Tanımı:** Rapor Formatları ekranında Rapor Tanımı bilgisinin girildiği alandır.

**Rapor Şablonu:** Rapor Formatları ekranında Rapor Şablonun adı ve uzantısı bilgisinin girildiği alandır.

**Rapor Tipi:** Rapor Formatları ekranında Kayıt Bazında, Form Bazında ve Genel olmak üzere üç seçenek Rapor Tipi bilgisinin verildiği alandır.

Açılan ekranda tanıtılacak rapor formatlarının isimleri Rapor Tanımı alanına yazılır. Rapor Şablonu alanına ise, Rapor Formatları Düzenleme menüsünden kopyaladığımız dosya adı **uzantısıyla beraber** yapıştırılır. Rapor Şablonu seçmeli alanında bulunan seçeneklerden;

-   **Kayıt Bazında:** Her risk detayı için ayrı bir şablon hazırlandığı durumlarda seçilir. (EYS/Kurumsal Risk Değerlendirme/Risk Değerlendirme Formu Tanımlama menüsünde Detaylar butonuna basıldıktan sonra çıkan “pdf” butonuyla alınır. Kayıt bazında tanımlama olmadığı sürece pdf butonu görüntülenmez.)
-   **Form Bazında:** Her risk formu altındaki detayları tek bir liste halinde Excel’e aktarıldığı durumlar için seçilir.

    (EYS/Kurumsal Risk Değerlendirme/Risk Değerlendirme Formu Tanımlama menüsünde Detaylar butonuna basıldıktan sonra çıkan “Excel” butonuyla alınır.)

-   **Genel:** Tüm risk detaylarının tek bir Excel’de görülmek istenmesi durumunda seçilir.

(EYS/Kurumsal Risk Değerlendirme/Raporlar/Genel Risk Listesi rapor ekranından alınır.)

Rapor Tanımlama ekranında gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb7126322-0d77-432e-b92a-92ea5055c29b) (kaydet) butonu tıklanarak Rapor Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload43fa2ccf-c84b-454e-9dfd-8aacaceb1c65)

## **6.2.Entegre Yönetim Sistemi/Kurumsal Risk Değerlendirme**

Kurumsal Risk Değerlendirme Modülü kapsamında Faaliyet Grupları, Faaliyet, Risk Formu, Risk Form Detaylarının tanımlandığı, Raporların ve Grafiklerin görüntülendiği kısımdır.

### **6.2.1.Faaliyet Grubu Tanımlama**

**Menü Adı**: Entegre Yönetim Sistemi/Kurumsal Risk Değerlendirme/ Faaliyet Grubu Tanımlama

Kurumsal Risk Değerlendirme Modülünde kullanılacak olan faaliyetlerin tanımlanması için öncelikle bu faaliyetlerin bağlı bulunacağı grupların tanımlanması gerekir. Bunun için kurumsal Risk Modülünün Entegre Yönetim Sistemi başlığı altına gelinerek Faaliyet Grubu Tanımlama menüsüne tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcb4fd42a-a33c-4260-9c27-997cdb7f9895)

**Açılan ekrandaki butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload173c7481-1720-4ab5-a8ef-367d8121005c): Yeni Faaliyet Grubu tanımlanabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload631e7142-126f-4ca7-a9d1-95e5e104e271): Listede seçili Faaliyet Grubu bilgisi güncellenebilir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2ae29da1-4327-419e-9458-8fb3f84dcf85): Listede seçili Faaliyet Grubu bilgisini silmek için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3719332d-8cbe-4731-bdd4-3ae534b7319e): Veriler Excel’e aktarılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload00672bc3-b3d3-492f-b530-88fa3e590ce8): Şablon yüklemek için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc55f011b-b737-4dd2-b4fc-dbb295fe4e20): Şablon oluşturmak için kullanılır.

Faaliyet Grubu Tanımlama ekranına yeni bir Faaliyet Grubu eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload607297d2-f9af-4677-acbd-eca4b368b7fd)(yeni) butonu tıklanarak Faaliyet Grubu Tanımlama \\Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload55596856-1f1c-4f96-9b52-a868cb6513f8)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Bağlı Olduğu Faaliyet Grubu:** Faaliyet Grubu Tanımlama ekranında Bağlı Olduğu Faaliyet Grubu bilgisinin sistemde tanımlı olan Faaliyet Grubu Listesinden seçilebildiği alandır.

**Faaliyet Grubu Kodu:** Faaliyet Grubu Tanımlama ekranında Faaliyet Grubu Kodu bilgisinin girildiği alandır.

**Faaliyet Grubu Tanımı:** Faaliyet Grubu Tanımlama ekranında Faaliyet Grubu Tanımı bilgisinin girildiği alandır.

**Sorumlu Kullanıcı Grupları:** Faaliyet Grubu Tanımlama ekranında Sorumlu Kullanıcı Gruplarının bilgisinin sistemde tanımlı olan Kullanıcı Grubu Listesinden seçilebildiği alandır.

**Sorumlu Personel:** Faaliyet Grubu Tanımlama ekranında Sorumlu Personel bilgisinin sistemde tanımlı olan Personel Listesinden seçilebildiği alandır.

**Otomatik Kod Şablonu**: Faaliyet Grubu Tanımlama ekranında Otomatik Kod Şablonu bilgisinin verildiği alandır.

**Otomatik Kod Sayacı:** Faaliyet Grubu Tanımlama ekranında Otomatik Kod Sayacı kaçtan başladığının bilgisinin verildiği alandır.

**Durum:** Faaliyet Grubu Tanımlama ekranında Faaliyet Grubu Aktif veya Pasif Durumun seçilebildiği alandır.

Bu sayfada (varsa) faaliyet grubunun bağlı olduğu faaliyet grubu, faaliyet grubu kodu ve tanımı bilgileri girilir. Eğer sadece belirli kullanıcı gruplarının bu faaliyetlerle işlem yapması isteniyorsa sorumlu kullanıcı grupları kısmından kullanıcı grupları seçilip eklenir. Aktif/ pasif durumu belirlenerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadedee82a9-81db-4939-aa09-982b9f266d32) (kaydet) butonu tıklanarak faaliyet grubu tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc26cb7e8-297c-4534-a0bc-a0acd48aa072)

### **6.2.2.Faaliyet Tanımlama**

**Menü Adı**: Entegre Yönetim Sistemi/Kurumsal Risk Değerlendirme/ Faaliyet Tanımlama

Kurumsal Risk Değerlendirme Modülünde analizi yapılan risklerin ait olduğu faaliyetlerin tanımlandığı yerdir. Entegre Yönetim Sistemi altında Faaliyet Tanımlama menüsü altında ilgili sayfa görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9f5d66fd-b5cc-409a-a2d5-6626acbf6ab7)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload173c7481-1720-4ab5-a8ef-367d8121005c): Yeni Faaliyet tanımlanabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload631e7142-126f-4ca7-a9d1-95e5e104e271): Listede seçili Faaliyet bilgisi güncellenebilir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2ae29da1-4327-419e-9458-8fb3f84dcf85): Listede seçili Faaliyet bilgisi silmek için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadca45fb0e-a443-40ad-9332-fea821f815d6): Listede seçili Faaliyet kopyalanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3719332d-8cbe-4731-bdd4-3ae534b7319e): Veriler Excel’e aktarılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload00672bc3-b3d3-492f-b530-88fa3e590ce8): Şablon yüklemek için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc55f011b-b737-4dd2-b4fc-dbb295fe4e20): Şablon oluşturmak için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload899ccb49-582f-4472-83b8-1ef02777f293): Önceki ekrana geri dönülür.

Faaliyet Tanımlama ekranına yeni bir Faaliyet eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload607297d2-f9af-4677-acbd-eca4b368b7fd)(yeni) butonu tıklanarak Faaliyet Tanımlama \\Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb22a01e6-9f84-406d-8121-9a00768d902b)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Faaliyet Grubu:** Faaliyet Tanımlama ekranında Faaliyet Grubu bilgisinin sistemde tanımlı olan Faaliyet Grubu Listesinden seçebildiği alandır.

**Faaliyet Kodu:** Faaliyet Tanımlama ekranında Faaliyet Kodu bilgisinin sistem tarafından otomatik olarak verildiği alandır.

**Sorumlu Kullanıcı Grupları:** Faaliyet Tanımlama ekranında Sorumlu Kullanıcı Gruplarının bilgisinin sistemde tanımlı olan Kullanıcı Grupları Listesinden seçilebildiği alandır.

**Sorumlu Personel:** Faaliyet Tanımlama ekranında Sorumlu Personel bilgisinin sistemde tanımlı olan Personel Listesinde seçilebildiği alandır.

**Durum:** Faaliyet Tanımlama ekranında Faaliyet Tanımı Aktif veya Pasif durumun bilgisinin seçilebildiği alandır.

Açılan ekranda sırasıyla faaliyet grubunu, faaliyet kodunu eğer parametreden otomatik kod verme aktif edilmemişse kod bilgisi, faaliyet tanımını ve yine eğer sorumlu kullanıcı grupları kullanılacaksa bu alan doldurulduktan sonra, durum bilgisi seçilip ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload090004ca-d246-4605-96dd-3d569fd718e9) (kaydet) butonu tıklanarak Faaliyet tanımı kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload40e5fa28-cc8a-479a-b2ce-463ad278889e)

### **6.2.3.Risk Değerlendirme Formu Tanımlama**

**Menü Adı**: Entegre Yönetim Sistemi/Kurumsal Risk Değerlendirme/ Risk Değerlendirme Formu Tanımlama

Kurumsal Risk Değerlendirme Modülünde faaliyet ve faaliyet grupları da tanımlandıktan sonra yapılacak son aşama, risklerin yer alacağı formların (RDF ) tanımlanmasıdır. Bunun için Entegre Yönetim Sistemi başlığı altındaki Kurumsal Risk Değerlendirme Modülünün altında Risk Değerlendirme Formu menüsü açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6d49a5c9-6e98-48dc-83c3-8907a34d7430)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload173c7481-1720-4ab5-a8ef-367d8121005c): Yeni RDF ( Risk Değerlendirme Formu) tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload631e7142-126f-4ca7-a9d1-95e5e104e271): Listede seçili RDF bilgisi güncellenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2ae29da1-4327-419e-9458-8fb3f84dcf85): Listede seçili RDF bilgisi silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadca45fb0e-a443-40ad-9332-fea821f815d6): Listede seçili RDF bilgisi kopyalanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb565855a-cdcb-426d-9fc5-fa1260ae3b87): Filtre ekranındaki kriterlere göre arama yapar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbc9d1c1e-bbc5-4770-933b-c71ebbdfe053): RDF listesini Excel’e aktarır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload218e4a6f-cf88-4739-860c-31ac25abedd2): Seçili RDF’nin detay bilgiler ekranını açar.

RDF Tanımlama ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload64219648-26ab-4816-99ca-ca32e9bacf50) (Yeni) butonuyla yeni RDF tanımlaması gerçekleştirilir. RDF tanımlamadaki amaç, risk analizinin yapılacağı detay formların belirli kategoriler ( ünite, birim, faaliyet grubu, departman vb. ) altında sınıflandırmaktır

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload78908006-1d4d-4ec3-927c-e7a83e25209a)

**Açılan ekranda ilgili alanlar tanımlanır:**

**RDF Kodu:** Risk Değerlendirme Formu Tanımlama ekranında RDF Kodu bilgisinin sistem tarafından otomatik olarak bilgisinin verildiği alandır.

**RDF Tanımı:** Risk Değerlendirme Formu Tanımlama ekranında RDF Tanımı bilgisinin girildiği alandır.

**Sorumlu Kullanıcı Grupları:** Risk Değerlendirme Formu Tanımlama ekranında Sorumlu Kullanıcı Grupları bilgisinin sistemde tanımlı olan Kullanıcı Grupları Listesinden seçilebildiği alandır.

**Sorumlu Personeller:** Risk Değerlendirme Formu Tanımlama ekranında Sorumlu Personeller bilgisinin sistemde tanımlı olan Personel Listesinden seçilebildiği alandır.

**Otomatik Kod Şablonu:** Risk Değerlendirme Formu Tanımlama ekranında Otomatik Kod Şablonu bilgisinin verildiği alandır.

**Otomatik Kod Sayacı:** Risk Değerlendirme Formu Tanımlama ekranında Otomatik Kod Sayacı bilgisinin kaçtan başlayacağı bilgisinin verildiği alandır.

RDF tanımlama ekranında formun kodunu eğer otomatik kod verme aktif edilmemişse kod bilgisi, formun tanımını ve istenirse sorumlu kullanıcı grupları eklenerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload090004ca-d246-4605-96dd-3d569fd718e9) (kaydet) butonu tıklanarak Risk Değerlendirme Formu Tanımlama kayıt işlemi gerçekleştirilir.

Bu şekilde bütün RDF’ ler tanımlandıktan sonra, risk detayı eklemek istenen RDF seçili iken sağ üstteki butonlardan ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload185f3252-343c-4633-881e-a754b1232c81)(Detaylar) butonu tıklanarak Risk Değerlendirme Formu Detayı (RDFD) ekranına gelinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade193d15c-255c-43ac-a893-e996396a1866)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload173c7481-1720-4ab5-a8ef-367d8121005c): Yeni RDFD tanımlanabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload631e7142-126f-4ca7-a9d1-95e5e104e271): Listede seçili RDFD bilgisi güncellenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload053ac8b6-c6b5-490f-9169-213ad1551b21): Listede seçili RDFD bilgisi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9b20ff7a-74cc-44da-b576-376af58f9ef8): Listede seçili olan RDFD bilgisi kopyalanabilir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2ae29da1-4327-419e-9458-8fb3f84dcf85): Listede seçili olan RDFD bilgisini silmek için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload82b5566a-5d30-4d09-8024-70d2c9cbfb09): Listede seçili olan RDFD bilgisi revize edilerek onaya gönderilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload127bbc30-11d5-4de9-bdc8-c4cbd9714a1b): Listede seçili RDFD bilgisinin eski revizyonları izlenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9143bf67-21cd-45d0-b69c-fe2263693616): Listede seçili RDFD bilgisi gözden geçirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload83e87cce-c08d-4cb9-b719-6afd8464779a): Listede seçili RDFD bilgisi için eski gözden geçirmeler izlenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade995c07a-f998-46d5-800e-c86e238569f3): Arama Fonksiyonu kullanılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload01a6b33e-d958-4587-a811-da1943da9233): Yazdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3719332d-8cbe-4731-bdd4-3ae534b7319e): Listede seçili Form detayları Excel’ e aktarılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload85d9f1dd-9e44-4034-a2bd-0b9720130719): Revizyon Değişimi gösterir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0f88dbf1-adc0-4d3d-b765-42145ceee7d7):Bir önceki ekrana dönmek için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6a935850-25e9-4f54-805b-7b231a1dd572): Grafik çizmek için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc55f011b-b737-4dd2-b4fc-dbb295fe4e20): Şablon oluşturmak için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload00672bc3-b3d3-492f-b530-88fa3e590ce8): Şablon yüklemek için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload64219648-26ab-4816-99ca-ca32e9bacf50)(Yeni) butonuyla Risk Değerlendirme Formu/Detaylar ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload51bbc4cc-be71-49a7-8e27-824414123ecd)

**Açılan ekranda ilgili alanlar tanımlanır:**

**RDF Tanımı:** Risk Değerlendirme sekmesinde RDF Tanımı bilgisinin girildiği alandır.

**RDFD Kodu:** Risk Değerlendirme sekmesinde RDFD Kodu bilgisinin sistem tarafından otomatik olarak verildiği alandır.

**Faaliyet Tipi:** Risk Değerlendirme sekmesinde Faaliyet Tipi bilgisinin seçilebildiği alandır.

**Faaliyet:** Risk Değerlendirme sekmesinde Faaliyet bilgisinin seçilebildiği alandır.

**Revizyon No:** Risk Değerlendirme sekmesinde Revizyon No bilgisinin verildiği alandır.

**Revizyon Tarihi:** Risk Değerlendirme sekmesinde Revizyon Tarihi bilgisinin girildiği alandır.

**Olasılık:** Risk Değerlendirme Formunda olasılık alanın değer bilgisinin seçilebildiği alandır (Kullanıcı tanımlıdır. Alan tanımlama menüsünden tanımlanması gereklidir.)

**Şiddet:** Risk Değerlendirme Formunda Şiddet alanın değer bilgisinin seçilebildiği alandır. (Kullanıcı tanımlıdır. Alan tanımlama menüsünden tanımlanması gereklidir.)

**Risk Düzeyi:** Risk Değerlendirme sekmesinde Risk Düzeyin sistem tarafından hesaplandığı bilgisinin verildiği alandır. (Kullanıcı tanımlıdır. Alan tanımlama menüsünden tanımlanması gereklidir.)

**Risk Derecesi:** Risk Değerlendirme sekmesinde Risk Derecesinin sistem tarafından hesaplandığı bilgisinin verildiği alandır. (Kullanıcı tanımlıdır. Alan tanımlama menüsünden tanımlanması gereklidir.)

Risk Değerlendirme sekmesinde risk analizi için gerekli olan temel bilgiler ve kullanıcı tanımlı alanlar doldurulur. Riskin revizyon numarası, revizyon tarihi, Faaliyet tipi ve Faaliyet seçimi seçilir. Bu bilgiler girildikten sonra risk metodolojisinin gerektirdiği kullanıcı tanımlı alanlar doldurulur.

Risk değerlendirme formu doldurulduktan sonra, firmaya ait olan Kurumsal Risk Değerlendirme Metodolojisine göre risk seviyesinin belirlenen aralıkları için ana ekranda sarı, kırmızı, yeşil gibi renkli noktalar görülmektedir. Riskler için önlemler alındıktan ve gerçekleştirildikten sonra revize işleminin de yapılmasıyla risk seviyesi düşürülmekte, daha düşük seviyelerdeki risk aralıklarındaki renk butonlarına dönüşmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadca3c15d6-ebe8-4704-b1e8-da113790a0c8)

Trend kısmı ile o riske ait riskin şu anki durumu görülmektedir. Böylece riskin azalan mı, artan mı, yoksa değişmeyen bir durumda mı olduğu görülmüş olur.

Kullanılan risk değerlendirme yöntemine göre, risk durumunun yüksek, orta, kabul edilebilir gibi seviyeleri risk değerlendirme formu detayındaki “renk” kısmında görülmektedir. Bu renklere göre belirlenen riskin ne seviyede olduğu anlaşılır. Bu renk seçimleri, alan tanımlama ekranında risk yöntemi ve prosedürüne uygun olarak tanımlanmaktadır.

Önlemler sekmesinde ise bulunan risk değerinin azaltılması için alınacak önlemler planlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6fe0a815-b3cd-48f9-8e6b-c38eb4ed2d5b)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload173c7481-1720-4ab5-a8ef-367d8121005c): Yeni bir Önlem tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload631e7142-126f-4ca7-a9d1-95e5e104e271): Listede seçili Önlem bilgisi güncellenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2ae29da1-4327-419e-9458-8fb3f84dcf85): Listede seçili Önlem bilgisi silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf5f658b1-68d0-4bd7-96d3-eae16cc7f336): Listede seçili Önlem bilgisi görüntülenir.

Önlemler sekmesine gelindiğinde ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload64219648-26ab-4816-99ca-ca32e9bacf50) (Yeni) butonuyla yeni önlem tanımlama işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2f191def-6093-4e89-a20e-e792ead58fd5)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Referans Tipi:** Önlemler sekmesinde Referans Tipi bilgisi Döf, Aksiyon, Doküman, ve Diğer seçeneklerinden seçilebildiği alandır. Referans Tipi “Listeden Seç” seçeneği seçilirse Referans tipi bilgisi Listeden seçilir. Referans Tipi “Yeni oluştur” seçeneği seçilirse Referans Tipi bilgisi Yeni oluşturulur.

**Referans Bilgisi:** Önlemler sekmesinde Referans Tipi Aksiyon Seçildiğinde Referans bilgisinin verildiği alandır.

**Önlem Tipi:** Önlemler sekmesinde Önlem Tipinin Mevcut veya planlanan seçilebildiği alandır.

**Önlem Tarihi:** Önlemler sekmesinde Önlem Tarihi bilgisinin girildiği alandır.

**Açıklama:** Önlemler sekmesinde Açıklama bilgisinin girildiği alandır.

Açılan ekranda Referans Tipi açılır menüsünden önlemin türü seçilir. ( DÖF, Aksiyon, Doküman, Diğer). Daha sonra önlem tipi ( Mevcut, Planlanan ) ve önlem tarihi girildikten sonra önlemin açıklaması girilir ve ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload090004ca-d246-4605-96dd-3d569fd718e9) (kaydet) butonu tıklanarak önlem tanımlama kayıt işlemi gerçekleştirilir. Örnekte Önlem Referans tipi Aksiyon seçilerek ve listede seçeneği ile listeden seçim yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload370db67b-0719-4391-b888-3307739bf9de)

Referans tipi olarak DÖF ve Aksiyon seçilirse, QDMS’teki DÖF ve Aksiyon Modülleri ile bağlantı kurulacaktır. Mevcut açılmış DÖF ve Aksiyonlardan herhangi biri önlemle ilişkilendirilebileceği gibi, yeni kayıtta açılabilir. Referans tipi olarak Doküman seçilirse, QDMS’teki doküman ağacından önleme doküman referansı verilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5ed24000-b5ab-48ec-845a-01e7fad5718c)

**Revizyon İşlemi:** RDFD’ler kaydedildikten sonra herhangi bir anda revizyon işlemine tabi tutulabilir ve yeni risk analizleri gerçekleştirilebilir. Bunun için RDFD listesi açıkken ilgili risk detayı seçilir ve sağ üstteki butonlardan ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2576365f-74bb-45ae-ab73-f75d0d74d630)(Revizyon) botunu tıklanır. Bundan sonraki aşama risk detayını ilk kez doldururken izlenen adımlarla birebir aynıdır. Tek fark, RDFD ekranındayken Revizyon No.su bir artacaktır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload634348bb-613f-4ddc-a86e-46eed03e9a14)İlgili RDFD’nin eski revizyonlarını görüntülemek için, listede seçili durumdayken ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcaa79cf0-655e-4063-b6f5-aea82600b186)(Eski revizyonlar) butonuna basılır. Açılan yeni ekranda eski revizyonlar listelenir. Bir eski revizyon bilgilerini görüntülemek içinse listede seçim yaptıktan sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload63e025c6-3585-43b7-9c4f-a21064eeeb2b) (görüntüle) butonuyla bilgiler görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf0a8b0ce-1b2c-4aef-a2ee-6d96ad678c5f)

**Gözden Geçirme:** Mevcut riskler herhangi bir gözden geçirme işlemine tabi tutulabilir ve mevcut durum değerlendirilip açıklamalar yapılabilir. Bunun için RDFD listesi açıkken ilgili risk detayı seçilir ve sağ üstteki butonlardan ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9143bf67-21cd-45d0-b69c-fe2263693616)(Gözden Geçir) butonutıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload28d3824e-e944-48d8-8d7a-3e82a560dd56)

İlgili RDFD’nin eski gözden geçirmelerini görüntülemek için, listede seçili durumdayken ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload83e87cce-c08d-4cb9-b719-6afd8464779a) (Eski gözden geçirme) butonuna basılır. Açılan yeni ekranda risk eski gözden geçirmeleri listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfd5dcd85-64e2-4765-bf4a-ad2a12b688b5)

### **6.2.4.Raporlar**

Kurumsal Risk Değerlendirme Modülü kapsamındaki raporlarının görüntülendiği kısımdır.

#### **6.2.4.1.Genel Risk Listesi**

**Menü Adı**: Entegre Yönetim Sistemi/ Kurumsal Risk Değerlendirme/Raporlar/Genel Risk Listesi

Genel Risk Listesi raporunu almak için, Raporlar menüsünden Genel Risk Listesi açılır. Kurumsal Risk Değerlendirme Modülü kapsamında kayıtlardaki tüm risk detaylarının görülebildiği listedir. İstenirse Filtre sekmesinden alanlara göre filtreleme işlemi de gerçekleştirilebilir.Açılan pencerede RDFD’lerin listesi görüntülenmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddfef38fc-5879-4c49-8f77-79b57da40759)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload076b70b0-75aa-467b-80d8-678df037e68d): Veriler Excel’ e aktarılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfcf033eb-a926-4c7d-a621-2f9bb3cd8e9b): Kayıtlar filtrelenerek arama yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8e48deaf-d607-496f-b6a0-2e44cf0fe31d)(Excel’e aktar) butonuna basılırsa, sistem otomatik olarak Genel Risk Listesi raporunu oluşturup kullanıcıya Excel formatında sunmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8099541f-37dc-4b57-8034-7d2d25fe3f12)

#### **6.2.4.2.Faaliyetler Tarihçesi**

**Menü Adı**: Entegre Yönetim Sistemi/ Kurumsal Risk Değerlendirme/Raporlar/Faaliyetler Tarihçesi

Kurumsal Risk Değerlendirme Modülünde kapsamında sistemde tanımlı Faaliyetlerin tarihçe bilgisinin görüntülendiği rapordur. Alınan raporda Faaliyet kodu, Faaliyet Tanımı ve Faaliyet Grubu Tanımı gibi alanların bilgileri görüntülenir. İstenirse Filtre sekmesinden alanlara göre filtreleme işlemi de gerçekleştirilebilir.Faaliyetler Tarihçesi raporunu almak için, Raporlar menüsünden Faaliyetler Tarihçesi açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4255e762-ece6-4a66-9307-d7ca1bad9805)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload076b70b0-75aa-467b-80d8-678df037e68d):Veriler Excel’ e aktarılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfcf033eb-a926-4c7d-a621-2f9bb3cd8e9b):Kayıtlar filtrelenerek arama yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8e48deaf-d607-496f-b6a0-2e44cf0fe31d)(Excel’e aktar) butonuna basılırsa, sistem otomatik olarak Faaliyetler Tarihçesi raporunu oluşturup kullanıcıya Excel formatında sunmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload77ccdc81-f716-41ec-bae8-6c2a547769cd)

#### **6.2.4.3.Faaliyet Grubu Tarihçesi**

**Menü Adı**: Entegre Yönetim Sistemi/ Kurumsal Risk Değerlendirme/Raporlar/ Faaliyet Grubu Tarihçesi

Kurumsal Risk Değerlendirme Modülünde kapsamında sistemde tanımlı Faaliyet gruplarının tarihçe bilgisinin görüntülendiği rapordur. Alınan raporda Faaliyet Grubu kodu, Faaliyet Grubu Tanımı ve Üst Faaliyet Grubu Tanımı gibi alanların bilgileri görüntülenir. İstenirse Filtre sekmesinden alanlara göre filtreleme işlemi de gerçekleştirilebilir. Faaliyetler Grubu Tarihçesi raporunu almak için, Raporlar menüsünden Faaliyetler Grubu Tarihçesi açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcf5b4d8e-ee5d-425f-ae20-c9461ffb7824)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8e48deaf-d607-496f-b6a0-2e44cf0fe31d) (Excel aktar) butonuna basılırsa sistem listedeki RDFD’lerin Faaliyet Grubu Tarihçesini Excel formatında oluşturup kullanıcıya sunmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8d658c1c-f414-45a1-bf9a-4d88b93fb158)

#### **6.2.4.4.Faaliyet Raporu**

**Menü Adı**: Entegre Yönetim Sistemi/Kurumsal Risk Değerlendirme/Raporlar/ Faaliyet Raporu

Kurumsal Risk Değerlendirme Modülü kapsamında sistemde tanımlı Faaliyetlerin görüntülendiği rapordur. Alınan raporda Faaliye Kodu, Faaliyet Tanımı ve Faaliyet Grubu gibi alanların bilgileri görüntülenir. İstenirse Filtre sekmesinden alanlara göre filtreleme işlemi de gerçekleştirilebilir. Faaliyetler Raporunu almak için, Raporlar menüsünden Faaliyetler Raporu açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7c5950a6-690a-40e7-9dc8-aaca8c370fda)

**Ekranındaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload076b70b0-75aa-467b-80d8-678df037e68d): Veriler Excel’ e aktarılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfcf033eb-a926-4c7d-a621-2f9bb3cd8e9b): Kayıtlar filtrelenerek arama yapılabilir

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8e48deaf-d607-496f-b6a0-2e44cf0fe31d)(Excel aktar) butonuna basılırsa sistem listedeki RDFD’lerin Faaliyet Raporunu Excel formatında oluşturup kullanıcıya sunmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload86c86340-b1c8-4291-a589-afbf3bcfecfe)

#### **6.2.4.5.Aksiyon Raporu**

**Menü Adı**: Entegre Yönetim Sistemi/Kurumsal Risk Değerlendirme/Raporlar/ Aksiyon Raporu

Kurumsal Risk Değerledirme kapsamında Önlemler sekmesinde sistemde tanımlı aksiyonların görüntülendiği rapordur. İstenirse Aksiyon Arama sekmesinden alanlara göre filtreleme işlemi de gerçekleştirilebilir.Aksiyon Raporunu almak için, Raporlar menüsünden Aksiyon Raporu açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload85ce2a7a-9267-42a7-89e4-704ec787782a)

Kurumsal Risk Değerlendirme sonucu alınan aksiyon önlemlerinin alındığı bu rapor Excel’ e aktarılabilir. Özet raporu alınabilir. Ayrıca zaman bazlı aksiyon çizelge raporu çekilebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8e48deaf-d607-496f-b6a0-2e44cf0fe31d)(Excel aktar) butonuna basılırsa sistem Aksiyon Raporunun Excel formatında oluşturup kullanıcıya sunmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload447e1e5f-a2ff-4e43-a2a2-503537a82dfd)

#### **6.2.4.6.Tekrar Eden Kayıtlar Raporu**

**Menü Adı**: Entegre Yönetim Sistemi/Kurumsal Risk Değerlendirme/Raporlar/ Tekrar Eden Kayıtlar Raporu

Benzer risk kayıtlarının kaç kez tekrar ettiğini gösteren rapordur. Entegre Yönetim Sistemi/ Kurumsal Risk Değerlendirme /Raporlar/Tekrar Eden Kayıtlar raporundan ilgili rapor şablonu seçilir.Tekrar Eden Raporu ekranında Rapor Şablonu seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9b2a3acf-a558-45cf-92d4-593d7d9c1658)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfcf033eb-a926-4c7d-a621-2f9bb3cd8e9b) Ara butonu ile kayıtlar filtrelenerek arama yapılabilir ve ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload076b70b0-75aa-467b-80d8-678df037e68d) (Excel aktar) botunu ile veriler Excel’ e aktarılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload071a5c0d-bfad-44af-af73-6537e95309c3)

#### **6.2.4.7.Risklerin Bölgelere Dağılımı**

**Menü Adı**: Entegre Yönetim Sistemi / Kurumsal Risk Değerlendirme /Raporlar/Risklerin Bölgelere Dağılımı

Kurumsal Risk Değerlendirme Modülü kapsamında iş yeri ve departman bazlı risklerin haritada gösterilmesinin sağlandığı rapordur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2cb9f3b5-a1a8-4b3f-ae43-518205969b5d)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfcf033eb-a926-4c7d-a621-2f9bb3cd8e9b): Kayıtlar filtrelenerek arama yapılabilir.

İlgili İşyeri listesi veya Departman listesinde seçim yapılarak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfcf033eb-a926-4c7d-a621-2f9bb3cd8e9b)(ara) butonu tıklanarak Harita sekmesinde işyeri ve departman bazlı risklerin harita üzerinde görüntülenmesi sağlanır.

### **6.2.5.Grafikler**

Kurumsal Risk Değerlendirme Modülü kapsamında grafiklerin görüntülendiği kısımdır.

#### **6.2.5.1.En Çoklar Analizi**

**Menü Adı**: Entegre Yönetim Sistemi/Kurumsal Risk Değerlendirme/ Grafikler/En Çoklar Analizi

En Çoklar Analizi grafiğini almak için, Grafikler menüsünden En Çoklar Analizi sekmesi tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload88e591ba-6bcd-4aef-8274-3116e3446299)

En Çoklar Analizi ekranında, Grafik Seçenekleri bölümünde gerekli seçimler gerçekleştirilir. Grafikte olması istenen en çok aralık belirlenir. Grafik Seçeneklerinden X ekseninde yer alması istenen nitelik seçilir. Ana tema, renk paleti özelliklerinden grafik özelleştirilebilir. Grafik başlığı belirtilerek grafik oluşturmak için ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7f178b9f-ff48-48e2-9767-f3adcdf3a13e) (grafik çiz) butonuna tıklanır. Eğer istenirse birçok kritere göre filtreleme yapılabilir ve sadece bu özellikteki RDFD’lerin grafikte yer alması sağlanabilir.

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7f178b9f-ff48-48e2-9767-f3adcdf3a13e): Belirlenen özelliklere göre ekrana grafiği çizdirir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb59092ec-835f-45dc-a42f-23658c58de04) : İstenen grafiği açılır menüden seçilen format türüne ( excel, jpg, pdf, vb. ) dönüştürerek dış ortama aktarır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2dcb5718-9b9a-478d-89c8-a468a70c41d6): Grafik verileri, Excel listesi biçiminde aktarılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfe020f86-f04c-44d9-8ec6-e0fb4fef040a)

#### **6.2.5.2.Risk Dağılım Matrisi**

**Menü Adı**: Entegre Yönetim Sistemi/Kurumsal Risk Değerlendirme/ Grafikler/ Risk Dağılım Matrisi

Risk Dağılım Matrisini almak için, Grafikler menüsünden Risk Dağılım Matrisi sekmesi tıklanır. Hangi aralıkta kaç tane risk olduğunu gösteren 2 boyutlu bir grafik oluşturur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade29eae7b-ff29-45ef-adf8-2d158fee4659)

**Ekranındaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload076b70b0-75aa-467b-80d8-678df037e68d) :Veriler Excel’ e aktarılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfcf033eb-a926-4c7d-a621-2f9bb3cd8e9b):Kayıtlar filtrelenerek arama yapılabilir

Açılan ekranda grafik türü seçilir ve ara butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload54025231-a672-44d9-b2c5-154885a17c2b)

#### **6.2.5.3.Risk Karşılaştırma Grafiği**

**Menü Adı**: Entegre Yönetim Sistemi/Kurumsal Risk Değerlendirme/ Grafikler/ Risk Karşılaştırma Grafiği

Risk Karşılaştırma Grafiğini almak için, Grafikler menüsünden Risk Karşılaştırma Grafiği sekmesi tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload38c2d533-b64b-40ff-a3e1-fe490547ab37)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7f178b9f-ff48-48e2-9767-f3adcdf3a13e): Belirlenen özelliklere göre ekrana grafiği çizdirir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb59092ec-835f-45dc-a42f-23658c58de04): İstenen grafiği açılır menüden seçilen format türüne ( excel, jpg, pdf, vb. ) dönüştürerek dış ortama aktarır.

Açılan ekranda filtre sekmesinden grafik karşılaştırmasını almak istediğimiz alanları doldurarak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadeeb97126-87ee-49c0-9aac-e90cf4f00e1b) (grafik çiz) butonu ile istenilen risk karşılaştırması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcf51992a-68f1-4365-9a4f-c4d5ccf98b78)

#### **6.2.5.4.Risk Revizyon Karşılaştırma Grafiği**

**Menü Adı**: Entegre Yönetim Sistemi/Kurumsal Risk Değerlendirme/ Grafikler/ Risk Revizyon Karşılaştırma Grafiği

Risk Revizyon Karşılaştırma Grafiğini almak için, Grafikler menüsünden Risk Revizyon Karşılaştırma Grafiği sekmesi tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc91d2fb0-1e1a-47ee-8d63-2172e96c9d1f)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7f178b9f-ff48-48e2-9767-f3adcdf3a13e): Belirlenen özelliklere göre ekrana grafiği çizdirir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb59092ec-835f-45dc-a42f-23658c58de04): İstenen grafiği açılır menüden seçilen format türüne ( excel, jpg, pdf, vb. ) dönüştürerek dış ortama aktarır.

Açılan ekranda filtre sekmesinden grafik karşılaştırmasını almak istediğimiz alanları doldurarak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadeeb97126-87ee-49c0-9aac-e90cf4f00e1b) (grafik çiz) butonu ile istenile risk revizyon karşılaştırması yapılır. Güncel öncesi revizyon sayısı ve X ekseni seçilerek grafik çiz butonu ile grafik oluşturulur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload56c241ec-9d03-4e4d-a9b6-4d8de282ee38)

### **6.2.6.Risk Değerlendirme Talebi**

**Menü Adı**: Entegre Yönetim Sistemi/Kurumsal Risk Değerlendirme/ Risk Değerlendirme Talebi

Risk Değerlendirme Talebi menüsü kullanılarak herhangi bir personele risk değerlendirme görevi aksiyon olarak açılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadee258f1d-83d9-42c1-b142-308764f55c8e)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb63b2d8-6ecc-49ab-b651-a9bd402e7c24): Yeni Risk Değerlendirme Talebi tanımlar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1511c37b-b087-44b0-9fd4-ccb81620d0d5): Risk Değerlendirme Talebini görüntüler.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade995c07a-f998-46d5-800e-c86e238569f3): Arama fonksiyonu kullanılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3719332d-8cbe-4731-bdd4-3ae534b7319e): Risk Değerlendirme Talebini Excel’ e aktarılır.

Açılan ekranda yeni talep oluşturmak için ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb63b2d8-6ecc-49ab-b651-a9bd402e7c24)(Yeni) butonu tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload097cd379-ce6e-4306-b135-8822e69af754)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Değerlendirecek Kişi:** Risk Değerlendirme Talebi Tanımlama ekranında Değerlendirecek Kişi bilgisinin sistemde tanımlı olan Personel Listesinden seçilebildiği alandır.

**Talep Açıklama:** Risk Değerlendirme Talebi Tanımlama ekranında Talep Açıklama bilgisinin girildiği alandır.

Açılan pencerede Risk Talebi ekranında değerlendirecek kişi ve talebin açıklaması girildikten sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb412234-f80c-4cd2-a416-6147a15f7b5e) (kaydet) butonuyla talep kaydedilir ve ilgili kişiye aksiyon olarak açılır.
