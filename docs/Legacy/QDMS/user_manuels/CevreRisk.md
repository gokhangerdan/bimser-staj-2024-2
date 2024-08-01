---
title: Çevresel Boyutlar ve Etkileri
description: Çevresel Boyutlar ve Etkileri Yardım Dokümanı
sidebar_position: 24
---

:::tip Bilgi

İlgili konu başlığına sağ tarafta bulunan navigasyon yardımıyla hızlı bir şekilde ulaşabilirsiniz.

:::



**Çevresel Boyutlar ve Etkileri Modülü(v.5.24) Kullanıcı Yardım Dokümanı**

Modül Versiyonu: 5.24



**1.GİRİŞ:** Çevresel Risk Değerlendirme Modülün amacı; firmada yapılan her türlü faaliyette yapılacak işin özelliğine göre çevre üzerine olabilecek etkileri belirlemek ve bu etkilerin bertarafı veya etki derecesinin en aza indirilmesine yönelik gerekli önlemleri alabilmek amacıyla yapılacak çalışmalara ait gerekli düzenlemeleri oluşturmaktır.

**2.AMAÇ:** Bu yardım kılavuzunun amacı, QDMS kullanan kuruluşların Çevresel Boyutlar ve Etkileri Modülünün implementasyonu sırasında ve sonrasında risk formları ile bu risklerle ilgili alınacak önlemlerin planlanması aşamasında izleyeceği yolu belirlemektir.

**3.SORUMLULUKLAR:** Yönetim Sistemleri Temsilcisi, Çevre Görevlisi, İşyeri Temsilcisi.

**4.KISALTMALAR:**

RDF: Risk Değerlendirme Formu

RDFD: Risk Değerlendirme Form Detayı

**5.İŞ AKIŞI:**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc8f770a6-b35a-4112-aa4c-b658dd1ab2ac)


# **6. Çevresel Boyutlar ve Etkileri Modülü**

Kullanılmakta olan Çevresel Boyutlar ve Etkileri metodolojisinin dijital ortamda takibini sağlama, risk analiz tarihçesini oluşturma ve izleme, risk değerlendirme sonucunda önlemleri belirleme ve takip etme, mevcut risk formlarının sisteme aktarımı, risk formları üzerinde yetki kontrolünü sağlama ile yetkisiz erişimi engellemeyi sağlayan risk değerlendirme modülüdür.

## **6.1.Sistem Altyapı Tanımları/ Çevresel Boyutlar ve Etkileri**

Çevresel Boyutlar ve Etkileri Modülünün altyapısını oluşturmak amacıyla gerekli tanımlamaların yapıldığı kısımdır. Yapılan tanımlamalara göre Entegre Yönetim Sistemi menüsünden girişlerde bu veriler kullanılmakta ve görülmektedir.

### **6.1.1.Alan Tanımlama**

**Menü adı:** Sistem Altyapı Tanımları/ Çevresel Boyutlar ve Etkileri /Alan Tanımlama

Çevre Boyutlar ve Etkileri modülünde ilişki kurulacak fonksiyonlarda (Risk Değerlendirmeleri, Faaliyet Grubu Tanımlama, Faaliyet Tanımlama vb.) kullanılacak alanların tanımlandığı menüdür. Burada oluşturulan alanlar, alan havuzuna eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload847b1af2-eed2-4d32-a88f-51a3c941b790)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2fdedcaf-a969-4ff7-b18f-2607dbf1c16e): Yeni bir alan eklenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4946f959-e0c3-49e0-a5e5-3aaeb69c023d):Var olan alanda değişiklik yapılmak istenirse kullanılır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5fe337f8-9048-4ce4-8bc4-e8bbe14f903b):İlgili alanı silmek için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade39e1f16-51bd-4aac-b998-dc1be1f5998a): Alanın değerleri tanımlanır.

Listeye yeni bir alan eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbd79c684-4a84-4cf8-89f8-71f4017d4c98) (Yeni) butonu tıklanarak Alan Tanımlama\\Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload665bfb7a-bead-4991-b3ef-a9be8ea63a27) ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf7ef2fb5-385b-44ea-ad65-33f02f797f2a)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Alan Kodu:** Alan kodu bilgisi tanımlanır. Daha önce tanımlamış alanlarla aynı olmayacak şekilde boşluk, Türkçe karakter gibi karakterler kullanmadan tanımlanmalıdır. Ör. ‘001’ , ‘RK’

**Alan Adı:** Alan adı bilgisi tanımlanır.

**Başlık Notu:** Alanın başlık notu bilgisi tanımlanır.

**Giriş Tipi:** Oluşturulan alanda kullanıcı tarafından veri girişi/seçim mi yapacağı ya da hesaplama yöntemi ile otomatik olarak sistem tarafından mı atanacağı belirlenir.

**Alan Tipi**: Oluşturulan alanın metin, numerik, tarih, liste vb. alan tiplerinden hangisi olacağı belirlenir.

**Görünme Şartı:** Tanımlama işlemi devam eden alanın daha önceden tanımlanan başka bir alanın değerine göre görünüp görünmeyeceği belirlenir. Kullanımı [ALANKODU]=ALAN_DEĞERİ vb. şekildedir.

**Durum:** Alan durumu aktif veya pasif olarak seçilir.

**Termin Alanı:** Termin alanı aktif edilecekse ilgili kutucuk işaretlenir. Aksiyon ve DF’ lerin terminleri buradaki süre göz önüne alınarak belirlenir.

**Güncellemeden değer yükselmesin:** Güncellemeden değer yükselmesin bilgisi aktif edilecekse ilgili kutucuk işaretlenir. Bu bilginin işaretli olduğu alanlarda puan değeri güncelleme sırasında mevcut değerden daha yüksek olarak girilemez.

**İlişkili Alan:** İlişkili alan özelliği ile seçenek tipli iki alan arasında ilişki kurulabilmektedir. Referans alanın elemanlarının tanımlandığı ekranda ilişkili alandan hangi değerler ile ilişkili olduğu seçilebilmektedir. Böylece referans alanın form üzerinde değeri değiştiğinde ilişkili alan seçimli olarak otomatik dolabilmekte ya da seçim ekranından sadece ilişkilendirilen değerler arasından seçim yapılabilmektedir.

**İlişkili Alan Otomatik Doldurulsun:** ilişkili alan otomatik doldurulsun seçeneği aktif edilecekse ilgili kutucuk işaretlenir. Liste tipli iki alanın değerleri arasında kurulan ilişkiye göre alanlardan birinin otomatik doldurulmasını sağlar.

**Genişlik:** Alanın kolon genişliği bilgisi tanımlanır.

Alan tanımlama ekranında gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload085770ed-f820-4bdc-af64-4abcc83076fa) (Kaydet) butonu tıklanarak kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5aa87dc0-1353-427b-aa02-68a2c23f7975)

Örnek olarak Frekans alanının tanımlanması için alan kodu, alan adı yazılmalı, giriş tipi veri girişi, alan tipi puanlı liste, durumu aktif olarak seçilmelidir. Şiddet gibi diğer alanların tanımlanması da bu menüde gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload21e508bf-29cd-46e7-8984-901060fde545)

Frekans alanına değer eklemek için olasılık alanı seçili iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload830d2649-b925-4708-9956-730cf0135718) (Değerler) butonuna tıklanarak alanın değerlerinin tanıtılacağı ekrana gelinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadea3478e9-4b6d-43d4-9a6d-ef1ab9209a00)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload666c14be-47ec-4955-ab1c-8edc06c99129):Yeni bir değer tanımlanır

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload21e3b106-85a8-4463-b56d-bc38a0e73d27): Değer ile ilgili herhangi bir düzeltme veya güncelleme yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0754f53d-e88d-4451-a0cb-5c0006350824): Değer silinebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb530ab95-66c5-4f0c-b45e-571d533e128b): Kayıtlar filtrelenerek arama yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0f4e18db-835a-4b26-a650-842b230eaa03) : Veriler Excel’ e aktarılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1e1d5ee5-6a4a-447b-b4a9-255c7be84d7a): Şablon indirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7a1595cb-0a39-4258-b1db-c83f2941b0d0): Şablon yüklenilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc8e8e50c-4d47-48d7-a515-89f168a12b24) (Yeni) butonuna tıklanarak yeni değer tanımlama işlemine başlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload138dacbb-9d20-4135-bf56-e8a71108d98f) ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddeb91a89-1073-43ca-a545-4588bb2bce1b)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Tanım:** Tanım bilgisi girilir.

**Açıklama:** Açıklama bilgisi yazılır.

**Değer:** Değerin puan karşılığı girilir.

**Durum:** Değerin durumu aktif veya pasif olarak seçilir.

**Varsayılan:** İlgili liste değerinin varsayılan olarak alanda görünmesini sağlar.

**Önlem zorunlu mu?:** Bu değer seçili olduğunda önlemler sekmesinden en az bir önlem girilmesi zorunlu olur.

Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload085770ed-f820-4bdc-af64-4abcc83076fa) (Kaydet) butonu tıklanarak değer tanımlama işlemi gerçekleştirilir. Olasılık, şiddet, frekans vb. puanlı liste, liste, arama özellikli liste tipli alanların değer tanımlama işlemleri bu şekilde yapılır. Alan özelliklerine göre bu ekranda değişiklikler olabilmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload302e9d5d-752f-4ce8-bd7f-9eaf111a56b0)

Olasılık Alanın değerleri tanımlama işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload374689d5-1b93-4630-b409-8d3a997ce799)

Şiddet Alanın değerleri tanımlama işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1e42da11-4627-4583-a199-59582cadd44b)

Kişi Sayısı alanının değerleri tanımlama işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0f30d31f-f7f8-430d-a5c2-3414ed9250b3)

Alanların değerlerinin tanımlanma işlemi gerçekleştikten sonra risk değeri gibi veri giriş tipi hesaplanan olan alanların formül girişleri yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada94dd4b1-4757-49d7-89bd-4dc49401ecdc) ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd2625918-b9c6-4d28-acad-53d92d32ac26)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload65fd7a12-279b-4775-b50e-b3e74cb5b23c)

Formül girişleri ilgili alanların tanımlama ekranlarında gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbfbf8705-d184-49ff-9bb4-6aca3afcb510) ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3affe66e-46af-4bd4-baa1-1d9849cc754f)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9402ff6e-099a-49bf-b6aa-5346f6dff4f4)

Risk Seviyesi alanının değerleri tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaeda0eb4-40fd-4ee9-b53c-f27297c280d6)![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5472b2a4-7cb4-4c2c-b6ad-9bb73354e396)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade01cab19-4601-420d-992c-ff19776b31f2)

Risk seviyesinin değerleri tanımlama işleminden sonra formül girişi yapılır. ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf27c5097-f4e6-4151-b39e-b67ed560e715) (Değiştir) butonu tıklanarak formül girişi yapılarak kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb92db35d-205f-4b5d-96df-b9d751b86503) ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2644c751-b6ba-4fe3-ba15-66fa5a259c89)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc440e161-c198-42a6-8057-ef242d90defc)

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

### **6.1.2.Fonksiyon Dizayner**

**Menü Adı:** Sistem Altyapı Tanımları/ Çevresel Boyutlar ve Etkileri / Fonksiyon Dizayner

Fonksiyon Dizayner özelliği ile alan havuzuna eklenen alanlar Çevresel Boyutlar ve Etkileri Değerlendirme modülünün ilgili fonksiyonları ile ilişkilendirilebilir. Bunun için Sistem Altyapı Tanımları / Çevresel Boyutlar ve Etkileri Risk Değerlendirme modülünün altından Fonksiyon Dizayner menüsüne gelinir. Açılan ekranda bu modülün alan eklenebilecek fonksiyonları sıralanacaktır. Kaynak Grubu Tanımlama, Kaynak Tanımlama, risk değerlendirme form tanımlama, Risk Değerlendirme Detay, Önlem Tanımlama ve Kontrol Tanımlama fonksiyonlarında kullanılacak alanlar ve bunların sıralaması ile onay işlemlerindeki hiyerarşi detayı tanımlanır. Bu menüde kullanılacak butonlar Çevresel Boyutları ve Etkileri modülü parametrelerinden “Statü kullanılsın mı?” (22. Parametre) parametresine bağlı olarak değişir. Bu parametre değeri “Evet” ise aşağıda bulunan butonların tamamı gözükür; ancak parametre değeri “Hayır” olduğu durumlarda sadece “Alanlar” butonu görünür durumda olur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd7c9d2e7-572b-4361-b262-bc993f202572)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0da8bd19-5d00-4298-9391-2f26eb60d392): Statü tanımlamak için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade716a006-d9a5-4c06-be9e-640acc94db8d): Butonlar tanımlamak için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc14548c4-5eff-476a-b610-ef6fbd11dc88): Formların detaylarında kullanılacak Alanlar belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd1a9bf90-e5eb-45b4-a2c5-01b5e61761d8)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2fdedcaf-a969-4ff7-b18f-2607dbf1c16e): Yeni Fonksiyon eklenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4946f959-e0c3-49e0-a5e5-3aaeb69c023d): Listede seçili Fonksiyon bilgisi değiştirilir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5fe337f8-9048-4ce4-8bc4-e8bbe14f903b): Listede seçili Fonksiyon bilgisi silinebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload89291549-321d-4682-92b1-30205e5cf488): Önceki ekrana geri dönülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf6fb519e-1551-497d-95f9-741457f9e4ec)(Alanlar) butonu ile açılan ekranda seçili fonksiyonda kullanılacak alanlar ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbd79c684-4a84-4cf8-89f8-71f4017d4c98)(Yeni) butonuna tıklanarak belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9560aa4a-5f3e-4f84-9e62-dc4c494e2511) ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5b59c9bb-75c2-4e92-b813-1648084c4f92)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Alan Adı:** Alan tanımlama ekranında tanımlanmış alanlardan alan seçimi yapılır.

**Zorunlu Mu? :** Alanın zorunlu olup olmadığı seçilir.

**Zorunluluk Mesajı:** Zorunlu alan doldurulmadığında verilecek uyarı mesajı bilgisi bu alana yazılır.

**Sıra No:** Alanın sıra no belirlenir.

**Varsayılan Rol:** İlgili alanın değeri daha önce tanımlanmış bir üst formdan ya da kaydı giren kişinin adı soyadı, pozisyonu, unvanı, departmanı, iş yeri gibi verileri ise bunlar için tanımlanmış rol seçilebilir.

**Varsayılan Değer Değiştirilmesin:** Seçilen alan varsayılan olarak bir değer getiriyorsa getirdiği değerin değiştirmemesini sağlar.

**Gridde göster:** Alanın gridde gösterilmesi gerekiyorsa ilgili kutucuk işaretlenir.

**Seçimde göster:** Alanın seçimde gösterilmesi gerekiyorsa ilgili kutucuk işaretlenir.

**Satır Sayısı:** İlgili alan çoklu satır ise, veri girişi ekranında kaç satır gözükmesi gerektiği belirlenir.

**Kolon Genişliği:** İlgili modülde girilen kayıtların listesinde (gridde) alanın kolon genişliği bilgisinin belirlenir. Verinin uzun olduğu alanlar için ort. 250, sadece rakam girilen alanlar için ise 75 kullanılması idealdir. Alana girilecek veriler düşünülerek bu aralıklarda bir değer kullanmak uygun olacaktır.

**Aktif Statü:** Alanın sisteme tanımlanan statülerin hangilerinde aktif olacağını belirler. Bu alanda işaretlenen statülerde ilgili alanın tipine göre işlem gerçekleştirilebilir.

**Görünür Statü:** Alanın sisteme tanımlanan statülerin hangilerinde görüleceğini belirler. Aktif statüsü seçilen alanlar için aynı zamanda görünür statüde en az aktif statü alanında işaretlenen statüler olacak şekilde belirlenmelidir.

**Zorunlu Statü:** **:** Alanın sisteme tanımlanan statülerin hangilerinde zorunlu olacağını belirler.

Açılan ekranda alan bilgileri listeden seçilir, zorunlu bir alan ise kullanıcının bu alanı doldurmadığında çıkacak mesaj tanımlanır, sıra numarası belirlenir. Aktif statü, Görünür Statü ve Zorunlu Statü durumları seçilir. Zorunlu olup olmadığı, gridde gösterilip gösterilmeyeceği, kolon genişliği belirlenerek gerekli tüm alanlar doldurulduktan sonra ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6c2e095a-8568-4def-aee5-e7c5278bdb0e) (Kaydet) butonu tıklanarak, ilgili alan için fonksiyon ile ilişkilendirme işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload05566cbb-bc63-4717-9806-842d48e1dad1)

### **6.1.3.Risk Dağılım Matrisi Tanımlama**

**Menü Adı:** Sistem Altyapı Tanımları/ Çevresel Boyutlar ve Etkileri / Risk Dağılım Matrisi Tanımlama

Risk Dağılım Matrisi tanımlama işleminin gerçekleştiği menüdür. Risk Dağılım Matrisi tanımlamadaki amaç, belirlenen parametrelere göre risk dağılımın hangi aralıklarda daha yoğun olduğunu tespit etmektir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddbefad1e-d510-4729-ab7c-29f2dd5a1ba4)

**Ekranındaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2fdedcaf-a969-4ff7-b18f-2607dbf1c16e): Yeni bir Risk Dağılım Matrisi tanımlar.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4946f959-e0c3-49e0-a5e5-3aaeb69c023d): Listede seçili Risk Dağılım Matrisi bilgisi günceller.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5fe337f8-9048-4ce4-8bc4-e8bbe14f903b): Listede seçili Risk Dağılım Matrisi bilgisi silinebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload598db1e1-285c-493c-83e7-205e4d65b9aa): Risk dağılım matrisini renklendirir.

Listeye yeni bir Risk Dağılım Matrisi eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbd79c684-4a84-4cf8-89f8-71f4017d4c98) yeni butonu tıklanarak Risk Dağılım Matrisi Tanımlama\\Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8b458f64-7cb1-4626-8df4-7b91665b3b7f) ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade5d7d0e2-98ae-4357-a3b8-0eaefb34ce9b)

Açılan ekranda “Grafik Adı” belirlenir. X ve Y eksenindeki parametreler için risk karşılaştırmasında kullanılacak alanlar belirlenir. Bu alanların alan tanımlama menüsündeki formülleri “X Formülü” ve “Y Formülü” kısımlarına yazılır. “X Aralıkları” ve “Y Aralıkları” kısımlarına ise alanların değerleri girilir. İşlemler tamamlandıktan sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload085770ed-f820-4bdc-af64-4abcc83076fa) (kaydet) butonu tıklanarak kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1c037e7d-53bd-4bea-a5fe-ed69786780bd)

Risk Dağılım Matrisini kullanılan yönteme uygun olarak renklendirmek için risk dağılım matrisi tanımlama ekranındaki sağ üst köşede bulunan ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload69858e28-df76-4eda-9aed-258b8ebd2b4f) (Renklendir) butonuyla oluşturulan matris açılır. Ekrandaki her kutucuğun üzerine tıklanarak kutucuklar renklendirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload08b9a383-3984-4c4f-8d71-c7a5a4a9ddfe)

### **6.1.4.Onay Akışı Tanımlama**

Değerlendirilen risklerin belirlenen kullanıcılara onaya gitmesi için sistemde onay akışı kurgulanması gereklidir. Modülde statü kullanımı aktifleştirilerek onay akış kurgusu gerçekleştirilir. Bunun için Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Parametreler menüsüne gelinir. Filtreden Çevresel Boyutlar ve Etkileri Modülü seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload618ab114-0432-4bb2-8648-5c5951c61e2b)

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4946f959-e0c3-49e0-a5e5-3aaeb69c023d)(Değiştir) butonu tıklanarak 22 numaralı parametre olan “Statü kullanılacak mı?” değeri “Evet” olarak değiştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload81b30514-972a-4135-9b20-97a5983e17fc)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc1cbb917-6f5c-46e3-9b0e-d02bb0f8bf1b)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload433d1616-237c-4d7e-868e-34f73859fb09)

**NOT:** Akış tanımları Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Akış tanımlama ekranından kontrol edilmeli yoksa akışları tanımlanmalıdır. Ayrıca Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Rol Tanımlama ekranından da onay akışları için rol tanımlamaları yapılır![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3cbabcf8-d0c5-402d-ad29-126d7ea78c4d)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfd30a301-dd45-4dcc-93e5-bf67c2fefa94)

Sistem Altyapı Tanımları/ BSAT/ Tanımlar/ Mesaj Gövdesi Tanımlama ekranından modül için yeni mesaj gövdesi tanımlamaları yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload169a7514-4f2b-414e-bade-2ea760b47bd7)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload03b4cec4-58c1-473e-a4ba-1f7c85e0d26e)

Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Akış Tanımlama ekranından akış tanımlamaları yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade837e1e4-0794-432f-8839-80fef997eaa1)

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2fdedcaf-a969-4ff7-b18f-2607dbf1c16e)(Yeni) butonu tıklanarak Akış Tanımlama\\Yeni Kayıt ekranı görüntülenir. Ya da var olan bir akışın güncellenmesi gerekiyorsa ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4946f959-e0c3-49e0-a5e5-3aaeb69c023d) (Değiştir) butonu tıklanarak Akış Tanımlama-Kayıt Güncelleme ekranı açılır. ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada9758a25-4576-4e62-935e-cd6396db7eba) (Ekle) butonu ile sistemde tanımlı rollerden yeni bir rol eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb7943eb9-954f-4c7e-b64e-1086e8babfaa)

Fonksiyon Dizayner menüsüne gelinir. Statü ve Butonlar adında iki farklı işlem butonu Risk Değerlendirme Form Tanımlama ve Risk Değerlendirme Detay fonksiyonları için menüye gelecektir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload78a16459-57f4-4637-9a42-73733bc90fc3)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0da8bd19-5d00-4298-9391-2f26eb60d392): Statü tanımlamak için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4d7de49d-831e-484e-85b3-099ecef368ce): Butonlar tanımlamak için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade2051398-770a-40b7-9f38-58f82ae085e2) : Alanlar tanımlanır.

Fonksiyon Dizayner menüsünden ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0da8bd19-5d00-4298-9391-2f26eb60d392) (Statüler) butonu ile statüler tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9f734f47-8d23-403c-be82-32527bf973fd)

**Ekranındaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2fdedcaf-a969-4ff7-b18f-2607dbf1c16e): Yeni bir statü tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4946f959-e0c3-49e0-a5e5-3aaeb69c023d): Listede seçili statü bilgisi güncellenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5fe337f8-9048-4ce4-8bc4-e8bbe14f903b): Listede seçili statü bilgisi silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadca394bfa-f850-43d1-bcde-8e7c803e9378): Önceki ekrana geri dönülür.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2fdedcaf-a969-4ff7-b18f-2607dbf1c16e) (Yeni) butonu ile yeni statü tanımlama ekranına gelinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0ef4a2fc-4a15-43f6-a8f7-2e9c73330653)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6f2a469d-e8a8-44f0-b1b3-86395fed7594)

Açılan ekranda statü kodu, statü adı, akışın başlatılıp başlatılmayacağı, yeni statü, durum, akış tanımı, onay talep mesajı, onay tamam mesajı ve onay ret mesajı girişleri yapılarak kaydedilir.

Fonksiyon Dizayner ‘dan ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4d7de49d-831e-484e-85b3-099ecef368ce) (Butonlar) butonu ile statülerde kullanılacak butonlar tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb51a714-2498-43d1-8766-3b086d56e652)

**Ekranındaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2fdedcaf-a969-4ff7-b18f-2607dbf1c16e): Yeni bir buton tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4946f959-e0c3-49e0-a5e5-3aaeb69c023d): Listede seçili buton bilgisi güncellenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5fe337f8-9048-4ce4-8bc4-e8bbe14f903b): Listede seçili buton bilgisi silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadca394bfa-f850-43d1-bcde-8e7c803e9378): Önceki ekrana geri dönülür.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2fdedcaf-a969-4ff7-b18f-2607dbf1c16e)(Yeni) butonu ile yeni buton tanımlama ekranına gelinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload147daf5d-a023-4cc1-8fa9-10fe0fbed620)

Açılan ekranda Buton Kodu, Buton Adı belirlenir. Buton tipi ve Resmi belirlenir. Görünür Statüsü, Yeni Statü ve Durumu seçilir. Gerekli alanlar doldurulduktan sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbb087c40-4a59-427e-b158-13065a7140d9)(Kaydet) butonuyla kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4aa7373f-14fe-49bb-b382-b3ee18b84a3a)

Risk değerlendirme detay fonksiyonu için statü ve buton tanımlama işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6ac6f707-963b-46a6-afab-2eb8f9897ffb)

Risk değerlendirme detay fonksiyonu için statüler tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload90ba5c41-6bab-4c80-8a16-7444ede06f25)

Risk değerlendirme detay fonksiyonu için butonlar tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3f15a5e9-b1e7-4e9a-9a44-e4f7a8598403)

### **6.1.5.Alan Menüsü Tanımlama**

**Menü Adı:** Sistem Altyapı Tanımları/ Çevresel Boyutlar ve Etkileri / Alan Menüsü Tanımlama

Liste tipli alanlara değer eklenmesi için Entegre Yönetim Sistemi altında menü oluşturulmasını sağlayan menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload78f7584c-c367-4fc6-88c5-354ce0b09ba3)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2fdedcaf-a969-4ff7-b18f-2607dbf1c16e): Yeni menü tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4946f959-e0c3-49e0-a5e5-3aaeb69c023d): Listede seçili menü bilgisi güncellenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5fe337f8-9048-4ce4-8bc4-e8bbe14f903b): Listede seçili menü bilgisi silinir.

Listeye yeni bir Menü eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbd79c684-4a84-4cf8-89f8-71f4017d4c98) (Yeni) butonu tıklanarak Menü Tanımlama\\ Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf147beab-08c9-40ae-9dc7-4247d5df5350)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Açılan ekranda ilgili alanlar tanımlanır:**

**Menü Adı:** Menü adı bilgisi tanımlanır.

**Alan:** Alan bilgisi seçilir.

**Sıra No:** Sıra no bilgisi girilir.

Menü tanımlama ekranında gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload085770ed-f820-4bdc-af64-4abcc83076fa) (Kaydet) butonu tıklanarak menü tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8f07113c-eb57-4864-8496-7c9117443b24)

Menü tanımlaması yapıldıktan sonra Çevresel Boyutlar ve Etkileri Modülün Entegre Yönetim Sistemi kısmında menü olarak görüntülenmesi için SAT/BSAT/Tanımlar/Yetki Grupları Tanımlama menüsünde menü görme yetkisi verilmelidir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload95fb8871-15b5-4d04-bd96-085c0cde63d2)

Tanımlanan menünün Yetki Grupları Tanımlama menüsünde menü görme yetkisi verildikten sonra Çevresel Boyutlar ve Etkileri Modülün Entegre Yönetim Sistemi kısmında menü olarak görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8588421b-2e28-420f-a604-8d8906820593)

### **6.1.6.E-Posta Ayarları**

**Menü Adı:** Sistem Altyapı Tanımları/ Çevresel Boyutlar ve Etkileri / E-Posta Ayarları

Çevresel Boyutlar ve Etkileri modülünden oluşturulacak maillerin kime ve hangi mesaj gövdesiyle gönderileceğinin ayarlandığı menüdür.

Bildirim ayarı yapılacak değerin üzerine gelinip ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9eb951d2-09a3-4207-86a7-544cea75cb1b) (Değiştir) butonu tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb94fd700-e84a-4962-ab8b-229b4d8d25e7)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9eb951d2-09a3-4207-86a7-544cea75cb1b) (Değiştir) butonu ile değerin içine girildikten sonra rollere göre uygun mesaj gövdesi seçilir ve e-posta gitsin mi kutucuğu işaretlenerek kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload58566e04-3fbc-49a8-b645-ce3a9a054a68)

### **6.1.7.Çevresel Boyutlar ve Etkileri Parametreleri**

**Menü Adı:** Sistem Altyapı Tanımları/ Çevresel Boyutlar ve Etkileri / Çevresel Boyutlar Parametreleri

Çevresel Boyutlar ve Etkileri Modülünün kullanıcının istek ve ihtiyaçlarına göre sistemsel ayarlarının yapıldığı ve bunlara göre parametreleri belirlendiği menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3a8fc964-b3f5-4440-93c1-9508d65e5382)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4946f959-e0c3-49e0-a5e5-3aaeb69c023d): Listede seçili parametre değiştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb530ab95-66c5-4f0c-b45e-571d533e128b): Kayıtlar filtrelenerek arama yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0f4e18db-835a-4b26-a650-842b230eaa03): Veriler Excel’ e aktarılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3700f6ec-36e6-45ac-b298-f380adb041a1)

### **6.1.8.Rapor Formatları**

**Menü Adı:** Sistem Altyapı Tanımları/ Çevresel Boyutlar ve Etkileri / Rapor Formatları

Çevresel Boyutlar ve Etkileri metotlarına göre farklı rapor formatları oluşturmak için Rapor Formatları menüsü kullanılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload089b0ee3-eafd-4b26-a0fc-5bd7fc49ae03)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2fdedcaf-a969-4ff7-b18f-2607dbf1c16e):Yeni bir Rapor Formatı tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4946f959-e0c3-49e0-a5e5-3aaeb69c023d): Listede seçili Rapor Formatı bilgisi güncellenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5fe337f8-9048-4ce4-8bc4-e8bbe14f903b): Listede seçili Rapor Formatı bilgisi silinebilir.

Bunun için öncelikle SAT/BSAT/Konfigürasyon Ayarları/Rapor Formatları Düzenleme menüsüne oluşturacağımız rapor formatlarının tümü tanımlanmalıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc0a76e12-0135-4294-bd0b-12491613449e)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload666c14be-47ec-4955-ab1c-8edc06c99129):Sisteme yeni bir Rapor formatı yüklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8bdc86d5-9bf5-468c-83df-8b41249a7935):Listede seçili Rapor Formatı görüntülenip, indirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0754f53d-e88d-4451-a0cb-5c0006350824):Listede seçili Rapor Formatı silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload666c14be-47ec-4955-ab1c-8edc06c99129)(Yeni) butonu tıklanarak sisteme Rapor Formatı yükleme işlemine başlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadad0cc491-6e23-4e7b-93fe-8704675d2278)

Açılan menüde ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbd79c684-4a84-4cf8-89f8-71f4017d4c98) (Yeni) butonuna tıklanarak Rapor Formatı eklemesi yapılır ve Rapor Formatının adı uzantısıyla beraber kopyalanır. Ardından SAT/ Çevresel Boyutlar ve Etkileri /Rapor Formatları menüsü açılır.

Listeye yeni bir Rapor formatı eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbd79c684-4a84-4cf8-89f8-71f4017d4c98) (Yeni) butonu tıklanarak Rapor formatı \\Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4d2f5196-b52f-4289-9ca9-1e136644f6a3)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Rapor Tanımı:** Rapor tanımı bilgisinin girilir.

**Rapor Şablonu:** rapor şablonun adı ve uzantısı bilgisi girilir.

**Rapor Tipi:** Kayıt bazında, form bazında ve genel olmak üzere üç seçenek rapor tipi bilgisi seçilebilir.

-   **Kayıt Bazında:** Her bir risk kaydının ayrı olarak raporlanması talep edildiğinde seçilir. (EYS/Çevresel Boyutlar ve Etkileri /Risk Değerlendirme Formu tanımlama menüsünde Detaylar butonuna basıldıktan sonra çıkan “PDF” butonuyla alınır. Kayıt bazında tanımlama olmadığı sürece PDF butonu görüntülenmez.)
-   **Form Bazında:** Her risk formu altındaki risk detay kayıtlarının tek bir liste halinde Excel’e aktarıldığı durumlar için seçilir.

    (EYS/ Çevresel Boyutlar ve Etkileri /Risk Değerlendirme Formu Tanımlama menüsünde Detaylar butonuna basıldıktan sonra çıkan “Excel” butonuyla alınır.)

-   **Genel:** Tüm risk detay kayıtlarının tek bir Excel’de görülmesi talep edildiği durumda seçilir.

(EYS/ Çevresel Boyutlar ve Etkileri /Raporlar/Genel Risk Listesi Rapor ekranından alınır.)

**PDF olarak oluştur:** Rapor tipi kayıt bazında seçilen rapor formatlarında Entegre Yönetim Sistemi/ Çevresel Boyutlar ve Etkileri /Risk Değerlendirme Formu Tanımlama/Risk Değerlendirme Form Detayı ekranında seçilen bir risk kaydının PDF olarak aktarılabilmesi için bu kutucuk işaretlenebilir.

Açılan ekranda tanıtılacak rapor formatlarının isimleri Rapor Tanımı alanına yazılır. Rapor Şablonu alanına ise rapor formatları düzenleme menüsünden kopyalanan dosya adı **uzantısıyla birlikte** yapıştırılır.

Rapor Tanımlama ekranında gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload085770ed-f820-4bdc-af64-4abcc83076fa) (Kaydet) butonu tıklanarak Rapor Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade6d1d64e-a807-4f26-a861-550cf9326843)

### **6.1.9.Kontroller**

#### **6.1.9.1.Kontrol Tanımlama**

**Menü Adı**: Sistem Altyapı Tanımları/ Çevresel Boyutlar ve Etkileri / Kontroller/ Kontrol Tanımlama

Kontroller QDMS'te Risk Modüllerinde kullanılır. Kontroller 27001 EK A maddesinde geçen maddelerdir ve önlemler sekmesinde gelmektedir. Önlemler sekmesinde her bir risk için kontrol adımı seçebilebilir.Önlemler sekmesinde, seçtiğiniz kontrol maddeleri, QDMS ortamında raporlar başlığında SOA raporu almak istediğinizde karşınıza çıkacaktır.Kısaca Kontroller SOA raporunun hazırlanmasında kullanılmaktadır. 95 nolu parametre evet ise kontroller risk yeni kayıt ekranında sekme olarak karşımıza çıkar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5f7e9f46-d2be-41c0-ab5e-ffa6c0240a2b)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2fdedcaf-a969-4ff7-b18f-2607dbf1c16e): Yeni bir Kontrol tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4946f959-e0c3-49e0-a5e5-3aaeb69c023d): Listede seçili Kontrol bilgisi güncellenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5fe337f8-9048-4ce4-8bc4-e8bbe14f903b): Listede seçili Kontrol bilgisi silinebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0f4e18db-835a-4b26-a650-842b230eaa03): Veriler Excel’ e aktarılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb530ab95-66c5-4f0c-b45e-571d533e128b): Kayıtlar filtrelenerek arama yapılabilir.

Kontrol Tanımlama ekranına yeni bir Kontrol eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbd79c684-4a84-4cf8-89f8-71f4017d4c98)(yeni) butonu tıklanarak Kontrol Tanımlama\\Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade30b5ab2-4bf6-4f1a-81a1-5839b9679f03)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Kontrol Kodu:** Kontrol Tanımlama ekranında Kontrol Kodu bilgisinin girildiği alandır.

**Bağlı Olduğu Kontrol:** Oluşturulma aşamasında olan Üst Kontrol Kodu, bir kontrol kodu tanımının alt kırılımı olması halinde bu alan otomatik dolu gelir. Dolu olarak gelen alanda bağlı olduğu kontrol kodu tanımının adı yazar. Bağlı olduğu üst kırılım silinmek istenildiğinde sağ yanda bulunan ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade6ee934c-b509-45f1-a8a5-ac7aa835469c) (sil) butonu veya değiştirilmek istenildiğinde sağ yanda bulunan ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9ef1116b-94e3-45a4-8bb1-6a6eca2bf827) (seç) butonu kullanılır. Bağlı olduğu bir üst kontrol yok ise bu alan boş gelir.

**Kontrol Tanımı:** Kontrol Tanımlama ekranında Kontrol Tanım bilgisinin girildiği alandır.

**Açıklama:** Kontrol Tanımlama ekranında Açıklama bilgisinin girildiği alandır.

**Durum:** Kontrol Tanımlama ekranında Aktif ve Pasif durum bilgisinin seçilebildiği alandır.

Kontrol Tanımlama ekranında gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload085770ed-f820-4bdc-af64-4abcc83076fa) (Kaydet) butonu tıklanarak Kontrol Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload51d2a4f9-ce95-4705-a7d6-ae7f7c9cfef8)

### **6.1.10. Tekrar Eden Kayıtlar Raporu Şablonu**

**Menü Adı**: Sistem Altyapı Tanımları/ Çevresel Boyutlar ve Etkileri / Tekrar Eden Kayıtlar Raporu Şablonu

Sistemde bir kullanıcı için istenen konularda tekrar eden kayıtları gösteren menüdür. İlk olarak Sistem Altyapı Tanımları/ Çevresel Boyutlar ve Etkileri /Tekrar Eden Kayıtlar Raporu Şablonu menüsünden raporda çekilecek alanlar seçilir.

Daha sonra Entegre Yönetim Sistemi/ Çevresel Boyutlar ve Etkileri /Raporlar/Tekrar Eden Kayıtlar raporundan ilgili rapora ulaşılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload794b30c5-6850-4aa2-9510-691533fcc6a5)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload666c14be-47ec-4955-ab1c-8edc06c99129): Yeni Tekrar Eden Kayıtlar Şablonu tanımlanır

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload21e3b106-85a8-4463-b56d-bc38a0e73d27): Listede seçili Tekrar Eden Kayıtlar Şablonu bilgisi güncellenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0754f53d-e88d-4451-a0cb-5c0006350824): Listede seçili Tekrar Eden Kayıtlar Şablonu bilgisi silinebilir.

Tekrar Eden Kayıtlar Raporu Şablonları ekranına yeni bir Tekrar Eden Kayıtlar Raporu Şablonları eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbd79c684-4a84-4cf8-89f8-71f4017d4c98)(yeni) butonu tıklanarak Tekrar Eden Kayıtlar Raporu Şablonları \\Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3f6de387-7215-4522-a502-1e9917021355)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Tanım:** Tekrar Eden Kayıtlar Raporu Şablonları ekranında Tekrar Eden Kayıtlar Raporu Şablonları tanım bilgisinin girildiği alandır.

**Kolanlar:** Tekrar Eden Kayıtlar Raporu Şablonları ekranında Kolanlar bilgisinin seçilebildiği alandır.

Açılan ekranda Tekrar Eden Kayıtlar Raporu tanım bilgisi girilir. İlgili Kolanlar seçilir. Tekrar Eden Kayıtlar Raporu Şablonları ekranında gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload085770ed-f820-4bdc-af64-4abcc83076fa) (kaydet) butonu tıklanarak Tekrar Eden Kayıtlar Raporu Şablonları kayıt işlemi gerçekleştirilir.

Entegre Yönetim Sistemi/ Çevresel Boyutlar ve Etkileri /Raporlar/Tekrar Eden Kayıtlar raporundan ilgili rapor şablonu seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb5f02f8c-34e8-488e-a336-f6a2de9f7c62)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb530ab95-66c5-4f0c-b45e-571d533e128b) Ara butonu ile kayıtlar filtrelenerek arama yapılabilir ve ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0f4e18db-835a-4b26-a650-842b230eaa03)( Excel aktar) botunu ile veriler Excel’ e aktarılabilir.

## **6.2.Entegre Yönetim Sistemi/ Çevresel Boyutlar ve Etkileri**

Çevresel Boyutlar ve Etkileri Modülü kapsamında Faaliyet Grupları, Faaliyet, Risk Formu, Risk Form Detaylarının tanımlandığı, Raporların ve Grafiklerin görüntülendiği kısımdır.

### **6.2.1.Faaliyet Grubu Tanımlama**

**Menü Adı:** Entegre Yönetim Sistemi/ Çevresel Boyutlar ve Etkileri / Faaliyet Grubu Tanımlama

Risk Modülünde risk kaynağı, eğer sistemde tanımlı olan risk kaynaklarından kullanılacaksa 23.parametre olan “risk kaynağı kullanılacak mı?” parametresinin aktif olması gerekir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbcf2015f-df16-4da7-b9b3-76c2e8bd3f51) Bu parametre aktif hale getirildikten sonra Faaliyet Grubu Tanımlama ve Faaliyet Tanımlama işlemleri gerçekleştirilir. Faaliyetlerin tanımlanması için öncelikle bu faaliyetlerin bağlı bulunacağı grupların tanımlanması gerekir. Bunun için Çevresel Boyutlar ve Etkileri Modülünün Entegre Yönetim Sistemi başlığı altına gelinerek Faaliyet Grubu Tanımlama menüsüne tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb8c3ec9d-36dd-4620-95d6-7c2078b0bfe9)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada83bcc04-0add-4ce8-9bc2-81ac54972e73): Yeni bir Faaliyet Grubu tanımlanabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc8804aaa-4d9d-4a97-8df6-73b5d13cd6d9): Listede seçili Faaliyet Grubu bilgisi güncellenebilir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5fe337f8-9048-4ce4-8bc4-e8bbe14f903b): Listede seçili Faaliyet Grubu bilgisini silmek için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb0cddce8-9f34-4244-9a20-c958a094ebde): Faaliyet grupları Excel’ e aktarılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload59282110-7ea6-40c0-82b0-cb0fc2f7820a): Şablon yüklemek için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload153a1fd1-cc6e-49c9-8a9b-21bd8b27bf62): Şablon oluşturmak için kullanılır.

Faaliyet Grubu Tanımlama ekranına yeni bir Faaliyet Grubu eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbd79c684-4a84-4cf8-89f8-71f4017d4c98)(Yeni) butonu tıklanarak Faaliyet Grubu Tanımlama \\Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbbd74118-f4f3-469e-b328-16a922fead1d)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Bağlı Olduğu Faaliyet Grubu:** Bağlı olunan faaliyet grubu bilgisi sistemde tanımlı olan faaliyet grubu seç listesinden seçilir.

**Faaliyet Grubu Kodu:** Faaliyet Grubu Kodu bilgisi tanımlanır.

**Faaliyet Grubu Tanımı:** Faaliyet Grubu Tanımı girilir.

**Sorumlu Kullanıcı Grupları:** Sorumlu Kullanıcı Gruplarının sistemde tanımlı olan kullanıcı grubu seç listesinden seçilebilir.

**Sorumlu Personel:** Faaliyet Grubu tanımlama ekranında sorumlu personel bilgisinin sistemde tanımlı olan personel seç listesinden seçilebilir.

**Otomatik Kod Şablonu**: Otomatik Kod Şablonu bilgisi tanımlanır.

**Otomatik Kod Sayacı:** Otomatik kod şablonunda belirlenen koda göre verilen risk kayıtlarının kodunun hangi değerden başlayacağı belirlenir.

**Durum:** Aktif veya pasif durum seçilir.

Bu sayfada (varsa) faaliyet grubunun bağlı olduğu faaliyet grubu, faaliyet grubu kodu ve tanımı bilgisi girilir. Eğer sadece belirli kullanıcı gruplarının bu faaliyetlerle işlem yapması gerekiyorsa sorumlu kullanıcı grupları alanından kullanıcı grupları seçilip eklenir. Aktif/ Pasif durumu belirlenir. ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbb087c40-4a59-427e-b158-13065a7140d9) (Kaydet) butonuyla kaydedilerek faaliyet grubu kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2f5b3fc3-8e3c-4809-9074-40ab9b9731a2)

### **6.2.2.Faaliyet Tanımlama**

**Menü Adı:** Sistem Altyapı Tanımları/ Çevresel Boyutlar ve Etkileri / Faaliyet Tanımlama

Çevresel Boyutlar ve Etkileri Modülünde analizi yapılan risklerin ait olduğu faaliyetlerin tanımlandığı menüdür. Entegre Yönetim Sistemi altında Faaliyet Tanımlama menüsü altında ilgili sayfa görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload73b4f6a6-1b1a-4361-9a59-f9a017cd040e)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada83bcc04-0add-4ce8-9bc2-81ac54972e73): Yeni bir Faaliyet tanımlanabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc8804aaa-4d9d-4a97-8df6-73b5d13cd6d9): Listede seçili Faaliyet bilgisi güncellenebilir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5fe337f8-9048-4ce4-8bc4-e8bbe14f903b): Listede seçili Faaliyet bilgisi silmek için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade7d64b7f-384f-4b69-80d1-dbfae4efcd32): Listede seçili Faaliyet bilgisi kopyalanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload169c663c-8c6c-456c-ad31-b60200b9037e): Filtre ekranındaki kriterlere göre arama yapar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb0cddce8-9f34-4244-9a20-c958a094ebde):Veriler Excel’e aktarılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload52d7e224-5c56-41ec-b54f-9840b90054c7): Önceki ekrana geri dönülür.

Faaliyet tanımlama ekranına yeni bir faaliyet eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbd79c684-4a84-4cf8-89f8-71f4017d4c98)(Yeni) butonu tıklanarak Faaliyet Tanımlama \\Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2c18bdc2-aed1-493f-a5a8-d5542e31cece)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Faaliyet Grubu:** Faaliyet Grubu bilgisinin sistemde tanımlı olan faaliyet grubundan seçilir.

**Faaliyet Kodu:** Faaliyet Kodu bilgisi sistem tarafından otomatik olarak verilir.

**Sorumlu Kullanıcı Grupları:** Sorumlu Kullanıcı Gruplarının bilgisi sistemde tanımlı olan kullanıcı grubu listesinden seçilebilir.

**Sorumlu Personel:** Sorumlu Personel bilgisinin sistemde tanımlı olan personel listesinden seçilir.

**Durum:** Faaliyet durumu Aktif veya Pasif seçilir.

Açılan ekranda sırasıyla faaliyet grubunu, faaliyet kodunu eğer parametreden otomatik kod verme aktif edilmemişse kod bilgisi, faaliyet tanımını ve yine eğer sorumlu kullanıcı grupları kullanılacaksa bu alan doldurulduktan sonra, durum bilgisi seçilip ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd732c3ed-7661-4004-8cde-e8571e73b5ce) (Kaydet) butonu ile faaliyet tanımlama işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf20179ae-0919-41e0-845f-004e4b129a39)

### **6.2.3.Risk Değerlendirme Formu Tanımlama**

**Menü Adı:** Entegre Yönetim Sistemi/ Çevresel Boyutlar ve Etkileri/ Risk Değerlendirme Formu Tanımlama

Çevresel Boyutlar ve Etkileri Modülünde faaliyet ve faaliyet grupları da tanımlandıktan sonra yapılacak son aşama, risklerin yer alacağı formların (RDF) tanımlanmasıdır. RDF tanımlamadaki amaç, risk analizinin yapılacağı detay formların belirli kategoriler ( ünite, birim, faaliyet grubu, departman vb. ) altında sınıflandırmaktır. Bunun için Entegre Yönetim Sistemi başlığı altındaki Çevresel Boyutlar ve Etkileri Modülünün altında Risk Değerlendirme Formu menüsü açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc5498452-0b86-4144-b8f3-a81a65a5a6a1)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada83bcc04-0add-4ce8-9bc2-81ac54972e73): Yeni RDF (Risk Değerlendirme Formu) tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc8804aaa-4d9d-4a97-8df6-73b5d13cd6d9): Listede seçili RDF bilgisi güncellenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5fe337f8-9048-4ce4-8bc4-e8bbe14f903b): Listede seçili RDF bilgisi silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade7d64b7f-384f-4b69-80d1-dbfae4efcd32): Listede seçili RDF bilgisi kopyalanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload169c663c-8c6c-456c-ad31-b60200b9037e): Filtre ekranındaki kriterlere göre arama yapar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload788773d6-2921-454e-8558-fdc876f54746): RDF listesini Excel’e aktarır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade327052e-273a-4686-b4c3-81d3737a8acb): Seçili RDF’nin detay bilgiler ekranını açar.

RDF Tanımlama ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6ff2cb88-f651-4902-8757-191ebbff342a) (Yeni) butonuyla yeni RDF tanımlaması gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3f149236-6916-45fa-a72c-fdc94af5cef0)

**Açılan ekranda ilgili alanlar tanımlanır:**

**RDF Kodu:** RDF kodu bilgisi sistem tarafından otomatik olarak verilir.

**RDF Tanımı:** RDF tanımı bilgisi girilir.

**Sorumlu Kullanıcı Grupları:** Sorumlu Kullanıcı Grupları bilgisi sistemde tanımlı olan kullanıcı gruplarından seçilebilir.

**Sorumlu Personeller:** Sorumlu Personeller bilgisi sistemde tanımlı olan personel listesinden seçilebilir.

**Otomatik Kod Şablonu:** Otomatik kod şablonu bilgisi tanımlanır. Bu alan, ilgili RDF içerisine risk kayıtları eklendiğinde bu kayıtların kodunun nasıl olacağını belirler.

**Otomatik Kod Sayacı:** Otomatik kod şablonunda belirlenen koda göre verilen risk kayıtlarının kodunun hangi değerden başlayacağı belirlenir.

RDF tanımlama ekranında formun kodunu eğer otomatik kod verilmemişse kullanıcı tarafından girilir, formun tanımı ve sorumlu kullanıcı grupları eklenerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd732c3ed-7661-4004-8cde-e8571e73b5ce) (Kaydet) butonu tıklanarak risk değerlendirme formu tanımlama işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload860a5f0f-1d87-4e60-837d-9f4199d2a4e3)

Bu şekilde bütün RDF’ler tanımlandıktan sonra, risk detayı eklenilecek RDF seçili iken sağ üstteki butonlardan ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3490d683-7402-4c77-a895-9cecc96fc893) (Detaylar) butonu tıklanarak Risk Değerlendirme Formu Detayı (RDFD) ekranına gelinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf2fdc42b-a698-44bc-8b7f-6ce2c3bf7a13)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada83bcc04-0add-4ce8-9bc2-81ac54972e73): Yeni bir RDFD tanımlanabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc8804aaa-4d9d-4a97-8df6-73b5d13cd6d9): Listede seçili RDFD bilgisi güncellenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9a2f2b29-750b-42d4-9b01-7750ce879056): Listede seçili RDFD bilgisi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload005f1f61-f0b1-4416-87bb-0ce4c3ff768b): Listede seçili olan RDFD bilgisi kopyalanabilir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5fe337f8-9048-4ce4-8bc4-e8bbe14f903b): Listede seçili olan RDFD bilgisini silmek için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d3b33eb-f953-4be3-8124-40d5d7bc23bf): Listede seçili olan RDFD bilgisi revize edilerek onaya gönderilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload26d55a68-c673-46eb-b915-cf1eec4df606): Listede seçili RDFD bilgisinin eski revizyonları izlenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaec3785f-076c-4b67-a149-7538d8fd71c4): Listede seçili RDFD bilgisi gözden geçirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0955d89e-fa34-4539-a482-8aa9162fa5fd): Listede seçili RDFD bilgisi için eski gözden geçirmeler izlenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6db1255c-eb75-40b9-b624-934a58af1a98) : Arama fonksiyonu kullanılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb0cddce8-9f34-4244-9a20-c958a094ebde): Seçili RDFD detayları Excel’ e aktarılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaa02ee0c-64ce-4390-8edc-a41bea23a10c): Revizyon Değişimi gösterir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4b7cd2c6-3439-4c99-9650-becea76f0c20): Bir önceki ekrana dönmek için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadea3baf6b-9cc2-4c42-bda7-013d8f0e71a8): Grafik çizmek için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload153a1fd1-cc6e-49c9-8a9b-21bd8b27bf62) : Şablon oluşturmak için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload59282110-7ea6-40c0-82b0-cb0fc2f7820a): Şablon yüklemek için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6ff2cb88-f651-4902-8757-191ebbff342a)(Yeni) butonuyla Risk Değerlendirme Formu/Detaylar ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4b243a05-b49f-4dc3-a10f-268d1e3ffa8f)

**Açılan ekranda ilgili alanlar tanımlanır:**

**RDF Tanımı:** RDF Tanımı bilgisi girilir.

**RDFD Kodu:** RDFD Kodu bilgisi sistem tarafından otomatik olarak verilir.

**Revizyon No:** Revizyon No bilgisi verilir.

**Revizyon Tarihi:** Revizyon Tarihi bilgisi verilir.

**Risk Kaynağı Tipi:** Faaliyet Grubu ve Faaliyet olarak Risk Kaynağı Tipi seçilebilir.

**Risk Kaynağı:** Risk Kaynağı bilgisinin faaliyet seç listesinden seçilir.

**Risk Kaynağı:** Risk Değerlendirme sekmesinde Risk Kaynağı bilgisinin sistemde tanımlı olan Faaliyet Listesinden seçilebildiği alandır.

**Not:** Risk Kaynağı tipi ve Risk Kaynağı alanları Çevresel Boyutlar ve Etkileri modülünün 23 numaralı “Risk Kaynağı Kullanılacak mı?” parametresine bağlı olarak sistemde görünür. Bu parametre değeri “Hayır” bu alanlar Risk Değerlendirme Form Detayı ekranında görünmeyecektir.

görünmeyecektir.

**Durum:** Durum bilgisi belirlenir.

**Frekans:** Frekans değeri seçilir. (Kullanıcı tanımlıdır. Alan tanımlama menüsünden tanımlanması gereklidir.)

**Olasılık:** Olasılık değeri seçilir. (Kullanıcı tanımlıdır. Alan tanımlama menüsünden tanımlanması gereklidir.)

**Şiddet:** Şiddet değeri seçilir. (Kullanıcı tanımlıdır. Alan tanımlama menüsünden tanımlanması gereklidir.)

**Kişi Sayısı:** Kişi Sayı belirlenir. (Kullanıcı tanımlıdır. Alan tanımlama menüsünden tanımlanması gereklidir.)

**Risk Puanı:** Sistem tarafından hesaplanarak bilgisi verilir. (Kullanıcı tanımlıdır. Alan tanımlama menüsünden tanımlanması gereklidir.)

**Risk Seviyesi:** Sistem tarafından hesaplanarak bilgisi verilir. (Kullanıcı tanımlıdır. Alan tanımlama menüsünden tanımlanması gereklidir.)

Risk değerlendirme sekmesinde risk analizi için gerekli olan temel bilgiler ve kullanıcı tanımlı alanlar doldurulur. Risk değerlendirme formu doldurulduktan sonra, firmaya ait olan risk değerlendirme metodolojisine göre risk seviyesinin belirlenen aralıkları için ana ekranda sarı, kırmızı, yeşil gibi renkli noktalar görülmektedir. Riskler için önlemler alındıktan ve gerçekleştirildikten sonra revize işleminin de yapılmasıyla risk seviyesi düşürülmekte, daha düşük seviyelerdeki risk aralıklarındaki renklere dönüşmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload70693ea7-a126-4a5e-96dc-620740c6ae4d)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload336d0b59-b2b8-4d4a-94b3-3870fa754f1e)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4f598b79-8d33-4661-831f-97c7e30bbda7)

Trend sütununda ise ilgili risk kaydının değerinin bir önceki revizyona göre artış, azalış ya da durağan bir trende mi sahip olduğu görülebilir. Bu ekranda görülen risk ve trend ifadeleri alan tanımlama işlemi gerçekleştirilirken hesaplanan giriş tipine sahip alanlarda belirlenebilir.

Önlemler sekmesinde ise bulunan risk değerinin azaltılması için alınacak önlemler planlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2a4e3916-a614-4f77-9a95-728b88f49d16)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada83bcc04-0add-4ce8-9bc2-81ac54972e73): Yeni bir Önlem tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc8804aaa-4d9d-4a97-8df6-73b5d13cd6d9): Listede seçili Önlem bilgisi güncellenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5fe337f8-9048-4ce4-8bc4-e8bbe14f903b): Listede seçili önlem bilgisi silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2889c2a5-29dd-490c-8565-18d0d4fc3a16): Listede seçili Önlem bilgisi görüntülenir.

Önlemler sekmesine gelindiğinde ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6ff2cb88-f651-4902-8757-191ebbff342a) (Yeni) butonuyla yeni önlem girişi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2a2f43be-707c-454d-afe9-06d666944b3d)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Referans Tipi:** Referans Tipi bilgisi DÖF, aksiyon, doküman, ve diğer seçeneklerinden seçilebildiği alandır. Referans tipi listeden seç seçeneği seçilirse referans tipi bilgisi listeden seçilir. Referans tipi yeni oluştur seçeneği seçilirse referans tipi bilgisi yeni oluşturulur.

**Referans Bilgisi:** Referans tipi DÖF, Aksiyon ve doküman olarak seçildiğinde ilgili referans kayıt seçilir.

**Önlem Tipi:** Mevcut veya planlanan olarak seçilir.

**Önlem Tarihi:** Önlem Tarihi bilgisi seçilir.

**Açıklama:** Açıklama bilgisi tanımlanır.

Açılan ekranda referans tipi açılır menüsünden önlemin türü seçilir. (DÖF, aksiyon, doküman, diğer). Daha sonra önlem tipi (mevcut, planlanan) ve önlem tarihi belirlendikten sonra önlemin açıklaması girilir ve ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload085770ed-f820-4bdc-af64-4abcc83076fa) (Kaydet) butonu tıklanarak kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7e16a652-af2a-427b-90bf-984d81f23d74)

Referans tipi olarak DÖF ve aksiyon seçilirse, QDMS’teki DÖF ve aksiyon modülleri ile bağlantı kurulacaktır. Mevcut açılmış DÖF ve aksiyonlardan herhangi biri önlemle ilişkilendirilebileceği gibi, yeni kayıtta açılabilir. Referans tipi olarak doküman seçilirse, QDMS’teki doküman ağacından doküman seçilir.

Örneğin önlem türü olarak aksiyon seçilir, listeden seç ve yeni oluştur seçeneklerinden yeni oluştur seçeneği seçilerek Aksiyon oluşturulursa aşağıdaki şekilde aksiyon modülü ile bağlantı kurulur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddabb6e21-e5d2-4430-84cd-cfd85b6e8007)

Ek Dosyalar Sekmesi Aksiyon ile ilgili bir ek dosya varsa sisteme eklendiği sekmedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcc78c957-9762-46ed-92e4-fda3bd2feadb)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload41d2473f-cbef-46e7-a123-88dcbb4a0607): Ek dosya sisteme yüklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9f633c50-54c8-419e-aa94-1f46c25fc75b): Yüklenen ek dosya bilgisi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload38b7dd4f-0836-49df-9a08-b2478e103914): Yüklenen ek dosya bilgisi silinir.

Yönlendirme Tarihçesi sekmesi Yönlendirme tarihçesi bilgisinin verildiği sekmedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf16072a8-ae4f-439f-a088-a47b020aed58)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload085770ed-f820-4bdc-af64-4abcc83076fa)( Kaydet) butonu tıklanarak Aksiyon gerçekleştirme işlemi için ilgili kullanıcıya gönderilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload002d05ab-a3fe-4d17-ba97-6b71aa17daa7)

**Revizyon İşlemi:** RDFD’ler kaydedildikten sonra herhangi bir anda revizyon işlemine tabi tutulabilir ve yeni risk analizleri gerçekleştirilebilir. Bunun için RDFD listesi açıkken ilgili risk detayı seçilir ve sağ üstteki butonlardan ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadddde8f67-5562-4831-b254-45fb4e26c310) (Revizyon) butonu tıklanır.

Bundan sonraki aşama risk detayını ilk kez doldururken izlenen adımlarla birebir aynıdır. Tek fark, RDFD ekranındayken revizyon numarası otomatik olarak bir artacaktır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload682776e4-61b6-4249-a06f-ff6758b6e754)

İlgili RDFD’nin eski revizyonlarını görüntülemek için, listede seçili durumdayken ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc2e4357b-1f69-4594-b59e-6ab138c0e474) (Eski Revizyonlar) butonuna basılır. Açılan yeni ekranda eski revizyonlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada272b834-2431-4c58-bbab-f80713cadd75)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1a989f3c-6ae3-4f2e-b995-dc7758504858):Eski Revizyonları görüntüler.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0f4e18db-835a-4b26-a650-842b230eaa03): Veriler Excel’ e aktarılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd4f15776-f0e1-4776-82f9-0e2afb47515b):Önceki ekrana geri dönülür.

Bir eski revizyon bilgilerini görüntülemek içinse listede seçim yaptıktan sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1ea1ab23-9af7-40ed-b8f6-31e4df8ad5c0) (Görüntüle) butonuyla bilgiler görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload74e90748-777b-476b-8b4f-ac22c1c8561d)

**Gözden Geçirme:** Mevcut riskler herhangi bir gözden geçirme işlemine tabi tutulabilir ve mevcut durum değerlendirilip açıklamalar yapılabilir. Bunun için RDFD listesi açıkken ilgili risk detayı seçilir ve sağ üstteki butonlardan ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaec3785f-076c-4b67-a149-7538d8fd71c4)(Gözden Geçir) butonu tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload232155de-7d59-408c-afdf-fc4e6b702860)

İlgili RDFD’nin eski gözden geçirmelerini görüntülemek için, listede seçili durumdayken ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0955d89e-fa34-4539-a482-8aa9162fa5fd) (Eski Gözden Geçirme) butonuna basılır. Açılan yeni ekranda risk eski gözden geçirmeleri listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadce75e768-950e-48ed-8705-af7e3cc91a78)

RDFD ekranındaki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd027b3cc-2491-435c-96b6-2de7e29c709d) (Grafik çiz) butonu yardımıyla ise revizyonlar bazında risk durum grafiği çizdirilebilir.

Açılan ekranda sol tarafta seçim yapılacak ve grafikte gösterilecek “Alanlar” bulunur. Alanlar kısmından ilgili seçimler yapıldıktan sonra ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd027b3cc-2491-435c-96b6-2de7e29c709d) (Grafik Çiz) butonuna basılarak grafiğin çizdirilmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbd740972-6e2d-42b7-a9a6-24d22889803a)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb13334e8-e3d7-4fa0-9644-f4abdbfe8a1b) ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1ecd243c-c989-483f-a95c-7e8784c4e1ad)

### **6.2.4.Raporlar**

**Menü Adı:** Entegre Yönetim Sistemi /Çevresel Boyutlar ve Etkileri/Raporlar

Çevresel Boyutlar ve Etkileri Modülü ile ilgili raporlar görüntülendiği kısımdır.

#### **6.2.4.1.Aksiyon Raporu**

**Menü Adı:** Entegre Yönetim Sistemi /Çevresel Boyutlar ve Etkileri/Raporlar/Aksiyon Raporu

Aksiyon Raporunu almak için, Raporlar menüsünden Aksiyon Raporu tıklanır. Çevresel Boyutlar ve Etkileri sonucu alınan aksiyon önlemlerinin alındığı rapordur. Bu rapor Excel’ e aktarılabilir. Özet raporu alınabilir. Ayrıca zaman bazlı aksiyon çizelge raporu çekilebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5421a7f9-30ec-4a4c-b93e-eab011815d61)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0f4e18db-835a-4b26-a650-842b230eaa03): Veriler Excel’ e aktarılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb530ab95-66c5-4f0c-b45e-571d533e128b): Kayıtlar filtrelenerek arama yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload06b87987-720b-449c-9335-64cde0f16a92):Özet Rapor alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload30e522e4-72e3-4b33-ae39-4aa30f3b61f6):Log görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc7c2bcb6-8cc7-4136-bcb3-2daafb3830dc):Aksiyon çizelge raporunu görüntüler.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf5b58c73-17e8-4996-931c-ef1e022cbbbc)(Excel aktar) butonuna basılırsa sistem listedeki Aksiyon Raporunu Excel formatında oluşturup kullanıcıya sunmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload528a73be-2cbc-40ae-be4a-a8d70503c32e)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload06b87987-720b-449c-9335-64cde0f16a92)(Özet Rapor) butonu tıklanarak Aksiyon Özet Rapor görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload108e14a7-19d5-4c46-9d63-eb25357a3ca9)

#### **6.2.4.2.Genel Risk Listesi**

**Menü Adı:** Entegre Yönetim Sistemi/Çevresel Boyutlar ve Etkileri/Raporlar/ Genel Risk Listesi

Genel Risk Listesi raporunu almak için, Raporlar menüsünden Genel Risk Listesi açılır. Kayıtlardaki tüm risk detaylarının görülebildiği listedir. Açılan pencerede RDFD’lerin listesi görüntülenmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload59438aec-a54e-4421-8012-35902ba91777)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0f4e18db-835a-4b26-a650-842b230eaa03): Veriler Excel’ e aktarılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb530ab95-66c5-4f0c-b45e-571d533e128b): Kayıtlar filtrelenerek arama yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf5b58c73-17e8-4996-931c-ef1e022cbbbc)(Excel aktar) butonuna basılırsa sistem listedeki RDFD’lerin Genel Risk Listesini Excel formatında oluşturup kullanıcıya sunmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload364bbf0f-bf46-402c-939b-f542d9252f35)

#### **6.2.4.3.Faaliyet Tarihçesi**

**Menü Adı:** Entegre Yönetim Sistemi/Çevresel Boyutlar ve Etkileri/Raporlar/ Faaliyet Tarihçesi

Çevresel Boyutlar ve Etkileri Modülünde kapsamında sistemde tanımlı Faaliyetlerin tarihçe bilgisinin görüntülendiği rapordur. Alınan raporda Faaliyet kodu, Faaliyet Tanımı ve Faaliyet Grubu Tanımı gibi alanların bilgileri görüntülenir. İstenirse Filtre sekmesinden alanlara göre filtreleme işlemi de gerçekleştirilebilir.Faaliyetler Tarihçesi raporunu almak için, Raporlar menüsünden Faaliyetler Tarihçesi açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc1fca5f8-b443-48c2-86d3-f94bdc89500f)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0f4e18db-835a-4b26-a650-842b230eaa03): Veriler Excel’ e aktarılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb530ab95-66c5-4f0c-b45e-571d533e128b): Kayıtlar filtrelenerek arama yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf5b58c73-17e8-4996-931c-ef1e022cbbbc)(Excel’e aktar) butonuna basılırsa, sistem otomatik olarak Faaliyetler Tarihçesi raporunu oluşturup kullanıcıya Excel formatında sunmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload26b4c2b3-9e72-4779-b2ef-865a40e35591)

#### **6.2.4.4.Faaliyet Grubu Tarihçesi**

**Menü Adı:** Entegre Yönetim Sistemi/Çevresel Boyutlar ve Etkileri/Raporlar/ Faaliyet Grubu Tarihçesi

Çevresel Boyutlar ve Etkileri Modülünde kapsamında sistemde tanımlı Faaliyet gruplarının tarihçe bilgisinin görüntülendiği rapordur. Alınan raporda Faaliyet Grubu kodu, Faaliyet Grubu Tanımı ve Üst Faaliyet Grubu Tanımı gibi alanların bilgileri görüntülenir. İstenirse Filtre sekmesinden alanlara göre filtreleme işlemi de gerçekleştirilebilir. Faaliyetler Grubu Tarihçesi raporunu almak için, Raporlar menüsünden Faaliyetler Grubu Tarihçesi açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade35505a0-3b67-4e68-9fe1-5abcaee1e2e7)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0f4e18db-835a-4b26-a650-842b230eaa03): Veriler Excel’ e aktarılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf5b58c73-17e8-4996-931c-ef1e022cbbbc)(Excel aktar) butonuna basılırsa sistem listedeki RDFD’lerin Faaliyet Grubu Tarihçesini Excel formatında oluşturup kullanıcıya sunmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload73f358aa-0143-45da-8402-5859b283db75)

#### **6.2.4.5.Faaliyet Raporu**

**Menü Adı:** Entegre Yönetim Sistemi/Çevresel Boyutlar ve Etkileri/Raporlar/ Faaliyet Raporu

Çevresel Boyutlar ve Etkileri Modülü kapsamında sistemde tanımlı Faaliyetlerin görüntülendiği rapordur. Alınan raporda Faaliye Kodu, Faaliyet Tanımı ve Faaliyet Grubu gibi alanların bilgileri görüntülenir. İstenirse Filtre sekmesinden alanlara göre filtreleme işlemi de gerçekleştirilebilir. Faaliyetler Raporunu almak için, Raporlar menüsünden Faaliyetler Raporu menüsü açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7c022f70-fe6d-41d7-95f0-dd2d58af1d6e)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0f4e18db-835a-4b26-a650-842b230eaa03): Veriler Excel’ e aktarılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb530ab95-66c5-4f0c-b45e-571d533e128b): Kayıtlar filtrelenerek arama yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf5b58c73-17e8-4996-931c-ef1e022cbbbc)(Excel aktar) butonuna basılırsa sistem listedeki RDFD’lerin Faaliyet Raporunu Excel formatında oluşturup kullanıcıya sunmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbaf838a1-0171-4854-a953-37536cdf6ea9)

#### **6.2.4.6. Tekrar Eden Kayıtlar Raporu**

**Menü Adı**: Entegre Yönetim Sistemi/ Çevresel Boyutlar ve Etkileri /Raporlar/ Tekrar Eden Kayıtlar Raporu

Benzer risk kayıtlarının kaç kez tekrar ettiğini gösteren rapordur. Entegre Yönetim Sistemi/ Çevresel Boyutlar ve Etkileri /Raporlar/Tekrar Eden Kayıtlar raporundan ilgili rapor şablonu seçilir.Tekrar Eden Raporu ekranında Rapor Şablonu seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload598c2ecf-9930-4a63-ba77-f59911d64813)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb530ab95-66c5-4f0c-b45e-571d533e128b) Ara butonu ile kayıtlar filtrelenerek arama yapılabilir ve ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0f4e18db-835a-4b26-a650-842b230eaa03) (Excel aktar) botunu ile veriler Excel’ e aktarılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload64bcb107-76ce-4979-bbe6-011be2855a83)

#### **6.2.4.7.Risklerin Bölgelere Dağılımı**

**Menü Adı**: Entegre Yönetim Sistemi / Çevresel Boyutlar ve Etkileri /Raporlar/Risklerin Bölgelere Dağılımı

Çevresel Boyutlar ve Etkileri Modülü kapsamında iş yeri ve departman bazlı risklerin haritada gösterilmesinin sağlandığı rapordur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload03b5f084-bd91-407a-9f4d-1944484c7917)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb530ab95-66c5-4f0c-b45e-571d533e128b): Kayıtlar filtrelenerek arama yapılabilir.

İlgili İşyeri listesi veya Departman listesinde seçim yapılarak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb530ab95-66c5-4f0c-b45e-571d533e128b)(ara) butonu tıklanarak Harita sekmesinde işyeri ve departman bazlı risklerin harita üzerinde görüntülenmesi sağlanır.

### **6.2.5.Grafikler**

**Menü Adı:** Entegre Yönetim Sistemi/Çevresel Boyutlar ve Etkileri/ Grafikler

Çevresel Boyutlar ve Etkileri Modülü ile ilgili grafiklerin görüntülendiği kısımdır.

#### **6.2.5.1.Risk Revizyon Karşılaştırma Grafiği**

**Menü Adı:** Entegre Yönetim Sistemi/Çevresel Boyutlar ve Etkileri/ Grafikler/ Risk Revizyon Karşılaştırma Grafiği

Risk Revizyon Karşılaştırma Grafiğini almak için, Grafikler menüsünden Risk Revizyon Karşılaştırma Grafiği menüsü tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3e5924fc-7107-4575-bd21-c4f2179eb521)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload06b87987-720b-449c-9335-64cde0f16a92): Belirlenen özelliklere göre ekrana grafiği çizdirir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5c13f8b7-be94-43d5-ba4e-e914dc863a2f) : İstenen grafiği açılır menüden seçilen format türüne ( Excel, JPG, PDF vb. ) dönüştürerek dış ortama aktarır.

Açılan ekranda filtre sekmesinden grafik karşılaştırmasını almak istediğimiz alanları doldurarak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada79f8d10-ff72-485f-a5cb-4577a87b673f) (grafik çiz) butonu ile istenile risk revizyon karşılaştırması yapılır. Güncel öncesi revizyon sayısı ve X ekseni seçilerek grafik çiz butonu ile grafik oluşturulur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd8f6afde-b482-4f32-996d-9cef109bdf02)

#### **6.2.5.2.En Çoklar Analizi**

**Menü Adı:** Entegre Yönetim Sistemi/Çevresel Boyutlar ve Etkileri/ Grafikler/ En Çoklar Analizi

En Çoklar Analizi grafiğini almak için, Grafikler menüsünden En Çoklar Analizi menüsü tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload75b2f813-b49e-45a1-9d66-23049859b892)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload06b87987-720b-449c-9335-64cde0f16a92): Belirlenen özelliklere göre ekrana grafiği çizdirir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5c13f8b7-be94-43d5-ba4e-e914dc863a2f): İstenen grafiği açılır menüden seçilen format türüne ( Excel, JPG, PDF vb. ) dönüştürerek dış ortama aktarır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaa3e08e0-326e-4d0f-a688-bfce032dc525): Grafik verileri, Excel listesi biçiminde aktarılır.

En Çoklar Analizi ekranında, Grafik Seçenekleri bölümünde gerekli seçimler gerçekleştirilir. Grafikte olması istenen en çok aralık belirlenir. Grafik Seçeneklerinden X ekseninde yer alması istenen nitelik seçilir. Ana tema, renk paleti özelliklerinden grafik özelleştirilebilir. Grafik başlığı belirtilerek grafik oluşturmak için ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload06b87987-720b-449c-9335-64cde0f16a92) (Grafik çiz) butonuna tıklanır. Eğer istenirse birçok kritere göre filtreleme yapılabilir ve sadece bu özellikteki RDFD’lerin grafikte yer alması sağlanabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc5092289-88d6-44ed-aaf4-09928022dd33)

#### **6.2.5.3.Risk Dağılım Matrisi**

**Menü Adı:** Entegre Yönetim Sistemi/Çevresel Boyutlar ve Etkileri/ Grafikler/ Risk Dağılım Matrisi

Risk Dağılım Matrisini almak için, Grafikler menüsünden Risk Dağılım Matrisi menüsü tıklanır. Hangi aralıkta kaç tane risk olduğunu gösteren 2 boyutlu bir grafik oluşturur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload839ff2c5-c4ef-4667-9661-8f8137575056)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0f4e18db-835a-4b26-a650-842b230eaa03): Veriler Excel’ e aktarılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb530ab95-66c5-4f0c-b45e-571d533e128b): Kayıtlar filtrelenerek arama yapılabilir

Açılan ekranda grafik türü seçilir ve ara butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload411cf477-2176-4daa-95a2-8ea381be18dc)

#### **6.2.5.4.Risk Karşılaştırma Grafiği**

**Menü Adı:** Entegre Yönetim Sistemi/Çevresel Boyutlar ve Etkileri/ Grafikler/ Risk Karşılaştırma Grafiği

Risk Karşılaştırma Grafiğini almak için, Grafikler menüsünden Risk Karşılaştırma Grafiği sekmesi tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc0a4763c-8a79-49d4-bcd6-1f8d633cff00)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload06b87987-720b-449c-9335-64cde0f16a92): Belirlenen özelliklere göre ekrana grafiği çizdirir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5c13f8b7-be94-43d5-ba4e-e914dc863a2f): İstenen grafiği açılır menüden seçilen format türüne ( excel, jpg, pdf, vb. ) dönüştürerek dış ortama aktarır.

Açılan ekranda filtre sekmesinden grafik karşılaştırmasını almak istediğimiz alanları doldurarak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada79f8d10-ff72-485f-a5cb-4577a87b673f) (Grafik Çiz) butonu ile istenilen risk karşılaştırması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8b7cfb2b-3bc0-4d36-a944-4a45b52895a8)

### **6.2.6.Risk Değerlendirme Talebi**

**Menü Adı:** Entegre Yönetim Sistemi/ Çevresel Boyutlar ve Etkileri /Risk Değerlendirme Talebi

Risk Değerlendirme Talebi işleminin gerçekleştiği menüdür. Bu menü kullanılarak herhangi bir personele risk değerlendirme görevi aksiyon olarak açılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5161a2f5-03b6-4e9e-b9d8-ddb4d308f82b)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload48500497-a545-469b-89e3-1bea4c79e926):Yeni bir risk değerlendirme talebi tanımlar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2a9104f8-a7df-42fe-a865-52c991dae221): Listede seçili Risk değerlendirme talebini görüntüler.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0f4e18db-835a-4b26-a650-842b230eaa03): Veriler Excel’ e aktarılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb530ab95-66c5-4f0c-b45e-571d533e128b): Kayıtlar filtrelenerek arama yapılabilir

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload48500497-a545-469b-89e3-1bea4c79e926)(Yeni) butonu tıklanarak Risk Değerlendirme Talebi Tanımlama ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload582d20e5-8498-4f8f-9538-0b46c5e993f3)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Değerlendirecek Kişi:** Risk Değerlendirme Talebi Tanımlama ekranında Değerlendirecek Kişi bilgisinin sistemde tanımlı olan Personel Listesinden seçilebildiği alandır.

**Talep Açıklama:** Risk Değerlendirme Talebi Tanımlama ekranında Talep Açıklama bilgisinin girildiği alandır.

Risk Değerlendirme Talebi ile ilgili eklenecek Ek Dosya varsa eklendiği sekmedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2867bc0d-749e-40bb-b658-27369fe08c39)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload41d2473f-cbef-46e7-a123-88dcbb4a0607): Ek dosya sisteme yüklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9f633c50-54c8-419e-aa94-1f46c25fc75b): Yüklenen ek dosya bilgisi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload38b7dd4f-0836-49df-9a08-b2478e103914): Yüklenen ek dosya bilgisi silinir.

Açılan pencerede Risk Talebi ekranında değerlendirecek kişi ve talebin açıklaması girildikten sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload782d0b94-f78b-4ea5-8786-cf351632d5a5) (Kaydet) butonuyla talep kaydedilir ve ilgili kişiye aksiyon olarak açılır.
