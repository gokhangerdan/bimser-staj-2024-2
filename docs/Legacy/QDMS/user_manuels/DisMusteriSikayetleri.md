---
title: Dış Müşteri Şikayetleri
description: Dış Müşteri Şikayetleri Yardım Dokümanı
sidebar_position: 6
---

:::tip Bilgi

İlgili konu başlığına sağ tarafta bulunan navigasyon yardımıyla hızlı bir şekilde ulaşabilirsiniz.

:::

**Dış Müşteri Şikayetleri Modülü(v.5.26) Kullanıcı Yardım Dokümanı**

Modül Versiyonu: 5.26




## **1.GİRİŞ** 

**“QDMS Dış Müşteri Şikayetleri Modülü”**, Dış Müşteriden gelen şikayetlerin alındığı, raporlandığı ve sonuçlandırıldığı bir modüldür.

## **2.AMAÇ** 

Bu yardım kılavuzunun amacı; Dış Müşteri Şikayetlerinin akışını anlatmaktır. Sistem Altyapı Tanımları ile birlikte Entegre Yönetim Sistemleri kısmında bulunan Müşteri Şikayeti işlemleri ve talebi, çeşitli raporlamalar ve grafik alımları anlatılmıştır.

## **3.SORUMLULUKLAR** 

Tüm QDMS kullanıcıları

## **4.KISALTMALAR:**

**QDMS**: Kalite Dokümanları Yönetim Sistemi “ Quality Document Management System”

**DMS**: Dış Müşteri Şikayetleri


## **5.İŞ AKIŞI:**

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_7.png)


## **6.Dış Müşteri Şikayetleri Modülü**
Kurum dışı tüm şikayetlerin yönetimini kapsayan; şikayetleri şirket prosedürlerine uygun olarak kayıt altına alma, takip etme, raporlama, şikayetler ile ilgili alınan aksiyonların anlık olarak takip edilmesi aksiyon atanan kişileri sistem üzerinden bilgilendirme, geciken işlerde ilgililerin ve yöneticilerin bilgilendirilmesini ve raporlanmasını sağlayan modüldür.

Bu modül içeriğinde aşağıdaki özellikleri kapsamaktadır.

- Dış Müşteri şikayetinden sisteme girilmesinden,gelişme raporunun aşamasının yapılması, kök neden analizi yapılmasına, aksiyon planlanmasına ve gerçekleştirilmesine, sonuç raporun aşamasının yapılması , şikayet değerlendirmesine  ve şikayetin kapatılmasına kadar olan süreci yönetilmesi.
- Dış Müşteri şikayetleri işlemleri ile kaydı yapılan şikayetleri çözecek ekip ve ekip liderinin belirlenerek sorunun iletilebilmesi ve ek dosya eklenerek de şikayetin detaylandırılması sağlanması.
- Dış Müşteri şikayetin devam edip etmediği belli bir süre kontrolü yapılması için İzleme aşamasının yapılması ve izleme sorumlusunun atanması 
- Dış Müşteri şikayetinin açılması ve kapatılması esnasında onay akışları kurgulanması
- Dış Müşteri şikayeti kapsamında ihtiyaç olduğunda ekstra bilgiler  için Qdms üzerinde Metin, liste, tarih gibi  parametrik alan tiplerinin tanımlanarak kullanıcı bazlı modülün özelleştirilmesi işleminin yapılması
- Müşteri bazında rapor şablonu tanımlanması ve müşteriye gönderilmesi
- Dış Müşteri şikayeti incelenmesi aşamasında Kök neden analiz şablonun kullanılması
- Dış Müşteri Şikayetinde DÖF modülün kullanılması ve sürecin bir DÖF kaydı üzerinde devam edilmesinin sağlanması
- Dış Müşteri şikayetin otomatik aksiyonun  kullanılması,
- Dış Müşteri Şikayetlerinde  kullanılan otomatik aksiyon manuel veya otomatik olarak yayınlanmasının  ayarlanmasının yapılması
- Dış Müşteri Şikayetinde hata maliyetleri modülü aktif edilerek kurumdaki hataların personel ve departman bazında dağılımının görüntülenmesi 
- Sistem üzerinden şikayet kayıtları ile ilgili raporlar  ve grafiklerin alınması
- Dış Müşteri şikayetlerinde kök neden  ve neden-neden analizi özelliklerinin kullanılması
- Şikayetlerin kategorilere ayrılması ve analiz edilmesi
- Raporlar aracılığıyla şikayetlere bağlı hangi aksiyonların alındığını bu aksiyonların anlık durumlarını görüntülenmesi
- Dış Müşteri şikayeti sürecinde yorum modülün kullanılması ve şikayet kaydı aşamalarında  yorum tanımlama işlemi yapılarak yorum özelliğinin kullanılması.
- Dış Müşteri Şikayetleri  yönetim sistemi, süreç ve madde numaraları ile ilişkilendirilmesi 
- Web service desteği ile şikayetlerin sonucunun müşterilere mail ve sms ile bildirimi sağlanması.
- “En çoklar Analiz” grafiği ile hangi kategoriye, hangi departmana, hangi ürüne olan şikayetlerin dağılımın grafiği alınması ve istenen grafiği açılır menüden seçilen format türüne (Excel, jpg, pdf vb.) dönüştürerek dış ortama aktarılması sağlanması.
- “Zaman Boyutlu Analiz” grafiği ile şikayetlerin hangi zaman dilimlerinde sıklaştığı bilgisinin grafiği alınması ve istenen grafiği açılır menüden seçilen format türüne (Excel, jpg, pdf vb.) dönüştürerek dış ortama aktarılması sağlanması
### **6.1.Sistem Altyapı Tanımları/  Dış Müşteri Şikayetleri**
Dış Müşteri Şikayetleri  modülünün altyapısının oluşturularak tanımlamaların yapıldığı modül altyapısı tasarımının yapıldığı kısımdır. Entegre Yönetim Sistemi menüsünden girişlerde yapılan bu tanımlamalara göre veriler karşımıza çıkmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_8.png)

#### **6.1.1.Şikayet Kategorisi Tanımlama**
**Menü Adı:** Sistem Altyapı Tanımları /Dış Müşteri Şikayetleri/ Şikayet Kategorisi Tanımlama

Şikayet tanımlarının kategorize edildiği menüdür. Dış müşteri şikayetlerinde modülünde verimli raporlar alabilmek, problemin yaşandığı yeri görebilmek ve şirket hafızası oluşturabilmek için kategori kısmı önem arzetmektedir. Şikayet kategorileri tanımlarını gerçekleştirirken, firmanın tecrübe ettiği şikayetlerden yola çıkarak alt kırılımı gerçekleştirmek gerekir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_9.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref1]: Yeni bir değerlendirme kategorisi tanımlanır.

![ref2]:Listede seçili değerlendirme kategorisi bilgisi üzerinde düzenleme/güncelleme/değişiklik yapılır.

![ref3]: Listede seçili değerlendirme kategorisi bilgisi silinebilir.

![ref4]: Kayıtlar filtrelenerek arama yapılabilir.

![ref5]: Veriler Excel’ e aktarılır.(Şikayet Kategorisi Tanımlama ekranında liste sekmesinde bulunan Şikayet  Kategorisi Tanımlama listesinin Excel formatında raporu alınır.)

Şikayet kategorisi ekranında yeni bir şikayet kategorisi tanımlama işlemi için ekranın sol üst kösesindeki ![ref1]  butonu tıklanarak Şikayet Kategorisi Tanımlama - Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_15.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Bağlı olduğu Kategori:** Şikayet Kategorisi Tanımlama - Yeni Kayıt ekranında**  tanımlama  aşamasında** olan** şikayet kategorisi,** bir başka kategorinin alt kırılımı olarak tanımlanmak istenirse bu alan dolu olmalıdır. Dolu olarak gelen alanda bağlı olduğu şikayet kategorisi tanımının adı yazıldığı alandır. Bağlı olduğu üst kırılım silinmek istenildiğinde sağ yanda bulunan ![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_16.png)  butonu veya değiştirilmek istenildiğinde sağ yanda bulunan ![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_17.png)  butonu kullanılır. Bağlı olduğu bir üst şikayet kategorisi yok ise bu alan boş gelir.

**Şikayet Kategorisi Kodu:** Şikayet Kategorisi Tanımlama - Yeni Kayıt ekranında**  Şikayet Kategorisinin kodu bilgisinin yazıldığı alandır.

**Şikayet Kategorisi:** Şikayet Kategorisi Tanımlama - Yeni Kayıt ekranında**  Şikayet Kategorisinin tanım bilgisinin yazıldığı alandır.

**İş Yeri:** Şikayet Kategorisi Tanımlama - Yeni Kayıt ekranında**  Şikayet Kategorisinin iş yeri ile ilişkinin kurulduğu alandır. İşyeri alanında listelenen iş yerlerinde seçim yapılarak şikayet kategorinin iş yeri ilişkisi kurulur.

**Durum:** Şikayet Kategorisi Tanımlama - Yeni Kayıt ekranında durum bilgisi "Aktif" ve "Pasif" olarak ikiye ayrılmaktadır. Aktif olarak tanımlı şikayet kategorisi sistemde kullanılan şikayet kategorisini ifade etmektedir. Eğer kullanılmış bir şikayet kategorisi tanımı sistemde artık kullanılmayacaksa,  durumu bilgisi “Pasif” olarak değiştirilmelidir. Böylece hem geçmişteki mevcut kayıtlar etkilenmez, hem de yeni şikayet kategorisi seçim ekranlarında pasife alınan şikayet kategorisi görüntülenmez.

Açılan Şikayet Kategorisi Tanımlama - Yeni Kayıt ekranında** şikayet kategorisi tanımlanır ve durum kısmı “Aktif” seçilir.  Gerekli alanlar doldurulduktan sonra sonra sol üst köşede yer alan  ![ref6]   butonuna tıklanarak alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_19.png)
#### **6.1.2.Değerlendirme Kategorisi Tanımlama**
**Menü Adı**: Sistem Altyapı Tanımları/Dış Müşteri Şikayetleri/ Değerlendirme Kategorisi Tanımlama

Gelen şikayetlerin çözümler sonucundaki değerlendirme durumlarının yazıldığı menüdür. Gelen şikayetler hangi biçimde değerlendirilmeli ise, müşterinin haklı veya haksız durumuna göre ne tür cevaplar verilmeli ise, bu menüde kategorize edilerek alt yapısı oluşturulur. Haklılık veya haksızlık değerlendirme durumlarına göre alt kategorileri yapılıp detay tanımlamaları tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_20.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref1]: Yeni bir değerlendirme kategorisi tanımlanır.

![ref2]:Listede seçili değerlendirme kategorisi bilgisi üzerinde düzenleme/güncelleme/değişiklik yapılır.

![ref3]: Listede seçili değerlendirme kategorisi bilgisi silinebilir.

![ref7]: Değerlendirme kategorisinin alt kategorileri tanımlanır.

![ref4]: Kayıtlar filtrelenerek arama yapılabilir.

![ref5]: Veriler Excel’ e aktarılır.(Değerlendirme Kategorisi Tanımlama ekranında liste sekmesinde bulunan Değerlendirme  Kategorisi Tanımlama listesinin Excel formatında raporu alınır.)

![ref8]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref9]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref10]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

**Örnek:** Haklı Müşteri Şikayeti,

Değerlendirme  Kategorisi Tanımlama ekranına yeni bir değerlendirme kategorisi eklemek için ekranın sol üst köşesindeki ![ref1]  butonu tıklanarak Değerlendirme Kategorisi Tanımlama\Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_25.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Değerlendirme Kategorisi Kodu:** Değerlendirme Kategorileri-Yeni Kayıt ekranında değerlendirme kategorisinin kod bilgisinin  girildiği alandır.

**Değerlendirme Kategorisi Tanımı:** Değerlendirme Kategorileri-Yeni Kayıt ekranında değerlendirme kategorisinin tanım bilgisinin girildiği alandır.

**Durum:** Değerlendirme Kategorileri-Yeni Kayıt ekranında değerlendirme kategorisinin durum bilgisinin “Aktif” ve “Pasif “ seçeneklerinden “Aktif” olarak seçimin yapıldığı alandır.

Açılan Değerlendirme Kategorileri-Yeni Kayıt ekranında değerlendirme kategorileri kodu ve tanım bilgisi girilir. Durum kısmı “Aktif” olarak seçilir. Değerlendirme kategorileri tanımlama ekranında gerekli alanlar doldurulduktan sol üst köşede yer alan  ![ref11]  butonu tıklanarak Değerlendirme Kategorileri kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_27.png)

Bu sayfada genellikle iç müşterinin haklı ve ya haksız olma durumuna göre kategoriler yapılır. Daha sonra bir kayıt üzerinde iken ![ref7]  butonuna basılarak değerlendirme kategorisinin detaylarına inilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_28.png)

**Ekrandaki bulunan butonlar yardımıyla,**

![ref1]: Yeni bir değerlendirme kategorisinin alt kategorisi tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_29.png): Listede seçili değerlendirme kategorisinin alt kategorisi bilgisi üzerinde değişiklik/düzenleme/güncelleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_30.png): Listede seçili değerlendirme kategorisinin alt kategorisi bilgisi silinebilir.

![ref5]: Veriler Excel’ e aktarılır.

![ref8]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref9]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref10]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Değerlendirme Kategorileri Alt Kategoriler ekranına yeni bir Değerlendirme Kategorileri Alt Kategoriler eklemek için ekranın sol üst köşesindeki ![ref1]  butonu tıklanarak Değerlendirme Kategorileri Alt Kategoriler ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_31.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Değerlendirme Kategorisi Tanımı:** Değerlendirme Kategorileri Alt Kategoriler ekranında değerlendirme kategorisi tanımı bilgisinin yer aldığı alandır.

**Değerlendirme Alt Kategorisi Kodu:** Değerlendirme Kategorileri Alt Kategoriler ekranında değerlendirme alt kategorisinin kodu bilgisinin girildiği alandır.

**Değerlendirme Alt Kategorisi Tanımı:** Değerlendirme Kategorileri Alt Kategoriler ekranında değerlendirme alt kategorisinin tanım bilgisinin girildiği alandır.

**Tip:** Değerlendirme Kategorileri Alt Kategoriler ekranında değerlendirme kategorileri alt kategoriler ekranında parametrik alan tipleri bilgisinin seçilebildiği alandır. Seçilebilen parametrik alan tipler;miktar, metin, seçenek, tarih ve tutardır.

Açılan Değerlendirme Kategorileri Alt Kategoriler ekranda değerlendirme alt kategori kodu ve tanımı bilgisi girilir. Ayrıca bu tanıma bağlı ne tür bir alan çıkacağı belirtilir ( örnekte olduğu gibi  “Geri Ödeme Yapılacaktır” denilmişse alan tipi tutar olarak girilebilir) ve gerekli alanlar doldurulduktan sonra ekranın sol üstte köşede yer alan ![ref6]  butonu tıklanarak değerlendirme alt kategoriler tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_32.png)

Dış Müşteri Şikayetleri Modülü parametrelerinde  78 numaralı “Değerlendirme kullanılacak mı? (E/H)” parametresi değeri “Evet” seçilerek parametre aktif edilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_33.png)

Parametre aktif edildikten sonra Şikayet Detayı ekranında Değerlendirme sekmesi  görüntülenir ve şikayetin değerlendirme  işlemi yapılır.

Şikayet Detayında değerlendirme bilgisinin zorunlu olması içinde  Dış Müşteri Şikayetleri Modülü parametrelerinde 37 numaralı “Değerlendirme Bilgisi zorunlu olsun mu?(E/H)” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_34.png)

Parametre aktif edildikten sonra şikayet detayı ekranında değerlendirme bilgisinin  zorunlu olması sağlanır. Sistem tarafından “Değerlendirme Bilgisinin doldurulması zorunludur “ uyarısı  verilir değerlendirme bilgisi girilmeden şikayet kapatılmaz.
#### **6.1.3.E-posta Ayarları**
**Menü Adı**: Sistem Altyapı Tanımları/Dış Müşteri Şikayetleri/ E-posta Ayarları

E-Posta Ayarları ekranında, Dış Müşteri Şikayetleri Modülü süreçlerinin hangi aşamasında kimlere mail ve sms gönderimi yapılacağı belirlendiği menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_35.png)

**Ekranda bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_36.png): Listede seçili olan  E-postaları  değeri bilgisi üzerinde düzenleme/değişiklik/güncelleme işlemi yapılır.

![ref8]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref9]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref10]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

**E- Posta Ayarlarında SMS  bildirimi kullanılacak ise;** 

Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/ Parametreler menüsü tıklanılır. Açılan Parametreler ekranında listelenen Sistem Altyapı Tanımları  modülü parametrelerinde 102 numaralı “SMS bildirimi kullanıcak mı?” parametresinin parametreler ekranında Filtre sekmesinde parametre no alanına parametre numarası yazılarak ![ref12] (Ara) butonu tıklanarak aratılarak seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_38.png)

Sistem Alyapı Tanımları modülü parametrelerinde 102 numaralı “SMS bildirimi kullanıcak mı?” parametresi seçildikten sonra ![ref13] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_40.png)

Açılan parametreler ekranın parametre değeri “Evet” seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_41.png)

Parametreler ekranında parametre değeri “Evet” seçildikten sonra ekranın sol üstte yer alan ![ref11]  butonu tıklanarak parametreyi aktif etme kayıt işlemi  yapılır.

` `![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_42.png)

Parametre Aktif edildikten sonra E- Posta Ayarları ekranında SMS bildirimi kullanılması ile ilgili “SMS gitsin mi?” alanı ile ilgili check box görüntülenir.  İlgili check box işaretlenerek E-Posta ayarlarında SMS bildirimi kullanılır.

Hangi basamakta e-posta/ mesaj gitmesi isteniyorsa seçilir ve  ![ref13]  butonu tıklanılır. 

Örn: “Şikayet Açma Bildirimi “ basamağı seçilir ve ![ref13]  butonu tıklanılır.  

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_43.png)

Açılan E-Posta Ayarları/ Şikayet Açma Bildirimi ekranı görüntülenir. Roller kısmı, e-posta ve mesaj bildirimimin gideceği rolü yani kişiyi göstermektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_44.png)

E-Posta Ayarları/ Şikayet Açma Bildirimi ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_45.png)  butonu tıklanarak açılan sistemde tanımlı Mesaj Gövdesi listesinde  gönderilecek mesaj gövdesi ilgili listeden seçilir. Yanlış eklenen bir mesaj gövdesini silmek içinse ![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_46.png)  butonu kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_47.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_48.png) butonu ile Mesaj Gövdesinin içeriği detaylı bir şekilde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_49.png)

Mesaj Gövdesi listesinde seçilen Mesaj Gövdesi ![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_50.png) butonu tıklanarak seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_51.png)

Kime E-Posta gitmesi isteniyorsa, o rolle ilgili “E-Posta Gitsin Mi/ SMS Gitsin Mi” check box ‘ı işaretlenir.Mesaj gitmesi için rolde tanımlı olan kişinin cep telefon numarası personel tanımlama ekranında tanımlı olmalıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_52.png)

E-Posta Ayarları/ Şikayet Açma Bildirimi ekranında E-Posta gitmesi  rollerle  ilgili “E-Posta Gitsin Mi/ SMS Gitsin Mi” check box ‘ı işaretlendikten sonra ekranın sol üstte köşede yer alan ![ref11]  butonu tıklanarak E- Posta Ayarları kayıt işlemi gerçekleştirilir.
#### **6.1.4.Kök Neden Tanımlama**
**Menü Adı:** Sistem Altyapı Tanımları/ Dış Müşteri Şikayetleri/ Kök Neden Tanımlama

Dış Müşteri Şikayetleri Modülü kapsamında firmada kullanılan kök nedenlerin tanımlamasının yapıldığı menüdür. Neden-neden analizine göre kök nedenlerin başlıklarının tanımlanır.  Şikayet Detayı ekranında Kök Nedenler sekmesinde şikayetin kaynağının ne olduğunun tanımlandığı ve bu sekmede şikayetin asıl nedeninin seçimi yapılır. Standart olarak “İnsan, Makine, Metot, Malzeme/  Ekipman, Çevre, Yönetim” olarak belirlense de firmadan firmaya kök nedenler değişmektedir. Sektörler değiştikçe daha özel kök nedenler yazma ihtiyacı doğduğundan, firmalar kendileri için daha anlamlı seçimler yapabilmektedirler.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_53.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref14] : Yeni bir Kök neden tanımlanır.

![ref2] : Listede seçili olan Kök neden bilgisi üzerinde düzenleme/değişiklik/güncelleme işlemi yapılır.Not: Pasif özelliği ilgili kök neden tipinin artık kullanılmak istenmediğinde, uç kullanıcının görmemesi için kullanılır. Bu işlem yapıldığında eski bilgiler saklanır, fakat uç kullanıcılar pasif edilen tipi seçememektedir.

![ref15] : Listede seçili kök neden bilgisi silinebilir.Uzun süredir kullanılan bir kök neden bilgisinin silinmesi önerilmez, silindiği anda eski kayıtlarda bu tip kullanıldı ise kayıtlar bozulur.

![ref16] : Veriler excele aktarılabilir.( Kök Neden Tanımlama ekranında liste sekmesinde bulunan Kök Neden listesinin Excel formatında raporu alınır.)

Kök Neden Tanımlama ekranına yeni bir Kök Neden eklemek için ekranın sağ üst köşesindeki ![ref14]  butonu tıklanarak Kök Neden Tanımlama\Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_57.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Üst Kök Neden:** Kök Neden Tanımlama ekranında oluşturulma aşamasında** olan** Üst Kök Neden,** bir** Kök Neden** tanımının** alt kırılım olması halinde bu alan otomatik dolu gelir. Dolu olarak gelen alanda bağlı olduğu Kök Neden tanımının adı yazar. Bağlı olduğu üst kırılım silinmek istenildiğinde sağ yanda bulunan ![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_58.png)  butonu veya değiştirilmek istenildiğinde sağ yanda bulunan ![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_59.png)  butonu kullanılır. Bağlı olduğu bir üst Kök Neden yok ise bu alan boş gelir.

**Kök Neden No:** Kök Neden Tanımlama ekranında Kök Neden No’su bilgisinin girildiği alandır.

**Kök Neden:** Kök Neden Tanımlama ekranında Kök Neden Tanım bilgisinin girildiği alandır.

**Durum:** Kök Neden Tanımlama ekranında ekranında Kök Neden bilgisinin aktif veya pasif durum bilgisinin seçilebildiği alandır.

Açılan Kök Neden Tanımlama ekranında Kök Neden No ve Kök Neden tanım bilgisi girilir. Durum kısmı Aktif seçilir. Kök Neden Tanımlama ekranında gerekli alanlar doldurulduktan sonra sol üst köşede yer alan  ![ref6]   butonuna tıklanarak Kök Neden Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_60.png)
#### **6.1.5.Tekrar Eden Kayıtlar Rapor Şablonu**
**Menü Adı:** Sistem Altyapı Tanımları /Dış  Müşteri Şikayetleri/ Tekrar Eden Kayıtlar Rapor Şablonu

Şikayet kayıtlarında yer alan alanların tekrar etme durumunu göre rapor olarak  alındığı menüdür.İlk olarak Sistem Altyapı Tanımları/ Dış Müşteri Şikayetleri/Tekrar Eden Kayıtlar Raporu Şablonu menüsünden raporda gösterilecek alanlar seçilir ve rapor formatı kaydedilir.Daha sonra Entegre Yönetim Sistemi/Dış Müşteri Şikayetleri/Raporlar/Tekrar Eden Kayıtlar raporundan ilgili rapora ulaşılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_61.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref14]: Yeni Tekrar Eden Kayıtlar Şablonu tanımlanır

![ref17]: Listede seçili Tekrar Eden Kayıtlar Şablonu bilgisi güncellenir.

![ref15]: Listede seçili Tekrar Eden Kayıtlar Şablonu bilgisi silinebilir.

![ref8]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref9]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref10]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranında kullanıcı bazlı tasarlama işlemi yapılır.

Tekrar Eden Kayıtlar Raporu Şablonları ekranına yeni bir Tekrar Eden Kayıtlar Raporu Şablonları eklemek için ekranın sol üst köşesindeki ![ref14]  butonu tıklanarak Tekrar Eden Kayıtlar Raporu Şablonları \Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_63.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Tanım:** Tekrar Eden Kayıtlar Raporu Şablonları ekranında Tekrar Eden Kayıtlar Raporu Şablonları tanım bilgisinin girildiği alandır.

**Kolonlar:** Tekrar Eden Kayıtlar Raporu Şablonları ekranında kolonlar bilgisinin seçilebildiği alandır.

Açılan ekranda Tekrar Eden Kayıtlar Raporu tanım bilgisi girilir. İlgili kolonlar seçilir. Tekrar Eden Kayıtlar Raporu Şablonları ekranında gerekli alanlar doldurulduktan sonra sol üst köşedeki  ![ref6]  butonu tıklanarak Tekrar Eden Kayıtlar Raporu Şablonları kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_64.png)

Entegre Yönetim Sistemi/Dış Müşteri Şikayetleri/Raporlar/Tekrar Eden Kayıtlar raporundan ilgili rapor şablonu seçilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_65.png)
#### **6.1.6.Rapor Formatları**
**Menü Adı:** Sistem Altyapı Tanımları/Dış Müşteri Şikayetleri/ Rapor Formatları

Dış Müşteri Şikayetleri modülünde rapor formatları tanımlama işlemi yapıldığı menüdür. Bildirim Raporu, Gelişme Raporu, Sonuç Raporu, Müşteri Raporu ve  Kapatma Raporu vb. rapor formatları  için sistemde tanımlı müşterilere özgü raporların müşteri bazında farklı formatlarda çıktı alınmasının istenmesi durumunda istenirse bu menü kullanılır.Düzenlenen rapor formatları Sistem Altyapı Tanımları /BSAT/Konfigürasyon Ayarları/Rapor Formatları menüsüne yüklenir. Yüklenen rapor formatları rapor formatları düzenleme menüsünde adı ve uzantısı sağ tıkla /kopyala yöntemi  ile kopyalanarak Rapor Formatları menüsünde ilgili alanlara sağ tıkla/Yapıştır yöntemi ile yapıştırılarak tanımlanılır.Tanımlanan bu rapor formatları Dış Müşteri Şikayetleri  İşlemleri menüsünde müşteri ile ilgili şikayet seçilerek ![ref18] butonu tıklanarak ilgili rapor formatlarının raporları  alınır. Rapor formatları menüsünde  müşteri bazında farklı rapor formatları tanımlanmadığında müşteri seçilerek ilgili şikayet kaydı ile ![ref18] butonu tıklanarak rapor alındığında parametrelerde tanımlı rapor formatlarının raporu alınır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_67.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref1]:Yeni bir müşteri rapor formatı tanımlanır.

![ref2]: Listede seçili müşteri rapor formatı bilgisi güncellenir.

![ref3]: Listede seçili müşteri rapor formatı bilgisi silinebilir.

![ref8]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref9]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref10]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Bunun için öncelikle Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Rapor Formatları Düzenleme menüsüne oluşturacağımız rapor formatlarının tümü tanımlanmalıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_68.png)

**Ekranda bulanan butonlar yardımıyla;**

![ref19]: Sisteme yeni bir rapor formatı yüklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_70.png): Listede seçili olan rapor formatı görüntülenip, indirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_71.png): Listede seçili olan rapor formatı silinir.

![ref20]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref21]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref22]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Varsayılan rapor Formatlarının Düzenlemesi ekranında sisteme yeni bir rapor formatı eklemek için ![ref23]  butonuna tıklanır. Dosya Yükleme ekranında Gözat butonu tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_76.png)

İlgili rapor seçilerek Rapor Formatları Düzenleme menüsüne yükleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_77.png)

Varsayılan Rapor Formatları Düzenleme ekranında müşteri için ayrı ayrı oluşturulan bildirim, gelişme, sonuç, müşteri ve kapatma raporları yüklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_78.png)

Müşteri Rapor Formatları  menüsü tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_79.png)

Müşteri Rapor Formatı  ekranında yeni bir Müşteri Rapor formatı eklemek için ekranın sol üst köşede yer alan  ![ref14]  butonu tıklanarak Müşteri Rapor formatı \Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_80.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Müşteri:** Müşteri Rapor Formatları-Yeni Kayıt ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_81.png) butonu tıklanarak açılan sistemde tanımlı olan Müşteri listesinden müşteri bilgisinin seçildiği alandır.

**Bildirim Raporu:** Müşteri Rapor Formatları-Yeni Kayıt ekranında Bildirim Raporunun Sistem Altyapı Tanımları/BSAT/ Konfigürasyon Ayarları/ Rapor Formatları Düzenleme menüsünde adının ve uzantısının kopyalandıktan sonra yapıştırıldığı alandır.

**Gelişme Raporu:** Müşteri Rapor Formatları- Yeni Kayıt ekranında Gelişme Raporunun Sistem Altyapı Tanımları /BSAT/ Konfigürasyon Ayarları/ Rapor Formatları Düzenleme menüsünde adının ve uzantısının kopyalandıktan sonra yapıştırıldığı alandır.

**Sonuç Raporu:** Müşteri Rapor Formatları- Yeni Kayıt ekranında Sonuç Raporunun Sistem Altyapı Tanımları /BSAT/ Konfigürasyon Ayarları/ Rapor Formatları Düzenleme menüsünde adının ve uzantısının kopyalandıktan sonra yapıştırıldığı alandır.

**Müşteri Raporu**: Müşteri Rapor Formatları - Yeni Kayıt ekranında Müşteri Raporunun Sistem Altyapı Tanımları /BSAT/ Konfigürasyon Ayarları/ Rapor Formatları Düzenleme menüsünde adının ve uzantısının kopyalandıktan sonra yapıştırıldığı alandır.

**Kapatma Raporu:** Müşteri Rapor Formatları- Yeni Kayıt ekranında Kapatma Raporunun Sistem Altyapı Tanımları /BSAT/ Konfigürasyon Ayarları/ Rapor Formatları Düzenleme menüsünde adının ve uzantısının kopyalandıktan sonra yapıştırıldığı alandır.

Sistem Altyapı Tanımları /BSAT/ Konfigürasyon Ayarlar/ Rapor Formatları Düzenleme ekranda, Müşteri için ayrı ayrı oluşturulan bildirim, gelişme, sonuç, müşteri ve kapatma raporları yükleme işlemi yapılır.Müşteri listesinden müşteri seçimi yapıldıktan sonra, rapor formatlarının adı ve uzantısı ilgili alanlara sağ tıkla/kopyala-yapıştır yöntemi ile yapıştırılır. Müşteri Rapor Formatları - Yeni Kayıt ekranında gerekli alanlar ilgili bilgiler girildikten sonra ekranın sol üst köşesindeki ![ref11]  butonu tıklanarak Müşteri Rapor formatları kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_82.png)
#### **6.1.7.Otomatik Aksiyon**
**Menü Adı:** Sistem Altyapı Tanımları/Dış Müşteri Şikayetleri/ Otomatik Aksiyon

Otomatik aksiyon tanımlama işleminin gerçekleştiği menüdür. Bu menünün kullanım amacı; firmanın her müşteri şikayetinde klasikleşen/ kesinlikle aldığı bir aksiyon var ise ve bu aksiyonu belli bir rol yapıyorsa otomatik aksiyon tanıtılıp, kök nedenlerden sonra bu belirtilen aksiyonun otomatik açılması sağlamaktır. Dış Müşteri Şikayetleri  Modülü parametrelerinde 83 numaralı “Otomatik Aksiyon (0 Hiç bir zaman, 1 Kullanıcıya bağlı, 2 Her zaman)” parametre değerine göre otomatik aksiyonun tanımlanmaması, kullanıcıya bağlı olarak tanımlanması veya her zaman tanımlanması ayarı yapılır.Parametre değerine “0” değeri girildiğinde otomatik aksiyon tanımlama işlemi yapılmaz.

![ref24]

Parametre değerine”1” değeri girildiğinde Şikayet Detayı ekranında Gelişme Raporu sekmesinde “Otomatik Aksiyon Başlat” alanı ile check box görüntülenir. Kullanıcı isterse ilgili alan ilgili check box işaretleyerek otomatik aksiyon tanımlama işlemini başlatır. 

![ref25]

Parametre değeri “2” olduğunda sistemde otomatik aksiyonlar tanımlı ise otomatik olarak aksiyonları açar.

![ref26]

Otomatik Aksiyon menüsü tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_86.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref1] : Yeni bir Otomatik Aksiyon tanımlanır.

![ref27] : Listede seçili olan Otomatik Aksiyon bilgisi ilgili herhangi bir düzeltme, değişiklik veya güncelleme yapılır.

![ref3] : Listede seçili olan Otomatik Aksiyon bilgisi silinir.

![ref20]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref21]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref22]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Otomatik Açılacak Aksiyonlar ekranına yeni bir Otomatik Aksiyon eklemek için ekranın sol üst köşesindeki ![ref1]  butonu tıklanarak Otomatik Açılacak Aksiyonlar   / Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_88.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Sorumlu Kişi:** Otomatik Açılacak Aksiyonlar- Yeni Kayıt ekranında Sorumlu kişi bilgisinin sorumlu kişi alanında ![ref28] butonu tıklanarak açılan sistemde tanımlı Rol tanımları listesinden seçilebildiği alandır. Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Rol Tanımlama menüsüne Dış Müşteri Şikayetleri Modülü için tanımlı Rol tanımları listesi görüntülenir ve uygun rol seçimi yapılır. İstenirse Rol Tanımlama  menüsünde Dış Müşteri Şikayetleri Modülü için yeni bir rol tanımlaması yapılır ve seçimide yapılır.

**İşi Yapacak Kişi:** Otomatik Açılacak Aksiyonlar- Yeni Kayıt ekranında İşi Yapacak Kişi bilgisinin sorumlu kişi alanında ![ref28] butonu tıklanarak açılan sistemde tanımlı Rol tanımları listesinden seçilebildiği alandır. Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Rol Tanımlama menüsüne Dış Müşteri Şikayetleri Modülü Modülü için tanımlı Rol tanımları listesi görüntülenir ve uygun rol seçimi yapılır. İstenirse Rol Tanımlama  menüsünde Dış Müşteri Şikayetleri Modülü Modülü için yeni bir rol tanımlaması yapılır ve seçimide yapılır.

**Aksiyon:** Otomatik Açılacak Aksiyonlar - Yeni Kayıt ekranında Aksiyon tanımı bilgisi girildiği alandır.

**Süre (Gün):** Otomatik Açılacak Aksiyonlar- Yeni Kayıt ekranında Otomatik Açılacak Aksiyonun süresinin gün olarak girildiği alandır. 

Açılan Otomatik Açılacak Aksiyonlar- Yeni Kayıt ekranında  Sorumlu ve İşi yapacak kişi bilgisi sistemde tanımlı Rol tanımları listesinden seçilir. Aksiyon tanım ve süresi gün olarak bilgisi girilir.

Otomatik Açılacak Aksiyonlar- Yeni Kayıt ekranında gerekli alanlar doldurulduktan sonra sol üst köşedeki ![ref11] butonuna tıklanarak Otomatik Açılacak Aksiyonlar kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_90.png)

83 numaralı “Otomatik Aksiyon (0 Hiç bir zaman, 1 Kullanıcıya bağlı, 2 Her zaman)” parametre değeri “0” olduğunda; 

Otomatik Aksiyon Tanımlama menüsünde otomatik Aksiyon tanımlı olsa bile hiç bir zaman Şikayet Detayı tanımlandığında otomatik aksiyon açılmaz.

![ref24]

83 numaralı “Otomatik Aksiyon (0 Hiç bir zaman, 1 Kullanıcıya bağlı, 2 Her zaman)” parametre değeri “1” olduğunda;

![ref25]

Dış Müşteri Şikayetleri Modülünde gelişme raporu aşamasındaki bir Şikayet detayı seçilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_91.png)

Gelişme Raporu aşamasındaki Şikayet detayı seçildikten sonra  ![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_92.png) butonu ile içeriği görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_93.png)

Gelişme Raporu aşaması ilgili gerekli alanlar girildikten sonra ekranın sağ üst köşedeki ![ref11] butonu  tıklanarak Gelişme raporu aşaması kayıt işlemi yapılır.Sistem tarafından “286 Nolu Aksiyonlar açılmış ama yayınlanmamıştır” mesajı verilerek otomatik aksiyonun numarası verilerek aksiyonun açıldığı ama yayınlanmamıştır bilgisi verilir. Yayınlanma işlemi için 85 numaralı “Otomatik Aksiyon Yayınlama(E (Otamatik) /H (Kullanıcı Yayınlayacak)” parametresinin parametre değeri “Hayır” seçili olduğundan yayınlama işlemi ![ref29] butonu ile yapılmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_95.png)

İlgili Şikayet kaydında Kök Neden analizi yapıldıktan sonra Aksiyonlar aşamasının yapıldığı Aksiyonlar sekmesinde Otomatik Aksiyon Tanımlama menüsünde tanımlı aksiyon onay durumunda olduğu görülür.Görüntülenen Aksiyonla ilgili işlem aşamaların yapılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_96.png)

Parametre değeri “2” olduğunda sistem Otomatik Aksiyon Tanımlama menüsünde otomatik aksiyon tanımlı ise otomatik olarak aksiyonu açar. Şikayet kaydı  ekranında gelişme raporu aşaması bittikten sonra sistem tarafından Otomatik Aksiyon menüsünde tanımlı tüm aksiyonlar her zaman açılır.

![ref26]

Otomatik Aksiyonlar her zaman seçeneğine göre parametrede ayarlandığında Şikayet  kaydının ekranında gelişme raporu aşaması bittikten sonra sistem tarafında tanımlı tüm aksiyonlar otomatik olarak açılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_97.png)

Şikayet detayı Aksiyonlar sekmesinde açılan Aksiyonların durumu “Onay” statüsünde görüntülenir. Aksiyonlarda onay kurgusu tanımlandığına durumu onay statüsünde görüntülenir. Onay statüsündeki otomatik aksiyonlar onaylama işleminde sonra durumu “Açık” statüsüne gelerek gerçekleştirme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_98.png)

Dış Müşteri Şikayetleri modülü parametrelerinde 109 numaralı “Otomatik Aksiyon Yayınlama(E (Otomatik) /H (Kullanıcı Yayınlayacak) parametre değeri “Hayır” ise ![ref29] butonu görüntülenir. ![ref29] butonu tıklanarak  otomatik Aksiyonun yayınlama işleminde  kullanıcıya bağlı olarak yayınlama işlemi yapılır.Ör:

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_99.png)

Bekleyen İşlerimde “Gerçekleştirilecek Dış Müşteri Şikayeti Aksiyonları Listesi” olarak iş olarak görev düşen, Otomatik Aksiyonun görevin Şikayet- Aksiyon No  alanında Aksiyon Kodu linki tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_100.png)

Şikayet Detayı  ekranında Aksiyonlar sekmesinde durumu Açık statüsündeki otomatik Aksiyon seçili iken ![ref29] butonu görüntülenir ve bu buton tıklanarak Otomatik Aksiyonları yayınlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_101.png)

Dış Müşteri Şikayeti İşlemleri modülü parametrelerinde 85 numaralı “Otomatik Aksiyon Yayınlama(E (Otomatik) /H (Kullanıcı Yayınlayacak) parametre değeri “Evet” olduğunda ![ref29] butonu görüntülenmez sistem otomatik olarak  otomatik aksiyonların yayınlama işlemi yapar.
#### **6.1.8.Alan Tanımlama**
**Menü Adı:** Sistem Altyapı Tanımları/Dış Müşteri Şikayetleri/ Alan Tanımlama

Alan tanımlama işleminin gerçekleştiği menüdür. Alan tanımlama menüsündeki amaç; risk matrisi elemanlarının belirlenmesi bununla birlikte herhangi bir şikayetin firma üzerindeki risk büyüklüğünün ve önceliğinin hesaplanmasıdır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_102.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref1]: Yeni bir alan tanımlanır.

![ref30]: Listede seçili olan alan bilgisi üzerinde  düzeltme/ değişiklik/ güncelleme yapılır.Kod bilgisi güncellenemez.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_104.png):Listede seçili olan alan bilgisi kopyalanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_105.png): Listede seçili olan alan bilgisi silinir.  

![ref31] : Alanın değerleri tanımlanır.

![ref8]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref9]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref10]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Alan Tanımlama ekranına yeni bir alan eklemek için ekranın sol üst köşesindeki ![ref14]  butonuna tıklanarak Alan Tanımlama\ Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_107.png)![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_108.png)

**Açılan ekranda ilgili alanlar tanımlanır;**

**Alan Kodu:** Alan Tanımlama-Yeni Kayıt ekranında Alan Kodu bilgisinin girildiği zorunlu alandır. Daha önce tanımlamış alanlarla aynı olmayacak şekilde boşluk, Türkçe karakter gibi karakterler kullanmadan tanımlanmalıdır. Ör. ‘001’ , ‘RK’

**Alan Adı:** Alan Tanımlama-Yeni Kayıt ekranında Alan Adı bilgisinin girildiği alandır. 

**Başlık Notu:** Alan Tanımlama-Yeni Kayıt ekranında alanı veri girişinin yapılması ile ilgili  açıklayıcı bilgi içeren not bilgisinin girildiği alandır. Mouse ile alanın üzerine gelindiğinde görüntülenen bilgidir.

**Giriş Tipi:** Alan Tanımlama-Yeni Kayıt ekranında giriş tipinin Hesaplanan veya Veri Girişi tipi bilgisinin seçilebildiği alandır. Giriş Tipi seçeneği oluşturulan alanın manuel olarak veri girişi ile mi yoksa hesaplama yöntemi ile mi belirleneceğini gösterir. 

**Alan Tipi:** Alan Tanımlama-Yeni Kayıt ekranında alan tipinin bilgisinin seçilebildiği alandır. Alan Tipi ise oluşturulan alanın metin, nümerik, tarih, liste vb.  parametrik alan tiplerinden hangisi olduğunu gösterir. 

**Görünme Şartı:** Alan Tanımlama-Yeni Kayıt ekranında Görünme Şartı bilgisinin girildiği alandır. Bir alan eğer başka bir alanın şartına bağlı olarak görülecekse görünme şartı kullanılır. Liste tipli alanın değerlerine göre oluşturulan alanın görüntülenmesini sağlar. Kullanımı [ALANKODU]=ALAN\_DEĞERİ vb. şekildedir. (Örneğin, Fırsat var mı? Alanının  alan kodu 01; Fırsat alanının alan kodu 02 olsun. Eğer “Fırsat” Alanının, “Fırsat var mı?” Alanındaki seçeneklerden değer kodu 100 olan “Evet” değeri seçili ise görülmesi gerekiyorsa 02 numaraları “Fırsat” alanının görünme şartı bölümüne formül şu şekilde yazılmalıdır: [01]=100)

**Durum:** Alan Tanımlama-Yeni Kayıt ekranında durumun Aktif veya Pasif olarak bilgisinin seçilebildiği alandır. 

**Termin Alanı:** Alan Tanımlama-Yeni Kayıt ekranında Termin alanı aktif edilecekse ilgili check box’ı işaretlenir. Aksiyon ve DÖF’ lerin terminleri buradaki süre göz önüne alınarak belirlenir.

**Güncellemeden değer yükselmesin:** Alan Tanımlama-Yeni Kayıt ekranında “Güncellemeden değer yükselmesin” bilgisi aktif edilecekse ilgili check box’ı işaretlenir. Bu bilginin işaretli olduğu alanlarda puan değeri güncelleme sırasında mevcut değerden daha yüksek olarak girilemez.

**İlişkili Alan:** Alan Tanımlama-Yeni Kayıt ekranında İlişkili alan özelliği ile seçenek tipli iki alan arasında ilişki kurulabilmektedir. Referans alanın elemanlarının tanımlandığı ekranda ilişkili alandan hangi değerler ile ilişkili olduğu seçilebilmektedir. Böylece referans alanın form üzerinde değeri değiştiğinde ilişkili alan seçimli olarak otomatik dolabilmekte ya da seçim ekranından sadece ilişkilendirilen değerler arasından seçim yapılabilmektedir.

**İlişkili Alan Otomatik Doldurulusun:** Alan Tanımlama-Yeni Kayıt ekranında ilişkili alan otomatik doldurulsun seçeneği aktif edilecekse ilgili check box’ı  işaretlenir. Liste tipli iki alanın değerleri arasında kurulan ilişkiye göre alanlardan birinin otomatik doldurulmasını sağlar.

**Genişlik:** Alan Tanımlama-Yeni Kayıt ekranında genişlik bilgisinin girildiği alandır.

Alan Tanımlama-Yeni Kayıt ekranında ekranında gerekli alanlar doldurulduktan sonra sol üst köşede yer alan  ![ref6]   butonuna tıklanarak alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_109.png)

Olasılık alanına değer eklemek için olasılık alanı seçili iken ![ref31]  butonuna tıklanarak alanın değerlerinin tanıtılacağı ekrana gelinir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_110.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref1]:Yeni bir değer tanımlanır.

![ref17]: Listede seçili değer bilgisi üzerinde düzenleme/güncelleme/değişiklik yapılır.

![ref15]: Listede seçili değer bilgisi silinir.

![ref32]: Kayıtlar filtrelenerek arama yapılabilir.

![ref33]: Şablon indirilir.

![ref34]: Şablon yüklenilir.

![ref35]: Veriler Excel’ e aktarılabilir.

![ref20]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref21]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref22]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Not: ![ref33] ve ![ref34] butonları ile sisteme toplu olarak alan değerleri aktarılabilmektedir. ![ref33] butonu ile sistem şablonu bilgisayara indirir. İlgili şablon kullanıcılar tarafından doldurularak ![ref34] butonu ile sisteme yüklendiğinde şablondaki tüm alan değerleri sisteme aktarılmış olacaktır.

![ref1]  butonuna tıklanarak yeni değer tanımlama işlemine başlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_115.png)![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_116.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Tanım:** Değerler- Yeni Kayıt ekranında tanım bilgisi girilir.

**Açıklama:** Değerler- Yeni Kayıt ekranında Açıklama bilgisi yazılır.

**Değer:** Değerler- Yeni Kayıt ekranında değerin puan karşılığı girilir.

**Durum:** Değerler- Yeni Kayıt ekranında değerin durumu aktif veya pasif olarak seçilir.

**Varsayılan:** Değerler- Yeni Kayıt ekranında ilgili liste değerinin alanda otomatik olarak görünmesini sağlar.

Gerekli alanlar doldurulduktan sonra sol üst köşede yer alan  ![ref6]   butonuna tıklanarak değer tanımlama işlemi gerçekleştirilir. Olasılık, şiddet, frekans vb. puanlı liste, liste, arama özellikli liste tipli alanların değer tanımlama işlemleri bu şekilde yapılır. Alan özelliklerine göre bu ekranda değişiklikler olabilmektedir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_117.png)

Olasılık alanı ilgili tüm değerlerin tanımlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_118.png)

Olasılık puanlı liste tipinde olduğu gibi butonlar kullanılarak aynı şekilde Şiddet puanlı liste tipli alanı tanımlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_119.png)

Olasılık puanlı liste tipinde olduğu gibi butonlar kullanılarak aynı şekilde Şiddet puanlı liste alanın tüm değerlerinin tanımlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_120.png)

Giriş tipi olarak veri girişi seçilen alanların tanımlanması yukarıdaki gibi gerçekleştirilir. Giriş tipleri hesaplanan (Risk Büyüklüğü gibi) olacak alanlar ise formülleri ile birlikte tanımlanır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_121.png)

Risk Büyüklüğü alanın tanımlama işlemi için ![ref14] butonu tıklanarak Alan Tanımlama-Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_122.png)![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_123.png)

**Açılan ekranda ilgili alanlar tanımlanır;**

**Alan Kodu:** Alan Tanımlama-Yeni Kayıt ekranında Alan Kodu bilgisinin girildiği zorunlu alandır. Daha önce tanımlamış alanlarla aynı olmayacak şekilde boşluk, Türkçe karakter gibi karakterler kullanmadan tanımlanmalıdır. Ör. ‘001’ , ‘RK’

**Alan Adı:** Alan Tanımlama-Yeni Kayıt ekranında Alan Adı bilgisinin girildiği alandır. 

**Başlık Notu:** Alan Tanımlama-Yeni Kayıt ekranında alanı veri girişinin yapılması ile ilgili  açıklayıcı bilgi içeren not bilgisinin girildiği alandır. Mouse ile alanın üzerine gelindiğinde görüntülenen bilgidir.

**Giriş Tipi:** Alan Tanımlama-Yeni Kayıt ekranında giriş tipinin Hesaplanan veya Veri Girişi tipi bilgisinin seçilebildiği alandır. Giriş Tipi seçeneği oluşturulan alanın manuel olarak veri girişi ile mi yoksa hesaplama yöntemi ile mi belirleneceğini gösterir. Giriş Tipi seçeneği Hesaplanan olarak seçilir.

**Formül Tipi :** Alan Tanımlama-Yeni Kayıt ekranında alanda kullanılacak formül tipi seçeneğinin Excel veya SQL olarak seçildiği alandır. SQL formül tipi seçeneğinde kullanıcak formül için Bimser Destek Ekibinde yardım almak gerekir.Formül Tipi Excel seçeneği olarak seçilir.

**Formül:** Alan Tanımlama-Yeni Kayıt ekranında seçilen formül tipine göre yazılacak formül bilgisinin girildiği alandır. Excel formül tipi seçeneği seçildiği için ilgili alana Excel Formülü yazılır.

**Alan Tipi:** Alan Tanımlama-Yeni Kayıt ekranında alan tipi seçeneklerinde seçim yapıldığı alandır. Alan tipleri Metin, Nümerik ve Liste parametrik alan tipli seçeneklerdir.Genelde formül için Nümerik alan tipi seçilir. 

**Görünme Şartı:** Alan Tanımlama-Yeni Kayıt ekranında Görünme Şartı bilgisinin girildiği alandır. Bir alan eğer başka bir alanın şartına bağlı olarak görüntülünecekse görünme şartı kullanılır. Liste tipli alanın değerlerine göre oluşturulan alanın görüntülenmesini sağlar. Kullanımı [ALANKODU]=ALAN\_DEĞERİ vb. şekildedir. (Örneğin, Fırsat var mı? Alanının  alan kodu 01; Fırsat alanının alan kodu 02 olsun. Eğer “Fırsat” Alanının, “Fırsat var mı?” Alanındaki seçeneklerden değer kodu 100 olan “Evet” değeri seçili ise görülmesi gerekiyorsa 02 numaraları “Fırsat” alanının görünme şartı bölümüne formül şu şekilde yazılmalıdır: [01]=100)

**Durum:** Alan Tanımlama-Yeni Kayıt ekranında durumun Aktif veya Pasif olarak bilgisinin seçilebildiği alandır. 

**Trend:** Alan Tanımlama-Yeni Kayıt ekranında  tanımlanan riskin trend olarak gösterimi yapılacak ilgili alanla ilgili check box’ın işaretlendiği alandır.

Alan Tanımlama-Yeni Kayıt ekranında ekranında gerekli alanlar doldurulduktan sonra sol üst köşede yer alan  ![ref6]   butonuna tıklanarak alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_124.png)

Formül girişleri ilgili alanların tanımlama ekranlarında gerçekleştirilir. Örnek olarak bir formül aşağıdaki gibi analiz edilebilir.Risk Büyüklüğü ile ilgili formülde  [01]\*[02]+[01]/[02] şeklinde yazılan bir alanda köşeli parantez içinde yazılan ifade alan kodlarını temsil etmektedir. Bu ifadeler alan tanımlama ekranında alanları tanımlarken kullanıcı tarafından belirlenir. Olasılık alanı için, 01; Şiddet alanı için,  02 olarak kodlama yapılmış formül, ([[01]\*[02]+[01]/[02] şeklinde olacaktı. Bu formülün sonucu olarak Risk Büyüklüğü  Alanı, Olasılık ve Şiddet alanında seçilen değerlerin çarpımı alınarak ,Olasılık ve Şiddet alanın bölümü alınarak sonuçlarının toplamı olmak  üzere sistem tarafından otomatik olarak hesaplanacaktır. 

**Sistemde mevcut bulunan alan tiplerinin tam listesi aşağıda belirtilmiştir**;

**Metin:** Metin kutucuğu ekler.

**Metin Çok Satırlı:** Çok satırlı metin kutucuğu ekler.

**Nümerik-Parasal:** Parasal değer olarak nümerik giriş yaptırır.

**Nümerik-Biri**m**:** Birim olarak nümerik giriş yaptırır.

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

**Ürün Grubu**: QDMS Ürün Grubu veri tabanından ürün grubu bilgisinin seçilebilmesini sağlar.

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
#### **6.1.9.Fonksiyon Dizayner**
**Menü Adı:** Sistem Altyapı Tanımları/ Dış Müşteri Şikayetleri/  Fonksiyon Dizayner

İç Müşteri Şikayetleri Modülünde tanımlanan alanları Risk matrisine bağlama işleminin gerçekleştiği menüdür. İç Müşteri Şikayetleri  modülü parametrelerinde 103 numaralı “Risk Matrisi Kullanılacak mı?” parametresi parametre değeri “Evet” seçilerek parametre aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_125.png)

Parametre aktif edildikten sonra Şikayet Detayı ekranında Risk matrisi sekmesinde ilgili alanların görüntülenip ve bu alanları veri girişleri yapılarak herhangi bir şikayetin  firma üzerindeki risk büyüklüğünü hesaplanması sağlanır.Bunu yapmak için Sistem Altyapı Tanımları/ Dış Müşteri Şikayetleri/ Fonksiyon Dizayner Menüsüne gelinir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_126.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref36]: Alanları fonksiyonlarla ilişkilendirilir.

![ref8]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref9]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref10]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranında kullanıcı bazlı tasarlama işlemi yapılır.

Fonksiyon Dizayn ekranında ![ref36]  butonu tıklanılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_128.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref1]: Listede seçili fonksiyona yeni bir alan eklenir.

![ref30]:Listede seçili eklenen fonksiyona eklenen alan bilgisi üzerinde değişiklik/düzenleme/güncelleme işlemi yapılır.

![ref3]: Listede seçili eklenen fonksiyona eklenen alan bilgisi silinir.

Açılan Fonksiyon Dizayn - Alanlar – Risk Matrisi  ekranda seçili olan fonksiyonda kullanılacak alanlar  ![ref1]  butonuna tıklanarak belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_129.png) ![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_130.png)

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

Alan Tanımlama - Fonksiyonlar - Yeni Kayıt ekranında gerekli tüm alanlar doldurulduktan sonra ekranın sol üst köşesindeki ![ref6]  butonuna tıklanarak alanın risk matrisine bağlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_131.png)

Alan havuzuna eklenen alanları tümü aynı şekilde Alan Tanımlama - Fonksiyonlar - Yeni Kayıt ekranında  Risk matrisine bağlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_132.png)

Bu şekilde Şikayet Detayı ekranında Risk Matrisi sekmesinde hangi alanların yer alacağı belirlenmiş olur. Risk matrisinin çalışması için, Dış Müşteri Şikayetleri Modülü parametrelerinde 103 numaralı “Risk Matrisi Kullanılacak mı?”  parametrenin aktif edilmesi gerekir. Parametre aktif edildiğinde Şikayet Detayı ekranında Risk Matrisi sekmesi görüntülenir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_133.png)

Risk matrisi sekmesinde ilgili alanların görüntülenip ve bu alanları veri girişleri yapılarak herhangi bir Şikayetin firma üzerindeki risk büyüklüğünü hesaplanması sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_134.png)
#### **6.1.10.Dış Müşteri Şikayetleri Parametreleri**
**Menü Adı:** Sistem Altyapı Tanımları/ Dış Müşteri Şikayetleri/ Dış Müşteri Şikayetleri Parametreleri

Dış Müşteri Şikayetleri Modülü için kullanıcının istek ve ihtiyaçlarına göre çeşitli ayarlamaların yapabildiği ve bunlara göre parametreleri belirlendiği (seçilebildiği) menüdür. Sistemde bu menüde yapılan ayarlamalar sadece Dış Müşteri Şikayetleri modülünün içeriğini kapsar. Parametrelerde yapılan değişikler tüm Qdms kullanıcılarını kapsamaktadır.Parametreler ekranında Liste ve Filtre sekmesi olmak üzere iki sekme karşımıza çıkar. Liste sekmesinde Dış Müşteri Şikayetleri ile ilgi tüm parametreler listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_135.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref30]: Listede seçili olan parametre bilgisi üzerinde düzenleme/değişiklik/güncelleme işlemi yapılır.

![ref4]: Kayıtlar filtrelenerek arama yapılır.

![ref5]: Veriler Excel’ e aktarılır.( Parametreler ekranında liste sekmesinde bulunan İç Müşteri Şikayetleri Modülü parametrelerin listesinin Excel formatında raporu alınır.)

![ref8]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref9]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref10]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Parametreler  ekranında Filtre sekmesinde, Parametre No ve Parametre Tanımı gibi alanlara veri        girilip,  ![ref4] (Ara) butonu tıklanarak arama kriterlerine göre filtreleme işlemleri yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_136.png)

Dış Müşteri Şikayetleri Modülü parametrelerinde 5 numaralı “Sonuç Raporu Hazırlama Süresi” parametresi parametreler ekranında Filtre sekmesinde parametre no alanına numarası yazılarak ![ref12] (Ara) butonu tıklanarak aratılarak seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_137.png)

Arama işlemi için Parametreler ekranında liste sekmesinde gridde kolonların karşılığındaki alanlarda kullanılır. Parametre numarası bilinmiyorsa parametre liste sekmesinde gridde Tanım alanında  parametre içerisinde geçen anahtar bir kelime yazılarak aratılma işlemi de yapılabilir. Yada parametre numarası biliyorsa gridde parametre No alanınada parametre numarası yazılırak parametrenin aratılma işlemide yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_138.png)

Parametre seçildiktende sonra ![ref30] butonu tıklanılır.Açılan parametreler ekranında parametre değerinin değiştirilmek istenilen yeni değer bilgisi girilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_139.png)

Parametreler ekranında parametre değerine girilen yeni değer bilgisinden sonra ekranın sol üst köşede yer alan ![ref11]  butonu tıklanarak parametre kayıt güncelleme işlemi yapılır.Yeni girilen parametre değerine göre Aksiyonlar gerçekleştirildikten sonra sonuç raporunun kaç gün içerisinde hazırlanacağını maksimum 10  gün  olarak  sistemsel ayarı işlemi yapılır.

Dış Müşteri Şikayetleri modülü parametrelerinde 13 numaralı “Açanın departman sorumlusu bilgilendirmeye eklensin(E/H)?” parametresi parametreler ekranında Filtre sekmesinde parametre no alanına parametre numarası yazılarak ![ref37] (Ara) butonu tıklanarak aratılarak seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_141.png)

Parametre seçildiktende sonra ![ref38] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_143.png)

Açılan parametreler ekranında parametre değeri seçeneklerinde  “Evet” ilgili check box seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_144.png)

Parametreler ekranında parametre değeri “Evet” seçildikten sonra ekranın sol üst köşesinde yer alan ![ref11]  butonu tıklanarak parametre aktif etme kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_145.png)

Dış  Müşteri Şikayetleri modülünde Şikayet  Kategorisi ile ilgili parametrelerinde liste sekmesinde listelenmesi için Filtre sekmesinde veya gridde Parametre Tanım alanına “Şikayet  Kategorisi” ilgili anahtar kelimeler yazılarak ![ref12] (Ara) butonu tıklanılır.  

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_146.png)

Şikayet Kategorisinin tanımın içeriğinde geçtiği ve Şikayet Kategorisi ilgili parametrelerin listelenmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_147.png)

Bu şekilde parametreler ekranında filtre sekmesi arama kriterleri olan alanlar ve liste sekmesinde griddeki alanlar kullanılarak  ilgili parametrenin aratılma işlemi yapılarak,  ![ref30] butonu tıklanarak içeriği görüntülenen parametreyi aktif etme, aktif edilen parametreyi pasif etme veya parametrenin değerini değiştirme gibi işlemler yapılır. 

#### **6.1.11.Anket Soru Listeleri(Dış Müşteri Şikayeti İşlemleri)**
**Menü Adı:** Sistem Altyapı Tanımları/ Dış  Müşteri Şikayeti İşlemleri / Anket Soru Listeleri(Dış Müşteri Şikayeti İşlemleri)

Dış Müşteri Şikayetleri Modülü için Anket Soru listelerin ilgili fonksiyonlar için hazırlandığı menüdür. Anket Soru Listeleri (Dış Müşteri Şikayeti İşlemleri) menüsünde  anket görevi parametrelere bağlı olarak Ajan uygulamasıyla birlikte oluşmaktadır.Şikayeti Kapatma aşamasında “Değerlendirme kullanılacak mı?” check box ile işaretlenip, İç Müşteri Şikayeti modülü  ile ilgili  kayıt kapandıktan minimum 1 gün sonra bu anketler “Bekleyen işlerime” Anket İşlemleri Modülünde” “Doldurulması Gereken Anketler” işi olarak görev düşer. Bu görevin düşmesi için ajan programında ilgili fonksiyonun sunucudan çalıştırılması işlemi mutlaka yapılması gerekmektedir.İlgili görevdeki anket kodu alanında link tıklanarak Anket doldurma işlemi yapılır.

Anket işlemleri Modülü olmayan kullanıcıların Anket işlemleri modülünde açılan Anket şablonu ekranında olduğu gibi bu modülde ilgili fonksiyon için Anket şablonu tasarlaması amacıyla kullanılmaktadır. Bu fonksiyon  “Şikayet Değerlendirme”  fonksiyonudur. Anket Soru Listeleri(Dış Müşteri Şikayeti İşlemleri) ekranında fonksiyon olarak “Şikayet Değerlendirme”  fonksiyonu seçildiğinde sol üstteki ![ref39] butonu tıklanarak Tedarikçi Değerlendirme modülü mantığında sistemde şablon anketler bu menüde tasarlanıp kaydedilmesi sağlanmaktadır. Şablon anketler tasarlandıktan sonra Dış Müşteri Şikayeti modülün 1. fonksiyonla ilgili parametresi olan 121 numaralı “Değerlendirme Anket Kodu”parametresinin  parametre değeri  boş ise sistem otomatik olarak tanımlanan anket kodunu parametre değerine  tanımlamaktadır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_149.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref39]: Tanımlanacak ankete soru ekleme işlemi yapılır.

![ref20]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref21]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref22]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

![ref39]  butonu tıklanarak  Anket Modülün yapısındaki soru ekleme işlemin yapıldı ekran gibi Dış Müşteri Şikayetleri modülü için ilgili fonksiyon için soru ekleme ekranı görüntülenerek soru seçeneklerinden soru ekleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_151.png)

Dış Müşteri Şikayetleri parametrelerinden 121 numaralı “Değerlendirme Anket Kodu” parametresinin parametre değerine herhangi bir parametre kodu tanımlı olmadığında sistem “Yeni bir anket oluşturulacaktır. Onaylıyor musunuz?”  uyarı mesajına “Tamam” butonu tıklanarak anket soruları ekranı görüntülenir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_152.png) **Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_153.png): Sorularınızı yazdırmaya sağlayan butondur.

![ref40]: Anketi bölümlendirerek başlık eklemek istenilirse bu buton kullanılır. Her başlık ayıracından sonra tanımlanan sorunun numarası 1 olarak gelir. 

![ref41] : Anketi dolduran kişilere, serbest bilgi girilmesi gereken sorular sorulduğunda, kullanılan soru tipidir. 

![ref42]: Verilen cevapların belirtilen seçenekler içinden seçilmesi durumunda kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_157.png):Bir sorunun seçeneklerinden tüm seçeneklerin tercih edilip, öncelik sırasına göre listelendiği durumda kullanılır. Seçenekler çoktan aza veya azdan çoğa doğru sıralanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_158.png): Oluşturmak istenilen soruda çok fazla şık mevcutsa ve bunların check list gibi seçilmesi gerekiyor ise, çoklu seçim listesi tipinde soru eklenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_159.png):Sorulan sorunun açılır listeden tek cevap seçilmesi durumunda kullanılacak soru tipidir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_160.png):Bu soru tipi Qdms’de tanımlı personel, müşteri, departman, şirket profili ve ürün alanlarındaki listelerin seçilmesini sağlar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_161.png): Soru metni altında alt soruların tanımlama işlemi yapıldığı matris şeklinde oluşturulan soru tipidir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_162.png):Soru metni alanında resim eklendiği ve seçeklerinde resim ekleme işlemi yapıldığı resimli matris şeklindeki soru tipidir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_163.png): Tıklanarak açılan ekranda, kullanıcıya tarih seçtirilecek soru eklenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_164.png):Ankete Ek dosya ekleme işlemi için Ek Dosya alanı oluşturur.** 

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_165.png):Anket İşlemler modülü alt yapısında bulunan Soru Havuzu menüsünde açılan Soru Kategorileri ekranında tanımlı soru kategorileri listesinde seçim yapıldığı soru tipidir.

**Örnek Soru seçenekleri ekleme;**

![ref40] butonu tıklanarak Anket bölümlendirilerek başlık eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_166.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_167.png)

Başlık ekle alanına ilgili başlık eklenerek ![ref43] butonuyla kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_169.png)

![ref41] butonu tıklanarak serbest bilgi girilmesi için tanımlanacak soru tanımlanır. Bir Metin alanı oluşturulur ve bu metin alanın kaç satırdan oluşacağında soru tanımlama ekranında ayarlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_170.png)

**Açılan ekranda ilgili alanlar tanımlanır;**

**Soru Metni:** Sorulacak soru metni, Türkçe alana yazılır. Diğer dillerde kullanım olması durumunda ilgili dillerin olduğu alana sorulacak soru verisi girilir.

**Satır Sayısı:** Satır sayısı, metnin büyüklüğünü belirlemek için kullanılır. 0 veya 1 olması durumunda cevap verilecek alan tek satır olarak görülür.

Sorulacak sorunun cevap verme zorunluluğu bu alandan belirlenir. Cevap zorunluluğu var ise soru cevaplanmadığında kaydetmeye izin verilmez, uyarı mesajı verilir.

**İlişkili Soru/Seçenek:** Bir sorunun, seçeneklerinden biri ile ilişki kurulduğunda, ilişkili sorunun çıkması istenilirse ilişkili soru/seçenek kısmından bağlantı sağlanır.

Sorulacak soru metni Türkçe alana yazılarak ![ref44]  butonuyla kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_172.png)

![ref42]   butonu tıklanarak verilen cevapların beliritilen seçeneklerden seçilme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_173.png)![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_174.png)** 

**Açılan ekranda ilgili alanlar tanımlanır;**

**Soru Metni:** Sorulacak soru metni, Türkçe alana yazılır. Diğer dillerde kullanım olması durumunda ilgili dillerin olduğu alana sorulacak soru verisi girilir.

**Seçenek/Puan:** Bu alana sorunun seçenekleri girilir. Eğer anket, puanlı bir anket olacaksa, girilen seçenekler için puan da yazılmalıdır.

Sorulacak sorunun cevap verme zorunluluğu bu alandan belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_175.png)

Seçeneklerden 1 veya 1’den fazlasının seçilebilmesi bu alandaki check box’a göre belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_176.png)

Seçeneklerin yan yana (Tek Satırlı) veya alt altta (Çok Satırlı) dizili olarak görülmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_177.png)

Eğer çok satırlı seçeneği işaretlenirse kolon sayısı diye bir alan çıkar ve sorunun seçenekleri belirlenen değer kadar, kolonda görüntülenir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_178.png)

**Min/Max Seçim Sayısı :** Minimum ve maxsimum soru seçim sayısının belirlendiği alandır.(Birden Fazla seçenek seçilebilir seçeneği işaretli olduğunda bu alan görüntülenir)

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_179.png)

**Hesaplama Yöntemi:** Anketin puanlı anket olması durumunda,  bu sorunun seçeneklerine verilen puanların hangi yöntemle hesaplanılacağının belirlendiği alandır. Örneğin; 10 kişinin cevaplayacağı anketteki bir sorunun 4 seçeneği ve her bir seçeneğin kendine has puanları vardır. İlk seçeneğin puanının 5 olduğunu varsayarsak, 10 kullanıcının ilk seçeneği seçmesi halinde, bu puanlar toplanarak mı (50) veya ortalaması alınarak mı (5) anketin ortalama puanına dahil edilme durumu belirlenir.(Birden Fazla seçenek seçilebilir seçeneği işaretli olduğunda bu alan görüntülenir)

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_180.png)

**Ağırlıklı Puan:** Anketin puanlı anket olması durumunda sorunun anket içindeki ağırlığının belirlendiği alandır. Tüm sorular eş değer ağırlıktaysa 1 değeri yazılmalıdır. 0 olarak yazıldığı durumda anket puanı hesaplanmaz.

**İlişkili Soru/ Seçenek:** Bir sorunun başka bir sorunun seçeneğindeki şarta bağlı olarak görünmesi istenirse ilişkili soru/seçenek mantığı kullanılır.

İlgili alanlar doldurulduktan sonra ![ref44]  butonu tıklanarak kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_181.png)

Anket Soru Listeleri(Dış Müşteri Şikayetleri) menüsünde İlgili fonksiyon seçili iken ![ref39] butonu tıklanarak açılan Anket soruları ekranında örnek olarak birkaç soru seçeneği tanımlanarak Anket Soru Listeleri(Dış Müşteri Şikayetleri) tanımlama işlemi yapılır. Diğer soru seçeneklerin tanımlama işlemi Anket İşlemleri Modülünün soru tanımlama ekranındaki aynı şekilde yapılmaktadır. Açılan ekranda Anket İşlemleri soru tanımlama ekranı ile aynıdır. Soru tanımlama işlemi yapıldıktan sonra Anket Soru Listeleri(Dış Müşteri Şikayetleri) menüsü ilgili modülün ilgili parametresi olan 121 numaralı “Değerlendirme Anket Kodu” parametresine sistem otomatik olarak anket kodu tanımlar. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_182.png)

Anket Soru Listeleri (Dış Müşteri Şikayetleri) menüsünde ![ref39] butonu tıklanarak açılan Anket soruları ekranında anket soru tanımlama işlemi yapıldıktan sonra  Şikayet kapatma aşamasındaki bir Şikayet Detayı kaydının tıklanarak açılır. Açılan Şikayet Detayı kapatma sekmesinde “Değerlendirme anketi kullanılacak mı?” alanı ile  ilgili check box işaretlenir.“ Değerlendirme anketi kullanılacak mı?” alanı ile ilgili check box işaretlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_183.png)

Dış  Müşteri Şikayetleri Modülü parametrelerinde 122 numaralı “Şikayet kaç gün sonra değerlendirilecek” parametresindeki parametre değerine girilen değere baz alınarak şikayetin kapatılmasından ajan programının ilgili fonksiyonu çalıştırılarak ilgili görevin parametrede tanımlı rolün bekleyen işlerine  Anket işlemleri modülünde “Doldurulması Gereken Anketler” olarak görev olarak düşmesi sağlanır.

Dış  Müşteri Şikayetleri Modülü parametrelerinde 123 numaralı “Değerlendirmede kullanılacak rol” parametresinde  tanımlı rolün bekleyen işlere  “Doldurulması Gereken Anketler” görevi olarak iş düşer. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_184.png)

123 numaralı parametreye Dış Müşteri Şikayetleri Modülünde Rol Tanımlamada tanımlı rol kodu tanımlanmalıdır.Rol Kodu bilgisi Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Rol Tanımlama menüsünde alınır.

122 numaralı parametrede de parametre değeri “1” olduğuna göre ajanın programın şikayetin kapatılmasından sonra çalıştırılması için 1 gün olarak baz alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_185.png)

Anket görevi düştükten parametrede tanımlı ilgili rolün bekleyen işlere  düştükten sonra anketin değerlendirme geçerlik süresinde 124 numaralı parametreye tanımlı olması gerekmektedir. Bu parametredeki parametre değerindeki günü  göre anketin geçerlik süresi belirlenir.Anket bu sürede bekleyen işlerde görev olarak kalır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_186.png)

#### **6.1.12.Dashboard/Dış Müşteri Şikayetleri** 
Menü Adı: Dashboard/Dış Müşteri Şikayetleri/Dış Müşteri Şikayetleri  Dashboard

Qdms sisteminde  kullanıcılara işlemleri, metrikleri, grafikleri ve raporları tek bir ekranda görüntülemelerine olanak sağlayan kısımdır. Dashboard, bilgi akışını ve/veya içeriğini özetlemek amacıyla kullanılan, grafikler ve tablolar yoluyla belirli bir durumu açıklamaya yarayan göstergeler ekranı, iş panosu ve  görtergeler tablosu olarak ifade edilmektedir. Amacı en kısa sürede, en az etkileşim ve düşünme gereksinimi ile gerekli olan bilginin sunulmasıdır.Genelde yönetici konumundaki kişileri sıklıkla kullandıkları ekrandır. Qdms sisteminde Dış Müşteri Şikayetleri  Modülü kapsamında Dashboard özelliği getirilmiştir. Menü görme yetkisine bağlı olarak bu ekran gelmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_187.png)

Dashboard menüsü tıklanıldığında liste ve filtre sekmesi olmak üzere iki sekme karşımıza çıkmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_188.png)

Filtre sekmesinde arama kriterlerine bulunan alanlara göre filtreleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_189.png)

Dış Müşteri Şikayetleri modülünde Dış Müşteri Şikayetleri  Dashboard ekranında Liste sekmesinde Toplam Dış Müşteri Şikayeti , Açık Dış Müşteri Şikayetleri, Kapalı Dış Müşteri Şikayetleri, Gecikmeli Kapanan Dış Müşteri Şikayetler ve  Zamanında Kapanan Dış Müşteri Şikayetleri alanları sabit alanlar olarak ekrana gelerek üzerinde herhangi bir düzenleme işlem yapılmamaktadır.Bu sabit alanlarda toplam ve yüzdelik dilimleri ile bilgileri verilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_190.png)

Dış Müşteri Şikayetleri Dashboard ekranında ilk açılışta 6 tane varsayılan grafik görüntülenir.Modül Yöneticileri istedikdikleri takdirde  grafik sayısı artırabilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_191.png)

Dış Müşteri Şikayetleri Dashboard ekranında kaç tane grafik olacağı, grafiğin adının ne olacağı, grafiklerin sırasını ne olacağı Z ekseninde, Y ekseninde hangi alanlar olacağı, grafik boyu, grafik eninin ne olacağı ve grafik tipinin ne olacağı gibi ayarlarmalarla grafik tasarlama işlemini yapılır. Bu ayarlamalarının Dış Müşteri Şikayetleri Dashboard ekranında yapılması için kullanıcının Dış Müşteri Şikayetleri Modülünde Modül Yönetici olarak tanımlı olması gerekir. (Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Yönetici Tanımlama  menüsünde Dış Müşteri Şikayetleri Modülünde modül yönetici tanımlama işlemi yapılır.)

Kullanıcı Dış Müşteri Şikayetleri Modülünde Modül Yönetici  olmadığında Dış Müşteri Şikayetleri Dashboard ekranında  aşağıdaki ekran görüntüsündeki buton görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_192.png)

Dış Müşteri Şikayetleri Modülünde modül Yönetici olarak tanımlı olan kullanıcının Dış Müşteri Şikayetleri Dashboard ekranında  birinci buton olan ![ref45]  butonu görüntülenir. Modül Admini olan kullanıcı Dış Müşteri Şikayetleri Dashboard ekranında gerekli  ayarlamaları ![ref45]  butonu yardımıyla grafik tasarlama işlemide yapar.Modül Yöneticileri olmayan kullanıcılar ise Dashboard Konfigürasyonu ekranında Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/ Dashboard Konfigürasyonu/ Dış Müşteri Şikayetleri menüsünde gerekli ayarlamalar yapılarak grafik tasarım işlemide yapabilirler.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_194.png)

Dış Müşteri Şikayetleri Modülünde grafik tasarlama, listede seçili tasarlanmış grafik  bilgileri güncelleme ve silme işlemleri yapmak için ![ref46]  butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_196.png)

Dashboard Konfigürasyonu ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_197.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref14]: Yeni bir Dashboard tanımlanır.

![ref17]: Listede seçili olan Dashboard bilgisi üzerinde düzeltme/ değişiklik/ güncelleme yapılır. 

![ref15]: Listede seçili olan Dashboard bilgisi silinir.

- : Dashboard Konfigürasyonu ekranı kapatılır.

Dış Müşteri Şikayetleri Modülünde yeni bir Dashboard  ekleme işlemi için  ![ref14]  butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_198.png)

Dashboard Konfigürasyonu - Yeni Kayıt ekranında gerekli alanlar ilgili bilgiler doldurulduktan sonra ekranın sol üstte yer alan ![ref6]  butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_199.png)

Sistem tarafından “Kaydetmek istediğinize emin misiniz?” uyarı mejasında “Tamam” butonu tıklanarak grafik ayarlarının başarı olarak kaydedilmesi işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_200.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_201.png)

Dış Müşteri Şikayetleri Dashboard ekranında tanımlanan Dashboard görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_202.png)

![ref47]  Grafiği aktar butonu tıklanarak grafiği açılır menüden seçilen format türüne (png,jpg,bmp,xls, vb. ) dönüştürerek dış ortama aktarılma işlemide yapılır.

Grafik Boyu min  değeri 500  maxsimum 1000 aralığında sınırlandırılmıştır. Grafik Eni min değeri 550 ve maxsimim değeri 1800 aralığında sınırlandırılmıştır. Bu değerler arasında grafik boyu ve Eni seçilmelidir. Dashboard Konfigürasyonu - Yeni Kayıt sıra numarası önceden kullanılmışsa kaydetme aşamasında sistem tarafında “Belirtmiş olduğunuz sıra numarası kullanımdadır, kullanımda olmayan bir sıra numarası belirtmelisiniz.”  hata mesajı verilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_204.png)

Bu şekilde Grafik Ayarları butonu ile açılan ekranda yeni bir grafik eklenebilir.  Eklenen grafik bilgisi üzerinde düzenleme, güncelleme, değiştirme ve silme işlemleri yapılır. Listede  ilgili grafikler için filtreleme ekranı tanımlanmış ve indirilebilir olarak ayarlanmıştır.

Modül Yöneticileri olmayan kullanıcılar ise Dashboard Konfigürasyonu ekranı Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/ Dashboard Konfigürasyonu/ Dış Müşteri Şikayetleri menüsünde tıklayarak açılan ekranda gerekli ayarlamalar yapılarak grafik tasarım işlemide yapılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_205.png)

Dış Müşteri Şikayetleri Dashboard Konfigürasyonu ekranında  aynı butonları kullanarak aynı işlem basamakların yaparak yeni bir Dashboard tanımlama işlemi yapabilirler.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_206.png)
### **6.2.Entegre Yönetim Sistemi/Dış Müşteri Şikayetleri** 
Dış Müşteri Şikayetleri modülünde, Dış Müşteri Şikayet İşlemleri, Dış Müşteri Talebi, Onay Bekleyen Dış Müşteri Şikayetleri, Raporlar ve Grafikler menüleri yer aldığı kısımdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_207.png)
#### **6.2.1.Dış Müşteri Şikayet İşlemleri**
**Menü Adı**: Entegre Yönetim Sistemi/Dış Müşteri Şikayetleri/Dış Müşteri Şikayet İşlemleri

Firmaya gelen şikayetlerin sisteme girildiği menüdür. Dış Müşteri Şikayetleri  Kurum dışında tüm şikayetlerin açma, açılan Şikayet kaydı ilgili ilk acil önlemleri alarak gelişme raporu yazma, açılan Şikayet kaydı ilgili kök neden analizi yapma, kök nedenleri ortadan kaldıracak aksiyonları planlama, planlanan aksiyonları yapacak kişi ve sorumluları atama, planlanan aksiyonların gerçekleşmesi, alınan aksiyonların sonucunda sonuç raporu yazma, açılan Şikayet kaydı kapatma aşamasında gerektiğinde alınan aksiyonlar yeterli olup olmadığını takip etmek için belli zaman aralığında izleme yapma, gerektiğinde alınan aksiyonlar yeterli olmadığında tekrar aksiyon açma ve alınan aksiyonlar yeterli olduğunda açılan Şikayet  kaydı kapatma işlem aşamaları ile Şikayet  kaydı kaydının açılıp- kapatılması kadar devam eden süreçtirAçılan Dış Müşteri Şikayet İşlemleri ekranında iki sekme görüntülenir. Bu sekmeler Liste ve Filtre sekmesidir.

**Liste sekmesi;** 

Dış Müşteri Şikayet İşlemleri Modülü kapsamında Dış Müşteri Şikayet işlemleri ekranında sistemde tanımlı şikayet  kayıtlarının listesi yer alır. Bu sekmede ilgili butonlar kullanılarak yeni bir Şikayet kaydı tanımlama, listede seçili Şikayet kaydı üzerinde yetkiye bağlı olarak düzenleme/güncelleme/değişiklik yapma, şikayet kaydında  açılan Döf kayıtlarına gitme, Dış Müşteri Şikayet İşlemleri modülünde modül yöneticisi olarak tanımlı kullanıcıların seçili şikayet kaydını silme,  kayıt bakım özelliği kullanma ve iptal etme  işlemlerının yapılması sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_208.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref1] :Yeni bir şikayet kaydının sisteme girilip, tanımlama işlemi yapılır.

![ref27] :Listede seçili Şikayet kaydı üzerinde yetki olması halinde değişiklik/günceleme/düzenleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_209.png) :Listede seçili Şikayet kaydının tüm bilgilerini görüntüleme işlemi yapılır.

![ref48] :Listede seçili Şikayet kaydının bağlı DÖF Kaydı varsa şayet ilgili kayda götürülme işlemi yapılır.Liste sekmesinde ekranı görütüsündeki şikayet kaydı durumu Kapalı (\* Kapalı) olarak görüntülenmektedir. Bu  şikayet kaydında DÖF açıldığı bilgisi verilmektedir. Parantez içerisindeki Şikayet kaydında açılan DÖF kaydının durumu kapalı statüde olduğu belirtilmektedir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_211.png)

Listede seçili Şikayet kaydı seçili iken DÖF ile ilişkilendirilmiş DÖF kaydına gitmek istenildiğinde ![ref48](DÖF kaydına Git) butonu tıklanılır. Açılan DÖF İşlemleri ekranında Liste sekmesinde listede İlgili DÖF kaydı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_212.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_213.png):Listede seçili Şikayet kaydının düzeltmeler için kullanılan kayıt bakım butonudur.Bu butonun görüntülenmesi için Dış Müşteri Şikayetleri Modülün Modül Yönetici olmak gerekir. Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Yönetici Tanımlama menüsünde  Dış Müşteri Şikayetleri Modülünde yönetici tanımlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_214.png) :Listede seçili Şikayet kaydının silmek istenirse kullanılacak butondur. Sistem Yöneticilerinde çıkar. Uç kullanıcılarda görünmez. Bu  butonun görüntülenmesi için  kullanıcının Dış Müşteri Şikayetleri Modülünde Modül Yönetici olması gerekir. Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Yönetici Tanımlama menüsünde  Dış Müşteri Şikayetleri Modülünde yönetici tanımlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_215.png) : Parametrik bir buton olmakla birlikte Sistem Yöneticilerin ekranında çıkar. Şikayet kayıtlarının  iptal etmek için kullanılır. Silmekten farklı bir işlemdir. Şakayet  kaydının  İşleyişi durur fakat sistem de kayıtlı olmaya devam eder. Bir onay akış çerçevesinde çalışır. Bunun için alt yapıda akışın tanımlanması gereklidir.  Akış Tanımlama Sistem Altyapı Tanımları/Konfigürasyon Ayarları/Akış Tanımlama menüsünden tanımlanır.(İptal edilmek istenen Şikayet kayıtlarının hangi rol tarafından onaylanacak veya red edilecek olduğunu belirlemek için Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Akış Tanımlama menüsüne gelinir ve Dış müşteri şikayeti İptal Onay Akışı ![ref30]  butonuyla role bağlanır.)

![ref49] : Şikayet kaydının  herhangi bir aşamasına göre çıktı alma işlemi yapılır. Hangi aşamaya kadar rapor alınmak istenilirse şikayet kaydı seçilerek yapılarak ![ref49]  butonuna tıklanır. Seçili kayıda ait rapor bilgisayara çekilmiş olur. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_217.png)

**Bildirim Raporu;**

DMS kayıtları için  Bildirim Raporunun Şikayet Yazdır ekranında alınması için  Rapor formatları düzenleme menüsünde Bildirim Raporu şablon dosyasının yüklenerek Dış Müşteri Şikayetleri  parametrelerinde 46 numaralı “Bildirim raporu şablon dosyası” parametre değerine tanımlanması gerekir. Tanımlama işlemi için öncelikle Rapor Formatları Düzenleme menüsünde ![ref1]  butonu ile raporunun yüklenmesi gerekir. Yüklenen rapor formatı şablonun adı ve uzantısı birlikte ilgili parametreye  sağ tıkla/kopyala-yapıştır yönetimi ile yapıştırılması gerekir.

.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_218.png)

Bu parametreye tanımlanan Bildirim raporu şablonu Şikayet Yazdır ekranında Rapor Tipi “Bildirim Raporu” seçilerek ![ref49]  butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_219.png)

Şikayet Yazdır ekranında Bildirim Raporu  Excel formatında alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_220.png)

**Gelişme Raporu;**

DMS kayıtları için  Gelişme Rapourunun  Şikayet Yazdır ekranında alınması için  Rapor formatları düzenleme menüsünde Gelişme Raporu şablon dosyasının yüklenerek Dış Müşteri Şikayetleri  parametrelerinde 47 numaralı “Gelişme raporu şablon dosyası” parametre değerine tanımlanması gerekir. Tanımlama işlemi için öncelikle Rapor Formatları Düzenleme menüsünde ![ref1]  butonu ile raporunun yüklenmesi gerekir. Yüklenen rapor formatı şablonun adı ve uzantısı birlikte ilgili parametreye  sağ tıkla/kopyala-yapıştır yönetimi ile yapıştırılması gerekir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_221.png)

Bu parametreye tanımlanan Gelişme raporu şablonu Şikayet Yazdır ekranında Rapor Tipi “Gelişme Raporu” seçilerek ![ref49]  butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_222.png)

Şikayet Yazdır ekranında Gelişme Raporu  Excel formatında alınır.

![ref50]

**Sonuç Raporu;**

DMS kayıtları için  Sonuç  Raporunun Şikayet Yazdır ekranında alınması için  Rapor formatları düzenleme menüsünde Sonruç Raporu şablon dosyasının yüklenerek Dış Müşteri Şikayetleri  parametrelerinde 48 numaralı “Sonuç raporu şablon dosyası” parametre değerine tanımlanması gerekir. Tanımlama işlemi için öncelikle Rapor Formatları Düzenleme menüsünde ![ref1]  butonu ile raporunun yüklenmesi gerekir. Yüklenen rapor formatı şablonun adı ve uzantısı birlikte ilgili parametreye  sağ tıkla/kopyala-yapıştır yönetimi ile yapıştırılması gerekir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_224.png)

Bu parametreye tanımlanan  Sonuç raporu şablonu Şikayet  Yazdır ekranında Rapor Tipi “Sonuç Raporu” seçilerek ![ref49]  butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_225.png)

Şikayet Yazdır ekranında Sonuç Raporu Excel formatında alınır.

![ref50]

**Kapatma Raporu;**

DMS kayıtları için  Kapatma  Raporunun Şikayet Yazdır ekranında alınması için  Rapor formatları düzenleme menüsünde Kapatma Raporu şablon dosyasının yüklenerek Dış Müşteri Şikayetleri  parametrelerinde 52 numaralı “Kapatma raporu şablon dosyası” parametre değerine tanımlanması gerekir. Tanımlama işlemi için öncelikle Rapor Formatları Düzenleme menüsünde ![ref1]  butonu ile raporunun yüklenmesi gerekir. Yüklenen rapor formatı şablonun adı ve uzantısı birlikte ilgili parametreye  sağ tıkla/kopyala-yapıştır yönetimi ile yapıştırılması gerekir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_226.png)

Bu parametreye tanımlanan  Kapatma raporu şablonu Şikayet Yazdırma ekranında Rapor Tipi “Kapatma Raporu” seçilerek ![ref49]  butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_227.png)

Şikayet Yazdır ekranında Kapatma Raporu Excel formatında alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_228.png)

**Müşteri Raporu;**

DMS kayıtları için  Müşteri  Raporunun Şikayet Yazdır ekranında alınması için  Rapor formatları düzenleme menüsünde Müşteri Raporu şablon dosyasının yüklenerek Dış Müşteri Şikayetleri  parametrelerinde 49 numaralı “Müşteri raporu şablon dosyası” parametre değerine tanımlanması gerekir. Tanımlama işlemi için öncelikle Rapor Formatları Düzenleme menüsünde ![ref1]  butonu ile raporunun yüklenmesi gerekir. Yüklenen rapor formatı şablonun adı ve uzantısı birlikte ilgili parametreye  sağ tıkla/kopyala-yapıştır yönetimi ile yapıştırılması gerekir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_229.png)

Bu parametreye tanımlanan  Müşteri raporu şablonu Şikayet Yazdırma ekranında Rapor Tipi “Müşteri Raporu” seçilerek ![ref49]  butonu tıklanılır .

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_230.png)

Şikayet Yazdır ekranında Müşteri Raporu Excel formatında alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_231.png)

![ref5]: Ekrandaki liste sekmesinde listelenen Şikayet kayıtlarının Excel formatında raporunu alınma işlemi yapılır.

![ref4]: Kayıtlar filtrelenerek arama yapılabilir. 

![ref8]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref9]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref10]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranında kullanıcı bazlı tasarlama işlemi yapılır.

**Filtre sekmesi;**

Dış Müşteri Şikayetleri  Modülü kapsamında Dış  Müşteri Şikayetleri  işlemleri ekranında Kayıt No, Durum, Müşteri  ve Açan gibi alanlara göre veri girilip, ![ref51] butonu tıklanarak arama kriterlerine göre filtreleme yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_233.png)
##### **6.2.1.1.Yeni Şikayet Kaydının Açılması**
Dış Müşteri Şikayetleri işlemleri ekranında yeni bir Şikayet kaydının tanımlama için  ![ref1]   butonu tıklanarak  Şikayet Detayı ekranına açılır. Açılan ekranda, kaydı açanın  doldurması gereken 3 sekme vardır. Şikayet detayı, çözüm ekibi, ek dosyalar sekmeleridir.Dil ayarlarında parametrik alan tanımlanmış ise şikayet detayı diğer alanlar sekmesi de açan kişi tarafından doldurulur.

**Şikayet Detayı sekmesi;**

Şikayet  detay bilgilerin yer aldığı sekmedir.Şikayetin hangi müşteriden geldiği, şikayetin tanımı, detayı, şikayetin kategorisi gibi zorunlu alanlar girilecektir. İstenilirse şikayetin hangi işyeri, hangi ürün, hangi süreç ve yönetim sistemi ile alakalı olduğu da belirtilebilir. Şikayetle ilgili bilgi sahibi olması gereken kullanıcılar ise bilgilendirme alanından seçilebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_234.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Müşteri:** Şikayet Detayı ekranında şikayetin hangi Müşteriden geldiği bilgisinin ![ref52] butonu tıklanarak açılan sistemde tanımlı müşteri listesinden seçildiği alandır.

**Şikayet Tanımı:** Şikayet Detayı ekranında şikayetin tanım bilgisinin yazıldığı alandır. Dış Müşteri Şikayetleri Modülü parametrelerinde 109 numaralı “Şikayet kategorisi seçildiğinde tanım alanına otomatik yazılsın” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. ![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_236.png)

Parametre aktif edildikten sonra Şikayet kategorisi ekranında seçilen şikayet kategorisi tanımı, şikayet Tanımı alanına otomatik olarak yazılır.

**Şikayet Detayı:** Şikayet Detayı ekranında şikayetin detaylandırılarak yazıldığı alandır.

**İş Yeri:** Şikayet Detayı ekranında şikayetin ilgili olduğu işyeri bilgisinin ![ref52] butonu tıklanarak açılan sistemde tanımlı işyeri listesinde seçildiği alandır.

Dış Müşteri Şikayetleri Modülü parametrelerinde 70 numaralı “İş yeri bazında güvenlik uygulansın mı? (E/H)” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_237.png)

Parametre aktif edildikten sonra Dış Müşteri Şikayetleri ekranında Modül yöneticisi hariç diğer kişiler sadece kendi iş yerlerindeki Şikayet kayıtlarını görebilmeleri sağlanır. Diğer iş yerlerindeki Şikayet  kayıtları güvenlik getirilerek görünmesi gizlenmiş olur.

**Şikayet Kategorisi:** Şikayet Detayı ekranında şikayetin ilgili olduğu şikayet kategorisi bilgisinin ![ref52] butonu tıklanarak açılan sistemde tanımlı şikayet kategori listesinden seçildiği alandır. Şikayet kategori listesi Sistem Altyapı Tanımları/Dış Müşteri Şikayetleri/Şikayet Kategori Tanımlama menüsünde tanımlı olarak gelmektedir.

Dış Müşteri Şikayetleri Modülü parametrelerinde 35 numaralı “Şikayet Kategorisi Detayı zorunlu olsun (E/H)” parametre değeri “Evet” seçilerek parametre aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_238.png)

Parametre aktif edildikten sonra şikayet detayı ekranında şikayet kategorisi alanı ile bilgi girişinin yapılması zorunlu bırakılır.

Dış Müşteri Şikayetleri Modülü parametrelerinde 34 numaralı “Şikayet Kategorisi-İş yeri ilişkisi kurulsun mu?(E/H)” parametre değeri “Evet” seçilerek parametre aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_239.png)

Parametre aktif edildikten sonra Şikayet detayı ekranında işyeri alanı seçildiğinde  o işyerine bağlı şikayet kategorileri şikayet kategorileri listesinde gelir ve seçim işlemi yapılır. Şikayet Kategorisi tanımlama menüsünde şikayet kategorisi ile işyeri ilişkinin önceden kurulması gerekmektedir.

Dış Müşteri Şikayetleri Modülü parametrelerinde 84 numaralı “Şikayet Kategorisi bir tane seçilebilsin (çoklu seçimi engelle). (E/H) parametresinin parametre değeri”Evet” seçilerek parametre aktif edilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_240.png)

Parametre aktif edildiğinde şikayet kategori alanında şikayet kategorisi listesinde tekli seçim işlemi yapılır. Parametre değeri “Hayır” seçilerek parametre pasif edilirse Şikayet kategori alanında şikayet kategori listesinde çoklu seçim işlemi yapılır.

Dış  Müşteri Şikayetleri Modülü parametrelerinden 144 numaralı “Şikayet kategorisinde sadece en alt kategori seçilsin mi?” parametresi “Evet” seçilerek parametre aktif edilir. 

Parametre aktif edildikten sonra Şikayet kategori alanında  Şikayet detayı ekranında Şikayet kategori listesinde seçim yapıldığında ana kırılım altındaki alt kırılımlar seçilerek ilgili alana gelir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_241.png)

**Bilgilendirme:** Bu şikayetle ilgili bilgilendirme yapılacak kişi veya kullanıcı gruplarının bilgisinin seçildiği alandır.Bilgilendirme alanında şikayet detayı ile bilgilendirme yapılacak personel bilgisi için ![ref53] butonu tıklanarak açılan Personel listesinde seçim işlemi yapılır. Bilgilendirme alanında şikayet detayı ile bilgilendirme yapılacak Kullanıcı grubu bilgisi ![ref54] butonu tıklanarak açılan  sistemde tanımlı Kullanıcı Grubu listesinde seçim işlemi yapılır.Bu şikayeti ile ilgili Çözüm Ekip lideri ve Çözüm Ekibi dışında bilgilendirilmek istenilen kişilerin bu şekilde seçilir. Şikayet Detayında bilgilendirme ile ilgili parametrelerde gerekli ayarlama yapılarak bilgilendirme alanına otomatik olarak kişi veya varsayılan kullanıcı grubu bazında ekleme işlemi yapılır. Şikayet  kaydının açanın departman sorumlusu, bir üst amiri, ekip liderinin departman sorumlusu, Ekip Liderinin bir üst amiri, işyeri seçildiğinde sorumlusu, süreç seçildiğinde süreç sahibinin ve ürün seçildiğinde ürün grup sorumlusunu bilgilendirme alanına otomatik olarak sistem tarafından gelmesi için ilgili parametrelerde ayarlamalar yapılması gerekmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_244.png)

Dış Müşteri Şikayetleri Modülü parametrelerinde 10 numaralı “Varsayılan bilgilendirme için kullanıcı grubu kodu” parametresinin parametre değerine sistemde tanımlı Kullanıcı Grubu kod tanımlanır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_245.png)

Tanımlanan Kullanıcı Grubundaki kişiler bilgilendirme alanına varsayılan olarak gelir.Tanımlanan Kullanıcı Grubu kod bilgisi Sistem Altyapı Tanımları/BSAT/Tanımlar/Kullanıcı Grubu Tanımlama menüsünde alınır.

**Yönetim Sistemi:** Şikayet kaydı ekranında şikayet kaydının ilişkili olduğu yönetim sistemi bilgisi açılır liste tıklanarak açılan sistemde tanımlı yönetim sistemi listesinde seçildiği alandır. Yönetim Sistemi ile ilgili Dış Müşteri Şikayetleri Modülü parametrelerinde 169 numaralı “Yönetim sistemi çoklu seçilsin mi?” parametresi değeri “Evet” seçilerek parametre aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_246.png)

Parametre aktif edildikten sonra Şikayet Kaydı ekranında Yönetim Sistemi alanında ![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_247.png) butonu tıklanarak açılan sistemde tanımlı Yönetim Sistemi listesinde çoklu seçim işlemi yapılır

**Süreç:** Şikayet Kaydı ekranında şikayetin ilgili olduğu süreç bilgisi ![ref53] butonu tıklanarak açılan sistemde tanımlı süreç listesinden seçildiği alandır. Süreç listesindeki Süreçler Ensemble Süreç Yönetimi programında tanımlı olarak listeye gelmektedir.

**Ürün:** Şikayet Kaydı ekranın şikayetin ilgili olduğu ürün bilgisi ![ref53] butonu tıklanarak açılan sistemde tanımlı ürün listesinde seçildiği alandır.

**Şikayet Detayı Diğer Alanlar;** Firmanın özel istekleri doğrultusunda oluşturulmuş parametrik alanları içerdiği sekmedir. Eğer Dış Müşteri Şikayetleri Modülü için önceden parametrik alanlar oluşturulmuş ise Şikayet Detayı Diğer Alanlar sekmesine geçilerek bu alanlar doldurulur. Dış Müşteri Şikayetleri Modülü ile ilgili metin, metin(çoklu satır), liste  ve  müşteri gibi parametrik alan tanımlama işlemi Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Dil Ayarları menüsünde yapılır. Açılan Dil Ayarları menüsünde Modüller alanında Dış Müşteri Şikayetleri modülü seçilir. Dış Müşteri Şikayetleri Modülü ilgili pasif alanlar görüntülenir ve listede seçilir. 

Dış Müşteri Şikayetleri Modülü sekmelerine dil ayarlarında parametrik alan tanımlama işlemi için label kodlarının başlangıç kısmına dikkat etmek gerekir.

**lbl:** Label kodunun başlangıç kısmı bu şekilde başlarsa Şikayet Detayı Diğer Alanlar sekmesinde parametrik alanların tanımlama işlemi yapılır.

**lblG\_**: Label kodunun başlangıç kısmı bu şekilde başlarsa Gelişme raporu sekmesinde parametrik alanların tanımlama işlemi yapılır.

**lblKOK**: Label kodunun başlangıç kısmı bu şekilde başlarsa Kök Neden sekmesinde parametrik alanların tanımlama işlemi yapılır. 

**lblA\_**: Label kodunun başlangıç kısmı bu şekilde başlarsa Aksiyon sekmesinde parametrik alanların tanımlama işlemi yapılır. 

**lblS\_**: Label kodunun başlangıç kısmı bu şekilde başlarsa Sonuç Raporu sekmesinde parametrik alanların tanımlama işlemi yapılır. 

**lblK\_**: Label kodunun başlangıç kısmı bu şekilde başlarsa Kapatma sekmesinde parametrik alanların tanımlama işlemi yapılır. 

**Tarih Tipli Parametrik Alan Tanımlama;**

Şikayet Detayı diğer alanlara tanımlanacak lblDPARAM1… lblDPARAM5 sırasıyla kodlu alanlar tarih tipli tanımlanan pasif alanlandır. Bu alanlarda dil ayarlarında  bu sekmede  tarih tipli alanların tanımlama işlemi yapılır.

Dış Müşteri Şikayetleri modülünde tarih tipli parametrik alan tanımlama işlemi için Dil ayarlarından gridde Tipi alanında “Tarih” yazılarak Tarih tipli alanların listelenmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_248.png)

Şikayet Detayı Diğer alanlara Tarih tipli parametrik alan tanımlama işlemi için Dil Ayarlarında pasif  Tarih tipli alan seçili iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_249.png)  butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_250.png)

Açılan Dil ayarları ekranında değeri alanında tarih tipli alanın tanım  bilgisi yazılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_251.png)

Alanın zorunlu alan olup, olmayacağı , gridde gösterilip gösterilmeyeceği ile ilgili check box işaretlenir. Gerekli alanlar ilgili bilgiler girilerek ekranın sol üst kösesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_252.png)  butonu tıklanarak parametrik alan tanımlama kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_253.png)

Şikayet Detayı Değer alanlar sekmesinde tanımlanan tarih tipli parametrik alan görüntülenerek açılan açılır takvim alanında tarih seçimi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_254.png)

**Çözüm Ekibi sekmesi**;

Gelen şikayetleri çözüme ulaştıracak, kök neden analizini yapacak ve kalıcı aksiyonları planlayacak olan ekip lideri ve ekip üyelerinin seçildiği  ve gelişme raporunun plananan tarihinin açılana takvim alanında seçildiği sekmedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_255.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Ekip Lideri:** Şikayet Detayı Çözüm ekibi sekmesinde Ekip lideri bilgisinin ![ref53] butonu tıklanarak açılan sistemde tanımlı personel listesinden seçildiği alandır.

Dış Müşteri Şikayetleri Modülü parametrelerinden 8 numaralı “Varsayılan ekip lideri rol id” parametresine rol kodu tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_256.png)

Rol  kodu Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/ Rol Tanımlama menüsünde tanımlanan rolün kodunun yazıldığı parametredir.İşletme bünyesinde Şikayet kaydının ekip lideri bir role bağlı olarak seçilmesi sağlanır.Sistem Şikayet Kaydı Çözüm ekibi sekmesinde Ekip lideri alanında otomatik olarak parametrede tanımlı rol kodunundaki kişiyi ilgili alana otomatik olarak getirir.

Eğer herhangi bir  Şikayet Kaydı işleminde ürün ile ilişki kurulduğunda bu ürün grubu sorumlusunun direkt ekip lideri olarak atanması istenirse  Dış Müşteri Şikayetleri  Modülü parametrelerinde 80 numaralı  “Ürün seçildiğinde ürün grubu sorumlusu ekip lideri olarak atansın mı?(E/H)” parametresinin parametre değeri “Evet”seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_257.png)

Şikayet  kaydını açan personelin bağlı olduğu departman sorumlusunun ekip lideri olarak atanması isteniyorsa Dış Müşteri Şikayetleri  Modülü modülü parametrelerinde 114 numaralı “Açanın departman sorumlusu ekip lideri olarak atansın” parametresinin parametre değeri “Evet” seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_258.png)

Şikayet kaydı açılırken Açanın bir üst amiri ekip lideri olarak atanması isteniryorsa Dış Müşteri Şikayetleri  Modülü modülü parametrelerinde 113 numaralı “Açanın bir üst amiri ekip lideri olarak atansın” parametre değeri “Evet” seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_259.png)

Şikayet kaydı açılırken ilgili süreç seçildiği zaman süreç sorumlusunun ekip lideri olarak atanması isteniyorsa  Dış Müşteri Şikayetleri  Modülü modülü parametrelerinde 128 numaralı “Süreç seçildiğinde süreç sorumlusu ekip lideri olarak atansın mı?(E/H)” parametresinin parametre değeri "Evet" seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_260.png)

**Sorumlu Departman:** Şikayet Detayı Çözüm sekmesinde sorumlu departman bilgisi ![ref53] butonu tıklanarak açılan departman listesinden seçim yapıldığı alandır.

**Ekip:** Şikayet Detayı Çözüm sekmesinde Ekibe eklenecek kişilerin personel ve kullanıcı grubu listesinden seçildiği alandır. Ekibi eklenecek kişiler için ![ref55] butonu tıklanarak açılan personel listesinde seçim işlemi yapılır. Eğer ekibe bir kullanıcı grubundaki kişiler eklenecekse ![ref56] butonu tıklanarak açılan  sistemde tanımlı Kullanıcı Grubu listesinde seçim işlemi yapılır.

**Gelişme Raporu Tarihi (Planlanan**): Gelişme Raporu Tarihi (Planlanan) sistem tarafından parametrede yazılan değere göre otomatik verilir. Şikayeti açan kişi bu tarihte güncelleme yapabilir.

Dış  Müşteri Şikayetleri Modülü parametrelerinde 3 numaralı “Gelişme Raporu Hazırlama Süresi” parametresinde parametre değerine göre Müşteri şikayeti açıldıktan sonra gelişme raporunun kaç gün içerisinde yazılacağını belirlenir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_263.png)

Dış Müşteri Şikayetleri parametrelerinde 7 numaralı “Gelişme Raporu Hazırlama Süreleri Değiştirilebilsin mi? (E/H)” parametresinin parametre değerine “Evet” seçilerek Gelişme raporu hazırlama sürelerinin değiştirilmesi işlemi yapılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_264.png)

Parametre değeri “Hayır” seçildiğinde parametre pasif edildiğinde gelişme raporu Tarihi alanında sistem değişiklik yapılmasına izin vermez.

**Ek Dosyalar sekmesi;**

Şikayet Detayı ekranında şikayetle ilgili bir ek dosya varsa sisteme eklendiği sekmedir. Şikayet  kaydına doküman, ses, görüntü vb. formatlarda istenen dosyaların eklenmesi gerçekleştirilebilir

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_265.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref57]: Ek dosya sisteme yüklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_267.png):Yüklenen ek dosya bilgisi görüntülenir.

![ref3]: Yüklenen ek dosya bilgisi silinir.

Şikayet Detayı Ek dosyalar sekmesinde  ![ref57]  butonu tıklanarak Şikayet  kaydına ek dosya eklenir. Birden çok ek dosya eklenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_268.png)

Dosya Ekle ekranında Gözat butonu tıklanarak bilgisayardaki dosya seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_269.png)

Dosya Ekle ekranında Yükle butonu tıklanarak sisteme dosyanın yükleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_270.png)

Dosya Ekle ekranında Yükle butonu tıklanarak dosya sisteme yüklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_271.png)

Şikayet Detayı  ekranında gerekli alanlar ilgili bilgiler girildikten sonra ekranın sol üst köşesesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_272.png) butonu tıklanarak Şikayet Detayı kayıt işlemi yapılır. Eğer Şikayet açma onayı için bir akış kurgulandıysa ilgili rolün onayına kurgulanmadıysa Ekip Liderine Gelişme Raporu yazılması için görev düşer.

![ref58]  butonu tıklanarak Şikayet kaydı taslak olarak kaydedilir.Bu butonun görüntülenmesi için 102 numaralı “Taslak kaydetme kullanılacak mı?” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_274.png)

Parametre aktif edildiğinde Şikayet Kaydı ekranında![ref58]  butonu görüntülenir ve bu buton tıklanarak Şikayet kaydını taslak olarak kaydedilir. Şikayet  kaydı henüz hazırlama işlemi tamamlanmışsa taslak olarak kaydedilerek üzerinde işlem yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_275.png)

Dış Müşteri Şikayetleri modülünde Bekleyen İşlerimde taslak olarak kaydedilen Şikayet kaydı “Taslak Dış  Müşteri Şikayetleri Listesi” işi olarak görev düşer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_276.png)
##### **6.2.2.2. Taslak Dış Müşteri Şikayetleri Listesi**
Taslak olarak kaydedilen Şikayet kaydının Bekleyen İşlerim ekranında “Taslak Dış Müşteri Şikayetleri Listesi” görevindeki Şikayet No alanında Şikayet Kodu linki tıklanılır.Açılan Şikayet Detayı ekranında taslak aşamasında Şikayet kaydı ile istenirse ilgili alanlar üzerinde düzenleme, değişiklik ve güncelleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_277.png)

**Ekranda bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_278.png): Şikayet Detayı ekranında ilgili alanlarla bilgiler girilerek taslak olarak kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_279.png):Şikayet kaydının iptal edilme işlemi yapılır.

![ref59]:Şikayet kaydının kayıt işlemi yapılır. 

Şikayet Kaydı ekranında gerekli alanlar ilgili düzenleme ve güncelleme işlemi yapıldıktan sonra ![ref59] butonu tıklanarak bu aşamada da Şikayet kaydında Şikayet Kaydı açma onayı için bir akış kurgulandıysa ilgili rolün onayına kurgulanmadıysa Ekip Liderine Gelişme Raporu yazılması için görev düşer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_281.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_282.png)

Onaydaki kişiye sistem mail yollarken aynı zamanda bekleyen işlerine **“Onay Bekleyen Dış Müşteri Şikayetleri listesi”** şeklinde görüntülenir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_283.png)

##### **6.2.1.3.Şikayet Onaylama**
Şikayet açma onayına gönderildikten sonra ilgili kişi, Bekleyen İşleri’ne gelerek “**Onay Bekleyen Dış Müşteri Şikayetleri Listesi**” adı altında açma onayı vereceği Şikayet Detayını görür. Şikayet No alanındaki Şikayet kodu linki  tıklanarak  “Onay Bekleyen Şikayetler” listesini görüntüler.Kullanıcı onayında bekleyen DMS kayıtlarını Entegre Yönetim Sistemi/Dış Müşteri Şkayetleri/Onay Bekleyen İç Müşterileri menüsünden de ulaşabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_284.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref60]: İlgili Şikayet kaydının görüntüleme işlemi yapılır.

![ref61] : İlgili Şikayet kaydı ile değişik yapması istenirse kullanılır. Eğer talepten açılan Şikayet ise zorunlu alanları doldurmadan onaylama işlemi yapmamıza sistem izin vermeyecektir.

![ref62] : Şikayet onaylama işlemini yapmak için kullanılır. Onay işleminden sonra ilgili Şikayet kaydı Ekip liderinin önüne düşer.

![ref63] : Şikayet kaydınında girilen bilgiler uygun olmadığı durumda, Şikayet kaydı reddetmek için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_289.png):Şikayet kaydı kapatılır..

![ref64]  : Çok fazla onaylanması gereken Şikayet kaydı olması durumunda filtre seçeneğinden bilgiler süzülerek arama yapmak istendiğinde kullanılır.

![ref8]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref9]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref10]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranında kullanıcı bazlı tasarlama işlemi yapılır.

Onay Bekleyen Şikayetler ekranında ![ref60] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_291.png)

Açılan Görüntüleme ekranında Şikayet kaydı ile ilgili sekmeler tıklanarak Detay bilgileri görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_292.png)

Tarihçe sekmesinde Şikayet kaydı ile ilgili Şikayet açma gibi  onay durumları  ilgili işlem adımlarının yer aldığı şikayetin onay geçmişi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_293.png)

Onay Bekleyen Şikayetler ekranında ![ref61] butonu tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_294.png)

Açılan Şikayet Detayı ekranında görüntülenen sekmelerde ilgili alanlar üzerinde düzenleme ve değişiklik yapma işlemi yapılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_295.png)

Şikayet Detayı ekranında yapılan değişikliklerin kaydedilmesi için ekranın sol üst köşesindeki ![ref59]  butonu tıklanılır. Onay Bekleyen Şikayetler ekranında **![ref65]** butonu tıklanarak Ret nedeni girilerek Şikayet kaydı ret edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_297.png)

Açılan Şikayet Ret ekranında Şikayet Detayı bilgileri kontrol edilerek uygun olmadığı görüldüğünde Şikayet  ret etme işlemi yapılır ve  Ret Nedeni bilgisi yazılması zorunludur. Red edilen açan kişiye ret etme nedeniyle birlikte gönderilebilir. Ret ederken detay bilgi için ret veya şikayet kaydın iptali için ret edilebilir, buna bağlı olarak ilgili seçeneği seçmelidir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_298.png)

Onay Bekleyen Şikayetler ekranında ![ref66] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_300.png)Açılan şikayet detayı ekranında kapatma sekmesinde bu aşamada yeterlilik bilgisi ve onay notu bilgisi yazılarak şikayet kapatılma işlemi yapılır. ![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_301.png) butonu tıklanarak açılan DÖF İşlemleri-Yeni Kayıt ekranında DÖF kaydı ile ilgili alanlar ilgili bilgiler girilerek DÖF Kaydının açılma işlemi bu aşamada yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_302.png)Onay Bekleyen Şikayetler ekranında Şikayet Kapat butonunun bu aşamada görüntülenip, bu aşamada şikayetin kapatılma işlemin yapılması için Dış Müşteri Şikayetleri parametrelerinde 68 numaralı “Açma onayında şikayet kapatılabilsin mi? (E/H)” parametresinin parametre değerinin “Evet seçilerek parametrenin aktif edilmesi gerekmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_303.png)

Parametre aktif edildikten sonra Onay Bekleyenler Şikayetler ekranında ![ref66] butonu görüntülenir.  Bu buton kullanılarak bu aşamada şikayetin kapatılma işlemi yapılır.

Onay Bekleyen Şikayetler ekranında **![ref62]**  butonu tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_304.png)

Açılan Şikayet Onay ekranında Onay notu alanında Onay notu bilgisi yazılarak ![ref67] butonu tıklanarak Şikayet kaydı onaylanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_306.png)

Şikayet Detayı onaylarken onay notu bilgisi Dış Müşteri Şikayetler modülü parametrelerinde 142 numaralı “Şikayet onaylarken onay notu girilsin?” parametresinde parametre değeri “Evet” seçilerek parametre aktif edilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_307.png)

Parametre aktif edildikten sonra Şikayet Onay ekranlarında Onay Notu alanı görüntülenir ve onay notu bilgisi girilerek Şikayet Detayı onaylama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_308.png) 

Şikayet Kaydı onaylama işlemi gerçekleşen Şikayet kaydı  eğer Şikayet Gelişme Raporu  onayı için bir akış kurgulandıysa ilgili rolün onayına kurgulanmadıysa Ekip Liderine Gelişme Raporu yazılması için görev düşer.
##### **6.2.1.4.Gelişme Raporu Onayı**
Şikayet kaydı için Şikayet Gelişme Raporu onayı için akış kurgulandığı için onaydaki kişiye sistem mail yollarken aynı zamanda bekleyen işlerine “**Gelişme Raporu Onayı Bekleyen Dış Müşteri Şikayetleri Listesi”** işi olarak görev düşürür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_309.png)

Şikayet Kaydı gelişme raporu  onayına gönderildikten sonra ilgili kişi, Bekleyen İşleri’ne gelerek “**Gelişme Raporu Onayı Bekleyen Dış  Müşteri Şikayetleri Listesi**” adı altında Gelişme Raporu onayı vereceği şikayet kaydını görür. Şikayet No alanındaki şikayet kodu linki  tıklanarak  “**Onay Bekleyen Şikayetler**” listesini görüntüler.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_310.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref60]: İlgili Şikayet kaydının görüntüleme işlemi yapılır.

![ref62] : Şikayet onaylama işlemini yapmak için kullanılır. Onay işleminden sonra ilgili Şikayet kaydı Ekip liderinin önüne düşer.

![ref63] : Şikayet kaydınında girilen bilgiler uygun olmadığı durumda, Şikayet kaydı reddetmek için kullanılır. 

![ref8]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref9]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref10]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranında kullanıcı bazlı tasarlama işlemi yapılır.

Onay Bekleyen Şikayetler ekranında ![ref60] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_311.png)

Açılan Görüntüleme ekranında Şikayet kaydı ile ilgili sekmeler tıklanarak Detay bilgileri görüntülenir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_312.png)

Tarihçe sekmesinde Şikayet kaydı ile ilgili Şikayet açma, Gelişme Raporu  gibi işlem adımlarının ve onay durumları ile ilgili bilgilerin yer aldığı onay geçmişi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_313.png)

Onay Bekleyen Şikayetler ekranında **![ref65]** butonu tıklanarak Ret nedeni girilerek Şikayet kaydı ret edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_314.png)

Açılan Şikayet Ret ekranında Şikayet Detayı bilgileri kontrol edilerek uygun olmadığı görüldüğünde  Şikayet Ret etme işlemi yapılır ve  Ret Nedeni bilgisi yazılması zorunludur. Red edilen Şikayet kaydı açan kişiye ret etme nedeniyle birlikte gönderilebilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_315.png)

Onay Bekleyen Şikayetler ekranında **![ref62]**  butonu tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_316.png)

Açılan Şikayet Onay ekranında Onay notu alanında Onay notu bilgisi yazılarak ![ref67] butonu tıklanarak Şikayet kaydı onaylanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_317.png)

Şikayet onaylarken onay notu bilgisi Dış Müşteri Şikayetleri modülü parametrelerinde 142 numaralı “Şikayet onaylarken onay notu girilsin?” parametresinde parametre değeri “Evet” seçilerek parametre aktif edildiği için görüntülenip, onay notunun girilmesi zorunlu bırakılmıştır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_318.png)

Şikayet Kaydı Gelişme Raporu  onayı  işlemi yapıldıktan sonra Şikayet kaydı Ekip Liderine Gelişme Raporu yazılması için görev düşer
##### **6.2.1.5.Gelişme Raporu**
Şikayet Kaydı Gelişme Rapor onayının onaylama işleminden sonra gelişme raporu yazmak üzere Ekip liderinin bekleyen işlerine düşer.** Ekip üyeleri/ ekip lideri, Bekleyen İşleri’ne “**Gelişme Raporu Yazılacak Dış  Müşteri Şikayetleri Listesi**” işi olarak görev düşer. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_319.png)

İlgili Şikayet No alanındak Şikayet Kodu linki tıklayarak Şikayet Kaydı ekranında Gelişme raporu sekmesi tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_320.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Gelişme ve Sonuç Raporu Aynı Olsun:** Şikayet Detayı ekranında Gelişme Raporu sekmesinde Gelişme ve Sonuç raporu aynı olsun alanı ile ilgili “Evet” seçeneği işaretlenirse gelişme raporu aşamasındaki Kök Neden Analizi ve Aksiyon Planlama aşaması gerçekleşmeden gelişme raporunun kısmı sonuç raporu kısmına otomatik olarak sistem tarafından getirelerek şikayetin durumu sonuç aşamasında görüntülenerek  kapatma aşamasına gelir. Parametreye bağlı olarak görüntülenen bir alandır. Dış Müşteri Şikayetleri Modülü parametrelerinde “Gelişme ve Sonuç Raporu aynı olsun seçeneği kullanılacak mı?(E:Evet,H:Hayır,[ParametrikAlanAdı]=[Parametrik Alan Degeri])” parametre değeri “Evet” seçilerek parametre aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_321.png)

Parametre aktif edildikten sonra şikayet detayı gelişme raporu sekmesinde ilgili alan görüntülenir. 

**Gelişme Raporu:** Şikayet Detayı ekranında Gelişme Raporu sekmesinde Gelişme Raporu açıklama bilgisinin girildiği alandır.

**Sonuç Raporu Tarihi(P):** Şikayet Detayı ekranında Gelişme Raporu sekmesinde planlanan sonuç raporu tarihinin açılan takvim alanında belirlendiği alandır.

Şikayet Detayı ekranında Gelişme Raporu sekmesinde Dış  Müşteri Şikayetleri modülü ekranında 106 numaralı “Müşteri şikayetinden DÖF oluşturulabilsin mi?” parametresi parametre değeri “Evet” seçilerek parametre aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_322.png)

Parametre aktif edildikten sonra  Müşteri Şikayet ilgili DÖF kaydının  açılıp, açılmaması veya DÖF kaydı açıldığı takdirde DÖF işlemleri -Yeni Kayıt ekranında yada mevcutta kayıtlı DÖF Kayıtlarında seçilme işlemi ile seçenekler  sunulur.

![ref68]

- Şikayet kaydında DÖF ile ilgili “DÖF’e ihtiyaç yok” seçeneği seçilirse Müşteri şikayetinde DÖF Kaydı açılmaz.
- Şikayet kaydında DÖF ile İlgili “Yeni DÖF Aç” seçeneği seçilirse Şikayet detayı ekranında Gelişme Raporu sekmesinde ilgili alanlar bilgiler girildikten sonra kayıt işleminde sonra  DÖF İşlemleri-Yeni Kayıt ekranı açılarak müşteri şikayeti DÖF kaydı ile devam eder.
- Şikayet kaydında DÖF ile ilgili “Listeden Seç” seçeneği seçilirse, sistemde tanımlı DÖF’lerin yer aldığı DÖF listesinin yer aldığı alan görüntülenir. Görüntülenen bu alanda mevcutta kayıtlı DÖF’ler yer alır ve bu DÖF kayıtlarından seçim işlemi yapılır.

  ![ref69]

Görüntülenen alanda ![ref70] butonu tıklanarak mevcutta kayıtlı olan DÖF listesinde DÖF kaydı seçilir ve DÖF kaydının hangi aşamada ise o aşamadan şikayet kaydı DÖF kaydında devam edilir.

Dış  Müşteri Şikayeti modülünde 23 numaralı “MM - DOF ilişkisi korunsun mu? (E / H)” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_326.png)

Parametre aktif edildikten sonra müşteri şikayeti kaydında DÖF açıldığında müşteri şikayeti DÖF ile devam eder. DÖF kaydı kapatılmadan müşteri şikayeti kapatılmaz.

**Ekip:** Şikayet Detayı ekranında Gelişme Raporu sekmesinde ekibe eklenecek kişilerin personel ve kullanıcı grubu listesinden seçildiği alandır. Ekibi eklenecek kişiler için ![ref55] butonu tıklanarak açılan personel listesinde seçim işlemi yapılır. Eğer ekibe bir kullanıcı grubundaki kişiler eklenecekse ![ref56] butonu tıklanarak açılan  sistemde tanımlı Kullanıcı Grubu listesinde seçim işlemi yapılır. Ekibe kişi ekleme ve çıkarma işlemi bu alanda yapılır.

**Ek Dosyalar:** Şikayet Detayı ekranında Gelişme Raporu sekmesinde bu aşamada varsa bu gelişme raporu ile ilgili  kanıt doküman, fotoğraf gibi ek dosya yükleme işlemi butonlar yardımıyla  yapılır. Gelişme raporu aşamasında ek dosya yüklenmesi zorunluğu gerekli ayarlamalar yapılarak getirilir.Gelişme raporu aşamasında ek dosya yükleme işlemi zorunlu getirilmesi işlemi için Dış Müşteri Şikayetleri Modülü parametrelerinde 168 numaralı “Gelişme raporunda ek dosya zorunlu olsun” parametresinin parametre değeri “Evet”seçilerek parametre aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_327.png)

Parametre aktif edildiğinde Gelişme raporu aşamasında Ek Dosya yükleme işlemi yapılmadan gelişme raporu kayıt  işlemi gerçekleşmez. 

Dış Müşteri Şikayetleri  Modülü parametrelerinde 32 numaralı “Yorum modülü aktif (E/H)” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_328.png)

Parametre aktif edildikten sonra Şikayet Kaydı  ekranında Yorumlar sekmesi görüntülenir. Şikayet Kaydı ekranında görüntülenen bu sekmede kullanıcı isterse her aşamada ilgili yorumları  ekleme,eklenen yorumları düzenleme,güncelleme,değiştirme ve silme işlemleri ilgili butonlar ile yapar. Ayrıca eklenen yorumların listesinde excel formatında raporunu bu aşamada alır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_329.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref1]: Yeni bir yorum tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_330.png): Listede seçili olan yorum bilgisi üzerinde düzenleme/değişiklik/güncelleme işlemi yapılır.

![ref3]: Listede seçili olan yorum bilgisi silinir. 

![ref5]: Veriler Excel’ e aktarılır.

![ref8]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref9]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref10]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Yorumlar ekranına yeni bir yorum eklemek için ekranın sol üst köşesindeki ![ref1]  butonu tıklanarak Yorumlar-Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_331.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Yorum:** Yorumlar-Yeni Kayıt ekranında yapılan yorum bilgisinin girildiği alandır.

**Ek Dosyalar:** Yorumlar sekmesinde bu aşamada yorumla ilgili varsa kanıt doküman, fotoğraf gibi ek dosya yükleme işlemi butonlar yardımıyla  yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_332.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref71]: Ek dosya sisteme yüklenir.

![ref72]: Yüklenen ek dosya bilgisi görüntülenir.

![ref3]: Yüklenen ek dosya bilgisi silinir.

![ref71]  butonu tıklanarak tanımlanan yorumu istenirse ek dosya eklenir. Birden çok ek dosya eklenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_335.png)

Yorumlar- Yeni Kayıt ekranında gerekli alanlar doldurulduktan sonra sol üst köşede yer alan  ![ref6]   butonuna tıklanarak yorum  tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_336.png)

Gelişme raporu aşamasında Yorum ekleme işlemi yapıldıktan sonra Ekip lideri Acil aldığı önlemlerle  ilgili gelişme raporu yazar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_337.png)

Şikayet Detayı ekranında gelişme raporu sekmesinde gelişme raporu bilgisi, sonuç raporu tarihi açılan takvim alanından seçilir. İstenirse bu aşamada şikayet kaydı DÖF kaydı  devam edilir. Varsa ekip eklenecek kişi ve kullanıcı grubu ekleme işlemi yapılır. Gerekli alanlar ilgili bilgiler girildikten sonra ekranın sol üst köşesindeki ![ref6]  butonu tıklanarak gelişme raporu kayıt işlemi yapılır. Gelişme raporu aşamasında sonra Ekip Liderine ve Ekipe Şikayet kaydı için Kök Neden Analizi/Aksiyon Planlama işlemin  yapılması için görev düşer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_338.png)
##### **6.2.1.6.Kök Neden Analizi**
Gelişme raporu yazıldıktan sonra, Kök Nedenler sekmesi aktif olur. Kök Neden Analizi ekranına gelinir. Şikayetin hangi kök nedenden dolayı kaynaklandığının belirlendiği ve kök neden analizi yapıldığı sekmedir.  Ekip ve Ekip liderin bulunduğu çözüm ekibi tarafından Şikayeti çözüme ulaştırmada öncelikle kök nedenlerin bilinip ve bu kök nedenleri ortadan kaldıracak kalıcı çözümlerin alınması planlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_339.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref1]:Yeni bir Kök Neden ekleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_340.png):Listede seçili Kök Neden bilgisi üzerinde değişiklik/düzenleme/güncelleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_341.png):Listede seçili Kök Neden bilgisi silinir.

![ref73]:Kök Neden Analizine Kullanılacak Şablonlar doküman kodları görüntülenir ve kök neden analizindeki kullanılacak şablon dokümanları tıklanarak bilgisayara indirilme işlemi yapılır. Parametreye bağlı görüntülenen bir alandır. Dış Müşteri Şikayetleri  modülü parametrelerinde 119 numaralı “Kök Neden Analizinde kullanılacak şablon doküman kodları(Birden fazla ise "," ile ayırınız) parametresinde parametre değerine Doküman Yönetimi Modülünde yüklü olan şablon dokümanları kodları yazılarak parametreye tanımlanılır. Şablon doküman kodları Entegre Yönetim Sistemi/Doküman Yönetimi/Doküman Görme menüsünden alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_343.png)

![ref73] butonu tıklanıldığında parametreye tanımlı şablon doküman kodlar görüntülenir ve görüntülenen şablon doküman kodları tıklanarak bilgisayara indirilir. İndirilen Kök Neden Analizinde Kullanılacak Şablonlar ![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_344.png) butonu tıklanarak Kök Nedenler sekmesinde istenirse Kök Neden Analiz Raporu sisteme yükleme işlemi yapılır.

Parametreye bağlı olarak Kök Neden Analiz Raporu yükleme işlemi zorunlu bırakılır. Dış Müşteri Şikayetleri modülü parametrelerinde 118 numaralı “Kök neden analiz dosyası zorunlu olsun” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_345.png)

Parametre aktif edildiğinde Kök Nedenler sekmesinde Kök neden tanımlama işlemi yapılmadan önce “Kök neden eklemeden önce kök neden analiz raporunu yüklemelisiniz” sistem tarafından uyarı mesajı verilerek Kök Neden Analizi raporu yükleme işlemi zorunluluğunu getirilir.

Dış Müşteri Şikayetleri Modülü  parametrelerinde 58 numaralı “Kök Neden Kullanılacak mı?” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_346.png)

Parametre aktif edildikten sonra Şikayet Kaydı ekranında Kök Nedenler sekmesini görüntülenir ve Şikayet kaydınında Kök Nedenler aşaması  kullanılır.

Dış Müşteri Şikayetleri Modülü parametrelerinde 59 numaralı “Kök Neden girişi zorunlu olsun mu?” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_347.png)

Parametre aktif edildikten sonra Şikayet Kaydı ekranında aksiyon planlamadan önce kök neden girişinin zorunlu olması sağlanır. Eğer böyle bir zorunluluk istenmiyorsa parametre değeri "Hayır" seçilerek parametre pasif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_348.png)

Dış Müşteri Şikayetleri Modülü parametrelerinden 118 numaralı  “Kök neden analiz dosyası zorunlu olsun” parametresi aktif olduğunda ![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_349.png) butonu tıklanarak Yeni bir Kök Neden tanımlama işlemi yapıldığından sistem “Kök neden eklemeden önce kök neden analiz raporunu yüklemelisiniz” uyarı mesajı verir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_350.png)

Kök Neden Analizinde Kullanılacak şablonlardan yada kullanıcının bilgisayarında sisteme şablon yükleme işlem yapılması zorunlu kılar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_351.png)

Şikayet Detayı ekranında Kök Neden Analizi sekmesinde![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_352.png) butonu tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_353.png)

Sistem Dış Müşteri Şikayetleri modülü parametrelerinde 119 numaralı parametrede tanımlı Kök Neden Analizinde kullanılacak Şablon görüntülenerek tıklanarak bilgisayara indirilir

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_354.png)

Şikayet Detayı ekranında Kök Neden Analizi sekmesinde ![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_355.png) butonu tıklanarak Kök neden analizi raporunun sisteme yükleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_356.png)

Dosya Seç ekranında Gözat butonu tıklanarak bilgisayardaki indirilenen Kök Neden Analizi Dosyası seçilerek yükleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_357.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_358.png)

Şikayet Detayı ekranında Kök Neden Analizi sekmesinde yeni bir Kök neden tanımlamak için  ![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_359.png) butonu tıklanarak Kök neden Analizi  ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_360.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Kök Neden:** Kök Nedenler Analizi ekranında Kök Neden bilgisinin ![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_361.png) butonu tıklanarak açılan sistemde tanımlı Kök Neden listesinden seçilebildiği alandır. Sistem Altyapı Tanımları/Dış Müşteri Şikayetleri/Kök Neden Tanımlama ekranında tanımlı Kök Neden listesinde seçim yapılır.

**Açıklama:** Kök Nedenler Analizi ekranında Kök Nedenin Açıklama bilgisinin girildiği alandır.

Açılan ekranda daha önceden tanımlanan kök nedenlerden seçilir, açıklama bilgisi girilir. Gerekli alanlar ilgili bilgiler girildikten sonra ![ref11]  butonu tıklanarak kök neden kaydedilerek Şikayet kaydı hangi kök nedenlerde  ortaya çıktığı belirlenerek  ilişkisi kurulmuş olur. Birden fazla kök neden seçimi ile çoklu seçim yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_362.png)

Dış Müşteri Şikayetleri Modülünde 136 numaralı “Sadece ekip lideri kök neden analizi yapabilsin” parametre değeri “Evet” seçilerek parametre aktif edilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_363.png)

Parametre aktif edildikten sonra sadece Ekip lideri Kök neden analizi yapması zorunluğu sistemde getirilir.

Dış Müşteri Şikayetleri Modülü parametrelerinden 181 numaralı “Kök-Neden Analizi içerisinde aynı kök neden tekrar seçilebilsin mi? (E/H)” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_364.png)

Parametre aktif edildikten sonra Kök Neden Analizi sekmesinde aynı Kök Nedenin tekrar seçilme işlemi yapılır.
##### **6.2.1.7.Aksiyonlar**
Çözüm ekibinde bulanan Ekip Lideri ve ekipteki kişiler Kök nedenler belirlendikten sonra süreç, bu kök nedenleri ortadan kaldıracak Aksiyonların planlama işleminin yapılmasıdır.  Kök nedenlerin ortadan kaldıracak Aksiyonların planlama işlemin yapıldığı sekmedir. Çözüm ekibindeki kişiler Ekip Lideri ve ekip bu sekmede Aksiyon planlaması yapar. Şikayet Kaydı  Aksiyonlarının planlanması ile devam eder. Aksiyonlar sekmesine gelinir. Burada Şikayet kaydı ile ilgili oluşturulacak kök nedenleri ortadan kaldıracak  aksiyonlar planlanır ve iş olarak atanır.  Aksiyon planlaması yapılarken  Aksiyonun ne olacağı, Aksiyonu  yapacak kişi ve sorumlu kişinin atama işlemide yapılır. Bu aşamada yapılan Aksiyonlar Aksiyon Modülü kapsamı dışında Aksiyonlardır.

Dış Müşteri Şikayetleri modülü parametrelerinde 50 numaralı “Aksiyon Kullanılacak mı?” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_365.png)

Parametre aktif edildikten sonra Şikayet Detayı ekranında Aksiyonlar sekmesi görüntülenir ve Şikayet kaydı ile ilgili Aksiyon planlaması işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_366.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref74] : Yeni bir aksiyon ekleme işlemi yapılır.

![ref75] :Listede seçili Aksiyon bilgisinin içeriği görüntülenir.

![ref76]:Listede seçili Aksiyon bilgisi üzerinde değişiklik/düzenleme/güncelleme işlemi yapılır.

![ref77] Listede seçili Aksiyon bilgisi kopyalama işlemi yapılır.

![ref78]:Listede seçili Aksiyonun gerçekleştirilmesi işlemi yapılır.

![ref79] :Listede seçili planlanan aksiyonun termin süresini geciktirme işlemi yapılır.Parametreye bağlı olarak görüntülenen butondur.Dış Müşteri Şikayetleri modülü parametrelerinden 24 numaralı “Aksiyon geciktirilebilsin mi?(E/H)” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilmelidir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_373.png)

Parametre aktif edildikten sonra Şikayet Kaydı ekranında Aksiyonlar sekmesinde ![ref79](Aksiyon Geciktir) butonu görüntülenir ve bu buton tıklanarak Aksiyon geciktirme işlemi  yapılır.

![ref5]: Veriler Excel’ e aktarılır.

![ref8]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref9]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref10]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranında kullanıcı bazlı tasarlama işlemi yapılır.

Şikayet Kaydı ekranında Aksiyonlar sekmesinde yeni bir Aksiyon  eklemek için ekranın sol üst köşesindeki ![ref1]  butonuna tıklanarak Aksiyon Tanımlama / Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_374.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Aksiyon Sorumlu:** Aksiyonlar-Yeni Kayıt ekranında aksiyonun sorumlu bilgisi ![ref80] butonu tıklanarak açılan  sistemde tanımlı personel listesinde seçilebildiği alandır.

**Aksiyon İşi Yapacak Kişi:** Aksiyonlar-Yeni Kayıt ekranında Aksiyonun işi yapacak kişi bilgisinin ![ref80] butonu tıklanarak açılan  sistemde tanımlı olan personel listesinden seçilebildiği alandır.

**Aksiyon:** Aksiyonlar-Yeni Kayıt ekranında Aksiyon bilgisinin girildiği alandır.

**Planlanan Bitiş Tarihi:** Aksiyonlar-Yeni Kayıt ekranında Aksiyonun planlanan bitiş tarihi  bilgisinin açılan takvim alanında belirlendiği alandır.

**Standart Madde No:** Aksiyonlar-Yeni Kayıt ekranında Aksiyonla ilişkilendirilen ilgili Standart Madde No bilgisinin ![ref80] butonu tıklanarak açılan sistemde tanımlı olan Madde No listesinden seçilebildiği alandır.

**İlgili Doküman:** Aksiyonlar-Yeni Kayıt ekranında ilgili Doküman bilgisinin ![ref80] butonu tıklanarak açılan sistemde tanımlı olan Doküman listesinden seçilebildiği alandır.

**İlgili Kök Neden:** Aksiyonlar-Yeni Kayıt ekranında İlgili Kök Neden Bilgisinin ![ref80] butonu tıklanarak açılan Kök neden sekmesinde kök neden olarak seçilen kök neden veya kök nedenlerle ilişki kurulduğu alandır.Kök Neden listesi Sistem Altyapı Tanımları/Dış Müşteri Şikayetleri/Kök Neden Tanımlama menüsünde tanımlı gelmektedir.

**Ek Dosyalar:** Aksiyonlar  sekmesinde bu aşamada varsa bu Aksiyonla ile ilgili  kanıt doküman, fotoğraf gibi ek dosya yükleme işlemi butonlar yardımıyla  yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_376.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref81]: Ek dosya sisteme yüklenir.

![ref82]: Yüklenen ek dosya bilgisi görüntülenir.

![ref15]: Yüklenen ek dosya bilgisi silinir.

![ref81]  butonu tıklanarak  Aksiyonlar aşamasında Şikayet kaydına ek dosya eklenir. Birden çok ek dosya eklenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_379.png)

Açılan Aksiyonlar-Yeni Kayıt ekranda Aksiyondan sorumlu kişi ve aksiyonu yapacak kişi listeden seçilir, aksiyon bilgisi girilir, aksiyonun planlanan bitiş tarihi belirlenir, aksiyon ile ilgili standart madde numaraları eklenebilir ve kök nedenler eklenir. Yine istenirse Ek Dosyalar kısmından, Aksiyon ile alakalı ek dosya, doküman vb. eklenebilir. 

Aksiyonlar -Yeni Kayıt ekranında gerekli alanlar doldurulduktan sonra sol üst köşede yer alan  ![ref6]   butonuna tıklanarak aksiyon planlanmış olur ve onaydaki kişiye onay için aksiyon gönderilir. Şikayet Kaydı Aksiyon Açma  onayı için bir akış kurgulandıysa ilgili rolün onayına gönderilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_380.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_381.png)
##### **6.2.1.8.Açma Onayı Bekleyen Aksiyonlar**
Şikayet Kaydı için Şikayet Kaydı ile ilgili Aksiyon onayı için akış kurgulandığı için** onaydaki kişiye sistem mail yollarken aynı zamanda bekleyen işlerine “**Açma Onayı Bekleyen Dış  Müşteri Şikayeti Aksiyonları Listesi**” işi olarak görev düşürür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_382.png)

Şikayet Kaydı  Aksiyonu Açma onayına gönderildikten sonra ilgili kişi, Bekleyen İşleri’ne gelerek “**Açma Onayı Bekleyen Dış  Müşteri Şikayeti Aksiyonları Listesi**” adı altında Açma Onayı Aksiyonu vereceği Şikayeti görür. Şikayet -Aksiyon No  alanındaki Şikayet -Aksiyon No   kodu linki  tıklanarak  “**Onay Bekleyen Şikayetler**” listesini görüntüler.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_383.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref60]: İlgili Şikayet kaydının görüntüleme işlemi yapılır.

![ref83]:İlgili Şikayet kaydı bilgisi üzerinde güncelleme işlemi yapılır.

![ref62] : Şikayet kaydının onaylama işlemini yapmak için kullanılır. Onay işleminden sonra ilgili Şikayet kaydı Ekip Liderinin önüne düşer.

![ref63] :Şikayet kaydında  girilen bilgiler uygun olmadığı durumda, Şikayet kaydını  reddetmek için kullanılır. 

![ref8]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref9]: Menü ekranın tekrar varsayılan ayarlara gelmesi işlemi yapılır.

![ref10]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranında kullanıcı bazlı tasarlama işlemi yapılır.

Onay Bekleyen Şikayetler ekranında ![ref60] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_385.png)

Açılan Görüntüleme ekranında Şikayet kaydı ile ilgili sekmeler tıklanarak Detay bilgileri görüntülenir

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_386.png)

Tarihçe sekmesinde Şikayet kaydı ile ilgili Şikayet açma, Gelişme Raporu ve Aksiyon Açma  gibi işlem adımlarının ve onay durumları ile ilgili bilgiler yer aldığı şikayetin onay geçmişi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_387.png)

Onay Bekleyen Şikayetler ekranında ![ref83]butonu tıklanarak şikayet kaydı ile değişiklik ve güncelleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_388.png)

Şikayet Detayı ekranında şikayet detayı ile ilgili alanlar üzerinde düzenleme ve güncelleme işlemi yapılarak ekranın sol üst köşesindeki ![ref6]  butonu tıklanarak Şikayet detayı kayıt güncelleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_389.png)

Onay Bekleyen Şikayetler** ekranında ![ref65] butonu tıklanarak Ret nedeni girilerek Şikayet kaydı ret edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_390.png)

Açılan Şikayet Ret ekranında Şikayet Kaydının bilgileri kontrol edilerek uygun olmadığı görüldüğünde Şikayet Kaydı Ret etme işlemi yapılır ve  Ret Nedeni bilgisi yazılması zorunludur. Red edilen açan kişiye ret etme nedeniyle birlikte gönderilebilir. Ret ederken detay bilgi için ret veya kaydın iptali için ret edilebilir, buna bağlı olarak ilgili seçeneği seçmelidir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_391.png)

Onay Bekleyen Şikayetler ekranında **![ref62]**  butonu tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_392.png)

Açılan Şikayet Onay ekranında Onay notu alanında Onay notu bilgisi yazılarak ![ref67] butonu tıklanarak  Şikayet kaydı onaylanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_393.png)

Şikayet onaylarken onay notu bilgisi Dış Müşteri Şikayetleri modülü parametrelerinde 142 numaralı “Şikayet onaylarken onay notu girilsin??” parametresinde parametre değeri “Evet” seçilerek parametre aktif edilir. Parametre aktif edildikten sonra Şikayet Onay ekranlarında Onay Notu alanı görüntülenir ve onay notu bilgisi girilerek Şikayet onaylama işlemi yapılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_394.png)

Açma Onayı onaylanan Aksiyonların durumu “Açık” statüne gelir. Açık statüsündeki Aksiyonlar işi yapacak kişinin bekleyen işlerinde görev olarak düşer.
##### **6.2.1.9.Gerçekleştirilecek Aksiyonlar**
Şikayet Kaydında açma onayı işlemi yapılan Aksiyonlar durumu “Açık” statüsünde geldikten sonra işi yapacak kişinin “bekleyen işlerinde” “**Gerçekleştirilecek Dış Müşteri Şikayeti Aksiyonları Listesi**” işi olarak görev düşer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_395.png)

Bekleyen İşleri’nden “**Gerçekleştirilecek Dış Müşteri Şikayeti Aksiyonları Listesi**” altına gelinerek Şikayet-Aksiyon No alanındaki link tıklanır ve Şikayet bilgileri ekranına ulaşılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_396.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref74] : Yeni bir aksiyon ekleme işlemi yapılır.

![ref75] :Listede seçili Aksiyon bilgisinin içeriği görüntülenir.

![ref76]:Listede seçili Aksiyon bilgisi üzerinde değişiklik/düzenleme/güncelleme işlemi yapılır.

![ref77] Listede seçili Aksiyon bilgisi kopyalama işlemi yapılır.

![ref78]:Listede seçili Aksiyonun gerçekleştirilmesi işlemi yapılır.

![ref79] :Listede seçili planlanan aksiyonun termin süresini geciktirme işlemi yapılır.

![ref5]: Veriler Excel’ e aktarılır.

![ref8]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref9]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref10]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranında kullanıcı bazlı tasarlama işlemi yapılır.

Şikayet Detayı ekranında Aksiyonlar sekmesinde ![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_397.png) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_398.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Aksiyon:** Aksiyon gerçekleştirme ekranında planlanan aksiyonun tanım bilgisi sistem tarafından otomatik verildiği alandır.

**Yapılan İş:** Aksiyonlar gerçekleştirme ekranında yapılan iş açıklama bilgisinin girildiği alandır.

**Aksiyon Gerçekleştirme Tarihi:** Aksiyonlar gerçekleştirme ekranında Aksiyon Gerçekleştirme Tarihinin belirlendiği alandır.

**Ek Dosyalar:** Aksiyonlar gerçekleştirme ekranında bu aşamada varsa bu Aksiyonla ile ilgili  kanıt doküman, fotoğraf gibi ek dosya yükleme işlemi butonlar yardımıyla  yapılır

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_399.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref81]: Ek dosya sisteme yüklenir.

![ref82]: Yüklenen ek dosya bilgisi görüntülenir.

![ref15]: Yüklenen ek dosya bilgisi silinir.

![ref81]  butonu tıklanarak  Aksiyonlar aşamasında Şikayet kaydına ek dosya eklenir. Birden çok ek dosya eklenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_400.png)

Aksiyon Gerçekleştirme ekranında, aksiyonun gerçekleştirme bilgisi ve gerçekleştirme tarihi girilir. Ayrıca istenirse aksiyonun gerçekleştirme aşamasına ek dosya eklenebilir. Yapılan iş ve varsa ek dosya eklendikten sonra gerekli alanlar doldurulduktan sonra sol üst köşede yer alan  ![ref6]   butonuna tıklanarak aksiyon gerçekleştirilmiş olur. Gerçekleşme onayı  bekleyen Şikayet Aksiyonları için bir akış kurgulandıysa ilgili rolün onayına gönderilir. Onay kurgulanmadıysa Sonuç raporu yazmak için Ekip Lideri/  Ekip üyesinin Bekleyen İşlerine gönderilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_401.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_402.png)
##### **6.2.1.10.Gerçekleştirme Onayı Bekleyen Dış Müşteri Şikayetleri Aksiyonları Listesi**
Şikayet kaydı için Gerçekleştirme Onayı Bekleyen Şikayet Aksiyonları için akış kurgulandığı için onaydaki kişiye sistem mail yollarken aynı zamanda bekleyen işlerine “Gerçekleştirme Onayı Bekleyen Dış Müşteri Şikayeti Aksiyonları Listesi” işi olarak görev düşürür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_403.png)

Şikayet Aksiyonu Gerçekleşme işlemi  yapıldıktan sonra ilgili kişi, Bekleyen İşleri’ne gelerek “**Gerçekleştirme Onayı Bekleyen Dış Müşteri Şikayeti Aksiyonları Listesi**” adı altında Gerçekleşme  Onayı Bekleyen Şikayet Aksiyonları olan  Şikayeti görür. Şikayet-Aksiyon No  alanındaki  kod linki  tıklanarak  **“Onay Bekleyen Şikayetler”** ekranı  görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_404.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref60]: İlgili Şikayet kaydının görüntüleme işlemi yapılır.

![ref62] :Şikayet kaydı onaylama işlemini yapmak için kullanılır. Onay işleminden sonra ilgili şikayet kaydı Ekip liderinin önüne düşer.

![ref63] :Şikayet kaydında girilen bilgiler uygun olmadığı durumda, Şikayet Kaydını reddetmek için kullanılır.** 

![ref8]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref9]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref10]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranında kullanıcı bazlı tasarlama işlemi yapılır.

Onay Bekleyen Şikayetler ekranında ![ref60] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_405.png)

Açılan Görüntüleme ekranında Şikayet kaydı ile ilgili sekmeler tıklanarak Detay bilgileri görüntülenir

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_406.png)

Tarihçe sekmesinde Şikayet kaydı ile ilgili Şikayet açma, Gelişme Raporu, Aksiyon Açma ve Aksiyon Gerçekleşme gibi işlem adımlarının ve onay durumları ile ilgili bilgiler yer aldığı şikayet onay geçmişi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_407.png)

Onay Bekleyen Şikayetler** ekranında ![ref65] butonu tıklanarak Ret nedeni girilerek Şikayet kaydı ret edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_408.png)

Onay Bekleyen Şikayetler ekranında **![ref62]**  butonu tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_409.png)

Açılan Şikayet Onay ekranında Onay notu alanında Onay notu bilgisi yazılarak ![ref67] butonu tıklanarak  Şikayet kaydı onaylanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_410.png)

Aksiyonlar planlanıp, gerçekleştikten ve onaylandıktan sonra Şikayet Kaydının aşaması  Sonuç Raporu aşamasında geçer.
##### **6.2.1.11.Sonuç Raporu**
Aksiyonların tamamı gerçekleştirildikten sonraki aşama, sonuç raporu yazma basamağıdır. Sonuç raporu sekmesinde ekip lideri tarafından aksiyonlar incelenerek yeterliliği araştırılır. Ekip lideri sonuç raporu yazarken, şikayetin bu aksiyonlar ile kapatılıp kapatılamayacağına dair kapatma onayındaki kişiye geri bildirim verir.  Aksiyonlar planlanıp gerçekleştirildikten sonra süreç, sonuç raporunun yazılmasıyla devam eder. Ekip Lideri/  Üyesi, Bekleyen İşleri’de  “**Sonuç Raporu Yazılacak Dış Müşteri Şikayetleri Listesi”** işi olarak görev düşer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_411.png)

Dış Müşteri Şikayetinde  Aksiyonu planıp, gerçekleştilip ve onaya  gönderildikten sonra Ekip/Ekibin, Bekleyen İşleri’ne gelerek “**Sonuç Raporu Yazılacak Dış Müşteri Şikayetleri Listesi**” adı altında  Sonuç Raporu yazılacak Şikayet kaydını görür. Şikayet Kaydı  alanındaki Şikayet kodu linki  tıklanarak  Şikayet Detayı ekranında Sonuç Raporu sekmesi görüntüler. Dış Müşteri Şikayetleri Modülü parametrelerinde 89 numaralı “Sonuç Raporu kullanılacak mı? (E/H))” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_412.png)

Parametre aktif edildikten sonra Şikayet Detayı ekranında Sonuç Raporu sekmesini görüntülenir ve Şikayet kaydınında Soruç raporu aşaması  kullanılır. Sonuç raporu, Şikayetle ile ilgili alınan nihai önlemleri, çözüm önerilerini içeren bir rapordur.Sonuç Raporu şikayetin giderilmesi için bu aşama kadar yapılan işlem basamakların bir özet raporudur. Sonuç Raporu yine Çözüm Ekibi oluşturan Ekip lideri tarafında yazılır. Şikayet Detayı  sırasında yapılan tüm işlemlerin özeti niteliğinde, kapatma onayı verecek kişi için hazırlanan sonuç raporudur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_413.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Sonuç Raporu:** Sonuç Raporu sekmesinde Sonuç Raporu açıklama bilgisinin girildiği alandır.

Şikayet Detayı ekranında Sonuç Raporu sekmesinde Dış Müşteri Şikayetleri modülü  parametrelerinden 106 numaralı “Müşteri şikayetinden DÖF oluşturulabilsin mi?” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_414.png)

Parametre aktif edildikten sonra  Müşteri Şikayet ilgili DÖF kaydının  açılıp, açılmaması veya DÖF kaydı açıldığı takdirde DÖF işlemleri -Yeni Kayıt ekranında yada mevcutta kayıtlı DÖF Kayıtlarında seçilme işlemi ile seçenekler  sunulur.

![ref84]

- Şikayet kaydında DÖF ile ilgili “DÖF’e ihtiyaç yok” seçeneği seçilirse Müşteri şikayetinde DÖF kaydı açılmaz.
- Şikayet kaydında DÖF ile İlgili “Yeni DÖF Aç” seçeneği seçilirse Şikayet detayı ekranında Sonuç Raporu sekmesinde ilgili alanlar bilgiler girildikten sonra kayıt işleminde sonra  DÖF İşlemleri-Yeni Kayıt ekranı açılarak müşteri şikayeti DÖF kaydı ile devam eder.
- Şikayet kaydında DÖF ile ilgili “Listeden Seç” seçeneği seçilirse, sistemde tanımlı DÖF’lerin yer aldığı DÖF listesinin yer aldığı alan görüntülenir. Görüntülenen bu alanda mevcutta kayıtlı DÖF’ler yer alır ve bu DÖF kayıtlarından seçim işlemi yapılır.

  ![ref85]

Görüntülenen alanda ![ref86] butonu tıklanarak mevcutta kayıtlı olan DÖF listesinde DÖF kaydı seçilir ve DÖF kaydının hangi aşamada ise o aşamadan şikayet kaydı DÖF kaydında devam edilir.

**Ek Dosyalar:** Sonuç Raporu sekmesinde bu aşamada varsa bu sonuç raporu ile ilgili  kanıt doküman, fotoğraf gibi ek dosya yükleme işlemi butonlar yardımıyla  yapılır. Sonuç raporu aşamasında ek dosya yükleme işlemi zorunlu getirilmesi işlemi için Dış Müşteri Şikayetleri modülü parametrelerinde 167 numaralı “Sonuç raporunda ek dosya zorunlu olsun” parametresinin parametre değeri “Evet”seçilerek parametre aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_418.png)

Parametre aktif edildiğinde Sonuç raporu aşamasında ek dosya yükleme işlemi yapılmadan sonuç raporu kayıt  işlemi gerçekleşmez.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_419.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref81]: Ek dosya sisteme yüklenir.

![ref72]: Yüklenen ek dosya bilgisi görüntülenir.

![ref15]: Yüklenen ek dosya bilgisi silinir.

![ref81]  butonu tıklanarak  sonuç raporu aşamasında Şikayet Detayı kaydına Sonuç Raporu aşamasında ek dosya eklenir. Birden çok ek dosya eklenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_420.png)

Açılan ekranda Sonuç Raporu yazılır. Sonuç Raporu’na eklenmek istenen ek dosyalar, varsa eklenebilir. Gerekli alanlar ilgili bilgiler girildikten sonra ekranın sol üst köşeside yer alan  ![ref11]  butonu tıklanarak Sonuç Raporu kaydedilir ve Şikayet kapatma onayına gider.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_421.png)

Sonuç raporu yazılma işlemi kaydedildikten sonra, önceden belirlenen Şikayet kapatma sorumlusuna bekleyen işlerine **“Kapatılacak Dış Müşteri Şikayetleri Listesi ”** işi olarak görev düşecektir.
##### **6.2.1.12.İzleme**
Şikayetin kapatılması aşamasında bazen belirli tarih aralığına kadar aynı problemle karşılaşılacak mı diye Şikayet kapatılmaz ve izlemeye alınabilir. İzleme işlemi şikayetin devam edip edilmediğini kontrol amaçlı belirli bir zaman diliminde izleme sorumlusuna görev ataması yapıldığı süreçtir. İzleme sorumlusu belirlenen tarihlerde şikayetin devam edip etmediğini üzerine atanan görevden dolayı kontrol eder. Yapılan aksiyonların yeterliliğini, etkinliğini veya düzgün yapılıp yapılmadığını atanan bu görevle izleyerek rapor yazma işlemi yapar.

Şikayet Kaydı sonuç raporu aşamasında sonra Şikayet  Kapatma sorumlusunun Bekleyen işlerinde “**Kapatılacak Dış Müşteri Şikayetleri Listesi”**  işi olarak görev  düşer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_422.png)

İlgili görevdeki Şikayet No  alanındaki Şikayet  kodu linki tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_423.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref87] :Şikayet detayı ile ilgili tüm bilgileri görüntüleme işlemi yapılır.

![ref88] : Kapatma onayı verecek kişi yapılan aksiyonların yeterli olmadığı kararı verdiğinde, eksik kalan aksiyonları tanımlama işlemi yapılır. 

![ref89] : Yapılan aksiyonların yeterliliğini, etkinliğini veya düzgün yapılıp yapılmadığını farklı bir kişi tarafından izlenerek rapor yazma görevi verilme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_427.png) :Kapat Onayını ve yeterlilik bilgisinin yazılma işlemi yapılarak Şikayet kaydı kapatılır.

![ref8]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref9]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref10]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranında kullanıcı bazlı tasarlama işlemi yapılır.

Onay Bekleyen Şikayetler ekranında İzleme işlemi yapmak için  ![ref89] botunu tıklanır

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_428.png)

Dış Müşteri Şikayetleri modülü parametrelerinde 64 numaralı “İzleme Raporu Kullanılacak mı? (E/H)  parametre değeri “Evet” seçilerek parametre aktif edilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_429.png)

Parametre aktif edildikten sonra Şikayet Detayı ekranında İzleme sekmesi görüntülenir ve izleme özelliği kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_430.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref1]: Yeni bir izleme bilgisi tanımlanır.

![ref5]: Veriler Excel’ e aktarılır.

![ref8]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref9]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref10]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_431.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Sorumlu:** İzleme -Yeni Kayıt ekranında Sorumlu kişini bilgisinin ![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_432.png) butonu tıklanarak açılan sistemde tanımlı olan Personel listesinden seçilebildiği alandır.

**İzleme Bitiş Tarihi:** İzleme -Yeni Kayıt ekranında açılan Takvim alanından İzleme Bitiş Tarihi seçildiği alandır.

**İzleme Bilgisi:** İzleme -Yeni Kayıt ekranında İzleme açıklama bilgisinin girildiği alandır.

**Ek Dosyalar:** İzleme -Yeni Kayıt ekranında bu aşamada varsa bu izleme ile ilgili  kanıt doküman, fotoğraf gibi ek dosya yükleme işlemi butonlar yardımıyla  yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_433.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref81]: Ek dosya sisteme yüklenir.

![ref72]: Yüklenen ek dosya bilgisi görüntülenir.

![ref15]: Yüklenen ek dosya bilgisi silinir.

![ref81]  butonu tıklanarak  izleme aşamasında Şikayet kaydınana ek dosya eklenir. Birden çok ek dosya eklenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_434.png)

Açılan İzleme -Yeni Kayıt ekranında izlemeden sorumlu kişi bilgisi girilir, izlemenin bitiş tarihi belirlenir, izleme bilgisi girilir, varsa izleme ile alakalı ek dosya, doküman vb. eklenebilir. Gerekli alanlar doldurulduktan sonra sol üst köşede yer alan  ![ref11]  butonu tıklanarak İzleme kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_435.png)

Dış Müşteri Şikayetleri modülü parametrelerinden 185 numaralı “İzleme zorunlu olsun mu?” parametre değeri “Evet” seçilerek parametre aktif edilerek Dış Müşteri Şikayetleri modülünde İzleme aşamasının zorunlu olması  sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_436.png)

Bu parametreye göre Şikayet kaydında izleme aşaması yapılmadan Şikayet kaydı kapatılmaz.

Dış  Müşteri Şikayetleri Modülü parametrelerinde 186 numaralı “Varsayılan izleme sorumlusu rol kodu” parametresine rol kodu tanımlanılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_437.png)

Tanımlanan bu Rol kodu Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Rol Tanımlama menüsünde modül olarak Dış Müşteri Şikayetleri modülü seçilerek listelenen rol tanımlarından alınır. İzleme Görevi atama işleminde izleme sorumlusu alanında parametreye tanımlı bu rol kodundaki kişiyi sistem otomatik olarak varsayılan olarak getirir.

İzleme görevinin atama işleminden sonra İzleme sorumlusunun  Bekleyen İşlerimde “**İzleme Raporu Yazılacak Dış Müşteri Şikayetleri Listesi**” iş olarak görev düşer. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_438.png)

İzleme Sorumlusu ilgili görevdeki Şikayet No alanındaki Şikayet Kodu linki tıklayarak Şikayet Detayı ekranında İzleme sekmesini görüntüler.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_439.png)

**Ekranda bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_440.png):Yeni bir izleme işlemi açılır.

![ref90]:İzleme Raporu yazılma işlemi yapılır.

![ref5]: Veriler Excel’ e aktarılır.

![ref8]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref9]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref10]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranında kullanıcı bazlı tasarlama işlemi yapılır.

![ref90] butonu tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_442.png)

İzleme raporu yazılacağı ekran açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_443.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**İzleme Raporu:** İzleme Raporu ekranında  İzleme Raporu açıklama bilgisinin yazıldığı alandır.

**Ek Dosyalar:** İzleme Raporu ekranında bu aşamada varsa bu İzleme raporu ile ilgili  kanıt doküman, fotoğraf gibi ek dosya yükleme işlemi butonlar yardımıyla  yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_444.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref81]: Ek dosya sisteme yüklenir.

![ref72]: Yüklenen ek dosya bilgisi görüntülenir.

![ref15]: Yüklenen ek dosya bilgisi silinir.

![ref81]  butonu tıklanarak istenirse İzleme raporu aşamasında Şikayet kaydınana ek dosya eklenir. Birden çok ek dosya eklenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_445.png)

Açılan Şikayet Detayı  ekranında İzleme Raporu sekmesinde  İzleme Raporu bilgisi yazılır varsa izleme raporu ile ek dosya butonlar yardımıyla yükleme işlemi yapılır.  Gerekli alanlar doldurulduktan sonra sol üst köşede yer alan  ![ref91]  butonu tıklanarak izleme raporu kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_447.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_448.png)
##### **6.2.1.13.Kapatma**
Şikayet  Kaydı izleme raporu aşamasında sonra Şikayet Kapatma sorumlusunun Bekleyen işlerinde “**Kapatılacak Dış Müşteri Şikayetleri Listesi**”  iş olarak görev  düşer. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_449.png)

İlgili görevdeki Şikayet No alanındaki Şikayet Kodu linki tıklanarak ilgili Şikayet kaydı  görüntüler. Bu aşamada şikayetler ilgili alınan aksiyonlar sonucu şikayetin giderildiği  görüldüğünde Süreç Şikayet kaydının kapatma aşaması ile devam edilir.Şikayet Kodu  üzerine tıklayarak “**Onay Bekleyen Şikayetler”**  ekranına gelir.Bu aşamada seçenekler sunulur. Bu aşamada Şikayet kaydı ile bilgileri görüntüler. Kapatma onayı verecek kişi yapılan aksiyonların yeterli olmadığı kararı verdiğinde, eksik kalan aksiyonları tanımlama süreci başlatabilir. Süreç Aksiyonlar sekmesinde yeni Aksiyonların planlanması ve bu Aksiyonlara bağlı olarak Sonuç raporu sekmesinde sonuç raporun yazılması işlemini şeklinde aşama aşama devam eder. Bir başka seçenek olarak İzleme açılabilir. Alınan Aksiyonların yeterli olup, olmadığı kontrol amaçlı izleme sorumlusu atanarak ve izleme sorumlu izleme raporu yazma şeklinde süreç devam edebilir. Şikayet giderildiği  kesin olarak ulaşıldığında  Şikayet kapatılmasına karar verilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_450.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref87] : Şikayet Kaydı ile ilgili tüm bilgileri görüntüleme işlemi yapılır.

![ref88] : Kapatma onayı verecek kişi yapılan aksiyonların yeterli olmadığı kararı verdiğinde, eksik kalan aksiyonları tanımlama işlemi yapılır. 

![ref89] : Yapılan aksiyonların yeterliliğini, etkinliğini veya düzgün yapılıp yapılmadığını farklı bir kişi tarafından izlenerek rapor yazma görevi verilme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_451.png) :Kapat Onayını ve yeterlik bilgisinin girme işlemi yapılarak Şikayet kaydı kapatılır.

![ref8]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref9]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref10]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranında kullanıcı bazlı tasarlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_452.png) butonu tıklanır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_453.png)

Şikayet  Kapatma ekranına  açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_454.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Yeterlilik Bilgisi:** Şikayet Detayı ekranında Kapatma sekmesinde Yeterlilik açıklama bilgisinin girildiği alandır.

**Onay Notu:** Şikayet Detayı ekranında Kapatma sekmesinde Onay Notu açıklama bilgisinin girildiği alandır.

**Şikayet Kategorisi:** Şikayet Detayı ekranında Kapatma Sekmesinde Şikayet Kategorisi bilgisinin sistemde tanımlı Şikayet Kategorisi listesinden seçilebildiği alandır.

**Şikayet Maliyeti:** Şikayet Detayı ekranında Kapatma sekmesinde Şikayet Maliyeti bilgisinin girildiği alandır.

**Ek Dosyalar:** Şikayet Detayı  ekranında Kapatma sekmesinde varsa Ek Dosya yüklendiği kısımdır.

**Hata Dağılımları;**

Dış Müşteri Şikayetleri modülünde hata maliyetlerinin  tanımlama işleminin yapıldığı, departmanlara, personellere göre hata dağılımlarının, departmanlara personellere göre dağılımlarının  yüzde oranın belirlendiği sekmedir.Hata dağılımları genelde otomativ sektöründe kullanılmaktadır. Dış Müşteri Şikayetleri modülü parametrelerinde 86 numaralı “Hata Maliyetleri Modülü Aktif (E/H)” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_455.png)

Parametre aktif edildikten sonra Şikayet Detayı ekranından Hata Dağılımları sekmesi görüntülenir ve hata dağılımları özelliği kullanılır. Şikayet Detayı ekranında Hata Dağılımları sekmesi tıklanarak Hata dağılımları ekranı görüntülenir. Hata dağılımları sekmesinde Hatalarının personellere ve departmanlara göre dağılımlarının ve yüzde oranlarının girilmesi işlemide yapılır. 

Dış Müşteri Şikayetleri Modülü parametrelerinde 27 numaralı “Hataların Bölümlere Ayrılması Modülü Aktif” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_456.png)

Parametre aktif edildikten sonra Şikayet Detayı ekranında Hata Dağılımı sekmesinde Hataların Departmanlara Dağılımı alanı görüntülenir ve Hataların departmanlara dağılımın yüzde oranları girilerek bu özellik kullanılır.

Şikayet Detayı ekranında Hata Dağılımı sekmesinde hatalarının personellere dağılımının yapılması için 28 numaralı “Hataların Personele Dağılımı Modülü Aktif” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_457.png)

Parametre aktif dildikten sonra Şikayet Detayı ekranında Hata Dağılımı sekmesinde Hatalarının Personellere Dağılımı alanı görüntülenir ve personellere göre hataların dağılım oranları girilerek bu özellik kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_458.png) ![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_459.png)

Dış Müşteri Şikayetleri Modülü parametrelerinde 155 numaralı “Hata dağılımları zorunlu olsun(E/H)” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_460.png)

Parametre aktif edildikten sonra Hata Dağılımları sekmesinde  bulunan alanların bilgi girişi yapılmadan şikayet kaydı kapatılmaz.

**Değerlendirme;**

Dış Müşteri Şikayetleri modülü parametrelerinde “Değerlendirme kullanılacak mı? (E/H)” parametre değeri “Evet” seçilerek parametre aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_461.png)

Parametre aktif edildiğinde Şikayet Detayı ekranında  Değerlendirme sekmesi görüntülenir ve alt yapıda tanımlanan değerlendirme kategorilerine göre  şikayetin değerlendirme işlemi yapılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_462.png) **Ekrandaki bulunan butonlar yardımıyla;**

![ref92]:Yeni bir değerlendirme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_464.png):Listede seçili değerlendirme işlemi güncellenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_465.png):Listede seçili değerlendirme işlemi silinir.

Şikayet Detayı ekranında ![ref92]  butonu tıklanarak Değerlendirme/Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_466.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Değerlendirme Kategorisi:** Değerlendirme-Yeni Kayıt ekranında açılır liste tıklanarak açılan Değerlendirme Kategori listesinde seçim yapıldığı alandır. Sistem Altyapı Tanımları/Dış Müşteri Şikayetleri/Değerlendirme kategori tanımlama menüsünde tanımlı değerlendirme kategorileri listede görüntülenir.

**Değerlendirme Alt Kategorisi:** Değerlendirme-Yeni Kayıt ekranında açılır liste tıklanarak açılan Değerledirme Alt Kategorsi listesinden seçim yapıldığı alandır.

**Açıklama:** Değerlendirme-Yeni Kayıt ekranında Değerlendirme açıklamasının yazıldığı alandır.

Değerlendirme-Yeni Kayıt gerekli alanlar doldurulduktan sonra sol üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_467.png)  butonu tıklanarak kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_468.png)
##### **6.2.1.14.Görüntüleme**
Şikayet Detayı ekranında Görüntüle sekmesi tıklanarak Şikayet kaydının aşama aşama işlem basamaklarının detay bilgileri görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_469.png)

Tarihçe sekmesinde Şikayet Açma, Gelişme Raporu ve Aksiyon Açma gibi işlem adımları  ile onay durumlarının bilgisi yer aldığı onay geçmişi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_470.png)

Şikayet Detayı ekranında Şikayet Kapatma sekmesinde gerekli alanlari ilgili bilgiler girildikten sonra ekranın sol üst köşesindeki ![ref93]  butonu tıklanarak Şikayet kapatma kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_472.png)

Dış Müşteri Şikayetleri işlemleri ekranında liste sekmesinde  kapatma aşaması yapılan şikayet kaydının durum kapalı statüsünde listede yer alır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_473.png)
##### **6.2.1.15.Müşteri Şikayetleri Kayıt Bakım** 
Listede seçili Şikayet Kaydı üzerinde  ilgili düzenleme/değişiklik/güncelleme  işlemi yapılır.Kayıt bakım özelliği işlemi yapma yetkisinde sahip kullanıcılar Şikayet kaydı üzerinde  her türlü değişiklik yapma yetkisine sahip olurlar. Şikayet kaydı  kapalı bir durumda olsa bile kayıt üzerinde her türlü değişiklik yapılabilir. Bu işlemleri yapabilmek için kullanıcının, Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Modül Yöneticisi menüsünde, Dış Müşteri Şikayetleri Modülünde modül yöneticisi olarak atanması gerekir. Modül yöneticisi olarak atanan kullanıcıların ekranlarında  ![ref94]  butonu görüntülenir ve buton ile bir Şikayet kaydı üzerinde istenilen bilgileri düzenlenebilirler.

Dış Müşteri Şkayetleri İşlemleri ekranında durumu kapalı statüsündeki Şikayet Kaydı seçili iken ![ref94]  butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_475.png)

**Ekranda bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_476.png):Şikayet kaydı gelişme raporu aşamasına döndürülme işlemi yapılır.Kapalı statüsündeki Şikayet kaydı Gelişme raporu aşamasında başlar.Şikayet kaydındaki süreç Gelişme raporu aşaması ile devam eder.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_477.png):Şikaye kaydı sonuç raporu aşamasına döndürülme işlemi yapılır.Kapalı statüsündeki Şikayet  kaydı Sonuç raporu aşamasında başlar.** Şikayet kaydındaki süreç  Sonuç  raporu aşaması ile devam eder.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_478.png):Yapılan değişiklikler ilgili kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_479.png):Şikayet  Kaydı ile ilgili DÖF kaydı varsa ilgili DÖF kaydı görüntülenme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_480.png)

Müşteri Şikayetleri kayıt bakım ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_481.png) butonu tıklanarak ilgili alanlar üzerinde değişiklik ve düzenleme işlemi yapılır. ![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_482.png)  butonu tıklanarak ilgili kaydın silinme işlemi yapılır. ![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_483.png) (Yayınla)  butonu ile kayıt ile ilgili açma bildirimi yayınlanır.. ![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_484.png) butonu tıklanarak Kök Neden Analizi sekmesinde yeni bir Kök Neden ekleme işlemi yapılır. Kayıt Bakım özelliği kullanılarak ilgili alanlar üzerinde Şikayet kaydının aşamalarında düzenleme işlemi yapılır
##### **6.2.1.16.Dış Müşteri Şikayeti İptal İşlemi**
Listede seçili Şikayet kaydının iptal işlemi yapılır. İptal işlemi silme işleminde farklı bir işlemdir. Şikayet kaydının  işleyişi durur fakat sistem de kayıtlı olmaya devam eder. Bir onay akış çerçevesinde çalışır. ![ref95] butonu tıklanarak iptal işlemi yapılır.Açılan Dış Müşteri Şikayeti İptal - Kayıt Güncelle ekranında Şikayet kaydının İptal nedeni bilgisi yazılarak kayıt işlemi yapılır. Kayıt işleminde sonra Şikayet kaydı akıştaki kişinin İptal onayı gönderilir.Bunun için Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Akış Tanımlama menüsünde Şikayet İptal Onayı akışının kurgulanması ve akıştaki rolün atanması gerekir. Akış Tanımlama işlemi yapılan iptal işleminde Alt Modül Tanımlama kısmında akışın kontrolünün yapılması gerekmektedir. Şikayet İptal işleminin kullanılması için kullanıcının modül yönetici olması ve Dış Müşteri Şikayetleri modülü parametrelerinde 87 numaralı “İptal fonksiyonu kullanılacak mı? “ parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_486.png)

Parametre aktif edildikten sonra Modül Yöneticinin Dış Müşteri Şikayetleri İşlemleri ekranında ![ref95] butonu görüntülenir ve  iptal fonksiyonu özelliği kullanılır. Dış Müşteri Şikayetleri İşlemleri  ekranında liste sekmesinde listede Şikayet kaydı seçilerek ![ref95] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_487.png)

Açılan İç Müşteri Şikayeti İptal - Kayıt Güncelle ekranında İptal Nedeni alanın Şikayet kaydının neden iptal edildiği bilgisi yazılır

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_488.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Kayıt No:** Dış Müşteri Şikayeti İptal - Kayıt Güncelle ekranında şikayetin kayıt no bilgisininin sistem tarafından verildiği alandır.	

**Açan:** Dış Müşteri Şikayeti İptal - Kayıt Güncelle ekranında şikayetin kim tarafından açıldığı bilgisinin sistem tarafından verildiği alandır.**	

**Şikayet Açılma Tarihi:** Dış  Müşteri Şikayeti İptal - Kayıt Güncelle ekranında şikayetin açılma tarihi bilgisinin sistem tarafından verildiği alandır.**	

**Şikayet Tanımı:** Dış  Müşteri Şikayeti İptal - Kayıt Güncelle ekranında şikayet tanım bilgisinin sistem tarafından verildiği alandır.

**İptal Nedeni:** Dış  Müşteri Şikayeti İptal - Kayıt Güncelle ekranında şikayet neden- sebep iptal edildiği bilgisinin yazıldığı alandır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_489.png)

Dış Müşteri Şikayeti İptal - Kayıt Güncelle ekranında Şikayet kaydının iptal nedeni bilgisi yazılarak, gerekli alanlar doldurulduktan sonra sol üst köşede yer alan  ![ref11]  butonu tıklanarak iptal işlemi akıştaki kişinin onayına sunulur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_490.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_491.png)

Onaydaki kişinin Bekleyen İşlerinde “**İptal Onayı Bekleyen Dış Müşteri Şikayetleri**” işi olarak görev düşer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_492.png)

İlgili görevdeki Şikayet No alanındaki Şikayet Kodu linki tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_493.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref60]: İlgili Şikayet kaydının görüntüleme işlemi yapılır.

![ref62] : Şikayet kaydının onaylama işlemini yapmak için kullanılır. 

![ref63] :Şikayet kaydında girilen bilgiler uygun olmadığı durumda, Şikayet kaydını reddetmek için kullanılır. 

![ref64]  : Çok fazla onaylanması gereken Şikayet kaydı olması durumunda filtre seçeneğinden bilgiler süzülerek arama yapmak istendiğinde kullanılır.

![ref8]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref9]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref10]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranında kullanıcı bazlı tasarlama işlemi yapılır.

Onay Bekleyen Şikayetler ekranında ![ref60] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_494.png)

Açılan Görüntüleme ekranında Şikayet kaydı ile ilgili sekmeler tıklanarak Detay bilgileri görüntülenir.

**Görüntüle sekmesi;**

Şikayet detayının açma aşamasından başlayara son aşamaya kadar olan bütün bilgileri görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_495.png)

**Tarihçe sekmesi;**

Açılan Şikayet  ile ilgili Şikayet Açma, Şikayet iptal gibi işlem adımları ve onay durum bilgileri yer aldığı onay geçmişi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_496.png)

**Onay Bekleyen Şikayetler** ekranında ![ref96] butonu tıklanarak Ret nedeni girilerek Şikayet kaydının iptal işleminin ret edilme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_498.png)

Açılan Şikayet Ret ekranında Şikayet kaydının iptal işlemi Ret etme işlemi yapılır ve  Ret Nedeni bilgisi yazılması zorunludur. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_499.png)

Onay Bekleyen Şikayetler ekranında **![ref97]**  butonu tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_501.png)

Açılan Şikayet Onay ekranında  Onay notu alanında Onay notu bilgisi yazılarak ![ref67] butonu tıklanarak  Şikayet kaydı iptal işlemi onaylanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_502.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_503.png)
##### **6.2.1.17.Şikayet Kaydını Silme İşlemi**
Dış Müşteri Şikayeti İşlemleri ekranında liste sekmesinde listede seçili Şikayet kaydının silme işlemi yapılır. Silme işleminin yapılması için kullanıcının modül yönetici olarak tanımlı olması gerekmektedir. Modül Yönetici olarak tanımlı kullanıcının Dış Müşteri Şikayet İşlemleri ekranında ![ref98] butonu  görüntülenir. Dış Müşteri Şikayeti işlemleri ekranında liste sekmesinde listede  Şikayet kaydı seçilerek ![ref98]  butonu tıklanarak Şikayet kaydının silinme işlemi yapılır.
Dış Müşteri Şikayeti işlemleri ekranında liste sekmesinde listede Dış Müşteri Şikayeti kaydı seçilir ve ![ref98]  butonu tıklanır.,

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_505.png)

Sistem tarafından “Seçili kaydı silmek istediğinizden emin misiniz?” uyarı mesajında “Tamam” butonu tıklanarak listede seçili Şikayet kaydının silinme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_506.png)

Silme işlemi yapılan Şikayet kayıtları veritabandan da siliniyor ve bu verilere sistemde ulaşılmıyor.
#### **6.2.2.Dış Müşteri Talebi**
**Menü Adı**: Entegre Yönetim Sistemi/Dış Müşteri Şikayetleri/** Dış  Müşteri Talebi

Dış  Müşteri Talebi tanımlama işleminin gerçekleştiği menüdür. Bu menü fonksiyonel olarak Dış  Müşteri Şikayeti İşlemleri ile aynı işleve sahiptir. Farkı ise daha sade bir menü yapısında olmasıdır. Dış Müşteri Şikayetleri İşlemleri menü yetkisi verilmeyecek kullanıcılar için kurgulanmıştır. Sadece talepte bulunabilirler, onun haricinde şikayet ile ilgili herhangi bir işlem yapamazlar. Talep girildikten sonra açılma onayına düşer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_507.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Müşteri:** Şikayet Talebi ekranında şikayetin olduğu Müşteri bilgisinin ![ref99] butonu tıklanarak açılan sistemde tanımlı olan Müşteri listesinden seçilebildiği alandır.	 	

**Şikayet Tanımı:** Şikayet Talebi ekranında şikayetin tanım bilgisinin yazıldığı alandır.		

**Şikayet Detayı:** Şikayet Talebi ekranında şikayetin detay bilgisinin yazıldığı alandır.		

**İş Yeri:** Şikayet Talebi ekranında şikayetin ilgili olduğu işyeri bilgisinin ![ref99] butonu tıklanarak açılan sistemde tanımlı olan İş yeri listesinden seçilebildiği alandır.	

**Ürün:** Şikayet Talebi ekranında şikayetin ilgili olduğu ürün bilgisinin ![ref99] butonu tıklanarak açılan Ürün listesinde seçildiği alandır.

**Ek Dosyalar:** Dış Müşteri Talebi ekranında varsa bu aşamada Dış Müşteri Talebi ile ilgili  kanıt doküman, fotoğraf gibi ek dosya yükleme işlemi butonlar yardımıyla  yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_509.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref81]: Ek dosya sisteme yüklenir.

![ref82]: Yüklenen ek dosya bilgisi görüntülenir.

![ref15]: Yüklenen ek dosya bilgisi silinir.

![ref81]  butonu tıklanarak  Şikayet Talebi  aşamasında ek dosya eklenir. Birden çok ek dosya eklenebilir.

Şikayet Talebi ekranında gerekli alanlar doldurulduktan sonra sol üst köşede yer alan  ![ref6]   butonuna tıklanarak Şikayet Talebini sistem onaya gönderir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_510.png)

Onaydaki kişiye sistem mail yollarken aynı zamanda bekleyen işlerine **“Onay Bekleyen Dış Müşteri Şikayetleri Listesi”** iş olarak görev düşer. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_511.png)

İlgili görevdeki Şikayet No alanındaki şikayet kodu linki tıklanarak **“Onay Bekleyen Şikayetler”** ekranı açılır. Bu ekranda şikayet kaydı ile görüntüleme, güncelleme, reddetme ve şikayet kapatma işlemleri yapılır. Onay Bekleyen Şikayetler ekranında güncelleme işlemi yapıldığında Şikayet ile ilgili zorunlu alanlar doldurulmadan kayıt işlemi yapılmaz.
#### **6.2.3.Onay Bekleyen Dış Müşteri Şikayetleri**
**Menü Adı**: Entegre Yönetim Sistemi/Dış Müşteri Şikayetleri/Onay Bekleyen Dış Müşteri Şikayetleri

Onay bekleyen dış müşteri şikayetlerinin onaylanması işlemlerinin gerçekleştiği menüdür. Onayda bekleyen Dış Müşteri Şikayetlerini  task üzerinde (bekleyen işlerim) takip etmek istemeyen kullanıcılar Entegre Yönetim Sistemi/Dış Müşteri Şikayetleri/ Onay Bekleyen Dış Müşteri Şikayetleri mesünde görüntüleyebilir. Modül yöneticisi yetkisi olan kullanıcılar Dış Müşteri Şikayetleri durumunu takip etmek için Onay Bekleyen Dış Müşteri Şikayetleri sayfasını kullanılır.Bu ekranda şikayetin  Gelişme Raporu, şikayeti kapatma gibi statülerine göre butonlar değişmektedir.  

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_512.png)

**Ekranda bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_513.png): İlgili Şikayet kaydının görüntüleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_514.png) : İlgili Şikayet kaydı ile değişiklik/düzenleme/güncelleme yapılması işlemi yapılır. Eğer talepten açılan Şikayet kaydı ise zorunlu alanları doldurmadan onaylama işlemi yapmamıza sistem izin vermeyecektir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_515.png) : Şikayet kaydı onaylama işlemini yapılır. Onay işleminden sonra ilgili Şikayet kaydı Ekip Liderinin önüne düşer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_516.png) : Şikayet kaydı girilen bilgiler uygun olmadığı durumda Şikayet kaydı reddetme işlemi yapılır.Red edilen,  açan kişiye ret etme nedeniyle birlikte gönderilebilir. Ret ederken detay bilgi için ret veya kaydın iptali için ret edilebilir, buna bağlı olarak ilgili seçeneği seçmelidir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_517.png):Şikayet kaydı kapatılır.

![ref100]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref101]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref102]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranında kullanıcı bazlı tasarlama işlemi yapılır.

Onay Bekleyen Şikayetler ekranında ![ref60] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_521.png)

Açılan Görüntüleme ekranında Şikayet kaydı ile ilgili sekmeler tıklanarak Detay bilgileri görüntülenir.

**Görüntüle sekmesi;**

Şikayet detayının açma aşamasından başlayarak son aşamaya kadar olan bütün bilgileri görüntülenir. ![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_522.png)

**Tarihçe sekmesi;**

Açılan Şikayet  ile ilgili Şikayet Açma, Şikayet iptal  gibi işlem adımları ve onay durum bilgileri yer aldığı onay geçmişi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_523.png)

Onay Bekleyen Şikayetler ekranında ![ref61] butonu tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_524.png)

Açılan Şikayet Detayı ekranında görüntülenen sekmelerde ilgili alanlar üzerinde düzenleme ve değişiklik yapma işlemi yapılır. Şikayet talebinden gelen bir Şikayet kaydı ise zorunlu alanları doldurmadan onaylama işlemi yapmamıza sistem izin vermeyecektir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_525.png)

Şikayet Detayı ekranında yapılan değişikliklerin kaydedilmesi için ekranın sol üst köşesindeki ![ref103]  butonu tıklanılır. Onay Bekleyen Şikayetler ekranında **![ref104]** butonu tıklanarak Ret nedeni girilerek Şikayet kaydı ret edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_528.png)

Açılan Şikayet Ret ekranında Şikayet Detayı bilgileri kontrol edilerek uygun olmadığı görüldüğünde Şikayet  ret etme işlemi yapılır ve  Ret Nedeni bilgisi yazılması zorunludur. Red edilen açan kişiye ret etme nedeniyle birlikte gönderilebilir. Ret ederken detay bilgi için ret veya şikayet kaydın iptali için ret edilebilir, buna bağlı olarak ilgili seçeneği seçmelidir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_529.png)

Onay Bekleyen Şikayetler ekranında ![ref105] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_531.png)

Açılan şikayet detayı ekranında kapatma sekmesinde bu aşamada yeterlilik bilgisi ve onay notu bilgisi yazılarak şikayet kapatılma işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_532.png)

Onay Bekleyen Şikayetler ekranında **![ref62]**  butonu tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_533.png)

Açılan Şikayet Onay ekranında Onay notu alanında Onay notu bilgisi yazılarak ![ref67] butonu tıklanarak Şikayet kaydı onaylanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_534.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_535.png)
#### **6.2.4.Raporlar**
**Menü Adı**: Entegre Yönetim Sistemi/Dış Müşteri Şikayetleri/Raporlar

Dış Müşteri Şikayetleri Modülü ile ilgili raporlarının görüntülendiği kısımdır
##### **6.2.4.1.Dış Müşteri Şikayet Raporu**
**Menü Adı**: Entegre Yönetim Sistemi/Dış Müşteri Şikayetleri/ Raporlar/ Dış Müşteri Şikayet Raporu

Dış Müşteri Şikayetleri Modülü ile ilgili raporlarının görüntülendiği kısımdır. Dış Müşteri Şikayetleri Modülü parametrelerinde 62 numaralı “Dış müşteri şikayeti raporu şablon dosyası”parametresinde parametre değerine tanımlı rapor şablonuna göre bu rapor alınmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_536.png)

Rapor formatı şablonun tanımlamak için öncelikle Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Rapor Formatları Düzenleme menüsünde ilgili rapor formatının şablonun yüklü olması gerekmektedir. Rapor Formatları Düzenle menüsünde yüklü olan rapor formatının şablonun adı ve uzantısı  sağ tıkla/kopyala yöntemi ile kopyalarak ilgili parametreye sağ tıkla/yapıştır yönetimi yapıştırılarak tanımlanır. Tanımlanan rapor formatı şablonuna göre ilgili rapor bu menüden alınır.


![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_537.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref5]: Veriler Excel’ e aktarılabilir.

Dış Müşteri Şikayetleri Raporu ekranında ![ref5] (Excele aktar) butonu ile Excel formatında Dış Müşteri Şikayet Raporu görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_538.png)
##### **6.2.4.2.Onay Durum Raporu**
**Menü Adı**: Entegre Yönetim Sistemi/Dış Müşteri Şikayetleri/Raporlar/Onay Durum Raporu

Onayda bekleyen şikayetlerin hangi onayda, kimde, ne zamandır beklediği ile alakalı bilgiler verilmektedir. Onay Durum Raporu menüsüne gelinir. ![ref106] (Excele aktar) butonuna tıklanarak rapor alınabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_540.png) 

**Ekrandaki bulunan butonlar yardımıyla;**

![ref107]:Şikayet Detayı görüntülenir.

![ref106]: Veriler Excel’ e aktarılabilir.

Dış Müşteri Şikayeti Onay Durum Raporu ekranında şikayet kaydı seçili iken  ![ref107] butonu tıklanılır.  

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_542.png)

Açılan Görüntüle ekranında şikayetin detay bilgisi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_543.png)

Dış Müşteri Şikayeti Onay Durum Raporu ekranında ![ref106] (Excele aktar) butonu ile Excel formatında Onay Durum Raporu görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_544.png)
##### **6.2.4.3.Dış Müşteri Şikayetleri Aksiyon Raporu**
**Menü Adı**: Entegre Yönetim Sistemi/Dış Müşteri Şikayetleri/Raporlar/ Dış Müşteri Şikayetleri Aksiyon Raporu

Bu rapor Dış Müşteri Şikayetleri modülünde aksiyonların durumunu ve bilgilerini göstermektedir. Dış  Müşteri Şikayetleri kayıtlarının hem geneline hem de aksiyonlarına ait bilgiyi aynı anda verebilen rapordur. Bu rapor formatı Dış Müşteri Şikayetleri modülü parametrelerinde 76 numaralı “Dış müşteri şikayeti aksiyon raporu şablon dosyası”parametresine tanımlı raporu göre gelmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_545.png) Rapor Formataları düzenleme menüsünde yüklenen rapor formatı şablonun adı ve uzantısı ile birlikte ilgili parametreye tanımlama işlemi yapılırak  Dış Müşteri Şikayetleri Aksiyon Raporu  ekranında raporunun alınma işlemi yapılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_546.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref5]: Veriler Excel’ e aktarılabilir.

Dış Müşteri Şikayetleri Aksiyon Raporu ekranında **![ref16]**(Excel’e aktar) butonu ile Excel formatında Dış Müşteri Şikayetleri Aksiyon Raporu görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_547.png)

##### **6.2.4.4.Tekrar Eden Kayıtlar Raporu**
**Menü Adı**: Entegre Yönetim Sistemi/Dış Müşteri Şikayetleri/Raporlar/ Tekrar Eden Kayıtlar Raporu

Sistemde bir kullanıcı için istenen konularda tekrar eden kayıtları gösteren  menüdür.Açılan ekranda  ilk olarak Tekrar Eden Kayıtlar Raporu Şablonu menüsünden raporda çekilecek alanlar seçilerek Tekrar Eden Kayıtlar Raporu Şablonları tanımlama işlemi yapılır.Daha sonra Entegre Yönetim Sistemi/ Dış Müşteri Şikayetleri /Raporlar/Tekrar Eden Kayıtlar raporundan ilgili rapora ulaşılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_548.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref4]: Kayıtlar filtrelenerek arama yapılabilir.

![ref5]: Veriler Excel’ e aktarılabilir.

Entegre Yönetim Sistemi/ Dış Müşteri Şikayetleri /Raporlar/Tekrar Eden Kayıtlar raporundan Rapor Şablonu alanında ilgili rapor şablonu seçilir 

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_549.png)

Tekrar Eden Kayıtlar raporunda Rapor şablonu alanında ilgili rapor şablonu seçildikten sonra ve ![ref5] (Excel Aktar) butonu tıklanarak excel formatında Tekrar Eden Kayıtla” r raporu alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_550.png)
##### **6.2.4.5.Şikayet Detay Raporu**
**Menü Adı**: Entegre Yönetim Sistemi/Dış Müşteri Şikayetleri/Raporlar/Şikayet Detay Raporu

Şikayet Detayı ile ilgili bütün detay bilgilerinin yer aldığı rapordur. Bu rapor formatı Dış Müşteri Şikayetleri modülü parametrelerinde 197 numaralı “Detay Raporunda kullanılacak şablon”parametresine tanımlı raporu göre gelmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_551.png) Rapor Formataları düzenleme menüsünde yüklenen rapor formatı şablonun adı ve uzantısı ile birlikte ilgili parametreye tanımlama işlemi yapılır.Parametreye raporunun tanımlama işleminden sonra Şikayet Detay Raporu ekranında arama kriterlerindeki alanlara veri girişleri yapılarak ![ref16] (Excel Aktar) butonu tıklanarak Excel formatında istenilenen rapor alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_552.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref5]: Veriler Excel’ e aktarılabilir.

Şikayet Detay Raporu ekranında ![ref108] (Excele aktar)  butonu tıklanarak excel formatında “Şikayet Detay Raporu”  görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_554.png)
##### **6.2.4.6.Dış Müşteri Şikayetleri Özet Raporu**
**Menü Adı**: Entegre Yönetim Sistemi/Dış Müşteri Şikayetleri/Raporlar/ Dış Müşteri Şikayetleri Özet Raporu

Dış Müşteri Şikayetlerin genel bilgilerini ve açılma-kapanma tarih bilgileri ile onay mekanizmasındaki rollerin onay verme sürelerini detay bazda veren rapordur. Dış Müşteri Şikayetleri Modülü parametrelerinde 126 numaralı “Dış müşteri şikayeti özet raporu şablon dosyası” parametresinde tanımlı rapor şablonua göre bu rapor alınmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_555.png)

Rapor formatı şablonun tanımlamak için öncelikle Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Rapor Formatları Düzenleme menüsünde ilgili rapor formatının şablonun yüklü olması gerekmektedir. Rapor Formatları Düzenle menüsünde yüklü olan rapor formatının şablonun adı ve uzantısı  sağ tıkla/kopyala yöntemi ile kopyalarak ilgili parametreye sağ tıkla/yapıştır yönetimi yapıştırılarak tanımlanır. Tanımlanan rapor formatı şablonuna göre ilgili rapor bu menüden alınır.

Dış Müşteri Şikayetleri  Özet Raporu ekranındaki ilgili alanlar doldurularak istenen kriterler belirlenir ve ![ref5] (Excel’e aktar) butonu ile rapor alınır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_556.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref5]: Veriler Excel’ e aktarılabilir.

Dış Müşteri Şikayetleri Raporu ekranında ![ref5](Excele aktar)  butonu ile Excel formatında Dış Müşteri Şikayetleri Özet Raporu görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_557.png)
##### **6.2.4.7.Dış Müşteri Şikayetleri Aksiyon Raporu-2**
**Menü Adı**: Entegre Yönetim Sistemi/Dış Müşteri Şikayetleri/Raporlar/ Dış Müşteri Şikayetleri Aksiyon Raporu-2

Koşullu filtreler kullanılarak raporlar üretilmesini sağlayan menüdür. Dış Müşteri Şikayetleri Aksiyon Raporu ekranında Listesi ve Filtre sekmesi olmak üzere iki sekme karşımıza çıkar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_558.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref5]: Veriler Excel’ e aktarılabilir.

![ref4]: Kayıtlar filtrelenerek arama yapılabilir.

![ref8]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref9]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref10]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Dış Müşteri Şikayetleri Aksiyon Raporu ekranında Filtre sekmesinde arama kriterlerindeki alanlara  veri girişleri yapılarak ![ref4] (Ara) butonu tıklanarak filtreleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_559.png)

Dış Müşteri Şikayetleri Aksiyon Raporu ekranında  liste sekmesinde listede  Filtre sekmesinde yapılan filtre ayarlarına göre istenilen verilere ait raporların görüntülenmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_560.png)

Dış Müşteri Şikayetleri Aksiyon Raporu ekranında liste sekmesinde listeden Şikayet kaydı seçili iken   ![ref5] (Excele aktar)  butonu tıklanarak excel formatında “ Dış Müşteri Şikayetleri Aksiyon Raporu”  görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_561.png)
##### **6.2.4.8.Dış Müşteri Şikayetleri Aksiyon Raporu-3**
**Menü Adı**: Entegre Yönetim Sistemi/Dış Müşteri Şikayetleri/Raporlar/ Dış Müşteri Şikayetleri Aksiyon Raporu-3

Dış Müşteri Şikayetleri kayıtlarının hem geneline hem de aksiyonlarına ait bilgiyi aynı anda verebilen rapordur. Şikayet aksiyonların ağaç kırılımı şeklinde birbiriyle bağlantılı olarak verilen rapordur. Bu rapor formatı Dış Müşteri Şikayetleri  modülü parametrelerinde 177 numaralı “Dış müşteri şikayeti aksiyon raporu şablon dosyası” parametresine tanımlı raporu göre gelmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_562.png) Rapor Formataları düzenleme menüsünde yüklenen rapor formatı şablonun adı ve uzantısı ile birlikte ilgili parametreye tanımlama işlemi yapılırak  Dış Müşteri Şikayetleri Aksiyon Raporu-3 ekranında raporunun alınma işlemi yapılır. Dış Müşteri Şikayetleri Aksiyon Raporu ekranında Listesi ve Filtre sekmesi olmak üzere iki sekme karşımıza çıkar. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_563.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref5]: Veriler Excel’ e aktarılabilir.

![ref4]: Kayıtlar filtrelenerek arama yapılabilir.

Dış Müşteri Şikayetleri Aksiyon Raporu ekranında Filtre sekmesinde arama kriterlerindeki alanlara  veri girişleri yapılarak ![ref4] (Ara) butonu tıklanarak filtreleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_564.png)

Dış Müşteri Şikayetleri Aksiyon Raporu ekranında  liste sekmesinde listede  Filtre sekmesinde yapılan filtre ayarlarına göre istenilen verilere ait raporların görüntülenmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_565.png)

Dış Müşteri Şikayetleri Aksiyon Raporu ekranında liste sekmesinde listeden  ağaç krılım şeklinde görüntülen Şikayet kayıtlarında    ![ref5] (Excele aktar)  butonu tıklanarak excel formatında “Dış Müşteri Şikayetleri Aksiyon Raporu” görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_566.png)
#### **6.2.5.Grafikler**
**Menü Adı**: Entegre Yönetim Sistemi/Dış Müşteri Şikayetleri/Grafikler

Dış Müşteri Şikayetleri Modülünde grafiklerin görüntülendiği kısımdır.
##### **6.2.6.1.En çoklar Analizi**
**Menü Adı**: Entegre Yönetim Sistemi/Dış Müşteri Şikayetleri/ Grafikler/En çoklar Analizi

X ekseninde yer alan seçim tiplerine göre grafik oluşturulmasını sağlar. Oluşturulan bu grafik için de veri seçenekleri kullanılarak detay bazlı filtreleme yapılır. Örnek olarak  en çok hangi Şikayet kategorisine göre şikayet alındığı ve alınan bu şikayetlerin statülerin bilgisi verilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_567.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref109]: Belirlenen özelliklere göre ekrana grafiği çizdirir.

![ref47] : Grafiği açılır menüden seçilen format türüne (png,jpg,bmp,xls, vb. ) dönüştürerek dış ortama aktarılma işlemi yapılır.

![ref5]: Veriler Excel’ e aktarılabilir.

Grafik oluşturmak için iki ayrı ayar alanı bulunmaktadır. Bunlar Grafik ve Veri seçenekleridir. Adından da anlaşılacağı gibi grafiğin renkleri, eni-boyu gibi ayarlamaların yapıldığı alandır. Grafik ayarlarında önemli olan X ekseni ve Y eksenidir. X ekseninden sorgulamak istediğimiz, Şikayet Kategorisi, Sorumlu Departman, Ürün, süreç, durum, Ekip lideri, Kök Neden  vb. konulara göre grafik elde etmemizi sağlar. Y Ekseninden ise ilgili sorgunun sayı miktarı olan adet veya maliyetlere göre  ve Z eksenine göre istenen seçeneğe göre grafiğinin raporunun alınması sağlanır.Veri Seçeneklerinden ise belirlediğimiz grafik ayarlarından daha kısıtlı bir veri almak için filtreleme yapmak istenirse kullanılan alandır. Bar üzerine adet bilgisi yazılsın check box işaretlendiğinde grafikte bar üzerine adet bilgiside görüntülenir.Ayarlamalar tamamlandıktan sonra ![ref109] butonu tıklanarak grafik oluşur. Grafiği farklı formatlara almak istenirse, formatı sağdan seçtikten sonra![ref47] (Grafiği Aktar) soldan butona basıldığın da xls, png, jpg. Formatlarına grafik basılabilir. ![ref5] (Excel’e aktar) butonu ile de oluşan verileri Excel’e aktarması sağlanır. Bu veriler ile farklı formattaki grafiklerde oluşturulabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_569.png) ![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_570.png)

En çoklar Analizi ekranında![ref5] (Excel’e aktar) butonu tıklanarak En çoklar Analizi Grafiği Excel formatında alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_571.png)
##### **6.2.6.2.Zaman Boyutlu Analiz**
**Menü Adı**: Entegre Yönetim Sistemi/Dış Müşteri Şikayetleri/ Grafikler/Zaman Boyutlu Analiz

Şikayetlerin hangi zaman dilimlerinde sıklaştığı bilgisi bu grafik aracılığıyla elde edilir. Şikayet  kayıtları  ile ilgili seçilen verilere göre  aylık bazda grafiklerin alınma işlemi yapılır. “X ekseni” alanında seçilen değere göre, ![ref109]  butonuna tıklanarak pasta, çubuk ve StackedBar grafik olarak grafik raporu alınabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_572.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref109]: Belirlenen özelliklere göre ekrana grafiği çizdirir.

![ref47] : Grafiği açılır menüden seçilen format türüne (png,jpg,bmp,xls, vb. ) dönüştürerek dış ortama aktarılma işlemi yapılır.

![ref5]: Veriler Excel’ e aktarılabilir.

Şikayet Zaman Boyutlu Analizi raporu ekranında, grafik seçenekleri bölümünde gerekli seçimler gerçekleştirilir. Grafik Tipi kısmında X  ve Y ekseninde  yer alması istenen nitelik seçilir. Ana Tema, renk paleti alanlarında açılır liste seçeneklerinde seçim  yapılarak Ana tema, renk paleti özelliklerinden grafik özelleştirilebilir. Grafik seçenekleri  kısmında En çok alanında grafikte olması istenen en çok aralık belirlenir. 

Şikayet Zaman Boyutlu Analizi ekranında grafik  seçenekleri bölümünde gerekli seçimler gerçekleştirildikten sonra istenirse Grafik başlığı belirtilerek grafik oluşturmak için ![ref109]  butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_573.png) ![](https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_574.png)



[ref1]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_10.png
[ref2]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_11.png
[ref3]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_12.png
[ref4]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_13.png
[ref5]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_14.png
[ref6]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_18.png
[ref7]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_21.png
[ref8]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_22.png
[ref9]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_23.png
[ref10]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_24.png
[ref11]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_26.png
[ref12]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_37.png
[ref13]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_39.png
[ref14]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_54.png
[ref15]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_55.png
[ref16]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_56.png
[ref17]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_62.png
[ref18]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_66.png
[ref19]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_69.png
[ref20]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_72.png
[ref21]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_73.png
[ref22]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_74.png
[ref23]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_75.png
[ref24]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_83.png
[ref25]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_84.png
[ref26]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_85.png
[ref27]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_87.png
[ref28]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_89.png
[ref29]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_94.png
[ref30]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_103.png
[ref31]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_106.png
[ref32]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_111.png
[ref33]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_112.png
[ref34]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_113.png
[ref35]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_114.png
[ref36]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_127.png
[ref37]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_140.png
[ref38]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_142.png
[ref39]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_150.png
[ref40]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_154.png
[ref41]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_155.png
[ref42]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_156.png
[ref43]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_168.png
[ref44]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_171.png
[ref45]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_193.png
[ref46]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_195.png
[ref47]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_203.png
[ref48]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_210.png
[ref49]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_216.png
[ref50]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_223.png
[ref51]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_232.png
[ref52]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_235.png
[ref53]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_242.png
[ref54]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_243.png
[ref55]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_261.png
[ref56]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_262.png
[ref57]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_266.png
[ref58]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_273.png
[ref59]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_280.png
[ref60]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_285.png
[ref61]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_286.png
[ref62]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_287.png
[ref63]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_288.png
[ref64]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_290.png
[ref65]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_296.png
[ref66]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_299.png
[ref67]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_305.png
[ref68]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_323.png
[ref69]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_324.png
[ref70]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_325.png
[ref71]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_333.png
[ref72]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_334.png
[ref73]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_342.png
[ref74]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_367.png
[ref75]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_368.png
[ref76]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_369.png
[ref77]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_370.png
[ref78]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_371.png
[ref79]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_372.png
[ref80]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_375.png
[ref81]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_377.png
[ref82]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_378.png
[ref83]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_384.png
[ref84]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_415.png
[ref85]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_416.png
[ref86]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_417.png
[ref87]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_424.png
[ref88]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_425.png
[ref89]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_426.png
[ref90]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_441.png
[ref91]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_446.png
[ref92]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_463.png
[ref93]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_471.png
[ref94]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_474.png
[ref95]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_485.png
[ref96]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_497.png
[ref97]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_500.png
[ref98]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_504.png
[ref99]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_508.png
[ref100]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_518.png
[ref101]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_519.png
[ref102]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_520.png
[ref103]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_526.png
[ref104]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_527.png
[ref105]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_530.png
[ref106]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_539.png
[ref107]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_541.png
[ref108]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_553.png
[ref109]: https://docsbimser.blob.core.windows.net/imagecontainer/293fc584-cef1-4d5e-9bcf-fecf6bc57cf3_568.png
