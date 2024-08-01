---
title: Toplu Risk Aktarım İşlemi
description: Toplu Risk Aktarım İşlemi Yardım Dokümanı
sidebar_position: 3
---

:::tip Bilgi

İlgili konu başlığına sağ tarafta bulunan navigasyon yardımıyla hızlı bir şekilde ulaşabilirsiniz.

:::


**Risk Modüllerinde Toplu Risk Aktarım İşlemi Kullanıcı Yardım Dokümanı**
# 

# **1.Bilgi Güvenliği Risk Değerlendirme Modülünde Riskleri Toplu Aktarım İşlemi**

Kullanılmakta olan Bilgi Güvenliği Risk Değerlendirme metodolojisinin dijital ortamda takibini sağlama, risk analiz tarihçesini oluşturma ve izleme, risk değerlendirme sonucunda önlemleri belirleme ve takip etme, mevcut risk formlarının sisteme aktarımı, risk formları üzerinde yetki kontrolünü sağlama ile yetkisiz erişimi engellemeyi sağlayan risk değerlendirme modülüdür. Risklerin toplu aktarımına örnek olarak Bilgi Güvenliği Risk Değerlendirme Modülünde risklerin toplu aktarım işlemin yapılması için Sistem Altyapı Tanımları kısmında Alan tanımlama, Fonksiyon Dizayner ve Onay akışı tanımlama işlemlerin yapılması gerekmektedir. Sistem Altyapı Tanımları kısmında Altyapı tanımları oluşturulduktan sonra Entegre Yönetim Sisteminde Varlık Grupları Tanımlama, Varlık Tanımlama ve Risk Değerlendirme Formu Tanımlama işlemi yapıldıktan sonra Risk Değerlendirme formu -Detaylar kısmında Şablon oluştur butonu ile şablon bilgisayara indirilerek ilgili alanlar doldurularak şablon yükle butonu ile şablon sisteme yüklenerek Risklerin toplu aktarım işlemi gerçekleştirilir. Bu butonların Risk Değerlendirme formu -Detaylar ekranında görüntülenmesi için ilgili modülde kullanıcının Modül yöneticisi olması gerekmektedir. Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Yönetici Tanımlama menüsünde Yeni butonu tıklanarak Modül olarak Bilgi Güvenliği Risk Değerlendirme seçilerek kullanıcının bu Modülde yönetici olarak tanımlama işlemi yapılmalıdır.

## **1.1.Sistem Altyapı Tanımları/ Bilgi Güvenliği Risk Değerlendirme**

Bilgi Güvenliği Risk Değerlendirme Modülünün risklerin toplu aktarım işlemi için altyapısını oluşturmak amacıyla gerekli tanımlamaların yapıldığı kısımdır. Yapılan tanımlamalara göre Entegre Yönetim Sistemi menüsünden girişlerde bu veriler kullanılarak Risk değerlendirme Formu- Detaylar menüsünde Risklerin toplu aktarım işlemi yapılır.

### **1.1.1.Alan Tanımlama**

**Menü Adı:** Sistem Altyapı Tanımları/Bilgi Güvenliği Risk Değerlendirme/Alan Tanımlama

Bilgi Güvenliği Risk Değerlendirme Modülünde ilişki kurulacak fonksiyonlarda (Risk Değerlendirmeleri, Varlık Grubu Tanımlama, Varlık Tanımlama vb.) kullanılacak alanların tanımlandığı menüdür. Burada oluşturulan alanlar, alan havuzuna eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaded1da9ef-4378-426d-9f01-114da8aed4c9)



**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4fa9c103-d815-4701-bc66-4edcb6ec5924): Yeni bir alan eklenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadecb2f595-4ab1-4788-ae84-014a5a32dc47):Var olan alanda değişiklik yapılmak istenirse kullanılır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8c1abd76-8c84-451f-a046-d8c579e6d8d2):İlgili alanı silmek için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc8197025-ec5c-4f4a-99c0-d48342aff5ce): Alanın değerleri tanımlanır.

Listeye yeni bir alan eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload04352e5b-f6f3-4609-bb33-096c5462c569)(Yeni) butonu tıklanarak Alan Tanımlama/Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0ce97583-9322-433e-b81b-037f7a797dff) ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5dc5a46c-bd3c-440a-891c-442e7ffde0e6)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Alan Kodu:** Alan kodu bilgisi tanımlanır. Daha önce tanımlamış alanlarla aynı olmayacak şekilde boşluk, Türkçe karakter gibi karakterler kullanmadan tanımlanmalıdır. Ör. ‘001’ , ‘RK’

**Alan Adı:** Alan adı bilgisi tanımlanır.

**Başlık Notu:** Alanın başlık notu bilgisi tanımlanır.

**Giriş Tipi:** Oluşturulan alanda kullanıcı tarafından veri girişi/seçim mi yapacağı ya da hesaplama yöntemi ile otomatik olarak sistem tarafından mı atanacağı belirlenir.

**Alan Tipi**: Oluşturulan alanın metin, numerik, tarih, liste vb. alan tiplerinden hangisi olacağı belirlenir.

**Görünme Şartı:** Tanımlama işlemi devam eden alanın daha önceden tanımlanan başka bir alanın değerine göre görünüp görünmeyeceği belirlenir. Kullanımı [ALANKODU]=ALAN_DEĞERİ vb. şekildedir. (Örneğin, Fırsat var mı? Alanının alan kodu 01; Fırsat alanının alan kodu 02 olsun. Eğer “Fırsat” Alanının, “Fırsat var mı?” Alanındaki seçeneklerden değer kodu 100 olan “Evet” değeri seçili ise görülmesi gerekiyorsa 02 numaraları “Fırsat” alanının görünme şartı bölümüne formül şu şekilde yazılmalıdır: [01]=100)

**Durum:** Alan durumu aktif veya pasif olarak seçilir.

**Termin Alanı:** Termin alanı aktif edilecekse ilgili check box işaretlenir. Aksiyon ve DF’ lerin terminleri buradaki süre göz önüne alınarak belirlenir.

**Güncellemeden değer yükselmesin:** Güncellemeden değer yükselmesin bilgisi aktif edilecekse ilgili check box işaretlenir. Bu bilginin işaretli olduğu alanlarda puan değeri güncelleme sırasında mevcut değerden daha yüksek olarak girilemez.

**İlişkili Alan:** İlişkili alan özelliği ile seçenek tipli iki alan arasında ilişki kurulabilmektedir. Referans alanın elemanlarının tanımlandığı ekranda ilişkili alandan hangi değerler ile ilişkili olduğu seçilebilmektedir. Böylece referans alanın form üzerinde değeri değiştiğinde ilişkili alan seçimli olarak otomatik dolabilmekte ya da seçim ekranından sadece ilişkilendirilen değerler arasından seçim yapılabilmektedir.

**İlişkili Alan Otomatik Doldurulusun:** İlişkili alan otomatik doldurulsun seçeneği aktif edilecekse ilgili check box işaretlenir. Liste tipli iki alanın değerleri arasında kurulan ilişkiye göre alanlardan birinin otomatik doldurulmasını sağlar.

**Genişlik:** Alanın kolon genişliği bilgisi tanımlanır.

Alan tanımlama ekranında gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbfa5a41a-360d-43ee-be15-e009c6e68d14) (Kaydet) butonu tıklanarak kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload05cadac8-5e68-4e4d-9ca3-28240a190c57)

Örnek olarak olasılık alanının tanımlanması için alan kodu, alan adı yazılmalı, giriş tipi veri girişi, alan tipi puanlı liste, durumu aktif olarak seçilmelidir. Şiddet, Olasılık gibi diğer alanların tanımlanması da bu menüde gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7dced8f0-7470-4dc4-8677-11952e789a36)

Olasılık alanına değer eklemek için olasılık alanı seçili iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada2148a6b-d56f-4394-a3b0-ce693506a7cc) (Değerler) butonuna tıklanarak alanın değerlerinin tanıtılacağı ekrana gelinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadae5ccaf6-482c-49ce-8937-0f0fccae9142)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5189986c-d63e-437a-9efa-33ff787acb02):Yeni bir değer tanımlanır

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload48b30a43-7224-4027-947c-f7f392772c61): Değer ile ilgili herhangi bir düzeltme veya güncelleme yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada9c759cc-da68-4880-bdc9-23ee031435a8): Değer silinebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload50b54035-3dd6-4997-a819-7df71ad84ef5): Kayıtlar filtrelenerek arama yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd3f3005a-f4a2-412b-b323-114d76adbb5b) : Veriler Excel’ e aktarılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1535df85-8d14-4991-aa82-037afcffed85): Şablon indirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload48d7c1c2-4f58-4f70-8e9d-3ffb9b5a6712): Şablon yüklenilir.

Not: Şablon İndir ve Şablon Yükle butonları ile sisteme toplu olarak alan değerleri aktarılabilmektedir. Şablon indirme butonu ile sistem şablonu bilgisayara indirir. İlgili şablon kullanıcılar tarafından doldurularak şablon yükleme butonu ile sisteme yüklendiğinde şablondaki tüm alan değerleri sisteme aktarılmış olacaktır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload466df6af-14a8-42a5-a1de-f86d19a95bb0) Yeni butonuna tıklanarak yeni değer tanımlama işlemine başlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc3a2cde0-8a4a-48f1-a1be-1010a6369868) ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade1acb769-0f07-489d-8d2c-b013f7af69c1)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Tanım:** Tanım bilgisi girilir.

**Açıklama:** Açıklama bilgisi yazılır.

**Değer:** Değerin puan karşılığı girilir.

**Durum:** Değerin durumu aktif veya pasif olarak seçilir.

**Varsayılan:** İlgili liste değerinin varsayılan olarak alanda görünmesini sağlar.

**Önlem zorunlu mu?:** Bu değer seçili olduğunda önlemler sekmesinden en az bir önlem girilmesi zorunlu olur.

Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbfa5a41a-360d-43ee-be15-e009c6e68d14) (Kaydet) butonu tıklanarak değer tanımlama işlemi gerçekleştirilir. Olasılık, şiddet, frekans vb. puanlı liste, liste, arama özellikli liste tipli alanların değer tanımlama işlemleri bu şekilde yapılır. Alan özelliklerine göre bu ekranda değişiklikler olabilmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7351117d-da13-43af-8f2a-7c53446097d1)

Şiddet Alanının değerleri tanımlama işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8b4d72d9-28bb-4985-ac82-bd05daeaf5f3)

Giriş tipi olarak veri girişi seçilen alanların tanımlanması yukarıdaki gibi gerçekleştirilir. Giriş tipleri hesaplanan (risk değeri gibi) olacak alanlar ise formülleri ile birlikte tanımlanır.”

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb0630f88-c66b-493c-bb15-d91e71d2d6bd)![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload080b5e32-368e-4f31-8bd9-0751575b5454)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0092635d-54a4-4d58-afb2-a9da4aa900bc)

Formül girişleri ilgili alanların tanımlama ekranlarında gerçekleştirilir. Örnek olarak bir formül aşağıdaki gibi analiz edilebilir.

([OL]\*[FR]\*[SD]) şeklinde yazılan bir alanda köşeli parantez içinde yazılan ifade alan kodlarını temsil etmektedir. Bu ifadeler alan tanımlama ekranında alanları tanımlarken kullanıcı tarafından belirlenir. Olasılık alanı için, OL yerine 01; Frekans alanı için, FR yerine 02; Şiddet alanı için, SD yerine 03 olarak kodlama yapılmış olsaydı formül, ([01]\*[02]\*[03]) şeklinde olacaktı. Bu formülün sonucu olarak Risk Seviyesi Alanı, Olasılık, Frekans ve Şiddet alanında seçilen değerlerin çarpımı olmak üzere sistem tarafından otomatik olarak hesaplanacaktır. Hesaplanan alanlarda bir diğer formül kullanımı ise IF fonksiyonu ile olmaktadır. IF Fonksiyonunun liste tipli alanlar için kullanılabilmesi için öncelikle ilgili alana değer tanımlanması gereklidir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb146a9d3-7ce4-4e5a-9a69-8e67108f0ff0) ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload98349f52-b611-4b3b-a509-a6c96cf5b105)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload585ed3de-9442-4f85-b956-f0871f1e0b09)

Risk Büyüklüğü alanının değerleri tanımlanır. Alan tanımlama ekranında ilgili alanda renk kutucuğu işaretlendiyse değerler ekranında bu değerin hangi rengi temsil ettiği seçilmelidir. Bu renklendirmeler Entegre Yönetim Sistemi menüsü altında risk detaylarını görüntülendiğinde ilgili riskin hangi aralıkta yer aldığını kullanıcılara görsel olarak sunmaktadır. Buradaki renklendirmelerin risk prosedüründeki renklerle uyumlu olmasına dikkat edilmelidir.![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade815f8fc-e32a-4c94-98f5-d357da28894e)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload466df6af-14a8-42a5-a1de-f86d19a95bb0) Yeni butonuna tıklanarak yeni değer tanımlama işlemine başlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2c29c0e5-b6b9-4e4e-9b6b-b3fb4857d6d7)![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc4db88a0-e840-42a1-b13d-e0fdab4820a7)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb1b32e33-74d3-424f-8d4c-3be61c1650f7)

İlgili alan değerleri tanımlandıktan sonra formül girişi yapılır. Formül girişi için alan tanımlama ekranındayken ilgili alanın üzerine tıklanır ve ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload303251aa-51f7-4ffa-8339-4ca2ac91e3a2) (Değiştir) butonu ile alan detaylarına girilir.

Bu alanda formül girişi gerçekleştirirken daha önce belirtildiği üzere alan kodlarının köşeli parantez olarak yazılması gereklidir. Formül, bazı ifadelerin farklı olması haricinde (noktalı virgül, virgül vb.) Excel’de kullanılan IF fonksiyonu ile aynı mantıkta yazılmalıdır. Formül kullanımı: IF([ALANKODU]KoşulŞartı; Doğru ise Değer Kodu; Yanlışsa Değer Kodu şeklindedir.

Örneğin bir formül şu şekilde bir analiz gerçekleştirilebilir.

| Formül Satırı                              | Satır Anlamı                                                                                                                                                                 |
|--------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  IF([RD]\>=400;3217;                       | RD alanı 400’den büyük eşitse Risk Seviyesi alanının 3217 numaralı değeri (Tolerans gösterilemez risk), değilse..                                                            |
|  IF(AND([RD]\<400;[RD]\>=200);3218;        | ..RD alanı 400’den küçük ve 200’den büyük eşitse Risk Seviyesi alanının 3218 numaralı değeri (Esaslı Risk), değilse…                                                         |
|  IF(AND([RD]\<200;[RD]\>=70);3219;         | ..RD alanı 200’den küçük ve 70’den büyük eşitse Risk Seviyesi alanının 3219 numaralı değeri (Önemli Risk), değilse…                                                          |
|   IF(AND([RD]\<70;[RD]\>=20);3220;3221)))) | ..RD alanı 200’den küçük ve 70’den büyük eşitse Risk Seviyesi alanının 3220 numaralı değeri (Olası Risk), değilse Risk Seviyesi alanının 3221 numaralı değeri (Önemsiz Risk) |

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8bae2d8a-b0f7-4d2d-b177-6211d889753a) ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload50444d80-e203-4a5c-a55b-afa63028eebb)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada12be5ea-d00c-4674-8fbf-f0fe20dc36a9)

Formül bir bütün olarak yazılırsa aşağıdaki şekilde olacaktır.

IF([RD]\>=400;3217;IF(AND([RD]\<400;[RD]\>=200);3218;IF(AND([RD]\<200;[RD]\>=70);3219;IF(AND([RD]\<70;[RD]\>=20);3220;3221))))

Sistemde mevcut bulunan alan tiplerinin tam listesi aşağıda belirtilmiştir;

-   **Metin:** Elle yazım imkanı veren metin kutucuğu ekler.
-   **Metin Çok Satırlı:** Elle yazım imkanı veren karakter sınırı olmayan çok satırlı metin kutucuğu ekler.
-   **Nümerik:** Sayısal olarak veri girişi yaptırır.
-   **Nümerik-Parasal:** Parasal değer olarak nümerik giriş yaptırır.
-   **Nümerik-Birim:** Birim olarak nümerik giriş yaptırır.
-   **Tarih:** Takvim alanı ekler.
-   **Liste:** Birden fazla element arasından tek seçim yaptırır.
-   **Puanlı Liste:** Açılır menüden seçim yaptırır, liste elementlerinin puan değerleri mevcuttur.
-   **Arama Özellikli Liste:** Birden fazla element arasından geniş arama fonksiyonuyla arama yapabilecek şekilde, tekli ve/ veya çoklu seçim yapılmasını sağlar.
-   **Ağaç Liste:** Ağaç kırılımına sahip birden fazla element arasından geniş arama fonksiyonuyla arama yapabilecek şekilde seçim yapılmasını sağlar.
-   **Personel:** QDMS personel veri tabanından kişi seçilebilmesini sağlar.
-   **Departman:** QDMS departman veri tabanından departman bilgisi seçilebilmesini sağlar.
-   **Unvan:** QDMS unvan veri tabanından unvan bilgisi seçilebilmesini sağlar.
-   **Doküman:** QDMS doküman veri tabanından doküman seçilebilmesini sağlar.
-   **Süreç:** QDMS süreç veri tabanından süreç seçilebilmesini sağlar.
-   **Yönetim Sistemi:** QDMS yönetim sistemi veri tabanından yönetim sistemi bilgisi seçilebilmesini sağlar.
-   **Müşteri:** QDMS müşteri veri tabanından müşteri bilgisi seçilebilmesini sağlar.
-   **Tedarikçi:** QDMS tedarikçi veri tabanından tedarikçi bilgisi seçilebilmesini sağlar.
-   **Ürün Grubu:** QDMS ürün grubu veri tabanından ürün grubu bilgisinin seçilebilmesini sağlar.
-   **Ürün:** QDMS ürün veri tabanından ürün bilgisinin seçilebilmesini sağlar.
-   **Şirket Profili:** QDMS şirket profili veri tabanından şirket profili bilgisi seçilebilmesini sağlar.
-   **Başlık:** Formlara koyu harflerle yazılacak başlık alanı ekler.
-   **Dosya:** Dosya eklemesi için uygun alan getirecektir
-   **Resim:** Resim eklemesi için uygun alan getirecektir
-   **Resim Liste:** Resim listesinden seçim sağlar.
-   **Çoklu Resim:** Çoklu resim seçilmesini sağlar.
-   **Tablo:** Tablo tipli alan oluşturulmasını sağlar. (Bu tip bir alan eklendikten sonra alan değerleri olarak yeni alan tanımlamalarının yapılması gereklidir.)
-   **Sorgu:** QDMS/Ensemble veri tabanları içerisindeki ana verilerden seçim yapılabilmesi için tanımlanabilen alan türüdür. (Sadece Bimser Destek Ekibi tarafından tanımlanmalıdır) Tekli ve çoklu seçim yapılabilir.
-   **Sorgu Ağaç:** QDMS/Ensemble veri tabanları içerisindeki ağaç kırılımlı ana verilerden seçim yapılabilmesi için tanımlanabilen alan türüdür. (Sadece Bimser Destek Ekibi tarafından tanımlanmalıdır) Tekli ve çoklu seçim yapılabilir.
-   **Sekme:** Mevcut risk değerlendirme formunda alanların bulunduğu sekmenin haricinde alanların ilişki kurularak içerisinde görülebileceği yeni bir sekme oluşturur.
-   **Onay Kutusu Liste:** Talebe göre tekli veya çoklu seçim yaptırılacak tipte bir liste tipli alandır.
-   **Risk:** Risk tabanlı modüllerden değerlerin seçilebilmesini sağlar. Bu tip bir alan eklendikten sonra hangi modülden değerlerin geleceği alan tanımlama ekranında seçilmesi gereklidir.
-   **Açıklamalı Liste:** Seçilen liste değerinin yanına açıklama yazabilme imkanı sağlayan alan tipidir. Alan Tanımlama menüsünde alan değerleri tanımlanırken her değer için açıklama kutucuğunun aktif olup olmayacağının seçilmesi gerekir. Burada yapılan seçime göre Entegre Yönetim Sistemi menüsü altında bu alanın görüleceği menüde ilgili seçim yapıldığında alan değerinin yanına kullanıcının açıklama yazabilmesi için kutucuk açılmış olur.
-   **Pozisyon:** QDMS pozisyon veri tabanından pozisyon bilgisi seçilebilmesini sağlar.
-   **Saat:** Saat tipli alan ekler.

### **1.1.2.Fonksiyon Dizayner**

**Menü Adı:** Sistem Altyapı Tanımları/Bilgi Güvenliği Risk Değerlendirme/ Fonksiyon Dizayner

Fonksiyon Dizayner menüsü ile alan havuzuna eklenen alanlar risk modüllerinin istenilen sayfaları ile ilişkilendirilebilir. Bunun için Sistem Altyapı Tanımları/ Bilgi Güvenliği Risk Değerlendirme Modülünün altından Fonksiyon Dizayner menüsüne gelinir. Açılan ekranda risk modülünün alan eklenebilecek fonksiyonları sıralanacaktır. Bu ekranda Varlık Grubu Tanımlama, Varlık Tanımlama, Risk Değerlendirme Form Tanımlama, Risk Değerlendirme Detay, Önlem Tanımlama ve Kontrol Tanımlama fonksiyonlarında kullanılacak alanlar ve bunların sıralaması ile onay işlemlerindeki hiyerarşi detayı tanımlanır. Bu menüde kullanılacak butonlar Bilgi Güvenliği Risk Değerlendirme modülü parametrelerinden “Statü kullanılsın mı?” (22. Parametre) parametresine bağlı olarak değişir. Bu parametre değeri “Evet” ise aşağıda bulunan butonların tamamı gözükür. Ancak parametre değeri “Hayır” olduğu durumlarda sadece “Alanlar” butonu görünür durumda olur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload22d1d826-b794-4bf2-8e8c-5ef4cb02e682)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada07daddb-fbe4-4f69-9cb3-e62b45103d73): Statü tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload90274d87-7cec-40f1-a0a1-b60acdf7bbd3): Buton tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfc1ba132-e220-4597-ba14-53d8598e58e6): Alanları fonksiyonlarla ilişkilendirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfc1ba132-e220-4597-ba14-53d8598e58e6): Alanlar butonuna tıklanarak alanların ilgili fonksiyonla ilişkilendirilme yapılacağı ekran açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload52a7a646-08ce-4a38-b7b6-d38a05c73761)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4fa9c103-d815-4701-bc66-4edcb6ec5924): Yeni bir alan eklenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadecb2f595-4ab1-4788-ae84-014a5a32dc47): Listede seçili alan değiştirilir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8c1abd76-8c84-451f-a046-d8c579e6d8d2): Listede seçili alan silinebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcf1c07d6-cd0c-48f4-a2bc-4bf5c4b980cc): Önceki ekrana geri dönülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload69141a05-8fa1-4f35-ad10-c0f76e1c05a8) ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9fecfc9f-d248-4ae7-8748-354b8f9abaf8)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Alan Adı:** Alan tanımlama ekranında tanımlanmış alanlardan alan seçimi yapılır.

**Zorunluluk Mesajı:** Zorunlu alan doldurulmadığında verilecek uyarı mesajı bilgisi bu alana yazılır.

**Sıra No:** Alanın sıra no belirlenir.

**Varsayılan Rol:** İlgili alanın değeri daha önce tanımlanmış bir üst formdan ya da kaydı giren kişinin adı soyadı, pozisyonu, unvanı, departmanı, iş yeri gibi verileri ise bunlar için tanımlanmış rol seçilebilir. Örneğin, Risk detay formunda risk girişini yapanın departmanı adında bir alanda sisteme kaydı giren kullanıcının departmanı gelmesi gerekiyor varsayılan rol kullanılabilir. Kullanılmadığı durumda kullanıcı kendi departmanını hem yanlış seçebilir hem de kaydı giren kullanıcı fazladan bir işlem yapmış olur. Burada seçilen varsayılan rol sayesinde, kullanıcı risk girişi yapmaya başladığında departmanı otomatik gelecektir.

**Varsayılan Değer Değiştirilmesin:** Seçilen alan varsayılan olarak bir değer getiriyorsa getirdiği değerin değiştirmemesini sağlar.

**Gridde göster:** Alanın gridde gösterilmesi gerekiyorsa ilgili check box işaretlenir.

**Seçimde göster:** Diğer risk ya da olay modüllerinden ilişki kurulması gerekli olduğu durumlarda alan tanımlama menüsünde risk tipli bir alan tanımlanabilir. Bunun sonucunda ilgili form ilişkisi kurulduğu takdirde risk sekmesi oluşacaktır. Bu sekmede ekle butonuna basıldığında ilişki kurulması gereken modüldeki risklerin /olayların listesi gelecektir. Gelen listenin sütunlarında hangi alanların gözükmesi gerekiyorsa o alanlar için ilgili modülde seçimde göster check box işaretlenmelidir. (Tablo, dosya, resim vb. tipli metinsel ifadenin dışında olan alanlar seçilmemelidir).

**Satır Sayısı:** İlgili alan çoklu satır ise, veri girişi ekranında kaç satır gözükmesi gerektiği belirlenir.

**Kolon Genişliği:** İlgili modülde girilen kayıtların listesinde (gridde) alanın kolon genişliği bilgisinin belirlenir. Verinin uzun olduğu alanlar için ort. 250, sadece rakam girilen alanlar için ise 75 kullanılması idealdir. Alana girilecek veriler düşünülerek bu aralıklarda bir değer kullanmak uygun olacaktır.

**Aktif Statü:** Alanın sisteme tanımlanan statülerin hangilerinde aktif olacağını belirler. Bu alanda işaretlenen statülerde ilgili alanın tipine göre işlem gerçekleştirilebilir.

**Görünür Statü:** Alanın sisteme tanımlanan statülerin hangilerinde görüleceğini belirler. Aktif statüsü seçilen alanlar için aynı zamanda görünür statüde en az aktif statü alanında işaretlenen statüler olacak şekilde belirlenmelidir.

**Zorunlu Statü:** **:** Alanın sisteme tanımlanan statülerin hangilerinde zorunlu olacağını belirler.

Açılan ekranda alan bilgileri listeden seçilir, zorunlu bir alan ise kullanıcının bu alanı doldurmadığında çıkacak mesaj tanımlanır, sıra numarası belirlenir. Aktif statü, Görünür Statü ve Zorunlu Statü durumları seçilir. Zorunlu olup olmadığı, gridde gösterilip gösterilmeyeceği, kolon genişliği belirlenerek gerekli tüm alanlar doldurulduktan sonra ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbc43aa83-fdce-4f02-9da7-b8700406492f) (Kaydet) butonu tıklanarak, ilgili alan için fonksiyon ile ilişkilendirme işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1d3dd780-98e9-4dd4-bcca-111373885ab8)

### **1.1.3.Onay Akışı Tanımlama**

Değerlendirilen risklerin belirlenen kullanıcılara onaya gitmesi için sistemde onay akışı kurgulanması gereklidir. Modülde statü kullanımı aktifleştirilerek onay akış kurgusu gerçekleştirilir. Bunun için Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Parametreler menüsüne gelinir. Filtreden Bilgi Güvenliği Risk Değerlendirme modülü seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload08fca2dc-e2f0-4f29-8422-f19734f10bbd)

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadecb2f595-4ab1-4788-ae84-014a5a32dc47)Değiştir butonu tıklanarak 22 numaralı parametre olan “Statü kullanılacak mı?” değeri “Evet” olarak değiştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload193b990c-13ac-49f2-a44f-d49b2a4c68f8)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8651cdb3-c0c2-4fe8-99ae-3bd1e62a1207)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc5d15a7b-ca02-4fa9-97a7-39c89146f03b)

**NOT:** Akış tanımları Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Akış tanımlama ekranından kontrol edilmeli yoksa akışları tanımlanmalıdır. Ayrıca Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Rol Tanımlama ekranından da onay akışları için rol tanımlamaları yapılır. Rol tanımlama işlemlerinde SQL ve QDMS veri tabanı bilgisi gerekeceğinden Bimser Teknik Destek ekibiyle iletişime geçilerek gerekli rol talep edilebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1d248480-b997-4b81-bf05-910c69e7f893)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4fa9c103-d815-4701-bc66-4edcb6ec5924):Yeni bir rol tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadecb2f595-4ab1-4788-ae84-014a5a32dc47): Listede seçili rol bilgisi güncellenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8c1abd76-8c84-451f-a046-d8c579e6d8d2): Listede seçili rol bilgisi silinebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload50b54035-3dd6-4997-a819-7df71ad84ef5): Kayıtlar filtrelenerek arama yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd3f3005a-f4a2-412b-b323-114d76adbb5b): Veriler Excel’ e aktarılabilir.

Rol Tanımlama ekranına yeni bir rol eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload04352e5b-f6f3-4609-bb33-096c5462c569)(Yeni) butonu tıklanarak Rol Tanımlama/Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload41e0c8ae-6b92-41ef-8d47-a8324077c4f8)

Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbfa5a41a-360d-43ee-be15-e009c6e68d14) (Kaydet) butonu tıklanarak rol tanımlama işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd4ac2848-d3b7-4de7-a8cb-1a04de53d9f3)

Sistem Altyapı Tanımları/ BSAT/ Tanımlar/ Mesaj Gövdesi Tanımlama ekranından modül için yeni mesaj gövdesi tanımlamaları yapılabilir. Ayrıca Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Akış Tanımlama ekranından akış tanımlamaları yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0f788015-6a32-4807-b457-219d4243144d)

Fonksiyon Dizayner menüsüne gelinir. Statü ve Butonlar adında iki farklı işlem butonu Risk Değerlendirme Form Tanımlama ve Risk Değerlendirme Detay fonksiyonları için menüye gelecektir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0b1d9cdd-d233-42f1-be5f-7f5203d4c8c1)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada07daddb-fbe4-4f69-9cb3-e62b45103d73): Statü tanımlamak için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcc19bc8d-4e48-4084-b9d5-bd2f090f5b64): Buton tanımlamak için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload42dbb2b1-20a0-4758-a9e3-45d34b142986) : Alanlar tanımlanır.

Fonksiyon Dizayner menüsünden ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada07daddb-fbe4-4f69-9cb3-e62b45103d73) (Statüler) butonu ile statüler tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc79aa815-07f0-4ffb-8709-ef522e3013e0)

**Ekranındaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4fa9c103-d815-4701-bc66-4edcb6ec5924): Yeni bir statü tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadecb2f595-4ab1-4788-ae84-014a5a32dc47): Listede seçili statü bilgisi güncellenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8c1abd76-8c84-451f-a046-d8c579e6d8d2): Listede seçili statü bilgisi silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload953f8a40-e37c-4e39-8063-861506b69196): Önceki ekrana geri dönülür.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4fa9c103-d815-4701-bc66-4edcb6ec5924) Yeni butonu ile yeni statü tanımlama ekranına gelinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload14008473-90f1-43b9-a1fb-718a0350c5a2)

Açılan ekranda statü kodu, statü adı, akışın başlatılıp başlatılmayacağı, yeni statü, durum, akış tanımı, onay talep mesajı, onay tamam mesajı ve onay ret mesajı girişleri yapılarak kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3a29cf54-3ab1-4432-a171-db230d6da287)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload953f8a40-e37c-4e39-8063-861506b69196): Butonu ile önceki ekrana dönülür

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0bd1dd85-ae7a-4181-9bda-4a47d06e5ac7)

Fonksiyon Dizayner ‘dan ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcc19bc8d-4e48-4084-b9d5-bd2f090f5b64) (Butonlar) butonu ile statülerde kullanılacak butonlar tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7e5af36a-7c5e-4cee-b53b-f0f63d8da87e)

**Ekranındaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4fa9c103-d815-4701-bc66-4edcb6ec5924): Yeni bir buton tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadecb2f595-4ab1-4788-ae84-014a5a32dc47): Listede seçili buton bilgisi güncellenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8c1abd76-8c84-451f-a046-d8c579e6d8d2): Listede seçili buton bilgisi silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload953f8a40-e37c-4e39-8063-861506b69196): Önceki ekrana geri dönülür.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4fa9c103-d815-4701-bc66-4edcb6ec5924)Yeni butonu ile yeni buton tanımlama ekranına gelinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5bab86de-891e-43d0-a37d-59a877637347)

Açılan ekranda Buton Kodu, Buton Adı belirlenir. Buton tipi ve Resmi belirlenir. Görünür Statüsü, Yeni Statü ve Durumu seçilir. Gerekli alanlar doldurulduktan sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload204dbea1-3b35-4931-bfad-f2be1de4f884)(kaydet) butonuyla kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload848af32c-3133-489a-8bd9-6b6fb07ff052)

Risk değerlendirme detay fonksiyonu için statü ve buton tanımlama işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0c5fd56a-901c-46b3-8a76-4d874a10e189)

Risk değerlendirme detay fonksiyonu için statüler tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc09d88c1-4039-407d-840d-f407c8a7dd7a)

Risk değerlendirme detay fonksiyonu için butonlar tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload26ea5488-df9b-4a36-bcb7-7f84cc754c0e)

## **1.2.Entegre Yönetim Sistemi/Bilgi Güvenliği Risk Değerlendirme**

Varlık Grupları, Varlık, Risk Formu, Risk Form Detaylarının tanımlandığı, Raporların ve Grafiklerin görüntülendiği kısımdır. Bu kısımda Risklerin toplu aktarım işlemin yapılması için öncelikle Varlık Tanımlama, Varlık grubu tanımlama, ve Risk Değerlendirme Formu tanımlama işlemlerinin yapılması gerekmektedir. Sistem altyapı Tanımlarında altyapı işlemleri tamamlandığı için Entegre Yönetim sistem kısmında bu tanımlama işlemleri yapılarak Risk toplu aktarım işlemleri yapılacaktır. Risk Değerlendirme Formu tanımlama menüsünde detaylar butonu tıklanarak açılan Risk Değerlendirme Formu-Detaylar sayfasında şablon oluştur butonu ile şablon bilgisayara indirilir, indirilen şablonda ilgili alanlar kullanıcılar tarafından doldurulduktan sonra şablon yükle butonu ile sisteme yüklenerek Risklerin toplu aktarım işlemi gerçekleşecektir.

### **1.2.1.Varlık Grubu Tanımlama**

**Menü Adı:** Entegre Yönetim Sistemi/Bilgi Güvenliği Risk Değerlendirme/Varlık Grubu Tanımlama

Bilgi Güvenliği Risk Değerlendirme Modülünde kullanılacak olan varlıkların tanımlanması için öncelikle bu varlıkların bağlı bulunacağı grupların tanımlanması gerekir. Bunun için Bilgi Güvenliği Risk Değerlendirme Modülünün Entegre Yönetim Sistemi başlığı altına gelinerek Varlık Grubu Tanımlama ekranı açılır. Bu ekranda Bilgi Güvenliği Risk Değerlendirmesine tabi tutulacak varlıkların genel ve alt kategorileri belirlenir. Varlık Grubu tanımlama işlemi Risk Modülünde risklerin toplu olarak aktarım işleminde karşımıza şablonda risk kaynağı tipi varlık grubu olarak seçildiğinde Risk kaynağı kodu alanında doldurulması gereken varlık kodu alanı olarak çıkmaktadır. Risk toplu aktarım şablonun Varlık grubu kodu alanı bilgisi doldurularak risklerin varlık grubu ilişkisi kurulduğu için bu menüde tanımlama işlemi yapılmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload17c24195-bcee-4ebf-b96a-bd9535a6a470)

**Ekrandaki bulunan butonlar yardımıyla**;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0912fbfa-3671-414d-bbbd-edab3d2827a3): Yeni bir varlık grubu tanımlanabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadff9a7849-13a0-4565-947d-55c840b6fcbb): Listede seçili varlık grubu bilgisi güncellenebilir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8c1abd76-8c84-451f-a046-d8c579e6d8d2): Listede seçili varlık grubu bilgisi silmek için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbecd2b2d-1ad3-4953-9597-a3e1ba38ad18):Varlık grupları tanımlamalarını Excel’ e aktarılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6194618e-b074-4131-ba73-05b44978cf8e): Şablon yüklemek için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9fed3c14-ce1f-406e-bb6c-4fb9a1985311): Şablon oluşturmak için kullanılır.

Not: Şablon oluştur ve Şablon Yükle butonları ile sisteme toplu olarak varlık gruplarının tanımları aktarılabilmektedir. Şablon oluştur butonu ile sistem şablonu bilgisayara indirir. İlgili şablon kullanıcılar tarafından doldurularak şablon yükleme butonu ile sisteme yüklendiğinde şablondaki tüm varlık grupları tanımları sisteme aktarılmış olacaktır.

Listeye yeni varlık grubu eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload04352e5b-f6f3-4609-bb33-096c5462c569) (Yeni) butonu tıklanarak Varlık grubu /Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0c0a0225-def5-4b87-8d6b-e1ad5f3a7701)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Bağlı Olduğu Varlık Grubu:** Bağlı olunan varlık grubu bilgisi sistemde tanımlı olan varlık grubu listesinden seçilir.

**Varlık Grubu Kodu:** Varlık grubu kodu bilgisi tanımlanır.

**Varlık Grubu Tanımı:** Varlık grubu tanımı girilir.

**Sorumlu Kullanıcı Grupları:** Sorumlu kullanıcı gruplarının sistemde tanımlı olan kullanıcı grubu listesinden seçilebilir.

**Otomatik Kod Şablonu**: Otomatik kod şablonu bilgisi tanımlanır.

**Otomatik Kod Sayacı:** Otomatik kod şablonunda belirlenen koda göre verilen varlık kayıtlarının kodunun hangi değerden başlayacağı belirlenir.

**Durum:** Aktif veya pasif durum seçilir.

Bu sayfada (varsa) varlık grubunun bağlı olduğu varlık grubu, varlık grubu kodu ve tanımı girilir. Eğer sadece belirli kullanıcı gruplarının bu varlıklarla işlem yapması isteniyorsa sorumlu kullanıcı grupları kısmından kullanıcı grupları seçilip eklenir. Durum menüsünden aktif/ pasif durumu belirlenir. ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload63316e19-180f-47dd-897d-4218401ab0cc) (Kaydet) butonuyla tıklanarak Varlık Grubu kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload884333a7-d3b7-4050-9349-eb3bba18c5a7)

Varlık grubu tanımlama işlemi sonrasında sistemde tanımlı olan varlık grubu Risk Kaynağı tipi seçeneği varlık grubu olarak seçim yapıldığında şablonda Risk kaynağı Kodu alanında varlık grubu kodu bilgisinin aktarım şablonunda yazılması için gereken zorunlu alandır. Risk Değerlendirme Formu -Detaylar Şablonunda Risklerin Toplu aktarım işleminin gerçekleşmesi için Varlık grubu tanımlanması kayıt işleminin yapılması gerekmektedir.

### **1.2.2.Varlık Tanımlama**

**Menü Adı:** Entegre Yönetim Sistemi/Bilgi Güvenliği Risk Değerlendirme/ Varlık Tanımlama

Risk Modülünde analizi yapılan risklerde ilişki kurulabilecek varlıkların tanımlandığı yerdir. Burada, oluşturulan varlık gruplarına bağlı olarak varlıklar tanımlanır. Varlık tanımlama sayfası, varlık grubu tanımlama sayfasına benzemektedir. Varlık tanımlama işlemi Risk Modülünde risklerin toplu olarak aktarım işleminde karşımıza şablonda risk kaynağı tipi varlık olarak seçildiğinde Risk kaynağı kodu alanında doldurulması gereken varlık kodu alanı olarak çıkmaktadır. Risk toplu aktarım şablonun Varlık kodu alanı bilgisi doldurularak risklerin varlık grubu ilişkisi kurulduğu için bu menüde tanımlama işlemi yapılmaktadır. Entegre Yönetim Sistemi altında Varlık Tanımlama menüsü tıklanarak ilgili sayfa görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload06dea82e-27d7-4c91-8e7a-676af613a988)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0912fbfa-3671-414d-bbbd-edab3d2827a3): Yeni varlık tanımlanabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadff9a7849-13a0-4565-947d-55c840b6fcbb): Listede seçili varlık bilgisi güncellenebilir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8c1abd76-8c84-451f-a046-d8c579e6d8d2): Listede seçili varlık bilgisi silmek için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadccecb380-2ff5-4f94-9abc-27dd68c1182a): Listede seçili varlık bilgisi kopyalar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb563ba41-2be8-45f7-9b81-5b4e872b7ce2): Arama fonksiyonu kullanılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbecd2b2d-1ad3-4953-9597-a3e1ba38ad18): Varlık tanımlamalarını Excel’ e aktarılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6194618e-b074-4131-ba73-05b44978cf8e): Şablon yüklemek için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9fed3c14-ce1f-406e-bb6c-4fb9a1985311): Şablon oluşturmak için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcf1c07d6-cd0c-48f4-a2bc-4bf5c4b980cc):Önceki ekrana geri dönülür.

Not: Şablon oluştur ve Şablon Yükle butonları ile sisteme toplu olarak varlık tanımları aktarılabilmektedir. Şablon oluştur butonu ile sistem şablonu bilgisayara indirir. İlgili şablon kullanıcılar tarafından doldurularak şablon yükleme butonu ile sisteme yüklendiğinde şablondaki tüm varlık tanımları sisteme aktarılmış olacaktır.

Listeye yeni varlık eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload04352e5b-f6f3-4609-bb33-096c5462c569) (Yeni) butonu tıklanarak Varlık Tanımla/Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6c45955b-4af7-4ab2-b1ef-91b757c6e420)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Varlık Grubu:** Varlık grubu bilgisinin sistemde tanımlı olan varlık grubundan seçilir.

**Varlık Kodu:** Varlık Kodu bilgisi sistem tarafından otomatik olarak verilir.

**Varlık Tanımı:** Varlık tanımı girilir.

**Sorumlu Kullanıcı Grupları:** Sorumlu kullanıcı gruplarının bilgisi sistemde tanımlı olan kullanıcı grubu listesinden seçilebilir.

**Sorumlu Personeller:** Sorumlu Personel bilgisi sistemde tanımlı olan Personel listesinden seçilebilir.

**Durum:** Faaliyet durumu aktif veya pasif seçilir.

Açılan ekranda sırasıyla varlık grubu, varlık kodu (eğer parametreden otomatik kod verme aktif edilmemişse (5-6. Parametreler)), varlık tanımı girilir. Eğer sorumlu kullanıcı grupları kullanılacaksa bu alan doldurulur. Aktif/ pasif durum bilgisi seçilir ve kaydedilerek varlık tanımı gerçekleştirilmiş olur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0380bddc-c61a-4571-9e52-d75d2fc759c0)

Varlık tanımlama işlemi sonrasında sistemde tanımlı olan varlık Risk Kaynağı tipi seçeneği varlık olarak seçim yapıldığında şablonda Risk kaynağı Kodu alanında varlık kodu bilgisinin aktarım şablonunda yazılması için gereken zorunlu alandır. Risk Değerlendirme Formu -Detaylar Şablonunda Risklerin Toplu aktarım işleminin gerçekleşmesi için Varlık tanımlanması kayıt işleminin yapılması gerekmektedir.

### **1.2.3.Risk Değerlendirme Formu Tanımlama**

**Menü Adı:** Entegre Yönetim Sistemi/ Bilgi Güvenliği Risk Değerlendirme/ Risk Değerlendirme Formu Tanımlama

Bilgi Güvenliği Risk Değerlendirme Modülü’nde varlık ve varlık grupları da tanımlandıktan sonra yapılacak son aşama, risklerin yer alacağı formların (RDF) tanımlanmasıdır. Bunun için Entegre Yönetim Sistemi başlığı altındaki Bilgi Güvenliği Risk Değerlendirme Modülü’nün altında Risk Değerlendirme Formu Tanımlama menüsü açılır. RDF tanımlamadaki amaç, risk analizinin yapılacağı detay formların belirli kategoriler ( ünite, birim, faaliyet grubu, departman vb. ) altında sınıflandırmaktır. Risklerin toplu olarak aktarım yapılması öncelikle Risk Değerlendirme Formu tanımlama işlemini yapılır. Risk Değerlendirme Formu tanımlama işleminde sonra açılan ekranda Detaylar butonu tıklanarak açılan Risk Değerlendirme Formu-Detaylar sayfasında şablon oluştur ve Şablon Yükle butonları karşımıza çıkar. Bu butonlar yardımıyla Risklerin toplu şekilde aktarım işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5b0f1283-c6eb-4a8e-9c97-6b6f5f463ad7)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4fa9c103-d815-4701-bc66-4edcb6ec5924): Yeni RDF ( Risk Değerlendirme Formu) tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadecb2f595-4ab1-4788-ae84-014a5a32dc47): Listede seçili RDF bilgisi güncellenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5d48afd8-dd15-466c-832c-26cb3c4cbb85): Listede seçili RDF bilgisi kopyalanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8c1abd76-8c84-451f-a046-d8c579e6d8d2): Listede seçili RDF bilgisi silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9e96a702-8a9a-427f-bd42-f1b9110d6008): Filtre ekranındaki kriterlere göre arama yapar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadba6f44b4-a417-4e4f-848f-d50d9f99fb87): RDF listesini Excel’e aktarır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload47ce7d98-cddf-4a31-b78f-9aed5bd9110c): Seçili RDF’nin detay bilgiler ekranını açar.

RDF Tanımlama ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload37a1ae5d-8fa3-4633-9c48-3d588b06e564) (yeni) butonuyla yeni RDF tanımlaması gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload37beb0c3-e003-4891-ad99-dda08c04a6c4)

**Açılan ekranda ilgili alanlar tanımlanır:**

**RDF Kodu:** RDF kodu bilgisi sistem tarafından otomatik olarak verilir.

**RDF Tanımı:** RDF tanımı bilgisi girilir.

**Sorumlu Kullanıcı Grupları:** Sorumlu kullanıcı grupları bilgisi sistemde tanımlı olan kullanıcı gruplarından seçilebilir.

**Sorumlu Personeller:** Sorumlu personeller bilgisi sistemde tanımlı olan personel listesinden seçilebilir.

**Otomatik Kod Şablonu:** Otomatik kod şablonu bilgisi tanımlanır. Bu alan, ilgili RDF içerisine risk kayıtları eklendiğinde bu kayıtların kodunun nasıl olacağını belirler.

**Otomatik Kod Sayacı:** Otomatik kod şablonunda belirlenen koda göre verilen risk kayıtlarının kodunun hangi değerden başlayacağı belirlenir.

RDF tanımlama ekranında formun kodunu (eğer otomatik kod verme aktif edilmemişse) kod bilgisi, formun tanımını ve istenirse sorumlu kullanıcı grupları eklenerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload71ac94e6-1417-4fe4-9ef7-2e5ac1f9b60e) (Kaydet) butonu tıklanarak risk değerlendirme formu tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc147bfb2-9a81-4d89-860c-1fd2c5c14aec)

Bu şekilde bütün RDF’ler tanımlandıktan sonra, risk detayı eklemek istenen RDF seçili iken sağ üstteki butonlardan ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf62515dc-6e58-4738-901a-bf0fd724d51e) (Detaylar) butonu tıklanarak Risk Değerlendirme Formu Detayı (RDFD) ekranına gelinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1f280ec8-e690-4c83-b743-5586d658dd41)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0912fbfa-3671-414d-bbbd-edab3d2827a3): Yeni RDFD tanımlanabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadff9a7849-13a0-4565-947d-55c840b6fcbb): Listede seçili form bilgisi güncellenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3a456f60-0760-4b91-a6f6-5eb3ad741df6): Listede seçili form bilgisi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9daaf72d-e0b4-4d94-b735-39bad886b99b): Listede seçili olan form bilgisi kopyalanabilir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8c1abd76-8c84-451f-a046-d8c579e6d8d2): Listede seçili olan form bilgisini silmek için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6f3452b9-9b23-4a6f-bf9e-94106716dc47): Listede seçili olan form bilgisi revize edilerek onaya gönderilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4c5f784a-4dc7-4f7c-b512-29fc4fc251fe): Listede seçili form bilgisinin eski revizyonları izlenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d5adab3-7e3a-4b9b-bc08-f1b219bdd65f): Listede seçili form bilgisi gözden geçirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload57ddcccd-ed92-422e-ab28-df2f8277661f): Listede seçili form bilgisi için eski gözden geçirmeler izlenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb563ba41-2be8-45f7-9b81-5b4e872b7ce2): Filtreleme fonksiyonu kullanılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3cee8de6-26da-401c-a026-0581a5ed7807): Yazdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc5d627c9-b786-4f95-be90-8357cc0cdbe0): Revizyon değişimi gösterir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbecd2b2d-1ad3-4953-9597-a3e1ba38ad18): Seçili form detayları Excel’ e aktarılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3cdb79c9-57cc-42e9-9ccd-ae43b541d2cc): Bir önceki ekrana dönmek için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfa812573-9def-41cf-8b13-235a033603ef):Grafik çizme için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4a47f654-78b7-4421-8014-9802f18102f8) : Şablon indirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload46b57486-5b33-42cb-b4ed-96987a792b5a) : Şablon yüklenilir.

Risk Değerlendirme Formu- Detaylar ekranında Şablon oluştur ve Şablon Yükle butonları ile sisteme toplu olarak Riskler aktarılabilmektedir. Şablon oluştur butonu ile sistem şablonu bilgisayara indirir. İlgili şablon kullanıcılar tarafından doldurularak şablon yükleme butonu ile sisteme yüklendiğinde şablondaki tüm riskler sisteme topluca aktarılma işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4a47f654-78b7-4421-8014-9802f18102f8) Şablon oluştur butonu ile İlgili şablon bilgisayara indirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9f1ce5b6-9fdb-45f3-a004-75880f4dae35)

**Risk Değerlendirme Formu Detaylar şablonunda ilgili alanlar tanımlanır;**

**RDFD Kodu:** Aktarım yapılacak Riskin sistemde tanımlı olmayan kod bilgisinin aktarım şablonuna yazıldığı zorunlu alandır. Numerik ve alphanumerik kod bilgisi girilir.

**Revizyon No:** Aktarım yapılacak Riskin Revizyon no bilgisinin aktarım şablonuna yazıldığı zorunlu alandır.

**Revizyon Tarihi:** Aktarım yapılacak Riskin Revizyon tarihi bilgisinin aktarım şablonuna yazıldığı zorunlu alandır.

**Risk Kaynağı Tipi:** Aktarım yapılacak Riskin Risk kaynağı tipinin Varlık grubu ve varlık seçeneklerinde aktarım şablonunda seçilebildiği alandır.

**Risk Kaynağı Kodu:** Aktarım yapılacak Riskin risk kaynağın kodu bilgisinin aktarım şablonuna yazıldığı zorunlu alandır. Risk kaynağı kodu bilgisi olan sistemde tanımlı varlık, varlık grupların kodu listesi şablonda varlık ve varlık grubu sekmelerinde bulunmaktadır. Bu listeden kod bilgisi alınarak şablona yazılır. Risk Kaynağı kodu varlık grubu için Varlık grubu kodu bilgisi, varlık içinde varlık kodu bilgisi şablona yazılmaktadır.

**Statü:** Aktarım yapılacak Riskin statü bilgisini seçeneklerinden aktarım şablonunda seçilebildiği alandır.

**Olasılık:** Aktarım yapılacak Riskin olasılık alanın puanlı liste değerlerin seçeneklerinde aktarım şablonunda seçilebildiği alandır.

**Şiddet:** Aktarım yapılacak Riskin şiddet alanın puanlı liste değerlerin seçeneklerinde aktarım şablonunda seçilebildiği alandır.

**Risk:** Aktarım yapılacak Riskin risk alanına metin tipli alan olarak tanım bilgisinin aktarım şablona yazılır.

**Risk Büyüklüğü:** Aktarım yapılacak Riskin Risk büyüklüğü alanın puanlı liste değerlerin seçeneklerinde aktarım şablonunda seçilebildiği alandır.

**Eski Revizyon:** Aktarım yapılacak Riskin varsa Eski revizyon bilgisinin aktarım şablonuna yazıldığı zorunlu alandır.

Risk Değerlendirme Formu- Detaylar Şablonunda Varlık sekmesinde sistemde tanımlı varlıkların listesi bulunmaktadır. Sistemde tanımlı varlıkların tanım ve kod bilgileri bu sekmede yer almaktadır. Aktarım şablonunda Risk kaynağı tipi varlık seçildiği takdirde kod bilgisine bu sekmeden ulaşılarak Risk kaynağı kodu alanında bilgisi şablonda yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadefb63992-327e-40ab-9c00-e05af46e82a9)

Risk Değerlendirme Formu- Detaylar Şablonunda Varlık grubu sekmesinde sistemde tanımlı varlık grupların listesi bulunmaktadır. Sistemde tanımlı varlık grupların tanım ve kod bilgileri bu sekmede yer almaktadır. Aktarım şablonunda Risk kaynağı tipi varlık grubu seçildiği takdirde kod bilgisine bu sekmeden ulaşılarak Risk kaynağı kodu alanında bilgisi şablonda yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9280da6c-fc81-4288-811a-a191880e5d0e)

Risk Değerlendirme Formu Detaylar şablonu doldurularak kaydedilir. ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload46b57486-5b33-42cb-b4ed-96987a792b5a) (Şablon yükle) butonu ile doldurulan şablon sisteme yüklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf4103803-1583-4350-b3c1-49bdd736615d)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf751dd85-ed7f-4d13-8c83-6d300daf419d)

Gözat botunu tıklanarak kaydedilen Risk Değerlendirme Formu-Detaylar şablonu seçilerek sisteme yükleme işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload084caf52-7581-4be0-9454-90db3ad406a2)

Sistemde “ Riskler başarıyla aktarılmıştır” mesajı ile Risklerin toplu aktarım işlemi gerçekleşmiştir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8abb45ac-f8b6-4faa-bb91-762db16f98f4)

Risk Değerlendirme Formu-Detaylar ekranında Risk Değerlendirme Formu-Detaylar şablonu ile toplu olarak aktarım yapılan Riskler liste sekmesinde Risk listesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5cfed00f-4b0b-4d95-9f8f-bc2275f92615)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadff9a7849-13a0-4565-947d-55c840b6fcbb)(Güncelle) butonu tıklanarak toplu aktarım yapılan risk görüntülenir. Alan Tanımlama menüsünde tanımlanan alanları, formüllerin bağlantılı olan Risk ve Risk büyüklüğünün sistemin otomatik olarak hesapladığı görüntülenir. Bu şekilde toplu bir şekilde risklerin aktarım işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2855e45a-d489-4873-9c10-8cbc55c3fdd1)

Not: Uyarlama çalışmaları sonrasında mevcut risk değerlendirmeleri sisteme toplu olarak aktarılabilmektedir. Bu sebeple alan tanımlama vb. işlemler tamamlandıktan sonra sistemin kullanıma hazır olduğuna karar verildiği takdirde BSAT\>Konfigürasyon Ayarları\>Yönetici Tanımlama menüsünde bu Modülde yani Bilgi Güvenliği Risk Değerlendirme Modülünde yönetici olarak belirlenen kullanıcıların Risk Değerlendirme Form Detayı ekranında şablon oluştur ve şablon yükle butonu çıkmaktadır. Bu şekilde şablon, sistemde tanımlanan alanlara göre otomatik olarak oluşturulmaktadır. Şablon oluştur butonu ile sistemde oluşturulan şablonu bilgisayara indirir. İlgili şablon kullanıcılar tarafından doldurularak şablon yükleme butonu ile sisteme yüklendiğinde form bazında tüm risklerini sisteme aktarma işlemi gerçekleştirilmiş olur.
