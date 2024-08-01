---
title: Düzeltici ve Önleyici Faaliyetler
description: Düzeltici ve Önleyici Faaliyetler Yardım Dokümanı
sidebar_position: 4
---

:::tip Bilgi

İlgili konu başlığına sağ tarafta bulunan navigasyon yardımıyla hızlı bir şekilde ulaşabilirsiniz.

:::


**DÖF Modülü(v.5.26) Kullanıcı Yardım Dokümanı**

Modül Versiyonu: 5.26



## **1.GİRİŞ**

**“Düzeltici ve Önleyici Faaliyetler Modülü”**, Yönetim Sistemleri içinde yer alan bütün düzeltici faaliyetlerin, belli kurallar dahilinde QDMS sisteminde takip edilmesini sağlayan modüldür.

## **2.AMAÇ** 
Bu yardım kılavuzunun amacı; QDMS “DÖF” Modülünün çalışma sürecini anlatmaktır. İşlemekte olan düzeltici faaliyetleri sistem üzerinden tek çatı altında toplayarak belli bir standartta ilerlemesi amacıyla DÖF Modülü kullanılır.

## **3.SORUMLULUKLAR**
DÖF Açma Yetkisine Sahip Personeller, DÖF Ekip Lideri, DÖF Ekip Üyeleri, Aksiyon Sorumlusu, Aksiyon İşi Yapacak, İzleme Sorumlusu, DÖF Kapatma Onaylayıcısı. Opsiyona Bağlı Sorumluluklar; DÖF Açılış Onaylayıcısı, Etkinlik Değerlendirici, Gelişme Raporu Uygunluk Onaylayıcısı, Aksiyon Açılış Onaylayıcısı, Aksiyon Kapatma Onaylayıcısı.

## **4.KISALTMALAR**

**QDMS**: Kalite Dokümanları Yönetim Sistemi “ Quality Document Management System”

**DÖF**: Düzeltici ve Önleyici Faaliyetler

## **5.İŞ AKIŞI**

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_7.png)


## **6. Düzeltici ve Önleyici Faaliyetler(DÖF veya DİF)**
DÖF ortaya çıkan bir uygunsuzluğun düzeltici aksiyonlar alınarak çözümlenmesini, uygunsuzlukların kayıt altına alınarak ve uçtan uca dijital ortamda etkin bir şekilde yönetilmesini sağlayan modüldür.Bu modül içeriğinde aşağıdaki özellikleri kapsamaktadır.

- Düzeltici/Önleyici faaliyetler ile ilgili alınan aksiyonları anlık takip etme ve otomatik bilgilendirme yapılması sağlanır.
- Geciken işlerde ilgililere ve yöneticilere periyodik hatırlatma yapılması sağlanır.
- DÖF sürecinde istenilen akış ve onay adımlarını tanımlama işlemi yapılır.
- Farklı kök neden analizi yöntemleri kurgulayabilir, kök nedenlere bağlı aksiyon atayabilir.
- Bildirim, gelişme ve sonuç raporu şablonlarını tanımlama işlemi yapılır.
- Müşteri, tedarikçi ve şirket içi olarak farklı rapor formatları tanımlayabilir, sistem tarafından otomatik oluşturulmuş rapor alabilir.
- Müşteriye ve Tedarikçilere özel Global 8 Disiplin (G8D) desteği sağlanır.
- Denetim, Müşteri Şikayet, FMEA, Olay Bildirimi ve Risk Yönetim modülleri ile entegrasyon sağlanır.
- İşlem kaynakları, uygunsuzluk kategorileri ve kök nedenleri kuruma özgü tanımlama işlemi yapılır.
- Uygunsuzluk raporları ve grafikleri alınır.
- Yönetim sistemi ve süreç gibi değişik kriterlerde Düzeltici/Önleyici faaliyetleri izleme yapılır.
- Düzeltici/Önleyici faaliyetler ile ilgili kapatma öncesi ve sonrası etkinlik değerlendirme yapılır.
- Dış uygulamalardan Düzeltici/Önleyici faaliyet kaydı açılması için Web Service desteği sağlanır.
### **6.1. Sistem Altyapı Tanımları/  DÖF**
DÖF modülünün altyapısının oluşturularak tanımlamaların yapıldığı modül altyapısı tasarımının yapıldığı kısımdır. Entegre Yönetim Sistemi menüsünden girişlerde yapılan bu tanımlamalara göre veriler karşımıza çıkmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_8.png)
#### **6.1.1.DÖF Kök Neden**
**Menü Adı**: Sistem Altyapı Tanımları/ DÖF/ DÖF Kök Neden

DÖF Modülü kapsamında firmada kullanılan kök nedenlerin tanımlamasının yapıldığı menüdür. Neden-neden analizine göre kök nedenlerin başlıklarının tanımlanır.  Kök Nedenler sekmesinde uygunsuzluğun kaynağının ne olduğunun tanımlandığı ve bu sekmede uygunsuzluğun kaynaklandığı asıl nedeninin seçimi yapılır. Standart olarak “İnsan, Makine, Metot, Malzeme/  Ekipman, Çevre, Yönetim” olarak belirlense de firmadan firmaya kök nedenler değişmektedir. Sektörler değiştikçe daha özel kök nedenler yazma ihtiyacı doğduğundan, firmalar kendileri için daha anlamlı seçimler yapabilmektedirler.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_9.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref1] : Yeni bir Kök neden tanımlanır.

![ref2] : Listede seçili olan Kök neden bilgisi üzerinde düzenleme/değişiklik/güncelleme işlemi yapılır.

Not: Pasif özelliği ilgili kök neden tipinin artık kullanılmak istenmediğinde, uç kullanıcının görmemesi için kullanılır. Bu işlem yapıldığında eski bilgiler saklanır, fakat uç kullanıcılar pasif edilen tipi seçememektedir.

![ref3] : Listede seçili kök neden bilgisi silinebilir.Uzun süredir kullanılan bir kök neden bilgisinin silinmesi önerilmez, silindiği anda eski kayıtlarda bu tip kullanıldı ise kayıtlar bozulur.

![ref4] : Veriler excele aktarılabilir.( Kök Neden Tanımlama ekranında liste sekmesinde bulunan Kök Neden listesinin Excel formatında raporu alınır.)

Kök Neden Tanımlama ekranına yeni bir Kök Neden eklemek için ekranın sağ üst köşesindeki ![ref1]  butonu tıklanarak Kök Neden Tanımlama\Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_14.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Üst Kök Neden:** Kök Neden Tanımlama ekranında oluşturulma aşamasında olan Üst Kök Neden, bir Kök Neden tanımının alt kırılım olması halinde bu alan otomatik dolu gelir. Dolu olarak gelen alanda bağlı olduğu Kök Neden tanımının adı yazar. Bağlı olduğu üst kırılım silinmek istenildiğinde sağ yanda bulunan ![ref5]  butonu veya değiştirilmek istenildiğinde sağ yanda bulunan ![ref6]  butonu kullanılır. Bağlı olduğu bir üst Kök Neden yok ise bu alan boş gelir.

**Kök Neden No:** Kök Neden Tanımlama ekranında Kök Neden No’su bilgisinin girildiği alandır.

**Kök Neden:** Kök Neden Tanımlama ekranında Kök Neden Tanım bilgisinin girildiği alandır.

**Durum:** Kök Neden Tanımlama ekranında ekranında Kök Neden bilgisinin aktif veya pasif durum bilgisinin seçilebildiği alandır.

Açılan Kök Neden Tanımlama ekranında Kök Neden No ve Kök Neden tanım bilgisi girilir. Durum kısmı Aktif seçilir. Kök Neden Tanımlama ekranında gerekli alanlar doldurulduktan sonra sol üst köşede yer alan  ![ref7]   butonuna tıklanarak Kök Neden Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_18.png)
#### **6.1.2.DÖF İşlem Kaynağı**
**Menü Adı:** Sistem Altyapı Tanımları/ DÖF/ DÖF İşlem Kaynağı

DÖF İşlem kaynağı tanımlama işlemin gerçekleştiği menüdür. İşlem Kaynağı, DÖF’ ün oluştuğu kanalının tanımlamasının yapıldığı kısımdır.DÖF İşlem Kaynakları tanımlamakta amaç; DÖF’ün ortaya nasıl çıktığının yani hangi kanaldan geldiğinin gösterildiği ekrandır. Örneğin Müşteri şikayeti, iş kazası, denetim gibi DÖF İşlem Kaynaklarının belirlendiği menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_19.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref8]: Yeni bir işlem kaynağı tanımlanır.

![ref2]: Listede seçili olan işlem kaynağı bilgisi üzerinde düzenleme/değişiklik/güncelleme işlemi yapılır.

![ref9]: Listede seçili olan işlem kaynağı bilgisi silinir. Uzun süredir kullanılan bir İşlem Kaynağı bilgisi silinmesi önerilmez, silindiği anda eski kayıtlarda kullanıldı ise kayıtlar bozulur.

![ref10]: Veriler Excel’ e aktarılır.( İşlem kaynağı Tanımlama ekranında liste sekmesinde bulunan İşlem kaynağı listesinin Excel formatında raporu alınır.)

![ref11]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref12]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref13]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

İşlem Kaynağı Tanımlama ekranına yeni bir İşlem kaynağı eklemek için ekranın sol üst köşesindeki ![ref8]  butonu tıklanarak İşlem Kaynağı Tanımlama** ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_26.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**İşlem Kaynağı No:** İşlem Kaynağı Tanımlama ekranında İşlem Kaynağı No bilgisinin girildiği alandır.

**İşlem Kaynağı:** İşlem Kaynağı Tanımlama ekranında İşlem Kaynağı tanım bilgisinin girildiği alandır.

**İşlem Kaynağı Tipi:** İşlem Kaynağı Tanımlama ekranında İşlem Kaynağı Tipi bilgisinin seçilebildiği alandır. İşlem kaynak tipi alanında açılır seçenek listesi toplam olarak 4 seçenek işlem kaynak tipi olarak tanımlıdır. Bunlar Şirket İçi, Şirket Dışı, Müşteri Şikayeti ve Tedarikçi işlem kaynak tipleridir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_27.png)

Seçilen tipi göre DÖF İşlemleri -Yeni Kayıt ekranında kullanıcıların karşılaştığı yer başlığı değişir: 

- Şirket içi seçildiğinde, uygunsuzluğu karşılaşıldığı bölüm seçme alanı gelir. DÖF İşlemleri -Yeni Kayıt ekranında Uygunsuzluğun olduğu Bölüm alanında ![ref14] butonu tıklanarak  sistemde tanımlı departman listesinden görüntülenir ve departman listesinde departman seçimi yapılır.

  ![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_29.png)

- Şirket Dışı seçildiğinde, müşteri seçme alanı gelir. DÖF İşlemleri -Yeni Kayıt ekranında Müşteri alanında ![ref14] butonu tıklanarak sistemden tanımlı Müşteri listesi görüntülenir ve Müşteri listesinde müşteri seçimi yapılır.

  ![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_30.png)

- Tedarikçi seçildiğinde, Tedarikçi seçme alanı gelir. DÖF İşlemleri -Yeni Kayıt ekranında Tedarikçi alanında ![ref15] butonu tıklanarak sistemde tanımlı Tedarikçi Listesi görüntülenir ve Tedarikçi listesinden tedarikçi seçimi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_32.png)

- Müşteri Şikayeti seçildiğinde ise Müşteri Şikayeti Modülü ile konuşan bir işlem kaynağı oluşturulmuş olunur. Müşteri Şikayeti kimden geldiği belli olduğunda seçmeye gerek kalmaz. Müşteri Şikayet Modüllerinde DÖF açılan,** DÖF İşlemleri -Yeni kayıt ekranında işlem kaynağı alanında  işlem kaynakları listesi  görüntülenir ve bu işlem kaynaklarından seçim yapılır.Müşteri Şikayeti seçilen işlem kaynakları DÖF modülünde DÖF İşlemleri-Yeni Kayıt ekranında görüntülenmez.

**Denetim:** İşlem Kaynağı Tanımlama ekranında Denetim ve Denetim Değil seçenekleri seçilebildiği alandır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_33.png)

Denetim seçeneği seçildiğinde işlem kaynağı Denetim Faaliyetleri Modülünde DÖF açılan, DÖF İşlemleri -Yeni kayıt ekranında işlem kaynağı alanında  işlem kaynakları listesinde görüntülenir. “Denetim değil” seçeneği seçilen işlem kaynakları Denetim Faaliyetleri Modülünde DÖF açılan, DÖF işlemleri-Yeni Kayıt ekranında işlem kaynağı alanında listesinden görüntülenmez. Denetim Faaliyetleri Modülünde DÖF açılan,  DÖF Kaydı tanımlama ekranı olan DÖF İşlemleri -Yeni Kayıt ekranında işlem kaynakları alanında hangi işlem kaynaklarının görüntülenip, görüntülenmeyecek bu alanda belirlenir.** Denetim Faaliyetler Modülü ve DÖF Modülü  ile ilişkisi kurulması istenilen işlem kaynakları için kullanılır. Denetimden Faaliyetleri Modülünde  DÖF açıldığı anda kullanıcının karşısına Denetim seçilenler gelir.

DÖF parametrelerinden 162 numaralı “Denetim kaynaklı işlem kaynağı seçilebilsin mi ?” parametresinin parametre değeri “Evet” seçilerek parametre Aktif edilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_34.png) Parametre aktif edildikten sonra tanımlanan işlem kaynaklarında “Denetim” seçeneği seçili işlem kaynakları DÖF Modülünde DÖF İşlemleri-Yeni Kayıt ekranında İşlem Kaynağı alanında  İşlem Kaynağı listesinde görüntülenmesi ve bu işlem kaynaklarınında seçilme işlemi yapılması sağlanacaktır.Parametre değeri “Hayır” seçilerek parametre pasif edildiğinde İşlem kaynağı aşamasında “Denetim” seçilir ise  DÖF Modülünde, DÖF İşlemleri-Yeni Kayıt ekranında İşlem Kaynağı alanında İşlem Kaynağı listesinde bu işlem kaynakları görüntülenmez. Denetimden Faaliyetleri Modülünde, DÖF açıldığı anda kullanıcının karşısına Denetim seçilen işlem kaynakları görüntülenir.

**Durum:** İşlem Kaynağı bilgisinin Aktif veya Pasif durum bilgisinin seçilebildiği alandır.

İşlem Kaynağı Tanımlama ekranda İşlem Kaynağı No ve İşlem Kaynağı tanım bilgisi girilir. İşlem kaynağı bilgisi Şirket içi, Denetim bilgisi Denetimde Değil ve Durum kısmı Aktif seçilir. İşlem Kaynağı Tanımlama ekranında gerekli alanlar doldurulduktan sonra sol üst köşede yer alan  ![ref16]  butonu tıklanarak İşlem Kaynağı Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_36.png)
#### **6.1.3.Uygunsuzluk Kategorisi Tanımlama**
**Menü Adı:** Sistem Altyapı Tanımları/ DÖF/  Uygunsuzluk Kategorisi Tanımlama

Uygunsuzluk Kategorisi tanımlama işleminin gerçekleştiği menüdür. Uygunsuzluk kategorisi DÖF’leri analiz edebilmek için önemlidir. Tanımlanan DÖF’lerin kategorize edilmesi amacıyla bu menü kullanılmaktadır.Uygunsuzluk kategorileri tanımlarını gerçekleştirirken, firmanın tecrübe ettiği uygunsuzluklardan yola çıkarak alt kırılımı gerçekleştirmek gerekir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_37.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref8]: Yeni bir uygunsuzluk kategorisi tanımlanır. Direkt yeni butonu ana kategori oluştururken kategorilerden birini seçerek butonu tıklanırsa ilgili kategorinin altına başlık tanımlanmış olur.

![ref2]: Listede seçili olan uygunsuzluk kategorisi bilgisi üzerinde düzenleme/değişiklik/güncelleme işlemi yapılır.

![ref9]: Listede seçili olan uygunsuzluk kategorisi bilgisi silinir. Uzun süredir kullanılan bir uygunsuzluk kategorisinin silinmesi önerilmez, silindiği anda eski kayıtlarda kullanıldığı için  kayıtlar bozulur.

![ref17]: Kayıtlar filtrelenerek arama yapılabilir.

![ref10]: Veriler Excel’ e aktarılır.( Uygunsuzluk Kategorisi Tanımlama ekranında liste sekmesinde bulunan Uygunsuzluk Kategorisi Tanımlama listesinin Excel formatında raporu alınır.)

Uygunsuzluk Kategorisi Tanımlama ekranına yeni bir Uygunsuzluk Kategorisi eklemek için ekranın sol üst köşesindeki ![ref8]  butonu tıklanarak Uygunsuzluk Kategorisi Tanımlama\Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_39.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Bağlı Olduğu Kategori:** Uygunsuzluk Kategorisi Tanımlama - Yeni Kayıt ekranında tanımlama  aşamasında olan Bağlı Olduğu Kategori, bir uygunsuzluk kategorisi tanımının alt kırılım olması halinde bu alan otomatik dolu gelir. Dolu olarak gelen alanda bağlı olduğu Uygunsuzluk Kategorisi tanımının adı yazar. Bağlı olduğu üst kırılım silinmek istenildiğinde sağ yanda bulunan ![ref18]  butonu veya değiştirilmek istenildiğinde sağ yanda bulunan ![ref19]  butonu kullanılır. Bağlı olduğu bir üst uygunsuzluk kategorisi yok ise bu alan boş gelir.

**Uygunsuzluk Kategorisinin Kodu:** Uygunsuzluk Kategorisi Tanımlama ekranında  Uygunsuzluk Kategorisi kodu bilgisi girildiği alandır.

**DÖF uygunsuzluk kategorisi ağaç kırılım formatının ayarlanması;**

Sistem Altyapı Tanımları/DÖF/DÖF Parametreleri menüsü tıklanılır. Açılan Parametreler ekranında listelenen Düzeltici ve Önleyici Faaliyetler Modülü parametrelerinde 131 numaralı “DÖF uygunsuzluk kategorisi ağaç kırılım formatı” parametresi parametreler ekranında Filtre sekmesinde parametre no alanına parametre  numarası yazılarak ![ref20] (Ara) butonu tıklanarak aratılarak seçilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_43.png)

Düzeltici ve Önleyici Faaliyetler Modülü parametrelerinde 131 numaralı “DÖF uygunsuzluk kategorisi ağaç kırılım formatı” parametresi seçildikten sonra ![ref21] butonu tıklanılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_45.png)

Açılan parametreler ekranında parametre değerine ağaç kırılım formatının bilgisi yazılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_46.png)

Parametre değerine ağaç kırılım formatı bilgisi yazıldıktan sonra ekranın sol üstte köşede yer alan ![ref7]  butonu tıklanarak parametre kayıt güncelleme işlemi yapılır. Uygunsuzluk Kategorisi Tanımlama ekranında işleminde parametre yapılan sistemsel ayarlama göre ağaç kırılım formatına göre sistem otomatik kod ataması yapar. Uygunsuzluk Kategorisi kod alanı müdahele edilmesine sistem izin vermez.Örn: 01,02,03 şeklinde Uygunsuzluk Kategorisi kod ataması sırasıyla yapar. Bu parametre ile DÖF uygunsuzluk kategorisi tanımlama ekranında kategori kodlarının nasıl gelmesi belirlenir. Aksi takdirde parametrede parametre değeri boş bırakılırsa, tanımlama yapılırken istenildiği şekilde kod yapısı kullanılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_47.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Uygunsuzluk Kategorisi:** Uygunsuzluk Kategorisi Tanımlama ekranında Uygunsuzluk Kategorisi Tanım bilgisinin girildiği alandır. 

**İş Yeri:** Uygunsuzluk Kategorisi Tanımlama ekranında İş Yeri bağlantısının bilgisinin seçilebildiği alandır. Birden fazla işyeri ile Uygunsuzluk kategorisi ilişkisi kurulabilir. 

Düzeltici ve Önleyici Faaliyetler modülü parametrelerinden 170 numaralı “Döf eklerken İş yerine göre uygunsuzluk kategorileri gelsin mi?” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. Parametre aktif edildikten sonra DÖF İşlemleri -Yeni Kayıt ekranında iş yeri alanında seçim yapıldığında uygunsuzluk kategorisi tanımlama ekranında işyeri ilişki kurulan kategorilere göre o işyeri ile ilgili Uygunsuzluk kategorileri listede yer alması sağlanır.

**Durum:** Uygunsuzluk Kategorisi bilgisinin aktif veya pasif durum bilgisinin seçilebildiği alandır.

Açılan Uygunsuzluk Kategorisi Tanımlama ekranda Uygunsuzluk Kategorisi kodu ve tanım bilgisi girilir. İş Yeri alanında işyeri bağlantısı olan İş yerleri iş yerleri listesinde seçilir. Durum kısmı Aktif seçilir. Uygunsuzluk Kategorisi Tanımlama ekranında gerekli alanlar doldurulduktan sonra sol üst köşede yer alan  ![ref7]   butonuna tıklanarak Uygunsuzluk Kategorisi kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_48.png)

Uygunsuzluk Kategorisi Tanımlama ekranda Filtre sekmesi ile Kategori Kodu, Kategori Adı	

ve Durum gibi alanlarına veri girilip,  ![ref17] (Ara) butonu tıklanarak arama kriterlerine göre filtreleme yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_49.png)
#### **6.1.4.E-Posta Ayarları**
**Menü Adı**: Sistem Altyapı Tanımları/ DÖF/  E-Posta Ayarları

DÖF Modülü süreçlerinin hangi aşamasında kimlere e-posta/ mesaj gönderimi yapılacağı belirlendiği menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_50.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref22]: Listede seçili olan  E-postaları  değeri bilgisi üzerinde düzenleme/değişiklik/güncelleme işlemi yapılır.

![ref11]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref12]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref13]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

**E- Posta Ayarlarında SMS  bildirimi kullanılacak ise;** 

Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/ Parametreler menüsü tıklanılır. Açılan Parametreler ekranında listelenen Sistem Altyapı Tanımları  modülü parametrelerinde 102 numaralı “SMS bildirimi kullanıcak mı?” parametresinin parametreler ekranında Filtre sekmesinde parametre no alanına parametre numarası yazılarak ![ref20] (Ara) butonu tıklanarak aratılarak seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_52.png)

Sistem Alyapı Tanımları modülü parametrelerinde 102 numaralı “SMS bildirimi kullanıcak mı?” parametresi seçildikten sonra ![ref23] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_54.png)

Açılan parametreler ekranın parametre değeri “Evet” seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_55.png)

Parametreler ekranında parametre değeri “Evet” seçildikten sonra ekranın sol üstte yer alan ![ref16]  butonu tıklanarak parametreyi aktif etme kayıt işlemi  yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_56.png)

Parametre Aktif edildikten sonra E- Posta Ayarları ekranında SMS bildirimi kullanılması ile ilgili “SMS gitsin mi?” alanı ile ilgili check box görüntülenir.  İlgili check box işaretlenerek E-Posta ayarlarında SMS bildirimi kullanılır.

Hangi basamakta e-posta/ mesaj gitmesi isteniyorsa seçilir ve  ![ref22]  butonu tıklanılır. 

Örn: “ACMA\_BILDIRIMI “ basamağı seçilir ve ![ref22]  butonu tıklanılır.  

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_57.png)

Açılan “ACMA\_BILDIRIMI”  ekranı görüntülenir. Roller kısmı, e-posta ve mesaj bildirimimin gideceği rolü yani kişiyi göstermektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_58.png)

“ACMA\_BILDIRIMI”  ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_59.png)  butonu tıklanarak açılan sistemde tanımlı Mesaj Gövdesi listesinde gönderilecek mesaj gövdesi ilgili listeden seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_60.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_61.png) butonu ile Mesaj Gövdesinin içeriği detaylı bir şekilde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_62.png)

Mesaj Gövdesi listesinde seçilen Mesaj Gövdesi ![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_63.png) butonu tıklanarak seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_64.png)

Kime E-Posta gitmesi isteniyorsa, o rolle ilgili “E-Posta Gitsin Mi/ SMS Gitsin Mi” check box ‘ı işaretlenir.Mesaj gitmesi için rolde tanımlı olan kişinin cep telefon numarası personel tanımlama ekranında tanımlı olmalıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_65.png)

“ACMA\_BILDIRIMI” ekranında E-Posta gitmesi  rollerle  ilgili “E-Posta Gitsin Mi/ SMS Gitsin Mi” check box ‘ı işaretlendikten sonra ekranın sol üstte köşede yer alan ![ref16]  butonu tıklanarak E- Posta Ayarları kayıt işlemi gerçekleştirilir.
#### **6.1.5.Müşteri Rapor Formatları**
**Menü Adı:** Sistem Altyapı Tanımları/ DÖF/  Müşteri Rapor Formatları 

DÖF Modülünde Müşteri rapor formatlarının tanımlama işlemi yapıldığı menüdür.Her müşteri için ayrı ayrı oluşturulan bildirim, gelişme, sonuç, müşteri ve G8D raporları yüklenir. Yüklenen raporların müşterinin mail adresleri ile iletilme işlemi yapılır. Yüklenen raporların müşterinin mail adresleri ile iletilmesi işlemi için Müşteri-Tedarikçi  tanımlama ekranında müşterilerin mail adreslerinin tanımlı olması gerekmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_66.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref8]:Yeni bir müşteri rapor formatı tanımlanır.

![ref2]: Listede seçili müşteri rapor formatı bilgisi güncellenir.

![ref9]: Listede seçili müşteri rapor formatı bilgisi silinebilir.

![ref11]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref12]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref13]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Bunun için öncelikle Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Rapor Formatları Düzenleme menüsüne oluşturacağımız rapor formatlarının tümü tanımlanmalıdır.

![ref24]

**Ekranda bulanan butonlar yardımıyla;**

![ref25]: Sisteme yeni bir rapor formatı yüklenir.

![ref26]: Listede seçili olan rapor formatı görüntülenip, indirilir.

![ref27]: Listede seçili olan rapor formatı silinir.

![ref28]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref29]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref30]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Varsayılan rapor Formatlarının Düzenlemesi ekranında sisteme yeni bir rapor formatı eklemek için ![ref31]  butonuna tıklanır. Dosya Yükleme ekranında Gözat butonu tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_75.png)

İlgili rapor seçilerek Rapor Formatları Düzenleme menüsüne yükleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_76.png)    

Varsayılan Rapor Formatları Düzenleme ekranında müşteri için ayrı ayrı oluşturulan bildirim, gelişme, sonuç, müşteri ve G8D raporları yüklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_77.png)

Müşteri Rapor Formatları  menüsü tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_78.png)

Müşteri Rapor Formatı  ekranında yeni bir Müşteri Rapor formatı eklemek için ekranın sol üst köşede yer alan  ![ref1]  butonu tıklanarak Müşteri Rapor formatı \Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_79.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Müşteri:** Müşteri Rapor Formatları-Yeni Kayıt ekranında ![ref32] butonu tıklanarak açılan sistemde tanımlı olan Müşteri listesinden Müşteri bilgisinin seçildiği alandır.

**Bildirim Raporu:** Müşteri Rapor Formatları-Yeni Kayıt ekranında Bildirim Raporunun Sistem Altyapı Tanımları/BSAT/ Konfigürasyon Ayarlar/ Rapor Formatları Düzenleme menüsünde adının ve uzantısının kopyalandıktan sonra yapıştırıldığı alandır.

**Gelişme Raporu:** Müşteri Rapor Formatları- Yeni Kayıt ekranında Gelişme Raporunun Sistem Altyapı Tanımları /BSAT/ Konfigürasyon Ayarları/ Rapor Formatları Düzenleme menüsünde adının ve uzantısının kopyalandıktan sonra yapıştırıldığı alandır.

**Sonuç Raporu:** Müşteri Rapor Formatları- Yeni Kayıt ekranında Sonuç Raporunun Sistem Altyapı Tanımları /BSAT/ Konfigürasyon Ayarları/ Rapor Formatları Düzenleme menüsünde adının ve uzantısının kopyalandıktan sonra yapıştırıldığı alandır.

**Müşteri Raporu**: Müşteri Rapor Formatları - Yeni Kayıt ekranında Müşteri Raporunun Sistem Altyapı Tanımları /BSAT/ Konfigürasyon Ayarları/ Rapor Formatları Düzenleme menüsünde adının ve uzantısının kopyalandıktan sonra yapıştırıldığı alandır.

**G8D Raporu:** Müşteri Rapor Formatları- Yeni Kayıt ekranında G8D Raporunun Sistem Altyapı Tanımları /BSAT/ Konfigürasyon Ayarları/ Rapor Formatları Düzenleme menüsünde adının ve uzantısının kopyalandıktan sonra yapıştırıldığı alandır.

Sistem Altyapı Tanımları /BSAT/ Konfigürasyon Ayarları/ Rapor Formatları Düzenleme ekranda, Müşteri için ayrı ayrı oluşturulan bildirim, gelişme, sonuç, Müşteri ve G8D raporları yükleme işlemi yapılır.Müşteri listesinden müşteri seçimi yapıldıktan sonra, rapor formatlarının adı ve uzantısı ilgili alanlara sağ tıkla/kopyala-yapıştır yöntemi ile yapıştırılır. Müşteri Rapor Formatları - Yeni Kayıt ekranında gerekli alanlar ilgili bilgiler girildikten sonra ekranın sol üst köşesindeki ![ref16]  butonu tıklanarak Müşteri Rapor formatları kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_81.png)
#### **6.1.6.Tedarikçi Rapor Formatları**
**Menü Adı:** Sistem Altyapı Tanımları/ DÖF/  Tedarikçi Rapor Formatları

DÖF Modülünde Tedarikçi rapor formatlarının tanımlama işlemi yapıldığı menüdür.Her tedarikçi için ayrı ayrı oluşturulan bildirim, gelişme, sonuç, müşteri ve G8D raporları yüklenir. Yüklenen raporların tedarikçinin  mail adresleri ile iletilme işlemi yapılır. Yüklenen raporların tedarikçi mail adresleri ile iletilmesi işlemi için Müşteri-Tedarikçi  tanımlama ekranında Tedarikçinin  mail adreslerinin tanımlı olması gerekmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_82.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref8]:Yeni bir tedarikçi rapor formatı tanımlanır.

![ref2]: Listede seçili tedarikçi rapor formatı bilgisi güncellenir.

![ref9]: Listede seçili tedarikçi rapor formatı bilgisi silinebilir.

![ref28]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref29]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref30]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Bunun için öncelikle Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Rapor Formatları Düzenleme menüsüne oluşturacağımız rapor formatlarının tümü tanımlanmalıdır.

![ref24]

**Ekranda bulanan butonlar yardımıyla;**

![ref25]: Sisteme yeni bir rapor formatı yüklenir.

![ref26]: Listede seçili olan rapor formatı görüntülenip, indirilir.

![ref27]: Listede seçili olan rapor formatı silinir.

![ref28]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref29]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref30]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Varsayılan rapor Formatlarının Düzenlemesi ekranında sisteme yeni bir rapor formatı eklemek için ![ref31]  butonuna tıklanır. Dosya Yükleme ekranında Gözat butonu tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_83.png)

İlgili rapor seçilerek Rapor Formatları Düzenleme menüsüne yükleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_84.png)

Varsayılan Rapor Formatları Düzenleme ekranında tedarikçi için ayrı ayrı oluşturulan bildirim, gelişme, sonuç, müşteri ve G8D raporları yüklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_85.png)

Tedarikçi Rapor Formatları  menüsü tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_86.png)

Tedarikçi Rapor Formatı  ekranında yeni bir Tedarikçi Rapor formatı eklemek için ekranın sol üst köşede yer alan  ![ref1]  butonu tıklanarak Tedarikçi Rapor formatı \Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_87.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Tedarikçi:** Tedarikçi Rapor Formatları-Yeni Kayıt ekranında ![ref32] butonu tıklanarak açılan sistemde tanımlı olan Tedarikçi listesinden Tedarikçi bilgisinin seçildiği alandır.

**Bildirim Raporu:** Tedarikçi Rapor Formatları-Yeni Kayıt ekranında Bildirim Raporunun Sistem Altyapı Tanımları/BSAT/ Konfigürasyon Ayarları/ Rapor Formatları Düzenleme menüsünde adının ve uzantısının kopyalandıktan sonra yapıştırıldığı alandır.

**Gelişme Raporu:** Tedarikçi Rapor Formatları- Yeni Kayıt ekranında Gelişme Raporunun Sistem Altyapı Tanımları /BSAT/ Konfigürasyon Ayarları/ Rapor Formatları Düzenleme menüsünde adının ve uzantısının kopyalandıktan sonra yapıştırıldığı alandır.

**Sonuç Raporu:** Tedarikçi Rapor Formatları- Yeni Kayıt ekranında Sonuç Raporunun Sistem Altyapı Tanımları /BSAT/ Konfigürasyon Ayarları/ Rapor Formatları Düzenleme menüsünde adının ve uzantısının kopyalandıktan sonra yapıştırıldığı alandır.

**Tedarikçi Raporu**: Tedarikçi Rapor Formatları - Yeni Kayıt ekranında Müşteri Raporunun Sistem Altyapı Tanımları /BSAT/ Konfigürasyon Ayarları/ Rapor Formatları Düzenleme menüsünde adının ve uzantısının kopyalandıktan sonra yapıştırıldığı alandır.

**G8D Raporu:** Müşteri Rapor Formatları- Yeni Kayıt ekranında G8D Raporunun Sistem Altyapı Tanımları /BSAT/ Konfigürasyon Ayarları/ Rapor Formatları Düzenleme menüsünde adının ve uzantısının kopyalandıktan sonra yapıştırıldığı alandır.

Sistem Altyapı Tanımları /BSAT/ Konfigürasyon Ayarları/ Rapor Formatları Düzenleme ekranda, Tedarikçi için ayrı ayrı oluşturulan bildirim, gelişme, sonuç, Müşteri ve G8D raporları yükleme işlemi yapılır Tedarikçi listesinden Tedarikçi seçimi yapıldıktan sonra, rapor formatlarının adı ve uzantısı ilgili alanlara sağ tıkla/kopyala-yapıştır yöntemi ile yapıştırılır. Tedarikçi Rapor Formatları - Yeni Kayıt ekranında gerekli alanlar ilgili bilgiler girildikten sonra ekranın sol üst köşesindeki ![ref16]  butonu tıklanarak Tedarikçi Rapor formatları kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_88.png)
#### **6.1.7.Otomatik Aksiyon**
**Menü Adı**: Sistem Altyapı Tanımları/ DÖF/ Otomatik Aksiyon

DÖF Modülünde Otomatik Aksiyon tanımlama işleminin gerçekleştiği menüdür. Bu menünün kullanım amacı; firmanın her DÖF’te klasikleşen/  kesinlikle aldığı bir aksiyon var ise ve bu aksiyonu belli bir rol yapıyorsa otomatik aksiyon tanıtılıp, kök nedenlerden sonra bu belirtilen aksiyonun otomatik açılması sağlamaktır.DÖF Modülü parametrelerinde 107 numaralı “Otomatik Aksiyon (0 Hiç bir zaman, 1 Kullanıcıya bağlı, 2 Her zaman)” parametre değerine göre otomatik aksiyonun tanımlanmaması, kullanıcıya bağlı olarak tanımlanması veya her zaman tanımlanması ayarı yapılır.Parametre değerine “0” değeri girildiğinde otomatik aksiyon tanımlama işlemi yapılmaz.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_89.png)

Parametre değerine”1” değeri girildiğinde DÖF İşlemleri-Yeni Kayıt ekranında Gelişme Raporu sekmesinde “Otomatik Aksiyon Başlat” alanı ile check box görüntülenir. Kullanıcı isterse ilgili alan ilgili check box işaretleyerek otomatik aksiyon tanımlama işlemini başlatır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_90.png) Parametre değeri “2” olduğunda sistemde otomatik aksiyonlar tanımlı ise sitem otomatik olarak aksiyonları açar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_91.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref8] : Yeni bir Otomatik Aksiyon tanımlanır.

![ref33] : Listede seçili olan Otomatik Aksiyon bilgisi ilgili herhangi bir düzeltme, değişiklik veya güncelleme yapılır.

![ref9] : Listede seçili olan Otomatik Aksiyon bilgisi silinir.

![ref28]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref29]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref30]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Otomatik Açılacak Aksiyonlar ekranına yeni bir Otomatik Aksiyon eklemek için ekranın sol üst köşesindeki ![ref8]  butonu tıklanarak Otomatik Açılacak Aksiyonlar   / Yeni Kayıt** ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_93.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Aksiyon Türü:** Otomatik Açılacak Aksiyonlar ekranında Aksiyon Türü bilgisinin seçilebildiği alandır. Düzeltici, İyileştirici ve Önleyici aksiyon türlerinde seçim yapılır.

**Sorumlu Kişi:** Otomatik Açılacak Aksiyonlar ekranında Sorumlu kişi bilgisinin sorumlu kişi alanında ![ref34] butonu tıklanarak açılan sistemde tanımlı Rol tanımları listesinden seçilebildiği alandır. Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Rol Tanımlama menüsüne Düzeltici ve Önleyici Faaliyetler Modülü için tanımlı Rol tanımları listesi görüntülenir ve uygun rol seçimi yapılır. İstenirse Rol Tanımlama  menüsünde Düzeltici ve Önleyici Faaliyetler Modülü için yeni bir rol tanımlaması yapılır ve seçimide yapılır.

**İşi Yapacak Kişi:** Otomatik Açılacak Aksiyonlar ekranında İşi Yapacak Kişi bilgisinin sorumlu kişi alanında ![ref34] butonu tıklanarak açılan sistemde tanımlı Rol tanımları listesinden seçilebildiği alandır. Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Rol Tanımlama menüsüne Düzeltici ve Önleyici Faaliyetler Modülü için tanımlı Rol tanımları listesi görüntülenir ve uygun rol seçimi yapılır. İstenirse Rol Tanımlama  menüsünde Düzeltici ve Önleyici Faaliyetler Modülü için yeni bir rol tanımlaması yapılır ve seçimide yapılır.

**Aksiyon:** Otomatik Açılacak Aksiyonlar ekranında Aksiyon tanımı bilgisi girildiği alandır.

**Süre (Gün):** Otomatik Açılacak Aksiyonlar ekranında Otomatik Açılacak Aksiyonun süresinin gün olarak girildiği alandır. 

Açılan ekranda Aksiyon Türü Düzeltici seçilir. Sorumlu ve İşi yapacak kişi bilgisi sistemde tanımlı Rol tanımları listesinden seçilir. Aksiyon tanım ve süresi gün olarak bilgisi girilir.

Otomatik Açılacak Aksiyonlar ekranında gerekli alanlar doldurulduktan sonra sol üst köşedeki ![ref16] butonuna tıklanarak Otomatik Açılacak Aksiyonlar kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_95.png)

107 numaralı “Otomatik Aksiyon (0 Hiç bir zaman, 1 Kullanıcıya bağlı, 2 Her zaman)” parametre değeri “0” olduğunda; 

Otomatik Aksiyon Tanımlama menüsünde otomatik Aksiyon tanımlı olsa bile hiç bir zaman DÖF kaydı tanımlandığında otomatik aksiyon açılmaz.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_96.png)

107 numaralı “Otomatik Aksiyon (0 Hiç bir zaman, 1 Kullanıcıya bağlı, 2 Her zaman)” parametre değeri “1” olduğunda;

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_97.png)

DÖF İşlemleri-Yeni Kayıt ekranında yeni bir DÖF kaydı açılır. Açılan bu DÖF kaydı Bekleyen İşlerime “Gelişme Raporu Yazılacak DÖFler Listesi” iş olarak görev düşer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_98.png)

İlgili görevdeki DÖF No alanındaki DÖF kodu linki tıklanılır.Açılan Gelişme Raporu aşamasında “Otomatik Aksiyonları Başlat” alanı ilgili check box işaretlenerek kullanıcıya bağlı olarak otomatik aksiyon açma işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_99.png)Gelişme Raporu aşaması ilgili gerekli alanlar girildikten sonra ekranın sağ üst köşedeki ![ref16] butonu  tıklanarak Gelişme raporu aşaması kayıt işlemi yapılır.Sistem tarafından “339 Nolu Aksiyonlar açılıp ilgili kişilere bilgisi gönderilmiştir” mesajı verilerek otomatik aksiyonun numarası verilerek aksiyonun açıldığı ve ilgili kişilere bilgisinin gidildiği verilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_100.png)

İlgili DÖF kaydında Kök Neden analizi yapıldıktan sonra Aksiyonlar aşamasının yapıldığı Aksiyonlar sekmesinde  Otomatik Aksiyon Tanımlama menüsünde tanımlı aksiyon onay durumunda olduğu görülür.Görüntülenen Aksiyonla ilgili işlem aşamaların yapılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_101.png)

Parametre değeri “2” olduğunda sistem Otomatik Aksiyon Tanımlama menüsünde otomatik aksiyon tanımlı ise otomatik olarak aksiyonu açar. 

Otomatik Açılacak Aksiyonlar menüsünde tanımlı aksiyonlar:

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_102.png)

DÖF kaydı  ekranında gelişme raporu aşaması bittikten sonra sistem tarafından Otomatik Aksiyon menüsünde tanımlı tüm aksiyonlar her zaman açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_103.png)

DÖF işlemleri -Kayıt Güncelleme ekranında Gelişme Raporu sekmesinde Gelişme raporu ilgili alanlar  bilgisi girildikten sonra ekranın sol üst köşesindeki ![ref16]  butonu tıklanılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_104.png) Gelişme raporu kayıt işleminde sonra Sistem Altyapı Tanımları kısmında tanımlı Otomatik aksiyonlar sistem otomatik olarak açma işlemini yapar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_105.png)

Sistem tarafından “392, 393 Nolu Aksiyonlar açılmış ama yayınlanmamıştır”   aksiyon numaralı bilgisi içeriğinde yer alan mesaj verilir. Açılan Aksiyonlardan sonra kök neden sekmesinde kök neden ekleme işlemi yapılarak kök neden analizi yapılır.  Kök Neden analizi işlemi yapıldıktan sonra Aksiyonlar sekmesinda parametredeki 107 numaralı parametredeki parametrede değeri “2” göre sistemde tanımlı otomatik aksiyonların açıldığı görülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_106.png)

Düzeltici ve Önleyici Faaliyetler modülü parametrelerinde 109 numaralı “Otomatik Aksiyon Yayınlama(E (Otomatik) /H (Kullanıcı Yayınlayacak) parametre değeri “Hayır” ise ![ref35] butonu görüntülenir. ![ref35] butonu tıklanarak  otomatik Aksiyonun yayınlama işleminde  kullanıcıya bağlı olarak yayınlama işlemi yapılır.

Örn:

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_108.png)

Bekleyen İşlerimde “Gerçekleştirilecek DÖF Aksiyonları Listesi” olarak iş olarak görev düşen, Otomatik Aksiyonun görevin DÖF Aksiyon No alanında Aksiyon Kodu linki tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_109.png)

Açılan Aksiyonlar aşamasının gerçekleştiği Aksiyonlar sekmesinde ![ref35] butonu görüntülenir ve bu buton tıklanarak Otomatik Aksiyonları yayınlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_110.png)

Düzeltici ve Önleyici Faaliyetler modülü parametrelerinde 109 numaralı “Otomatik Aksiyon Yayınlama(E (Otomatik) /H (Kullanıcı Yayınlayacak) parametre değeri “Evet” olduğunda ![ref35] butonu görüntülenmez sistem otomatik olarak  otomatik aksiyonların yayınlama işlemi yapar.
#### **6.1.8.DÖF Parametreleri**
**Menü Adı:** Sistem Altyapı Tanımları/ DÖF/ DÖF Parametreleri

DÖF Modülü için kullanıcının istek ve ihtiyaçlarına göre çeşitli ayarlamaların yapabildiği ve bunlara göre parametreleri belirlendiği (seçilebildiği) menüdür. Sistemde bu menüde yapılan ayarlamalar sadece DÖF modülünün içeriğini kapsar. Parametrelerde yapılan değişikler tüm Qdms kullanıcılarını kapsamaktadır.Parametreler ekranında Liste ve Filtre sekmesi olmak üzere iki sekme karşımıza çıkar. Liste sekmesinde Düzeltici ve Önleyici Faaliyetler Modülü ile ilgi tüm parametreler listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_111.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref36]: Listede seçili olan parametre bilgisi üzerinde düzenleme/değişiklik/güncelleme işlemi yapılır.

![ref17]: Kayıtlar filtrelenerek arama yapılır.

![ref10]: Veriler Excel’ e aktarılır.( Parametreler ekranında liste sekmesinde bulunan Düzeltici ve Önleyici Faaliyetler Modülü parametrelerin listesinin Excel formatında raporu alınır.)

![ref11]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref12]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref13]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Parametreler  ekranında Filtre sekmesinde, Parametre No ve Parametre Tanımı gibi alanlara veri        girilip,  ![ref17] (Ara) butonu tıklanarak arama kriterlerine göre filtreleme işlemleri yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_113.png)

Bir parametrede değişiklik yapılmak isteniyorsa, değişiklik yapılmak istenilen parametre öncelikle seçilir.  Parametre seçili iken  parametreyi pasif durumundaki parametreyi aktif etme, aktif durumundaki parametreyi pasif etme veya parametre değerini değiştirme gibi işlemler yapılır.

Düzeltici ve Önleyici Faaliyetler Modülü parametrelerinde 5 numaralı “Sonuç Raporu Hazırlama Süresi” parametresi parametreler ekranında Filtre sekmesinde parametre no alanına numarası yazılarak ![ref20] (Ara) butonu tıklanarak aratılarak seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_114.png)

Arama işlemi için Parametreler ekranında liste sekmesinde gridde kolonların karşılığındaki alanlarda kullanılır. Parametre numarası bilinmiyorsa parametre liste sekmesinde gridde Tanım alanında  parametre içerisinde geçen anahtar bir kelime yazılarak aratılma işlemi de yapılabilir. Yada parametre numarası biliyorsa gridde parametre No alanınada parametre numarası yazılırak parametrenin aratılma işlemide yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_115.png)

Parametre seçildiktende sonra ![ref36] butonu tıklanılır.Açılan parametreler ekranında parametre değerinin değiştirilmek istenilen yeni değer bilgisi girilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_116.png)

Parametreler ekranında parametre değerine girilen yeni değer bilgisinden sonra ekranın sol üst köşede yer alan ![ref16]  butonu tıklanarak parametre kayıt güncelleme işlemi yapılır.Yeni girilen parametre değerine göre Aksiyonlar gerçekleştirildikten sonra sonuç raporunun kaç gün içerisinde hazırlanacağını maksimum 10  gün  olarak  sistemsel ayarı işlemi yapılır.

Düzeltici ve Önleyici Faaliyetler modülü parametrelerinde 13 numaralı “Açanın departman sorumlusu bilgilendirmeye eklensin(E/H)?” parametresi parametreler ekranında Filtre sekmesinde parametre no alanına parametre numarası yazılarak ![ref37] (Ara) butonu tıklanarak aratılarak seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_118.png)

Parametre seçildiktende sonra ![ref38] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_120.png)

Açılan parametreler ekranında parametre değeri seçeneklerinde  “Evet” ilgili check box seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_121.png)

Parametreler ekranında parametre değeri “Evet” seçildikten sonra ekranın sol üst köşesinde yer alan ![ref16]  butonu tıklanarak parametre aktif etme kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_122.png)

Düzeltici ve Önleyici Faaliyetler modülünde Uygunsuzluk Kategorisi ile ilgili parametrelerinde liste sekmesinde listelenmesi için Filtre sekmesinde veya gridde Parametre Tanım alanına “Uygunsuzluk Kategorisi” ilgili anahtar kelimeler yazılarak ![ref20] (Ara) butonu tıklanılır.  

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_123.png)

Uygunsuzluk Kategorisinin tanımın içeriğinde geçtiği ve Uygunsuzluk Kategorisi ilgili parametrelerin listelenmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_124.png)

Bu şekilde parametreler ekranında filtre sekmesi arama kriterleri olan alanlar ve Liste sekmesinde griddeki alanlar kullanılarak  ilgili parametrenin aratılma işlemi yapılarak,  ![ref36] butonu tıklanarak içeriği görüntülenen parametreyi aktif etme, aktif edilen parametreyi pasif etme veya parametrenin değerini değiştirme gibi işlemler yapılır. 


#### **6.1.9.Toplu DÖF İptali**
**Menü Adı:** Sistem Altyapı Tanımları/ DÖF/  Toplu DÖF İptali

Sistemde tanımlı DÖF kayıtlarının toplu bir şekilde iptal işlemin yapıldığı menüdür. Bu menünün amacı toplu bir şekilde DÖF kayıtlarının toplu  iptal işlemin gerçekleştirmektir. Bu işlemi DÖF modülünde  gerçekleştirilmesi için Sistem Altyapı Tanımları/ DÖF/ “Toplu DÖF İptali” menüsü tıklanılır. Açılan “DÖF işlemleri” ekranında Liste ve Filtre sekmeleri olmak üzere iki sekme görüntülenir. Listesi sekmesinde sistemde tanımla DÖF kayıtları listenir. Liste sekmesinde istenirse tekli seçim yapılarak tek tek DÖF iptal işlemi veya çoklu seçim yapılarak ![ref39]  butonu tıklanarak açılan “DÖF Red” pop-upn’da Red  nedeni bilgisi yazılarak toplu bir şekilde DÖF kayıtlarının  iptal işlemi yapılır. DÖF  Listesinde “Tümünü seç” seçeneği ile ilgili check box işaretlenerek Toplu bir şekilde DÖF Listesinde DÖF’ kayıtlarının tümü seçilerek![ref39]  butonu tıklanarak açılan “DÖF Red” pop-upn’da “Red  nedeni” bilgisi yazılarak Toplu İptal işlemi  de yapılır. Toplu iptal edilmiş DÖF kayıtlarının durumu “İptal Edilmiş” statüsü olarak değişir. Toplu olarak iptal işlemi yapılan DÖF kayıtları DÖF Modülünü raporlarında Düzeltici ve Önleyici Faaliyetler  Raporunde Filtre sekmesinde durumu “İptal ” olarak statüsü seçilerek listenerek raporu alınması sağlanır

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_126.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref40]: Listede seçili DÖF kaydı görüntülenir.

![ref39]:Listede seçili DÖF Kaydı iptal edilir.

![ref17]: Kayıtlar filtrelenerek arama yapılabilir.

![ref11]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref12]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref13]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Toplu DÖF İptali ekranında DÖF kaydı seçili iken ![ref40] butonu tıklanarak DÖF kaydının görüntüleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_128.png)

Toplu DÖF İptali ekranında İptal edilecek DÖF kayıtları seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_129.png)

![ref39]  butonu tıklanarak açılan “DÖF Red” pop-upn’da Ret nedeni bilgisi yazılarak DÖF kayıtları toplu olarak iptal edilme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_130.png)
#### **6.1.10.Alan Tanımlama**
**Menü Adı:** Sistem Altyapı Tanımları/ DÖF/ Alan Tanımlama

DÖF modülünde alan tanımlama işlemin yapıldığı menüdür. Alan Tanımlama ile tanımlanan alanlarla, DÖF İşlemleri menüsünde Risk Matrisi sekmesinde karşılaşılmaktadır. Alan tanımlama menüsündeki amaç; risk matrisi elemanlarını belirtilip, herhangi bir DÖF’ün firma üzerindeki risk büyüklüğünü hesaplamaktır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_131.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref8]: Yeni bir alan eklenir.

![ref36]: Listede seçili olan alan bilgisi üzerinde  düzeltme/ değişiklik/ güncelleme yapılır.Kod bilgisi güncellenemez.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_132.png):Listede seçili olan alan bilgisi kopyalanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_133.png): Listede seçili olan alan bilgisi silinir.  

![ref41] : Alanın değerleri tanımlanır.

![ref11]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref12]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref13]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Alan Tanımlama ekranına yeni bir alan eklemek için ekranın sol üst köşesindeki ![ref1]  butonuna tıklanarak Alan Tanımlama\ Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_135.png)![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_136.png)

**Açılan ekranda ilgili alanlar tanımlanır;**

**Alan Kodu:** Alan Tanımlama-Yeni Kayıt ekranında Alan Kodu bilgisinin girildiği zorunlu alandır. Daha önce tanımlamış alanlarla aynı olmayacak şekilde boşluk, Türkçe karakter gibi karakterler kullanmadan tanımlanmalıdır. Ör. ‘001’ , ‘RK’

**Alan Adı:** Alan Tanımlama-Yeni Kayıt ekranında Alan Adı bilgisinin girildiği alandır. 

**Başlık Notu:** Alan Tanımlama-Yeni Kayıt ekranında alanı veri girişinin yapılması ile ilgili  açıklayıcı bilgi içeren not bilgisinin girildiği alandır. Mouse ile alanın üzerine gelindiğinde görüntülenen bilgidir.

**Giriş Tipi:** Alan Tanımlama-Yeni Kayıt ekranında giriş tipinin Hesaplanan veya Veri Girişi tipi bilgisinin seçilebildiği alandır. Giriş Tipi seçeneği oluşturulan alanın manuel olarak veri girişi ile mi yoksa hesaplama yöntemi ile mi belirleneceğini gösterir. 

**Alan Tipi:** Alan Tanımlama-Yeni Kayıt ekranında alan tipinin bilgisinin seçilebildiği alandır. Alan Tipi ise oluşturulan alanın metin, nümerik, tarih, liste vb. tiplerinden hangisi olduğunu gösterir. 

**Görünme Şartı:** Alan Tanımlama-Yeni Kayıt ekranında Görünme Şartı bilgisinin girildiği alandır. Bir alan eğer başka bir alanın şartına bağlı olarak görülecekse görünme şartı kullanılır. Liste tipli alanın değerlerine göre oluşturulan alanın görüntülenmesini sağlar. Kullanımı [ALANKODU]=ALAN\_DEĞERİ vb. şekildedir. (Örneğin, Fırsat var mı? Alanının  alan kodu 01; Fırsat alanının alan kodu 02 olsun. Eğer “Fırsat” Alanının, “Fırsat var mı?” Alanındaki seçeneklerden değer kodu 100 olan “Evet” değeri seçili ise görülmesi gerekiyorsa 02 numaraları “Fırsat” alanının görünme şartı bölümüne formül şu şekilde yazılmalıdır: [01]=100)

**Durum:** Alan Tanımlama-Yeni Kayıt ekranında durumun Aktif veya Pasif olarak bilgisinin seçilebildiği alandır. 

**Termin Alanı:** Alan Tanımlama-Yeni Kayıt ekranında Termin alanı aktif edilecekse ilgili check box’ı işaretlenir. Aksiyon ve DÖF’ lerin terminleri buradaki süre göz önüne alınarak belirlenir.

**Güncellemeden değer yükselmesin:** Alan Tanımlama-Yeni Kayıt ekranında “Güncellemeden değer yükselmesin” bilgisi aktif edilecekse ilgili check box’ı işaretlenir. Bu bilginin işaretli olduğu alanlarda puan değeri güncelleme sırasında mevcut değerden daha yüksek olarak girilemez.

**İlişkili Alan:** Alan Tanımlama-Yeni Kayıt ekranında İlişkili alan özelliği ile seçenek tipli iki alan arasında ilişki kurulabilmektedir. Referans alanın elemanlarının tanımlandığı ekranda ilişkili alandan hangi değerler ile ilişkili olduğu seçilebilmektedir. Böylece referans alanın form üzerinde değeri değiştiğinde ilişkili alan seçimli olarak otomatik dolabilmekte ya da seçim ekranından sadece ilişkilendirilen değerler arasından seçim yapılabilmektedir.

**İlişkili Alan Otomatik Doldurulusun:** Alan Tanımlama-Yeni Kayıt ekranında ilişkili alan otomatik doldurulsun seçeneği aktif edilecekse ilgili check box’ı  işaretlenir. Liste tipli iki alanın değerleri arasında kurulan ilişkiye göre alanlardan birinin otomatik doldurulmasını sağlar.

**Genişlik:** Alan Tanımlama-Yeni Kayıt ekranında genişlik bilgisinin girildiği alandır.

Alan Tanımlama-Yeni Kayıt ekranında ekranında gerekli alanlar doldurulduktan sonra sol üst köşede yer alan  ![ref7]   butonuna tıklanarak alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_137.png)

Olasılık alanına değer eklemek için olasılık alanı seçili iken ![ref41]  butonuna tıklanarak alanın değerlerinin tanıtılacağı ekrana gelinir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_138.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref8]:Yeni bir değer tanımlanır

![ref42]: Listede seçili değer bilgisi üzerinde düzenleme/güncelleme/değişiklik yapılır.

![ref3]: Listede seçili değer bilgisi silinir.

![ref43]: Kayıtlar filtrelenerek arama yapılabilir.

![ref44]: Şablon indirilir.

![ref45]: Şablon yüklenilir.

![ref46]: Veriler Excel’ e aktarılabilir.

![ref28]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref29]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref30]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Not: ![ref44] ve ![ref45] butonları ile sisteme toplu olarak alan değerleri aktarılabilmektedir. ![ref44] butonu ile sistem şablonu bilgisayara indirir. İlgili şablon kullanıcılar tarafından doldurularak ![ref45] butonu ile sisteme yüklendiğinde şablondaki tüm alan değerleri sisteme aktarılmış olacaktır.

![ref8]  butonuna tıklanarak yeni değer tanımlama işlemine başlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_144.png)![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_145.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Tanım:** Değerler- Yeni Kayıt ekranında tanım bilgisi girilir.

**Açıklama:** Değerler- Yeni Kayıt ekranında Açıklama bilgisi yazılır.

**Değer:** Değerler- Yeni Kayıt ekranında değerin puan karşılığı girilir.

**Durum:** Değerler- Yeni Kayıt ekranında değerin durumu aktif veya pasif olarak seçilir.

**Varsayılan:** Değerler- Yeni Kayıt ekranında ilgili liste değerinin varsayılan olarak alanda görünmesini sağlar.

**Önlem zorunlu mu?:** Değerler- Yeni Kayıt ekranında bu değer seçili olduğunda önlemler sekmesinden en az bir önlem girilmesi zorunlu olur. İlgili alanın değeri seçildiğinde bu değere bağlı önlem alınması zorunluğu getirilir.

Gerekli alanlar doldurulduktan sonra sol üst köşede yer alan  ![ref7]   butonuna tıklanarak değer tanımlama işlemi gerçekleştirilir. Olasılık, şiddet, frekans vb. puanlı liste, liste, arama özellikli liste tipli alanların değer tanımlama işlemleri bu şekilde yapılır. Alan özelliklerine göre bu ekranda değişiklikler olabilmektedir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_146.png)

Olasılık alanı ilgili tüm değerlerin tanımlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_147.png)

Olasılık puanlı liste tipinde olduğu gibi butonlar kullanılarak aynı şekilde Şiddet puanlı liste tipli alanı tanımlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_148.png)

Olasılık puanlı liste tipinde olduğu gibi butonlar kullanılarak aynı şekilde Şiddet puanlı liste alanın tüm değerlerinin tanımlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_149.png)

Giriş tipi olarak veri girişi seçilen alanların tanımlanması yukarıdaki gibi gerçekleştirilir. Giriş tipleri hesaplanan (Risk Büyüklüğü gibi) olacak alanlar ise formülleri ile birlikte tanımlanır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_150.png)

Risk Büyüklüğü alanın tanımlama işlemi için ![ref1] butonu tıklanarak Alan Tanımlama-Yeni Kayıt ekranı açılır

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_151.png) ![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_152.png)

**Açılan ekranda ilgili alanlar tanımlanır;**

**Alan Kodu:** Alan Tanımlama-Yeni Kayıt ekranında Alan Kodu bilgisinin girildiği zorunlu alandır. Daha önce tanımlamış alanlarla aynı olmayacak şekilde boşluk, Türkçe karakter gibi karakterler kullanmadan tanımlanmalıdır. Ör. ‘001’ , ‘RK’

**Alan Adı:** Alan Tanımlama-Yeni Kayıt ekranında Alan Adı bilgisinin girildiği alandır. 

**Başlık Notu:** Alan Tanımlama-Yeni Kayıt ekranında alanı veri girişinin yapılması ile ilgili  açıklayıcı bilgi içeren not bilgisinin girildiği alandır. Mouse ile alanın üzerine gelindiğinde görüntülenen bilgidir.

**Giriş Tipi:** Alan Tanımlama-Yeni Kayıt ekranında giriş tipinin Hesaplanan veya Veri Girişi tipi bilgisinin seçilebildiği alandır. Giriş Tipi seçeneği oluşturulan alanın manuel olarak veri girişi ile mi yoksa hesaplama yöntemi ile mi belirleneceğini gösterir. Giriş Tipi seçeneği Hesaplanan olarak seçilir.

**Formül Tipi :** Alan Tanımlama-Yeni Kayıt ekranında alanda kullanılacak formül tipi seçeneğinin Excel veya SQL olarak seçildiği alandır. SQL formül tipi seçeneğinde kullanıcak formül için Bimser Destek Ekibinde yardım almak gerekir.Formül Tipi Excel seçeneği olarak seçilir.

**Formül:** Alan Tanımlama-Yeni Kayıt ekranında seçilen formül tipine göre yazılacak formül bilgisinin girildiği alandır. Excel formül tipi seçeneği seçildiği için ilgili alana Excel Formülü yazılır.

**Alan Tipi:** Alan Tanımlama-Yeni Kayıt ekranında alan tipi seçeneklerinde seçim yapıldığı alandır. Alan tipleri Metin, Nümerik ve Liste tipli seçeneklerdir.Genelde formül için Nümerik alan tipi seçilir

**Görünme Şartı:** Alan Tanımlama-Yeni Kayıt ekranında Görünme Şartı bilgisinin girildiği alandır. Bir alan eğer başka bir alanın şartına bağlı olarak görüntülünecekse görünme şartı kullanılır. Liste tipli alanın değerlerine göre oluşturulan alanın görüntülenmesini sağlar. Kullanımı [ALANKODU]=ALAN\_DEĞERİ vb. şekildedir. (Örneğin, Fırsat var mı? Alanının  alan kodu 01; Fırsat alanının alan kodu 02 olsun. Eğer “Fırsat” Alanının, “Fırsat var mı?” Alanındaki seçeneklerden değer kodu 100 olan “Evet” değeri seçili ise görülmesi gerekiyorsa 02 numaraları “Fırsat” alanının görünme şartı bölümüne formül şu şekilde yazılmalıdır: [01]=100)

**Durum:** Alan Tanımlama-Yeni Kayıt ekranında durumun Aktif veya Pasif olarak bilgisinin seçilebildiği alandır. 

**Trend:** Alan Tanımlama-Yeni Kayıt ekranında  tanımlanan riskin trend olarak gösterimi yapılacak ilgili alanla ilgili check box’ın işaretlendiği alandır.

Alan Tanımlama-Yeni Kayıt ekranında ekranında gerekli alanlar doldurulduktan sonra sol üst köşede yer alan  ![ref7]   butonuna tıklanarak alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_153.png)

Formül girişleri ilgili alanların tanımlama ekranlarında gerçekleştirilir. Örnek olarak bir formül aşağıdaki gibi analiz edilebilir.Risk Büyüklüğü ile ilgili formülde  [01]\*[02]+[01]/[02] şeklinde yazılan bir alanda köşeli parantez içinde yazılan ifade alan kodlarını temsil etmektedir. Bu ifadeler alan tanımlama ekranında alanları tanımlarken kullanıcı tarafından belirlenir. Olasılık alanı için, 01; Şiddet alanı için,  02 olarak kodlama yapılmış formül, ([[01]\*[02]+[01]/[02] şeklinde olacaktı. Bu formülün sonucu olarak Risk Büyüklüğü  Alanı, Olasılık ve Şiddet alanında seçilen değerlerin çarpımı alınarak ,Olasılık ve Şiddet alanın bölümün alınarak sonuçlarının toplamı olmak  üzere sistem tarafından otomatik olarak hesaplanacaktır. 

**Sistemde mevcut bulunan alan tiplerinin tam listesi aşağıda belirtilmiştir**;

**Metin:** Metin kutucuğu ekler.

**Metin Çok Satırlı:** Çok satırlı metin kutucuğu ekler.

**Nümerik-Parasal:** Parasal değer olarak nümerik giriş yaptırır.

**Nümerik-Birim:** Birim olarak nümerik giriş yaptırır.

**Tarih:** Takvim alanı ekler.

**Liste:** Birden fazla element arasından tek seçim yaptırır.

**Puanlı Liste:** Açılır menüden tekli seçim yaptırır, liste elementlerinin puan değerleri mevcuttur.

**Arama Özellikli Liste:** Açılır menü altından birden fazla seçim yapılmasını sağlar.

**Ağaç Liste:** Ağaç dallanması şeklinde menü altından birden fazla seçim yapılmasını sağlar.

**Personel:** QDMS Personel veri tabanından kişi bilgisi seçilebilmesini sağlar.

**Departman:** QDMS Departman veri tabanından departman bilgisinin seçilebilmesini sağlar.

**Ünvan:** QDMS ünvan veri tabanından ünvan bilgisinin seçilebilmesini sağlar.

**Doküman:** QDMS Doküman veri tabanından doküman seçilebilmesini sağlar.

**Yönetim Sistemi:** QDMS Yönetim Sistemi veri tabanından yönetim sistemi bilgisi seçilebilmesini sağlar.

**Müşteri:** QDMS Müşteri veri tabanından müşteri bilgisi seçilebilmesini sağlar.

**Tedarikçi:** QDMS Tedarikçi veri tabanından tedarikçi bilgisi seçilebilmesini sağlar.

**Ürün:** QDMS Ürün veri tabanından ürün bilgisinin seçilebilmesini sağlar.

**Şirket Profili:** QDMS Şirket Profili veri tabanından şirket profili bilgisi seçilebilmesini sağlar.

**Başlık:** Risk formuna ya da detay ekranına başlık ekler.

**Dosya:** Dosya ekler.

**Resim:** Resim ekler.

**Resim Liste**: Resim listesinden seçim sağlar.

**Çoklu Resim:** Çoklu resim seçilmesini sağlar.

**Tablo:** Tablo verilerinin kullanılmasını sağlar.

**Sorgu:** Sorgulama şeklinde seçim sağlar.

**Sorgu Ağaç:** Ağaç dallanması şeklinde sorgu yapılmasını sağlar.
#### **6.1.11.Fonksiyon Dizayner**
**Menü Adı:** Sistem Altyapı Tanımları/ DÖF/  Fonksiyon Dizayner

DÖF Modülünde tanımlanan alanları Risk matrisine bağlama işleminin gerçekleştiği menüdür. DÖF modülü parametrelerinde 140 numaralı “Risk Matrisi Kullanılacak mı?” parametresi parametre değeri “Evet” seçilerek parametre aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_154.png)

Parametre aktif edildikten sonra DÖF işlemleri -Yeni Kayıt ekranında Risk matrisi sekmesinde ilgili alanların görüntülenip ve bu alanları veri girişleri yapılarak herhangi bir DÖF’ün firma üzerindeki risk büyüklüğünü hesaplanması sağlanır.Bunu yapmak için Sistem Altyapı Tanımları/ DÖF/ Fonksiyon Dizayner Menüsüne gelinir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_155.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref47]: Alanları fonksiyonlarla ilişkilendirilir.

![ref11]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref12]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref13]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranında kullanıcı bazlı tasarlama işlemi yapılır.

Fonksiyon Dizayn ekranında ![ref47]  butonu tıklanılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_157.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref8]: Listede seçili fonksiyona yeni bir alan eklenir.

![ref36]:Listede seçili eklenen fonksiyona eklenen alan bilgisi üzerinde değişiklik/düzenleme/güncelleme işlemi yapılır.

![ref9]: Listede seçili eklenen fonksiyona eklenen alan bilgisi silinir.

![ref48]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref49]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref50]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Açılan Fonksiyon Dizayn - Alanlar – Risk Matrisi  ekranda seçili olan fonksiyonda kullanılacak alanlar  ![ref8]  butonuna tıklanarak belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_161.png) ![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_162.png)

**Açılan ekranda ilgili alanlar tanımlanır;**

**Alan Adı:** Alan Tanımlama - Fonksiyonlar - Yeni Kayıt ekranında tanımlanan ilgili alan adı seçilir.

**Zorunlu Mu? :** Alan Tanımlama - Fonksiyonlar - Yeni Kayıt ekranında seçilen alan için veri girişinin zorunlu olup olmadığı belirlenir. “Evet” seçeneği seçildiğinde alan için veri girişi zorunludur.

**Zorunluluk Mesajı:** Alan Tanımlama - Fonksiyonlar - Yeni Kayıt ekranında seçilen alan için Zorunluluk Mesajı bilgisinin girildiği alandır. Zorunlu alanlar doldurulmadığında verilecek uyarı mesajı bilgisi yazılır.

**Sıra No:** Alan Tanımlama - Fonksiyonlar - Yeni Kayıt ekranında seçilen alanın ekranda kaçıncı sırada görüntüleneceği bilgisinin girildiği alandır.

**Varsayılan Rol:** Alan Tanımlama - Fonksiyonlar - Yeni Kayıt ekranında seçilen alan için, rol tanımlama ekranında bulunan hangi rol tarafından onaylanacağı bilgisinin girildiği alandır. 

**Varsayılan Değer Değiştirilmesin:** Alan Tanımlama - Fonksiyonlar - Yeni Kayıt ekranında seçilen alan varsayılan olarak bir değer getiriyorsa getirdiği değerin değiştirmemesini sağlar

**Gridde göster:** Alan Tanımlama - Fonksiyonlar - Yeni Kayıt ekranında seçilen alanın liste grid ekranında gösterilmesi isteniyorsa ilgili check box işaretlenir.

**Satır Sayısı**: Alan Tanımlama - Fonksiyonlar - Yeni Kayıt ekranında seçilen alan için satır sayısı bilgisinin belirlendiği alandır.

**Kolon Genişliği:** Alan Tanımlama - Fonksiyonlar - Yeni Kayıt ekranında seçilen alan için kolon genişliği bilgisinin belirlendiği alandır.

Alan Tanımlama - Fonksiyonlar - Yeni Kayıt ekranında gerekli tüm alanlar doldurulduktan sonra ekranın sol üst köşesindeki ![ref7]  butonuna tıklanarak alanın risk matrisine bağlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_163.png)

Alan havuzuna eklenen alanları tümü aynı şekilde Alan Tanımlama - Fonksiyonlar - Yeni Kayıt ekranında  Risk matrisine bağlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_164.png)

Bu şekilde DÖF İşlemleri -Yeni Kayıt ekranında Risk Matrisi sekmesinde hangi alanların yer alacağı belirlenmiş olur. Risk matrisinin çalışması için, DÖF Modülü parametrelerinde 140. numaralı “Risk Matrisi Kullanılacak mı?”  parametrenin aktif edilmesi gerekir. Parametre aktif edildiğinde DÖF İşlemleri-Yeni Kayıt ekranında Risk Matrisi sekmesi görüntülenir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_165.png)

Risk matrisi sekmesinde ilgili alanların görüntülenip ve bu alanları veri girişleri yapılarak herhangi bir DÖF’ün firma üzerindeki risk büyüklüğünü hesaplanması sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_166.png)

DÖF Modülü parametrelerinden 178 numaralı “Döf modülünde risk seçimi yapılsın mı?” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_167.png)

Parametre aktif edildikten sonra DÖF İşlemleri - Yeni Kayıt ekranında İlişkili Risk sekmesi görüntülenir. Bu sekmede DÖF modülünde  Risk modüllerinde sistemde tanımlı riskler ile ilişki kurulması sağlanır. Bu işlemin yapılması için  tanımlı olan bir DÖF Kaydı tıklanılır. Açılan DÖF İşlemleri -Yeni Kayıt ekranın butonlar yardımıyla risk modüllerinde sistemde tanımlı riskler ile ilişkilendirilme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_168.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref51]: DÖF kaydının seçilen modülde tanımlı risklerin ekleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_170.png):Risk ilişkilendirilmesi yapılan riskin görüntüleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_171.png):Risk ilişkilendirilmesi  yapılan riskin silinme işlemi yapılır.

DÖF İşlemleri - Yeni Kayıt ekranında İlişkili Risk sekmesinde ![ref51]  butonu tıklanılır.   Açılan  Modül listesinde  ilişkilendirilme yapılacak risk modülü  seçilerek ![ref52]  butonu seçim işlemi yapılır.


![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_173.png)

Modül seçim işleminden sonra ilişkilendirilme yapılacak risk modülün sistemde tanımlı riskleri listesi görüntülenir. Risk Değerlendirme Formu-Detaylar ekranında  Risk listesinde seçim yapılarak ![ref52] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_174.png)

Risk Değerlendirme Formu-Detaylar ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_175.png) butonu tıklanarak  bu aşamada  ilişkilendirme işlemi yapılan risk modülüne yeni bir risk tanımlama işlemide yapılır. DÖF işlemleri-Yeni Kayıt ekranında ilişkili Risk sekmesinde risk modülünde  risk ekleme işlemi eklenen riskleri  görüntülenir. 


![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_176.png)
#### **6.1.12. Anket Soru Listeleri(Düzeltici ve Önleyici Faaliyetler)**
**Menü Adı:** Sistem Altyapı Tanımları/ DÖF/ Anket Soru Listeleri(Düzeltici ve Önleyici Faaliyetler)

Düzeltici ve Önleyici Faaliyetler Modülü için Anket Soru listelerin ilgili fonksiyonlar için hazırlandığı menüdür. Anket Soru listelerin (Düzeltici ve Önleyici Faaliyetler) menüsünde  anket görevi parametrelere bağlı olarak Ajan uygulamasıyla birlikte oluşmaktadır.DÖF Kapatma aşamasında “DÖF’ün etkinliği değerlendirilecek mi?” check box ile işaretlenip, DÖF ile ilgili  kayıt kapandıktan minimum 1 gün sonra bu anketler “Bekleyen işlerime” Anket İşlemleri Modülünde” “Doldurulması Gereken Anketler” işi olarak görev düşer. Bu görevin düşmesi için ajan programında ilgili fonksiyonun sunucudan çalıştırılması işlemi mutlaka yapılması gerekmektedir.İlgili Görevdeki anket kodu alanında link tıklanarak Anket doldurma işlemi yapılır.

Anket işlemleri Modülü olmayan kullanıcıların Anket işlemleri modülünde açılan Anket şablonu ekranında olduğu gibi bu modülde ilgili fonksiyon için Anket şablonu tasarlaması amacıyla kullanılmaktadır. Bu fonksiyon  “DÖF Etkinlik Değerlendirme”  fonksiyonudur. Anket Soru Listeleri(Düzeltici ve Önleyici Faaliyetler)ekranında fonksiyon olarak “DÖF Etkinlik Değerlendirme”  fonksiyonu seçildiğinde sol üstteki ![ref53] butonu tıklanarak Düzeltici ve Önleyici Faaliyetler modülü mantığında sistemde şablon anketler bu menüde tasarlanıp kaydedilmesi sağlanmaktadır. Şablon anketler tasarlandıktan sonra Düzeltici ve Önleyici Faaliyetler modülün 1. fonksiyonla ilgili parametresi olan 80 numaralı “Etkinlik Değerlendirme Anket Kodu”parametresinin  parametre değeri  boş ise sistem otomatik olarak anket kodunu parametre değerine  tanımlamaktadır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_178.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref53]: Tanımlanacak ankete soru ekleme işlemi yapılır.

![ref28]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref29]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref30]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

![ref53]  butonu tıklanarak  Anket Modülün yapısındaki soru ekleme işlemin yapıldı ekranı gibi DÖF modülü için ilgili fonksiyon için soru ekleme ekranı görüntülenerek soru seçeneklerinden soru ekleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_180.png)

Düzeltici ve Önleyici Faaliyetler Parametrelerinden 80 numaralı “Etkinlik Değerlendirme Anket Kodu” parametresinin parametre değerine herhangi bir parametre kodu tanımlı olmadığında sistem “Yeni bir anket oluşturulacaktır. Onaylıyor musunuz?”  uyarı mesajına “Tamam” butonu tıklanarak anket soruları ekranı görüntülenir.  

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_181.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_182.png): Sorularınızı yazdırmaya sağlayan butondur.

![ref54]: Anketi bölümlendirerek başlık eklemek istenilirse bu buton kullanılır. Her başlık ayıracından sonra tanımlanan sorunun numarası 1 olarak gelir. 

![ref55] : Anketi dolduran kişilere, serbest bilgi girilmesi gereken sorular sorulduğunda, kullanılan soru tipidir. 

![ref56]: Verilen cevapların belirtilen seçenekler içinden seçilmesi durumunda kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_186.png):Bir sorunun seçeneklerinden tüm seçeneklerin tercih edilip, öncelik sırasına göre listelendiği durumda kullanılır. Seçenekler çoktan aza veya azdan çoğa doğru sıralanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_187.png): Oluşturmak istenilen soruda çok fazla şık mevcutsa ve bunların check list gibi seçilmesi gerekiyor ise, çoklu seçim listesi tipinde soru eklenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_188.png): Sorulan sorunun açılır listeden tek cevap seçilmesi durumunda kullanılacak soru tipidir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_189.png): Bu soru tipi Qdms’de tanımlı personel, müşteri, departman, şirket profili ve ürün alanlarındaki listelerin seçilmesini sağlar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_190.png): Soru metni altında alt soruların tanımlama işlemi yapıldığı matris şeklinde oluşturulan soru tipidir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_191.png): Soru metni alanında resim eklendiği ve seçeklerinde resim ekleme işlemi yapıldığı resimli matris şeklindeki soru tipidir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_192.png): Tıklanarak açılan ekranda, kullanıcıya tarih seçtirilecek soru eklenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_193.png): Ankete Ek dosya ekleme işlemi için Ek Dosya alanı oluşturur.** 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_194.png): Anket İşlemler modülü alt yapısında bulunan Soru Havuzu menüsünde açılan Soru Kategorileri ekranında tanımlı soru kategorileri listesinde seçim yapıldığı soru tipidir.

**Örnek Soru seçenekleri ekleme;**

![ref54] butonu tıklanarak Anket bölümlendirilerek başlık eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_195.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_196.png)

Başlık ekle alanına ilgili başlık eklenilerek ![ref57] butonuyla kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_198.png)

![ref55] butonu tıklanarak serbest bilgi girilmesi için tanımlanacak soru tanımlanır. Bir Metin alanı oluşturulur ve bu metin alanın kaç satırdan oluşacağında soru tanımlama ekranında ayarlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_199.png)

**Açılan ekranda ilgili alanlar tanımlanır;**

**Soru Metni:** Sorulacak soru metni, Türkçe alana yazılır. Diğer dillerde kullanım olması durumunda ilgili dillerin olduğu alana sorulacak soru verisi girilir.

**Satır Sayısı:** Satır sayısı, metnin büyüklüğünü belirlemek için kullanılır. 0 veya 1 olması durumunda cevap verilecek alan tek satır olarak görülür.

Sorulacak sorunun cevap verme zorunluluğu bu alandan belirlenir. Cevap zorunluluğu var ise soru cevaplanmadığında kaydetmeye izin verilmez, uyarı mesajı verilir.

**İlişkili Soru/Seçenek:** Bir sorunun, seçeneklerinden biri ile ilişki kurulduğunda, ilişkili sorunun çıkması istenilirse ilişkili soru/seçenek kısmından bağlantı sağlanır.

Sorulacak soru metni Türkçe alana yazılarak ![ref58]  butonuyla kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_201.png)

![ref56]  butonu tıklanarak verilen cevapların beliritilen seçeneklerden seçilme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_202.png)![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_203.png)

**Açılan ekranda ilgili alanlar tanımlanır.**

**Soru Metni:** Sorulacak soru metni, Türkçe alana yazılır. Diğer dillerde kullanım olması durumunda ilgili dillerin olduğu alana sorulacak soru verisi girilir.

**Seçenek/Puan:** Bu alana sorunun seçenekleri girilir. Eğer anket, puanlı bir anket olacaksa, girilen seçenekler için puan da yazılmalıdır.

Sorulacak sorunun cevap verme zorunluluğu bu alandan belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_204.png)

Seçeneklerden 1 veya 1’den fazlasının seçilebilmesi bu alandaki check box’a göre belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_205.png)

Seçeneklerin yan yana (Tek Satırlı) veya alt altta (Çok Satırlı) dizili olarak görülmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_206.png)

Eğer çok satırlı seçeneği işaretlenirse kolon sayısı diye bir alan çıkar ve sorunun seçenekleri belirlenen değer kadar, kolonda görüntülenir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_207.png)

**Min/Max Seçim Sayısı :**Minimum ve maxsimum soru seçim sayısının belirlendiği alandır.(Birden Fazla seçenek seçilebilir seçeneği işaretli olduğunda bu alan görüntülenir)

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_208.png)

**Hesaplama Yöntemi:** Anketin puanlı anket olması durumunda,  bu sorunun seçeneklerine verilen puanların hangi yöntemle hesaplanılacağının belirlendiği alandır. Örneğin; 10 kişinin cevaplayacağı anketteki bir sorunun 4 seçeneği ve her bir seçeneğin kendine has puanları vardır. İlk seçeneğin puanının 5 olduğunu varsayarsak, 10 kullanıcının ilk seçeneği seçmesi halinde, bu puanlar toplanarak mı (50) veya ortalaması alınarak mı (5) anketin ortalama puanına dahil edilme durumu belirlenir.(Birden Fazla seçenek seçilebilir seçeneği işaretli olduğunda bu alan görüntülenir)

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_209.png)

**Ağırlıklı Puan:** Anketin puanlı anket olması durumunda sorunun anket içindeki ağırlığının belirlendiği alandır. Tüm sorular eş değer ağırlıktaysa 1 değeri yazılmalıdır. 0 olarak yazıldığı durumda anket puanı hesaplanmaz.

**İlişkili Soru/ Seçenek:** Bir sorunun başka bir sorunun seçeneğindeki şarta bağlı olarak görünmesi istenirse ilişkili soru/seçenek mantığı kullanılır.

İlgili alanlar doldurulduktan sonra ![ref58]  butonu tıklanarak kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_210.png)

Anket Soru Listeleri(Düzeltici ve Önleyici Faaliyetler) menüsünde İlgili fonksiyon seçili iken ![ref53] butonu tıklanarak açılan Anket soruları ekranında örnek olarak birkaç soru seçeneği tanımlanarak Anket Soru Listeleri(Düzeltici ve Önleyici Faaliyetler) tanımlama işlemi yapılır. Diğer soru seçeneklerin tanımlama işlemi Anket İşlemleri Modülünün soru tanımlama ekranındaki aynı şekilde yapılmaktadır. Açılan ekranda Anket İşlemleri soru tanımlama ekranı ile aynıdır. Soru tanımlama işlemi yapıldıktan sonra Anket Soru Listeleri(Düzeltici ve Önleyici Faaliyetler) menüsü ilgili modülün ilgili parametresi olan 80 numaralı “Etkinlik Değerlendirme Anket Kodu” parametresine sistem otomatik olarak anket kodu tanımlar. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_211.png)

Anket Soru Listeleri (Düzeltici ve Önleyici Faaliyetler) menüsünde ![ref53] butonu tıklanarak açılan Anket soruları ekranında anket soru tanımlama işlemi yapıldıktan sonra  DÖF Kapatma aşamasındaki bir DÖF kaydının tıklanarak açılır. Açılan DÖF İşlemleri -Yeni Kayıt Güncelle ekranında kapatma sekmesinde DÖF  Kapatma kısmında “DÖF’ün etkinliği değerlendirilecek mi?” alanı ile  ilgili check box işaretlenir. Etkinlik Değerlendirme süresi alanı ilgili süre bilgisi girilir.“DÖF’ün etkinliği değerlendirilecek mi?” alanı ile ilgili check box işaretlendikten sonra  anket görevi parametrelere bağlı olarak Ajan uygulamasıyla ilgili fonksiyonun sunucudan çalıştırılması ile birlikte oluşmaktadır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_212.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_213.png)Anket ilgili DÖF Modülü parametrelerinde 80 numaralı “Etkinlik Değerlendirme Anket Kodu” parametresinde kod tanımlı olmadığında Anket Soru Listeleri(Düzeltici ve Önleyici Faaliyetler) menüsünde anket tanımlanırsa, tanımlanan anketin kodu sistem parametreye otomatik olarak tanımlanır. DÖF Modülü ile ilgili diğer bir parametrede 83 numaralı “Etkinlik değerlendirme anketi geçerlilik süresi” parametresinin parametre değeri girilmesi gerekir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_214.png)

DÖF ile ilgili  kayıt kapandıktan minimum 1 gün sonra bu anketler “Bekleyen işlerime” Anket İşlemleri Modülünde “Doldurulması Gereken Anketler” işi olarak görev düşer.**    

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_215.png)

İlgili görevdeki Anket kodu alanındaki Anket kodu linki tıklanarak Anket Doldurma ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_216.png)

Anket doldurma ekranında anket soruları ilgili bilgiler girilerek anket doldurma işlemi yapıldıktan sonra ekranın sol üstte yer alan ![ref59]  butonu tıklanarak Anket doldurma işlemi gerçekleştirilir.Sistem tarafında verilen “Anketiniz başarıyla kaydedilmiştir” uyarı mesajında “Tamam” butonu tıklanılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_218.png)
#### **6.1.13.Tekrar Eden Kayıtlar Rapor Şablonu**
**Menü Adı:** Sistem Altyapı Tanımları /DÖF/ Tekrar Eden Kayıtlar Rapor Şablonu

DÖF  kayıtlarında yer alan alanların tekrar etme durumunu göre  rapor olarak verildiği menüdür. İlk olarak Sistem Altyapı Tanımları/ DÖF/Tekrar Eden Kayıtlar Raporu Şablonu menüsünden raporda gösterilecek alanlar seçilir ve rapor formatı kaydedilir.Daha sonra Entegre Yönetim Sistemi/Düzeltici ve Önleyici Faaliyetler/Raporlar/Tekrar Eden Kayıtlar raporundan ilgili rapora ulaşılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_219.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref1]: Yeni Tekrar Eden Kayıtlar Şablonu tanımlanır

![ref42]: Listede seçili Tekrar Eden Kayıtlar Şablonu bilgisi güncellenir.

![ref3]: Listede seçili Tekrar Eden Kayıtlar Şablonu bilgisi silinebilir.

![ref11]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref12]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref13]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranında kullanıcı bazlı tasarlama işlemi yapılır.

Tekrar Eden Kayıtlar Raporu Şablonları ekranına yeni bir Tekrar Eden Kayıtlar Raporu Şablonları eklemek için ekranın sol üst köşesindeki ![ref1]  butonu tıklanarak Tekrar Eden Kayıtlar Raporu Şablonları \Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_220.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Tanım:** Tekrar Eden Kayıtlar Raporu Şablonları ekranında Tekrar Eden Kayıtlar Raporu Şablonları tanım bilgisinin girildiği alandır.

**Kolonlar:** Tekrar Eden Kayıtlar Raporu Şablonları ekranında kolonlar bilgisinin seçilebildiği alandır.

Açılan ekranda Tekrar Eden Kayıtlar Raporu tanım bilgisi girilir. İlgili kolonlar seçilir. Tekrar Eden Kayıtlar Raporu Şablonları ekranında gerekli alanlar doldurulduktan sonra sol üst köşedeki  ![ref7]  butonu tıklanarak Tekrar Eden Kayıtlar Raporu Şablonları kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_221.png)

Entegre Yönetim Sistemi/Düzeltici ve Önleyici Faaliyetler /Raporlar/Tekrar Eden Kayıtlar raporundan ilgili rapor şablonu seçilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_222.png)

![ref17] (Ara) butonu ile kayıtlar filtrelenerek arama yapılabilir  ve kayıtlar liste sekmesinde listenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_223.png)

![ref10] (Excel’e aktar) botunu ile Excel formatında tanımlanan Tekrar eden Rapor alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_224.png)
#### **6.1.14.Dashboard/Düzeltici ve Önleyici Faaliyetler** 
Qdms sisteminde  kullanıcılara işlemleri, metrikleri, grafikleri ve raporları tek bir ekranda görüntülemelerine olanak sağlayan kısımdır. Dashboard, bilgi akışını ve/veya içeriğini özetlemek amacıyla kullanılan, grafikler ve tablolar yoluyla belirli bir durumu açıklamaya yarayan göstergeler ekranı, iş panosu ve  göstergeler tablosu olarak ifade edilmektedir. Amacı en kısa sürede, en az etkileşim ve düşünme gereksinimi ile gerekli olan bilginin sunulmasıdır.Genelde yönetici konumundaki kişileri sıklıkla kullandıkları ekrandır. Qdms sisteminde Düzeltici ve Önleyici Faaliyetler   Modülü kapsamında Dashboard özelliği getirilmiştir. Menü görme yetkisine bağlı olarak bu ekran gelmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_225.png)

Dashboard menüsü tıklanıldığında liste ve filtre sekmesi olmak üzere iki sekme karşımıza çıkmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_226.png)

Filtre sekmesinde arama kriterlerine bulunan alanlara göre filtreleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_227.png)

Düzeltici ve Önleyici Faaliyetler modülünde Dashboard ekranında Liste sekmesinde Toplam Döf, Açık Döfler, Gecikmeli Kapalı Döfler, Zamanında Kapanan Döfler, Toplam Aksiyon Sayısı, Açık Aksiyon Sayısı ve Gecikmiş Aksiyon Sayısı  alanları sabit alanlar olarak ekrana gelerek üzerinde herhangi bir düzenleme işlem yapılmamaktadır.Bu sabit alanlarda toplam ve yüzdelik dilimleri ile bilgileri verilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_228.png)

Düzeltici ve Önleyici Faaliyetler Dashboard ekranında ilk açılışta 6 tane varsayılan grafik görüntülenir.Modül Yöneticileri isterlersen grafik sayısı artırabilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_229.png)

Düzeltici ve Önleyici Faaliyetler Dashboard ekranında kaç tane grafik olacağı, grafiğin adının ne olacağı, grafiklerin sırasını ne olacağı Z ekseninde, Y ekseninde hangi alanlar olacağı, grafik boyu, grafik eninin ne olacağı ve grafik tipinin ne olacağı gibi ayarlarmalarla grafik tasarlama işlemini yapılır. Bu ayarlamalarının Düzeltici ve Önleyici Faaliyetler Dashboard ekranında yapılması için kullanıcının Düzeltici ve Önleyici Faaliyetler Modül Yönetici olarak tanımlı olması gerekir. (Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Yönetici Tanımlama  menüsünde Düzeltici ve Önleyici Faaliyetler Modülünde modül yönetici tanımlama işlemi yapılır.)

Kullanıcı Düzeltici ve Önleyici Faaliyetler Modülünde Modül Yönetici  olmadığında Düzeltici ve Önleyici Faaliyetler Dashboard ekranında  aşağıdaki ekran görüntüsündeki buton görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_230.png)

Düzeltici ve Önleyici Faaliyetler Modülünde modül Yönetici olarak tanımlı olan kullanıcının Düzeltici ve Önleyici Faaliyetler Dashboard ekranında  birinci buton olan ![ref60]  butonu görüntülenir. Modül Admini olan kullanıcı Düzeltici ve Önleyici Faaliyetler Dashboard ekranında gerekli  ayarlamaları ![ref60] ( Grafik ayarları) butonu yardımıyla grafik tasarlama işlemide yapar.Modül Yöneticileri olmayan kullanıcılar ise Dashboard Konfigürasyonu ekranında Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/ Dashboard Konfigürasyonu/ Düzeltici ve Önleyici Faaliyetler menüsünde gerekli ayarlamalar yapılarak grafik tasarım işlemide yapabilirler.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_232.png)

Düzeltici ve Önleyici Faaliyetler Modülünde grafik tasarlama, listede seçili tasarlanmış grafik  bilgileri güncelleme ve silme işlemleri yapmak için ![ref61]  butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_234.png)

Dashboard Konfigürasyonu ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_235.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref1]: Yeni bir Dashboard tanımlanır.

![ref42]: Listede seçili olan Dashboard bilgisi üzerinde düzeltme/ değişiklik/ güncelleme yapılır. 

![ref3]: Listede seçili olan Dashboard bilgisi silinir.

- : Dashboard Konfigürasyonu ekranı kapatılır.

Düzeltici ve Önleyici Faaliyetler Modülünde yeni bir Dashboard  ekleme işlemi için  ![ref1]  butonu tıklanılır

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_236.png)

Dashboard Konfigürasyonu - Yeni Kayıt ekranında gerekli alanlar ilgili bilgiler doldurulduktan sonra ekranın sol üstte yer alan ![ref7]  butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_237.png)

Sistem tarafından “Kaydetmek istediğinize emin misiniz?” uyarı mejasında “Tamam” butonu tıklanarak grafik ayarlarının başarı olarak kaydedilmesi işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_238.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_239.png)

Düzeltici ve Önleyici Faaliyetler Dashboard ekranında tanımlanan Dashboard görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_240.png)

![ref62]  Grafiği aktar butonu tıklanarak grafiği açılır menüden seçilen format türüne (png,jpg,bmp,xls, vb. ) dönüştürerek dış ortama aktarılma işlemide yapılır.

Grafik Boyu min  değeri 500  maxsimum 1000 aralığında sınırlandırılmıştır. Grafik Eni min değeri 550 ve maxsimim değeri 1800 aralığında sınırlandırılmıştır. Bu değerler arasında grafik boyu ve Eni seçilmelidir. Dashboard Konfigürasyonu - Yeni Kayıt ekranında sıra numarası önceden kullanılmışsa kaydetme aşamasında sistem tarafında “Belirtmiş olduğunuz sıra numarası kullanımdadır, kullanımda olmayan bir sıra numarası belirtmelisiniz.”  hata mesajı verilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_242.png)

Bu şekilde Grafik Ayarları butonu ile açılan ekranda yeni bir grafik eklenebilir.  Eklenen grafik bilgisi üzerinde düzenleme, güncelleme, değiştirme ve silme işlemleri yapılır. Listede  ilgili grafikler için filtreleme ekranı tanımlanmış ve indirilebilir olarak ayarlanmıştır.

Modül Yöneticileri olmayan kullanıcılar ise Dashboard Konfigürasyonu ekranı Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/ Dashboard Konfigürasyonu/ Düzeltici ve Önleyici Faaliyetler menüsünde tıklayarak açılan ekranda gerekli ayarlamalar yapılarak grafik tasarım işlemide yapılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_243.png)

Düzeltici ve Önleyici Faaliyetler Dashboard Konfigürasyonu ekranında  aynı butonları kullanarak aynı işlem basamakların yaparak yeni bir Dashboard tanımlama işlemi yapabilirler.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_244.png)
### **6.2.Entegre Yönetim Sistemi/ Düzeltici ve Önleyici Faaliyetler**
DÖF Modülünde DÖF işlemleri, DÖF talebi, DÖF onaylama, raporların ve grafiklerin görüntüleme işlemlerinin gerçekleştiği kısımdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_245.png)
#### **6.2.1.DÖF İşlemleri**
**Menü Adı:** Entegre Yönetim Sistemi/ Düzeltici ve Önleyici Faaliyetler /DÖF İşlemleri

Firmada meydana gelen uygunsuzlukların kayıt altına alındığı menüdür. Açılan DÖF işlemleri ekranında iki sekme görüntülenir. Bu sekmeler Liste ve Filtre sekmesidir.

**Liste sekmesi;** 

DÖF Modülü kapsamında DÖF işlemleri ekranında sistemde tanımlı DÖF kayıtlarının listesi yer alır. Bu sekmede ilgili butonlar kullanılarak yeni bir DÖF Kaydı tanımlama, listede seçili DÖF kaydı üzerinde yetkiye bağlı olarak düzenleme/güncelleme/değişiklik yapma, DÖF modülünde modül yöneticisi olarak tanımlı kullanıcıların seçili DÖF kaydını silme ve kayıt bakım özelliği kullanma, seçili DÖF kaydını iptal etme, parametreye bağlı kalınarak DÖF yaygınlaştırma gibi işlemleri yapılması sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_246.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref8] :Yeni bir DÖF kaydının sisteme girilip, tanımlama işlemi yapılır.

![ref33] :Listede seçili DÖF kaydı üzerinde yetki olması halinde değişiklik/günceleme/düzenleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_247.png) :Listede seçili DÖF kaydının tüm bilgilerini görüntüleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_248.png) :Listede seçili DÖF kaydının bağlı Müşteri Şikayeti varsa şayet ilgili kayda götürülme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_249.png):Listede seçili DÖF kaydının düzeltmeler için kullanılan kayıt bakım butonudur.Bu butonun görüntülenmesi için DÖF Modülün Modül Yönetici olmak gerekir. Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Yönetici Tanımlama menüsünde  DÖF Modülünde yönetici tanımlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_250.png) :Listede seçili DÖF kaydının silmek istenirse kullanılacak butondur. Sistem Yöneticilerinde çıkar. Uç kullanıcılarda görünmez. Bu  butonun görüntülenmesi için  kullanıcının DÖF Modülün Modül Yönetici olması gerekir. Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Yönetici Tanımlama menüsünde  DÖF Modülünde yönetici tanımlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_251.png) : Parametrik bir buton olmakla birlikte Sistem Yöneticilerin ekranında çıkar. DÖF kayıtlarının  iptal etmek için kullanılır. Silmekten farklı bir işlemdir. DÖF kaydının  İşleyişi durur fakat sistem de kayıtlı olmaya devam eder. Bir onay akış çerçevesinde çalışır. Bunun için alt yapıda akışın tanımlanması gereklidir.  Akış Tanımlama Sistem Altyapı Tanımları/Konfigürasyon Ayarları/Akış Tanımlama menüsünden tanımlanır.(İptal edilmek istenen DÖF kayıtlarının hangi rol tarafından onaylanacağı veya red edilecek olduğunu belirlemek için Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Akış Tanımlama menüsüne gelinir ve DÖF İptal Onay Akışı ![ref36]  butonuyla role bağlanır.)

![ref63]: DÖF Modülünde açılan DÖF kaydının  işyerinin diğer lokasyonları veya departmanlarda da uygulanmak isteniliyorsa DÖF Yaygınlaştırma özelliği kullanılır.DÖF Modülü  parametrelerinden 163 numaralı  “Döf işlemlerinde yaygınlaştırma olacak mı?” parametresinin  parametre değerinin “Evet” seçilerek parametre aktif edilmelidir.  Parametre aktif edildiğinde ![ref63] butonu DÖF işlemleri- Yeni Kayıt ekranında görüntülenir ve bu özellik kullanılır.

![ref64]

DÖF Modülü parametrelerinde 165 numaralı “Kimler yaygınlaştırma yapabilecek?(Modül Yöneticileri=M,Açan=A,Ekip Lideri=E,Herkes=H)(Birden fazla için virgülle ayırınız)”  parametresine girilen değere göre kimlerin DÖF modülünde yaygınlaştırma işlemi yapacağı belirlenir.

![ref65] : DÖF kaydının  herhangi bir aşamasına göre çıktı alma işlemi yapılır. Hangi aşamaya kadar rapor alınmak istenilirse seçim yapılarak ![ref65] (Yazdır) butonuna tıklanır. Seçili kayıda ait rapor bilgisayara çekilmiş olur. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_255.png)

**Bildirim Raporu;**

DÖF kayıtları için  Bildirim Raporunun DÖF Yazdırma ekranında alınması için  Rapor formatları düzenleme menüsünde Bildirim Raporu şablon dosyasının yüklenerek Düzeltici ve Önleyici Faaliyetler Modülü parametrelerinde 65 numaralı “DÖF bildirim raporu şablon dosyası” parametre değerine tanımlanması gerekir. Tanımlama işlemi için öncelikle Rapor Formatları Düzenleme menüsünde ![ref8]  butonu ile raporunun yüklenmesi gerekir. Yüklenen rapor formatı şablonun adı ve uzantısı birlikte ilgili parametreye  sağ tıkla/kopyala-yapıştır yönetimi ile yapıştırılması gerekir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_256.png)

Bu parametreye tanımlanan  DÖF Bildirim raporu şablonu DÖF Yazdırma ekranında Rapor Tipi “Bildirim Raporu” seçilerek ![ref65] (Yazdır) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_257.png)

DÖF Yazdırma ekranında Bildirim Raporu  Excel formatında alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_258.png)

**Gelişme Raporu;**

DÖF kayıtları için Gelişme raporunun DÖF Yazdırma ekranında alınması için  Rapor formatları düzenleme menüsünde Gelişme Raporu şablon dosyasının yüklenerek Düzeltici ve Önleyici Faaliyetler Modülü parametrelerinde 66 numaralı “DÖF gelişme raporu şablon dosyası” parametre değerine tanımlanması gerekir. Tanımlama işlemi için öncelikle Rapor Formatları Düzenleme menüsünde ![ref8]  butonu ile raporunun yüklenmesi gerekir. Yüklenen rapor formatı şablonun adı ve uzantısı birlikte ilgili parametreye  sağ tıkla/kopyala-yapıştır yönetimi ile yapıştırılması gerekir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_259.png)

Bu parametreye tanımlanan DÖF Gelişme raporu şablonu DÖF Yazdırma ekranında Rapor Tipi “Gelişme Raporu” seçilerek ![ref65] (Yazdır) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_260.png)

DÖF Yazdır ekranında Gelişme Raporu Excel formatında alınır.

**Sonuç Raporu;**

DÖF kayıtları için Sonuç raporunun DÖF Yazdırma ekranında alınması için  Rapor formatları düzenleme menüsünde Sonuç Raporu şablon dosyasının yüklenerek Düzeltici ve Önleyici Faaliyetler Modülü parametrelerinde 67 numaralı “DÖF sonuç raporu şablon dosyası” parametre değerine tanımlanması gerekir. Tanımlama işlemi için öncelikle Rapor Formatları Düzenleme menüsünde ![ref8]  butonu ile raporunun yüklenmesi gerekir. Yüklenen rapor formatı şablonun adı ve uzantısı birlikte ilgili parametreye  sağ tıkla/kopyala-yapıştır yönetimi ile yapıştırılması gerekir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_261.png)

Bu parametreye tanımlanan  DÖF Sonuç raporu şablonu DÖF Yazdırma ekranında Rapor Tipi “Sonuç Raporu” seçilerek ![ref65] (Yazdır) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_262.png)

DÖF Yazdırma ekranında Sonuç Raporu Excel formatında alınır.

**Müşteri Raporu;**

DÖF kayıtları için Müşteri raporunun DÖF Yazdırma ekranında alınması için  Rapor formatları düzenleme menüsünde Müşteri Raporu şablon dosyasının yüklenerek Düzeltici ve Önleyici Faaliyetler Modülü parametrelerinde 68 numaralı “	DÖF müşteri raporu şablon dosyası” parametre değerine tanımlanması gerekir. Tanımlama işlemi için öncelikle Rapor Formatları Düzenleme menüsünde ![ref8]  butonu ile raporunun yüklenmesi gerekir. Yüklenen rapor formatı şablonun adı ve uzantısı birlikte ilgili parametreye  sağ tıkla/kopyala-yapıştır yönetimi ile yapıştırılması gerekir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_263.png)

Bu parametreye tanımlanan  DÖF Müşteri raporu şablonu DÖF Yazdırma ekranında Rapor Tipi “Müşteri Raporu” seçilerek ![ref65] (Yazdır) butonu tıklanılır **.**

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_264.png)

DÖF Yazdır ekranında Müşteri Raporu** Excel formatında alınır.

**G8D Raporu;**

DÖF kayıtları için G8D raporunun DÖF Yazdırma ekranında alınması için  Rapor formatları düzenleme menüsünde G8D Raporu şablon dosyasının yüklenerek Düzeltici ve Önleyici Faaliyetler Modülü parametrelerinde 69 numaralı “DÖF G8D raporu şablon dosyası” parametre değerine tanımlanması gerekir. Tanımlama işlemi için öncelikle Rapor Formatları Düzenleme menüsünde ![ref8]  butonu ile raporunun yüklenmesi gerekir. Yüklenen rapor formatı şablonun adı ve uzantısı birlikte ilgili parametreye  sağ tıkla/kopyala-yapıştır yönetimi ile yapıştırılması gerekir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_265.png)

Bu parametreye tanımlanan  DÖF G8D raporu şablonu DÖF Yazdırma ekranında Rapor Tipi “G8D Raporu” seçilirek ![ref66] (Yazdır) butonu tıklanılır **.**

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_267.png)

DÖF Yazdır ekranında G8D Raporu** Excel formatında alınır.

![ref10]: Ekrandaki liste sekmesinde listelenen DÖF kayıtlarının Excel formatında raporunu alınma işlemi yapılır.

![ref17]: Kayıtlar filtrelenerek arama yapılabilir. 

![ref11]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref12]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref13]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranında kullanıcı bazlı tasarlama işlemi yapılır.

**Filtre sekmesi;**

DÖF Modülü kapsamında DÖF işlemleri ekranında DÖF kodu, Durum, Departman/Müşteri/Tedarikçi ve Uygunsuzluğun olduğu Bölüm gibi alanlara göre veri girilip, ![ref67] (Ara) butonu tıklanarak arama kriterlerine göre filtreleme yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_269.png)
##### **6.2.1.1.Yeni DÖF Kaydının Açılması.**
DÖF işlemleri ekranında yeni bir DÖF kaydının tanımlama için  ![ref8]   butonu tıklanarak  DÖF İşlemleri / Yeni Kayıt ekranına açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_270.png)

**DÖF sekmesi;**

DÖF İşlemleri -Yeni Kayıt ekranında DÖF sekmesinde DÖF detay bilgilerin yer aldığı sekmedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_271.png)![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_272.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**DÖF Türü:** DÖF işlemleri ekranında DÖF Türü bilgisinin seçilebildiği alandır. Düzeltici, İyileştirici ve Önleyici olmak üzere 3 tür bulunmaktadır.DÖF türü seçeneklerinde düzeltici, iyileştirme ve Önleyici seçeneklerinde seçim yapıldığı alandır. DÖF Modülü parametrelerinde 22 numaralı “DÖF Takibi (K)ayıt bazında mı, (A)ksiyon bazında mı takip edilecek? (K/A)” parametresi parametre değeri “K” seçilirse DÖF açılırken, DÖF’ün hangi türde ( Düzeltici-İyileştirici-Önleyici) olduğuna bu alanda karar verilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_273.png)

DÖF Modülü parametrelerinde 88 numaralı “DÖF türünde iyileştirme seçeneği kullanılsın mı? (E/H)” parametresi değeri “Evet” seçilerek parametre aktif edilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_274.png)

Parametre aktif edildikten sonra DÖF Türü alanında DÖF türü için Düzeltici veya Önleyici dışında ek olarak İyileştirme seçeneği kullanılmak isteniyorsa parametre değeri "Evet" olarak aktif edilir. Bu  22 ve 88 numaralı  DÖF Modülü parametrelerinde yapılan ayarlamalara göre DÖF Türü alanına DÖF Türü seçenekleri gelmektedir.

**İşlem Kaynağı:** DÖF işlemleri-Yeni Kayıt ekranından İşlem Kaynağı bilgisinin girildiği alandır. Sistem Altyapı Tanımları/DÖF/DÖF İşlem Kaynakları menüsünde tanımlı kaynaklar listesi görüntülenir ve bu işlem kaynakları listesinde seçim yapılır. DÖF İşlem kaynakları tanımlama ekranında seçilen işlem kaynağının İşlem Kaynağı Tipi alanında Şirket içi seçildiği için  alt kısımda Uygunsuzluğun olduğu Bölüm alanı görüntülenir.Bu alanın seçimde İşlem Kaynak Tipi Şirket Dışı seçilseydi sistemde tanımlı Müşteri listesi, Tedarikçi seçilseydi ise sistemden seçili Tedarikçi listesi ek bir alan olarak görüntülenecektir.  Müşteri Şikayeti işlem Kaynağı Tipi Müşteri şikayetleri modüllerinde ve Denetim seçeneğini seçildiği alan ilgili İşlem kaynakları Denetim Faaliyetleri Modülünde DÖF kaydının  açılma aşamasında görüntülenecektir. 

**Uygunsuzluk Olduğu Bölüm:** DÖF İşlemleri-Yeni Kayıt ekranında uygunsuzluk olduğu bölüm bilgisi sistemde tanımlı olan departman listesinden seçilebildiği alandır.

**İş Yeri:** DÖF İşlemleri-Yeni Kayıt ekranında İş yeri bilgisinin sistemde tanımlı olan İş Yeri  listesinden seçilebildiği alandır.

Düzeltici ve Önleyici Faaliyetler modülü parametrelerinde “İş yeri bazında güvenlik uygulansın mı? (E/H)” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. ![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_275.png)

Parametre aktif edildikten sonra DÖF ekranında Modül yöneticisi hariç diğer kişiler sadece kendi iş yerlerindeki DÖF kayıtlarını görebilmeleri sağlanır. Diğer iş yerlerindeki DÖF kayıtları güvenlik getirilerek görünmesi gizlenmiş olur. 

**Uygunsuzluk Tanımı:** DÖF İşlemleri ekranında Uygunsuzluk Tanımı bilgisinin girildiği alandır.

Uygunsuzluk kategorisi seçildiğinde  uygunsuzluk tanım alanın otomatik gelmesi isteniyorsa 130 numaralı “Uygunsuzluk kategorisi seçildiğinde tanım alanına otomatik yazılsın” parametresinin parametre değeri “Evet”seçilerek parametre aktif edilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_276.png)

Parametre aktif edildikten sonra DÖF girişi sırasında seçilen uygunsuzluk kategorisi tanımı, Uygunsuzluk Tanımı alanına otomatik olarak yazılır.

**Uygunsuzluk Detayı:** DÖF İşlemleri ekranında Uygunsuzluk detay bilgisinin girildiği alandır.Ugunsuzluk Detayı ile ilgili Düzeltici ve Önleyici Faaliyetler modülü parametrelerinde 35 numaralı “Uygunsuzluk Kategorisi Detayı zorunlu olsun (E/H)” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_277.png)

Parametre Aktif edildikten sonra DÖF İşlemleri-Yeni Kayıt ekranıdna Uygunsuzluk Kategorisi Detayı alanın bilgi girişinin yapılması zorunlu bırakılır.

**Uygunsuzluk Kategorisi:** DÖF İşlemleri ekranında Uygunsuzluk Kategorisi bilgisinin sistemde tanımlı Uygunsuzluk Kategorisi listesinden seçilebildiği alandır. Sistem Altyapı Tanımları/DÖF/Uygunsuzluk Kategorisi Tanımlama menüsünde tanımlı Uygunsuzluk Kategorisi listesinde seçim yapılır.

DÖF İşlemleri-Yeni Kayıt ekranında Uygunsuzluk Kategorisi alanı parametreye bağlı olarak görüntülenen bir alandır.Düzeltici ve Önleyici Faaliyetler modülü paraemtrelerinde 145 numaralı “Uygunsuzluk Kategorisi kullanılacak mı?” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_278.png)

Parametre aktif edildikten sonra DÖF işlemleri-Yeni Kayıt ekranında Uygunsuzluk Kategorisi alanı görüntülenir.Düzeltici ve Önleyici Faaliyetler modülünde 108 numaralı “Uygunsuzluk Kategorisi bir tane seçilebilsin (çoklu seçimi engelle). (E/H) parametresi “Evet” seçilerek parametre aktif edilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_279.png)

Parametre aktif edildiğinde DÖF işlemleri-Yeni Kayıt ekranında Uygunsuzluk Kategori  alanında Uygunsuzluk Kategorisi listesinde seçim yapıldığında tekli seçim işlemine izin verilir. Parametre değeri “Hayır” seçildiğinde parametre pasif edildiğinde Uygunsuzluk Kategori alanında Uygunsuzluk Kategorisi listesinde çoklu seçim işlemine  izin verilir.Yeni bir DÖF kaydı oluşturulurken uygunsuzluk kategorisi seçilmek istenildiği zaman sadece ana kırılımın altındaki alt kategorilerin seçilmesi isteniliyorsa 161 numaralı “Uygunsuzluk kategorisi sadece en alt kategori seçilsin mi?” parametresinin parametre değeri “Evet” seçilmelidir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_280.png)

**Bilgilendirme:**DÖF İşlemleri ekranında DÖF kaydının ilgili  bilgilendirme yapılacak kişinin bilgisinin sistemde tanımlı personel listesinden seçilebildiği alandır.DÖF işlemlerinde bilgilendirme ile ilgili parametrelerde gerekli ayarlama yapılarak bilgilendirme alanına otomatik olarak kişi veya varsayılan kullanıcı grubu bazında ekleme işlemi yapılır. DÖF  kaydının açanın departman sorumlusu, bir üst amiri, ekip liderinin departman sorumlusu, Ekip Liderinin bir üst amiri, işyeri seçildiğinde sorumlusu,süreç seçildiğinde süreç sahibinin, ürün seçildiğinde ürün grup sorumlusunun, uygunsuzluğun olduğu bölümün üst amiri ve açanın bilgilendirme alanı eklenmesi için ilgili parametrelerde ayarlamalar yapılması gerekmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_281.png)

Düzeltici ve Önleyici Faaliyetler Modülü parametrelerinde 10 numaralı “Varsayılan bilgilendirme için kullanıcı grubu kodu”  parametresine parametre değerine Kullanıcı Grubu kodu tanımlanır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_282.png)Tanımlanan Kullanıcı Grubundaki kişiler bilgilendirme alanına varsayılan olarak gelir.Tanımlanan Kullanıcı Grubu kod bilgisi Sistem Altyapı Tanımları/BSAT/Tanımlar/Kullanıcı Grubu Tanımlama menüsünde alınır. 

**Süreç:** DÖF İşlemleri ekranında Süreç bilgisinin sistemde tanımlı olan Süreç  listesinden seçilebildiği alandır.

**Yönetim Sistemi:** DÖF İşlemleri ekranında DÖF kaydının sistemde tanımlı Yönetim Sistemi ile bağlantısının seçilebildiği alandır. Düzeltici ve Önleyici Faaliyetler modülü parametrelerinden 149 numaralı “Döf işlemlerinde yönetim sisteminin çoklu seçilsin mi?” parametresi parametre değeri “Evet” seçilerek parametre aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_283.png)

Parametre aktif edildikten sonra DÖF İşlemleri- Yeni Kayıt ekranında Yönetim Sistemi alanında ![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_284.png) butonu tıklanarak açılan sistemde tanımlı Yönetim Sistemi listesinde çoklu seçim işlemi yapılır.

**Std. Madde No:** DÖF İşlemleri ekranında DÖF kaydının  Madde No bilgisinin sistemde tanımlı Madde No Listesinden seçilebildiği alandır.

Burada düzeltici,  iyileştirici ve önleyici  olma durumuna göre DÖF Türü seçilir. Daha sonra işlem kaynağı, uygunsuzluğun olduğu bölüm, işyeri, uygunsuzluk tanımı, uygunsuzluk detayı ve uygunsuzluk kategorisi belirlenir. İstenirse bilgilendirmeye eklenecek personeller, işyeri, süreç ve madde no seçildikten sonra yönetim sistemleri açılır menüsünden ilgili yönetim sistemi listeden seçilir. 

Seçim tipli alanlara göre aynı seçimlerde son 1 ayda, son 1 yılda ve toplamda kaç DÖF açılmış sayısı görebilirsiniz. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_285.png)

Sayının gösterildiği mavi alana tıklamanız durumunda bu kayıtların içeriğini görüntüleyebilirsiniz.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_286.png)

DÖF işlemleri ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_287.png) butonu tıklanarak DÖF kaydı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_288.png)

DÖF Görüntüleme ekranında ![ref68] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_290.png)

DÖF kaydı ile ilgili  link ekranda görüntülenir. Sağ tıkla/kopyala -yapıştır yöntemleri yada kopyala- Yapıştır kısayol tuşları (Ctrl+C-Ctrl+V) ile DÖF Kaydının görüntülenip , ilgili kişilere paylaşımı yapılır

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_291.png)

**Detay Bilgiler Sekmesi;**

DÖF Modülü için önceden parametrik alan tipleri tanımlanmış ise Detay Bilgiler sekmesinde görüntülenir. DÖF modülü içi parametrik alan tipleri tanımlanmamışsa bu sekme görüntülenmez. DÖF Modülü ile ilgili metin, metin(çoklu satır), liste, tarih, sorgu  gibi parametrik alan tipleri tanımlama işlemi Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Dil Ayarları menüsünde yapılır.Açılan Dil Ayarları menüsünde Modüller alanında Düzeltici ve Önleyici Faaliyetler modülü seçilir. Düzeltici Faaliyetler ve Önleyici Modülü ilgili tanımlanacak pasif parametrik alanlar görüntülenir ve listede seçilir. Pasif parametrik alanlar listede seçili iken![ref36]  butonu tıklanarak açılan Dil Ayarları ekranında Değeri alanında parametrik alanın tanım bilgisi yazılarak ekranın sol kösesindeki ![ref7]  butonu tıklanarak parametrik alan tanımlama işlemi yapılır.

**Çözüm Ekibi Sekmesi;**

Açılan uygunsuzluğun ortadan kaldırılması için acil önlemleri alacak, Kök neden analizi yapacak, kök nedenleri ortadan kaldıracak Aksiyonların planlanması yapılacak ve uygunsuzluğu çözüme ulaştıracak Ekip lideri ve Ekibin tanımlama işlemin yapıldığı sekmedir. Eğer oluşturulmamışsa Çözüm Ekibi sekmesi tıklanarak DÖF çözüm ekibi tanımlanır. DÖF çözüm ekibi ekranında çözüm ekibi lideri ve sorumlu departman seçilir. Ekip üyeleri, personel listesinden seçilir. Ayrıca Gelişme Raporu’nun yazılacağı son tarih belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_292.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Ekip Lideri:** Çözüm Ekibi sekmesinde ekip lideri bilgisi ![ref69] butonu tıklanarak açılan sistemde tanımlı olan personel listesinden seçilebildiği alandır. Düzeltici ve Önleyici Faaliyetler modülü parametrelerinde 8 numaralı “Varsayılan ekip lideri rol id” parametresine rol kodu tanımlanır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_294.png)

Rol  kodu Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Rol Tanımlama menüsünde tanımlanan rolün kodunun yazıldığı parametredir.İşletme bünyesinde DÖF işlemlerinde ekip lideri bir role bağlı olarak seçilmesi sağlanır. Sistem Ekip lideri alanında parametrede tanımlı roldeki kişiyi otomatik olarak ilgili alana getirir.

Eğer herhangi bir DÖF işleminde ürün ile ilişki kurulduğunda bu ürün grubu sorumlusunun direkt ekip lideri olarak atanması istenirse  Düzeltici ve Önleyici Faaliyetler Modülü parametrelerinde 104 numaralı  “Ürün seçildiğinde ürün grubu sorumlusu ekip lideri olarak atansın mı?(E/H)” parametresinin parametre değeri “Evet”seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_295.png)

DÖF kaydını açan personelin bağlı olduğu departman sorumlusunun ekip lideri olarak atanması isteniyorsa Düzeltici ve Önleyici Faaliyetler modülü parametrelerinde 135 numaralı “Açanın departman sorumlusu ekip lideri olarak atansın” parametresinin parametre değeri “Evet” seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_296.png)

DÖF kaydı açılırken ilgili süreç seçildiği zaman süreç sorumlusunun ekip lideri olarak atanması isteniyorsa  Düzeltici ve Önleyici Faaliyetler modülü parametrelerinde 142 numaralı “Süreç seçildiğinde süreç sorumlusu ekip lideri olarak atansın mı?(E/H)” parametresinin parametre değeri "Evet" seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_297.png)

Bu parametreler gibi Düzeltici ve Önleyici Faaliyetler modülü parametrelerinde Ekip lideri ilgili parametrelerde gerekli ayarlamalar yapılır.

**Sorumlu Departman:** Çözüm Ekibi sekmesinde sorumlu Departman bilgisi ![ref69] butonu tıklanarak açılan sistemde tanımlı olan departman listesinde seçilebildiği alandır.

**Gelişme Raporu Tarihi(Planlanan):** Çözüm Ekibi sekmesinde gelişme Raporu Tarihi(Planlanan) bilgisinin açılan Takvim alanında seçilebildiği alandır.

**Bilgilendirme:** Çözüm Ekibi sekmesinde bilgilendirme bilgisinin sistemde tanımlı personel ve kullanıcı grubu listesinden seçilebildiği alandır.

**Ek Dosyalar ;**

Ek Dosyalar sekmesine geçilerek istenirse DÖF kaydına doküman, ses, görüntü vb. formatlarda istenen dosyaların eklenmesi gerçekleştirilebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_298.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref70]: Ek dosya sisteme yüklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_300.png):Yüklenen ek dosya bilgisi görüntülenir.

![ref9]: Yüklenen ek dosya bilgisi silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_301.png): Yüklü olan Ek dosya listesinin Excel formatında raporu alınır.

![ref70]  butonu tıklanarak DÖF kaydına ek dosya eklenir. Birden çok ek dosya eklenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_302.png)

Dosya Ekle ekranında Gözat butonu tıklanarak bilgisayardaki dosya seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_303.png)

Dosya Ekle ekranında Yükle butonu tıklanarak sisteme dosyanın yükleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_304.png)

DÖF işlemleri-Yeni Kayıt ekranında gerekli alanlar ilgili bilgiler girildikten sonra ekranın sol üst köşesesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_305.png) butonu tıklanarak DÖF kayıt işlemi yapılır. Eğer DÖF açma onayı için bir akış kurgulandıysa ilgili rolün onayına kurgulanmadıysa Ekip Liderine Gelişme Raporu yazılması için görev düşer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_306.png)  butonu tıklanarak DÖF kaydı taslak olarak kaydedilir.Bu butonun görüntülenmesi için 125 numaralı “Taslak kaydetme kullanılacak mı?” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_307.png)

Parametre aktif edildiğinde DÖF İşlemleri-Yeni Kayıt ekranında “Taslağa Kaydet” butonu görüntülenir ve bu buton tıklanarak DÖF kaydını taslak olarak kaydedilir. DÖF kaydı henüz hazırlama işlemi tamamlanmışsa taslak olarak kaydedilerek üzerinde işlem yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_308.png)

DÖF işlemleri modülünde Bekleyen İşlerimde taslak olarak kaydedilen DÖF kayıtları “Taslak DÖF’ler Listesi” işi olarak görev düşer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_309.png)
##### **6.2.2.2.Taslak DÖFler Listesi**
Taslak olarak kaydedilen DÖF kaydının Bekleyen İşlerim ekranında “Taslak DÖFler Listesi” görevindeki DÖF No alanında DÖF Kodu linki tıklanılır.Açılan  DÖF İşlemleri - Kayıt Güncelle ekranında taslak aşamasında DÖF kaydı ile istenirse ilgili alanlar üzerinde düzenleme, değişiklik ve güncelleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_310.png)

**Ekranda bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_311.png): DÖF İşlemleri- Kayıt Güncelleme ekranında ilgili alanlarla bilgiler girilerek taslak olarak kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_312.png):DÖF  kaydının iptal edilme işlemi yapılır.

![ref71]:DÖF kaydının kayıt işlemi yapılır. 

DÖF İşlemleri- Kayıt Güncelleme ekranında gerekli alanlar ilgili düzenleme ve güncelleme işlemi yapıldıktan sonra ![ref71] butonu tıklanarak bu aşamada da DÖF kaydında  DÖF açma onayı için bir akış kurgulandıysa ilgili rolün onayına kurgulanmadıysa Ekip Liderine Gelişme Raporu yazılması için görev düşer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_314.png)

Onaydaki kişiye sistem mail yollarken aynı zamanda bekleyen işlerine “**Onay Bekleyen DÖF listesi**” şeklinde görüntülenir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_315.png)
##### **6.2.1.3.DÖF Onaylama**
DÖF açma onayına gönderildikten sonra ilgili kişi, Bekleyen İşleri’ne gelerek “Onay Bekleyen DÖF’ ler Listesi” adı altında açma onayı vereceği DÖF’ü görür. DÖF no’sunun alanındaki DÖF kodu linki  tıklanarak  “Onay Bekleyen DÖF’ler” listesini görüntüler.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_316.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref72]: İlgili DÖF kaydının görüntüleme işlemi yapılır.

![ref73] : İlgili DÖF kaydı ile değişik yapması istenirse kullanılır. Eğer talepten açılan DÖF ise zorunlu alanları doldurmadan onaylama işlemi yapmamıza sistem izin vermeyecektir.

![ref74] : DÖF onaylama işlemini yapmak için kullanılır. Onay işleminden sonra ilgili DÖF kaydı Ekip liderinin önüne düşer.

![ref75] : DÖF’ te girilen bilgiler uygun olmadığı durumda, DÖF’ ü reddetmek için kullanılır. 

![ref76]  : Çok fazla onaylanması gereken DÖF olması durumunda filtre seçeneğinden bilgiler süzülerek arama yapmak istendiğinde kullanılır.

![ref11]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref12]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref13]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranında kullanıcı bazlı tasarlama işlemi yapılır.

Onay Bekleyen DÖF’ler ekranında ![ref72] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_322.png)

Açılan Görüntüleme ekranında DÖF kaydı ile ilgili sekmeler tıklanarak Detay bilgileri görüntülenir. DÖF kaydının görüntüleme ekranında ![ref68] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_323.png)

DÖF Kaydı ile ilgili  link ekranda görüntülenir. Sağ tıkla/kopyala -yapıştır yöntemleri yada kopyala- Yapıştır kısayol tuşları (Ctrl+C-Ctrl+V) ile DÖF Kaydının görüntülenip , ilgili kişilere paylaşımı yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_324.png)

Onay Bekleyen DÖF’ler ekranında ![ref73] butonu tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_325.png)

Açılan DÖF İşlemleri-Kayıt Güncelleme ekranında görüntülenen sekmelerde ilgili alanlar üzerinde düzenleme ve değişiklik yapma işlemi yapılma işlemi yapılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_326.png)

DÖF İşlemleri-Kayıt Güncelleme ekranında yapılan değişikliklerin kaydedilmesi için ekranın sol üst köşesindeki ![ref71]  butonu tıklanılır. 

Onay Bekleyen DÖF’ler ekranında ![ref77]  butonu tıklanarak Ret nedeni girilerek DÖF kaydı ret edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_328.png)

Açılan DÖF Ret ekranında DÖF bilgileri kontrol edilerek uygun olmadığı görüldüğünde DÖF Ret etme işlemi yapılır ve  Ret Nedeni bilgisi yazılması zorunludur. Red edilen açan kişiye ret etme nedeniyle birlikte gönderilebilir. Ret ederken detay bilgi için ret veya kaydın iptali için ret edilebilir, buna bağlı olarak ilgili seçeneği seçmelidir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_329.png)

Onay Bekleyen DÖF’ler ekranında ![ref74]  butonu tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_330.png)

Açılan DÖF Onay ekranında  Onay notu alanında Onay notu bilgisi yazılarak ![ref78] butonu tıklanarak DÖF kaydı onaylanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_332.png)

DÖF onaylarken onay notu bilgisi Düzeltici ve Önleyici Faaliyetler modülü parametrelerinde 154 numaralı “DÖF onaylarken onay notu girilsin?” parametresinde parametre değeri “Evet” seçilerek parametre aktif edilir. 

![ref79]


Parametre aktif edildikten sonra DÖF Onay ekranlarında Onay Notu alanı görüntülenir ve onay notu bilgisi girilerek DÖF onaylama işlemi yapılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_334.png)

DÖF onaylama işlemi gerçekleşen DÖF kaydı  eğer DÖF Gelişme Raporu  onayı için bir akış kurgulandıysa ilgili rolün onayına kurgulanmadıysa Ekip Liderine Gelişme Raporu yazılması için görev düşer.
##### **6.2.1.4.** **Gelişme Raporu Onayı**
DÖF Kaydı için DÖF Gelişme Raporu onayı için akış kurgulandığı için onaydaki kişiye sistem mail yollarken aynı zamanda bekleyen işlerine “**Gelişme Raporu Onayı Bekleyen DÖFler Listesi**” işi olarak görev düşürür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_335.png)

DÖF gelişme raporu  onayına gönderildikten sonra ilgili kişi, Bekleyen İşleri’ne gelerek “Gelişme Raporu Onayı Bekleyen DÖFler Listesi” adı altında Gelişme Raporu onayı vereceği DÖF’ü görür. DÖF no’sunun alanındaki DÖF kodu linki  tıklanarak  “Onay Bekleyen DÖF’ler” listesini görüntüler.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_336.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref80]: İlgili DÖF kaydının görüntüleme işlemi yapılır.

![ref81] : DÖF onaylama işlemini yapmak için kullanılır. Onay işleminden sonra ilgili DÖF kaydı Ekip Liderinin önüne düşer.

![ref82] : DÖF’ te girilen bilgiler uygun olmadığı durumda, DÖF’ ü reddetmek için kullanılır. 

![ref83]  : Çok fazla onaylanması gereken DÖF olması durumunda filtre seçeneğinden bilgiler süzülerek arama yapmak istendiğinde kullanılır.

![ref48]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref49]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref50]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranında kullanıcı bazlı tasarlama işlemi yapılır.

Onay Bekleyen DÖF’ler ekranında ![ref72] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_341.png)

Açılan Görüntüleme ekranında DÖF kaydı ile ilgili sekmeler tıklanarak Detay bilgileri görüntülenir. DÖF kaydının görüntüleme ekranında ![ref68] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_342.png)

DÖF kaydı ile ilgili  link ekranda görüntülenir. Sağ tıkla/kopyala -yapıştır yöntemleri yada kopyala- Yapıştır kısayol tuşları (Ctrl+C-Ctrl+V) ile DÖF Kaydının görüntülenip , ilgili kişilere paylaşımı yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_343.png)

Onay Bekleyen DÖF’ler ekranında ![ref84]  butonu tıklanarak Ret nedeni girilerek DÖF kaydı ret edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_345.png)

Açılan DÖF Ret ekranında DÖF bilgileri kontrol edilerek uygun olmadığı görüldüğünde  DÖF Ret etme işlemi yapılır ve  Ret Nedeni bilgisi yazılması zorunludur. Red edilen açan kişiye ret etme nedeniyle birlikte gönderilebilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_346.png)

Onay Bekleyen DÖF’ler ekranında ![ref81]  butonu tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_347.png)

Açılan DÖF Onay ekranında  Onay notu alanında Onay notu bilgisi yazılarak ![ref78] butonu tıklanarak DÖF kaydı onaylanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_348.png)

DÖF onaylarken onay notu bilgisi Düzeltici ve Önleyici Faaliyetler modülü parametrelerinde 154 numaralı “DÖF onaylarken onay notu girilsin?” parametresinde parametre değeri “Evet” seçilerek parametre aktif edildiği için görüntülenip, onay notunun girilmesi zorunlu bırakılmıştır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_349.png)

DÖF Gelişme Raporu  onayı  işlemi yapıldıktan sonra DÖF kaydı Ekip Liderine Gelişme Raporu yazılması için görev düşer. 
##### **6.2.1.5.Gelişme Raporu**
Gelişme Rapor onayının onaylama işleminden sonra gelişme raporu yazmak üzere Ekip liderinin bekleyen işlerine düşer. Ekip üyeleri/ ekip lideri, Bekleyen İşleri’ne “**Gelişme Raporu Yazılacak DÖF’ler Listesi”** işi olarak görev düşer. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_350.png)

İlgili DÖF No alanındak DÖF Kodu linki tıklayarak DÖF bilgilerinin olduğu ekrana gelinir.

![ref85]
 Gelişme raporu sekmesinde uygunsuzlukla ilgili acil önlemlerin alındığı sekmedir. Ekip Lideri veya Ekipteki herhangi kişi tarafından gelişme raporu yazılır. Uygunsuzluk fark edilirken ilk olarak yapılacak acil önlemleri işlem adımları bu rapora yazılır. İsternirse bu sekmede Ekipe yeni kişilerde eklenir. DÖF parametrelerinde 78 numaralı “Gelişme Raporu kullanılacak mı? (E/H)” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_352.png)

Parametre aktif edildikten sonra DÖF İşlemleri-Kayıt güncelleme ekranında Gelişme Raporu sekmesini görüntülenir ve DÖF kaydınında Gelişme raporu aşaması kullanılır.

Bu sekmede uygunsuzluğun çözümü için Aksiyonlara ihtiyaç olup olmadığıda belirlenir. Parametreye bağlı olarak bu alan gelmektedir.DÖF modülü parametrelerinde 42 numaralı “Gelişme raporunda aksiyon yazmadan DÖF sonuçlandırılabilsin mi?” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_353.png)

Parametre aktif edildikten sonra “Aksiyona ihtiyaç Var mı? alanı gelişme raporu sekmesinde görüntülenir. Parametre değeri “Hayır” seçilerek parametre pasif edildiğinde Gelişme Raporu sekmesinde bu alan görüntülenmez.

![ref85]

**Açılan ekranda ilgili alanlar tanımlanır:**

**Aksiyon İhtiyaç Var mı? :** DÖF İşlemleri- Kayıt Güncelleme ekranında Gelişme Raporu sekmesinde “Aksiyon İhtiyaç Var Mı?” alanı ilgili  DÖF kaydı için Aksiyon ihtiyaç olup, olmamasının bilgisinin “Evet” ya da “Hayır” seçeneği seçilebilmesi ile belirlendiği alandır. DÖF kaydında   Aksiyon ihtiyaç olması için “Evet” seçeneği seçilir.

**Gelişme Raporu:** DÖF İşlemleri- Kayıt Güncelleme ekranında Gelişme Raporu sekmesinde Gelişme Raporu açıklama bilgisinin girildiği alandır.

**Sonuç Raporu Tarihi(P):** DÖF İşlemleri- Kayıt Güncelleme ekranında Gelişme Raporu sekmesinde planlanan sonuç raporu tarihinin belirlendiği alandır.

Düzeltici ve Önleyici Modülü parametrelerinde 5 numaralı “Sonuç Raporu Hazırlama Süresi” parametresine girilen değere göre  ne kadar sürede hazılırlanması bilgisi tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_354.png)

**Ekip:** DÖF İşlemleri- Kayıt Güncelleme ekranında Gelişme Raporu sekmesinde Ekibi oluşturan  kişilerin bilgisinin görüntülendiği alandır.

**Ek Dosyalar:** Gelişme Raporu sekmesinde bu aşamada varsa bu gelişme raporu ile ilgili  kanıt doküman, fotoğraf gibi ek dosya yükleme işlemi butonlar yardımıyla  yapılır. Gelişme raporu aşamasında ek dosya yüklenmesi zorunluğu gerekli ayarlamalar yapılarak getirilir.Gelişme raporu aşamasında ek dosya yükleme işlemi zorunlu getirilmesi işlemi için Düzeltici ve Önleyici Faaliyetler modülü parametrelerinde 215 numaralı “Gelişme raporunda ek dosya zorunlu olsun” parametresinin parametre değeri “Evet”seçilerek parametre aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_355.png)

Parametre aktif edildiğinde Gelişme raporu aşamasında Ek Dosya yükleme işlemi yapılmadan gelişme raporu kayıt  işlemi gerçekleşmez. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_356.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref86]: Ek dosya sisteme yüklenir.

![ref87]: Yüklenen ek dosya bilgisi görüntülenir.

![ref3]: Yüklenen ek dosya bilgisi silinir.

![ref86]  butonu tıklanarak  gelişme raporu aşamasında DÖF kaydınana ek dosya eklenir. Birden çok ek dosya eklenebilir.

DÖF Modülü parametrelerinde 32 numaralı “Yorum modülü aktif (E/H)” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_359.png)

Parametre aktif edildikten sonra DÖF İşlemleri -Kayıt Güncelleme ekranında Yorumlar sekmesi görüntülenir. DÖF İşlemleri- Kayıt Güncelleme ekranında görüntülenen bu sekmede kullanıcı isterse her aşamada  ilgili  yorum  ekleme,eklenen yorumları düzenleme,güncelleme,değiştirme ve silme işlemleri ilgili butonlar ile yapar. Ayrıca eklenen yorumların listesinde excel formatında raporunu bu aşamada alır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_360.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref8]: Yeni bir yorum tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_361.png): Listede seçili olan yorum bilgisi üzerinde düzenleme/değişiklik/güncelleme işlemi yapılır.

![ref9]: Listede seçili olan yorum bilgisi silinir. 

![ref10]: Veriler Excel’ e aktarılır.( Yorumlar ekranında liste sekmesinde bulunan Yorum listesinin Excel formatında raporu alınır.)

![ref11]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref12]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref13]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Yorumlar ekranına yeni bir yorum eklemek için ekranın sol üst köşesindeki ![ref8]  butonu tıklanarak Yorumlar-Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_362.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Yorum:** Yorumlar-Yeni Kayıt ekranında yapılan yorum bilgisinin girildiği alandır.

**Ek Dosyalar:** Yorumlar sekmesinde bu aşamada yorumla ilgili varsa kanıt doküman, fotoğraf gibi ek dosya yükleme işlemi butonlar yardımıyla  yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_363.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref88]: Ek dosya sisteme yüklenir.

![ref87]: Yüklenen ek dosya bilgisi görüntülenir.

![ref9]: Yüklenen ek dosya bilgisi silinir.

![ref88]  butonu tıklanarak tanımlanan yorumu istenirse ek dosya eklenir. Birden çok ek dosya eklenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_365.png)

Yorumlar- Yeni Kayıt ekranında gerekli alanlar doldurulduktan sonra sol üst köşede yer alan  ![ref7]   butonuna tıklanarak yorum  tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_366.png)Gelişme raporu aşamasında Yorum ekleme işlemi yapıldıktan sonra Ekip lideri Acil aldığı önlemlerle  ilgili gelişme raporu yazar. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_367.png)

DÖF Sonuçlandırma süresini, Ekibini varsa ek dosyasını ekleyerek![ref7]  butonunu tıklar ise bir sonraki aşamaya geçilir.  Aksiyona ihtiyaç durumu parametrik bir alandır. Aksiyon almadan kapatılan DÖF’ler varsa kullanılır. Gerekli alanlar ilgili bilgiler girildikten sonra ekranın sol üst köşedeki  ![ref7]  butonuyla tıklanarak Gelişme raporu kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_368.png)

Gelişme raporu aşamasında sonra Ekip Liderine ve Ekipe DÖF kaydı için Kök Neden Analizi/Aksiyon Planlama işlemin  yapılması için görev düşer.
##### **6.2.1.6.Kök Nedenler**
Gelişme Raporu aşamasından sonra Kök Neden Analizi ve Aksiyonların planlama işlemi için,  DÖF Kaydı  Ekip/ Ekip Liderinin Bekleyen İşlerinde **“Kök Neden Analizi Yapılacak / Aksiyon Planlanacak DÖFler Listesi**” işi olarak görev düşer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_369.png)

İlgili DÖF No alanındak DÖF Kodu linki tıklayarak DÖF bilgilerinin olduğu ekrana gelinir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_370.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref8]:Yeni bir Kök Neden ekleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_371.png):Listede seçili Kök Neden bilgisi üzerinde değişiklik/düzenleme/güncelleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_372.png):Listede seçili Kök Neden bilgisi silinir.

![ref89]:Kök Neden Analizine Kullanılacak Şablonlar doküman kodları görüntülenir ve kök neden analizindeki kullanılacak şablon dokümanları tıklanarak bilgisayara indirilme işlemi yapılır. Parametreye bağlı görüntülenen bir alandır.DÖF parametrelerinde 89 numaralı “Kök Neden Analizinde kullanılacak şablon doküman kodları(Birden fazla ise "," ile ayırınız) parametresinde parametre değerine Doküman Yönetimi Modülünde yüklü olan şablon dokümanları kodları yazılarak parametreye tanımlanılır. Şablon doküman kodları Entegre Yönetim Sistemi/Doküman Yönetimi/Doküman Görme menüsünden alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_374.png)![ref89] butonu tıklanıldığında parametreye tanımlı şablon doküman kodlar görüntülenir ve görüntülenen şablon doküman kodları tıklanarak bilgisayara indirilir. İndirilen Kök Neden Analizinde Kullanılacak Şablonlar ![ref90] butonu tıklanarak Kök Nedenler sekmesinde istenirse sisteme yükleme işlemi yapılır.

![ref90]:Kök Neden Analiz Raporu yükleme işlemi yapılır.Parametreye bağlı olarak Kök Neden Analiz Raporu yükleme işlemi zorunlu bırakılır. Düzeltici ve Önleyici Faaliyetler modülü parametrelerinde 25 numaralı “Kök neden analiz dosyası zorunlu olsun” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_376.png)

Parametre aktif edildiğinde Kök Nedenler sekmesinde Kök neden tanımlama işlemi yapılmadan önce “Kök neden eklemeden önce kök neden analiz raporunu yüklemelisiniz” sistem tarafından uyarı mesajı verilerek Kök Neden Analizi raporu yükleme işlemi zorunluluğunu getirilir.

Gelişme raporu yazıldıktan sonra, Kök Nedenler sekmesi aktif olur. Kök Neden Analizi ekranına gelinir. Uygunsuzluğun hangi kök nedenden dolayı kaynaklandığının belirlendiği ve kök neden analizi yapıldığı sekmedir.  Ekip ve Ekip liderin bulunduğu çözüm ekibi tarafından Uygunsuzluğun çözüme ulaştırmada öncelikle kök nedenlerin bilinip ve bu kök nedenleri ortadan kaldıracak kalıcı çözümlerin alınması belirlenir.DÖF parametrelerinde 146 numaralı “Kök Neden Kullanılacak mı?” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_377.png)

Parametre aktif edildikten sonra DÖF İşlemleri-Kayıt güncelleme ekranında Kök Nedenler sekmesini görüntülenir ve DÖF kaydınında Kök Nedenler aşaması  kullanılır.

Düzeltici ve Önleyici Faaliyetler Modülü parametrelerinde 36 numaralı “Kök Neden girişi zorunlu olsun mu?” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_378.png)

Parametre aktif edildikten sonra DÖF işlemleri ekranında aksiyon planlamadan önce kök neden girişinin zorunlu olması sağlanır. Eğer böyle bir zorunluluk istenmiyorsa parametre değeri "Hayır" seçilerek parametre pasif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_379.png)

Düzeltici ve Önleyici Faaliyetler modülü parametrelerinden 25 numaralı  ““Kök neden analiz dosyası zorunlu olsun” parametresi aktif olduğunda ![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_380.png) butonu tıklanarak Yeni bir Kök Neden tanımlama işlemi yapıldığından sistem “Kök neden eklemeden önce kök neden analiz raporunu yüklemelisiniz” uyarı mesajı verir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_381.png)

Kök Neden Analizinde Kullanılacak şablonlardan yada kullanıcının bilgisayarında sisteme şablon yükleme işlem yapılması zorunlu kılar.

DÖF İşlemleri-Kayıt Güncelleme ekranında Kök Neden Analizi sekmesinde![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_382.png) butonu tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_383.png)

Sistem Düzeltici ve Önleyici Modülü parametrelerinde 89 numaralı parametrede tanımlı Kök Neden Analizinde kullanılacak Şablon görüntülenerek tıklanarak bilgisayara indirilir.


![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_384.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_385.png) butonu tıklanarak Kök neden analizi raporunun sisteme yükleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_386.png)

Dosya Seç ekranında Gözat butonu tıklanarak bilgisayardaki indirilenen Kök Neden Analizi Dosyası seçilerek yükleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_387.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_388.png)

DÖF işlemleri-Yeni Kayıt ekranında Kök Neden Analizi sekmesinde yeni bir Kök neden tanımlamak için  ![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_389.png) butonu tıklanarak Kök neden Analizi  ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_390.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Kök Neden:** Kök Nedenler Analizi ekranında Kök Neden bilgisinin seçilebildiği alandır. Sistem Altyapı Tanımları/DÖF/DÖF Kök Neden Tanımlama ekranında tanımlı Kök Neden Listesinde seçim yapılır.

**Açıklama:** Kök Nedenler Anlizi ekranında Kök Nedenin Açıklama bilgisinin girildiği alandır.

**Neden Ekle**:Kök Nedenler Analizi ekranında neden ekleme işleminin yapıldığı alandır. DÖF işlemlerinde kök neden tanımlama sekmesinde detaylı olarak (neden-neden) kök neden analizi yapılmak isteniliyorsa bu alan kullanılır. Parametreye bağlı olarak görüntülenen alandır.Düzeltici ve Önleyici Faaliyetler modülü parametrelerinde 155 numaralı “Detaylı Kök neden analizi yapılacak mı?” parametre değeri “Evet”seçilerek parametre aktif edilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_391.png)

Parametre aktif edildikten sonra Neden Ekle alanı görüntülenir ve (neden-neden) Kök neden analizi yapılır.Düzeltici ve Önleyici Faaliyetler modülü parametrelerinde 192 numaralı “Detaylı kök neden analizi minimum seviye” parametresinin parametre değerine girilen değere göre detaylı Kök neden analizin minimum seviyesi belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_392.png)

Kök Neden  Analizi ekranında gerekli alanlar doldurulduktan sonra sol üst köşede yer alan  ![ref16]  butonu tıklanarak kök neden analizi kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_393.png)

Parametrede minimum seviye 2 olarak tanımlı ise Kök neden analizi seviyesi minimum seviyesinin altında sistem “Lütfen minimum 2 Detaylı kök neden analizi giriniz.”
uyarı mesajı verir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_394.png)

Kök Neden Analizi ekranında minimum detaylı kök neden analizi bilgisi girilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_395.png)

Açılan ekranda daha önceden tanımlanan kök nedenlerden seçilir, açıklama bilgisi girilir. Detaylı neden analizi yapılır. Daha sonra ![ref16]  butonu tıklanarak kök neden kaydedilerek DÖF kaydı hangi kök nedenlerde  ortaya çıktığı belirlenerek  ilişkisi kurulmuş olur. Birden fazla kök neden seçimi ile çoklu seçim yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_396.png)

Düzeltici ve Önleyici Faaliyetler Modülünde 151 numaralı “Sadece ekip lideri kök neden analizi yapabilsin” parametre değeri “Evet” seçilerek parametre aktif edilir. 

Parametre aktif edildikten sonra sadece Ekip lideri Kök neden analizi yapması zorunluğu sistemde getirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_397.png)

**Önemli Not:** Ekranda 2 adet kaydet düğmesi görülüyor. Alttaki kaydet butonu kök nedeni kaydetmektedir. Üsteki kaydet tıklanır ise kök neden kaydedilmeden bu aşamaya kadar yapılan işlemleri DÖF kaydı olarak kaydedilmiş olur.
##### **6.2.1.*7*.Aksiyonlar**
Çözüm ekibinde bulanan Ekip Lideri ve Ekipteki kişiler Kök nedenler belirlendikten sonra süreç, bu kök nedenleri ortadan kaldıracak Aksiyonların planlama işleminin yapılmasıdır.  Kök nedenlerin ortadan kaldıracak Aksiyonların planlama işleminin yapıldığı sekmedir. Çözüm ekibindeki kişiler Ekip Lideri ve Ekip bu sekmede Aksiyon planlaması yapar. DÖF Aksiyonlarının planlanması ile devam eder. Aksiyonlar sekmesine gelinir. Burada DÖF ile ilgili oluşturulacak kök nedenleri ortadan kaldıracak  aksiyonlar planlanır ve iş olarak atanır.  Aksiyon planlaması yapılarken Aksiyonun ne olacağı, Aksiyonu  yapacak kişi ve sorumlu kişinin atama işlemide yapılır.Bu aşamada yapılan Aksiyonlar Aksiyon Modülü kapsamı dışında Aksiyonlardır.

Düzeltici ve Önleyici Faaliyetler modülü parametrelerinde “Aksiyon Kullanılacak mı?” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_398.png)

Parametre aktif edildikten sonra DÖF işlemleri-Kayıt güncelleme ekranında Aksiyonlar sekmesi görüntülenir ve DÖF kaydı ile ilgili Aksiyon planlaması işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_399.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref91] : Yeni bir aksiyon ekleme işlemi yapılır.

![ref92] :Listede seçili Aksiyon bilgisinin içeriği görüntülenir.

![ref93]:Listede seçili Aksiyon bilgisi üzerinde değişiklik/düzenleme/güncelleme işlemi yapılır.

![ref94] Listede seçili Aksiyon bilgisi kopyalama işlemi yapılır.

![ref95]:Listede seçili Aksiyonun gerçekleştirilmesi işlemi yapılır.

![ref96] :Listede seçili planlanan aksiyonun termin süresini geciktirme işlemi yapılır.Parametreye bağlı olarak görüntülenen butondur.Düzeltici ve Önleyici Faaliyetler modülü parametrelerinden 23 numaralı “Aksiyon geciktirilebilsin mi?(E/H)” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilmelidir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_406.png)

Parametre aktif edildikten sonra DÖF İşlemleri- Kayıt Güncelleme ekranında Aksiyonlar sekmesinde ![ref96] butonu görüntülenir ve  bu buton tıklanarak Aksiyon geciktirme işlemi  yapılır.

![ref10]: Veriler Excel’ e aktarılır.( Aksiyonlar ekranında listede  bulunan Aksiyon listesinin Excel formatında raporu alınır.)

![ref11]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref12]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref13]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranında kullanıcı bazlı tasarlama işlemi yapılır.

DÖF İşlemleri- Kayıt Güncelleme ekranında Aksiyonlar sekmesinde yeni bir Aksiyon  eklemek için ekranın sol üst köşesindeki ![ref8]  butonuna tıklanarak Aksiyon Tanımlama / Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_407.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Sorumlu Kişi:** Aksiyonlar-Yeni Kayıt ekranında aksiyonun sorumlu kişi bilgisi ![ref97] butonu tıklanarak açılan  sistemde tanımlı Personel listesinde seçilebildiği alandır.

**İşi Yapacak Kişi:** Aksiyonlar-Yeni Kayıt ekranında Aksiyonun işi yapacak kişi bilgisinin ![ref97] butonu tıklanarak açılan sistemde tanımlı olan Personel listesinden seçilebildiği alandır.

**Aksiyon:** Aksiyonlar Sekmesinde Aksiyon bilgisinin girildiği alandır.

**Planlanan Bitiş Tarihi:** Aksiyonlar-Yeni Kayıt ekranında Aksiyonun planlanan bitiş tarihi  bilgisinin açılan takvim alanında belirlendiği alandır.

**Standart Madde No:** Aksiyonlar-Yeni Kayıt ekranında Aksiyonla ilişkilendirilen ilgili Standart Madde No bilgisinin ![ref97] butonu tıklanarak açılan sistemde tanımlı olan Madde No listesinden seçilebildiği alandır.

**İlgili Doküman:** Aksiyonlar-Yeni Kayıt ekranında ilgili Doküman bilgisinin ![ref97] butonu tıklanarak açılan sistemde tanımlı olan Doküman listesinden seçilebildiği alandır.

**İlgili Kök Neden:** Aksiyonlar-Yeni Kayıt ekranında İlgili Kök Neden Bilgisinin ![ref97] butonu tıklanarak açılan Kök neden sekmesinde kök neden olarak seçilen kök neden veya kök nedenlerle ilişki kurulduğu alandır.

**Revize Edilecek dokümanlar:** Aksiyonlar-Yeni Kayıt ekranında revize edilecek dokümanı ![ref97] butonu tıklanarak açılan Doküman listesinde seçildiği alandır.

Düzeltici ve Önleyici Faaliyetler modülü parametrelerinde 183 numaralı “DÖF Aksiyon - Doküman ilişkisi kurulacak mı?” parametresi parametre değeri “Evet” seçilerek parametre aktif edilir. ![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_409.png)

Parametre aktif edildikten sonra Doküman Yönetimi Modülünde Doküman ile ilgili revizyon talebi gönderilir. Doküman Revizyon Talepleri görevinde tıklanarak Doküman Yönetimi Modülünde revizyon işlemi başlatırılır.Revizyon işlemi doküman modülünda olduğu varsa görüş, kontrol ve onay aşamalarında geçerek doküman dağıtım matrisindeki kullanıcılara okuma görevi olarak gönderilir. Bu aşamalar yapıldıktan sonra Aksiyonlar sekmesinde yapılan iş kısmında dokümanın yayınlandığı bilgisi verilir.Doküman revizyon talebi işlemi yapılmadığı takdirde Aksiyonun gerçekleştirme işlemine sistem izin vermez. Sistem tarafında “Aksiyondaki ilişkili dokümanların revizyon işlemleri tamamlanmadığı için kayıt kapatılamaz!” uyarı mesajı verilir.Dokümanda revizyon işlemi yapılarak doküman yayınlandıktan sonra DÖF Kaydında Aksiyonlar sekmesinde Aksiyon gerçekleştirme işlemi yapılr. 

**Ek Dosyalar:** Aksiyonlar  sekmesinde bu aşamada varsa bu Aksiyonla ile ilgili  kanıt doküman, fotoğraf gibi ek dosya yükleme işlemi butonlar yardımıyla  yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_410.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref86]: Ek dosya sisteme yüklenir.

![ref98]: Yüklenen ek dosya bilgisi görüntülenir.

![ref3]: Yüklenen ek dosya bilgisi silinir.

![ref86]  butonu tıklanarak  Aksiyonlar aşamasında DÖF kaydınana ek dosya eklenir. Birden çok ek dosya eklenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_412.png)

Açılan Aksiyonlar-Yeni Kayıt ekranda Aksiyondan sorumlu kişi ve aksiyonu yapacak kişi listeden seçilir, aksiyon bilgisi girilir, aksiyonun planlanan bitiş tarihi belirlenir, aksiyon ile ilgili standart madde numaraları eklenebilir, aksiyon ile ilgili varsa referans dokümanlar ve kök nedenler eklenir. Yine istenirse Ek Dosyalar kısmından, Aksiyon ile alakalı ek dosya, doküman vb. eklenebilir. 

Aksiyonlar -Yeni Kayıt ekranında gerekli alanlar doldurulduktan sonra sol üst köşede yer alan  ![ref7]   butonuna tıklanarak aksiyon planlanmış olur ve onaydaki kişiye onay için aksiyon gönderilir.DÖF  Aksiyon Açma  onayı için bir akış kurgulandıysa ilgili rolün onayına gönderilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_413.png)
##### **6.2.1.8.Açma Onayı Bekleyen Aksiyonlar**
DÖF Kaydı için DÖF Aksiyon onayı için akış kurgulandığı için onaydaki kişiye sistem mail yollarken aynı zamanda bekleyen işlerine “**Açma Onayı Bekleyen DÖF Aksiyonları Listesi**” işi olarak görev düşürür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_414.png)

DÖF Aksiyonu Açma onayına gönderildikten sonra ilgili kişi, Bekleyen İşleri’ne gelerek “**Açma Onayı Bekleyen DÖF Aksiyonları Listesi**” adı altında Açma Onayı Aksiyonu  vereceği DÖF’ü görür. DÖF -Aksiyon No  alanındaki DÖF-Aksiyon kodu linki  tıklanarak  “**Onay Bekleyen DÖF’ler**” listesini görüntüler.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_415.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref72]: İlgili DÖF kaydının görüntüleme işlemi yapılır.

![ref73] : İlgili DÖF kaydı ile değişiklik yapması istenirse kullanılır. Eğer talepten açılan DÖF ise zorunlu alanları doldurmadan onaylama işlemi yapmamıza sistem izin vermeyecektir.

![ref74] : DÖF onaylama işlemini yapmak için kullanılır. Onay işleminden sonra ilgili DÖF kaydı Ekip Liderinin önüne düşer.

![ref75] : DÖF’ te girilen bilgiler uygun olmadığı durumda, DÖF’ ü reddetmek için kullanılır. 

![ref76]  : Çok fazla onaylanması gereken DÖF olması durumunda filtre seçeneğinden bilgiler süzülerek arama yapmak istendiğinde kullanılır.

![ref11]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref12]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref13]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranında kullanıcı bazlı tasarlama işlemi yapılır.

Onay Bekleyen DÖF’ler ekranında ![ref72] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_416.png)

Açılan Görüntüleme ekranında DÖF kaydı ile ilgili sekmeler tıklanarak Detay bilgileri görüntülenir. DÖF kaydının görüntüleme ekranında ![ref68] butonu tıklanılır.

DÖF kaydı ile ilgili  link ekranda görüntülenir. Sağ tıkla/kopyala -yapıştır yöntemleri yada kopyala- Yapıştır kısayol tuşları (Ctrl+C-Ctrl+V) ile DÖF kaydının görüntülenip, ilgili kişilere paylaşımı yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_417.png)

Onay Bekleyen DÖF’ler ekranında ![ref73] butonu tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_418.png)

Açılan DÖF İşlemleri-Kayıt Güncelleme ekranında görüntülen sekmelerde ilgili alanlar üzerinde düzenleme ve değişiklik yapılma işlemi yapılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_419.png)

DÖF İşlemleri-Kayıt Güncelleme ekranında yapılan değişikliklerin kaydedilmesi için ekranın sol üst köşesindeki ![ref71]  butonu tıklanılır. 

![ref77]  butonu tıklanarak Ret nedeni girilerek DÖF kaydı ret edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_420.png)

Açılan DÖF Ret ekranında DÖF bilgileri kontrol edilerek uygun olmadığı görüldüğünde DÖF Ret etme işlemi yapılır ve  Ret Nedeni bilgisi yazılması zorunludur. Red edilen açan kişiye ret etme nedeniyle birlikte gönderilebilir. Ret ederken detay bilgi için ret veya kaydın iptali için ret edilebilir, buna bağlı olarak ilgili seçeneği seçmelidir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_421.png)

Onay Bekleyen DÖF’ler ekranında ![ref74]  butonu tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_422.png)

Açılan DÖF Onay ekranında Onay notu alanında Onay notu bilgisi yazılarak ![ref78] butonu tıklanarak  DÖF kaydı onaylanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_423.png)

DÖF onaylarken onay notu bilgisi Düzeltici ve Önleyici Faaliyetler modülü parametrelerinde 154 numaralı “DÖF onaylarken onay notu girilsin?” parametresinde parametre değeri “Evet” seçilerek parametre aktif edilir. 

![ref79]


Parametre aktif edildikten sonra DÖF Onay ekranlarında Onay Notu alanı görüntülenir ve onay notu bilgisi girilerek DÖF onaylama işlemi yapılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_424.png)

Açma Onayı onaylanan Aksiyonların durumu “Açık” statüne gelir. Açık statüsündeki Aksiyonlar işi yapacak kişinin bekleyen işlerinde görev olarak düşer.
##### **6.2.1.9.Gerçekleştirilecek Aksiyonlar**
DÖF işlemlerinde açma onayı işlemi yapılan Aksiyonlar durumu “Açık” statüsünde geldikten sonra işi yapacak kişinin “bekleyen işlerinde” “**Gerçekleştirilecek DÖF Aksiyonları Listesi**” işi olarak görev düşer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_425.png)

Bekleyen İşleri’nden “**Gerçekleştirilecek DÖF Aksiyonlar Listesi**” altına gelinerek DÖF-Aksiyon No üzerine tıklanır. DÖF bilgileri ekranına ulaşılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_426.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref91] : Yeni bir aksiyon ekleme işlemi yapılır.

![ref92] :Listede seçili Aksiyon bilgisinin içeriği görüntülenir.

![ref93]:Listede seçili Aksiyon bilgisi üzerinde değişiklik/düzenleme/güncelleme işlemi yapılır.

![ref94] Listede seçili Aksiyon bilgisi kopyalama işlemi yapılır.

![ref95]:Listede seçili Aksiyonun gerçekleştirilmesi işlemi yapılır.

![ref96] :Listede seçili** planlanan aksiyonun termin süresini geciktirme işlemi yapılır.

![ref10]: Veriler Excel’ e aktarılır.( Aksiyonlar ekranında listede  bulunan Aksiyon listesinin Excel formatında raporu alınır.)

![ref11]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref12]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref13]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranında kullanıcı bazlı tasarlama işlemi yapılır.

DÖF İşlemeleri-Kayıt Güncelleme ekranında Aksiyonlar sekmesinde ![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_427.png)(Aksiyonu Gerçekleştir) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_428.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Yapılan İş:** Aksiyonlar gerçekleştirme ekranında yapılan iş açıklama bilgisinin girildiği alandır.

**Aksiyon Gerçekleştirme Tarihi:** Aksiyonlar gerçekleştirme ekranında Aksiyon Gerçekleştirme Tarihinin belirlendiği alandır.

**Ek Dosyalar:** Aksiyonlar gerçekleştirme ekranında bu aşamada varsa bu Aksiyonla ile ilgili  kanıt doküman, fotoğraf gibi ek dosya yükleme işlemi butonlar yardımıyla  yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_429.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref86]: Ek dosya sisteme yüklenir.

![ref98]: Yüklenen ek dosya bilgisi görüntülenir.

![ref3]: Yüklenen ek dosya bilgisi silinir.

![ref86]  butonu tıklanarak  Aksiyonlar aşamasında DÖF kaydına ek dosya eklenir. Birden çok ek dosya eklenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_430.png)

Aksiyon Gerçekleştirme ekranında, aksiyonun gerçekleştirme bilgisi ve gerçekleştirme tarihi girilir. Ayrıca istenirse aksiyonun gerçekleştirme aşamasına ek dosya eklenebilir. Yapılan iş ve varsa ek dosya eklendikten sonra gerekli alanlar doldurulduktan sonra sol üst köşede yer alan  ![ref7]   butonuna tıklanarak aksiyon gerçekleştirilmiş olur. Gerçekleşme onayı  bekleyen DÖF Aksiyonları için bir akış kurgulandıysa ilgili rolün onayına gönderilir. Onay kurgulanmadıysa Sonuç raporu yazmak için Ekip Lideri/  Ekip üyesinin Bekleyen İşlerine gönderilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_431.png)
##### **6.2.1.10. Gerçekleştirme Onayı Bekleyen DÖF Aksiyonları Listesi**
DÖF kaydı için Gerçekleştirme Onayı Bekleyen DÖF Aksiyonları için akış kurgulandığı için onaydaki kişiye sistem mail yollarken aynı zamanda bekleyen işlerine “**Gerçekleştirme Onayı Bekleyen DÖF Aksiyonları Listesi**” işi olarak görev düşürür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_432.png)

DÖF Aksiyonu Gerçekleşme işlemi  yapıldıktan sonra ilgili kişi, Bekleyen İşleri’ne gelerek “**Gerçekleştirme Onayı Bekleyen DÖF Aksiyonları Listesi**” adı altında Gerçekleşme  Onayı Bekleyen DÖF Aksiyonları olan  DÖF’ü görür. DÖF -Aksiyon No  alanındaki DÖF-Aksiyon kodu linki  tıklanarak  “**Onay Bekleyen DÖF’ler**” ekranı  görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_433.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref72]: İlgili DÖF kaydının görüntüleme işlemi yapılır.

![ref74] : DÖF onaylama işlemini yapmak için kullanılır. Onay işleminden sonra ilgili DÖF kaydı Ekip liderinin önüne düşer.

![ref75] : DÖF’ te girilen bilgiler uygun olmadığı durumda, DÖF’ ü reddetmek için kullanılır. 

![ref76]  : Çok fazla onaylanması gereken DÖF olması durumunda filtre seçeneğinden bilgiler süzülerek arama yapmak istendiğinde kullanılır.

![ref11]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref12]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref13]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranında kullanıcı bazlı tasarlama işlemi yapılır.

Onay Bekleyen DÖF’ler ekranında ![ref72] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_434.png)

Açılan Görüntüleme ekranında DÖF kaydı ile ilgili sekmeler tıklanarak Detay bilgileri görüntülenir. DÖF kaydının görüntüleme ekranında ![ref68] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_435.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_436.png)

Görüntüleme ile ilgili link ekranda görüntülenir. Sağ tıkla/kopyala -yapıştır yöntemleri yada kopyala- Yapıştır kısayol tuşları (Ctrl+C-Ctrl+V) ile DÖF Kaydının görüntülenip , ilgili kişilere paylaşımı yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_437.png)

G8D raporu sekmesinde, G8D raporu detay bilgiler görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_438.png)

Tarihçe sekmesinde DÖF Kaydı ilgili yapılan işlere ait DÖF açma onayı, DÖF gelişme raporu ,DÖF Aksiyon Açma, DÖF Aksiyon Gerçekleştirme gibi DÖF  kaydının  onay geçimişi listesinin bilgisi verilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_439.png)

Onay Bekleyen DÖF’ler ekranında ![ref77]  butonu tıklanarak Ret nedeni girilerek DÖF kaydı ret edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_440.png)DÖF Ret ekranında ![ref77]  butonu tıklanarak Ret nedeni girilerek DÖF kaydı ret edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_441.png)Onay Bekleyen DÖF’ler ekranında ![ref74]  butonu tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_442.png)Açılan DÖF Onay ekranında  Onay notu alanında Onay notu bilgisi yazılarak ![ref78] butonu tıklanarak  DÖF kaydı onaylanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_443.png)

DÖF onaylarken onay notu bilgisi Düzeltici ve Önleyici Faaliyetler modülü parametrelerinde 154 numaralı “DÖF onaylarken onay notu girilsin?” parametresinde parametre değeri “Evet” seçilerek parametre aktif edilir. Parametre aktif edildikten sonra DÖF Onay ekranlarında Onay Notu alanı görüntülenir ve onay notu bilgisi girilerek DÖF onaylama işlemi yapılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_444.png)

Aksiyonlar planlanıp, gerçekleştikten ve onaylandıktan sonra DÖF Kaydının aşaması  Sonuç Raporu aşamasında geçer.
##### **6.2.1.11.Sonuç Raporu**
Aksiyonlar planlanıp gerçekleştirildikten sonra süreç, sonuç raporunun yazılmasıyla devam eder. Ekip Lideri/  Üyesi, Bekleyen İşleri’de  “**Sonuç Raporu Yazılacak DÖFler Listesi”** iş olarak görev düşer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_445.png)

DÖF Aksiyonu planıp, gerçekleştilip ve onaya  gönderildikten sonra Ekip/Ekibin, Bekleyen İşleri’ne gelerek “**Sonuç Raporu Yazılacak DÖFler Listesi**” adı altında  Sonuç Raporu yazılacak DÖF’ü görür. DÖF -No  alanındaki DÖF kodu linki  tıklanarak  DÖF İşlemleri-Kayıt Günceleme ekranında Sonuç Raporu sekmesi görüntüler. DÖF parametrelerinde 79 numaralı “Sonuç Raporu kullanılacak mı? (E/H))” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_446.png)

Parametre aktif edildikten sonra DÖF İşlemleri-Kayıt güncelleme ekranında Sonuç Raporu sekmesini görüntülenir ve DÖF kaydınında Soruç raporu aşaması  kullanılır. Sonuç raporu, DÖF ile ilgili alınan nihai önlemleri, çözüm önerilerini içeren bir rapordur.Sonuç Raporu uygunsuzluğun giderilmesi için bu aşama kadar yapılan işlem basamakların bir özet raporudur. Sonuç Raporu yine Çözüm Ekibi oluşturan Ekip lideri tarafında yazılır. DÖF İşlemleri sırasında yapılan tüm işlemlerin özeti niteliğinde, kapatma onayı verecek kişi için hazırlanan sonuç raporudur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_447.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Sonuç Raporu:** Sonuç Raporu sekmesinde Sonuç Raporu açıklama bilgisinin girildiği alandır.

**Ek Dosyalar:** Sonuç Raporu sekmesinde bu aşamada varsa bu sonuç raporu ile ilgili  kanıt doküman, fotoğraf gibi ek dosya yükleme işlemi butonlar yardımıyla  yapılır. Sonuç raporu aşamasında ek dosya yükleme işlemi zorunlu getirilmesi işlemi için Düzeltici ve Önleyici Faaliyetler modülü parametrelerinde 214 numaralı “Sonuç raporunda ek dosya zorunlu olsun” parametresinin parametre değeri “Evet”seçilerek parametre aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_448.png)

Parametre aktif edildiğinde Sonuç raporu aşamasında ek dosya yükleme işlemi yapılmadan sonuç rapor kayıt  işlemi gerçekleşmez.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_449.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref86]: Ek dosya sisteme yüklenir.

![ref87]: Yüklenen ek dosya bilgisi görüntülenir.

![ref3]: Yüklenen ek dosya bilgisi silinir.

![ref86]  butonu tıklanarak  gelişme raporu aşamasında DÖF kaydına Sonuç Raporu aşamasında ek dosya eklenir. Birden çok ek dosya eklenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_450.png)

Açılan ekranda Sonuç Raporu yazılır. Sonuç Raporu’na eklenmek istenen ek dosyalar, varsa eklenebilir. Gerekli alanlar ilgili bilgiler girildikten sonra ekranın sol üst köşeside yer alan  ![ref16]  butonu tıklanarak Sonuç Raporu kaydedilir ve DÖF kapatma onayına gider.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_451.png)Sonuç raporu yazılma işlemi kaydedildikten sonra, önceden belirlenen DÖF kapatma sorumlusuna bekleyen işlerine **“Kapatılacak DÖF’ler Listesi”** işi olarak görev düşecektir. 
##### **6.2.1.12.İzleme**
DÖF’ün kapatılması aşamasında bazen belirli tarih aralığına kadar aynı problemle karşılaşılacak mı diye DÖF kapatılmaz ve izlemeye alınabilir. İzleme işlemi uygunsuzluğun devam edip edilmediğini kontrol amaçlı belirli bir zaman diliminde izleme sorumlusuna görev ataması yapıldığı süreçtir. İzleme sorumlusu belirlenen tarihlerde uygunsuzluğun devam edip etmediğini üzerine atanan görevden dolayı kontrol eder. Yapılan aksiyonların yeterliliğini, etkinliğini veya düzgün yapılıp yapılmadığını atanan bu görevle izleyerek rapor yazma işlemi yapar.

DÖF Kaydı sonuç raporu aşamasında sonra DÖF Kapatma sorumlusunun Bekleyen işlerinde “**Kapatılacak DÖFler Listesi”**  işi olarak görev  düşer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_452.png)

İlgili görevdeki DÖF No alanındaki DÖF kodu linki tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_453.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref99] : Düzeltici ve Önleyici Faaliyet  ile ilgili tüm bilgileri görüntüleme işlemi yapılır.

![ref100] : Kapatma onayı verecek kişi yapılan aksiyonların yeterli olmadığı kararı verdiğinde, eksik kalan aksiyonları tanımlama işlemi yapılır. 

![ref101] : Yapılan aksiyonların yeterliliğini, etkinliğini veya düzgün yapılıp yapılmadığını farklı bir kişi tarafından izlenerek rapor yazma görevi verilme işlemi yapılır.

![ref102] :Kapat Onayını ve yeterlik bilgisinin girme işlemi yapılarak DÖF kaydı kapatılır.

![ref76]  : Çok fazla onaylanması gereken DÖF olması durumunda filtre seçeneğinden bilgiler süzülerek arama yapmak istendiğinde kullanılır.

![ref11]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref12]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref13]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranında kullanıcı bazlı tasarlama işlemi yapılır.

Onay Bekleyen DÖF’ler ekranında İzleme işlemi yapmak için  ![ref101] botunu tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_458.png)

Düzeltici ve Önleyici Faaliyetler modülü parametrelerinde 98 numaralı “Döf İzleme kulakçığı kapatılsın mı? (E/H) parametre değeri “Evet” seçildiğinde DÖF kaydında DÖF izleme sekmesi görüntülenmez. Parametre değeri ”Hayır” olduğunda DÖF İzleme sekmesi DÖF kaydında görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_459.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref8]: Yeni bir izleme bilgisi tanımlanır.

![ref10]: Veriler Excel’ e aktarılır.

![ref11]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref12]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref13]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_460.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Sorumlu:** İzleme -Yeni Kayıt ekranında Sorumlu kişini bilgisinin ![ref103] butonu tıklanarak açılan sistemde tanımlı olan Personel listesinden seçilebildiği alandır.

**İzleme Bitiş Tarihi:** İzleme -Yeni Kayıt ekranında açılan Takvim alanından İzleme Bitiş Tarihi seçildiği alandır.

**İzleme Bilgisi:** İzleme -Yeni Kayıt ekranında İzleme açıklama bilgisinin girildiği alandır.

**İlgili Dokümanlar:** İzleme -Yeni Kayıt ekranında ilgili dokümanların ![ref103] butonu tıklanarak açılan sistemde tanımlı Doküman listesinden seçilebildiği alandır.

**Ek Dosyalar:** İzleme -Yeni Kayıt ekranında bu aşamada varsa bu izleme ile ilgili  kanıt doküman, fotoğraf gibi ek dosya yükleme işlemi butonlar yardımıyla  yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_462.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref86]: Ek dosya sisteme yüklenir.

![ref87]: Yüklenen ek dosya bilgisi görüntülenir.

![ref3]: Yüklenen ek dosya bilgisi silinir.

![ref86]  butonu tıklanarak izleme aşamasında DÖF kaydınana ek dosya eklenir. Birden çok ek dosya eklenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_463.png)

Açılan İzleme -Yeni Kayıt ekranında izlemeden sorumlu kişi bilgisi girilir, izlemenin bitiş tarihi belirlenir, izleme bilgisi girilir, varsa izleme ile alakalı ek dosya, doküman vb. eklenebilir. Gerekli alanlar doldurulduktan sonra sol üst köşede yer alan  ![ref16]  butonu tıklanarak İzleme kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_464.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_465.png)

Düzeltici ve Önleyici Faaliyetler modülü parametrelerinden 137 numaralı “DÖF İzleme zorunlu Olsun Mu?” parametre değeri “Evet” seçilerek parametre aktif edilerek Düzeltici ve Önleyici Faaliyetler modülünde İzleme aşamasının zorunlu olması  sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_466.png)

DÖF kaydında izleme aşaması yapılmadan DÖF kaydı kapatılmaz.

Düzeltici ve Önleyici Faaliyetler Modülü parametrelerinde 139 numaralı “Varsayılan izleme sorumlusu rol kodu” parametresine rol kodu tanımlanılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_467.png)

Tanımlanan bu Rol kodu Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Rol Tanımlama menüsünde modül olarak Düzeltici ve Önleyici Faaliyetle modülü seçilerek listelenen rol tanımlarından alınır. İzleme Görevi atama işleminde izleme sorumlusu alanında  parametreye tanımlı bu rol kodundaki kişiyi sistem otomatik olarak varsayılan olarak getirir.

İzleme görevinin atama işleminden sonra İzleme sorumlusunun  Bekleyen İşlerimde “**İzleme Raporu Yazılacak DÖFler Listesi**” işi olarak görev düşer. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_468.png)

İzleme Sorumlusu ilgili görevdeki DÖF No alanındaki DÖF kodu linki tıklayarak DÖF işlemleri-Kayıt Güncelleme ekranında İzleme sekmesini görüntüler.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_469.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref104]:İzleme Raporu yazılma işlemi yapılır.

![ref10]: Veriler Excel’ e aktarılır.

![ref11]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref12]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref104] butonu tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_471.png)

İzleme raporu yazılacağı ekran açılır

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_472.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**İzleme Raporu:** İzleme Raporu ekranında  İzleme Raporu açıklama bilgisinin girildiği alandır.

**Ek Dosyalar:** İzleme Raporu ekranında bu aşamada varsa bu İzleme raporu ile ilgili  kanıt doküman, fotoğraf gibi ek dosya yükleme işlemi butonlar yardımıyla  yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_473.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref86]: Ek dosya sisteme yüklenir.

![ref87]: Yüklenen ek dosya bilgisi görüntülenir.

![ref3]: Yüklenen ek dosya bilgisi silinir.

![ref86]  butonu tıklanarak istenirse İzleme raporu aşamasında DÖF kaydına ek dosya eklenir. Birden çok ek dosya eklenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_474.png)

Açılan DÖF işlemleri-Kayıt güncelleme ekranında İzleme Raporu sekmesinde  İzleme Raporu bilgisi yazılır varsa izleme raporu ile ek dosya butonlar yardımıyla yükleme işlemi yapılır.  Gerekli alanlar doldurulduktan sonra sol üst köşede yer alan  ![ref105]  butonu tıklanarak izleme raporu kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_476.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_477.png)

**Hata Dağılımları;**

Düzeltici ve Önleyici Faaliyetler modülünde hata maliyetlerinin  tanımlama işleminin yapıldığı, tutarın hesaplandığı  departmanlara, personellere göre hata dağılımlarının, departmanlara personellere göre dağılımlarının  yüzde oranın belirlendiği sekmedir.Hata dağılımları genelde otomativ sektöründe kullanılmaktadır.Düzeltici ve Önleyici Faaliyetler modülü parametrelerinde 26 numaralı “Hata Maliyetleri Modülü Aktif (E/H)” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_478.png)

Parametre aktif edildikten sonra DÖF İşlemleri -Kayıt Güncelleme ekranından Hata Dağılımları sekmesi görüntülenir ve hata dağılımları özelliği kullanılır.DÖF işlemleri -Kayıt Güncelleme ekranında Hata Dağılımları sekmesi tıklanarak Hata dağılımları ekranı görüntülenir. Hata dağılımları sekmesinde hatalarının personellere ve departmanlara göre dağılımlarının ve yüzde oranlarının girilmesi işlemide yapılır. 

Düzeltici ve Önleyici Faaliyetler Modülü parametrelerinde 27 numaralı “Hataların Bölümlere Ayrılması Modülü Aktif” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_479.png)

Parametre aktif edildikten sonra DÖF İşlemleri-Kayıt Güncelle ekranında Hata Dağılımı sekmesinde Hataların Departmanlara Dağılımı alanı görüntülenir ve Hataların departmanlara dağılımın yüzde oranları girilerek bu özellik kullanılır.

DÖF İşlemleri-Kayıt Güncelle ekranında Hata Dağılımı sekmesinde hatalarının personellere dağılımının yapılması için 28 numaralı “Hataların Personele Dağılımı Modülü Aktif” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_480.png)

Parametre aktif edildikten sonra DÖF İşlemleri-Kayıt Güncelle ekranında Hata Dağılımı sekmesinde Hatalarının Personellere Dağılımı alanı görüntülenir ve personellere göre hataların dağılım oranları girilerek bu özellik kullanılır.



![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_481.png) ![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_482.png)

**G8D Raporu;**

Düzeltici ve  Önleyici Faaliyetlerin modülünde  D1’den D8’e adım adım kök neden analizi ve çözümleri ile hata tekrarını engelleyici uygulanacak aksiyonların detaylı takibini sağlayan 8 adımlı problem çözme ve raporlama tekniği desteklendiği rapordur. G8D yaklaşımını kullanarak problemin tekrar oluşmaması için her türlü önlemin alınma işlemi yapılır.Düzeltici ve Önleyici Faaliyetler modülü parametrelerinde 33 numaralı “DÖF G8D Raporu kullanılacak mı?” parametresi parametre değeri “Evet” seçilerek parametre aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_483.png)

Parametre aktif edildikten sonra DÖF işlemleri-Yeni Kayıt ekranında G8D  Raporu sekmesi görüntülenir ve bu özellik kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_484.png)

Düzeltici ve Önleyici Faaliyetler modülü parametrelerinde 34 numaralı “G8D zorunlu olsun mu?(E/H)” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_485.png)

Parametre aktif edildikten sonra DÖF İşlemleri -Kayıt Güncelleme ekranında G8D Raporu sekmesinde  tıklanarak açılan alanların doldurulmasını zorunlu tutar.

DÖF işlemleri -Kayıt güncelleme ekranında G8D Raporu sekmesinde ![ref106] (Yazdır)  butonu tıklanarak  G8D raporu alınır. G8D raporunun Düzeltici ve Önleyici Faaliyetler modülü parametrelerinde 69 numaralı “DÖF G8D raporu şablon dosyası” parametresine rapor formatının tanımlanması gerekir. G8D rapor formatının parametreye tanımlama işlemi için Sistem Altyapı Tanımları/BSAT/ Konfigürasyon Ayarları/Rapor Formatları Düzenleme menüsünde ![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_487.png) butonu tıklanarak G8D rapor formatının sisteme yükleme işlemi yapılmadır. Rapor Formatları Düzenleme menüsünde sisteme yüklenen G8D rapor formatının sağ tıkla/kopyala yöntemi ile adı ve uzantısı kopyalanır. Kopyalanan G8D rapor formatının adı ve uzantısı Düzeltici ve Önleyici Faaliyetler Modülü parametrelerinden  69 numaralı parametrenin parametre değerine sağ tıkla/yapıştır yöntemi ile yapıştırılarak tanımlanır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_488.png)

Tanımlama işlemi yapıldıktan sonra ![ref106] (Yazdır)   butonu tıklanarak G8D raporu alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_489.png)

G8D raporunun Excel formatında raporu alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_490.png)
##### **6.2.1.13.Kapatma**
DÖF Kaydı izleme raporu aşamasında sonra DÖF Kapatma sorumlusunun Bekleyen işlerinde “**Kapatılacak DÖFler Listesi**”  işi olarak görev  düşer. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_491.png)

İlgili görevdeki DÖF No alanındaki DÖF Kodu linki tıklanarak ilgili DÖF’ü görüntüler. Bu aşamada uygunsuzluk ilgili alınan aksiyonlar sonucu uygunsuzluk giderildiği  görüldüğünde Süreç DÖF kaydının kapatma aşaması ile devam edilir. DÖF no’su üzerine tıklayarak “**Onay Bekleyen DÖF’ler”**  ekranına gelir.Bu aşamada seçenekler sunulur. Bu aşamada DÖF kaydı ile bilgileri görüntüler. Kapatma onayı verecek kişi yapılan aksiyonların yeterli olmadığı kararı verdiğinde, eksik kalan aksiyonları tanımlama süreci başlatabilir. Süreç Aksiyonlar sekmesinde yeni Aksiyonların planlanması ve bu Aksiyonlara bağlı olarak Sonuç raporu sekmesinde sonuç raporun yazılması işlemini şeklinde aşama aşama devam eder. Bir başka seçenek olarak İzleme açılabilir. Alınan Aksiyonların yeterli olup, olmadığı kontrol amaçlı izleme sorumlusu atanarak ve izleme sorumlu izleme raporu yazma şeklinde süreç devam edebilir. Uygunsuzluğun giderildiği  kesin olarak ulaşıldığında  DÖF kapatılmasına karar verilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_492.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref99] : Düzeltici ve Önleyici Faaliyet  ile ilgili tüm bilgileri görüntüleme işlemi yapılır.

![ref100] : Kapatma onayı verecek kişi yapılan aksiyonların yeterli olmadığı kararı verdiğinde, eksik kalan aksiyonları tanımlama işlemi yapılır. 

![ref101] : Yapılan aksiyonların yeterliliğini, etkinliğini veya düzgün yapılıp yapılmadığını farklı bir kişi tarafından izlenerek rapor yazma görevi verilme işlemi yapılır.

![ref102] :Kapat Onayını ve yeterlik bilgisinin girme işlemi yapılarak DÖF kaydı kapatılır.

![ref76]  : Çok fazla onaylanması gereken DÖF olması durumunda filtre seçeneğinden bilgiler süzülerek arama yapmak istendiğinde kullanılır.

![ref11]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref12]: Menü ekranın tekrar varsayılan ayarlama gelmesi işlemi yapılır.

![ref13]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranında kullanıcı bazlı tasarlama işlemi yapılır.

![ref102] (DÖF Kapatma) butonu tıklanır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_493.png)

DÖF’ü Kapatma ekranına  açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_494.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Yeterlilik Bilgisi:** DÖF İşlemleri- Kayıt Güncelleme ekranında Kapatma sekmesinde Yeterlilik açıklama bilgisinin girildiği alandır.

**Onay Notu:** DÖF İşlemleri- Kayıt Güncelleme ekranında Kapatma sekmesinde Onay Notu açıklama bilgisinin girildiği alandır.

**Uygunsuzluk Kategorisi:** DÖF İşlemleri- Kayıt Güncelleme ekranında Kapatma Sekmesinde Uygunsuzluk Kategorisi bilgisinin sistemde tanımlı Uygunsuzluk Kategorisi Listesinden seçilebildiği alandır.

**DÖF ‘ün Etkinliği değerlendirilecek mi? :** DÖF İşlemleri- Kayıt Güncelleme ekranında Kapatma sekmesinde DÖF ‘ün Etkinliği değerlendirilecek mi? aktif edilecekse ilgili check box işaretlenir. Parametreye bağlı olarak görüntülenen alandır.Düzeltici ve Önleyici Faaliyetler Modülü parametrelerinde 87 numaralı “DÖF Etkinlik Değerlendirme kullanılacak mı? (E/H)” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. Parametre aktif edildikten sonra DÖF İşlemleri- Kayıt Güncelleme ekranında “DÖF ‘ün Etkinliği değerlendirilecek mi?” alanı görüntülenir. İlgili check box işaretlenerek Düzeltici ve Önleyici Faaliyetler  modülünde DÖF etkinlik değerlendirme işlemi kullanılır. Bu işlemin kullanılması için Anket Soru listeleri menüsünde DÖF etkinlik değerlendirme ile ilgili anket tanımlanmalıdır. Ayrıca Anket ile ilgili Düzeltici ve Önleyici Modülü parametlerinden 80 numaralı “Etkinlik Değerlendirme Anket Kodu”  parametreye tanımlanmalıdır.83 numaralı “Etkinlik değerlendirme anketi geçerlilik süresi” parametresinde anketin geçerlilik süre bilgisinin girilmesi gerekir. DÖF ile ilgili  kayıt kapandıktan minimum 1 gün sonra bu anketler “Bekleyen işlerime” Anket İşlemleri Modülünde” “Doldurulması Gereken Anketler” işi olarak görev düşer. Bu görevin düşmesi için ajan programında ilgili fonksiyonun sunucudan çalıştırılması işlemi mutlaka yapılması gerekmektedir.İlgili Görevdeki anket kodu alanında link tıklanarak Anket doldurma işlemi yapılır.

**DÖF Maliyeti:** DÖF İşlemleri- Kayıt Güncelleme ekranında Kapatma sekmesinde DÖF Maliyeti bilgisinin girildiği alandır.

**Ek Dosyalar:** DÖF İşlemleri- Kayıt Güncelleme ekranında Kapatma sekmesinde varsa Ek Dosya yüklendiği kısımdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_495.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref88]: Ek dosya sisteme yüklenir.

![ref87]: Yüklenen ek dosya bilgisi görüntülenir.

![ref9]: Yüklenen ek dosya bilgisi silinir.

![ref88]  butonu tıklanarak tanımlanan kapatma aşamasında ek dosya eklenir. Birden çok ek dosya eklenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_496.png)

Açılan DÖF İşlemleri- Kayıt Güncelleme ekranında Kapatma sekmesinde yeterlilik bilgisi girilir. Ayrıca istenirse uygunsuzluk kategorisi alanına eklemeler yapılabilir. Yine istenirse kapatma aşamasına ek dosya eklenebilir. Gerekli alanlar doldurulduktan sonra sol üst köşede yer alan  ![ref7]   butonuna tıklanarak bilgiler kaydedilir ve DÖF kapatılmış olur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_497.png)

Düzeltici ve Önleyici Faaliyetler modülünde 6 numaralı “Kapatma Süresi” parametresinde parametre değerine girilen değere göre DÖF Sonuç raporu yazıldıktan kaç gün sonra DÖF’ün kapatılacağını ayarının yapılma işlemi yapılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_498.png)

Parametrede yapılan bu ayara göre kapatma onayında maksimum bekleme süresini ifade etmektedir.
##### **6.2.1.14.Görüntüleme**
DÖF işlemleri-Kayıt Güncelleme ekranında Görüntüle sekmesi tıklanarak DÖF kaydının aşama aşama işlem basamaklarının detay bilgileri görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_499.png)

DÖF kaydının görüntüleme ekranında ![ref107] butonu tıklanılır. Görüntüleme ile ilgili link ekranda görüntülenir. Sağ tıkla/kopyala -yapıştır yöntemleri yada kopyala- yapıştır kısayol tuşları (Ctrl+C-Ctrl+V) ile DÖF Kaydının görüntülenip , ilgili kişilere paylaşımı yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_501.png)

Tarihçe sekmesinde DÖF Kaydı ilgili yapılan işlere ait DÖF açma onayı, DÖF gelişme raporu, DÖF Aksiyon Açma, DÖF Aksiyon Gerçekleştirme gibi onay geçmişi ilgili bilgilerin listesi görüntülenir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_502.png)
##### **6.2.1.15.DÖF Kayıt Bakım** 
Listede seçili DÖF Kaydı üzerinde  ilgili düzenleme/değişiklik/güncelleme  işlemi yapılır.Kayıt Bakım özelliği işlemi yapma yetkisinde sahip kullanıcılar DÖF kaydı üzerinde  her türlü değişiklik yapma yetkisine sahip olurlar. DÖF Kaydı  kapalı bir durumda olsa bile kayıt üzerinde her türlü değişiklik yapılabilir. Bu işlemleri yapabilmek için kullanıcının, Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Modül Yöneticisi menüsünde, Düzeltici ve Önleyici Faaliyetler Modülü modül yöneticisi olarak atanması gerekir. Modül yöneticisi olarak atanan kullanıcıların ekranlarında  ![ref108]  butonu görüntülenir ve buton ile bir DÖF kaydı üzerinde istenilen bilgileri düzenlenebilirler.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_504.png)

DÖF İşlemleri ekranında durumu kapalı statüsündeki DÖF Kaydı seçili iken ![ref108]  butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_505.png)

**Ekranda bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_506.png):DÖF kaydı gelişme raporu aşamasına döndürülme işlemi yapılır.Kapalı statüsündeki DÖF Kaydı Gelişme raporu aşamasında başlar.DÖF kaydındaki süreç Gelişme raporu aşaması ile devam eder.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_507.png):DÖF kaydı sonuç raporu aşamasına döndürülme işlemi yapılır.Kapalı statüsündeki DÖF kaydı Sonuç raporu aşamasında başlar. DÖF kaydındaki süreç  Sonuç  raporu aşaması ile devam eder.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_508.png):Yapılan değişiklikler ilgili kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_509.png):DÖF Kaydı ile ilgili G8D raporu görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_510.png)

DÖF Kayıt Bakım ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_511.png) butonu tıklanarak ilgili alanlar üzerinde değişiklik ve düzenleme işlemi yapılır. ![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_512.png)  butonu tıklanarak ilgili kaydın silinme işlemi yapılır. ![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_513.png)(Açma Bildirimini Yayınla)  butonu ile kayıt ile ilgili açma bildirimi yayınlanır. ![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_514.png)(Açık Statüsüne Getir) butonu tıklanarak Aksiyonu açık statüsüne getirme işlemleri yapılır. ![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_515.png) butonu tıklanarak Kök Neden Analizi sekmesinde yeni bir Kök Neden ekleme işlemi yapılır. Kayıt Bakım özelliği kullanılarak ilgili alanlar üzerinde DÖF kaydının aşamalarında düzenleme işlemi yapılır.
##### **6.2.1.16.DÖF Yaygınlaştırma**
Açılan DÖF kaydının  DÖF Yaygınlaştırma özelliği kullanılarak  işyerinin diğer lokasyonları veya  departmanlarda da uygulanması işlemidir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_516.png)

DÖF Modülü  parametrelerinden 163 numaralı  “Döf işlemlerinde yaygınlaştırma olacak mı?” parametresinin parametre değerinin “Evet” seçilerek parametre aktif edilmelidir.  Parametre aktif edildiğinde ![ref63] butonu DÖF işlemleri- Yeni Kayıt ekranında görüntülenir ve bu özellik kullanılır.

![ref64]

DÖF Modülü parametrelerinde 165 numaralı “Kimler yaygınlaştırma yapabilecek?(Modül Yöneticileri=M,Açan=A,Ekip Lideri=E,Herkes=H)(Birden fazla için virgülle ayırınız)”  parametresine girilen değere göre kimlerin DÖF modülünde yaygınlaştırma işlemi yapacağı belirlenir.

DÖF İşlemleri ekranında DÖF Kaydı seçili iken ![ref63] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_517.png)

**Açılan ekranda ilgili alanlar tanımlanır**

**Departman/Müşteri/Tedarikçi:** DÖF Yaygınlaştırma ekranında ![ref109] butonu tıklanarak açılan sistemde tanımlı Departman listesinde yaygınlaştırma yapılacak Departman bilgisi seçildiği alandır.**		

**Ekip Lideri:** DÖF Yaygınlaştırma ekranında ![ref109] butonu tıklanarak açılan sistemde tanımlı personel listesinde istenirse Ekip lideri bilgisi seçildiği alandır.**			

**Sorumlu Departman	:**DÖF Yaygınlaştırma ekranında ![ref109] butonu tıklanarak açılan sistemde tanımlı departman listesinde yaygınlaştırma yapılacak Departman bilgisi seçildiği alandır.**	

**İş Yeri:** DÖF Yaygınlaştırma ekranında ![ref109] butonu tıklanarak açılan sistemde tanımlı iş yeri listesinde yaygınlaştırma yapılacak iş yeri bilgisi seçildiği alandır.

**Bilgilendirme:** DÖF Yaygınlaştırma ekranında Bilgilendirme alanına eklenecek personel veya kullanıcı grubu listesinde personel veya kullanıcı grubu ekleme işlemi yapıldığı alandır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_519.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref110]:Yeni bir DÖF  yaygınlaştırma işlemi ile eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_521.png):Listede seçili yaygınlaştırma yapılan DÖF kaydı bilgisi silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_522.png):Kayıt işlemi yapılır.

DÖF Yaygınlaştırma ekranında yaygınlaştırma yapılacak departman bilgisi seçilir, İstenirse Ekip lideri alanında personel listesinden ekip lideri seçimi yapılır.Yaygınlaştırma yapılacak İş yeri listesinde bilgisi İş yeri listesinde seçilir. DÖF Yaygınlaştırma ekranında gerekli alanlar ilgili bilgiler girildikten sonra![ref110]  butonu tıklanarak DÖF yaygınlaştırma işlemi eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_523.png)

DÖF Yaygınlaştırma ekranında yeni bir DÖF kaydına DÖF yaygınlaştırma listesine ekleme işleminden sonra ekranın sol üst köşede yer alan  ![ref16] butonu tıklanarak DÖF yaygınlaştırma kayıt işlemi gerçekleştirilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_524.png)
##### **6.2.1.17.DÖF İptal İşlemi**
Listede seçili DÖF Kaydının iptal işlemi yapılır. İptal işlemi silme işleminde farklı bir işlemdir. DÖF kaydının  işleyişi durur fakat sistem de kayıtlı olmaya devam eder. Bir onay akış çerçevesinde çalışır. ![ref111] butonu tıklanarak iptal işlemi yapılır.Açılan DÖF İptal  ekranında DÖF kaydının İptal nedeni bilgisi yazılarak kayıt işlemi yapılır. Kayıt işleminde sonra DÖF kaydı akıştaki kişinin İptal onayı gönderilir.Bunun için Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Akış Tanımlama menüsünde DÖF İptal Onayı akışının kurgulanması ve akıştaki rolün atanması gerekir. Akış Tanımlama işlemi yapılan iptal işlemin Alt Modül Tanımlama kısmında akışın kontrolünün yapılması gerekmektedir.DÖF İptal işleminin kullanılması için kullanıcının modül yönetici olması ve Düzeltici ve Önleyici Faaliyetler modülü parametrelerinde 95 numaralı “İptal fonksiyonu kullanılacak mı? “ parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_526.png)

Parametre aktif edildikten sonra Modül Yöneticinin DÖF İşlemleri ekranında ![ref111] butonu görüntülenir ve  iptal fonksiyonu özelliği kullanılır.DÖF İşlemleri  ekranında liste sekmesinde listede DÖF Kaydı seçilerek ![ref111] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_527.png)

Açılan DÖF İptal ekranında İptal Nedeni alanın DÖF Kaydının neden iptal edildiği bilgisi yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_528.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**DÖF Kodu:** DÖF İptal ekranında DÖF kodu bilgisi otomatik olarak sistem tarafında verildiği alandır.	

**DÖF'ü Açan:** DÖF İptal ekranında DÖF’ü Açan bilgisi otomatik olarak sistem tarafında verildiği alandır.		

**DÖF Açılma Tarihi:** DÖF İptal ekranında DÖF Açılma Tarihi bilgisi otomatik olarak sistem tarafında verildiği alandır.		

**Uygunsuzluk Tanımı:** DÖF İptal ekranında Uygunsuzluk Tanımı bilgisi otomatik olarak sistem tarafında verildiği alandır.	

**İptal Nedeni:** DÖF İptal ekranında DÖF kaydının neden iptal edildiği bilgisinin yazıldığı alandır.

**Ek Dosyalar:** DÖF İptal ekranında iptal aşamasında varsa bu DÖF kayıdının iptal ile ilgili  kanıt doküman, fotoğraf gibi ek dosya yükleme işlemi butonlar yardımıyla  yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_529.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref86]: Ek dosya sisteme yüklenir.

![ref87]: Yüklenen ek dosya bilgisi görüntülenir.

![ref3]: Yüklenen ek dosya bilgisi silinir.

![ref86]  butonu tıklanarak  iptal aşamasında DÖF kaydına ek dosya eklenir. Birden çok ek dosya eklenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_530.png)

DÖF İptal ekranında DÖF kaydının iptal nedeni bilgisi yazılarak , İptal nedeni ilgili varsa Ek Dosya yükleme işlemi yapılarak gerekli alanlar doldurulduktan sonra sol üst köşede yer alan  ![ref16]  butonu tıklanarak iptal işlemi akıştaki kişinin onayına sunulur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_531.png)

Onaydaki kişinin Bekleyen İşlerinde “**İptal Onayı Bekleyen DÖFler**” işi olarak görev düşer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_532.png)

İlgili görevdeki DÖF No alanındaki DÖF kodu linki tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_533.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref72]: İlgili DÖF kaydının görüntüleme işlemi yapılır.

![ref74] : DÖF onaylama işlemini yapmak için kullanılır. 

![ref75] : DÖF’ te girilen bilgiler uygun olmadığı durumda, DÖF’ ü reddetmek için kullanılır. 

![ref76]  : Çok fazla onaylanması gereken DÖF olması durumunda filtre seçeneğinden bilgiler süzülerek arama yapmak istendiğinde kullanılır.

![ref11]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref12]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref13]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranında kullanıcı bazlı tasarlama işlemi yapılır.

Onay Bekleyen DÖF’ler ekranında ![ref72] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_534.png)

Açılan Görüntüleme ekranında DÖF kaydı ile ilgili sekmeler tıklanarak Detay bilgileri görüntülenir. DÖF kaydının görüntüleme ekranında ![ref68] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_535.png)

DÖF kaydı  ile ilgili link ekranda görüntülenir. Sağ tıkla/kopyala -yapıştır yöntemleri yada kopyala- yapıştır kısayol tuşları (Ctrl+C-Ctrl+V) ile DÖF kaydının görüntülenip, ilgili kişilere paylaşımı yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_536.png)

G8D raporu sekmesi tıklanarak ![ref112] (Yazdır) butonu tıklanarak G8D raporu alanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_538.png)

Tarihçe sekmesinde DÖF Kaydı ilgili yapılan işlere ait DÖF açma onayı, DÖF İptal gibi onay geçmişi bilgilerinin listesine ulaşılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_539.png)

Onay Bekleyen DÖF’ler ekranında ![ref84]  butonu tıklanarak Ret nedeni girilerek DÖF kaydı iptal işlemi ret edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_540.png)

Açılan DÖF Ret ekranında DÖF kaydının  iptal işlemi Ret etme işlemi yapılır ve  Ret Nedeni bilgisi yazılması zorunludur. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_541.png)

Onay Bekleyen DÖF’ler ekranında ![ref81]  butonu tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_542.png)

Açılan DÖF Onay ekranında  Onay notu alanında Onay notu bilgisi yazılarak ![ref78] butonu tıklanarak  DÖF kaydı iptal işlemi onaylanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_543.png)
##### **6.2.1.18.DÖF Kaydını Silme İşlemi**
DÖF İşlemleri ekranında liste sekmesinde listede seçili DÖF Kaydının silme işlemi yapılır. Silme işleminin yapılması için kullanıcının modül yönetici olarak tanımlı olması gerekmektedir. Modül Yönetici olarak tanımlı kullanıcının DÖF İşlemleri ekranında ![ref113] butonu  görüntülenir.  DÖF işlemleri ekranında liste sekmesinde listede  DÖF Kaydı seçilerek ![ref113]  butonu tıklanarak DÖF Kaydının silinme işlemi yapılır.
DÖF işlemleri ekranında liste sekmesinde listede DÖF Kaydı seçilir ve ![ref113]  butonu tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_545.png)

Sistem tarafından “Seçili kaydı silmek istediğinizden emin misiniz?” uyarı mesajında “Tamam” butonu tıklanarak listede seçili DÖF kaydının silinme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_546.png)

Silme işlemi yapılan DÖF kayıtları veritabandan da siliniyor ve bu verilere sistemde ulaşılmıyor.
##### **6.2.1.19.DÖF Aksiyonlarını Toplu Onaya Gönderilme İşlemi**
DÖF kaydının Aksiyonlar sekmesinde DÖF Aksiyonları toplu onaya gönderilme işlemi yapılır. Bu işlemin yapılması için Düzeltici ve Önleyici Faaliyetler modülü parametrelerinde 186 numaralı “DÖF Aksiyonları toplu onaya gönderilsin mi?” parametresi değeri “Evet” seçilerek parametre aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_547.png)

Parametre aktif edildikten sonra Aksiyonlar sekmesinde ![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_548.png) butonu görüntülenir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_549.png)

Bu buton tıklanarak DÖF kayıtlarında Aksiyonlar sekmesinde tanımlanan ve durumu taslak statüsündeki Aksiyonlar toplu bir şekilde onaylama işlemi yapılarak Aksiyonların durumun “Açık” statüsüne gelmesi sağlanır. 

Aksiyonlar sekmesinde ![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_550.png) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_551.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_552.png)

Aksiyonlar ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_553.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref72]:Listede seçili Aksiyon bilgisinin görüntüleme işlemi yapılır.

![ref74] : Aksiyon onaylama işlemini yapılır ve onaylama işleminde sonra aksiyon durumu açık statüne gelir.

![ref75] : Aksiyon onaylama işleminde ret nedeni bilgisi yazılarak ret edilme işlemi yapılır.

![ref10]: Veriler Excel’ e aktarılabilir.

![ref11]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref12]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref13]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranında kullanıcı bazlı tasarlama işlemi yapılır.

Aksiyonlar  ekranında Aksiyon seçili iken ![ref72] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_554.png)

Açılan Aksiyon Görüntüleme ekranında Aksiyonun detay bilgileri görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_555.png)

Aksiyonlar ekranında ![ref77]  butonu tıklanarak ret nedeni girilerek Aksiyon ret edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_556.png)

Açılan DÖF Ret ekranında Ret Nedeni bilgisi yazılarak Aksiyonu onaylama işlemi ret edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_557.png)

Aksiyonlar  ekranında ![ref74]  butonu tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_558.png)

Aksiyonlar ekranında durumu taslak statüsünde olan  Aksiyonlar durumu “Aksiyonlar Plan Onayı” statüsüne gelir.Aksiyonlar ekranında  toplu onaylama işleminde sonra tüm  “Aksiyonlar Plan Onayı” statüsündeki Aksiyonlar durumu açık statüne gelir. Aksiyonlar sekmesinde durumu açık statüsüne gelen Aksiyonların gerçekleştirme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_559.png)

Düzeltici ve Önleyici Faaliyetler modülü parametrelerinde 186 numaralı “DÖF Aksiyonları toplu onaya gönderilsin mi?” parametresi aktif edilerek Aksiyonlar sekmesinde bu şekilde toplu onaya gönderilme işlemi yapılarak  toplu bir şekilde Aksiyonları açık statüne getirilir.  Açık statüsüne getirilen Aksiyonların gerçekleştirme işlemi yapılır.
##### **6.2.1.20.Aksiyon Uygunluk Kontrolü** 
Düzeltici ve Önleyici Faaliyetler modülünde kapatma aşamasında alınan aksiyon uygunluk  kontrolü işlemi yapılır. Bu işlemin yapılması için Düzeltici ve Önleyici Faaliyetler modülü parametrelerinde 173 numaralı “DÖF kapatmada aksiyon uygunluk kontrolü yapılsın mı?” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_560.png)

Parametre aktif edildikten sonra DÖF İşlemleri-Kayıt Güncelleme ekranında Kapatma sekmesinde DÖF’ün kapatma aşamasında “Tüm Aksiyonlar Uygun” alanı ile ilgili check box görüntülenir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_561.png)

İlgili check box işaretlenirse Kapatma aşama ilgili alanlar görüntülenir ve DÖF kaydının kapatma aşamasında ilgili alanlar doldurularak DÖF kaydı kapatılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_562.png)

DÖF İşlemleri-Kayıt Güncelleme ekranında Kapatma sekmesinde DÖF kapatma aşamasında Aksiyonun uygunluk kontrolünde Uygun değil ile ilgili check box işaretlendiğinde uygun olmaması ilgili açıklamanın yazılacağı alanı görüntülenir. Varsa Aksiyonun uygun olmama nedeni bu alana yazılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_563.png)

Bu aşamada uygun olup olmadığı kontrol edildiği gibi “Yeni bir Aksiyon aç” alanı ilgili check  box işaretlenerek yeni bir aksiyon açılma işlemi kapatma aşamasında gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_564.png)

DÖF İşlemleri -Yeni Kayıt  Güncelle ekranında Kapatma sekmesinde DÖF Kapatma aşamasında “Yeni Aksiyon Aç”  alanı ilgili check box işaretlendiğinde  ekranın sağ üstte ![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_565.png) butonu tıklanıldığında Aksiyonlar - Yeni Kayıt ekranı açılarak yeni bir aksiyon tanımlama işlemi yapılmasına olanak sistem olanak sağlar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_566.png)
##### **6.2.1.21.Düzeltici ve Önleyici Faaliyetler Modülü Ortak Kullanım İçin Yeni Alan Oluşturma**
Düzeltici ve Önleyici Faaliyetler Modülünde Detay Bilgiler, Gelişme Raporu,Kök Nedenler, Aksiyonlar, Sonuç Raporu ve Kapatma sekmelerinde  firmanın istemiş olduğu sistemde olmayan ekstra alanlar tanımlanabilir. Tanımlanan bu alanlar tüm Düzeltici ve Önleyici Faaliyetler Modül kaynakları için geçerlidir. Sistem Altyapı Tanımları/BSAT/ Konfigürasyon Ayarları/Dil Ayarları menüsü tıklanılır. Açılan Dil Ayarları sayfasında Modül alanında  “Düzeltici ve Önleyici Faaliyetler” seçilir ve ekranda Düzeltici ve Önleyici Faaliyetler Modülü ile ilgili dil tanımları görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_567.png)

Düzeltici ve Önleyici Faaliyetler Modülünde Entegre Yönetim Sistemi/ Düzeltici ve Önleyici Faaliyetler /DÖF işlemleri menüsünde ![ref8] butonu tıklatıldığında açılan DÖF işlemleri -Yeni Kayıt ekranında Detay Bilgiler sekmesinde parametrik tipli alan tanımlaması Dil Ayarların menüsünde yapılmaktadır. Ayrıca Düzeltici ve Önleyici Faaliyetler Modülünde Gelişme Raporu, Kök Nedenler, Aksiyonlar, Sonuç Raporu ve Kapatma aşamaların gerçekleştiği sekmelerde Dil Ayarları menüsünde parametrik tipli alan tanımlamasıda yapılmaktır. Bu aşamaların gerçekleştiği sekmelerde örneğin Gelişme Raporu ile ilgili parametrik tipli alan tanımlaması yapıldığında Gelişme Raporu sekmesinde, Kök Nedenler ilgili parametrik tipli alan tanımlaması yapıldığında Kök Nedenler sekmesinde tanımlanan parametrik alanlar görüntülenmektedir. Hangi sekmede parametrik tipli alan tanımlaması yapıldıysa ilgili sekmede parametrik tipli alanlar görüntülenmektedir. Bu aşamalarda parametrik tipli alanlarda kullanılan kısa kodlar bulunmaktadır. Hangi aşamada hangi kısa kodlar kullanılmış ayırt etmek mümkündür. 

Örneğin tanımlanan Metin Tipli parametrik tipli alanlarda hangi aşamada olduğunun ayırt etmek için aşağıdaki kısa kodların başlama kısımlarına dikkate etmek gerekir;

**Detay  Bilgiler:** lblPARAM1 kısa kodları genelde detay bilgiler sekmesinde görüntülen parametrik alanları temsil eder.

**Gelişme Raporu:** lblG\_Param1, lblG\_ ile başlayan kısa kodları genelde Gelişme raporu aşamasında görüntülenen parametrik tipli alanları temsil eder.

**Kök Nedenler:** lblKOKPARAM1, lblKOK\_ ile başlayan kısa kodları genelde Kök nedenler aşamasında görüntülenen parametrik tipli alanları temsil eder

**Aksiyonlar:** lblA\_Param1, lblA \_kısa kodları ile başlayan genelde Aksiyonlar aşamasında görüntülenen parametrik tipli alanları temsil eder.

**Sonuç Raporu:** lblS\_Param1, lblS\_ kısa kodları ile başlayan genelde Sonuç Raporu aşamasında görüntülenen parametrik tipli alanları temsil eder.

**Kapatma:** lblK\_Param1, lblK\_ kısa kodları ile başlayan genelde Kapatma aşamasında görüntülenen parametrik tipli alanları temsil eder.

**Detay bilgiler sekmesinde Dil Ayarlarında Metin Tipli Parametrik Alanların Listelenmesi**

DÖF Modülünde Entegre Yönetim Sistem/ Düzeltici ve Önleyici Faaliyetler/DÖF İşlemleri menüsünde Detay Bilgiler sekmesinde metin tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsünde modül listesinde açılır modül listesinde Düzeltici ve Önleyici Faaliyetler modülü seçilerek seçilen modülün dil tanımları görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_568.png)

Dil Ayarlarında gridde adı alanı “lblLPARAM” ve  tipi alanında “Metin” yazılarak Düzeltici ve Önleyici Faaliyetler modülü ilgili detay bilgiler sekmesinde  metin tipli alanlarının listelenmesi  sağlanılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_569.png)lblLPARAM  Metin tipli parametrik seçilerek alanın veri girişi için ![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_570.png)  butonuna tıklanır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_571.png)

Açılan Dil Ayarları ekranında değeri alanında tanımlanacak alanın tanım bilgisi yazılır. Başlık notu bilgisi, alanın zorunluluk bilgisi ,görüntülecek işlem kaynağı bilgisi  ve DÖF Türü bilgileri seçilir.  İlgili alanın Detay bilgiler sekmesinde görüntülenmesi işlemi DÖF işlemleri -Yeni kayıt ekranında seçilen işlem kaynağı ve DÖF türüne göre belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_572.png)

Gerekli alanlar ilgili bilgiler girildikten sonra ekranın sol üst köşesindeki ![ref16]  butonu tıklanarak dil ayarları kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_573.png)

Tanımlanan metin tipli alanın görüntülenmesi için Entegre Yönetim Sistemi/Düzeltici ve Önleyici Faaliyetler/DÖF İşlemleri menüsü tıklanılır.  Açılan ekranda tanımlanan metin tipli alanı DÖF Türü alanında tanımlama alanında seçilen DÖF türü ve İşlem kaynağı bilgisi seçilerek  Detay bilgiler sekmesinde görüntülenmesi sağlanır. Tanımlanan alanın zorunlu alan olduğu ve üzerine  mouse gelindeiğinde başlık notu bilgisinin görüntülendiği görülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_574.png)

#### **6.2.2.DÖF Talebi**
**Menü Adı**: Entegre Yönetim Sistemi/ Düzeltici ve Önleyici Faaliyetler / DÖF Talebi

DÖF Talebi tanımlama işleminin yapıldığı menüdür.DÖF talebi menüsü ile de sisteme yeni bir DÖF kaydedilebilir. Talepten açılan DÖF’ te sadece en temel bilgileri doldurulur. DÖF işlemleri menü yetkisi verilmeyecek, DÖF’ün her hangi bir akışında yer almayacak sadece DÖF talebinde bulunacak kullanıcılar için bu menüden yararlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_575.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Uygunsuzluğun Olduğu Departman:** DÖF Talebi ekranında Uygunsuzluğun Olduğu Departman bilgisinin ![ref114] butonu tıklanarak açılan sistemde tanımlı olan Departman listesinden seçilebildiği alandır.

**İş Yeri:** DÖF Talebi ekranında İş yeri bilgisinin ![ref114] butonu tıklanarak açılan sistemde tanımlı olan İş yeri listesinden seçilebildiği alandır.

**İşlem Kaynağı:** DÖF Talebi ekranında İşlem kaynağı bilgisinin açılır liste tıklanarak açılan sistemde kayıtlı İşlem kaynaklarından seçilebildiği alandır.

**Uygunsuzluk Tanımı:** DÖF Talebi ekranında Uygunsuzluk Tanımı bilgisinin girildiği alandır.

**Uygunsuzluk Detayı**: DÖF Talebi ekranında Uygunsuzluk Detayı bilgisinin girildiği alandır.

**Yönetim Sistemi:** DÖF Talebi ekranında Yönetim Sistemi bilgisinin açılır liste tıklanarak açılan sistemde tanımlı Yönetim sistemi listesinde  seçilerek ilişkilendirildiği alandır.

**Ürün:** DÖF Talebi ekranında Ürün bilgisinin ![ref114] butonu tıklanarak açılan Ürün listesinde seçilerek  bağlantısının seçilebildiği alandır.

**Ek Dosyalar:** DÖF Talebi ekranında varsa bu aşamada DÖF Talebi ile ilgili  kanıt doküman, fotoğraf gibi ek dosya yükleme işlemi butonlar yardımıyla  yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_577.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref86]: Ek dosya sisteme yüklenir.

![ref98]: Yüklenen ek dosya bilgisi görüntülenir.

![ref3]: Yüklenen ek dosya bilgisi silinir.

![ref86]  butonu tıklanarak  DÖF Talebi  aşamasında ek dosya eklenir. Birden çok ek dosya eklenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_578.png)

DÖF Talebi ekranında gerekli alanlar doldurulduktan sonra sol üst köşede yer alan  ![ref7]   butonuna tıklanarak DÖF Talebini sistem onaya gönderir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_579.png)

Onaydaki kişiye sistem mail yollarken aynı zamanda bekleyen işlerine “**Onay Bekleyen DÖF’ler listesi**” şeklinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_580.png)
#### **6.2.3.DÖF Onaylama**
**Menü Adı:** Entegre Yönetim Sistemi/ Düzeltici ve Önleyici Faaliyetler /  DÖF Onaylama

DÖF Onaylama işlemin yapıldığı menüdür.Onayda bekleyen DÖF’lerin task üzerinde (bekleyen işlerim) takip etmek istemeyen kullanıcılar Entegre Yönetim Sistemi DÖF onaylama ekranında görüntüleyebilir. Modül yöneticisi yetkisi olan kullanıcılar DÖF’lerin durumunu takip etmek için DÖF onaylama sayfasını kullanılır.DÖF Onaylama ekranında durum kısmında DÖF kaydının Açık, İptal, Gelişme, İzleme, Sonuç gibi statüleri seçilir. Bu statülerdeki bekleyen işlerimdeki iş olarak DÖF Kayıtları görev düşer. Bu ilgili görevlerdeki  aşamalarda yapılan işlem basamakları DÖF Onaylama ekranında yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_581.png)

**Ekranda bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_582.png): İlgili DÖF kaydının görüntüleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_583.png) : İlgili DÖF kaydı ile değişiklik/düzenleme/güncelleme yapılması işlemi yapılır. Eğer talepten açılan DÖF kaydı ise zorunlu alanları doldurmadan onaylama işlemi yapmamıza sistem izin vermeyecektir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_584.png) : DÖF onaylama işlemini yapılır. Onay işleminden sonra ilgili DÖF kaydı Ekip Liderinin önüne düşer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_585.png) : DÖF kaydı girilen bilgiler uygun olmadığı durumda** DÖF kaydı reddetme işlemi yapılır.Red edilen, Açan kişiye ret etme nedeniyle birlikte gönderilebilir. Ret ederken detay bilgi için ret veya kaydın iptali için ret edilebilir, buna bağlı olarak ilgili seçeneği seçmelidir.

![ref83]  : Çok fazla onaylanması gereken DÖF olması durumunda filtre seçeneğinden bilgiler süzülerek arama yapmak istendiğinde kullanılır.

![ref48]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref49]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref50]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranında kullanıcı bazlı tasarlama işlemi yapılır.

Onay Bekleyen DÖF’ler ekranında ![ref72] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_586.png)

Açılan Görüntüleme ekranında DÖF kaydı ile ilgili sekmeler tıklanarak Detay bilgileri görüntülenir. DÖF kaydının görüntüleme ekranında ![ref68] butonu tıklanılır..

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_587.png)

DÖF Kaydı ile ilgili link ekranda görüntülenir. Sağ tıkla/kopyala -yapıştır yöntemleri yada kopyala- Yapıştır kısayol tuşları (Ctrl+C-Ctrl+V) ile DÖF Kaydının görüntülenip , ilgili kişilere paylaşımı yapılır

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_588.png)

G8D raporu sekmesi tıklanarak ![ref112] (Yazdır) butonu tıklanarak G8D raporu alanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_589.png)

Tarihçe sekmesi tıklanarak DÖF kaydı ilgili yapılan işlere ait DÖF açma onayı, DÖF gelişme raporu ,DÖF Aksiyon Açma, DÖF Aksiyon Gerçekleştirme  onay geçmişi bilgileri listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_590.png)

Onay Bekleyen DÖF’ler ekranında ![ref84]  butonu tıklanarak Ret nedeni girilerek DÖF kaydı ret edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_591.png)

Açılan DÖF Ret ekranında DÖF bilgileri kontrol edilerek uygun olmadığı görüldüğünde  DÖF Ret etme işlemi yapılır ve  Ret Nedeni bilgisi yazılması zorunludur. Red edilen açan kişiye ret etme nedeniyle birlikte gönderilebilir. Ret ederken detay bilgi için ret veya kaydın iptali için ret edilebilir, buna bağlı olarak ilgili seçeneği seçmelidir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_592.png)

Onay Bekleyen DÖF’ler ekranında ![ref74]  butonu tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_593.png)

Açılan DÖF Onay ekranında  Onay notu alanında Onay notu bilgisi yazılarak ![ref78] butonu tıklanarak  DÖF kaydı onaylanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_594.png)

DÖF onaylarken onay notu bilgisi Düzeltici ve Önleyici Faaliyetler modülü parametrelerinde 154 numaralı “DÖF onaylarken onay notu girilsin?” parametresinde parametre değeri “Evet” seçilerek parametre aktif edilir. 

![ref79]


Parametre aktif edildikten sonra DÖF Onay ekranlarında Onay Notu alanı görüntülenir ve onay notu bilgisi girilerek DÖF onaylama işlemi yapılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_595.png)

DÖF onaylama işlemi gerçekleşen DÖF kaydı  eğer DÖF Gelişme Raporu  onayı için bir akış kurgulandıysa ilgili rolün onayına kurgulanmadıysa Ekip Liderine Gelişme Raporu yazılması için görev düşer.DÖF Onaylama ekranında durumu Sonuç statüsündeki  DÖF Kaydının işlem basamakları yapıldığında Sonuç aşamasında görülen butonlar görüntülenir ve bu butonlar kullanılarak işlem aşamaları yapılır. Her aşamada kullanılan butonlar DÖF kaydında olduğu gibi farklılık gösterir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_596.png)
#### **6.2.4.Raporlar**
**Menü Adı:** Entegre Yönetim Sistemi/ Düzeltici ve Önleyici Faaliyetler / Raporlar

DÖF Modülü ile ilgili raporlar görüntülendiği kısımdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_597.png)

##### **6.2.4.1.Düzeltici Faaliyetler Raporu**
**Menü Adı:** Entegre Yönetim Sistemi/ Düzeltici ve Önleyici Faaliyetler / Raporlar/  Düzeltici ve Önleyici Faaliyetler Raporu

Düzeltici Faaliyetlerin hakkında genel olarak tüm bilgilerin göründüğü ekrandır. İlgili raporda şirketten şirkete ayarlama yapılabilir.

İstenilen kolanlar çıkartılabilir veya eklenmesini istediğimiz DÖF bilgileri bu rapora yansıtılabilir. 

Düzeltici ve Önleyici Faaliyetler modülü parametrelerinde 72 numaralı “DÖF raporu şablon dosyası” parametresinde tanımlı raporu göre gelmektedir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_598.png)

Parametreye rapor formatı şablonu tanımlamak için öncelikle Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Rapor Formatları Düzenleme menüsünde ilgili rapor ilgi rapor şablonun![ref8]  butonu tıklarak yükleme işlemi yapılır. Rapor Formatları Düzenleme meüsüne yüklenen rapor formatı şablonun adı ve uzantısı sağ tıkla/kopyala yönetimi  ile birlikte ilgili parametrenin parametre değerine sağ tıkla/ yapıştır  yöntemi ile yapıştırılarak tanımlama işlemi yapılır. Düzeltici ve Önleyici Faaliyetler Raporu ekranındaki ilgili alanlar doldurularak istenen kriterler belirlenir ve ![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_599.png) (Excel Aktar) butonu ile rapor alınır. İstenirse alanlar boş bırakılarak bütün DÖF faaliyetleri ile ilgili bilgiler çekilebilir. Düzeltici ve Önleyici Faaliyetler Raporu ekranında Liste ve Filtre sekmesi olmak üzere iki sekme karşımıza çıkar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_600.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref10]: Veriler Excel’ e aktarılabilir.

![ref17]: Kayıtlar filtrelenerek arama yapılabilir.

![ref11]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref12]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref13]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Düzeltici ve Önleyici Faaliyetler Raporu ekranında Filtre sekmesinde arama kriterlerindeki alanlara  veri girişleri yapılarak ![ref17] (Ara) butonu tıklanarak filtreleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_601.png)

Düzeltici ve Önleyici Faaliyetler Raporu ekranında  liste sekmesinde listede  Filtre sekmesinde yapılan filtre ayarlarına göre istenilen verilere ait raporların görüntülenmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_602.png)

Düzeltici ve Önleyici Faaliyetler Raporu ekranında liste sekmesinde listeden DÖF kaydı seçili iken   ![ref10] (Excele aktar)  butonu tıklanarak excel formatında “  Düzeltici ve Önleyici Faaliyetler Raporu”  görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_603.png)

Düzeltici ve Önleyici Faaliyetler Raporu ekranında Gruplama özelliğini uygulayarak girid ekranında kolonların karşılığı olan alanları için mouse ile alanın üzeri tıklanarak sürüklenerek “Sütun başlığını o sütuna göre gruplamak için buraya sürükle” alana getirilerek Qdms sisteminde gridlerde gruplama özelliği yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_604.png)

Düzeltici ve Önleyici Faaliyetler Raporu ekranında ![ref50] “Kolon Seçici “ butonu tıklanılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_605.png)

Açılan alan seçicisi ekranın gridde bulunan görüntülenmesi istemendiği alanlar mouse tutup -sürekle yöntemi ile Alan seçicisi ekranı ekleyerek alanın menü ekranında görüntülenmemesi sağlar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_606.png)

İstediği şekilde alanları menü ekranların gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_607.png)

Düzeltici ve Önleyici Faaliyetler Raporu ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_608.png) butonu tıklanılır. ![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_608.png) butonu tıklandıktan sonra tekrar varsayılan ayarlarına yani menü ekranın ilk kez kullanılmaya başlandığında veya herhangi bir yapılandırma değişikliği yapılmadığında durumuna getirilmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_610.png)
##### **6.2.4.2.Düzeltici ve Önleyici Faaliyetler Aksiyon Raporu**
**Menü Adı:** Entegre Yönetim Sistemi/ Düzeltici ve Önleyici Faaliyetler /  Raporlar/ Düzeltici ve Önleyici Faaliyetler Aksiyon Raporu

DÖF’lerde yer alan aksiyonlarınların tek bir liste olarak çekmek istediğimizde kullanılan rapordur. 

Düzeltici ve Önleyici Faaliyetler modülü parametrelerinde 73 numaralı “DÖF aksiyon raporu şablon dosyası” parametresinde tanımlı raporu göre gelmektedir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_611.png)

Parametreye rapor formatı şablonu tanımlamak için öncelikle Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Rapor Formatları Düzenleme menüsünde ilgili rapor ilgi rapor şablonun![ref8]  butonu tıklarak yükleme işlemi yapılır. Rapor Formatları Düzenleme meüsüne yüklenen rapor formatı şablonun adı ve uzantısı sağ tıkla/kopyala yönetimi  ile birlikte ilgili parametrenin parametre değerine sağ tıkla/ yapıştır  yöntemi ile yapıştırılarak tanımlama işlemi yapılır. Tanımlanan rapor formatı şablonuna göre ilgili rapor bu menüden alınır

Düzeltici ve Önleyici Faaliyetler Aksiyon Raporu ekranındaki ilgili alanlar doldurularak istenen kriterler belirlenir ve ![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_612.png) (Excel aktar) butonu ile rapor alınır. İstenirse alanlar boş bırakılarak bütün DÖF aksiyonları ile ilgili bilgiler çekilebilir. Düzeltici ve Önleyici Faaliyetler Aksiyon Raporu ekranında  Liste ve Filtre sekmesi olmak üzere iki sekme karşımıza çıkar. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_613.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref10]: Veriler Excel’ e aktarılabilir.

![ref17]: Kayıtlar filtrelenerek arama yapılabilir.

![ref11]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref12]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref13]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Düzeltici ve Önleyici Faaliyetler Aksiyon Raporu ekranında Filtre sekmesinde arama kriterlerindeki alanlara  veri girişleri yapılarak ![ref17] (Ara) butonu tıklanarak filtreleme işlemi yapılır. ![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_614.png)

Düzeltici ve Önleyici Faaliyetler Aksiyon Raporu ekranında  liste sekmesinde listede  Filtre sekmesinde yapılan filtre ayarlarına göre istenilen verilere ait raporların görüntülenmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_615.png)

Düzeltici ve Önleyici Faaliyetler Aksiyon Raporu ekranında liste sekmesinde listeden DÖF kaydı seçili iken   ![ref115] (Excele aktar)  butonu tıklanarak excel formatında “ Düzeltici ve Önleyici Faaliyetler Aksiyon Raporu”  görüntülenir

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_617.png)
##### **6.2.4.3.DÖF Onay Durum Raporu**
Menü Adı: Entegre Yönetim Sistemi/ Düzeltici ve Önleyici Faaliyetler / Raporlar/ DÖF Onay Durum Raporu

DÖF akışın da farklı aşamalarda onay mekanizmaları çalışmakta, DÖF’lerin hangi onayda beklediğini görebilmek adına kullanılan rapordur. Onay tipi bölümünden DÖF Açma, DÖF Kapama, Aksiyon açma, Aksiyon Kapama  gibi hangi aşamada beklediğini görebilme işlemi yapılır. 

Düzeltici ve Önleyici Faaliyetler modülü parametrelerinde 217 numaralı “DÖF Onay durum raporu şablon dosyası” parametresinde tanımlı raporu göre gelmektedir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_618.png)

Parametreye rapor formatı şablonu tanımlamak için öncelikle Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Rapor Formatları Düzenleme menüsünde ilgili rapor ilgi rapor şablonun![ref8]  butonu tıklarak yükleme işlemi yapılır. Rapor Formatları Düzenleme meüsüne yüklenen rapor formatı şablonun adı ve uzantısı sağ tıkla/kopyala yönetimi  ile birlikte ilgili parametrenin parametre değerine sağ tıkla/ yapıştır  yöntemi ile yapıştırılarak tanımlama işlemi yapılır. Tanımlanan rapor formatı şablonuna göre ilgili rapor bu menüden alınır.

DÖF Onay Durum Raporu ekranında  Liste ve Filtre sekmesi olmak üzere iki sekme karşımıza çıkar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_619.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref10]: Veriler Excel’ e aktarılabilir.

![ref17]: Kayıtlar filtrelenerek arama yapılabilir.

![ref11]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref12]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref13]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

DÖF Onay Durum Raporu ekranında Filtre sekmesinde arama kriterlerindeki alanlara  veri girişleri yapılarak ![ref17] (Ara) butonu tıklanarak filtreleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_620.png)

DÖF Onay Durum Raporu ekranında  liste sekmesinde listeden  Filtre sekmesinde yapılan filtre ayarlarına göre istenilen verilere ait raporların görüntülenmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_621.png)

DÖF Onay Durum Raporu ekranında liste sekmesinde listesinde DÖF kaydı seçili iken   ![ref10] (Excel’e aktar)  butonu tıklanarak excel formatında “ DÖF Onay Durum Raporu”  görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_622.png)
##### **6.2.4.4.DÖF Özet Raporu**
**Menü Adı:** Entegre Yönetim Sistemi/ Düzeltici ve Önleyici Faaliyetler / Raporlar/ DÖF Özet Raporu

DÖF’lerin genel bilgilerini listeye aktardığı ve DÖF kaydı hakkında süre ile ilgili bilgileri raporunun alındığı menüdür. Düzeltici ve Önleyici Faaliyetler modülü parametrelerinde 74 numaralı “DÖF özet raporu şablon dosyası” parametresinde tanımlı raporu göre gelmektedir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_623.png)

Parametreye rapor formatı şablonu tanımlamak için öncelikle Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Rapor Formatları Düzenleme menüsünde ilgili rapor ilgi rapor şablonun![ref8]  butonu tıklarak yükleme işlemi yapılır. Rapor Formatları Düzenleme meüsüne yüklenen rapor formatı şablonun adı ve uzantısı sağ tıkla/kopyala yönetimi  ile birlikte ilgili parametrenin parametre değerine sağ tıkla/ yapıştır  yöntemi ile yapıştırılarak tanımlama işlemi yapılır. Tanımlanan rapor formatı şablonuna göre ilgili rapor bu menüden alınır.DÖF Özet Raporu ekranındaki ilgili alanlar doldurularak istenen kriterler belirlenir ve ![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_624.png) (Excel’e aktar) butonu ile rapor alınır. İstenirse alanlar boş bırakılarak bütün bilgiler, DÖF özet raporuna aktarılabilir. ![ref116] (Pdf Aktar) butonu ile Pdf formatında DÖF Özet Raporu alınır. DÖF Özet Raporu ekranında  Liste ve Filtre sekmesi olmak üzere iki sekme karşımıza çıkar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_626.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref10]: Veriler Excel’ e aktarılabilir.

![ref116]: Pdf formatında DÖF Özet Raporu alınır.

![ref17]: Kayıtlar filtrelenerek arama yapılabilir.

![ref11]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref12]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref13]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Düzeltici Ve Önleyici Faaliyetler Özet Raporu ekranında Filtre sekmesinde arama kriterlerindeki alanlara  veri girişleri yapılarak ![ref17] (Ara) butonu tıklanarak filtreleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_627.png)

Düzeltici ve Önleyici Faaliyetler Özet Raporu ekranında  liste sekmesinde listeden  Filtre sekmesinde yapılan filtre ayarlarına göre istenilen verilere ait raporların görüntülenmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_628.png)

Düzeltici ve Önleyici Faaliyetler Özet Raporu ekranında liste sekmesinde listeden  DÖF kaydı seçili iken   ![ref10] (Excele aktar)  butonu tıklanarak excel formatında “Düzeltici Ve Önleyici Faaliyetler Özet Raporu”  görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_629.png)

Düzeltici ve Önleyici Faaliyetler Özet Raporu ekranında liste sekmesinde listeden  DÖF kaydı seçili iken   ![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_630.png) (Pdf’e aktar)  butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_631.png)

Pdf formatında “Düzeltici Ve Önleyici Faaliyetler Özet Raporu”  görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_632.png)
##### **6.2.4.5.DÖF Etkinlik Değerlendirme Raporu**
**Menü Adı:** Entegre Yönetim Sistemi/ Düzeltici ve Önleyici Faaliyetler / Raporlar/ DÖF Etkinlik Değerlendirme Raporu

DÖF Etkinlik Değerlendirmesi yapılan DÖF kayıtlarının raporunun alındığı menüdür. 

Düzeltici ve Önleyici Faaliyetler modülü parametrelerinde 86 numaralı “DÖF Etkinlik Degerlendirme Raporu Şablon Dosyası” parametresinde tanımlı raporu göre gelmektedir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_633.png)

Parametreye rapor formatı şablonu tanımlamak için öncelikle Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Rapor Formatları Düzenleme menüsünde ilgili rapor ilgi rapor şablonun![ref8]  butonu tıklarak yükleme işlemi yapılır. Rapor Formatları Düzenleme meüsüne yüklenen rapor formatı şablonun adı ve uzantısı sağ tıkla/kopyala yönetimi  ile birlikte ilgili parametrenin parametre değerine sağ tıkla/ yapıştır  yöntemi ile yapıştırılarak tanımlama işlemi yapılır. Tanımlanan rapor formatı şablonuna göre ilgili rapor bu menüden alınır

Raporu ekranındaki ilgili alanlar doldurularak istenen kriterler belirlenir ve ![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_634.png) (Excel’e aktar) butonu ile rapor alınır. DÖF Etkinlik Raporunun çalışabilmesi için  öncelikle Sistem Altyapı Tanımları/DÖF/Anket Soru listeleri menüsünde tanımlanan Ankette etkinlik sorularına göre değerlendirme bilgilerini rapora aktarılır. İlgili raporda Etkinlik Degerlendirenler, 	Etkin Degerlendirme Tarihi ve  Etkinlik Puanı gibi bilgilere ulaşılır.

DÖF Etkinlik Değerlendirme Raporu ekranında Filtre sekmesinde arama kriterlerindeki alanlara  veri girişleri yapılarak ![ref17] (Ara) butonu tıklanarak filtreleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_635.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref10]: Veriler Excel’ e aktarılabilir.

![ref116]: Pdf formatında DÖF Özet Raporu alınır.

![ref17]: Kayıtlar filtrelenerek arama yapılabilir.

![ref11]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref12]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref13]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

DÖF Etkinlik Değerlendirme Raporu ekranında liste sekmesinde listeden  DÖF kaydı seçili iken   ![ref10] (Excele aktar)  butonu tıklanarak excel formatında “DÖF Etkinlik Değerlendirme Raporu”  görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_636.png)
##### **6.2.4.6.DÖF- Aksiyon Raporu (2)**
**Menü Adı**: Entegre Yönetim Sistemi/ Düzeltici Faaliyetler/ Raporlar/  DÖF-Aksiyon Raporu (2)

Koşullu filtreler kullanılarak raporlar üretilmesini sağlayan rapor formatıdır. Düzeltici Ve Önleyici Faaliyetler Aksiyon Raporu ekranında Listesi ve Filtre sekmesi olmak üzere iki sekme karşımıza çıkar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_637.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref10]: Veriler Excel’ e aktarılabilir.

![ref17]: Kayıtlar filtrelenerek arama yapılabilir.

![ref11]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref12]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref13]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Düzeltici ve Önleyici Faaliyetler Aksiyon Raporu ekranında Filtre sekmesinde arama kriterlerindeki alanlara  veri girişleri yapılarak ![ref17] (Ara) butonu tıklanarak filtreleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_638.png)

Düzeltici ve Önleyici Faaliyetler Aksiyon Raporu ekranında  liste sekmesinde listede  Filtre sekmesinde yapılan filtre ayarlarına göre istenilen verilere ait raporların görüntülenmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_639.png)

Düzeltici ve Önleyici Faaliyetler Aksiyon Raporu ekranında liste sekmesinde listeden DÖF kaydı seçili iken   ![ref10] (Excele aktar)  butonu tıklanarak excel formatında “ Düzeltici Ve Önleyici Faaliyetler Aksiyon Raporu”  görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_640.png)
##### **6.2.4.7.DÖF-Aksiyon Raporu-3**
**Menü Adı:** Entegre Yönetim Sistemi/ Düzeltici Faaliyetler/ Raporlar/ DÖF-Aksiyon Raporu-3

DÖF aksiyonların ağaç kırılımı şeklinde birbiriyle bağlantılı olarak verilen rapordur. Düzeltici ve Önleyici Faaliyetler Raporu ekranında Listesi ve Filtre sekmesi olmak üzere iki sekme karşımıza çıkar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_641.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref10]: Veriler Excel’ e aktarılabilir.

![ref17]: Kayıtlar filtrelenerek arama yapılabilir.

Düzeltici ve Önleyici Faaliyetler Aksiyon Raporu ekranında Filtre sekmesinde arama kriterlerindeki alanlara  veri girişleri yapılarak ![ref17] (Ara) butonu tıklanarak filtreleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_642.png)

Düzeltici ve Önleyici Faaliyetler Aksiyon Raporu ekranında  liste sekmesinde listede  Filtre sekmesinde yapılan filtre ayarlarına göre istenilen verilere ait raporların görüntülenmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_643.png)

Düzeltici ve Önleyici Faaliyetler Aksiyon Raporu ekranında liste sekmesinde listeden  ağaç krılım şeklinde görüntülen DÖF kayıtlarında    ![ref10] (Excele aktar)  butonu tıklanarak excel formatında “Düzeltici ve Önleyici Faaliyetler Aksiyon Raporu”  görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_644.png)
##### **6.2.4.8.DÖF Detay Raporu**
**Menü Adı:** Entegre Yönetim Sistemi/ Düzeltici ve Önleyici Faaliyetler / Raporlar/  DÖF Detay Raporu

DÖF’le ilgili bütün detay bilgilerinin yer aldığı rapordur. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_645.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref10]: Veriler Excel’ e aktarılabilir.

DÖF Detay Raporu ekranında ![ref117] (Excele aktar)  butonu tıklanarak excel formatında “DÖF Detay Raporu”  görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_647.png)
##### **6.2.4.9.DÖF İzleme Raporu**
**Menü Adı:** Entegre Yönetim Sistemi/ Düzeltici ve Önleyici Faaliyetler Raporlar/  DÖF İzleme Raporu

DÖF’lere açılan izleme bilgilerinin verildiği rapordur.DÖF İzleme raporu ekranında ilgili alanlar bilgiler girilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_648.png)

DÖF  İzleme Raporu ekranında ilgili alanlar ilgili bilgiler girildikten sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_649.png)(Excel Aktar) butonu tıklanarak DÖF İzleme Raporu Excel formatında alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_650.png)
##### **6.2.5.10. Tekrar Eden Kayıtlar Raporu** 
**Menü Adı:** Entegre Yönetim Sistemi/ Düzeltici ve Önleyici Faaliyetler /Raporlar/ Tekrar Eden Kayıtlar Raporu

Sistemde bir kullanıcı için istenen konularda tekrar eden kayıtları gösteren  menüdür.Açılan ekranda  ilk olarak Tekrar Eden Kayıtlar Raporu Şablonu menüsünden raporda çekilecek alanlar seçilerek Tekrar Eden Kayıtlar Raporu Şablonları tanımlama işlemi yapılır.Daha sonra Entegre Yönetim Sistemi/ Düzeltici ve Önleyici Faaliyetler /Raporlar/Tekrar Eden Kayıtlar raporundan ilgili rapora ulaşılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_651.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref17]: Kayıtlar filtrelenerek arama yapılabilir.

![ref10]: Veriler Excel’ e aktarılabilir.

Entegre Yönetim Sistemi/ Düzeltici ve Önleyici Faaliyetler /Raporlar/Tekrar Eden Kayıtlar raporundan Rapor Şablonu alanında ilgili rapor şablonu seçilir 

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_652.png)

Tekrar Eden Kayıtlar raporunda Rapor şablonu alanında ilgili rapor şablonu seçildikten sonra ve ![ref10](Excel Aktar) butonu tıklanarak excel formatında Tekrar Eden Kayıtlar raporu alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_653.png)
#### **6.2.5.Grafikler**
**Menü Adı:** Entegre Yönetim Sistemi/ Düzeltici ve Önleyici Faaliyetler /  Grafikler

DÖF Modülünde grafiklerin görüntülendiği kısımdır.
##### **6.2.5.1.En Çoklar Analizi**
**Menü Adı**: Entegre Yönetim Sistemi/ Düzeltici ve Önleyici Faaliyetler /  Grafikler/ En Çoklar Analizi

DÖF En Çoklar Analizi ekranında, sol taraftaki Grafik Seçeneklerinden X ve Y eksenlerinde yer alması istenen nitelikler seçilir. Veri Seçenekleri kısmından ise DÖF’ün açılma ve kapanma tarihine, işlem kaynağına, statüsüne vb. birçok kriterlere göre filtreleme yapılabilir ve sadece bu özellikteki DÖF’lerin grafikte yer alması sağlanabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_654.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref118]: Belirlenen özelliklere göre ekrana grafiği çizdirir.

![ref62] : Grafiği açılır menüden seçilen format türüne (png,jpg,bmp,xls, vb. ) dönüştürerek dış ortama aktarılma işlemi yapılır.

![ref10]: Veriler Excel’ e aktarılabilir.

Grafik oluşturmak için iki ayrı ayar alanı bulunmaktadır. Bunlar Grafik ve Veri seçenekleridir. Adından da anlaşılacağı gibi grafiğin renkleri, eni-boyu gibi ayarlamaların yapıldığı alandır. Grafik ayarlarında önemli olan X ekseni ve Y eksenidir. X ekseninden sorgulamak istediğimiz, İşlem kaynağı, Uygunsuzluk kategorisi, kök neden, süreç, durum vb. konulara göre grafik elde etmemizi sağlar. Y Ekseninden ise ilgili sorgunun sayı miktarı veya maliyetlere göre grafik alınmasını sağlanır. Veri Seçeneklerinden ise belirlediğimiz grafik ayarlarından daha kısıtlı bir veri almak için filtreleme yapmak istenirse kullanılan alandır. Bar üzerine adet bilgisi yazılsın check box işaretlendiğinde grafikte bar üzerine adet bilgiside görüntülenir.Ayarlamalar tamamlandıktan sonra ![ref118]  butonu tıklanarak grafik oluşur. Grafiği farklı formatlara almak istenirse, formatı sağdan seçtikten sonra![ref62] (Grafiği Aktar) soldan butona basıldığın da xls, png, jpg. Formatlarına grafik basılabilir. ![ref10] (Excel’e aktar) butonu ile de oluşan verileri Excel’e aktarması sağlanır. Bu veriler ile farklı formattaki grafiklerde oluşturulabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_656.png)![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_657.png)

DÖF En Çoklar Analizi ekranında![ref10] (Excel’e aktar) butonu tıklanarak DÖF En Çoklar Analizi Grafiği Excel formatında alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_658.png)
##### **6.2.5.2.DÖF Zaman Boyutlu Analiz**
**Menü Adı**: Entegre Yönetim Sistemi/ Düzeltici ve Önleyici Faaliyetler /  Grafikler/ En Çoklar Analizi

DÖF kayıtların  zaman  boyutlu   olarak grafiksel olarak görüntülendiği rapordur. DÖF kayıtları  ile ilgili seçilen verilere göre  aylık bazda grafiklerin alınma işlemi yapılır. “X ekseni” alanında seçilen değere göre, ![ref118]  butonuna tıklanarak pasta veya çubuk grafik olarak grafik raporu alınabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_659.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref118]: Belirlenen özelliklere göre ekrana grafiği çizdirir.

![ref62] : Grafiği açılır menüden seçilen format türüne (png,jpg,bmp,xls, vb. ) dönüştürerek dış ortama aktarılma işlemi yapılır.

![ref10]: Veriler Excel’ e aktarılabilir.

DÖF Zaman Boyutlu Analiz raporu ekranında, grafik seçenekleri bölümünde gerekli seçimler gerçekleştirilir. Grafik Tipi kısmında X  ve Y ekseninde  yer alması istenen nitelik seçilir. Ana Tema, renk paleti alanlarında açılır liste seçeneklerinde seçim  yapılarak Ana tema, renk paleti özelliklerinden grafik özelleştirilebilir. Grafik seçenekleri  kısmında En çok alanında grafikte olması istenen en çok aralık belirlenir. 

DÖF Zaman Boyutlu Analiz ekranında grafik  seçenekleri bölümünde gerekli seçimler gerçekleştirildikten sonra istenirse Grafik başlığı belirtilerek grafik oluşturmak için ![ref118]  butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_660.png) ![](https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_661.png)

[ref1]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_10.png
[ref2]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_11.png
[ref3]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_12.png
[ref4]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_13.png
[ref5]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_15.png
[ref6]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_16.png
[ref7]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_17.png
[ref8]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_20.png
[ref9]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_21.png
[ref10]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_22.png
[ref11]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_23.png
[ref12]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_24.png
[ref13]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_25.png
[ref14]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_28.png
[ref15]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_31.png
[ref16]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_35.png
[ref17]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_38.png
[ref18]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_40.png
[ref19]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_41.png
[ref20]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_42.png
[ref21]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_44.png
[ref22]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_51.png
[ref23]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_53.png
[ref24]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_67.png
[ref25]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_68.png
[ref26]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_69.png
[ref27]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_70.png
[ref28]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_71.png
[ref29]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_72.png
[ref30]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_73.png
[ref31]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_74.png
[ref32]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_80.png
[ref33]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_92.png
[ref34]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_94.png
[ref35]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_107.png
[ref36]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_112.png
[ref37]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_117.png
[ref38]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_119.png
[ref39]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_125.png
[ref40]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_127.png
[ref41]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_134.png
[ref42]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_139.png
[ref43]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_140.png
[ref44]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_141.png
[ref45]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_142.png
[ref46]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_143.png
[ref47]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_156.png
[ref48]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_158.png
[ref49]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_159.png
[ref50]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_160.png
[ref51]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_169.png
[ref52]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_172.png
[ref53]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_179.png
[ref54]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_183.png
[ref55]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_184.png
[ref56]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_185.png
[ref57]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_197.png
[ref58]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_200.png
[ref59]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_217.png
[ref60]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_231.png
[ref61]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_233.png
[ref62]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_241.png
[ref63]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_252.png
[ref64]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_253.png
[ref65]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_254.png
[ref66]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_266.png
[ref67]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_268.png
[ref68]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_289.png
[ref69]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_293.png
[ref70]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_299.png
[ref71]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_313.png
[ref72]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_317.png
[ref73]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_318.png
[ref74]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_319.png
[ref75]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_320.png
[ref76]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_321.png
[ref77]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_327.png
[ref78]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_331.png
[ref79]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_333.png
[ref80]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_337.png
[ref81]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_338.png
[ref82]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_339.png
[ref83]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_340.png
[ref84]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_344.png
[ref85]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_351.png
[ref86]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_357.png
[ref87]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_358.png
[ref88]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_364.png
[ref89]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_373.png
[ref90]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_375.png
[ref91]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_400.png
[ref92]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_401.png
[ref93]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_402.png
[ref94]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_403.png
[ref95]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_404.png
[ref96]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_405.png
[ref97]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_408.png
[ref98]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_411.png
[ref99]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_454.png
[ref100]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_455.png
[ref101]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_456.png
[ref102]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_457.png
[ref103]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_461.png
[ref104]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_470.png
[ref105]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_475.png
[ref106]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_486.png
[ref107]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_500.png
[ref108]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_503.png
[ref109]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_518.png
[ref110]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_520.png
[ref111]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_525.png
[ref112]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_537.png
[ref113]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_544.png
[ref114]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_576.png
[ref115]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_616.png
[ref116]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_625.png
[ref117]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_646.png
[ref118]: https://docsbimser.blob.core.windows.net/imagecontainer/c33a9f2d-e0a1-4d17-9950-82f04149079b_655.png
