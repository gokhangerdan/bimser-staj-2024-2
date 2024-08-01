---
title: İSG Risk Değerlendirme 
description: İSG Risk Değerlendirme Yardım Dokümanı
sidebar_position: 22
---

:::tip Bilgi

İlgili konu başlığına sağ tarafta bulunan navigasyon yardımıyla hızlı bir şekilde ulaşabilirsiniz.

:::


**İSG Risk Değerlendirme Modülü(v.5.26) Kullanıcı Yardım Dokümanı**

Modül Versiyonu: 5.26

## **1.GİRİŞ**

İş sağlığı ve güvenliği faaliyetlerindeki; yasal mevzuatların gerektirdiği bir takım risk analizlerinin yapılması gerekmektedir. Risk analizi işletme faaliyetleri sırasında oluşabilecek potansiyel tehlikelerin tanımlanması ve bunlara ilişkin risklerin değerlendirilmesi, böylece beklenen veya olası risklerle ilgili kontrol tedbirlerinin alınmasına ilişkin yöntem ve esasların sistematik bir şekilde belirlenmesini sağlayarak, yaralanmaların ve sağlık bozulmalarının asgari seviyelere indirilmesini sağlamaktır. Aynı zamanda yönetim sistemleri de bu risk analizlerini ve analizler sonrasında çeşitli eylem planlarının hazırlanarak riskin azaltılmasının sağlanmasını zorunlu tutmaktadır.

## **2.AMAÇ**
Bu yardım kılavuzunun amacı, QDMS kullanan kuruluşların İSG Risk Değerlendirme modülünün implementasyonu sırasında ve sonrasında risk formları ile bu risklerle ilgili alınacak önlemlerin planlanması aşamasında izleyeceği yolu belirlemektir.


## **3.SORUMLULUKLAR**

Yönetim Sistemleri Temsilcisi, İSG Uzmanı, İşyeri Temsilcisi.

## **4.KISALTMALAR**

**RDF:** Risk Değerlendirme Formu

**RDFD:** Risk Değerlendirme Form Detayı

## **5.İŞ AKIŞI:**

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_7.png)


# **6.İSG Risk Değerlendirme Modülü**
Kullanılmakta olan İSG Risk değerlendirme metodolojisinin dijital ortamda takibini sağlama, risk analiz tarihçesini oluşturma ve izleme, risk değerlendirme sonucunda önlemleri belirleme ve takip etme, mevcut risk formlarının sisteme aktarımı, risk formları üzerinde yetki kontrolünü sağlama ile yetkisiz erişimi engellemeyi sağlayan risk değerlendirme modülüdür.
## **6.1.Sistem Altyapı Tanımları/İSG Risk Değerlendirme**
QDMS İSG Risk Değerlendirme modülünün altyapısını oluşturmak amacıyla gerekli tanımlamaların yapıldığı kısımdır. Yapılan tanımlamalara göre Entegre Yönetim Sistemi menüsünden girişlerde bu veriler kullanılmakta ve görülmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_8.png)
### **6.1.1.Kontroller**
#### **6.1.1.1.Kontrol Tanımlama**
**Menü Adı**: Sistem Altyapı Tanımları/İSG Risk Değerlendirme/ Kontroller/ Kontrol Tanımlama

Kontroller QDMS'te Risk Modüllerinde kullanılır. Kontroller 27001 EK A maddesinde geçen maddelerdir ve Kontroller sekmesinde gelmektedir.Kontroller sekmesinde her bir risk için kontrol adımı seçebilebilir.Kontroller sekmesinde, seçtiğiniz kontrol maddeleri, QDMS ortamında raporlar başlığında SOA raporu almak istediğinizde karşınıza çıkacaktır.Kısaca Kontroller SOA raporunun hazırlanmasında kullanılmaktadır.

İSG Risk Değerlendirme Modülü parametrelerinde  95  numaralı “Kontroller sekmesi kullanılsın mı?” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_9.png) Parametre aktif edildikten sonra Risk Değerlendirme Formu -Detaylar ekranında  yeni bir risk kaydının tanımlama işleminin yapıldığı yeni kayıt ekranında sekme olarak çıkar. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_10.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref1]:Yeni bir Kontrol tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_12.png):Listede seçili Kontrol bilgisi üzerinde  düzeltme/ değişiklik/ güncelleme yapılır. Kod bilgisi güncellenemez.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_13.png):Listede seçili Kontrol bilgisi silinebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_14.png):Veriler Excel’ e aktarılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_15.png):Kayıtlar filtrelenerek arama yapılabilir.

Kontrol Tanımlama ekranına yeni bir Kontrol eklemek için ekranın sol üst köşesindeki ![ref1]butonu tıklanarak Kontrol Tanımlama\Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_16.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Kontrol  Kodu:** Kontrol Tanımlama ekranında Kontrol kodu bilgisi tanımlandığı zorunlu alandır. Daha önce tanımlamış alanlarla aynı olmayacak şekilde boşluk, Türkçe karakter gibi karakterler kullanmadan tanımlanmalıdır. Ör. ‘001’ , ‘RK’

İlgili modülün 96 numaralı “Kontroller Oto Kod Şablonu”   parametresinde tanımlı kod şablonuna göre sistem otomatik kod şablonu atamasını yapar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_17.png)Tanımlanan oto kod şablonun kaçıncı sayaç değerinde başlayacağı bilgiside ilgili modülün 97 numaralı “Kontroller Sayac” parametresinde parametre değerinde  tanımlı değere göre gelmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_18.png)

Parametre değerinde sayaç değeri “0” olarak tanımlıdır. Kod şablonu KNT.001, KNT.002, KNT.003 şeklinde sistem  kod ataması yapacaktır.

**Bağlı Olduğu Kontrol:** Oluşturulma aşamasında olan Üst Kontrol  bir Kontrol  tanımının alt kırılımı olması halinde bu alan otomatik dolu gelir. Dolu olarak gelen alanda bağlı olduğu Kontrol  tanımının adı yazar. Bağlı olduğu üst kırılım silinmek istenildiğinde sağ yanda bulunan ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_19.png)  butonu veya değiştirilmek istenildiğinde sağ yanda bulunan ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_20.png)  butonu kullanılır. Bağlı olduğu bir üst Kontrol yok ise bu alan boş gelir.

**Kontrol  Tanımı:** Kontrol Tanımlama ekranında Kontrol  tanım bilgisinin tanımlandığı zorunlu alandır.

**Açıklama:** Kontrol  Tanımlama ekranında Açıklama bilgisinin girildiği alandır.

**Durum:** Kontrol Tanımlama ekranında Durum bilgisinin “Aktif” ve “Pasif” seçeneklerinde “Aktif” seçeneğinin seçildiği alandır. Durumu pasif olanlar Kontroller sistemde artık kullanılmadığına bir işarettir. 

Kontrol  Tanımlama ekranında gerekli alanlar doldurulduktan sonra sol üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_21.png)butonu tıklanarak Kontrol  Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_22.png)

Kontrol Tanımlama ekranında Filtre sekmesi ile Kontrol Kodu, Bağlı Olduğu Kontrol ve Kontrol Tanımı gibi alanlara veri girilip, ![ref2]  butonu tıklanarak arama kriterlerine göre filtreleme yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_24.png)

### **6.1.2.Alan Tanımlama**
**Menü Adı:** Sistem Altyapı Tanımları/iSG Risk Değerlendirme/Alan Tanımlama

İSG Risk Değerlendirme modülünde Fonksiyon Dizanyer menüsünde bulunan fonksiyonların sayfaları ile ilişki kurulacak alanların tanımlama işleminin yapıldığı menüdür. Bu menüde tanımlanan alanlar alan havuza eklenir. Alan havuzuna eklenen alanlar Fonksiyon Dizanyer menüsünde  bulunan Faaliyet Grubu Tanımlama, Faaliyet Tanımlama, Risk Değerlendirme Detay, Risk Değerlendirme Form Tanımlama ,Önlem Tanımlama ve Kontrol Tanımlama fonksiyonlarının sayfaları ile ilişkilendirme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_25.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref3]:Yeni bir alan eklenir.

![ref4]:Listede seçili alan bilgisi üzerinde değişiklik/düzenleme/güncelleme işlemleri yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_28.png):Listede seçili alan bilgisi kopyalanır.

![ref5]:Listede seçili alan bilgisi silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_30.png):Alanın değerleri tanımlanır.

**Olasık Puanlı Liste Tipli Parametrik Alan Tanımlama:** Açılır menüden seçim yaptırır, liste elementlerinin puan değerleri mevcut olan parametrik alan tipidir.

Alan Tanımlama ekranına yeni bir alan eklemek için ekranın sol üst köşesindeki ![ref3]butonu tıklanarak Alan Tanımlama\ Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_31.png)

Alan Tanımlama-Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_32.png)

**Açılan ekranda ilgili alanlar tanımlanır;**

**Alan Kodu:** Alan Tanımlama-Yeni Kayıt ekranında Alan Kodu bilgisinin girildiği zorunlu alandır. Daha önce tanımlamış alanlarla aynı olmayacak şekilde boşluk, Türkçe karakter gibi karakterler kullanmadan tanımlanmalıdır. Ör. ‘001’ , ‘RK’

**Alan Adı:** Alan Tanımlama-Yeni Kayıt ekranında Alan Adı bilgisinin girildiği alandır. 

**Başlık Notu:** Alan Tanımlama-Yeni Kayıt ekranında alanı veri girişinin yapılması ile ilgili  açıklayıcı bilgi içeren not bilgisinin girildiği alandır. Mouse ile alanın üzerine gelindiğinde görüntülenen bilgidir.

**Giriş Tipi:** Alan Tanımlama-Yeni Kayıt ekranında giriş tipinin Hesaplanan veya Veri Girişi tipi bilgisinin seçilebildiği alandır. Giriş Tipi seçeneği oluşturulan alanın manuel olarak veri girişi ile mi yoksa hesaplama yöntemi ile mi belirleneceğini gösterir. Örneğin; Veri Girişi.

**Alan Tipi:** Alan Tanımlama-Yeni Kayıt ekranında alan tipinin bilgisinin seçilebildiği alandır. Alan Tipi ise oluşturulan alanın metin, numerik, tarih, liste vb. tiplerinden hangisi olduğunu gösterir. Alan Tipi olarak Puanlı liste seçilir.

**Görünme Şartı:** Alan Tanımlama-Yeni Kayıt ekranında Görünme Şartı bilgisinin girildiği alandır. Bir alan eğer başka bir alanın şartına bağlı olarak görülecekse görünme şartı kullanılır. Liste tipli alanın değerlerine göre oluşturulan alanın görüntülenmesini sağlar. Kullanımı [ALANKODU]=ALAN\_DEĞERİ vb. şekildedir. (Örneğin, Fırsat var mı? Alanının  alan kodu 01; Fırsat alanının alan kodu 02 olsun. Eğer “Fırsat” Alanının, “Fırsat var mı?” Alanındaki seçeneklerden değer kodu 100 olan “Evet” değeri seçili ise görülmesi gerekiyorsa 02 numaraları “Fırsat” alanının görünme şartı bölümüne formül şu şekilde yazılmalıdır: [01]=100)

**Durum:** Alan Tanımlama-Yeni Kayıt ekranında durumun “Aktif” veya “Pasif” olarak bilgisinin seçilebildiği alandır. 

**Termin Alanı:** Termin alanı aktif edilecekse ilgili check box’ı işaretlenir. Aksiyon ve DÖF’ lerin terminleri buradaki süre göz önüne alınarak belirlenir.

**Güncellemeden değer yükselmesin:** Güncellemeden değer yükselmesin bilgisi aktif edilecekse ilgili check box’ı işaretlenir. Bu bilginin işaretli olduğu alanlarda puan değeri güncelleme sırasında mevcut değerden daha yüksek olarak girilemez.

**İlişkili Alan:** İlişkili alan özelliği ile seçenek tipli iki alan arasında ilişki kurulabilmektedir. Referans alanın elemanlarının tanımlandığı ekranda ilişkili alandan hangi değerler ile ilişkili olduğu seçilebilmektedir. Böylece referans alanın form üzerinde değeri değiştiğinde ilişkili alan seçimli olarak otomatik dolabilmekte ya da seçim ekranından sadece ilişkilendirilen değerler arasından seçim yapılabilmektedir.

**İlişkili Alan Otomatik Doldurulusun:** İlişkili alan otomatik doldurulsun seçeneği aktif edilecekse ilgili check box’ı  işaretlenir. Liste tipli iki alanın değerleri arasında kurulan ilişkiye göre alanlardan birinin otomatik doldurulmasını sağlar.

**Genişlik:** Alan Tanımlama-Yeni Kayıt ekranında genişlik bilgisinin girildiği alandır.

Açılan Alan Tanımlama-Yeni Kayıt alan kodu ve alan adı bilgisi girilir. Giriş Tipi veri girişi   ve  Alan Tipi seçilir. Durum kısmı seçilir. Alan Tanımlama ekranında gerekli alanlar doldurulduktan sonra sol üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_33.png)butonuna tıklanarak Alan Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_34.png)

Tanımlanan Olasılık alanına değer eklemek için olasılık alanı seçili iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_35.png) butonuna tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_36.png)

Alanın değerlerinin tanıtılacağı ekrana gelinir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_37.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref6]:Yeni bir değer tanımlanır

![ref7]:Listede seçili değer bilgisi üzerinde düzeltme veya güncelleme işlemleri yapılır.

![ref8]:Listede seçili değer bilgisinin silinme işlemi yapılır.

![ref9]:Kayıtlar filtrelenerek arama yapılabilir.

![ref10] :Veriler Excel’ e aktarılabilir.

![ref11]:Şablon indirilir.

![ref12]:Şablon yüklenilir.

Not: ![ref11]  ve ![ref12]  butonları ile sisteme toplu olarak alan değerleri aktarılabilmektedir. Şablon indirme butonu ile sistemdeki şablon kullanıcının bilgisayarına indirilir. İlgili şablon kullanıcılar tarafından doldurularak şablon yükleme butonu ile sisteme yüklendiğinde şablondaki tüm alan değerleri sisteme aktarılmış olacaktır.

Değerler-Olasılık ekranında ![ref6] butonuna tıklanarak yeni değer tanımlama işlemine başlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_45.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Tanım:** Değerler-Yeni Kayıt ekranında tanımlanan değerin tanım bilgisi yazıldığı alandır.

**Açıklama:** Değerler-Yeni Kayıt ekranında tanımlanan değerin açıklama bilgisi yazıldığı alandır.İSG Risk Değerlendirme parametrelerinde 21 numaralı “Puanlı Listede Açıklama Gösterilsin mi ?(E/H)” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_46.png)

Parametre aktif edildikten sonra risk kaydı ekranında alanın değeri seçildiğinde açıklama bilgiside görüntülenir.

**Değer:** Değerler-Yeni Kayıt ekranında tanımlanan değerin puan karşılığı yazıldığı alandır.

**Durum:** Değerler-Yeni Kayıt ekranında tanımlanan değerin durumu aktif veya pasif olarak seçildği alandır.

**Varsayılan:** Değerler-Yeni Kayıt ekranında tanımlanan değerin ilgili liste değerinin varsayılan olarak alanda görünmesini sağlandığı alandır. Bu alanla ilgili check box işaretlendiğinde sistem otomatik olarak alanın değerini seçenek olarak getirir.

**Önlem zorunlu mu?:** Değerler-Yeni Kayıt ekranında tanımlanan değerin  seçili olduğunda Önlemler sekmesinden en az bir önlem girilmesi zorunluğunun getirdiği alandır. İlgili seçenek seçildiğinde Önlemler sekmesinde önlem tanımlama işlemi yapılmadan sistem risk kaydını kaydetmez ve önlem tanımlama işlemi yapılacağına dair uyarı mesajı verir.

Gerekli alanlar doldurulduktan sonra sol üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_47.png) butonu tıklanarak değer tanımlama kayıt işlemi gerçekleştirilir. Olasılık, şiddet, frekans, puanlı liste, liste, arama özellikli liste tipli vb. alanların değer tanımlama işlemleri bu şekilde yapılır. Alan özelliklerine göre bu ekranda değişiklikler olabilmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_48.png)

Değerler -Olasılık ekranında diğer değerlerin tanımlama işlemi için ![ref11] ve ![ref12] butonları ile sisteme toplu olarak alan değerleri aktarım  işlemi yapılır.

Değerler-Olasılık ekranında ![ref11]  butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_49.png)

Değerler aktarım şablonu bilgisayara indirilir.İndirilen aktarım şablonunda ilgili alanlar ilgili bilgiler yazılarak doldurulur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_50.png)

Değerler-Olasılık  ekranında ![ref12] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_51.png)

Dosya Yükle ekranında “Gözat” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_52.png)

Açılan ekranda doldurulan Değerler Aktarım şablonu seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_53.png)

Sistem tarafından “Aktarım işlemi başarıyla tamamlandı.” mesajı verilerek puanlı liste alan tipinin değerlerinin aktarım işlemin gerçekleştiği belirtilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_54.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_55.png)

**Frekans Puanlı Liste Tipli Parametrik Alan Tanımlama:** Açılır menüden seçim yaptırır, liste elementlerinin puan değerleri mevcut olan parametrik alan tipidir.

Olasılık Puanlı liste tipli alanın tanımlama işlemi gibi aynı şekilde Frekans puanlı liste tipli  alanın tanımlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_56.png)

**Frekans Puanlı Liste tipli parametrik alanın değerlerinin tanımlama işlemi;**

Olasılık puanlı liste alan tipinde olduğu gibi Frekans Puanlı Liste tipinin  değerlerin tanımlama işlemi Değerler ekranında  ![ref6] butonu  ile manuel yada ![ref11] ve ![ref12] butonları ile kullanarak sisteme toplu olarak alan değerleri toplu aktarım işlemi  yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_57.png)

**Şiddet Puanlı Liste Parametrik  Alan Tipi Tanımlama:** Açılır menüden seçim yaptırır, liste elementlerinin puan değerleri mevcut olan parametrik alan tipidir.

Olasılık Puanlı liste tipli alanın tanımlama işlemi gibi aynı şekilde Şiddet puanlı liste tipli  alanın tanımlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_58.png)

**Şiddet Puanlı Liste tipli parametrik alanın değerlerinin tanımlama işlemi;**

Olasılık puanlı liste alan tipinde olduğu gibi Şiddet Puanlı Liste tipinin  değerlerin tanımlama işlemi Değerler ekranında  ![ref6] butonu  ile manuel yada ![ref11] ve ![ref12] butonları ile kullanarak sisteme toplu olarak alan değerleri toplu aktarım işlemi  yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_59.png)

Giriş tipi olarak veri girişi seçilen alanların tanımlanması yukarıdaki gibi gerçekleştirilir. Puanlı liste tipli alanlar ve değerlerinin tanımlama işlemi bu şekilde yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_60.png)

Giriş tipleri hesaplanan (risk değeri gibi) olacak alanlar ise formülleri ile birlikte tanımlanır.

**Risk Değeri  Metin tipli Parametik Alan Tanımlama İşlemi:** Elle yazım imkanı veren metin kutucuğu ekleyen parametrik alan tipidir.

Fomüle bağlı olarak tanımlanan bir alandır.Bu alanın tanımlama işleminde Giriş Tipi alanında Hesaplanan seçeneği seçilir.Formül Tipi seçeneklerinde Excel ve SQL seçeneklerinde Excel seçilir.(Excel ve SQL seçeneklerinde bağlı olarak tanımlanan Formül alanlarında Bimser Destek ekibinde yardım alınma işlemi yapılır. )

Risk Değeri  metin tipli parametrik alanın tanımlama işleminde ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_61.png) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_62.png)

Alan Tanımlama-Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_63.png)

**Açılan ekranda ilgili alanlar tanımlanır;**

**Alan Kodu:** Alan Tanımlama-Yeni Kayıt ekranında Alan Kodu bilgisinin girildiği zorunlu alandır. Daha önce tanımlamış alanlarla aynı olmayacak şekilde boşluk, Türkçe karakter gibi karakterler kullanmadan tanımlanmalıdır. Ör. ‘001’ , ‘RK’

**Alan Adı:** Alan Tanımlama-Yeni Kayıt ekranında Alan Adı bilgisinin girildiği alandır. 

**Başlık Notu:** Alan Tanımlama-Yeni Kayıt ekranında alanı veri girişinin yapılması ile ilgili  açıklayacı bilgi içeren not bilgisinin girildiği alandır. Mouse ile alanın üzerine gelindiğinde görüntülenen bilgidir.

**Giriş Tipi:** Alan Tanımlama-Yeni Kayıt ekranında giriş tipinin Hesaplanan veya Veri Girişi tipi bilgisinin seçilebildiği alandır. Giriş Tipi seçeneği oluşturulan alanın manuel olarak veri girişi ile mi yoksa hesaplama yöntemi ile mi belirleneceğini gösterir. Örneğin; Hesaplanan seçilir.

**Formül Tipi:** Alan Tipi -Yeni Kayıt ekranında giriş tipi Hesaplanan seçeneği seçildiğinde görüntülenen alandır. Formül Tipi alanında tanımlanan alanın formülü yazılır. 

**Formül :** ([Y01]\*[Y02]\*[Y03]) formül alan kodlarının köşeli parantez içerisinde yazılarak çarpım işlemi şeklinde yazılır. Bu işlemde Alan Tanımlama menüsünde Olasılık, Frekans ve Şiddet puanlı liste tipli alanlarının köşeli parantez içerisinde  alan kodu yazılarak çarpımı şeklinde tanımlanarak yazılır.

**Alan Tipi:** Alan Tanımlama-Yeni Kayıt ekranında alan tipinin bilgisinin seçilebildiği alandır. Alan Tipi ise oluşturulan alanın metin, numerik, tarih, liste vb. tiplerinden hangisi olduğunu gösterir. Formül Tipli alanların tanımlama işleminde nümerik veya metin tipli alan seçim işlemi yapılır. Ör:Metin alan tipi seçilir.

**Görünme Şartı:** Alan Tanımlama-Yeni Kayıt ekranında Görünme Şartı bilgisinin girildiği alandır. Bir alan eğer başka bir alanın şartına bağlı olarak görülecekse görünme şartı kullanılır. Liste tipli alanın değerlerine göre oluşturulan alanın görüntülenmesini sağlar. Kullanımı [ALANKODU]=ALAN\_DEĞERİ vb. şekildedir. (Örneğin, Fırsat var mı? Alanının  alan kodu 01; Fırsat alanının alan kodu 02 olsun. Eğer “Fırsat” Alanının, “Fırsat var mı?” Alanındaki seçeneklerden değer kodu 100 olan “Evet” değeri seçili ise görülmesi gerekiyorsa 02 numaraları “Fırsat” alanının görünme şartı bölümüne formül şu şekilde yazılmalıdır: [01]=100)

**Durum:** Alan Tanımlama-Yeni Kayıt ekranında durumun “Aktif” veya “Pasif” olarak bilgisinin seçilebildiği alandır. 

**Genişlik:** Alan Tanımlama-Yeni Kayıt ekranında genişlik bilgisinin girildiği alandır.

Açılan Alan Tanımlama-Yeni Kayıt alan kodu ve alan adı bilgisi girilir. Giriş Tipi ve Alan Tipi seçilir. Giriş Tipi Hesaplanan olarak seçilerek Formül tipi alanında alan kodlarına bağlı olarak oluşturulan formül yazılır.Durum kısmı seçilir. Alan Tanımlama ekranında gerekli alanlar doldurulduktan sonra sol üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_64.png) butonuna tıklanarak Formül içerikli alanın tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_65.png)

Formül girişleri ilgili alanların tanımlama ekranlarında gerçekleştirilir. Örnek olarak bir formül aşağıdaki gibi analiz edilebilir.

([Y01]\*[Y02]\*[Y03]) şeklinde yazılan bir alanda köşeli parantez içinde yazılan ifade alan kodlarını temsil etmektedir. Bu ifadeler alan tanımlama ekranında alanları tanımlarken kullanıcı tarafından belirlenir. 

Risk Değeri alanı için, Y01; Olasılık alanı için, Y02; Frekans alanı için,  Y03;Şiddet alanı için, olarak kodlama yapılmış olduğu için formül, ([Y01]\*[Y02]\*[Y03]) şeklinde olacaktır. Bu formülün sonucu olarak Risk Değeri Alanı, Olasılık, Frekans ve Şiddet alanında seçilen değerlerin çarpımı olmak üzere sistem tarafından otomatik olarak hesaplanacaktır. Hesaplanan alanlarda bir diğer formül kullanımı ise IF fonksiyonu ile olmaktadır. IF Fonksiyonunun liste tipli alanlar için kullanılabilmesi için öncelikle ilgili alana değer tanımlanması gereklidir.

**Risk Seviyesi Liste Tipli Parametrik Alan Tanımlama:** Birden fazla element arasından tek seçim yaptıran parametrik alan tipidir. Tanımlanan liste tipli parametrik alanın liste değerlerinde seçim yapılır.Son olarak Risk Seviyesi liste tipli alanın tanımlama işlemi yapılır. 

Alan Tanımlama ekranına yeni bir alan eklemek için ekranın sol üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_66.png)butonu tıklanarak Alan Tanımlama\ Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_67.png)

Alan Tanımlama-Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_68.png)

Risk Seviyesi  alanın formül alanı ile ilgili formül yerine “.” işareti konularak  tanımlanılır. Liste değerlerine bağlı olarak yazılacak formül için Risk Seviyesi  tanımlama işlemi yapıldıktan sonra alan güncellenerek formül alanı yazılır. Risk Seviyesi  alanının değerleri tanımlanır. Alan tanımlama ekranında ilgili alanda renk kutucuğu işaretlendiyse değerler ekranında bu değerin hangi rengi temsil ettiği seçilmelidir. Bu renklendirmeler Entegre Yönetim Sistemi kısmı altında risk detaylarını görüntülendiğinde ilgili riskin hangi aralıkta yer aldığını kullanıcılara görsel olarak sunmaktadır. Buradaki renklendirmelerin risk prosedüründeki renklerle uyumlu olmasına dikkat edilmelidir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_69.png)

Alan Tanımlama ekranında Risk Seviyesi liste tipli alan seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_70.png) butonu tıklanarak alanın değerlerinin tanımlama işlemi Olasılık alanın değerlerinin tanımlama işlemin yapıldığı gibi tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_71.png)

Açılan Değerler - Risk Seviyesi  ekranın yeni bir Değer tanımlama işlemi için ![ref13]butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_73.png)

Değerler -Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_74.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Tanım:** Değerler-Yeni Kayıt ekranında tanımlanan değerin tanım bilgisinin yazıldığı alandır.   	

**Açıklama:** Değerler-Yeni Kayıt ekranında tanımlanan değerin varsa açıklama bilgisinin yazıldığı alandır.  	

**Durum:** Değerler-Yeni Kayıt ekranında tanımlanan değerin durum bilgisinin açılır liste tıklanarak açılan seçeneklerden “Aktif” seçeneğinin seçildiği alandır.   	

**Renk:** Değerler-Yeni Kayıt ekranında tanımlanan değerin açılır liste tıklanarak açılan renk seçeneklerinden seçildiği alandır. 	

**Varsayılan:** Değerler-Yeni Kayıt ekranında tanımlanan değerin varsayılan olarak gelmesi için ilgili alanla ilgili  check box işaretlendiği alandır. Varsayılan alanı ile ilgili check box işaretlendiğinde alanın değeri alanda sistem tarafında otomatik olarak getirilir. 	

**Önlem Zorunlu mu?:** Değerler-Yeni Kayıt ekranında tanımlanan değer ilgili önlem alınması istenirse ilgili check box işaretlendiği alandır. İlgili check box işaretlendiğinde alanın değeri seçildiğinde sistem bu değer için önlem alınmasını zorunluğu getirir. Risk kaydı kayıt işleminde önlem alınmadığında sistem tarafından önlem alınması ile ilgili uyarı mesajı gelir.   	

**Alınacak Önlem Zorunlu mu?:** Değerler-Yeni Kayıt ekranında Değerler-Yeni Kayıt ekranında tanımlanan değer ilgili alınacak önlem alınması istenirse ilgili check box işaretlendiği alandır. İlgili check box işaretlendiğinde alanın değeri seçildiğinde sistem bu değer için alınacak önlem alınmasını zorunluğu getirir. Risk kaydı kayıt işleminde alınacak önlem alınmadığında sistem tarafından alınacak önlem alınması ile ilgili uyarı mesajı gelir.İSG Risk Değerlendirme Modülü parametrelerinde 133 numaralı “Alınacak Önlemler Kullanılacak mı?” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_75.png)

Parametre aktif edildikten sonra Değerler -Yeni Kayıt ekranında bu alan görüntülenir.

Gerekli alanlar ilgili bilgiler girildikten sonra ekranın sol üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_76.png) butonu tıklanarak alanın değeri kayıt işlemi yapılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_77.png)

Ayn şekilde Risk Seviyesinin değerleri![ref13] butonu tıklanarak manuel yada aktarım şablonu indirilip, indirilen şablon doldurularak sisteme yükleme işlemi yapılarak tüm değerlerin tanımlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_78.png)

İlgili alan değerleri tanımlandıktan sonra formül girişi yapılır. Formül girişi için alan tanımlama ekranındayken ilgili alanın üzerine tıklanır ve ![ref14] butonu ile alan detaylarına girilir. Bu alanda formül girişi gerçekleştirirken daha önce belirtildiği üzere alan kodlarının köşeli parantez olarak yazılması gereklidir. Formül, bazı ifadelerin farklı olması haricinde (noktalı virgül, virgül vb.) Excel’de kullanılan IF fonksiyonu ile aynı mantıkta yazılmalıdır. Formül kullanımı: IF([ALANKODU]KoşulŞartı; Doğru ise Değer Kodu; Yanlışsa Değer Kodu şeklindedir. Örneğin:

**Formül :** IF([R09]<2;4192; IF(AND([R09]\>=2;[R09]<8);4191;4190))

Aşağıdaki ekran görüntüsünde örneği verilen formül açılırsa şu şekilde bir analiz gerçekleştirilebilir.Liste değerlerine bağlı  olarak formül tanımlanır.Aşağıdaki ekran görüntüsünde örneği verilen formül açılırsa şu şekilde bir analiz gerçekleştirilebilir.







|Formül Satırı|Satır Anlamı|
| - | - |
|IF([Y04]\>=400;4981|Y04 alanı 400’den büyük eşitse Risk Seviyesi alanının 4981 numaralı değeri (Tolerans gösterilemez risk), değilse..|
|IF(AND([Y04]<400;[Y04]\>=200);4980|..Y04 alanı 400’den küçük ve 200’den büyük eşitse Risk Seviyesi alanının 4980 numaralı değeri (Esaslı Risk), değilse…|
|IF(AND([Y04]<200;[Y04]\>=70);4979|..Y04 alanı 200’den küçük ve 70’den büyük eşitse Risk Seviyesi alanının 4979 numaralı değeri (Önemli Risk), değilse…|
|IF(AND([Y04]<70;[Y04]\>=20);4978;4977))))|..Y04 alanı 200’den küçük ve 70’den büyük eşitse Risk Seviyesi alanının 4978 numaralı değeri (Olası Risk), değilse Risk Seviyesi alanının 4977 numaralı değeri (Önemsiz Risk)|

Formül bir bütün olarak yazılırsa aşağıdaki şekilde olacaktır. Ekran görüntüsünde olduğu üzere 4977  numaralı değer formüle bir şart olarak eklenebileceği gibi son şart zaten bu değer olduğu için noktalı virgülden sonra bu değerin yazılması da formülü tamamlamaya yetecektir. IF sayısı kadar parantez kapatılarak formül tamamlanır. 

IF([Y04]\>=400;4981;IF(AND([Y04]<400;[Y04]\>=200);4980;IF(AND([Y04]<200;[Y04]\>=70);4979;IF(AND([Y04]<70;[Y04]\>=20);4978;4977))))

Alan Tanımlama ekranında Risk Seviyesi  alanı seçilir ve ![ref14] butonu tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_80.png)

Açılan Alan Tanımlama - Kayıt Güncelle ekranında Formül alanına oluşturulan formül bilgisi yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_81.png)

Gerekli alanlar ilgili bilgiler girildikten sonra ekranın sol üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_82.png)butonu tıklanarak kayıt güncelleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_83.png)

Alan Tanımlamada tüm alanlar tanımlandıktan sonra Fonksiyon Dizanyer menüsünde 22 numaralı “Statü kullanılacak mı?”  parametresine bağlı olarak görüntülenen ![ref15]ve ![ref16] butonları kullanılarak statü , butonların tanımlama işlemi yapılır. Statü ve buton tanımlama işleminde sonra ![ref17] butonu tıklanarak  alanların Fonksiyon Dizanyer menüsünde tanımlı fonksiyonların ilgili sayfalarıyla ilişkilendirilme işlemi yapılır. Bu işlemlerin yapılmasında onay akışı kurgusunun Akış Tanımlama  menüsünde tanımlanıp  ve Alt Modül Tanımlama menüsünde ise  akışların  kontrolün yapılması gerekmektedir.

Sistemde mevcut bulunan alan tiplerinin tam listesi aşağıda belirtilmiştir; 

- **Metin:** Elle yazım imkanı veren metin kutucuğu ekler.
- **Metin Çok Satırlı:** Elle yazım imkanı veren karakter sınırı olmayan çok satırlı metin kutucuğu ekler.
- **Nümerik:** Sayısal olarak veri girişi yaptırır.
- **Nümerik-Parasal:** Parasal değer olarak nümerik giriş yaptırır.
- **Nümerik-Birim:** Birim olarak nümerik giriş yaptırır.
- **Tarih:** Takvim alanı ekler.
- **Liste:** Birden fazla element arasından tek seçim yaptırır.
- **Puanlı Liste:** Açılır menüden seçim yaptırır, liste elementlerinin puan değerleri mevcuttur.
- **Arama Özellikli Liste:** Birden fazla element arasından geniş arama fonksiyonuyla arama yapabilecek şekilde, tekli ve/ veya çoklu seçim yapılmasını sağlar.
- **Ağaç Liste:** Ağaç kırılımına sahip birden fazla element arasından geniş arama fonksiyonuyla arama yapabilecek şekilde seçim yapılmasını sağlar.
- **Personel:** QDMS personel veri tabanından kişi seçilebilmesini sağlar.
- **Departman:** QDMS departman veri tabanından departman bilgisi seçilebilmesini sağlar.
- **Unvan:** QDMS unvan veri tabanından unvan bilgisi seçilebilmesini sağlar.
- **Doküman:** QDMS doküman veri tabanından doküman seçilebilmesini sağlar.
- **Yönetim Sistemi:** QDMS yönetim sistemi veri tabanından yönetim sistemi bilgisi seçilebilmesini sağlar.
- **Müşteri:** QDMS müşteri veri tabanından müşteri bilgisi seçilebilmesini sağlar.
- **Tedarikçi:** QDMS tedarikçi veri tabanından tedarikçi bilgisi seçilebilmesini sağlar.
- **Ürün:** QDMS ürün veri tabanından ürün bilgisinin seçilebilmesini sağlar.
- **Şirket Profili:** QDMS şirket profili veri tabanından şirket profili bilgisi seçilebilmesini sağlar.
- **Başlık:** Formlara koyu harflerle yazılacak başlık alanı ekler.
- **Dosya:** Dosya eklemesi için uygun alan getirecektir 
- **Resim:** Resim eklemesi için uygun alan getirecektir
- **Resim Liste:** Resim listesinden seçim sağlar.
- **Çoklu Resim:** Çoklu resim seçilmesini sağlar.
- **Tablo:** Tablo tipli alan oluşturulmasını sağlar.  (Bu tip bir alan eklendikten sonra alan değerleri olarak yeni alan tanımlamalarının yapılması gereklidir.)
- **Sorgu:** QDMS/Ensemble veri tabanları içerisindeki ana verilerden seçim yapılabilmesi için tanımlanabilen alan türüdür. (Sadece Bimser Destek Ekibi tarafından tanımlanmalıdır) Tekli ve çoklu seçim yapılabilir.
- **Sorgu Ağaç:** QDMS/Ensemble veri tabanları içerisindeki ağaç kırılımlı ana verilerden seçim yapılabilmesi için tanımlanabilen alan türüdür. (Sadece Bimser Destek Ekibi tarafından tanımlanmalıdır) Tekli ve çoklu seçim yapılabilir.
- **Sekme:** Mevcut risk değerlendirme formunda alanların bulunduğu sekmenin haricinde alanların ilişki kurularak içerisinde görülebileceği yeni bir sekme oluşturur.
- **Onay Kutusu Liste:** Talebe göre tekli veya çoklu seçim yaptırılacak tipte bir liste tipli alandır.
- **Risk:** Risk tabanlı modüllerden değerlerin seçilebilmesini sağlar. Bu tip bir alan eklendikten sonra hangi modülden değerlerin geleceği alan tanımlama ekranında seçilmesi gereklidir..
- **Açıklamalı Liste:** Seçilen liste değerinin yanına açıklama yazabilme imkanı sağlayan alan tipidir. Alan Tanımlama menüsünde alan değerleri tanımlanırken her değer için açıklama kutucuğunun aktif olup olmayacağının seçilmesi gerekir. Burada yapılan seçime göre Entegre Yönetim Sistemi menüsü altında bu alanın görüleceği menüde ilgili seçim yapıldığında alan değerinin yanına kullanıcının açıklama yazabilmesi için kutucuk açılmış olur.
- **Pozisyon:** QDMS pozisyon veri tabanından pozisyon bilgisi seçilebilmesini sağlar.
- **Saat:** Saat tipli alan ekler.

### **6.1.3.Fonksiyon Dizayner**
**Menü Adı:** Sistem Altyapı Tanımları/İSG Risk Değerlendirme/ Fonksiyon Dizayner

Fonksiyon Dizayner menüsü ile alan havuzuna eklenen alanlar risk modüllerinin istenilen sayfaları ile ilişkilendirilebilir. Bunun için Sistem Altyapı Tanımları/ İSG Risk Değerlendirme Modülünün altından Fonksiyon Dizayner menüsüne gelinir. Açılan ekranda risk modülünün alan eklenebilecek fonksiyonları sıralanacaktır. Bu ekranda Faaliyet Grubu Tanımlama, Faaliyet Tanımlama, Risk Değerlendirme Form Tanımlama, Risk Değerlendirme Detay, Önlem Tanımlama ve Kontrol Tanımlama fonksiyonlarında kullanılacak alanlar ve bunların sıralaması ile onay işlemlerindeki hiyerarşi detayı tanımlanır. Bu menüde kullanılacak butonlar İSG Risk Değerlendirme modülü parametrelerinden 22 numaralı  “Statü kullanılsın mı?” parametresinin parametre değeri “Evet” seçilerek parametrenin aktif edilmesi bağlı olarak butonlar değişir. Bu parametrenin parametre değeri “Evet” seçilerek parametre aktif edildiğinde ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_87.png) ve ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_88.png) butonların menüde gözükür. Ancak 22 numaralı parametrenin  parametre değeri “Hayır” seçilerek parametre pasif olduğu durumlarda sadece ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_89.png)butonu görünür durumda olur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_90.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref18]: Statü tanımlaama işlemi yapılır.

![ref19]: Buton tanımlama işlemi yapılır.

![ref20] : Alanların ilgili fonksiyon ile ilişkilendirilme işlemi yapılır.

Fonksiyon Dizayn ekranında 4. Numaralı “Risk Değerlendirme Detayı” fonksiyonu seçili iken  ![ref20] butonuna tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_94.png)

Alanların ilgili fonksiyonla ilişkilendirilme yapılacağı ekran açılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_95.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref21]:Listede seçili fonksiyona yeni bir alan eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_97.png):Listede seçili eklenen fonksiyona eklenen alan bilgisi üzerinde değişiklik ve düzenleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_98.png):Listede seçili eklenen fonksiyona eklenen alan bilgisi silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_99.png) :Önceki ekrana geri dönülür.

Fonksiyon Dizayn - Alanlar - Risk Değerlendirme Detay ekranında ![ref21] botunu tıklanarak  Alan Tanımlama -Fonksiyonlar -Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_100.png) ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_101.png) 
**Açılan ekranda ilgili alanlar tanımlanır:** 

**Alan Adı:** Alan Tanımlama - Fonksiyonlar - Yeni Kayıt ekranında tanımlanmış alanlardan alan seçimi yapıldığı alandır.

**Mesajı:** Alan Tanımlama - Fonksiyonlar - Yeni Kayıt ekranında zorunlu alan doldurulmadığında verilecek uyarı mesajı bilgisi yazıldığı alandır.

**Sıra No:** Alan Tanımlama - Fonksiyonlar - Yeni Kayıt ekranında alanın sıra no belirlenlendiği alandır.

**Varsayılan Rol:** Alan Tanımlama - Fonksiyonlar - Yeni Kayıt ekranında ilgili alanın değeri daha önce tanımlanmış bir üst formdan ya da kaydı giren kişinin adı soyadı, pozisyonu, unvanı, departmanı, iş yeri gibi verileri ise bunlar için tanımlanmış rol seçilebilir. Örneğin, Risk detay formunda risk girişini yapanın departmanı adında bir alanda sisteme kaydı giren kullanıcının departmanı gelmesi gerekiyor varsayılan rol kullanılabilir. Kullanılmadığı durumda kullanıcı kendi departmanını hem yanlış seçebilir hem de kaydı giren kullanıcı fazladan bir işlem yapmış olur. Burada seçilen varsayılan rol sayesinde, kullanıcı risk girişi yapmaya başladığında departmanı otomatik gelecektir.  

**Varsayılan Değer Değiştirilmesin:** Alan Tanımlama - Fonksiyonlar - Yeni Kayıt ekranında seçilen alan varsayılan olarak bir değer getiriyorsa getirdiği değerin değiştirmemesini sağlandığı alandır.

**Gridde göster:** Alan Tanımlama - Fonksiyonlar - Yeni Kayıt ekranında alanın gridde gösterilmesi gerekiyorsa ilgili check box işaretlendiği alandır.. 

**Seçimde göster:** Alan Tanımlama - Fonksiyonlar - Yeni Kayıt ekranında diğer risk ya da olay modüllerinden ilişki kurulması gerekli olduğu durumlarda alan tanımlama menüsünde risk tipli bir alan tanımlanabilir. Bunun sonucunda ilgili form ilişkisi kurulduğu takdirde risk sekmesi oluşacaktır. Bu sekmede ekle butonuna basıldığında ilişki kurulması gereken modüldeki risklerin /olayların listesi gelecektir. Gelen listenin sütunlarında hangi alanların gözükmesi gerekiyorsa o alanlar için ilgili modülde seçimde göster check box’ı işaretlenmelidir. (Tablo, dosya, resim vb. tipli metinsel ifadenin dışında olan alanlar seçilmemelidir).

**Satır Sayısı:** Alan Tanımlama - Fonksiyonlar - Yeni Kayıt ekranında ilgili alan çoklu satır ise, veri girişi ekranında kaç satır gözükmesi gerektiği belirlendiği alandır.

**Kolon Genişliği:** Alan Tanımlama - Fonksiyonlar - Yeni Kayıt ekranında ilgili modülde girilen kayıtların listesinde (gridde) alanın kolon genişliği bilgisinin belirlenir. Verinin uzun olduğu alanlar için ort. 250, sadece rakam girilen alanlar için ise 75 kullanılması idealdir. Alana girilecek veriler düşünülerek bu aralıklarda bir değer kullanmak uygun olacaktır.

**Aktif Statü:** Alan Tanımlama - Fonksiyonlar - Yeni Kayıt ekranında alanın sisteme tanımlanan statülerin hangilerinde aktif olacağını belirlendiği alandır. Bu alanda işaretlenen statülerde ilgili alanın tipine göre işlem gerçekleştirilebilir.

**Görünür Statü:** Alan Tanımlama - Fonksiyonlar - Yeni Kayıt ekranında alanın sisteme tanımlanan statülerin hangilerinde görüleceğini belirlendiği alandır. Aktif statüsü seçilen alanlar için aynı zamanda görünür statüde en az aktif statü alanında işaretlenen statüler olacak şekilde belirlenmelidir.

**Zorunlu Statü:** Alan Tanımlama - Fonksiyonlar - Yeni Kayıt ekranında alanın sisteme tanımlanan statülerin hangilerinde zorunlu olacağını belirlendiği alandır. 

Açılan ekranda alan bilgileri listeden seçilir, zorunlu bir alan ise kullanıcının bu alanı doldurmadığında çıkacak mesaj tanımlanır, sıra numarası belirlenir. Aktif statü, Görünür Statü ve Zorunlu Statü durumları seçilir. Zorunlu olup olmadığı, gridde gösterilip gösterilmeyeceği, kolon genişliği belirlenerek gerekli tüm alanlar doldurulduktan sonra ekranın sol üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_102.png) butonu tıklanarak, ilgili alan için fonksiyon ile ilişkilendirme işlemi gerçekleştirilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_103.png)

Alan Tanımlamada tanımlanıp alan havuzuna eklenen tüm alanların ilgili fonksiyonun sayfaları ile ilişkilendirileme işlemi bu şekilde yapılarak tanımlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_104.png)

Fonksiyon Dizayn - Alanlar - Risk Değerlendirme Detay ekranında ![ref21] butonu tıklanarak açılan ekranda alan havuza eklenen alanların ilgili fonksiyonla ilişkilendirilme işlemi aşamasında Aktif, Gönür ve Zorunlu statülerin seçim işlemi yapılır. Bu statülerin bu ekran dışında başka bir ekranda seçim işlemi yapılır.  Fonksiyon Dizanyer menüsünde ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_105.png) botonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_106.png)

Statü Tanımlama - Risk Değerlendirme Detay ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_107.png)

Açılan Statü Tanımlama - Risk Değerlendirme Detay ekranında ![ref17] butonu tıklanarak Fonksiyon Dizanyer menüsünde ilgili fonksiyonla ilişkilendirilmiş alanların  Aktif, Görünür ve Zorunlu statüleri ilgili check box işaretlenerek belirlenir. Örn: Taslak statüsünde alanları Aktif, Görünür ve Zorunlu statüleri ilgili check box işaretlenerek belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_108.png)

Statü Tanımlama-Risk Değerlendirme Detay-Taslak aşamasında Aktif, Görünür ve Zorunlu statüleri belirlendikten sonra ekranın sol üst köşesindeki ![ref22] butonu tıklanılır.Tüm Statüler içinde aynı işlem aşaması yapılarak alanların  Aktif,Görünür ve Zorunlu stüleri belirlenir.
### **6.1.4.Risk Dağılım Matrisi Tanımlama**
**Menü Adı:** Sistem Altyapı Tanımları/İSG Risk Değerlendirme/ Risk Dağılım Matrisi Tanımlama

Risk dağılım matrisi tanımlama işleminin gerçekleştiği menüdür. Risk dağılım matrisi tanımlamadaki amaç, belirlenen parametrelere göre risk dağılımın hangi aralıklarda daha yoğun olduğunu tespit etmektir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_110.png)

**Ekranındaki bulunan butonlar yardımıyla;**

![ref23]: Yeni bir risk dağılım matrisi tanımlar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_112.png):Listede seçili risk dağılım matrisi bilgisi üzerinde değişiklik ve güncelleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_113.png): Listede seçili risk dağılım matrisi bilgisi silinir.

![ref24]: Risk dağılım matrisini renklendirir.

Listeye yeni bir risk dağılım matrisi eklemek için ekranın sağ üst köşesindeki ![ref23]butonu tıklanarak Risk Dağılım Matrisi Tanımlama\Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_115.png) ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_116.png)

Açılan ekranda “Grafik Adı” belirlenir. X ve Y eksenindeki parametreler için risk karşılaştırmasında kullanılacak alanlar belirlenir. Bu alanların alan tanımlama menüsündeki formülleri “X Formülü” ve “Y Formülü” kısımlarına yazılır. “X Aralıkları” ve “Y Aralıkları” kısımlarına ise alanların değerleri girilir. İşlemler tamamlandıktan sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_117.png)butonu tıklanarak kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_118.png)

Risk Dağılım Matrisini kullanılan yönteme uygun olarak renklendirmek için risk dağılım matrisi tanımlama ekranındaki sol üst köşede bulunan  ![ref24] butonuyla oluşturulan matris açılır. Ekrandaki her kutucuğun üzerine tıklanarak kutucuklar renklendirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_119.png)
### **6.1.5.Alan Menüsü Tanımlama**
**Menü Adı**: Sistem Altyapı Tanımları/İSG Risk Değerlendirme/ Alan Menüsü Tanımlama

Liste tipli alanlara değer eklenmesi için Entegre Yönetim Sistemi altında menü oluşturulmasını sağlayan menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_120.png) **Ekrandaki bulunan butonlar yardımıyla;**

![ref25]: Yeni bir menü tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_122.png):Listede seçili menü bilgisi üzerinde düzenleme ve güncelleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_123.png):Listede seçili menü bilgisi silinir.

Listeye yeni bir menü eklemek için ekranın sol üst köşesindeki ![ref25] butonu tıklanarak Menü Tanımlama\ Yeni Kayıt ekranı görüntülenir

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_124.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Menü Adı:** Menü adı bilgisi tanımlanır.

**Alan:** Alan bilgisi açılır liste tıklanarak açılan alan listesinde seçilir.

**Sıra No:** Sıra no bilgisi girilir.

Menü tanımlama ekranında gerekli alanlar doldurulduktan sonra sol üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_125.png) butonu tıklanarak menü tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_126.png)

Menü tanımlaması yapıldıktan sonra İSG Risk Değerlendirme modülün  Entegre Yönetim Sistemi kısmında menü olarak görüntülenmesi için Sistem Altyapı Tanımları /BSAT/Tanımlar/Yetki Grupları Tanımlama menüsünde menü görme yetkisi verilmelidir.

Yetki Grupları Tanımlama ekranında Yetki Grubu seçili iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_127.png) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_128.png)

Açılan QDMS Yönetim Sistemi - Kayıt Güncelle ekranında Menü seçilir. Menü seçildikten sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_129.png) butonu tıklanarak menü görme ekranda geçilmesi sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_130.png)

Açılan ekranda ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_131.png)butonu tıklandıktan sonra menü görme yetkisinin verilmesi için ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_132.png)butonu tıklanarak menü görme yetkisi kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_133.png)

Qdms logosu tıklanarak yenile işlemi yapılarak menü görme yetkisi verilen liste tipli alanın menü olarak görüntülenmesi için İSG Risk Değerlendirme Modülü Entegre Yönetim Sistemi kısmı tıklanarak  görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_134.png)

Entegre Yönetim Sistemi/İSG Güvenliği Risk Değerlendirme/Risk Seviyesi  menüsü tıklanılır. Değerler-Risk Seviyesi menüsünde  açılır.Açılan menüde liste tipli parametrik alanın tanımlanmış liste değerleri görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_135.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref6]:Yeni bir değer tanımlanır

![ref7]: Listede seçili değer bilgisi üzerinde düzeltme veya güncelleme işlemleri yapılır.

![ref8]: Listede seçili değer bilgisinin silinme işlemi yapılır.

![ref9]: Kayıtlar filtrelenerek arama yapılabilir.

![ref10] : Veriler Excel’ e aktarılabilir.

![ref11]: Şablon indirilir.

![ref12]: Şablon yüklenilir.

Not: ![ref11] ve ![ref12] butonları ile sisteme toplu olarak alan değerleri aktarılabilmektedir. Şablon indirme butonu ile sistemdeki şablon kullanıcının bilgisayarına indirilir. İlgili şablon kullanıcılar tarafından doldurularak şablon yükleme butonu ile sisteme yüklendiğinde şablondaki tüm alan değerleri sisteme aktarılmış olacaktır.Değerler- Risk Seviyesi  ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_136.png) butonu tıklanarak manuel değer tanımlama yada toplu aktarın butonları kullanılarak değerlerin  toplu aktarım işlemi yapılır. Bu şekilde liste tipli alanların bu Alan menüsünde menüsü tanımlanır. Tanımlanan menüde yeni değer tanımlama işlemi sağlanılır.

### **6.2.6. İSG Risk Değerlendirme Parametreleri**
**Menü Adı**: Sistem Altyapı Tanımları/İSG Risk Değerlendirme /İSG Risk Değerlendirme  Parametreleri

İSG Risk Değerlendirme Modülü için kullanıcıların istek ve ihtiyaçlarına göre çeşitli ayarlamalar yapabildiği ve bunlara göre parametreleri belirlediği (seçebildiği) menüdür. Filtre sekmesinde Modüller alanında İSG Risk Değerlendirme Modülü seçili olarak gelir ve Liste sekmesinde İSG Risk Değerlendirme Modülü parametreleri listelenir. Seçili parametre bilgisi üzerinden  değişiklik yapmak için ![ref26]butonu kullanılır. Filtre sekmesinde parametre no ve parametre tanımı arama kriterlerine göre filtreleme işlemi yapıldığı gibi liste sekmesinde ise gridde parametre no ve tanım alanlara göre de arama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_138.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref26]:Listede seçili parametre üzerinde değişiklik ve düzenleme işlemi yapılır.

![ref2]: Kayıtlar filtrelenerek arama yapılır.

![ref27]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref28]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref29]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip-gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Parametreler ekranında liste sekmesinde 11 numaralı parametreler seçili iken ![ref26] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_142.png)

Açılan parametreler ekranında “Sorumlu kullancı grupları üzerinden yetki kontrolü yapılacak mı? parametresinin parametre değeri bilgisi üzerinde değişiklik yapılır. İstenirse parametreler ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_143.png) butonu tıklanarak parametrenin parametre değeri ile ilgili varsayılan değeri bilgisinin gelmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_144.png)

Açılan Parametreler ekranında parametrenin parametre değeri “Evet” seçilerek gerekli alanlar ilgili bilgiler girildikten sonra ekranın sol üst köşesindeki ![ref30]butonu tıklanarak parametre kayıt güncelleme işlemi yapılır

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_146.png)

Parametreler ekranında ![ref26] butonu tıklanarak seçili pasif parametrenin parametre değeri “Evet”seçilerek parametreyi aktif etme, seçili aktif edilenen parametrenin parametre değeri “Hayır” seçilerek parametreyi pasif etme,  seçili parametrenin varsa parametre değeri değiştirme   ve seçili parametrenin varsayılan değeri seçme gibi işlemler yapılır.
### **6.2.7.E-Posta Ayarları**
**Menü Adı**: Sistem Altyapı Tanımları/ İSG Risk Değerlendirme/E-Posta Ayarları

İSG Risk Değerlendirme Modülü kapsamındaki mail bildirimlerinin yapıldığı menüdür. E-Posta Ayarları ekranında, “İSG Risk Değerlendirme” modülünde hangi aşamasında kimlere mail gönderiminin yapılacağı belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_147.png)

**Ekranda bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_148.png): Listede seçili olan  E-postaları  değeri bilgisi üzerinde düzenleme/değişiklik/güncelleme işlemi yapılır.

![ref31]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref32]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref33]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip-gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

**E- Posta Ayarlarında SMS  bildirimi kullanılacak ise;**

Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/ Parametreler menüsü tıklanılır. Açılan Parametreler ekranında listelenen Sistem Altyapı Tanımları  modülü parametrelerinde 102 numaralı “SMS bildirimi kullanıcak mı?” parametresinin parametreler ekranında Filtre sekmesinde parametre no alanına parametre numarası yazılarak ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_152.png)  butonu tıklanarak aratılarak seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_153.png)

Sistem Alyapı Tanımları modülü parametrelerinde 102 numaralı “SMS bildirimi kullanıcak mı?” parametresi seçildikten sonra ![ref34] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_155.png)

Açılan parametreler ekranında parametre değeri “Evet” seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_156.png)

Parametreler ekranında parametre değeri “Evet” seçildikten sonra ekranın sol üstte yer alan ![ref35]  butonu tıklanarak parametreyi aktif etme kayıt işlemi  yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_158.png)

Parametre Aktif edildikten sonra E- Posta Ayarları ekranında SMS bildirimi kullanılması ile ilgili “SMS gitsin mi?” alanı ile ilgili check box görüntülenir.  İlgili check box işaretlenerek E-Posta ayarlarında SMS bildirimi kullanılır.

Hangi basamakta e-posta/ mesaj gitmesi isteniyorsa seçilir ve  ![ref34] butonu tıklanılır. 

Örn:E-Posta Ayarları ekranında “İSG Müdür Onayı” basamağı seçilir ve ![ref36]  butonu tıklanılır.  

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_160.png)

Açılan E-Posta Ayarları/ İSG Müdür Onayı ekranı görüntülenir. Roller kısmı, e-posta ve mesaj bildiriminin gideceği rolü yani kişiyi göstermektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_161.png)

E-Posta Ayarları / İSG Müdür Onayı ekranında Rapor formatı alanında Rapor formatları Tanımlama menüsünde kayıt bazlı tanımlı raporları listesi açılır liste tıklanarak görüntülenir. Kullanıcılar bu görüntülenen kayıt bazlı rapor formatlı listesinde rapor seçim işlemi yaparak e- posta olarak rapor formatının gönderilme işlemi yapabilir.

E-Posta Ayarları / İSG Müdür Onayı ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_162.png)  butonu tıklanarak açılan sistemde tanımlı Mesaj Gövdesi listesinde  gönderilecek mesaj gövdesi ilgili listeden seçilir. Yanlış eklenen bir mesaj gövdesini silmek için ise ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_163.png)  butonu kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_164.png)

Mesaj Gövdesi listesinde mesaj gövdesi seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_165.png) butonu tıklanarak  mesaj gövdesinin içeriği detaylı bir şekilde görüntülenir.
# ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_166.png)
İlgili roller için gidecek mesaj gövdeleri mesaj gövdesi listesinde  mesaj gövdesi seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_167.png) butonu tıklanarak seçilme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_168.png)

Kime E-Posta gitmesi isteniyorsa, o rolle ilgili “E-Posta Gitsin Mi/ SMS Gitsin Mi” check box’ı işaretlenir.Mesaj gitmesi için rolde tanımlı olan kişinin cep telefon numarası personel tanımlama ekranında tanımlı olmalıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_169.png)

E-Posta Ayarları/ İSG Müdür Onayı ekranında E-Posta gitmesi  rollerle  ilgili “E-Posta Gitsin Mi/ SMS Gitsin Mi” check box ‘ı işaretlendikten sonra ekranın sol üstte köşede yer alan ![ref37]  butonu tıklanarak E- Posta Ayarları kayıt işlemi gerçekleştirilir.
### **6.1.8.Rapor Formatları**
**Menü Adı:** Sistem Altyapı Tanımları/İSG Risk Değerlendirme/ Rapor Formatları

İSG Risk Değerlendirme metotlarına göre farklı rapor formatları tanımlama işleminin yapıldığı menüdür. İSG Risk Değerlendirme Modülü için rapor formatları tüm kullanıcılar için  farklı kurgulandığı için sabit bir rapor şablonu bulunmuyor. Bu nedenle her rapor için ayrı rapor şablonu sıfırdan hazırlanıyor ve sisteme aktarılma işlemi yapılmaktadır. İSG Risk Modülünde  Rapor formatları şablonları tasarlama işleminde Sistem Altyapı Tanımları kısmında altyapısı kurgulanmaktadır. Altyapıda kurgulama işleminde Alan Tanımlama, Fonksiyon Dizanyer ve Rapor Formatları menüleri kullanılmaktadır. Alan Tanımlama menüsünde rapor formatında bulanan alanların tanımlama işlemi yapılır. Fonksiyon Dizanyer da tanımlan bu alanların 4 numaralı Risk Değerlendirme Detay fonksiyonu sayfalarında görüntülenmesi için ilişkisi kurulur. Fonksiyon Dizanyer menüsünde ise  ![ref38] butonu tıklanarak açılan ekranda alan kodların tagleri Rapor formatıda şablonda  alan değerleri kısmına eklenir. Tag ekleme işlemi yapılan Rapor formatı şablonu  sisteme yüklenir. Rapor formatı şablonun sisteme yükleme işlemi Sistem Altyapı Tanımları/BSAT/Konfigürasyon ayarları/Rapor Formatları Düzenleme menüsünde ![ref39] butonu ile yapılır. Sistem Altyapı Tanımları/ İSG Risk Değerlendirme /Rapor Formatları menüsü tıklanır. Açılan Rapor Formatları menüsünde ![ref39]butonu tıklanılır. Açılan Rapor Formatları ekranında ilgili alana Rapor Formatı şablonun adı yazılır.  Rapor Formatları Düzenleme menüsünde gidilerek sistem yüklenen Rapor formatı şablonu seçilerek adı ve uzantısı sağ tıkla/kopyala yönetimi ile kopyala işlemi yapıldıktan sonra Rapor Formatları ekranındaki Rapor şablonu alanına sağ tıkla/yapıştırma yönetimi ile ilgili alana yapıştır işlemi yapılır. Rapor formatları ekranında Rapor şablon formatı tanımladıktan sonra Rapor şablonu alanında istenilen seçeneğe göre rapor seçimi yapılarak ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_173.png) butonu tıklanarak Rapor formatı tanımlama işlemi gerçekleştirilir. Bu menüde Rapor şablonu seçenekleri olarak Form Bazında, Kayıt Bazında ve Genel olmak üzere üç seçeneğe göre rapor formatı alınma işlemi yapılır.Form ve Kayıt bazında tanımlanan rapor formatları Entegre Yönetim Sistemi/ İSG Risk Değerlendirme/Risk  Değerlendirme Formu Tanımlama / Detaylar menüsünde ilgili butonlar tıklanarak alınır. Kayıt bazında rapor formatı bu menüde ![ref40] butonu tıklanarak alınırken Form bazında rapor formatı ise ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_175.png) butonu tıklanarak alınmaktadır. Kayıt bazında rapor formatı alınırken rapor formatları menüsünde tanımlanırken “PDF olarak Oluştur” check box işaretlenirse rapor formatının PDF formatında alınma işlemide yapılır. İlgili check box işaretli olmadığında kayıt bazında rapor formatı Excel formatında alınır. Genel bazda tanımlanan rapor formatları ise Entegre Yönetim Sistemi/ İSG Risk Değerlendirme/Raporlar/Genel Risk Listesi menüsünde ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_176.png) butonu tıklanarak tanımlanan rapor formatı seçilerek alınır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_177.png) 

**Ekrandaki bulunan butonlar yardımıyla;** 

![ref3]: Yeni bir rapor formatı tanımlanır.

![ref4]: Listede seçili rapor formatı bilgisi üzerinde değişiklik ve güncelleme işlemi yapılır.

![ref5]: Listede seçili rapor formatı bilgisi silinir.

**Kayıt Bazında Rapor Formatı Tanımlama;**

Entegre Yönetim Sistem/ İSG Risk Değerlendirme/Risk  Değerlendirme Formu Tanımlama / Detaylar menüsünde ![ref40] butonuna basılarak alınan rapor adımları takip ederek rapor şablonu oluşturulabilir. İlk olarak yeni bir Excel dosyası oluşturulur. Dosyanın adına bir isim verilir. İsim verilirken dikkat edilmesi kısım dosya adında boşluk karakterinin olmamasıdır. Örneğin dosya adının " ISG Rapor Formatı Şablonu (Kayıt Bazında).xlsx "  olduğu gibi.

Sistemde tanımlı olan sabit alanlar için dokümanda yer alan  "sabit tagler.txt" dosyasını kontrol edilir. Sistem Altyapı Tanımları/ İSG Risk Değerlendirme/ Alan Tanımlama menüsünde tanımlanan parametrik alanları rapora basabilmek için ise; Sistem Altyapı Tanımları / İSG Risk Değerlendirme/Fonksiyon Dizayner menüsüne gelerek 4 numaralı fonksiyon olan Risk Değerlendirme Detay fonksiyonu seçilir. Risk Değerlendirme Detay fonksiyonu seçili iken sol üstte yer alan ![ref38]butona tıklanır. Açılan ekranda "Risk Tanımı" adında bir alanınız olduğunu ve bu alan için "Alan Kodu" alanında ALAN5 ise bu durumda "Risk Tanımı" alanını rapora basabilmek için kullanmanız gereken tag  <ALAN5\> şeklinde olacaktır. Eğer rapora eklemek istediğiniz alan liste tipli bir alanda ise, <ALANKODU\_ACK\> şeklinde bir tag kullanmanız gerekiyor. Alanlar tümü “ACK” eki eklenemeyecek ise  <ALANKODU\> şeklinde olur. Kullanılan tag’ların başında ve sonunda herhangi bir boşluk karakteri olmamasına dikkat edilmemesi gerekmektedir. Tüm taglerin bilgisi rapor formatı şablona aşağıdaki formda olduğu gibi yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_178.png)

Rapor şablonunuzu bu bilgiler doğrultusunda hazırladıktan sonra Sistem Altyapı Tanımları/ BSAT/Konfigürasyon Ayarları/ Rapor Formatları Düzenleme menüsünde ![ref39]butonu tıklanarak rapor formatının sisteme aktarma işlemi yapılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_179.png)

Dosya Yükle ekranında Gözat butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_180.png)

Açılan ekranda Rapor formatı şablonu seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_181.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_182.png)

Sisteme aktarılan rapor formatı Rapor Formatları Düzenleme menüsünde seçilir. Seçilen Rapor Formatı uzantısıyla birlikte sağ tıkla/ kopyala yöntemi ile kopyalanır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_183.png)

Sistem Altyapı Tanımları/ İSG Risk Değerlendirme/Rapor formatları menüsüne gidilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_184.png)Açılan Rapor Formatları ekranında  ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_185.png)butonu tıklanılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_186.png) Açılan Rapor Formatları ekranında Rapor Tanımı kısmına Raporun adı bilgisi yazılır. Rapor Şablonu alanında Rapor Formatlarında uzantısıyla kopyalanan Rapor formatı bilgisi sağ tıkla/yapıştır komutu ile yapıştırma işlemi yapılır. Rapor Şablonu alanında sisteme aktardığınız şablonun tam adını, uzantısıyla birlikte yazmanız gerekir.  Örneğin rapor formatlı düzenleme menüsünde şablonunuzu " ISG Rapor Formatı Şablonu (Kayıt Bazında).xlsx "  ismi ile aktardıysanız, Rapor Şablonu alanına “ISG Rapor Formatı Şablonu (Kayıt Bazında).xlsx” yazmanız gerekiyor. Rapor Formatının rapor şablonu alanında  kayıt bazında rapor formatı seçildiğinde “Kayıt Bazında” seçeneği seçilir. Kayıt Bazında rapor formatının Pdf formatından alınmak isteniyorsa “Pdf Olarak Oluştur” alanı ilgili check box işaretlinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_187.png) 

**Açılan ekranda ilgili alanlar tanımlanır:**

**Rapor Tanımı:** Rapor Formatları ekranında Rapor tanımı bilgisinin yazıldığı alandır.

**Rapor Şablonu:** Rapor Formatları ekranında Rapor şablonun adı ve uzantısı bilgisi yazıldığı alandır. (Rapor Formatları Düzenleme menüsünde rapor şablonun yüklenip adı ve uzantısının sağ tıkla/kopyala yöntemi ile kopyalarak  bu alana sağ tıkla/yapıştır yöntemi ile yapıştırma işleminin yapılır.)

**Rapor Tipi:** Kayıt bazında, form bazında ve genel olmak üzere üç seçenek rapor tipi bilgisi seçilebilir. 

- **Kayıt Bazında:** Her bir risk kaydının ayrı olarak raporlanması talep edildiğinde seçilir. (Entegre Yönetim Sistemi/ İSG Risk Değerlendirme/ Risk Değerlendirme Formu tanımlama menüsünde Detaylar butonuna basıldıktan sonra çıkan  ![ref40]  butonuyla alınır. Kayıt bazında rapor formatı tanımlama işlemi olmadığı sürece ![ref40]   butonu görüntülenmez.)
- **Form Bazında:** Her risk formu altındaki risk detay kayıtlarının tek bir liste halinde Excel’e aktarıldığı durumlar için seçilir.

(Entegre Yönetim Sistemi /İSG Risk Değerlendirme/Risk Değerlendirme Formu Tanımlama menüsünde Detaylar butonuna basıldıktan sonra çıkan ![ref41]   butonuyla alınır.)

- **Genel:** Tüm risk detay kayıtlarının tek bir Excel’de görülmesi talep edildiği durumda seçilir.

(Entegre Yönetim Sistemi / İSG Risk Değerlendirme/Raporlar/Genel Risk Listesi Raporu ekranından ![ref41]   butonu ile alınır.)

**PDF olarak oluştur:** Rapor tipi kayıt bazında seçilen rapor formatlarında Entegre Yönetim Sistemi/ İSG Risk Değerlendirme/Risk Değerlendirme Formu Tanımlama/Risk Değerlendirme Form Detayı ekranında seçilen bir risk kaydının PDF formatı olarak aktarılabilmesi için bu check box’ı işaretlenebilir.

Açılan ekranda tanıtılacak rapor formatlarının isimleri Rapor Tanımı alanına yazılır. Rapor Şablonu alanına ise rapor formatları düzenleme menüsünden kopyalanan dosya adı uzantısıyla birlikte  ilgili alana yapıştırılır. Rapor Tanımlama ekranında gerekli alanlar doldurulduktan sonra sol üst köşedeki ![ref42] butonu tıklanarak rapor formatı kayıt bazında  tanımlama kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_190.png)

Tanımlanan kayıt bazında rapor formatının alınması için Entegre Yönetim Sistemi/ İSG Risk Değerlendirme/ Risk Değerlendirme Formu tanımlama menüsünde ![ref43] butonuna tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_192.png) 

Açılan Risk Değerlendirme Formu - Detaylar  ekranında ![ref44]  butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_194.png) 

Tanımlanan Kayıt Bazında rapor formatı alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_195.png) 

Rapor formatları Tanımlama ekranında Kayıt bazında rapor formatı tanımlama işleminde “Pdf Olarak Oluştur” alanı ile ilgili check box işaretlinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_196.png)

Rapor formatı ekranında ilgili check box işaretlendikten sonra ![ref42]butonu tıklanarak kayıt bazında rapor formatı  kayıt güncelleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_197.png)

Tanımlanan kayıt bazında  rapor formatının Pdf formatından alınması için Entegre Yönetim Sistemi/ İSG Risk Değerlendirme/ Risk Değerlendirme Formu tanımlama menüsünde ![ref43] butonuna tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_198.png) 

Açılan Risk Değerlendirme Formu - Detaylar  ekranında ![ref44]  butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_199.png) 

Tanımlanan rapor formatının Pdf formatında raporu alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_200.png)

**Form Bazında Rapor Formatı Tanımlama;**

Rapor Formatını Form bazında tanımlama işlemin işlem aşamaları kayıt bazında rapor formatının işlem aşamaları aynı şekilde yapılmaktadır. Rapor formatları menüsünde sadece Rapor Şablonu alanı seçeneklerinden Form seçeneği seçilerek rapor formatı kayıt işlemi yapılır.Rapor Form Şablonu aşağıdaki şekilde gerekli alanlar ilgili Tagler doldurulur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_201.png)

Rapor Formatı şablonu Rapor Formatı Düzenleme menüsüne yüklenir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_202.png)

Rapor Formatları menüsüne tıklanılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_203.png)

Açılan ekranda rapor tanımı alanına rapor formatının adı ve rapor formatları düzenleme menüsünde yüklenen rapor formatı şablonun adı ve uzantısı rapor şablonu alanı kopyala-yapıştır yöntemi ile yapıştırılır. Rapor şablonu alanı seçeneklerinde form bazında seçeneği seçilerek ekranın sol üst köşesindeki ![ref45]butonu tıklanarak rapor formatı form bazında kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_205.png)

Tanımlanan form bazında rapor formatının alınması için Entegre Yönetim Sistemi/ İSG Risk Değerlendirme/ Risk Değerlendirme Formu tanımlama menüsünde ![ref43] butonuna tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_206.png) 

Açılan Risk Değerlendirme Formu - Detaylar  ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_207.png)  butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_208.png) 

Tanımlanan form bazında rapor formatının raporu alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_209.png)

**Genel Bazda Rapor Formatı Tanımlama;**

Rapor Formatını Genel bazında tanımlama işlemin işlem aşamaları kayıt bazında rapor formatının işlem aşamaları aynı şekilde yapılmaktadır. Rapor formatları menüsünde sadece Rapor Şablonu alanı seçeneklerinden genel  seçeneği seçilerek rapor formatı kayıt işlemi yapılır.Rapor Form Şablonu aşağıdaki şekilde gerekli alanlar ilgili Tagler doldurulur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_210.png)

Rapor Formatı şablonu Rapor Formatı Düzenleme menüsüne yüklenir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_211.png)

Rapor Formatları menüsüne tıklanılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_212.png)

Açılan ekranda rapor tanımı alanına rapor formatının adı ve rapor formatları düzenleme menüsünde yüklenen rapor formatı şablonun adı ve uzantısı rapor şablonu alanı kopyala-yapıştır yöntemi ile yapıştırılır. Rapor şablonu alanı seçeneklerinde Genel seçeneği seçilerek ekranın sol üst köşesindeki ![ref45]butonu tıklanarak rapor formatı genel bazında kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_213.png)

Tanımlanana genel rapor formatının görüntülenmesi için Entegre Yönetim Sistemi /İSG Risk Değerlendirme/Raporlar/Genel Risk Listesi Raporu ekranı tıklanılır. Açılan ekranda RDF kodu alanına ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_214.png) butonu tıklanarak açılan Risk Değerlendirme Form listesinde formlar seçilerek  ![ref41]   butonu tıklanılır

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_215.png)

Genel Bazda rapor formatının alınma işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_216.png)
#### **6.1.8.1 Risk Modüllerinde Sabit Tagler Listesi**
Risk Modüllerinde Sabit Tag’ler listesi aşağıdaki tabloda yer almaktadır. Formlarda kullanılacak sabit tag’lerin alan kodları bu tablodan alınır.

|**Kısaltma**|**Açıklama**|
| - | - |
|<RDF\_KODU\>|RDF Kodu (Form Kodu)|
|<RDF\_TANIMI\>|RDF Tanımı(Form Tanımı)|
|<RDFD\_KODU\>|RDFD Kodu|
|<RDF\_NO\>|RDF Numarası|
|<RDFD\_NO\>|RDFD Numarası|
|<MSDS\_KODU\>|MSDS Kodu|
|<REV\_NO\>|Revizyon No|
|<REV\_TAR\>|Revizyon Tarihi|
|<HAZIRLAYAN\>|Hazırlayanın Adı Soyadı|
|<SISTEME\_GIREN\>|Sisteme Girenin Adı Soyadı|
|<REVIZE\_EDEN\>|Revize Edenin Adı Soyadı|
|<STATU\_ADI\>|Statü Adı |
|<RISK\_KAYNAGI\>|Risk Kaynağı|
|<REVIZE\_EDEN\_ACK\>|Revize Edenin Sicil Numarası|
|<SISTEME\_GIREN\_ACK\>|Sisteme Girenin Sicil numarası|
|<COLOR\>|Risk ekranındaki renk|
|<TREND\>|Risk ekranındaki oklar|
|<SURECLER\>|Süreçler Sekmesinde  Seçilen Süreç Bilgisi|
|<MEVCUT\_ONLEMLER\>|Önlemler sekmesinde Önlem tipi alanında  Mevcut seçeneğini bilgisi|
|<PLANLANAN\_ONLEMLER\>|Önlemler sekmesinde Önlem tipi alanında  Planlanan  seçeneğini bilgisi|

ÖNLEMLER İÇİN TAGLER
|**Kısaltma**|**Açıklama**|
| - | - |
|<YAPILANIS\>|Yapılan iş|
|<REF\_KODU\>|Alt aksiyonlar -DÖF kodu|
|<STATU\_ADI\>|Statü Adı|
|<ACIKLAMA\>|Önlem tanımı|
|<SORUMLU\>|Aksiyon Sorumlusu Olan Kişi|
|<YAPACAK\>|Aksiyon Yapacak Olan Kişi|
|<DURUM\>|Aksiyon Durumu  -DÖF durumu|
|<BITIS\_TARIHI\>|Aksiyon Bitiş Tarihi|
|<REF\_TIPI\>|Referans Tipi (Doküman, Aksiyon, DÖF, Diğer seçenekleri bilgisi)|
|<ONLEM\_TIPI\>|Önlem Tipi (Mevcut ve Planlanan Seçenek bilgisi)|
|<ONLEM\_TARIHI\>|Önlem Tarihi|
|<ONLEM\_NO\>|Önlem No|
|<GERCEKLESME\_TARIHI\>|Aksiyon Gerçekleşme Tarihi|

Geçmiş revizyon alanları için <ALAN6\_PREV\>  gibi tag kullanabilirsiniz. Liste tipli alanlarda prev tagı desteklenmemektedir. Prev tagı sadece  numerik  ve text tipli alan için çalışmaktadır.
### **6.1.9. Onay Akışı Tanımlama**
Değerlendirilen risklerin belirlenen kullanıcılara onaya gitmesi için sistemde onay akışı kurgulanması gereklidir. Modülde statü kullanımı aktifleştirilerek onay akış kurgusu gerçekleştirilir. Bunun için Sistem Altyapı Tanımları/ İSG Risk Değerlendirme / İSG Risk Değerlendirme Modülü Parametreler menüsü tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_217.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref46]: Listede seçili olan parametre bilgisi üzerinde düzenleme/değişiklik/güncelleme işlemi yapılır.

![ref47]: Kayıtlar filtrelenerek arama yapılır.

![ref48]: Veriler Excel’ e aktarılır.

![ref27]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref28]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref29]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Açılan Parametreler ekranında Parametre No alanına 22 numaralı  parametrenin numarası yazılarak ![ref47] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_221.png)

Parametreler ekranında 22 numaralı “Statü kullanılacak mı?” parametresi seçili iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_222.png)butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_223.png)

Açılan Parametreler ekranında parametrenin parametre değeri “Evet” seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_224.png)

Parametreler ekranında parametre değeri “Evet” seçilerek ekranın sol üst köşesindeki ![ref22]butonu tıklanarak parametre aktif etme kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_225.png)

22 numaralı “Statü kullanılacak mı?” parametresinin aktif edilme işleminden sonra Fonksiyon Dizanyer menüsünde ![ref49] ve ![ref50] olmak üzere iki buton görüntülenir.Fonksiyon Dizanyer menüsünde  ilgili fonksiyon için  ![ref49] butonu ile buton tanımlaması ve ![ref50] butonu ile statülerin tanımlama işlemleri yapılır.

**NOT:** Akış tanımları Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Akış tanımlama ekranından kontrol edilmeli yoksa akışları tanımlanmalıdır. Ayrıca Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Rol Tanımlama ekranından da onay akışları için rol tanımlamaları yapılır. Rol tanımlama işlemlerinde SQL ve QDMS veri tabanı bilgisi gerekeceğinden Bimser Teknik Destek ekibiyle iletişime geçilerek gerekli rol talep edilebilir.Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Rol Tanımlama menüsü tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_228.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref51]:Yeni bir rol tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_230.png): Listede seçili rol bilgisi güncellenir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_231.png): Listede seçili rol bilgisi silinebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_232.png): Kayıtlar filtrelenerek arama yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_233.png): Veriler Excel’ e aktarılabilir.

Rol Tanımlama ekranına yeni bir rol eklemek için ekranın sol üst köşesindeki ![ref51]butonu tıklanarak Rol Tanımlama/Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_234.png)

Gerekli alanlar doldurulduktan sonra sol üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_235.png)butonu tıklanarak rol tanımlama işlemi gerçekleştirilir. İSG Risk Değerlendirme Modülünde akış tanımlamaları için  kullanılacak rol  tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_236.png)

Sistem Altyapı Tanımları/ BSAT/ Tanımlar/ Mesaj Gövdesi Tanımlama ekranından modül için yeni mesaj gövdesi tanımlamaları yapılabilir. Ayrıca Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Akış Tanımlama ekranından İSG Risk Değerlendirme Modülünde kullanılacak akış tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_237.png)

Fonksiyon Dizayner menüsüne gelinir. Statü ve Butonlar adında iki farklı işlem butonu Risk Değerlendirme Form Tanımlama ve Risk Değerlendirme Detay fonksiyonları için menüye gelecektir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_238.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref18]: Statü tanımlama işlemi yapılır.

![ref19]: Buton tanımlama işlemi yapılır.

![ref20] : Alanların ilgili fonksiyon ile ilişkilendirilme işlemi yapılır.

Fonksiyon Dizayner menüsünden 3 numaralı fonksiyon seçili iken  ![ref18]butonu tıklanılarak  fonksiyonun statülerin tanımlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_239.png)

**Ekranındaki bulunan butonlar yardımıyla;**

![ref52]: Yeni bir statü tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_241.png): Listede seçili statü bilgisi güncellenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_242.png): Listede seçili statü bilgisi silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_243.png): Alanlar aktif, görünür ve zorunlu statüleri belirlenir.

![ref53]: Önceki ekrana geri dönülür.

Statü Tanımlama ekranında ![ref52]butonu tıklanarak yeni statü tanımlama ekranına açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_245.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Statü Kodu:** Statü Tanımlama-Yeni kayıt ekranında statü kodu bilgisi tanımlandığı alandır.  Daha önce tanımlamış alanlarla aynı olmayacak şekilde boşluk, Türkçe karakter gibi karakterler kullanmadan tanımlanmalıdır.

**Statü Adı:** Statü Tanımlama-Yeni kayıt ekranında statü adı bilgisi tanımlandığı alandır.

**Akış Başlatılsın:** Statü Tanımlama-Yeni kayıt ekranında tanımlanan statüde herhangi bir akış başlatılacaksa akış başlatılsın check box işaretlendiği alandır. 

**Yeni Statü:** Statü Tanımlama-Yeni kayıt ekranında sistemde tanımlı statülerden seçilebildiği alandır. Tanımlanan statüden sonra geçilecek statü varsa seçilir.

**Onay Süresi:** Statü Tanımlama-Yeni kayıt ekranında onay süresi bilgisi tanımlandığı alandır.

**İlk Hatırlatma:** Statü Tanımlama-Yeni kayıt ekranında onay süresi bilgisinin boyunca ilk hatırlatma mailinin gideceği günün tanımlandığı alandır. Tanımlanan günlerde onay için hatırlatma maileri gidilmesi sağlanır.

**İkinci Hatırlatma:** Statü Tanımlama-Yeni kayıt ekranında onay süresi bilgisinin boyunca ikinci hatırlatma mailinin gideceği günün tanımlandığı alandır. Tanımlanan günlerde onay için 2. hatırlatma maileri gidilmesi sağlanır.

**Son Hatırlatma:** Statü Tanımlama-Yeni kayıt ekranında onay süresi bilgisinin boyunca son hatırlatma mailinin gideceği günün tanımlandığı alandır. Tanımlanan günlerde onay için hatırlatma maileri gidilmesi sağlanır.

**Revizyon Başlatılsın:** Statü Tanımlama-Yeni kayıt ekranında tanımlanan statüde Revizyonun başlatılması isteniyorsa ilgili check box işaretlenir. 

**Durum:** Statü Tanımlama-Yeni kayıt ekranında statü  durumu aktif veya pasif olarak seçildiği  alandır.

**Akış Tanımı:** Statü Tanımlama-Yeni kayıt ekranında sistemde tanımlı akışlarda hangi akışın olacağı seçilebildiği alandır. Akış tanımlama işlemi BSAT/Sistem Altyapı Tanımları/Konfigürasyon Ayarları/Akış Tanımlama menüsünde tanımlanır.

**Onay Talep Mesajı:** Statü Tanımlama-Yeni kayıt ekranında sistemde tanımlı mesaj gövdesinde onay talep mesajının seçildiği alandır. Onay Talep Mesajı BSAT/Sistem Altyapı Tanımları/Tanımlar/Mesaj Gövdesi Tanımlama menüsünde tanımlanır.

**Onay Tamam Mesajı:** Sistemde tanımlı mesaj gövdesinde onay tamam mesajının seçilir. Onay Tamam Mesajı BSAT/Sistem Altyapı Tanımları/Tanımlar/Mesaj Gövdesi Tanımlama menüsünde tanımlanır.

**Onay Red Mesajı:** Statü Tanımlama-Yeni kayıt ekranında sistemde tanımlı mesaj gövdesinde oany red mesajının seçildiği alandır. Onay red Mesajı BSAT/Sistem Altyapı Tanımları/Tanımlar/Mesaj Gövdesi Tanımlama menüsünde tanımlanır.

Açılan ekranda statü kodu, statü adı, akışın başlatılıp başlatılmayacağı, yeni statü, durum, akış tanımı, onay talep mesajı, onay tamam mesajı ve onay ret mesajı veri girişleri yapılarak gerekli alanlar doldurulduktan sonra ekranın sol üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_246.png) botunu tıklanarak statü tanımlama kayıt işlemi Risk Değerlendirme Form Tanımlama fonksiyonu  için yapılır.Tüm ilgili fonksiyon için statülerin tanımlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_247.png)

![ref53] Geri butonu ile önceki ekrana dönülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_248.png)

Fonksiyon Dizayner menüsünde ilgili fonksiyon için  ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_249.png)butonu tıklanarak statülerde kullanılacak butonlar tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_250.png)

**Ekranındaki bulunan butonlar yardımıyla;**

![ref54]: Yeni bir buton tanımlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_252.png): Listede seçili buton bilgisi güncellenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_253.png): Listede seçili buton bilgisi silinir.

![ref53]: Önceki ekrana geri dönülür.

Buton Tanımlama ekranında  ![ref54]butonu ile yeni buton tanımlama ekranına açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_254.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Buton Kodu:** Buton Tanımlama -Yeni Kayıt ekranında buton kodu bilgisi yazıldığı alandır.. Daha önce tanımlamış alanlarla aynı olmayacak şekilde boşluk, Türkçe karakter gibi karakterler kullanmadan tanımlanmalıdır.

**Buton Adı:** Buton Tanımlama -Yeni Kayıt ekranında Buton adı bilgisinin yazıldığı alandır.

**Buton Tipi:** Buton Tanımlama -Yeni Kayıt ekranında sistemde tanımlı buton tipi seçenekleri  Onay ve red seçeneklerinde  belirlendiği alandır.

**Görünür Statü:** Buton Tanımlama -Yeni Kayıt ekranında tanımlanan butonun hangi statüde görüntüleneceği belirlendiği alandır.

**Yeni Statü:** Buton Tanımlama -Yeni Kayıt ekranında tanımlanan butona tıkanıldığında hangi statü geçiş yapacağı sistemde tanımlı statülerden seçildiği alandır.

**Durum:** Buton Tanımlama -Yeni Kayıt ekranında tanımlanan butonun durumu aktif veya pasif seçeneklerinden seçildiği alandır.

**Uyarı Mesajı:** Buton Tanımlama -Yeni Kayıt ekranında tanımlanan butona tıklatıldığında ekranda uyarı mesajının bilgisinin girildiği alandır. Örneğin: Onaya göndermek istediğinizden emin misiniz?

Açılan ekranda Buton kodu, Buton adı bilgisi girilir. Buton tipi belirlenir. Görünür statüsü, Yeni statüsü ve durumu seçilir. Gerekli alanlar doldurulduktan sonra ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_255.png) butonu tıklanarak Risk Değerlendirme Form Tanımlama fonksiyonu  için buton tanımlama kayıt işlemi gerçekleştirilir

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_256.png)

Açılan ekranda aynı şekilde 3. fonksiyon olan  Risk Değerlendirme Form Tanımlama fonksiyonun olduğu  gibi 4. fonksiyon olan Risk Değerlendirme Detayı  fonksiyonun tüm statülerin tanımlama işlemi yapılır. Statü tanımlama işleminde Akış Tanımı alanında ilgili statü için akışın ilişkilendirilmesi işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_257.png)

Açılan ekranda aynı şekilde 3. fonksiyon olan  Risk Değerlendirme Form Tanımlama fonksiyonun olduğu  gibi 4. fonksiyon olan Risk Değerlendirme Detayı  fonksiyonun tüm statülerin tanımlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_258.png)

Fonksiyon Dizanyer menüsünde 4. Numaralı fonksiyon olan Risk Değerlendirme Detay fonksiyon seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_259.png) butonları tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_260.png)

Açılan ekranda aynı şekilde 3. fonksiyon olan  Risk Değerlendirme Form Tanımlama fonksiyonun olduğu  gibi 4. fonksiyon olan Risk Değerlendirme Detayı fonksiyonun tüm butonlarının  tanımlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_261.png)
### **6.1.10. Tekrar Eden Kayıtlar Rapor Şablonu**
**Menü Adı**: Sistem Altyapı Tanımları / İSG Risk Değerlendirme / Tekrar Eden Kayıtlar Rapor Şablonu

Risk kayıtlarında yer alan alanların tekrar etme durumunu göre rapor olarak  alındığı menüdür.İlk olarak Sistem Altyapı Tanımları/ İSG Risk Değerlendirme /Tekrar Eden Kayıtlar Raporu Şablonu menüsünden raporda gösterilecek alanlar seçilir ve rapor formatı kaydedilir.

Daha sonra Entegre Yönetim Sistemi/ İSG Risk Değerlendirme /Raporlar/Tekrar Eden Kayıtlar raporundan ilgili rapora ulaşılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_262.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref55]:Yeni tekrar eden kayıtlar şablonu tanımlanır

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_264.png): Listede seçili tekrar eden kayıtlar şablonu bilgisi ile ilgili herhangi bir düzeltme, değişiklik veya güncelleme yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_265.png): Listede seçili tekrar eden kayıtlar şablonu bilgisi silinebilir.

Tekrar Eden Kayıtlar Raporu Şablonları ekranında yeni bir Tekrar Eden Kayıtlar Raporu Şablonu tanımlamak için ekranın sol üst köşesindeki ![ref55]butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_266.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Tanım:** Tekrar Eden Kayıtlar Raporu Şablonları ekranında Tekrar Eden Kayıtlar Raporu Şablonları tanım bilgisinin girildiği alandır.

**Kolonlar:** Tekrar Eden Kayıtlar Raporu Şablonları ekranında Kolonlar bilgisinin seçilebildiği alandır.

Açılan ekranda Tekrar Eden Kayıtlar Raporu tanım bilgisi girilir. İlgili Kolonlar seçilir. Tekrar Eden Kayıtlar Raporu Şablonları ekranında gerekli alanlar doldurulduktan sonra sol üst köşedeki ![ref30]butonu tıklanarak Tekrar Eden Kayıtlar Raporu Şablonları kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_267.png)

Entegre Yönetim Sistemi/ İSG Risk Değerlendirme /Raporlar/Tekrar Eden Kayıtlar raporu ekranı gidilir.  

![ref56]

Tekrar Eden Kayıtlar ekranında Filtre sekmesinde filtre arama kriterleri olan “Rapor Şablonu ” alanında açılan açılır  listede  Rapor Şablonu seçilerek   ![ref57]  butonu tıklanılır.

![ref58]

Tekrar Eden Kayıtlar ekranında liste sekmesinde yapılan filtredeki arama kriterlerine göre kayıtlar listelenir.

![ref59]

Tekrar Eden Kayıtlar ekranında ![ref60]  butonu tıklanarak Tekrar Eden Kayıtlar raporun Excel formatından raporu alınır.

![ref61]
## **6.2.Entegre Yönetim Sistemi/ İSG Risk Değerlendirme**
İSG Risk Değerlendirme Modülü kapsamında Faaliyet  Grupları Tanımlama, Faaliyet Tanımlama, Risk Formu Tanımlama,  Risk Form Detaylarının Tanımlandığı, Raporların ve Grafiklerin görüntülendiği kısımdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_274.png)
### **6.2.1.Faaliyet Grubu Tanımlama**
**Menü Adı:** Entegre Yönetim Sistemi/ İSG Risk Değerlendirme/Faaliyet Grubu Tanımlama

İSG Risk Değerlendirme Modülünde kullanılacak olan faaliyetlerin  tanımlanması için öncelikle bu faaliyelere  bağlı bulunacağı grupların tanımlanması gerekir. Bu faaliyetlere bağlı bulunacağı gruplarının tanımlama işlemi yapıldığı menüdür.Bu menüde İSG Risk Değerlendirmesine tabi tutulacak faaliyetlerin  genel ve alt kategorileri belirlenir.İSG Risk Değerlendirme modülü süreci kapsamında öncelikle kuruma ait tüm Faaliyet grupları tanımlanması gerekmektedir.Bu tanımlama işlemi tek tek sistem arayüzünden giriş yapılabildiği gibi, toplu  aktarım şablonu olan excel dosyasına indirilip, indirilen aktarım şablonunda ilgili alanlarla ilgili bilgiler girilerek sisteme aktarım şablonu yüklenerek toplu şekilde faaliyet gruplarının aktarım işlemi yapılmaktadır. Şablonla kuruma ait faaliyet grupların yükleme işlemi için Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Yönetici Tanımlama menüsünde ilgili modülde modül yönetici olarak tanımlı olmak gerekmektedir. Modül Yönetici olarak tanımlı kullacının  ekranında aktarım şablonlar ile ilgili butonlar görüntülenir.Aksi takdirde kullanıcı modül yöneticisi olmadığında aktarım şablonlar ile ilgili butonlar görüntülenmez.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_275.png)

**Ekrandaki bulunan butonlar yardımıyla**;

![ref62]: Yeni bir Faaliyet grubu tanımlanabilir.

![ref63]:Listede seçili Faaliyet grubu bilgisi güncellenebilir.

![ref64]:Listede seçili Faaliyet grubu bilgisi silmek için kullanılır. 

![ref65]:Faaliyet grupları tanımlamalarını Excel’ e aktarılır.

![ref66]: Şablon yüklemek için kullanılır. (Bu butonun görüntülenmesi için ilgili Modülde modül Yönetici olarak tanımlı olmak gerekmektedir)

![ref67]: Şablon oluşturmak için kullanılır. (Bu butonun görüntülenmesi için ilgili Modülde modül Yönetici olarak tanımlı olmak gerekmektedir)

**Faaliyet Grubu  Toplu Aktarım İşlemi;**

Faaliyet Grubu  Tanımlama ekranında![ref68]  butonu ile Faaliyet Grubu  Tanımlama Şablonu  bilgisayara indirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_283.png)

Faaliyet Grubu  Tanımlama şablonunda ilgili alanlar ilgili bilgiler yazılarak bilgisayara kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_284.png)

Faaliyet Grubu  Tanımlama ekranında ![ref69] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_286.png)

Dosya Yükle ekranında “Gözat” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_287.png)

Açılan ekranda doldurulan Faaliyet Grubu Tanımlama şablonu seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_288.png)

Sistem tarafından Faaliyet Grupları başarıyla aktarılmıştır.Lütfen ilgili otokod şablon ve sayaçlarını kontrol ediniz” mesajı verilerek  Faaliyet Grubu aktarım işlemin gerçekleştiği belirtilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_289.png)

Faaliyet Grubu Tanımlama ekranında listede toplu aktarım işlemi yapılan Faaliyet grupları  görüntülenir. Toplu aktarım yapılan Faaliyet grupları seçilerek ![ref70] butonu tıklanarak otokod şablon ve sayaçlarını kontrol edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_291.png)

Faaliyet Grubu Tanımlama ekranında yeni bir Faaliyet Grubu Tanımlama işlemi için ![ref62] butonu tıklanarak Faaliyet Grubu Tanımlama ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_292.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Bağlı Olduğu Faaliyet Grubu:** Faaliyet Grubu Tanımlama ekranında bağlı olunan Faaliyet grubu bilgisi seçildiği alandır. Ana Faaliyet grubuna bağlı alt kırılımlı bir Faaliyet grubu tanımlamak için ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_293.png)  butonu tıklanarak açılan sistemde tanımlı Faaliyet grubu listesinde ana Faaliyet grubu tanımı seçilir.

**Faaliyet Grubu Kodu:** Faaliyet Grubu Tanımlama ekranında Faaliyet grubu kodu bilgisi tanımlandığı zorunlu alandır. Daha önce tanımlamış alanlarla aynı olmayacak şekilde boşluk, Türkçe karakter gibi karakterler kullanmadan tanımlanmalıdır. Ör. ‘001’ , ‘RK’

**Faaliyet Grubu Tanımı:** Faaliyet Grubu Tanımlama ekranında tanım bilgisinin tanımlandığı zorunlu alandır.

**Sorumlu Kullanıcı Grupları:** Faaliyet Grubu Tanımlama ekranında Sorumlu kullanıcı gruplarının sistemde tanımlı olan kullanıcı grubu listesinden seçilebilir. Sorumlu Kullanıcı Grupları” alanında seçim yapılacak kullanıcı grupları ile belirli Faaliyet gruplarını belirli kullanıcı sorumluları yetkilendirebilirsiniz. Bu sayede kullanıcı grubuna dahil olmayan kişiler bu Faaliyet grupları göremez ve alt Faaliyet grup tanımlamaları veya Faaliyet grupların güncelleme işlemleri gerçekleştiremez. Sorumlu Kullanıcı Grupları alanına ilgili alanı ilgili bu  modülün parametre ayarlarından “Sorumlu kullanıcı grupları üzerinden yetki kontrolü yapılacak mı?” parametre değeri”Evet" olarak işaretlenirse bu yetkilendirme işlemi aktif hale gelir.

![ref71]

**Sorumlu Personeller:** Faaliyet Grubu Tanımlama ekranında sorumlu faaliyet grubuna ait sorumlu personeller bilgi açılan sistemde tanımlı personeller listesinde seçildiği alandır.Parametreye bağlı olarak görüntülenen bir alandır. İSG Risk Değerlendirme Modülü parametrelerinde  19 numaralı “Sorumlu personeller seçilsin mi?(E/H)” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir.

![ref72]

Parametre aktif edildikten sonra Faaliyet Grubu Tanımlama ekranında bu alan görüntülenir ve Faaliyet grubu için sorumlu personel açılan personel listesinden seçim yapılır. 

**Otomatik Kod Şablonu:** Faaliyet Grubu Tanımlama ekranında Otomatik kod şablonu bilgisi tanımlandığı alandır. Tanımlanan otomatik kod şablona göre Faaliyet tanımlama işleminde seçilen Faaliyet grup kodu göre otomatik kod atamasını sistem yapar. Örn:[DMC].001, DMC].002, DMC].003 otomatik kod sayac değerine göre otomatik kod ataması yapar. Faaliyet Tanımlama ekranında tanımlanan Faaliyet bağlı olduğu Faaliyet grubu seçildiğinde bağlı olunan Faaliyet grubunda tanımlı kod şablonu göre atama yapar.

**Otomatik Kod Sayacı:** Faaliyet Grubu Tanımlama ekranında otomatik kod şablonunda belirlenen koda göre verilen Faaliyet kayıtlarının kodunun hangi değerden başlayacağı belirlendiği alandır. 

**Durum:** Faaliyet Grubu Tanımlama ekranında durum bilgisinin “Aktif” ve “Pasif” seçeneklerinde “Aktif” seçeneğinin seçildiği alandır. Durumu pasif olanlar Faaliyet grupları tanımları sistemde artık kullanılmadığına bir işarettir.

Açılan ekranda varsa Faaliyet grubunun bağlı olduğu Faaliyet grubu, Faaliyet grubu kodu ve tanımı girilir. Eğer sadece belirli kullanıcı gruplarının bu Faaliyetlerle işlem yapması isteniyorsa sorumlu kullanıcı grupları kısmından kullanıcı grupları seçilip eklenir. Durum menüsünden aktif/ pasif durumu belirlenir.Gerekli alanlar ilgili bilgiler girildikten sonra ekranın sol üst köşesindeki  ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_296.png) butonuyla tıklanarak Faaliyet Grubu kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_297.png)
### **6.2.2.Faaliyet Tanımlama**
**Menü Adı:** Entegre Yönetim Sistemi/İSG Risk Değerlendirme/ Faaliyet Tanımlama

Risk Modülünde analizi yapılan risklerde ilişki kurulabilecek Faaliyetların tanımlandığı menüdür. Bu menüde  oluşturulan Faaliyet gruplarına bağlı olarak Faaliyetler  tanımlanır. Entegre Yönetim Sistemi altında Faaliyet Tanımlama menüsü tıklanarak ilgili sayfa görüntülenir. Faaliyet tanımlama sayfası, Faaliyet grubu tanımlama sayfasına benzemektedir. Bu menüde İSG Risk Değerlendirme modülü süreci kapsamında öncelikle kuruma ait tüm Faaliyet tanımlanması yapılmaktadır.Bu tanımlama işlemi tek tek sistem arayüzünden giriş yapılabildiği gibi,  toplu  aktarım şablonu olan excel dosyasına indirilip, indirilen aktarım şablonunda ilgili alanlarla ilgili bilgiler girilerek sisteme aktarım şablonu yüklenerek toplu şekilde Faaliyet tanımlarının aktarım işlemi yapılmaktadır. Şablonla kuruma ait Faaliyet tanımlanrın yükleme işlemi için Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Yönetici Tanımlama menüsünde ilgili modülde modül yönetici olarak tanımlı olmak gerekmektedir. Modül Yönetici olarak tanımlı kullacının  ekranında aktarım şablonlar ile ilgili butonlar görüntülenir.Aksi takdirde kullanıcı modül yöneticisi olmadığında aktarım şablonlar ile ilgili butonlar görüntülenmez.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_298.png)

**Ekrandaki bulunan butonlar yardımıyla**;

![ref62]:Yeni bir Faaliyet tanımlanabilir.

![ref63]:Listede seçili Faaliyet bilgisi güncellenebilir.

![ref64]:Listede seçili Faaliyet bilgisi silmek için kullanılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_299.png): Listede seçili Faaliyet bilgisinin kopyalama işlemi yapılır.

![ref65]:Faaliyet tanımlamalarını Excel’ e aktarılır.

![ref66]:Şablon yüklemek için kullanılır. (Bu butonun görüntülenmesi için ilgili Modülde modül Yönetici olarak tanımlı olmak gerekmektedir)

![ref67]:Şablon oluşturmak için kullanılır. (Bu butonun görüntülenmesi için ilgili Modülde modül Yönetici olarak tanımlı olmak gerekmektedir)

**Faaliyet Toplu Aktarım İşlemi;**

Faaliyet Tanımlama ekranında![ref68]  butonu ile Faaliyet Tanımlama Şablonu  bilgisayara indirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_300.png)

Faaliyet Tanımlama şablonunda ilgili alanlar ilgili bilgiler yazılarak bilgisayara kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_301.png)

Faaliyet Tanımlama ekranında ![ref69] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_302.png)

Dosya Yükle ekranında “Gözat” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_303.png)

Açılan ekranda doldurulan Faaliyet Tanımlama şablonu seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_304.png)

Sistem tarafından “Faaliyetler başarıyla aktarılmıştır.Lütfen ilgili otokod şablon ve sayaçlarını kontrol ediniz” mesajı verilerek  Faaliyet  aktarım işlemin gerçekleştiği belirtilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_305.png)

Faaliyet Tanımlama ekranında listede toplu aktarım işlemi yapılan Faaliyetler  görüntülenir. Toplu aktarım yapılan Faaliyetler seçilerek ![ref70] butonu tıklanarak otokod şablon ve sayaçlarını kontrol edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_306.png)

Faaliyet Tanımlama ekranında yeni bir Faaliyet Tanımlama işlemi için ![ref62] butonu tıklanarak Faaliyet Tanımlama ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_307.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Faaliyet Grubu:** Faaliyet Tanımlama ekranında Faaliyet tanımın bağlı olduğu Faaliyet grubu sistemden tanımlı Faaliyet grubu listesinde seçildiği alandır.

**Faaliyet Kodu:** Faaliyet  Tanımlama ekranında Faaliyet kodu bilgisi tanımlandığı zorunlu alandır. Daha önce tanımlamış alanlarla aynı olmayacak şekilde boşluk, Türkçe karakter gibi karakterler kullanmadan tanımlanmalıdır. Faaliyet Grubu Tanımlama menüsünde tanımlanan kod şablona göre sistem otomatik kod ataması yapar. Bu otomatik kod ataması işleminin olması için Faaliyet grubu alanında Faaliyet grubu seçim işlemi yapılması gerekir. Seçim işlemi yapılan bu Faaliyet grubunda tanımlı otomatik kod şablonu ve sayac değerine göre Faaliyet  bilgisini kodunu sistem otamatik atar.

**Faaliyet Tanımı:** Faaliyet Tanımlama ekranında tanım bilgisinin tanımlandığı zorunlu alandır.

**Sorumlu Kullanıcı Grupları:** Faaliyet Tanımlama ekranında Sorumlu kullanıcı gruplarının sistemde tanımlı olan kullanıcı grubu listesinden seçilebilir. Sorumlu Kullanıcı Grupları alanında seçim yapılacak kullanıcı grupları ile belirli Faaliyet tanımlarında belirli kullanıcı sorumluları yetkilendirebilirsiniz. Bu sayede kullanıcı grubuna dahil olmayan kişiler bu Faaliyet tanımlarını göremez ve  Faaliyet tanımları bilgisi üzerinde güncelleme işlemleri gerçekleştiremez. Sorumlu Kullanıcı Grupları alanına ilgili  alanı ilgili bu  modülün parametre ayarlarından “ Sorumlu kullanıcı grupları üzerinden yetki kontrolü yapılacak mı?” parametre değeri”Evet" olarak işaretlenirse bu yetkilendirme işlemi aktif hale gelir.

![][ref71]

**Sorumlu Personeller:** Faaliyet Tanımlama ekranında sorumlu faaliyet grubuna ait sorumlu personeller bilgi açılan sistemde tanımlı personeller listesinde seçildiği alandır.Parametreye bağlı olarak görüntülenen bir alandır. İSG Risk Değerlendirme Modülü parametrelerinde  19 numaralı “Sorumlu personeller seçilsin mi?(E/H)” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir.

![][ref72]

Parametre aktif edildikten sonra Faaliyet Tanımlama ekranında bu alan görüntülenir ve Faaliyet için sorumlu personel açılan personel listesinden seçim yapılır. 

**Durum:** Faaliyet Tanımlama ekranında durum bilgisinin “Aktif” ve “Pasif” seçeneklerinde “Aktif” seçeneğinin seçildiği alandır. Durumu pasif olanlar Faaliyet tanımları sistemde artık kullanılmadığına bir işarettir.

Açılan ekranda  Faaliyet grubunun bağlı olduğu Faaliyet grubu, Faaliyet  kodu ve tanımı girilir. Eğer sadece belirli kullanıcı gruplarının bu Faaliyetlerle işlem yapması isteniyorsa sorumlu kullanıcı grupları kısmından kullanıcı grupları seçilip eklenir. Durum menüsünden aktif/ pasif durumu belirlenir.Gerekli alanlar ilgili bilgiler girildikten sonra ekranın sol üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_308.png)butonuyla tıklanarak Faaliyet tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_309.png)
### **6.2.3.Risk Değerlendirme Formu Tanımlama**
**Menü Adı:** Entegre Yönetim Sistemi/ İSg Risk Değerlendirme/ Risk Değerlendirme Formu Tanımlama

İSG Risk Değerlendirme Modülü’nde Faaliyet ve Faaliyet grupları da tanımlandıktan sonra yapılacak son aşama, risklerin yer alacağı formların (RDF) tanımlanmasıdır. Bunun için Entegre Yönetim Sistemi başlığı altındaki İSG Risk Değerlendirme Modülü’nün altında Risk Değerlendirme Formu Tanımlama menüsü açılır. RDF tanımlamadaki amaç, risk analizinin yapılacağı detay formların belirli kategoriler ( ünite, birim, faaliyet grubu, departman vb. ) altında sınıflandırmaktır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_310.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref73]: Yeni RDF ( Risk Değerlendirme Formu) tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_312.png):Listede seçili RDF bilgisi güncellenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_313.png): Listede seçili RDF bilgisi kopyalanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_314.png): Listede seçili RDF bilgisi silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_315.png): Listede seçili RDF’nin detay bilgiler ekranını açar.

![ref74]:Listede seçili RDF bilgisinin sıra numarası değiştirme işlemi yapılır. Risk Değerlendirme Formu Tanımlama ekranda liste sekmesinde RDF seçili iken ![ref74] butonu tıklanılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_317.png)

Açılan Sıra Numarası Değiştir ekranında Yeni Sıra Numarası bilgisi belirlenerek ![ref75] butonu tıklanırak sıra numarası değiştirme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_319.png)

Risk Değerlendirme Formu Tanımlama ekranında listede seçili formun sıra numarası değiştirme işleminden sonra sıra numarasının değiştirildiği görülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_320.png)

![ref76]:Risk Yetki Matrisi ekranın açılma işlemi yapılır.Tanımlanan risk formlarında hangi rolün veya kullanıcı grubunun kayıt görme, güncelleme vb. yetkilere sahip olacağının belirlendiği alandır.

Risk Değerlendirme Formu Tanımlama ekranda ![ref76] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_322.png)

Risk Yetkisi Matrisi ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_323.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref77]:Risk Yetki matrisi  ekranında kayıt işlemi yapılır

![ref78]:Risk Yetki Matrisi ekranında yetkilendirme yapılan listede seçili Kullanıcı grubunda bulanan personellerin listesi görüntülenir

![ref79]:Risk Yetki Matrisi ekranında sistemde tanımlı kullanıcı grubu listesinde yetki verilmek istenilen kullanıcı grubu ekleme işlemi yapılır.

![ref80]: Risk Yetki Matrisi ekranında yetki verilen listede seçili kullanıcı grubunu silme işlemi yapılır.

Risk  Yetki Matrisi ekranında Roller Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Rol Tanımlama menüsünde  tanımlı gelmektedir.Rol tanımları hangi role yetki verilmesi isteniyorsa o role karşılık gelen ilgili yetki check box  işaretlenir ve ![ref77] butonu ile kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_328.png)

Risk Yetki Matrisi ekranında bir kullanıcı grubuna yetki vermek için  ![ref79] butonu tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_329.png)

Açılan sistemde tanımlı kullanıcı grubu listesinde yetki verilmek istenilen kullanıcı grubu seçilir ve ekranın sol üst kösesinde yer alan  ![ref81] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_331.png)

Risk  yetki matrisi ekranında kullanıcı grubu için  İSG Risk Değerlendirme Modülü  işlemleri için yetkilendirme işlemler için yetki check box’ları işaretlendikten sonra ekranın sol üst köseşinde yer alan ![ref77] butonu tıklanarak kullanıcı grubu bazlı yetkilendirme kayıt işlemi yapılır.Örn:Hazırlama, Revizyon ve Kopyalama yetkileri gibi ilgili check box işaretlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_332.png)

Yetki verilen kullanıcı grubundan yetkiler alınıp, kullanıcı grubunun yetki matrisinden çıkarılması isteniyorsa ![ref80] butonu kullanılır.Risk Yetki matrisi ekranında yetkilendirme yapılan Kullanıcı grubu listede seçili iken ![ref78]butonu tıklanılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_333.png)

Kullanıcı grubunda bulunan personellerin listesinin görüntülenmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_334.png)

![ref68]: Şablon oluşturmak için kullanılır. Aktarım şablonu bu buton ile kullanıcının bilgisayarına indirilerek ilgili alanlar doldurulur.

![ref82]: Şablon yüklemek için kullanılır.Kullanıcının bilgisayara indirilip, doldurulan şablon sisteme bu buton ile yüklenir.

Not: Uyarlama çalışmaları sonrasında mevcut risk değerlendirme formları (RDF’ler) sisteme toplu olarak aktarılabilmektedir. Bu sebeple alan tanımlama vb. işlemler tamamlandıktan sonra sistemin kullanıma hazır olduğuna karar verildiği takdirde BSAT/Konfigürasyon Ayarları/Yönetici Tanımlama menüsünde bu modülde yönetici olarak belirlenen kullanıcıların Risk Değerlendirme Form Tanımlama ekranında ![ref68]ve ![ref82]butonu çıkmaktadır. Aktarım Şablonu sistemde tanımlanan alanlara göre otomatik olarak oluşturulmaktadır. ![ref83]butonu ile sistem oluşturulan şablonu bilgisayara indirir. İlgili şablon kullanıcılar tarafından doldurularak ![ref84]butonu ile sisteme yüklendiğinde Risk Değerlendirme Formları (RDF’ler) sisteme aktarmış olur.

**Risk  Değerlendirme Formu  Toplu Aktarım İşlemi;**

Risk Değerlendirme Formu Tanımlama ekranında![ref68]  butonu ile Risk Değerlendirme Formu Tanımlama Şablonu  bilgisayara indirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_338.png)

Risk Değerlendirme Formu Tanımlama şablonunda ilgili alanlar ilgili bilgiler yazılarak bilgisayara kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_339.png)

Risk Değerlendirme Form Tanımlama ekranında ![ref69] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_340.png)

Dosya Yükle ekranında “Gözat” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_341.png)

Açılan ekranda doldurulan Risk Değerlendirme Formu Tanımlama şablonu seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_342.png)

Sistem tarafından “Riskler başarıyla aktarılmıştır.Lütfen ilgili otokod şablon ve sayaçlarını kontrol ediniz” mesajı verilerek  RDF(Risk Değerlendirme Formu) aktarım işlemin gerçekleştiği belirtilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_343.png)

Risk Değerlendirme Form Tanımlama ekranında liste sekmesinde listede toplu aktarım işlemi yapılan RDF görüntülenir

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_344.png)

Risk Değerlendirme Form Tanımlama ekranında yeni bir Risk Değerlendirme Formu tanımlamak için  ![ref73] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_345.png)

Risk Değerlendirme Form Tanımlama ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_346.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**RDF Kodu:** Risk Değerlendirme Formu Tanımlama ekranında sistem tarafından otomatik verildiği alandır.İlgili modülün 1 numaralı “Risk Değerlendirme Oto Kod Şablonu”   parametresinde tanımlı kod şablonuna göre sistem otomatik kod şablonu atamasını yapar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_347.png)Tanımlanan oto kod şablonun kaç sayaç değerinde başlayacağı bilgiside  ilgili modülün 2 numaralı “Risk Değerlendirme Sayac” parametresinde parametre değerinde  tanımlı değere göre gelmektedir. Parametre değerinde sayaç değeri “2” olarak tanımlıdır. Kod şablonu RD.002, RD.003, RD.004 şeklinde kod ataması yapacaktır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_348.png)

**RDF Tanımı:** Risk Değerlendirme Formu Tanımlama ekranında ekranında RDF Ana Form Tanımı bilgisinin tanımlandığı zorunlu alandır.	

**Sorumlu Kullanıcı Grupları:** Risk Değerlendirme Formu Tanımlama ekranında Sorumlu kullanıcı gruplarının sistemde tanımlı olan kullanıcı grubu listesinden seçilebilgiği alandır. Sorumlu Kullanıcı Grupları” alanında seçim yapılacak kullanıcı grupları ile belirli RDF Ana Formları belirli kullanıcı grupları sorumluları yetkilendirebilirsiniz. Bu sayede kullanıcı grubuna dahil olmayan kişiler bu RDF Ana Formları göremez veya güncelleme işlemleri gerçekleştiremez. Sorumlu Kullanıcı Grupları alanına ilgili  alanı ilgili bu  modülün parametre ayarlarından 11 numaralı  “ Sorumlu kullanıcı grupları üzerinden yetki kontrolü yapılacak mı?” parametresinin parametre değeri”Evet" olarak işaretlenirse bu yetkilendirme işlemi aktif hale gelir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_349.png)

**Sorumlu Personeller:** Risk Değerlendirme Formu Tanımlama ekranında Risk Ana Form üzerinde sorumlu olacak personellerin seçildiği alandır. Bu alanda ilgili modülün 19 numaralı “Sorumlu personeller seçilsin mi?(E/H)” parametresini parametre değeri “Evet” seçilerek parametre aktif edildiğinde görüntülenmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_350.png)

**Otomatik Kod Şablonu:** Risk Değerlendirme Formu Tanımlama ekranında Otomatik kod şablonu bilgisi tanımlandığı alandır. Bu alan ile  ilgili Risk Ana Formu içerisine Risk  Ana Form Detay kayıtları eklendiğinde bu detay kayıtların kodunun nasıl olacağını belirlenir.Ör:[RDFD].001, [RDFD.002], [RDFD].003  otomatik kod sayac değeri “0” göre sistem otomatik kod ataması yapacaktır.	 

**Otomatik Kod Sayacı:** Risk Değerlendirme Formu Tanımlama ekranında otomatik kod şablonunda belirlenen koda göre verilen Risk  Ana Form Detay kayıtlarının kodunun hangi değerden başlayacağı belirlenir.

Risk Değerlendirme Formu Tanımlama ekranında Risk Ana Formun kodunu (eğer otomatik kod verme aktif edilmemişse) kod bilgisi, formun tanımını ve istenirse sorumlu kullanıcı grupları eklenir. Gerekli alanlar ilgili bilgiler girildikten sonra ekranında sol üst köşesindeki  ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_351.png) butonu tıklanarak Risk Ana Formun tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_352.png)

Sistem tarafından “İSG Risk Değerlendirme Formunu kaydetmek ister misiniz?” mesajında “Tamam” butonu tıklanarak Risk Değerlendirme Formu kaydedilir. Ana Form tanımlama ekranlarında, kullanıcıların kurumuna özgü tutulması gereken bilgiler mevcut ise istenilen kadar özel alan eklemesi sunulan arayüzler aracılığı ile yapılabilmektedir.Kullanıcının kuruma özgü alanları Alan Tanımlama menüsünde  ile tanımlanıp, Fonksiyon Dizanyer menüsünde 3 numaralı “Risk Değerlendirme Formu Tanımlama” fonksiyonu sayfalarıyla ilişkilendirilip, görüntülenmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_353.png)

Bu şekilde bütün Risk Değerlendirme Formları (RDF’ler)  tanımlandıktan sonra, risk detayı eklemek istenen Risk Değerlendirme Formu  seçili iken sol üstteki butonlardan ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_354.png)butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_355.png)

Risk Değerlendirme Formu Detayı (RDFD) ekranına açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_356.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_357.png):Yeni RDFD (Risk Değerlendirme Form Detayı)  tanımlanabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_358.png):Listede seçili RDFD bilgisi güncellenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_359.png):Listede seçili RDFD bilgisi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_360.png):Listede seçili olan RDFD bilgisi kopyalanabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_361.png): Listede seçili olan RDFD bilgisini silmek için kullanılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_362.png):Listede seçili olan RDFD bilgisi revize edilerek onaya gönderilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_363.png):Listede seçili RDFD bilgisinin eski revizyonları izlenebilme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_364.png):Listede seçili RDFD bilgisinin revizyon değişim işlemi  yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_365.png): Listede seçili RDFD bilgisi gözden geçirilme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_366.png): Listede seçili RDFD bilgisi için eski gözden geçirmeler izlenebilme işlemi yapılır.

![ref74]:Listede seçili RDFD bilgisinin sıra numarası değiştirme işlemi yapılır. Risk Değerlendirme Formu-Detaylar ekranda liste sekmesinde RDFD seçili iken ![ref74] butonu tıklanılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_367.png)

Açılan Sıra Numarası Değiştir ekranında Yeni Sıra Numarası bilgisi belirlenerek ![ref75] butonu tıklanırak sıra numarası değiştirme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_368.png)

Risk Değerlendirme Formu - Detaylar ekranında listede seçili RDFD (Risk Değerlendirme Form Detayı)  sıra numarası değiştirme işleminden sonra sıra numarasının değiştirildiği görülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_369.png)

![ref76]:Risk Yetki Matrisi ekranın açılma işlemi yapılır.Tanımlanan Risk Değerlendirme Form Detayların hangi rolün veya kullanıcı grubunun kayıt görme, güncelleme vb. yetkilere sahip olacağının belirlendiği menüdür. Bu buton parametre bağlı olarak görüntülenen bir butondur. İSG Risk Değerlendirme Modülü parametrelerinde 111 numaralı “Detay kayıt bazında yetkilendirme yapılacak mı?” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. Parametre aktif edildikten sonra  Risk Değerlendirme Formu - Detaylar ekranında Yetki matrisi butonu görüntülenir ve İSG Risk Değerlendirme modülünde detay bazında yetkilendirme işlemleri yapılır.

Risk Değerlendirme Formu-Detaylar ekranında  ![ref76] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_370.png)

Risk Yetkisi Matrisi ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_371.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref77]:Risk Yetki matrisi  ekranında  kayıt işlemi yapılır

![ref79]:Risk Yetki Matrisi ekranında sistemde tanımlı kullanıcı grubu listesinde yetki verilmek istenilen kullanıcı grubu ekleme işlemi yapılır.

![ref80]: Risk Yetki Matrisi ekranında yetki verilen listede seçili kullanıcı grubunu silme işlemi yapılır.

Risk  Yetki Matrisi ekranında Roller Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Rol Tanımlama menüsünde tanımlı gelmektedir.Rol tanımları hangi role yetki verilmesi isteniyorsa o role karşılık gelen ilgili yetki check box  işaretlenir ve ![ref77] butonu ile kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_372.png)

Risk Yetki Matrisi ekranında bir kullanıcı grubuna yetki vermek için  ![ref79] butonu tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_373.png)

Açılan sistemde tanımlı kullanıcı grubu listesinde yetki verilmek istenilen kullanıcı grubu seçilir ve ekranın sol üst kösesinde yer alan  ![ref81] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_374.png)

Risk  yetki matrisi ekranında kullanıcı grubu için İSG Risk Değerlendirme Modülünde Risk Değerlendirme Detayı işlemleri için yetkilendirme işlemler için yetki check box’ları işaretlendikten sonra ekranın sol üst köseşinde yer alan ![ref77] butonu tıklanarak kullanıcı grubu bazlı yetkilendirme kayıt işlemi yapılır.Örn:Revizyon, Güncelleme ve  Kopyalama yetkileri gibi ilgili check box işaretlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_375.png)

Yetki verilen kullanıcı grubundan yetkiler alınıp, kullanıcı grubunun yetki matrisinden çıkarılması isteniyorsa ![ref80] butonu kullanılır.

![ref68]: Şablon oluşturmak için kullanılır. Aktarım şablonu bu butonu ile kullanıcının bilgisayarına indirilerek ilgili alanlar doldurulur.

![ref82]: Şablon yüklemek için kullanılır.Kullanıcının bilgisayara indirilip, doldurulan şablon sisteme bu buton ile yüklenir.

Not: Uyarlama çalışmaları sonrasında mevcut Risk Değerlendirme detayları (RDFD’ler)  sisteme toplu olarak aktarılabilmektedir. Bu sebeple alan tanımlama vb. işlemler tamamlandıktan sonra sistemin kullanıma hazır olduğuna karar verildiği takdirde BSAT/Konfigürasyon Ayarları/Yönetici Tanımlama menüsünde bu modülde yönetici olarak belirlenen kullanıcıların Risk Değerlendirme Form -Detaylar ekranında ![ref68]ve ![ref82]butonu çıkmaktadır. Şablon, sistemde tanımlanan alanlara göre otomatik olarak oluşturulmaktadır. ![ref83]butonu ile sistem oluşturulan şablonu bilgisayara indirir. İlgili şablon kullanıcılar tarafından doldurularak ![ref84]butonu ile sisteme yüklendiğinde Risk Değerlendirme Detayları (RDFD’ler) sisteme aktarmış olur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_376.png) : Arama fonksiyonu kullanılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_377.png):Listede seçili  form detayları Excel’ e aktarılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_378.png): Yazdır.Sistem Altyapı Tanımları/ İSG Risk Değerlendirme /Rapor Formatları Tanımlama menüsünde tanımlı kayıt bazında rapor formatlarının seçili görüntülenmesi işlemi sağlanır. Bu buton tıklanarak  Excel ve Pdf formatında kayıt bazında rapor formatı alınır. Kayıt bazında rapor formatı tanımlama işlemi olmadığı sürece ![ref40]   butonu görüntülenmez.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_379.png): Grafik çizmek için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_380.png): Bir önceki ekrana dönmek için kullanılır.

Risk Değerlendirme Fomu-Detaylar ekranında yeni bir Risk Değerlendirme Detayı tanımlamak için   ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_381.png)butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_382.png)

Risk Değerlendirme Formu-Detaylar ekranı açılarak yeni bir risk değerlendirme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_383.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_384.png): Risk Değerlendirme Form Detayı kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_385.png): Risk Değerlendirme Form Detayı onay akışındaki kişiye onaya gönderilir.

**Açılan ekranda ilgili alanlar tanımlanır:**

**RDF Tanımı**: Risk Değerlendirme Formu-Detaylar ekranında RDF(Risk Değerlendirme Formu) bilgisi sistem tarafından otomatik verildiği alandır.	 	 

**RDFD Kodu:** Risk Değerlendirme Formu-Detaylar ekranında Risk Değerlendirme Formu Tanımlama ekranında tanımlanan Otomatik kod şablonu bilgisi göre tanımlanana Risk Değerlendirme Form Detayının kodunu sistem otomatik olarak verdiği alandır. Bu alanda sistem tarafından otomatik  kod ataması yapılır. Bu işlemi yapılması için İSG Risk Değerlendirme Modülü parametrelerinde 3 numaralı “Risk Değerlendirme Detayı Oto Kod Şablonu” parametresine kod şablonu tanımlanır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_386.png) İSG Risk Değerlendirme modülü parametrelerinden 4 numaralı “	Risk Değerlendirme Detayı Sayac” parametresinde tanımlı sayac değerine göre Otomatik kod şablonun kaçıncı değerden başlanacağı belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_387.png)

Örn:Otomatik kod şablonu parametrede RDFD.### olarak tanımlıdır. Sistem 4 numaralı parametredeki “0” sayac değerine göre RDFD.001, RDFD.002, RDFD.003 şeklinde otomatik kod ataması yapar.Parametrede Otomatik kod şablonu ve sayac değerinin tanımlama işlemin ilgili alan aşağıdaki şekilde görüntülenir ve İSG Risk Değerlendirme Detay formu kayıt işleminden sonra kaydedilen formun kodu atanır.	 	

**Revizyon No:** Risk Değerlendirme Formu-Detaylar ekranında sistem tarafından tanımlanana Risk Değerlendirme Form Detayının revizyon no bilgisinin verildiği alandır.

**Revizyon Tarihi:** Risk Değerlendirme Formu-Detaylar ekranında tanımlanan Risk Değerlendirme Form Detayının revizyon tarihi bilgisinin açılan Takvim alanında seçildiği  alandır.	 	

**Risk Kaynağı:** Risk Değerlendirme Formu-Detaylar ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_388.png) butonu tıklanarak açılan sistemde tanımlı Faaliyet bilgisinin seçildiği alandır. İSG  Risk Değerlendirme modülü parametrelerinde 23 numaralı “Risk Kaynağı Kullanılacak mı?” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_389.png)

Parametre aktif edildikten sonra Risk Değerlendirme Formu-Detaylar ekranında  bu alan görüntülenir ve açılan sistemde tanımlı Faaliyet listesinden Faaliyet seçim işlemi yapılır.	   
**Olasılık:** Risk Değerlendirme Formu-Detaylar ekranında tanımlanan Risk Değerlendirme Form Detayının açılır liste tıklanarak açılan liste değerlerinde olasılık değerinin seçildiği alandır.(Kullanıcı tanımlıdır. Alan tanımlama menüsünden puanlı liste tipli parametrik alanın tanımlanması  gereklidir.)	 

**Frekans:** Risk Değerlendirme Formu-Detaylar ekranında tanımlanan Risk Değerlendirme Form Detayının açılır liste tıklanarak açılan liste değerlerinde Frekans değerinin seçildiği alandır.(Kullanıcı tanımlıdır. Alan tanımlama menüsünden puanlı liste tipli parametrik alanın tanımlanması  gereklidir.)	

**Şiddet:** Risk Değerlendirme Formu-Detaylar ekranında tanımlanan Risk Değerlendirme Form Detayının açılır liste tıklanarak açılan liste değerlerinde şiddet  değerinin seçildiği alandır.(Kullanıcı tanımlıdır. Alan tanımlama menüsünden puanlı liste tipli parametrik alanın tanımlanması  gereklidir.)		

**Risk Değeri:** Risk Değerlendirme Formu-Detaylar ekranında tanımlanan Risk Değerlendirme Form Detayının Risk Değeri  alanın değerinin hesaplanarak bilgisi verildiği alandır. (Kullanıcı tanımlıdır. Alan tanımlama menüsünden giriş tipli hesaplanan olarak seçilerek formül alanında formül girişi yapılan  metin tipli parametrik alan tanımlanması gereklidir.)	

**Risk Seviyesi:** Risk Değerlendirme Formu-Detaylar ekranında tanımlanan Risk Değerlendirme Form Detayının Risk seviyesi alanın değerinin hesaplanarak bilgisi verildiği alandır. (Kullanıcı tanımlıdır. Alan tanımlama menüsünden giriş tipli hesaplanan olarak seçilerek formül alanında formül girişi yapılan  liste tipli parametrik alan tanımlanması gereklidir.)

Risk Değerlendirme sekmesinde risk analizi için gerekli olan temel bilgiler ve kullanıcı tanımlı alanlar doldurulur.Gerekli alanlar ilgili bilgiler girildikten sonra ekranın sol üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_390.png) butonu tıklanılır. Risk Değerlendirme detay formu için onay akışı tanımlı ise onaydaki kişinin onayına onaya gönderilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_391.png)

Sistem tarafından “İSG Risk Değerlendirme Formunu  İSG Müdür onayına göndermek ister misiniz?” mesajında “Tamam” butonu butonu  tıklanarak İSG Müdürüne  Risk Değerlendirme  detayı onaya gönderilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_392.png)

Onay akışının kullanıcının bekleyen işlerim sayfasında Risk Değerlendirme Detay Formu “**Onay Bekleyen ISG Risk Değerlendirme Detay Formları**” görevi olarak iş düşer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_393.png)

İlgili görevdeki Form kodu alanındaki link kodu tıklanarak Risk Değerlendirme Formu – Detaylar ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_394.png) **Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_395.png):Risk Değerlendirme Form Detayı red edilme işlemi yapılır.

![ref85]: Risk Değerlendirme Form Detayının onay işlemi yapılır.

Risk Değerlendirme Formu – Detaylar ekranında ![ref85]butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_397.png)


İSG Müdürünün Risk Değerlendirme Form Detayı onaylama işleminden sonra durumu “Tamanlanan/Onaylanan” statüne gelir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_398.png)

Risk Değerlendirme Formu-Detaylar ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_399.png) butonu tıklanarak Risk Değerlendirme işlemleri yapılır. Risk değerlendirme sekmesinde risk analizi için gerekli olan temel bilgiler ve kullanıcı tanımlı alanlar doldurulur. Risk değerlendirme formu doldurulduktan sonra, firmaya ait olan İSG Değerlendirme metodolojisine göre risk seviyesinin belirlenen aralıkları için ana ekranda sarı, kırmızı, yeşil gibi renkli noktalar görülmektedir. Riskler için Süreçler alındıktan ve gerçekleştirildikten sonra revize işleminin de yapılmasıyla risk seviyesi düşürülmekte, daha düşük seviyelerdeki risk aralıklarındaki renklere dönüşmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_400.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_401.png) butonu ile gösterilen Trend sütununda ise ilgili risk kaydının değerinin bir önceki revizyona göre artış, azalış ya da durağan bir trende mi sahip olduğu görülebilir.  Bu ekranda görülen risk ve trend ifadeleri alan tanımlama işlemi gerçekleştirilirken hesaplanan giriş tipine sahip alanlarda belirlenebilir.

Risk Değerlendirme -Detaylar ekranında listede sekmesinde  Risk Değerlendirme Detay seçili iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_402.png) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_403.png)

Risk Değerlendirme Formu-Detaylar ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_404.png)

**Önlemler Sekmesi:** Risk Değerlendirme Formu -Detaylar ekranında Önlemler sekmesinde bulunan risk değerinin azaltılması için Önlemler planlanır. Önlemler sekmesi İSG Risk Değerlendirme Modülü parametrelerinde  61 numaralı “Önlemler  kullanılsın mı?” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_405.png)

Parametre aktif edildikten sonra Risk Değerlendirme Formu-Detaylar ekranında Önlemler sekmesi görüntülenir ve risk kaydı ile ilgili riskin seviyesini düşermek için önlem alınma işlemi yapılır. Önlemler sekmesinin ayrıca aktif olacağı statülerin ayarlama işlemi yapılır. İSG Risk Değerlendirme modülü parametrelerinde 102 numaralı “Önlemler sekmesinin aktif olacağı statü kodları(Virgül ile yazınız)” parametrenin parametre değerine Fonksiyon Dizanyer menüsünde tanımlı olan statü kodları yazılarak , yazılan statü kodlarında bulanan statülerde Önlemler sekmesinin aktif olması sağlanır. Birden fazlan statü için parametre değerinde statü kodları arasında virgül konularak yazılarak tanımlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_406.png)

Risk Değerlendirme Formu-Detaylar ekranında Önlemler sekmesi tıklanılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_407.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref86]:Yeni bir önlem tanımlanır.

![ref87]:Listede seçili önlem bilgisi üzerinde düzenleme ve güncelleme işlemi yapılır.Parametreye bağlı olarak görüntülenen bir butondur.İSG Risk Değerlendirme Modülü parametrelerinde 167 numaralı “Önlemler sekmesinde silme ve güncelleme işlemi yapılabilsin mi?” parametresini parametre değeri “Evet” seçilerek parametre aktif edilir. 

![ref88]

Parametre aktif edildikten sonra bu buton görüntülenir ve seçili önlem bilgisi üzerinde düzenleme ve güncelleme işlemi yapılır.

![ref89]:Listede seçili önlem bilgisi silinir. Parametreye bağlı olarak görüntülenen bir butondur.İSG Risk Değerlendirme Modülü parametrelerinde 167 numaralı “Önlemler sekmesinde silme ve güncelleme işlemi yapılabilsin mi?” parametresini parametre değeri “Evet” seçilerek parametre aktif edilir. 

![][ref88]

Parametre aktif edildikten sonra bu buton görüntülenir ve seçili önlem bilgisinin silinme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_412.png):Listede seçili önlem bilgisi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_413.png):Listede seçili önlem bilgisinde önlem iptal nedeni yazılarak iptal edilir.

Önlemler sekmesinde yeni bir önlem tanımlamak için ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_414.png) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_415.png)Önlemler ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_416.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Referans Tipi:** Önlemler sekmesinde Önlem olarak Doküman, DÖF ve Aksiyon seçeneklerinde seçim yapıldığı alandır. 

**Referans tipi Doküman seçildiğinde;**

Referans bilgisi doküman seçildiğinde referans bilgisi alanında ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_417.png) butonu tıklanarak açılan sistemde tanımlı Doküman listesinde seçilir. Doküman Yönetimi Modülünde yüklü olan dokümanlar Doküman listesinde görüntülenir. 

**Referans tipi seçeneği DÖF seçildiğinde;**

DÖF  Kaydının mevcut kayıtlı listeden seçilme veya yeni bir DÖF kaydının tanımlama işlem adımının seçeneğinin yer aldığı alan görüntülenir.”Listeden seç” seçeneği seçildiğinde açılan referans tipi alanında sistemde tanımlı DÖF kayıtlarından seçim yapılır.

Listeden Seçme işleminde sistemde tanımlı kapalı DÖF seçilme işlemide yapılır. Bu işlemi yapılması için İSG Risk Değerlendirme Modülü parametrelerinde 160 numaralı “Önlemlerde kapalı Döfler seçilebilsin mi?”parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_418.png)

Parametre aktif edildikten sonra “Listeden Seç” seçeneği seçildiğinde açılan sistemde tanımlı DÖF Listesine kapalı DÖF’lerin  listede yer alması sağlanarak  seçilme işlemin yapılır.

“Yeni Oluştur” seçeneği seçildiğinde açılan DÖF İşlemleri-Yeni Kayıt ekranında yeni bir DÖF kaydının tanımlama işlemi yapılır. İSG Risk Değerlendirme Modülü  parametrelerinde 183 numaralı “Önlemlerde Kullanılacak Döf İşlem Kaynağı?” parametresinin parametre değerine DÖF işlem kaynağının kod bilgisi yazılarak tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_419.png)Tanımlanan İşlem Kaynağı kodu bilgisi Sistem Altyapı Tanımları/DÖF/ DÖF İşlem Kaynağı menüsünde alınır. İSG Risk Değerlendirme modülünde  önlem olarak DÖF alındığında açılan bu DÖF kaydı  parametre tanımlı DÖF İşlem  kaynağına  bağlı olarak açılır.

**Referans tipi seçeneği Aksiyon seçildiğinde;**

Aksiyon  kaydının mevcut kayıtlı listeden seçilme veya yeni bir Aksiyon tanımlama işlem adımın seçeneğinde yer aldığı alan görüntülenecektir.”Listeden seç” seçeneği seçilirse sistemde tanımlı mevcut Aksiyonlardan seçim yapılır. Listeden Seçme işleminde sistemde tanımlı kapalı Aksiyonları seçilme işlemide yapılır. Bu işlemi yapılması için İSG Risk Değerlendirme Modülü parametrelerinde 161 numaralı “Önlemlerde kapalı Aksiyonlar seçilebilsin mi?” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_420.png)

Parametre aktif edildikten sonra “Listeden Seç “ seçeneği seçildiğİnde açılan sistemde tanımlı Aksiyon Listesine kapalı aksiyonları listede yer alması sağlanarak  seçilme işlemin yapılır.

“Yeni Oluştur” seçeneği seçildiğinde açılan Aksiyon Kalemi Planlama-Yeni Kayıt ekranı açılarak yeni bir Aksiyon Kalemi tanımlama işlemi yapılır. İSG Risk Değerlendirme Modülü  parametrelerinde 8 numaralı “Aksiyon - Kaynak Kodu” parametresine tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_421.png)

Aksiyon Kaynak kodu bilgisi Sisyem Altyapı Tanımları/Aksiyon/Aksiyon Kaynak Tanımlama ekranında alınır. İSG Risk Değerlendirme modülünde  önlem olarak Aksiyon alındığında açılan bu aksiyonlar parametre tanımlı aksiyon kaynağına  bağlı olarak açılır.

**Önlem Tipi:** Önlemler sekmesinde Mevcut ve Planlanan seçeneğinde seçim yapıldığı alandır. Mevcut seçiminde önlem olarak  sistemde kayıtlı DÖF ve Aksiyonları seçilir. Planlanan seçim işleminde yeni bir  önlem olarak DÖF Kaydının açılması yada önlem olarak yeni bir Aksiyon tanımlama işleminin yapılması işlemidir.

**Önlem Tarihi:** Önlemler sekmesinde tanımlanacak önlemin tarihinin açılan takvim alanında seçimin yapıldığı alandır.

**Açıklama:** Önlemler sekmesinde tanımlanacak önlemin varsa açıklama bilgisinin yazıldığı alandır.

Örneğin: Önlem türü olarak aksiyon seçilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_422.png)

“Listeden Seç” ve “Yeni Oluştur” seçeneklerinden “Yeni Oluştur” seçeneği seçilerek Aksiyon oluşturulursa aşağıdaki şekilde Aksiyon modülü ile bağlantı kurulur. Aksiyon Kalemi Planlama - Yeni Kayıt ekranı açılır. 

**Aksiyon Bilgileri sekmesi:** Aksiyon ile ilgili bilgilerin girildiği sekmedir.Aksiyonlar ilgili bilgiler yazılarak girilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_423.png)

**Ek Dosyalar Sekmesi:** Aksiyon ile ilgili bir ek dosya varsa sisteme eklendiği sekmedir. İstenirse önlem olarak açılan aksiyonla ilgili ek dosya yükleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_424.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_425.png): Ek dosya sisteme yüklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_426.png): Yüklenen ek dosya bilgisi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_427.png): Yüklenen ek dosya bilgisi silinir.

Yönlendirme tarihçesi sekmesi yönlendirme tarihçesi bilgisinin verildiği sekmedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_428.png)

Aksiyon Kalemi Planlama - Yeni Kayıt ekranında gerekli alanlar ilgili bilgiler girldikten sonra ekranın sol üst köşesindeki ![ref90]butonu tıklanarak Aksiyon Kalemi Planlama kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_430.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_431.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_432.png)

Açılan ekranda referans tipi açılır menüsünden önlemin türü seçilir. (DÖF, aksiyon, doküman, diğer). Daha sonra önlem tipi (mevcut, planlanan) ve önlem tarihi belirlendikten sonra önlemin açıklaması girilir ve ![ref91]butonu tıklanarak kayıt işlemi gerçekleştirilir.Bu şekilde Referans tipi olarak DÖF ve aksiyon seçilirse, QDMS’teki DÖF ve aksiyon modülleri ile bağlantı kurulacaktır. Mevcut açılmış DÖF ve aksiyonlardan herhangi biri önlemle ilişkilendirilebileceği gibi, bu şekilde yeni kayıtta açılabilmektedir. Referans tipi olarak doküman seçilirse, QDMS’teki doküman ağacından doküman seçilir.

**Süreçler sekmesi:** Risk Değerlendirme Formu -Detaylar ekranında risk kaydına sistemde tanımlı süreç ekleme işlemi yapılarak risk kaydının süreçler ilişkilendirilmesi işlemi yapılır. Süreçler sekmesi İSG Risk Değerlendirme Modülü parametrelerinde  127 numaralı “Süreç Kullanılacak mı??” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_434.png)

Parametre aktif edildikten sonra Risk Değerlendirme Formu-Detaylar ekranında Süreçler sekmesi görüntülenir ve risk kaydı Ensemble programında tanımlı süreçler ile ilişkilendirilmesi işlemi yapılır. İSG Risk Değerlendirme parametrelerinde 218 numaralı “Süreçler sekmesinin aktif olacağı statü kodları(Virgül ile yazınız)” parametresine tanımlı statülere göre süreç sekmesinin görüntüleme işlemi yapılır.Statü kodları bilgisi Fonksiyon Dizanyer menüsünde alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_435.png)

Süreçler sekmesinde Risk kaydının bir süreç ile ilişkilendirilme işleminin zorunluluğunun getirilmesi için İSG Risk Değerlendirme parametrelerinde 131 numaralı” Süreç zorunlu olsun” parametresi aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_436.png)

Parametre aktif edildiğine Süreçler sekmesinde süreç ekleme işlemi yapılmadığında Risk kayıdının kayıt işlemi yapılmaz ve kayıt işleminde süreç ekleme işleminin yapılması ile ilgili uyarı mesajı verir.

Risk Değerlendirme Formu-Detaylar ekranında Süreçler sekmesi tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_437.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref92]:Süreç listesinde süreç ekleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_439.png):Listede seçili süreç bilgisi silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_440.png):Listede seçili süreç görüntülenir.

Süreçler sekmesinde yeni bir süreç ekleme işlemi için ![ref92] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_441.png)

Açılan Süreç listesinde süreç seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_442.png) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_443.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_444.png)Süreçler sekmesinde![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_445.png) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_446.png)

Risk kaydı ile ilişkilendirilen süreçin Ensemble programı açılarak  görüntüleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_447.png)

Açılan Ensemble programında ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_448.png) butonu tıklanarak süreçin görsel modelin görüntüleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_449.png)

**Onaycılar Sekmesi:** Risk kaydının onay geçmişi bilgilerinin yer aldığı sekmedir. Bu sekmede risk kaydının onaycıları, onay durumu ve açıklama gibi onay bilgilerine ulaşılır.Risk Değerlendirme Formu-Detaylar ekranında Onaycılar  sekmesi tıklanarak risk kaydını onay bilgileri görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_450.png)

**Kontroller sekmesi:* *Sistem Altyapı Tanımları/İSG Risk Değerlendirme/Kontroller/Kontrol Tanımlama menüsünde tanımlı olan Kontroller bu sekmede risk değerlendirme form detayı ile ilişkilendirilir.Kontrolller sekmesi İSG Risk Değerlendirme Modülü parametrelerinde 95 numaralı “Kontroller sekmesi kullanılsın mı?” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_451.png)

Parametre aktif edildiğinde Risk Değerlendirme Form-Detaylar ekranında Kontroller sekmesi görüntülenir ve risk kaydı ile kontrollerin ilişkilendirilmesi işlemi yapılır.

İSG Risk Değerlendirme parametrelerinde 104 numaralı “Kontroller sekmesinin aktif olacağı statü kodları(Virgül ile yazınız)” parametresine tanımlı statülere göre kontroller sekmesinin görüntüleme işlemi yapılır.Statü kodları bilgisi Fonksiyon Dizanyer menüsünde alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_452.png)

Kontroller sekmesinde Risk kaydının bir kontrolle ile ilişkilendirilme işleminin zorunluluğunun getirilmesi için İSG Risk Değerlendirme parametrelerinde 229 numaralı” Kontrol seçimi zorunlu olsun mu?” parametresi aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_453.png)

Parametre aktif edildiğine Kontroller sekmesinde kontrol  ekleme işlemi yapılmadığında Risk kayıdının kayıt işlemi yapılmaz ve kayıt işleminde kontrol ekleme işleminin yapılması ile ilgili uyarı mesajı verir.Risk Değerlendirme Formu-Detaylar ekranında Kontroller  sekmesi tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_454.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref93]: Yeni bir kontrol ekleme işlemi yapılır.

![ref94]: Listede seçili kontrol bilgisi üzerinde düzenleme ve güncelleme işlemi yapılır.

![ref95]: Listede seçili kontrol bilgisi silinir.

Kontroller sekmesinde  yeni bir kontrol ekleme işlemi için ![ref93] butonu tıklanılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_458.png)Kontroller ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_459.png)

Kontroller ekranında Kontrol alanında ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_460.png) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_461.png)

Kontrol listesine kontrol seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_462.png) butonu tıklanarak kontrol ekleme işlemi yapılır.

Açılan ekranda istenirse ![ref93]butonu tıklanarak yeni bir kontrol tanımlama işlemi yapılarak kontrol listesine ekleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_463.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_464.png)

Kontroller ekranında kontrol ekleme işleminden sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_465.png) butonu tıklanarak kontrol ekleme kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_466.png)

Risk Değerlendirme sekmesi tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_467.png)

Açılan Risk Değerlendirme Formu - Detaylar  ekranında ilgili alanlar  ilgili düzenleme işlemi yapılarak   ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_468.png) butonu tıklanarak onay akışında kişiye Risk Değerlendirme Detayı onaya gönderilir.Sistem tarafından “İSG Risk Değerlendirme Formunu  İSG Müdür onayına göndermek ister misiniz??” mesajında “Tamam” butonu tıklanılır

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_469.png)

**Revizyon İşlemi:** RDFD’ler kaydedildikten sonra herhangi bir anda revizyon işlemine tabi tutulabilir ve yeni risk analizleri gerçekleştirilebilir. Bunun için RDFD listesi açıkken ilgili risk detayı seçilir ve sol üstteki butonlardan ![ref96] butonu tıklanır. Bundan sonraki aşama risk detayını ilk kez doldururken izlenen adımlarla birebir aynıdır. Tek fark, RDFD ekranındayken revizyon numarası bir artacaktır.Revizyon işlemi yapılması için İSG Risk Değerlendirme Modülü parametrelerinde 80 numaralı “Revizyon kullanılacak mı?” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. 

![ref97]

Parametre aktif edildikten sonra Risk Değerlendirme Formu – Detaylar ekranında revizyon işlemi ile ilgili butonlar görüntülenir. Bu butonlar ile revizyon, eski revizyonlar görme ve revizyon değişimi işlemleri yapılır.Revizyon işleminde revizyon tarihinin güncellenip, güncellenmemesi parametre olarak değişmektedir. İSG Risk Değerlendirme modülü parametrelerinde 72 numaralı “Revizyon Tarihi Güncellenebilsin mi?” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_472.png)

Parametre aktif edildiğinde Risk kaydının için revizyon işlemi yapılan ekranda revizyon tarihi ile ilgili değişiklik yapılması sağlanır. Parametrenin parametre değeri “Hayır” seçilerek parametre pasif edildiğinde Risk kaydının revizyon işlemi aşamasında revizyon tarihi alanına müdahele edilemez. 

Risk Değerlendirme Formu – Detaylar ekranında risk kaydı seçili iken ![ref96] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_473.png)

Açılan Risk Değerlendirme Formu – Detaylar ekranında revizyon işlemi için ilgili alanlar üzerinde değişiklik yapılır. Revizyon numarasının  bir artığı görülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_474.png)

Gerekli alanlarla ilgili değişiklik yapıldıktan sonra ekranın sol üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_475.png) butonu tıklanarak revizyon kayıt işlemi yapılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_476.png)

Sistem tarafından “İSG Risk Değerlendirme Formunu kaydetmek ister misiniz?” mesajında “Tamam” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_477.png)

**Eski Revizyonları Görme İşlemi:** Risk Değerlendirme Formu – Detaylar ekranında revizyon işlemi yapılan bir risk kaydı seçili iken butonu tıklanarak risk kaydının eski revizyonun görme işlemi yapılır.

Eski Revizyon görme işlemi yapılması için İSG Risk Değerlendirme Modülü parametrelerinde 80 numaralı “Revizyon kullanılacak mı?” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. 

![][ref97]

Parametre aktif edildikten sonra Risk Değerlendirme Formu – Detaylar ekranda ![ref98] butonu görüntülenir ve seçilen risk kaydının bu buton tıklanarak eski revizyonlarının görüntüleme işlemi yapılır.

Risk Değerlendirme Formu – Detaylar ekranında risk kaydı seçili iken ![][ref98] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_479.png)

Risk Değerlendirme Detay - Eski Revizyonlar ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_480.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref99]:Eski revizyonları görüntüler.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_482.png): Veriler Excel’ e aktarılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_483.png): Önceki ekrana geri dönülür.

Risk Değerlendirme Detay - Eski Revizyonlar ekranında listede risk kaydı seçili iken ![ref99] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_484.png)

Risk Değerlendirme Formu – Detaylar ekranı görüntülenerek Risk kaydının  eski revizyonu görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_485.png)

**Revizyon Değişim İşlemi:** Revizyon işlemi yapılan riskin revizyonlarının karşılaştırılma işleminin yapılmasıdır. Revizyon Değişim işlemi yapılması için İSG Risk Değerlendirme Modülü parametrelerinde 80 numaralı “Revizyon kullanılacak mı?” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. 

![][ref97]

Parametre aktif edildikten sonra Risk Değerlendirme Formu – Detaylar ekranda ![ref100] butonu görüntülenir ve seçilen risk kaydının bu buton tıklanarak risk kaydının revizyon karşılaştırma işleminin yapılması sağlanır.

Risk Değerlendirme Formu – Detaylar ekranında risk kaydı seçili iken![ref100]  butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_487.png)

Açılan Risk Revizyon Karşılaştırma ekranında risk kaydının 0.revizyonu ile 1.revizyonu arasındaki alanlar ilgili değişiklikler görüntülenerek karşılaştırma işleminin yapıldığı görülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_488.png)

**Gözden Geçirme İşlemi :** Mevcut riskler herhangi bir gözden geçirme işlemine tabi tutulabilir ve mevcut durum değerlendirilip açıklamalar yapılabilir. Bunun için RDFD listesi açıkken ilgili risk detayı seçilir ve sol üstteki ![ref101]butonu tıklanarak gözden geçirme işlemi yapılır.Risk kaydında Gözden Geçirme işlemi yapılması için İSG Risk Değerlendirme Modülü parametrelerinde 39 numaralı “Gözden geçirme fonksiyonu kullanılacak mı ? (E/H)parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. 

![ref102]

Parametre aktif edildikten sonra Risk Değerlendirme Formu – Detaylar ekranda ![ref101] butonu görüntülenir ve seçilen risk kaydının bu buton tıklanarak gözden geçirme işlemi yapılır.İSG Risk Değerlendirme modülü parametrelerinde  174 numaralı “Gözden geçirme fonksiyonu için pasif olacak statü kodları(Virgül ile yazınız)” parametrede tanımlı statü kodlarındaki risk kayıtlarına gözden geçirme görevi düşmez. Statü kodları bilgisi Fonksiyon Dizanyer menüsünde alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_491.png)

Risk Değerlendirme Formu – Detaylar ekranında risk kaydı seçili iken ![ref101] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_492.png)

Risk Gözden Geçirme ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_493.png)

Risk Gözden Geçirme ekranında risk kaydının açıklama alanında gözden geçirme işlemi ile ilgili açıklama bilgisi yazılır. Tarih alanında gözden geçirme işlemi tarihi açılan Takvim alanında seçilir. Gerekli alanlar ilgili bilgiler girildikten sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_494.png) butonu tıklanarak gözden geçirme kayıt işlemi yapılır.

**Eski Gözden Geçirme Görme İşlemi:** Mevcut riskler herhangi bir gözden geçirme işlemine tabi tutulabilir ve mevcut durum değerlendirilip açıklamalar yapılabilir. Gözden Geçirme işlemi yapılan risk detayı seçilir ve sol üstteki ![ref103]butonu tıklanarak eski  gözden geçirme işlemlerinin görüntülenmesi sağlanır.Risk kaydında Eski Gözden Geçirmelerin görme  işlemi yapılması için İSG Risk Değerlendirme Modülü parametrelerinde 39 numaralı “Gözden geçirme fonksiyonu kullanılacak mı ? (E/H)parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. 

![][ref102]

Parametre aktif edildikten sonra Risk Değerlendirme Formu – Detaylar ekranda ![ref103] butonu görüntülenir ve seçilen risk kaydının bu buton tıklanarak eski gözden geçirmelerin görme  işlemi yapılır.

Risk Değerlendirme Formu – Detaylar ekranında risk kaydı seçili iken  ![ref103]butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_496.png)

Risk Eski Gözden Geçirmeler ekranı açılır ve eski gözden geçirme işlemleri ile ilgili bilgiler görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_497.png)

**Grafik Çizme İşlemi;** Risk Değerlendirme Formu – Detaylar ekranında Risk kayıtları  seçili iken ![ref104] butonu tıklanarak risk kayıtların grafiklerinin alınma işlemi yapılır. Bu buton parametreye bağlı olarak görüntülenen bir butondur. İSG Risk Değerlendirme modülü parametelerinden 84 numaralı “Risk Değerlendirme detayında grafik çiz fonksiyonu kullanılsın mı?” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_499.png)

Parametre aktif edildikten sonra Risk Değerlendirme Formu – Detaylar ekranında  ![ref104]   butonu görüntülenir ve listede seçili risk kaydının grafiği alınır.

Risk Değerlendirme Formu – Detaylar ekranında risk kaydı seçili iken ![ref104]  butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_500.png)

Revizyon Bazında Risk Durumu Grafiği ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_501.png)

Açılan ekranda alanlar alanında grafiği alınacak alanlar seçilerek ![ref105] butonu tıklanarak risk kaydının grafiğinin alınma işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_503.png)

### **6.2.4.Grafikler**
**Menü Adı:** Entegre Yönetim Sistemi/İSG Risk Değerlendirme/Grafikler 

İSG Risk Değerlendirme Modülünde Grafiklerin görüntülendiği kısımdır.
#### **6.2.4.1.Risk Revizyon Karşılaştırma Grafiği**
**Menü Adı:** Entegre Yönetim Sistemi/İSG Risk Değerlendirme/Grafikler/ Risk Revizyon Karşılaştırma Grafiği

Risk kayıtlarında revizyon karşılaştırılma işlemi yapılarak grafiğinin alındığı menüdür. Risk Revizyon Karşılaştırma Grafiğini almak için, Grafikler menüsünden Risk Revizyon Karşılaştırma Grafiği menüsü tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_504.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref106]: Belirlenen özelliklere göre ekrana grafiği çizdirir.

![ref107] : Grafiği açılır menüden seçilen format türüne ( Excel, JPG, PDF vb. ) dönüştürerek dış ortama aktarır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_507.png)

Açılan ekranda filtre sekmesinden grafik karşılaştırmasını almak istediğimiz alanları doldurarak ![ref106] butonu ile istenilen risk revizyon karşılaştırması yapılır. 

Risk Revizyon Karşılaştırma Grafiği ekranında güncel öncesi revizyon sayısı ve X ekseni seçilerek ![ref106]butonu tıklanarak Risk Revizyon Karşılaştırme  grafik oluşturulur. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_508.png)

Risk Revizyon Karşılaştırma Grafiği ekranında ![ref108] butonu tıklanarak açılır listede tıklanarak  “xls” seçeneği seçilerek  Risk Revizyon Karşılaştırma Grafiğinin Excel formatında raporu alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_510.png)

#### **6.2.4.2.En Çoklar Analizi**
**Menü Adı:** Entegre Yönetim Sistemi/İSG Risk Değerlendirme/Grafikler/ En Çoklar Analizi

X ekseninde yer alan seçim tiplerine göre grafik oluşturulmasını sağlar. Oluşturulan bu grafik için de veri seçenekleri kullanılarak detay bazlı filtreleme yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_511.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref109]: Belirlenen özelliklere göre ekrana grafiği çizdirir.

![ref110] : Grafiği açılır menüden seçilen format türüne (png,jpg,bmp,xls, vb. ) dönüştürerek dış ortama aktarılma işlemi yapılır.

![ref48]: Veriler Excel’ e aktarılabilir.

Grafik oluşturmak için iki ayrı ayar alanı bulunmaktadır. Bunlar Grafik ve Veri seçenekleridir. Adından da anlaşılacağı gibi grafiğin renkleri, eni-boyu gibi ayarlamaların yapıldığı alandır. Grafik ayarlarında önemli olan X ekseni ve Y eksenidir. X ekseninden sorgulamak istediğimiz, olasılık, Şiddet, Frekans vb. konulara göre grafik elde etmemizi sağlar. Y Ekseninden ise ilgili sorgunun sayı miktarı olan adet ve Z eksenine göre istenen seçeneğe göre grafiğinin raporunun alınması sağlanır.Veri Seçeneklerinden ise belirlediğimiz grafik ayarlarından daha kısıtlı bir veri almak için filtreleme yapmak istenirse kullanılan alandır. Bar üzerine adet bilgisi yazılsın check box işaretlendiğinde grafikte bar üzerine adet bilgiside görüntülenir.Ayarlamalar tamamlandıktan sonra ![ref109] butonu tıklanarak grafik oluşur. Grafiği farklı formatlara almak istenirse, formatı sağdan seçtikten sonra![ref110]  soldan butona basıldığın da xls, png, jpg. Formatlarına grafik basılabilir. ![ref48]  butonu ile de oluşan verileri Excel’e aktarması sağlanır. Bu veriler ile farklı formattaki grafiklerde oluşturulabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_514.png)![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_515.png) 

En çoklar Analizi ekranında![ref48]  butonu tıklanarak En çoklar Analizi Grafiği Excel formatında alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_516.png)
#### **6.2.4.3.Risk Dağılım Matrisi**
**Menü Adı:** Entegre Yönetim Sistemi/İSG Risk Değerlendirme/Grafikler/ Risk Dağılım Matrisi

Risk Dağılım Matrisi Grafiğini almak için, Grafikler menüsünden Risk Dağılım Matrisi menüsü tıklanır. Amaç; hangi aralıkta risklerin daha yoğun olduğunu hangilerinde daha az olduğunu görmektir. Filtre sekmesinden kullanılan grafik türü seçilerek, varsa ilgili alanları belirtilerek risk dağılım matrisi elde edilir. Bu matris ile hangi risk skalasından kaç adet risk olduğu belirtilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_517.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref48]: Veriler Excel’ e aktarılabilir.

![ref47]: Kayıtlar filtrelenerek arama yapılabilir.

Risk Dağılım Matrisi ekranında![ref48]  butonuna basılırsa, sistem otomatik olarak Risk Dağılım Matrisi grafiğini oluşturup kullanıcıya Excel formatında sunmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_518.png)
#### **6.2.4.4.Risk Karşılaştırma Grafiği**
**Menü Adı:** Entegre Yönetim Sistemi/İSG Risk Değerlendirme/Grafikler/ Risk Karşılaştırma Grafiği

Risk karşılaştırma grafiği alınma işleminin yapıldığı menüdür.Risk Karşılaştırma Grafiğini almak için, Grafikler menüsünden Risk Karşılaştırma Grafiği menüsü tıklanır. Bu grafikle, filtrelenen detay formlar üzerindeki iki alanın karşılaştırılabilmesi gibi, yine seçilen alanların güncel ve eski revizyonları görüntülenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_519.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref106]: Belirlenen özelliklere göre ekrana grafiği çizdirir.

![ref107] : Grafiği açılır menüden seçilen format türüne ( Excel, JPG, PDF vb. ) dönüştürerek dış ortama aktarır.

Açılan ekranda filtre sekmesinden grafik karşılaştırmasını almak istediğimiz alanları doldurarak ![ref106] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_520.png)

Risk Karşılaştırma Grafiği ekranda istenilen alanların risk karşılaştırması yapılarak grafiği alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_521.png)

Risk Karşılaştırma Grafiği ekranında ![ref108]  butonu tıklanarak açılır listede tıklanarak  “xls” seçeneği seçilerek  Risk Karşılaştırma Grafiğinin Excel formatında raporu alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_522.png)
### **6.2.5.Raporlar**
**Menü Adı:** Entegre Yönetim Sistemi/İSG Risk Değerlendirme/Raporlar

İSG Risk Değerlendirme Modülünde raporların görüntülendiği kısımdır.
#### **6.2.5.1.Genel Risk Listesi**
**Menü Adı:** Entegre Yönetim Sistemi/İSG Risk Değerlendirme/Raporlar/ Genel Risk Listesi

Genel Risk Raporunun alındığı menüdür.Genel Risk Listesi raporunu almak için, Genel Risk Listesi menüsü tıklanır.Açılan ekranda Liste ve Filtre olmak üzere iki sekme karşımıza çıkar. Filtre sekmesinde arama kriterlerine göre filtreleme işlemi yapılır. Liste sekmesinde ise bu arama kriterleri olan alanlara göre filtreleme işlemine göre kayıtları listelenir. Genel Risk Listesi ekranında Sistem Altyapı Tanımları/İSG Risk Değerlendirme/Rapor Formatları menüsünde Genel bazda rapor formatı tanımlı ise ![ref111] butonu tıklanıldığında bu rapor formatının Excel formatında raporu alınır. Rapor Formatları menüsünde genel bazda rapor formatı tanımlı değilse Genel Risk Listesi ekranında filtre sekmesinde arama kriterlerine göre liste sekmesinde listelenen kayıtların ![ref111] butonu tıklanıldığında Excel formatında raporu alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_524.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref112]:Kayıtlar filtrelenerek arama yapılır.

![ref111]:Veriler Excel’ e aktarılır.

![ref31]:Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref32]:Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref33]:Menü ekranlarında kolonların karşılığı olan alanların gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Genel Risk Listesi  ekranında Filtre sekmesinde filtre arama kriterleri olan “RDF ” alanında ![ref113] butonu tıklanarak açılan  RDF  listesinde RDF seçilerek  ![ref57]  butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_527.png)

Genel Risk Listesi ekranında liste sekmesinde yapılan filtredeki arama kriterlerine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_528.png)

Genel Risk Listesi ekranında ![ref60]  butonu tıklanarak Genel Risk Listesi raporun Excel formatından raporu alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_529.png)
#### **6.2.5.2.Faaliyetler Tarihçesi**
**Menü Adı**: Entegre Yönetim Sistemi/İSG Risk Değerlendirme/Raporlar/ Faaliyetler Tarihçesi

İSG Risk Değerlendirme Modülü kapsamında sistemde tanımlı Faaliyetlerın tarihçe bilgisinin raporun alındığı menüdür. Alınan raporda Faaliyet kodu, Faaliyet Tanımı ve Faaliyet Grubu Tanımı gibi alanların bilgileri görüntülenir. Faaliyetler Tarihçesi raporunu almak için, Raporlar menüsünden Faaliyetler Tarihçesi menüsü tıklanır. Açılan menü ekranında Liste ve Filtre olmak üzere iki sekme karşımıza çıkar. Filtre sekmesinde arama kriterlerine göre filtreleme işlemi yapılır. Liste sekmesinde ise bu arama kriterleri olan alanlara göre filtreleme işlemine göre kayıtları listelenir

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_530.png)**Ekrandaki bulunan butonlar yardımıyla;**

![ref112]:Kayıtlar filtrelenerek arama yapılır.

![ref111]:Veriler Excel’ e aktarılır.

![ref31]:Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref32]:Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref33]:Menü ekranlarında kolonların karşılığı olan alanların gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Faaliyetler Tarihçesi ekranında Filtre sekmesinde filtre arama kriterleri olan “Faaliyet Kodu ” alanında Faaliyet  kodu yazılarak  ![ref57]  butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_531.png)

Faaliyetler Tarihçesi ekranında liste sekmesinde yapılan filtredeki arama kriterlerine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_532.png)

Faaliyetler Tarihçesi ekranında ![ref60]  butonu tıklanarak Faaliyetler Tarihçesi raporun Excel formatından raporu alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_533.png)
#### **6.2.5.3.Faaliyet Grubu Tarihçesi**
**Menü Adı:** Entegre Yönetim Sistemi/İSG Risk Değerlendirme/Raporlar/ Faaliyet  Grubu Tarihçesi

İSG Risk Değerlendirme Modülü kapsamında sistemde tanımlı Faaliyet Grubu  tarihçe bilgisinin raporunun alındığı menüdür. Menüde alınan raporda Faaliyet Grubu kodu, Faaliyet Grubu Tanımı ve Üst Faaliyet Grubu Tanımı gibi alanların bilgileri ulaşılır. Faaliyet Grubu Tarihçesi raporunu almak için, Raporlar menüsünden Faaliyet  Grubu Tarihçesi menüsü tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_534.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref112]:Kayıtlar filtrelenerek arama yapılır.

![ref111]:Veriler Excel’ e aktarılır.

![ref31]:Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref32]:Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref33]:Menü ekranlarında kolonların karşılığı olan alanların gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Faaliyet Grubu Tarihçesi ekranında ![ref60]  butonu tıklanılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_535.png)

Faaliyet Grubu Tarihçesi ekranında Faaliyet Grubu Tarihçesi raporunun Excel formatından raporu alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_536.png)
#### **6.2.5.4.Faaliyetler Raporu**
**Menü Adı:** Entegre Yönetim Sistemi/İSG Risk Değerlendirme/Raporlar/ Faaliyetler  Raporu

İSG Risk Değerlendirme Modülü kapsamında sistemde tanımlı Faaliyetlerin listesinin raporun alındığı menüdür.Menüde alınan raporda Faaliyet kodu, Faaliyet Tanımı ve Faaliyet Grubu gibi alanların bilgilerine ulaşılır. Faaliyetler  Raporunu almak için, Raporlar menüsünden Faaliyetler Raporu menüsü tıklanır. Açılan menü ekranında Liste ve Filtre olmak üzere iki sekme karşımıza çıkar. Filtre sekmesinde arama kriterlerine göre filtreleme işlemi yapılır. Liste sekmesinde ise bu arama kriterleri olan alanlara göre filtreleme işlemine göre kayıtları listelenir

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_537.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref112]:Kayıtlar filtrelenerek arama yapılır.

![ref111]:Veriler Excel’ e aktarılır.

![ref31]:Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref32]:Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref33]:Menü ekranlarında kolonların karşılığı olan alanların gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Faaliyetler Raporu ekranında Filtre sekmesinde filtre arama kriterleri olan “Faaliyet Kodu ” alanında faaliyet  kodu yazılarak  ![ref57]  butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_538.png)

Faaliyetler Raporu ekranında liste sekmesinde yapılan filtredeki arama kriterlerine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_539.png)

Faaliyetler Raporu ekranında ![ref60]  butonu tıklanarak Faaliyetler raporun Excel formatından raporu alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_540.png)
#### **6.2.5.5.Aksiyon Raporu**
**Menü Adı**: Entegre Yönetim Sistemi/ İSG Risk Değerlendirme/ Raporlar/ Aksiyon Raporu

Aksiyon raporunu almak için, raporlar menüsünden aksiyon raporu açılır. İSG Risk Değerlendirme sonucu alınan aksiyon önlemlerinin alındığı rapordur. Bu rapor Excel’ e aktarılabilir. Özet raporu alınabilir. Ayrıca zaman bazlı aksiyon çizelge raporu çekilebilir. Akisyon  raporunu almak için, Raporlar menüsünden Aksiyon Raporu  menüsü tıklanır. Açılan menü ekranında Liste ve Filtre olmak üzere iki sekme karşımıza çıkar. Filtre sekmesinde arama kriterlerine göre filtreleme işlemi yapılır. Liste sekmesinde ise bu arama kriterleri olan alanlara göre filtreleme işlemine göre kayıtları listelenir

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_541.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_542.png): Kayıtlar filtrelenerek arama yapılabilir.

![ref114]: Aksiyon çizelge raporunu görüntüleme işlemi yapılır.

![ref115]: Özet Rapor alınma işlemi yapılır.

![ref116]: Veriler Excel’ e aktarılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_546.png):Log görüntüleme işlemi yapılır.

![ref31]:Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref32]:Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref33]:Menü ekranlarında kolonların karşılığı olan alanların gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

İSG Risk Değerlendirme Aksiyon Raporu ekranında Filtre sekmesinde filtre arama kriterleri olan “RDF ” alanında ![ref113] butonu tıklanarak açılan  RDF  listesinde RDF seçilerek  ![ref57]  butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_547.png)

İSG Risk Değerlendirme Aksiyon Raporu ekranında liste sekmesinde yapılan filtredeki arama kriterlerine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_548.png)

İSG Risk Değerlendirme Aksiyon Raporu ekranında ![ref114]  butonu tıklanarak Aksiyon raporun Excel formatından Aksiyon Çizelge raporu alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_549.png)

İSG Risk Değerlendirme Aksiyon Raporu ekranında ![ref115] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_550.png)

İSG Risk Değerlendirme Aksiyon Raporu ekranında Aksiyon Özet Rapor görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_551.png)

İSG Risk Değerlendirme Aksiyon Raporu ekranında ![ref116]  butonu tıklanılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_552.png)

İSG Risk Değerlendirme Aksiyon Raporu ekranında Aksiyon Raporunu Excel formatında raporu alınır

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_553.png)

İSG Risk Değerlendirme Aksiyon Raporu ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_554.png) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_555.png)

İSG Risk Değerlendirme Aksiyon Raporu ekranında Aksiyon Raporunun Log Görüntüleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_556.png)
#### **6.2.5.6. Tekrar Eden Kayıtlar Raporu**
**Menü Adı:** Entegre Yönetim Sistemi/ İSG Risk Değerlendirme /Raporlar/ Tekrar Eden Kayıtlar Raporu

Benzer risk kayıtlarının kaç kez tekrar ettiğini gösteren raporun alındığı menüdür.Entegre Yönetim Sistemi/ İSG Risk Değerlendirme /Raporlar/Tekrar Eden Kayıtlar raporundan ilgili rapor şablonu seçilir. Tekrar Eden Kayıtlar raporunu almak için, Tekrar Eden Kayıtlar menüsü tıklanır.Açılan ekranda Liste ve Filtre olmak üzere iki sekme karşımıza çıkar. Filtre sekmesinde arama kriterlerine göre filtreleme işlemi yapılır. Liste sekmesinde ise bu arama kriterleri olan alanlara göre filtreleme işlemine göre kayıtları listelenir 

![ref56]

**Ekrandaki bulunan butonlar yardımıyla;**

![ref112]:Kayıtlar filtrelenerek arama yapılır.

![ref111]:Veriler Excel’ e aktarılır.

Tekrar Eden Kayıtlar ekranında Filtre sekmesinde filtre arama kriterleri olan “Rapor Şablonu ” alanında açılan açılır  listede  Rapor Şablonu seçilerek   ![ref57]  butonu tıklanılır.

![ref58]

Tekrar Eden Kayıtlar ekranında liste sekmesinde yapılan filtredeki arama kriterlerine göre kayıtlar listelenir.

![ref59]

Tekrar Eden Kayıtlar ekranında ![ref60]  butonu tıklanarak Tekrar Eden Kayıtlar raporun Excel formatından raporu alınır.

![ref61]
#### **6.2.5.7. Risklerin Bölgelere Dağılımı**
**Menü Adı:** Entegre Yönetim Sistemi / İSG Risk Değerlendirme /Raporlar/Risklerin Bölgelere Dağılımı

İSG Risk Değerlendirme Modülü kapsamında iş yeri ve departman bazlı risklerin haritada gösterilmesinin sağlandığı rapordur. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_557.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref112]: Kayıtlar filtrelenerek arama yapılabilir.

Filtre sekmesinde ilgili işyeri veya departman listesinde seçim yapılarak ![ref112]  butonu tıklanarak Harita sekmesinde işyeri ve departman bazlı risklerin harita üzerinde görüntülenmesi sağlanır.
#### **6.2.5.8.Risk Kontrol Matris Raporu**
**Menü Adı:** Entegre Yönetim Sistemi / İSG Risk Değerlendirme /Raporlar/Risk Kontrol Matris Raporu

Risk kayıtlarında ilişkili kontrollerin raporunun alındığı menüdür. İSG Risk Değelendirme  modülü parametrelerinde 98 numaralı “Risk Kontrol Matrisi Şablon Dosyası” parametresinde tanımlı raporu göre gelmektedir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_558.png)

Parametreye rapor formatı şablonu tanımlamak için öncelikle Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Rapor Formatları Düzenleme menüsünde ilgili rapor ilgi rapor şablonun![ref117] (Yeni) butonu tıklarak yükleme işlemi yapılır. Rapor Formatları Düzenleme meüsüne yüklenen rapor formatı şablonun adı ve uzantısı sağ tıkla/kopyala yönetimi  ile birlikte ilgili parametrenin parametre değerine sağ tıkla/ yapıştır  yöntemi ile yapıştırılarak tanımlama işlemi yapılır. Tanımlanan rapor formatı şablonuna göre ilgili rapor bu menüden alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_560.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref118]: Veriler Excel’ e aktarılabilir.

Risk Kontrol Matrisi Raporu ekranında Filtre sekmesinde filtre arama kriterleri olan “RDFD Kodu ” alanında RDFD  kodu yazılarak  ![ref118]  butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_562.png)

Risk Kontrol Matrisi Raporu ekranında ![ref119]  butonu tıklanarak Risk Kontrol Matrisi raporun Excel formatından raporu alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_564.png)

### **6.2.6.Risk Değerlendirme Talebi**
**Menü Adı**: Entegre Yönetim Sistemi /İSG Risk Değerlendirme/ Risk Değerlendirme Talebi

Risk Değerlendirme Talebi menüsü kullanılarak herhangi bir personele risk değerlendirme görevi aksiyon olarak açılabilir.Risk Değerlendirme görevi aksiyon işleminin açılması için İlgili modülde risk değerlendirme talebi ile ilgili parametrelerinde öncelikle gerekli ayarlamalarının yapılması gerekmektedir. İSG Risk Değerlendirme Modülü parametrelerinde 16 numaralı “Risk Değerlendirme Talebinde Kullanılacak Ana Aksiyon Kodu ?” parametresinde parametre değerine risk değerlendirme görevinde açılacak aksiyon görevinin hangi plan içersinde tanımlancağının plan kodu tanımlanır.Parametrenin parametre değerine tanımlanacak  Ana Aksiyon Kodu Entegre Yönetim Sistemi /Aksiyon Yönetimi/Planlama menüsünde alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_565.png)

Risk Değerlendirme görevinde açılacak aksiyon süresi bilgisi İSG Risk Değerlendirme Modülü parametrelerinde 17 numaralı “Risk Değerlendirme Talebinde Kullanılacak Aksiyon Süresi ?” parametresinin parametre değerine tanımlanması gerekmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_566.png)

Ayrıca İSG Risk Değerlendirme Modülü parametrelerinde 18 numaralı “Risk Değerlendirme Talebinde Kullanılacak Aksiyonun Tip Kodu ?” parametresinde parametre değerine risk değerlendirme görevinde açılacak aksiyon görevinin kullanılacak aksiyon kalem tipi bilgisi tanımlanır.Parametrenin parametre değerine tanımlanacak  Aksiyon Kalem Tipi bilgisi  Sistem Altyapı Tanımları /Aksiyon /Aksiyon Kalemi Tanımlama  menüsünde alınır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_567.png)Bu parametrelerde gerekli ayarlamalar yapıldıktan sonra bu menüde ilgili kişi ilgili risk değerlendirme aksiyonu açılma işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_568.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref120]:Yeni bir risk değerlendirme talebi tanımlar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_570.png): Listede seçili Risk değerlendirme talebini görüntüler.

![ref112]:Kayıtlar filtrelenerek arama yapılır.

![ref111]:Veriler Excel’ e aktarılır.

![ref31]:Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref32]:Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref33]:Menü ekranlarında kolonların karşılığı olan alanların gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Rsik Değerlendirme Talebi ekranıdnda yeni bir Risk Değerlendirme Talebi tanımlamak için ekranın sol üst köşesindeki ![ref120]butonu tıklanarak Risk Değerlendirme Talebi Tanımlama ekranı açılır.

**Risk Talebi Sekmesi:** Risk Değerlendirme Talebi işlemi ilgili detay bilgilerin girildiği sekmesidir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_571.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Değerlendirecek Kişi:** Risk Değerlendirme Talebi Tanımlama ekranında Değerlendirecek Kişi bilgisinin sistemde tanımlı olan personel listesinden seçilebildiği alandır.

**Talep Açıklama:** Risk Değerlendirme Talebi Tanımlama ekranında Talep Açıklama bilgisinin girildiği alandır.

**Ek Dosyalar Sekmesi:** Risk Değerlendirme Talebi ile ilgili eklenecek ek dosya varsa eklendiği sekmedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_572.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_573.png): Ek dosya sisteme yüklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_574.png): Yüklenen ek dosya bilgisi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_575.png): Yüklenen ek dosya bilgisi silinir.

Risk Talebi sekmesi tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_576.png)

Açılan Risk Talebi ekranında değerlendirecek kişi ve talebin açıklaması girildikten sonra ekranın sol üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_577.png)butonuyla tıklanarak  talep kaydedilir ve ilgili kişiye aksiyon olarak açılır.
## **6.3.Dashboard/İSG Risk Değerlendirme**
**Menü:** Dashboard/İSG Risk Değerlendirme

Qdms sisteminde  kullanıcılara işlemleri, metrikleri, grafikleri ve raporları tek bir ekranda görüntülemelerine olanak sağlayan kısımdır. Dashboard, bilgi akışını ve/veya içeriğini özetlemek amacıyla kullanılan, grafikler ve tablolar yoluyla belirli bir durumu açıklamaya yarayan göstergeler ekranı, iş panosu ve  göstergeler tablosu olarak ifade edilmektedir. Amacı en kısa sürede, en az etkileşim ve düşünme gereksinimi ile gerekli olan bilginin sunulmasıdır.Genelde yönetici konumundaki kişileri sıklıkla kullandıkları ekrandır. Qdms sisteminde İsg Risk Değerlendirme Modülü kapsamında Dashboard özelliği getirilmiştir. Menü görme yetkisine bağlı olarak bu ekran gelmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_578.png)

Dashboard menüsü tıklanıldığında liste ve filtre sekmesi olmak üzere iki sekme karşımıza çıkmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_579.png)

Filtre sekmesinde arama kriterlerine bulunan alanlara göre filtreleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_580.png)

İSG Risk Değerlendirme  modülünde Dashboard ekranında Liste sekmesinde Planlanan Toplam Ana Form, Toplam Detay Form, Açık Kayıtlar ve Kapalı Kayıtlar alanları sabit alanlar olarak ekrana gelerek üzerinde herhangi bir düzenleme işlem yapılmamaktadır.Bu sabit alanlarda toplam ve yüzdelik dilimleri ile bilgileri verilir.

![ref121] 

İSG Risk Değerlendirme modülünde Modül yöneticileri istedikleri grafık tasarlama işlemi yaparak grafik sayısı artırabilirler.

![ref121]

İSG Risk Değerlendirme Modülü  Dashboard ekranında kaç tane grafik olacağı, grafiğin adının ne olacağı, grafiklerin sırasını ne olacağı Z ekseninde, Y ekseninde hangi alanlar olacağı, grafik boyu, grafik eninin ne olacağı ve grafik tipinin ne olacağı gibi ayarlarmalarla grafik tasarlama işlemini yapılır. Bu ayarlamalarının İSG Risk Değerlendirme Dashboard ekranında yapılması için kullanıcının İSG Risk Değerlendirme modülünde Modül Yönetici olarak tanımlı olması gerekir. (Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Yönetici Tanımlama  menüsünde İSG Risk Değerlendirme Modülünde modül yönetici tanımlama işlemi yapılır.)

Kullanıcı İSG Risk Değerlendirme Modülünde Modül Yönetici  olmadığında İSG Risk Değerlendirme Dashboard ekranında  aşağıdaki ekran görüntüsündeki buton görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_582.png)

İSG Risk Değerlendirme Modülünde modül Yönetici olarak tanımlı olan kullanıcının İSG Risk Değerlendirme Dashboard ekranında  birinci buton olan ![ref122]  butonu görüntülenir. Modül Admini olan kullanıcı İSG Risk Değerlendirme Dashboard ekranında gerekli  ayarlamaları ![ref122]  butonu yardımıyla grafik tasarlama işlemide yapar.Modül Yöneticileri olmayan kullanıcılar ise Dashboard Konfigürasyonu ekranında Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/ Dashboard Konfigürasyonu/ İSG Risk Değerlendirme menüsünde gerekli ayarlamalar yapılarak grafik tasarım işlemide yapabilirler.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_584.png) İSG Risk Değerlendirme Modülünde grafik tasarlama, listede seçili tasarlanmış grafik  bilgileri güncelleme ve silme işlemleri yapmak için ![ref122]  butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_585.png)

Dashboard Konfigürasyonu ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_586.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref123]:Yeni bir Dashboard tanımlanır.

![ref124]:Listede seçili olan Dashboard bilgisi üzerinde düzeltme/ değişiklik/ güncelleme yapılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_589.png):Listede seçili olan Dashboard bilgisi silinir.

- :Dashboard Konfigürasyonu ekranı kapatılır.

İSG Risk Değerlendirme Modülünde yeni bir Dashboard  ekleme işlemi için  ![ref123]butonu tıklanılır

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_590.png)

Dashboard Konfigürasyonu - Yeni Kayıt ekranında gerekli alanlar ilgili bilgiler doldurulduktan sonra ekranın sol üstte yer alan ![ref125] butonu tıklanılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_592.png)

İSG Risk Değerlendirme Dashboard ekranında kayıt işleminden sonra sistem tarafından “Grafik ayarlarınız başarıyla kaydedilmiştir.” mesajı verilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_593.png)

İSG Risk Değerlendirme Dashboard ekranında tanımlanan Dashboard görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_594.png)

![ref110]  Grafiği aktar butonu tıklanarak grafiği açılır menüden seçilen format türüne (png,jpg,bmp,xls, vb. ) dönüştürerek dış ortama aktarılma işlemide yapılır.

Grafik Boyu min  değeri 500  maxsimum 1000 aralığında sınırlandırılmıştır. Grafik Eni min değeri 550 ve maxsimim değeri 1800 aralığında sınırlandırılmıştır. Bu değerler arasında grafik boyu ve Eni seçilmelidir. Dashboard Konfigürasyonu - Yeni Kayıt ekranında sıra numarası önceden kullanılmışsa kaydetme aşamasında sistem tarafında “Belirtmiş olduğunuz sıra numarası kullanımdadır, kullanımda olmayan bir sıra numarası belirtmelisiniz.”  hata mesajı verilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_595.png) Bu şekilde Grafik Ayarları butonu ile açılan ekranda yeni bir grafik eklenebilir.  Eklenen grafik bilgisi üzerinde düzenleme, güncelleme, değiştirme ve silme işlemleri yapılır. Listede  ilgili grafikler için filtreleme ekranı tanımlanmış ve indirilebilir olarak ayarlanmıştır.

Modül Yöneticileri olmayan kullanıcılar ise Dashboard Konfigürasyonu ekranı Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/ Dashboard Konfigürasyonu/ İSG Risk Değerlendirme menüsünde tıklayarak açılan ekranda gerekli ayarlamalar yapılarak grafik tasarım işlemide yapılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_596.png)

İSG Risk Değerlendirme Dashboard Konfigürasyonu ekranında  aynı butonları kullanarak aynı işlem basamakların yaparak yeni bir Dashboard tanımlama işlemi yapabilirler.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_597.png)


[ref1]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_11.png
[ref2]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_23.png
[ref3]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_26.png
[ref4]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_27.png
[ref5]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_29.png
[ref6]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_38.png
[ref7]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_39.png
[ref8]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_40.png
[ref9]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_41.png
[ref10]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_42.png
[ref11]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_43.png
[ref12]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_44.png
[ref13]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_72.png
[ref14]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_79.png
[ref15]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_84.png
[ref16]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_85.png
[ref17]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_86.png
[ref18]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_91.png
[ref19]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_92.png
[ref20]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_93.png
[ref21]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_96.png
[ref22]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_109.png
[ref23]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_111.png
[ref24]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_114.png
[ref25]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_121.png
[ref26]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_137.png
[ref27]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_139.png
[ref28]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_140.png
[ref29]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_141.png
[ref30]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_145.png
[ref31]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_149.png
[ref32]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_150.png
[ref33]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_151.png
[ref34]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_154.png
[ref35]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_157.png
[ref36]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_159.png
[ref37]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_170.png
[ref38]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_171.png
[ref39]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_172.png
[ref40]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_174.png
[ref41]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_188.png
[ref42]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_189.png
[ref43]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_191.png
[ref44]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_193.png
[ref45]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_204.png
[ref46]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_218.png
[ref47]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_219.png
[ref48]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_220.png
[ref49]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_226.png
[ref50]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_227.png
[ref51]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_229.png
[ref52]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_240.png
[ref53]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_244.png
[ref54]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_251.png
[ref55]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_263.png
[ref56]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_268.png
[ref57]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_269.png
[ref58]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_270.png
[ref59]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_271.png
[ref60]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_272.png
[ref61]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_273.png
[ref62]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_276.png
[ref63]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_277.png
[ref64]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_278.png
[ref65]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_279.png
[ref66]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_280.png
[ref67]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_281.png
[ref68]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_282.png
[ref69]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_285.png
[ref70]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_290.png
[ref71]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_294.png
[ref72]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_295.png
[ref73]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_311.png
[ref74]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_316.png
[ref75]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_318.png
[ref76]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_321.png
[ref77]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_324.png
[ref78]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_325.png
[ref79]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_326.png
[ref80]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_327.png
[ref81]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_330.png
[ref82]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_335.png
[ref83]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_336.png
[ref84]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_337.png
[ref85]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_396.png
[ref86]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_408.png
[ref87]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_409.png
[ref88]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_410.png
[ref89]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_411.png
[ref90]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_429.png
[ref91]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_433.png
[ref92]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_438.png
[ref93]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_455.png
[ref94]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_456.png
[ref95]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_457.png
[ref96]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_470.png
[ref97]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_471.png
[ref98]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_478.png
[ref99]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_481.png
[ref100]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_486.png
[ref101]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_489.png
[ref102]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_490.png
[ref103]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_495.png
[ref104]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_498.png
[ref105]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_502.png
[ref106]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_505.png
[ref107]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_506.png
[ref108]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_509.png
[ref109]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_512.png
[ref110]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_513.png
[ref111]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_523.png
[ref112]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_525.png
[ref113]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_526.png
[ref114]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_543.png
[ref115]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_544.png
[ref116]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_545.png
[ref117]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_559.png
[ref118]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_561.png
[ref119]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_563.png
[ref120]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_569.png
[ref121]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_581.png
[ref122]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_583.png
[ref123]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_587.png
[ref124]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_588.png
[ref125]: https://docsbimser.blob.core.windows.net/imagecontainer/3203cd9a-3c6f-4b8c-97fa-186c7d5e156d_591.png
