---
title: Acil Durumlar
description: Acil Durumlar Yardım Dokümanı
sidebar_position: 48
---

:::tip Bilgi

İlgili konu başlığına sağ tarafta bulunan navigasyon yardımıyla hızlı bir şekilde ulaşabilirsiniz.

:::



**Acil Durumlar Modülü(v.5.26) Kullanıcı Yardım Dokümanı**

Modül Versiyonu: 5.26


## **1.GİRİŞ**  

6331  sayılı İş Sağlığı  ve  Güvenliği Yasası’nın  11’inci maddesine göre  işverenler; çalışma ortamı, kullanılan maddeler, iş ekipmanı ile çevre şartlarını dikkate alarak meydana gelebilecek acil durumları önceden değerlendirmek, çalışanları ve çalışma çevresini etkilemesi mümkün ve muhtemel acil durumları belirlemek ve bunların olumsuz etkilerini önleyici ve sınırlandırıcı tedbirleri almakla yükümlüdür.  İş yerlerinde acil durumların olumsuz etkilerinden korunmak üzere gerekli ölçüm ve değerlendirmelerin yapılması ve acil durum planlarının hazırlanması zorunludur.  6331 sayılı İş Sağlığı ve Güvenliği Yasası’nın 1’inci maddesine göre ise ciddi, yakın ve önlenemeyen tehlikenin meydana gelmesi durumunda işverenler; çalışanların işi bırakarak derhal çalışma yerlerinden ayrılıp güvenli bir yere gidebilmeleri için, önceden gerekli düzenlemeleri yapmak ve çalışanlara gerekli talimatları vermekle yükümlüdür. İş yerinde güvenli toplanma yeri belirlenmeli ve çalışanlar bu konuda bilgilendirilmelidir.

Bu konuda yapılacak çalışmalar, 18 Haziran 2013 tarih ve 28681 sayılı Resmi Gazetede yayınlanan “İş yerlerinde Acil Durumlar Hakkında Yönetmelik” hükümlerine uygun olarak yapılmalıdır.

## **2.AMAÇ**  

Bu  yardım kılavuzunun amacı,  QDMS kullanan  kuruluşların  Acil Durumlar  Modülünün implementasyonu sırasında ve sonrasında izleyeceği yolu belirlemektir.

## **3.SORUMLULUKLAR**  

İş yeri  Hekimi,  İş Güvenliği Uzmanı, İdari İşler  Sorumlusu,  İşveren


## **4.KISALTMALAR**

**AD:** Acil Durumlar


## **5.Acil Durumlar Modülü**
İş yerinin tamamında veya bir kısmında meydana gelebilecek yangın, patlama, tehlikeli kimyasal maddelerden kaynaklanan yayılım, doğal afet gibi acil müdahale, mücadele, ilk yardım veya tahliye gerektiren olaylara acil durum denir. İş yerlerinde acil durum planlarının hazırlanması, önleme, koruma, tahliye, yangınla mücadele, ilk yardım ve benzeri konularda yapılması gereken çalışmalar ile bu durumların güvenli olarak yönetilmesi ve bu konularda görevlendirilecek çalışanların belirlenmesi, acil durumlarda müdahale edecek acil durum ekiplerinin tanımlanması gibi işlemlerin yapıldığı modüldür. 

Bu modül içeriğinde aşağıdaki özellikleri kapsamaktadır.

- Yangın, sel ve deprem gibi Acil durum tiplerinin tanımlama işlemi yapılması
- Kurumda mevcut olan koruma, söndürme ve arama kurtarma gibi Acil Durum Ekiplerinin tanımlama işlemi yapılması
- Her tür felaket için farklı ekip kurabilmesi sağlanması
- Kullanıcının istek ve ihtiyaçlarına göre sistemsel ayarların yapılması.
- İş yeri bazında tatbikatların oluşturulmasının  yapılması
- Acil durum ekipleri için revizyon işlemi yapabilmesi
- Acil Durum ekiplerine eklenen ekip üyelerin aldığı eğitimlerin bilgisi görüntülenmesi
- Acil Durum ekiplerin gözden geçirme periyoduna bağlı olarak sistem tarafından otomatik bilgilendirmelerin yapılması
- Tatbikat zamanı geldiği zaman tatbikat sorumlusuna bildirim maili gidilmesinin sağlanması
- Acil Durum Ekipleri” ile hangi iş yerinde hangi ekibin olduğunu ve ekip üyelerin bilgisini görüntülenmesi ve filtre sekmesinde istenilen kriterlere göre rapor alınması sağlanması.
- “Acil Durum Tatbikatları” ile işyeri bazında tatbikat listelerini bilgisi görüntülenmesi ve filtre sekmesinde istenilen kriterlere göre rapor alınması sağlanması.
**5.1.Sistem Altyapı Tanımları/Acil Durumlar**
**Acil Durumlar** modülünün altyapısının oluşturularak tanımlamaların yapıldığı menüdür. Entegre Yönetim Sistemi menüsünden girişlerde yapılan bu tanımlamalara göre veriler karşımıza çıkmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_7.png)

### **5.1.Sistem Altyapı Tanımları/Acil Durumlar**
#### **5.1.1.Alan Tanımlama**
**Menü Adı:** Sistem Altyapı Tanımları/Acil Durumlar/Alan Tanımlama

Entegre Yönetim Sistemi menüsü altında bulunan Acil Durum Ekibi Tanımlama,  Acil Durum Ekip Üyesi Tanımlama, Acil Durum Tatbikatı Tanımlama menülerinde görülmesi gereken alanların tanımlandığı menüdür. Burada oluşturulan alanlar alan havuzuna eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_8.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref1]: Yeni bir alan eklenir.

![ref2]: Listede seçili olan alan bilgisi üzerinde  düzeltme/ değişiklik/ güncelleme yapılır.Kod bilgisi güncellenemez.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_11.png):Listede seçili olan alan bilgisi kopyalanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_12.png): Listede seçili olan alan bilgisi silinir.  

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_13.png) : Alanın değerleri tanımlanır.

Alan Tanımlama ekranına yeni bir alan eklemek için ekranın sol üst köşesindeki ![ref3] (Yeni) butonuna tıklanarak Alan Tanımlama\ Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_15.png) ![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_16.png)

**Açılan ekranda ilgili alanlar tanımlanır;**

**Alan Kodu:** Alan Tanımlama-Yeni Kayıt ekranında Alan Kodu bilgisinin girildiği zorunlu alandır. Daha önce tanımlamış alanlarla aynı olmayacak şekilde boşluk, Türkçe karakter gibi karakterler kullanmadan tanımlanmalıdır. Ör. ‘001’ , ‘RK’

**Alan Adı:** Alan Tanımlama-Yeni Kayıt ekranında Alan Adı bilgisinin girildiği alandır. 

**Başlık Notu:** Alan Tanımlama-Yeni Kayıt ekranında alanı veri girişinin yapılması ile ilgili  açıklayıcı bilgi içeren not bilgisinin girildiği alandır. Mouse ile alanın üzerine gelindiğinde görüntülenen bilgidir.

**Giriş Tipi:** Alan Tanımlama-Yeni Kayıt ekranında giriş tipinin Hesaplanan veya Veri Girişi tipi bilgisinin seçilebildiği alandır. Giriş Tipi seçeneği oluşturulan alanın manuel olarak veri girişi ile mi yoksa hesaplama yöntemi ile mi belirleneceğini gösterir. 

**Alan Tipi:** Alan Tanımlama-Yeni Kayıt ekranında alan tipinin bilgisinin seçilebildiği alandır. Alan Tipi ise oluşturulan alanın metin, nümerik, tarih, liste vb. tiplerinden hangisi olduğunu gösterir. 

**Görünme Şartı:** Alan Tanımlama-Yeni Kayıt ekranında Görünme Şartı bilgisinin girildiği alandır. Bir alan eğer başka bir alanın şartına bağlı olarak görülecekse görünme şartı kullanılır. Liste tipli alanın değerlerine göre oluşturulan alanın görüntülenmesini sağlar. Kullanımı [ALANKODU]=ALAN\_DEĞERİ vb. şekildedir. (Örneğin, Fırsat var mı? Alanının  alan kodu 01; Fırsat alanının alan kodu 02 olsun. Eğer “Fırsat” Alanının, “Fırsat var mı?” Alanındaki seçeneklerden değer kodu 100 olan “Evet” değeri seçili ise görülmesi gerekiyorsa 02 numaraları “Fırsat” alanının görünme şartı bölümüne formül şu şekilde yazılmalıdır: [01]=100)

**Durum:** Alan Tanımlama-Yeni Kayıt ekranında durumun Aktif veya Pasif olarak bilgisinin seçilebildiği alandır. 

Alan Tanımlama-Yeni Kayıt ekranında ekranında gerekli alanlar doldurulduktan sonra sol üst köşede yer alan  ![ref4]  (Kaydet) butonuna tıklanarak alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_18.png)

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

#### **5.1.2.Fonksiyon Dizayner**
**Menü adı:** Sistem Altyapı Tanımları/Acil Durumlar/ Fonksiyon Dizayner

Fonksiyon Dizayner menüsü ile alan havuzuna eklenen alanlar Acil Durumlar modülünün ilgili fonksiyonları ile ilişkilendirilebilir. Bunun için Sistem Altyapı Tanımları / Acil durumlar modülünün altından Fonksiyon Dizayner menüsüne gelinir. Açılan ekranda Acil Durumlar modülünün alan eklenebilecek fonksiyonları sıralanacaktır. Bu ekranda Acil Durum Ekibi Tanımlama, Acil Durum Ekip Üyesi Tanımlama ve Acil Durum Tatbikatı Tanımlama fonksiyonlarında kullanılacak alanlar ve bunların sıralaması ile onay işlemlerindeki hiyerarşi detayı tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_19.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref5]: Alanları fonksiyonlarla ilişkilendirilir.

![ref6]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref7]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref8]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranında kullanıcı bazlı tasarlama işlemi yapılır.

Fonksiyon Dizayn ekranında ilgili fonksiyon seçilerek ![ref5]  butonu tıklanılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_24.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref1]: Listede seçili fonksiyona yeni bir alan eklenir.

![ref2]:Listede seçili eklenen fonksiyona eklenen alan bilgisi üzerinde değişiklik/düzenleme/güncelleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_25.png): Listede seçili eklenen fonksiyona eklenen alan bilgisi silinir.

![ref1]: Yeni butonu tıklanarak Alan Tanımlama-Fonksiyonlar-Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_26.png) ![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_27.png)

**Açılan ekranda ilgili alanlar tanımlanır;**

**Alan Adı:** Alan Tanımlama - Fonksiyonlar - Yeni Kayıt ekranında tanımlanan ilgili alan adı seçilir.

**Zorunlu Mu? :** Alan Tanımlama - Fonksiyonlar - Yeni Kayıt ekranında seçilen alan için veri girişinin zorunlu olup olmadığı belirlenir. “Evet” seçeneği seçildiğinde alan için veri girişi zorunludur.

**Zorunluluk Mesajı:** Alan Tanımlama - Fonksiyonlar - Yeni Kayıt ekranında seçilen alan için Zorunluluk Mesajı bilgisinin girildiği alandır. Zorunlu alanlar doldurulmadığında verilecek uyarı mesajı bilgisi yazılır.

**Sıra No:** Alan Tanımlama - Fonksiyonlar - Yeni Kayıt ekranında seçilen alanın ekranda kaçıncı sırada görüntüleneceği bilgisinin girildiği alandır.

**Gridde göster:** Alan Tanımlama - Fonksiyonlar - Yeni Kayıt ekranında seçilen alanın liste grid ekranında gösterilmesi isteniyorsa ilgili check box işaretlenir.

**Satır Sayısı**: Alan Tanımlama - Fonksiyonlar - Yeni Kayıt ekranında seçilen alan için satır sayısı bilgisinin belirlendiği alandır.

**Kolon Genişliği:** Alan Tanımlama - Fonksiyonlar - Yeni Kayıt ekranında seçilen alan için kolon genişliği bilgisinin belirlendiği alandır.

**Aktif Statü:** Alanın sisteme tanımlanan statülerin hangilerinde aktif olacağını veri girişi yapılacağı  belirlendiği alandır. Bu alanda işaretlenen statülerde ilgili alanın tipine göre işlem gerçekleştirilebilir.

**Görünür Statü:** Alanın sisteme tanımlanan statülerin hangilerinde görüleceğini belirlendiği alandır. Aktif statüsü seçilen alanlar için aynı zamanda görünür statüde en az aktif statü alanında işaretlenen statüler olacak şekilde belirlenmelidir.

**Zorunlu Statü:** Alanın sisteme tanımlanan statülerin hangilerinde zorunlu olacağını belirlendiği alandır.Zorunlu olarak belirlenen alanda veri girişinin girilmesi zorunlu kılınır.

Alan Tanımlama - Fonksiyonlar - Yeni Kayıt ekranında gerekli tüm alanlar doldurulduktan sonra ekranın sol üst köşesindeki ![ref4] butonuna tıklanarak alanın Acil Durum Tatbikatı Tanımlama fonksiyona bağlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_28.png)

Tanımlanan alan ilgili fonksiyonla ilişkilendirme işlemi yapıldıktan sonra Acil Durum Tatbikatı Tanımlama ekranında görüntülenir.Tanımlanan alanın  Aktif statü, Görünür statü ve Zorunlu statü ilgili alanı işaretli olduğu için alanın görüntülenip, veri girişi yapılması ve yıldızlı işaretli olarak zorunlu alan olduğu görülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_29.png)

#### **5.1.3.Acil Durum Tipleri**
**Menü adı:** Sistem Altyapı Tanımları/Acil Durumlar/ Acil Durum Tipleri

Acil durum tiplerinin tanımlama işleminin yapıldığı menüdür. İşyerinin tamamında veya bir kısmında meydana gelebilecek yangın, sel, deprem, sabotaj, doğal afet gibi acil müdahele, müdahele, ilk yardım veya tahliye gerektiren olayların tümü tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_30.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref9]: Yeni acil durum tipi tanımlanır.

![ref10]: Listede seçili acil durum tipi bilgisi üzerinde düzenleme/güncelleme/değişiklik yapılır.

![ref11]: Listede seçili acil durum tipi bilgisi silinir.

![ref12]: Kayıtlar filtrelenerek arama yapılabilir.

![ref6]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref7]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

Acil Durum Tipi Tanımlama ekranına yeni bir acil durum tipi eklemek için ekranın sol üst köşesindeki ![ref9] butonu tıklanarak Acil Durum Tipi Tanımlama ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_35.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Kod:** Acil Durum Tipi Tanımlama ekranında Acil durum tipinin kod şablonu yazıldığı  alandır.Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/ Parametreler menüsünde Modül alanında Acil Durumlar modülü seçilerek açılan Acil Durumlar Modülü parametrelerindein 1 numaralı “Acil Durum Tipi Oto Kod Şablonu” parametre değerinde tanımlı kod yapısına göre sistem otomatik kod şablonu tanımlaması yapar. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_36.png)

Acil Durumlar Modülü parametrelerinde 2 numaralı “Acil Durum Tipi Sayac” parametresinin parametre değerine atanan sayaç değerine göre kod şablonun kaçtan başlayacağı belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_37.png)

Acil Durum Tipi Tanımlama ekranında ADL.001, ADL.002, ADL.003 sayac değeri “0” olduğunda kod şablonu otomatik olarak tanımlanır.

**Adı:** Acil Durum Tipi Tanımlama ekranında Acil durum tipinin tanım bilgisi yazıldığı alandır.

**Tatbikat Yapılacak Mı**: Acil Durum Tipi Tanımlama ekranında Tatbikat yapılacak mı bilgisi aktif edilecekse ilgili check box işaretlenir. İlgili check box işaretlenirse tatbikat periyodu ve tatbikat yapacak rol olmak üzere iki alan ortaya çıkar.

**Tatbikat Periyodu:**  Acil Durum Tipi Tanımlama ekranında Tatbikat periyodu bilgisi yazıldığı alandır.Hangi periyot aralığında tatbikatının yapılcağı belirlenir.

**Tatbikat Yapacak Rol:** Acil Durum Tipi Tanımlama ekranında Tatbikat yapacak rol bilgisinin rol tanımlarından seçildiği alandır. (Tatbikatı yapacak rol, Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Rol Tanımlama menüsünden tanımlanır.)

**Alınması Gerekenler:** Acil Durum Tipi Tanımlama ekranında Alınması gerekenler bilgisi yazıldığı alandır. Tatbikat yapılırken ihtiyaç duyulan gereksinimlerdir. 

**Ön Bildirim Süresi (Gün):** Acil Durum Tipi Tanımlama ekranında Ön bildirim süresi gün olarak belirlendiği alandır. Tatbikat yapılmadan önce kaç gün önceden bilgilendirme yapıldığı gün sayısının girildiği alandır.

Acil Durum Tipi Tanımlama ekranında gerekli alanlar doldurulduktan sol üst köşede yer alan  ![ref13] butonu tıklanarak Acil Durum Tipi Tanımlama ekranında kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_39.png)

Acil Durum Tipi Tanımlama ekranında Filtre sekmesinde Kodu, Adı, Alınması Gerekenler gibi alanları veri girilip, ![ref14] (Ara) butonu tıklanarak arama kriterlerine göre filtreleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_41.png)

#### **5.1.4.Acil Durum Ekip Tipleri**
**Menü adı:** Sistem Altyapı Tanımları/Acil Durumlar/ Acil Durum Ekip Tipleri

Firmada mevcut olan acil durum ekip tipleri Qdms’e tanımlama işlemin yapıldığı menüdür. (Koruma, söndürme, arama kurtarma, ilk yardım, vb.).

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_42.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref15]:Yeni acil durum ekip tipi eklenir.

![ref16]: Listede seçili acil durum ekip tipi bilgisi üzerinde düzenleme/güncelleme/değişiklik yapılır.

![ref17]: Listede seçili acil durum ekip tipi bilgisi silinir.

![ref12]: Kayıtlar filtrelenerek arama yapılabilir.

![ref6]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref7]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

Acil Durum Ekip Tipi Tanımlama ekranına yeni bir acil durum ekip  tipi eklemek için ekranın sol üst köşesindeki ![ref9] butonu tıklanarak Acil Durum Ekip Tipi Tanımlama ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_46.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Ekip Kodu:** Acil Durum Ekip Tipi Tanımlama ekranından Acil durum ekip tipinin kodu bilgisi yazıldığı alandır. Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/ Parametreler menüsünde Modül alanında Acil Durumlar modülü seçilerek açılan Acil Durumlar Modülü parametrelerindein 1 numaralı “Acil Durum Ekip Tipi Kod Şablonu” parametre değerinde tanımlı kod yapısına göre sistem otomatik kod şablonu tanımlaması yapar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_47.png)

Acil Durumlar Modülü parametrelerinde 4 numaralı “Acil Durum Ekip Tipi Sayaç” parametresinin parametre değerine atanan sayaç değerine göre kod şablonun kaçtan başlayacağı belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_48.png)

Acil Durum Ekip Tipi Tanımlama ekranından ADEK.001, ADEK.002, ADEK.003 sayac değeri “0” olduğunda kod şablonu otomatik olarak tanımlanır.

**Ekip Tanımı:** Acil Durum Ekip Tipi Tanımlama ekranından Acil durum ekip tipinin tanım bilgisi yazıldığı  alandır.

**Amaç:** Acil Durum Ekip Tipi Tanımlama ekranından Acil durum ekip tipinin amacı bilgisinin yazıldığı alandır.

**İlişkili Dokümanlar:** Acil Durum Ekip Tipi Tanımlama ekranında Acil durum ekip tipinin ilişkili olduğu dokümanlar ![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_167.png) butonu tıklanarak açılan sistemde tanımlı doküman listesinden seçildiği alandır.

**Acil Durum Tipleri:** Acil Durum Ekip Tipi Tanımlama ekranında Acil durum ekip tipinin acil durum tipleri bilgisinin ![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_167.png) butonu tıklanarak açılan sistemde tanımlı acil ekip tipi listesinden seçildiği alandır. (Acil Durum Ekip Tipi listesi Sistem Altyapı Tanımları/Acil Durumlar/Acil Durum Tipleri listesinde tanımlı olarak gelmektedir.)[Acil Durum Tipleri](#_5.1.3.acil_durum_tipleri)

Acil Durum Ekip Tipi Tanımlama ekranında gerekli alanlar doldurulduktan sonra sol üst köşede yer alan  ![ref13] butonu tıklanarak acil durum ekip tipi tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_50.png)

Acil Durum Ekip Tipi Tanımlama ekranında Filtre sekmesinde Ekip kodu, Ekip Tanımı, Amaç gibi alanları veri girilip, ![ref14] (Ara) butonu tıklanarak arama kriterlerine göre filtreleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_51.png)
#### **5.1.5.E-posta Ayarları**
**Menü Adı**: Sistem Altyapı Tanımları/Acil Durumlar/ E-posta Ayarları

E-Posta Ayarları ekranında, Acil Durumlar  Modülü süreçlerinin hangi aşamasında kimlere mail ve sms gönderimi yapılacağı belirlendiği menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_52.png)

**Ekranda bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_53.png): Listede seçili olan  E-postaları  değeri bilgisi üzerinde düzenleme/değişiklik/güncelleme işlemi yapılır.

![ref6]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref7]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref8]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

**E- Posta Ayarlarında SMS  bildirimi kullanılacak ise;** 

Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/ Parametreler menüsü tıklanılır. Açılan Parametreler ekranında listelenen Sistem Altyapı Tanımları  modülü parametrelerinde 102 numaralı “SMS bildirimi kullanıcak mı?” parametresinin parametreler ekranında Filtre sekmesinde parametre no alanına parametre numarası yazılarak ![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_54.png) (Ara) butonu tıklanarak aratılarak seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_55.png)

Sistem Alyapı Tanımları modülü parametrelerinde 102 numaralı “SMS bildirimi kullanıcak mı?” parametresi seçildikten sonra ![ref19] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_57.png)

Açılan parametreler ekranın parametre değeri “Evet” seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_58.png)

Parametreler ekranında parametre değeri “Evet” seçildikten sonra ekranın sol üstte yer alan ![ref13] butonu tıklanarak parametreyi aktif etme kayıt işlemi  yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_59.png)

Parametre Aktif edildikten sonra E- Posta Ayarları ekranında SMS bildirimi kullanılması ile ilgili “SMS gitsin mi?” alanı ile ilgili check box görüntülenir.  İlgili check box işaretlenerek E-Posta ayarlarında SMS bildirimi kullanılır.

Hangi basamakta e-posta/ mesaj gitmesi isteniyorsa seçilir ve  ![ref19] butonu tıklanılır. 

Örn: “	Ekip Oluşturma Onayı “ basamağı seçilir ve ![ref19] butonu tıklanılır.  

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_60.png)

Açılan E-Posta Ayarları/ Ekip Oluşturma Onayı ekranı görüntülenir. Roller kısmı, e-posta ve mesaj bildirimimin gideceği rolü yani kişiyi göstermektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_61.png)

E-Posta Ayarları/ Ekip Oluşturma Onayı ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_62.png) (Seç) butonu tıklanarak açılan sistemde tanımlı Mesaj Gövdesi listesinde  gönderilecek mesaj gövdesi ilgili listeden seçilir. Yanlış eklenen bir mesaj gövdesini silmek içinse ![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_63.png) (Sil) butonu kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_64.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_65.png) butonu ile Mesaj Gövdesinin içeriği detaylı bir şekilde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_66.png)

Mesaj Gövdesi listesinde seçilen Mesaj Gövdesi ![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_67.png) butonu tıklanarak seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_68.png)

Kime E-Posta gitmesi isteniyorsa, o rolle ilgili “E-Posta Gitsin Mi/ SMS Gitsin Mi” check box ‘ı işaretlenir.Mesaj gitmesi için rolde tanımlı olan kişinin cep telefon numarası personel tanımlama ekranında tanımlı olmalıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_69.png)

E-Posta Ayarları/ Ekip Oluşturma Onayı ekranında E-Posta gitmesi  rollerle  ilgili “E-Posta Gitsin Mi/ SMS Gitsin Mi” check box ‘ı işaretlendikten sonra ekranın sol üstte köşede yer alan ![ref13] butonu tıklanarak E- Posta Ayarları kayıt işlemi gerçekleştirilir.

#### **5.1.6.Acil Durumlar Modülü Parametreleri** 
**Menü Adı:** Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Parametreler

Acil Durumlar Modülü için kullanıcının istek ve ihtiyaçlarına göre çeşitli ayarlamaların yapabildiği ve bunlara göre parametreleri belirlendiği (seçilebildiği) menüdür. Parametrelerde yapılan değişikler tüm Qdms kullanıcılarını kapsamaktadır. Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Parmetreler menüsü tıklanılır. Açılan parametreler ekranında liste ve filtre sekmesi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_70.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref2]: Listede seçili olan parametre bilgisi üzerinde düzenleme/değişiklik/güncelleme işlemi yapılır.

![ref12]: Kayıtlar filtrelenerek arama yapılır.

![ref20]: Veriler Excel’ e aktarılır.( Parametreler ekranında liste sekmesinde bulunan İç Müşteri Şikayetleri Modülü parametrelerin listesinin Excel formatında raporu alınır.)

Parametreler ekranında Filtre sekmesinde Modüller alanında açılır liste tıklanılarak sistemde tanımlı modül listesinde Acil Durumlar modülü seçilir ve ![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_72.png)(Ara) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_73.png)

Acil Durumlar modülü ile ilgili parametrelerinde liste sekmesinde listelenmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_74.png)

Açılan Acil Durumlar Modülü parametreleri ekranında parametrelerle ilgili parametre değerinin “Evet” seçilerek aktif etme, parametre değerini “Hayır” seçilerek parametreyi pasif etme  parametre değeri bilgisini  girme ve girilen parametre değeri bilgisini değiştirme işlemleri yapılır.

Örnek; Parametre Aktifleme işlemi

Acil Durumlar Modülü parametrelerinde 28 numaralı “Tatbikatın mevcut durumu onay mailine PDF formatında ek dosya olarak eklensin mi?” parametresi seçili iken ![ref19] butonu tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_75.png)

Açılan parametreler ekranında parametrenin parametre değeri “ Evet” seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_76.png)

Parametreler ekranında parametre değeri “Evet seçilerek gerekli alanlar ilgili bilgiler üzerinde değişiklik yapıldıktan sonra ekranın sol üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_77.png) butonu tıklanarak parametre kayıt güncelleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_78.png)

Aynı aşamalar yapılarak parametre değeri “Hayır” seçilerek parametre pasif etme işlemi yapılır ve parametre değerine yeni değeri girilerek parametre değeri bilgisi girilme işlemi yapılır. Yada parametre değeri bilgisi değiştirme işlemi yapılır.

### **5.2.Entegre Yönetim Sistemi/Acil Durumlar**
Acil durum planlarının tanımlandığı, görev alınan acil durum ekiplerinin gösterildiği, raporların Excel formatında alındığı, acil durum ekibi ve acil durum tatbikatı onaylama işlemlerinin yapıldığı kısımdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_79.png)

#### **5.2.1.Acil Durum Planları**
**Menü adı:** Entegre Yönetim Sistemi/Acil Durumlar/ Acil Durum Planları

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_80.png)

İş yeri bazında acil durum ekiplerinin oluşturulup tatbikatların planlandığı menüdür. Açılan ekranda iş yerleri ağaç kırılımı şeklinde listelenmektedir. İşlem yapılacak iş yeri seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_81.png) butonuna tıklanır. Bu ekranda üç farklı sekme bulunur. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_82.png)

Acil Durumlar Ekipleri ekranında Ekipler sekmesinde bulunan butonlar yardımıyla aşağıdaki işlemler gerçekleştirilebilir;

![ref21]: Yeni acil durum ekibi eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_84.png): Listede seçili acil durum ekip bilgisi üzerinde düzenleme/değişiklik/günceleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_85.png): Listede seçili acil durum ekip bilgisi silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_86.png): Listede seçili acil durum ekibine Ekip üyesi eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_87.png): Listede seçili acil durum ekibi onaya gönderilme işlemi yapılır. (Sadece Taslak halinde acil durum ekipleri onaya gönderilebilir.)

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_88.png): Listede seçili acil durum ekibi revizyon başlatılma işlemi yapılır.( Sadece durumu Aktif statüsündeki acil durum ekiplere revizyon başlatılma işlemi yapılır)

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_89.png): Revizyondan vazgeçmek için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_90.png): Listede seçili acil durum ekibin varsa eski revizyonları görüntüleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_91.png):Listede seçili durumu aktif statüsündeki acil durum ekibi pasif onaya gönderme işlemi yapılır.

![ref12]: Kayıtlar filtrelenerek arama yapılabilir.

![ref20]: Veriler Excel’ e aktarılır.

![ref6]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref7]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref8]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Yeni bir ekip eklemek için ekranın sağ üst köşesindeki ![ref21] butonu tıklanarak Acil Durum Ekip Tanımlama/Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_92.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_93.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**İş Yeri:** Acil Durum Ekibi Tanımlama ekranında İş yeri bilgisi sistem tarafında verildiği alandır.

**Ekip Tipi:** Acil Durum Ekibi Tanımlama ekranında Ekip Tipi bilgisi ![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_94.png) butonu tıklanarak açılan sistemde tanımlı Acil Ekip Tipi listesinde seçim yapıldığı alandır.(Acil Ekip Tipi listesi Sistem Altyapı Tanımları/Acil Durumlar/ Acil Durum Ekip Tipleri menüsünde tanımlı olarak gelmektedir.)[Acil Durum Ekip Tipleri](#_5.1.4.acil_durum_ekip)

**Statü:** Acil Durum Ekibi Tanımlama ekranında Acil durum ekibinin statü bilgisinin sistem tarafından  verildiği alandır.

**Revizyon No:** Acil Durum Ekibi Tanımlama ekranında Acil Durum ekibinin revizyon no bilgisinin sistem tarafından verildiği alandır.

**Revizyon Tarihi:** Acil Durum Ekibi Tanımlama ekranında Acil Durum ekibinin revizyon tarihi bilgisinin sistem tarafından verildiği alandır.

**Son Gözden Geçirme Tarihi:** Acil Durum Ekibi Tanımlama ekranında Acil Durum ekibinin son gözden geçirme tarihi görülür.

**Minimum Gerekli Ekip Üyesi Sayısı:** Acil Durum Ekibi Tanımlama ekranında Acil Durum ekibi minimum gerekli ekip üyesi sayısı bilgisinin girildiği alandır.Acil Durum ekibinin onaydaki kişiye onaya gitmesi için gerekli minimum ekip sayısıdır. Minimum  ekip sayısı Acil Durum ekibe eklenmediği zaman sistem minumum ekip sayısının girilmediğina dair uyarı mesajı verir.

Açılan Acil Durum Ekibi Tanımlama ekranında ekranda acil durum ekibinin ekip tipi sistemde tanımlı olan Acil Ekip Tipi listesinden seçilir. Minimum gerekli ekip üyesi sayısı bilgisi girilir. Acil durum ekibinin statü bilgisi, revizyon no, revizyon tarihi, son geçirme tarihi bilgisi sistem tarafından verilir. Gerekli alanlar ilgili bilgiler girildikten sonra ekranın sol üst köşesindeki 

![ref13] butonu tıklanarak Acil Durum Ekip tanımlama kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_95.png)

Acil Durum Ekip Listesi ekranında Acil Durum Ekipi seçili iken  ![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_96.png) butonu tıklanarak  Acil Durum ekibine Ekip üyesi ekleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_97.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref22]: Yeni ekip üyesi tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_99.png): Listede seçili ekip üyesi bilgisini üzerinde düzenleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_100.png): Listede seçili ekip üyesi bilgisi silinir.

![ref23] :Listede seçili  ekip üyesinin aldığı eğitimleri görüntüler.

Acil durum ekibine yeni bir ekip üyesi eklemek için ekranın sağ üst köşesindeki ![ref22] butonu tıklanarak Acil Durum Ekibi Tanımlama ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_102.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Personel:** Acil Durum Ekibi Tanımlama ekranında Acil durum ekip üyesinin ![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_103.png) butonu tıklanarak açılan sistemde tanımlı  personel listesinden seçildiği alandır.

**Görev:** Acil Durum Ekibi Tanımlam ekranında Acil durum ekip üyesinin görev bilgisi açılır liste tıklanarak açılan sistemde tanımlı görev listesinden seçildiği alandır.Görev listesi bilgisi Sistem Altyapı Tanımları/BSAT/ Konfigürasyon Ayarları/Sabitler menüsünde Modüller alanında Acil Durumlar modülü seçilerek Acil Durumlar modülü ile ilgili sabitlerin listelenmesi sağlanır.Listede Acil Durum Ekip Görevleri sabit tanımı seçilerek ![ref24] butonu tıklanır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_105.png)

Açılan Sabitler ekranında değer kısmında listelenen Acil durum Ekip görevi seçilerek tekrar ![ref24] butonu tıklanır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_106.png)

Açılan Sabit Değerleri - Kayıt Güncelle  değerin içeriğini değiştirme, aktif veya pasif etme işlemleri yapılır.  Görev tanımları seçeneğin ilgili alanda görüntülenip, görüntülenmesi sağlanır.

**Görev Tanımı:** Acil Durum Ekibi Tanımlama ekranında Acil durum ekip üyesinin görev tanımı bilgisinin yazıldığı alandır.

Açılan Acil Durum Ekibi Tanımlama ekranında acil durum ekip üyesi personel sistemde tanımlı olan personel listesinden seçilir. Seçilen personeli görev tanımı sistemde tanımlı olan görevlerden seçilir. Örneğin  yardımcı, ekip üyesi gibi görevlendirmesi yapılan personelin görev tanımı bilgisi yazılır. Gerekli alanlar ilgili bilgiler girildikten sonra ekranın sol üst köşesindeki ![ref13] butonu tıklanarak acil durum ekip üyesi tanımlama kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_107.png)

![ref23] butonu ile ekip üyesinin aldığı eğitimler ve geçerlilik tarihleri görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_108.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_109.png) butonu tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_110.png)

Firmada kullanılacak tüm ekip tipleri bu şekilde kaydedilir. Ekipler oluşturulduktan sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_111.png) butonu ile onaya gönderilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_112.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_113.png)

Bekleyen işlerime  **“Oluşturma Onayı Bekleyen Acil Durum Ekipleri “** olarak iş düşer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_114.png)

Acil durum ekibinin ilgili kodu tıklanarak Acil Durumu Ekibi Onaylama ekranına gelinerek acil durum ekibi onaylanır veya reddedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_115.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref25]: Listede seçili acil durum ekibi görüntüler.

![ref26]: Listede seçili acil durum ekibini onaylar.

![ref27]: Listede seçili acil durum ekibini reddeder.

Acil Durum Ekibi Onaylama ekranında listede acil durum ekibi seçili iken ![ref25] butonu tıklanarak Acil Durum Ekibi tanımlama ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_119.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_120.png)

Acil Durum Ekibi Onaylama ekranında listede acil durum ekibi seçili iken  ![ref27] butonu tıklanırsa ret nedeni yazılarak acil durumlar ekibi  reddedilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_121.png)

Acil Durum Ekibi Onaylama ekranında listede acil durum ekibi seçili iken  ![ref26] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_122.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_123.png)

Onaylanan acil durum ekip listesi kişiye mail olarak iletilir. Onaylanan acil durum ekip listesi “**Bekleyen İşlerim**” menüsünde **“Görev Aldığım Acil Durum Ekipleri”** iş olarak görev düşer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_124.png)

Entegre Yönetim Sistemi/Acil Durumlar/Acil Durum Planları menüsünde iş yeri seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_125.png) butonu tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_126.png)

Açılan Acil Durum Ekipleri ekranında 3 sekme karşımıza çıkar. Ekipler , Krokiler ve Tatbikatlar sekmeleridir. 

**Ekipler sekmesinde ;**

Acil Durum Ekipleri tanımlama işlemi yapılır ve tanımlı Acil Durum Ekiplerinin listesine görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_127.png)

**Krokiler sekmesi;**

Krokiler sekmesinde acil durum planları ile ilgili krokileri ek dosya olarak yükleme, yüklenen ek dosyaları görüntüleme ve silme işlemlerinin yapıldığı sekmedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_128.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref28]: Ek dosya sisteme yüklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_130.png): Yüklenen ek dosya bilgisi silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_131.png): Yüklenen ek dosya bilgisi görüntülenir.

Krokiler sekmesinde Ek Dosyalar  ekranında ![ref28] butonu tıklanarak Acil Durum Planları ile ek dosya ekleme işlemi yapılır. Birden çok ek dosya eklenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_132.png)

Dosya Yükleme ekranında Gözat butonu tıklanarak ilgili doküman seçilerek sisteme yükleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_133.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_134.png)

**Tatbikatlar sekmesi;**

Acil Durum Planları ile tatbikatların tanımlama işlemin yapıldığı, listede seçili tatbikatların düzenleme ve silme işlemlerinin yapıldığı sekmedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_135.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref29]:Yeni bir Tatbikat tanımlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_137.png):Listede seçili tatbikat bilgisi üzerinde düzenleme/değişiklik/güncelleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_138.png):Listede seçili tatbikat bilgisi silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_139.png):Arama kriterlerine göre filtreleme yapılır.

![ref20]: Veriler Excel’ e aktarılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_140.png):Pdf formatında acil durum tatbikatı görüntüler.

![ref6]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref7]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref8]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Acil Durum Tatbikatları ekranında yeni bir Tatbikat ekleme işlemi için ![ref29] butonu tıklanarak Acil Durum Ekibi Tanımlama ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_141.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Tatbikat Kodu:** Acil Durum Ekibi Tanımlama ekranında Tatbikat kodu bilgisinin parametreye bağlı olarak sistem tarafından otomatik verildiği alandır. Acil Durumlar Modülü parametrelerinde 5 numaralı “Acil Durum Tatbikat Oto Kod Şablonu” parametresinde tanımlı kod şablonu tanımlanır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_142.png)

6 numaralı “Acil Durum Tatbikat Sayaç” parametresinde sayac değerine göre kod şablonun kaçtan başlanacağı belirlenerek ilgili alana otomatik olarak atanır. Tanımlanan kod şablonuna göre  6 numaralı parametredeki sayac değeri “163” göre kod şablonu [TBKK]\_164, [TBKK]\_165 şeklinde sırasıyla sistem otomatik kod ataması yapar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_143.png)

**Tatbikat Adı:** Acil Durum Ekibi Tanımlama ekranında Tatbikat adı bilgisi yazıldığı alandır.

**Acil Durum Tipi:** Acil Durum Ekibi Tanımlama ekranında Acil durum tipi  bilgisinin ![ref30] butonu tıklanarak açılan sistemde tanımlı olan acil durum tipi listesinden seçildiği alandır. (Acil Durum Tipi listesi Sistem Altyapı Tanımları/Acil Durumlar/Acil Durum Tipleri menüsünde tanımlı olarak gelmektedir.)[Acil Durum Tipleri](#_5.1.3.acil_durum_tipleri)

**Tatbikat Sorumlusu:** Acil Durum Ekibi Tanımlama ekranında Tatbikat sorumlusu bilgisinin ![ref30] butonu tıklanarak açılan sistemde tanımlı olan personel listesinden seçildiği alandır.

**Tatbikat Yeri:** Acil Durum Ekibi Tanımlama ekranında Tatbikat yeri bilgisi yazıldığı alandır.

**Tatbikat Tarihi:** Acil Durum Ekibi Tanımlama ekranında Tatbikat tarihi bilgisi açılan Takvim alanında seçildiği alandır.

**Tatbikat Saati:** Acil Durum Ekibi Tanımlama ekranında Tatbikat saati bilgisi seçildiği alandır.

**Kullanılan Ekipmanlar:** Acil Durum Ekibi Tanımlama ekranında kullanılan ekipmanlar yazıldığı alandır

**Tatbikat Ekibi:** Acil Durum Ekibi Tanımlama ekranında Tatbikat ekibi bilgisi ![ref30] butonu tıklanarak açılan sistemde tanımlı olan Acil Durum Ekibi listesinde seçildiği alandır.(Acil Durum Ekibi listesi Sistem Altyapı Tanımları/Acil Durumlar/Acil Durum Ekip Tipleri menüsünde tanımlı olarak gelmektedir.)[Acil Durum Ekip Tipleri](#_5.1.4.acil_durum_ekip)

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_145.png)

Açılan ekranda tatbikat kodu sistem tarafından otomatik verilir. Tatbikatın adı tanımlanır, acil durum tipi bilgisi sistemde tanımlı olan Acil Durum Ekip Tipi listesinden ve tatbikat sorumlusu da sistemde tanımlı olan personel listesinden seçilir. Tatbikatın yeri yazılır, tatbikatın tarihi ve saati bilgisi girilir. Kullanılan ekipmanlar varsa yazılır. Gerekli alanlar ilgili bilgiler girildikten sonra ekranın sol üst köşedeki  ![ref4] butonuyla tıklanarak tatbikat tanımlama kayıt işlemi yapılır.Tatbikat ekibi sistemde tanımlı acil durum ekibi listesinden seçilir. Tatbikat zamanı geldiği zaman tatbikat sorumlusuna bildirim maili gitmektedir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_146.png)

Onaya giden tatbikat “**Bekleyen İşlerime**” **”Tamamlanması Gereken Tatbikatlar”** iş olarak görev düşer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_147.png)

İlgili görevdeki Tatbikat Kodu alanındaki link tıklanarak Acil Durum Tatbikatları ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_148.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref31]:Listede seçili Acil Durum Tatbikat bilgisi görüntülenir.

![ref32]:Listede seçili Acil Durum Tatbikat bilgisinin onaylama işlemi yapılır.

![ref33]:Listede seçili Acil Durum Tatbikat bilgisininin red nedeni yazılarak ret edilme işlemi yapılır.

Acil Durum Tatbikatları ekranında listede Acil Durum Tatbikatı seçili iken ![ref31] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_152.png)

Açılan Acil Durum Ekibi Tanımlama ekranında Tatbikatlar ve Önlemler sekmesi olarak iki sekme karşımıza çıkar.

**Tatbikatlar sekmesi;**

Acil Durum Ekibi ile ilgili tanımlanan tatbikatın detay bilgileri görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_153.png)

**Önlemler sekmesi;**

Acil Durum Ekibi ile ilgili tanımlanan tatbikatla ilgili alınan önlemlerin görüntülendiği sekmedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_154.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref34] **Acil Durum Tatbikatı Tanımlama** ekranında Önlemler sekmesinde listede seçili önlem bilgisi görüntülenir.

Acil Durum Tatbikatları ekranında ![ref35]  butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_157.png)

Acılan Reddet pop-upn’da  red nedeni bilgisi yazılarak Acil Durum Tatbikat onayının ret edilme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_158.png)

Acil Durum Tatbikatları ekranında ![ref36] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_160.png)

Açılan Acil Durum Tatbikatı Tanımlama ekranında Tatbikatlar ve Önlemler sekmesi görüntülenir.

**Tatbikatlar sekmesi;**

Acil Durum Ekibi ile ilgili tanımlanan tatbikatın detay bilgileri görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_161.png)

**Önlemler sekmesi;**

Acil Durum Ekibi ile ilgili tanımlanan tatbikatla ilgili alınacak önlemleri ekleme ,listede seçili önlem bilgisini düzenleme ve silme  işlemin yapıldığı sekmedir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_162.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref37]: Acil Durum Tatbikatı Tanımlama** ekranında Önlemler sekmesinde yeni bir önlem ekleme işlemi yapılır.

![ref38]: Acil Durum Tatbikatı Tanımlama** ekranında Önlemler sekmesinde  listede seçili önlem bilgisi üzerinde düzenleme işlemi yapılır.

![ref39]: Acil Durum Tatbikatı Tanımlama** ekranında Önlemler sekmesinde listede seçili önlem bilgisi silinir.

![ref34]: Acil Durum Tatbikatı Tanımlama** ekranında Önlemler sekmesinde listede Acil Durum Tatbikatı Tanımlama** ekranında yeni bir Önlem ekleme işlemi yapmak için ![ref37] butonu tıklanarak Önlemler ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_166.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Referans Tipi:**.Önlemler sekmesinde Önlem olarak Doküman, DÖF ve Aksiyon seçeneklerinde seçim yapıldığı alandır. 

**Referans tipi Doküman seçildiğinde;**

Referans bilgisi doküman seçildiğinde referans bilgisi alanında ![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_167.png) butonu tıklanarak açılan sistemde tanımlı Doküman listesinde seçilir. Doküman Yönetimi Modülünde yüklü olan dokümanlar Doküman listesinde görüntülenir. 

**Referans tipi seçeneği DÖF seçildiğinde;**  DÖF  Kaydının mevcut kayıtlı listeden seçilme veya yeni bir DÖF kaydının tanımlama işlem adımının seçeneğinin yer aldığı alan görüntülenir.”Listeden seç” seçeneği seçildiğinde açılan referans tipi alanında sistemde tanımlı DÖF kayıtlarından seçim yapılır. “Yeni Oluştur” seçeneği seçildiğinde açılan DÖF İşlemleri-Yeni Kayıt ekranında yeni bir DÖF kaydının tanımlama işlemi yapılır.

**Referans tipi seçeneği Aksiyon seçildiğinde;**  Aksiyon  kaydının mevcut kayıtlı listeden seçilme veya yeni bir Aksiyon tanımlama işlem adımın seçeneğinde yer aldığı alan görüntülenecektir.”Listeden seç” seçeneği seçilirse sistemde tanımlı mevcut Aksiyonlardan seçim yapılır. “Yeni Oluştur” seçeneği seçildiğinde açılan Aksiyon Kalemi Planlama-Yeni Kayıt ekranı açılarak yeni bir Aksiyon Kalemi tanımlama işlemi yapılır.

Acil Durumlar Modülü parametrelerinde 21 numaralı “Acil Durum Tatbikat önlemi için Ana Aksiyon No” parametresine ana aksiyon kodu tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_168.png)

` `Ana Aksiyon Kodu bilgisi Aksiyon Yönetimi modülünde Aksiyon Planlama ekranında alınır. Acil Durum Tatbikat önlemi olarak Aksiyon alındığında açılan bu aksiyonlar parametre tanımlı ana aksiyona bağlı olarak açılır.

**Önlem Tipi:** Önlemler sekmesinde Mevcut ve Planlanan seçeneğinde seçim yapıldığı alandır. Mevcut seçiminde önlem olarak  sistemde kayıtlı DÖF ve Aksiyonları seçilir. Planlanan seçim işleminde yeni bir  önlem olarak DÖF Kaydının açılması yada önlem olarak yeni bir Aksiyon tanımlama işleminin yapılması işlemidir.

**Önlem Tarihi:** Önlemler sekmesinde tanımlanacak önlemin tarihinin açılan takvim alanında seçimin yapıldığı alandır.

**Açıklama:** Önlemler sekmesinde tanımlanacak önlemin varsa açıklama bilgisinin yazıldığı alandır.

**Referans Tipi Doküman seçilirse;**

Acil Durum Ekibi Tanımlama ekranında Önlemler sekmesinde Referans Tipi doküman seçilerek ilgili alanlar ilgili bilgiler girilir.  

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_169.png)

Gerekli alanlar ilgili bilgiler girildikten sonra ekranın sol üst köseşindeki ![ref13] butonu tıklanarak referans tipi doküman olan önlem tanımlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_170.png)

**Referans tipi seçeneği DÖF seçildiğinde;**  

Acil Durum Ekibi Tanımlama ekranında Önlemler sekmesinde Referans Tipi DÖF  seçilerek ilgili alanlar ilgili bilgiler girilir.  DÖF İşlemleri-Yeni Kayıt ekranında DÖF kaydı ile alanların  bilgilerinin girilmesi gerekir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_171.png)

Gerekli alanlar ilgili bilgiler girildikten sonra ekranın sol üst köseşindeki ![ref13] butonu tıklanarak referans tipi DÖF olan önlem tanımlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_172.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_173.png)

**Referans tipi seçeneği Aksiyon seçildiğinde;**  

Acil Durum Ekibi Tanımlama ekranında Önlemler sekmesinde Referans Tipi aksiyon seçilerek ilgili alanlar ilgili bilgiler girilir.  Aksiyon Kalemi Planlama-Yeni Kayıt ekranında aksiyon kaydı ile ilgili alanların bilgileri girilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_174.png)

Gerekli alanlar ilgili bilgiler girildikten sonra ekranın sol üst köseşindeki ![ref13] butonu tıklanarak referans tipi Aksiyon olan önlem tanımlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_175.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_176.png)

Acil Durum Ekibi Tanımlama ekranında Önlemler sekmesinde referans tipi seçilerek tüm önlemlerin tanımlama işlemi yapılır.

Tatbikat ile ilgili önlemlerin tanımlama işlemi yapıldıktan sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_177.png) butonu tıklanarak tatbikat tamamlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_178.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_179.png)

#### **5.2.2.Görev Aldığım Acil Durum Ekipleri**
**Menü adı:** Entegre Yönetim Sistemleri/ Acil Durumlar/ Görev Aldığım Acil Durum Ekipleri

Görev alınan acil durum ekiplerini gösteren menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_180.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref20]: Veriler Excel’ e aktarılır.

![ref6]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref7]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref8]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Görev Aldığım Acil Durum Ekipleri ekranında ![ref20] (Excel’e aktar ) butonuna tıklanarak, sistem otomatik olarak Görev Aldığım Acil Durum Ekipleri listesini kullanıcıya Excel formatında sunmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_181.png)

#### **5.2.3.Acil Durum Ekibi Onaylama**
**Menü adı:** Entegre Yönetim Sistemleri/ Acil Durumlar/ Acil Durum Ekibi Onaylama

Oluşturulan acil durum ekiplerinin onaylama işlemin yapıldığı menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_182.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref40]: Listede seçili acil durum ekibi görüntüler.

![ref41]: Listede seçili acil durum ekibini onaylar.

![ref42]: Listede seçili acil durum ekibini reddeder.

Acil Durum Ekibi Onaylama ekranında listede acil durum ekibi seçili iken ![ref40] butonu tıklanarak Acil Durum Ekibi tanımlama ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_186.png)

Acil Durum Ekibi Onaylama ekranında listede acil durum ekibi seçili iken  ![ref42] butonu tıklanır.  

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_187.png)

Açılan Reddet ekranında Ret Nedeni bilgisi yazılarak istenirse Acil Durum ekibi ret edilme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_188.png)

Acil Durum Ekibi Onaylama ekranında listede acil durum ekibi seçili iken  ![ref41] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_189.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_190.png)

#### **5.2.4.Acil Durum Tatbikat Onayı**
**Menü adı:** Entegre Yönetim Sistemleri/ Acil Durumlar/ Acil Durum Tatbikat Onayı

Acil durum tatbikatlarının onay işlemlerinin yapıldığı menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_191.png) **Ekrandaki bulunan butonlar yardımıyla;**

![ref43]:Listede seçili Acil Durum Tatbikat bilgisi görüntülenir.

![ref44]:Listede seçili Acil Durum Tatbikat bilgisinin onaylama işlemi yapılır.

![ref35]:Listede seçili Acil Durum Tatbikat bilgisininin red nedeni yazılarak ret edilme işlemi yapılır.

Acil Durum Tatbikatları ekranında listede Acil Durum Tatbikatı seçili iken ![ref43] butonu tıklanılır. 

Açılan Acil Durum Ekibi Tanımlama ekranında Tatbikatlar ve Önlemler sekmesi olarak iki sekme karşımıza çıkar.

**Tatbikatlar sekmesi;**

Acil Durum Ekibi ile ilgili tanımlanan tatbikatın detay bilgileri görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_194.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_195.png)

**Önlemler sekmesi;**

Acil Durum Ekibi ile ilgili tanımlanan tatbikatla ilgili alınan önlemlerin görüntülendiği sekmedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_196.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref34]: **Acil Durum Tatbikatı Tanımlama** ekranında Önlemler sekmesinde listede seçili önlem bilgisi görüntülenir.

Acil Durum Tatbikatları ekranında ![ref35] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_197.png)

Acılan Reddet pop-upn’da  red nedeni bilgisi yazılarak Acil Durum Tatbikat onayının ret edilme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_198.png)

Acil Durum Tatbikatları ekranında ![ref44] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_199.png)

Açılan Acil Durum Tatbikatı Tanımlama ekranında Tatbikatlar ve Önlemler sekmesi görüntülenir.

**Tatbikatlar sekmesi;**

Acil Durum Ekibi ile ilgili tanımlanan tatbikatın detay bilgileri görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_200.png)

**Önlemler sekmesi;**

Acil Durum Ekibi ile ilgili tanımlanan tatbikatla ilgili alınacak önlemleri ekleme ,listede seçili önlem bilgisini düzenleme ve silme  işlemin yapıldığı sekmedir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_201.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref37]: Acil Durum Tatbikatı Tanımlama ekranında Önlemler sekmesinde yeni bir önlem ekleme işlemi yapılır.

![ref38]: Acil Durum Tatbikatı Tanımlama ekranında Önlemler sekmesinde  listede seçili önlem bilgisi üzerinde düzenleme işlemi yapılır.

![ref39]: Acil Durum Tatbikatı Tanımlama ekranında Önlemler sekmesinde listede seçili önlem bilgisi silinir.

![ref34]: Acil Durum Tatbikatı Tanımlama ekranında Önlemler sekmesinde listede seçili önlem bilgisi görüntülenir.

Acil Durum Tatbikatı Tanımlama ekranında yeni bir Önlem ekleme işlemi yapmak için ![ref37] butonu tıklanarak Önlemler ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_202.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Referans Tipi:**.Önlemler sekmesinde Önlem olarak Doküman, DÖF ve Aksiyon seçeneklerinde seçim yapıldığı alandır. 

**Önlem Tipi:** Önlemler sekmesinde Mevcut ve Planlanan seçeneğinde seçim yapıldığı alandır. Mevcut seçiminde önlem olarak  sistemde kayıtlı DÖF ve Aksiyonları seçilir. Planlanan seçim işleminde yeni bir  önlem olarak DÖF Kaydının açılması yada önlem olarak yeni bir Aksiyon tanımlama işleminin yapılması işlemidir.

**Önlem Tarihi:** Önlemler sekmesinde tanımlanacak önlemin tarihinin açılan takvim alanında seçimin yapıldığı alandır.

**Açıklama:** Önlemler sekmesinde tanımlanacak önlemin varsa açıklama bilgisinin yazıldığı alandır.

Acil Durum Tatbikatı Tanımlama ekranında Önlemler sekmesinde referans tipi seçilerek istenirse Tatbikat ile ilgili önlemlerin tanımlama işlemi yapılır.

Acil Durum Tatbikatı Tanımlama ekranında ![ref32] butonu tıklanarak Acil Durum Tatbikat Onayı işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_203.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_204.png)

Acil Durum Tatbikatları ekranından tatbikat onaylama işleminden sonra tatbikatın statüsü “Tamamladı” olarak görüntülenir.

Acil Durumlar modülü parametrelerinden 20 numaralı “Tatbikat onayı ekranında düzenlemeye izin ver” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_205.png)

Parametre aktif edildiğinde Acil Durumlar modülünde tatbikat onaylama işlemi yapılan Acil Durum Tatbikat tanımlama ekranında Tatbikatlar sekmesinde  ilgili alanlar üzerinde düzenleme ve değişiklik yapılmasına sistem izin verir. Parametre değeri “Hayır” seçildiğinde parametre pasif edildiğinde Acil Durum Tatbikat Tanımlama ekranında tatbikatlar sekmesinde butonlar görüntülenmez ve  görüntülenen alanlar üzerinde düzenleme sistem izin vermez.

Acil Durumlar Modülü parametrelerinden 7 numaralı “Onay Süresi” parametresinde parametre değerinde  girelen değere göre tamamlanması gereken tatbikatlarda onayın başladığı tarihe eklenecek süre bilgisinin belirlenmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_206.png)

#### **5.2.5.Raporlar**
##### **5.2.5.1.Acil Durum Ekipleri**
**Menü adı:** Entegre Yönetim Sistemleri/ Acil Durumlar/ Raporlar/Acil Durum Ekipleri

Hangi iş yerinde hangi ekibin olduğunu belirten rapordur. Bu raporda Ekip Tipi, İş Yeri, Revizyon No, Revizyon Tarihi, Son Gözden Geçirme Tarihi ve Statü gibi alanlar hakkında bilgi verilmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_207.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref45]:Ekip üyeleri detay bilgisini görüntüler.

![ref12]: Kayıtlar filtrelenerek arama yapılır.

![ref20]: Veriler Excel’ e aktarılır.

![ref6]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref7]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref8]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

![ref20] (Excel’e aktar) butonuna basılırsa, sistem otomatik olarak Acil Durum Ekipleri Raporunu oluşturup kullanıcıya Excel formatında sunmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_209.png)

Acil Durum Ekip Listesi ekranında liste sekmesinde Acil Durum ekipi seçili iken ![ref45] butonu tıklanarak ekip Üyeleri Detay Bilgileri görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_210.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref20]: Veriler Excel’ e aktarılır.

![ref6]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref7]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref20] (Excel’e aktar) butonuna basılırsa, sistem otomatik olarak ekip üyeleri detay bilgilerini kullanıcıya Excel formatında sunmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_211.png)

Acil Durum Ekip Listesi ekranında Filtre sekmesinde İş yeri, Ekip Tipi,Statü ve Revizyon No gibi arama kriterleri alanlarına veri girilerek ![ref12] (Ara) butonu tıklanarak filtreleme işlemi işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_212.png)

##### **5.2.5.2.Acil Durum Tatbikatları**
**Menü adı:** Entegre Yönetim Sistemleri/ Acil Durumlar/ Raporlar/Acil Durum Tatbikatları

İşyeri bazında tatbikat listelerini veren rapordur. Bu raporda İş Yeri, Tatbikat Kodu, Tatbikat Adı, Durum Tip Kodu, Durum Tip Adı, Sorumlu Adı, Sorumlu Soyadı, Tatbikat Yeri, Statü ve Tatbikat Tarihi gibi alanlar hakkında bilgi verilmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_213.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref45]:Ekip üyeleri detay bilgisini görüntüler.

![ref12]: Kayıtlar filtrelenerek arama yapılır.

![ref20]: Veriler Excel’ e aktarılır.

![ref6]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref7]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref8]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

![ref20] ( Excel’e aktar) butonuna basılırsa, sistem otomatik olarak Acil Durum Tatbikatları Raporunu oluşturup kullanıcıya Excel formatında sunmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_214.png)

Acil Durum Tatbikatları ekranında ![ref45] butonu tıklanarak Acil Durum Ekip Listesi  detay bilgileri görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_215.png)

Acil Durum Ekip listesinde ![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_216.png) butonu tıklanarak seçili olan Acil Durumun ekip üyelerinin görüntüleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_217.png)

Acil Durum Ekip üyelerinin listesini ![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_218.png) (Excel Aktar) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_219.png)

Acil Durum Ekip üyelerinin Excel formatında raporu alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_220.png)


[ref1]: https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_9.png
[ref2]: https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_10.png
[ref3]: https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_14.png
[ref4]: https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_17.png
[ref5]: https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_20.png
[ref6]: https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_21.png
[ref7]: https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_22.png
[ref8]: https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_23.png
[ref9]: https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_31.png
[ref10]: https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_32.png
[ref11]: https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_33.png
[ref12]: https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_34.png
[ref13]: https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_38.png
[ref14]: https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_40.png
[ref15]: https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_43.png
[ref16]: https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_44.png
[ref17]: https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_45.png
[ref18]: https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_49.png
[ref19]: https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_56.png
[ref20]: https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_71.png
[ref21]: https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_83.png
[ref22]: https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_98.png
[ref23]: https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_101.png
[ref24]: https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_104.png
[ref25]: https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_116.png
[ref26]: https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_117.png
[ref27]: https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_118.png
[ref28]: https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_129.png
[ref29]: https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_136.png
[ref30]: https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_144.png
[ref31]: https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_149.png
[ref32]: https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_150.png
[ref33]: https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_151.png
[ref34]: https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_155.png
[ref35]: https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_156.png
[ref36]: https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_159.png
[ref37]: https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_163.png
[ref38]: https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_164.png
[ref39]: https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_165.png
[ref40]: https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_183.png
[ref41]: https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_184.png
[ref42]: https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_185.png
[ref43]: https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_192.png
[ref44]: https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_193.png
[ref45]: https://docsbimser.blob.core.windows.net/imagecontainer/fcad1150-5928-4ee2-a641-61787a63b595_208.png
