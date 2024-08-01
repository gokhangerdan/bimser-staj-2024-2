---
title: Statü, Buton Tanımlama ve Alanları Statülere Atanması
description: Statü, Buton Tanımlama ve Alanları Statülere Atanması Yardım Dokümanı
sidebar_position: 1
---

:::tip Bilgi

İlgili konu başlığına sağ tarafta bulunan navigasyon yardımıyla hızlı bir şekilde ulaşabilirsiniz.

:::


**İSG Risk Değerlendirme Modülünde Statü, Buton Tanımlama ve Alanları Statülere Atanması Yardım dokümanı**


# **1.İSG RİSK DEĞERLENDİRME MODÜLÜ**

Kullanılmakta olan İSG risk değerlendirme metodolojisinin dijital ortamda takibini sağlama, risk analiz tarihçesini oluşturma ve izleme, risk değerlendirme sonucunda önlemleri belirleme ve takip etme, mevcut risk formlarının sisteme aktarımı, risk formları üzerinde yetki kontrolünü sağlama ile yetkisiz erişimi engellemeyi sağlayan risk değerlendirme modülüdür.

## **1.1.Sistem Altyapı Tanımları/İSG Risk Değerlendirme**

QDMS İSG Risk Değerlendirme Modülünün altyapısını oluşturmak amacıyla gerekli tanımlamaların yapıldığı kısımdır. Yapılan tanımlamalara göre Entegre Yönetim Sistemi menüsünden girişlerde bu veriler kullanılmakta ve görülmektedir.

### **1.1.1.Alan Tanımlama**

**Menü Adı**: Sistem Altyapı Tanımları/İSG Risk Değerlendirme/Alan Tanımlama

İSG Risk Değerlendirme Modülünde ilişki kurulacak fonksiyonlarda (Risk Değerlendirme Form Tanımlama, Risk Değerlendirme Detay, Faaliyet Grubu Tanımlama, Faaliyet Tanımlama) kullanılacak alanların tanımlandığı menüdür. Burada oluşturulan alanlar, alan havuzuna eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2b56bb29-53e4-4c4b-9dd7-e5f7c252e477)



**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload48d03ad3-5c61-49cc-9c7c-8c3473e5f508): Yeni bir alan eklenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload015b5fd1-f08a-4502-a612-4cba662d112e):Var olan alanda değişiklik yapılmak istenirse kullanılır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddd0afc38-18bc-421c-bf09-d87e5ae4b96d):İlgili alanı silmek için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf8accd5d-6caf-4d11-9ecd-46a160a3cf1b): Alanın değerleri tanımlanır.

Listeye yeni bir alan eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload768ad3ff-d73f-45b8-a137-f61e30a2a7b8) (Yeni) butonu tıklanarak Alan Tanımlama\\Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload95cfde30-6ef7-44b3-a893-8a0fbb1ab1dd)![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd1ac3699-1785-4d4c-b228-94d1255c5954)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Alan Kodu:** Alan kodu bilgisi tanımlanır. Daha önce tanımlamış alanlarla aynı olmayacak şekilde boşluk, Türkçe karakter gibi karakterler kullanmadan tanımlanmalıdır. Ör. ‘001’ , ‘RK’

**Alan Adı:** Alan adı bilgisi tanımlanır.

**Başlık Notu:** Alanın başlık notu bilgisi tanımlanır.

**Giriş Tipi:** Oluşturulan alanda kullanıcı tarafından veri girişi/seçim mi yapacağı ya da hesaplama yöntemi ile otomatik olarak sistem tarafından mı atanacağı belirlenir.

**Alan Tipi**: Oluşturulan alanın metin, numerik, tarih, liste vb. alan tiplerinden hangisi olacağı belirlenir.

**Görünme Şartı:** Tanımlama işlemi devam eden alanın daha önceden tanımlanan başka bir alanın değerine göre görünüp görünmeyeceği belirlenir. Kullanımı [ALANKODU]=ALAN_DEĞERİ vb. şekildedir. (Örneğin, Fırsat var mı? Alanının alan kodu 01; Fırsat alanının alan kodu 02 olsun. Eğer “Fırsat” Alanının, “Fırsat var mı?” Alanındaki seçeneklerden değer kodu 100 olan “Evet” değeri seçili ise görülmesi gerekiyorsa 02 numaraları “Fırsat” alanının görünme şartı bölümüne formül şu şekilde yazılmalıdır: [01]=100)

**Durum:** Alan durumu aktif veya pasif olarak seçilir.

**Termin Alanı:** Termin alanı aktif edilecekse ilgili kutucuk işaretlenir. Aksiyon ve DF’ lerin terminleri buradaki süre göz önüne alınarak belirlenir.

**Güncellemeden değer yükselmesin:** Güncellemeden değer yükselmesin bilgisi aktif edilecekse ilgili check box işaretlenir. Bu bilginin işaretli olduğu alanlarda puan değeri güncelleme sırasında mevcut değerden daha yüksek olarak girilemez.

**İlişkili Alan:** İlişkili alan özelliği ile seçenek tipli iki alan arasında ilişki kurulabilmektedir. Referans alanın elemanlarının tanımlandığı ekranda ilişkili alandan hangi değerler ile ilişkili olduğu seçilebilmektedir. Böylece referans alanın form üzerinde değeri değiştiğinde ilişkili alan seçimli olarak otomatik dolabilmekte ya da seçim ekranından sadece ilişkilendirilen değerler arasından seçim yapılabilmektedir.

**İlişkili Alan Otomatik Doldurulusun:** İlişkili alan otomatik doldurulsun seçeneği aktif edilecekse ilgili check box işaretlenir. Liste tipli iki alanın değerleri arasında kurulan ilişkiye göre alanlardan birinin otomatik doldurulmasını sağlar.

**Genişlik:** Alanın kolon genişliği bilgisi tanımlanır.

Alan tanımlama ekranında gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload763d7839-5c2e-4ff1-b437-44d519a45b08) (Kaydet) butonu tıklanarak kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf356473b-b01d-4def-9524-c46b1c510129)

Örnek olarak Frekans alanının tanımlanması için alan kodu, alan adı yazılmalı, giriş tipi veri girişi, alan tipi puanlı liste, durumu aktif olarak seçilmelidir. Şiddet gibi diğer alanların tanımlanması da bu menüde gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcf5e36e1-cc11-4f8b-a75e-f261d858ea41)

Frekans alanına değer eklemek için olasılık alanı seçili iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7f5a5445-8a98-40ae-9b43-ccde3cdb7ea4) (Değerler) butonuna tıklanarak alanın değerlerinin tanıtılacağı ekrana gelinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload384eaaa2-3d4e-4b39-a1e6-10384e173c62)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2bd00757-b350-43b4-b2a8-8f9da680c81c):Yeni bir değer tanımlanır

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8b738e03-b6ee-4f52-bdd7-9d4245dc794c): Değer ile ilgili herhangi bir düzeltme veya güncelleme yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8b93f23d-4c7c-47ab-a2c3-8e50974bcbf3): Değer silinebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload142d91bc-628d-4a60-940f-cb21aff5aa12): Kayıtlar filtrelenerek arama yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5eb0e5af-0047-4459-bfed-967ee9f06407) : Veriler Excel’ e aktarılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadec1a5340-c963-4205-b37b-839b5d86dcce): Şablon indirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc558d55a-2cac-4fea-9511-844b35c28fde): Şablon yüklenilir.

**Not:** Şablon İndir ve Şablon Yükle butonları ile sisteme toplu olarak alan değerleri aktarılabilmektedir. Şablon indirme butonu ile sistem şablonu bilgisayara indirir. İlgili şablon kullanıcılar tarafından doldurularak şablon yükleme butonu ile sisteme yüklendiğinde şablondaki tüm alan değerleri sisteme aktarılmış olacaktır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf405a5f7-38e1-4f51-9ebf-fa11b64ec4dd) : Yeni butonuna tıklanarak yeni değer tanımlama işlemine başlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6a3a0467-ad2e-419e-8351-fcd9a63f8b4a)![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1c03c4a1-b9b3-475d-abef-66ba11fa17e7)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Tanım:** Tanım bilgisi girilir.

**Açıklama:** Açıklama bilgisi yazılır.

**Değer:** Değerin puan karşılığı girilir.

**Durum:** Değerin durumu aktif veya pasif olarak seçilir.

**Varsayılan:** İlgili liste değerinin varsayılan olarak alanda görünmesini sağlar.

**Önlem zorunlu mu?:** Bu değer seçili olduğunda önlemler sekmesinden en az bir önlem girilmesi zorunlu olur.

Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload763d7839-5c2e-4ff1-b437-44d519a45b08) (Kaydet) butonu tıklanarak değer tanımlama işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc848151e-defb-4b6a-a52b-3b6de196a2aa)

Olasılık Alanın değerleri tanımlama işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload40f9b4c8-f4c7-4a18-b096-f0e238332691)

Şiddet Alanın değerleri tanımlama işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf584b1d8-cad6-4900-b7b4-2f15f601f92d)

Kişi Sayısı alanının değerleri tanımlama işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload82154cd8-7e3d-49e3-a5c1-13d10dd8131f)

Alanların değerlerinin tanımlanma işlemi gerçekleştikten sonra risk değeri gibi veri giriş tipi hesaplanan olan alanların formül girişleri yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcacbecb5-c183-441d-bd69-60406601ce14)![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada9b109c4-113f-46fd-b23c-34683fb18dd3)

Alan tanımlama-Yeni Kayıt ekranında Risk Puanın formul girişi yapılması için Giriş tipi alanı seçenek kısmından Hesaplanan seçeneği seçilir. Formül tipi Excel olarak belirlenir. Formül alanına Risk Puanın formül bilgisi yazılır. Alan Tipi alanında alan tipi sçeneklerinden metin seçilir. Gerekli alanlar dolduralarak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload763d7839-5c2e-4ff1-b437-44d519a45b08)(Kaydet) butonu tıklanarak Alan tanımlama -Yeni Kayıt ekranında formül girişi işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfea2fe33-db62-4000-994d-dd291ed87971)

Örnekteki formül aşağıdaki gibi analiz edilebilir.

**(F]\*[O]\*[S]\*[KS])** şeklinde yazılan bir alanda köşeli parantez içinde yazılan ifade alan kodlarını temsil etmektedir. Bu ifadeler alan tanımlama ekranında alanları tanımlarken kullanıcı tarafından belirlenir. Frekans alanı için, F yerine 01; Olasılık alanı için, O yerine 02; Şiddet alanı için, S yerine 03, Kişi Sayısı alanı için KS yerine 04 olarak kodlama yapılmış olsaydı formül, **([01]\*[02]\*[03]\*[04])** şeklinde olacaktı. Bu formülün sonucu olarak Risk Puanı Alanı, Frekans, Olasılık, Şiddet, Kişi Sayısı alanında seçilen değerlerin çarpımı olmak üzere sistem tarafından otomatik olarak hesaplanacaktır

**Sistemde mevcut bulunan alan tiplerinin tam listesi aşağıda belirtilmiştir;**

**Metin:** Elle yazım imkanı veren metin kutucuğu ekler.

**Metin Çok Satırlı:** Elle yazım imkanı veren karakter sınırı olmayan çok satırlı metin kutucuğu ekler.

**Nümerik:** Sayısal olarak veri girişi yaptırır.

**Nümerik-Parasal:** Parasal değer olarak nümerik giriş yaptırır.

**Nümerik-Birim:** Birim olarak nümerik giriş yaptırır.

**Tarih:** Takvim alanı ekler.

**Liste:** Birden fazla element arasından tek seçim yaptırır.

**Puanlı Liste:** Açılır menüden seçim yaptırır, liste elementlerinin puan değerleri mevcuttur.

**Arama Özellikli Liste:** Birden fazla element arasından geniş arama fonksiyonuyla arama yapabilecek şekilde, tekli ve/ veya çoklu seçim yapılmasını sağlar.

**Ağaç Liste:** Ağaç kırılımına sahip birden fazla element arasından geniş arama fonksiyonuyla arama yapabilecek şekilde seçim yapılmasını sağlar.

**Personel:** QDMS personel veri tabanından kişi seçilebilmesini sağlar.

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

**Başlık:** Formlara koyu harflerle yazılacak başlık alanı ekler.

**Dosya:** Dosya eklemesi için uygun alan getirecektir

**Resim:** Resim eklemesi için uygun alan getirecektir

**Resim Liste:** Resim listesinden seçim sağlar.

**Çoklu Resim:** Çoklu resim seçilmesini sağlar.

**Tablo:** Tablo tipli alan oluşturulmasını sağlar. (Bu tip bir alan eklendikten sonra alan değerleri olarak yeni alan tanımlamalarının yapılması gereklidir.)

**Sorgu:** QDMS/Ensemble veri tabanları içerisindeki ana verilerden seçim yapılabilmesi için tanımlanabilen alan türüdür. (Sadece Bimser Destek Ekibi tarafından tanımlanmalıdır) Tekli ve çoklu seçim yapılabilir.

**Sorgu Ağaç:** QDMS/Ensemble veri tabanları içerisindeki ağaç kırılımlı ana verilerden seçim yapılabilmesi için tanımlanabilen alan türüdür. (Sadece Bimser Destek Ekibi tarafından tanımlanmalıdır) Tekli ve çoklu seçim yapılabilir.

**Sekme:** Mevcut risk değerlendirme formunda alanların bulunduğu sekmenin haricinde alanların ilişki kurularak içerisinde görülebileceği yeni bir sekme oluşturur.

**Onay Kutusu Liste:** Talebe göre tekli veya çoklu seçim yaptırılacak tipte bir liste tipli alandır.

**Risk:** Risk tabanlı modüllerden değerlerin seçilebilmesini sağlar. Bu tip bir alan eklendikten sonra hangi modülden değerlerin geleceği alan tanımlama ekranında seçilmesi gereklidir..

**Açıklamalı Liste:** Seçilen liste değerinin yanına açıklama yazabilme imkanı sağlayan alan tipidir. Alan Tanımlama menüsünde alan değerleri tanımlanırken her değer için açıklama kutucuğunun aktif olup olmayacağının seçilmesi gerekir. Burada yapılan seçime göre Entegre Yönetim Sistemi menüsü altında bu alanın görüleceği menüde ilgili seçim yapıldığında alan değerinin yanına kullanıcının açıklama yazabilmesi için kutucuk açılmış olur.

**Pozisyon:** QDMS pozisyon veri tabanından pozisyon bilgisi seçilebilmesini sağlar.

**Saat:** Saat tipli alan ekler.

### **1.1.2.Fonksiyon Dizayner**

**Menü Adı**: Sistem Altyapı Tanımları/İSG Risk Değerlendirme/ Fonksiyon Dizayner

Fonksiyon Dizayner menüsü ile alan havuzuna eklenen alanlar İSG Risk Değerlendirme Modülünün ilgili fonksiyonları ile ilişkilendirilebilir. Bunun için Sistem Altyapı Tanımları / İSG Risk Değerlendirme Modülünün altından Fonksiyon Dizayner menüsüne gelinir. Açılan ekranda İSG Risk Değerlendirme Modülünün alan eklenebilecek fonksiyonları sıralanacaktır. Bu ekranda Kaynak Grubu Tanımlama, Kaynak Tanımlama, Risk Değerlendirme Form tanımlama, Risk Değerlendirme Detay, Önlem Tanımlama ve Kontrol Tanımlama fonksiyonlarında kullanılacak alanlar ve bunların sıralaması ile onay işlemlerindeki hiyerarşi detayı tanımlanır. Bu menüde kullanılacak butonlar İSG Risk Değerlendirme Modülü parametrelerinden “Statü kullanılsın mı? (E/H) ” 22. Numaralı parametresine bağlı olarak değişir. Bu parametre değeri “Evet” ise aşağıda bulunan butonların (![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload49aaf9f0-7de9-4ccc-a32d-002df0dc0e8a)Statüler, ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc25fc4b-e505-4eee-b554-818dd38e7f64)Butonlar ) tamamı gözükür; ancak parametre değeri “Hayır” olduğu durumlarda sadece ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbc1fd1e5-5ead-488b-a413-676a6e5c297a) (Alanlar) butonu görünür durumda olur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc52a3bab-248c-4770-84ad-6f96c2991721) **Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload49aaf9f0-7de9-4ccc-a32d-002df0dc0e8a): Statü tanımlamak için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc25fc4b-e505-4eee-b554-818dd38e7f64): Butonlar tanımlamak için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbc1fd1e5-5ead-488b-a413-676a6e5c297a): Formların detaylarında kullanılacak Alanlar belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbc1fd1e5-5ead-488b-a413-676a6e5c297a): Alanlar butonuna tıklanarak alanların ilgili fonksiyonla ilişkilendirilme yapılacağı ekran açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadeb215d56-d470-4269-8600-8fdae4ea7820)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadba56cd00-e9fa-4972-811a-e9ae5100b2b8)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload48d03ad3-5c61-49cc-9c7c-8c3473e5f508): Yeni Fonksiyon eklenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload015b5fd1-f08a-4502-a612-4cba662d112e): Listede seçili Fonksiyon bilgisi değiştirilir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddd0afc38-18bc-421c-bf09-d87e5ae4b96d): Listede seçili Fonksiyon bilgisi silinebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada277389b-a4db-492b-ba53-92079ec25259): Önceki ekrana geri dönülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb6f64e84-235b-4467-a30f-265218c476e4)Alanlar butonu ile açılan ekranda seçili fonksiyonda kullanılacak alanlar ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload768ad3ff-d73f-45b8-a137-f61e30a2a7b8)(Yeni) butonuna tıklanarak belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload38a6fb0b-32e2-44bb-8ef0-3337c3d21945)![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload46af1259-400b-4c83-a6bf-c06380727bb4)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Alan Adı:** Alan tanımlama ekranında tanımlanmış alanlardan alan seçimi yapılır.

**Zorunlu Mu? :** Alanın zorunlu olup olmadığı seçilir.

**Zorunluluk Mesajı:** Zorunlu alan doldurulmadığında verilecek uyarı mesajı bilgisi bu alana yazılır.

**Sıra No:** Alanın sıra no belirlenir.

**Varsayılan Rol:** İlgili alanın değeri daha önce tanımlanmış bir üst formdan ya da kaydı giren kişinin adı soyadı, pozisyonu, unvanı, departmanı, iş yeri gibi verileri ise bunlar için tanımlanmış rol seçilebilir.

**Varsayılan Değer Değiştirilmesin:** Seçilen alan varsayılan olarak bir değer getiriyorsa getirdiği değerin değiştirmemesini sağlar.

**Gridde göster:** Alanın gridde gösterilmesi gerekiyorsa ilgili check box işaretlenir.

**Seçimde göster:** Alanın seçimde gösterilmesi gerekiyorsa ilgili check box işaretlenir.

**Satır Sayısı:** İlgili alan çoklu satır ise, veri girişi ekranında kaç satır gözükmesi gerektiği belirlenir.

**Kolon Genişliği:** İlgili Modülde girilen kayıtların listesinde (gridde) alanın kolon genişliği bilgisinin belirlenir. Verinin uzun olduğu alanlar için ort. 250, sadece rakam girilen alanlar için ise 75 kullanılması idealdir. Alana girilecek veriler düşünülerek bu aralıklarda bir değer kullanmak uygun olacaktır.

**Aktif Statü:** Alanın sisteme tanımlanan statülerin hangilerinde aktif olacağını belirler. Bu alanda işaretlenen statülerde ilgili alanın tipine göre işlem gerçekleştirilebilir.

**Görünür Statü:** Alanın sisteme tanımlanan statülerin hangilerinde görüleceğini belirler. Aktif statüsü seçilen alanlar için aynı zamanda görünür statüde en az aktif statü alanında işaretlenen statüler olacak şekilde belirlenmelidir.

**Zorunlu Statü:** **:** Alanın sisteme tanımlanan statülerin hangilerinde zorunlu olacağını belirler.

Açılan ekranda alan bilgileri listeden seçilir, zorunlu bir alan ise kullanıcının bu alanı doldurmadığında çıkacak mesaj tanımlanır, sıra numarası belirlenir. Aktif statü, Görünür Statü ve Zorunlu Statü durumları seçilir. Zorunlu olup olmadığı, gridde gösterilip gösterilmeyeceği, kolon genişliği belirlenerek gerekli tüm alanlar doldurulduktan sonra ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8c786e70-b8f9-4b94-ad78-ed4d88994f06) (Kaydet) butonu tıklanarak, ilgili alan için fonksiyon ile ilişkilendirme işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload63508ad9-f5a4-4798-b233-7830bb2f500d)

### **1.1.3. İSG Risk Değerlendirme Parametreleri**

**Menü Adı:** Sistem Altyapı Tanımları/İSG Risk Değerlendirme/ İSG Risk Değerlendirme Parametreleri

İSG Risk Değerlendirme Modülünün kullanıcının istek ve ihtiyaçlarına göre sistemsel ayarlarının yapıldığı ve bunlara göre parametreleri belirlendiği menüdür. Parametrelerde yapılan değişikler tüm QDMS kullanıcılarını kapsar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada6e8d1a8-1e82-4e5f-a2c1-fd930ddd70c3)

İSG Risk Değerlendirme parametreleri menüsüne İSG Risk Değerlendirme kapsamında ulaşıldığı gibi BSAT/SAT/Konfigürasyon Ayarları/Parametreler menüsünden bu menüye de ulaşılmaktadır. Bsat Modülü menüsünde açılan ekranda tüm Modüllere ait parametrik ayarlamaların yapıldığı bölümdür. Açılan ekrandan filtre sekmesinden İSG Risk Değerlendirme seçilerek arama yapıldığında, ilgili Modülün parametreleri ekrana gelmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload65875cfb-c7db-478b-8cc0-6a647a6be8ef)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload96fa6259-3379-4009-b559-da7f3d1b31a7)

**Ekranda bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload015b5fd1-f08a-4502-a612-4cba662d112e): Listede seçili olan parametre için düzeltme/ değişiklik/ güncelleme yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload142d91bc-628d-4a60-940f-cb21aff5aa12): Kayıtlar filtrelenerek arama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5eb0e5af-0047-4459-bfed-967ee9f06407): Veriler Excel’ e aktarılır.

Bir paramatreden değişiklik yapılmak isteniyorsa, değişiklik yapılmak istenilen parametre seçilir. Parametrenin seçilmesi için parametre no alanına parametrenin numarası yazılır. Yada parametrenın numarası bilinmiyorsa tanım kısmına parametre ile ilgili anahtar bir kelime yazılırak parametre seçilir. İSG Risk Değerlendirme Modülü parametrelerinden 22 numaralı “Statu kullanılsın mı? (E/H)” parametresi bulunmaktadır. Bu yardım dokümanında İSG Risk Değerlendirme 22 numaralı parametresi aktif edilerek İSG Risk Değerlendirme Modülünde statü kullanımının işlem aşamalarının nasıl gerçekleştiği anlatılacaktır. Parametre değeri “Evet” seçilirse Sistem Altyapı Tanımları/ İSG Risk Değerlendirme / Fonksiyon Dizayner menüsünde Taslak, Onay vb. statü tanımlama işlemleri aşama aşama menüde gerçekleştirilerek gösterilecektir.

**Parametre No:**22

**Parametre Tanımı:** Statu kullanılsın mı? (E/H)

**Parametrenin Açıklaması:** İSG Risk Değerlendirme Modülünde statü kullanımı veya kullanılmaması sağlayan parametredir. Parametre değeri”Evet”seçildiğinde İSG Risk Değerlendirme Modülünde Fonksiyon Dizayner münüsünde Taslak , Onay vb. statü tanımlamasına yapılmasına imkan verir. Aksi takdirde parametre değeri “Hayır” seçilirse İSG Risk Değerlendirme Modülünde Fonksiyon Dizayner münüsünde Taslak , Onay vb. statü tanımlamasına yapılmasına imkan vermez.

Sistem Altyapı Tanımları/ İSG Risk Değerlendirme/ İSG Risk Değerlendirme Parametreleri menüsü tıklanılır. Açılan ekranda Parametre No alanına 22 numarası yazılarak 22 numaralı “Statu kullanılsın mı? (E/H)” parametresi seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaded253cb2-5604-4d36-938c-60099649f354)

İSG Risk Değerlendirme modülünün 22 numaralı “Statu kullanılsın mı? (E/H)” parametresi seçili iken ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload015b5fd1-f08a-4502-a612-4cba662d112e) (Değiştir) butonu tıklanarak parametrenin içeriği görüntülenir. Açılan ekranda parametre değeri Evet ve Hayır seçeneklerinde seçim yapılır. Parametre değeri Evet seçilirek parametre aktif yapılarak modülde statü kullanıma izin veriler. Aksi takdirde parametre değeri Hayır seçilerek parametre pasif yapılarak modülde statü kullanımına izın verilemez. Parametre değeri Evet seçilerek parametre aktif edilerek statü kullanıma izin verildikten sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload763d7839-5c2e-4ff1-b437-44d519a45b08) (kaydet) butonu tıklanarak kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload687e3b48-66ca-4d61-ae52-4ff9cf39ba53)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5514ebe0-4e60-44cb-b636-857479faec2a)

### **1.1.4.Onay Akışı Tanımlama**

Değerlendirilen risklerin belirlenen kullanıcılara onaya gitmesi için sistemde onay akışı kurgulanması gereklidir. Modülde statü kullanımı aktifleştirilerek onay akış kurgusu gerçekleştirilir. Bunun için Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Parametreler menüsüne gelinir. Açılan ekrandan Filtre sekmesinde İsg Risk Değelrlendirme Modülü seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0b4ef0d6-828f-4557-958e-43a7f3706b7c)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf270b436-19cf-4c3f-a09d-d5d784519881)

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload015b5fd1-f08a-4502-a612-4cba662d112e)(Değiştir) butonu tıklanarak 22 numaralı parametre olan “Statü kullanılacak mı?” değeri “Evet” olarak değiştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadffad2d1c-1c38-4942-aa9b-0536d33e7479)

Akış tanımları Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Akış tanımlama ekranından kontrol edilmeli yoksa akışları tanımlanmalıdır. Ayrıca Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Rol Tanımlama ekranından da onay akışları için rol tanımlamaları yapılır. Rol tanımlama işlemlerinde SQL ve QDMS veri tabanı bilgisi gerekeceğinden Bimser Teknik Destek ekibiyle iletişime geçilerek gerekli rol talep edilebilir.

### **1.1.4.1.Rol Tanımlama**

**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Rol Tanımlama

Modüllerde kullanılan onay akışları için onaycı olarak hangi role gideceği bilgisinin tanımlandığı menüdür. Sistemde her modül için rol tanımları mevcuttur. Gerekli görüldüğü durumlarda İsg risk Modülü için yeni rol tanımlamaları yapılır. Roller değiştirilmek istenildiğinde ya da yeni bir rol tanımlanmak istenildiğinde Bimser Çözüm Ekibinden destek alınabilir. İsg Risk değerlendirme Modülü için yeni bir Rol tanımlaması için Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Rol Tanımlama menüsü tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf2c70bfa-3d3b-45c3-962a-8284d6272ccf)

Açılan ekranda filtre sekmesinde Risk Değerlendirme Modülü seçilir. ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload142d91bc-628d-4a60-940f-cb21aff5aa12) (Ara) butonu tıklanarak sistemde tanımlı İsg Risk değerlendirme Modülü ilgili Rol Tanımlama listesi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload31138ba7-842f-43af-b7ec-bd01fbf9f2f1)

Rol Tanımlama ekranına yeni bir Rol eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload768ad3ff-d73f-45b8-a137-f61e30a2a7b8)(Yeni) butonuna tıklanarak Rol Tanımlama/ Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcd1e98e9-d4b9-4b67-8789-d83098b8ed31)

Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload763d7839-5c2e-4ff1-b437-44d519a45b08) (kaydet) butonuna tıklanarak Rol Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade91214c3-cb64-434d-9512-802d9a15bdd0)

### **1.1.4.2.Mesaj Gövdesi Tanımlama**

**Menü Adı:** Sistem Altyapı Tanımları/BSAT/Tanımlar/ Mesaj Gövdesi Tanımlama

Modüllerde yapılan işlemler sonrası gidecek olan maillerin içeriklerinin tanımlandığı menüdür. Sistemde İsg Risk değerlendirme Modülü için mesaj gövdeleri tanımlıdır, gerekli durumlarda mail içeriklerinde güncelleme yapılır veya yeni mesaj gövdeleri tanımlanabilir. İsg Risk değerlendirme Modülü için yeni bir Mesaj Gövdesi tanımlaması için Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Mesaj Gövdesi Tanımlama menüsü tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3c5435e9-3396-44f7-b432-1fe646253aab)

Açılan ekranda filtre sekmesinde Risk Değerlendirme Modülü seçilir. ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload142d91bc-628d-4a60-940f-cb21aff5aa12) (Ara) butonu tıklanarak sistemde tanımlı İsg Risk değerlendirme Modülü ilgili Mesaj Gövdesi Tanımlama listesi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd7f5533e-4b70-4e88-b55d-0ff69fd32e64)

Mesaj Gövdesi Tanımlama ekranına yeni bir Mesaj Gövdesi eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload768ad3ff-d73f-45b8-a137-f61e30a2a7b8)(Yeni) butonuna tıklanarak Mesaj Gövdesi Tanımlama/ Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaa6afa7d-ee8f-4321-a6b5-9092254d517e)

Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload763d7839-5c2e-4ff1-b437-44d519a45b08) (kaydet) butonuna tıklanarak Mesaj Gövdesi Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade4972eb3-e99b-43a7-9a9e-832effec8676)

### **1.1.4.3.Akış Tanımlama**

**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Akış Tanımlama

Modüllerde kullanılan onay akışlarının tanımlamaları yer aldığı menüdür. Sistemde her Modül için akış tanımı mevcuttur. Bu gerekli görüldüğü durumlarda İsg Risk Değerlendirme Modülü için yeni akış tanımlamaları yapılır. İsg Risk değerlendirme Modülü için yeni bir Akış tanımlaması için Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Akış Tanımlaması menüsü tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4493fd22-4756-45b6-9f46-4fb681c38af6)

Açılan ekranda filtre sekmesinde İSG Risk Değerlendirme Modülü seçilir. ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload142d91bc-628d-4a60-940f-cb21aff5aa12) (Ara) butonu tıklanarak sistemde tanımlı İsg Risk değerlendirme Modülü ilgili Akış Tanımlama listesi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload96f6bb90-670b-44cf-b292-de84f8e59ca0)

Akış Tanımlama ekranında yeni bir Akış eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload768ad3ff-d73f-45b8-a137-f61e30a2a7b8)(Yeni) butonuna tıklanarak Akış Tanımlama / Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb0c90fcc-6a59-4fff-bee3-00f654eda4c6)

Bu ekranda daha önceden sistemde tanımlanmış olan rollerden ilgili olan rol seçilerek eklenir .![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfb5a2adb-c211-4e5f-8bd8-2cf7f7a83184)(Ekle) butonuna tıklandığında rol tanımlamada yer alan roller açılmaktadır. Uygun olan rol seçilip kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload74988162-f949-444e-afcb-6be2dd25e6f8)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada0c9c1e6-cbe3-4d50-b036-9a6bacae4c9b)

İsg Risk Değerlendirme Modülü birden çok akış onaycısı tanımlanabilir. Ekranda sıra numarası onaycının kaçıncı sırada onay vereceğini belirtir. Hiyerarşi yapılır. 0, 1, 2 gibi sıra numaraları ile en son sıfırıncı onaycıya gelmesi sağlanabilir. Eğer onaycı olarak rol tanımlamadan bir grup seçildi ise ekranda onaycı sayısı o gruptan kaç personelin onaylamasının yeterli olacağını göstermektedir.

Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload763d7839-5c2e-4ff1-b437-44d519a45b08) (kaydet) butonuna tıklanarak Akış Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5c62f654-9197-4cac-8144-bf26c67bb6ee)

Akış tanımlama için uygun rol seçildikten sonra Alt modüle tanımlama menüsü de kontrol edilmelidir. Aksi takdirde Alt modülde tanımlama uygun değilse akış uygun bir şekilde sağlanmayabilir veya istenilen akış çalışmayabilir.

İsg Risk Değerlendirme Modülü için statü tanımlama işlemi için gerekli altyapı tanımlama işlemleri yapıldıktan sonra Statü tanımlama işlemlerine başlamak için Sistem Altyapı Tanımları/İSG Risk Değerlendirme/ Fonksiyon Dizayner menüsü tıklanılır. Açılan ekranda alan havuzuna eklenen alanların ilişkilendirileceği İSG Risk Değerlendirme Modülünün ilgili fonksiyonları listenilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload33a12f17-b346-44a1-b3f8-ea8228f8382f)

İSG Risk Değerlendirme modülünün 22 numaralı “Statü kullanılsın mı?(E/H)” parametresi değeri Hayır seçili (Parametre pasif iken) iken Fonksiyon Dizayner menüsünde görülen buton:

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7440e01e-7832-4e83-94e8-2a7f019cafc9)

**Ekranda bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbc1fd1e5-5ead-488b-a413-676a6e5c297a): Alanları fonksiyonlarla ilişkilendirilir.

İSG Risk Değerlendirme Modülünün 22 numaralı parametresinin parametre değeri Evet seçilmediğinde sadece ilk aşamada ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbc1fd1e5-5ead-488b-a413-676a6e5c297a) alanlar butonu görüntüler.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb9b90d0f-fbea-45e0-9524-de18b0d84f85)

İSG Risk Değerlendirme Modülünün 22 numaralı “Statü kullanılsın mı?(E/H)” parametresi değeri Evet seçili (Parametre aktif iken) iken Fonksiyon Dizayner menüsünde görülen butonlar:

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadde4f53e7-a4ab-404e-be42-839c1dd62e4a)

**Ekranda bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload49aaf9f0-7de9-4ccc-a32d-002df0dc0e8a): Statü tanımlamak için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc25fc4b-e505-4eee-b554-818dd38e7f64): Butonlar tanımlamak için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbc1fd1e5-5ead-488b-a413-676a6e5c297a): Alanları fonksiyonlarla ilişkilendirilir.

Parametre değeri Evet seçilerek parametre aktif edildikten İsg Risk Değerlendirme Modülünde statü kullanılması imkan verilmesi sağlanılır. 22 numaralı parametre aktif edildikten sonra Fonksiyon Dizanner menüsün de Statü ve Buton tanımlaması işlemini gerçekleştirildiği ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload49aaf9f0-7de9-4ccc-a32d-002df0dc0e8a)(Statüler) ve ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc25fc4b-e505-4eee-b554-818dd38e7f64)(Butonlar) adında iki buton ekranda görüntülenir.

### **1.1.2.1.Statü Tanımlama**

İSG Risk Değerlendirme Modülünde Fonksiyon Dizayner menüsü tıklanılır. Açılan ekranda alan havuzuna eklenen alanların ilişkilendirileceği İSG Risk Değerlendirme Modülünün ilgili fonksiyonları listenilir. Risk Değerlendirme Detay fonksiyon seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload54938ad5-3bdc-4f91-928f-84a74513396a)

Seçilen Risk Değerlendirme detay ekranda statü tanımlama işlemi gerçekleştirmek için ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3d9b5a80-5a38-45d0-9431-3d6f9abe31c7)(Statüler) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfca34e30-b88c-4127-9248-ae0565201537)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd5a5ae13-70a2-4263-ad09-0cd761e94c42)

**Ekranındaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload48d03ad3-5c61-49cc-9c7c-8c3473e5f508): Yeni bir statü tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload015b5fd1-f08a-4502-a612-4cba662d112e): Listede seçili statü bilgisi güncellenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddd0afc38-18bc-421c-bf09-d87e5ae4b96d): Listede seçili statü bilgisi silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload351a8604-3799-4c88-af8a-764b51b56563): Önceki ekrana geri dönülür.

Statü Tanımlama ekranında yeni bir statü eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload768ad3ff-d73f-45b8-a137-f61e30a2a7b8)(Yeni) butonuna tıklanarak Statü Tanımlama / Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadda672f89-794f-4688-9133-04042004da80)

**Açılan ekranda ilgili alanlar tanımlanır:**

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

**Akış Tanımı:** Sistemde tanımlı akışlarda hangi akışın olacağı seçilebildiği alandır. Akış tanımlama işlemi Bsat/Sistem Altyapı Tanımları/Konfigürasyon Ayarları/Akış Tanımlama menüsünde tanımlanır.

**Onay Talep Mesajı:** Sistemde tanımlı Mesajlardan Onay Talep Mesajının seçilebildiği alandır. Mesaj tanımlama işlemi Bsat/Sistem Altyapı Tanımları/Tanımlar /Mesaj Gövdesi Tanımlama menüsünde tanımlanır.

**Onay Taman Mesajı:** Sistemde tanımlı Mesajlardan Onay Taman Mesajının seçilebildiği alandır. Mesaj tanımlama işlemi Bsat/Sistem Altyapı Tanımları/Tanımlar /Mesaj Gövdesi Tanımlama menüsünde tanımlanır.

**Onay Red Mesajı:** Sistemde tanımlı Mesajlardan Onay Red Mesajının seçilebildiği alandır. Mesaj tanımlama işlemi Bsat/Sistem Altyapı Tanımları/Tanımlar /Mesaj Gövdesi Tanımlama menüsünde tanımlanır

Açılan ekranda statü kodu, statü adı, akışın başlatılıp başlatılmayacağı, yeni statü, durum, akış tanımı, onay talep mesajı, onay tamam mesajı ve onay ret mesajı girişleri yapılarak gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload763d7839-5c2e-4ff1-b437-44d519a45b08) (kaydet) butonuna tıklanarak statü tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6827b412-8675-4587-9a8b-4469581bfa96)

İsg Risk değerledirme Modülünde Risk Değerlendirme Detay menüsü ile ilgili tüm statülerin aynı şekilde tanımlama işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5c48cf34-98e2-4f8a-8115-ee636c9f4154)

### **1.1.2.2. Buton Tanımlama**

İSG Risk Değerlendirme Modülünde Fonksiyon Dizayner menüsü tıklanılır. Açılan ekranda alan havuzuna eklenen alanların ilişkilendirileceği İSG Risk Değerlendirme Modülünün ilgili fonksiyonları listenilir. Risk Değerlendirme Detay fonksiyon seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadca8bb42e-2dd8-4dd7-a0ef-fe95cc53306c)

Seçilen Risk Değerlendirme detay ekranda buton tanımlama işlemi gerçekleştirmek için ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1089c592-97ff-4458-9704-681fbfd4532b) (Butonlar ) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5ace322b-e7e0-4c26-afc0-2edaaf5796ea)

**Ekranındaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload48d03ad3-5c61-49cc-9c7c-8c3473e5f508): Yeni bir buton tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload015b5fd1-f08a-4502-a612-4cba662d112e): Listede seçili buton bilgisi güncellenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddd0afc38-18bc-421c-bf09-d87e5ae4b96d): Listede seçili buton bilgisi silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload351a8604-3799-4c88-af8a-764b51b56563): Önceki ekrana geri dönülür.

Buton Tanımlama ekranında yeni bir buton eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload768ad3ff-d73f-45b8-a137-f61e30a2a7b8)(Yeni) butonuna tıklanarak Buton Tanımlama / Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbe4542ac-e03d-4618-a28f-cbfc64d641b3)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Buton Kodu:** Buton kodu bilgisi tanımlanır. Daha önce tanımlamış alanlarla aynı olmayacak şekilde boşluk, Türkçe karakter gibi karakterler kullanmadan tanımlanmalıdır.

**Buton Adı:** Buton adı bilgisi tanımlanır.

**Buton Tipi:** Sistemde tanımlı buton tipi seçeneklerinde belirlendiği alandır.

**Resim:** Tanımlanan butonun resminin hangi buton resmi olacağının sistemde tanımlı buton resim seçeneklerinden belirlendiği alandır.

**Görünür Statü:** Tanımlanan butonun hangi statüde görüntüleneceği belirlendiği alandır.

**Yeni Statü:** Tanımlanan butona tıkanıldığında hangi statü geçiş yapacağı sistemde tanımlı statülerden seçildiği alandır.

**Durum:** Tanımlanan butonun durumu aktif veya pasif olarak seçilir.

**Uyarı Mesajı:** Tanımlanan butona tıklatıldığında ekranda uyarı mesajının bilgisinin girildiği alandır. Örneğin: Onaya göndermek istediğinizden emin misiniz?

Açılan ekranda Buton Kodu, Buton Adı belirlenir. Buton tipi ve Resmi belirlenir. Görünür Statüsü, Yeni Statü ve Durumu seçilir. Gerekli alanlar doldurulduktan sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfb3277e9-895f-461d-8046-cb3d13113e2e)(kaydet) butonuyla buton tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload925d602b-036e-4bb3-9837-7c6d3c4c91f6)

İsg Risk değerlendirme Modülünde Risk Değerlendirme Detay menüsü ile ilgili tüm butonlar aynı şekilde tanımlama işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd7b4b2cf-9e64-4df1-a6d8-251e40ab2b85)

## **1.2.Entegre Yönetim Sistemi/İSG Risk Değerlendirme**

Faaliyet Grupları, Faaliyet, Risk Formu, Risk Form Detaylarının tanımlandığı, Raporların Ve Grafiklerin görüntülendiği kısımdır.

### **1.2.1. Risk Değerlendirme Formu Tanımlama**

**Menü Adı**: Entegre Yönetim Sistemi/İSG Risk Değerlendirme/ Risk Değerlendirme Formu Tanımlama

Risk değerlendirme Formu Tanımlama işleminin gerçekleştiği menüdür. RDF tanımlamadaki amaç, risk analizinin yapılacağı detay formların belirli kategoriler (ünite, birim, faaliyet grubu, departman vb.) altında sınıflandırmaktır. Bunun için Entegre Yönetim Sistemi başlığı altındaki İSG Risk Değerlendirme Modülünün altında Risk Değerlendirme Formu Tanımlama menüsü açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadabc3e694-8cdf-4564-9ded-4ac7ddfc16f7)

RDF Tanımlama ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1175fab4-daed-413d-a92d-36836ceb165f) (Yeni) butonuyla yeni RDF tanımlaması gerçekleştirilebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9ef5027d-8211-4ecb-a27f-eba7f2617580)

RDF tanımlama ekranında formun kodunu eğer otomatik kod verilmemişse kullanıcı tarafından girilir, formun tanımı ve sorumlu kullanıcı grupları eklenerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload13acec60-d695-4157-8786-326cff6f863a) (Kaydet) butonu tıklanarak risk değerlendirme formu tanımlama işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfef2e135-b09a-43fb-9947-14097fd9d10d)

Bu şekilde bütün RDF’ler tanımlandıktan sonra, risk detayı eklenilecek RDF seçili iken sağ üstteki butonlardan ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload78a7bee6-863f-4d2e-b926-eec2e8f56b3c) (Detaylar) butonu tıklanarak Risk Değerlendirme Formu Detayı (RDFD) ekranına gelinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9cc01a67-b730-4c3d-bafa-7783d8f91895)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1175fab4-daed-413d-a92d-36836ceb165f)(Yeni) butonuyla Risk Değerlendirme Formu/Detaylar ekranı görüntülenir. İsg Risk Değerlendirme Modülü parametrelerinde 22 numaralı parametre “Statü kullanılsın (E/H) parametresi aktif edilerek görüntülen butonlar yardımıyla işlemlerin gerçekleştiği Risk değerlendirme Formu- Detaylar menüsünde görülmüştür. Sistem Altyapı Tanımları/ İsg Risk Değerlendirme/ Fonksiyon Dizayner menüsünde Alanlar butonu ile fonksiyonda ilişkilendirilen alanlar görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1cc44a30-eebe-4f11-88fb-c29e0dfbe529)

Risk Değerlendirme Formu-Detaylar menüsü ile ilişkilendirilen alanları değer kısmı seçilerek Risk Puanı hesaplaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload020c9c1a-16aa-4972-a4bd-579a07ff94fe)

Risk Değerlendirme Formu-Detaylar menüsünde gerekli alanlar doldurulduktan sonra Fonksiyon Dizayner menüsünde ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc25fc4b-e505-4eee-b554-818dd38e7f64)(Butonlar) butonu ile tanımlama işlemi yapılan ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfb3277e9-895f-461d-8046-cb3d13113e2e)(Taslak olarak Kaydet) butonu tıklanarak aynı menüde ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload49aaf9f0-7de9-4ccc-a32d-002df0dc0e8a)(Statüler) butonu ile tanımlama işlemi yapılan Taslak statüsü olarak kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadee7fb3de-84b9-40d4-a435-226b2ea60d4c)
