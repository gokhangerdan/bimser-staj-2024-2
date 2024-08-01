---
title: FMEA Risk Değerlendirme
description: FMEA Risk Değerlendirme Yardım Dokümanı
sidebar_position: 25
---

:::tip Bilgi

İlgili konu başlığına sağ tarafta bulunan navigasyon yardımıyla hızlı bir şekilde ulaşabilirsiniz.

:::

**FMEA Risk Değerlendirme Modülü(v.5.24) Kullanıcı Yardım Dokümanı**

Modül Versiyonu: 5.24



**1.GİRİŞ:** FMEA İngilizce dilinde Failure Mode Effect Analysis kelimelerin kısaltması olan Türkçe karşılığı ise Hata Türü ve Etki Analizi olarak tanımlanmaktadır. Sistem, tasarım, süreç veya serviste oluşabilecek hataların analizi ile değerlendirmesi ve azaltılmasını hedefleyen bir Modüldür. Bu Modül sayesinde operasyonlardaki hataların önlenmesi, riskleri azaltılması ile verimliliğin artırılarak maliyetlerin düşürülmesi sağlanarak ve rekabet gücünün kazanılması sağlanmaktadır.

**2.AMAÇ:** Bu yardım kılavuzun amacı, Qdms FEMA-Hata Türleri ve Etki Analizi Modülün implementasyonu sırasında ve sonrasındaki risk formaları ve risklerle ilgili alınacak önlemlerin planlanması aşamasında izlenecek yolu belirlemektir.

**3.SORUMLULUKLAR:** Yönetim Sistemi Temsilcisi

**4.KISALTMALAR:**

FMEA: Hata Türleri ve Etkileri

RDF: Risk Değerlendirme Formu

RDFD: Risk Değerlendirme Form Detayı

**5.İŞ AKIŞI:**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload935b64e0-4708-4a24-9698-6eecf2881075)



# **6.FMEA Risk Değerlendirme Modülü**

Sistemde meydana gelebilecek potansiyel hata türlerinin analiz etmek amacıyla hataları olasılıklarına ve benzerliklerine göre sınıflandırma işlemini yapılması, olası risklerin tanımlanması, değerlendirilmesi, önceliklendirilmesi ve gerekli önlemlerin için aksiyonların alınmasını sağlayan modüldür.

## **6.1.Sistem Altyapı Tanımları/FMEA Risk Değerlendirme**

FMEA Risk Değerlendirme modülün altyapısının oluşturmak amacıyla gerekli tanımlamaların yapıldığı kısımdır. FMEA Risk Değerlendirme modülün altyapısının oluşturmak için 2 önemli menü bulunmaktadır. Bu menüler Alan Tanımlama ve Fonksiyon Dizanyer menüleridir. Alan Tanımlama menüsünde Risk ekranlarında yer alınacak alanlar tanımlanır. Fonksiyon Dizanyer menüsünde ise, tanımlanan alanların Risk formaları ve Risk Detayları ile ilişkisinin kurulması sağlanır. Yapılan bu menülerde tanımlamalara göre Entegre Yönetim Sistemi kısmında girişlerinde bu alanların görüntülenmesi ve alan girişleri yapılması sağlanır.

### **6.1.1.Alan Tanımlama**

**Menü Adı:** Sistem Altyapı Tanımları/ FMEA Risk Değerlendirme /Alan Tanımlama

FMEA Risk Değerlendirme modülünde ilişki kurulacak fonksiyonlarda Risk Formu ve Risk Detayı ekranlarında yer alacak bütün alanların tanımlandığı menüdür. Alan tanımlamaları Bimser Destek Ekibi tarafından tanımlı olarak sistemde yer almaktadır. Müşterinin isteği doğrultusunda ekstra alan tanımlamalarını bu menüde yapılması da olanak sağlanır. Burada tanımlanan alanlar alan havuzuna eklenmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload77b7a424-8f0c-406a-832d-91e547a3e794)

**Ekranda Bulunan Butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2d478a58-ec79-4917-8181-c1e686272c20)**:**Yeni bir alan tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload15fea01a-448f-40ad-b231-e577b694a279):Var olan alanda değişiklik yapılmak istenirse kullanılır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8253f73f-696d-4930-9fc3-182c0fe0c002):İlgili alanı silmek için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada275fe04-4771-4325-8e88-ae828a24c548) :Alanın değerlerini tanımlanır. (Tanımlanan Liste, puanlı liste gibi alan tiplerinde)

Listeye “Süreç, Konu” sorgu tipli alan eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload65717e0f-0fde-4ce0-ac98-7c75591b3a73)(Yeni) butonu tıklanarak Alan Tanımlama/Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc60cd0de-3c4a-414e-8685-e0f8c6dc48b9) ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8a3f6156-230b-464e-a96e-e35f7e6f8f74)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Alan Kodu:** Alan kodu bilgisi tanımlanır. Daha önce tanımlamış alanlarla aynı olmayacak şekilde boşluk, Türkçe karakter gibi karakterler kullanmadan tanımlanmalıdır. Ör. ‘001’ , ‘RK’

**Alan Adı:** Alan adı bilgisi tanımlanır.

**Başlık Notu:** Alanın başlık notu bilgisi tanımlanır.

**Giriş Tipi:** Oluşturulan alanda kullanıcı tarafından veri girişi/seçim mi yapacağı ya da hesaplama yöntemi ile otomatik olarak sistem tarafından mı atanacağı belirlenir.

**Seçim Tipi:**Oluşturulan alanın tekli ve çoklu seçim seçeneklerin belirlenir.

**Alan Tipi**: Oluşturulan alanın metin, numerik, tarih, liste vb. alan tiplerinden hangisi olacağı belirlenir.

**Görünme Şartı:** Tanımlama işlemi devam eden alanın daha önceden tanımlanan başka bir alanın değerine göre görünüp görünmeyeceği belirlenir. Kullanımı [ALANKODU]=ALAN_DEĞERİ vb. şekildedir.

**Durum:** Alan durumu aktif veya pasif olarak seçilir..

**İlişkili Alan:** İlişkili alan özelliği ile seçenek tipli iki alan arasında ilişki kurulabilmektedir. Referans alanın elemanlarının tanımlandığı ekranda ilişkili alandan hangi değerler ile ilişkili olduğu seçilebilmektedir. Böylece referans alanın form üzerinde değeri değiştiğinde ilişkili alan seçimli olarak otomatik dolabilmekte ya da seçim ekranından sadece ilişkilendirilen değerler arasından seçim yapılabilmektedir.

**İlişkili Alan Otomatik Doldurulsun:** ilişkili alan otomatik doldurulsun seçeneği aktif edilecekse ilgili kutucuk işaretlenir. Liste tipli iki alanın değerleri arasında kurulan ilişkiye göre alanlardan birinin otomatik doldurulmasını sağlar.

**Genişlik:** Alanın kolon genişliği bilgisi tanımlanır.

Sorgu tipli alanların tanımlama işleminde Tablo, Kod, Tanım, Açıklama, Sorgu Koşul ve Sorgu ilişkisi alanları ile bilgi girişlerinde Bimser Destek Ekibinde tarafında destek alınmalıdır.

Alan Tanımlama ekranında alan tipi alanında Sorgu seçilerek gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1c1ce32b-0149-4936-b3c2-959fc7a59e24) (Kaydet) butonu tıklanarak sorgu tipli alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadddce4953-b552-4907-a65e-f95dcc2b9913)

Listeye “Proses Öğeleri(Sistem, Alt Sistem, Parça veya Proses Adı” metin tipli alan eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload65717e0f-0fde-4ce0-ac98-7c75591b3a73)(Yeni) butonu tıklanarak Alan Tanımlama/Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload537f22fa-1b67-4870-b1bf-5b35839ead1c) ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb301e63e-d7b8-4554-9ae3-c0ddbe5eab5c)

Alan Tanımlama ekranında alan tipi alanında Metin seçilerek gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1c1ce32b-0149-4936-b3c2-959fc7a59e24) (Kaydet) butonu tıklanarak metin tipli alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddabe0c30-680d-4cad-94d9-6bb8b2daa57a)

Listeye “Proses Adımı, İstasyon No ve Odak Parçanın Adı” sorgu tipli alan eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload65717e0f-0fde-4ce0-ac98-7c75591b3a73)(Yeni) butonu tıklanarak Alan Tanımlama/Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade5076d5c-703b-48f8-ba42-3f3e5383a19f) ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9e120686-7fa5-4a77-baea-4b0bc49f249a)

Sorgu tipli alanların tanımlama işleminde Tablo, Kod, Tanım, Açıklama, Sorgu Koşul ve Sorgu ilişkisi alanları ile bilgi girişlerinde Bimser Destek Ekibinde tarafında destek alınmalıdır.

Alan Tanımlama ekranında alan tipi alanında Sorgu seçilerek gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1c1ce32b-0149-4936-b3c2-959fc7a59e24) (Kaydet) butonu tıklanarak sorgu tipli alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada6d75cbd-9cd6-4bf6-87c7-9842e56e7004)

Listeye “Proses İş öğeleri 4M Tipi(İnsan, Makine, Malzeme, Çevre)” metin çok satırlı tipli alan eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload65717e0f-0fde-4ce0-ac98-7c75591b3a73)(Yeni) butonu tıklanarak Alan Tanımlama/Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4d439cc4-c29b-4203-bba7-7858f7d40f7e) ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadee7da76b-97a9-4e45-891b-4042ec646429)

Alan Tanımlama ekranında alan tipi alanında Metin Çok Satırlı seçilerek gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1c1ce32b-0149-4936-b3c2-959fc7a59e24) (Kaydet) butonu tıklanarak Metin Çok Satırlı tipli alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf54fca0f-4073-41f7-be25-2a3f3b211da0)

Listeye “YAPISAL ANALİZ” Başlık tipli alan eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload65717e0f-0fde-4ce0-ac98-7c75591b3a73)(Yeni) butonu tıklanarak Alan Tanımlama/Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8601fbf7-864f-46d7-8b80-b70a03104ea6) ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada7880b35-d073-47da-a359-19ca3aed6bf5)

Alan Tanımlama ekranında alan tipi alanında Başlık seçilerek gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1c1ce32b-0149-4936-b3c2-959fc7a59e24) (Kaydet) butonu tıklanarak Başlık tipli alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload68707eba-c629-498b-83c1-89f6cdddc74a)

Listeye “Hatanın Nedeninin (FC) Olasılığı” Puanlı Liste tipli alan eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload65717e0f-0fde-4ce0-ac98-7c75591b3a73)(Yeni) butonu tıklanarak Alan Tanımlama/Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload479904a4-ee81-4feb-bb11-9c84bb218a8c) ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4d2b4022-dd41-444a-99fd-49d0c8fa50e5)

Alan Tanımlama ekranında alan tipi alanında Puanlı Liste seçilerek gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1c1ce32b-0149-4936-b3c2-959fc7a59e24) (Kaydet) butonu tıklanarak Puanlı Liste tipli alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload70fa5260-73a6-4ba3-a7dc-16e6e5839f7d)

“Hatanın Nedeninin (FC) Olasılığı” Puanlı liste tipli alanın değerleri eklemek için “Hatanın Nedeninin (FC) Olasılığı” alanı seçili iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6b726cd0-5bba-4389-a339-ee1938c32595)(Değerler) butonu tıklanarak alanın değerlerinin tanıtılacağı ekrana gelinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb379e466-ca5b-4247-b792-97fc68278bf6)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc3074170-893c-43b0-9a7b-2092be827c7e):Yeni botunu tıklanarak yenin değer tanımlama işlemine başlanır. İstenirse ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1aba927b-f1f9-4c64-b300-ae5c7af62686)(şablon İndir) ve ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf00ab593-6b9a-49c1-9952-409793f678f3)(Şablon Yükle) butonları ile sisteme toplu olarak alan değerleri aktarabilmektedir. ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1aba927b-f1f9-4c64-b300-ae5c7af62686)(Şablon İndir) butonu ile sistem şablonu bilgisayara indirir. İlgili şablon kullanıcılar tarafıdan doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf00ab593-6b9a-49c1-9952-409793f678f3)(Şablon Yükle) butonu ile sistem yüklendiğinde şablondaki tüm alan değerleri sisteme aktarılmış olur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9348bdac-df5b-4f82-a053-b74a142b77a8) ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1b5bf9e8-4e92-4acf-8b80-530dd5107080)

Gerekli alanlar doldurularak sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1c1ce32b-0149-4936-b3c2-959fc7a59e24) (Kaydet) butonu tıklanarak değer tanımlama işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload90305887-7ef5-4d6f-8d32-ab050bf606c2)

“Hatanın Nedeninin (FC) Olasılığı” Puanlı Liste tipli alanın liste elemanları(Değerleri) aynı şekilde tümü tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8ccc9d19-54e9-45d0-8cc2-d36c197d8f6a)

FMEA Risk Değerlendirme Modülünde ilişki kurulacak fonksiyonlarda Risk Formu ve Risk Detayı ekranlarında yer alacak bütün alanların tanımlama işlemi aynı şekilde yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload251cbc10-6c08-4110-9593-c9fa910f82ae)

FMEA Risk Değerlendirme modülünde ilişki kurulacak fonksiyonlarda Risk Formu ve Risk Detayı ekranlarında yer alacak bütün alanların tanımla işlemi Bimser Destek ekibi tarafından yapılır. Kullanıcılar bu modülde ekstra alan tanımlama işlemi yapmak isterlerse alan havuzuna ekleme işlemi yapabilir.

Sistemde mevcut bulunan alan tiplerinin tam listesi aşağıda belirtilmiştir;

-   **Metin:** Elle yazım imkanı veren metin kutucuğu ekler.
-   **Metin Çok Satırlı:** Elle yazım imkanı veren karakter sınırı olmayan çok satırlı metin kutucuğu ekler.
-   **Nümerik:** Sayısal olarak veri girişi yaptırır.
-   **Nümerik-Parasal:** Parasal değer olarak nümerik giriş yaptırır.
-   **Nümerik-Birim:** Birim olarak nümerik giriş yaptırır.
-   **Tarih:** Takvim alanı ekler.
-   **Liste:** Birden fazla element arasından tek seçim yaptırır.
-   **Puanlı Liste:** Açılır menüden seçim yaptırır, liste elementlerinin puan değerleri mevcuttur.
-   **Arama Özellikli Liste:** Birden fazla element arasından geniş arama fonksiyonuyla arama yapabilecek şekilde, tekli ve/veya çoklu seçim yapılmasını sağlar.
-   **Ağaç Liste:** Ağaç kırılımına sahip birden fazla element arasından geniş arama fonksiyonuyla arama yapabilecek şekilde seçim yapılmasını sağlar.
-   **Personel:** QDMS personel veri tabanından kişi seçilebilmesini sağlar.
-   **Departman:** QDMS departman veri tabanından departman bilgisi seçilebilmesini sağlar.
-   **Unvan:** QDMS unvan veri tabanından unvan bilgisi seçilebilmesini sağlar.
-   **Doküman:** QDMS doküman veri tabanından doküman seçilebilmesini sağlar.
-   **Süreç:** QDMS süreç veri tabanından süreç seçilebilmesini sağlar.
-   **Yönetim Sistemi:** QDMS yönetim Sistemi veri tabanından yönetim sistemi bilgisi seçilebilmesini sağlar.
-   **Müşteri:** QDMS müşteri veri tabanından müşteri bilgisi seçilebilmesini sağlar.
-   **Tedarikçi:** QDMS tedarikçi veri tabanından tedarikçi bilgisi seçilebilmesini sağlar.
-   **Ürün Grubu:** QDMS ürün grubu veri tabanından ürün grubu bilgisinin seçilebilmesini sağlar.
-   **Ürün:** QDMS ürün veri tabanından ürün bilgisinin seçilebilmesini sağlar.
-   **Şirket Profili:** QDMS şirket profili veri tabanından şirket profili bilgisi seçilebilmesini sağlar.
-   **Başlık:** Formlara koyu harflerle yazılacak başlık alanı ekler.
-   **Dosya:** Dosya ekler.
-   **Resim:** Resim ekler.
-   **Resim Liste:** Resim listesinden seçim sağlar.
-   **Çoklu Resim:** Çoklu resim seçilmesini sağlar.
-   **Tablo:** Tablo tipli alan oluşturulmasını sağlar. (Bu tip bir alan eklendikten sonra alan değerleri olarak yeni alan tanımlamalarının yapılması gereklidir.)
-   **Sorgu:** QDMS/Ensemble veritabanları içerisindeki ana verilerden seçim yapılabilmesi için tanımlanabilen alan türüdür. (Sadece Bimser Destek Ekibi tarafından tanımlanmalıdır) Tekli ve çoklu seçim yapılabilir.
-   **Sorgu Ağaç:** QDMS/Ensemble veritabanları içerisindeki ağaç kırılımlı ana verilerden seçim yapılabilmesi için tanımlanabilen alan türüdür. (Sadece Bimser Destek Ekibi tarafından tanımlanmalıdır) Tekli ve çoklu seçim yapılabilir.
-   **Sekme:** Aktif sekme haricinde alanların ilişki kurularak içerisinde görülebileceği yeni bir sekme oluşturur.
-   **Onay Kutusu Liste:** Tekli veya çoklu seçim yaptırılacak tipte bir liste tipli alandır.
-   **Risk:** Risk tabanlı modüllerden değerlerin seçilebilmesini sağlar. Bu tip bir alan eklendikten sonra hangi modülden değerlerin geleceği alan tanımlama ekranında seçilmesi gereklidir.
-   **Açıklamalı Liste:** Seçilen liste değerinin yanına açıklama yazabilme imkanı sağlayan alan tipidir. Alan Tanımlama menüsünde alan değerleri tanımlanırken her değer için açıklama kutucuğunun aktif olup olmayacağının seçilmesi gerekir. Burada yapılan seçime göre Entegre Yönetim Sistemi menüsü altında bu alanın görüleceği menüde ilgili seçim yapıldığında alan değerinin yanına kullanıcının açıklama yazabilmesi için kutucuk açılmış olur.
-   **Pozisyon:** QDMS pozisyon veri tabanından pozisyon bilgisi seçilebilmesini sağlar.
-   **Saat:** Saat tipli alan ekler.

### **6.1.2.Onay Akışı Tanımlama**

Değerlendirilen Risklerin belirlenen kullanıcılara onaya gitmesi için sistemde onay akışının kurgulanması gereklidir. İlgili Modülde Statü kullanımı aktifleştirilerek onay akış kurgusu gerçekleştirilir. Onay akış kurgusu için Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Parametreler menüsüne gidilir. Filtreden FMEA Risk Değerlendirme Modülü seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload728596f4-bc1c-41ce-9625-d8c32ae735f3)

22 numaralı parametre olan “Statü Kullanılacak mı?” parametresinin seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload70f0787d-6ec3-4f97-a0a3-80c255946468)

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload15fea01a-448f-40ad-b231-e577b694a279) (Değiştir) butonu tıklanarak 22 numaralı parametre olan “Statü Kullanılacak mı?” parametresinin parametre değeri Evet seçilerek parametre aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload904c1607-0841-40d5-be32-bbe0c62dec22)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc32262df-7553-442e-ba8e-3d26ac3db57a)

Akış tanımları Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/ Akış Tanımlama menüsünde kontrol edilmesi yoksa akışların bu menüde tanımlanması sağlanmadır. Ayrıca Sistem Altyapı Tanımları /BSAT/Konfigürasyon Ayarları/Rol Tanımlama menüsünde de onay akışları için Rol tanımları yapılır. Rol tanımlama işlemlerinde SQL ve QDMS veri tabanı bilgisi gerekeceğinden Bimser Destek Ekibiyle iletişeme geçilerek gerekli rol talep edilebilir.

#### **6.1.2.1.Rol Tanımlama**

Modüllerde onay akışları için onaycı olarak hangi role gideceğinin bilgisinin tanımlandığı menüdür. FMEA Risk Değerlendirme modülünde yeni bir Rol tanımlaması için Sistem Altyapı Tanımları\>BSAT\>Konfigürasyon Ayarları\>Rol Tanımlama menüsü tıklanılır. Açılan ekranda filtre sekmesinde FMEA Risk Değerlendirme modülü seçilir. ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload68bf1c2d-2df1-4c54-b41d-031cb27da4fe)(Ara) butonu tıklanarak sistemde tanımlı FMEA Risk Değerlendirme modülü ile ilgil Rol Tanımlarının listesi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6b6254be-a4c2-4979-838a-51a3e51c0e56)

FMEA Risk Değerlendirme modülü için Rol tanımlama ekranından yeni bir Rol eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload65717e0f-0fde-4ce0-ac98-7c75591b3a73) (Yeni) butonu tıklanarak Rol Tanımlama/Yeni Kayıt ekranın açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3aec8d99-918c-4875-af07-7af66477363e)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb96bac8b-fd81-4818-add9-91b21d926381)

Gerekli alanlar doldurultan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1c1ce32b-0149-4936-b3c2-959fc7a59e24) (Kaydet) butonu tıklanarak FMEA Risk Değerlendirme Modülü için Rol tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfd635934-60d4-43fc-8ba0-8ffceba02e9b)

#### **6.1.2.2.Mesaj Gövdesi Tanımlama**

Menü:Sistem Altyapı Tanımları/BSAT/Tanımlar/Mesaj Gövdesi Tanımlama

Modüllerde yapılan işlemler sonrasında gidecek olan maillerin içeriklerinin tanımlandığı menüdür. Sistemde FMEA Risk Değerlendirme modülü için mesaj gövdesi tanımlıdır. Tanımlı olan bu mesaj gövdelerinde güncelleme yapılır veya yeni mesaj gövdeleri tanımlanabilir.FMEA Risk Değerlendirme Modülü için Mesaj Gövdesi tanımlamak için Sistem Altyapı Tanımları/BSAT/TAnımlar/Mesaj Gövdesi Tanımlama menüsü tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4a28823b-782a-46bc-b5cd-8ee963f199fb)

Açılan ekranda Filtre sekemesinde FMEA Risk Değerlendirme Modülü seçilir. ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload68bf1c2d-2df1-4c54-b41d-031cb27da4fe) (Ara) butonu tıklanarak sistemde tanımlı FMEA Risk Değerlendirme Modülü ile ilgili Mesaj Gövdesi listesi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada9442480-8374-431f-afa9-39a66ffc0c72)

Mesaj Gövdesi Tanımlama ekranında FMEA Risk Değerlendirme Modülü için yeni bir Mesaj gövdesi eklemek için ekranın sağ üst kösesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload65717e0f-0fde-4ce0-ac98-7c75591b3a73) (Yeni) butonu tıklanarak Mesaj Gövdesi Tanımlama/Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload674e75ec-23c4-4b4d-8f7b-a2c556790a8f)

Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1c1ce32b-0149-4936-b3c2-959fc7a59e24) (Kaydet) butonu tıklanarak FMEA Risk Değerlendirme Modülü için Mesaj Gövdesi tanımalama kayıt işlemi gerçekleştirilir.

. ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload878261ec-1e06-49f8-b89d-468c775ff076)

#### **6.1.2.3.Akış Tanımlama**

**Menü Adı:**Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Akış Tanımlama

Modüllerde kullanılan onay akışlarının tanımlamaların yer aldığı menüdür. FMEA Risk Değerlendirme modülü için yeni bir akış tanımlaması yapılır. FMEA Risk Değerlendirme Modülü için yeni bir akış tanımlaması için Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Akış Tanımlama menüsü tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload07b8dd57-eaa0-417d-b604-fe8cb3b52d90)

Açılan ekranda Filtre sekemesinde FMEA Risk Değerlendirme Modülü seçilir. ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload68bf1c2d-2df1-4c54-b41d-031cb27da4fe) (Ara) butonu tıklanarak sistemde tanımlı FMEA Risk Değerlendirme Modülü ile ilgili Akış Tanımlama listesi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload897dc923-6af1-4e0f-9998-0639fb3cd68e)

Mesaj Gövdesi Tanımlama ekranında FMEA Risk Değerlendirme Modülü için yeni bir Akış Tanımlaması eklemek için ekranın sağ üst kösesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload65717e0f-0fde-4ce0-ac98-7c75591b3a73) (Yeni) butonu tıklanarak Akış Tanımlama/Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload90abd7ff-15aa-4e02-82f3-0af79cca909c)

Bu ekranda daha önceden sistemde FMEA Risk Değerlendirme Modülü için tanımlanmış olan rollerden ilgili olan rol seçilerek eklenir. ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload22e148ac-60a5-4356-9bad-e0ef194931c0) (Ekle) butonu tıklandığında FMEA Risk Değerlendirme Modülü için tanımlı Rol tanımlamalarında yer alan Roller açılmaktadır. Uygun olan Rol seçilip kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd7c3ea3a-ea40-49f7-b55f-220276a9d176)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb836b9f-0509-4baf-b363-6a22ab9141ec)

FMEA Risk Değerlendirme Modülü için birden çok akış onayıcısı tanımlanabilir. Ekranda sıra numarası onaycının kaçıncı sırada onay vereceğini belirtir. Hiyerarşisi yapılır. 0,1,2 gibi sıra numaraları ile en son sıfırıncı onaycı gelmesi sağlanabilir. Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1c1ce32b-0149-4936-b3c2-959fc7a59e24) (Kaydet) butonu tıklanarak FMEA Risk Değerlendirme Modülü için Akış tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadea7e8eea-9cf2-472b-b384-e5a93b48d4ee)

Akış Tanımlama için FMEA Risk Değerlendirme Modülü için uygun rol seçildikten sonra Alt Modüle Tanımlama menüsü kontrol edilmelidir. Alt Modülde tanımlama FMEA Risk Değerlendirme Modülü için uygun değilse akış uygun bir şekilde sağlanamayabilir veya istenilen akış çalışmayabilir.

FMEA Risk Değerlendirme Modülü için statü tanımlama işlemi için gerekli altyapı tanımlama işlemleri yapıldıktan sonra statü tanımlama işlemlerine başlamak için Sistem Altyapı Tanımları/FMEA Risk Değerlendirme/Fonksiyon Dizanyer menüsü tıklanılır. Açılan ekranda alan havuza eklenen alanların ilişkilendirileceği FMEA Risk Değerlendirme Modülü ile ilgili fonksiyonlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade1737e23-3c61-47df-81fe-d5cd3c7b4168)

FMEA Risk Değerlendirme Modülünün 22 numaralı “Statü Kullanılsın mı?(E/H)” parametresi değeri Evet seçilerek parametre aktif iken Fonksiyon Dizayner menüsünde Statü, butonlar ve Alanlar butonları görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload37b64e33-cda4-4e05-b1a1-dbd9a858385e)

**Ekranda bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4be59109-0251-4046-966a-fa419c9796fa)**:**Statü tanımlamak için kulllanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload572ae157-8052-4f2c-bfda-1969659d50cc)**:**Butonları tanımlamak için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload19b3fe7c-8c42-482f-b79b-0ef424703e61):Alanları fonksiyonlarla ilişkilendirmek için kullanılır.

Parametre değeri Evet seçilerek parametre aktif edildikten sonra FMEA Risk Değerlendirme Modülünde statü kullanılmasına imkan verilmesi sağlanır. FMEA Risk Değerlendirme modülünde 22 numaralı parametre aktif edildikten sonra görüntülenen statü ve butonlar butonları ile statülerin ve butonların tanımlama işlemi yapılır.

#### **6.1.2.4.Statü Tanımlama**

FMEA Risk Değerlendirme Modülünde Fonksiyon Dizayner menüsü tıklanılır. Açılan ekranda alan havuza eklenen alanların ilişkilendirileceği FMEA Risk Değerlendirme Modülü ile ilgili fonksiyonlar listelenir. 4. numaralı Risk Değerlendirme Detay Fonksiyonu seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload15774731-69cf-46fe-bedf-63523c39f1df)

4 numaralı Risk Değerlendirme Detay fonksiyonu seçili iken statü tanımlama işlemi gerçekleştirmek içim ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8349171e-7ceb-4ed4-8822-f69ac9133b27) (Statüler) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4d75ec39-fe4c-46cc-97fa-443323afc8c6)

**Ekranda bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2d478a58-ec79-4917-8181-c1e686272c20):Yeni bir statü tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload15fea01a-448f-40ad-b231-e577b694a279):Listede seçili statü bilgisi güncellenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8253f73f-696d-4930-9fc3-182c0fe0c002): Listede seçili statü bilgisi silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd7c897b9-0ab7-46f3-b814-bffe602af9f4):Önceki ekrana geri dönülür.

Statü tanımlama ekranında FMEA Risk Değerlendirme modülü için yeni bir statü eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload65717e0f-0fde-4ce0-ac98-7c75591b3a73) (Yeni) butonuna tıklanarak Statü tanımlama/Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload23ae57c4-9a22-49ff-b548-8b9b99b8c97f) **Açılan ekranda ilgili alanlar tanımlanır:**

**Statü Kodu:** Statü kodu bilgisi tanımlandığı alandır. Daha önce tanımlamış alanlarla aynı olmayacak şekilde boşluk, Türkçe karakter gibi karakterler kullanmadan tanımlanmalıdır.

**Statü Adı:** Statü adı bilgisi tanımlandığı alandır.

**Akış Başlatılsın:** Bu statüde herhangi bir akış başlatılacaksa akış başlatılsın check box işaretlendiği alandır.

**Yeni Statü:** Sistemde tanımlı statülerden seçilebildiği alandır.

**Onay Süresi:** Onay süresi bilgisi tanımlanır.

**İlk Hatırlatma:**  Onay süresi bilgisinin boyunca ilk hatırlatma mailinin gideceği gün tanımlanır. Tanımlanan günlerde onay için hatırlatma maileri gidilmesi sağlanır.

**İkinci Hatırlatma:** Onay süresi bilgisinin boyunca ikinci hatırlatma mailinin gideceği gün tanımlanır. Tanımlanan günlerde onay için hatırlatma maileri gidilmesi sağlanır.

**Son Hatırlatma:** Onay süresi bilgisinin boyunca son hatırlatma mailinin gideceği gün tanımlanır. Tanımlanan günlerde onay için hatırlatma maileri gidilmesi sağlanır.

**Revizyon Başlatılsın:** Tanımlanan statüde Revizyonun başlatılması isteniyorsa ilgili check box işaretlenir.

**Durum:** Statü durumu aktif veya pasif olarak seçilir.

**Akış Tanımı:** Sistemde tanımlı akışlarda hangi akışın olacağı seçilebildiği alandır. Akış tanımlama işlemi BSAT/Sistem Altyapı Tanımları/Konfigürasyon Ayarları/Akış Tanımlama menüsünde tanımlanır.

**Onay Talep Mesajı:** Sistemde tanımlı mesaj gövdesinde onay talep mesajının seçilir. Onay Talep Mesajı BSAT/Sistem Altyapı Tanımları/Tanımlar/Mesaj Gövdesi Tanımlama menüsünde tanımlanır.

**Onay Tamam Mesajı:** Sistemde tanımlı mesaj gövdesinde onay tamam mesajının seçilir. Onay Tamam Mesajı BSAT/Sistem Altyapı Tanımları/Tanımlar/Mesaj Gövdesi Tanımlama menüsünde tanımlanır.

**Onay Red Mesajı:** Sistemde tanımlı mesaj gövdesinde oany red mesajının seçilir. Onay red Mesajı BSAT/Sistem Altyapı Tanımları/Tanımlar/Mesaj Gövdesi Tanımlama menüsünde tanımlanır.

Açılan ekranda statü kodu, statü adı, akışın başlatılıp başlatılmayacağı, yeni statü, durum, akış tanımı, onay talep mesajı, onay tamam mesajı ve onay ret mesajı veri girişleri yapılarak gerekli alanlar doldurulduktan sonra ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1c1ce32b-0149-4936-b3c2-959fc7a59e24) (Kaydet) botunu tıklanarak statü tanımlama kayıt işlemi FMEA Risk Değerlendirme modülü için yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada8fa1ac3-c62d-434d-9917-f32db06a3003)

FMEA Risk Değerlendirme Modülünde 4 numaralı Risk Değerlendirme Detay fonksiyonu için ilgili tüm statülerin tanımlama işlemi aynı şekilde yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0b36dda9-1e88-4f3b-ae51-f56c5cecc47c)

Aynı şekilde FMEA Risk Değerlendirme Modülü için 3 numaralı Risk Değerlendirme Form Tanımlama fonksiyonu için statü tanımlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0bf9f4fa-75ea-4a3f-a2ae-0d945e356bbf)

#### **6.1.2.5.Buton Tanımlama**

FMEA Risk Değerlendirme Modülünde fonksiyon Dizanyer menüsü tıklanarak Risk detayı ve Risk Formunda kullanılacak butonların tanımlama işlemi yapılır. Açılan ekranda alan havuzana eklenen alanların ilişkilendirileceği FMEA Risk Değerlendirme Modülü ile ilgili fonksiyonlar listelenir. 4 numaralı Risk Değerlendirme Detay fonksiyonu seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload86c1f1dd-8317-4565-9f6d-4940a668bb9b)

4 numaralı Risk Değerlendirme Detay fonksiyonu seçili iken FMEA Risk Değerlendirme modülü ile ilgili buton tanımlama işlemini gerçekleştirmek için ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddd153e4c-2064-4f97-abff-86eefb4fe9fd) (Butonlar) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9dd283c6-8737-4240-972b-09d0df27097e)

**Ekranda bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2d478a58-ec79-4917-8181-c1e686272c20):Yeni bir buton tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload15fea01a-448f-40ad-b231-e577b694a279):Listede seçili buton bilgisi güncellenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8253f73f-696d-4930-9fc3-182c0fe0c002): Listede seçili buton bilgisi silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd7c897b9-0ab7-46f3-b814-bffe602af9f4):Önceki ekrana geri dönülür.

Statü tanımlama ekranında FMEA Risk Değerlendirme modülü için yeni bir buton eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload65717e0f-0fde-4ce0-ac98-7c75591b3a73) (Yeni) butonuna tıklanarak Buton Tanımlama/Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc87e36e4-24dd-4a61-a0f2-c8aff107c907)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Buton Kodu:** Buton kodu bilgisi tanımlanır. Daha önce tanımlamış alanlarla aynı olmayacak şekilde boşluk, Türkçe karakter gibi karakterler kullanmadan tanımlanmalıdır.

**Buton Adı:** Buton adı bilgisi tanımlanır.

**Buton Tipi:** Sistemde tanımlı buton tipi seçeneklerinde belirlendiği alandır.

**Resim:** Tanımlanan butonun resminin hangi buton resmi olacağının sistemde tanımlı buton resim seçeneklerinden belirlendiği alandır.

**Görünür Statü:** Tanımlanan butonun hangi statüde görüntüleneceği belirlendiği alandır.

**Yeni Statü:** Tanımlanan butona tıkanıldığında hangi statü geçiş yapacağı sistemde tanımlı statülerden seçildiği alandır.

**Durum:** Tanımlanan butonun durumu aktif veya pasif olarak seçilir.

**Uyarı Mesajı:** Tanımlanan butona tıklatıldığında ekranda uyarı mesajının bilgisinin girildiği alandır. Örneğin: Onaya göndermek istediğinizden emin misiniz?

Açılan ekranda Buton kodu, Buton adı bilgisi girilir. Buton tipi ve Resmi belirlenir. Görünür statüsü, Yeni statüsü ve durumu seçilir. Gerekli alanlar doldurulduktan sonra ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0e8a956a-2a53-4c37-a53d-8c138b292d72) (Kaydet) butonu tıklanarak FMEA Risk Değerlendirme modülü için buton tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb463a804-e2a7-4b13-ac09-36d8daf7bdc9)

FMEA Risk Değerlendirme Modülünün 4 numaralı Risk Değerlendirme Detay fonksiyonu için bütün butonların tanımlama işlemi aynı şekilde yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd534da83-36c6-4ac3-a87e-ca8651e26d71)

FMEA Risk Değerlendirme Modülün 3 numaralı Risk Değerlendirme Form Tanımlama fonksiyonu içinde aynı şekilde buton tanımlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload41930efe-9920-4502-b208-7cf799faaf2b)

### **6.1.3.Fonksiyon Dizanyer**

**Menü Adı:** Sistem Altyapı Tanımları/FMEA Risk Değerlendirme/Fonksiyon Dizanyer

Fonksiyon Dizanyer menüsü ile alan havuzuna eklenen alanlar FMEA Risk Değerlendirme Modülünün ilgili fonksiyonların sayfaları ile ilişkilendirilir. Bunun için Sistem Altyapı Tanımları kısmında FMEA Risk Değerlendirme Modülünün Fonksiyon Dizanyer menüsüne tıklanılır. Açılan ekranda FMEA Risk Değerlendirme Modülünde alan eklenebilecek fonksiyonlar sıralanır. Bu ekranda Kaynak Grubu Tanımlama, Kaynak Tanımlama, Risk Değerlendirme Form Tanımlama, Risk Değerlendirme Detay, Önlem Tanımlama ve Kontrol Tanımlama fonksiyonlarında kullanılacak alanlar ve bunların sıralaması ile onay işlemlerindeki hiyerarşi detayı tanımlanır. Bu menüde FMEA Risk Değerlendirme Modülünde 3 numaralı Risk Değerlendirme Form Tanımlama ve 4 numaralı Risk Değerlendirme Detayı menüsünün sayfalarıyla ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbc99c4ee-324b-4e66-a34b-91e3420e6de1)(Alanlar) butonu yardımıyla ilişkilendirilmesi işlemi yapılacaktır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload35a1575e-3c3b-47d0-a897-e092960c65ed)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7734222c-f654-4691-929e-8c659d00f357)

**Ekranda bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2d478a58-ec79-4917-8181-c1e686272c20):Yeni Fonksiyon eklenir

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload15fea01a-448f-40ad-b231-e577b694a279):Listede seçili fonksiyon bilgisi güncellenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8253f73f-696d-4930-9fc3-182c0fe0c002): Listede seçili fonksiyon bilgisi silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd7c897b9-0ab7-46f3-b814-bffe602af9f4):Önceki ekrana geri dönülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbc99c4ee-324b-4e66-a34b-91e3420e6de1)(Alanlar) butonu ile FMEA Risk Değerlendirme Modülü için açılan ekranda seçili fonksiyonda kullanılacak Alanlar ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload65717e0f-0fde-4ce0-ac98-7c75591b3a73) (Yeni) butonu tıklanarak belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadce39351a-72da-4854-8500-dea228142d68)

**Alan Adı:** Alan tanımlama ekranında tanımlanmış alanlardan alan seçimi yapılır.

**Zorunluluk Mesajı:** Zorunlu alan doldurulmadığında verilecek uyarı mesajı bilgisi bu alana yazılır.

**Sıra No:** Alanın sıra no belirlenir.

**Varsayılan Rol:** İlgili alanın değeri daha önce tanımlanmış bir üst formdan ya da kaydı giren kişinin adı soyadı, pozisyonu, unvanı, departmanı, iş yeri gibi verileri ise bunlar için tanımlanmış rol seçilebilir.

**Varsayılan Değer Değiştirilmesin:** Seçilen alan varsayılan olarak bir değer getiriyorsa getirdiği değerin değiştirmemesini sağlar.

**Gridde göster:** Alanın gridde gösterilmesi gerekiyorsa ilgili check box işaretlenir.

**Seçimde göster:** Alanın seçimde gösterilmesi gerekiyorsa ilgili check box işaretlenir.

**Satır Sayısı:** İlgili alan çoklu satır ise, veri girişi ekranında kaç satır gözükmesi gerektiği belirlenir.

**Kolon Genişliği:** İlgili modülde girilen kayıtların listesinde (gridde) alanın kolon genişliği bilgisinin belirlenir. Verinin uzun olduğu alanlar için ort. 250, sadece rakam girilen alanlar için ise 75 kullanılması idealdir. Alana girilecek veriler düşünülerek bu aralıklarda bir değer kullanmak uygun olacaktır.

**Aktif Statü:** Alanın sisteme tanımlanan statülerin hangilerinde aktif olacağını belirler. Bu alanda işaretlenen statülerde ilgili alanın tipine göre işlem gerçekleştirilebilir.

**Görünür Statü:** Alanın sisteme tanımlanan statülerin hangilerinde görüleceğini belirler. Aktif statüsü seçilen alanlar için aynı zamanda görünür statüde en az aktif statü alanında işaretlenen statüler olacak şekilde belirlenmelidir.

**Zorunlu Statü:** **:** Alanın sisteme tanımlanan statülerin hangilerinde zorunlu olacağını belirler.

Açılan ekranda alan bilgileri listeden seçilir, zorunlu bir alan ise kullanıcının bu alanı doldurmadığında çıkacak mesaj tanımlanır, sıra numarası belirlenir. Aktif statü, Görünür Statü ve Zorunlu Statü durumları seçilir. Zorunlu olup olmadığı, gridde gösterilip gösterilmeyeceği, kolon genişliği belirlenerek gerekli tüm alanlar doldurulduktan sonra ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfd531407-d54c-41f6-820a-79eef27164d8) (Kaydet) butonu tıklanarak, ilgili alan için fonksiyon ile ilişkilendirme işlemi gerçekleştirilir. FMEA Risk Değerlendirme Modülünün 3 numaralı Risk Değerlendirme Form Tanımlama fonksiyonu için bütün alanları ilgili fonksiyonun sayfaları ile ilişkilendirilmesi işlemi aynı şekilde yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada35485fd-932b-4e1d-a2ff-b40934fa39fc)

FMEA Risk Değerlendirme Modülün 4. numaralı Risk Değerlendirme Detayı fonksiyona aynı şekilde ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbc99c4ee-324b-4e66-a34b-91e3420e6de1)(Alanlar) butonu ile fonksiyonun sayfalarıyla ilişkilendirilme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3a874c77-1802-4d0e-afb3-f46040905856)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbc99c4ee-324b-4e66-a34b-91e3420e6de1)(Alanlar) butonu ile FMEA Risk Değerlendirme Modülü için açılan ekranda seçili fonksiyonda kullanılacak Alanlar ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload65717e0f-0fde-4ce0-ac98-7c75591b3a73) (Yeni) butonu tıklanarak belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9bc14b1b-d7c6-44f6-96d6-7016b4ef9f75)

Açılan ekranda alan bilgileri listeden seçilir, zorunlu bir alan ise kullanıcının bu alanı doldurmadığında çıkacak mesaj tanımlanır, sıra numarası belirlenir. Aktif statü, Görünür Statü ve Zorunlu Statü durumları seçilir. Zorunlu olup olmadığı, gridde gösterilip gösterilmeyeceği, kolon genişliği belirlenerek gerekli tüm alanlar doldurulduktan sonra ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfd531407-d54c-41f6-820a-79eef27164d8) (Kaydet) butonu tıklanarak, ilgili alan için fonksiyon ile ilişkilendirme işlemi gerçekleştirilir. FMEA Risk Değerlendirme Modülünün 4 numaralı Risk Değerlendirme Detay fonksiyonu için bütün alanları ilgili fonksiyonun sayfaları ile ilişkilendirilmesi işlemi aynı şekilde yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d0a65f6-a36d-4493-ba37-9b9fee8dd532)

### **6.1.4.Risk Dağılım Matrisi Tanımlama**

**Menü Adı:** Sistem Altyapı Tanımları/ FMEA Risk Değerlendirme/ Risk Dağılım Matrisi Tanımlama

FMEA Risk Değerlendirme modülünde Risk Dağılım Matrisi tanımlama işleminin gerçekleştiği menüdür. Risk Dağılım Matrisi tanımlamadaki amaç, belirlenen parametrelere göre risk dağılımın hangi aralıklarda daha yoğun olduğunu tespit etmektir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload55780681-644e-47ff-9e2a-13d7d2ad74d1)

**Ekranındaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2d478a58-ec79-4917-8181-c1e686272c20): Yeni bir Risk Dağılım Matrisi tanımlar.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload15fea01a-448f-40ad-b231-e577b694a279): Listede seçili Risk Dağılım Matrisi bilgisi günceller.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8253f73f-696d-4930-9fc3-182c0fe0c002): Listede seçili Risk Dağılım Matrisi bilgisi silinebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8be4c125-974b-4d44-b5b4-4be8059ac488): Risk dağılım matrisini renklendirir.

Listeye yeni bir Risk Dağılım Matrisi eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload65717e0f-0fde-4ce0-ac98-7c75591b3a73) yeni butonu tıklanarak Risk Dağılım Matrisi Tanımlama\\Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload264b2895-34ed-4756-b229-1896020b3ea3)

Açılan ekranda “Grafik Adı” belirlenir. X ve Y eksenindeki parametreler için risk karşılaştırmasında kullanılacak alanlar belirlenir. Bu alanların alan tanımlama menüsündeki formülleri “X Formülü” ve “Y Formülü” kısımlarına yazılır. “X Aralıkları” ve “Y Aralıkları” kısımlarına ise alanların değerleri girilir. İşlemler tamamlandıktan sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1c1ce32b-0149-4936-b3c2-959fc7a59e24) (kaydet) butonu tıklanarak kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3a8ca472-bff2-4ee3-8e2b-f56b77616355)

Risk Dağılım Matrisini kullanılan yönteme uygun olarak renklendirmek için risk dağılım matrisi tanımlama ekranındaki sağ üst köşede bulunan “Renklendir” ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload369df482-5e71-4b68-abbb-737103e5a222) butonuyla oluşturulan matris açılır. Ekrandaki her kutucuğun üzerine tıklanarak kutucuklar renklendirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload89cdc4fd-8fcc-4857-bcc7-d06d1189fcbe)

### **6.1.5.FMEA Risk Değerlendirme Parametreleri**

**Menü Adı:** Sistem Altyapı Tanımları/ FMEA Risk Değerlendirme / FMEA Risk Değerlendirme Parametreleri

FMEA Risk Değerlendirme Modülünün kullanıcının istek ve ihtiyaçlarına göre sistemsel ayarlarının yapıldığı ve bunlara göre parametreleri belirlendiği menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload006cfd6b-0891-4c3a-838e-ccac32f91e61)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload15fea01a-448f-40ad-b231-e577b694a279): Listede seçili parametre değiştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload68bf1c2d-2df1-4c54-b41d-031cb27da4fe): Kayıtlar filtrelenerek arama yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb16af0e0-2acd-429e-be34-798b5b83b69a): Veriler Excel’ e aktarılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8eba924d-562b-40fc-9456-2ed1c0bd0d29)

### **6.1.6.E-Posta Ayarları**

**Menü Adı:** Sistem Altyapı Tanımları/ FMEA Risk Değerlendirme / E-Posta Ayarları

FMEA Risk Değerlendirme modülünden oluşturulacak maillerin kime ve hangi mesaj gövdesiyle gönderileceğinin ayarlandığı menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf5d23ba0-a9dc-40b5-a77e-320560009266)

Bildirim ayarı yapılacak değerin üzerine gelinip ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload62b5bf88-f405-4e6c-98ee-fb577fb54c91) (Değiştir) butonu tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload431c0f1e-ee1c-43ca-a3d6-085086333a74)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload62b5bf88-f405-4e6c-98ee-fb577fb54c91) (Değiştir) butonu ile değerin içine girildikten sonra rollere göre uygun mesaj gövdesi seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload98966984-e824-4b43-bd5a-f5dc4e2e4f20)

E-posta gitsin mi check box’ı işaretlenerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0e8a956a-2a53-4c37-a53d-8c138b292d72)(kaydet) butonu tıklanarak kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload210ebb16-fa4a-4901-99ec-e17fd3fa7b45)

### **6.1.7.Rapor Formatları**

**Menü Adı:** Sistem Altyapı Tanımları/ FMEA Risk Değerlendirme / Rapor Formatları

FMEA Risk Değerlendirme metotlarına göre farklı rapor formatları oluşturmak için Rapor Formatları menüsü kullanılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload710fec35-4e8c-49b9-afe5-9b627fb518c5)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2d478a58-ec79-4917-8181-c1e686272c20):Yeni bir Rapor Formatı tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload15fea01a-448f-40ad-b231-e577b694a279): Listede seçili Rapor Formatı bilgisi güncellenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8253f73f-696d-4930-9fc3-182c0fe0c002): Listede seçili Rapor Formatı bilgisi silinebilir.

Bunun için öncelikle SAT/BSAT/Konfigürasyon Ayarları/Rapor Formatları Düzenleme menüsüne oluşturacağımız rapor formatlarının tümü tanımlanmalıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbf2e0be7-c4d7-450a-ad8d-1251148c7054)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9bd2c450-fc4b-4a1a-b3cb-f9ac2618be2d):Sisteme yeni bir Rapor formatı yüklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload847c8c47-e34e-4159-a03f-bea84ed9053b):Listede seçili Rapor Formatı görüntülenip, indirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload65b14add-da35-4e0c-8a27-4f225e5723d6):Listede seçili Rapor Formatı silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9bd2c450-fc4b-4a1a-b3cb-f9ac2618be2d)(Yeni) butonu tıklanarak sisteme Rapor Formatı Şablonun yükleme işlemine başlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddbc182c3-6078-4790-968a-49fadfe1e0ea)

Açılan ekranda Rapor Formatının adı uzantısıyla beraber kopyalanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload440f5199-013c-4242-affe-130665d9d9d0)

Ardından SAT/ FMEA Risk Değerlendirme /Rapor Formatları menüsü açılır. Listeye yeni bir Rapor formatı eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload65717e0f-0fde-4ce0-ac98-7c75591b3a73) (Yeni) butonu tıklanarak Rapor formatı \\Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload77ba0b8d-76b8-4ca1-b055-111ebb73df8e)

Kopyalan Rapor formatının adı ve uzantısı Rapor Şablonu alanında sağ tıkla/Yapıştır yöntemi ile yapıştırılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4cd39e65-6b3b-4b41-beeb-862ed93ec97c)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Rapor Tanımı:** Rapor tanımı bilgisinin girilir.

**Rapor Şablonu:** rapor şablonun adı ve uzantısı bilgisi girilir.

**Rapor Tipi:** Kayıt bazında, form bazında ve genel olmak üzere üç seçenek rapor tipi bilgisi seçilebilir.

**Kayıt Bazında:** Her bir risk kaydının ayrı olarak raporlanması talep edildiğinde seçilir. (EYS/ FMEA Risk Değerlendirme /Risk Değerlendirme Formu tanımlama menüsünde Detaylar butonuna basıldıktan sonra çıkan “PDF” butonuyla alınır. Kayıt bazında tanımlama olmadığı sürece PDF butonu görüntülenmez.)

**Form Bazında:** Her risk formu altındaki risk detay kayıtlarının tek bir liste halinde Excel’e aktarıldığı durumlar için seçilir.(EYS/ FMEA Risk Değerlendirme /Risk Değerlendirme Formu Tanımlama menüsünde Detaylar butonuna basıldıktan sonra çıkan “Excel” butonuyla alınır.)

**Genel:** Tüm risk detay kayıtlarının tek bir Excel’de görülmesi talep edildiği durumda seçilir.(EYS/ FMEA Risk Değerlendirme /Raporlar/Genel Risk Listesi Rapor ekranından alınır.)

**PDF olarak oluştur:** Rapor tipi kayıt bazında seçilen rapor formatlarında Entegre Yönetim Sistemi/FMEA Risk Değerlendirme /Risk Değerlendirme Formu Tanımlama/Risk Değerlendirme Form Detayı ekranında seçilen bir risk kaydının PDF olarak aktarılabilmesi için bu kutucuk işaretlenebilir.

Açılan ekranda tanıtılacak rapor formatlarının isimleri Rapor Tanımı alanına yazılır. Rapor Şablonu alanına ise rapor formatları düzenleme menüsünden kopyalanan dosya adı **uzantısıyla birlikte** yapıştırılır. Rapor Tanımlama ekranında gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1c1ce32b-0149-4936-b3c2-959fc7a59e24) (Kaydet) butonu tıklanarak Rapor Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade9cfee05-8dbd-4bbd-a933-6946795ced82)

### **6.1.8.Kontroller**

#### **6.1.8.1.Kontrol Tanımlama**

**Menü Adı**: Sistem Altyapı Tanımları/ FMEA Risk Değerlendirme / Kontroller/ Kontrol Tanımlama

Kontroller QDMS'te Risk Modüllerinde kullanılır. Kontroller 27001 EK A maddesinde geçen maddelerdir ve önlemler sekmesinde gelmektedir. Önlemler sekmesinde her bir risk için kontrol adımı seçebilebilir.Önlemler sekmesinde, seçtiğiniz kontrol maddeleri, QDMS ortamında raporlar başlığında SOA raporu almak istediğinizde karşınıza çıkacaktır.Kısaca Kontroller SOA raporunun hazırlanmasında kullanılmaktadır. 95 nolu parametre evet ise kontroller risk yeni kayıt ekranında sekme olarak karşımıza çıkar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd82fbdd1-e451-456e-b5c6-2216eeb66281)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2d478a58-ec79-4917-8181-c1e686272c20): Yeni bir Kontrol tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload15fea01a-448f-40ad-b231-e577b694a279): Listede seçili Kontrol bilgisi güncellenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8253f73f-696d-4930-9fc3-182c0fe0c002): Listede seçili Kontrol bilgisi silinebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb16af0e0-2acd-429e-be34-798b5b83b69a): Veriler Excel’ e aktarılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload68bf1c2d-2df1-4c54-b41d-031cb27da4fe): Kayıtlar filtrelenerek arama yapılabilir.

Kontrol Tanımlama ekranına yeni bir Kontrol eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload65717e0f-0fde-4ce0-ac98-7c75591b3a73)(yeni) butonu tıklanarak Kontrol Tanımlama\\Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb3faec8c-31bd-4011-b1c5-fbc1afda9495)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Kontrol Kodu:** Kontrol Tanımlama ekranında Kontrol Kodu bilgisinin girildiği alandır.

**Bağlı Olduğu Kontrol:** Oluşturulma aşamasında olan Üst Kontrol Kodu, bir kontrol kodu tanımının alt kırılımı olması halinde bu alan otomatik dolu gelir. Dolu olarak gelen alanda bağlı olduğu kontrol kodu tanımının adı yazar. Bağlı olduğu üst kırılım silinmek istenildiğinde sağ yanda bulunan ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9fce39ad-22d8-41a4-877b-e04cafb1ddab) (Sil) butonu veya değiştirilmek istenildiğinde sağ yanda bulunan ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcf1c843b-70df-4d74-8987-0e920bc81e5a) (Seç) butonu kullanılır. Bağlı olduğu bir üst kontrol yok ise bu alan boş gelir.

**Kontrol Tanımı:** Kontrol Tanımlama ekranında Kontrol Tanım bilgisinin girildiği alandır.

**Açıklama:** Kontrol Tanımlama ekranında Açıklama bilgisinin girildiği alandır.

**Durum:** Kontrol Tanımlama ekranında Aktif ve Pasif durum bilgisinin seçilebildiği alandır.

Kontrol Tanımlama ekranında gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1c1ce32b-0149-4936-b3c2-959fc7a59e24) (Kaydet) butonu tıklanarak Kontrol Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1a5dc0fc-c91c-4298-811c-4d2cb2e9fb66)

### **6.1.9.Alan Menüsü Tanımlama**

**Menü Adı:** Sistem Altyapı Tanımları/ FMEA Risk Değerlendirme / Alan Menüsü Tanımlama

Liste tipli alanlara değer eklenmesi için Entegre Yönetim Sistemi altında menü oluşturulmasını sağlayan menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload01cebc6b-c17f-4b0c-ad14-9de0311475f7)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2d478a58-ec79-4917-8181-c1e686272c20): Yeni menü tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload15fea01a-448f-40ad-b231-e577b694a279): Listede seçili menü bilgisi güncellenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8253f73f-696d-4930-9fc3-182c0fe0c002): Listede seçili menü bilgisi silinir.

Listeye yeni bir Menü eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload65717e0f-0fde-4ce0-ac98-7c75591b3a73) (Yeni) butonu tıklanarak Menü Tanımlama\\ Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc119ec30-83b8-4950-85b4-dca74db7ae69)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Açılan ekranda ilgili alanlar tanımlanır:**

**Menü Adı:** Menü adı bilgisi tanımlanır.

**Alan:** Alan bilgisi seçilir.

**Sıra No:** Sıra no bilgisi girilir.

Menü tanımlama ekranında gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1c1ce32b-0149-4936-b3c2-959fc7a59e24) (Kaydet) butonu tıklanarak menü tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb45295db-6fe2-41e9-b554-72be4f6cb525)

Menü tanımlaması yapıldıktan sonra FMEA Risk Değerlendirme Modülün Entegre Yönetim Sistemi kısmında menü olarak görüntülenmesi için SAT/BSAT/Tanımlar/Yetki Grupları Tanımlama menüsünde menü görme yetkisi verilmelidir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload83ae59df-ae49-4487-a680-3aa4ef737dab)

Tanımlanan menünün Yetki Grupları Tanımlama menüsünde menü görme yetkisi verildikten sonra FMEA Risk Değerlendirme Modülün Entegre Yönetim Sistemi kısmında menü olarak görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf7adbd20-31ac-4a4d-b912-8fef24e28d3d)

### **6.1.10. Tekrar Eden Kayıtlar Raporu Şablonu**

**Menü Adı**: Sistem Altyapı Tanımları/ FMEA Risk Değerlendirme/Tekrar Eden Kayıtlar Raporu Şablonu

Sistemde bir kullanıcı için istenen konularda tekrar eden kayıtları gösteren menüdür. İlk olarak Sistem Altyapı Tanımları/ FMEA Risk Değerlendirme /Tekrar Eden Kayıtlar Raporu Şablonu menüsünden raporda çekilecek alanlar seçilir.

Daha sonra Entegre Yönetim Sistemi/ FMEA Risk Değerlendirme /Raporlar/Tekrar Eden Kayıtlar raporundan ilgili rapora ulaşılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0855e5a9-0a2b-47e0-9e44-146dd3bf3d31)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9bd2c450-fc4b-4a1a-b3cb-f9ac2618be2d): Yeni Tekrar Eden Kayıtlar Şablonu tanımlanır

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9246c9f6-b364-41b7-bb6d-ac2a2cbaf3a1): Listede seçili Tekrar Eden Kayıtlar Şablonu bilgisi güncellenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload65b14add-da35-4e0c-8a27-4f225e5723d6): Listede seçili Tekrar Eden Kayıtlar Şablonu bilgisi silinebilir.

Tekrar Eden Kayıtlar Raporu Şablonları ekranına yeni bir Tekrar Eden Kayıtlar Raporu Şablonları eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload65717e0f-0fde-4ce0-ac98-7c75591b3a73)(Yeni) butonu tıklanarak Tekrar Eden Kayıtlar Raporu Şablonları \\Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload59301fdd-477c-4420-9f7e-3f0de99fa7c0)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Tanım:** Tekrar Eden Kayıtlar Raporu Şablonları ekranında Tekrar Eden Kayıtlar Raporu Şablonları tanım bilgisinin girildiği alandır.

**Kolanlar:** Tekrar Eden Kayıtlar Raporu Şablonları ekranında Kolanlar bilgisinin seçilebildiği alandır. Seçilen Kolanlar Tekrar eden Kayıtlar Raporunda alan olarak görüntülecektir. Bu alanlar ile ilgili bilgilere rapora yansıyacaktır.

Açılan ekranda Tekrar Eden Kayıtlar Raporu tanım bilgisi girilir. İlgili Kolanlar seçilir. Tekrar Eden Kayıtlar Raporu Şablonları ekranında gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1c1ce32b-0149-4936-b3c2-959fc7a59e24) (kaydet) butonu tıklanarak Tekrar Eden Kayıtlar Raporu Şablonları kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload58711e73-8481-4c77-ada5-4d104f47831a)

Entegre Yönetim Sistemi/ FMEA Risk Değerlendirme /Raporlar/Tekrar Eden Kayıtlar raporundan ilgili rapor şablonu seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada00686b6-1aa0-4138-aff0-e6d4a84011cb)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload68bf1c2d-2df1-4c54-b41d-031cb27da4fe) (Ara) butonu ile kayıtlar filtrelenerek arama yapılabilir ve ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb16af0e0-2acd-429e-be34-798b5b83b69a)( Excel aktar) botunu ile veriler Excel’ e aktarılabilir.

## **6.2.Entegre Yönetim Sistemi/FMEA Risk Değerlendirme**

Faaliyet, Faaliyet Grubu, Risk Formları, Risk Form Detayların tanımlandığı, Raporların ve Grafiklerin görüntülendiği kısımdır.

### **6.2.1.Faaliyet Grubu Tanımlama**

**Menü Adı:** Entegre Yönetim Sistemi/FMEA Risk Değerlendirme/Faaliyet Grubu Tanımlama

FMEA Risk Değerlendirme Modülünde Faaliyet gruplarının tanımlama işlemi yapıldığı menüdür. FMEA Risk Değerlendirme Modülü sistemde risk kaynağı kullanılacaksa 23 numaralı “Risk Kaynağı kullanılacak mı?” parametresinin parametre değeri Evet seçilerek aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7311f1a7-6d67-4c3f-b0b2-2b5429c3d605)

Bu parametre aktif hale getirildikten sonra Faaliyet Grubu Tanımlama ve Faaliyet Tanımlama işlemleri gerçekleştirilir. Faaliyetlerin tanımlanması için öncelikle bu faaliyetlere bağlı bulunacağı grupların tanımlanması gerekir. Bunun için FMEA Risk Değerlendirme Modülün Entegre Yönetim Sistemi başlığı altına gelinerek Faaliyet Grubu tanımlama menüsü tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd8151d22-795d-4040-998b-788bffc18f1b)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6a14dc29-eedc-4eca-bee5-12a74c81bc15): Yeni bir Faaliyet Grubu tanımlanabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfa7c6075-89e6-4f8d-a070-8fdfd456b2eb): Listede seçili Faaliyet Grubu bilgisi güncellenebilir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8253f73f-696d-4930-9fc3-182c0fe0c002): Listede seçili Faaliyet Grubu bilgisini silmek için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6a476f09-818a-4e91-9c60-d1b9699d2f9a): Faaliyet grupları Excel’ e aktarılır.

Faaliyet Grubu Tanımlama ekranına yeni bir Faaliyet Grubu eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload65717e0f-0fde-4ce0-ac98-7c75591b3a73)(Yeni) butonu tıklanarak Faaliyet Grubu Tanımlama \\Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf48e8803-2c84-484e-8929-a4ab98a73a61)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Bağlı Olduğu Faaliyet Grubu:** Bağlı olunan faaliyet grubu bilgisi sistemde tanımlı olan faaliyet grubu seç listesinden seçilir.

**Faaliyet Grubu Kodu:** Faaliyet Grubu Kodu bilgisi tanımlanır.

**Faaliyet Grubu Tanımı:** Faaliyet Grubu Tanımı girilir.

**Sorumlu Kullanıcı Grupları:** Sorumlu Kullanıcı Gruplarının sistemde tanımlı olan kullanıcı grubu seç listesinden seçilebilir.

**Sorumlu Personel:** Faaliyet Grubu tanımlama ekranında sorumlu personel bilgisinin sistemde tanımlı olan personel seç listesinden seçilebilir.

**Otomatik Kod Şablonu**: Otomatik Kod Şablonu bilgisi tanımlanır.

**Otomatik Kod Sayacı:** Otomatik kod şablonunda belirlenen koda göre verilen risk kayıtlarının kodunun hangi değerden başlayacağı belirlenir.

**Durum:** Aktif veya pasif durum seçilir.

Bu sayfada (varsa) faaliyet grubunun bağlı olduğu faaliyet grubu, faaliyet grubu kodu ve tanımı bilgisi girilir. Eğer sadece belirli kullanıcı gruplarının bu faaliyetlerle işlem yapması gerekiyorsa sorumlu kullanıcı grupları alanından kullanıcı grupları seçilip eklenir. Aktif/ Pasif durumu belirlenir. ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0e8a956a-2a53-4c37-a53d-8c138b292d72) (Kaydet) butonuyla kaydedilerek faaliyet grubu kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload37e479bc-0ea9-4fb1-806a-345598ef802a)

### **6.2.2.Faaliyet Tanımlama**

**Menü Adı:** Sistem Altyapı Tanımları/ FMEA Risk Değerlendirme / Faaliyet Tanımlama

FMEA Risk Değerlendirme Modülünde analizi yapılan risklerin ait olduğu faaliyetlerin tanımlandığı menüdür. Entegre Yönetim Sistemi altında Faaliyet Tanımlama menüsü altında ilgili sayfa görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade4de5fcc-7fb5-421c-87f5-db1bd036772a)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6a14dc29-eedc-4eca-bee5-12a74c81bc15): Yeni bir Faaliyet tanımlanabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfa7c6075-89e6-4f8d-a070-8fdfd456b2eb): Listede seçili Faaliyet bilgisi güncellenebilir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8253f73f-696d-4930-9fc3-182c0fe0c002): Listede seçili Faaliyet bilgisi silmek için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8d71cf00-7a42-44b0-8cda-d41c04c308f0): Listede seçili Faaliyet bilgisi kopyalanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9ff6afe7-83e1-49d0-b6e2-cd6f0255ca33): Filtre ekranındaki kriterlere göre arama yapar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6a476f09-818a-4e91-9c60-d1b9699d2f9a):Veriler Excel’e aktarılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8e6af64c-6b3a-454b-b13f-b73905c8808c): Önceki ekrana geri dönülür.

Faaliyet tanımlama ekranına yeni bir faaliyet eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload65717e0f-0fde-4ce0-ac98-7c75591b3a73)(Yeni) butonu tıklanarak Faaliyet Tanımlama \\Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8b24c377-b05c-4ab2-b7b1-af5ae7b98ad1)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Faaliyet Grubu:** Faaliyet Grubu bilgisinin sistemde tanımlı olan faaliyet grubundan seçilir.

**Faaliyet Kodu:** Faaliyet Kodu bilgisi sistem tarafından otomatik olarak verilir.

**Sorumlu Kullanıcı Grupları:** Sorumlu Kullanıcı Gruplarının bilgisi sistemde tanımlı olan kullanıcı grubu listesinden seçilebilir.

**Sorumlu Personel:** Sorumlu Personel bilgisinin sistemde tanımlı olan personel listesinden seçilir.

**Durum:** Faaliyet durumu Aktif veya Pasif seçilir.

Açılan ekranda sırasıyla faaliyet grubunu, faaliyet kodunu eğer parametreden otomatik kod verme aktif edilmemişse kod bilgisi, faaliyet tanımını ve yine eğer sorumlu kullanıcı grupları kullanılacaksa bu alan doldurulduktan sonra, durum bilgisi seçilip ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade021bd1a-fea9-42b7-a51d-201ffee8883d) (Kaydet) butonu ile faaliyet tanımlama işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7a489e78-95f3-4b27-a8f8-f1782179a7ff)

### **6.2.3.Risk Değerlendirme Formu Tanımlama**

**Menü Adı:** Entegre Yönetim Sistemi/ FMEA Risk Değerlendirme/ Risk Değerlendirme Formu Tanımlama

FMEA Risk Değerlendirme Modülünde faaliyet ve faaliyet grupları da tanımlandıktan sonra yapılacak son aşama, risklerin yer alacağı formların (RDF) tanımlanmasıdır. RDF tanımlamadaki amaç, risk analizinin yapılacağı detay formların belirli kategoriler ( ünite, birim, faaliyet grubu, departman vb. ) altında sınıflandırmaktır. Bunun için Entegre Yönetim Sistemi başlığı altındaki FMEA Risk Değerlendirme Modülünün altında Risk Değerlendirme Formu menüsü açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload303ac3f7-79d1-4931-a170-28a8762c559b)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6a14dc29-eedc-4eca-bee5-12a74c81bc15): Yeni RDF (Risk Değerlendirme Formu) tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfa7c6075-89e6-4f8d-a070-8fdfd456b2eb): Listede seçili RDF bilgisi güncellenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8253f73f-696d-4930-9fc3-182c0fe0c002): Listede seçili RDF bilgisi silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8d71cf00-7a42-44b0-8cda-d41c04c308f0): Listede seçili RDF bilgisi kopyalanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9ff6afe7-83e1-49d0-b6e2-cd6f0255ca33): Filtre ekranındaki kriterlere göre arama yapar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3e4b5f5d-fa1d-42b9-a427-d6a00dabb089): RDF listesini Excel’e aktarır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6a9e466e-8601-485b-902c-1adc4b060cc1): Seçili RDF’nin detay bilgiler ekranını açar.

RDF Tanımlama ekranında FMEA Risk Değerlendirme Modülü için ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7fc2ff1b-45ab-4640-9401-e6654f50e13f) (Yeni) butonuyla yeni Risk Değerlendirme Formu tanımlaması gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7a39df89-59dd-4181-a426-1d97e24e9e0d) **Açılan ekranda ilgili alanlar tanımlanır:**

**RDF Kodu:** RDF kodu bilgisi sistem tarafından otomatik olarak verilir.

**RDF Tanımı:** RDF tanımı bilgisi girilir.

**PFMEA Ekibi:** PFMEA Ekibi bilgisi sistemde tanımlı olan kullanıcı gruplarından seçilebilir.

**Proses Sorumlusu:** Proses Sorumlusu bilgisi sistemde tanımlı olan personel listesinden seçilebilir.

**Otomatik Kod Şablonu:** Otomatik kod şablonu bilgisi tanımlanır. Bu alan, ilgili RDF içerisine risk kayıtları eklendiğinde bu kayıtların kodunun nasıl olacağını belirler.

**Otomatik Kod Sayacı:** Otomatik kod şablonunda belirlenen koda göre verilen risk kayıtlarının kodunun hangi değerden başlayacağı belirlenir.

Alan tanımlama menüsünde tanımlanıp, Fonksiyon Dizanyer menüsüne 3. numaralı Risk Değerlendirme Form Tanımlama fonksiyonun sayfalarıyla ilişkilendirilen alanlar formda görüntülenir. FMEA Risk Değerlendirme Modülü kapsamında görüntülenen bu alanların tanımlanması ve ilgili fonksiyonun sayfalarıyla ilişkilendirme işlemi Bimser Destek Ekibi tarafından ayrıca yapılmaktadır

RDF tanımlama ekranında formun kodunu eğer otomatik kod verilmemişse kullanıcı tarafından girilir, formun tanımı, PFMEA Ekibi sorumlu kullanıcı grupları listesinde seçilerek, alan tanımlama menüsünde tanımlanıp ilgili fonksiyonun sayfalarıyla ilişkilendirilen alanları bilgi girişleri yapılarak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade021bd1a-fea9-42b7-a51d-201ffee8883d) (Kaydet) butonu tıklanarak risk değerlendirme formu tanımlama işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddbec9cee-8e4e-4445-8dfd-46f154b3c323)

Bu şekilde bütün RDF’ler tanımlandıktan sonra, risk detayı eklenilecek RDF seçili iken sağ üstteki butonlardan ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc5ca297b-c577-47a3-bb14-d74b8013e83e) (Detaylar) butonu tıklanarak Risk Değerlendirme Formu Detayı (RDFD) ekranına gelinir.   
![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload107d1ee1-6ba2-4c9e-8835-bccef522331a)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6a14dc29-eedc-4eca-bee5-12a74c81bc15): Yeni bir RDFD tanımlanabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfa7c6075-89e6-4f8d-a070-8fdfd456b2eb): Listede seçili RDFD bilgisi güncellenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7df43df6-44ea-4be0-9afd-04c5d8ac3bed): Listede seçili RDFD bilgisi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc770178d-c9e7-4d62-98a6-d10320ad10c5): Listede seçili olan RDFD bilgisi kopyalanabilir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8253f73f-696d-4930-9fc3-182c0fe0c002): Listede seçili olan RDFD bilgisini silmek için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc1bb840e-c094-4e38-8762-8a921da0b25f): Listede seçili olan RDFD bilgisi revize edilerek onaya gönderilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd1a13dfb-956a-488f-8259-b75e2d911c01): Listede seçili RDFD bilgisinin eski revizyonları izlenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade33d9132-e49c-4c7a-8651-49d1d17ba177) : Arama fonksiyonu kullanılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6a476f09-818a-4e91-9c60-d1b9699d2f9a): Seçili form detayları Excel’ e aktarılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc058da32-3b88-4bc1-a340-17995f2870ba): Revizyon Değişimi gösterir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbae833f2-7cf8-4bbb-8f4b-22b5764d3ec0): Bir önceki ekrana dönmek için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2c26dc65-d1ae-4dcb-8cbd-19eeb3e144bb): Grafik çizmek için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7fc2ff1b-45ab-4640-9401-e6654f50e13f)(Yeni) butonuyla Risk Değerlendirme Formu- Detaylar ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload31131c6f-475a-44b8-aa70-dfca541d213d) ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7bd9cd19-7f6f-46e1-acff-2cb06b589098)

Risk Değerlendirme Formu-Detaylar ekranında alan tanımlama menüsünde tanımlanıp, fonksiyon Dizanyer menüsünde FMEA Risk Değerlendirme Modülün 4. numaralı Risk Değerlendirme Detayı fonksiyonun sayfaları ile ilişkilendirilen alanlar görüntülenir. FMEA Risk Değerlendirme Modülü kapsamında görüntülenen bu alanların tanımlanması ve ilgili fonksiyonun sayfalarıyla ilişkilendirme işlemi Bimser Destek Ekibi tarafından ayrıca yapılmaktadır. Risk değerlendirme sekmesinde risk analizi için gerekli olan temel bilgiler ve kullanıcı tanımlı alanlar doldurulur. Riskler için önlemler alındıktan ve gerçekleştirildikten sonra revize işleminin de yapılmasıyla risk seviyesi düşürülmektedir. Önlemler sekmesinde ise bulunan risk değerinin azaltılması için alınacak önlemler planlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload40ab9fc2-96d4-4f90-b78c-6c9ed65d8ff4)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6a14dc29-eedc-4eca-bee5-12a74c81bc15): Yeni bir Önlem tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfa7c6075-89e6-4f8d-a070-8fdfd456b2eb): Listede seçili Önlem bilgisi güncellenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8253f73f-696d-4930-9fc3-182c0fe0c002): Listede seçili önlem bilgisi silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload48b566a5-d287-4812-aa32-379946f97b98): Listede seçili Önlem bilgisi görüntülenir.

Önlemler sekmesine gelindiğinde ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7fc2ff1b-45ab-4640-9401-e6654f50e13f) (yeni) butonuyla yeni önlem girişi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbbfff301-efec-41d5-89d0-48d294dbab05)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Referans Tipi:** Referans Tipi bilgisi DÖF, aksiyon, doküman, ve diğer seçeneklerinden seçilebildiği alandır. Referans tipi listeden seç seçeneği seçilirse referans tipi bilgisi listeden seçilir. Referans tipi yeni oluştur seçeneği seçilirse referans tipi bilgisi yeni oluşturulur.

**Referans Bilgisi:** Referans tipi DÖF, Aksiyon ve doküman olarak seçildiğinde ilgili referans kayıt seçilir.

**Önlem Tipi:** Mevcut veya planlanan olarak seçilir.

**Önlem Tarihi:** Önlem Tarihi bilgisi seçilir.

**Açıklama:** Açıklama bilgisi tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload12a4bc1d-984b-41b5-adee-0599c882c2f7)

Referans tipi olarak DÖF ve aksiyon seçilirse, QDMS’teki DÖF ve aksiyon modülleri ile bağlantı kurulacaktır. Mevcut açılmış DÖF ve aksiyonlardan herhangi biri önlemle ilişkilendirilebileceği gibi, yeni kayıtta açılabilir. Referans tipi olarak doküman seçilirse, QDMS’teki doküman ağacından doküman seçilir.Örneğin önlem türü olarak aksiyon seçilir, listeden seç ve yeni oluştur seçeneklerinden yeni oluştur seçeneği seçilerek Aksiyon oluşturulursa aşağıdaki şekilde aksiyon modülü ile bağlantı kurulur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2d892fb1-6429-4a1d-beb7-c393974ec89f)

Ek Dosyalar Sekmesi Aksiyon ile ilgili bir ek dosya varsa sisteme eklendiği sekmedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3d429d41-288e-4e70-883e-810520ea574f)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0c548a4b-de17-4962-9c68-e791cdcb4016): Ek dosya sisteme yüklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload84e81496-cb71-41fd-9509-6cc9abc1b947): Yüklenen ek dosya bilgisi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddf0b35c2-9b5f-4422-80c4-19e61b1cadbd): Yüklenen ek dosya bilgisi silinir.

Yönlendirme Tarihçesi sekmesi Yönlendirme tarihçesi bilgisinin verildiği sekmedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload758ac281-2273-45ff-a7d0-bece7ecde124)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1c1ce32b-0149-4936-b3c2-959fc7a59e24) (Kaydet) butonu tıklanarak Aksiyon gerçekleştirme işlemi için ilgili kullanıcıya gönderilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1af5cfad-4822-44e7-9165-dbe2bd4aca6b)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade410c9ae-98f0-48d7-b702-9b6b23016b85)

Önlemler sekmesinde Önlem olarak bir Aksiyon tanımlaması yapılır. FMEA sekmesinde gerekli alanlar bilgisi girilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcdbee46e-7e73-4c7a-b8ba-2ec7f178dc8d)(Kontrol Planına Gönder) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6e2ee373-7184-41a9-a053-8473116eb828)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8a5bb9e2-9381-4507-98c1-388438781002)

Risk Değerlendirme Form detayı yeni statü Kontrol Planı Statüsünde görüntülenir. Onaydaki kişinin bekleyen işlerinde **“Onay Bekleyen FMEA Risk Değerlendirme Detay Formları**” olarak bekleyen işlere iş düşer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload348a9279-d874-497f-9a46-dc89c0f19555)

Form kodu tıklanarak Risk Değerledirme Formu-Detay ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb1a9ff2d-bfe6-4674-b08e-afd0bcb43ff9)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload157a2e59-d7d9-4672-b86c-b990062c36b3):FMEA Risk Değerlendirme Form detayı ret edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc21a29ff-7b4f-4074-acdf-869c02a3ca47):FMEA Risk Değerlendirme Form Detayı yayınlanarak tamamlandı stasüne geçer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2c830a89-d19a-4353-b377-d555ca99bf30):FMEA Risk Değerlendirme Form Detayın Aksiyonu Bekleme Al statüsüne geçer.

Açılan ekranda Kontrol Planı sekmesindeki tıklanarak bu ekrandaki tanımlanmış alanları bilgisi girilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4c7eea3c-9531-44fc-908f-41eb761eb586)

İstenirse bu aşamada Önlem alınır. Daha önceki aşamadaki alınan önlem olarak Aksiyonlar görüntülenir

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7c3d4937-4dfb-4af3-9357-8cc399fc97e9)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload08f4fcd4-e0f4-461a-9f82-aa3b506bc6c7) Yayınla butonu tıklanara Risk Değerlendirme Form Detayı yayınlanarak statüsü tamamlandı aşamasına gelir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload14f973c3-2963-4bda-8a3f-2e836b92d645)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada424a830-fecf-4855-9129-6223f4ec4de4)

**Revizyon İşlemi:** RDFD’ler kaydedildikten sonra herhangi bir anda revizyon işlemine tabi tutulabilir ve yeni risk analizleri gerçekleştirilebilir. Bunun için RDFD listesi açıkken ilgili risk detayı seçilir ve sağ üstteki butonlardan ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3a861c14-16c4-4675-83a4-8b0c48019105) (Revizyon) butonu tıklanır. Bundan sonraki aşama risk detayını ilk kez doldururken izlenen adımlarla birebir aynıdır. Tek fark, RDFD ekranındayken revizyon numarası otomatik olarak bir artacaktır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada3a96977-56e5-4177-b093-fc6b7f5e2986)

İlgili RDFD’nin eski revizyonlarını görüntülemek için, listede seçili durumdayken ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadafc9c5fb-f68b-448f-974b-624e3d8d25e3) (Eski Revizyonlar) butonuna basılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3eb65559-55bf-42b1-86ec-db2d42b8883f)

Açılan yeni ekranda eski revizyonlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade99deccf-4a63-4211-af89-af0619e0a83e)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9244fd22-9d56-4afb-97c4-60f56ebfb123):Eski Revizyonları görüntüler.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb16af0e0-2acd-429e-be34-798b5b83b69a):Veriler Excel’ e aktarılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc4e19b4c-a2eb-4d3a-b2c4-c07ac9d9147c):Önceki ekrana geri dönülür.

Bir eski revizyon bilgilerini görüntülemek içinse listede seçim yaptıktan sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload77cdcde6-f1dd-48b1-b692-d5b2bb016073) (görüntüle) butonuyla bilgiler görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb4dce26b-9b56-47ac-871d-d07e38d3fd80)

RDFD ekranındaki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload63b97cf2-fbf4-437a-a95c-ff9b126185bf) (grafik çiz) butonu yardımıyla ise revizyonlar bazında risk durum grafiği çizdirilebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb46ed917-3a24-45fc-9ee7-dbf8d231e41b)

Açılan ekranda sol tarafta seçim yapılacak ve grafikte gösterilecek “Alanlar” bulunur. Alanlar kısmından ilgili seçimler yapıldıktan sonra ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload63b97cf2-fbf4-437a-a95c-ff9b126185bf) (Grafik Çiz) butonuna basılarak grafiğin çizdirilmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade2fbea8d-77b1-4e6c-b4fb-3017c53013ac)

### **6.2.4.Raporlar**

**Menü Adı:** Entegre Yönetim Sistemi / FMEA Risk Değerlendirme /Raporlar

FMEA Risk Değerlendirme Modülü ile ilgili raporlar görüntülendiği kısımdır.

#### **6.2.4.1.Aksiyon Raporu**

**Menü Adı:** Entegre Yönetim Sistemi / FMEA Risk Değerlendirme /Raporlar/Aksiyon Raporu

FMEA Risk Değerlendirme Modülünde önlemleri sonucu alınan aksiyonların listelendiği rapordur. Bu rapor Excel’e aktarılabilir. Özet rapor ve ayrıca zaman bazlı aksiyon çizelge raou çekilebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload92df2680-5f15-448f-ba08-156ed406a9e5)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb16af0e0-2acd-429e-be34-798b5b83b69a): Veriler Excel’ e aktarılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload68bf1c2d-2df1-4c54-b41d-031cb27da4fe): Kayıtlar filtrelenerek arama yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4bdababd-618c-4f92-84a9-b3a6871ee47f):Özet Rapor alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb07e32aa-cb50-4e6c-9218-efb77a240443):Log görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade844caa4-1b88-44ab-b3f6-478020adf80d):Aksiyon çizelge raporunu görüntüler.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload406771d0-160f-4a22-ad70-6c66ac05a9a8) Excel aktar butonuna basılırsa sistem listedeki Aksiyon Raporunu Excel formatında oluşturup kullanıcıya sunmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8537f3a1-38d9-4d97-986f-994ad4fbedda)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4bdababd-618c-4f92-84a9-b3a6871ee47f) Özet Rapor butonu tıklanarak Aksiyon Özet Rapor görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcb100f2a-795c-4354-91ad-1c8405e1eeee)

#### **6.2.4.2.Genel Risk Listesi**

**Menü Adı:** Entegre Yönetim Sistemi/FMEA Risk Değerlendirme /Raporlar/ Genel Risk Listesi

Kayıtlardaki tüm risk detaylarının görülebildiği listedir. Açılan pencerede RDFD’lerin listesi görüntülenmektedir. Genel Risk Listesi raporunu almak için, Raporlar menüsünden Genel Risk Listesi açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0938daa0-2c44-41a4-8f5d-3dbfd3eeb814)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb16af0e0-2acd-429e-be34-798b5b83b69a): Veriler Excel’ e aktarılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload68bf1c2d-2df1-4c54-b41d-031cb27da4fe): Kayıtlar filtrelenerek arama yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload406771d0-160f-4a22-ad70-6c66ac05a9a8) Excel aktar butonuna basılırsa sistem listedeki RDFD’lerin Genel Risk Listesini Excel formatında oluşturup kullanıcıya sunmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf504bd80-1203-4960-97ce-2525a6ef52a2)

#### **6.2.4.3.Faaliyet Tarihçesi**

**Menü Adı:** Entegre Yönetim Sistemi/FMEA Risk Değerlendirme/Raporlar/ Faaliyet Tarihçesi

FMEA Risk Değerlendirme Modülünde kapsamında sistemde tanımlı Faaliyetlerin tarihçe bilgisinin görüntülendiği rapordur. Alınan raporda Faaliyet kodu, Faaliyet Tanımı ve Faaliyet Grubu Tanımı gibi alanların bilgileri görüntülenir. İstenirse Filtre sekmesinden alanlara göre filtreleme işlemi de gerçekleştirilebilir.Faaliyetler Tarihçesi raporunu almak için, Raporlar menüsünden Faaliyetler Tarihçesi açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3ea6cab2-38f3-4968-8a5c-1dee1e942a79)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload406771d0-160f-4a22-ad70-6c66ac05a9a8) Excel’e aktar butonuna basılırsa, sistem otomatik olarak Faaliyetler Tarihçesi raporunu oluşturup kullanıcıya Excel formatında sunmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5ebdf28c-164a-4e33-9c1c-69915c901ff5)

#### **6.2.4.4.Faaliyet Grubu Tarihçesi**

**Menü Adı:** Entegre Yönetim Sistemi/FMEA Risk Değerlendirme/Raporlar/ Faaliyet Grubu Tarihçesi

FMEA Risk Değerlendirme Modülünde kapsamında sistemde tanımlı Faaliyet gruplarının tarihçe bilgisinin görüntülendiği rapordur. Alınan raporda Faaliyet Grubu kodu, Faaliyet Grubu Tanımı ve Üst Faaliyet Grubu Tanımı gibi alanların bilgileri görüntülenir. İstenirse Filtre sekmesinden alanlara göre filtreleme işlemi de gerçekleştirilebilir. Faaliyetler Grubu Tarihçesi raporunu almak için, Raporlar menüsünden Faaliyetler Grubu Tarihçesi açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfb29dc81-79d7-4cf7-aca6-8df7c60ac118)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb16af0e0-2acd-429e-be34-798b5b83b69a): Veriler Excel’ e aktarılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload406771d0-160f-4a22-ad70-6c66ac05a9a8) Excel aktar butonuna basılırsa sistem listedeki RDFD’lerin Faaliyet Grubu Tarihçesini Excel formatında oluşturup kullanıcıya sunmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf7aa909f-943d-4e00-97d5-9f61bafabb95)

#### **6.2.4.5.Faaliyet Raporu**

**Menü Adı:** Entegre Yönetim Sistemi/ FMEA Risk Değerlendirme /Raporlar/ Faaliyet Raporu

FMEA Risk Değerlendirme Modülü kapsamında sistemde tanımlı Faaliyetlerin görüntülendiği rapordur. Alınan raporda Faaliye Kodu, Faaliyet Tanımı ve Faaliyet Grubu gibi alanların bilgileri görüntülenir. İstenirse Filtre sekmesinden alanlara göre filtreleme işlemi de gerçekleştirilebilir. Faaliyetler Raporunu almak için, Raporlar menüsünden Faaliyetler Raporu menüsü açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1d1bb3c0-d107-43d6-b485-023c6f61e819)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb16af0e0-2acd-429e-be34-798b5b83b69a): Veriler Excel’ e aktarılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload68bf1c2d-2df1-4c54-b41d-031cb27da4fe): Kayıtlar filtrelenerek arama yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload406771d0-160f-4a22-ad70-6c66ac05a9a8) Excel aktar butonuna basılırsa sistem listedeki RDFD’lerin Faaliyet Raporunu Excel formatında oluşturup kullanıcıya sunmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1eb4f6e4-0983-49fc-9dfd-e729cc4a79d6)

#### **6.2.4.6. Tekrar Eden Kayıtlar Raporu**

**Menü Adı:** **Menü Adı**: Entegre Yönetim Sistemi/ FMEA Risk Değerlendirme /Raporlar/ Tekrar Eden Kayıtlar Raporu

Benzer risk kayıtlarının kaç kez tekrar ettiğini gösteren rapordur. Entegre Yönetim Sistemi/ FMEA Risk Değerlendirme /Raporlar/Tekrar Eden Kayıtlar raporundan ilgili rapor şablonu seçilir.Tekrar Eden Raporu ekranında Rapor Şablonu seçilir. Rapor Şablonun tanımlaması Sistem Altyapı Tanımları/ FMEA Risk Değerlendirme/ Tekrar Eden Kayıtlar Raporu Şablonu menüsünden tanımlanır. Filtre sekmesinde Rapor Şablonu seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb439497f-9861-41b5-bdf3-0abbfaefd66f)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload68bf1c2d-2df1-4c54-b41d-031cb27da4fe) (Ara) butonu tıklanarak liste sekmesinde kayıtlar listenilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload19830805-bc09-48bc-93e7-1d481e40cd32)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb16af0e0-2acd-429e-be34-798b5b83b69a) (Excel aktar) botunu ile “Tekrar Eden Kayıtlar Raporu” Excel formatın görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload018d9d8c-b6b0-42ab-b6bb-16776872f573)

#### **6.2.4.7. Risklerin Bölgelere Dağılımı**

**Menü Adı**: Entegre Yönetim Sistemi / FMEA Risk Değerlendirme /Raporlar/Risklerin Bölgelere Dağılımı

FMEA Risk Değerlendirme Modülü kapsamında iş yeri ve departman bazlı risklerin haritada gösterilmesinin sağlandığı rapordur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload567091db-b827-49ea-958a-883d820ddcd8)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload68bf1c2d-2df1-4c54-b41d-031cb27da4fe): Kayıtlar filtrelenerek arama yapılabilir.

İlgili İşyeri listesi veya Departman listesinde seçim yapılarak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload68bf1c2d-2df1-4c54-b41d-031cb27da4fe)(ara) butonu tıklanarak Harita sekmesinde işyeri ve departman bazlı risklerin harita üzerinde görüntülenmesi sağlanır.

### **6.2.5.Grafikler**

**Menü Adı:** Entegre Yönetim Sistemi/FMEA Risk Değerlendirme/ Grafikler

FMEA Risk Değerlendirme Modülü ile ilgili grafiklerin görüntülendiği kısımdır.

#### **6.2.5.1.Risk Revizyon Karşılaştırma Grafiği**

**Menü Adı:** Entegre Yönetim Sistemi/FMEA Risk Değerlendirme/ Grafikler/ Risk Revizyon Karşılaştırma Grafiği

Risk Revizyon Karşılaştırma Grafiğini almak için, Grafikler menüsünden Risk Revizyon Karşılaştırma Grafiği menüsü tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade476f1a4-0bfd-4f9b-b979-e1a95404f219)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4bdababd-618c-4f92-84a9-b3a6871ee47f): Belirlenen özelliklere göre ekrana grafiği çizdirir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload85969d34-a9ab-4068-a511-bf2404c978f0) : İstenen grafiği açılır menüden seçilen format türüne (Excel, JPG, PDF vb. ) dönüştürerek dış ortama aktarır.

Açılan ekranda filtre sekmesinden grafik karşılaştırmasını almak istediğimiz alanları doldurarak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9f877c0f-a06f-4600-8e2b-b6b291e5f45c) (grafik çiz) butonu ile istenile risk revizyon karşılaştırması yapılır. Güncel öncesi revizyon sayısı ve X ekseni seçilerek grafik çiz butonu ile grafik oluşturulur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb3da8bae-6210-4d6f-8dc1-50dc4c4ff4aa)

#### **6.2.5.2.En Çoklar Analizi**

**Menü Adı:** Entegre Yönetim Sistemi/FMEA Risk Değerlendirme / Grafikler/ En Çoklar Analizi

En Çoklar Analizi grafiğini almak için, Grafikler menüsünden En Çoklar Analizi menüsü tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload584ebf9d-7f41-40c8-b0d8-bbde9a7b2509)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4bdababd-618c-4f92-84a9-b3a6871ee47f): Belirlenen özelliklere göre ekrana grafiği çizdirir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload85969d34-a9ab-4068-a511-bf2404c978f0): İstenen grafiği açılır menüden seçilen format türüne (Excel, JPG, PDF vb. ) dönüştürerek dış ortama aktarır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4ff9b450-2e89-4513-8ced-86ed17bfbf2c): Grafik verileri, Excel listesi biçiminde aktarılır.

En Çoklar Analizi ekranında, Grafik Seçenekleri bölümünde gerekli seçimler gerçekleştirilir. Grafikte olması istenen en çok aralık belirlenir. Grafik Seçeneklerinden X ekseninde yer alması istenen nitelik seçilir. Ana tema, renk paleti özelliklerinden grafik özelleştirilebilir. Grafik başlığı belirtilerek grafik oluşturmak için ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4bdababd-618c-4f92-84a9-b3a6871ee47f) (grafik çiz) butonuna tıklanır. Eğer istenirse birçok kritere göre filtreleme yapılabilir ve sadece bu özellikteki RDFD’lerin grafikte yer alması sağlanabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload771498e9-ceb1-4f5c-a465-ae75882501e7)

#### **6.2.5.3.Risk Dağılım Matrisi**

**Menü Adı:** Entegre Yönetim Sistemi/FMEA Risk Değerlendirme/ Grafikler/ Risk Dağılım Matrisi

Risk Dağılım Matrisini almak için, Grafikler menüsünden Risk Dağılım Matrisi menüsü tıklanır. Hangi aralıkta kaç tane risk olduğunu gösteren 2 boyutlu bir grafik oluşturur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload017e171a-15f2-480d-a89e-cd8a41939fd4)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb16af0e0-2acd-429e-be34-798b5b83b69a): Veriler Excel’ e aktarılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload68bf1c2d-2df1-4c54-b41d-031cb27da4fe): Kayıtlar filtrelenerek arama yapılabilir

Açılan ekranda grafik türü seçilir ve ara butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9336118f-cfff-4f6b-aa93-81dfa5a14eaf)

#### **6.2.5.4.Risk Karşılaştırma Grafiği**

**Menü Adı:** Entegre Yönetim Sistemi FMEA Risk Değerlendirme / Grafikler/ Risk Karşılaştırma Grafiği

Risk Karşılaştırma Grafiğini almak için, Grafikler menüsünden Risk Karşılaştırma Grafiği sekmesi tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9e644155-140a-4273-9384-5a40dfb89c0d)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4bdababd-618c-4f92-84a9-b3a6871ee47f): Belirlenen özelliklere göre ekrana grafiği çizdirir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload85969d34-a9ab-4068-a511-bf2404c978f0): İstenen grafiği açılır menüden seçilen format türüne (excel, jpg, pdf, vb. ) dönüştürerek dış ortama aktarır.

Açılan ekranda filtre sekmesinden grafik karşılaştırmasını almak istediğimiz alanları doldurarak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9f877c0f-a06f-4600-8e2b-b6b291e5f45c) (Grafik Çiz) butonu ile istenilen risk karşılaştırması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload48fa91b2-095b-4fb7-b333-26571148250d)

### **6.2.6.Risk Değerlendirme Talebi**

**Menü Adı:** Entegre Yönetim Sistemi/ FMEA Risk Değerlendirme /Risk Değerlendirme Talebi

FMEA Risk Değerlendirme modülü kapsamında Risk Değerlendirme Talebi işleminin gerçekleştiği menüdür. Bu menü kullanılarak herhangi bir personele risk değerlendirme görevi aksiyon olarak açılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4ecb59b9-7662-4e01-9604-f19add745483)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload171f9c5a-5770-4d5a-8d78-f511a12c26df):Yeni bir risk değerlendirme talebi tanımlar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb7a06685-f44d-415a-a3be-9d8205d407f9): Listede seçili Risk değerlendirme talebini görüntüler.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb16af0e0-2acd-429e-be34-798b5b83b69a): Veriler Excel’ e aktarılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload68bf1c2d-2df1-4c54-b41d-031cb27da4fe): Kayıtlar filtrelenerek arama yapılabilir

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload171f9c5a-5770-4d5a-8d78-f511a12c26df)Yeni butonu tıklanarak Risk Değerlendirme Talebi Tanımlama ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload73e9e3b2-67c8-44ea-b267-924364e0707f)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Değerlendirecek Kişi:** Risk Değerlendirme Talebi Tanımlama ekranında Değerlendirecek Kişi bilgisinin sistemde tanımlı olan Personel Listesinden seçilebildiği alandır.

**Talep Açıklama:** Risk Değerlendirme Talebi Tanımlama ekranında Talep Açıklama bilgisinin girildiği alandır.

Risk Değerlendirme Talebi ile ilgili eklenecek Ek Dosya varsa eklendiği sekmedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc108998e-62e3-44d9-a1bb-3e6945b94371)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0c548a4b-de17-4962-9c68-e791cdcb4016): Ek dosya sisteme yüklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload84e81496-cb71-41fd-9509-6cc9abc1b947): Yüklenen ek dosya bilgisi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddf0b35c2-9b5f-4422-80c4-19e61b1cadbd): Yüklenen ek dosya bilgisi silinir.

Açılan pencerede Risk Talebi ekranında değerlendirecek kişi ve talebin açıklaması girildikten sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb1d2d419-afb0-4db1-bea1-7fa872e9e82a) (Kaydet) butonuyla talep kaydedilir ve ilgili kişiye aksiyon olarak açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3aca2567-fdc1-4dd9-a800-0840b05a6a60)

.
