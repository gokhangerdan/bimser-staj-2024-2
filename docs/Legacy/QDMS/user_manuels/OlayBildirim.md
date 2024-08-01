---
title: Olay Bildirim
description: Olay Bildirim Yardım Dokümanı
sidebar_position: 30
---

:::tip Bilgi

İlgili konu başlığına sağ tarafta bulunan navigasyon yardımıyla hızlı bir şekilde ulaşabilirsiniz.

:::


**Olay Bildirim Modülü(v.5.26) Kullanıcı Yardım Dokümanı**

Modül Versiyonu: 5.26

## **1.GİRİŞ**

Olay Bildirim Modülü, firmalarda meydana gelen iş sağlığı ve güvenliği, çevre, bilgi güvenliği olayları vb. olayların kayıt altına alınması ve takibi için kullanılmaktadır. İş sağlığı ve güvenliği ve çevre kapsamında meydana gelen ramak kala, iş kazası, çevre kazası gibi olaylar; bilgi güvenliği kapsamında meydana gelen bilgi güvenliği ihlal olayları gibi olayların takibi bu modül ile sağlabilir.


## **2.AMAÇ**

Bu yardım kılavuzunun amacı, QDMS Olay Bildirim Modülünü kullanan kuruluşlara yeni olay girişini ve takibinin nasıl yapıldığının anlatılmasıdır.

## **3.SORUMLULUKLAR**

Yönetim Sistemleri Temsilcisi, İSG / Çevre Uzmanı, Doktor


## **4.KISALTMALAR**

**İSG**: İş Sağlığı ve Güvenliği  


## **5.Olay Bildirim Modülü**
“İş Kazaları” ve “Ramakkala Bildirimleri” sistem üzerinden yapılması, kullanıcıların sistem üzerinden, tanımlanan “İş Kazası” ve Ramakkala” formlarını doldurarak bildirim yapabilmesi kullanıcıların yapmış olduğu bildirimlere statü ve onay seviyeleri tanımlanması, bildirim detayları, kazazede ve yaralanma bilgileri girilmesi,  bu veriler çerçevesinde raporlar alınabilmesi , bildirim tipine göre olayları risk formları ile ilişkilendirebilir, olayın ilişkili olduğu risk formunun tekrar gözden geçirilmesini sağlanaması, Olaylar bildirimler sonucunda ortaya çıkan uygunsuzluklar için QDMS’in DİF ve Aksiyon modülleri ile entegre olarak çalışan önlem takip sistemini kullanılmasını sağlayan modüldür.
### **5.1.Sistem Altyapı Tanımları/Olay Bildirim**
Olay Bildirim Modülünün altyapısını oluşturmak amacıyla gerekli tanımlamaların yapıldığı kısımdır. Yapılan tanımlamalara göre giriş ekranında veriler karşımıza çıkmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_7.png)

#### **5.1.1.Kontroller**
##### **5.1.1.1.Kontrol Tanımlama**
**Menü Adı**: Sistem Altyapı Tanımları/Olay Bildirim/ Kontroller/ Kontrol Tanımlama

Kontroller QDMS'te Risk Modüllerinde kullanılır. Kontroller 27001 EK A maddesinde geçen maddelerdir ve Kontroller sekmesinde gelmektedir.Kontroller sekmesinde her bir olay bildirimi için kontrol adımı seçebilebilir.Kontroller sekmesinde, seçtiğiniz kontrol maddeleri, QDMS ortamında raporlar başlığında SOA raporu almak istediğinizde karşınıza çıkacaktır.Kısaca Kontroller SOA raporunun hazırlanmasında kullanılmaktadır. Olay Bildirim Modülü parametrelerinde  95  numaralı “Kontroller sekmesi kullanılsın mı?” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_8.png) Parametre aktif edildikten sonra Olay Bildirim Formu – Detaylar ekranında  yeni bir olay bildirimi  kaydının tanımlama işleminin yapıldığı yeni kayıt ekranında sekme olarak çıkar. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_9.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref1]:Yeni bir Kontrol tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_11.png):Listede seçili Kontrol bilgisi üzerinde  düzeltme/ değişiklik/ güncelleme yapılır. Kod bilgisi güncellenemez.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_12.png):Listede seçili Kontrol bilgisi silinebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_13.png):Veriler Excel’ e aktarılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_14.png):Kayıtlar filtrelenerek arama yapılabilir.

Kontrol Tanımlama ekranına yeni bir Kontrol eklemek için ekranın sol üst köşesindeki ![ref1]butonu tıklanarak Kontrol Tanımlama\Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_15.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Kontrol  Kodu:** Kontrol Tanımlama ekranında Kontrol kodu bilgisi tanımlandığı zorunlu alandır. Daha önce tanımlamış alanlarla aynı olmayacak şekilde boşluk, Türkçe karakter gibi karakterler kullanmadan tanımlanmalıdır. Ör. ‘001’ , ‘RK’

İlgili modülün 96 numaralı “Kontroller Oto Kod Şablonu”   parametresinde tanımlı kod şablonuna göre sistem otomatik kod şablonu atamasını yapar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_16.png)Tanımlanan oto kod şablonun kaç sayaç değerinde başlayacağı bilgiside ilgili modülün 97 numaralı “Kontroller Sayac” parametresinde parametre değerinde  tanımlı değere göre gelmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_17.png)

Parametre değerinde sayaç değeri “0” olarak tanımlıdır. Kod şablonu KNT.001, KNT.002, KNT.003 şeklinde sistem  kod ataması yapacaktır.

**Bağlı Olduğu Kontrol:** Oluşturulma aşamasında olan Üst Kontrol  bir Kontrol  tanımının alt kırılımı olması halinde bu alan otomatik dolu gelir. Dolu olarak gelen alanda bağlı olduğu Kontrol  tanımının adı yazar. Bağlı olduğu üst kırılım silinmek istenildiğinde sağ yanda bulunan ![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_18.png)  butonu veya değiştirilmek istenildiğinde sağ yanda bulunan ![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_19.png)  butonu kullanılır. Bağlı olduğu bir üst Kontrol yok ise bu alan boş gelir.

**Kontrol  Tanımı:** Kontrol Tanımlama ekranında Kontrol  tanım bilgisinin tanımlandığı zorunlu alandır.

**Açıklama:** Kontrol  Tanımlama ekranında Açıklama bilgisinin girildiği alandır.

**Durum:** Kontrol  Tanımlama ekranında Durum bilgisinin “Aktif” ve “Pasif” seçeneklerinde “Aktif” seçeneğinin seçildiği alandır. Durumu pasif olanlar Kontroller sistemde artık kullanılmadığına bir işarettir. 

Kontrol  Tanımlama ekranında gerekli alanlar doldurulduktan sonra sol üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_20.png)butonu tıklanarak Kontrol  Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_21.png)

Kontrol Tanımlama ekranında Filtre sekmesi ile Kontrol Kodu, Bağlı Olduğu Kontrol ve Kontrol Tanımı gibi alanlara veri girilip, ![ref2]  butonu tıklanarak arama kriterlerine göre filtreleme yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_23.png)
#### **5.1.2.Alan Tanımlama**
**Menü Adı:** Sistem Altyapı Tanımları/ Olay Bildirim /Alan Tanımlama

Olay Bildirim  modülünde Fonksiyon Dizanyer menüsünde bulunan fonksiyonların sayfaları ile ilişki kurulacak alanların tanımlama işleminin yapıldığı menüdür. Bu menüde tanımlanan alanlar alan havuza eklenir. Alan havuzuna eklenen alanlar Fonksiyon Dizanyer menüsünde  bulunan Kaynak  Grubu Tanımlama, KaynakTanımlama,Olay Bildirim Formu Tanımlama, Olay Bildirim ,Önlem Tanımlama ve Kontrol Tanımlama fonksiyonlarının sayfaları ile ilişkilendirme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_24.png)

**Ekrandaki bulunan butonlar yardımıyla;** 

![ref3]:Yeni bir alan eklenir.

![ref4]:Listede seçili alan bilgisi üzerinde değişiklik/düzenleme/güncelleme işlemleri yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_27.png):Listede seçili alan bilgisi kopyalanır.

![ref5]:Listede seçili alan bilgisi silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_29.png):Alanın değerleri tanımlanır.

**Olay Türü Onay Kutusu Tipli Parametrik Alan Tanımlama İşlemi :** Talebe göre tekli veya çoklu seçim yaptırılacak tipte bir liste tipli alan tipidir.

Alan Tanımlama ekranına yeni bir alan eklemek için ekranın sol üst köşesindeki ![ref3]butonu tıklanarak Alan Tanımlama\ Yeni Kayıt ekranı açılır.

![ref6]

Alan Tanımlama-Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_31.png)

**Açılan ekranda ilgili alanlar tanımlanır;**

**Alan Kodu:** Alan Tanımlama-Yeni Kayıt ekranında Alan Kodu bilgisinin girildiği zorunlu alandır. Daha önce tanımlamış alanlarla aynı olmayacak şekilde boşluk, Türkçe karakter gibi karakterler kullanmadan tanımlanmalıdır. Ör. ‘001’ , ‘RK’

**Alan Adı:** Alan Tanımlama-Yeni Kayıt ekranında Alan Adı bilgisinin girildiği alandır. İlgili bayrakların bulunduğu kısımda alan adının dil karşılığı bilgisi yazılır.

**Başlık Notu:** Alan Tanımlama-Yeni Kayıt ekranında alanı veri girişinin yapılması ile ilgili  açıklayıcı bilgi içeren not bilgisinin girildiği alandır. Mouse ile alanın üzerine gelindiğinde görüntülenen bilgidir. İlgili bayrakların bulunduğu kısımda başlık notunun  dil karşılığı bilgisi yazılır.

**Giriş Tipi:** Alan Tanımlama-Yeni Kayıt ekranında giriş tipinin Hesaplanan veya Veri Girişi tipi bilgisinin seçilebildiği alandır. Giriş Tipi seçeneği oluşturulan alanın manuel olarak veri girişi ile mi yoksa hesaplama yöntemi ile mi belirleneceğini gösterir. Örneğin; Veri Girişi.

**Alan Tipi:** Alan Tanımlama-Yeni Kayıt ekranında alan tipinin bilgisinin seçilebildiği alandır. Alan Tipi ise oluşturulan alanın metin, numerik, tarih, liste vb. tiplerinden hangisi olduğunu gösterir. Alan Tipi olarak Onay Kutusu Liste seçilir.

**Seçim Tipi:** Alan Tanımlama-Yeni Kayıt ekranında alan tipinin tekli ve çoklu seçeneklerinde seçim işlemi yapılır.

**Görünme Şartı:** Alan Tanımlama-Yeni Kayıt ekranında Görünme Şartı bilgisinin girildiği alandır. Bir alan eğer başka bir alanın şartına bağlı olarak görülecekse görünme şartı kullanılır. Liste tipli alanın değerlerine göre oluşturulan alanın görüntülenmesini sağlar. Kullanımı [ALANKODU]=ALAN\_DEĞERİ vb. şekildedir. (Örneğin, Fırsat var mı? Alanının  alan kodu 01; Fırsat alanının alan kodu 02 olsun. Eğer “Fırsat” Alanının, “Fırsat var mı?” Alanındaki seçeneklerden değer kodu 100 olan “Evet” değeri seçili ise görülmesi gerekiyorsa 02 numaraları “Fırsat” alanının görünme şartı bölümüne formül şu şekilde yazılmalıdır: [01]=100)

**Durum:** Alan Tanımlama-Yeni Kayıt ekranında durumun “Aktif” veya “Pasif” olarak bilgisinin seçilebildiği alandır. 

**Genişlik:** Alan Tanımlama-Yeni Kayıt ekranında genişlik bilgisinin girildiği alandır.

Açılan Alan Tanımlama-Yeni Kayıt alan kodu ve alan adı bilgisi girilir. Giriş Tipi veri girişi   ve  Alan Tipi seçilir. Durum kısmı seçilir. Alan Tanımlama ekranında gerekli alanlar doldurulduktan sonra sol üst köşedeki ![ref7]butonuna tıklanarak Alan Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_33.png)

Tanımlanan Onay Kutusu liste tipli alanına değer eklemek için Olay Türü alanı seçili iken ![ref8] butonuna tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_35.png)

Alanın değerlerinin tanıtılacağı ekrana gelinir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_36.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref9]:Yeni bir değer tanımlanır

![ref10]:Listede seçili değer bilgisi üzerinde  düzeltme veya güncelleme işlemleri yapılır.

![ref11]:Listede seçili değer bilgisinin silinme işlemi yapılır.

![ref12]: Kayıtlar filtrelenerek arama yapılabilir.

![ref13] : Veriler Excel’ e aktarılabilir.

![ref14]: Şablon indirilir.

![ref15]: Şablon yüklenilir.

Not: ![ref14] ve ![ref15] butonları ile sisteme toplu olarak alan değerleri aktarılabilmektedir. Şablon indirme butonu ile sistemdeki şablon kullanıcının bilgisayarına indirilir. İlgili şablon kullanıcılar tarafından doldurularak şablon yükleme butonu ile sisteme yüklendiğinde şablondaki tüm alan değerleri sisteme aktarılmış olacaktır.

Değerler-Olay Türü ekranında ![ref9] butonuna tıklanarak yeni değer tanımlama işlemine başlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_44.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Tanım:** Değerler-Yeni Kayıt ekranında tanımlanan değerin tanım bilgisi yazıldığı alandır.

**Açıklama:** Değerler-Yeni Kayıt ekranında tanımlanan değerin açıklama bilgisi yazıldığı alandır.. 

**Durum:** Değerler-Yeni Kayıt ekranında tanımlanan değerin durumu aktif veya pasif olarak seçildği alandır.

**Varsayılan:** Değerler-Yeni Kayıt ekranında tanımlanan değerin ilgili liste değerinin varsayılan olarak alanda görünmesini sağlandığı alandır. Bu alanla ilgili check box işaretlendiğinde sistem otomatik olarak alanın değerini seçenek olarak getirir.

**Önlem zorunlu mu?:** Değerler-Yeni Kayıt ekranında tanımlanan değerin  seçili olduğunda Önlemler sekmesinden en az bir önlem girilmesi zorunluğunun getirdiği alandır. İlgili seçenek seçildiğinde Önlemler sekmesinde önlem tanımlama işlemi yapılmadan sistem olay bildirim  kaydını kaydetmez ve önlem tanımlama işlemi yapılacağına dair uyarı mesajı verir.

**Alınacak Önlem Zorunlu mu? :** Değerler-Yeni Kayıt ekranında Değerler-Yeni Kayıt ekranında tanımlanan değer ilgili alınacak önlem alınması istenirse ilgili check box işaretlendiği alandır. İlgili check box işaretlendiğinde alanın değeri seçildiğinde sistem bu değer için alınacak önlem alınmasını zorunluğu getirir. Olay Bildirim kaydı kayıt işleminde alınacak önlem alınmadığında sistem tarafından alınacak önlem alınması ile ilgili uyarı mesajı gelir. Olay Bildirim  Modülü parametrelerinde 133 numaralı “Alınacak Önlemler Kullanılacak mı?” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir.Parametre aktif edildikten sonra Değerler -Yeni Kayıt ekranında bu alan görüntülenir.

**İlişkili Sekme:** Değerler -Yeni Kayıt ekranında alan tanımlamada tanımlı alan havuzundaki sekme tipli alanlar ile değerinin seçilerek ilişki kurulduğu alandır. Fonksiyon Dizanyer münüsünde 4. Numaralı fonksiyonun sayfaları ile alanları ilişkilendirilmesi yapıldığında bu alanda seçim yapıldığında  Olay bildirim formu-detay ekranında Onay kutusu liste tipli alanın değeri ile ilgili check box işaretlendiğinde ilgili sekme görüntülenir. Görüntülenen sekme tıklandığında sekmedeki alanlarda olay bildirim formu-detay ekranında görüntülenir. İlişkili sekme alanı ile ilgili ilişkilendirme işlemi için öncelikle sekme tipli parametrik alanların tanımlama işleminin yapılması gerekmektedir. Sekme Tipli alanın tanımlama işleminde sonra onay kutusu liste tipli alanın değeri ![ref10] butonu tıklanarak tıklanarak ilişkilendirme işlemi yapılır. 

Gerekli alanlar doldurulduktan sonra sol üst köşedeki ![ref16] butonu tıklanarak değer tanımlama kayıt işlemi gerçekleştirilir. Olasılık, şiddet, frekans vb. puanlı liste, liste, arama özellikli liste tipli alanların değer tanımlama işlemleri bu şekilde yapılır. Alan özelliklerine göre bu ekranda değişiklikler olabilmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_46.png)

Değerler -Olay Türü  ekranında diğer değerlerin tanımlama işlemi için ![ref14] ve ![ref15] butonları ile sisteme toplu olarak alan değerleri aktarım  işlemi yapılır.Toplu olarak alan değerlerini aktarım işlemi alanın değerleri birden fazla olduğunda kullanılmaktadır.

Değerler-Olay Türü ekranında ![ref14]  butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_47.png)

Değerler aktarım şablonu bilgisayara indirilir.İndirilen aktarım şablonunda ilgili alanlar ilgili bilgiler yazılarak doldurulur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_48.png)

Değerler-Olay Türü  ekranında ![ref15]butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_49.png)

Dosya Yükle ekranında “Gözat” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_50.png)

Açılan ekranda doldurulan Değerler Aktarım şablonu seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_51.png)

Sistem tarafından “Aktarım işlemi başarıyla tamamlandı.” mesajı verilerek onay kutusu liste alan tipinin değerlerinin aktarım işlemin gerçekleştiği belirtilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_52.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_53.png)

**Sekme Tipli parametrik alan Tanımlama İşlemi:** Mevcut Olay Bildirim  formunda alanların bulunduğu sekmenin haricinde alanların ilişki kurularak içerisinde görülebileceği yeni bir sekme oluşturup kullanılan sekme tipli parametrik alan tipidir.

Alan Tanımlama ekranına yeni bir alan eklemek için ekranın sol üst köşesindeki ![ref3]butonu tıklanarak Alan Tanımlama\ Yeni Kayıt ekranı açılır.

![ref6]

Alan Tanımlama-Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_54.png)

**Açılan ekranda ilgili alanlar tanımlanır;**

**Alan Kodu:** Alan Tanımlama-Yeni Kayıt ekranında Alan Kodu bilgisinin girildiği zorunlu alandır. Daha önce tanımlamış alanlarla aynı olmayacak şekilde boşluk, Türkçe karakter gibi karakterler kullanmadan tanımlanmalıdır. Ör. ‘001’ , ‘RK’

**Alan Adı:** Alan Tanımlama-Yeni Kayıt ekranında Alan Adı bilgisinin girildiği alandır. İlgili bayrakların bulunduğu kısımda alan adının dil karşılığı bilgisi yazılır.

**Başlık Notu:** Alan Tanımlama-Yeni Kayıt ekranında alanı veri girişinin yapılması ile ilgili  açıklayıcı bilgi içeren not bilgisinin girildiği alandır. Mouse ile alanın üzerine gelindiğinde görüntülenen bilgidir. İlgili bayrakların bulunduğu kısımda başlık notunun  dil karşılığı bilgisi yazılır.

**Giriş Tipi:** Alan Tanımlama-Yeni Kayıt ekranında giriş tipinin Hesaplanan veya Veri Girişi tipi bilgisinin seçilebildiği alandır. Giriş Tipi seçeneği oluşturulan alanın manuel olarak veri girişi ile mi yoksa hesaplama yöntemi ile mi belirleneceğini gösterir. Örneğin; Veri Girişi.

**Alan Tipi:** Alan Tanımlama-Yeni Kayıt ekranında alan tipinin bilgisinin seçilebildiği alandır. Alan Tipi ise oluşturulan alanın metin, numerik, tarih, liste vb. tiplerinden hangisi olduğunu gösterir. Alan Tipi olarak Sekme seçilir.

**Görünme Şartı:** Alan Tanımlama-Yeni Kayıt ekranında Görünme Şartı bilgisinin girildiği alandır. Bir alan eğer başka bir alanın şartına bağlı olarak görülecekse görünme şartı kullanılır. Liste tipli alanın değerlerine göre oluşturulan alanın görüntülenmesini sağlar. Kullanımı [ALANKODU]=ALAN\_DEĞERİ vb. şekildedir. (Örneğin, Fırsat var mı? Alanının  alan kodu 01; Fırsat alanının alan kodu 02 olsun. Eğer “Fırsat” Alanının, “Fırsat var mı?” Alanındaki seçeneklerden değer kodu 100 olan “Evet” değeri seçili ise görülmesi gerekiyorsa 02 numaraları “Fırsat” alanının görünme şartı bölümüne formül şu şekilde yazılmalıdır: [01]=100)

**Durum:** Alan Tanımlama-Yeni Kayıt ekranında durumun “Aktif” veya “Pasif” olarak bilgisinin seçilebildiği alandır. 

**Genişlik:** Alan Tanımlama-Yeni Kayıt ekranında genişlik bilgisinin girildiği alandır.

Açılan Alan Tanımlama-Yeni Kayıt alan kodu ve alan adı bilgisi girilir. Giriş Tipi veri girişi   ve  Alan Tipi  sekme seçilir. Durum kısmı seçilir. Alan Tanımlama ekranında gerekli alanlar doldurulduktan sonra sol üst köşedeki ![ref7]butonuna tıklanarak Alan Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_55.png)

Alan Tanımlama menüsünde diğer sekme tipli alanların tanımlama işlemi aynı şekilde yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_56.png)

Alan Tanımlama işleminde tüm sekmelerin tanımlama işleminde sonra “Olay Türü” onay kutusu liste tipli alanın değerleri ile ilgili sekmelerin ilişkilendirme işlemi yapılır.

Bu işlemin yapılması için “Olay Türü” onay kutusu liste tipli alan seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_57.png)butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_58.png)

Açılan Değerler-Olay Türü ekranında onay kutusu liste tipli alanın değerleri seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_59.png)butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_60.png)

Açılan Değerler-Kayıt Güncelleme ekranında ilişkili sekme alanında  alan tanımlamada tanımlanıp alan havuza eklenen sekmelerde Onay kutusu liste tipli alanın değerinin ilişkilendirilme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_61.png)

Değerler-Kayıt Güncelleme ekranında “Olay Türü” onay kutusu liste tipli alanında değerleri ile ilgili alan tanımlamada tanımlanıp alan havuzuna eklenen sekmenin ilişkilendirme işlemi yapıldıktan sonra ekranın sol üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_62.png)butonu tıklanarak değerler kayıt güncelleme işlemi yapılır.Aynı işlem aşamaları yapılarak  “Olay Türü” onay kutusu liste tipli alanın değerleri ile alan tanımlama menüsünde tanıplanıp alan havuzuna eklenen sekmeler ile ilişkilendirme işlemleri yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_63.png)

Tanımlanan alanların Olay Bildirim Formu – Detaylar ekranında görüntülenir. “Olay Türü” onay kutusu liste tipli alanın “İş Kazası” liste değeri  tıklanıldığında ilişkili olan “İş Kazası”  sekmesinin görüntülendiği görülür. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_64.png)

Olay Bildirim Formu – Detaylar ekranında “Olay Türü” onay kutusu liste tipli alanın “Ramak Kala” liste değeri  tıklanıldığında ilişkili olan “Ramak Kala”sekmesinin görüntülendiği görülür. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_65.png)

Olay Bildirim Formu – Detaylar ekranında “Tehlikeli Durum” onay kutusu liste tipli alanın “Tehlikeli Durum” liste değeri  tıklanıldığında ilişkili olan “Tehlikeli Durum”sekmesinin görüntülendiği görülür. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_66.png)

**Alan Tanımlamada Görünme Şartı olarak Alanın Tanımlama işlemi:** Bir alan eğer başka bir alanın şartına bağlı olarak görülecekse görünme şartı kullanılır. Liste tipli alanın değerlerine göre oluşturulan alanın görüntülenmesini sağlar. Kullanımı **[ALANKODU]=ALAN\_DEĞERİ** vb.(Örneğin,”Kazayı/Olayı Gören” alanın alan kodu l38;”Şahitlerin Adı Soyadı”alanın alan kodu L39 olsun. Eğer “Şahitlerin Adı Soyadı”alanının “Kazayı/Olayı Gören” Alanındaki seçeneklerden değer kodu 3651 olan “Var” değeri seçili ise görülmesi gerekiyorsa L39 numaraları “Şahitlerin Adı Soyadı” alanının görünme şartı bölümüne formül şu şekilde yazılmalıdır: [l38]=3651)

1\.Alan Tanımlam menüsünde onay kutusu liste tipli alanın tanımlama işlemi yapılır. Bu işlemin yapılması için öncelikle Alan Tanımlama ekranına yeni bir alan eklemek için ekranın sol üst köşesindeki ![ref3] butonu tıklanarak Alan Tanımlama\ Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_67.png)

Alan Tanımlama-Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_68.png)

Açılan Alan Tanımlama-Yeni Kayıt alan kodu ve alan adı bilgisi girilir. Giriş Tipi  veri girişi   ve  Alan Tipi seçilir. Durum kısmı seçilir. Alan Tanımlama ekranında gerekli alanlar doldurulduktan sonra sol üst köşedeki ![ref7]butonuna tıklanarak Alan Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_69.png)

Tanımlanan  Onay kutususu liste tipli  alanına değer eklemek için  onay kutusu liste tipli alan  seçili iken ![ref8] butonuna tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_70.png)

Alanın değerlerinin tanıtılacağı ekrana gelinir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_71.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref9]:Yeni bir değer tanımlanır

![ref10]: Listede seçili değer bilgisi üzerinde  düzeltme veya güncelleme işlemleri yapılır.

![ref11]: Listede seçili değer bilgisinin silinme işlemi yapılır.

![ref12]: Kayıtlar filtrelenerek arama yapılabilir.

![ref13] : Veriler Excel’ e aktarılabilir.

![ref14]: Şablon indirilir.

![ref15]: Şablon yüklenilir.

Not: ![ref14] ve ![ref15] butonları ile sisteme toplu olarak alan değerleri aktarılabilmektedir. Şablon indirme butonu ile sistemdeki şablon kullanıcının bilgisayarına indirilir. İlgili şablon kullanıcılar tarafından doldurularak şablon yükleme butonu ile sisteme yüklendiğinde şablondaki tüm alan değerleri sisteme aktarılmış olacaktır.

Değerler-Kazayı/Olayı Gören  ekranında ![ref9] butonuna tıklanarak yeni değer tanımlama işlemine başlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_72.png)

Gerekli alanlar doldurulduktan sonra sol üst köşedeki ![ref16] butonu tıklanarak değer tanımlama kayıt işlemi gerçekleştirilir

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_73.png)

Onay kutusu liste tipli alanın ikinci değerinin tanımlama işlemi aynı şekilde yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_74.png)2. Onay kutusu liste tipli alanın değerlerin tanımlama işleminden sonra görünme şartı uygulanacağı “Şahitlerin Adı Soyadı “ personel tipli alanın tanımlama işlemi yapılır. Bu işlemin yapılması için öncelikle Alan Tanımlama ekranına yeni bir alan eklemek için ekranın sol üst köşesindeki ![ref17]butonu tıklanarak Alan Tanımlama\ Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_76.png) Alan Tanımlama-Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_77.png)

Açılan Alan Tanımlama-Yeni Kayıt alan kodu ve alan adı bilgisi girilir. Giriş Tipi veri girişi   ve  Alan Tipi seçilir. Durum kısmı seçilir. [Kazayı/Olayı Gören alanın kodu]=  “Kazayı/Olayı Gören” Alanındaki seçeneklerden değer kodu 3651 olan “Var” değeri seçili ise görülmesi gerekiyorsa  yazılacak şekilde görünme şartı alanı  [l38]=3651  formül bilgi yazılır.Alan Tanımlama ekranında gerekli alanlar doldurulduktan sonra sol üst köşedeki ![ref18]butonuna tıklanarak Alan Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_79.png)

Olay Bildirim Formu – Detaylar ekranında “Kazayı/Olayı Gören Gören”alanıda görünme şartında formülde yazılmayan  alanın değeri seçili olduğunda  ekranın görüntüleme şekli aşağıdaki şekildedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_80.png)

Olay Bildirim Formu – Detaylar ekranında “Kazayı/Olayı Gören Gören”alanıda görünme şartında formülde yazılan alanın değeri seçili olduğunda  ekranın görüntüleme şekli aşağıdaki şekildedir. Ek olarak tanımlanan alanda görünme şartı uygulanan alan liste değeri seçildiğinde aşağıdaki ekran görüntüsünde olduğu gibi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_81.png)

**Alan Tanımlama Tablo Tipli Alanın Tanımlama işlemi:** Tablo tipli alan tanımlama işlemi yapılır.  (Bu tip bir alan eklendikten sonra alan değerleri olarak yeni alan tanımlamalarının yapılması gereklidir.) Olay Bildirim modülünde  Tablo tipli alan tanımlama işlemi için öncelikle Alan tanımlama menüsünde alan tipi Tablo olan alan tanımlama işlemi yapılır. Tablo tipli alanın içerine eklenecek alan tipleri tanımlama işlemi yapılır. Tablo tipli tanımlanan alanın içerisinde bir den fazla alan tipi tanımlama işlemi yapılır. Metin, Liste, Tarih, Personel, Saat gibi alan tiplerinin tanımlama işlemi tablo içerisine eklenecek alan tipleri olarak eklenebilir. Tanımlanan Tablo tipli alanın içerisine oluşturulacak alan tipleri Tablo tipli tanımlanan alanın tanımlama işleminde sonra görüntülenen ![ref19]butonu ile yapılır. ![ref19] butonu tıklanarak istenilen alan tipinde alan tanımlama işlemi yapılarak Tablo tipli alanın içerisinde oluşturulacak alan tipleri belirlenir. Alan Tanımlama işlemi yapılan Tablo tipli alan ve içerisinde alan tiplerinin Olay Bildirim Modülünde Fonksiyon Dizanyer menüsüne fonksiyonlarının ![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_83.png) butonu yardımıyla fonksiyonları ile ilişkilendirilmesi  yapılarak modülün ilgili sayfalarında görüntülemesi işlemi yapılır. Tablo içerindeki alan tiplerin Fonksiyon Dizanyer menüsünde fonksiyonlar ilişkilendirme işleme yapılan ekranda “Gridde göster” ile ilgili check box işaretlemesi gerekir. “Gridde Göster” seçeneği ilgili check box işaretlendiğinde Tablo tipli alanın içerisindeki Tablo tipli alanların gridde gösterilmesi ve Tablo içeresine veri girişi yapılması sağlanılır.

Tablo tipli alanın tanımlama işleminin yapılması için Alan Tanımlama ekranına yeni bir alan eklemek için ekranın sol üst köşesindeki ![ref3]butonu tıklanarak Alan Tanımlama\ Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_84.png)

Alan Tanımlama-Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_85.png)

Açılan Alan Tanımlama-Yeni Kayıt alan kodu ve alan adı bilgisi girilir. Giriş Tipi veri girişi   ve  Alan Tipi  “Tablo” olarak seçilir. Durum kısmı seçilir. Alan Tanımlama ekranında gerekli alanlar doldurulduktan sonra sol üst köşedeki ![ref7]butonuna tıklanarak Alan Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_86.png)

Tablo tipli alanın tanımlama işleminde sonra Tablo içerisine eklenecek alan tipleri tanımlamak için  ![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_87.png)butonuna tıklanılır.  

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_88.png)

Tablo tipli Alanın eklenecek alanların  tanıtılacağı Alan Tanımlama ekranı gelinir.. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_89.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref20]:Yeni bir alan  tanımlanır

![ref21]:Var olan alanda değişiklik yapılmak istenirse kullanılır.

![ref22]: İlgili alanı silmek için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_93.png):Listede seçili alanın kopyalama işlemi yapılır

**Tablo Tipli Alanın İçerisinin Eklenecek Alan Tiplileri Tanımlanır;**

Personel tipli  alan olan “Adı -Soyadı” Alanı tanımlamak için ekranın sol üst köşesindeki  ![ref20]butonuna tıklanarak “Alan Tanımlama/ Yeni Kayıt” ekranı görüntülenir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_94.png)

Açılan Alan Tanımlama-Yeni Kayıt alan kodu ve alan adı bilgisi girilir. Giriş Tipi veri girişi   ve  Alan Tipi  personel seçilir. Durum kısmı seçilir. Alan Tanımlama ekranında gerekli alanlar doldurulduktan sonra sol üst köşedeki ![ref23]butonuna tıklanarak Alan Tanımlama kayıt işlemi gerçekleştirilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_96.png)

Liste Tipli alan olan “Cinsiyet” alanı tanımlamak için ekranın sol  üst köşesindeki ![ref20]butonuna tıklanılır. “ 

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_97.png)

Alan Tanımlama/ Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_98.png)

Açılan Alan Tanımlama-Yeni Kayıt alan kodu ve alan adı bilgisi girilir. Giriş Tipi veri girişi   ve  Alan Tipi  liste seçilir. Durum kısmı seçilir. Alan Tanımlama ekranında gerekli alanlar doldurulduktan sonra sol üst köşedeki ![ref23]butonuna tıklanarak Alan Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_99.png)

Liste tipli alanına değer eklemek için “Cinsiyet” alanı seçili iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_100.png) butonuna tıklanarak alanın değerlerinin tanıtılacağı ekrana gelinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_101.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_102.png) butonuna tıklanarak yeni değer tanımlama işlemine başlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_103.png)

Gerekli alanlar doldurulduktan sonra sol üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_104.png) butonu tıklanarak değer tanımlama işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_105.png)

Liste tipli alanın tüm değerlerin tanımlama işlemi aynı şekilde yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_106.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_107.png)Geri butonu tıklanarak açılan Alan Tanımlama ekranında Tablo tipli alana eklenecek tüm alan tipleri aynı şekilde tanımlanır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_108.png)

Alan tanımlama Tablo tipli parametrik alana eklenecek alan tiplerinin tanımlama işleminde sonra dikkat edilmesi gerken husus Fonksiyon Dizanyer menüsünde  4 numaralı “Olay Bildirim” fonksiyonun sayfaları ile ilişkilendirme işleminde “Gridde Göster” seçeneğinin işaretli olması gerekmektedir. Tablo alan tanımlama işleminde “Gridde Göster” ile ilgili check box işaretlenmediği zaman Tablo içerine veri girişi yapılır ama Tablo içerisideki alan tipleri gridde gösterilmez.

Olay Bildirim Formu – Detaylar ekranında tanımlanan Tablo tipli parametrik alan aşağıdaki şekilde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_109.png)

Olay Bildirim -Detaylar ekranında ![ref24]  butonu tıklanarak “İşcinin;” tanımlı tablo tipli parametrik alanın 1. satır olarak veri girişi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_111.png)

Açılan ekranda Tablo tipli alanın içerisindeki eklenen alan tiplerine 1.satır olarak veri girişi yapılırak ![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_112.png) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_113.png)

Olay Bildirim -Detaylar ekranında ![ref24] butonu tıklanarak  Tablo tipli alana 2.satır   ekleme işlemi aynı şekilde yapılarak satır satır ekleme işlemi alana yapılır.

Olay Bildirim modülünda Alan Tanımlama menüsünde tüm alanların tanımlama işlemi aynı şekilde olur.Alan Tanımlama işleminde yapılırken Giriş Tipi veri girişi olarak seçeği seçildiğinde parametrik alan tipi  metin, liste, nümerik  gibi alan tipleri seçilerek tanımlama işlemi yapılır. Giriş Tipi Hesaplanan olarak seçeneği seçildiğinde ise  Formül Tipi ve Formül alanı görüntülenir. Formül Tipi alanında ilgili alanın Excel ve SQL olarak iki seçenek görüntülenir. Formül Tipinde Excel seçeneği seçildiğinde Excel formüller Alan Tanımlamada tanımlı alan kodlarına bağlı olarak köşeli parantez içerisinde yazılacak şekilde Formül alanı yazılır.Formül Tipi SQL olarak seçildiğinde Bimser Destek Ekibinde yardım alınarak Formül alanına ilgili formül yazılır.Olay Bildirim Modülünde tanımlanacak tüm alanlar tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_114.png)

Alan Tanımlamada tüm alanlar tanımlandıktan sonra Foksiyon Dizanyer menüsünde 22 numaralı “Statü kullanılacak mı?”  parametresine bağlı olarak görüntülenen ![ref25]ve ![ref26] butonları kullanılarak statü , butonların tanımlama işlemi yapılır. Statü ve buton tanımlama işleminde sonra ![ref27] butonu tıklanarak  alanların Fonksiyon Dizanyer menüsünde tanımlı fonksiyonların ilgili sayfalarıyla ilişkilendirilme işlemi yapılır. Bu işlemlerin yapılmasında onay akışı kurgusunun Akış Tanımlama  menüsünde tanımlanıp  ve Alt Modül Tanımlama menüsünde ise  akışların  kontrolün yapılması gerekmektedir.

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
#### **5.1.3.Fonksiyon Dizayner**
**Menü Adı:** Sistem Altyapı Tanımları/Olay Bildirim/ Fonksiyon Dizayner

Fonksiyon Dizayner menüsü ile alan havuzuna eklenen alanlar Olay Bildirm modülünü  istenilen sayfaları ile ilişkilendirilebilir. Bunun için Sistem Altyapı Tanımları/ Olay Bildirim  Modülünün altından Fonksiyon Dizayner menüsüne gelinir. Açılan ekranda Olay modülününde alan eklenebilecek fonksiyonları sıralanacaktır. Bu ekranda Kaynak Grubu Tanımlama, Kaynak Tanımlama, Olay BildirimForm Tanımlama, Olay Bildirim, Önlem Tanımlama ve Kontrol Tanımlama fonksiyonlarında kullanılacak alanlar ve bunların sıralaması ile onay işlemlerindeki hiyerarşi detayı tanımlanır. Bu menüde kullanılacak butonlar Olay Bildirim  modülü parametrelerinden 22 numaralı  “Statü kullanılsın mı?” parametresinin parametre değeri “Evet” seçilerek parametrenin aktif edilmesi bağlı olarak butonlar değişir. Bu parametrenin parametre değeri “Evet” seçilerek parametre aktif edildiğinde ![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_118.png) ve ![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_119.png) butonların menüde gözükür. Ancak 22 numaralı parametrenin  parametre değeri “Hayır” seçilerek parametre pasif olduğu durumlarda sadece ![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_120.png)butonu görünür durumda olur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_121.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref28]: Statü tanımlaama işlemi yapılır.

![ref29]: Buton tanımlama işlemi yapılır.

![ref30] : Alanların ilgili fonksiyon ile ilişkilendirilme işlemi yapılır.

Fonksiyon Dizayn ekranında 4. Numaralı “Olay Bildirim” fonksiyonu seçili iken  ![ref30] butonuna tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_125.png)Alanların ilgili fonksiyonla ilişkilendirilme yapılacağı ekran açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_126.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref31]: Listede seçili fonksiyona yeni bir alan eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_128.png):Listede seçili eklenen fonksiyona eklenen alan bilgisi üzerinde değişiklik ve düzenleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_129.png):Listede seçili eklenen fonksiyona eklenen alan bilgisi silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_130.png) : Önceki ekrana geri dönülür.

Fonksiyon Dizayn - Alanlar – Olay Bildirim  ekranında ![ref31] botunu tıklanarak  Alan Tanımlama -Fonksiyonlar -Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_131.png) ![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_132.png) 

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

Açılan ekranda alan bilgileri listeden seçilir, zorunlu bir alan ise kullanıcının bu alanı doldurmadığında çıkacak mesaj tanımlanır, sıra numarası belirlenir. Aktif statü, Görünür Statü ve Zorunlu Statü durumları seçilir. Zorunlu olup olmadığı, gridde gösterilip gösterilmeyeceği, kolon genişliği belirlenerek gerekli tüm alanlar doldurulduktan sonra ekranın sol üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_133.png) butonu tıklanarak, ilgili alan için fonksiyon ile ilişkilendirme işlemi gerçekleştirilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_134.png) 

Alan Tanımlamada tanımlanıp alan havuzuna eklenen tüm alanların ilgili fonksiyonun sayfaları ile ilişkilendirileme işlemi bu şekilde yapılarak tanımlama işlemi yapılır.Alan Tanımlamada tanımlanıp havuza eklenen tüm alanların ilgili fonksiyonun sayfaları ile ilişkilendirilme yapılarıken ilişkili sekme alanında alanın görüntüleneceği sekme seçilerek o sekmede görüntülenmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_135.png)

Fonksiyon Dizayn - Alanlar – Olay Bildirim ekranında ![ref31] butonu tıklanarak açılan ekranda alan havuza eklenen alanların ilgili fonksiyonla ilişkilendirilme işlemi aşamasında Aktif, Gönür ve Zorunlu statülerin seçim işlemi yapılır. Bu statülerin bu ekran dışında başka bir ekranda seçim işlemi yapılır.  Fonksiyon Dizanyer menüsünde ![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_136.png) botonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_137.png)

Statü Tanımlama - Olay Bildirim ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_138.png)Açılan Statü Tanımlama - Olay Bildirim ekranında ![ref27] butonu tıklanarak Fonksiyon Dizanyer menüsünde ilgili fonksiyonla ilişkilendirilmiş alanların  Aktif, Görünür ve Zorunlu statüleri ilgili check box işaretlenerek belirlenir. Örn: Taslak statüsünde alanları Aktif, Görünür ve Zorunlu statüleri ilgili check box işaretlenerek belirlenir. ![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_139.png)

Statü Tanımlama - Olay Bildirim Taslak aşamasında Aktif, Görünür ve Zorunlu statüleri belirlendikten sonra ekranın sol üst köşesindeki ![ref32] butonu tıklanılır.Tüm Statüler içinde aynı işlem aşaması yapılarak alanların  Aktif,Görünür ve Zorunlu stüleri belirlenir.
#### **5.1.4.Alan Menüsü Tanımlama**
**Menü Adı:** Sistem Altyapı Tanımları/ Olay Bildirim/ Alan Menüsü Tanımlama

Liste tipli alanlara değer eklenmesi için Entegre Yönetim Sistemi altında menü oluşturulmasını sağlayan menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_141.png) 
**Ekrandaki bulunan butonlar yardımıyla;**

![ref33]: Yeni bir menü tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_143.png):Listede seçili menü bilgisi üzerinde düzenleme ve güncelleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_144.png):Listede seçili menü bilgisi silinir.

Listeye yeni bir menü eklemek için ekranın sol üst köşesindeki ![ref33] butonu tıklanarak Menü Tanımlama\ Yeni Kayıt ekranı görüntülenir

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_145.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Menü Adı:** Menü adı bilgisi tanımlanır.

**Alan:** Alan bilgisi açılır liste tıklanarak açılan alan listesinde seçilir.

**Sıra No:** Sıra no bilgisi girilir.

Menü tanımlama ekranında gerekli alanlar doldurulduktan sonra sol üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_146.png) butonu tıklanarak menü tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_147.png)

Menü tanımlaması yapıldıktan sonra Olay Bildirim modülün  Entegre Yönetim Sistemi kısmında menü olarak görüntülenmesi için Sistem Altyapı Tanımları /BSAT/Tanımlar/Yetki Grupları Tanımlama menüsünde menü görme yetkisi verilmelidir.

Yetki Grupları Tanımlama ekranında Yetki Grubu seçili iken ![ref34] butonu tıklanılır.

![ref35]

Açılan QDMS Yönetim Sistemi - Kayıt Güncelle ekranında Menü seçilir. Menü seçildikten sonra ![ref36] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_151.png)

Açılan ekranda ![ref37]butonu tıklandıktan sonra menü görme yetkisinin verilmesi için ![ref38]butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_154.png)Qdms logosu tıklanarak yenile işlemi yapılarak menü görme yetkisi verilen liste tipli alanın menü olarak görüntülenmesi için Olay Bildirim Modülü Entegre Yönetim Sistemi kısmı tıklanarak  görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_155.png)

Entegre Yönetim Sistemi/Olay Bildirim /Vardiya menüsü tıklanılır. Değerler - Vardiya menüsünde  açılır.Açılan menüde liste tipli parametrik alanın tanımlanmış liste değerleri görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_156.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref9]:Yeni bir değer tanımlanır

![ref10]:Listede seçili değer bilgisi üzerinde  düzeltme veya güncelleme işlemleri yapılır.

![ref11]:Listede seçili değer bilgisinin silinme işlemi yapılır.

![ref12]:Kayıtlar filtrelenerek arama yapılabilir.

![ref13] :Veriler Excel’ e aktarılabilir.

![ref14]:Şablon indirilir.

![ref15]:Şablon yüklenilir.

Not: ![ref14] ve ![ref15] butonları ile sisteme toplu olarak alan değerleri aktarılabilmektedir. Şablon indirme butonu ile sistemdeki şablon kullanıcının bilgisayarına indirilir. İlgili şablon kullanıcılar tarafından doldurularak şablon yükleme butonu ile sisteme yüklendiğinde şablondaki tüm alan değerleri sisteme aktarılmış olacaktır.Değerler-Vardiya ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_157.png) butonu tıklanarak manuel değer tanımlama yada toplu aktarım butonları kullanılarak değerlerin  toplu aktarım işlemi yapılır. Bu şekilde liste tipli alanların bu Alan menüsünde menüsü tanımlanır. Tanımlanan menüde yeni değer tanımlama işlemi sağlanılır.
#### **5.1.5.Statü Menüsü Tanımlama**
**Menü Adı**: Sistem Altyapı Tanımları/Olay Bildirim /Statü Menüsü Tanımlama

Tanımlanmış olan statülerde bulunan kayıtları topluca göstermek için menü oluşturma işlemini gerçekleştirmeye sağlayan menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_158.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref3]:Yeni bir statü menüsü tanımlanır.

![ref4]:Listede seçili statü menüsü bilgisi güncellenir.

![ref5]:Listede seçili statü menüsü bilgisi silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_159.png): Bu menüde listelenecek kayıtlara varsayılan filtre uygulama işlemi yapılır.Örnek olarak;

KOD= SICIL\_NO

DEGER=SISTEME\_GIREN  bilgileri girildiğinde bu menüde seçilen statülerde bulunan ve o anda sisteme giren kullanıcının kayıtları listelenir.Bir başka örnek de; 

KOD= ALAN12

DEGER= KULLANICI\_GRUBU

Bilgileri girildiğinde olay  kaydını sadece 12 nolu alanda seçilen kullanıcı grubundaki kullanıcılar görebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_160.png): Menü  üzerinden olay kayıtları listelenirken gridde hangi alanların gösterileceğini ayarlamaktadır.Eğer burada herhangi bir seçim yapılmışsa, varsayılanda fonksiyon Dizayner menüsünde  seçilip listelenen grid kolonları yerine burada seçilen alanlar gride eklenir.

Listeye yeni bir “Statü Menüsü” eklemek için ekranın sağ üst köşesindeki  ![ref3]butonu tıklanarak Menü Tanımlama\ Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_161.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Menü Adı:** Menü Tanımlama-Yeni Kayıt ekranında menü adı bilgisi yazıldığı alandır.

**Statüler:** Menü Tanımlama-Yeni Kayıt ekranında menü olarak tanımlanacak statünün seçildiği alandır.

**Sıra No:** Menü Tanımlama-Yeni Kayıt ekranında sıra nosunun belirlendiği alandır

**Mobilde Göster:** Menü Tanımlama-Yeni Kayıt ekranında menü olarak tanımlanan statünün mobil ortamında görüntülenmesi için ilgili check box işaretlendiği alandır.

Gerekli alanlar doldurulduktan sonra sol üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_162.png)butonu tıklanarak Statü Menüsü Tanımlama işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_163.png)

Statü tanımlaması yapıldıktan sonra Olay Bildirim modülün  Entegre Yönetim Sistemi kısmında menü olarak görüntülenmesi için Sistem Altyapı Tanımları /BSAT/Tanımlar/Yetki Grupları Tanımlama menüsünde menü görme yetkisi verilmelidir.

Yetki Grupları Tanımlama ekranında Yetki Grubu seçili iken ![ref34] butonu tıklanılır.

![ref35]

Açılan QDMS Yönetim Sistemi - Kayıt Güncelle ekranında Statü seçilir. Statü seçildikten sonra ![ref36] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_164.png)

Açılan ekranda ![ref37]butonu tıklandıktan sonra menü görme yetkisinin verilmesi için ![ref38]butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_165.png)Qdms logosu tıklanarak yenile işlemi yapılarak menü görme yetkisi verilen statünün menü olarak  görüntülenmesi için Olay Bildirim Modülü Entegre Yönetim Sistemi kısmı tıklanarak  görüntülenir

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_166.png)

“Tamamlanan İş Kazası Bildirimleri” statüsü menü olarak görüntülenme işleminden sonra  Entegre Yönetim Sistemi/Olay Bildirim/ “Tamamlanan İş Kazası Bildirimleri” menüsü tıklanılır. Açılan ekranda durumu “Tamamlanan İş Kazası Bildirimleri” statüsü olan olay bildirimleri kayıtları görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_167.png) 

Aynı işlem basamakları yapılarak diğer statülerin menü olarak Entegre Yönetim Sistemi kısmında görüntülenmesi sağlanır.
#### **5.2.6. Olay Bildirim  Parametreleri**
**Menü Adı**: Sistem Altyapı Tanımları/ Olay Bildirim  / Olay Bildirim  Parametreleri

Olay Bildirim Modülü için kullanıcıların istek ve ihtiyaçlarına göre çeşitli ayarlamalar yapabildiği ve bunlara göre parametreleri belirlediği (seçebildiği) menüdür. Filtre sekmesinde Modüller alanında Olay Bildirim Modülü seçili olarak gelir ve Liste sekmesinde  Olay Bildirim Modülü parametreleri listelenir. Seçili parametre bilgisi üzerinden  değişiklik yapmak için ![ref39]butonu kullanılır. Filtre sekmesinde parametre no ve parametre tanımı arama kriterlerine göre filtreleme işlemi yapıldığı gibi liste sekmesinde ise gridde parametre no ve tanım alanlara göre de arama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_169.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref39]:Listede seçili parametre üzerinde değişiklik ve düzenleme işlemi yapılır.

![ref2]: Kayıtlar filtrelenerek arama yapılır.

![ref40]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref41]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref42]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip-gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Parametreler ekranında liste sekmesinde 21 numaralı parametreler seçili iken ![ref39] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_173.png)

Açılan parametreler ekranında “Puanlı Listede Açıklama Gösterilsin mi ?(E/H) “parametresinin parametre değeri bilgisi üzerinde değişiklik yapılır. İstenirse parametreler ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_174.png) butonu tıklanarak parametrenin parametre değeri ile ilgili varsayılan değeri bilgisinin gelmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_175.png)

Açılan Parametreler ekranında parametrenin parametre değeri “Evet” seçilerek gerekli alanlar ilgili bilgiler girildikten sonra ekranın sol üst köşesindeki ![ref43]butonu tıklanarak parametre kayıt güncelleme işlemi yapılır

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_177.png)

Parametreler ekranında ![ref39] butonu tıklanarak seçili pasif parametrenin parametre değeri “Evet”seçilerek parametreyi aktif etme, seçili aktif edilenen parametrenin parametre değeri “Hayır” seçilerek parametreyi pasif etme,  seçili parametrenin varsa parametre değeri değiştirme   ve seçili parametrenin varsayılan değeri seçme gibi işlemler yapılır.
#### **5.2.7.E-Posta Ayarları**
**Menü Adı**: Sistem Altyapı Tanımları/ Olay Bildirim/E-Posta Ayarları

Olay Bildirim Modülü kapsamındaki mail bildirimlerinin yapıldığı menüdür. E-Posta Ayarları ekranında, “Olay Bildirim” modülünde hangi aşamasında kimlere mail gönderiminin yapılacağı belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_178.png)

**Ekranda bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_179.png): Listede seçili olan  E-postaları  değeri bilgisi üzerinde düzenleme/değişiklik/güncelleme işlemi yapılır.

![ref44]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref45]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref46]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip-gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

**E- Posta Ayarlarında SMS  bildirimi kullanılacak ise;** 

Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/ Parametreler menüsü tıklanılır. Açılan Parametreler ekranında listelenen Sistem Altyapı Tanımları  modülü parametrelerinde 102 numaralı “SMS bildirimi kullanıcak mı?” parametresinin parametreler ekranında Filtre sekmesinde parametre no alanına parametre numarası yazılarak ![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_183.png)  butonu tıklanarak aratılarak seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_184.png)

Sistem Alyapı Tanımları modülü parametrelerinde 102 numaralı “SMS bildirimi kullanıcak mı?” parametresi seçildikten sonra ![ref47] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_186.png)

Açılan parametreler ekranında parametre değeri “Evet” seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_187.png)

Parametreler ekranında parametre değeri “Evet” seçildikten sonra ekranın sol üstte yer alan ![ref48]  butonu tıklanarak parametreyi aktif etme kayıt işlemi  yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_189.png)

Parametre Aktif edildikten sonra E- Posta Ayarları ekranında SMS bildirimi kullanılması ile ilgili “SMS gitsin mi?” alanı ile ilgili check box görüntülenir.  İlgili check box işaretlenerek E-Posta ayarlarında SMS bildirimi kullanılır.

Hangi basamakta e-posta/ mesaj gitmesi isteniyorsa seçilir ve  ![ref47] butonu tıklanılır. 

Örn:E-Posta Ayarları ekranında “İş Yeri Hekimi (İş Kazası)” basamağı seçilir ve ![ref49]  butonu tıklanılır.  

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_191.png)

Açılan E-Posta Ayarları/ İş Yeri Hekimi (İş Kazası) ekranı görüntülenir. Roller kısmı, e-posta ve mesaj bildiriminin gideceği rolü yani kişiyi göstermektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_192.png)

E-Posta Ayarları/ İş Yeri Hekimi (İş Kazası) ekranında  Rapor formatı alanında Rapor formatları Tanımlama menüsünde kayıt bazlı tanımlı raporları listesi açılır liste tıklanarak görüntülenir. Kullanıcılar bu görüntülenen kayıt bazlı rapor formatlı listesinde rapor seçim işlemi yaparak e- posta olarak rapor formatının gönderilme işlemi yapabilir.

E-Posta Ayarları/ İş Yeri Hekimi (İş Kazası) ekranında  ![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_193.png)  butonu tıklanarak açılan sistemde tanımlı Mesaj Gövdesi listesinde  gönderilecek mesaj gövdesi ilgili listeden seçilir. Yanlış eklenen bir mesaj gövdesini silmek için ise ![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_194.png)  butonu kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_195.png)

Mesaj Gövdesi listesinde mesaj gövdesi seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_196.png) butonu tıklanarak  mesaj gövdesinin içeriği detaylı bir şekilde görüntülenir.
# ![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_197.png)
İlgili roller için gidecek mesaj gövdeleri mesaj gövdesi listesinde  mesaj gövdesi seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_198.png) butonu tıklanarak seçilme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_199.png)

Kime E-Posta gitmesi isteniyorsa, o rolle ilgili “E-Posta Gitsin Mi/ SMS Gitsin Mi” check box ‘ı işaretlenir.Mesaj gitmesi için rolde tanımlı olan kişinin cep telefon numarası personel tanımlama ekranında tanımlı olmalıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_200.png)

E-Posta Ayarları/ İş Yeri Hekimi (İş Kazası) ekranında E-Posta gitmesi  rollerle  ilgili “E-Posta Gitsin Mi/ SMS Gitsin Mi” check box ‘ı işaretlendikten sonra ekranın sol üstte köşede yer alan ![ref50]  butonu tıklanarak E- Posta Ayarları kayıt işlemi gerçekleştirilir.
#### **5.1.8.Rapor Formatları**
**Menü Adı:** Sistem Altyapı Tanımları/Olay Bildirim / Rapor Formatları

Olay Bildirim metotlarına göre farklı rapor formatları tanımlama işleminin yapıldığı menüdür. Olay Bildirim Modülü için rapor formatları tüm kullanıcılar için  farklı kurgulandığı için sabit bir rapor şablonu bulunmuyor. Bu nedenle her rapor için ayrı rapor şablonu sıfırdan hazırlanıyor ve sisteme aktarılma işlemi yapılmaktadır. Olay Bildirim Rapor formatları şablonları tasarlama işleminde Sistem Altyapı Tanımları kısmında altyapısı kurgulanmaktadır. Altyapıda kurgulama işleminde Alan Tanımlama, Fonksiyon Dizanyer ve Rapor Formatları menüleri kullanılmaktadır. Alan Tanımlama menüsünde rapor formatında bulanan alanların tanımlama işlemi yapılır. Fonksiyon Dizanyer da tanımlan bu alanların 4 Olay Bildirim fonksiyonu sayfalarında görüntülenmesi için ilişkisi kurulur. Fonksiyon Dizanyer menüsünde ise  ![ref51]butonu tıklanarak açılan ekranda alan kodların tagleri Rapor formatıda şablonda  alan değerleri kısmına eklenir. Tag ekleme işlemi yapılan Rapor formatı şablonu  sisteme yüklenir. Rapor formatı şablonun sisteme yükleme işlemi Sistem Altyapı Tanımları/BSAT/Konfigürasyon ayarları/Rapor Formatları Düzenleme menüsünde ![ref52] butonu ile yapılır. Sistem Altyapı Tanımları/ Olay Bildirim /Rapor Formatları menüsü tıklanır. Açılan Rapor Formatları menüsünde ![ref52]butonu tıklanılır. Açılan Rapor Formatları ekranında ilgili alana Rapor Formatı şablonun adı yazılır.  Rapor Formatları Düzenleme menüsünde gidilerek sistem yüklenen Rapor formatı şablonu seçilerek adı ve uzantısı sağ tıkla/kopyala yönetimi ile kopyala işlemi yapıldıktan sonra Rapor Formatları ekranındaki Rapor şablonu alanına sağ tıkla/yapıştırma yönetimi ile ilgili alana yapıştır işlemi yapılır. Rapor formatları ekranında Rapor şablon formatı tanımladıktan sonra Rapor şablonu alanında istenilen seçeneğe göre rapor seçimi yapılarak ![ref53] butonu tıklanarak Rapor formatı tanımlama işlemi gerçekleştirilir. Bu menüde Rapor şablonu seçenekleri olarak Form Bazında, Kayıt Bazında ve Genel olmak üzere üç seçene göre rapor formatı alınma işlemi yapılır.Form ve Kayıt bazında tanımlanan rapor formatları Entegre Yönetim Sistemi/ Olay Bildirim / Olay Bildirim Formu - Detaylar menüsünde ilgili butonlar tıklanarak alınır. Kayıt bazında rapor formatı bu menüde ![ref54] butonu tıklanarak alınırken Form bazında rapor formatı ise ![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_206.png)butonu tıklanarak alınmaktadır. Kayıt bazında rapor formatı alınırken rapor formatları menüsünde tanımlanırken “PDF olarak Oluştur” check box işaretlenirse rapor formatının PDF formatında alınma işlemide yapılır. İlgili check box işaretli olmadığında kayıt bazında rapor formatı Excel formatında alınır. Genel bazda tanımlanan rapor formatları ise Entegre Yönetim Sistemi/ Olay Bildirim /Raporlar/Genel Olay Listesi menüsünde ![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_207.png) butonu tıklanarak tanımlanan rapor formatı seçilerek alınır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_208.png) 

**Ekrandaki bulunan butonlar yardımıyla;** 

![ref3]:Yeni bir rapor formatı tanımlanır.

![ref4]:Listede seçili rapor formatı bilgisi üzerinde değişiklik ve güncelleme işlemi yapılır.

![ref5]: Listede seçili rapor formatı bilgisi silinir.

**Kayıt Bazında Rapor Formatı Tanımlama;**

Entegre Yönetim Sistem/ Olay Bildirim / Olay Bildirim Formu - Detaylar ekranında  ![ref54] butonuna basılarak alınan rapor adımları takip ederek rapor şablonu oluşturulabilir. İlk olarak yeni bir Excel dosyası oluşturulur. Dosyanın adına bir isim verilir. İsim verilirken dikkat edilmesi kısım dosya adında boşluk karakterinin olmamasıdır. Örneğin dosya adının " Olay Bildirim Rapor Formatı (Kayıt Bazında).xlsx"  olduğu gibi.


Sistemde tanımlı olan sabit alanlar için dokümanda yer alan  "sabit tagler.txt" dosyasını kontrol edilir. Sistem Altyapı Tanımları/ Olay Bildirim / Alan Tanımlama menüsünde tanımlanan parametrik alanları rapora basabilmek için ise; Sistem Altyapı Tanımları / Olay Bildirim /Fonksiyon Dizayner menüsüne gelerek 4 numaralı fonksiyon olan Olay Bildirim fonksiyonu seçilir. Olay Bildirim fonksiyonu seçili iken sol üstte yer alan ![ref51]butona tıklanır. Açılan ekranda "Şube/Lokasyon" adında bir alanınız olduğunu ve bu alan için "Alan Kodu" alanında ALAN5 ise bu durumda " Şube/Lokasyon " alanını rapora basabilmek için kullanmanız gereken tag  <ALAN5\> şeklinde olacaktır. Eğer rapora eklemek istediğiniz alan liste tipli bir alanda ise, <ALANKODU\_ACK\> şeklinde bir tag kullanmanız gerekiyor. Alanlar tümü “ACK” eki eklenemeyecek ise  <ALANKODU\> şeklinde olur. Kullanılan tag’ların başında ve sonunda herhangi bir boşluk karakteri olmamasına dikkat edilmemesi gerekmektedir. Tüm taglerin bilgisi rapor formatı şablona aşağıdaki formda olduğu gibi yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_209.png)

Rapor şablonunuzu bu bilgiler doğrultusunda hazırladıktan sonra Sistem Altyapı Tanımları/ BSAT/Konfigürasyon Ayarları/ Rapor Formatları Düzenleme menüsünde ![ref52]butonu tıklanarak rapor formatının sisteme aktarma işlemi yapılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_210.png)

Dosya Yükle ekranında Gözat butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_211.png)

Açılan ekranda Rapor formatı şablonu seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_212.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_213.png)

Sisteme aktarılan rapor formatı Rapor Formatları Düzenleme menüsünde seçilir. Seçilen Rapor Formatı uzantısıyla birlikte sağ tıkla/ kopyala komutu yöntemi ile kopyalanır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_214.png)

Sistem Altyapı Tanımları/ Olay Bildirim /Rapor formatları menüsüne gidilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_215.png)Açılan Rapor Formatları ekranında  ![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_216.png)butonu tıklanılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_217.png) Açılan Rapor Formatları ekranında Rapor Tanımı kısmına Raporun adı bilgisi yazılır. Rapor Şablonu alanında Rapor Formatlarında uzantısıyla kopyalanan Rapor formatı bilgisi sağ tıkla/yapıştır komutu ile yapıştırma işlemi yapılır. Rapor Şablonu alanında sisteme aktardığınız şablonun tam adını, uzantısıyla birlikte yazmanız gerekir.  Örneğin rapor formatlı düzenleme menüsünde şablonunuzu "Olay Bildirim Rapor Formatı (Kayıt Bazında).xlsx ismi ile aktardıysanız, Rapor Şablonu alanına “Olay Bildirim Rapor Formatı (Kayıt Bazında).xlsx” yazmanız gerekiyor. Rapor Formatının rapor şablonu alanında  kayıt bazında rapor formatı seçildiğinde “Kayıt Bazında” seçeneği seçilir. Kayıt Bazında rapor formatının Pdf formatından alınmak isteniyorsa “Pdf Olarak Oluştur” alanı ilgili check box işaretlinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_218.png) 

**Açılan ekranda ilgili alanlar tanımlanır:**

**Rapor Tanımı:** Rapor Formatları ekranında Rapor tanımı bilgisinin yazıldığı alandır.

**Rapor Şablonu:** Rapor Formatları ekranında Rapor şablonun adı ve uzantısı bilgisi yazıldığı alandır. (Rapor Formatları Düzenleme menüsünde rapor şablonun yüklenip adı ve uzantısının sağ tıkla/kopyala yöntemi ile kopyalarak  bu alana sağ tıkla/yapıştır yöntemi ile yapıştırma işleminin yapılır.)

**Rapor Tipi:** Kayıt bazında, form bazında ve genel olmak üzere üç seçenek rapor tipi bilgisi seçilebilir. 

- **Kayıt Bazında:** Her bir Olay Bildirim  Detay kaydı ayrı olarak raporlanması talep edildiğinde seçilir. (Entegre Yönetim Sistemi/ Olay Bildirim/  Olay Bildirim Formu - Detaylar ekranında ![ref54]  butonuyla alınır. Kayıt bazında rapor formatı tanımlama işlemi olmadığı sürece ![ref54]   butonu görüntülenmez.)
- **Form Bazında:** Her olay bildirim  formu altındaki Olay Bildirim  Detay kayıtlarının tek bir liste halinde Excel’e aktarıldığı durumlar için seçilir.

(Entegre Yönetim Sistemi / Olay Bildirim / Olay Bildirim Formu - Detaylar  ekranında ![ref55]  butonuyla alınır.)

- **Genel:** Tüm Olay Bildirim  Detay kayıtlarının tek bir Excel’de görülmesi talep edildiği durumda seçilir.

(Entegre Yönetim Sistemi /Olay Bildirim/Raporlar/Genel Olay  Listesi Raporu ekranından ![ref55]   butonu ile alınır.)

**PDF olarak oluştur:** Rapor tipi kayıt bazında seçilen rapor formatlarında Entegre Yönetim Sistemi/Olay Bildirim/ Olay Bildirim Formu - Detaylar ekranında seçilen bir risk kaydının PDF formatı olarak aktarılabilmesi için bu check box’ı işaretlenebilir.

Açılan ekranda tanıtılacak rapor formatlarının isimleri Rapor Tanımı alanına yazılır. Rapor Şablonu alanına ise rapor formatları düzenleme menüsünden kopyalanan dosya adı **uzantısıyla birlikte**  ilgili alana yapıştırılır. Rapor Tanımlama ekranında gerekli alanlar doldurulduktan sonra sol üst köşedeki ![ref56]butonu tıklanarak rapor formatı kayıt bazında  tanımlama kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_221.png)

Tanımlanan kayıt bazında  rapor formatının alınması için Entegre Yönetim Sistemi/ Olay Bildirim/Yeni Kayıt/ Olay Bildirim Formu - Detaylar ekranında  Olay Bildirim  Detay kaydı  seçili iken ![ref57]  butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_223.png) 

Tanımlanan Kayıt Bazında rapor formatı alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_224.png) 

Rapor formatları Tanımlama ekranında Kayıt bazında rapor formatı tanımlama işleminde “Pdf Olarak Oluştur” alanı ile ilgili check box işaretlinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_225.png)

Rapor formatı ekranında ilgili check box işaretlendikten sonra ![ref56]butonu tıklanarak kayıt bazında rapor formatı  kayıt güncelleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_226.png)

Tanımlanan kayıt bazında  rapor formatının Pdf formatından alınması için Entegre Yönetim Sistemi/ Olay Bildirim/ Olay Bildirim Formu – Detaylar ekranında Olay Bildirim  Detay kaydı seçili iken  ![ref57]  butonu tıklanılır

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_227.png) 

Tanımlanan rapor formatının Pdf formatında raporu alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_228.png)

**Form Bazında Rapor Formatı Tanımlama;**

Rapor Formatını Form bazında tanımlama işlemin işlem aşamaları kayıt bazında rapor formatının işlem aşamaları aynı şekilde yapılmaktadır. Rapor formatları menüsünde sadece Rapor Şablonu alanı seçeneklerinden Form seçeneği seçilerek rapor formatı kayıt işlemi yapılır.Rapor Form Şablonu aşağıdaki şekilde gerekli alanlar ilgili Tagler doldurulur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_229.png)

Rapor Formatı şablonu Rapor Formatı Düzenleme menüsüne yüklenir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_230.png)

Rapor Formatları menüsüne tıklanılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_231.png)

Açılan ekranda rapor tanımı alanına rapor formatının adı ve rapor formatları düzenleme menüsünde yüklenen rapor formatı şablonun adı ve uzantısı rapor şablonu alanı kopyala-yapıştır yöntemi ile yapıştırılır. Rapor şablonu alanı seçeneklerinde form bazında seçeneği seçilerek ekranın sol üst köşesindeki ![ref58]butonu tıklanarak rapor formatı form bazında kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_233.png)

Tanımlanan form bazında  rapor formatının alınması için Entegre Yönetim Sistemi/ Olay Bildirim/ Olay Bildirim-Detaylar ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_234.png) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_235.png) 

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_236.png)

**Genel Bazda Rapor Formatı Tanımlama;**

Rapor Formatını Genel bazında tanımlama işlemin işlem aşamaları kayıt bazında rapor formatının işlem aşamaları aynı şekilde yapılmaktadır. Rapor formatları menüsünde sadece Rapor Şablonu alanı seçeneklerinden genel  seçeneği seçilerek rapor formatı kayıt işlemi yapılır.Rapor Form Şablonu aşağıdaki şekilde gerekli alanlar ilgili Tagler doldurulur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_237.png)

Rapor Formatı şablonu Rapor Formatı Düzenleme menüsüne yüklenir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_238.png)

Rapor Formatları menüsüne tıklanılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_239.png)

Açılan ekranda rapor tanımı alanına rapor formatının adı ve rapor formatları düzenleme menüsünde yüklenen rapor formatı şablonun adı ve uzantısı  rapor şablonu alanı kopyala-yapıştır yöntemi ile yapıştırılır. Rapor şablonu alanı seçeneklerinde Genel seçeneği seçilerek ekranın sol üst köşesindeki ![ref58]butonu tıklanarak rapor formatı genel bazında kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_240.png)

Tanımlanana genel rapor formatının görüntülenmesi için Entegre Yönetim Sistemi /Olay Bildirim/Raporlar/Genel Olay  Listesi Raporu ekranı tıklanılır. Açılan ekranda RDFD kodu alanına ![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_241.png) butonu tıklanarak açılan Olay Bildirim Formu – Detaylar listesinde Olay Bildirim Detay Kayıtları seçilerek  ![ref55]  butonu tıklanılır

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_242.png)

Genel Bazda rapor formatının alınma işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_243.png)
##### **5.1.8.1 Olay Bildirim Modülünde  Sabit Tagler Listesi**
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
#### **5.1.9. Onay Akışı Tanımlama**
Değerlendirilen olay bildirim detay kayıtlarının  belirlenen kullanıcılara onaya gitmesi için sistemde onay akışı kurgulanması gereklidir. Modülde statü kullanımı aktifleştirilerek onay akış kurgusu gerçekleştirilir. Bunun için Sistem Altyapı Tanımları/Olay Bildrim/Olay Bildirim Modülü Parametreler menüsü tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_244.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref59]: Listede seçili olan parametre bilgisi üzerinde düzenleme/değişiklik/güncelleme işlemi yapılır.

![ref60]: Kayıtlar filtrelenerek arama yapılır.

![ref61]: Veriler Excel’ e aktarılır.

![ref40]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref41]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref42]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Açılan Parametreler ekranında Parametre No alanına 22 numaralı  parametrenin numarası yazılarak ![ref60] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_248.png)

Parametreler ekranında 22 numaralı “Statü kullanılacak mı?” parametresi seçili iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_249.png)butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_250.png)

Açılan Parametreler ekranında parametrenin parametre değeri “Evet” seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_251.png)

Parametreler ekranında parametre değeri “Evet” seçilerek ekranın sol üst köşesindeki ![ref32]butonu tıklanarak parametre aktif etme kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_252.png)

22 numaralı “Statü kullanılacak mı?” parametresinin aktif edilme işleminden sonra Fonksiyon Dizanyer menüsünde ![ref62] ve ![ref63] olmak üzere iki buton görüntülenir.Fonksiyon Dizanyer menüsünde  ilgili fonksiyon için  ![ref62] butonu ile buton tanımlaması ve ![ref63] butonu ile statülerin tanımlama işlemleri yapılır.

**NOT:** Akış tanımları Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Akış tanımlama ekranından kontrol edilmeli yoksa akışları tanımlanmalıdır. Ayrıca Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Rol Tanımlama ekranından da onay akışları için rol tanımlamaları yapılır. Rol tanımlama işlemlerinde SQL ve QDMS veri tabanı bilgisi gerekeceğinden Bimser Teknik Destek ekibiyle iletişime geçilerek gerekli rol talep edilebilir.

Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Rol Tanımlama menüsü tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_255.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_256.png):Yeni bir rol tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_257.png):Listede seçili rol bilgisi güncellenir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_258.png):Listede seçili rol bilgisi silinebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_259.png):Kayıtlar filtrelenerek arama yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_260.png):Veriler Excel’ e aktarılabilir.

Rol Tanımlama ekranına yeni bir rol eklemek için ekranın sol üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_261.png)  butonu tıklanarak Rol Tanımlama/Yeni Kayıt ekanı açılarak rol tanımlama işlemi yapılır. Rol Tanımlama işlemi yapılan rol seçili iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_262.png) butonu tıklanılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_263.png)

Gerekli alanlar doldurulduktan sonra sol üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_264.png)butonu tıklanarak rol tanımlama kayıt güncelleme işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_265.png)

Olay Bildirim  Modülünde akış tanımlamaları için kullanılacak tüm roller tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_266.png)

Sistem Altyapı Tanımları/ BSAT/ Tanımlar/ Mesaj Gövdesi Tanımlama ekranından modül için yeni mesaj gövdesi tanımlamaları yapılabilir. Ayrıca Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Akış Tanımlama ekranından akış tanımlamaları yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_267.png)

Fonksiyon Dizayner menüsüne gelinir. Statü ve Butonlar adında iki farklı işlem butonu Olay Bildirim fonksiyonu için ilgili menüye gelecektir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_268.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref28]:Statü tanımlama işlemi yapılır.

![ref29]:Buton tanımlama işlemi yapılır.

![ref30] :Alanların ilgili fonksiyon ile ilişkilendirilme işlemi yapılır.

Fonksiyon Dizayner menüsünden 4 numaralı fonksiyon seçili iken  ![ref28]butonu tıklanılarak  fonksiyonun statülerin tanımlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_269.png)

**Ekranındaki bulunan butonlar yardımıyla;**

![ref64]:Yeni bir statü tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_271.png):Listede seçili statü bilgisi güncellenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_272.png):Listede seçili statü bilgisi silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_273.png): Alanlar aktif, görünür ve zorunlu statüleri belirlenir.

![ref65]: Önceki ekrana geri dönülür.

Statü Tanımlama ekranında ![ref64]butonu tıklanarak yeni statü tanımlama ekranına açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_275.png)

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

Açılan ekranda statü kodu, statü adı, akışın başlatılıp başlatılmayacağı, yeni statü, durum, akış tanımı, onay talep mesajı, onay tamam mesajı ve onay ret mesajı veri girişleri yapılarak gerekli alanlar doldurulduktan sonra ekranın sol üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_276.png) botunu tıklanarak statü tanımlama kayıt işlemi Olay Bildirim fonksiyonu  için yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_277.png)

Fonsiyon Dizanyer menüsünde Statü Tanımlama -Olay Bildirim ekranında 4. Numaralı Olay Bildirim fonksiyonu için tüm statülerin tanımlama işlemi aynı şekilde yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_278.png)

![ref65] Geri butonu ile önceki ekrana dönülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_279.png)

Fonksiyon Dizayner menüsünde ilgili fonksiyon için  ![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_280.png)butonu tıklanarak statülerde kullanılacak butonlar tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_281.png)

**Ekranındaki bulunan butonlar yardımıyla;**

![ref66]:Yeni bir buton tanımlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_283.png):Listede seçili buton bilgisi güncellenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_284.png):Listede seçili buton bilgisi silinir.

![ref65]: Önceki ekrana geri dönülür.

Buton Tanımlama ekranında  ![ref66]butonu ile yeni buton tanımlama ekranına açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_285.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Buton Kodu:** Buton Tanımlama -Yeni Kayıt ekranında buton kodu bilgisi yazıldığı alandır.. Daha önce tanımlamış alanlarla aynı olmayacak şekilde boşluk, Türkçe karakter gibi karakterler kullanmadan tanımlanmalıdır.

**Buton Adı:** Buton Tanımlama -Yeni Kayıt ekranında Buton adı bilgisinin yazıldığı alandır.

**Buton Tipi:** Buton Tanımlama -Yeni Kayıt ekranında sistemde tanımlı buton tipi seçenekleri  Onay ve red seçeneklerinde  belirlendiği alandır.

**Görünür Statü:** Buton Tanımlama -Yeni Kayıt ekranında tanımlanan butonun hangi statüde görüntüleneceği belirlendiği alandır.

**Yeni Statü:** Buton Tanımlama -Yeni Kayıt ekranında tanımlanan butona tıkanıldığında hangi statü geçiş yapacağı sistemde tanımlı statülerden seçildiği alandır.

**Durum:** Buton Tanımlama -Yeni Kayıt ekranında tanımlanan butonun durumu aktif veya pasif seçeneklerinden seçildiği alandır.

**Uyarı Mesajı:** Buton Tanımlama -Yeni Kayıt ekranında tanımlanan butona tıklatıldığında ekranda uyarı mesajının bilgisinin girildiği alandır. Örneğin: Onaya göndermek istediğinizden emin misiniz?

Açılan ekranda Buton kodu, Buton adı bilgisi girilir. Buton tipi belirlenir. Görünür statüsü, Yeni statüsü ve durumu seçilir. Gerekli alanlar doldurulduktan sonra ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_286.png) butonu tıklanarak Olay Bildirim  fonksiyonu  için buton tanımlama kayıt işlemi gerçekleştirilir

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_287.png)

Olay Bildirim fonksiyonu için tüm buton tanımlamaları aynı şekilde yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_288.png)

Fonksiyon Dizanyer menüsündde Olay Bildirim fonksiyonu için statü ve buton tanımlama işlemi gerçekleştirilir.
#### **5.1.10. Tekrar Eden Kayıtlar Rapor Şablonu**
**Menü Adı**: Sistem Altyapı Tanımları / Olay Bildirim / Tekrar Eden Kayıtlar Rapor Şablonu

Olay Bildirim Detay kayıtlarında yer alan alanların tekrar etme durumunu göre rapor olarak  alındığı menüdür.İlk olarak Sistem Altyapı Tanımları/ Olay Bildirim  /Tekrar Eden Kayıtlar Raporu Şablonu menüsünden raporda gösterilecek alanlar seçilir ve rapor formatı kaydedilir.

Daha sonra Entegre Yönetim Sistemi/ Olay Bildirim  /Raporlar/Tekrar Eden Kayıtlar raporundan ilgili rapora ulaşılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_289.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref67]:Yeni tekrar eden kayıtlar şablonu tanımlanır

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_291.png):Listede seçili tekrar eden kayıtlar şablonu bilgisi ile ilgili herhangi bir düzeltme, değişiklik veya güncelleme yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_292.png):Listede seçili tekrar eden kayıtlar şablonu bilgisi silinebilir.

Tekrar Eden Kayıtlar Raporu Şablonları ekranında yeni bir Tekrar Eden Kayıtlar Raporu Şablonu tanımlamak için ekranın sol üst köşesindeki ![ref67]butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_293.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Tanım:** Tekrar Eden Kayıtlar Raporu Şablonları ekranında Tekrar Eden Kayıtlar Raporu Şablonları tanım bilgisinin girildiği alandır.

**Kolonlar:** Tekrar Eden Kayıtlar Raporu Şablonları ekranında Kolonlar bilgisinin seçilebildiği alandır.

Açılan ekranda Tekrar Eden Kayıtlar Raporu tanım bilgisi girilir. İlgili Kolonlar seçilir. Tekrar Eden Kayıtlar Raporu Şablonları ekranında gerekli alanlar doldurulduktan sonra sol üst köşedeki ![ref43]butonu tıklanarak Tekrar Eden Kayıtlar Raporu Şablonları kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_294.png)

Entegre Yönetim Sistemi/ Olay Bildirim /Raporlar/Tekrar Eden Kayıtlar raporu ekranı gidilir.  

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_295.png)

Tekrar Eden Kayıtlar ekranında Filtre sekmesinde filtre arama kriterleri olan “Rapor Şablonu ” alanında açılan açılır  listede  Rapor Şablonu seçilerek   ![ref68]  butonu tıklanılır.

![ref69]

Tekrar Eden Kayıtlar ekranında liste sekmesinde yapılan filtredeki arama kriterlerine göre kayıtlar listelenir.

![ref70]

Tekrar Eden Kayıtlar ekranında ![ref71] butonu tıklanarak Tekrar Eden Kayıtlar raporun Excel formatından raporu alınır.

![ref72]
### **5.2.Entegre Yönetim Sistemi/Olay Bildirim**
Olay Bildirim  Modülü kapsamında firmada meydana gelen bütün olayların girişinin ve takibinin yapıldığı, Raporların ve Grafiklerin görüntülendiği kısımdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_301.png)
#### **5.2.1.Yeni Kayıt**
**Menü:** Entegre Yönetim Sistemi/Olay Bildirim/Yeni Kayıt.

Altyapı tanımlarından oluşturulan firma alanlarına göre yeni olay girişi yapılır. Alan Tanımlamada tanımlanıp, alan havuzuna eklenen ve Fonksiyon Dizanyer menüsünde 4 .numaralı fonksiyon olan Olay bildirim fonksiyonun sayfaları ilişkilendirilen firma alanlarının göre yeni olay girişi bu menüde yapılmaktadır. Yeni Olay Girişi için Entegre Yönetim Sistemi/Olay Bildirim/Yeni Kayıt menüsü tıklanılır. Olay Bildirim Formu -Detaylar ekranı açılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_302.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref73]: Olay Bildirim Detay  kaydı onay akışındaki kişiye gönderilir.

![ref74]:Önceki ekrana geri dönülür.

**Açılan ekranda ilgili alanlar tanımlanır:**

**RDFD Kodu:** Olay Bildirim Formu- Detaylar ekranında RDFD kodu bilgisinin yazıldığı alandır. Bu alanda sistem tarafından otomatik  kod ataması yapılır. Bu işlemi yapılması için Olay Bildirim Modülü parametrelerinde 3 numaralı “Olay Bildirim Detayı Oto Kod Şablonu” parametresine kod şablonu tanımlanır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_305.png) Olay Bildirim modülü parametrelerinden 4 numaralı “Olay Bildirim Detayı Sayac” parametresinde tanımlı sayac değerine göre Otomatik kod şablonun kaçıncı değerden başlanacağı belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_306.png)

Örn:Otomatik kod şablonu parametrede RDFD.### olarak tanımlıdır. Sistem 4 numaralı parametredeki “0” sayac değerine göre RDFD.001, RDFD.002, RDFD.003 şeklinde otomatik kod ataması yapar.Parametrede Otomatik kod şablonu ve sayac değerinin tanımlama işlemin ilgili alan aşağıdaki şekilde görüntülenir ve Olay Bildirim Detay formu kayıt işleminden sonra kaydedilen formun kodu atanır.

![ref75]

**Revizyon No:** Olay Bildirim Formu- Detaylar ekranında revizyon no bilgisinin sistem tarafından verildiği alandır. Yeni bir olay detay formu kaydı olduğu için revizyon no bilgisi “0” olarak verilir.

**Revizyon Tarihi:** Olay Bildirim Formu- Detaylar ekranında Revizyon Tarihi bilgisinin açılır Takvim alanında seçildiği alandır. Revizyon Tarihi bilgisi alanında güncelleme işlemi yapabilme işlemi parametreye bağlı olarak yapılmaktadır. Olay Bildirim Modülü parametrelerinden 72 numaralı” Revizyon Tarihi Güncellenebilsin mi?” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_308.png)

Parametre aktif edildikten sonra Revizyon Tarihi alanında açılır Takvim alanında tarih seçim işlemi yapılır. Parametre değeri “Hayır” seçilerek parametre pasif edildiğinde bu alanı aşağıdaki şekilde  sistem tarafından açılır Takvim alanı aktif etmeyerek Tarih seçim yaptırmaz.

![ref75]

Açılan ekranda firmanın kullandığı olay bildirim prosedür ve formlarına uygun olarak altyapılarda tanımlanan akışa göre olay girişleri yapılır. Olay Türü alanında İş kazası seçeneği seçilerek görüntülenen İş Kazası sekmesinde Alan Tanımlamada tanımlanarak alan havuzuna eklenerek Fonksiyon Dizanyer menüsü yardımıyla ilişkilendirilen Olay bildirim Sayfaları alanların bilgi girişi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_309.png) ![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_310.png) ![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_311.png) ![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_312.png)

Olay Bildirm Formu-Detaylar ekranında Fotoğraf 1 alanında ![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_313.png) butonu tıklanır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_314.png)

Olay Bildirim Formu-Detaylar  ekranında kaza ile ilgili fotoğraf ekleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_315.png)

Olay Bildirim Formu-Detaylar  ekranında Dosya Ekle ekranında Gözat butonu tıklanarak fotograf  1 ekleme işlemi yapılır.Açılan ekran eklenecek fotoğraf seçim işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_316.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_317.png)

Olay Bildirim Formu-Detaylar   ekranında aynı şekilde Fotoğraf 2 ve Fotoğraf 3 alanları ile ilgili kaza fotoğraflarının ekleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_318.png)

Olay Bildirim Formu-Detaylar  ekranında kaza ile ilgili fotoğraf ekleme işleminden sonra “İşcinin” tablo tipli alanın veri girişi ![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_319.png)  buton tıklanarak yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_320.png) 

Açılan ekranda tablo tipli alanın görüntülenen alan tiplerini bilgi girişleri yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_321.png)

Tablo tipli alanın alan değerlerin bilgi girişleri yapılarak ekranın sol üst köşesindeki ![ref53]butonu tıklanarak tablo tipli alanın kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_322.png)

Olay Bildirim Formu -Detaylar ekranında  Olay Bildirim sekmesi tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_323.png)

Gerekli alanlarla ilgili bilgiler girildikten sonra ekranın sol üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_324.png)butonu tıklanarak  onay akışındaki İş yeri Hekimin  onayına  gönderilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_325.png)

Tanımlanan Olay Bildirim Formu- Detayının durumu “İşyeri Hekimi” statüsü olarak görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_326.png)

Onay akışının kullanıcının bekleyen işlerim sayfasında Olay Detay Formu “**Onay Bekleyen Olay Bildirim Detay Formları**” görevi olarak iş düşer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_327.png)

İlgili görevdeki Form kodu alanındaki link kodu tıklanarak Olay Bildirim Formu- Detaylar ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_328.png)

![ref76]:Olay Detay Formu kaydı onay akışındaki kişiye onaya gönderilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_330.png): Olay Detay Formu kaydı red edilir.

Olay Bildirim Formu- Detaylar ekranında Olay Bildirim  Detay kaydının İş kazası sekmesi tıklanarak  ilgili alanlar ilgili veriler görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_331.png)Olay Bildirim Formu – Detaylar ekranında ![ref76] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_332.png)

Sistem tarafından “Olay Bildirim formunu İSG Uzmanı (İş Kazası)  onayına göndermek ister misiniz?” mesajında “Tamam” butonu tıklanılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_333.png)

Açılan Statü Değiştirme pop-upn’nda  onay notu bilgisi İş yeri Hekimi tarafından yazılarak ![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_334.png) butonu tıklanarak akıştaki  İSG Uzmanına Olay Detay Formu kaydı onayına gönderilir. Statü Değiştirme pop-upn’nda  Onay Notu alınma işlemi  Fonksiyon Dizanyer menüsünde tanımlı butonların  ekranında “Onay notu kullanılsın” alanı ile ilgili check box  işaretlenerek görüntülenmesi sağlanarak alınma işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_335.png)

Onay akışındaki İSG Uzmanın  kullanıcı adı ve parola bilgisi ile local adresine giriş yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_336.png)

Onay akışının İSG Uzmanınn  bekleyen işlerim sayfasında Olay Detay Formu “**Onay Bekleyen Olay Bildirim Detay Formları**” görevi olarak iş düşer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_337.png)

İlgili görevdeki Form kodu alanındaki link kodu tıklanarak Olay Bildirim Formu- Detaylar ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_338.png)

Olay Bildirim Formu- Detaylar ekranında İş Kazası sekmesi tıklanarak  iş kazısının detayları olan iş kazası ilgili alanları ve alanların bilgi girişleri görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_339.png)

**Önlemler Sekmesi:** Olay Bildirim Formu  -Detaylar ekranında Önlemler sekmesinde tıklanarak  Olay Bildirim  Detay kaydı  için Önlemler planlanır. Önlemler sekmesi Olay Bildirim  Modülü parametrelerinde  61 numaralı “Önlemler  kullanılsın mı?” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_340.png)

Parametre aktif edildikten sonra Olay Bildirim Formu  -Detaylar  ekranında Önlemler sekmesi görüntülenir ve Olay Bildirim  Detay kaydı  ile ilgili önlem alınma işlemi yapılır. Önlemler sekmesinin ayrıca aktif olacağı statülerin ayarlama işlemi yapılır. Olay Bildirim Formu  -Detaylar “modülü parametrelerinde 102 numaralı “Önlemler sekmesinin aktif olacağı statü kodları(Virgül ile yazınız)” parametrenin parametre değerine Fonksiyon Dizanyer menüsünde tanımlı olan statü kodları yazılarak , yazılan statü kodlarında bulanan statülerde Önlemler sekmesinin aktif olması sağlanır. Birden fazla statü için parametre değerinde statü kodları arasında virgül konularak yazılarak tanımlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_341.png)

Olay Bildirim Formu  -Detaylar ekranında Önlemler sekmesi tıklanılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_342.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref77]:Yeni bir önlem tanımlanır.

![ref78]:Listede seçili önlem bilgisi üzerinde düzenleme ve güncelleme işlemi yapılır.Parametreye bağlı olarak görüntülenen bir butondur.Olay Bildirim Modülü parametrelerinde 167 numaralı “Önlemler sekmesinde silme ve güncelleme işlemi yapılabilsin mi?” parametresini parametre değeri “Evet” seçilerek parametre aktif edilir. 

![ref79]

Parametre aktif edildikten sonra bu buton görüntülenir ve seçili önlem bilgisi üzerinde düzenleme ve güncelleme işlemi yapılır.

![ref80]:Listede seçili önlem bilgisi silinir. Parametreye bağlı olarak görüntülenen bir butondur.Olay Bildirim Modülü parametrelerinde 167 numaralı “Önlemler sekmesinde silme ve güncelleme işlemi yapılabilsin mi?” parametresini parametre değeri “Evet” seçilerek parametre aktif edilir. 

![ref79]

Parametre aktif edildikten sonra bu buton görüntülenir ve seçili önlem bilgisinin silinme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_347.png):Listede seçili önlem bilgisi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_348.png):Listede seçili önlem bilgisi önlem iptal nedeni yazılarak iptal edilir.

Önlemler sekmesinde yeni bir önlem tanımlamak için ![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_349.png) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_350.png) Önlemler ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_351.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Referans Tipi:** Önlemler sekmesinde Önlem olarak Doküman, DÖF ve Aksiyon seçeneklerinde seçim yapıldığı alandır. 

**Referans tipi Doküman seçildiğinde;**

Referans bilgisi doküman seçildiğinde referans bilgisi alanında ![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_352.png) butonu tıklanarak açılan sistemde tanımlı Doküman listesinde seçilir. Doküman Yönetimi Modülünde yüklü olan dokümanlar Doküman listesinde görüntülenir. 

**Referans tipi seçeneği DÖF seçildiğinde;**  DÖF  Kaydının mevcut kayıtlı listeden seçilme veya yeni bir DÖF kaydının tanımlama işlem adımının seçeneğinin yer aldığı alan görüntülenir.”Listeden seç” seçeneği seçildiğinde açılan referans tipi alanında sistemde tanımlı DÖF kayıtlarından seçim yapılır.

Listeden Seçme işleminde sistemde tanımlı kapalı DÖF seçilme işlemide yapılır. Bu işlemi yapılması için Olay Bildirim Modülü parametrelerinde 160 numaralı “Önlemlerde kapalı Döf’ler seçilebilsin mi?”parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_353.png)

Parametre aktif edildikten sonra “Listeden Seç “ seçeneği seçildiğinde açılan sistemde tanımlı DÖF Listesine kapalı DÖF’lerin  listede yer alması sağlanarak  seçilme işlemin yapılır.

“Yeni Oluştur” seçeneği seçildiğinde açılan DÖF İşlemleri-Yeni Kayıt ekranında yeni bir DÖF kaydının tanımlama işlemi yapılır. Olay Bildirim Modülü  parametrelerinde 183 numaralı “Önlemlerde Kullanılacak Döf İşlem Kaynağı?” parametresinin parametre değerine DÖF işlem kaynağının kod bilgisi yazılarak tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_354.png)

Tanımlanan İşlem Kaynağı kodu bilgisi Sistem Altyapı Tanımları/DÖF/ DÖF İşlem Kaynağı menüsünde alınır. Olay Bildirimmodülünde  önlem olarak DÖF alındığında açılan bu DÖF kaydı  parametre tanımlı DÖF İşlem  kaynağına  bağlı olarak açılır.

**Referans tipi seçeneği Aksiyon seçildiğinde;**  Aksiyon  kaydının mevcut kayıtlı listeden seçilme veya yeni bir Aksiyon tanımlama işlem adımın seçeneğinde yer aldığı alan görüntülenecektir.”Listeden seç” seçeneği seçilirse sistemde tanımlı mevcut Aksiyonlardan seçim yapılır. Listeden Seçme işleminde sistemde tanımlı kapalı Aksiyonları seçilme işlemide yapılır. Bu işlemi yapılması için Olay Bildirim Modülü parametrelerinde 161 numaralı “Önlemlerde kapalı Aksiyonlar seçilebilsin mi?” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_355.png)

Parametre aktif edildikten sonra “Listeden Seç “ seçeneği seçildiğnde açılan sistemde tanımlı Aksiyon Listesine kapalı aksiyonları listede yer alması sağlanarak  seçilme işlemin yapılır.

“Yeni Oluştur” seçeneği seçildiğinde açılan Aksiyon Kalemi Planlama-Yeni Kayıt ekranı açılarak yeni bir Aksiyon Kalemi tanımlama işlemi yapılır. Olay Bildirim Modülü  parametrelerinde 8 numaralı “Aksiyon - Kaynak Kodu” parametresine tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_356.png)

Aksiyon Kaynak kodu bilgisi Sisyem Altyapı Tanımları/Aksiyon/Aksiyon Kaynak Tanımlama ekranında alınır. Olay Bildirim modülünde  önlem olarak Aksiyon alındığında açılan bu aksiyonlar parametre tanımlı aksiyon kaynağına  bağlı olarak açılır.

**Önlem Tipi:** Önlemler sekmesinde Mevcut ve Planlanan seçeneğinde seçim yapıldığı alandır. Mevcut seçiminde önlem olarak  sistemde kayıtlı DÖF ve Aksiyonları seçilir. Planlanan seçim işleminde yeni bir  önlem olarak DÖF Kaydının açılması yada önlem olarak yeni bir Aksiyon tanımlama işleminin yapılması işlemidir.

**Önlem Tarihi:** Önlemler sekmesinde tanımlanacak önlemin tarihinin açılan takvim alanında seçimin yapıldığı alandır.

**Açıklama:** Önlemler sekmesinde tanımlanacak önlemin varsa açıklama bilgisinin yazıldığı alandır.

Örneğin: Önlem türü olarak aksiyon seçilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_357.png)

“Listeden Seç” ve “Yeni Oluştur” seçeneklerinden “Yeni Oluştur” seçeneği seçilerek Aksiyon oluşturulursa aşağıdaki şekilde Aksiyon modülü ile bağlantı kurulur. Aksiyon Kalemi Planlama - Yeni Kayıt ekranı açılır. 

**Aksiyon Bilgileri sekmesi:** Aksiyon ile ilgili bilgilerin girildiği sekmedir.Aksiyonlar ilgili bilgiler yazılarak girilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_358.png)

**Ek Dosyalar Sekmesi:** Aksiyon ile ilgili bir ek dosya varsa sisteme eklendiği sekmedir. İstenirse önlem olarak açılan aksiyonla ilgili ek dosya yükleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_359.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_360.png): Ek dosya sisteme yüklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_361.png): Yüklenen ek dosya bilgisi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_362.png): Yüklenen ek dosya bilgisi silinir.

Yönlendirme tarihçesi sekmesi yönlendirme tarihçesi bilgisinin verildiği sekmedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_363.png)

Aksiyon Kalemi Planlama - Yeni Kayıt ekranında gerekli alanlar ilgili bilgiler girldikten sonra ekranın sol üst köşesindeki ![ref81]butonu tıklanarak Aksiyon Kalemi Planlama kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_365.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_366.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_367.png)

Açılan ekranda referans tipi açılır menüsünden önlemin türü seçilir. (DÖF, aksiyon, doküman, diğer). Daha sonra önlem tipi (mevcut, planlanan) ve önlem tarihi belirlendikten sonra önlemin açıklaması girilir ve ![ref82]butonu tıklanarak kayıt işlemi gerçekleştirilir.Bu şekilde Referans tipi olarak DÖF ve aksiyon seçilirse, QDMS’teki DÖF ve aksiyon modülleri ile bağlantı kurulacaktır. Mevcut açılmış DÖF ve aksiyonlardan herhangi biri önlemle ilişkilendirilebileceği gibi, bu şekilde yeni kayıtta açılabilmektedir. Referans tipi olarak doküman seçilirse, QDMS’teki doküman ağacından doküman seçilir.

**Onaycılar Sekmesi:** Olay Bildirim Detay Formu  kaydının onay geçmişi bilgilerinin yer aldığı sekmedir. Bu sekmede Olay Bildirim Detay Formu  kaydının onaycıları, onay durumu ve açıklama gibi onay bilgilerine ulaşılır. Olay Bildirim Formu- Detaylar ekranında Onaycılar  sekmesi tıklanarak Olay Bildirim Detay Formu  kaydını onay bilgileri görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_369.png)

**Kontroller sekmesi:** Sistem Altyapı Tanımları/ Olay Bildirim /Kontroller/Kontrol Tanımlama menüsünde tanımlı olan Kontroller bu sekmede Olay Bildirim  Detay kaydı ile ilişkilendirilir.

Kontrolller sekmesi Olay Bildirim Modülü parametrelerinde 95 numaralı “Kontroller sekmesi kullanılsın mı?” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_370.png)

Parametre aktif edildiğinde Olay Bildirim Formu- Detaylar ekranında ekranında Kontroller sekmesi görüntülenir ve Olay Bildirim  Detay kaydı  ile kontrollerin ilişkilendirilmesi işlemi yapılır.

Olay Bildirim modülü parametrelerinde 104 numaralı “Kontroller sekmesinin aktif olacağı statü kodları(Virgül ile yazınız)” parametresine tanımlı statülere göre kontroller sekmesinin görüntüleme işlemi yapılır.Statü kodları bilgisi Fonksiyon Dizanyer menüsünde alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_371.png)

Kontroller sekmesinde Olay Bildirim  Detay  kaydının bir kontrolle ile ilişkilendirilme işleminin zorunluluğunun getirilmesi için Olay Bildirim modülü parametrelerinde 229 numaralı” Kontrol seçimi zorunlu olsun mu?” parametresi aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_372.png)

Parametre aktif edildiğine Kontroller sekmesinde kontrol  ekleme işlemi yapılmadığında Olay Bildirim  Detay   kayıdının kayıt işlemi yapılmaz ve kayıt işleminde kontrol ekleme işleminin yapılması ile ilgili uyarı mesajı verir. Olay Bildirim Formu- Detaylar ekranında Kontroller  sekmesi tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_373.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref83]:Yeni bir kontrol ekleme işlemi yapılır.

![ref84]:Listede seçili kontrol bilgisi üzerinde düzenleme ve güncelleme işlemi yapılır.

![ref85]: Listede seçili kontrol bilgisi silinir.

Kontroller sekmesinde  yeni bir kontrol ekleme işlemi için ![ref83] butonu tıklanılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_377.png)Kontroller ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_378.png)

Kontroller ekranında Kontrol alanında ![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_379.png) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_380.png)

Kontrol listesine kontrol seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_381.png) butonu tıklanarak kontrol ekleme işlemi yapılır.

Açılan ekranda istenirse ![ref83]butonu tıklanarak yeni bir kontrol tanımlama işlemi yapılarak kontrol listesine ekleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_382.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_383.png)

Kontroller ekranında kontrol ekleme işleminden sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_384.png) butonu tıklanarak kontrol ekleme kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_385.png)

Olay Bildirim sekmesi tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_386.png)

**Tarihçe sekmesi:** Olay Bildirim  Detay kaydının  daha önce hangi işlemlerden geçtiğini gösterildiği sekmedir. Parametreye bağlı olarak görüntülenen bir sekmedir. Olay Bildirim Modülü parametrelerinde 149 numaralı “Detay Sayfasında Tarihçe sekmesi görüntülensin mi?” parametresinin parametre değeri”Evet” seçilerek parametre aktif edilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_387.png)

Parametre aktif edildikten sonra Olay Bildirim Formu-Detaylar  ekranında Tarihçe sekmesi görüntülenir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_388.png)

Olay Bildirim Formu  -Detaylar ekranda olay bildirim kaydı ile önlem alınma ve kontrollerle ilişkilendirilme işlemlerinden sonra ekranın sol üst köşesindeki ![ref86]butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_390.png)

Sistem tarafından “Olay Bildirim formunu İSG Müdürü (İş Kazası)  onayına göndermek ister misiniz?”mesajında “Tamam” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_391.png)

İSG Uzmanı açılan Statü Değiştirme pop-upn’da onay notu bilgisi yazarak  ![ref86] butonu tıklanarak onay akışındaki İSG Müdürü onayına Olay Bildirim  Detay kaydı  gönderir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_392.png)

Onay akışındaki İSG Müdürünün  kullanıcı adı ve parola bilgisi ile local adresine giriş yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_393.png)

Onay akışınındaki İSG Müdürünün  bekleyen işlerim sayfasında Olay Bildirim  Detay kaydı  “**Onay Bekleyen Olay Bildirim Detay Formları**” görevi olarak iş düşer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_394.png)

İlgili görevdeki Form kodu alanındaki link kodu tıklanarak Olay Bildirim Formu-Detaylar  ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_395.png)

Olay Bildirim Formu-Detaylar  İş kazası sekmesi tıklanarak bilgiler kontrrol edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_396.png)

Olay Bildirim Formu-Detaylar ekranında Olay Bildirim  Detay kaydı   ![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_397.png) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_398.png)

Sistem tarafından “Olay Bildirim Formu onaylamak ister misiniz?” mesajında “Tamam” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_399.png)

Olay Bildirim Formu-Detaylar ekranında onaylanan Olay Bildirim  Detay kaydının durumu “Tamamlanan İş Kazası Bildirimleri” statüsü olarak görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_400.png)

**Ramak Kala:** İşyerinde meydana gelen; çalışan, işyeri ya da iş ekipmanını zarara uğratma potansiyeli olduğu halde zarara uğratmayan olaylar olarak tanımlanılır. Ramak Kala Yeni Olay Girişi için Entegre Yönetim Sistemi/Olay Bildirim/Yeni Kayıt menüsü tıklanılır. Olay Bildirim Formu -Detaylar ekranı tıklanılır. Açılan ekranda firmanın kullandığı olay bildirim prosedür ve formlarına uygun olarak altyapılarda tanımlanan akışa göre olay girişleri yapılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_401.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref73]: Olay Bildirim Detayı  kaydı onay akışındaki kişiye gönderilir.

![ref74]:Önceki ekrana geri dönülür.

Olay Türü alanında Ramak Kala  seçeneği seçilerek görüntülenen Ramak Kala  sekmesinde Alan Tanımlamada tanımlanarak alan havuzuna eklenerek Fonksiyon Dizanyer menüsü yardımıyla ilişkilendirilen Olay bildirim Sayfaları alanların bilgi girişi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_402.png)

Ramakala Görseli alanında ![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_403.png) butonu tıklanarak ramak kala ile ilgil görsel ekleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_404.png)

Açılan Dosya Ekleme ekranında Gözat butonu tıklanarak Ramakkala ile ilgili görsel ekleme işlemi yapılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_405.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_406.png)

Olay Bildirim Formu-Detaylar ekranında Ramak Kala sekmesi ile görüntülenen alanların bilgi girişleri yapıldıktan sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_407.png) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_408.png)

Sistem tarafından “Olay  Bildirim formunu İş Yeri Hekimine  göndermek ister misiniz?”mesajında “Tamam	“ butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_409.png)

Ramak kala olay bildirim detay kayıtlarının onay akışı işlem aşamaları aynı şekilde İş kazası olay bildirim detay kayıtlarının  onay akışı işlem aşamaları aynı  şekilde yapılır. Onay işlem aşamları tamamlanan Ramak kala olay bildirim kayıtlarının durumu “Tamamlanan Ramak Kala Bildirimleri” statüsü olarak görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_410.png)

Statü Tanımlama menüsünde “Tamamlanan Ramak Kala Bildirimleri” statüsü menü olarak tanımlanır. Entegre Yönetim Sistemi/Olay Bildirim/ Tamamlanan Ramak Kala Bildirimleri tanımlanan statü menüsü tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_411.png)

Açılan ekranda “Tamamlanan Ramak Kala Bildirimleri” statüsündeki ramak kala olay bildirim kayıtları görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_412.png)

Entegre Yönetim Sistemi/Olay Bildirim/Yeni Kayıt menüsü tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_413.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref73]: Olay Bildirim Detay  kaydı onay akışındaki kişiye gönderilir.

![ref74]:Önceki ekrana geri dönülür.

![ref74] (Geri) butonu tıklanılır. Olay Bildirim Formu-Detaylar ekranı açılır. Açılan ekranda sistemde tanımlı kayıtlar görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_414.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_415.png): Yeni bir Olay Bildirim Detay kaydı  tanımlanabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_416.png): Listede seçili Olay Bildirim Detay kaydı bilgisi güncellenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_417.png): Listede seçili Olay Bildirim Detay kaydı bilgisi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_418.png): Listede seçili olan Olay Bildirim Detay kaydı bilgisi kopyalanabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_419.png): Listede seçili olan Olay Bildirim Detay kaydı bilgisini silmek için kullanılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_420.png):Listede seçili olan Olay Bildirim Detay kaydı bilgisi revize edilerek onaya gönderilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_421.png): Listede seçili Olay Bildirim Detay kaydı   bilgisinin eski revizyonları izlenebilme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_422.png):Listede seçili Olay Bildirim Detay kaydı   bilgisinin revizyon değişim işlemi  yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_423.png): Listede seçili Olay Bildirim Detay kaydı   bilgisi gözden geçirilme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_424.png): Listede seçili Olay Bildirim Detay kaydı   bilgisi için eski gözden geçirmeler izlenebilme işlemi yapılır.

![ref87]:Listede seçili Olay Bildirim Detay kaydı   bilgisinin sıra numarası değiştirme işlemi yapılır. Olay Bildirim Formu-Detaylar ekranda liste sekmesinde Olay Bildirimi Detay kaydı seçili iken ![ref87] butonu tıklanılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_426.png)

Açılan Sıra Numarası Değiştir ekranında Yeni Sıra Numarası bilgisi belirlenerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_427.png) butonu tıklanırak sıra numarası değiştirme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_428.png)

Olay Bildirim Formu - Detaylar ekranında listede seçili Olay Bildirim Detay kaydı sıra numarası değiştirme işleminden sonra sıra numarasının değiştirildiği görülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_429.png)

![ref88]: Olay Yetki Matrisi ekranında açılma işlemi yapılır.Tanımlanan Olay Bildirim Detay kayıtlarında hangi rolün veya kullanıcı grubunun kayıt görme, güncelleme vb. yetkilere sahip olacağının belirlendiği menüdür. Bu buton parametre bağlı olarak görüntülenen bir butondur. Olay Bildirim Modülü parametrelerinde 111 numaralı “Detay kayıt bazında yetkilendirme yapılacak mı?” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. Parametre aktif edildikten sonra Olay Bildirim Formu - Detaylar ekranında Yetki matrisi butonu görüntülenir ve Olay Bildirim modülünde detay kayıt bazında yetkilendirme işlemleri yapılır.

Olay Bildirim Formu - Detaylar ekranında ekranında  ![ref88] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_431.png)

Olay Yetki Matrisi ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_432.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref89]: Olay Yetki Matrisi ekranında  kayıt işlemi yapılır

![ref90]: Olay Yetki Matrisi ekranında sistemde tanımlı kullanıcı grubu listesinde yetki verilmek istenilen kullanıcı grubu ekleme işlemi yapılır.

![ref91]: Olay Yetki Matrisi ekranında yetki verilen listede seçili kullanıcı grubunu silme işlemi yapılır.

Olay Yetki Matrisi ekranında Roller Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Rol Tanımlama menüsünde tanımlı gelmektedir.Rol tanımları hangi role yetki verilmesi isteniyorsa o role karşılık gelen ilgili yetki check box  işaretlenir ve ![ref89] butonu ile kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_436.png)

Olay Yetki Matrisi ekranında bir kullanıcı grubuna yetki vermek için  ![ref90] butonu tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_437.png)

Açılan sistemde tanımlı kullanıcı grubu listesinde yetki verilmek istenilen kullanıcı grubu seçilir ve ekranın sol üst kösesinde yer alan  ![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_438.png) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_439.png)

Olay Yetki Matrisi ekranında kullanıcı grubu için  Olay Bildirim  Modülünde Olay Bildirim Detay kayıt işlemleri için yetkilendirme işlemler için yetki check box’ları işaretlendikten sonra ekranın sol üst köseşinde yer alan ![ref89] butonu tıklanarak kullanıcı grubu bazlı yetkilendirme kayıt işlemi yapılır.Örn:Revizyon, Güncelleme ve  Kopyalama yetkileri gibi ilgili check box işaretlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_440.png)

Olay Yetki Matrisi ekranında yetki verilen kullanıcı grubundan yetkiler alınıp, kullanıcı grubunun yetki matrisinden çıkarılması isteniyorsa ![ref91] butonu kullanılır.

![ref92]: Şablon oluşturmak için kullanılır. Aktarım şablonu bu butonu ile kullanıcının bilgisayarına indirilerek ilgili alanlar doldurulur.

![ref93]: Şablon yüklemek için kullanılır.Kullanıcının bilgisayara indirilip, doldurulan şablon sisteme bu buton ile yüklenir.

Not: Uyarlama çalışmaları sonrasında mevcut Olay Bildirim Detay kayıtları sisteme toplu olarak aktarılabilmektedir. Bu sebeple alan tanımlama vb. işlemler tamamlandıktan sonra sistemin kullanıma hazır olduğuna karar verildiği takdirde BSAT/Konfigürasyon Ayarları/Yönetici Tanımlama menüsünde bu modülde yönetici olarak belirlenen kullanıcıların Olay Bildirim Formu - Detaylar ekranında ![ref92]ve ![ref93]butonu çıkmaktadır. Şablon, sistemde tanımlanan alanlara göre otomatik olarak oluşturulmaktadır. ![ref94]butonu ile sistem oluşturulan şablonu bilgisayara indirir. İlgili şablon kullanıcılar tarafından doldurularak ![ref95]butonu ile sisteme yüklendiğinde Olay Bildirim Detay kayıtları sisteme aktarmış olur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_445.png) : Arama fonksiyonu kullanılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_446.png):Listede seçili  form detayları Excel’ e aktarılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_447.png): Yazdır.Sistem Altyapı Tanımları/Olay Bildirim /Rapor formatları menüsünde tanımlı kayıt bazında rapor formatlarının seçili görüntülenmesi işlemi sağlanır. Bu buton tıklanarak  Excel ve Pdf formatında kayıt bazında rapor formatı alınır. Kayıt bazında rapor formatı tanımlama işlemi olmadığı sürece ![ref54]   butonu görüntülenmez.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_448.png): Grafik çizmek için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_449.png): Bir önceki ekrana dönmek için kullanılır.

**Revizyon İşlemi:** Olay Bildirim Detay kayıtları  kaydedildikten sonra herhangi bir anda revizyon işlemi yapılır. Bunun için Olay Bildirim Detay kayıtları listesi açıkken ilgili Olay Bildirim Detay kaydı seçilir ve sol üstteki butonlardan ![ref96] butonu tıklanır. Bundan sonraki aşama Olay Bildirim Detay kaydı  ilk kez doldururken izlenen adımlarla birebir aynıdır. Tek fark, Olay Bildirim Detay kaydı ekranındayken revizyon numarası bir artacaktır.Revizyon işlemi yapılması için Olay Bildirim Modülü parametrelerinde 80 numaralı “Revizyon kullanılacak mı?” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. 

![ref97]

Parametre aktif edildikten sonra Olay Bildirim Formu - Detaylar ekranında revizyon işlemi ile ilgili butonlar görüntülenir. Bu butonlar ile revizyon, eski revizyonlar görme ve revizyon değişimi işlemleri yapılır.Revizyon işleminde revizyon tarihinin güncellenip, güncellenmemesi parametre olarak değişmektedir. Olay Bildirim modülü parametrelerinde 72 numaralı “Revizyon Tarihi Güncellenebilsin mi?” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_452.png)

Parametre aktif edildiğinde Olay Bildirim Detay kaydı için revizyon işlemi yapılan ekranda revizyon tarihi ile ilgili değişiklik yapılması sağlanır. Parametrenin parametre değeri “Hayır” seçilerek parametre pasif edildiğinde Olay Bildirim Detay kaydının revizyon işlemi aşamasında revizyon tarihi alanına müdahele edilemez. 

Olay Bildirim Formu - Detaylar ekranında Olay Bildirim Detay  kaydı seçili iken ![ref96] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_453.png)

Açılan Olay Bildirim Formu - Detaylar ekranında  revizyon işlemi için ilgili alanlar üzerinde değişiklik yapılır. Revizyon numarasının  bir artığı görülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_454.png)

Olay Bildirim Formu - Detaylar ekranında İş Kazası sekmesi tıklanarak ilgili alanlar görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_455.png)

Olay Bildirim Formu- Detaylar ekranında Revizyon Değişim sekmesi görüntülenir. Bu sekme parametreye bağlı olarak görüntülenir. Olay Bildirim Modülü parametrelerinde 214 numaralı “Detay sayfasında Revizyon Değişimi gösterilsin mi?” parametrresinin parametre değeri “Evet” seçilerek parametre aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_456.png)

Parametre aktif edildikten sonra Olay Bildirim Formu- Detaylar ekranında Revizyon Değişimi sekmesi görüntülenerek  Olay Bildirim Detay kaydının revizyon değişimi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_457.png)
Gerekli alanlarla ilgili değişiklik yapıldıktan sonra ekranın sol üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_458.png) butonu tıklanarak revizyon kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_459.png)

Sistem tarafından “Olay  Bildirim formunu İş Yeri Hekimine  göndermek ister misiniz?” mesajında “Tamam” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_460.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_461.png)

**Eski Revizyonları Görme İşlemi:** Olay Bildirim Formu - Detaylar ekranında revizyon işlemi yapılan bir Olay Bildirim Detay kaydı seçili iken butonu tıklanarak Olay Bildirim Detay kaydının eski revizyonun görme işlemi yapılır.Eski Revizyon görme işlemi yapılması için Olay Bildirim Modülü parametrelerinde 80 numaralı “Revizyon kullanılacak mı?” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. 

![ref97]

Parametre aktif edildikten sonra Olay Bildirim Formu - Detaylar ekranında ![ref98] butonu görüntülenir ve seçilen Olay Bildirim Detay kaydının bu buton tıklanarak eski revizyonlarının görüntüleme işlemi yapılır.

Olay Bildirim Formu - Detaylar ekranında ekranında Olay Bildirim Detay kaydı seçili iken ![ref98] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_463.png)

Olay Bildirim - Eski Revizyonlar ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_464.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref99]:Eski revizyonları görüntüler.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_466.png): Veriler Excel’ e aktarılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_467.png): Önceki ekrana geri dönülür.

Olay Bildirim - Eski Revizyonlar ekranında listede Olay Bildirim Detay kaydı seçili iken ![ref99] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_468.png)

Olay Bildirim Formu - Detaylar ekranı görüntülenerek Olay Bildirim Detay kaydının  eski revizyonu görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_469.png)

**Revizyon Değişim İşlemi:** Revizyon işlemi yapılan Olay Bildirim Detay kaydının revizyonlarının karşılaştırılma işleminin yapılmasıdır. Revizyon Değişim işlemi yapılması için Olay Bildirim Modülü parametrelerinde 80 numaralı “Revizyon kullanılacak mı?” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. 

![ref97]

Parametre aktif edildikten sonra Olay Bildirim Formu - Detaylar ekranında  ![ref100] butonu görüntülenir ve seçilen Olay Bildirim Detay kaydının bu buton tıklanarak Olay Bildirim Detay kaydının revizyon karşılaştırma işleminin yapılması sağlanır.

Olay Bildirim Formu - Detaylar ekranında ekranında Olay Bildirim Detay  kaydı seçili iken![ref100]  butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_471.png)

Açılan Olay Bildirim Revizyon Karşılaştırma ekranında Olay Bildirim Detay  kaydının 0.revizyonu ile 1.revizyonu arasındaki alanlar ilgili değişiklikler görüntülenerek karşılaştırma işleminin yapıldığı görülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_472.png)

**Gözden Geçirme İşlemi:** Mevcut Olay Bildirim Detay kayıtlar herhangi bir gözden geçirme işlemine tabi tutulabilir ve mevcut durum değerlendirilip açıklamalar yapılabilir. Bunun için Olay Bildirim Detay kayitları listesi açıkken ilgili Olay Bildirim Detay kaydı  seçilir ve sol üstteki ![ref101] butonu tıklanarak gözden geçirme işlemi yapılır. Olay Bildirim Detay  kaydında Gözden Geçirme işlemi yapılması için Olay Bildirim Modülü parametrelerinde 39 numaralı “Gözden geçirme fonksiyonu kullanılacak mı ? (E/H)” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. 

![ref102]

Parametre aktif edildikten sonra Olay Bildirim Formu - Detaylar ekranda ![ref101] butonu görüntülenir ve seçilen Olay Bildirim Detay kaydında  bu buton tıklanarak gözden geçirme işlemi yapılır. Olay Bildirim modülü parametrelerinde  174 numaralı “Gözden geçirme fonksiyonu için pasif olacak statü kodları(Virgül ile yazınız)” parametrede tanımlı statü kodlarındaki Olay Bildirim Detay kayıtlarına gözden geçirme görevi düşmez. Statü kodları bilgisi Fonksiyon Dizanyer menüsünde alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_475.png)

Olay Bildirim Formu - Detaylar ekranında ekranında Olay Bildirim Detay  kaydı seçili iken ![ref101] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_476.png)

Olay Bildirim Gözden Geçirme ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_477.png)

Olay Bildirim Gözden Geçirme ekranında Olay Bildirim Detay kaydının açıklama alanında gözden geçirme işlemi ile ilgili açıklama bilgisi yazılır. Tarih alanında gözden geçirme işlemi tarihi açılan Takvim alanında seçilir. Gerekli alanlar ilgili bilgiler girildikten sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_478.png) butonu tıklanarak gözden geçirme kayıt işlemi yapılır.

**Eski Gözden Geçirme Görme İşlemi:** Mevcut Olay Bildirim Detay kayıtları herhangi bir gözden geçirme işlemine tabi tutulabilir ve mevcut durum değerlendirilip açıklamalar yapılabilir. Gözden Geçirme işlemi yapılan Olay Bildirim Detay kaydı seçilir ve sol üstteki ![ref103]butonu tıklanarak eski  gözden geçirme işlemlerinin görüntülenmesi sağlanır. Olay Bildirim Detay  kaydında Eski Gözden Geçirmelerin görme  işlemi yapılması için Olay Bildirim Modülü parametrelerinde 39 numaralı “Gözden geçirme fonksiyonu kullanılacak mı ? (E/H)” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. 

![ref102]

Parametre aktif edildikten sonra Olay Bildirim Formu - Detaylar ekranda ![ref103] butonu görüntülenir ve seçilen Olay Bildirim Detay  kaydında bu buton tıklanarak eski gözden geçirmelerin görme  işlemi yapılır.

Olay Bildirim Formu - Detaylar  ekranında Olay Bildirim Detay  kaydı seçili iken  ![ref103]butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_480.png)

Risk Eski Gözden Geçirmeler ekranı açılır ve eski gözden geçirme işlemleri ile ilgili bilgiler görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_481.png)

**Grafik Çizme İşlemi;** Olay Bildirim Formu - Detaylar ekranında Olay Bildirim Detay  kayıtları  seçili iken ![ref104] butonu tıklanarak Olay Bildirim Detay  kayıtların grafiklerinin alınma işlemi yapılır. Bu buton parametreye bağlı olarak görüntülenen bir butondur. Olay Bildirim modülü parametelerinden 84 numaralı “Olay Bildirim detayında grafik çiz fonksiyonu kullanılsın mı?parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_483.png)

Parametre aktif edildikten sonra Olay Bildirim Formu - Detaylar ekranında ![ref104]   butonu görüntülenir ve listede seçili Olay Bildirim Detay kaydının grafiği alınır.

Olay Bildirim Formu - Detaylar ekranında Olay Bildirim Detay  kaydının seçili iken ![ref104]  butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_484.png)

Revizyon Bazında Olay Durumu Grafiği ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_485.png)

Açılan ekranda alanlar alanında grafiği alınacak alanlar seçilerek ![ref105] butonu tıklanarak Olay Bildirim Detay  kaydının grafiğinin alınma işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_487.png)
#### **5.2.2.Grafikler**
**Menü Adı:** Entegre Yönetim Sistemi/Olay Bildirim/Grafikler 

Olay Bildirim  Modülünde Grafiklerin görüntülendiği kısımdır.
##### **5.2.2.1.Olay Revizyon Karşılaştırma Grafiği**
**Menü Adı:** Entegre Yönetim Sistemi/ Olay Bildirim /Grafikler/ Olay Revizyon Karşılaştırma Grafiği

Olay Bildirim Detay  kayıtlarında revizyon karşılaştırılma işlemi yapılarak grafiğinin alındığı menüdür.Olay  Revizyon Karşılaştırma Grafiğini almak için, Grafikler menüsünden Olay  Revizyon Karşılaştırma Grafiği menüsü tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_488.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref106]: Belirlenen özelliklere göre ekrana grafiği çizdirir.

![ref107] : Grafiği açılır menüden seçilen format türüne ( Excel, JPG, PDF vb. ) dönüştürerek dış ortama aktarır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_491.png)

Açılan ekranda filtre sekmesinden grafik karşılaştırmasını almak istediğimiz alanları doldurarak ![ref106] butonu ile istenilen olay revizyon karşılaştırması yapılır. 

Olay  Revizyon Karşılaştırma Grafiği ekranında güncel öncesi revizyon sayısı ve X ekseni seçilerek ![ref106]butonu tıklanarak Olay Revizyon Karşılaştırme grafik oluşturulur. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_492.png)

Olay  Revizyon Karşılaştırma Grafiği ekranında ![ref108] butonu tıklanarak açılır listede tıklanarak  “xls” seçeneği seçilerek  Olay Revizyon Karşılaştırma Grafiğinin Excel formatında raporu alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_494.png)
##### **5.2.2.2.En Çoklar Analizi**
**Menü Adı:** Entegre Yönetim Sistemi/Olay Bildirim/Grafikler/ En Çoklar Analizi

X ekseninde yer alan seçim tiplerine göre grafik oluşturulmasını sağlar. Oluşturulan bu grafik için de veri seçenekleri kullanılarak detay bazlı filtreleme yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_495.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref109]: Belirlenen özelliklere göre ekrana grafiği çizdirir.

![ref110] : Grafiği açılır menüden seçilen format türüne (png,jpg,bmp,xls, vb. ) dönüştürerek dış ortama aktarılma işlemi yapılır.

![ref61]: Veriler Excel’ e aktarılabilir.

Grafik oluşturmak için iki ayrı ayar alanı bulunmaktadır. Bunlar Grafik ve Veri seçenekleridir. Adından da anlaşılacağı gibi grafiğin renkleri, eni-boyu gibi ayarlamaların yapıldığı alandır. Grafik ayarlarında önemli olan X ekseni ve Y eksenidir. X ekseninden sorgulamak istediğimiz, Olay Türü, Kaza/Olay Tarihi vb. konulara göre grafik elde etmemizi sağlar. Y Ekseninden ise ilgili sorgunun sayı miktarı olan adet ve Z eksenine göre istenen seçeneğe göre grafiğinin raporunun alınması sağlanır.Veri Seçeneklerinden ise belirlediğimiz grafik ayarlarından daha kısıtlı bir veri almak için filtreleme yapmak istenirse kullanılan alandır. Bar üzerine adet bilgisi yazılsın check box işaretlendiğinde grafikte bar üzerine adet bilgiside görüntülenir.Ayarlamalar tamamlandıktan sonra ![ref109] butonu tıklanarak grafik oluşur. Grafiği farklı formatlara almak istenirse, formatı sağdan seçtikten sonra![ref110]  soldan butona basıldığın da xls, png, jpg. Formatlarına grafik basılabilir. ![ref61] butonu ile de oluşan verileri Excel’e aktarması sağlanır. Bu veriler ile farklı formattaki grafiklerde oluşturulabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_498.png)![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_499.png) 

En çoklar Analizi ekranında![ref61] butonu tıklanarak En çoklar Analizi Grafiği Excel formatında alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_500.png)

##### **5.2.2.3.Olay Dağılım Matrisi**
**Menü Adı:** Entegre Yönetim Sistemi/Olay Bildirim/Grafikler/ Olay Dağılım Matrisi

Olay Dağılım Matrisi Grafiğini almak için, Grafikler menüsünden Olay Dağılım Matrisi menüsü tıklanır. Amaç; hangi aralıkta olay bildirim detay kayıtlarının  daha yoğun olduğunu hangilerinde daha az olduğunu görmektir. Filtre sekmesinden kullanılan grafik türü seçilerek, varsa ilgili alanları belirtilerek olay bildirim detay kayıtları dağılım matrisi elde edilir. Bu matris ile hangi olay bildirim  detay kayıtlarının skalasından kaç adet olay bildirim detay kayıtları  olduğu belirtilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_501.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref61]: Veriler Excel’ e aktarılabilir.

![ref60]: Kayıtlar filtrelenerek arama yapılabilir.

Olay Dağılım Matrisi ekranında![ref61] butonuna basılırsa, sistem otomatik olarak  Olay  Dağılım Matrisi grafiğini oluşturup kullanıcıya Excel formatında sunmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_502.png)
##### **5.2.2.4.Olay Karşılaştırma Grafiği**
**Menü Adı:** Entegre Yönetim Sistemi/Olay Bildirim /Grafikler/ Olay  Karşılaştırma Grafiği

Olay  karşılaştırma grafiği alınma işleminin yapıldığı menüdür.Olay Karşılaştırma Grafiğini almak için, Grafikler menüsünden Olay  Karşılaştırma Grafiği menüsü tıklanır. Bu grafikle, filtrelenen detay formlar üzerindeki iki alanın karşılaştırılabilmesi gibi, yine seçilen alanların güncel ve eski revizyonları görüntülenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_503.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref106]: Belirlenen özelliklere göre ekrana grafiği çizdirir.

![ref107] : Grafiği açılır menüden seçilen format türüne ( Excel, JPG, PDF vb. ) dönüştürerek dış ortama aktarır.

Açılan ekranda filtre sekmesinden grafik karşılaştırmasını almak istediğimiz alanları doldurarak ![ref106] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_504.png)

Olay  Karşılaştırma Grafiği ekranda istenilen alanların olay  karşılaştırması yapılarak grafiği alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_505.png)

Olay Karşılaştırma Grafiği ekranında ![ref108]  butonu tıklanarak açılır listede tıklanarak  “xls” seçeneği seçilerek  Olay  Karşılaştırma Grafiğinin Excel formatında raporu alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_506.png)
#### **5.2.3.Raporlar**
**Menü Adı:** Entegre Yönetim Sistemi/Olay Bildirim /Raporlar

Olay Bildirim  Modülünde raporların görüntülendiği kısımdır.
##### **5.2.3.1.Genel Olay Listesi**
**Menü Adı:** Entegre Yönetim Sistemi/Olay Bildirim/Raporlar/ Genel Olay Listesi

Genel Olay Raporunun alındığı menüdür.Genel Olay Listesi raporunu almak için, Genel Olay Listesi menüsü tıklanır.Açılan ekranda Liste ve Filtre olmak üzere iki sekme karşımıza çıkar. Filtre sekmesinde arama kriterlerine göre filtreleme işlemi yapılır. Liste sekmesinde ise bu arama kriterleri olan alanlara göre filtreleme işlemine göre kayıtları listelenir. Genel Olay Listesi ekranında Sistem Altyapı Tanımları/Olay Bildirim/Rapor Formatları menüsünde Genel bazda rapor formatı tanımlı ise ![ref111] butonu tıklanıldığında bu rapor formatının Excel formatında raporu alınır. Rapor Formatları menüsünde genel bazda rapor formatı tanımlı değilse Genel Olay Listesi ekranında filtre sekmesinde arama kriterlerine göre liste sekmesinde listelenen kayıtların ![ref111] butonu tıklanıldığında Excel formatında raporu alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_508.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref112]:Kayıtlar filtrelenerek arama yapılır.

![ref111]:Veriler Excel’ e aktarılır.

![ref44]:Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref45]:Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref46]:Menü ekranlarında kolonların karşılığı olan alanların gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Genel Olay Listesi  ekranında Filtre sekmesinde filtre arama kriterleri olan “RDFD ” alanında ![ref113] butonu tıklanarak açılan  RDFD  listesinde RDFD seçilerek  ![ref68]  butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_511.png)

Genel Olay Listesi ekranında liste sekmesinde yapılan filtredeki arama kriterlerine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_512.png)

Genel Olay Listesi ekranında ![ref71] butonu tıklanarak Genel Olay Listesi raporun Excel formatından raporu alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_513.png)
##### **5.2.3.2.Aksiyon Raporu**
**Menü Adı**: Entegre Yönetim Sistemi/ Olay Bildirim/ Raporlar/ Aksiyon Raporu

Aksiyon raporunu almak için, raporlar menüsünden aksiyon raporu açılır. Olay Bildirim  sonucu alınan aksiyon önlemlerinin alındığı rapordur. Bu rapor Excel’ e aktarılabilir. Özet raporu alınabilir. Ayrıca zaman bazlı aksiyon çizelge raporu çekilebilir. Akisyon  raporunu almak için, Raporlar menüsünden Aksiyon Raporu  menüsü tıklanır. Açılan menü ekranında Liste ve Filtre olmak üzere iki sekme karşımıza çıkar. Filtre sekmesinde arama kriterlerine göre filtreleme işlemi yapılır. Liste sekmesinde ise bu arama kriterleri olan alanlara göre filtreleme işlemine göre kayıtları listelenir

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_514.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_515.png): Kayıtlar filtrelenerek arama yapılabilir.

![ref114]: Aksiyon çizelge raporunu görüntüleme işlemi yapılır.

![ref115]: Özet Rapor alınma işlemi yapılır.

![ref116]: Veriler Excel’ e aktarılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_519.png):Log görüntüleme işlemi yapılır.

![ref44]:Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref45]:Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref46]:Menü ekranlarında kolonların karşılığı olan alanların gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Olay Bildirim  Aksiyon Raporu ekranında Filtre sekmesinde filtre arama kriterleri olan “RDFD ” alanında ![ref113] butonu tıklanarak açılan  RDFD  listesinde RDFD seçilerek  ![ref68]  butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_520.png)

Olay Bildirim Aksiyon Raporu ekranında liste sekmesinde yapılan filtredeki arama kriterlerine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_521.png)

Olay Bildirim Aksiyon Raporu ekranında ![ref114]  butonu tıklanarak Aksiyon raporun Excel formatından Aksiyon Çizelge raporu alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_522.png)

Olay Bildirim  Aksiyon Raporu ekranında ![ref115] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_523.png)

Olay Bildirim  Aksiyon Raporu ekranında Aksiyon Özet Rapor görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_524.png)

Olay Bildirim Aksiyon Raporu ekranında ![ref116] butonu tıklanılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_525.png)

Olay Bildirim Aksiyon Raporu ekranında Aksiyon Raporunu Excel formatında raporu alınır

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_526.png)

Olay Bildirim Aksiyon Raporu ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_527.png) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_528.png)

Olay Bildirim  Aksiyon Raporu ekranında Aksiyon Raporunun Log Görüntüleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_529.png)
##### **5.2.3.3. Tekrar Eden Kayıtlar Raporu** 
**Menü Adı:** Entegre Yönetim Sistemi/ Olay Bildirim  /Raporlar/ Tekrar Eden Kayıtlar Raporu

Benzer Olay Bildirim  detay kayıtlarının kaç kez tekrar ettiğini gösteren raporun alındığı menüdür.Entegre Yönetim Sistemi/ Olay Bildirim  /Raporlar/Tekrar Eden Kayıtlar raporundan ilgili rapor şablonu seçilir. Tekrar Eden Kayıtlar raporunu almak için, Tekrar Eden Kayıtlar menüsü tıklanır.Açılan ekranda Liste ve Filtre olmak üzere iki sekme karşımıza çıkar. Filtre sekmesinde arama kriterlerine göre filtreleme işlemi yapılır. Liste sekmesinde ise bu arama kriterleri olan alanlara göre filtreleme işlemine göre kayıtları listelenir 

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_530.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref112]:Kayıtlar filtrelenerek arama yapılır.

![ref111]:Veriler Excel’ e aktarılır.

Tekrar Eden Kayıtlar ekranında Filtre sekmesinde filtre arama kriterleri olan “Rapor Şablonu ” alanında açılan açılır  listede  Rapor Şablonu seçilerek   ![ref68]  butonu tıklanılır.

![ref69]

Tekrar Eden Kayıtlar ekranında liste sekmesinde yapılan filtredeki arama kriterlerine göre kayıtlar listelenir.

![ref70]

Tekrar Eden Kayıtlar ekranında ![ref71] butonu tıklanarak Tekrar Eden Kayıtlar raporun Excel formatından raporu alınır.

![ref72]
##### **5.2.3.4. Olayların Bölgelere Dağılımı**
**Menü Adı:** Entegre Yönetim Sistemi / Olay Bildirim  /Raporlar/Olayların  Bölgelere Dağılımı

Olay Bildirim  Modülü kapsamında iş yeri ve departman bazlı olayların  haritada gösterilmesinin sağlandığı rapordur. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_531.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref112]: Kayıtlar filtrelenerek arama yapılabilir.

Filtre sekmesinde ilgili işyeri veya departman listesinde seçim yapılarak ![ref112]  butonu tıklanarak Harita sekmesinde işyeri ve departman bazlı olayların harita üzerinde görüntülenmesi sağlanır.
### **5.3.Dashboard/Olay Bildirim**
**Menü:** Dashboard/Olay Bildirim 

Qdms sisteminde  kullanıcılara işlemleri, metrikleri, grafikleri ve raporları tek bir ekranda görüntülemelerine olanak sağlayan kısımdır. Dashboard, bilgi akışını ve/veya içeriğini özetlemek amacıyla kullanılan, grafikler ve tablolar yoluyla belirli bir durumu açıklamaya yarayan göstergeler ekranı, iş panosu ve  göstergeler tablosu olarak ifade edilmektedir. Amacı en kısa sürede, en az etkileşim ve düşünme gereksinimi ile gerekli olan bilginin sunulmasıdır.Genelde yönetici konumundaki kişileri sıklıkla kullandıkları ekrandır. Qdms sisteminde Olay Bildirim  Modülü kapsamında Dashboard özelliği getirilmiştir. Menü görme yetkisine bağlı olarak bu ekran gelmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_532.png)

Dashboard menüsü tıklanıldığında liste ve filtre sekmesi olmak üzere iki sekme karşımıza çıkmaktadır.

![ref117]

Filtre sekmesinde arama kriterlerine bulunan alanlara göre filtreleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_534.png)

Olay Bildirim  modülünde Dashboard ekranında Liste sekmesinde Planlanan Toplam Ana Form, Toplam Detay Form, Açık Kayıtlar ve Kapalı Kayıtlar alanları sabit alanlar olarak ekrana gelerek üzerinde herhangi bir düzenleme işlem yapılmamaktadır.Bu sabit alanlarda toplam ve yüzdelik dilimleri ile bilgileri verilir.

![ref117] 

Olay Bildirim  modülünde Modül yöneticileri istedikleri grafık tasarlama işlemi yaparak grafik sayısı artırabilirler.

![ref117]

Olay Bildirim Modülü  Dashboard ekranında kaç tane grafik olacağı, grafiğin adının ne olacağı, grafiklerin sırasını ne olacağı Z ekseninde, Y ekseninde hangi alanlar olacağı, grafik boyu, grafik eninin ne olacağı ve grafik tipinin ne olacağı gibi ayarlarmalarla grafik tasarlama işlemini yapılır. Bu ayarlamalarının Olay Bildirim  Dashboard ekranında yapılması için kullanıcının Olay Bildirim modülünde Modül Yönetici olarak tanımlı olması gerekir. (Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Yönetici Tanımlama  menüsünde Olay Bildirim  Modülünde modül yönetici tanımlama işlemi yapılır.)

Kullanıcı Olay Bildirim  Modülünde Modül Yönetici  olmadığında Olay Bildirim  Dashboard ekranında  aşağıdaki ekran görüntüsündeki buton görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_535.png)

Olay Bildirim Modülünde modül Yönetici olarak tanımlı olan kullanıcının Olay Bildirim Dashboard ekranında  birinci buton olan ![ref118]  butonu görüntülenir. Modül Admini olan kullanıcı Olay Bildirim Dashboard ekranında gerekli  ayarlamaları ![ref118] ( Grafik ayarları) butonu yardımıyla grafik tasarlama işlemide yapar.Modül Yöneticileri olmayan kullanıcılar ise Dashboard Konfigürasyonu ekranında Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/ Dashboard Konfigürasyonu/ Olay Bildirim menüsünde gerekli ayarlamalar yapılarak grafik tasarım işlemide yapabilirler.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_537.png) Olay Bildirim  Modülünde grafik tasarlama, listede seçili tasarlanmış grafik  bilgileri güncelleme ve silme işlemleri yapmak için ![ref118]  butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_538.png)

Dashboard Konfigürasyonu ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_539.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref119]: Yeni bir Dashboard tanımlanır.

![ref120]: Listede seçili olan Dashboard bilgisi üzerinde düzeltme/ değişiklik/ güncelleme yapılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_542.png): Listede seçili olan Dashboard bilgisi silinir.

- : Dashboard Konfigürasyonu ekranı kapatılır.

Olay Bildirim Modülünde yeni bir Dashboard  ekleme işlemi için  ![ref119]  butonu tıklanılır

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_543.png)

Dashboard Konfigürasyonu - Yeni Kayıt ekranında gerekli alanlar ilgili bilgiler doldurulduktan sonra ekranın sol üstte yer alan ![ref121] butonu tıklanılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_545.png)

Olay Bildirim  Dashboard ekranında kayıt işleminden sonra sistem tarafından “Grafik ayarlarınız başarıyla kaydedilmiştir.” mesajı verilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_546.png)

Olay Bildirim  Dashboard ekranında tanımlanan Dashboard görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_547.png)

![ref110]  Grafiği aktar butonu tıklanarak grafiği açılır menüden seçilen format türüne (png,jpg,bmp,xls, vb. ) dönüştürerek dış ortama aktarılma işlemide yapılır.

Grafik Boyu min  değeri 500  maxsimum 1000 aralığında sınırlandırılmıştır. Grafik Eni min değeri 550 ve maxsimim değeri 1800 aralığında sınırlandırılmıştır. Bu değerler arasında grafik boyu ve Eni seçilmelidir. Dashboard Konfigürasyonu - Yeni Kayıt ekranında sıra numarası önceden kullanılmışsa kaydetme aşamasında sistem tarafında “Belirtmiş olduğunuz sıra numarası kullanımdadır, kullanımda olmayan bir sıra numarası belirtmelisiniz.”  hata mesajı verilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_548.png) Bu şekilde Grafik Ayarları butonu ile açılan ekranda yeni bir grafik eklenebilir.  Eklenen grafik bilgisi üzerinde düzenleme, güncelleme, değiştirme ve silme işlemleri yapılır. Listede  ilgili grafikler için filtreleme ekranı tanımlanmış ve indirilebilir olarak ayarlanmıştır.

Modül Yöneticileri olmayan kullanıcılar ise Dashboard Konfigürasyonu ekranı Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/ Dashboard Konfigürasyonu/ Olay Bildirim menüsünde tıklayarak açılan ekranda gerekli ayarlamalar yapılarak grafik tasarım işlemide yapılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_549.png)

Olay Bildirim Dashboard Konfigürasyonu ekranında  aynı butonları kullanarak aynı işlem basamakların yaparak yeni bir Dashboard tanımlama işlemi yapabilirler.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_550.png)



[ref1]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_10.png
[ref2]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_22.png
[ref3]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_25.png
[ref4]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_26.png
[ref5]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_28.png
[ref6]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_30.png
[ref7]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_32.png
[ref8]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_34.png
[ref9]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_37.png
[ref10]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_38.png
[ref11]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_39.png
[ref12]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_40.png
[ref13]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_41.png
[ref14]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_42.png
[ref15]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_43.png
[ref16]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_45.png
[ref17]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_75.png
[ref18]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_78.png
[ref19]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_82.png
[ref20]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_90.png
[ref21]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_91.png
[ref22]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_92.png
[ref23]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_95.png
[ref24]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_110.png
[ref25]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_115.png
[ref26]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_116.png
[ref27]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_117.png
[ref28]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_122.png
[ref29]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_123.png
[ref30]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_124.png
[ref31]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_127.png
[ref32]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_140.png
[ref33]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_142.png
[ref34]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_148.png
[ref35]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_149.png
[ref36]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_150.png
[ref37]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_152.png
[ref38]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_153.png
[ref39]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_168.png
[ref40]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_170.png
[ref41]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_171.png
[ref42]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_172.png
[ref43]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_176.png
[ref44]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_180.png
[ref45]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_181.png
[ref46]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_182.png
[ref47]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_185.png
[ref48]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_188.png
[ref49]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_190.png
[ref50]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_201.png
[ref51]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_202.png
[ref52]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_203.png
[ref53]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_204.png
[ref54]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_205.png
[ref55]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_219.png
[ref56]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_220.png
[ref57]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_222.png
[ref58]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_232.png
[ref59]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_245.png
[ref60]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_246.png
[ref61]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_247.png
[ref62]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_253.png
[ref63]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_254.png
[ref64]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_270.png
[ref65]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_274.png
[ref66]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_282.png
[ref67]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_290.png
[ref68]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_296.png
[ref69]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_297.png
[ref70]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_298.png
[ref71]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_299.png
[ref72]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_300.png
[ref73]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_303.png
[ref74]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_304.png
[ref75]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_307.png
[ref76]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_329.png
[ref77]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_343.png
[ref78]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_344.png
[ref79]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_345.png
[ref80]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_346.png
[ref81]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_364.png
[ref82]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_368.png
[ref83]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_374.png
[ref84]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_375.png
[ref85]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_376.png
[ref86]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_389.png
[ref87]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_425.png
[ref88]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_430.png
[ref89]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_433.png
[ref90]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_434.png
[ref91]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_435.png
[ref92]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_441.png
[ref93]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_442.png
[ref94]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_443.png
[ref95]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_444.png
[ref96]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_450.png
[ref97]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_451.png
[ref98]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_462.png
[ref99]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_465.png
[ref100]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_470.png
[ref101]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_473.png
[ref102]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_474.png
[ref103]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_479.png
[ref104]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_482.png
[ref105]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_486.png
[ref106]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_489.png
[ref107]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_490.png
[ref108]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_493.png
[ref109]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_496.png
[ref110]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_497.png
[ref111]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_507.png
[ref112]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_509.png
[ref113]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_510.png
[ref114]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_516.png
[ref115]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_517.png
[ref116]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_518.png
[ref117]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_533.png
[ref118]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_536.png
[ref119]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_540.png
[ref120]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_541.png
[ref121]: https://docsbimser.blob.core.windows.net/imagecontainer/fa758004-e614-4947-bd5b-28eb8d57189f_544.png
