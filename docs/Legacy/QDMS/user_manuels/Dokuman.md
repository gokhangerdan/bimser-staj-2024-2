---
title: Doküman Yönetimi
description: Doküman Yönetimi Yardım Dokümanı
sidebar_position: 2
---

:::tip Bilgi

İlgili konu başlığına sağ tarafta bulunan navigasyon yardımıyla hızlı bir şekilde ulaşabilirsiniz.

:::


**Doküman Yönetimi Modülü(v.5.26) Kullanıcı Yardım Dokümanı**

Modül Versiyonu: 5.26



## **1.GİRİŞ**

**“QDMS Doküman Yönetimi Modülü”**, yönetim sistemleri dokümantasyonunun hazırlandığı, revize edildiği, onay süreçlerinin yürütülerek dokümanların yayınlandığı, doküman raporlarının alınabildiği ve tüm dokümantasyonun arşivlendiği bir modüldür.

## **2.AMAÇ** 

Bu yardım kılavuzunun amacı; “Doküman Yönetimi” modülünün çalışma sürecini anlatmaktır.Bu yardım kılavuzu sistem altyapı tanımlarındaki tanımlamalar ve parametrelerden başlayarak, dokümantasyonun temellerinin oluşturulduğu “Klasör Tanımlama, Doküman Hazırlama,  Revizyon, İptal” süreçlerinin detaylı olarak uygulama örnekleri ile anlatmaktadır. Sistemden dokümantasyonla ilgili alınan “Raporlar” ve uygulamada kullanıcılara yardımcı olacak “Sistem Altyapı  Tanımları”  kısmı yine örnekler yoluyla anlatılmaktadır.

## **3.SORUMLULUKLAR**

 QDMS Doküman Modülü Yöneticileri, Dokümanların Sorumluları, Tüm Çalışanlar

## **4.KISALTMALAR**

**QDMS**: Kalite Dokümanları Yönetim Sistemi “Quality Document Management System”

## **5.İŞ AKIŞI**

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_7.png)



## **6. Doküman Yönetimi Modülü**
   Doküman yönetimi modülü, standartlara uygun olarak doküman yönetim sürecini sağlayan bir modüldür. Yönetim sistemleri dokümantasyonunun QDMS sistemi üzerinde onay sürecinden geçirilerek hazırlanmasını, kontrol edilmesini, onaylanmasını, revize edilmesini, yayınlanarak elektronik ortamda ilgili personellere dağıtılmasını, raporlanmasını ve tüm dokümantasyonun arşivlenmesini ve iptal sürecinin yürütülmesini sağlar. Personellerin yetkili oldukları klasörler/ dokümanlar kapsamında dokümanlara ulaşıp, dokümanlar üzerinde işlem yapmasına olanak sağlar. Hızlı, kolay ve güvenilir bir doküman yönetimi için QDMS ‘te;

- Güvenli doküman kontrolü ve hızlı onay mekanizması
- Birbirleri ile ilişkilendirilebilir dokümanlar
- Kolay tasnif edilen, indekslenen dokümanlar ile hızlı arama
- Yetkilendirme özelliği ile dokümanlara kontrollü erişim
- Dokümanların otomatik yayınlanması ve okunan dokümanların kolay takibi
- Basılı dokümanların yönetimi
- Onay, kontrol, revizyon ve yayınlama aşamalarında e-mail ile bilgilendirme
- Otomatik olarak sistem tarafından doküman master listesi oluşturma
- Şablon kullanımı ile dokümanlarda standardizasyon sağlama
- Dokümanları ürün, süreç ve yönetim sistemleri ile dinamik olarak ilişkilendirme
- Manuel olarak doldurup arşivlenen kalite kayıtlarının takibi
### **6.1.Sistem Altyapı Tanımları/ Doküman İşlemleri**
Doküman İşlemleri Modülünde altyapı tanımları tanımlama işlemi yapıldığı kısımdır. Doküman İşlemleri modülünde başlamadan önce altyapıda bulunan doküman tiplerinin tanımlanması gerekir. Ayrıca kontrollü kopya olarak dağıtımı yapılacak dokümanların, fiziksel dağıtım noktaları olan dağıtım yerleri ve dağıtım yerlerinin ortaklaştırılarak sınıflandırılmasını sağlayan dağıtım gruplarını tanımlama işlemi ilk aşamada yapılması gerekmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_8.png)

#### **6.1.1.Doküman Tipleri** 
Doküman tiplerinin tanımlama işleminin yapıldığı menüdür.Klasör tiplerinin belirlenmesinde, doküman hazırlama işleminde ne tip doküman hazırlandığının belirlenmesinde ve raporlamalarda kullanılmaktadır.

Örneğin; 

EK-El Kitabı, 

PO-Politika, 

SR-Süreç,

IA-İş Akışı,

PR-Prosedür, 

TL-Talimatları, 

FR-Form, 

LS-Liste, 

SZ-Sözleşme, 

DKD-Dış Kaynaklı doküman vb. doküman tipleri kullanılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_9.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref1]:Yeni bir doküman tipi tanımlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_11.png):Listede seçili doküman tipi bilgisi üzerinde güncelleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_12.png):Listede seçili doküman tipi bilgisi silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_13.png):Matris Tanımlama ekranı açılır ve doküman tipi bazında matris tanımlama işlemi yapılır.

![ref2]: Kayıtlar filtrelenerek arama yapılabilir.

![ref3]: Veriler Excel’ e aktarılır.

![ref4]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref5]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

- Sadece Aktif Olan Kayıtları Listele: İlgili check box işaretlenirse sadece durunu aktif statüsündeki doküman tipleri kayıtları listelenir.

Doküman Tipi Tanımlama ekranına yeni bir doküman tipi eklemek için ekranın sol üst köşesindeki ![ref1]  butonu tıklanarak Doküman Tipi Tanımlama/ Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_18.png)

**Açılan ekranda ilgili alanlar tanımlanır;**

**Doküman Tipi Kodu:** Doküman Tipi Tanımlama -Yeni Kayıt ekranında firma bünyesinde tanımlı olan doküman tiplerinin kodunun yazıldığı alandır. Örneğin; Prosedür için PR,  Polika için PO kodları tanımlanır.

**Doküman Tipi Açıklama:** Doküman Tipi Tanımlama-Yeni Kayıt ekranında doküman tipinin  açıklama bilgisi yazılır.Örneğin; Prosedür, Politika gibi. Diğer dil seçenekleri de kullanılacaksa ilgili bayrağın bulunduğu alanlara ilgili doküman tipinin dil karşılığı yazılır.

**Kısa Kod:** Doküman Tipi Tanımlama-Yeni Kayıt ekranında doküman kod yapısında belirlenen, doküman tipine ait kısa kodun, sistem üzerinde doküman hazırlarken kullanılan doküman kodu yapısında otomatik olarak kullanılması isteniyorsa bu alan doldurulur. Örneğin; Prosedür için P0X kısa kodunun, doküman işlemlerinde klasör tanımlamada otomatik şablonda kullanılması isteniyorsa, [TIP] kodu kullanılır. Böylece sistemde oluşturulan yeni doküman için kod şablonu kısmında [TIP] görülen yere otomatik olarak “POX”  kodunu getirir.  Klasör Tanımlama- Yeni Kayıt ekranında tanımlanan otomatik kod şablonunda doküman tipi “Politika” seçildiğinde  [TIP]  kısmında kısa kod alanında tanımlı kod gelir.Kısa kod tanımlı olmadığında doküman tipinin kod alanındaki kod bilgisi [TIP] alanı gelmektedir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_19.png)

Doküman Hazırlama işlemin yapıldığı Yeni Doküman ekranında doküman kodları sayac değerine göre B-2024-POX.001, B-2024-POX.002, B-2024-POX.003 şeklinde sıralı otomatik gelmesi sağlanır.

**Exceller Sayfalara Bölünsün:** Doküman Tipi Tanımlama-Yeni Kayıt ekranında ilgili doküman tipinin excel olduğu durumlarda bu özellik kullanılır. Yazdırma yada okuma aşamasında Excel’i PDF’e dönüştürürken tüm sayfaların tek bir sayfa olarak görüntülenip görüntülenmeyeceği belirlenir. Eğer ilgili check box seçili değilse, excel çalışma sayfası içerisinde bulunan tüm sayfaları (page) PDF’e çevirirken tek bir sayfaya sıkıştırır. Eğer ilgili check box seçili olan ise, excel çalışma sayfası içerisinde bulunan tüm sayfaları (page) PDF’e çevirirken ayrı ayrı sayfalar halinde dönüştürür.

**Doküman Print Formatı:** Doküman Tipi Tanımlama-Yeni Kayıt ekranında ilgili doküman tipi için sistemde önceden tanımlanmış olan doküman print formatının (doküman hazırlama şablonundaki hazır alt/ üst bilgiler kısmı) kullanılması isteniyorsa ilgili format seçimi yapılır.Doküman Print Formatı tanımları listesi Sistem Altyapı Tanımları /Doküman İşlemleri/Doküman Print Formatında Tanımlama menüsünde tanımlı olarak gelmektedir.

**Durum:** Doküman Tipi Tanımlama-Yeni Kayıt ekranında ilgili doküman tipinin aktiflik ya da pasiflik durumu belirlenir.

Doküman Tipi Tanımlama-Yeni Kayıt ekranında gerekli alanlar ilgili bilgiler girildikten sonra ekranın sol üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_20.png)  butonu tıklanarak doküman tipi kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_21.png)Doküman Tipi Tanımlama ekranında Doküman Tipi seçili iken ![ref6] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_23.png)

Açılan Matris Tanımlama ekranında ile ilgili doküman tipi için yetki, dağıtım, onay, görüş matrisleri ve kontrollü kopya dağıtım yerlerinin belirlemesi sağlanır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_24.png)Örneğin; Doküman tipi Politika olan dokümanlar için yetki matrisi, dağıtım matrisi veya onay matrisleri tanımlanmış kullanıcı/ kullanıcı grubu olması isteniyorsa bu menüden ilgili seçimler yapılır. Matris tanımlama işlemleri doküman tipi aynı olsa bile farklılık gösterecek dokümanlar için klasör tanımlama menüsünden ya da doküman hazırlama işlemlerinden dokümana özgü olarak gerçekleştirilir.

Matris Tanımlama işlemi yapmak için ilgili doküman tipi seçilerek, ![ref6] butonuna tıklanır. Açılan ekranında, yetki, dağıtım, onay, görüş, kontrollü kopya matrisleri tanımlanır. 

**Yetki Matrisi**

Doküman tipinin bağlı olduğu dokümanlar için hangi kullanıcı yada kullanıcı gruplarının okuma, yazdırma, hazırlama/ revize etme, eski revizyonları görme ve iptal etme yetkilerine sahip olacağı belirlendiği sekmedir.  

**Dokümanda Yetki Matrisinde Yetkilendirme;**

**Okuma:** Doküman tipine bağlı dokümanlar için  dokümanları görüntüleme ve okumabilme işlemi yapma yetkisi

**Yazdırma:** Doküman tipine bağlı dokümanlar için dokümanı bilgisayarı indirip yazdırabilme işlemi yapma yetkisi

**Hazırla/Revize:** Doküman Tipine bağlı dokümanlarda yeni bir doküman hazırlama ve var olan dokümanda revizyon işlemi yapma yetkisi

**Eski Revizyon:** Doküman tipine bağlı dokümanlarda Revizyon işlemi yapılmış dokümanları eski revizyonları varsa görüntüleme işlemi yapma yetkisi

**İptal Etme:** Doküman Tipine bağlı dokümanlarda doküman iptal işleminin yapılması yetkisi

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_25.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref7]: Seçili olan kullanıcı grubundaki personelleri gösterir.

![ref8]: Listeye pozisyon eklenir.

` `![ref9] :Yetki matrisine sistemde tanımlı Kullanıcı grubundan kullanı grubu ekleme işlemi yapılır

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_29.png) : Yetki matrisinde seçili satırın silinme işlemi yapılır.

![ref9]: Listede seçili olan pozisyondaki/ kullanıcı grubundaki yetkileri siler.

Doküman Tipine bağlı dokümanlarda yetki matrisi atama yapmak için  ![ref9] /![ref8] butonları tıklanır. Sistemde tanımlı olan Kullanıcı Grubu/ Pozisyon listesinde yetki verilmek istenilen kullanıcılar için seçim yapılır. Hangi yetkiler verilmek isteniyorsa işaretlenir.

![ref9]butonu tıklanarak sistemde tanımlı kullanıcı grubu listesinden yetkilendirme işlemi  yapılacak Kullanıcı grubu seçilerek ![ref10] butonu tıklanarak  yetki matrisine eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_31.png)

Yetki Matrisine Kullanıcı Grubu ekleme   işleminde sonra okuma, yazdırma, hazırlama/ revize etme, eski revizyonları görme ve iptal etme yetkilerinden hangileri verilecek ilgili check box’lar işaretlenerek  yetkilendirme işlemi yapılır. Okuma yetkisi kullanıcı ve kullanıcı grupları için varsayılan olarak işaretli gelir.  

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_32.png)

**Dağıtım Matrisi** 

Doküman tipinin bağlı olduğu dokümanlar için hangi kullanıcı ya da kullanıcı gruplarına okuma görevi düşeceğinin belirlendiği sekmedir. 

**Önemli:** Doküman tipine bağlı dokümanlarda önemli ile ilgili, check box işaretlinir. Önemli check box işaretli dokümanlar kullanıcının Bekleyen işlerim sayfasında “**Okunması Gereken Önemli Dokümanlar Listesi**” işi olarak görev düşer. Doküman tipine bağlı dokümanlarda ilgili check box işaretli değilse kullanıcının Bekleyen işlerim sayfasında  “Okunması Gereken Dokümanlar Listesi” işi olarak görev düşer. Doküman Yönetimi Modülü parametrelerinde 273 numaralı “Dağıtım matrisinde Önemli Dokuman fonksiyonu kullanılacak mı?” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir.

![ref11]

Parametre aktif edildikten sonra Dağıtım Matrisi sekmesinde “Önemli” alanı görüntülenir ve bu özellik doküman yönetimi modülünde kullanılır.

**Okuma Görevi Düşmesin:** Doküman tipine bağlı dokümanlar için okuma görevi düşmesi istenmiyorsa ilgili check box işaretlenir. Doküman Yönetimi parametrelerine 274 numaralı “Dağıtım matrisinde Okuma Görevi Düşmesin fonksiyonu kullanılacak mı ?” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. 

![ref12]

Parametre aktif edildikten sonra “Okuma görevi düşmesin” alanı dağıtım matrisi sekmesinde görüntülenir.

**Anket:** Doküman tipine bağlı dokümanlar için anket kullanılacaksa ilgili check box işaretlenir. Parametre bağlı olarak görüntülenen bir alandır.81 numaralı “Dokümanda Anket kulakçığı kullanılacak mı? (E/H)” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_35.png)

Parametre aktif edildikten sonra Doküman tipine bağlı dokümanda Yeni Doküman ekranında Diğer bilgiler sekmesinde “Anket Kullanılacak” alanla ilgili check box işaretlenir. “Anket Kullanılacak” alanla ilgili check box işaretlendikten sonra Anket sorularının tanımlanacak anket sekmesinin aktif edilmesi sağlanır.

![ref13]

Anket sekmesi tıklanarak Soru tanımlama ekranı görüntülenir.

![ref14]

Anket sekmesinde ![ref15] butonu tıklanarak Anket ile ilgili soruların tanımlama işlemi yapılarak Anket tanıımlama işlemi yapılır.

![ref16]

Anket Tanımlama işlemi yapılan dokümanda dağıtım matrisi sekmesinde eklenen kullanıcı /Kullanıcı Gruplarından “Anket” alanı ile ilgili check box işaretli ise anket gönderilme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_40.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref7]: Seçili olan kullanıcı grubundaki personelleri gösterir.

![ref8]: Listeye pozisyon eklenir.

![ref9] : Listeye kullanıcı grubu eklenir

![ref17] : Listede seçili olan pozisyondaki/ kullanıcı grubundaki dağıtımı siler.

Doküman Tipine bağlı dokümanda dağıtım matrisine atama yapmak için  ![ref9]/![ref8]    butonunları tıklanır. Sistemde tanımlı olan Kullanıcı Grubu/ Pozisyon listesinden dağıtım matrisine eklenmek istenilen kullanıcılar için seçim yapılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_42.png)

Doküman Tipleri Matris Tanımlama ekranında Dağıtım Matrisi sekmesinde ![ref9] butonu tıklanır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_43.png)

Sistemde tanımlı kullanıcı grubu listesinden dağıtım matrisine okuma görevi düşecek Kullanıcı grubu seçilerek![ref10]butonu tıklanarak Dağıtım matrisine eklenme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_44.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_45.png)

Dağıtım matrisine kullanıcı grubu ekleme işleminde sonra  ilgili alanlar ilgili check box’lar işaretlenerek önemli doküman ve anket gibi özellikleri kullanıp, kullanıcağı belirlenir.

**Onay Matrisi sekmesinde;** 

Doküman tipinin bağlı olduğu dokümanların kimler tarafından onaylanacağı ve onay seviyeleri. belirlendiği sekmedir.Doküman Tipine Bağlı dokümadanda onay matrisinde seviye kısmı ters mantıkla çalışmaktadır.Onay işleminde seviye kısmında yazılan değer “0” sıfır ise  0 seviyesindeki onaycı son onaycıdır.

1\.Görseldeki  doküman tipine bağlı dokümanda onay işleminde seviye kısmındaki değer “0” olup son onaycı olduğundan sadece son onaycı olan pozisyondaki kişiye doküman onaya gider.

![ref18]

2\.Görseldeki doküman tipine bağlı dokümanda  onay işleminde tersten başa doğru onaya gider. İlk olarak “1”  seviyesindeki onaycı doküman tipi bağlı dokümanı onaylama işlemi yapar. Son olarak “0”seviyesindeki onaycı doküman tipine bağlı dokümanın onaylama işlemini yapar.

![ref19]

3\. Görseldeki doküman tipinde bağlı dokümanda onay işleminde paralel onay olarak tanımlanır. Paralel onaylama işleminde aynı seviyede onaycılar olup , belli bir sıralama gerekmekten onaylama işlemi yapılır. Tüm onaycıların onaylama işlemi bittikten sonra doküman tipine bağlı dokümanda onay işlemi biter. “0” seviyesindeki herhangi bir onaycının sıralama gerekmekten onaylama işlemi yaparlar. 

![ref20]

4\.Görseldeki doküman tipine bağlı dokümanda onay işleminde tersten başa doğru onaya gider. 1.seviyesindeki onaycılardan herhangi bir sıralama gerekmekteden 1.seviyedeki onaycıların onaylama işlemi yapıldıktan sonra son onaycı olan “0” seviyedeki pozisyondaki kişiye onaylama işlemi yapılır.

![ref21]

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_50.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref22] : Listeye pozisyon eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_52.png) :Listede seçili olan satırı siler. 

Doküman Tipine bağlı dokümanda onay matrisinde bulunması istenilen onaycıları atamak için ![ref22]butonuna tıklanır. Sistemde tanımlı olan pozisyon listesinden onay matrisine eklenmek istenilen kullanıcılar için seçim yapılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_53.png)

Doküman Tipleri Matris Tanımlama ekranında Onay matrisi sekmesinde ![ref8] butonu tıklanılarak sistemde tanımlı Pozisyon Listesinde eklenecek onaycı seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_54.png)  butonu tıklanarak onaycı ekleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_55.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_56.png)

**Görüş Matrisi sekmesinde;** 

Doküman tipinin bağlı olduğu dokümanların hangi kullanıcıya ya da kullanıcı gruplarına görüşe gideceği belirlendiği sekmedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_57.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref23]: Listeye pozisyon eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_59.png): Listede seçili olan görüş pozisyonu siler.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_60.png):	Görüş matrisinde eklenen tüm pozisyonlardaki personelerin silinme işlemi yapılır.

Doküman Tipleri Matris Tanımlama ekranında Görüş Matrisi sekmesinde görüşcü eklemek için ![ref23] butonu tıklanılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_61.png)

Açılan sistemde tanımlı pozisyon listesinde ilgili pozisyon seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_62.png)  butonu tıklanara Görüş matrisine görüşcü ekleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_63.png)

**Kontrol Kopya Sekmesi;**

Doküman tipinin bağlı olduğu dokümanların hangi dağıtım yeri ya da dağıtım yeri grubuna kontrollü kopya olarak dağıtılacağı belirlendiği sekmedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_64.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref24]: Listeye dağıtım yeri eklenir..

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_66.png): Listeye dağıtım yeri grubu eklenir..

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_67.png): Listede seçili olan satır silinir.

Doküman Tipine bağlı  kontrollü kopya sekmesinde bulunması istenilen fiziksel dağıtım yerlerini atamak için  ![ref25]/ ![ref26] butonları tıklanır. Sistemde tanımlı olan dağıtım yerleri/dağıtım grupları listesinden kontrollü kopya sekmesine eklenmek istenilen dağıtım yerleri için seçim yapılır.

Doküman Tipleri Matris Tanımlama ekranında kontrol kopya sekmesinde Doküman tipine bağlı dokümanlar için  ![][ref24] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_70.png)

Açılan kontrol kopya sekmesinde dağıtım yeri listesinde eklenecek dağıtım yeri seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_71.png)  butonu tıklanarak ekleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_72.png)

Doküman tipine bağlı dokümanlarda ilgili sekmelerde işlem adımları yapıldıktan sonra ekranın sol üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_73.png)  butonu tıklanarak doküman tipine bağlı matris tanımlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_74.png)

Doküman  tipi  bağlı Matris Tanımlama işlemi  sonra Entegre Yönetim Sistemi/Doküman İşlemleri/ Doküman  Hazırlama menüsü tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_75.png)

Açılan Doküman Hazırlama -Klasör Seçme ekranında dokümanın hazırlanacağı klasör seçilir ve İleri butonu tıklanılır.Açılan Yeni Doküman ekranında Doküman Tipi alanından matris tanımlama işlemi yapılan doküman tipinin seçim işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_76.png)

Doküman Tipi alanında Matris tanımlama işlemi yapılan Doküman tipinin seçim işleminden sonra ![ref27] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_78.png)

Sistem tarafından verilen “Matrisleri doküman tipinden almak istediğinizden emin misiniz?” mesajında “Tamam” butonu tıklanarak tanımlanan doküman tipindeki  matris tanımlama göre dokümanın matrisleri tanımlanır.

Yetki Matrisi Doküman Tipi Politika için tanımlanan matristeki kullanıcı/Kullanıcı gruplarına göre yetki  ve yetkilendirmeleri gelir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_79.png)

Diğer matrislerde aynı şekilde doküman tipinde matris tanımlamada olduğu şekilde ilgili sekmelere eklenen kullanıcı/kullanıcı grupları ve pozisyonlar gelir. Bu işlemin yapılması için öncelik doküman tipi tanımlama menüsünde ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_80.png) butonu olan doküman tipi matrislerin tanımlama işlemi yapılır. Doküman Hazırlama ekranı olan Yeni Doküman ekranında matris tanımlama işlemi yapılan doküman tipi seçilerek  ![][ref27] butunu tıklanarak doküman tipinde bağlı doküman için matris tanımlama işlemi yapılır
#### **6.1.2.Dağıtım Yeri Tanımlama**
**Menü Adı**: Sistem Altyapı Tanımları /Doküman işlemleri/ Dağıtım Yeri Tanımlama

Kontrollü Kopya olarak dağıtımı yapılacak dokümanların, fiziksel dağıtım noktaları bu menüde tanımlanır. Bu işlemin amacı; yayınlanan dokümanların sistemde kontrollü olarak dağıtılmasını sağlamaktır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_81.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref28]:Yeni bir dağıtım yeri tanımlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_83.png):Listede seçili dağıtım yeri bilgisi üzerinde düzenleme/değiştirme/güncelleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_84.png):Listede seçili dağıtım yeri bilgisi silinir.

![ref29]: Kayıtlar filtrelenerek arama yapılır.

![ref30]: Veriler Excel’ e aktarılır. 

![ref4]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref5]: Menü ekranın tekrar varsayılan ayarlarına  gelmesi işlemi yapılır.

Dağıtım Yeri Tanımlama ekranında yeni bir dağıtım yeri eklemek için ekranın sol üst köşesindeki ![ref28]  butonu tıklanarak Dağıtım Yeri Tanımlama/ Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_87.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Yer Kodu:** Dağıtım Yeri Tanımlama -Yeni Kayıt ekranında	 tanımlanan dağıtım yerinin kod bilgisinin yazıldığı alandır. Daha önce tanımlamış alanlarla aynı olmayacak şekilde boşluk, Türkçe karakter gibi karakterler kullanmadan tanımlanmalıdır. Ör. ‘001’ , ‘RK’

**Açıklama:** Dağıtım Yeri Tanımlama -Yeni Kayıt ekranında	tanımlanan dağıtım yerinin adının yazıldığı alandır.İlgili bayrakların bulundu kısımlara tanımlanan dağıtım yerinin açıklama alanın dil karşılığı yazılır. 

**Sorumlu:** Dağıtım Yeri Tanımlama- Yeni Kayıt ekranında	tanımlanan dağıtım yerinin sorumlusunun ![ref31] butonu tıklanarak açılan sistemde tanımlı personel listesinden seçildiği alandır. Doküman kontrollü kopya dağıtımı kimin sorumluluğunda yapılacağı bu alanda belirlenir.

**Dağıtım Sorumlusu:** Dağıtım Yeri Tanımlama-Yeni Kayıt ekranında tanımlanan dağıtım yerinin sorumlusunun  ![ref31] butonu tıklanarak açılan sistemde tanımlı personel listesinden seçildiği alandır. Dokümanın, fiziksel olarak dağıtım yerlerine dağıtmaktan sorumlusu belirlenir.

**Durum:** Dağıtım Yeri Tanımlama -Yeni Kayıt ekranında tanımlanan dağıtım yerinin aktif ve pasif seçeneklerinde seçim yapıldığı alandır. Tanımlanan dağıtım yeri durumu “Aktif” seçilir.

**Baskı Departmanı:** Dağıtım Yeri Tanımlama-Yeni Kayıt ekranında dokümanların hangi departmanlara fiziksel olarak dağıtılacağının belirlendiği alandır. Baskı departmanı alanında ![ref31] butonu tıklanarak açılan Departman listesinde baskı departmanlarının seçim işlemi yapılır.	

“Durum” bilgisi “aktif” olarak seçilir. “Baskı Departmanı” alanından dokümanların hangi departmanlara fiziksel olarak dağıtılacağı departman listesinden seçilir.Gerekli alanlar ilgili bilgiler girildikten sonra ekranın sol üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_89.png)  butonu tıklanarak dağıtım yeri tanımlama kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_90.png)

Dağıtım Yeri Tanımlama ekranında Dağıtım Yeri Arama sekmesinde Yer Kodu, Sorumlu, Açıklama, Dağıtım Sorumlusu ve Durum  gibi arama kriterleri olan alanlara veri girilip, ![ref32] (Ara) butonu tıklanarak arama kriterlerine göre filtreleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_92.png)
#### **6.1.3.Dağıtım Yeri Grupları**
**Menü Adı**: Sistem Altyapı Tanımları/ Doküman İşlemleri/ Dağıtım Yeri Grupları

Dağıtım Yeri Tanımlama menüsünde tanımlanan dağıtım yerlerinin ortaklaştırılarak sınıflandırılmasını sağlayan menüdür. Böylece kontrollü kopya dağıtımı yapılırken, aynı noktaya ait olan dağıtım yerleri topluca seçilebilmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_93.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref33]:Yeni bir dağıtım yeri grubu tanımlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_95.png):Listede seçili dağıtım yeri grubu bilgisi üzerinde değişiklik/Güncelleme/düzemleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_96.png):Listede seçili dağıtım yeri grubu bilgisi silinir.

Dağıtım Yeri Grupları Tanımlama ekranına yeni bir dağıtım yeri grubu eklemek için ekranın sol üst köşesindeki ![ref33] butonu tıklanarak Dağıtım Yeri Grupları Tanımlama/ Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_97.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Grup Kodu:** Dağıtım Yeri Grupları Tanımlama - Yeni Kayıt ekranında tanımlanan dağıtım yeri grubunun kod bilgisi yazıldığı alandır. Daha önce tanımlamış alanlarla aynı olmayacak şekilde boşluk, Türkçe karakter gibi karakterler kullanmadan tanımlanmalıdır. Ör. ‘001’ , ‘RK’	

**Açıklama:** Dağıtım Yeri Grupları Tanımlama - Yeni Kayıt ekranında tanımlanan dağıtım yeri grubun adının yazıldığı alandır	

**Grup Üyeleri:** Dağıtım Yeri Grupları Tanımlama - Yeni Kayıt ekranında  ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_98.png) butonu tıklanarak açılan sistemde tanımlı dağıtım yeri  listesinden seçim yapıldığı alandır. 

Gerekli alanlar ilgili bilgiler girildikten sonra ekranın sol üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_99.png) butonu tıklanarak Dağıtım Yeri Grupları tanımlama kayıt işlemi   yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_100.png)

Dağıtım Yeri Tanımlama ekranında Dağıtım Yeri Grubu Arama sekmesinde Grup Kodu, Açıklama gibi arama kriterleri olan alanlara veri girilip, ![ref32] (Ara) butonu tıklanarak arama kriterlerine göre filtreleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_101.png)
### **6.2. Entegre Yönetim Sistemi /Doküman İşlemleri** 
Doküman Yönetimi Modülü  kapsamındaki  bu  kısımdakı tüm menüleri işleyişi, tüm doküman süreçlerin yönetilmesi , takip edilmesi ve raporlamasının  yapılması sağlanır. Yeni bir doküman hazırlanması, hazırlanan dokümanın görüş matrisinde ataması yapıldıysa görüşe gönderilmesi,  kontrolcü varsa kontrolle ,  onay matrisinde onaycıya   onaydan sonra  son olarak  dağıtım matrisinde kişilere okuma görevi düşmesi süreçleri devam etmesidir. Dokümanda revizyon işlemin yapılması ve revizyon işlemi yapılmış bir dokümanın eski revizyonlarının görüntülenmesi , doküman iptal işlemi , bir doküman aktif ve pasif etme işlemleri yapılmasını kapsamaktadır. Ayrıca dokümların yönetileceği klasörlerin tanımlama işlemi yapılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_102.png)
#### **6.2.1.Klasör Tanımlama**
**Menü Adı**: Entegre Yönetim Sistemi/ Doküman İşlemleri/ Klasör Tanımlama

Qdms sisteminde dokümanların yönetileceği klasörlerin oluşturulduğu ve düzenlendiği menüdür. Klasör tanımlama ekranında öncelikle klasör ağaç yapısına karar verilmesi gerekmektedir. Organizasyon yapısına, süreçlere, doküman tiplerine, yönetim sistemlerine, departmanlara ya da firmanın uygun görüldüğü yapıya göre klasör ağaç yapısı oluşturulur. Klasör tanımlama ekranında klasör tanımlama işlemi yanında seçili klasörün bilgileri düzenleme, seçili klasörü kopyalama, seçili klasör kodunu değiştirme, seçili klasörü başka bir klasör altına taşıma ve seçili klasör ile ilgili parametrik alanların tanımlama işlemleri yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_103.png)

**Ekranda bulunan butonlar yardımıyla;** 

![ref34] : Yeni bir klasör tanımlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_105.png) : Seçili olan klasör ile ilgili bilgiler düzenlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_106.png) : Seçili olan klasörün kodu değiştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_107.png) : Seçili olan klasör, alt klasörleri ile beraber kopyalanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_108.png): Seçili olan klasör, başka bir klasörün altına taşınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_109.png): Klasör tanımlama ekranında seçili klasörün linkinin kopyalama işlemi yapılır. Doküman görme ekranında linki alınan klasörün klasör ağaç yapısında görüntülenecek şekilde alt klasör ve dokümanları ile listelenmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_110.png): Klasör tanımlama ekranında seçili klasörün linkinin kopyalama işlemi yapılır. Doküman görme ekranında klasör ağaç yapısı gizlenecek şekilde  linki alınan klasörün  varsa alt klasör  ve dokümanların  listelenmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_111.png):Seçili klasör silinir.

![ref35]:Klasör bazında parametrik alan tanımlama işlemi yapılır. Parametre bağlı olarak görüntülenen bir alandır. Doküman Yönetimi Modülü parametrelerinden 109 numaralı “Klasör bazında parametrik alan kullanılacak mı?” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_113.png)

Parametre aktif edildikten sonra  Klasör Tanımlama ekranında ![ref35] butonu görüntülenir. Klasör bazında metin, metin (Çoklu Satır), liste gibi parametrik tipli alanların tanımlama işlemi yapılır.

Klasör Tanımlama ekranın yeni bir klasör tanımlamak için ekranın sol üst köşesindeki ![ref34] butonu tıklanarak Klasör Tanımlama/Yeni Kayıt ekranı açılır. Firmanın klasör yapısı, Ağaç kırılımı şeklinde sistemde istenildiği detayda tanımlanabilir.

![ref36]![ref37] 

**Klasör Bilgileri sekmesinde;** 

Tanımlanan klasörün bağlı olduğu klasör, grup kodu, adı, içerisinde hazırlanacak dokümanların doküman tiplerinin bilgisi, otomatik kod şablounun ve sayac bilgisinin ne olacağı gibi genel yapısı ile ilgili bilgilerin tanımlandığı sekmedir.

**Klasör Bilgileri sekmesinde ekranda bulunan şu bilgiler tanımlanır;**

**Bağlı Olduğu Klasör:** Klasör Tanımlama- Yeni Kayıt ekranında Klasör bilgileri sekmesinde

ana klasöre bağlı bir alt klasör oluşturma işlemi yapıldığı alandır.Ana klasöre bağlı bir alt klasör tanımlama işlemi yapılmadığında alanın sağ tarafındaki ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_116.png)butonu tıklanarak bağlı olduğu klasör bilgisi silinir.Tanımlanan klasörde “Bimser” ana klasörüne  bağlı bir alt klasör tanımlama işlemi yapılır.

**Grup Kodu:** Klasör Tanımlama- Yeni Kayıt ekranında Klasör bilgileri sekmesinde

tanımlanan klasörün kod bilgisinin yazıldığı alandır.

**Klasör Adı:** Klasör Tanımlama- Yeni Kayıt ekranında Klasör bilgileri sekmesinde tanımlanan klasörün adı bilgisinin yazıldığı alandır.

**Doküman Tipi**: Klasör Tanımlama-Yeni Kayıt ekranında Klasör bilgileri sekmesinde tanımlanan klasör doküman tipi bilgisinin ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_117.png) butonu tıklanarak açılan sistemde tanımlı Doküman tipi listesinde seçim yapıldığı alandır.Doküman Tipleri Listesi Sistem Altyapı Tanımları/Doküman İşlemleri/Doküman Tipi Tanımlama menüsünde tanımlı olarak gelmektedir. Doküman Tipi alanından eğer klasör içine hazırlanacak dokümanlar için, her zaman klasör tipinde seçilen doküman tipinin tanımlı olarak gelmesi isteniyorsa “Varsayılan” seçeneği ilgili check box işaretlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_118.png)

Doküman Tipi alanında “Değiştirilemez” seçeneği ile ilgili cehck box işaretlendiğinde, seçili olan klasöre doküman eklerken seçili olan doküman tipi dışında doküman tipi seçilemez.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_119.png)

**Otomatik Kod Şablonu Kullanımı:**	Klasör Tanımlama-Yeni Kayıt ekranında Klasör bilgileri sekmesinde otomatik kod şablonun kullanım seçeneklerinde seçim yapıldığı alandır.

Otomatik Kod Şablonu Kullanımı alanında “Otomatik” seçeneği seçildiği zaman doküman hazırlama aşamasında doküman kodu Klasör Tanımlama-Yeni Kayıt ekranında tanımlı otomatik kod şablonu alanında tanımlı kod şablonu göre otomatik olarak gelmektedir ve sistemin kod alanında müdaheleye izin vermez.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_120.png)

Otomatik Kod Şablonu Kullanımı alanında “Elle” seçeneği seçildiği zaman doküman hazırlama aşamasında doküman kodu Klasör tanımlama-Yeni Kayıt ekranında tanımlı otomatik kod şablonu alanında tanımlı kod şablonu göre otomatik olarak gelmektedir ve sistem kod alanında müdaheleye izin verir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_121.png)

**Otomatik Kod Şablonu:** Klasör Tanımlama- Yeni Kayıt ekranında Klasör bilgileri sekmesinde klasör içerinde tanımlanacak dokümanlarının kod yapısının otomatik olarak gelmesi sağlayacak, doküman kod yapısının nasıl olacağı bilgisinin tanımlandığı alandır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_122.png)

Yukarıdaki tabloda “Otomatik Kod Şablonu” alanında yapılan örneğe göre ilk kod bilgisi “2024” yılı simgelemektedir, [TIP] kodu doküman tipinin kod bilgisini getirir. #’ ler ise kaç haneli bir sayı aralığı olacağını simgelemektedir. Sayaç ise #’ lerin kaçtan başlayacağını belirtir.

Prosedür doküman tipinde kısa kod bilgisi varsa [TIP] alanına gelir. Kısa kod bilgisi olmadığında doküman tipinin kod bilgisi [TIP] alanında otomatik olarak gelmektedir. Prosedürün kod bilgisi “PR” ve sayac değeri “0” göre sistem  Entegre Yönetim Sistemi/Doküman İşlemleri/Doküman Hazırlama menüsü tıklanarak açılan Yeni doküman ekranında Doküman Kodu alanında kod atamaları sırasıyla aşağıdaki şekilde yapar. 2024-PR.001, 2024-PR.002, 2024-PR.003 

**Sayaç**: Klasör Tanımlama- Yeni Kayıt ekranında Klasör bilgileri sekmesinde doküman otomatik kod şablonu kullanılacaksa, doküman kodunun hangi sayıdan başlayacağı bilgisi yazıldığı alandır. Sayaç değerine 0 denilirse, eklenen dokümanlar kod şablonuna göre 1, 2, 3… şeklinde artarak devam eder. Klasör tanımlamada bu sayaç “0” olarak tanımlanır. Ancak klasöre toplu aktarımla doküman aktardıktan sonra, klasörün içerisine toplam kaç tane doküman atıldıysa sayaç o sayıdan başlatılır. Örneğin klasörün içerisine toplu aktarımla birlikte 20 adet doküman atıldıysa, klasör tanımlama ekranından ilgili klasör seçilerek klasör bilgileri ekranındaki sayaç “20” olarak değiştirilip kaydedilir. Böylece yeni hazırlanan doküman için sistem tarafından doküman kodu “21” olarak verilecektir.

**Ön Kontrol Tipi:** Klasör Tanımlama- Yeni Kayıt ekranında Klasör bilgileri sekmesinde parametrelere bağlı olarak görüntülenen bir alandır. Eğer doküman hazırlandıktan sonra kontrole gitmeden önce ön kontrole gitmesi isteniyorsa Doküman Yönetimi parametrelerinden 76.numaralı “Dokumanda Ön Kontrol Kullanılsın mı?” parametresinin parametre değeri “Evet” olarak seçilerek parametre aktif edilmelidir.

![ref38]

Ön Kontrol tipi olarak seçeneklerin görüntülenmeside ilgili parametrelerin aktif edilmesi ile sağlanmaktadır. 

**Ön Kontrol Tipi olarak grup seçilmesi için;**

Doküman Yönetimi Parametrelerinde 296 numaralı” Dokumanlarda Ön Kontrol Grubu kullanılacak mı?” parametresinin parametre değeri “Evet” seçilerek parametre “Aktif “ edilir.

![ref39]

Parametre aktif edildikten sonra Ön Kontrol Tipi alanında Grup seçeneği görüntülenir. Klasör içerisinde hazırlanacak dokümanlarda görüntülenen Ön Kontrol Grubu alanında ![ref40] butonu tıklanarak açılan sistemde tanımlı kullanıcı grubu listesinde ön kontrol yapacak kullanıcı grubu  seçilir.Seçilen kullanıcı grubunu  dokümanın yapı ve içerik kontrollünün yapılması sağlar.

![ref41]

**Ön Kontrol Tipi olarak Kullanıcı seçilmesi için;**

![ref42]

Ön Kontrol tipi olarak kullanıcı seçildiğinde görüntülenen Ön Kontrol Edecek alanında ![ref40] butonu tıklanarak açılan sistemde tanımlı Pozisyon listesinde ön kontrol yapacak pozisyon seçilir.Seçilen Pozisyondaki kişi dokümanın yapı ve içerik kontrollünün yapılması sağlar.Ön kontrol aşamasında hazırlanan doküman; hazırlayan kişinin departmanındaki ilgili kullanıcılara, hazırlayan kişinin amirine ya da doküman hakkında bilgisi olan bir kullanıcıya gönderilir. Kontrol aşamasında ise hazırlanan doküman yapı ve içerik kontrolü için genelde kalite sistem sorumlularına iletilir. 

**Ön Kontrol Tipi olarak Rol seçilmesi için;**

![ref43]

Ön Kontrol tipi olarak Rol seçildiğinde görüntülenen Ön Kontrol Rolü  alanında ![ref40] butonu tıklanarak açılan sistemde tanımlı Rol listesinde ön kontrol yapacak Rol seçilir.Seçilen Roldeki  kişi dokümanın yapı ve içerik kontrollünün yapılması sağlar.  Ön kontrol tipi alanında Rol seçeneği parametreye bağlı olarak görüntülenen bir alandır. Doküman Yönetimi parametrelerinde 298 numaralı “Dokuman ön kontrol aşamasında rol kullanılsın mı?(E/H)” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. 

![ref44]

Parametre aktif edildikten sonra Ön Kontrol Tipi seçeneklerinde rol seçeneğide ilgili alanda görüntülenir.Ön Kontrol Tipi alanında tanımlanan klasör için Kullanıcı tipi olarak seçim işlemi yapılır.

**Ön Kontrol Edecek:** Klasör Tanımlama- Yeni Kayıt ekranında Klasör bilgileri sekmesinde tanımlanacak klasör için  ![ref40] butonu tıklanarak açılan sistemde tanımlı Pozisyon listesinde ön kontrole gidecek pozisyon seçim işlemi yapılır. Tanımlanan klasörde hazırlanan dokümanlarda Pozisyondaki kişi ön kontrol aşamada yapı ve içerik olarak dokümanların incelenmesini yapacaktır.

**Kontrol Tipi:** Klasör Tanımlama- Yeni Kayıt ekranında Klasör bilgileri sekmesinde doküman kontrol tipinin seçeneklerin seçildiği alandır. 

**Kontrol Tipi olarak  Grup seçilmesi için;**

![ref45] Kontrol tipi olarak Grup seçildiğinde görüntülenen Kontrol Grubu  alanında ![ref40] butonu tıklanarak açılan sistemde tanımlı Kullanıcı Grubu listesinde onaydan önce dokümanın  kontrolünü yapacak  Kullanıcı grubu  seçilir.Seçilen Kullanıcı Grubu doküman üzerinde her türlü değişikliği yapma yetkisine sahiptir. Dokümanı yapı ve içerik olarak  kontrollü yaptığı gibi  doküman hazırlama aşamasındaki tüm sekmeler üzerinde değişiklik yapma yetkisine sahiptir. Grup kontrolünde gruptaki bir kişinin kontrolü yeterlidir. Bir kişi kontrol ettiğinde doküman onay statüsüne geçecektir. Parametreye bağlı  olarak görüntülenen alandır. Doküman Yönetimi parametrelerinde 80 numaralı “Dokumanlarda Kontrol Grubu kullanılacak mı?” parametresinin değeri “Evet” seçilerek parametre aktif edilir.

![ref46] Parametre aktif edildikten sonra Kontrol Tipi alanında Grup seçeneği görüntülenir ve hazırlanan dokümanın  onayında önce bir gruba kontrole gönderilmesi için seçim işlemi   yapılır.

**Kontrol Tipi olarak Kullanıcı seçilmesi için;**

![ref47]

Kontrol tipi olarak Kullanıcı seçildiğinde görüntülenen Kullanıcı  alanında ![ref40] butonu tıklanarak açılan sistemde tanımlı Pozisyon listesinde onaydan önce dokümanın  kontrolünü yapacak  Pozisyon seçilir.Seçilen Pozisyondaki kişi doküman üzerinde her türlü değişikliği yapma yetkisine sahiptir. Dokümanı yapı ve içerik olarak  kontrollü yaptığı gibi  doküman hazırlama aşamasındaki tüm sekmeler üzerinde değişiklik yapma yetkisine sahiptir.

**Kontrol Tipi olarak Rol seçilmesi için;**

![ref48]

Kontrol tipi olarak Rol seçildiğinde görüntülenen Kontrol Rolü alanında ![ref40] butonu tıklanarak açılan sistemde tanımlı Rol  listesinde onaydan önce dokümanın  kontrolünü yapacak  Rol seçilir.Seçilen Rol doküman üzerinde her türlü değişikliği yapma yetkisine sahiptir. Dokümanı yapı ve içerik olarak  kontrollü yaptığı gibi  doküman hazırlama aşamasındaki tüm sekmeler üzerinde değişiklik yapma yetkisine sahiptir. Parametreye bağlı  olarak görüntülenen alandır. Doküman Yönetimi parametrelerinde 180 numaralı “Doküman kontrol aşamasında rol kullanılsın mı?(E/H)” parametresinin değeri “Evet” seçilerek parametre aktif edilir.

![ref49] Parametre aktif edildikten sonra Kontrol Tipi alanında Rol seçeneği görüntülenir ve hazırlanan dokümanın  onayında önce bir role kontrole gönderilmesi için seçim işlemi   yapılır

**Kontrol Edecek:** Klasör Tanımlama- Yeni Kayıt ekranında Klasör bilgileri sekmesinde tanımlanan klasörde hazırlanacak dokümanların kontrollü yapacak  pozisyonun  ![ref50] butonu tıklanarak açılanan sistemde tanımlı Pozisyon listesinden seçildiği alandır.

**Gözden Geçirecek:** Klasör Tanımlama- Yeni Kayıt ekranında Klasör bilgileri sekmesinde dokümanlarının kimin tarafından gözden geçileceğininin belirlendiği alandır. Gözden Geçirme Periyodu, Klasör Tanımlama ekranındaki Klasör Ayarları sekmesinden ya da yeni doküman hazırlarken gözden geçirme periyodu alanından belirlenmektedir. Bu alan boş bırakılırsa ,  Doküman Yönetimi  parametrlerinde 5 numaralı “Doküman gözden geçirme mailleri kimlere gönderilsin? H(Hazırlayana),R (Revize Edene),S (Sorumlusuna),G (Gözden Geçirecek Kişiye). Birden fazla ise virgül ile ayırarak yazınız.” parametresinde parametre değerinde seçilen değere gözden geçirmeler gitmektedir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_136.png)

**Sistem - Madde No Zorunlu Olsun:** Klasör Tanımlama- Yeni Kayıt ekranında Klasör bilgileri sekmesinde check box işaretlenirse yeni bir doküman hazırlanırken veya mevcut bir doküman revize edilirken mutlaka dokümanın standart madde numarasıyla ilişkilendirilmesi gerekir.

**Referans Doküman Zorunlu Olsun:** Klasör Tanımlama- Yeni Kayıt ekranında Klasör bilgileri sekmesinde check box işaretlenirse yeni bir doküman hazırlanırken veya mevcut bir doküman revize edilirken mutlaka dokümanın sistemde tanımlı olan başka bir dokümanla ilişkilendirilerek referans verilmesi gerekir.

**Yetki Matrisi Değiştirilemesin:** Klasör Tanımlama- Yeni Kayıt ekranında Klasör bilgileri sekmesinde check box işaretlenirse yeni bir doküman hazırlanırken veya mevcut bir doküman revize edilirken klasörde tanımlı olan yetki matrisi değiştirilemez. Klasör Yetki Matrisi ekranında “Okuma, Hazırlama/ Revize Etme, Eski Revizyonları Görme, Yazdırma, İptal Etme, Alt Klasör Tanımlama” yetkileri nasıl tanımlandıysa, doküman hazırlamada/revize etmede de öyle tanımlı gelir ve değiştirilemez.

**Dağıtım Matrisi Değiştirilemesin:** Klasör Tanımlama- Yeni Kayıt ekranında Klasör bilgileri sekmesinde check box işaretlenirse yeni bir doküman hazırlanırken veya mevcut bir doküman revize edilirken klasörde tanımlı olan dağıtım matrisi değiştirilemez. Klasör Dağıtım Matrisi ekranında dokümanın kimlere dağıtılacağı ve okuma görevlerinin kimlere atanacağı bilgisi nasıl tanımlandıysa, doküman hazırlamada/ revize etmede de öyle tanımlı gelir ve değiştirilemez.

**Onay Matrisi Değiştirilemesin:** Klasör Tanımlama- Yeni Kayıt ekranında Klasör bilgileri sekmesinde yeni bir doküman hazırlanırken veya mevcut bir doküman revize edilirken klasörde tanımlı olan onay matrisi değiştirilemez. Klasör Onay Matrisi ekranında dokümanın kimler tarafından onaylanacağı bilgisi nasıl tanımlandıysa, doküman hazırlamada/ revize etmede de öyle tanımlı gelir ve değiştirilemez.

**Kontrollü Kopya Matrisi Değiştirilemesin:** Klasör Tanımlama- Yeni Kayıt ekranında Klasör bilgileri sekmesinde yeni bir doküman hazırlanırken veya mevcut bir doküman revize edilirken klasörde tanımlı olan kontrollü kopya matrisi değiştirilemez. Klasör Kontrollü Kopya Matrisi ekranında dokümanın hangi dağıtım yerlerine kontrollü kopya olarak dağıtılacağı bilgisi nasıl tanımlandıysa, doküman hazırlamada/ revize etmede de öyle tanımlı gelir ve değiştirilemez.

**Kontrol Eden Değiştirilemesin:** Klasör Tanımlama- Yeni Kayıt ekranında Klasör bilgileri sekmesinde yeni bir doküman hazırlanırken veya mevcut bir doküman revize edilirken klasörde tanımlı olan kontrol eden değiştirilemez. Kontrol edecek alanında dokümanın kimler tarafından kontrol edecek bilgisi nasıl tanımlandıysa, doküman hazırlamada/ revize etmede de öyle tanımlı gelir ve değiştirilemez.

**Ön Kontrol Eden Değiştirilemesin:** Klasör Tanımlama- Yeni Kayıt Klasör bilgileri sekmesinde ekranında yeni bir doküman hazırlanırken veya mevcut bir doküman revize edilirken klasörde tanımlı olan ön kontrol eden değiştirilemez. Ön Kontrol edecek alanında dokümanın kimler tarafından ön kontrol edecek bilgisi nasıl tanımlandıysa, doküman hazırlamada/ revize etmede de öyle tanımlı gelir ve değiştirilemez.

**Görüş Matrisi Değiştirilemesin:** Klasör Tanımlama- Yeni Kayıt Klasör bilgileri sekmesinde ekranında yeni bir doküman hazırlanırken veya mevcut bir doküman revize edilirken klasörde tanımlı olan görüş matrisi değiştirilemez. Klasör Görüş Matrisi ekranında dokümanın kimler tarafından görüş bilgisi nasıl tanımlandıysa, doküman hazırlamada/ revize etmede de öyle tanımlı gelir ve değiştirilemez.

**Durum:** Klasör Tanımlama- Yeni Kayıt Klasör bilgileri sekmesinde ekranında tanımlanan klasörün aktif ve  pasif durumunun belirlendiği alandır. İlgili klasörün klasör ağacı ekranında görüntülenip görüntülenmeyeceğini gösterir.

**İptalde Dağıtım Matrisi Değiştirilebilsin**: Klasör Tanımlama- Yeni Kayıt Klasör bilgileri sekmesinde ekranında check box işaretlenirse mevcut bir doküman iptal edilirken klasörde tanımlı olan dağıtım matrisi değiştirilebilir. Böylece iptali gerçekleşen dokümanın bilgisi dağıtım matrisinde kimler tanımlandıysa o kullanıcılara iletilir.

**Klasör Ayarları sekmesinde;** 

Klasör nitelikleri ile ilgili detay ayarlar gerçekleştirilir. Klasörün form klasörü olup olmayacağı, klasör için hangi doküman şablonunun kullanılacağı, eğitim sorumlusu ve onaycı rol olup olmayacağı, son onaylayan kişinin aynı zamanda yayımcı olup olmayacağı, gözden geçirme periyodu, doküman revizyon matris atama şekilleri gibi özel ayarlar uygulandığı sekmedir.












![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_137.png) ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_138.png) ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_139.png) ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_140.png) ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_141.png) ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_142.png)

**Klasör ayarları sekmesinde ekranda bulunan şu bilgiler tanımlanır;**

**Form klasörü**: Klasör Tanımlama-Yeni Kayıt ekranında Klasör Ayarları sekmesinde eğer bu klasörün içine sadece form dokümanları atanacaksa Form klasörü ilgili check box işaretlenir. Bu check box işaretlendiği takdirde form klasöründeki ilgili formlar kalite kaydı işlemlerinde de kullanılır.

**Onaysız/ Kontrolsüz**: Klasör Tanımlama-Yeni Kayıt ekranında Klasör Ayarları sekmesinde eğer bu seçenekle  ilgili check box işarelenirse, bu klasör için doküman yönetimindeki kontrol /onay süreci devreden çıkmış olur. Dokümanlar kontrolsüz/ onaysız bir şekilde kaydedildiği anda yayınlanır. Rapor, standart, yönetmelik, eğitim sunumları, ölçüm sonuçları gibi dış kaynaklı dokümanlar bu şekildeki klasörlere tanımlanabilir.

**PDF’ te Kontrollü/ Kontrolsüz Yazısı Basılmasın**: Klasör Tanımlama-Yeni Kayıt ekranında Klasör Ayarları sekmesinde eğer bu seçenekle ilgili check box işarelenirse doküman görüntüleme veya yazdırma işlemlerinde PDF halindeki dokümanlarda Kontrollü/ Kontrolsüz Yazısı gösterilmez.

**Anket Kullanılacak:** Klasör Tanımlama-Yeni Kayıt ekranında Klasör Ayarları sekmesinde  eğer bu seçenek seçilirse, bu klasör içerisine hazırlanan doküman yayınlandıktan sonra dokümanla ilgili dağıtım matrisindeki kullanıcılara anket gönderilebilir. Bunun için Doküman Parametrelerinden 81.parametre olan “Dokümanda anket kulakçığı kullanılacak mı” parametresinin parmatre değeri “Evet” olarak aktif edilmelidir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_143.png) Parametre aktif edildikten sonra Doküman hazırlama/ revizyon ekranında anket kulakçığına geldikten sonra, anket sorusu istenilen formatta eklenilebilir.

**Harici Doküman :** Klasör Tanımlama-Yeni Kayıt ekranında Klasör Ayarları sekmesinde parametreye bağlı olarak görüntülenen bir alandır.322 numaralı “Doküman Hazırlama da Harici Link Kullanılsın mı?” parametre değeri “Evet” seçilerek parametre aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_144.png)

Parametre aktif edildiğinde Entegre Yönetim Sistemi/Doküman İşlemleri/Klasör Tanımlamada yeni bir klasör tanımlandığında yada bir klasör güncellendiğinde Klasör ayarları sekmesinde Harici Doküman seçeneği ilgili alan ve bu alanla ilgili check box görüntülenir. Harici Dokümanla ilgili check box işaretlendiğinde bu klasörde doküman hazırlama işlemi yapıldığında, doküman hazırlama ekranında doküman sekmesinde harici doküman seçeneği bulunur. Bu Harici doküman seçeneği ilgili check box işaretlendiğinde Dosya ekle butonu kaldırılır. Dil metin alanı olan Dokuman Dosyası Yükleme( Türkçe ) alanına görüntülenmesi istenilen link yazılır. Doküman yayınlandığında ilgili linke gidilerek doküman görüntülenir. 

**Doküman Hazırlama Şablonu**: Klasör Tanımlama-Yeni Kayıt ekranında Klasör Ayarları sekmesinde daha önceden Qdms’ e şablon olarak yüklenmiş olan doküman hazırlama şablonlarından hangisi veya hangilerinin, bu klasöre bağlı olarak doküman hazırlarken kullanılabileceğini belirtmek için kullanıldığı alandır. Klasöre bağlı hazırlanacak dokümanlarda “bu şablonu kullan” demek için bu özellik kullanılmaktadır. 

**Eğitim Sorumlusu**: Klasör Tanımlama-Yeni Kayıt ekranında Klasör Ayarları sekmesinde Klasörlere bağlı dokümanlar için eğitim verilmesi düşünülüyor ise Eğitim sorumlusu alanına hazırlanan doküman için kimin eğitim vereceği bilgisi tanımlandığı alandır. Eğitim sorumlusu olarak sistemde tanımlı olan pozisyonlardan biri seçilebilir. “Eğitim Sorumlusu Haz/Rev.Eden olarak atansın” ilgili check box  işaretlenirse, eğitim sorumlusu olarak dokümanı hazırlayan/ revize eden personel kimse ona görev olarak atanması sağlanır. “Değiştirilemez”  ile ilgili check box işaretlenirse klasörde tanımlanan eğitim sorumlusu bilgisinin doküman hazırlama/ revizyon işlemlerinde değiştirilmesi engellenmiş olur.

**Onaycı Rol**: Klasör Tanımlama-Yeni Kayıt ekranında Klasör Ayarları sekmesinde doküman onay süreci sistemdeki belli rollere bağlanacaksa “Onaycı Rol” kısmı kullanıldığı alandır. Sistemde tanımlı olan roller Hazırlayan/ Revize Edenin Amiri ve Hazırlayan/ Revize Edenin Departman Sorumlusu rolleridir. Firmadaki ihtiyaca göre Bimser teknik personelleri tarafından yeni roller tanımlanabilir. Bu rollerden uygun olan onay başlangıç rolü seçilir. “Seviye” kutucuğununda seçilen rolden itibaren kaç üst seviye onay için yukarı çıkılacağının bilgisi girilir.

**Onaycı Rol (Üst Ünvan Sınırı)**: Klasör Tanımlama-Yeni Kayıt ekranında Klasör Ayarları sekmesinde eğer klasörde onaycı rol seçilmişse, bu onay sürecinin hangi ünvana kadar süreceğini gösteren ayarının   yapıldığı alandır. Listeden ünvan seçilir.  Seçili olan ünvana geldiğinde onay akışı durur.

**Onaycı Rol (Alt Ünvan Sınırı)**: Klasör Tanımlama-Yeni Kayıt ekranında Klasör Ayarları sekmesinde eğer klasörde onaycı rol seçilmişse, bu onay sürecinin hangi ünvanda başlayacağını gösteren ayarrının yapıldığı alandır. Listeden ünvan seçilir.  Seçili olan ünvanda onay akışı başlar.

**Tersten Çalışsın:** Klasör Tanımlama-Yeni Kayıt ekranında Klasör Ayarları sekmesinde Onaycı Rol seçimindeki akışında tersten çalışması isteniyorsa (yani son onaycıdan ilk onaycıya doğru) ilgili  check box  işaretlenir.

**Yayımlama**: Klasör Tanımlama-Yeni Kayıt ekranında Klasör Ayarları sekmesinde onay akışından sonra eğer firmada dokümanlar tek elden yayımlanıyorsa, yayımlama aktif edilir 0. onaycı tarafından dokümanlar yayımlandığı alandır.

**Gözden Geçirilecek Mi**: Klasör Tanımlama-Yeni Kayıt ekranında Klasör Ayarları sekmesinde Klasör içindeki dokümanların gözden geçirilip geçirilmeyeceğinin belirlendiği alandır.

**Gözden Geçirme Periyodu (Ay)**: Klasör Tanımlama-Yeni Kayıt ekranında Klasör Ayarları sekmesinde gözden geçirme süresinin kaç ay olacağının belirlendiği alandır.

**Gözden Geçirme Atanma Şekli:** Klasör Tanımlama-Yeni Kayıt ekranında Klasör Ayarları sekmesinde gözden geçirme atama şekli olarak  klasör veya doküman seçeneklerinden seçildiği alandır.Gözden geçirme atama şekli Klasör seçildiğinde Klasör ayarları sekmesinde gözden geçirme Perioydu(Ay)  alanında yazılan gözden geçirme periyodu baz alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_145.png)

Gözden geçirme atama şekli doküman seçildiğinde Doküman Hazırlama aşamasında açılan Yeni Doküman ekranında Diğer bilgiler sekmesinde gözden geçirme Periyodu(Ay)  alanında yazılan gözden geçirme periyodu baz alınır.  

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_146.png)     

**Kontrollü Kopya Yazdırma Nedeni**: Klasör Tanımlama-Yeni Kayıt ekranında Klasör Ayarları sekmesinde  Kontrollü Kopya özelliği kullanılacaksa bu alan seçilir. Sistemden bir dokümanı kontrollü kopya olarak alınması istenildiğinde, kontrollü kopya alma nedeni bilgisinin sistemde zorunlu olup olmadığının ayarının yapıldığı alandır. “Şirket Parametresi, Zorunlu, Zorunlu Değil” seçeneklerinden seçim yapılır. “Şirket Parametresi” doküman parametrelerinden 133.parametreye göre tanımlı olan zorunluluk durumunu belirtir.Doküman Yönetimi Modülü parametrelerinden 133 numaralı “Kontrollü Kopya Yazdırma Sayfasında Yazdırma Nedeni Zorunlu Olsun Mu?(E/H)” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_147.png)

Kontrollu Kopya Yazdırma Sayfasında Yazdırma nedeni yazılmadan kontrollü kopya yazdırma işlemi yapılmaması sağlanır. 

**Okudum Onayı;** Klasör Tanımlama-Yeni Kayıt ekranında Klasör Ayarları sekmesinde  tanımlanan bu klasörün içerisine hazırlanacak olan dokümanlar yayınlandıktan sonra dağıtım onayındaki kişilerden doküman okuma onayının alınıp alınmayacağının belirlendiği alandır. “Şirket Parametresi, Okudum Onayı Alınsın, Okudum Onayı Alınmasın” seçeneklerinden seçim yapılır. “Şirket Parametresi” doküman parametrelerinden 106.parametreye göre tanımlı olan durumunu belirtir.Doküman Yönetimi Modülü parametrelerinde 106. Numaralı “Dokuman görmede okudum onayı alınsın mı?” parametresinde parametre değeri “Evet” seçilerek parametre aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_148.png)

“Şirket Parametresi” doküman parametrelerinden 106.parametreye göre tanımlı olan durumunu belirtir. Parametre aktif edildiktenden sonra klasör içerinde tanımlı dokümanlar dağıtım matrisinda atama yapılan kullanıcıların Bekleyen İşlerimde “Okunması Gereken Dokümanlar Listesi” ve “Okunması Gereken Önemli Dokümanlar listesi” görevleri tıklanarak açılan doküman görme ekranlarında dokümanı okudukları dair “Dokümanı okudum.Kabul Ediyorum.” alanı görüntülenir. Bu  alanı  ilgili kullanıcılar tıklayarak dokümanı okudu statüsüne gelmesini sağlar.

**Revizyon No Değişimi**: Klasör Tanımlama-Yeni Kayıt ekranında Klasör Ayarları sekmesinde   Doküman revizyon sürecindeki revizyon numarasının sistem tarafından otomatik olarak 1-2-3,vb. şeklinden bir artarak otomatik gelmesi isteniyorsa “otomatik” seçeneği seçilir. Eğer revizyon numarası kullanıcı tarafından manuel verilsin isteniyorsa “manuel” seçeneği seçilir.

**Ek Dosyalar Revizyonda Taşınsın Mı?:** Klasör Tanımlama-Yeni Kayıt ekranında Klasör Ayarları sekmesinde  Klasör içerisindeki bir doküman revizyon edilirken, revizyon edilen ana dokümana ait ek dosyalar varsa, bu ek dosyaların yeni revizyonla dokümanın son haline taşınıp taşınmayacağının belirlendiği alandır. “Şirket Parametresi, Taşınsın, Taşınmasın” seçeneklerinden seçim yapılır. “Şirket Parametresi” doküman parametrelerinden 135. parametreye göre tanımlı olan durumunu belirtir.Doküman Yönetimi Modülü parametrelerinde “Revizyon sırasında ek dosyalar yeni revizyona taşınsın mı?(E/H)”parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_149.png)

Parametre aktif edildiktenden sonra ana dokümanda revizyon işlemi yapılırken , ana doküman ait ek dosyalarda varsa, bu ek dosyaların yeni revizyonla dokümanın son haline taşınıp taşınması sağlanılır.

**Kontrol Zorunlu**: Klasör Tanımlama-Yeni Kayıt ekranında Klasör Ayarları sekmesinde   Doküman yönetimi sürecinde kontrol basamağı zorunlu olsun, dokümanlar onay sürecinden önce mutlaka kontrol sürecine gitsin isteniyorsa ilgili check box işaretlenir.

**Süreç Matrisi Zorunlu**: Klasör Tanımlama-Yeni Kayıt ekranında Klasör Ayarları sekmesinde   Doküman yönetimi sürecinde hazırlanan dokümanın  sistemdeki süreç/süreçler ile ilişkilendirilmesi zorunlu olsun, doküman mutlaka bir sürece bağlansın isteniyorsa ilgili check box şaretlenir. Bu işlemin yapılması için Doküman Yönetimi parametrelerinden 41 numaralı “Doküman Modulünde Süreçler kulakçığı kullanılacak mı? (E/H)” parametresinin parametre değerinin “Evet” seçilerek parametre aktif edilerek süreç sekmesinin görüntülenmesi sağlanmaktadır.  

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_150.png)

Süreç sekmesinde görüntülendikten sonra Süreç Matrisi Zorunlu alanı ile ilgil check box işaretli olduğunda süreç sekmesinde süreç ekleme işleminin zorunluluğu getirilir.

**Doküman Print Formatı**: Klasör Tanımlama-Yeni Kayıt ekranında Klasör Ayarları sekmesinde    klasörün içerisine doküman hazırlanmak istenildiği zaman, dokümanın hangi formatta hazırlanacağının belirlendiği alandır. Sistem Altyapı Tanımları/Doküman Yönetim/ Doküman Print Formatı Tanımlama menüsünde tanımlanan doküman print formatı (alt bilgi/ üst bilgi içeriği) seçilerek dokümanın istenilen formata göre hazırlanması sağlanır.

**Zorunlu Dil Dosyaları**: Klasör Tanımlama-Yeni Kayıt ekranında Klasör Ayarları sekmesinde    dokümanların başka dillerde de kullanılması isteniyorsa, ekranda gözüken dil seçeneklerinden hangi dil seçeneklerinde zorunlu olacağı bilgisi seçilir ve zorunlu dil seçeneği için sistemde tanımlı olan hangi personel/Kullanıcı Grubu  tarafından dil çevirisi görevinin gerçekleştirileceği belirlendiği alandır.Dil çevirisi bir kullanıcı tarafından yapılacak ise ![ref51] butonu tıklanarak açılan sistemde tanımlı personel listesinde veya Dil çevirisi bir Kullanıcı grubu tarafından yapılacak ise  ![ref51] butonu tıklanarak açılan sistemde tanımlı Kullanıcı Grubu listesinde seçim yapılır.

**En az bir tanesinin onay matrisinde bulunması zorunlu pozisyonlar**: Klasör Tanımlama-Yeni Kayıt ekranında Klasör Ayarları sekmesinde ilgili klasörde hazırlanan dokümanlar için, zorunlu olarak bulunması gereken onaycı pozisyonun ![ref51] butonu tıklanarak açılan sistemde tanımlı Pozisyon Listesinde seçimin yapıldığı alandır.  Sistemde doküman hazırlanırken, hazırlayan personel tarafından belirlenen bu onaycı silinirse, sistem tarafından onay sürecine iletilmez, sistem onaycı pozisyonunda bulunması gereken zorunlu onaycının bulunmadığına dair uyarı verir.

**Bir tanesinin kontrolde bulunması zorunlu pozisyonlar**: Klasör Tanımlama-Yeni Kayıt ekranında Klasör Ayarları sekmesinde ilgili klasörde hazırlanan dokümanlar için, zorunlu olarak bulunması gereken kontrolcü pozisyonun![ref51] butonu tıklanarak açılan sistemde tanımlı 

Pozisyon Listesinde seçimin yapıldığı alandır. Sistemde doküman hazırlanırken, hazırlayan personel tarafından belirlenen bu kontrolcü silinirse, sistem tarafından kontrol sürecine iletilmez, sistem kontrolcü pozisyonunda bulunması gereken zorunlu kontrolcünün bulunmadığına dair uyarı verir.

**Doküman Hazırlama Talebi Gidecek Grup:** Klasör Tanımlama-Yeni Kayıt ekranında Klasör Ayarları sekmesinde sistemde, bu klasör üzerinde, doküman hazırlama yetkisi olmayan kullanıcılar tarafından doküman hazırlama talebi yapılsın isteniyorsa, doküman parametrelerinden 62, 229, 270 ve 271. parametreler aktif edilir. 

**62 numaralı Parametre ;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_152.png)

Parametrede parametre değerinde Doküman hazırlama Talebine cevap süresi gün bazında sayısal bir değer olarak bilgisi yazılır.

**229  numaralı Parametre ;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_153.png)

Parametre değeri “Evet” seçilerek Doküman Hazırlama Talebi Yap fonksiyonunun aktif edilmesi sağlanır.

**270 numaralı Parametre ;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_154.png)

Doküman Modülünde Doküman Hazırlama Talepleri kimlere gönderilmesi ayarlandığı parametredir.Parametresinde parametre değerine  Kullanıcı için :K değeri, Yönetici için :Y Değeri yazılır.

**271 numaralı Parametre ;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_155.png)

Doküman Hazırlama Talebi yaparken kullanıcı seçilip, seçilmemesinin ayarının yapıldığı parametredir.

Bu klasör kapsamında doküman hazırlama taleplerinin hangi kullanıcı grubu tarafından değerlendirilmesi isteniyorsa ![ref51] butonu tıklanarak açılan sistemde tanımlı Kullanıcı Grubu listesinde  o kullanıcı grubu seçilir.

**Revizyonda Yetki/ Dağıtım/ Onay/ Görüş/ Kontrollü Kopya Matrisi Atanma Şekli:** Klasör Tanımlama-Yeni Kayıt ekranında Klasör Ayarları sekmesinde  Klasör içerisindeki bir doküman revizyon edilirken “Yetki, Dağıtım, Onay, Görüş Matrislerinin ve Kontrollü Kopya Atama Şeklinin” mevcut dokümandan mı, dokümanın ait olduğu ilgili klasörden mi yoksa doküman tipinden mi yapılacağının belirlendiği ayarlardır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_156.png)

**Baskı Kullanılsın Mı?:** Klasör Tanımlama-Yeni Kayıt ekranında Klasör Ayarları sekmesinde    baskı kullanıp, kullanılmamasının ayarlandığı alandır.

**Baskı Alırken Mükerrer Kayıt Kontrolü Yapılacak Mı?:** Klasör Tanımlama-Yeni Kayıt ekranında Klasör Ayarları sekmesinde klasörde bulunan doküman için kontrollü/ kontrolsüz kopyalarda baskı özelliği kullanılarak, yazıcıda basılan dokümanlara ait bilgilerin sistemde tutulması ve alınan baskıda gösterilmesi sağlanabilir. Eğer baskı alırken sistemde tekrar eden kayıtlar varsa, bu kayıtların kontrolünün sistem tarafından yapılıp yapılmayacağının ayarlanması bu alandan yapılır.

**Yetki Matrisi sekmesinde;**

Klasör içerisindeki dokümanlar üzerinde hangi pozisyon ya da kullanıcı gruplarının “okuma, yazdırma, hazırlama/ revizyon, eski revizyonları görme, iptal talebi yapma, alt klasör tanımlama” yetkilerinden hangilerine sahip olacağının belirlenmesi sağlandığı sekmedir. Klasör için yetkiler verilirken doğru kullanıcı gruplarına ya da doğru pozisyonlara doğru yetkileri vermek önemlidir.

Belirlenen yetkiler ile klasör içerindeki tüm dokümanlar kapsamında aşağıdaki yetkiler verilir;

- Hangi kullanıcıların dokümanları görebileceği/ okuyabileceği,
- Hangi kullanıcıların dokümanları bilgisayarına indirip yazdırabileceği,
- Hangi kullanıcıların bu klasöre doküman hazırlayabileceği, klasör içerisinde bulunan mevcut dokümanı revize edebileceği,
- Hangi kullanıcıların dokümanların eski revizyondaki hallerini görebileceği,
- Hangi kullanıcıların dokümanları iptal edebileceği,
- Hangi kullanıcıların klasörün altına başka klasörler tanımlayabileceği,
- Hangi kullanıcıların zorunlu olarak yetki matrisinde bulunması gerektiği.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_157.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref7]: Seçili olan kullanıcı grubundaki personelleri gösterir.

![ref8]: Listeye pozisyon eklenir.

![ref9] : Listeye kullanıcı grubu eklenir.

![ref17] :Yetki matrisinde seçili satırın silinme işlemi yapılır.

![ref9]: Listede seçili olan pozisyondaki/ kullanıcı grubundaki yetkileri siler.

Klasöre yetki matrisi atamak için  ![ref9]/ ![ref8] butonları tıklanır. Sistemde tanımlı olan Kullanıcı Grubu/ Pozisyon listesinde yetki verilmek istenilen kullanıcılar için seçim yapılır. Hangi yetkiler verilmek isteniyorsa işaretlenir.

Klasör Tanımlama ekranında Yetki matrisi sekmesinde ![ref9] butonu tıklanarak sistemde tanımlı Kullanıcı grubu listesinde yetki matrisinde yetkilendirme işlemi yapılacak Kullanıcı Grubu ekleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_158.png)

Açılan Kullanıcı grubu listesinde Kullanıcı grubu seçim işlemi yapılarak ekranın sol üst köşesindeki ![ref52]  butonu tıklanarak ekleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_160.png)

Kullanıcı grubu ekleme işleminde sonra Yetki matrisi sekmesinde hangi yetkiler verilmek isteniyorsa ilgili yetkiler ilgili check box’lar işaretlenerek yetki matrisinde kullanıcı grubu bazlı yetkilendirme işlemi yapılır. Yetki matrisinde okuma yetkisi varsayılan olarak sistem tarafında işaretli olarak gelir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_161.png)

Klasör Tanımlama-Yeni Kayıt ekranında Yetki Matrisi sekmesinde ![ref8]  butonu tıklanarak listeye pozisyon ekleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_162.png)

Açılan Pozisyon Listesi ilgili pozisyon![ref52]  butonu tıklanarak seçim işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_163.png)

Pozisyon seçim işleminde sonra ilgili pozisyonla ilgili yetkilendirme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_164.png)

**Dağıtım Matrisi sekmesinde;**

Klasör içerisinde hazırlanan dokümanların yayınlandıktan sonra hangi kullanıcılara/ kullanıcı gruplarına dağıtılacağı, okuma görevi olarak kimlere atanacağı belirlendiği sekmedir. Dokümanlar yayınlandığında, dokümanın dağıtımında bulunan personellere doküman okuma bildirimi gider ve doküman dağıtımı yapılan bu kişiler dokümanları okunmakla yükümlüdür. 

Dağıtım Matrisi sekmesinde doğru kullanıcılar/ kullanıcı grupları belirlenerek, dokümanların doğru kullanıcılara dağıtılması sağlanır. Böylece yayınlanan doküman ile ilgisi olmayan kullanıcılara dağıtım mailleri ve okuma görevlerinin gitmesi engellenmiş olur. Doküman yayımlandığında buradaki belirtilen grup veya kişilerin Bekleyen İşlerim sayfasında **“Okunması Gereken Doküman Listesi”** görevi düşer.

Klasöre bağlı dokümanlar bazı kullanıcı/ kullanıcı grupları için çok daha önemli ise “Önemli” alanın ile check box işaretlenir. Önemli alanı ile ilgili check box  işaretlenen pozisyon/ kullanıcı gruplarına Bekleyen İşlerim sayfasında  **“Okunması Gereken Önemli Dokümanlar Listesi”** olarak görev düşer. Önemli alanı parametreye bağlı olarak görüntülenen bir alandır. Doküman Yönetimi Modülü parametrelerinde 273 numaralı “Dağıtım matrisinde Önemli Dokuman fonksiyonu kullanılacak mı?” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir.

![][ref11]

Parametre aktif edildikten sonra Dağıtım Matrisi sekmesinde “Önemli” alanı görüntülenir.

Doküman, “Okuma görevi düşmesin” olarak işaretlenen kullanıcı grupları veya kişilere görev olarak düşmesi sistem tarafından engellenir. Dağıtım matrisinde “Okuma görevi düşmesin” alanı parametreye bağlı olarak görüntülenen bir alandır.Doküman Yönetimi parametrelerine 274 numaralı “Dağıtım matrisinde Okuma Görevi Düşmesin fonksiyonu kullanılacak mı ?” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. 

![][ref12]

Parametre aktif edildikten sonra “Okuma görevi düşmesin” alanı dağıtım matrisi sekmesinde görüntülenir.

Aynı zamanda dokümanda anket özelliği kullanılıyor ise, anket gönderilmesi istenilen kullanıcılar/ kullanıcı grupları için dağıtım matrisinden Anket alanı ile ilgili check box işaretlenir. Dağıtım Matrisindeki Anket alanı parametreye bağlı olarak görüntülenen bir alandır. Doküman Yönetimi Modülü parametrelerinde 81 numaralı “Dokumanda Anket kulakçığı kullanılacak mı? (E/H)” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. Parametre aktif edildikten sonra Dağıtım Matrisi sekmesinde Anket alanı görüntülenir. Klasör içerisinde dokümanlarda diğer bilgiler sekmesinde “Anket Kullanılacak” ilgili check box işaretlenir. Anket sorularının tanımlanacak anket sekmesinin aktif edilmesi sağlanır.

![][ref13]

Anket sekmesi tıklanarak Soru tanımlama ekranı görüntülenir.

![][ref14]

Anket sekmesinde ![ref15] butonu tıklanarak Anket ile ilgili soruların tanımlama işlemi yapılarak Anket tanıımlama işlemi yapılır.

![][ref16]

Anket Tanımlama işlemi yapılan dokümanda dağıtım matrisi sekmesinde eklenen kullanıcı /Kullanıcı Gruplarından “Anket” alanı ile ilgili check box işaretli ise anket gönderilme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_165.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref7]: Seçili olan kullanıcı grubundaki personelleri gösterir.

![ref8]: Listeye pozisyon eklenir.

![ref9] : Listeye kullanıcı grubu eklenir

![ref17] : Listede seçili olan pozisyondaki/ kullanıcı grubundaki dağıtımı siler.

Klasöre dağıtım matrisi atamak için  ![ref9]/ ![ref8] butonlarına tıklanır. Sistemde tanımlı olan Kullanıcı Grubu/ Pozisyon listesinden dağıtıma eklenmek istenilen kullanıcılar için seçim yapılır. 

Klasör Tanımlama -Yeni Kayıt ekranında Dağıtım Matrisi sekmesinde ![ref9] butonu tıklanarak Dağıtım matrisine kullanıcı grubu ekleme işlemi yapılır

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_166.png)

Açılan Kullanıcı Grubu listesinde Kullanıcı Grubu seçim işlemi  yapılarak ![ref53]  butonu tıklanarak dağıtım matrisine Kullanıcı grubu ekleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_168.png)

Klasör Tanımlama -Yeni Kayıt ekranında Dağıtım Matrisi ekranında ![ref7] butonu tıklanarak kullanıcı Grubundaki grup üyelerin listesi görüntünlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_169.png)

Klasör  Tanımlama -Yeni Kayıt ekranında Dağıtım Matrisi sekmesinde ![ref8]  butonu tıklanarak dağıtım matrisine pozisyon ekleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_170.png)

Açılan Pozisyon Listesinden ilgili Pozisyon seçilerek ekranın sol üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_171.png)  butonu tıklanarak  pozisyon ekleme işlemi dağıtım matrisine yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_172.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_173.png)

**Onay Matrisi sekmesinde;**

Klasör içindeki dokümanların hazırlama, revizyon ve iptal işlemlerinde onaya gideceği pozisyonlar ve onay sıralaması belirlendiği sekmedir. Onay Matrisine pozisyonlar eklenir, eklenen pozisyonların seviyesi belirlenir. Birden fazla onaycı var ise, en son onaycı 0. seviyede olmalıdır. 0. seviye tek ve son onaycıya ait olmalıdır, diğer seviyelerde birden fazla onaycı bulunabilir. 0. seviyedeki pozisyon hiyerarşisinde en üst seviyeyi ifade eder. Klasör içerisinde hazırlanacak dokümanlar için onay matrisinde seviye kısmı ters mantıkla çalışmaktadır.

Onay işleminde seviye kısmında yazılan değer “0” sıfır ise  0 seviyesindeki onaycı son onaycıdır.

1\.Görseldeki  dokümanda onay işleminde seviye kısmındaki değer “0” olup son onaycı olduğundan sadece son onaycı olan pozisyondaki kişiye doküman onaya gider.

![ref18]

2\.Görseldeki dokümanda  onay işleminde tersten başa doğru onaya gider. İlk olarak “1”  seviyesindeki onaycı dokümanı onaylama işlemi yapar. Son olarak “0”seviyesindeki onaycı dokümanın onaylama işlemini yapar.

![][ref19]

3\. Görseldeki dokümanda onay işleminde paralel onay olarak tanımlanır. Paralel onaylama işleminde aynı seviyede onaycılar olup , belli bir sıralama gerekmekten onaylama işlemi yapılır. Tüm onaycıların onaylama işlemi bittikten sonra dokümanda onay işlemi biter. “0” seviyesindeki herhangi bir onaycının sıralama gerekmekten onaylama işlemi yaparlar. 

![][ref20]

4\.Görseldeki dokümanda onay işleminde tersten başa doğru onaya gider. 1.seviyesindeki onaycılardan herhangi bir sıralama gerekmekteden 1.seviyedeki onaycıların onaylama işlemi yapıldıktan sonra son onaycı olan “0” seviyedeki pozisyondaki kişiye onaylama işlemi yapılır.

![][ref21]

**Not:** Eğer sistemde klasör ayarları sekmesindeki “Onaycı Rol” kullanılacaksa onay matrisinde işlem yapılmaz, onay süreci onaycı rol akışına göre çalışır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_174.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref22] : Listeye pozisyon eklenir.

![ref54] :Listede seçili olan pozisyonu siler. 

Klasörde onay matrisinde bulunması istenilen onaycıları atamak için ![ref22] butonuna tıklanır. Sistemde tanımlı olan pozisyon listesinden onay matrisine eklenmek istenilen kullanıcılar için seçim yapılır. 

Klasör Tanımlama-Yeni Kayıt ekranında Onay matrisi sekmesinde onay matrisine onaycı ekleme işlemi için ![ref22] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_176.png)

Açılan Pozisyon listesinde onaycı seçim işleminde sonra ekranın sol üst köşesindeki ![ref53]  butonu tıklnarak onaycı ekleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_177.png)

**Görüş Matrisi sekmesinde;**

Klasör içerisinde oluşturulan dokümanların kontrol/ onay sürecine gönderilmeden önce belli kişilere görüşe gidip gitmeyeceği belirlendiği sekmedir. Eğer doküman yönetimi sürecinde görüş alma/verme işlemleri kullanılmayacaksa Doküman Yönetimi  parametrelerinde 38. “Doküman Modülünde Görüş Matrisi kulakçığı kullanılacak mı?” parametresinin parametre değeri “Hayır” seçilerek parametre pasif  edilir. Parametre pasif edildiğinde  Klasör ve klasör içerindeki dokümanlarda görüş matrisi sekmesi görüntülenmez. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_178.png)

Görüş matrisi tamamen opsiyoneldir. Eğer klasördeki tüm dokümanların kontrole/onaya gönderilmeden önce belli bir pozisyondan dokümanla ilgili görüş alınması isteniyorsa ve bu görüşçüler tüm dokümanlar için aynıysa/belirliyse Görüş Matrisi sekmesine pozisyon eklenir. Klasörde yapılan bu işlem, klasör içerisindeki tüm dokümanları kapsamaktadır. Görüş Matrisi sekmesi; doküman özelinde de seçilebilir. Bunun için doküman hazırlama/revizyon işlemlerinde hazırlayan kişi tarafından görüş matrisi seçilerek, dokümanla ilgili doğru kullanıcılardan görüş alınması sağlanabilir. Bu durumda klasördeki görüş matrisi sekmesinde tanımlama yapılmayarak, boş bırakılması yeterlidir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_179.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref55] : Listeye pozisyon eklenir.

![ref56] :Listede seçili olan görüş pozisyonunu siler. 

Klasörde görüş matrisinde bulunması istenilen görüşçüleri atamak için ![ref55] butonuna tıklanır. Sistemde tanımlı olan pozisyon listesinden görüş matrisine eklenmek istenilen kullanıcılar için seçim yapılır. 

Klasör Tanımlama-Yeni Kayıt ekranında Görüş  matrisi sekmesinde görüş  matrisine görüşcü ekleme işlemi için ![ref22] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_182.png)

Açılan Pozisyon listesinde görüşcü seçim işleminde sonra ekranın sol üst köşesindeki ![ref53]  butonu tıklanarak görüş matrisine  görüşcü  ekleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_183.png)

**Devam Politikası:**

Görüş matrisinde Devam politikası alanında Gün ve kişi alanları bulunmaktadır. Gün alanında 3 gün içerisinde Kişi alanında 1 kişinin görüşünün alınması gerekmektedir. 3 gün içerisinde görüşcünün görüş bildirmesi ile klasör içerisindeki dokümanlar “Görüşten Dönen Dokümanlar listesi “ olarak hazırlayan kişiye gider. Görüş opsiyoneldir. Devam politikası alanında görüşcü görüş vermediği sürece  gün alanında yazan 3 gün süresinin dolması beklenmesi sağlanır.

**Kontrol Kopya sekmesinde;**

Klasör içerisinde oluşturulan dokümanların kontrollü kopya olarak fiziksel dağıtılacağı yerler sistem altyapıda tanımlanan dağıtım yerleri listesinden seçildiği sekmedir.Eğer doküman yönetimi sürecinde dokümanların kontrollü kopya olarak fiziksel dağıtımı yapılmayacaksa Doküman  Yönetimi parametrelerinde 39 numaralı  “Doküman Modülünde Kontrollü Kopya kulakçığı kullanılacak mı?” parametresi “Hayır” olarak işaretlenir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_184.png)

Kontrollü kopya sekmesi tamamen opsiyoneldir. Eğer klasördeki tüm dokümanların fiziksel olarak dağıtılacağı yerler aynıysa/ belirliyse dağıtım yerleri eklenir. Klasörde yapılan bu işlem, klasör içerisindeki tüm dokümanları kapsamaktadır. Kontrollü Kopya sekmesi  doküman özelinde de seçilebilir. Bunun için doküman hazırlama/ revizyon işlemlerinde hazırlayan kişi tarafından kontrollü kopya sekmesinde fiziksel dağıtım yerleri seçilerek, dokümanla ilgili doğru fiziksel dağıtım yerlerine dokümanın dağıtılması sağlanabilir. Bu durumda klasördeki kontrollü kopya sekmesinde tanımlama yapılmayarak, boş bırakılması yeterlidir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_185.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref25]: Listeye Dağıtım yeri eklenir.

![ref26]:Listeye Dağıtım yeri grubu eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_186.png):  Listede seçili olan satır silinir.

Klasörde kontrollü kopya sekmesinde bulunması istenilen fiziksel dağıtım yerlerini atamak için  ![ref25]/ ![ref26]butonları tıklanır. Sistemde tanımlı olan dağıtım yerleri/dağıtım grupları listesinden kontrollü kopya sekmesine eklenmek istenilen dağıtım yerleri için seçim yapılır.

Klasör Tanımlama-Yeni Kayıt ekranında Kontrollu Kopya sekmesinde  Dağıtım Yeri ekleme işlemi için ![ref25]  butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_187.png)

Açılan Dağıtım Yeri listesinde Kontrol Kopya sekmesinde eklenecek Dağıtım Yeri seçilerek ekranın sol üst köşesindeki ![ref53]  butonu tıklanarak Dağıtım Yeri ekleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_188.png)

Klasör Tanımlama-Yeni Kayıt ekranında Kontrollu Kopya sekmesinde  Dağıtım Yeri grubu  ekleme işlemi için ![ref26]  butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_189.png)

Açılan Dağıtım Yeri Grubu listesinde Kontrol Kopya sekmesinde eklenecek Dağıtım Yeri Grubu seçilerek ekranın sol üst köşesindeki ![ref53]  butonu tıklanarak Dağıtım Yeri Grubu ekleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_190.png)

**Doküman Görme Formatı sekmesi**

Klasörde hazırlanacak dokümanların görme, yazdırma, kontrollü kopya yazdırma, görüşte ve onayda görüntüleme esnasındaki formatlarının belirlendiği sekmedir. “Şirket Parametresi, PDF Kullan, PDF Kullanma, Document Viewer” seçeneklerinden seçim yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_191.png)

![][ref36]![][ref37] 

Klasör tanımlama -Yeni Kayıt ekranında gerekli alanlar ilgili bilgiler yazıldıktan sonra ekranın sol üst köşesindeki ![ref57]  butuno tıklanarak Klasör tanımlama kayıt işlemi yapılır. Klasör Tanımlama işlemi yapılan klasör alt klaörlerin tanımlama işlemide yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_193.png)

Klasör Tanımlama işleminde  firmanın departman yapısına göre  klasör ağaç yapısı tasarlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_194.png)
##### **6.2.1.1.Klasör  Bilgileri Güncelleme İşlemi**
Klasör Tanımlama ekranında Klasör  bilgileri  üzerinde değiştirilme/güncelleme/düzenleme işlemi yapılır. Klasör bilgileri üzerinde güncelleme işlemi için öncelikle klasör  bilgileri değiştirilecek klasör seçilir. Klasör bilgileri değiştirilecek klasör seçili iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_195.png)  butonu tıklanarak Klasör bilgileri üzerinde  değiştirme işlemi yapılır. Klasör Tanımlama ekranında Klasör  bilgileri değiştirilecek Klasör seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_196.png)

Klasör Tanımlama ekranında klasör seçili iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_197.png) butonuna tıklanarak Klasör  Güncelleme ekranı açılır. Açılan ekranında ilgili alanlar üzerinde düzenleme ve günceleme işlemi yapılır. Klasör adı, doküman tipi, doküman kod şablonu, kontrolcü bilgisi, yetki/ dağıtım/ onay matrisleri  gibi alanlar yeni klasör yapısına göre düzenlenir

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_198.png)

Klasör Tanımlama- Kayıt Güncelleme ekranında gerekli alanlar üzerinde düzenleme işleminde sonra ekranın sol üst köşesindeki ![ref57]  butonu tıklanarak klasör kayıt güncelleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_199.png)

##### **6.2.1.2.Klasör Kodu Değiştirme İşlemi** 
Klasör Tanımlama ekranında Klasör kodu değiştirilme işlemi yapılır. Klasör kodu değiştirme işlemi için öncelikle klasör kodu değiştirilecek klasör seçilir. Klasör kodu değiştirilecek klasör seçili iken ![ref58] butonu tıklanarak Klasör kodu değiştirme işlemi yapılır. Klasör Tanımlama ekranında Klasör kodu değiştirilecek Klasör seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_201.png)

Klasör Tanımlama ekranında klasör seçili iken ![ref58]  butonuna tıklanarak Klasör Kodu Güncelleme ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_202.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Grup Kodu:** Klasör Kodu Güncelleme ekranında sistem tarafından klasörün kod bilgisi verildiği alandır.

**Yeni Klasör Kodu:** Klasör Kodu Güncelleme ekranında klasöre verilecek yeni kod bilgisinin yazıldığı alandır.

**Klasör Adı:** Klasör Kodu Güncelleme ekranında sistem tarafından klasörün adı bilgisinin verildiği alandır. İstenirse kullanıcılar bu alanda değişiklik yapıp klasöre yeni bir ad bilgisi verebilirler.

Klasör Kodu Güncelleme ekranında  yeni klasör  kodu alanında değiştir  işlemi yapılan klasör kod bilgisini yazılır. İstenirse Klasör adı alanında değişiklik yapılır. Gerekli alanlar üzerinde değişiklik yapıldıktan sonra ekranın sol üst köşesindeki ![ref57] butonu tıklanarak Klasör kodu değiştirme kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_203.png)
##### **6.2.1.3.Klasör Kopyalama İşlemi**
Klasör Tanımlama ekranında seçili olan klasör bilgileri kullanılarak yeni bir klasör oluşturulmak isteniyorsa  Klasör kopyalama işlemi yapılır. Klasör kopyalama işlemi için öncelikle kopyalama işlemi yapılacak klasör seçilir. Kopyalama işlemi yapılacak klasör seçili iken ![ref59]  butonu tıklanarak Klasör kopyalama  işlemi yapılır.  Aynı bilgilere sahip klasörde tekrar tanımlama yapmamak için kullanılmaktadır. Kopyalacak klasörün alt klasörleri  var ise kopyalami işlemi aşamasında ana klasör ile birlikte alt klasörlerinde kopyalama işlemi yapılır.Klasör Tanımlama ekranında Klasör kopyalama işlemi yapılacak  Klasör seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_205.png)

Klasör Tanımlama ekranında klasör seçili iken ![ref59]  butonuna tıklanarak Klasör Kopyalama ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_206.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Grup Kodu:** Klasör Kopyalama ekranında sistem tarafından kopyalanan klasörün kod bilgisinin verildiği alandır.

**Kopyalanacak Klasör Kodu:** Klasör Kopyalama ekranından kopyalanacak klasörün kod bilgisinin yazıldığı alandır.

**Yeni Kodu Alt Klasörün Başına Ekle:** Klasör Kopyalama ekranından yeni kodu alt klasörlerün başına ekleme işlemi isteniyorsa ilgili check box işaretlenir.

Klasör Kopyalama ekranında kopyalacak klasörü kod bilgisi yazılır. Gerekli alanlar ilgili bilgiler girildikten sonra ekranında sol  üst köşesesindeki![ref57] butonu tıklanarak Klasör kopyalama kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_207.png)
##### **6.2.1.4.Klasör Taşı İşlemi**
Klasör Tanımlama ekranında seçili olan bir klasör, başka bir klasörün altına taşıma işlemi yapılır.

Klasör Taşıma işlemi için öncelikle taşıma işlemi yapılacak klasör seçilir. Taşıma işlemi yapılacak klasör seçili iken ![ref60]  butonu tıklanarak Klasörü Taşımama  işlemi yapılır. Klasör Tanımlama ekranında Klasör Taşıma işlemi yapılacak  Klasör seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_209.png)

Klasör Tanımlama ekranında klasör seçili iken  ![ref60]  butonuna tıklanarak Klasör Taşıma ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_210.png)

Klasör Taşıma ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_211.png) butonu tıklanılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_212.png)

Açılan Doküman Klasörü listesinden seçili klasörün  hangi klasör altına taşanacağı klasör seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_213.png)  butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_214.png)

Klasör Taşıma ekranında seçili klasörün taşınacağı klasör seçim işleminden sonra ekranın sol üst köşesindeki ![ref57]  butonu tıklanarak Klasör taşıma kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_215.png)
##### **6.2.1.5.Link AL(Klasörleri Göster)  İşlemi**
Klasör Tanımlama ekranında seçili klasörün linkinin kopyalama işlemi yapılır. Klasör seçili iken ![ref61] butonu tıklanarak clipboard kopyalanan link Ctrl+V ( kısayol tuşları) veya sağ tıkla/yapıştır yöntemi  ilgili kullanıcılarla paylaşım işlemi yapılır. Linki sağ tıkla/yapıştır yöntemi tıklanarak açılan ekranda  doküman görme ekranı görüntülenir.  Doküman Görme ekranında linki alınan klasörün  klasör ağaç yapısında görüntülenecek şekilde alt klasör ve dokümanları ile listelenir.

Klasör Tanımlama ekranında Klasör link Alma işlemi yapılacak Klasör seçilir. Klasör seçili iken ![ref61] butonu tıklanılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_217.png)

Sistem tarafından “Bimser link clipboard'a kopyalanmıştır. İstediğiniz yerden link vermek için 'Ctrl+V' tuşlarını kullanabilir veya sağ tıklayarak 'yapıştır' diyebilirsiniz” mesajı verilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_218.png)

Sağa Yeni sekme açılarak sağ tıkla/ yapıştır  yöntemi ile seçilen klasörün linki tıklanılır. Açılan doküman Görme ekranında klasör ağaç yapısında seçilen klasör ve klasörlerin alt klasörler , dokümanlar listelenir. Kulllanıcılar bu şekilde klasörlerin linklerin  paylaşımı yapabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_219.png)
##### **6.2.1.6.Link AL(Klasörleri Gizle) İşlemi**
Klasör Tanımlama ekranında seçili klasörün linkinin kopyalama işlemi yapılır. Klasör seçili iken ![ref62] butonu tıklanarak clipboard kopyalanan link Ctrl+V ( kısayol tuşları) veya sağ tıkla/yapıştır yöntemi  ilgili kullanıcılarla paylaşım işlemi yapılır. Linki sağ tıkla/yapıştır yöntemi tıklanarak açılan ekranda  doküman görme ekranı görüntülenir.  Doküman Görme ekranında klasör ağaç yapısı gizlenecek şekilde  linki alınan klasörün  varsa alt klasör  ve dokümanların  listelenmesi sağlanır.

Klasör Tanımlama ekranında Klasör link Alma işlemi yapılacak Klasör seçilir. Klasör seçili iken ![ref62] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_221.png)

Sistem tarafından “Bimser link clipboard'a kopyalanmıştır. İstediğiniz yerden link vermek için 'Ctrl+V' tuşlarını kullanabilir veya sağ tıklayarak 'yapıştır' diyebilirsiniz” mesajı verilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_222.png)

Sağa  Yeni sekme açılarak sağ tıkla/ yapıştır  yöntemi ile seçilen klasörün linki tıklanılır. Açılan doküman Görme ekranında klasör ağaç yapısı gizlenerek seçilen klasör ve klasörlerin alt klasörler , dokümanları listelenir. Kulllanıcılar bu şekilde klasörlerin linklerin  paylaşımı yapabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_223.png)
##### **6.2.1.7.Klasör Silme İşlem** 
Klasör Tanımlama ekranında seçili klasörü silme işlemi yapılır.Klasör seçili iken ![ref63] butonu tıklanarak klasörün silme işlemi yapılır.

Klasör Tanımlama ekranında Klasör silme işlemi yapılacak Klasör seçilir. Klasör seçili iken ![ref63]  butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_225.png)

Sistem tarafından “Silmek istediğiniz klasörün altında klasör(ler) bulunmaktadır. Silmek istediğinize emin misiniz?” mejasında “Tamam” butonu tıklanarak klasör silinme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_226.png)
##### **6.2.1.8.Parametrik Alan Tanımlama**
Klasör bazında tanımlanması istenilen özel alanlar varsa parametrik alan tanımlama özelliği kullanılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_227.png)

Örneğin seçili olan “prosedürler” klasöründeki dokümanlar için, “Standarda Uygunluk (Uygun/ Uygun Değil)” olarak liste şeklinde klasöre özel bir alanın açılması isteniyorsa klasör bazlı parametrik alan tanımlanır.  Bu özelliğin aktif hale getirmek için Doküman Yönetimi Modülü parametrelerinde 109 numaralı “ Klasör Bazında Parametrik Alan Kullanılacak mı?” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_228.png)

Parametre aktif edildikten sonra Klasör Tanımlama ekranın ![ref64] butonu görüntülenerek klasör bazlı parametrik alan tanımlama işlemi yapılır.

Klasör Tanımlama ekranındaki ![ref64] butonuyla seçili klasör için parametrik alanlar tanımlanabilir. Klasör seçildikten sonra![ref64] butonuna tıklanır. Açılan ekranda klasör için oluşturulacak parametrik alan tipine göre (metin, tarih, liste, vb) seçilir ve ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_230.png) butonu ile alanın adı yazılır.   ![ref65]  butonu ile parametrik alan oluşturma işlemi tamamlanır.

Liste tipi parametrik alanın tanımlama işlemi;

Liste tipli parametrik alanın tanımlanması için parametrik alan tanımlama yapılacak klasör seçilir. Klasör seçili iken  ![ref64] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_232.png)

Açılan Parametrik Alan Düzenleme ekranında gridde Tip alanına “Liste” yazılarak liste tipi parametrik pasif alanların listelenmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_233.png)

Liste tipli parametrik alanlar listelendikten sonra tanımlama yapılacak” L\_ALAN1”  liste tipli alan seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_234.png) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_235.png)

Açılan Parametrik Alanları Düzenleme ekranında liste tipli alanın Başlık bilgisi , Başlık Notu , alanın zorunlu olup, olmayacağı gibi alanlar ilgili bilgiler  girilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_236.png)

Parametrik Alan Düzenleme ekranında gerekli alanlar ilgili bilgiler girildikten sonra ekranın sol üst köşesindeki ![ref65] butonu tıklanarak liste tipli parametrik alanın tanımlama işlemi yapılır. Liste tipli parametrik alanın tanımlama işleminde sonra parametrik alanın liste elemanlarının tanımlama işlemi yapılmalıdır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_237.png)

Liste elemanın tanımlama işlemi için liste tipli parametrik alan seçili iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_238.png) buton tıklanarak Değerler ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_239.png)

**Ekranda bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_240.png):Yeni bir değer tanımlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_241.png):Listede seçili değer bilgisi üzerinde güncelleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_242.png):Listede seçili değer bilgisi silinir

Değerler ekranında ![ref66]  butonu  tıklanarak yeni bir değer tanımlama işlemi yapılarak liste tipli parametrik alanın 1. Liste elemanın tanımlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_244.png)

Açılan Değerler ekranında Tanım alanında  1.liste elemanın tanım bilgisi yazılarak gerekli alanlar ilgili bilgiler girildikten sonra ekranın sol üst köşesindeki ![ref65]  butonu tıklanarak değer tanımlama kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_245.png)

Değerler ekranında ![ref66]  butonu  tıklanarak yeni bir değer tanımlama işlemi yapılarak liste tipli parametrik alanın 2. Liste elemanın tanımlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_246.png)

Açılan Değerler ekranında Tanım alanında  2.liste elemanın tanım bilgisi yazılarak gerekli alanlar ilgili bilgiler girildikten sonra ekranın sol üst köşesindeki ![ref65]  butonu tıklanarak değer tanımlama kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_247.png)

Liste tipli parametrik alanın tanımlama işleminde sonra  Entegre Yönetim Sistemi/Doküman İşlemleri/Doküman Hazırlama ekranı tıklanılır. Açılan Doküman Hazırlama-Klasör Seç ekranında parametrik alan tanımlamai işlemi yapılan klasör seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_248.png)  butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_249.png)

Açılan Yeni Doküman ekranında Parametrik Alanlar sekmesinde tanımlanan liste tipi parametrik alan görüntülenir. Parametrik alanda açılır liste tıklanarak açılan liste liste elemanları görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_250.png)

Liste tipli alanın zorunlu alan olduğu ve üzerindem mouse gelindiğinde başlık notunun görüntülendiği görülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_251.png)
#### **6.2.2. Doküman Hazırlama Şablonu** 
Firmanın yönetim sistemleri kapsamında doküman hazırlamak için kullandığı doküman hazırlama şablonları QDMS’te kullanılabilir. Doküman Hazırlama şablonunda alt bilgi/ üst bilgi kısmında bulunan “doküman kodu, doküman adı, hazırlanma tarihi, revizyon no, revizyon tarihi, ilk yayın tarihi, hazırlayan, kontrol eden, onaylayan” gibi bilgilerin QDMS’te doküman hazırlanırken girilen bilgilerden şablona otomatik olarak gelmesi sağlanabilir. Bunun için firma doküman hazırlama şablonununa QDMS Doküman Kısa Kodları ile işaretlenmesi gerekir.

Doküman Yönetimi Modülünde Doküman hazırlama şablonu oluşturmada kullanılan kısa kodlar aşağıdaki tabloda yer almaktadır. Kısaca Doküman kısaltma tablosu adı da denilebilir. Doküman hazırlama şablonu hazırlanırken bu kısa kodlar kullanılır. Örneğin; Doküman Kodu alanın bilgi girişinde **<DOC\_KODU\>** doküman kısaltması kullanılacaktır. Dokümanın adı alanın bilgi girişinde **<DOC\_ADI\>** doküman kısaltması kullanılacaktır. Şablonun içerisinde hangi alanın bilgi girişi kullanılacaksa ilgili doküman kısaltmaları yerleştirilerek alt bilgi ve üst bilgi kısmı oluşturuluyor. Firmanın Doküman hazırlama şablonu sistemde oluşturularak firma yeni bir doküman hazırlarken bu şablonun kullanılmasını sağlayarak standart bir yapıda bir doküman hazırlamasını işlemini gerçekleştirir.  



|**Doküman Yönetimi Modülü Doküman Hazırlama Şablonunda kullanılanan Kısa Kodlarının Listesi**||
| - | :- |
|**Kısaltma**|<p\>**Açıklaması**</p\><p\></p\>|
|<DOC\_KODU\>|DokümanKodu|
|<DOC\_TIPI\>|DokumanTipi|
|<REV\_NO\>  |Revizyon No|
|<DOC\_ADI\>|Doküman Adı|
|<DOC\_GRUP\_KODU\>|DokümanGrupKodu|
|<DOC\_GRUP\_ADI\>|Doküman GrupAdı|
|<DOC\_HAZ\_TAR\>|Hazırlanma Tarihi|
|<HAZ\_SICIL\>|Hazırlayan Sicil|
|<HAZ\_POZ\>|HazırlayanPozisyonKodu|
|<HAZ\_POZ\_TAN\>|HazırlayanPosizyonTanımı|
|<HAZIRLAYAN\>|HazırlayanınAdıSoyadı|
|<KONT\_SICIL\>|KontrolEden SicilNo|
|<KONT\_POZ\>|KontrolEden PozisyonKodu|
|<KONT\_POZ\_TAN\>|KontrolEdenPozisyonTanımı|
|<KONTROL\_EDEN\>|KontrolEdeninAdıSoyadı|
|<SORUMLU\_SICIL\>|Sorumlu SicilNo|
|<SORUMLU\_POZ\>|SorumluPozisyonKodu|
|<SORUMLU\_POZ\_TAN\>|SorumluPozisyonTanımı|
|<SORUMLU\>|SorumlununAdıSoyadı|
|<SOR\_KISIM\_KODU\>|SorumluDepartmanKodu|
|<SORUMLU\_KISIM\>|SorumluDepartman|
|<REV\_SICIL\>|RevizeEdenSicilNo|
|<REV\_POZ\>|RevizeEdenPozisyonKodu|
|<REV\_POZ\_TAN\>|RevizeEdenePozisyonTanımı|
|<REVIZE\_EDEN\>|RevizeEdenAdıSoyadı|
|<REV\_TARIHI\>|RevizyonTarihi|
|<REV\_NEDEN\>|RevizyonNedeni|
|<ONAY\_TAR\>|Onay Tarihi|
|<SON\_ONAY\_SICIL\>|Son Onaycı Sicili|
|<SON\_ONAY\_POZ\>|Son Onaycı Pozisyon Kodu|
|<SON\_ONAY\_POZ\_TAN\>|Son Onaycı Pozisyon Tanımı|
|<SON\_ONAY\>|Son Onaycı adı soyadı|
|<TUM\_ONAY\_SICIL\>|Tüm Onaycıların sicili|
|<TUM\_ONAY\_POZ\>|Tüm Onaycıların Pozisyonu|
|<TUM\_ONAY\_POZ\_TAN\>|Tüm onaycıların pozisyon tanımları|
|<TUM\_ONAY\_ADI\>|Tüm Onaycıları adı soyadı|
|<YAYIMLAYAN\_SICIL\>|Yayımlayan sicili|
|<YAYIMLAYAN\_POZ\>|Yayımlayan pozisyon kodu|
|<YAYIMLAYAN\_POZ\_TAN\>|Yayımlayan pozisyon tanımı|
|<YAYIMLAYAN\>|Yayımlayan adı soyadı|
|<YONETIM\_SISTEMLERI\>|YönetimSistemleri|
|<REFERANS\_DOKUMANLAR\>|ReferansDokümanlar|
|<GRUP\_EGITICI\>|Eğitmen|
|<X\_ONAY\_ADI\>|X. Onaylayanın Adı (X=1,2,3...)|
|<X\_ONAY\_SCL\>|X. Onaylayanın Sicili(X=1,2,3...)|
|<X\_ONAY\_POZ\>|X. Onaylayanın Pozisyon Kodu(X=1,2,3...)|
|<X\_ONAY\_POZ\_TAN\>|X. Onaylayanın Pozisyon Tanımı(X=1,2,3...)|
|<PRN\_KK\>|Kontrollü Kopya Parametresi(QDMS-GEN-29,30 nolu parametreler)|
|<P\_SICIL\>|Print Alan Sicil|
|<P\_ADI\>|Print Alan Personel Adı|
|<P\_TARIH\>|Print Alınan Tarih(gg.aa.yyyy)|
|<P\_UTARIH\>|Print Alınan Tarih (gg.aa.yyyy ss:dd:nn)|
|<DOC\_TIPI\>|Doküman Tipi|
|<KONTROL\_DEPARTMAN\_ADI\>|Kontrol eden kişinin Departmanı|
|<ONAYLAYAN\_DEPARTMAN\_ADI\>|Son Onaycının Departmanı|
|<REVIZYON\>|Revizyon|
|<KONTROL\_TAR\>|Kontrol tarihi|
|<REV\_EDEN\_DEPARTMAN\>|Revize Edenin Departmanı|
|<SURECLER\>|Dokumanın bağlı olduğu süreçler|
|<p\><X\_ID\>,<X\_DATE\>,<X\_APPROVAL\>,</p\><p\><X\_REASON\>,<X\_REVISION\> </p\>|Revizyon Tarihçesi X=1,2,3..|
|<ON\_KONT\_EDEN\>|Ön Kontrol eden ad soyad|
|<ON\_KONT\_POZ\_TAN\>|Ön kontrol eden pozisyon tanımı|

Firmaya ait bir Doküman hazırlama şablonu olmadığında durumda firmanın Prosedürleri ya da Talimatlar dokümanları alınıp içeriğindeki bilgiler boşaltılıp alt ve üst başlık kısımların şablon hazırlamadaki işlemler uygulanarak bir Doküman hazırlama şablonu yapısı standart bir şekilde hazırlanılabilir. Doküman hazırlama şablonun doküman hazırlarken kullanılmaktaki amaç hazırladığımız dokümanın standart bir yapıda oluşmasının sağlamaktır. Örnekte bir Doküman hazırlama şablonu yer almaktadır. Bu Doküman hazırlama şablonunda Doküman kısaltma tablosundaki kısaltmalar kullanılmıştır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_252.png)

Doküman Hazırlama Şablonu  onaysız/kontrolsuz bir şekilde sisteme aktarılma işlemi için Sistem Altyapı Tanımları/Doküman İşlemleri/Doküman Sisteme Aktarım menüsü tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_253.png)

Açılan Doküman Sisteme Aktarım -Klasör Seçme ekranında  Doküman Hazırlama Şablonun yükleme işleme işlemi yapılacak Klasör seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_254.png)  butonu tıklanılır. Açılan Doküman Sisteme Aktarım ekranında Doküman Bilgileri sekmesinde gerekli alanlar ilgili bilgiler yazılır. Doküman adı, dokümanın Hazırlama tarihi gibi detay bilgiler girilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_255.png)

Diğer Bilgiler sekmesi tıklanılır. Diğer bilgiler sekmesinde sisteme yükleceğimiz dokümanın türü Doküman ve Form seçeneklerinde ilgili check box işaretlenilerek belirlenir. Sisteme yükleceğimiz Doküman hazırlama şablonu olduğu için doküman Türü Form seçilir. Form kullanım seçeneklerinden Doküman hazırlama şablonu bir şablon olduğu için Doküman şablonu ile ilgili check box işaretlenir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_256.png)

Doküman hazırlama şablonun bir doküman şablon olduğu belirtildikten sonra Doküman sekmesi tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_257.png)

Doküman Sisteme Aktarım Doküman Sekmesinde ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_258.png)(Dosya Ekle) butonu tıklanarak Doküman Hazırlama Şablonun sisteme yükleme işlemi  yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_259.png)

Yüklenecek Doküman Hazırlama Şablonu seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_260.png)

Doküman Sisteme Aktarım Doküman sekmesinde Doküman Hazırlama şablonun yükleme işleminden sonra sistem tarafından “Dosya Başarlı Aktarılmıştır” mesajı gelir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_261.png)

Doküman Sisteme Aktarım ekranında Doküman Bilgileri sekmesinde Doküman Hazırlama Şablonun yükleme işleminde sonra ekranın sol üst köşesindeki ![ref65]butonu tıklanarak Doküman Hazırlama Şablonun sisteme yükleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_262.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_263.png)

Doküman Hazırlama Şablonun sisteme aktarılma işleminde sonra Entegre Yönetim Sistemi/Doküman İşlemleri/Klasör Tanımlama ekranı tıklanılır. Klasör Tanımlama menüsünde Doküman hazırlama şablonu tanıtılması işlemi için yapılacak Klasör seçilir ve ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_264.png)  butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_265.png)


Açılan Klasör Tanımlama-Kayıt Güncelleme ekranda  Klasör Ayarları sekmesi tıklanılır. Doküman Hazırlama Şablonu klasörde tanımlama işlemi için ilk olarak Klasör Ayarları sekmesinde  Doküman hazırlama şablonu alanı kısmına gelinir.  Doküman hazırlama şablonu alanında daha önceden Qdms’ e şablon olarak yüklenmiş olan doküman hazırlama şablonlarından hangisi veya hangilerinin, bu klasöre bağlı olarak doküman hazırlarken kullanılabileceğini belirtmek için kullanıldığı alandır. Klasöre bağlı hazırlanacak dokümanlarda “bu şablonu kullan” demek için bu özellik kullanılmaktadır. Doküman Hazırlama Şablonu alanında  ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_266.png)  butonu tıklanılır

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_267.png)

Açılan  Doküman Listesinde klasörde kullanılanacak Doküman Hazırlama Şablonu ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_268.png) butonu tıklanarak seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_269.png)

Klasör Ayarları  sekmesine gelip Doküman Hazırlama Şablonu alanında ilgili Doküman hazırlama şablonu ekleme  işlemi   ile  ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_270.png)  butonu tıklanarak Doküman hazırlama şablonu Klasörle ilişkilendirilme işlemi yapılmıştır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_271.png)

Doküman Hazırlama şablonu  ilgili klasörde ilişkilendirilme işleminde sonra ilgili klasörde  Şablon kullanılarak Doküman Hazırlama işlemi yapılır. Entegre Yönetim Sistemi/Doküman İşlemleri/Doküman Hazırlama menüsü tıklanılır. Açılan  Doküman Hazırlama - Klasör Seçme Doküman Hazırlama Şablonu ile ilişkilendirme işlemi yapılan Klasör seçilir ve ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_272.png) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_273.png)

Açılan Yeni Doküman ekranında Doküman Bilgileri  sekmesinde hazırlanan doküman detay bilgileri yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_274.png)

Yeni Doküman ekranda Doküman Bilgileri sekmesinde gerekli bilgiler ilgili bilgiler girildikten sonra Doküman sekmesi tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_275.png)

Yeni Doküman ekranında Doküman sekmesinde Dokuman Dosyası Yükleme (Türkçe) alanında ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_276.png)(Dosya Ekle) butonu tıklanarak sisteme dokümanın yükleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_277.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_278.png)

Dosya Ekle ekranında Gözat tıklanarak sisteme yüklenecek dosya seçim işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_279.png)

Sistem tarafında dosyanın yüklendiğine dair “ Dosya başarıyla aktarılmıştır” mesajı verilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_280.png)

Doküman bilgileri sekmesi tıklanarak ilgili alanlar bilgiler girildikten sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_281.png)  butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_282.png)

Sistem tarafından verilen “Göndermek istediğinize emin misiniz?” mesajında “Tamam” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_283.png)

Doküman Ön kontrol aşamasındaki ön kontrolcünün onaya gönderilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_284.png)

Doküman Dosyası Ön Kontrolcünün  Bekleyen işlerinde “ Ön kontrolde Bekleyen Dokümanlar” görevi olarak iş düşer. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_285.png)

İlgili görevdeki Doküman Kodu alanında doküman kodu link tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_286.png)

Doküman Ön kontrol ekranında Doküman sekmesi tıklanılır. Bu aşamada Doküman Hazırlama Şablonu ve Doküman bilgisayara indirilerek doküman bilgileri şablona eklenerek düzenleme işlemi yapılarak tekrar sisteme yükleme işlemi yapılır. Bu işlemin yapılması için öncelikle Doküman Hazılrma Şablonu  bilgisayara indiirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_287.png)

Doküman Hazırlama Şablonu ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_288.png)(Türkçe) butonu tıklanarak bilgisayara indirilir. Daha sonra Dokuman Dosyası Yükleme (Türkçe) alanında ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_289.png)(Dosya Görüntüle) butonu tıklanarak doküman bilgisayara indirilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_290.png)

İndirilenen şablonda doküman bilgileri eklenerek , düzenleme işlemi yapılarak doküman dosyası aynı isimde sistem yüklenmelidir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_291.png)

Dokuman Dosyası Yükleme (Türkçe) alanında ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_292.png)(Dosya Ekle) butonu tıklanarak Doküman Hazırlama Şablonu ile düzenlenmiş doküman dosyasını yükleme işlemi yapılır. ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_293.png)

Dosya Ekle ekranında Gözat butonu tıklanarak Doküman Hazırlama Şablonu ile Düzenlenmiş Doküman Dosyasının seçim işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_294.png)

Sistem tarafından “Dosya başarıyla aktarılmıştır” mesajı verilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_295.png)

Doküman Hazırlama Şablonu kullanılarak düzenlenmiş dokümanın sisteme aktarılma işleminde ön kontrolcü dokümanı içerik ve yapı olarak inceledik sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_296.png) butonu tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_297.png)

Sistem tarafından “Göndermek istediğinize emin misiniz?” mesajında “Tamam” butonu tıklanarak kontroldeki kontrolcüye kontrol işlemi için doküman dosyası gönderilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_298.png)

Doküman Dosyası  Kontrolcünün  Bekleyen işlerinde “Kontrolde Bekleyen Dokümanlar” görevi olarak iş düşer. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_299.png)

İlgili görevdeki Doküman Kodu alanındaki doküman kodu linki tıklanılır. Kontrolcü doküman ve sekmelerde bilgileri kontrol ettikten dokümanı ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_300.png) butonu tıklanarak onaydaki kişinin onayına sunar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_301.png)

Sistem tarafında “Göndermek istediğinize emin misiniz?” mesajına “Tamam” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_302.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_303.png)

Onay gönderilen Doküman  Onaycının  Bekleyen işlerinde “ Onay Bekleyen Dokümanlar”  görevi olarak iş düşer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_304.png)

İlgili görevdeki Doküman kodu alanındaki Doküman kodu link tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_305.png)

Onay aşamasındaki onaycı doküman  üzerinde değişiklik ve düzenleme işlemi yapmamaz . Dokümanı sadece onaylama ve uygun görmezse ret nedeni yazarak ret işlemi yaparak hazırlayıcı ger gönderir. Doküman Hazırlama Şablonu ile düzenlenmiş dokümanı onaylama işlemi için ekranın sol üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_306.png)  butonu tıklanarak Dokümanı onaylama işlemi yapılarak dağıtım matrisindeki atama görevi yapılan kullanıcı ve kullanıcı gruplarına okuma görevi düşmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_307.png)

Sistem tarafında “Göndermek istediğinize emin misiniz?” mesajına “Tamam” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_308.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_309.png)

Doküman yayınlanıp kullanıma açıldıktan sonra Dağıtım matrisindeki kullanıcılara  Bekleyen işlerinde “Okunması Gereken Doküman Listesi” işi olarak görev düşer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_310.png)

İlgli görevdeki Doküman Kodu alanındaki doküman linki tıklanılır. Açılan Doküman Görme ekranında Doküman Hazırlama Şablonu ile Düzenleme yapılmış dokümanda Doküman Kısa kod’ları (Tag’lerin) çalıştığı görülür. 

**Üst Bilgi bilgileri;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_311.png)

**Alt Bilgi bilgileri;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_312.png)

#### **6.2.3.Doküman Aktarım**
QDMS sisteminde Doküman Yönetimde doküman aktarma işleminin 3 yöntemi vardır.

**Doküman Hazırlama:** Dokümanı kontrollü-onaylı bir şekilde sisteme aktarma işlemi yapılır. Entegre Yönetim Sistemi/ Doküman İşlemleri/ Doküman Hazırlama menülerinde işlem adımları yapılarak onaylı bir şekilde doküman sisteme aktarılma işlemi yapılır.

**Doküman Sisteme Aktarım**: Dokümanı kontrol veya onaya gerek duymadan sisteme aktarmak için kullanılan bir yoldur. Doküman hazırlama şablonları gibi daha önceden onaylanan dokümanları tek tek sisteme aktarmak  için kullanılır. Sistem altyapı Tanımları/ Doküman İşlemleri/ Doküman Sisteme Aktarım menüleri takip edilerek aktarım işlemi gerçekleştirilir. 

**Toplu Aktarım** : QDMS’ e ilk geçiş aşamasında firmanın dokümanlarını toplu olarak sisteme aktarmak için kullanılan bir yöntemdir. Firma için tüm klasör ağaç yapısı QDMS’ te oluşturulduktan sonra, toplu aktarım işlemi gerçekleştirilir. Toplu aktarım için, firmanın dokümanlarında kullanılan doküman şablonlarını, sistemde kullanılacak şekilde işaretleyerek sisteme yükleme yapmak tavsiye edilen bir yöntemdir. Bunun için, Bimser teknik personelinden/danışmanından “DocumentBodyReplacement” programı temin edilerek değiştirme işlemi gerçekleştirilebilir. Toplu Doküman Aktarım Programı kullanılarak dokümanlar topluca sisteme aktarılır. Bunun için danışman/destek tarafından paylaşılan bir programa ihtiyaç vardır. (QDMS.CDSA).

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_313.png)

Bu verilen dosyanın içindeki programı çalıştırmadan önce firma tarafından yapılması gereken ön hazırlıklar vardır. Bunlar;

- Klasör ağacında tüm klasör yapısının çıkarılması gerekir. 
- Klasör yapısına bağlı olarak Hazırlayanların, Onaylayanların ve Yetki-Dağıtım matrislerinin belirli olması gerekir.
- Doküman şablonlarının kısa kodlar ile işaretlenmesi tavsiye edilir. (DocumentBodyReplacement)

İlk iki madde tam olduktan sonra Toplu aktarım adımlarına geçilebilir.

**Toplu Döküman Aktarım Adımları;**

- Toplu Aktarım dosyası içinde verilen Master List açılıp (DokSablonv5), uygun bir şekilde doldurulur. Doküman Kodu, Doküman Adı, Revizyon numarası, Hazırlanış Tarihi yazılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_314.png)

- Hazırlayan kişinin QDMS’ te tanımlı olan sicil numarası yazılır. Sorumlu Kişi; dokümanı hazırlayan, departman sorumlusu, süreç sorumlusu gibi doküman sahibinin kim olduğunu belirtilir. Sorumlu kişi kısmına dokümanın sorumlusu kimse onun QDMS’ te tanımlı olan sicil numarası yazılır. (Hazırlayan kişinin sicil numarası bilgisi Sistem Altyapı Tanımları/BSAT/Tanımlar/Personel Tanımlama menüsünde alınır.)

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_315.png)

- Sorumlu Kısım alanına dokümanın ait olduğu departmanın kodu yazılır, hazırlayan kişinin departman kodu neyse o kod tanımlanır.  (Departman Kodu bilgisi Sistem Altyapı Tanımları/BSAT/Tanımlar/Departman Tanımlama menüsünde alınır.)

Resmin boyutu küçük, boyutu arttırılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_316.png)

- Kontrol eden kısmına doküman kontrolcüsünün sicil numarası yazılır, eğer kontrolcü yok ise boş bırakılır.(Kontrol eden kişinin sicil numarası bilgisi Sistem Altyapı Tanımları/BSAT/ Tanımlar/Personel Tanımlama menüsünde alınır.)

  ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_317.png)

- Revizyon tarihi ve Revizyonu yapan kısımlarına revizyon numarası ve revizyonu yapan kişinin sicil numarası yazılır. Eğer doküman yeni bir doküman ise bu alanlara doküman hazırlanma tarihi ve dokümanı hazırlayan kişinin sicil numarası bilgisi tanımlanır. Revizyon nedeni kısmına; son revizyon gerçekleşme bilgisi tanımlanabilir ya da QDMS doküman aktarımından dolayı “QDMS’ e geçiş” yazılabilir.

  ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_318.png)

- Doküman/Form sütununa eğer doküman form ise F, diğerleri ise D seçeneği tanımlanır.

  ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_319.png)

- Doküman Tipi alanında ise daha önceden Sistem Altyapı Tanımları/ Doküman İşlemleri/ Doküman Tipi menüsünde tanımlanan doküman tiplerine karşılık gelen kodlar tanıtılmalıdır. ( Örneğin; Prosedür: PR)

Resmin boyutu küçük, resmin boyutu arttırılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_320.png)

- Grup Kodu alanına; eğer aktarılacak dokümanlar farklı klasörlere aitse, dokümanın aktarılacağı klasörün kodu tanımlanır. (Klasör Kodu bilgisi  Entegre Yönetim Sistemi/Doküman İşlemleri/Klasör Tanımlama menüsünde alınır)
- Bütün bilgiler tanımlandıktan sora Aktarım Şablonu kaydedilir. 
- Aktarılacak dokümanlar bir klasör içerisinde toplanır. Bu sırada dikkat edilmesi gereken bir husus vardır; Doküman kodlarını Master List’e yazdıktan sonra, bu kodların dokümanlara isim olarak verilmesi gerekmektedir. Yani; doküman kodu ile aktarım klasöründeki doküman isimleri aynı olmalıdır.


![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_321.png)

- Doküman Aktarım Listesi (Master List) oluşturulan aktarım klasörüne taşınmalıdır. Aktarılacak dokümanlar ile aktarım şablonu listesi aynı klasörde bulunmalıdır.

  ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_322.png)

- Toplu Doküman Aktarım Program klasörünün içindeki Config dosyası düzenle diyerek açılır. Config dosyasının içindeki adrese firma QDMS adresinin QDMSNET’ e kadar olan kısmı kopyalanarak yapıştırılır. Bu programı firma QDMS’ ini tanınması için yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_323.png)

- Firma adresi tanıtıldıktan sonra QDMS.Client programı çalıştırılır. 

  ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_324.png)

QDMS.Client programı kullanıcı Adı ve parola bilgisi Sistem Altyapı Tanımları/BSAT/Konfügürasyon Ayarlar/Servis Giriş Bilgileri Tanımlama menüsünde tanımlanmamışsa tanımlanır. Tanımlanmış ise tanımlı Kullanıcı Adı ve parola bilgisi alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_325.png)

QDMS.Client programı kullanıcı Adı ve şifre bilgisi tanımlama işlemi için program seçili iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_326.png) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_327.png)

Servis Giriş Bilgileri Tanımlama ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_328.png)

Kullanıcı adı ve şifre bilgisi yazılarak ekranın sol üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_329.png) butonu tıklanarak servis giriş bilgileri tanımlama kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_330.png)

Açılan ekranda QDMS.Client programı kullanıcı adı ve parola bilgisi yazılarak ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_331.png) butonu tıklanarak program giriş yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_332.png)



![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_333.png)

- Program çalıştıktan sonra yapılması gereken ilk iş “Open Document List” butonu ile hazırlanan aktarım şablonu listesini açmaktır. 

  ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_334.png)

`           `Aktarım Şablonu Listesi açıldıktan sonra firma aktarım dokümanları ekranda listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_335.png)

- Bu dokümanların hangi klasör içine atılması isteniyorsa “Folder Info” kulakçığında seçilir. Eğer dokümanlar birden çok klasöre atılacaksa, aktarım şablonunda grup kodları belirlenerek adresleme yapıldıysa en üst seviyedeki klasörü seçmek yeterli olacaktır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_336.png)

- Yetki/ Dağıtım/ Onay matrisleri sekmeleri de tıklanarak, bu alanların doğru şekilde tanımlı olup olmadığı kontrol edilir.

  ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_337.png)

- Son adım olarak da aşağı kısımda bulunan “Transfer Document” butonuna tıklanarak toplu doküman aktarımın işlemi gerçekleştirilir.

  ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_338.png)


![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_339.png)

- Herhangi bir dokümanın aktarılamaması durumunda Transfer Log kulakçığında hata mesajı alınmaktadır. 
#### **6.2.4.Doküman Hazırlama Süreci**
**Menü Adı**: Entegre Yönetim Sistemi/ Doküman İşlemleri/ Doküman Hazırlama

Yönetim sistemleri kapsamında yeni bir doküman hazırlamak için “Doküman Hazırlama” menüsü kullanılır. Personelin klasör üzerinde doküman hazırlayabilmesi için, klasör yetki matrisi sekmesinde kullanıcı grubu ya da pozisyon olarak tanımlı olması ve doküman hazırlama yetkisinin de atanmış olması gerekir. Personel, yetkisi olmayan klasörde doküman hazırlayamaz, “Bu klasöre doküman hazırlama yetkiniz yoktur” uyarısı sistem tarafından alır. Bu yüzden klasör yetki matrisinin doğru bir şekilde oluşturulması önemlidir. Doküman hazırlama yetkisi olan  Klasörde doküman hazırlama süreci  görüş , ön kontrol(ilgili parametrelerde gerekli ayarlamalar yapıldıysa), kontrol, onay son olarak dağıtım matrisinde tanımlı kişilere okuma görevi olarak gider. Dokümanda görüş zorunlu değildir. Görüşe giden döküman görüşcünün görüşleri alınarak hazırlayan kişiye “Görüşten Dönen Dokümanlar” olarak döner.Ön kontrolde ön kontrolcü dokümanın içerik ve yapısı incelenir. Dokümanı onaylama veya ret etme işlemleri yapar. Ret etme işleminde dokümanın ret nedeni yazılarak doküman hazırlayan kişiye gönderilir. Kontrol aşamasında ise kontrolcü  dokümanın tüm bilgileri üzerinde ve dokümanın tüm sekmeleri üzerinde değişiklik yapılır. Kontrol aşamasında sonra onaydaki kişi dokümanı onaylama ve ret etme işlemleri yapar. Ret etme işleminde ret nedeni yazılarak  doküman  hazırlayana geri gider. Doküman onaylama işleminde sonra yayınlanıp dağıtım matrisindeki kişilere okuma görevi olarak düşer.Ön Kontrol Aşamasında doküman “Ön Kontrolde bekleyen dokümanlar”, Kontrol aşamasında “Kontrolde Bekleyen Dokümanlar” ve onay aşaamasında “Onay Bekleyen Dokümanlar ” görevleri ilgili kişilerin bekleyen işlerine düşer. Dağıtımda ise önemli doküman olup, olmamasına göre görev taskı değişmektedir. Önemli doküman ise “Okunması Gereken Önemli Dokümanlar Listesi ” olarak dağıtım matrisindeki kişilere görev düşer. Diğer durumda “Okunması Gereken Dokümanlar listesi” olarak bekleyen işlerime görev düşer.

Yeni bir doküman hazırlamak için  Entegre Yönetim Sistemi/Doküman İşlemleri/Doküman Hazırlama menüsü tıklanılır. Klasör ağaç yapısından doküman hazırlanmak istenilen klasör seçilir ve ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_340.png)  butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_341.png)

**Doküman Bilgileri sekmesi;**

Dokümana ait temel bilgileri tanımlandığı sekmedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_342.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Grup Kodu:** Yeni Doküman ekranında doküman Doküman Bilgileri sekmesinde hazırlanacak klasörün kod bilgisinin sistem tarafından verildiği alandır.

**Klasör Kodu:** Yeni Doküman ekranında Doküman Bilgileri sekmesinde doküman hazırlanacak klasörün adı bilgisinin yazıldığı alandır.

**Doküman Kodu:** Yeni Doküman ekranında Doküman Bilgileri sekmesinde hazırlanan dokümanın kod bilgisinin sistem tarafından verildiği alandır. Kod bilgisi Doküman hazırlanan Klasörde tanımlı kod şablonu ve sayac değerine göre otomatik olarak gelmektedir. Kod şablonu bilgisi:2024-[TIP].#### ve sayac değeri “2” göre tanımlandığında 2024-PR.003 olarak gelmektedir. TIP kısmında doküman tipinin varsa kısa kod bilgi yoksa kod bilgisi gelir.

**Doküman Adı:** Yeni Doküman ekranında Doküman bilgileri sekmesinde klasör içerisinde hazırlanan dokümanın adı bilgisinin yazıldığı alandır.

**Revizyon  Numarası:** Yeni Doküman ekranında Doküman bilgileri sekmesinde klasör  içerisinde yeni hazırlanan dokümanın revizyon bilgisinin verildiği alandır. Yeni hazırlanan dokümanlar için revizyon Numarası “0” olarak  tanımlanılır. Klasörde Tanımlama -Yeni Kayıt ekranında Klasör Ayarları ekranında Revizyon Numarası değişim alanında manuel ve otomatik olarak iki seçeneğe bağlı olarak bu alanda revisyon numarasının verilmesi yapılır. Klasörde Tanımlama -Yeni Kayıt ekranında Klasör Ayarları ekranında Revizyon Numarası değişim alanında otomatik seçildiğinde sistem revizyon numarasını otomatik kod ataması yapacak şekilde atar. Klasörde Tanımlama -Yeni Kayıt ekranında Klasör Ayarları ekranında Revizyon Numarası değişim alanında manule seçimi olsaydı kullanıcı elle yazarak revizyon numarasını belirlerdir.

**Doküman Tipi:** Yeni Doküman ekranında Doküman Bilgileri sekmesinde klasör içerisinde hazırlanan dokümanın doküman tipi verildiği alandır. Doküman Tipi bilgisi dokümanın içerisinde bulunduğu klasörden tanımlı olarak gelmektedir.İstenirse doküman tipi alanında ![ref67] butonu tıklanarak sistemde tanımlı Doküman Tipleri listesinde seçim yapılarak değiştirilme işlemi yapılır. Prosedür:PR, Talimat:TA

**Doküman Sahibi:** Yeni Doküman ekranında Doküman Bilgileri sekmesinde doküman hazırlayan bilgisinin verildiği alandır. Doküman Sahibi Qdms giriş yapılan adresteki kişi olarak varsayılanan olarak sistem tarafından otomatik olarak gelmektedir. İstenirse Doküman Sahibi  ![ref67] butonu tıklanarak sistemde tanımlı Pozisyon listesinde seçim yapılarak başka bir pozisyondaki kişinin seçilme işlemi yapılır. Dokümanı hazırlayan, üst amir, süreç sahibi, departman amirinin pozisyonu olabilir

**İlgili Bölüm:** Yeni Doküman ekranında Doküman Bilgileri sekmesinde dokümanın ait olduğu departman bilgisinini verildiği alandır.

**Hazırlama Tarihi:** Yeni Doküman ekranında Doküman Bilgileri sekmesinde hazırlama tarihi bilgisinin açılan Takvim alanında seçildiği alandır. Sistem tarafından günün tarihi verilir. Doküman günün tarihinden eski bir tarihte hazırlanmaya başlandıysa sistemden seçilir. Doküman Yönetim Modülü parametreelerinde 55 numaralı “Hazırlanma Tarihi ile Revizyon Tarihi değiştirilebilsinmi?” parametresinin parametre değeri “Hayır” seçildiğinde parametre pasif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_344.png)

Parametre pasif edildikten sonra Hazırlama Tarihi alanı kilitlenir ve kullanıcı Takvim alanında seçim yapamayarak ilgili alan müdahele edemez. 

**Hazırlayan Kişi:** Yeni Doküman ekranında Doküman Bilgileri sekmesinde hazırlayan kişi bilgisinin verildiği alandır. Doküman Hazırlayan Kişi Qdms giriş yapılan adresteki kişi olarak varsayılanan olarak sistem tarafından otomatik olarak gelmektedir. İstenirse ![ref67] butonu tıklanarak sistemde tanımlı Personel listesinde seçim yapılarak başka bir personelin seçilme işlemi yapılır. Doküman Yönetimi Modülü 394 “Doküman Hazırlama sayfasında Hazırlayan Kişi değiştirilebilsin mi?” parametresinin parametre değeri “Hayır” seçilirse parametre pasif edilir. Parametre pasif edildikten sonra Hazırlayan Kişi alanında sistem giren kişi  bilgisi gelir. Sistem bu alanda değişiklik yapılmasına izin vermez. Parametre aktif edildiğinde Hazırlayan kişinin başka bir kişi olarak seçilmesine sistem izin verir.

**Ön Kontrol Tipi:** Yeni Doküman  ekranında Doküman Bilgileri sekmesinde parametrelere bağlı olarak görüntülenen bir alandır. Eğer doküman hazırlandıktan sonra kontrole gitmeden önce ön kontrole gitmesi isteniyorsa Doküman Yönetimi parametrelerinden 76.numaralı “Dokumanda Ön Kontrol Kullanılsın mı?” parametresinin parametre değeri “Evet” olarak seçilerek parametre aktif edilmelidir.

![][ref38]

Ön Kontrol tipi olarak seçeneklerin görüntülenmeside ilgili parametrelerin aktif edilmesi ile sağlanmaktadır. 

**Ön Kontrol Tipi olarak grup seçilmesi için;**

Doküman Yönetimi Parametrelerinde 296 numaralı” Dokumanlarda Ön Kontrol Grubu kullanılacak mı?” parametresinin parametre değeri “Evet” seçilerek parametre “Aktif “ edilir.

![][ref39]

Parametre aktif edildikten sonra Ön Kontrol Tipi alanında Grup seçeneği görüntülenir. Yeni Doküman ekranında görüntülenen Ön Kontrol Grubu alanında ![ref40] butonu tıklanarak açılan sistemde tanımlı kullanıcı grubu listesinde ön kontrol yapacak kullanıcı grubu  seçilir.Seçilen kullanıcı grubunu  dokümanın yapı ve içerik kontrollünün yapılması sağlar.

![ref41]

**Ön Kontrol Tipi olarak Kullanıcı seçilmesi için;**

![ref42]

Ön Kontrol tipi olarak kullanıcı seçildiğinde görüntülenen Ön Kontrol Edecek alanında ![ref40] butonu tıklanarak açılan sistemde tanımlı Pozisyon listesinde ön kontrol yapacak pozisyon seçilir.Seçilen Pozisyondaki kişi dokümanın yapı ve içerik kontrollünün yapılması sağlar.Ön kontrol aşamasında hazırlanan doküman; hazırlayan kişinin departmanındaki ilgili kullanıcılara, hazırlayan kişinin amirine ya da doküman hakkında bilgisi olan bir kullanıcıya gönderilir. Kontrol aşamasında ise hazırlanan doküman yapı ve içerik kontrolü için genelde kalite sistem sorumlularına iletilir.	


**Ön Kontrol Tipi olarak Rol seçilmesi için;**

![ref43]

Ön Kontrol tipi olarak Rol seçildiğinde görüntülenen Ön Kontrol Rolü  alanında ![ref40] butonu tıklanarak açılan sistemde tanımlı Rol listesinde ön kontrol yapacak Rol seçilir.Seçilen Roldeki  kişi dokümanın yapı ve içerik kontrollünün yapılması sağlar.  Ön kontrol tipi alanında Rol seçeneği parametreye bağlı olarak görüntülenen bir alandır. Doküman Yönetimi parametrelerinde 298 numaralı “Dokuman ön kontrol aşamasında rol kullanılsın mı?(E/H)” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. 

![][ref44]

Parametre aktif edildikten sonra Ön Kontrol Tipi seçeneklerinde rol seçeneğide ilgili alanda görüntülenir.Ön Kontrol Tipi alanında tanımlanan klasör için Kullanıcı tipi olarak seçim işlemi yapılır.

**Ön Kontrol Edecek:** Yeni Doküman ekranından Doküman Bilgileri sekmesinde  ![ref40] butonu tıklanarak açılan sistemde tanımlı Pozisyon listesinde ön kontrole gidecek pozisyon seçim işlemi yapılır. Tanımlanan klasörde hazırlanan dokümanlarda Pozisyondaki kişi ön kontrol aşamada yapı ve içerik olarak dokümanın incelemesini yapacak kişidir.

**Kontrol Tipi:** Yeni Doküman  ekranında Doküman Bilgileri sekmesinde dokümanın kontrol tipinin seçeneklerin seçildiği alandır. 

**Kontrol Tipi olarak  Grup seçilmesi için;**

![ref45] Kontrol tipi olarak Grup seçildiğinde görüntülenen Kontrol Grubu  alanında ![ref40] butonu tıklanarak açılan sistemde tanımlı Kullanıcı Grubu listesinde onaydan önce dokümanın  kontrolünü yapacak  Kullanıcı grubu  seçilir.Seçilen Kullanıcı Grubu doküman üzerinde her türlü değişikliği yapma yetkisine sahiptir. Dokümanı yapı ve içerik olarak  kontrollü yaptığı gibi  doküman hazırlama aşamasındaki tüm sekmeler üzerinde değişiklik yapma yetkisine sahiptir. Grup kontrolünde gruptaki bir kişinin kontrolü yeterlidir. Bir kişi kontrol ettiğinde doküman onay statüsüne geçecektir. Parametreye bağlı  olarak görüntülenen alandır. Doküman Yönetimi parametrelerinde 80 numaralı “Dokumanlarda Kontrol Grubu kullanılacak mı?” parametresinin değeri “Evet” seçilerek parametre aktif edilir. 

![][ref46]

Parametre aktif edildikten sonra Kontrol Tipi alanında Grup seçeneği görüntülenir ve hazırlanan dokümanın  onayında önce bir gruba kontrole gönderilmesi için seçim işlemi   yapılır.

**Kontrol Tipi olarak Kullanıcı seçilmesi için;**

![ref47]

Kontrol tipi olarak Kullanıcı seçildiğinde görüntülenen Kullanıcı alanında ![ref40] butonu tıklanarak açılan sistemde tanımlı Pozisyon listesinde onaydan önce dokümanın  kontrolünü yapacak  Pozisyon seçilir.Seçilen Pozisyondaki kişi doküman üzerinde her türlü değişikliği yapma yetkisine sahiptir. Dokümanı yapı ve içerik olarak  kontrollü yaptığı gibi  doküman hazırlama aşamasındaki tüm sekmeler üzerinde değişiklik yapma yetkisine sahiptir.

**Kontrol Tipi olarak Rol seçilmesi için;**

![ref48]

Kontrol tipi olarak Rol seçildiğinde görüntülenen Kontrol Rolü alanında ![ref40] butonu tıklanarak açılan sistemde tanımlı Rol  listesinde onaydan önce dokümanın  kontrolünü yapacak  Rol seçilir.Seçilen Rol doküman üzerinde her türlü değişikliği yapma yetkisine sahiptir. Dokümanı yapı ve içerik olarak  kontrollü yaptığı gibi  doküman hazırlama aşamasındaki tüm sekmeler üzerinde değişiklik yapma yetkisine sahiptir. Parametreye bağlı  olarak görüntülenen alandır. Doküman Yönetimi parametrelerinde 180 numaralı “Doküman kontrol aşamasında rol kullanılsın mı?(E/H)” parametresinin değeri “Evet” seçilerek parametre aktif edilir.

![][ref49]

Parametre aktif edildikten sonra Kontrol Tipi alanında Rol seçeneği görüntülenir ve hazırlanan dokümanın  onayında önce bir role kontrole gönderilmesi için seçim işlemi   yapılır

**Kontrol Edecek:** Yeni Doküman ekranında Doküman Bilgileri sekmesinde hazırlanan  dokümanın kontrollü yapacak  pozisyonun  ![ref50] butonu tıklanarak açılanan sistemde tanımlı Pozisyon listesinden seçildiği alandır.

**Gözden Geçirecek:** Yeni Doküman ekranında Doküman Bilgileri sekmesinde hazırlanan dokümanın kimin tarafından gözden geçileceğininin belirlendiği alandır.

**Eğitim Sorumlusu:** Yeni Doküman ekranında  Doküman Bilgileri sekmesinde hazırlanan dokümanla ilgili bir eğitim verilecek ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_345.png) butonu tıklanarak açılan sistemde tanımlı Pozisyon Listesinden eğitim sorumlusunun seçildiği alandır.  Parametreye bağlı olarak bu alan üzerinde değişiklik yapma yetkisi verilmektedir. Doküman Yönetimi Modülü parametrelerinde 121 numaralı “Doküman işlemlerinde eğitim veren kişi değiştirilebilsin mi? (E/H)”  parametresi değeri “Evet” seçilerek parametre aktif edilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_346.png)

Parametre aktif edildiğinde yeni bir doküman hazırlanırken  eğitim veren kişi değiştirilmesi işlemi yapılır. Parametre pasif edildiğinde bu alan klasörde nasıl tanımlı geldiyse o şekilde tanımlı gelir ve müdahale edilemez. Genelde Makina kullanım Talimatları dokümanlar gibi dokümanlar için eğitim sorumlusu ataması işlemi yapılır. 

**Revizyon Bilgileri Sekmesi;**

Dokümanda revizyon işlemi yapıldığında, Revize Eden, Revizyon nedeni ve Revizyonda yapılanan gibi alanların yazıldığı sekmedir. Yeni bir  doküman hazırlandığında bu sekmedeki alanlar boş bırakılır.Bu sekmenin görüntülenmesi parametreye bağlı olarak görüntülenir.  Bu sekmenin yeni doküman hazırlanırken görüntülenmesi istenmiyorsa Doküman Yönetim parametrelerinde 83 numaralı “Dokuman İlk Hazırlamada Revizyon Bilgileri Kulakçığı saklansın mı?” parametresinin parametre değeri “Evet” seçilerek parametre aktiif edilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_347.png)

Parametre aktif edildikten Revizyon bilgileri sekmesi doküman hazırlama aşamasında görüntülenmez. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_348.png)

**Diğer Bilgiler Sekmesi:** Hazırlanan dokümanın türünün belirlendiği, baskı nedeni bilgisi, varsa referans dokümanlarla ve sistem madde no ile ilişkilendirilmenin yapıldığı , anket kullanıp, kullanılmayacağı ve gözden geçirme  tarihinin belirlendiği sekmedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_349.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Doküman Türü:** Yeni Doküman ekranında Diğer bilgiler sekmesinde  hazırlanan dokümanın türü seçildiği alandır. Eğer üzerinde işlem yapılan bir dokümansa “Form”, prosedür-talimat gibi dokümalar ise “Doküman” seçeneği işaretlenir. “Form” seçildiğinde “Kullanım Şekli” olarak “Kalite Kaydı, Hazır Form, Doküman Şablonu ve Matbu Form” seçeneklerinden uygun olan seçilir.  Eğer sistemde kalite kaydı olarak işlem yapılacaksa kalite kaydı seçeneği işaretlenir. “Matbu Form” olarak kullanılacaksa ilgili seçenek işaretlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_350.png)

**Baskı Nedeni:** Yeni doküman ekranında Diğer bilgiler sekmesinde   “Genel, Sistem, Ürün, Bulk” seçenekleri arasından seçim yapıldığı alandır.Eğer kontrollü/ kontrolsüz kopyaların takibinde baskı özelliği kullanılacaksa bu alanda işlem yapılır.

**Şifreli Doküman:** Yeni doküman ekranında Diğer bilgiler sekmesinde şifreli doküman özelliğinin kullanılması isteniyorsa ilgili check box’ın işaretlendiği alandır. Parametreye bağlı olarak görüntülenen bir alandır. Doküman Yönetimi parametrelerinde 324 numaralı “Şifreli doküman özelliği kullanılacak mı ?” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir.  Şifreli doküman özelliği doküman yönetimi modülünde kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_351.png)

**Referans Dokümanlar :** Yeni doküman ekranında Diğer bilgiler sekmesinde hazırlanan dokümanla ilişkilendirilecek dokümanlar varsa ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_352.png) butonu tıklanarak açılan doküman listesinden seçildiği alandır. Doküman Yönetimi parametrelerinden 99 numaralı “Referans Dokuman Bildirimi Revizyon Talebi olarak eklensin mi? “ parametresinin parametre parametre değeri “Evet” seçilerek parametre aktif edilir. Parametre aktif edildiğinde  sistem tarafından revizyon talebi başlatılır.

**Sistem - Madde No:** Yeni doküman ekranında Diğer bilgiler sekmesinde hazırlanan dokümanın ![ref68] butonu tıklanarak açılan sistemde tanımlı madde no listesinde madde no seçilerek ilişkilendirilmesinin yapıldığı alandır.

Yeni Doküman ekranında Diğer Bilgiler sekmesinde Sistem -Madde No alanında ![ref68] butonu tıklanarak doküman Sistem -Maddde No ekleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_354.png)

Açılan Madde No listesinde Madde No seçimi yapılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_355.png)

Sistem – Madde No seçimi yapılarak hazırlanan doküman sistem madde no ile ilişkilendirilmesi işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_356.png) 

**Anket Kullanılacak:** Yeni doküman ekranında Diğer bilgiler sekmesinde hazırlanan dokümanla

ilgili anket hazırlanacaksa  ilgili check box işaretlenir. Doküman dağıtım matrisindeki kullanıcılar için anket oluşur. Bu özelliğin kullanılması için dağıtım matrisinde  kullanıcılarda anket ile ilgili check box işaretli olması gerekmektedir. Anket ile ilgili check box işaretlendiğinde Yeni doküman ekranında Anket sekmesi aktif olur ve dokümanla ilgili anket soruları ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_357.png) butonu yardımıyla tanımlanır.

**Sınıflandırma:** Yeni Doküman ekranında Diğer Bilgiler sekmesinde hazırlanan dokümanda Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Dil Ayarları ekranın modül olarak Doküman Modülü seçilerek pasif olan liste tipli alana tanımlanan liste tipli parametrik alandır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_358.png)

Bu sekmede istenirse metin ,metin (Çoklu Satır), ölçü birimi, parasal, Personel, Personel(Çoklu Seçim), Departman, Departman(Çoklu Seçim), Sorgu, tipli parametrik alanları tanımlama işlemi yapılır.

**Dokümanın Gözden Geçirme Tarihi:** Yeni doküman ekranında Diğer bilgiler sekmesinde hazırlanan dokümanın gözden geçirme işlemi yapılacak ise gözden geçirme tarihini açılan takvim alanında seçildiği alandır.

**Parametrik Alanlar Sekmesi :**

Klasör bazında tanımlanan parametrik alanlar varsa, istenilen bilgiler doğrultusunda veri girişi yapıldığı sekmedir. Klasör Tanımlama ekranında 109 numaralı “	Klasör Bazında Parametrik Alan Kullanılacak Mı?” parametreye bağlı görüntülenen  ![ref69] butonu tanımlanan text, çoklu Text, Tarih, Nümerik gibi parametrik tipli alanların tanımlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_360.png) Doküman hazırlandığı klasör seçilerek  ![ref69] butonu tıklanarak parametrik alan tanımlama işlemi yapıldıyda bu sekmede tanımlanan parametrik alanlar görüntülenir. Örn: Doküman Link Adresi Text tipli parametrik alandır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_361.png)

**Ek Dokümanlar Sekmesi;**

Yeni doküman Ek dokümanlar sekmesinde bir dokümana bağlı ek dosyalar varsa sisteme yüklemek için kullanılır. Ana doküman yüklenmeden ek doküman yüklenememektedir. Ana doküman revize edildiğinde veya iptal edildiğinde aynı işlemler ek dokümanlar içinde gerçekleştirilmektedir.  Ek Dokümanların hangi aşamalarda yükleme işlemi parametreye bağlı olarak ayarlamaktadır. 36 numaralı “Ek dokümanlar hangi aşamalarda eklenebilsin: H(Hazırlama),G(Görüş),K(Kontrol),O(Onay),Revizyon Talebi(RT),İptal(I).Birden fazla aşama ise virgül ile ayırarak yazınız.” parametresinde parametre değerine göre hangi aşamalarda ek dökümanın yükleme işlemi belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_362.png)

Parametre değerinde Hazırlama aşamasında parametre değerine “H”, yazılır.

Paraemetre değerinde Görüş aşamasında parametre değerine “G”, yazılır.

Paraemetre değerinde Kontrol aşamasında parametre değerine “K”, olacak şekilde parametre değerine  aşamanın karşılığı olan harf değeri yazılır. Birden fazla aşama için aşamaların karşılığı olan harfler arasına virgül konularak parametreye tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_363.png)

**Yetki Matrisi Sekmesi;**

Bu sekmede klasör için oluşturulan yetki matrisi tanımlı olarak gelmektedir. Klasörün ayarlarına göre bu aşamada yetki matrisi değiştirilebilir ya da değiştirilemez. Klasör Tanımlama-Yeni kayıt ekranında Klasör Bilgileri sekmesinde “Yetki Matrisi Değiştirilemesin” alanı ilgili check box işaretli olduğu takdirde bu sekmede butonlar görüntülenmez ve yetki matrisi üzerinde değişiklik yapılamaz. Klasör Tanımlama -Yeni Kayıt ekranında Yetki matrisi sekmesinde  eklenen  kullanıcı Grubu /Pozisyonlar “Zorunlu” alanı ile ilgili check box işaretli ise de  Doküman Hazırlama aşamasında “Zorunlu” alanı ilgili check box işaretli Kullanıcı Grubu/Pozisyonlar yetki matrisinde sistem silinmesine izin vermez.Eğer yetki matrisi değiştirilecekse, bu aşamadaki işlemler klasör yetki matrisi düzenlenirken gerçekleştirilen işlemlerle aynıdır. Pozisyon/ Kullanıcı Grubu seçilerek “Okuma, Yazdırma, Hazırlama/ Revize Etme, Eski Revizyonları Görme, İptal Etme” yetkileri tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_364.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref7]: Seçili olan kullanıcı grubundaki personelleri gösterir.

![ref8]: Listeye pozisyon eklenir.

![ref9] : Listeye kullanıcı grubu eklenir.

![ref17] :Yetki matrisinde seçili satırın silinme işlemi yapılır.

Yeni Doküman ekranından yetki matrisi atamak için  ![ref9]/ ![ref8]  butonları tıklanır. Sistemde tanımlı olan Kullanıcı Grubu/ Pozisyon listesinde yetki verilmek istenilen kullanıcılar için seçim yapılır. Hangi yetkiler verilmek isteniyorsa işaretlenir.

Yeni Doküman ekranında Yetki Matrisi Sekmesinde ![ref8] butonu tıklanalarak açılan sistemde tanımlı Pozisyon listesinde Pozisyon seçimi yapılarak ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_365.png) butonu tıklanarak Yetki Matrisine Pozisyon ekleme işlemi yapılır.


![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_366.png)

Yetki Matrisine Pozisyon Ekleme işleminde hangi yetkiler verilmek isteniryorsa  yetkiler ilgili check box’lar işaretlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_367.png)

Tanımsız bir pozisyon kodu veya kullanıcı grubu varsa alınan hatanın önemsenmeden devam edilebilmesi için “Tanımsız Kod Bilgisini Önemsemeden Devam Et” alanı ile ilgili check box işaretlenir. Doküman Yönetimi Modülü parametrelerinde 123 numaralı “Dokuman Hazırlama/Revizyon esnasında Yetki Dağıtım Matrisinde Tanımsız Kod var ise yinede devam edilmesine izin ver” parametresinde parametre değeri “Evet” seçilerek parametre aktif edilir. ![ref70] Yetki matrisinde atama yapılan  pozisyon sahibi  yok ise Tanımsız kod bilgisi içerir. Bu “Tanımsız kod bilgisini önemsemeden devam et” seçeneği işaretlenerek geçilir. Bu seçeneğin işaretlenerek tanımsız kod bilgisinin önemsemeden geçilmesi için 123 numaralı parametrenin aktif olması ve “Tanımsız Kod Bilgisini Önemsemeden Devam Et” alanı ile ilgili check box işaretli olması gerekir. Aksi takdirde parametre pasif ve yetki matrisinde tanımsız kod bilgisi içeriyorsa  sistem doküman hazırlama/revizyon işlemleri kayıt işlemlerinde “Yetki matrisi tanımsız kod bilgisi içermekte” uyarı mesajı verir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_369.png)

**Dağıtım Matrisi Sekmesi;**

Bu sekmede dokümanların okuma görevi olarak kimlere yayınlanacağı belirtilmektedir. Kullanıcılar ve kullanıcı grupları seçilebilir. Bu kişiler dokümanı okumakla yükümlüdürler. Dağıtım Matrisi klasörden tanımlı olarak gelmektedir. Yapılan klasör ayarına göre dağıtım matrisi değiştirilebilir/ değiştirilemez. Klasör Tanımlama-Yeni kayıt ekranında Klasör Bilgileri sekmesinde “Dağıtım Matrisi Değiştirilemesin” alanı ilgili check box işaretli olduğu takdirde bu sekmede butonlar görüntülenmez ve dağıtım matrisi üzerinde değişiklik yapılamaz. Doküman Dağıtım Matrisinde “Önemli” alanı ile ilgili check box işaretli olan kullanıcı grupları ya da pozisyonlar için “Okunması Gereken Önemli Dokümanlar Listesi” adında bir okuma görevi oluşur. Kişinin “Bekleyen İşlerim” menüsünde “Okunması Gereken Önemli Dokümanlar Listesi” olarak görüntülenir. Personellere doküman okuma görevi gitmeyip, sadece doküman yayınlanma maili iletilsin isteniyorsa “Okuma Görevi Düşmesin” seçeneği işaretlenir. Dağıtım Matrisinde Önemli fonksiyonu 273 numaralı “Dağıtım matrisinde Önemli Dokuman fonksiyonu kullanılacak mı?” parametresine parametre değeri “Evet” seçilerek parametre aktif edilerek  görüntülenmektedir.

Doküman Yönetimi  Modülü parametrelerinde 162 numaralı “Okuma Görevi Atama Tipi: 1=Okunması Gereken Dokumanlar, 2=Okunması Gereken Önemli Dokumanlar, 3= Her İkisi” parametre değerine okuma görevi atama tipi belirlenir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_370.png)

Bu parametreye göre okuma görevi olarak parametre değeri “3” olarak tanımlıdır. Parametre değerine göre okuma görevleri olarak “Okunması Gereken Dokumanlar Listesi” ve “Okunması Gereken Önemli Dokumanlar Listes” olarak bekleyen işlere atanması işlemi yapılır. Parametre değerinde 1, 2, ve 3 dışında bir değer ataması yapıldığında okuma görevleri bekleyen işlere görev olarak düşmeyecektir.

Dağıtım Matrisinde “Okuma Görevi Düşmesin” fonksiyonu 274 numaralı “Dağıtım matrisinde Okuma Görevi Düşmesin fonksiyonu kullanılacak mı ?” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilerek görüntülenir.

Dağıtım Matrisinde “Anket” fonksiyonu 81 numaralı “Dokumanda Anket kulakçığı kullanılacak mı? (E/H)” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilerek görüntülenen bir alandır.

Entegre Yönetim Sistemi/ Doküman İşlemleri/ Raporlar/ Doküman İzleme Raporu’nda Önemli ve Önemsiz dokümanların okunma durumları, görev atama tarihleri ve kaç günde okudukları bilgisi görülebilmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_371.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref7]: Seçili olan kullanıcı grubundaki personelleri gösterir.

![ref8]: Listeye pozisyon eklenir.

![ref9] : Listeye kullanıcı grubu eklenir

![ref17] : Listede seçili olan pozisyondaki/ kullanıcı grubundaki kullanıcıları siler.

Yeni Doküman ekranında dağıtım matrisi atamak için  ![ref9]/ ![ref8]    butonları tıklanır. Sistemde tanımlı olan Kullanıcı Grubu/ Pozisyon listesinden dağıtıma eklenmek istenilen kullanıcılar için seçim yapılır. 

Yeni Doküman  ekranında Dağıtım Matrisi sekmesinde ![ref8] butonu tıklanarak Dağıtım matrisine pozisyon ekleme işlemi yapılır


![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_372.png)

Açılan Pozisyon listesinde dağıtım matrisine eklenecek Pozisyon seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_373.png)  butonu tıklanarak dağıtım matrisine pozisyon ekleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_374.png)

Dağıtım Matrisine Pozisyon ekleme işleminde sonra önemli doküman ise önemli alanı ile ilgili check  box , okuma görevi düşmesin isteniyor ilgili check box veya anket görevi düşmesi isteniyorsa anket ile ilgili check box işaretlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_375.png)

Dağıtım Matrisinde Tanımsız bir pozisyon kodu veya kullanıcı grubu varsa alınan hatanın önemsenmeden devam edilebilmesi için “Tanımsız Kod Bilgisini Önemsemeden Devam Et” alanı ile ilgili check box işaretlenir. Doküman Yönetimi Modülü parametrelerinde 123 numaralı “Dokuman Hazırlama/Revizyon esnasında Yetki Dağıtım Matrisinde Tanımsız Kod var ise yinede devam edilmesine izin ver” parametresinde parametre değeri “Evet” seçilerek parametre aktif edilir. ![ref70] Dağıtım  matrisinde atama yapılan  pozisyon sahibi  yok ise tanımsız kod bilgisi içerir. Bu “Tanımsız kod bilgisini önemsemeden devam et” seçeneği işaretlenerek geçilir. Bu seçeneğin işaretlenerek tanımsız kod bilgisinin önemsemeden geçilmesi için 123 numaralı parametrenin aktif olması ve “Tanımsız Kod Bilgisini Önemsemeden Devam Et” alanı ile ilgili check box işaretli olması gerekir. Aksi takdirde parametre pasif ve dağıtım  matrisinde tanımsız kod bilgisi içeriyorsa  sistem doküman hazırlama/revizyon işlemleri kayıt işlemlerinde “Dağıtım matrisi tanımsız kod bilgisi içermekte” uyarı mesajı verir.

**Onay sekmesi**

Bu dokümanın kimler tarafından onaylanacağı ve onay seviyeleri seçilir. Klasörde tanımlı onaycı varsa bu sekmede görüntülenir.Birden fazla onaycı seçilebilir. Seviyeleri 0,1,2,3,… olabilir. Sıfırıncı seviye son onaycı olup, bu pozisyon tarafından doküman onaylandıktan sonra yayınlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_376.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref22] : Listeye pozisyon eklenir.

![ref54] :Listede seçili olan pozisyonu siler. 

Yeni doküman ekranında onay matrisinde bulunması istenilen onaycıları atamak için ![ref22] butonuna tıklanır. Sistemde tanımlı olan pozisyon listesinden onay matrisine eklenmek istenilen kullanıcılar için seçim yapılır. 

Yeni Doküman  ekranında Onay matrisi sekmesinde onay matrisine onaycı ekleme işlemi için ![ref22] butonu tıklanarak sistemde tanımlı pozisyon listesinde Pozisyon seçilerek ![ref71]  butonu tıklanarak Onay matrisine pozisyon ekleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_378.png) 

Onay matrisinde onaycı ekleme işleminde sonra dokümanın onay seviyesi belirlenir. Onaylama işlemi tersten başlayacak şekilde son onaycı “0” olacak şekilde olur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_379.png)

**Görüş sekmesinde;**

Bu sekmede dokümanın kontrol onayından önce kullanıcıların görüşüne gönderilmesi isteniyorsa, gün ve kişi politikası belirlenerek görüş matrisi tanımlanır.Görüş matrisine görüşcü atama işlemi klasörde değilde doküman özelinde atama işleminin yapılması daha doğru olur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_380.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref72]: Listeye kullanıcı grubu eklenir.

![ref55] : Listeye pozisyon eklenir.

![ref56] :Listede seçili olan görüş pozisyonunu siler. 

Klasörde görüş matrisinde bulunması istenilen görüşçüleri atamak için ![ref55] butonuna tıklanır. Sistemde tanımlı olan pozisyon listesinden görüş matrisine eklenmek istenilen kullanıcılar için seçim yapılır. 

Yeni Doküman  ekranında Görüş  matrisi sekmesinde görüş  matrisine görüşcü ekleme işlemi için ![ref22] butonu tıklanılarak açılan sistemde tanımlı pozisyon listesinde pozisyon seçimi yapılarak ![ref71]  butonu tıklanarak yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_382.png)

Devam politikasına alanında kaç gün içerisinde kaç kişiden görüş istenildiği belirtilir. Örneğin; 3 gün içinde görüşe 1 kişinin görüş vermesi yeterlidir.Devam Politikasına göre 3 gün içerisinde 1 kişinin görüşü alınıp , alınan görüşlerin hazırlayan gönderilmesi sağlanır. Fakat  belirlenen zaman içerisinde  1 kişi görüş belirtmezse sadece 3 gün süresinin dolması beklenir.

Eğer görüş sekmesi klasörde ayarlanmışsa tanımlı olarak gelir. Klasörde yapılan ayara göre değiştirilebilir/ değiştirilemez. Klasör Tanımlama-Yeni Kayıt ekranında Klasör Bilgileri sekmesinde “Görüş Matrisi Değiştirilemesin” ile ilgili check box işaretli ise Yeni doküman ekranında Görüş sekmesinde  butonlar görüntülenmez ve görüş matrisi değiştirilemez.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_383.png)

**Kontrollü Kopya sekmesinde;**

Bu sekmede doküman hazırlama/ revizyon sayfalarında dokümanın kontrollü kopya dağıtım yerleri seçilmektedir. Doküman yayınlandığında dağıtım sorumlusu olan kişiler, kontrollü kopya dağıtımını yapmaları gerektiği konusunda  e-mail ile sistem tarafından bilgilendirilir.  Bu bilgiler Entegre Yönetim Sistemi/ Doküman İşlemleri/ Kontrollü Kopya menüsünden izlenebilmekte ve raporlanabilmektedir. Bu sekme Doküman Yönetimi Modülü parametrelerinden 39 numaralı “Doküman Modulünde Kontrollü Kopya kulakçığı kullanılacak mı? (E/H)” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_384.png)

Parametre aktif edildikten sonra Yeni Doküman ekranında Kontrollu Kopya sekmesi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_385.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref73]:Dağıtım yeri eklenir.

![ref74] :Dağıtım yeri grubu eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_388.png) :Listede seçili olan dağıtım bilgisi silinir.

Doküman ![ref73] butonuna tıklanarak dokümanın sistemde tanımlı fiziksel olarak dağıtılacağı dağıtım yerleri seçilme işlemi yapılarak ![ref71]  butonu tıklanılır

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_389.png)

Yeni Doküman ekranından  ![ref74]  butonuna tıklanılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_390.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_391.png)

Dokümana sistemde tanımlı Dağıtım Yeri Grubu listesinden seçim yapılarak ![ref75] butonu tıklanarak Dağıtım yeri grubu ekleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_393.png)

**Kullanım Yeri sekmesinde;**

Dokümanın hangi departmanlarda kullanacığı bilgisinin sistemde tanımlı departman listesinde seçildiği sekmedir. Parametreye bağlı olarak görüntülenen bir sekmedir.Doküman Yönetimi Modülü parametrelerinden 40 numaralı “Doküman Modulünde Kullanım Yeri kulakçığı kullanılacak mı? (E/H)” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. Parametre aktif edildikten sonra Doküman Hazırlama/Revizyon ekranınlarında Kullanın Yeri sekmesi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_394.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref76]:Kullanım yeri ekleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_396.png):Listede seçili satırı siler.

Yeni Doküman ekranından Kullanım yeri sekmesinde yeni bir kullanım yeri eklemek için ![ref76] butonu tıklanılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_397.png)

Sistemde tanımlı departman listesinde departman seçim işlemi ![ref75] butonu tıklanarak  kullanım yeri ekleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_398.png)

**Süreç Sekmesi;**

Hazırlanan dokümanın sistemde tanımlı firmanın süreçleri ile ilişkilendirme işleminin yapıldığı sekmedir. Bu sekme parametreye bağlı olarak görüntülenen bir sekmedir. Doküman yönetimi modülü parametrelerinde 41 numaralı “Doküman Modulünde Süreçler kulakçığı kullanılacak mı? (E/H)” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_399.png)

Parametre aktif edildikten sonra Doküman Hazırlama/Revizyon ekranlarında Süreç sekmesi görüntülenir. Doküman Hazırlama ekranlarında süreç sekmesi görüntülendikten sonra dokümana ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_400.png) butonu Süreç ekleme işlemi yapılarak dokümanın sistemde tanımlı süreçler ile ilişkilendirilmesi yapılır. 

Doküman Modülü parametrelerinde 291 numaralı “Süreç seçiminde süreç adımları listelensin mi?” parametresinde parametre değeri “Evet” seçilerek parametre aktif edilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_401.png)

Parametre aktif edildikten sonra Süreç seçiminde Süreç adımlarının listelenmesi sağlanır.

Doküman Yönetimi parametrelerinde 297 “Süreçler Gridinde gösterilecek alanlar (Birdern fazla için virgülle ayırınız.) (T=Süreç Tipi, A = Amaç, G = Girdi, K = Kaynak, C = Çıktı)” parametre değerindeki parametre değerlerinin alanların karşılığı harfler parametre değerine yazılarak süreç sekmesinde gridde ilgili alanların gridde görüntülenmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_402.png)

Parametre tanımlanan alanlar Süreçler sekmesinde gridde süreçin Amaç ,varsa süreç bileşeni   olan girdi görüntülenir. Parametreye Amaç=A ve Girdi=G değerleri parametreye tanımlanmıştır.

Doküman Yönetimi Parametrelerinde 344 numaralı “Süreçler için link kullanılsın mı?” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. Parametre aktif edildikten sonra Doküman Hazırlama /Revizyon ekranlarında Süreçler sekmesinde eklenen süreçler link şeklinde eklenir. İlgili link tıklanarak  Ensemble programında süreçin görüntülenmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_403.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref77]:Süreç ekleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_405.png):Listede seçili satırı siler.

Yeni Doküman ekranından Süreçler sekmesinde  yeni bir süreç ekleme işlemi için ![ref77] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_406.png)

Açılan Süreç listesinde sistemde tanımlı süreç seçimi işlemi yapılarak ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_407.png)  butonu tıklanarak Dokümana Süreç ekleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_408.png)

Yeni Doküman ekranında Süreçler sekmesinde eklenen Süreç linki tıklanarak Ensemble programında tanımlı süreçin görüntüleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_409.png)

Açılan Süreç Detayı ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_410.png) butonu tıklanarak Süreçin görsel modülü görüntelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_411.png)

**Denetim Soruları**

Hazırlananan dokümanın denetim Faaliyetleri modülü soru havuzu menüsündeki sistemden tanımlı soruları ile ilişkilendirilemesi işleminin yapıldığı sekmedir. Denetim Faaliyetleri modülü ile entegre bir şekilde çalışıldığı sekmedir.Denetim Faaliyetleri modülü ile Doküman Yönetimi modülün entegre çalışması için Doküman Yönetimi modülü parametrelerinde 42 numaraları “Doküman Modulünde Denetim Soruları kulakçığı kullanılacak mı? (E/H)” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_412.png)

Parametre aktif edildikten sonra Denetim soruları sekmesi görüntülenir ve sekmedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_413.png) butonu tıklanarak açılan sistemde tanımlı Denetim Faaliyetleri Modülü soru havuzunda sorular ile ilişkilendirme işlemi yapılır.


![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_414.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref78]:Denetim sorusu ekleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_416.png):Listede seçili denetim sorusunun silinme işlemi yapılır.

Yeni Doküman ekranında Denetim Soruları sekmesinde  yeni bir  denetim sorusu ekleme işlemi için ![ref78]butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_417.png)

Açılan sistemde tanımlı Soru listesinde hazırlanacak Dokümana eklenecek soru seçimi yapılarak ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_418.png) butonu tıklanarak denetim sorusu ekleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_419.png)

**Ek Dosyalar Sekmesi;**

Hazırlanan dokümana resim, tutunak, doküman gibi  vb. formatlardaki ek dosyalarının yüklendiği sekmedir.Parametre bağlı olarak görüntülenen bir sekmedir. Doküman Yönetim Modülü parametrelerinde 43 numaralı “Doküman Modulünde Ek Dosyalar kulakçığı kullanılacak mı? (E/H)” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_420.png)

Parametre aktif edildikten sonra Doküman Hazırlama/rRevizyon ekranlarında Ek Dosyalar sekmesi görüntülenir. Görüntülenen bu sekmede  dosya ekleme, eklenen dosyayı görüntüleme ve istenirse eklenen dosyayı silme işlemleri butonlar yardımıyla yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_421.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref79]:Yeni bir dosya yükleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_423.png):Listede seçili dosyanın görüntüleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_424.png):Listede seçili dosyanın silinme işlemi yapılır.

Yeni Doküman ekranında Ek Dosya sekmesinde yeni bir ek dosya yükleme işlemi için ![ref79] butonu tıklanır.Dosya Ekle ekranında Gözat butonu tıklanır

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_425.png)

Yüklenecek dosyanın seçim işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_426.png)

Dosya Ekle ekranında yüklenecek dosyanın seçimden sonra “Yükle” butonu tıklanarak dosyanın yükleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_427.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_428.png)

**Eğitim sekmesi;** 

Doküman bilgileri sekmesinde eğitim sorumlusu seçildikten sonra eğitim sekmesinde geçilir. Unvan ekleme alanından eğitim verilecek unvanlar belirlenir. Doküman onaylandıktan sonra eğitim sorumlusu tarafından doküman ile ilgili eğitim verilerek dokümanın yayınlanması sağlanır. Eğitim sekmesi parametre bağlı olarak görüntülen bir sekmesidir. Doküman Yönetimi parametrelerinden 48 numaralı “Doküman Modulünde Eğitim kulakçığı kullanılacak mı? (E/H)” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_429.png)

Parametre aktif edildikten sonra Doküman Hazırlama/Revizyon ekranlarında Eğitim sekmesi görüntülenir.Dokümanla ilgili bir eğitim verilmesi için Eğitim kulakçığı için ilgili parametre ayarlarının yapılması gerekmektedir. Doküman parametrelerinden 110.parametre olan “Eğitim sorumlusuna aksiyon açılsın mı” parametresinin parametre değeri “Evet”seçilerek   doküman onaylandığı zaman eğitim sorumlusuna eğitim gerçekleştirilmesi için aksiyon görevi  oluşur. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_430.png)

Bunun olabilmesi için eğitim sorumlusuna açılacak aksiyonun plan kodunun 111numaralı “Eğitim sorumlusuna açılacak aksiyonun plan kodu” parametresinde parametre değerine tanımlanması gerekir. Parametreye tanımlı Aksiyon Plan Kodu bilgisi Entegre Yönetim Sistemi/Aksiyon Yönetim/Planlama ekranında alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_431.png) 

Eğitim sorumlusuna açılacak aksiyonun tipi kodu  112 numaralı “Eğitim sorumlusuna açılacak aksiyonun tipi” parametresinde parametre değerine tanımlanır.  Aksiyon tipi kodu bilgisi Sistem Altyapı Tanımları/Aksiyon/Aksiyon Kalem Tipi Tanımlama menüsünde alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_432.png)

Doküman Yönetim parametrelerinden 145 numaralı parametre olan “Eğitim sorumlusu üzerinde açık aksiyon varken doküman yayınlayabilsin mi”  parametresinin parametre değeri “Evet” ise son onaycıda gönder butonuna tıkladığında “Eğitim sorumlusu üzerinde açık aksiyonlar var yine de gönderilsin mi” diye uyarı mesajı çıkmaktadır, onaylandığı takdirde eğitim görevi tamamlanmadan doküman yayınlanır. 145.parametrenin parametre değeri “Hayır” ise “Eğitim sorumlusu üzerinde açık aksiyonlar var, kapatılamaz” diye uyarı verir. Eğitim sorumlusu eğitimleri verip aksiyonu kapatmadan dokümanı yayınlanamaz.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_433.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref80]:Unvan ekleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_435.png):Listede seçili Unvan bilgisi silinir.

Yeni doküman ekranında Eğitim sekmesinde yeni bir Unvan ekleme işlemi için  ekranın sağ üst köşesindeki ![ref80] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_436.png)

Açılan sistemde tanımlı Unvan listesinde Unvan seçim işlemi yapılarak ![ref81] butonu tıklanarak  Eğitim sekmesine Unvan ekleme işlemi yapılır.	![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_438.png)

**Ürün sekmesi;**

Hazırlanan dokümanın sistemde tanımlı ürünler ile ilişkilendirilme işleminin yapıldığı sekmedir.Parametreye bağlı olarak görüntülenen bir sekmedir. Doküman Yönetimi Modülü parametrelerinde 66 numaralı “Doküman modülünde ürün kulakçığı kullanılacak mı?” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. Parametre aktif edildikten sonra Doküman Hazırlama /Revizyon ekranlarında ürün sekmesi görüntülenir. Görüntülenen bu sekme ile hazırlanan yeni doküman sistemde tanımlı ürünler ile ilişkilendirilmesi işlemi butonlar yardımıyla ile yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_439.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref82]:Ürün ekleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_441.png): Listede seçili ürün bilgisi silinir.

Yeni doküman ekranında Ürün sekmesinde Yeni bir ürün eklemek  için ekranın sağ üst köşesindeki ![ref82] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_442.png)

Açılan sistemde tanımlı Ürün listesinden seçin yapılarak ![ref81]  butonu tıklanarak Ürün ekleme işlemi yapılarak doküman ürün ile ilişkisi kurulur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_443.png)

**Anket Sekmesi;**

Doküman yayımlandıktan sonra dağıtım matrisinde seçilen kullanıcılara dokümanla ilgili bir anket gönderilmek isteniyorsa Doküman Yönetimi Modülü parametrelerinden 81 numaralı “Dokümanda anket kulakçığı kullanılacak mı” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_444.png)

Parametre aktif edildikten sonra Doküman Hazırlama/Revizyon ekranlarında Anket sekmesi görüntülenir. Görüntülenen bu sekmede ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_445.png)  butonu tıklanarak istenilen format soru ekleme işlemi yapılır.  Anket sekmesinin aktif edilmesi için öncelikle Diğer Bilgiler sekmesinde Anket Kullanılacak alanı ile ilgili check box’ın işaretli olması gerekmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_446.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref83]:Ankete soru ekleme işlemi yapılır.

Yeni doküman ekranında Anket sekmesinde ankete  1. soru ekleme işlemi için ![ref83] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_448.png)

1. Soru için 

Açılan ekranında soru alanında anketin 1. soru tanımı ve  seçenek kısmında da seçenekleri yazılarak gerekli alanlar ilgili bilgiler girildikten sonra ekranın sağ üst köşesindeki ![ref84] butonu tıklanarak Anket sorusu kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_450.png)

Yeni doküman ekranında Anket sekmesinde ankete  2. soru ekleme işlemi için ![ref83] butonu tıklanılır.	![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_451.png)

Açılan ekranında soru alanında anketin 2. soru tanımı ve  seçenek kısmında da seçenekleri yazılarak gerekli alanlar ilgili bilgiler girildikten sonra ekranın sağ üst köşesindeki ![ref84] butonu tıklanarak Anket sorusu kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_452.png)

Soru Tanımlamada dikkat edilecek husus sorunun doğru seçeneğinin işaretli olarak tanımlı olması gerekmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_453.png)

Doküman Görme Formatı Sekmesi;

Doküman görme formatının seçildiği sekmedir. Dokümanın görüntülemede, yazdırmada, görüş aşamasında, onay aşamasında ve doküman kalite kaydı  ise görme formatlarının seçildiği sekmedir. Görme formatı olarak  Şirket formatı, Pdf kullanma, Pdf kullanmama,  Doküman Görüntüleyici ve Document Viewer seçeneklerinde seçim yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_454.png)

**Tarihçe Sekmesi;**

Dokümanın daha önce hangi işlemlerden geçtiğini gösterildiği sekmedir. Yeni doküman hazırlama aşamasında bu kısım boş gelmektedir

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_455.png)

**Doküman Sekmesi;**

Sisteme yüklenecek olan doküman, Doküman Dosyası Yükleme (Türkçe) alanında bulunan  ![ref85] (Dosya ekle) butonu tıklanarak  bilgisayardan yüklenecek dokümanın  seçilir ve yükleme işlemi gerçekleştirilir. Dokümanın mevcut dillerdeki versiyonları dil açıklamalarından yüklenebilir. Yüklenen doküman ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_457.png) (Dosya Görüntüle) butonu ile görüntülenebilir.

Yeni Doküman ekranında ![ref85] (Dosya Ekle) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_458.png)

Açılan Dosya Ekle ekranında Gözat butonu tıklanılır

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_459.png)

Bilgisayarda yüklenecek dosya seçimi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_460.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_461.png)

Dokümanı yüklendiğinde “dosya başarıyla aktarılmıştır” bilgisi alınmaktadır.![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_462.png) (Çevirmen Görevi Ata) butonu ile dokümanın başka dillere çevrilmesi için çevirmen görevi atanabilir.

Bu aşamada istenirse başka dokümanlara ve klasörlere link alınabilir. Açılır listelerden doküman/ klasör seçilir ve ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_463.png) (Link al)  butonu ile link alınır. Bu link, doküman içerisinde kullanılarak başka dokümanlara bağlantı verilebilir.

Doküman yükleme işleminden sonra henüz hazırlama işlemi tamamlanmadıysa, doküman bilgileri sekmesinden ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_464.png) butonuyla doküman taslağa dönüştürülerek saklanabilir. Taslak doküman, hazırlayıcının **“Bekleyen İşlerim**” sayfasında “**Saklanan Dokümanlar**” olarak görüntülenmektedir.

Eğer Dokümanla ilgili bütün hazırlık işlemleri tamamlandıktan sonra Doküman Bilgileri sayfasındaki  ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_465.png) butonu ile doküman onay süreci başlatılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_466.png)

Sistem tarafından “Göndermek istediğinizden emin misiniz? “mesajında “Tamam” butonu  tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_467.png)

Eğer görüş isteniyorsa hazırlanan doküman görüşe gidecektir. Eğer görüş kullanılmayacaksa (görüş matrisi tanımlı olmayan süreçlerde), süreç kontrol onayıyla devam eder. Eğer kontrolcü tanımlanmışsa önce kontrol onayına gider, kontrolcü tanımlı değilse onay matrisinde tanımlı kişilerin onayına gider.

Sistem tarafından dokümanın görüşe gönderildiği ve gönderildiği kullanıcı bilgisi verillir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_468.png)
##### **6.2.4.1. Görüş Bildirme Süreci**
Görüş bildirecek kişilerin “**Bekleyen İşlerim**” sayfasında “**Görüş Bekleyen Dokümanlar**” işi olarak görev düşer. Ayrıca görüşe gönderilen dokümanlar mail yoluyla da görüş verecek personele bildirilir. Görüş aşamasında Qdms ana giriş ekranında görüşcünün kullanıcı adı ve parolası ile Qdms local adresine giriş yapılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_469.png)

Görüşcünün açılan  Bekleyen işlerim ekranında “**Görüş Bekleyen Dokümanlar**” görevi tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_470.png)

İlgili görevdeki doküman kodu alanında link tıklanarak ilgili doküman bilgilerine ulaşılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_471.png)  

Görüş aşamasında görüşçü dokümanı görmek için doküman sekmesi tıklar ve Doküman Dosyası Yükleme (Türkçe) alanında ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_472.png)(Dosya Görüntüle) butonu ile dokümanı bilgisayarı indirerek görüntüler.  Görüntülenen dokümanı inceler ve incelediği doküman ile   varsa kanıt dosyaları isterse Ek Dosyalar sekmesinde dosya yükleme işlemi yapar.  Ek Dosyalar sekmesinde bu aşamada yüklenen ek dosyanın  eklenen statüsü alanında statüsü “Görüş” olarak  görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_473.png)

Dokümanın inceledikten sonra görüşleri bildirmek için  görüşler sekmesi tıklar. Doküman Yönetimi Modülü parametrelerinde “Görüş adımında Kabul-Ret özelliği kullanılacak mı?” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_474.png)

Parametre aktif edildikten sonra  görüş sekmesinde Görüş seçimi alanı  görüntülenir. Bu alanda ilgili seçenekler seçilerek Görüş aşamasında Kabul -Ret özelliğinin kullanılması sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_475.png)

Görüşcü parametreye bağlı olarak görüntülenen Kabul -Ret özelliğinde görüş seçimi alanında ilgili seçenekler ilgili check box işaretleyerek seçimi yapar. Görüşler sekmesinde Görüşcü  Not  alanında incelediği dokümanla ilgili görüşleri bildirir. İlgili görüşü  ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_476.png)  butonuna tıklanarak doküman hazırlayan kişiye iletilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_477.png)

Dokümanı hazırlayan kişinin “**Bekleyen İşlerim**” sayfasında, “**Görüşten Dönen Dokümanlar**” görevi olarak iş düşer.  Qdms ana giriş ekranında hazırlayan kişinin kullanıcı adı ve parolası  yazılarak  Qdms’sine giriş yapılarak Bekleyen işlerim sayfası  görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_478.png)

Dokümanı hazırlayan kişinin Bekleyen İşlerim sayfasındaki “Görüşten Dönen Dokümanlar” görevi olarak görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_479.png)

Görüntülenen görevdeki doküman kodu alanındaki link tıklanarak ilgili doküman bilgilerine ve verilen görüşlere ulaşılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_480.png)

Görüş sekmesi tıklanılır. Hangi kullanıcı tarafından hangi görüşün verildiği listesi görüntülenir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_481.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref86]:Doküman hakkındaki görüşler  bilgisi görüntülenir

![ref87]: Listeye görüşcü olarak kullanıcı grubu eklenir.

![ref88]: Listeye görüşcü olarak pozisyon eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_485.png): Listede seçili olan görüş pozisyonunu siler.

![ref89]: Dokümanda önceki görüşçülere tekrar görüşe gönderilme işlemi yapılır.

Gelen görüşlere göre dokümanda değişiklik yapılacaksa doküman sekmesine tıklanır, doküman üzerinde gerekli düzenlemeler yapılır. Düzenlenen doküman yeniden görüşe gönderilmek isteniliyorsa görüş sekmesine gelinerek yeni personeller için ![ref88]   veya kullanıcı gruplarına içinde ![ref87] butonları tıklanarak  görüşe gönderilebilir. Eğer isteniyorsa ![ref89]  butonu ile doküman önceki görüşçülere tekrar görüşe gönderilebilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_487.png)

![ref86] butonu ile de seçili olan kullanıcı görüşleri görüntülenir. Görüşler ekranında görüşler ile ilgili parametreye bağlı olarak görüntülenen Görüş Kabul Kriteri özelliğide kullanıldığı görülür. Varsa  Ek dosyalar sekmesinde yüklenilenen dosyalar incelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_488.png)

Doküman tekrar görüşe gönderilmeyecekse,![ref90]   butonu ile doküman akışa göre önce ön kontrolcü tanımlı ise ön kontrolle, ön kontrol aşamasından sonra (kontrolcü tanımlı ise) kontrole, sonra onaya gönderilir.

Doküman Hazırlama ekranında Görüş sekmesinde ![ref90] butonu tıklanarak  ön kontrolde tanımlı kişinin doküman ön kontrollerine  gönderilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_490.png)

Sistem tarafından “Göndermek istediğinize emin misiniz?” mesajında “Tamam” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_491.png)

Sistem tarafından dokümanın ön kontrolle gönderildiği ve gönderildiği kullanıcı bilgisi verillir

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_492.png)
##### **6.2.4.2. Ön kontrol Süreci**
Doküman Ön kontrol aşamasında ön kontrolcünün  “**Bekleyen İşlerim**” sayfasında “**Ön Kontrolde  Bekleyen Dokümanlar**” işi  olarak görev oluşur. Ön kontrol aşamasında Qdms ana giriş ekranında ön kontrolcünün  kullanıcı adı ve parolası ile Qdms local adresine giriş yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_493.png)

Ön kontrolcünün  açılan  Bekleyen işlerim ekranında “**Ön Kontrol Bekleyen Dokümanlar**” görevi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_494.png)

Görüntülenen görevdeki doküman kodu alanında link tıklanarak ilgili doküman bilgilerine ulaşılır. Ön kontrol eden kişi tıpkı doküman hazırlayan gibidir. Gerekli gördüğü durumlarda, doküman üzerinde her türlü değişikliği yapıp, dokümanı reddetme işlemi yapmadan değişiklik yaptığı dokümanı yükleyip, süreci devam ettirebilir. Hem hazırlanan doküman üzerinden, hem de hazırlama aşamasındaki doküman bilgileri/ yetki matrisi/ dağıtım matrisi/ onay matrisi gibi açılan her sekmede değişiklik yapabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_495.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref91]:Dokümanın kayıt işlemi yapılır.

![ref92]:Kaydet ve devam etme işlemi yapılır. Parametreye bağlı olarak görüntülenen  bir butondur.Doküman Yönetimi parametrelerinde 331 numaralı “Doküman hazırlama sayfasında kaydet ve devam et butonu kullanılsın mı?” parametresi parametre değeri “Evet” seçilerek parametre aktif edilir.

![ref93]

Parametre aktif edildikten sonra Doküman Hazırlama aşamasında  ![ref92] butonu görüntülenir.

![ref94]:Doküman onaylama işlemi yapılır.

![ref95]:Doküman red nedeni yazılarak ret etme işlemi yapılır.

![ref96]: İlgili kişilerde bu aşamada yorum isteme işlemi yapılır. Parametreye bağlı olarak görüntülenen bir butondur. Doküman Yönetimi parametrelerinde 113 numaralı “Kontrol ve Onay Adımında Yorum İstenebilecek mi” parametresinin parametre değeri “ Evet” seçilerek parametre aktif edilir.

![ref97]

Parametre aktif edildikten  ![ref96] butonu görüntülenir ve ilgili personellerde seçim yapılarak bu personellerden bu aşamada  yorumları alınır.  

![ref98]: Tanımlanan yorum bilgisi gösterir.

Ön Kontrol aşamasında Diğer işlemler alanındaki açılır liste tıklanarak ![ref96] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_504.png)

Açılan ekranında Yorum istenecek alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_505.png) butonu tıklanarak açılan sistemden tanımlı Personel listesinde yorum istenecek kişi bilgisi seçilir. Açıklama alanında  seçilen kişinin doküman ile ilgili yorum bilgisi yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_506.png)

Gerekli alanlarla ilgili bilgiler girildikten sonra ekranın sol üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_507.png)  butonu tıklanarak ilgili kişinin yorumu kaydetme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_508.png)

Tanımlanan Yorumları görmek için ![ref98] butonu tıklanarak görüntülenmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_509.png)

Ön Kontrol aşamasında ön kontrolcü Doküman sekmesi tıklayarak Dokuman Dosyası Yükleme (Türkçe) alanında ![ref99] (Dosya Görüntüle) butonu ile dokümanı bilgisayarına indirerek görüntüler.  

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_511.png)

Ön Kontrolcü bu aşamada görüntülenen dokümanı yapı ve içerik olarak incelemesi yapar. Dokümanı yapı ve içerik olarak inceledikten sonra dokümanı  onaylama ve Reddetme işlemleri yapar. 

Ön Kontrol Aşamasında ![ref95] butonu tıklayarak dokümanı ret etme işlemi yapar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_512.png)

Dokümanı reddet işleminde ret nedeni  zorunlu olarak yazmak zorundadır. Dokümanı red işleminde red nedeni yazarak  ve red nedeni ile varsa  ilgili ek dosya yükleme işlemi yaparak hazırlayan kişi dokümanı gönderir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_513.png)

Ön Kontrolcü dokümanı yapı ve içerik bakımından inceledikten sonra görüşleri ile bilgiler Ek Dosyalar sekmesinde dosya yükleme işlemi yaparak bu aşamada belirtir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_514.png)

Doküman Ön kontrol  ekranında Ek dosyalar sekmesinde  ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_515.png)  butonu tıklanayarak görüşlerini belirtiği ek dosyayı yükleme işlemi yapar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_516.png)

Dosya Ekle ekranında “Gözat” butonu tıklanarak yüklenecek ek dosya seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_517.png)

Dosya Ekle ekranında “Yükle” butonu tıklanarak ek dosyanın bu aşamada yükleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_518.png)

Ek Dosyalar sekmesinde hangi aşamada ek dosya yükleme işlemi yapıldıysa  eklenen Statü alanında statüsü sistem tarafından belirtirilir.

Ön Kontrolcü doküman ile ilgili yapı ve içerik incelemesinde  ve bu inceleme ile ilgili ek dosyasının ön kontrol aşamasında yükleme işlemi yaptık sonra  Doküman Bilgileri sekmesi tıklar.

Doküman Bilgileri sekmesinde ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_519.png) butonu tıklayarak akıştaki kontrol aşamasından kontrolcüye dokümanı kontrol işemini yapmak üzere gönderir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_520.png)

Sistem tarafından “Göndermek istediğinizden emin misiniz? “mesajında “Tamam” butonu  tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_521.png)

Sistem tarafından dokümanın kontrole gönderildiği ve gönderildiği kullanıcı bilgisi verillir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_522.png)

Kontrol aşamasında doküman kontrolcünün “**Bekleyen işlemlerim**” sayfasında “**Kontrolde Bekleyen Dokümanlar**” işi olarak görev düşer.
##### **6.2.4.3.Kontrol Süreci**
Kontrole gönderilen doküman, kontrolcünün “**Bekleyen İşlerim**” sayfasında “**Kontrol Bekleyen Dokümanlar**” listesi altında görüntülenir. Doküman koduna alanındaki doküman linki tıklanarak ilgili doküman bilgileri açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_523.png)

Kontrol eden kişi tıpkı doküman hazırlayan gibidir. Gerekli gördüğü durumlarda, doküman üzerinde her türlü değişikliği yapıp, dokümanı reddetmeden yeniden yükleyip, süreci devam ettirebilir. Hem hazırlanan doküman üzerinden, hem de hazırlama aşamasındaki doküman bilgileri/ yetki matrisi/ dağıtım matrisi/ onay matrisi gibi açılan her sekmede değişiklik yapabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_524.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref91]: Dokümanın kayıt işlemi yapılır.

![ref92]:Kaydet ve devam etme işlemi yapılır. Parametreye bağlı olarak görüntülenen bir butondur.Doküman Yönetimi parametrelerinde 331 numaralı “Doküman hazırlama sayfasında kaydet ve devam et butonu kullanılsın mı?” parametresi parametre değeri “Evet” seçilerek parametre aktif edilir.

![ref93]

Parametre aktif edildikten sonra Doküman Hazırlama aşamasında  ![ref92] butonu görüntülenir.

![ref94]:Doküman onaylama işlemi yapılır.

![ref95]:Doküman red nedeni yazılarak ret etme işlemi yapılır.

![ref96]: İlgili kişilerde bu aşamada yorum isteme işlemi yapılır. Parametreye bağlı olarak görüntülenen bir butondur. Doküman Yönetimi parametrelerinde 113 numaralı “Kontrol ve Onay Adımında Yorum istenebilecek mi” parametresinin parametre değeri “ Evet” seçilerek parametre aktif edilir. 

![ref97]Parametre aktif edildikten  ![ref96] butonu görüntülenir ve ilgili personellerde seçim yapılarak bu personellerden bu aşamada  yorumları alınır.  

![ref98]: Tanımlanan yorum bilgisi gösterir.

Kontrol aşamasında  kontrolcü Doküman sekmesi tıklayarak Dokuman Dosyası Yükleme (Türkçe) alanında ![ref99] (Dosya Görüntüle) butonu ile dokümanı bilgisayarına indirerek görüntüler.  Kontrolcü bu aşamada görüntülenen dokümanı  ve tüm sekmelerin incelemesini yapar.  Dokümanla ilgili görüşleri varsa bu görüşlerini bir ek dosyada belirterek  Ek Dosyalar sekmesinde yükleme işlemi yapar.Bu aşamada yüklenen ek dosyanın statüsü “Kontrol” olarak sistem tarafından  belirtilir. 

Dokümanı üzerinde bilgileri ile inceledikten sonra dokümanı  onaylama ve Reddetme işlemleri yapılır. Doküman Bilgileri sekmesi tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_525.png)

Doküman Bilgileri sekmesinde Kontrol aşamasında ![ref95] butonu tıklayarak istenirse dokümanı ret etme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_526.png)

Dokümanı reddet işleminde ret nedeni  zorunlu olarak yazılmak zorundadır. Dokümanı red işleminde red nedeni yazarak  ve red nedeni ile varsa  ilgili ek dosya yükleme işlemi yaparak hazırlayan kişi dokümanı gönderilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_527.png)

Kontrol aşamasında kontrolcü doküman bilgileri ve sekmeleri üzerinde gerekli incelemeyip yaptıktan sonra dokümanı uygun gördüğünde  ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_528.png) butonu tıklanayarak onay aşamasındaki onaycılara  doküman onaya gönderilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_529.png)

Sistem tarafından “Göndermek istediğinizden emin misiniz? “mesajında “Tamam” butonu  tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_530.png)

Onay Matrisinde sekmesinde 2 . onaycı bulunmaktadır. “0” sıfır son onaycı olup, onaylama aşaması ters şekilde çalışmaktadır. İlk olarak 1. Seviyedeki onaycıda onaylama işlemi yapıldıktanın sonra son  olarak  0. Seviyedeki  onaycı ile onay aşama tamamlanarak doküman dağıtım matrisindeki kişilere okuma görevi olarak düşer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_531.png)

1\.seviyede bulanan onaycının “**Bekleyen işlerim**” sayfasından “**Onay Bekleyen Dokümanlar**” işi olarak görev düşer. Qdms ana giriş ekranından 1. Seviye onaycının kullanıcı adı ve parola bilgisi ile Qdms local adresine giriş yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_532.png)
##### **6.2.4.4.Onay Süreci**
Onaya gönderilen doküman, onay matrisinde seviyelerine göre sırasıyla, onaycının“**Bekleyen İşlerim**” sayfasında “**Onay Bekleyen Dokümanlar**” listesi altında görüntülenir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_533.png)

İlgili görevdeki Doküman koduna alanındaki doküman kodu linki tıklanarak ilgili doküman bilgileri açılır. Onaycı doküman bilgileri üzerinde değişiklik yapamaz. Bu aşamada sadece doküman görüntülenebilir ve onay/ red işlemlerini  gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_534.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref91]:Doküman kayıt işlemi yapar.

![ref92]:Kaydet ve devam etme işlemi yapılır. Parametreye bağlı olarak görüntülenen bir butondur.Doküman Yönetimi parametrelerinde 331 numaralı “Doküman hazırlama sayfasında kaydet ve devam et butonu kullanılsın mı?” parametresi parametre değeri “Evet” seçilerek parametre aktif edilir.

![ref93]

Parametre aktif edildikten sonra Doküman Hazırlama aşamasında  ![ref92] butonu görüntülenir.

![ref94]:Doküman onaylama işlemi yapılır.

![ref95]:Doküman red nedeni yazılarak ret etme işlemi yapılır.

![ref100]: İlgili kişilerde bu aşamada yorum isteme işlemi yapılır. Parametreye bağlı olarak görüntülenen bir butondur. Doküman Yönetimi parametrelerinde 113 numaralı “Kontrol ve Onay Adımında Yorum İstenebilecek mi” parametresinin parametre değeri “ Evet” seçilerek parametre aktif edilir.

![ref97]

Parametre aktif edildikten  ![ref100] butonu görüntülenir ve ilgili personellerde seçim yapılarak bu personellerden bu aşamada  yorumları alınır.  

![ref98]: Tanımlanan yorum bilgisi gösterir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_536.png)

Doküman kulakçığında yer alan  ![ref101] (dosya görüntüle)  butonu ile doküman açılır.  Şablon kullanılarak hazırlanmış dokümanlarda, ![ref102] (yayınlanmış halini göster)  butonu ile hazırlama şablonuyla oluşturulan dokümanın görüntülenmesi sağlanır. Doküman Bilgileri sekmesi tıklanılır.

Onay sürecinde ![ref103] butonu ile ret nedeni girilerek doküman onayı reddedilir

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_540.png) Red durumunda mutlaka red nedeni bilgisinin girilmesi gerekmektedir. İstenirse ret nedeni ile ilgili ek dosya yükleme işlemi yapılır. Bu aşamada gönderilecek kişi alanında Hazırlayan/Revize eden , Kontrol  Eden ve Ön kontrol Eden seçeneklerinde seçim işlemi yapılır.![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_541.png)

Doküman Onaylama ekranında Doküman Bilgileri sekmesinde onay açıklaması bilgisi girilerek  ![ref104] butonu tıklanarak onay aşamasındaki    0. Seviyedeki kullanıcıya doküman onaya gönderilir. Bu aşamada onay açıklama parametreye bağlı olarak görüntülenen bir alandır. 85 numaralı “Onay Açıklaması zorunlu olsun” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. 

![ref105]

Parametre aktif edildikten onay aşamasındaki bir dokümanda onaylama işleminde onay açıklaması alanın ile ilgilinin bilgininin girilmesi  zorunluğu getirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_544.png)

Sistem tarafından “Göndermek istediğinizden emin misiniz? “mesajında “Tamam” butonu  tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_545.png)

Sistem tarafından dokümanın onaya gönderildiği ve gönderildiği kullanıcı bilgisi verillir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_546.png)

1\.seviyedeki onay matrisindeki onaycı olan kullanıcının onay işlemi bittikten sonra  Doküman son onaycı olan  0. Seviyedeki  Onaycının “**Bekleyen İşlerim**” sayfasında “**Onayda Bekleyen Dokümanlar**” işi olarak görev düşer.Son onaycının kullanıcı adı ve parola bilgisi ile Qdms local adresine  giriş yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_547.png)

Onaya gönderilen doküman, son  onaycının “**Bekleyen İşlerim**” sayfasında “**Onay Bekleyen Dokümanlar**” listesi altında görüntülenir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_548.png)

İlgili görevdeki Doküman koduna alanındaki doküman kodu linki tıklanarak ilgili doküman bilgileri açılır. Onay aşamasındaki son onaycı doküman bilgileri üzerinde değişiklik yapamaz. Bu aşamada sadece doküman görüntülenebilir ve onay/ red işlemlerini gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_549.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref91]:Dokümanın kayıt işlemi yapılır.

![ref92]:Kaydet ve devam etme işlemi yapılır. Parametreye bağlı olarak görüntülenen bir butondur.Doküman Yönetimi parametrelerinde 331 numaralı “Doküman hazırlama sayfasında kaydet ve devam et butonu kullanılsın mı?” parametresi parametre değeri “Evet” seçilerek parametre aktif edilir.

![ref93]

Parametre aktif edildikten sonra Doküman Hazırlama aşamasında  ![ref92] butonu görüntülenir.

![ref94]:Doküman onaylama işlemi yapılır.

![ref95]:Doküman red nedeni yazılarak ret etme işlemi yapılır.

![ref100]: İlgili kişilerde bu aşamada yorum isteme işlemi yapılır. Parametreye bağlı olarak görüntülenen bir butondur. Doküman Yönetimi parametrelerinde 113 numaralı “Kontrol ve Onay Adımında Yorum İstenebilecek mi” parametresinin parametre değeri “ Evet” seçilerek parametre aktif edilir. 

![ref97]

Parametre aktif edildikten  ![ref100] butonu görüntülenir ve ilgili personellerde seçim yapılarak bu personellerden bu aşamada  yorumları alınır.  

![ref98]: Tanımlanan yorum bilgisi gösterir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_550.png)

Doküman sekmesinde yer alan  ![ref101] (dosya görüntüle)  butonu ile doküman açılır.  Şablon kullanılarak hazırlanmış dokümanlarda, ![ref102] (yayınlanmış halini göster)  butonu ile hazırlama şablonuyla oluşturulan dokümanın görüntülenmesi sağlanır. Doküman Bilgileri sekmesi tıklanılır.

Dolüman Onaylama  ekranından onay sürecinde ![ref103] butonu ile ret nedeni girilerek doküman onayı reddedilir

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_551.png) Red durumunda mutlaka red nedeni bilgisinin girilmesi gerekmektedir. İstenirse ret nedeni ile ilgili ek dosya yükleme işlemi yapılır.  Bu aşamada gönderilecek kişi alanında Hazırlayan/Revize eden , Kontrol  Eden ve Ön kontrol Eden seçeneklerinde seçim işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_552.png)

Doküman Onaylama ekranında Doküman Bilgileri sekmesinde onay açıklaması bilgisi girilerek  ![ref104] butonu tıklanarak  dokümanın son onaycı tarafından onaylama işlemi  başlatılır.

Bu aşamada onay açıklama parametreye bağlı olarak görüntülenen bir alandır. 85 numaralı “Onay Açıklaması zorunlu olsun” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. 

![ref105]

Parametre aktif edildikten onay aşamasındaki bir dokümanda onaylama işleminde onay açıklaması alanı görüntülenir ve bu alanın bilgisi girişinin yapılması zorunluğunu getirir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_553.png)

Sistem tarafından “Göndermek istediğinizden emin misiniz? “mesajında “Tamam” butonu  tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_554.png)

Sistem tarafından “Doküman yayınlanıp kullanıma açılmıştır” mesajı verilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_555.png)

0nay aşaması sürecinde, onay matrisindeki sıraya göre son onaydan geçen doküman yayınlanarak dağıtım matrisinde olan kişilere dağıtılır ve kullanıma açılır. Dağıtım matrisindeki ilgili kişilere sistem tarafından mail gönderilir ve dokümana artık yetkili kişiler tarafından ulaşılabilmesi sağlanır.Qdms ana giriş ekranından Dağıtım matrisindeki kullanıcının adı ve parola bilgisi yazılarak Qdms local adresine giriş yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_556.png)

Açılan  kullanıcının “Bekleyen İşlerim” sayfasında “Okunması gereken Dokümanlar listesi ” olarak  iş olarak görev düşer. İlgili görevdeki doküman kodu alanındaki doküman kodu linki tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_557.png)

Açılan Doküman Görme ekranından doküman bilgisayara indirilerek görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_558.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_559.png)

Diğer dillerde dokümanın yüklü  ise ilgili dil seçeneği seçilerek dokümanın diğer dillerde indirilmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_560.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref106]:Dokümanın türkçe ve diğer dillerde yükle dil seçeneklerinde indirilip, görüntülenmesi sağlanır.

![ref107]

![ref108]:Dokümanla ilgili anket soruları görüntülenerak cevaplama işlemi yapılır. Doküman Yönetimi parametrelerinde 81 numaralı “Dokumanda Anket kulakçığı kullanılacak mı? (E/H)” parametresi parametre değeri “Evet” seçilerek parametre aktif edilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_564.png)

Parametre aktif edildikten sonra Doküman Hazırlama/Revize ekranında Anket sekmesi görüntülenir.  Doküman Hazırlama/Revizyon ekranında Diğer Bilgiler sekmesinde  Anket Kullanılacak alanı ile ilgili check box işaretlerek Anket sekmesi aktif edilerek  Dokümanla ilgili anket soruları tanımlama işlemi yapıldıktan sonra Dağıtım sekmesinde kullanıcılarda Anket alanı ile ilgili check box işaretli olan kullanıcılara anket doldurma görevi atanır.

Anket doldurma görevinde ankette başarı yüzdesi Doküman Yönetimi parametrelerinden 82 numaralı “Anket Başarı Yüzdesi(Sadece 81 numaralı parametre Evet olduğunda geçerlidir.)” parametre değerine tanımlı değere göre belirlenir. Tanımladığımız ankete bu parametreden bir başarı yüzdesi tanımlayıp doküman ile ilgili ne kadar bilgili olunup, olunmadığını buradan anlayabiliriz.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_565.png)

![ref109]: Kontrollü kopya talep etmek için kullanılır.

![ref110]:Doküman üzerinde revizyon işlemi başlatılır.

![ref111]:Doküman ilgili kişiler ilgili olup, olmamasını belirlenir. Parametreye bağlı olarak görüntülenen bir alandır. Doküman Yönetimi parametrelerinden 335 numaralı “Doküman okundu görevinde benimle ilgili değil seçeneği kullanılsın mı?” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. 

![ref112]

Parametre aktif edildikten sonra Doküman görme ekranında  “Benimle İlgili Değil”  butonu görüntülenir.Yayınlanma işlemi tamamlanmış Dokümanda  ilgisi olmayan kullanıcıların ilgili butonu tıklanıldığında Doküman benimle ilgili değil bilgisi hazırlayan/revize eden kişiye mail olarak iletilmesi sağlanır.

Doküman Yönetimi Modülünde parametrelerinde 336 numaralı “Doküman benimle ilgili değil bildirimleri için kullanılacak rol kodu” parametre değerine tanımlı rol koduna benimle ilgili değil bildirimleri gider.

![ref113]

Rol kodunda gidecek olan Doküman benimle ilgili değil bildirimleri için kullanılacak mesaj gövdesi kodu 337 numaralı “Doküman benimle ilgili değil bildirimleri için kullanılacak mesaj gövdesi kodu “ parametresinde parametre değerine tanımlanır.

![ref114]

![ref115]:Dokümanla ilgili iptal işlemi  başlatılması sağlanır.Doküman İptal ekranı açılır. Açılan ekranda “İptal Nedeni” nedeni bilgisi yazılarak ![ref116] butonu tıklanarak onay matrisinde bulunan onaycılara iptal onayına gönderilir.

![ref117]: Dokümanı yazdırmak için kullanılır.

![ref118]: Dokümanın kapak bilgilerini yazdırmak için kullanılır.

![ref108]  butonu tıklanarak anket ilgili anket soruları cevaplama işlemi yapılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_576.png)

Açılan Anket soruları kullanıcı tarafında cevaplanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_577.png)

Kullanıcı tarafından Anket soruları cevaplama işleminden sonra ekranın sol üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_578.png) butonu tıklanarak anket doldurma kayıt işlemi yapılır. Doldurulan anket ile ilgili sonuçların  görüntülenmesi işlemi için  Doküman Yönetim Modülü raporlarından Doküman İzleme Raporunda görüntülenir.



Doküman için Dağıtım matrisinde “Önemli” alanı ile ilgili seçenekle ilgili check box işaretli olan kullanıcılarının “**Bekleyen İşlerim**” sayfasında doküman yayınlandıktan sonra “**Okunması Gereken Önemli Dokümanlar Listesi**” işi olarak görev düşer.  Qdms ana giriş ekranından ilgili  kullanıcının Kullanıcı adı ve parola bilgisi ile Qdms local adresine  giriş yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_579.png)

Kullanıcının “Bekleyen İşlerim” sayfasında “Okunması Gereken Önemli Dokümanlar Listesi” görevindeki doküman kodu alanındaki link tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_580.png)

Doküman Görme ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_581.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref106]:Dokümanın diğer dillerde yükle dil seçeneklerinde indirilip, görüntülenmesi sağlanır.

![ref107]

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_582.png):Dokümanın okudu statüsüne getirilme işlemi yapılır. Bu buton tıklanıldığında sistem tarafından “Dokuman Başarıyla okundu statüsüne getirilmiştir”  mesajı verilir. Parametreye bağlı olarak görüntülenen bir butondur. Doküman Yönetimi parametrelerinden  106 numaralı “Dokuman görmede okudum onayı alınsın mı? Parametresinin parametre değeri “Evet” seçilerek parametre “Aktif” edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_583.png)

Parametre aktif edildikten sonra Doküman görme ekranında yayınlanmış dokümanlarda  bu buton tıklanarak dokümanın “okundu” statüsüne getirilme işlemi yapılır.

![ref108]:Dokümanla ilgili anket soruları görüntülenerak cevaplama işlemi yapılır.

![ref109]: Kontrollü kopya talep etmek için kullanılır.

![ref110]:Doküman üzerinde revizyon işlemi başlatılır.

![ref111]:Doküman ilgili kişiler ilgili olup, olmamasını belirlenir. Parametreye bağlı olarak görüntülenen bir alandır. Doküman Yönetimi parametrelerinden 335 numaralı “Doküman okundu görevinde benimle ilgili değil seçeneği kullanılsın mı?” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. 

![ref112]

Parametre aktif edildikten sonra Doküman görme ekranında  “Benimle İlgili Değil”  butonu görüntülenir.Yayınlanma işlemi tamamlanmış Dokümanda  ilgilisi olmayan kullanıcıların İlgili buton tıklanıldığında Doküman benimle ilgili değil bilgisi hazırlayan/revize edene mail olarak iletilmesi sağlanır.

Doküman Yönetimi Modülünde parametrelerinde 336 numaralı “Doküman benimle ilgili değil bildirimleri için kullanılacak rol kodu” parametre değerine tanımlı rol koduna benimle ilgili değil bildirimleri gider.

![ref113]

Rol kodunda gidecek olan Doküman benimle ilgili değil bildirimleri için kullanılacak mesaj gövdesi kodu 337 numaralı “Doküman benimle ilgili değil bildirimleri için kullanılacak mesaj gövdesi kodu “ parametresine tanımlanır.

![ref114]

![ref115]:Dokümanla ilgili iptal işlemi  başlatılması sağlanır.Doküman İptal ekranı açılır. Açılan ekranda “İptal Nedeni” nedeni bilgisi yazılarak ![ref116] butonu tıklanarak onay matrisinde bulunan onaycılara iptal onayına gönderilir.

![ref117]: Dokümanı yazdırmak için kullanılır.

![ref118]: Dokümanın kapak bilgilerini yazdırmak için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_584.png)

Doküman Görme ekranından ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_585.png) butonu tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_586.png)

Sistem tarafından “Dokuman Başarıyla okundu statüsüne getirilmiştir” mesajı verilir. Doküman “okundu” statüsüne getirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_587.png)
#### **6.3.5.Doküman Görüntüleme**
**Menü Adı**: Entegre Yönetim Sistemi/ Doküman işlemleri/ Doküman Görme 

Yayınlanmış olan bütün dokümanların görüntülendiği menüdür. Doküman görüntüleme yetkisi olan personeller/ kullanıcı grupları ilgili dokümanı görüntüleyebilirler. Doküman Görme menüsü açıldığı zaman, sol tarafta klasör ağacı görüntülenir. Doküman görme ekranında Doküman listesi, Doküman Arama ve Hızlı arama sekmeleri olmak üzere üç sekme karşımıza çıkar. Doküman Arama ve Hızlı Arama sekmelerinde arama kriterlerine göre filtreleme işlemi yapılarak Doküman listesinde ise bu arama kriterlerine göre yapılan filtreleme işlemlerine göre ilgili kayıtların listelenmesi sağlanır.Doküman Arama sekmesinde arama kriterlerinin detaylı bir şekilde filtreleme işlemi yapılır. Hızlı Arama sekmesinde ise sadece Doküman Kodu, Doküman Adı ve Doküman Tipi gibi alanlara göre arama kriterleri işlemleri yapılarak hızlı bir şekilde  arama işlemi yapılır.Doküman Yönetimi Modülü parametrelerinde 140 numaraları “Doküman görme sayfasında ilk açılacak kulakçık?(L(Liste)/A(Arama)/H(Hızlı Arama))” parametre değerine tanımlı değere göre doküman görme ekranında ilk açılacak sekme belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_588.png)

Parametrede liste değerinin karşığılı olan “L” değeri tanımlı olduğundan doküman görme sayfasından liste sekmesi ilk açılacak kulakçık olarak görüntülenir. Kullanıcı istediği doğrultusunda doküman görme ekranından ilk açılacak kulakçığı ayarlama işlemini yapabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_589.png)

**Ekranda bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_590.png):Doküman görüntüleme işlemi yapılır.

![ref119]:Doküman Hazırlama Talep İşlemi yapılır. Parametreye bağlı olarak görüntülenen bir butondur. Doküman Yönetimi Modülü parametrelerine 229 numaralı “Dokuman Hazırlama Talebi Yap fonksiyonu kullanılacak mı?” parametresinin değeri “Evet” seçilerek parametre aktif edilir. ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_592.png)Parametre aktif edildikten sonra Doküman görme ekranında ![ref119] butonu  görüntülenir ve seçili klasörde  doküman hazırlama talebi işlemi yapılır.

![ref120]:Favorilere favori sayfası ekleme işlemi yapılır. Parametre bağlı olarak görüntülenen bir butondur.Doküman Yönetimi parametrelerinde 131 numaralı “ Doküman görmede klasör bazında favorilere ekleme kullanılsın mı?” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_594.png)

Parametre aktif edildikten sonra Doküman Görme ekranında ![ref120] (Favorilere Ekle) butonu görüntülenir ve Favorilere favori ekleme işlemi yapılır.

Dokümanların görüntüleneceği klasör seçilir. İlgili klasör içerisindeki bulunan tüm dokümanlar listelenir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_595.png)

Görüntülenmek istenilen doküman seçilerek, doküman koduna tıklanır ve doküman açılır. Doküman ile ilgili bilgilere ulaşılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_596.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref106]:Dokümanın Türkçe ve  diğer dillerde yükle dil seçeneklerinde indirilip, görüntülenmesi sağlanır.

![ref107]

![ref109]: Kontrollü kopya talep etmek için kullanılır.

![ref110]:Doküman üzerinde revizyon işlemi başlatılır.

![ref115]:Dokümanla ilgili iptal işlemi  başlatılması sağlanır.Doküman İptal ekranı açılır. Açılan ekranda “İptal Nedeni” nedeni bilgisi yazılarak ![ref116] butonu tıklanarak onay matrisinde bulunan onaycılara iptal onayına gönderilir.

![ref117]: Dokümanı yazdırmak için kullanılır.

![ref118]: Dokümanın kapak bilgilerini yazdırmak için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_597.png) Önceki ekrana geri dönülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_598.png)

Eski revizyonların takibi için **“Revizyon Bilgileri” sekmesi** açılır. Dokümana ait önceki revizyon bilgilerinin hepsi liste şeklinde görüntülenir. Eğer yetki matrisinde kullanıcıya “eski revizyonları görme yetkisi” verildiyse, kullanıcı eski revizyonlara ait dokümanları görüntüleyebilir. İlgili revizyon numarasının üzerinde iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_599.png)butonuna tıklanarak eski revizyon dokümanı açılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_600.png)

**“Revizyon Talebi”** sekmesinde , doküman üzerinde revizyon yetkisi olmayan kullanıcılar için revizyon talebi etme işlemi gerçekleştirilir. Doküman Yönetimi Modülü parametrelerinde 150 numaraları  “Doküman modülünde Revizyon Talebi sekmesi kullanılacak mı?” parametresinde parametre değeri “Evet” seçilerek parametre aktif edilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_601.png)

Parametre aktif edildikten sonra Doküman Hazırlama/Revizyon ekranlarında Revizyon Talebi sekmesi görüntülenir.

Doküman Yönetimi Modülü parametrelerinden 91 numaralı “Revizyon Talepleri kimlere gönderilsin(Revize Eden:R,Sorumlu:S,Yönetici:Y) “ parametresinde parametre değeri tanımlı kişiye revizyon telepleri gönderilir.  Parametrede parametre değerine Revize Eden , Sorumlu ve Yönetici olarak karşılıkları değerler yazılarak tanımlama yapılmıştır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_602.png)

Doküman Yönetimi Modülü parametrelerinde 167 numaralı “Onay açıklaması için revizyon talebi oluşturulsun mu?” parametresi parametre değeri “Evet” seçilerek parametre aktif edilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_603.png)

Parametre aktif edildikten sonra Doküman için onay açıklaması için revizyon talebi oluşturulma işlemi yapılır. Onay açıklama bilgisi Revizyon Talebi olarak sistem tarafında otomatik olarak revizyon talebi olarak tanımlı olarak Revizyon Talebi sekmesine gelir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_604.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref121]:Yeni bir revizyon talebi tanımlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_606.png):Listede seçili revizyon talebi bilgisi üzerinde değilişiklik/güncelleme/düzenleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_607.png):Listede seçili revizyon talebi bilgi silinir.  Silme işlemi parametreye bağlı olarak yapılmaktadır. Doküman Yönetimi parametrelerinde “Revizyon talebini silmeye yetkili kullanıcılar: Yönetici(Y), Doküman Sahibi(S).Birden fazla ise virgül ile ayırarak yazınız.” parametresine tanımlı kullanıcılara göre silme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_608.png)

Parametrede tanımlı değere göre revizyon talebini silmeye yetkili kullanıcılar :Yönetici ve Doküman Sahibi olarak parametre göre tanımlanmıştır. Tanımlı değerlerin karşılığı olan değer parametre değerine yazılmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_609.png):Listede seçili talep bilgisi görüntüleme işlemi yapılarak okunması yapılır.

Doküman revizyon Talebi sekmesinde yeni bir revizyon talebi eklemek için ![ref121] butonu tıklanarak  Doküman Revizyon Talebi ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_610.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Talep:** Doküman Revizyon Talep ekranında talep açıklama bilgisinin yazıldığı alandır.

Doküman Revizyon Talebi ekranında tanımlanan talep açıklama bilgisi yazılır. Talep açıklama ile ilgili varsa ek dosya ekleme işlemi yapılır. Gerekli alanlar ilgili bilgiler yazıldıktan sonra ekranın sol üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_611.png)  butonu tıklanarak talep kayıt işleminde onaydaki kişiye onaya gönderilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_612.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_613.png)

Doküman Revizyon Talepleri  Bekleyen işlemlerinde 91 parametrede parametre değerine tanımlı olan Revize Eden , Sorumlu ve Yönetici  göre “**Doküman Revizyon Talepleri**” işi olarak görev düşer. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_614.png)

İlgili görevdeki Doküman Kodu alanında link tıklanarak Revizyon Talebi  Başlar-Redet ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_615.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref122]:Doküman görüntüleme işlemi yapılır.

![ref123]: Revizyon talebi kabul edilip revizyon başlatılır.

![ref124]:Revizyon talebi ret nedeni yazılarak ret işlemi yapılır.

![ref125]: Revizyon talebi başka bir kullanıcıya yönlendirme işlemi yapılır.

Revizyon Talebi  Başlar-Reddet ekranında ![ref122] butonu tıklanarak  doküman görüntüleme işlemi yapılır

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_620.png)

Revizyon Talebi  Başlar-Reddet ekranında  istenirse  Red nedeni yazılarak ![ref126]butonu tıklanarak Revizyon Talebi ret etme işlemi  yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_622.png)

Revizyon Talebi  Başlar-Reddet ekranında ![ref125] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_623.png)

Revizyon Talebi Yönlendirme ekranı açılır. ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_624.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Yönlendirilecek:** Revizyon Talebi Yönlendirme ekranında ![ref127] butonu tıklanarak açılan sistemde tanımlı personel listesinde talebinin yönlendirme işlemi yapılacak kişi bilgisi seçildiği alandır.

**Notlar:** Revizyon Talebi Yönlendirme ekranında revizyon talep yönlendirme işlemi ile varsa not bilgisi yazıldığı alandır.

Revizyon Talebi Yönlendirme ekranında ![ref127] butonu tıklanarak açılan sistemde tanımlı personel listesinde talebinin yönlendirme işlemi yapılacak kişi bilgisi seçilir . Varsa Talebi yönlendirme işlemi ile ilgili not bilgisi yazılır. Gerekli alanlar ilgili bilgiler girildikren sonra ekranın sol üst köşesindeki![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_626.png)  butonu tıklanarak Revizyon Talebi Yönlendirme işlemi yapılır.

Revizyon Talebi Başlar- Reddet ekranından ![ref123] butonu tıklanarak  Revizyon talebinde kapsamından Revizyon işlemi başlatılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_627.png)

Sistem tarafından “Doküman revizyon işlemlerini başlatmak istediğinizden emin misiniz?” mesajından “Tamam” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_628.png)

Sistem tarafından “Doküman başarıyla kaydedildi. Revizyon işlemleri başlamıştır.” Mesajı verilerek revizyon işlemi başladığı belirtilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_629.png)

Açılan Doküman Revizyon ekranından  revizyon işleminin “Bu revizyon , revizyon talebi ile başlatılmıştır “ bilgisi verilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_630.png)

Revizyon numarası sistem tarafından otomatik olarak verilmektedir. (Eğer klasörde manuel olarak tanımlandıysa, revizyon numarası bilgisi girilir.)

Doküman bilgileri, matris sekmeleri ve tüm doküman sekmeleri  üzerinde revizyon kapsamında istenilen değişiklikler yapılabilir. **“Revizyon Bilgileri”** sekmesinde revizyon nedeni girilir. Revizyonda yapılanlar tanımlanır. Bir revizyon talebinden sebep revizyon başlatıldıysa talep bilgisi seçilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_631.png)

Doküman sekmesine gelinerek ![ref128] (Dosya Görüntüle) butonu ile bilgisayara indirilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_633.png)

Doküman üzerinde revizyon işlemleri gerçekleştirildikten sonra ![ref129] (Dosya Ekle) butonuyla dokümanın sisteme yüklenme işlemi gerçekleştirilir. Sistemden indirilen dokümanın adı ile sisteme yüklenen dokümanın adının aynı olması gerekmektedir. Aksi takdirde sistem hata vermektedir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_635.png)

Sistemden indirilen dokümanın adı ile sisteme yüklenen dokümanın adının aynı olmadığı zaman sistem hata uyarısı verir. Sistem tarafından “Eklediğiniz dosya ismi doküman kodu ile uyuşmuyor.” mesajı verilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_636.png)


![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_637.png)

Örneğin; sistemden indirilen doküman adı 2024-PR.003\_1.docx olsun. Revize edilen dokümanın adı da 2024-PR.003.doc  olan Doküman Yönetimi Kullanıcı yardım Dokümanı olsun. Revize edilen doküman bu şekilde sisteme yüklenmek istenildiği zaman sistem tarafından hata uyarısı verilir. Revize edilen dokümanın adı, sistemden indirilen adı neyse o olacak şekilde değiştirilir, yani 2024-PR.003\_1.docx  şeklinde yapılarak  ve sisteme yüklenir. Sistemde indirilen dokümanın adı kısmındaki \_1  kısmı dokümanın 1. revizyonda olduğu bilgisinin göstermektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_638.png)

Doküman Revizyon ekranında Doküman sekmesinde ![ref130] (Dosya Ekle) butonu tıklanarak Revize edilen dokümanın adı, sistemden indirilen adı neyse o olacak şekilde değiştirilerek sisteme yükleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_640.png)

Dosya Ekle ekranında Gözat butonu tıklanılarak açılan ekranda  sisteme yüklenecek dokümanın seçim işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_641.png)

Doküman Revizyon ekranında Doküman sekmesinde “Dosya Başarıyla aktarılmıştır” mesajı gelir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_642.png)

Doküman Bilgileri sekmesi tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_643.png)

Doküman Revizyon ekranında ![ref131]  butonuna tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_645.png)

Sistem tarafından “Göndermek istediğinize emin misiniz?” mesajından “Tamam” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_646.png)

Sistemde görüş matrisinde  varsa görüşe görüş yoksa ön kontrolle / kontrol/ onay süreçlerine iletilir. Doküman hazırlama süreçlerindeki akış ile aynı aşamalar gerçekleştirilir. Revizyon İşlemi yapılan doküman ön kontrolcünün “Bekleyen işlerim” sayfasında “Ön Kontrol Bekleyen Dokümanlar” işi olarak görev düşer.  

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_647.png)

Doküman Revizyon işleminde Ön kontrol aşamasında başlanarak, kontrol ve onay aşamaları yapılarak dokümanın revizyon işlemi tamamlanır.

Revizyon İşlemi tamamlanmış klasör içerisindeki doküman görüntülenrek revizyon numarası 1 artarak 1. Revizyonda olduğu  görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_648.png)

Doküman Görme ekranından revizyon işlemi yapılan dokümanın kodu tıklanılarak dokümanın görüntüleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_649.png)

Görüntülenen dokümanında  Son revizyon nedeni bilgisi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_650.png)

Görüntülenen dokümanda Revizyon Bilgileri sekmesi tıklanarak Dokümanda yapılan revizyonlar görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_651.png)

Revizyon Bilgileri sekmesinde dokümanın eski revizyonları ile ilgili bilgilere ulaşılır ve ![ref132]butonu ile eski revizyonlarının görüntüleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_653.png)

Revizyon Bilgileri sekmesinde dokümanın 1. Revizyonu seçilerek  ![ref132] butonu tıklanarak görüntüleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_654.png)

Doküman Görme ekranındaki “**Doküman Arama”** sekmesinde, dokümanlar arasında istenen kriterlere göre filtreleme yapılarak arama işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_655.png)

İlgili alanlar doldurulduktan sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_656.png) (Ara) butonuna işlem gerçekleştirilir. Hızlı Arama özelliği ile doküman kodu, doküman adı, doküman tipine göre arama yapılabilmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_657.png)

**Doküman Hazırlama Talebi;**

Doküman Görme ekranında 229 numaralı “	Dokuman Hazırlama Talebi Yap fonksiyonu kullanılacak mı? parametreye bağlı olarak  görüntülenen ![ref133]butonu  ile seçili klasörde doküman hazırlama talebinde bulunma işlemi yapabilir.Doküman Hazırlama Talebi işlemin ilgili klasörde yapılması için Klasör Ayarları sekmesinde Doküman Hazırlama Talebi Gidecek Grup alanında doküman hazırlama Talebi gidecek grubun tanımlı olması gerekmektedir. Klasörde Klasör ayarları grubu tanımlı olmadığında Doküman hazırlama Talebi kayıt işlemini gerçekleştirmez. Sistem tarafından “Hazırlama Talebininin gideceği grup klasör üzerinden ayarlanmamıştır. Klasör üzerinde gerekli düzenlemeleri yapınız.”uyarı mesajı verilir.Doküman Hazırlama Talebi  bulunma işleminde  Doküman Yönetimi Modülü parametrelerinde 62 numaralı “Doküman Hazırlama Talebine Cevap Suresi” parametresinde doküman hazırlama Talebine cevap süresine ayarlama işleminide yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_659.png)

Parametrede ayarlanan süre bilgisine göre doküman hazırlama talebine cevap verilmesi sağlanır.

Doküman Görme ekranından  doküman hazırlama talebi işlemi için  klasör seçili iken ![ref133] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_660.png)

Dokuman Hazırlama Talebi ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_661.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref134]:Kayıt işlemi yapılır.

![ref135]:Dosya ekleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_664.png):Listede eklenen dosyayı silme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_665.png):Listede eklenen dosyanın görüntüleme işlemi yapılır.

**Açılan ekranda ilgili alanlar tanımlanır:**

**Talep:** Doküman Hazırlama Talep ekranında hazırlanması talep edilen dokümanın açıklaması bilgisi yazıldığı alandır.

**Talep Gidecek Kullanıcı:** Doküman Hazırlama Talep ekranında  doküman hazırlama talebinin gidecek kullanıcının ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_666.png) butonu tıklanarak açılanan Klasörde Klasör Ayarları sekmesinde Doküman Hazırlama Talebi Gidecek Grup alanında tanımlı grup üyelerinden seçildiği alandır. Seçilen kullanıcının Klasörde Klasör Ayarları sekmesinde Doküman Hazırlama Talebi Gidecek Grup alanında tanımlı grup üyesi olması gerekmektedir.Parametre bağlı olarak görüntülenen bir alandır. Doküman Yönetimi parametrelerinde 271 numaralı “Doküman Hazırlama Talebi Yaparken kullanıcı seçilebilsin mi?” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_667.png)

Parametre aktif edildikten sonra Doküman Hazırlama Talep ekranında Talep Gidecek Kullanıcı alanı görüntülenir ve  doküman hazırlama talep gidecek kullanıcı seçim işlemi yapılır.

Doküman Hazırlama Talebi ekranında ![ref135] butonu tıklanarak doküman hazırlama talebi ile ilgili ek dosya yükleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_668.png)

Dosya Ekle ekranında “Gözat” ekranın doküman hazırlama talebi eklenecek ek dosyanın seçilme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_669.png)

Dosya seçilme işleminde sonra Doküman Hazırlama Talebi ekranında yükleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_670.png)

Doküman Hazırlama Talebi ekranında gerekli alanlar ilgili bilgiler girildikten sonra ekranın sol üst köşesindeki ![ref134]  butonu tıklanılarak doküman Hazırlama Talebi kayıt işlemi yapılır. 

Sistem tarafından Kayıt işleminden sonra ilgili kullanıcıya doküman hazırlama Talebi gönderildiği bilgisi verilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_671.png)

Doküman Hazırlama Talepleri kayıt işleminde sonra ilgili kullanıcının “**Bekleyen İşlerim**” sayfasında “**Doküman Hazırlama Talepleri**” işi olarak görev düşer.

Doküman Yönetim Modülü parametrelerinden 270 numaralı “Doküman Modülünde  Doküman Hazırlama Talepleri Kimlere Gönderilsin?” parametresinde parametre değerine tanımlı kişiye gönderilme işlemi yapılır.Parametre değerine Yönetici=Y, Kullanıcı=K değerleri girilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_672.png)

Parametrede parametre değerinde Kullanıcı olarak tanımlandığı için kullanıcıya Doküman Hazırlama Talepleri gönderilir.

**Favorilere Ekle İşlemi;**

Doküman Görme ekranında  131 parametreye bağlı görüntülenen ![ref136] butonu tıklanarak Doküman Görme ekranında görüntülen ekranın Favorilerim sayfasına ekleme işlemi yapılır.Doküman Görme ekranında görüntülenen ekranı açıkken ![ref136] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_674.png)

Açılan Favori Ekle ekranında Açıklama alanında Doküman Görme ekranında açık olan ekranın favori sayfası olarak verilecek adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_675.png)

Favori Ekle ekranında gerekli alanlar ilgili bilgiler  yazıldıktan sonra ekranın sol üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_676.png) butonu tıklanarak favori sayfası olarak kayıt işlemi yapılır.Doküman görme ekranında favori sayfası olarak eklenen sayfayı görüntülemek için Qdms  kullanıcı adının bulunduğu kısımda ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_677.png)(Favorilerim) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_678.png)

Favorilerim ekranında doküman görme ekranında favori olarak eklenen favori sayfası link tıklanarak favori olarak kaydedilen sayfanın açılması sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_679.png)

Doküman Görme ekranından Klasör içerisindeki Doküman kodu alanındaki link tıklanarak doküman görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_680.png)

Açılan Doküman ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_681.png)(Doküman Yazdır) butonu tıklanılarak Doküman Yazdırma işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_682.png)

**Ekranda bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_683.png):Doküman yazdırma işlemi yapılır.

![ref137]:Kontrollü kopya yazdırma işlemi yapılır. Parametreye bağlı olarak görüntülenen bir butondur. Doküman Yönetimi modülü parametrelerinde 87 numaralı “Kontrollü Kopya Yazdır butonu kullanılacak mı ?” parametresi parametre değeri “Evet” seçilerek parametre aktif edilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_685.png)

Parametre aktif edildikten doküman görme ekranında Kontrollü kopya yazdır butonu  görüntülenir ve  kontrollü kopya yazdırma işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_686.png):Dokümanda kapak yazdırma işlemi yapılır.

Açılan ekrandan ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_687.png)(Yazdır) butonu tıklanarak Dokümanı yazdırılma işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_688.png)

**Kontrol Kopya Yazdırma;**

Doküman Görme ekranında Doküman Yönetimi Modülü parametrelerinde 87 numaralı parametreye bağlı olarak görüntülenen butona göre dokümanlarda kontrollü kopya alma işlemi yapılır.Doküman Yönetimi modülünde  parametrelerinden 10 numaralı “Kontrollü kopyalara basılacak label” parametresine göre kontrollü kopya basılacağı zaman alınan çıktıda nasıl bir yazı ile çıktı alınması  parametre değerine yazılan yazı ile belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_689.png)

Parametrede “KONTROLLÜ KOPYADIR..” parametrede tanımlı yazıya göre kontrollü kopyasında çıktısında görüntülenir.

Doküman Görme ekranından Kontrollü Kopya yazdırma işlemi için ![ref137] (Kontrollü Kopya Yazdır) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_690.png)

Kontrollü Kopya yazdır ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_691.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Doküman Kodu:** Sistem tarafında doküman kodunun verildiği alandır.

**Doküman Adı:** Sisrem tarafından doküman adının verildiği alandır.

**Kopya Sayısı:** Kontrollü kopya sayısının alacağı sayısal değerinin bilgisinin belirlendiği alandır.

**Açıklama:** Kontrollu kopyanın neden alındığına dair açıklama bilgisinin yazıldığı alandır. Açıklama alanı parametrede zorunluğunun getirilmesinin ayarı yapılmaktadır. Doküman Yönetimi Modülü parametrelerinden 133 numaralı “Kontrollü Kopya Yazdırma Sayfasında Yazdırma Nedeni Zorunlu Olsun Mu?(E/H) parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. Parametre aktif edildikten sonra kontrollü kopya yazdırma sayfasından yazdırma nedeni zorunlu olur. Parametre parametre değeri “Hayır” ise böyle bir zorunluluğuna gerek kalmaz.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_692.png)

Gerekli alanlari  ilgili bilgiler girildikten sonra ekranın sol üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_693.png)  butonu tıklanarak Kontrollü kopya yazdırma işlemi yapılır.

Doküman Yönetimi modülü parametreleri kapsamında  89 numaralı “Kontrollü Kopya yazdırmada güvenlik yapılandırılsın mı” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_694.png)

Parametre aktif edildiğinde Kontrollü kopya yazdırma esnasında güvenlik yapılandırılsın dersek ilgili kişi dokümanı bilgisayarına indirebilir ancak doküman üzerinde hiç bir şekilde değişiklik yapma yetkisine sahip olmaz.

**Kapak Yazdırma İşlemi;**

Doküman Görme ekranında  doküman modülünde kapak yazdırma işlemi ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_695.png)(Kapak Yazdır)  buton tıklanarak yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_696.png)

Kullanıcılar istedikleri formatta kapak  yazdırma işlemi yapmak için Sistem Altyapı Tanımları/BSAT/ Konfigürasyon Ayarları/Rapor Formatları Düzenleme menüsünde istenilen formattaki doküman kapak formatını yükleme işlemi yapabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_697.png)

Doküman Yönetimi Modülü parametrelerinde 11 numaralı “Kontrolsüz kopyalara basılacak label” parametresinde parametre değerinde tanımlı değere göre Kontrolsüz kopya basılacağı zaman çıktı alınırken, nasıl bir yazı ile çıktı alınabileceğinin belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_698.png)
#### **6.2.6.Doküman Revizyon**
**Menü Adı**: Entegre Yönetim Sistemi/ Doküman İşlemleri/ Doküman Revizyon

Dokümanların Revizyon işlemlerinin yapıldığı menüdür.  Dokümanları revize etmek için iki yöntem bulunmaktadır. Bunlar;

**1.Seçenek;**

Doküman revizyon işlemi yapmak için öncelikle Entegre Yönetim Sistemi/Doküman İşlemleri/Doküman Revizyon menüsü tıklanılır.Açılan ekranda revizyon işleminin yapılacak dokümanın bulunduğu klasör seçilir ve ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_699.png) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_700.png)

Açılan Doküman Revizyon - Doküman Belirleme ekranında Revizyon işlemi yapılacak doküman seçilir ve ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_701.png) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_702.png)

Sistem tarafından “Doküman başarıyla kaydedildi. Revizyon işlemleri başlamıştır.” mesajı verilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_703.png)

Doküman Revizyon işleminde Revizyon numarası sistem tarafından otomatik olarak “1” olarak artar. (Eğer klasörde manuel olarak tanımlandıysa, revizyon numarası bilgisi girilir.)

Doküman Revizyon ekranında, Doküman Hazırlama ekranında oluşturulan bilgiler karşımıza çıkar. Bu aşamada dokümanın bilgileri üzerinde istenilen değişiklikler yapılabilir. Doküman bilgileri, matris sekmeleri ve tüm doküman sekmeleri  üzerinde revizyon kapsamında istenilen değişiklikler yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_704.png)

Doküman Revizyon ekranında Revizyon Bilgileri sekmesi tıklanılır. Revizyon Nedeni alanında dokümanda neden revizyon yapılması ile ilgili bilgi yazılır. Revizyonda yapılanlar alanında ise dokümanda revizyon işleminde yapılanlar yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_705.png)

Doküman sekmesine gelinerek ![ref128] (Dosya Görüntüle) butonu ile bilgisayara indirilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_706.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_707.png)

Doküman üzerinde revizyon işlemleri gerçekleştirildikten sonra ![ref129] (Dosya Ekle) butonuyla dokümanın sisteme yüklenme işlemi gerçekleştirilir. Sistemden indirilen dokümanın adı ile sisteme yüklenen dokümanın adının aynı olması gerekmektedir. Aksi takdirde sistem hata vermektedir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_708.png)

Sistemden indirilen dokümanın adı ile sisteme yüklenen dokümanın adının aynı olmadığı zaman sistem hata uyarısı verir. Sistem tarafından “Eklediğiniz dosya ismi doküman kodu ile uyuşmuyor.” mesajı verilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_709.png)

Örneğin; Sistemden indirilen doküman adı 2024-PR.003\_1.docx olsun. Revize edilen dokümanın adı da 2024-PR.002.doc  Eğitim Planlama Modülü dokümanı olsun. Revize edilen doküman bu şekilde sisteme yüklenmek istenildiği zaman sistem tarafından hata uyarısı verilir. Revize edilen dokümanın adı, sistemden indirilen adı neyse o olacak şekilde değiştirilir, yani 2024-PR.002\_1.docx şeklinde yapılarak  ve sisteme yüklenir. Sistemde indirilen dokümanın adı kısmındaki \_1  kısmı dokümanın 1. revizyonda olduğu bilgisinin  göstermektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_710.png)

Doküman Revizyon ekranında Doküman sekmesinde ![ref130] (Dosya Ekle) butonu tıklanarak Revize edilen dokümanın adı, sistemden indirilen adı neyse o olacak şekilde değiştirilerek sisteme yükleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_711.png)

Dosya Ekle ekranında Gözat butonu tıklanılarak açılan ekranda  sisteme yüklenecek dokümanın seçim işlemi yapılır.,

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_712.png)

Dosya Ekle ekranında Gözat butonu tıklanılarak açılan ekranda  sisteme yüklenecek dokümanın seçim işlemi yapılır.,

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_713.png)

Doküman Revizyon ekranında Doküman sekmesinde “Dosya Başarıyla aktarılmıştır” mesajı gelir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_714.png)

Doküman Bilgileri sekmesi tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_715.png)

Doküman Revizyon ekranında ![ref131]  butonuna tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_716.png)

Sistem tarafından “Göndermek istediğinize emin misiniz?” mesajından “Tamam” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_717.png)

Sistemde görüş matrisinde  varsa görüşe görüş yoksa / kontrol/ onay süreçlerine iletilir. Doküman hazırlama süreçlerindeki akış ile aynı aşamalar gerçekleştirilir. Revizyon İşlemi yapılan doküman kontrolcünün “Bekleyen işlerim” sayfasında “Kontrol Bekleyen Dokümanlar” işi olarak görev düşer.   Kontrol aşamasında başlanarak  ve onay aşamaları yapılarak dokümanın revizyon işlemi tamamlanır.

**Revizyon İşleminde Kontrol aşaması;**

Revizyon işleminde kontrole gönderilen doküman, kontrolcünün “**Bekleyen İşlerim**” menüsünde “**Kontrol Bekleyen Dokümanlar**”  işi olarak görev düşer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_718.png)

Kontrolcü ilgili görevdeki doküman kodu alanındaki link tıklanarak doküman bilgileri ekranı görüntüler. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_719.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref91]:Doküman kayıt işlemi yapılır

![ref92]:Kaydet ve devam etme işlemi yapılır. Parametreye bağlı olarak görüntülenen bir butondur.Doküman Yönetimi parametrelerinde 331 numaralı “Doküman hazırlama sayfasında kaydet ve devam et butonu kullanılsın mı?” parametresi parametre değeri “Evet” seçilerek parametre aktif edilir.

![ref93]

Parametre aktif edildikten sonra Doküman Hazırlama aşamasında  ![ref92]butonu görüntülenir.

![ref94]:Doküman onaylama işlemi yapılır.

![ref95]:Doküman red nedeni yazılarak ret etme işlemi yapılır.

Bu arada doküman Kontrol aşamasında Doküman Sekmesi tıklayarak ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_720.png)(Dosya Görüntüle) butonu ile doküman görüntüleyerek doküman üzerinde değişiklik ve düzenleme işlemi yapar. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_721.png)

Ek dosya sekmesinde Dokümanla ilgili görüşleri içeren bir ek dosya yükleme işlemini  yapabilir. Doküman revizyon işleminde kontrol aşamasında dokümanı ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_722.png) butonu tıklayarak doküman hazırlayan kişiye gönderme işlemi yapar. Reddetme aşamasında dokümanın red nedeninin girilmesi zorunludur.

Doküman Bilgileri sekmesi tıklanılır.Dokümanda revizyon işleminde herhangi bir problem yoksa ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_723.png) butonuna basılarak doküman onay matrisindeki sıralamaya göre onaya gönderilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_724.png)

Sistem tarafından “Göndermek istediğinize emin misiniz?” mesajından “Tamam” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_725.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_726.png)

Doküman revizyon işlemi aşamasındaki kontrol işleminde tamamlandıktan sonra sistem tarafından  onaydaki kişiye onaya gönderildiği bilgisi verilir.

**Doküman Revizyon İşleminde Onay aşaması;**

Doküman revizyon işleminde  onay matrisinde yer alan kullanıcılar seviyelerine göre sırasıyla onay işlemini gerçekleştireceklerdir. Onaycıların  “**Bekleyen İşlerim**” menüsünde  “**Onay Bekleyen Dokümanlar”** işi olarak görev düşer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_727.png)

Onaydaki kişi ilgili görevdeki doküman kodu alanındaki link tıklayarak Doküman Onaylama ekranı görüntüler. Onaydaki kişi  doküman bilgileri üzerinde değişiklik yapmamaz. Bu aşamada sadece doküman görüntülenebilir ve onay/ red işlemleri gerçekleştirir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_728.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref94]:Doküman onaylama işlemi yapılır.

![ref95]:Doküman red nedeni yazılarak ret etme işlemi yapılır.

Doküman kulakçığında yer alan  ![ref101] (dosya görüntüle)  butonu ile doküman açılır.  Şablon kullanılarak hazırlanmış dokümanlarda, ![ref102] (yayınlanmış halini göster)  butonu ile hazırlama şablonuyla oluşturulan dokümanın görüntülenmesi sağlanır. Doküman Bilgileri sekmesi tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_729.png)

Doküman Bilgileri sekmesi tıklanılır. Doküman revizyon işleminde  onaycı tarafından onay açıklaması bilgisi yazılarak ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_730.png) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_731.png)

Sistem tarafından “Göndermek istediğinizden emin misiniz? “mesajında “Tamam” butonu  tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_732.png)

Sistem tarafından revizyon işlemi aşamasında dokümanın onaylama işleminde sonra “Doküman yayınlanıp kullanıma açılmıştır” mesajı verilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_733.png)

Doküman Revizyon işleminde  görüş varsa görüş , görüş yoksa onay ve kontrol aşamaları aynı şekilde doküman  hazırlama işlemindeki şekildedir. Revizyon işlemi yapılan dokümanın onay ve kontrol aşamasında sonra dağıtım matrisindeki tanımlı kişilerin bekleyen işlerinde “ **Okunması Gereken Doküman Listesi** “ ve  dağıtım matrisinde önemli dokümanlar için önemli alanı ile ilgili check box işaretli ise de “**Okunması Gereken Önemli Dokümanlar  Listesi**” olarak görev düşer.

Qdms Ana giriş ekranında dağıtım matrisindeki kullanıcının adı ve parola bilgisi yazılarak Qdms local adresine giriş yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_734.png)

Qdms’in giriş yapılan kullanıcının “Bekleyen İşlerim” sayfasında “Okunması Gereken Doküman Listesi “işi olarak görev düşer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_735.png)

İlgili görevdeki doküman kodu alanındaki link tıklanarak doküman bilgileri ekranı görüntülenir. Doküman Görme ekranında görüntülenen dokümanın Son Revizyon Nedeni  alanından son revizyon nedeni bilgisi yazıldığı görülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_736.png)

Doküman Bilgileri ekranı tıklanarak açılan ekranda Revizyon Numarası sistem tarafından otomatik olarak “1” olarak geldiği görülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_737.png)

1. **Seçenek;**

Entegre Yönetim Sistemi /Doküman İşlemleri/Doküman Görme menüsü tıklanılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_738.png)

Revizyon işlemi yapılacak dokümanın bulunduğu klasör seçilerek Doküman Listesinde içerisindeki dokümların listelenmesi sağlanır.Doküman Listesinde listelenen revizyon yapılacak dokümanın kodu tıklanarak  revizyon işlemi yapılacak dokümanın bilgileri görüntülenir. Doküman Görme ekranında ilgili dokümanı görüntülerken sayfasın sol üst köşesinde yer alan ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_739.png) butonu tıklanarak  Revizyon işlemine başlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_740.png)

Sistem tarafından “Doküman revizyon işlemlerini başlatmak istediğinizden emin misiniz?” mesajından “Tamam” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_741.png)

Sistem tarafından “Doküman başarıyla kaydedildi. Revizyon işlemleri başlamıştır.” mesajı verilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_742.png)

Her iki seçenekte de “Doküman başarıyla kaydedildi. Revizyon işlemleri başlamıştır.” bilgisi geldikten sonra Revizyon işlemine başlanılır. Doküman Revizyon ekranında, Doküman Hazırlama ekranında oluşturulan bilgiler karşımıza çıkar. Bu aşamada dokümanın bilgileri üzerinde istenilen değişiklikler yapılabilir. Ekranda “Revizyon Bilgileri” kulakçığa gelinerek Revizyon nedeni girilir. Revizyonda yapılanlar girilebilir. Eğer bir Revizyon talebinden geldiyse talep seçilerek belirtilebilir. Revizyon numarası sistem tarafından otomatik olarak verilmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_743.png)

Doküman sekmesine gelinerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_744.png) (Dosya görüntüle) butonu ile doküman revize edilmek üzere indirilir. Burada dikkat edilmesi gereken nokta, indirilen dokümanın adının \_X şeklinde gözükmesidir. X burada, dokümanın kaçıncı Revizyonda olduğunu göstermektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_745.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_746.png)

Doküman üzerinde Revizyon işlemleri gerçekleştirildikten sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_747.png) (Dosya yükle) butonuyla dokümanın sisteme yüklenme işlemi gerçekleştirilir. Burada da dikkat edilmesi gereken husus, sistemden indirilen dokümanın adı ile sisteme yüklenen Dokümanın adının aynı olması gerekliliğidir. Aksi takdirde sistem hata vermektedir. İndirilen dosya adı ile sisteme yüklenmesi gerektiği uyarısı çıkmaktadır. Ekleyeceğimiz dosya ismi \_X şeklinde değiştirilerek tekrar dosya yüklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_748.png)

Doküman Revizyon ekranında Doküman sekmesinde ![ref130] (Dosya Ekle) butonu tıklanarak Revize edilen dokümanın adı, sistemden indirilen adı neyse o olacak şekilde değiştirilerek sisteme yükleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_749.png)

Dosya Ekle ekranında Gözat butonu tıklanılarak açılan ekranda  sisteme yüklenecek dokümanın seçim işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_750.png)

Doküman Revizyon ekranında Doküman sekmesinde “Dosya Başarıyla aktarılmıştır” mesajı gelir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_751.png)

Doküman Bilgileri sekmesi tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_752.png)

Doküman Revizyon ekranında ![ref131]  butonuna tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_753.png)

Sistem tarafından “Göndermek istediğinize emin misiniz?” mesajından “Tamam” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_754.png)

Sistemde görüş matrisinde  varsa görüşe görüş yoksa  kontrol ve onay süreçlerine iletilir. Doküman hazırlama süreçlerindeki akış ile aynı aşamalar gerçekleştirilir. Revizyon İşlemi yapılan doküman kontrolcünün “Bekleyen işlerim” sayfasında “ Kontrol Bekleyen Dokümanlar” işi olarak görev düşer.   Kontrol aşamasında başlanarak, kontrol ve onay aşamaları yapılarak dokümanın revizyon işlemi tamamlanır.
#### **6.2.7.Doküman İptal İşlemi**
**Menü Adı**: Entegre Yönetim Sistemi/ Doküman İşlemleri/ Doküman İptal İşlemi

Dokümanların iptal işleminin gerçekleştirildiği menüdür. Doküman yürürlükten kaldırılacağı zaman “İptal İşlemi” başlatılır. Bir kullanıcının herhangi bir dokümanı iptal edebilmesi için, ilgili dokümanın “Yetki Matrisi” sekmesinden “İptal Etme” yetkisinin verilmiş olması gerekir. İptal işlemi tıpkı doküman hazırlama ve revizyon işlemlerinde olduğu gibi “Onay” sürecinden geçer ve ardından doküman iptal edilmiş olur.

Entegre Yönetim Sistemi/ Doküman İşlemleri/ Doküman İptal işlemi ekranı açılır.Açılan Doküman İptal -Klasör Seçme ekranında iptal edilecek dokümanın bulunduğu klasör seçilir ve ![ref138] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_756.png)

Açılan Doküman İptal - Doküman Belirleme ekranından iptal edilmek istenilen doküman seçilerek  ![ref138]  butonuna tıklanarak  Dokümanın iptal süreci başlatılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_757.png)

Açılan ekranda doküman bilgilerini sekmesinde  “İptal Nedeni” bilgisi yazılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_758.png)




Doküman İptal ekranında Doküman Bilgileri sekmesinde Dokümanın İptal Nedeni bilgisi yazılma işleminden sonra   ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_759.png) butonu tıklanarak onay matrisinde bulunan onaycılara Doküman iptal onayına gönderilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_760.png)

Sistem tarafından “Göndermek istediğinize emin misiniz?” mesajından “Tamam” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_761.png)

Sistem tarafından doküman iptal işlemi için onay gönderilenen kullanıcının bilgisi verilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_762.png)

İlgili doküman onaycının “**Bekleyen İşlerim”** sayfasında “**İptal Onayı Bekleyen Dokümanlar**”  işi olarak görev düşer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_763.png)

İlgili görevdeki  doküman kodu alanındaki  link tıklanarak doküman bilgileri sayfası açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_764.png)

**Ekranda bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_765.png):Doküman iptal işlemi onaylanır.

![ref139]:Dokümanın iptal işlemi red  edilir.

Dokümanın iptal talebi uygun bulunmayıp, onaycı tarafından red edilecekse  ![ref139] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_767.png)


Açılan  Doküman İptal-Onay Ret  ekranında açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_768.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Ret Nedeni:** Doküman İptal- Onay Ret ekranında dokümanın iptal işleminin ret nedeni bilgisinin yazıldığı alandır.

**Ekranda bulunan butonlar yardımıyla;**

![ref140]:Dosya ekleme işlemi yapılır.

![ref141]:Eklenen dosyanın görüntüleme işlemi yapılır.

![ref142]:Eklenen dosyanın silinme işlemi yapılır.

Doküman İptal- Onay Ret ekranında Ret Nedeni bilgisi girilmesi ve istenirse red nedeni ile ilgili ![ref140] butonu tıklanrak Ek dosya yükleme işlemi  yapılarak ekranın  sol üst köşesindeki  ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_772.png)  butonu tıklanarak doküman iptal işleminin  reddet edilme kayıt işlemi yapılır. Ayrıca bu ekranda eklenen dosyanın görüntüleme işlemi için ![ref141] butonu tıklanarak görüntüleme işlemi ve yanlışlıkla eklenen dosyanın silinmesi içinde ![ref142] butonu tıklanarak  işlemleride yapılır.

Doküman iptal işlemi aşamasında İptal nedeni bilgisi görüntülenir.  Onay verecek kişinin açıklaması alanı parametreye bağlı olarak görüntülenir. Doküman Yönetimi Modülü parametrelerinde 341 numaralı “Doküman İptal Onayında Ek Açıklama Girilsin mi?” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_773.png)

Parametre aktif edildikten sonra “Onay Verecek Kişinin Açıklaması” alanı görüntülenir. Onaycı bu alanda dokümanın iptal işlemi ile ilgili açıklama bilgisi girer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_774.png)

Onaydaki kişi dokümanın iptal işlemi ile ilgili açıklama  bilgisi girdikten sonra dokümanın iptal talebi uygun bulup, ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_775.png) butonu tıklayarak doküman iptal işlemi süreci başlatır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_776.png)

Sistem tarafından “Göndermek istediğinize emin misiniz?” mesajından “Tamam” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_777.png)

Sistem tarafından “Doküman iptal onayı tamamlanarak arşive gönderilmiştir.” mesajı verilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_778.png)

İptal onayı verildiğinde doküman iptal işlemi tamamlanıp raporlar menüsündeki, “ İptal Edilen Dokümanlar” listesinden raporlanabilir. Entegre Yönetim Sistemi/Doküman İşlemleri/Raporlar/ İptal Edilen Doküman Listesi  menüsü tıklanılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_779.png)

Açılan İptal Edilen Doküma Listesi ekranında  Doküman Arama sekmesinde filtrede arama kriterlerinden Doküman Kodu alanı iptal edilen dokümanın kod bilgisi yazılarak ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_780.png) (Ara) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_781.png)

İptal edilen Doküman Listesi ekranında Doküman Listesinde iptal edilen doküman seçili iken![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_782.png) butonu tıklanılır. Açılan ekranında Doküman Yönetimi Modülü parametrelerinden 92 numaralı “İptal Edilen Dokumanlara Basılacak Yazı”  parametre değerinde yazılan yazıya göre İptal edilmiş dokümanlarda PDF formatında görülecek yazının ayarlanması sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_783.png)

Bu parametredeki iptal edilen Dokümanlara yazılacak yazıyı belirledikten sonra bunun bir hologram şeklinde çapraz şeklinde çıkmasını istersek  93 numaralı “İptal edilen dökumanlarda yazdırma sırasında hologram basılsın mı?” parametresinin parametre değeri “Evet” seçilerek parametrenin aktif edilmesi gerekmektedir.![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_784.png) 

Parametre aktif edildikten sonra iptal edilen dokümanlar ekran görüntüsü şeklinde   yazının holagram şeklinde basılması sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_785.png)

İptal edilmiş dokümları iptal işleminden geri getirmek için  Sistem Altyapı Tanımları/Doküman İşlemleri/ Dokümanı İptalden Geri Getir menüsü kullanılmaktadır. 

Doküman İptal işlemi ikinci bir yöntem olarak  Doküman Görme menüsünde Doküman listesi sekmesinde doküman kodu tıklanılır. Dokümanın görüntülendiği açılan Doküman görme ekranında ![ref143] butonu tıklanarak yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_787.png)

Doküman Görme ekranında ![ref143] butonu tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_788.png)

Açılan Doküman İptal ekranında İptal Nedeni alanında dokümanın neden iptal işlemi yapıldığı nedeni yazılarak ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_789.png) butonu tıklanılır.  Doküman İptal İşlemi menüsündeki yapılan işlemi aşamaları aynı şekilde yapılarak dokümanın iptal işlemi yapılır.
#### **6.2.8.Doküman Askıya Alma**
**Menü Adı**: Entegre Yönetim Sistemi/ Doküman İşlemleri/ Doküman Askıya Alma

Dokümanlar istenildiğinde yetkili kullanıcılar tarafından erişime kapatılabilmektedir. Doküman askıya alma işlemi ile Aktif-Pasif özelliği kullanılır. Askıya alınan doküman pasifleştirilmiş olup, tekrar aktifleştirilene kadar kimse dokümana ulaşamaz. Dokümanı askıdan kaldırmak için, doküman askıya alma menüsünden pasif doküman seçilerek yeniden aktifleştirilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_790.png) Doküman Aktifleme/Pasifleme ekranından bir dokümanı askıya almak için  öncelikle Doküman Seç alanında ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_791.png) butonu tıklanarak sistemde yüklü doküman listesinde  ilgili doküman seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_792.png)

Doküma seçim işleminde sonra dokümanlar bilgileri ile  ilgili alanlardaki bilgiler sistem tarafından otomatik olarak verilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_793.png)

Doküman Aktifleme/Pasifleme ekranından Doküman seçiminin ardından ![ref144]butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_795.png)

Sistem tarafından “Dokumanı Aktiflemek-Pasiflemek istediğinize emin misiniz?	 mesajında “Tamam” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_796.png)

Doküman seçiminin ardından  ![ref144]butonu tıklanarak  durumu “**aktif**” olarak bulunan doküman “**pasif**” hale getirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_797.png)

Doküman Aktifleme/Pasifleme ekranından aynı şekilde durumu Pasif olan dokümanı durumu “Aktif” statüsüne getirmek için ![ref144] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_798.png)

Sistem tarafından “Dokumanı Aktiflemek-Pasiflemek istediğinize emin misiniz?	 mesajında “Tamam” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_799.png)

Doküman Aktifleme/Pasifleme ekranından  ![ref144]butonu tıklanarak  durumu “**pasif**” olarak bulunan doküman “**aktif**” hale getirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_800.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_801.png)

Entegre Yönetim Sistemi/Doküman işlemleri/Raporlar/ Askıya Alınan Doküman Listesi menüsünden  Askıya Alma işlemi yapılan  dokümlara listesine  ulaşılır.
#### **6.2.9.Doküman Değişiklik Talebi**
**Menü Adı**: Entegre Yönetim Sistemi/ Doküman İşlemleri/ Doküman Değişiklik Talebi

Üst yetkili kullanıcılar tarafından, dokümanların revize edilmesi/ yeni dokümanların hazırlanması işlemlerinin görev olarak atanması için kullanıldığı menüdür. Birden çok dokümanda yapılacak işlem için görev ataması yapılabilir. Doküman değişiklik talebi yapılacak personel, Doküman Yönetimi Modülü  parametrelerinden 49 numaralı “Doküman Değişiklik talebi açabilecek personeller(Sicil No'ları virgül ile ayırarak yazınız)” parametrede parametre değerine  sicil numaraları yazılarak tanımlanır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_802.png)

Parametrede sicil numaraları tanımlı personellerin Doküman Değişiklik Talebi ekranlarında ![ref145] butonu görüntülenir.Tanımlanan personellerin doküman değişiklik talebi ekranında görüntülenen ![ref145]  butonu aracılığıyla görev atama yetkisi olur. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_804.png) 

**Ekranda bulunan butonlar yardımıyla;**

![ref146]: Yeni bir Doküman Değişiklik Talebi tanımlanır.

![ref147]: Listede seçili olan Doküman Değişiklik Talebi bilgisi görüntülenir

![ref148]: Listede seçili olan Doküman Değişiklik Talebi bilgisi silinir.

![ref32]: Kayıtlar filtrelenerek arama yapılır.

![ref3]: Veriler Excel’ e aktarılır.

![ref4]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref5]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref149]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Doküman Değişiklik Talebi  ekranında ![ref146]  butonu tıklanarak yeni bir Doküman Değişiklik Talebi tanımlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_809.png)

**Doküman Değişiklik Talepleri Ekranında bulunan butonlar yardımıyla;**

![ref146]: Yeni bir Doküman Değişiklik Talebi yapılır.

![ref147]: Listede seçili olan Doküman Değişiklik Talebi bilgisi görüntülenir

![ref148]: Listede seçili olan Doküman Değişiklik Talebi bilgisi silinir.

Doküman Değişiklik Talepleri ekranında **![ref146]** butonu tıklanarak yeni bir doküman değişiklik talebi işlemi tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_810.png)

Açılan Doküman Değişiklik Talebi ekranında Doküman alanında ![ref150] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_812.png)

Açılan Doküma Listesinde değişiklik talebi yapılacak dokümanın seçim işlemi yapılarak ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_813.png) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_814.png)

Doküman değişiklik talebinde, hangi doküman olduğu ve bu talebi kimin gerçekleştireceği seçilir. İşin bitiş tarihi seçilir. Notlar alanında varsa not bilgisi girilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_815.png)

Doküman Değişiklik Talebi ekranında gerekli alanlar ilgili bilgiler girildikten sonra ekranın sol üst köşesindeki ![ref151] butonu tıklanarak doküman değişiklik talebi kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_817.png)

**Doküman Hazırlama  Talepleri Ekranında bulunan butonlar yardımıyla;**

![ref146]: Yeni bir doküman hazırlama talebi yapılır.

![ref147]: Listede seçili olan doküman hazırlama talebi bilgisi görüntülenir

![ref148]: Listede seçili olan doküman hazırlama talebi bilgisi silinir.

Doküman Hazırlama  Talepleri ekranında ![ref146] butonu tıklanarak yeni bir doküman hazırlama talebi işlemi tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_818.png)

Açılan Doküman Hazırlama Talebi ekranında Klasör Seç ekranında ![ref150] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_819.png)

Açılan Doküman Klasörü listesinde doküman hazırlama talebi yapılacak klasör seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_820.png) butonu tıklanılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_821.png)

Yeni doküman hazırlama talebi ekranında dokümanın hazırlanacağı klasör seçilir Doküman Kodu ve Adı tanımlanır. Dokümanın kim tarafından hazırlanacağı bilgisi seçilir. Notlar alanında varsa not bilgisi girilir.

Doküman Hazırlama Talebi ekranında gerekli alanlar ilgili bilgiler girildikten sonra ekranın sol üst köşesindeki ![ref151] butonu tıklanarak doküman hazırlama talebi kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_822.png)

Doküman Değişiklik Talebi ekranında Revizyon Nedeni bilgisi yazılarak ekranın sol üst köşesindeki ![ref151] butonu  tıklanarak Doküman Değişiklik Talebi kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_823.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_824.png)

Kişilere atanan görevler “**Bekleyen İşlerim**” sayfasında “**Saklanan Dokümanlar**” listesinin altında görüntülenir.

**Doküman Değişiklik Talebi;**

İlgili görevdeki doküman kodu alanındaki link tıklanarak açılan Doküman Revizyon  ekranında Doküman Revizyon menüsünde yapılan dokümanda revizyon işlem  aşamalarında yapılan işlem adımları süreç devam edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_825.png)

**Doküman Hazırlama Talebi;**

İlgili görevdeki doküman kodu alanındaki link tıklanarak açılan Yeni Doküman  ekranında Doküman Hazırlama  menüsünde yapılan dokümanda hazırlama işlem  aşamalarında yapılan işlem adımları ile süreç devam edilir.

.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_826.png)
#### **6.2.10.Kontrollü Kopya**
**Menü Adı**: Entegre Yönetim Sistemi/ Doküman İşlemleri/ Kontrollü Kopya

Kontrollü Kopya olarak dağıtılan dokümanların dağıtım raporlarının alındığı menüdür.
##### **6.2.10.1.Dağıtım Föyü Yazdırma**
**Menü Adı**: Entegre Yönetim Sistemi/ Doküman İşlemleri/ Kontrollü Kopya/ Dağıtım Föyü Yazdırma

Seçilen bir doküman için dağıtım föyü alındığı menüdür. Dağıtım Föyü yazdırma ekranından Doküman Arama ve Doküman Listesi sekmesi olmak üzere iki sekme karşımıza çıkar. Doküman Arama sekmesinde arama kriterlerine göre filtreleme işlemi yapılır. Doküman listesinde sekmesinde  ise bu arama kriterlerine göre filtreleme işlemine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_827.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref32]: Kayıtlar filtrelenerek arama yapılır.

![ref3]: Veriler Excel’ e aktarılır.

![ref4]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref5]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref149]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır

Dağıtım Föyü yazdırma ekranından Doküman Seç alanında ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_828.png)  butonuna tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_829.png)

Açılan Doküman Listesinde Doküman seçim işlemi yapılarak ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_830.png) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_831.png)

Doküman Dağıtım Föyü ekranında Doküman Listesi sekmesinde seçilen Dokümana göre  Dağıtım yerleri listenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_832.png)

Doküman Föyü Yazdırma ekranında Dokümana ait dağıtım yerleri seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_833.png) (Excel Aktar) butonu tıklanarak Excel formatında dağıtım Föyü raporu alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_834.png)
##### **6.2.10.2.Grup Bazında Dağıtım Föyü**
**Menü Adı**: Entegre Yönetim Sistemi/ Doküman İşlemleri/ Kontrollü Kopya/ Grup Bazında Dağıtım Föyü

Kontrollü Kopya olarak dağıtılan dokümanların “Klasör” bazında raporu alındığı menüdür. Klasör Bazından Doküman Föyü ekranından iki sekme karşımıza çıkar. Doküman Görme ve Doküman Seçme sekmeleridir. Doküman görme sekmesinde arama kriterlerine göre filtreleme işlemi yapılır. Doküman seçme sekmesinde ise bu arama kriterlerine göre filtreleme işlemine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_835.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref32]: Kayıtlar filtrelenerek arama yapılır.

![ref3]: Veriler Excel’ e aktarılır.

![ref4]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref5]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref149]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Doküman Seçme sekmesinde  Klasör Seç alanında ![ref152] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_837.png)

Açılan Doküman Klasör listesinde klasör seçim işlemi yapılarak ![ref153] butonu tıklanarak klasör seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_839.png)

Klasör seçim işleminde sonra ![ref154] (Ara) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_841.png)

Klasör Bazında Doküman Föyü ekranında  Doküman Seçme sekmesinde filtreleme işlemine göre seçilen dokümanlarla ilgili kontrollü kopya bilgileri listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_842.png)

Klasör Bazında Doküman Föyü ekranında  listelenen dokümanlar seçim işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_843.png)

Klasör Bazında Doküman Föyü ekranında   ![ref3] (Excel Aktar)  butonu tıklanarak Excel formatında rapor alınma işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_844.png)
##### **6.2.10.3.Dağıtım Yeri Bazında Dağıtım Föyü**
**Menü Adı**: Entegre Yönetim Sistemi/ Doküman İşlemleri/ Kontrollü Kopya/ Dağıtım Yeri Bazında Dağıtım Föyü

Kontrollü Kopya olarak dağıtılan dokümanların “Dağıtım Yerleri” bazında raporu alındığı menüdür. Dağıtım Yeri Bazında Dağıtım Föyü ekranından iki sekme karşımıza çıkar. Doküman Görme ve Doküman Yeri Seçme sekmeleridir. Doküman görme sekmesinde arama kriterlerine göre filtreleme işlemi yapılır. Doküman Yeri Seçme sekmesinde ise bu arama kriterlerine göre filtreleme işlemine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_845.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref32]: Kayıtlar filtrelenerek arama yapılır.

![ref3]: Veriler Excel’ e aktarılır.

![ref4]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref5]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref149]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Dağıtım Yeri  Seçme sekmesinde  Dağıtım Yeri Seç  alanında ![ref155] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_847.png)

Açılan Dağıtım Yeri listesinde Dağıtım yeri seçim işlemi yapılarak ![ref153] butonu tıklanarak Dağıtım yeri seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_848.png)

Dağıtım Yeri seçim işleminde sonra ![ref154] (Ara) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_849.png)

Dağıtım Yeri Bazında Dağıtım Föyü ekranında Dağıtım Yeri Seçme  sekmesinde filtreleme işlemine göre dağıtım yerleri bazında kontrollü kopya olarak dağıtılan dokümanların  listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_850.png)

Dağıtım Yeri Bazında Dağıtım Föyü ekranında Dağıtım Yeri Seçme sekmesinde listelenen dokümanlar seçim işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_851.png)

Dağıtım Yeri Bazında Dağıtım Föyü ekranında   ![ref3] (Excel Aktar)  butonu tıklanarak Excel formatında rapor alınma işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_852.png)
##### **6.2.10.4. Genel Dağıtım Föyü**
**Menü Adı**: Entegre Yönetim Sistemi/ Doküman İşlemleri/ Kontrollü Kopya/ Genel Dağıtım Föyü

Kontrollü Kopya olarak dağıtılan dokümanların “Genel” raporunun alındığı menüdür. Genel Dağıtım Föyü ekranında iki sekme karşımıza çıkar. Doküman Görme ve Doküman Seçme sekmeleridir.Doküman görme sekmesinde arama kriterlerine göre filtreleme işlemi yapılır. Doküman seçme sekmesinde ise bu arama kriterlerine göre filtreleme işlemine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_853.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref32]: Kayıtlar filtrelenerek arama yapılır.

![ref3]: Veriler Excel’ e aktarılır.

![ref4]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref5]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref149]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Genel Dağıtım Föyü ekranında filtre arama kriterlerinde Bağlı Olduğu Klasör alanında klasör seçim işlemi yapılarak ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_854.png) (Ara) butonu tıklanılır

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_855.png)

Genel Dağıtım Föyü ekranında Döküman Görme sekmesinde yapılan arama kriterlerine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_856.png)

Genel Dağıtım Föyü ekranında listelenen kayıtların seçim işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_857.png)

Genel Dağıtım Föyü ekranında ekranında   ![ref3] (Excel Aktar)  butonu tıklanarak Excel formatında rapor alınma işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_858.png)
#### **6.2.11.Kalite Kayıtları**
**Menü Adı**: Entegre Yönetim Sistemi/ Doküman İşlemleri/ Kalite Kayıtları
##### **6.2.11.1. Kalite Kaydı İşlemleri**
**Menü Adı**: Entegre Yönetim Sistemi/ Doküman İşlemleri/ Kalite Kayıtları/ Kalite Kaydı İşlemleri

Kalite kaydı işlemleri menüsünde boş form doldurularak,  paylaşılmakta ve kayıt olarak sistemde saklanmaktadır. Bir formun kalite kayıtları menüsünde aktif olarak kullanılabilmesi için, boş formun QDMS sisteminde oluşturulduğu sırada, “Form” olarak işaretlenmiş ve kullanım şeklinin de “Kalite Kaydı” olarak seçilmiş olması gerekmektedir. Bu şartı sağlayan formlar ekranın sol bölümünde ilgili klasörler altında sıralanır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_859.png)

Kayıt oluşturulacak form seçilerek, ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_860.png) butonuna basılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_861.png)

Kal,te Kaydı Listesi ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_862.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref156]:Yeni bir kalite kaydı oluşturulur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_864.png): Listede seçili olan kalite kaydı bilgisi güncellenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_865.png): Listede seçili olan kalite kaydı  silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_866.png): Listede seçili olan kalite kaydı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_867.png): Listede seçili olan kalite kaydı  kopyalanır

Kalite Kaydı Listesi ekranından ![ref156]  butonu tıklanarak yeni bir kalite kaydı tanımlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_868.png)

**Ekranda bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_869.png):Kayıt işlemi yapılır.

![ref157]: Kalite kaydının boş hali görüntülenerek bilgisayara indirilir.

![ref158]:Kalite kaydının dolu hali Qdms sistemine yüklenir.

Kalite Kaydı ekranında ![ref157] butonu tıklanarak kalite kaydının boş hali görüntülenerek kullanıcının bilgisayarına indirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_872.png)

İndirilen Kalite kaydı üzerinde ilgili alanlar doldurulur. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_873.png)

Doldurulan form bilgisayara yüklenirken sistem tarafından bir ad verilir ve oluşturulan kalite kaydı ![ref158]  butonu ile Qdms’e geri yükleme işlemi yapılır.  

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_874.png)

Dosya Ekle ekranında Gözat butonu tıklanılır

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_875.png)

Dolu kalite kaydı seçilirek Qdms sistemine yükleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_876.png)

Sistem tarafından “Dosya başarıyla aktarılmıştır” mesajı gelir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_877.png)

İç Dağıtım ve Dış Dağıtım alanlarına kalite kaydının gönderileceği kişiler/ gruplar belirlenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_878.png)

Kalite Kaydı ekranından Yetki Matrisi sekmesi tıklanılır. “Yetki Matrisi” sekmesinden bu kayıt üzerinde hangi pozisyonların/ kullanıcı gruplarının “Okuma, Hazırlama/ Revize, Silme” yetkisi olması isteniyorsa sistemden seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_879.png)

Kalite Kaydı ekranından Yetki Matrisi sekmesinde ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_880.png) ekle butonu tıklanarak yetki matrisine pozisyondaki personel eklenerek kalite kaydı ile ilgili yetkilendirme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_881.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_882.png)

Kalite Kaydı ekranında Yetki matrisinde yekilendirme işleminden sonra Kayıt Görüntüle sekmesi tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_883.png)

Son olarak  ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_884.png) butonu ile “Kalite Kaydı”  onay akışındaki kişiye onay gönderilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_885.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_886.png)

Kalite kayıtlarının oluşturulduktan sonra dağıtıma gitmeden önce onaya gitmesi isteniyorsa Doküman Yönetimi  Modülü parametrelerinden  227 numaralı “ Kalite Kaydı Güncelleme işleminde onaya gönderilsin mi?” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_887.png)

Sistem Altyapı/ BSAT/ Konfigürasyon Ayarları/ Akış Tanımlama ve Sistem Altyapı/ BSAT/ Konfigürasyon Ayarları/ /Rol Tanımlama menülerinden akışların kime gideceği ayarlanır.Bu kısımda Kalite Kaydı Onay Akışı için ilgili rol tanımlaması yapılır. Alt Modül Tanımlama menüsünde akışın kontrol işlemininin ayrıca yapılması gerekir.

Qdms ana giriş ekranında onay akışındaki kişinin  kullanıcı adı ve parola bilgisi ile Qdms local adresine giriş yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_888.png)

Onay gönderilen Kalite kayıtları onaydaki kişinin “Bekleyen İşlerim” sayfasında “Onaylanması Gereken Kalite Kayıtları” işi olarak görev düşer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_889.png)

İlgili görevdeki kayıt kodu alanındanki link tıklanarak Kalite kaydı ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_890.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref159]:Kalite kaydı formunun görüntüleme işlemi yapılır.

![ref160]: Kalite kaydı formunun onaylama işlemi yapılır

![ref161]:Kalite kaydı formunun red etme işlemi yapılır.

Kalite Kaydı ekranında ![ref159] butonu tıklanrak Kalite kaydı formunun görüntüleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_894.png)

Kalite Kaydı ekranında ![ref161] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_895.png)

Açılan Reddet pop-upn’da Kalite kaydı formunun ret nedeni bilgisi yazılarak bu aşamada kalite kaydının ret işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_896.png)

Kalite kaydı ekranında kalite kaydı formu uygun görüldüğünde ![ref162] butonu tıklanarak onaylama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_898.png)

Onaylama işleminde Doküman Yönetimi Modülü parametrelerinde 282 numaralı “Kalite kayıtlarında e-imza kullanılsın mı?” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_899.png)

Parametre aktif edildikten sonra kalite kaydı onaylama işleminde  “şifre onayı” pop-unp ‘ ı açılarak onaylama işleminde şifre onayı alınması sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_900.png)

Şifre onayında onaydaki kullanıcının şifre bilgisi yazılarak kalite kaydı formu onaylama işlemi onay akışındaki son onaycıdaki kişi gönderilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_901.png)

Kalite kaydı formunun onay aşamasındaki Qdms ana giriş ekranında son onaycını  kullanıcı adı ve parola bilgisi ile Qdms local adresine giriş yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_902.png)

Onay gönderilen Kalite kayıtları onaydaki kişinin “Bekleyen İşlerim” sayfasında “Onaylanması Gereken Kalite Kayıtları” işi olarak görev düşer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_903.png)

İlgili görevdeki kayıt kodu alanındanki link tıklanarak Kalite kaydı ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_904.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref163]:Kalite kaydı formunun görüntüleme işlemi yapılır.

![ref164]: Kalite kaydı formunun onaylama işlemi yapılır

![ref165]:Kalite kaydı formunun red etme işlemi yapılır.

Kalite kaydı ekranında ![ref163]butonu ile kalite kaydı formu görüntüleme işlemi , ![ref165] butonu ile kalite kaydı formunun ret nedeni yazılarak ret etme işlemi ve![ref164] butonu tıklanarak kullanıcının şifre bilgisi yazılarak onaylama işlemleri bu aşamada yapılır. 

Kalite kaydı ekranında kalite kaydı formu uygun görüldüğünde ![ref166] butonu tıklanarak onaylama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_909.png)

Kalite Kaydı formunun onaylama işleminde onaydaki kişinin parola bilgisi yazılarak  kalite kaydı formu onaylama işlemi yapılır. Doküman Yönetim Modülü parametrelerinde 282 numaralı parametre bağlı olarak Şifre onayı pop-unp’ı açılmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_910.png)
##### **62.11.2.Kalite Kaydı Raporu**
**Menü Adı**: Entegre Yönetim Sistemi/ Doküman İşlemleri/ Kalite Kaydı/ Kalite Kaydı Raporu 

“Kalite Kaydı Raporu” menüsü ile tüm kalite kayıtlarına ait raporlar alınır. Kalite kaydı filtreleme seçeneği ile istenilen kriterlere göre rapor alınması sağlanır. Kalite Kaydı Raporu ekranında iki sekme karşımıza çıkar. Bu sekmeler Kayıt Arama ve Kayıt Görüntüleme sekmeleridir.Kayıt arama sekmesinde arama kriterlerine göre filtreleme işlemi yapılarak ilgili kayıtların kayıt görüntüleme sekmesinde görüntülenmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_911.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref167]:Listede secili Kalite Kaydı formunun görüntüleme işlemi yapılır.

![ref2]: Kayıtlar filtrelenerek arama yapılır.

![ref3]: Veriler Excel’ e aktarılır.

![ref4]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref5]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref149]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Kalite Kaydı Listesi ekranında  Kayıt arama sekmesinde arama kriterleri olan doküman kodu alanına kalite kaydı formunu kod bilgisi yazılarak ![ref2] (Ara) butonu tıklanılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_913.png)

Kalite Kaydı Listesi ekranında  Kayıt Görüntüleme ekranında arama kriterlerine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_914.png)

Kalite Kaydı Listesi ekranında  Kayıt Görüntüleme sekmesinde  kayıt seçili iken ![ref167] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_915.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_916.png)

Kalite Kaydı Listesi ekranında  ![ref3] (Excel Aktar) butonu tıklanarak Kalite kaydı raporunu Excel formatından raporu alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_917.png)
#### **6.2.12.Raporlar**
**Menü Adı**: Entegre Yönetim Sistemi/ Doküman İşlemleri/ Raporlar

Doküman Yönetimi Modülü ile ilgili tüm raporlara ulaşıldığı ve bu raporların excel formatında görüntülendiği menüdür.
##### **6.2.12.1.Doküman Özet Listesi**
**Menü Adı**: Entegre Yönetim Sistemi/ Doküman Yönetimi/ Raporlar/Doküman Özet Listesi

Sistemdeki tüm dokümanların listesine ulaşıldığı ve raporun alındığı menüdür. Doküman Özet listesi ekranında doküman arama ve doküman listesi sekmesi olmak üzere iki sekme karşımıza çıkar. Doküman arama sekmesinde arama kriterlerine göre filtreleme işlemi yapılır. Doküman listesinde sekmesinde  ise bu arama kriterlerine göre filtreleme işlemine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_918.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref32]: Kayıtlar filtrelenerek arama yapılır.

![ref3]: Veriler Excel’ e aktarılır.

![ref4]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref5]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref149]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Doküman Özet listesi ekranında doküman arama sekmesinde filtre arama kriterleri olan “Bağlı olduğu klasör” alanında klasör seçim işlemi yapılarak ![ref32] (Ara) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_919.png)

Doküman Özet listesi ekranında doküman listesi sekmesinde  yapılan filtredeki  arama kriterlerine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_920.png)

Doküman Özet listesi ekranında doküman listesi sekmesinde listelenen dokümanlarda doküman kodu link tıklanarak dokümanın görüntüleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_921.png)

Açılan Doküman Görme ekranında doküman ilgili bilgilere ulaşılır.Bu aşamada dokümanın farklı diller yükleme işlemi yapılma işlemi yapıldıysa o dillerde dokümanı görüntüleme işlemi yapılır. ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_922.png) butonu tıklanarak kontrol kopya talebinde bulunma işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_923.png)

Doküman Özet Listesi ekranında ![ref3] (Excel’e Aktar) butonu tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_924.png)Doküman Özet Listesi Raporunun  Excel formatında raporu görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_925.png)
##### **6.2.12.2.Onay Bekleyen Doküman Listesi**
**Menü Adı**: Entegre Yönetim Sistemi/ Doküman Yönetimi/ Raporlar/ Onay Bekleyen Doküman Listesi

Hazırlanıp onaya gönderilmiş dokümanların kimde ve kaç gündür onayda beklediği listesinin görüntülendiği ve raporun alındığı menüdür. Onay Bekleyen Doküman Listesi  ekranında doküman arama ve doküman listesi sekmesi olmak üzere iki sekme karşımıza çıkar. Doküman arama sekmesinde arama kriterlerine göre filtreleme işlemi yapılır. Doküman listesinde sekmesinde  ise bu arama kriterlerine göre filtreleme işlemine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_926.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref168]:Listede seçili dokümanın görüntüleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_928.png):Listede seçili dokümanın onay matrisindeki onaycının değiştirilme işlemi yapılır.

![ref32]: Kayıtlar filtrelenerek arama yapılır.

![ref3]: Veriler Excel’ e aktarılır.

![ref4]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref5]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref149]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Onay Bekleyen Doküman Listesi  ekranında doküman arama sekmesinde filtre arama kriterleri olan “Bağlı olduğu klasör” alanında klasör seçim işlemi yapılarak ![ref29] (Ara) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_929.png)

Onay Bekleyen Doküman Listesi  ekranında doküman listesi sekmesinde  yapılan filtredeki  arama kriterlerine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_930.png)

Onay Bekleyen Doküman Listesi  ekranında doküman listesi ekranından doküman seçilerek ![ref169] butonu tıklanarak Doküman Onaylama ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_932.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref94]:Doküman onaylama işlemi yapılır.

![ref95]:Doküman red nedeni yazılarak ret etme işlemi yapılır.

![ref100]: İlgili kişilerde bu aşamada yorum isteme işlemi yapılır. Parametreye bağlı olarak görüntülenen bir butondur. Doküman Yönetimi parametrelerinde 113 numaralı “Kontrol ve Onay Adımında Yorum İstenebilecek mi” parametresinin parametre değeri “ Evet” seçilerek parametre aktif edilir. Parametre aktif edildikten  ![ref100] butonu görüntülenir ve ilgili personellerde seçim yapılarak bu personellerden bu aşamada  yorumları alınır.  

![ref98]: Tanımlanan yorum bilgisi gösterir.

Doküman onaylama ekranından  bu aşamada ![ref94] butonu tıklanarak dokümanı onaylama işlemi , ![ref95] butonu tıklanarak ret ned nedeni yazılarak dokümanı  ret etme işlemi yaparak hazırlayan geri gönderme işlemi , ![ref100]butonu ile ilgili personellerden yorum alma işlemi ve ![ref98]butonu ile de yapılan yorumları gösterme işlemleri yapılır. 

Onay Bekleyen Dokümanlar listesi ekranında ![ref170] butonu tıklanılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_934.png)

Açılan Onay Matrisini değiştirici ekranında  Onay matrisindeki onaycının değiştirilme veya yeni bir onaycı ekleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_935.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref171]:Kayıt işlemi yapılır.

![ref172]:Onay matrisine pozisyon ekleme işlemi yapılır.

![ref173]:Listede seçili satır silinme işlemi yapılır.

Onay Matrisi Değiştirici ekranından ![ref172]butonu tıklanarak açılan sistemde tanımlı pozisyon listesinden onay matrisine eklenecek pozisyondaki kişi ![ref174] butonu tıklanarak seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_940.png)

Onay Matrisi Değiştirici ekranında  onay matrisi değiştirme işleminden sonra ekranın sol üst köşesindeki ![ref175] butonu tıklanrak onay matrisi değiştirme kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_942.png)

Sistem tarafından “Onay Matrisini değiştirmek istediğinize emin misiniz?” mesajın “Tamam” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_943.png)



Sistem tarafından “Onay Matrisi başarıyla değiştirilmiştir.” mesajı verilerek  onay matrisinin değiştirme işlemi yapıldığı belirtilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_944.png)

Onay Bekleyen Doküman Listesi ekranında ![ref176] (Excel’e Aktar) butonu tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_946.png)

Onay Bekleyen Doküman Listesi raporunun  Excel formatında raporu görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_947.png)
##### **6.2.12.3. Doküman Dosya Boyut Raporu**
**Menü Adı**: Entegre Yönetim Sistemi/ Doküman Yönetimi/ Raporlar/ Doküman Dosya Boyut Raporu

Doküman Yönetim Modülü kapsamında sisteme yüklü olan dokümanların boyutlarını bilgisinin Kilobayt cinsinden listesinin görüntülendiği ve Excel formatında raporunun alındığı menüdür. Doküman Dosya Boyut  Raporu ekranında iki sekme karşımıza çıkar. Bu sekmeler doküman listesi ve doküman arama sekmeleridir. Doküman arama sekmesinde arama kriterlerine göre filtreleme işlemi yapılır. Doküman listesinde sekmesinde  ise bu arama kriterlerine göre filtreleme işlemine göre kayıtlar listelenir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_948.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref32]: Kayıtlar filtrelenerek arama yapılır.

![ref3]: Veriler Excel’ e aktarılır.

![ref4]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref5]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref149]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Doküman Dosya Boyut  Raporu ekranında doküman arama sekmesinde filtre arama kriterleri olan “Doküman Kodu ” alanında doküman kodu yazılarak  ![ref29] (Ara) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_949.png)

Doküman Dosya Boyut  Raporu ekranında doküman listesinden yapılan filtredeki  arama kriterlerine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_950.png)

Doküman Dosya Boyut  Raporu ekranında ![ref30] (Excel’e Aktar) butonu tıklanarak Doküman Dosya Boyut  Raporu Excel formatından raporu alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_951.png)
##### **6.2.12.4.Kontrol Bekleyen Doküman Listesi**
**Menü Adı**: Entegre Yönetim Sistemi/ Doküman Yönetimi/ Raporlar/ Kontrol Bekleyen Doküman Listesi

Hazırlanıp kontrole gönderilmiş dokümanların kimde/ kaç gündür kontrolde beklediğinin listesinin ve raporunun alındığı menüdür. Kontrol Bekleyen Doküman Listesi ekranında doküman arama ve doküman listesi sekmesi olmak üzere iki sekme karşımıza çıkar. Doküman arama sekmesinde arama kriterlerine göre filtreleme işlemi yapılır. Doküman listesinde sekmesinde  ise bu arama kriterlerine göre filtreleme işlemine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_952.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref168]:Listede seçili dokümanın görüntüleme işlemi yapılır.Bu butonun görüntülemesi için Sistem Altyapı Tanımları/BSAT/Konfügürasyon Ayarları/Yönetici Tanımlama menüsünde kullanıcının Doküman Yönetimi modülünde Modül Yönetici olarak tanımlı olması gerekmektedir.

![ref32]: Kayıtlar filtrelenerek arama yapılır.

![ref3]: Veriler Excel’ e aktarılır.

![ref4]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref5]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref149]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Kontrol Bekleyen Doküman Listesi ekranında doküman arama sekmesinde filtre arama kriterleri olan “Doküman Kodu ” alanında doküman kodu yazılarak  ![ref29] (Ara) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_953.png)

Kontrol Bekleyen Doküman Listesi ekranında doküman listesi sekmesinde  yapılan filtredeki  arama kriterlerine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_954.png)

Kontrol Bekleyen Doküman Listesi ekranında doküman listesi ekranından doküman seçilerek ![ref169] butonu tıklanarak Doküman Kontrol  ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_955.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref91]:Doküman kayıt işlemi yapılır.

![ref92]:Kaydet ve devam etme işlemi yapılır. Parametreye bağlı olarak görüntülenen bir butondur.Doküman Yönetimi parametrelerinde 331 numaralı “Doküman hazırlama sayfasında kaydet ve devam et butonu kullanılsın mı?” parametresi parametre değeri “Evet” seçilerek parametre aktif edilir.

![ref93]

Parametre aktif edildikten sonra Doküman Hazırlama aşamasında  ![ref92] butonu görüntülenir.

![ref94]:Doküman onaylama işlemi yapılır.

![ref95]:Doküman red nedeni yazılarak ret etme işlemi yapılır.

![ref96]: İlgili kişilerde bu aşamada yorum isteme işlemi yapılır. Parametreye bağlı olarak görüntülenen bir butondur. Doküman Yönetimi parametrelerinde 113 numaralı “Kontrol ve Onay Adımında Yorum istenebilecek mi” parametresinin parametre değeri “ Evet” seçilerek parametre aktif edilir. Parametre aktif edildikten  ![ref96] butonu görüntülenir ve ilgili personellerde seçim yapılarak bu personellerden bu aşamada  yorumları alınır.  

![ref98]: Tanımlanan yorum bilgisi gösterir.

Doküman kontrol  ekranından  Modül yöneticisi   kullanıcı tıpkı kontrolcü gibi doküman bilgileri ve sekmeleri üzerinde her türlü değişiklik yapma yetkisine sahiptir. Bu aşamada ![ref177] butonu tıklanarak dokümanı kontrol  işlemi yaparak onay matrisindeki onaycıya gönderme işlemi , ![ref178] butonu tıklanarak ret ned nedeni yazılarak dokümanı  ret etme işlemi yaparak hazırlayan geri gönderme işlemi , ![ref179]butonu ile ilgili personellerden yorum alma işlemi ve ![ref180]butonu ile de  yapılan yorumları gösterme işlemleri yapılır.

Doküman Kontrol ekranında ![ref178]butonu tıklanılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_960.png)

Açılan Kontrol Ret ekranın ret nedeni yazılarak  varsa ret nedeni ile ilgili ek dosya yükleme işlemi yapılarak doküman hazırlayan kişi gönderilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_961.png)

Doküman Kontrol ekranında ![ref177]butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_962.png)

Sistem tarafından “Göndermek istediğinize emin misiniz?” mesajında “Tamam” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_963.png)

Doküman Kontrol ekranında  dokümanın kontrol onayından sonra doküman onay matrisinde atanan onaycıya onay işlemi için gönderilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_964.png)

Kontrol Bekleyen Doküman Listesi ekranında doküman arama sekmesinde filtre arama kriterleri olan “Doküman Kodu ” alanında doküman kodu yazılarak  ![ref29] (Ara) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_965.png)

Kontrol Bekleyen Doküman Listesi ekranında doküman listesinden yapılan filtredeki  arama kriterlerine göre kayıtlar listelenir. Kontrol Bekleyen Doküman Listesi ekranında ![ref176] (Excel’e Aktar) butonu tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_966.png)

Kontrol Bekleyen Doküman Listesi raporunun  Excel formatında raporu görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_967.png)
##### **6.2.12.5.İptal Onayı Bekleyen Doküman Listesi**
**Menü Adı**: Entegre Yönetim Sistemi/ Doküman Yönetimi/ Raporlar/ İptal Onayı Bekleyen Doküman Listesi

Hazırlanıp iptal onayına gönderilmiş dokümanların kimde/ kaç gündür iptal onayında beklediğinin listesinin ve raporunun alındığı  menüdür. İptal Onayı Bekleyen Doküman Listesi ekranında kullanıcının modül yönetici olup, olmamasına göre ekrandaki butonlar değişmektedir doküman arama ve doküman listesi sekmesi olmak üzere iki sekme karşımıza çıkar. Doküman arama sekmesinde arama kriterlerine göre filtreleme işlemi yapılır. Doküman listesinde sekmesinde  ise bu arama kriterlerine göre filtreleme işlemine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_968.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref181]:Doküman görüntüleme işlemi yapılır. Bu butonun görüntülenmesi için Sistem Altyapı Tanımları/BSAT/Konfügürasyon Ayarları/Yönetici Tanımlama menüsünde kullanıcının Doküman Yönetimi Modülünde Modül yöneticisi olarak tanımlı olması gerekmektedir. 

![ref182]:Dokümanın onay matrisi değiştirme işlemi yapılır. Bu butonun görüntülenmesi için Sistem Altyapı Tanımları/BSAT/Konfügürasyon Ayarları/Yönetici Tanımlama menüsünde kullanıcının Doküman Yönetimi Modülünde Modül yöneticisi olarak tanımlı olması gerekmektedir.

![ref183]:Dokümanın iptal onayından geri getirme işlemi yapılır. Bu butonun görüntülenmesi için Sistem Altyapı Tanımları/BSAT/Konfügürasyon Ayarları/Yönetici Tanımlama menüsünde kullanıcının Doküman Yönetimi Modülünde Modül yöneticisi olarak tanımlı olması gerekmektedir.

![ref184]: Kayıtlar filtrelenerek arama yapılır.

![ref176]: Veriler Excel’ e aktarılır.

![ref185]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref186]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref187]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

İptal Onayı Bekleyen Doküman Listesi ekranında doküman arama sekmesinde filtre arama kriterleri olan “Doküman Kodu ” alanında doküman kodu yazılarak  ![ref184] (Ara) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_976.png)

İptal Onayı Bekleyen Doküman Listesi ekranında doküman listesi sekmesinde  yapılan filtredeki  arama kriterlerine göre kayıtlar listelenir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_977.png)

İptal Onay Bekleyen Doküman Listesi ekranında ![ref188] butonu tıklanılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_979.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref189]:Kayıt işlemi yapılır.

![ref190]:Onay matrisine pozisyon ekleme işlemi yapılır.

![ref191]:Listede seçili satır silinme işlemi yapılır.

Onay Matrisi Değiştirici ekranından ![ref190]butonu tıklanarak açılan sistemde tanımlı pozisyon listesinden onay matrisine eklenecek pozisyondaki kişi ![ref192] butonu tıklanarak seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_984.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_985.png)

Onay matrisi Değiştirici ekranından ![ref191]butonu tıklanarak  onay matrisindeki pozisyonu silinme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_986.png)

Onay Matrisi Değiştirici ekranında eklenen onay matrisindeki pozisyondaki kişinin seviyesi son onaycı olduğu için  “0” olarak değiştirilir. Onay Matrisi Değiştirici ekranında  onay matrisi değiştirme işleminden sonra ekranın sol üst köşesindeki ![ref193] butonu tıklanrak onay matrisi değiştirme kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_988.png)



Sistem tarafından “Onay Matrisi başarıyla değiştirilmiştir.” mesajı verilerek  onay matrisinin değiştirme işlemi yapıldığı belirtilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_989.png)

Sistem tarafından “Onay Matrisi başarıyla değiştirilmiştir.” mesajı verilerek  onay matrisinin değiştirme işlemi yapıldığı belirtilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_990.png)

İptal Onay Bekleyen Doküman Listesi ekranında iptal işlemi onayı aşamasındaki bir doküman iptal onayından geri getirme işlemi için doküman seçili iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_991.png) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_992.png)

Sistem tarafından “Doküman iptal onayından geri getirilecektir” mesajında “Tamam” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_993.png)

Sistem tarafından “Doküman iptal onayından geri getirilmiştir.” mesajı verilerek dokümanın iptal onayından geri getirme işlemi yapılır.





![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_994.png)

İptal Onay Bekleyen Doküman Listesi ekranında doküman listesinde doküman seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_995.png)

İptal Onay Bekleyen Doküman Listesi ekranında  doküman seçili iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_996.png) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_997.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref194]:Doküman iptal işlemi yapılırak arşive gönderilir.

![ref195]:Doküman İptal  işlemi ret edilir.

Doküman İptal ekranında ![ref195] butonu tıklanılır.Açılan Doküman İptal-Onay Ret ekranında ret nedeni yazılarak ve ret nedeni ile ilgili varsa ek dosya yükleme işlemi yapılarak doküman iptal onayının ret edilme işlemi yapılır. Reddedilen doküman hazırlayan/revize eden kişiye geri gönderilme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1000.png)

Doküman iptal ekranında  ona verecek kişi 341 numaralı “Doküman İptal Onayında Ek Açıklama Girilsin mi?” parametresine bağlı olarak görüntülenen “Onay Verecek Kişinin Açıklaması”  alanında açıklama bilgisini yazarak dokümanın ![ref194] butonu tıklanarak dokümanın iptal işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1001.png)

Sistem tarafından “Göndermek istediğinize emin misiniz?” mesajında “Tamam” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1002.png)

Sistem tarafından “Doküman iptal onayı tamamlanarak arşive gönderilmiştir.”  mesajı verilerek doküman iptal onayının işleminin yapıldığı belirtilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1003.png)

İptal Onayı Bekleyen Doküman listesinde ekranında kullanıcının  ![ref196],![ref197] ve ![ref198] butonların görüntülemesi ve bu işlemleri yapması için Doküman Yönetimi modülünde modül yönetici olarak tanımlı olması gerekmektedir.

İptal Onay Bekleyen Doküman Listesi ekranında doküman listesinde doküman seçili iken ![ref176] (Excel Aktar) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1007.png)

İptal Onay Bekleyen Doküman Listesi raporunun Excel formatında raporu görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1008.png)
##### **6.2.12.6.Doküman İzleme Raporu**
**Menü Adı**: Entegre Yönetim Sistemi/ Doküman Yönetimi/ Raporlar/ Doküman İzleme Raporu

Dağıtımı yapılmış dokümanların kimler tarafından okunduğu/ okunmadığı izlendiği menüdür. Bu rapor ile kime hangi tarihte okuma görevi atandığı, dokümanın okunma tarihi, kaç gündür dokümanın okuma görevinde beklediği, eğer anket kullanıldıysa anket sonuçları ya da dokümanın kaç günde okunduğu bilgisi görüntülenir.Doküman İzleme Raporu ekranında doküman arama ve doküman listesi sekmesi olmak üzere iki sekme karşımıza çıkar. Doküman arama sekmesinde arama kriterlerine göre filtreleme işlemi yapılır. Doküman listesinde sekmesinde  ise bu arama kriterlerine göre filtreleme işlemine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1009.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref199] :Listede seçili dokümanla ilgili oluşturulan anketin sonuçları görüntülenir.

![ref184]: Kayıtlar filtrelenerek arama yapılır.

![ref176]: Veriler Excel’ e aktarılır.

![ref185]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref186]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref187]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Doküman İzleme Raporu ekranında doküman arama sekmesinde filtre arama kriterlerinden olan “Doküman Kodu ” alanında doküman kodu yazılarak  ve statüsü “okuyan” olarak seçilerek     ![ref184] (Ara) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1011.png)

Doküman İzleme Raporu ekranında doküman listesi sekmesinde yapılan filtredeki  arama kriterlerine göre kayıtlar listelenir. 






![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1012.png)

Doküman İzleme Raporu ekranında ![ref199] butonu ile dokümanla ilgili oluşturulan anketin sonuçları görüntülenebilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1013.png)

Doküman İzleme Raporu ekranında ![ref200] (Excel Aktar) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1015.png)

Doküman İzleme raporunun Excel formatında raporu görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1016.png)
##### **6.2.12.7.Hazır Formlar Listesi**
**Menü Adı**: Entegre Yönetim Sistemi/ Doküman Yönetimi/ Raporlar/ Hazır Formlar Listesi

Sistemde tanımlı olan formların  ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1017.png)  butonu tıklanarak belirlenen kişilere gönderildiği menüdür. Hazır Formlar listesi ekranında doküman arama ve doküman listesi sekmesi olmak üzere iki sekme karşımıza çıkar. Doküman arama sekmesinde arama kriterlerine göre filtreleme işlemi yapılır. Doküman listesinde sekmesinde  ise bu arama kriterlerine göre filtreleme işlemine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1018.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref201]: Listede seçili formun hazır form gönderme ekranı görüntülenir.

![ref184]: Kayıtlar filtrelenerek arama yapılır.

![ref176]: Veriler Excel’ e aktarılır.

![ref185]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref186]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref187]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Hazır Formlar listesi  ekranında doküman arama sekmesinde filtre arama kriterleri olan “Doküman Kodu ” alanında doküman kodu yazılarak  ![ref202] (Ara) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1021.png)

Hazır Formlar listesi  ekranında doküman listesi sekmesinde yapılan filtredeki  arama kriterlerine göre kayıtlar listelenir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1022.png)

Hazır Formlar ekranında listede form seçili iken ![ref201] butonuna tıklanarak hazır form gönderme ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1023.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref203]: Önceki ekrana geri dönülür.

![ref204]: Dosya hazırla butonu ile form bilgisayar indirilir.

![ref205]: Kontrollü Kopya hazırlanır.

![ref206]: İndirilen form dosya ekle butonu ile sisteme yüklenir

![ref207]: Mail gönderilecek kişilere mail gönderilir.

Hazır Formlar ekranında ![ref204] butonu tıklanarak form kullanıcının bilgisayarına indirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1029.png)

İndirilen Form doldurulur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1030.png)

Doldurulan Form ![ref208]butonu ile Qdms sistemine geri yüklenir.



![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1032.png)

Dosya Ekle ekranında Gözat butonu tıklanarak doldurulan dosyanın seçim işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1033.png)

Sistem tarafından “Dosya başarıyla aktarılmıştır” mesajı verilir.


![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1034.png)

Dosya aktarılma işleminde sonra mail  Gönderilecek kişiler alanında kullanıcı/kullanıcı grubu/ müşteri/tederikçi alanlarında ve istenirse mailde mail adresi yazılarak  mail gönderilecek kişiler belirlenir. Hazır Form Gönderme ekranında ![ref209]  butonu ile mail gönderilecek kişilere gönderilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1036.png)

Sistem tarafından “Dosya ilgili kişilere başarıyla gönderilmiştir.” mesajı verilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1037.png)

Hazır Formlar Listesi ekranında  ![ref210] (Excel Aktar) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1039.png)Hazır Formlar Listesinin Excel formatında raporu görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1040.png)
##### **6.2.12.8.Askıya Alınan Dokümanlar**
**Menü Adı**: Entegre Yönetim Sistemi/ Doküman Yönetim/ Raporlar/ Askıya Alınan Dokümanlar

Sistemde askıya alınan dokümanların listesi görüntülenip, Excel formatından raporunun alındığı menüdür. Askıya Alınan Dokümanlar ekranında doküman arama ve doküman listesi sekmesi olmak üzere iki sekme karşımıza çıkar. Doküman Arama sekmesinde arama kriterlerine göre filtreleme işlemi yapılır. Doküman listesinde sekmesinde  ise bu arama kriterlerine göre filtreleme işlemine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1041.png) **Ekranda bulunan butonlar yardımıyla;**

![ref211]: Kayıtlar filtrelenerek arama yapılır.

![ref212]: Veriler Excel’ e aktarılır.

![ref213]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref214]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref215]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Askıya Alınan Dokümanlar ekranında doküman arama sekmesinde filtre arama kriterleri olan “Doküman Kodu ” alanında doküman kodu yazılarak  ![ref211] (Ara) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1047.png)

Askıya Alınan Dokümanlar ekranında doküman Listesi sekmesinde yapılan filtredeki  arama kriterlerine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1048.png) Askıya Alınan Dokümanlar ekranında ![ref212] (Excel’e Aktar) butonu tıklanarak Askıya Alınan Dokümanlar listesinin Excel formatından raporu alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1049.png)
##### **6.2.12.9.İptal Edilen Dokümanlar Listesi**
**Menü Adı**: Entegre Yönetim Sistemi/ Doküman Yönetimi/ Raporlar/ İptal Edilen Dokümanlar Listesi

Sistemde iptal edilen dokümanların listesi görüntülenip, Excel formatından raporunun alındığı menüdür. İptal Edilen Dokümanlar Listesi ekranında doküman arama ve doküman listesi sekmesi olmak üzere iki sekme karşımıza çıkar. Doküman arama sekmesinde arama kriterlerine göre filtreleme işlemi yapılır. Doküman listesinde sekmesinde  ise bu arama kriterlerine göre filtreleme işlemine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1050.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref216]: Listede seçili doküman görüntülenir.

![ref217]: Listede seçili dokümanın iptal nedeni bilgisi görüntülenir

![ref218]:Listede seçili dokümanın onay geçmiş ile ilgili bilgileri görüntülenir.Parametreye bağlı olarak görüntülenen bir butondur.Doküman Yönetimi Modülü parametrelerinde 326 numaralı “İptal Edilen Doküman Listesi Raporunda tarihçe gösterilsin mi?” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1054.png)

Parametre aktif edildikten sonra İptal Edilen Dokümanlar Listesi ekranında Tarihçe butonu görüntülenir.

![ref211]: Kayıtlar filtrelenerek arama yapılır.

![ref212]: Veriler Excel’ e aktarılır.

![ref213]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref214]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref215]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

İptal Edilen Dokümanlar Listesi ekranında doküman arama sekmesinde filtre arama kriterleri olan “Doküman Kodu ” alanında doküman kodu yazılarak  ![ref211] (Ara) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1055.png)

İptal Edilen Dokümanlar Listesi ekranında doküman listesi sekmesinde  yapılan filtredeki  arama kriterlerine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1056.png)

İptal Edilen Dokümanlar Listesi ekranında listede iptal edilen doküman seçili  iken ![ref216] butonu tıklanarak dokümanın görüntüleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1057.png)

İptal Edilen Dokümanlar Listesi ekranında listede iptal edilen doküman seçili  iken ![ref217] butonu tıklanılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1058.png)

İptal Edilen Dokümanlar Listesi ekranında dokümanın iptal nedeni bilgisinin görüntüleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1059.png)

İptal Edilen Dokümanlar Listesi ekranında listede iptal edilen doküman seçili  iken ![ref218] butonu tıklanılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1060.png)

İptal edilen dokümanın onay geçmişi ile ilgili bilgileri görüntülenir. Onay matrisinde atanan iptal işlemi yapan kullanıcının adı ve soyadı, işlemin yapıldığı tarih, saat  ve iptal nedeni bilgilerine tarihçe kısmından ulaşılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1061.png)

İptal Edilen Dokümanlar Listesi ekranında listede iptal edilen doküman seçili iken ![ref212] (Excel’e Aktar) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1062.png)

İptal Edilen Dokümanlar Listesi ekranın Excel formatından İptal edilen Dokümanın raporu alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1063.png)
##### **6.2.12.10.Taslak Doküman Listesi**
**Menü Adı**: Entegre Yönetim Sistemi/ Doküman Yönetimi/ Raporlar/ Taslak Doküman Listesi

Dokümanların durum bilgileri kontrol edildiği, dokümanların hangi statüde olduğu bilgisine erişildiği ve Excel formatında raporunun alındığı menüdür. Taslak Doküman Listesi ekranında kullanıcının modül yönetici olup, olmamasına göre ekrandaki butonlar değişmektedir.Taslak Doküman Listesi ekranında doküman arama ve doküman listesi sekmesi olmak üzere iki sekme karşımıza çıkar. Doküman arama sekmesinde arama kriterlerine göre filtreleme işlemi yapılır. Doküman listesinde sekmesinde  ise bu arama kriterlerine göre filtreleme işlemine göre kayıtlar listelenir.

**Taslak doküman Listesi menüsünde durum kısmı “Saklanan” olan dokümanda yapılan işlemler;**

Taslak Doküman listesinde doküman arama sekmesinde arama kriterlerinde “Taslak” durumundaki dokümanın kod bilgisi yazılarak ![ref219] (Ara) butonu tıklanarak doküman listesinde  dokümanın listede görüntülenmesi sağlanır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1065.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref220]:Listede seçili dokümanın görüntüleme işlemi yapılır.

![ref221]:Listede seçili statüsü görüş aşamasındaki dokümandaki görüşcüleri verdiği görüşleri görüntüleme işlem yapılır.

![ref222]: Listede seçili dokümanın personeli değiştirilme işlemi yapılır. Bu butonun görüntülenmesi için kullanıcıların Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Yönetici Tanımlama menüsünde  Doküman Yönetimi Modülünde modül yöneticisi olarak tanımlı olması gerekmektedir.

![ref223]:Listede seçili dokümanda kullanıcı grubunun değiştirilme işlemi yapılır. Bu butonun görüntülenmesi için kullanıcıların Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Yönetici Tanımlama menüsünde  Doküman Yönetimi Modülünde modül yöneticisi olarak tanımlı olması gerekmektedir.

![ref224]:Listede seçili dokümanın silinme işlemi yapılır. Eğer yeni hazırlanan bir dokümansa taslak dokümanın silinmesine, eğer revizyonda olan bir dokümansa revizyon sürecinin silinip, dokümanın eski haline geri getirilmesine olanak sağlanır. Bu butonun görüntülenmesi için kullanıcıların Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Yönetici Tanımlama menüsünde  Doküman Yönetimi Modülünde modül yöneticisi olarak tanımlı olması gerekmektedir.

![ref225]:Listede seçili dokümanda kapak yazdırma işlemi yapılır.

![ref226]:Listede seçili dokümanın yazdırma işlemi yapılır.

![ref227]:Listede seçili görüş statüsündeki  dokümanın görüşten geri gönderme işlemi yapılır.Görüşten geri gönderilme işlemi yapılan dokümanın  durumu “Görüşten Dönen”statüsü olur.

![ref228]:Listede seçili görüş statüsündeki  dokümana pozisyon  ve kullanıcı grubu listesinde görüşcü ekleme ve silme işlemleri yapılarak görüş düzenleme işlemi yapılır.

![ref211]: Kayıtlar filtrelenerek arama yapılır.

![ref212]: Veriler Excel’ e aktarılır.

![ref213]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref214]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref215]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1075.png)

Taslak Dokümanlar listesi ekranında durumu “Saklanan” olan doküman seçili iken ![ref220] butonu tıklanarak dokümanı görüntüleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1076.png)

Taslak Dokümanlar listesi ekranında durumu “Saklanan” olan doküman seçili iken ![ref222] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1077.png)

Açılan sistemde tanımlı Personel listesinde personel seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1078.png) butonu tıklanılır.  

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1079.png)

Dokümanın hazırlayan/Revize eden kişisinin değiştirilme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1080.png)

Taslak Dokümanlar listesi ekranında durumu “Saklanan” olan doküman seçili iken ![ref225] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1081.png)

Saklanan statüsündeki dokümanın kapak yazdırılma işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1082.png)

Taslak Dokümanlar listesi ekranında durumu “Saklanan” olan doküman seçili iken ![ref226] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1083.png)

Açılan ekranda ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1084.png) butonu tıklanarak dokümanın yazdırılma işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1085.png)

Taslak Dokümanlar listesi ekranında durumu “Saklanan” olan doküman seçili iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1086.png) butonu tıklanarak dokümanı silinme  işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1087.png)

Sistem tarafından “Seçili kaydı silmek istediğniz emin misiniz?” mesajında “Tamam” butonu tıklanarak dokümanı silinme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1088.png)

Taslak Dokümanlar listesi ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1089.png)(Excel’e Aktar) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1090.png)

“Taslak Doküman Listesi” raporu Excel formatında görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1091.png)

**Taslak doküman Listesi menüsünde durum kısmı “Görüş” olan dokümanda yapılan işlemler;**

Taslak Doküman listesinde doküman arama sekmesinde arama kriterlerinde “Görüş” durumundaki dokümanın kod bilgisi yazılarak ![ref219] (Ara) butonu tıklanarak doküman listesinde  dokümanın listede görüntülenmesi sağlanır. 

![ref229]

**Ekranda bulunan butonlar yardımıyla;**

![ref220]:Listede seçili dokümanın görüntüleme işlemi yapılır.

![ref221]:Listede seçili statüsü görüş aşamasındaki dokümandaki görüşcüleri verdiği görüşleri görüntüleme işlem yapılır.

![ref222]: Listede seçili dokümanın personeli değiştirilme işlemi yapılır. Bu butonun görüntülenmesi için kullanıcıların Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Yönetici Tanımlama menüsünde  Doküman Yönetimi Modülünde modül yöneticisi olarak tanımlı olması gerekmektedir.

![ref223]:Listede seçili dokümanda kullanıcı grubunun değiştirilme işlemi yapılır. Bu butonun görüntülenmesi için kullanıcıların Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Yönetici Tanımlama menüsünde  Doküman Yönetimi Modülünde modül yöneticisi olarak tanımlı olması gerekmektedir.

![ref224]:Listede seçili dokümanın silinme işlemi yapılır.Eğer yeni hazırlanan bir dokümansa taslak dokümanın silinmesine, eğer revizyonda olan bir dokümansa revizyon sürecinin silinip, dokümanın eski haline geri getirilmesine olanak sağlanır. Bu butonun görüntülenmesi için kullanıcıların Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Yönetici Tanımlama menüsünde  Doküman Yönetimi Modülünde modül yöneticisi olarak tanımlı olması gerekmektedir.

![ref225]:Listede seçili dokümanda kapak yazdırma işlemi yapılır.

![ref226]:Listede seçili dokümanın yazdırma işlemi yapılır.

![ref227]:Listede seçili görüş statüsündeki  dokümanın görüşten geri gönderme işlemi yapılır.Görüşten geri gönderilme işlemi yapılan dokümanın  durumu “Görüşten Dönen”statüsü olur.

![ref228]:Listede seçili görüş statüsündeki  dokümana pozisyon ve kullanıcı grubu listesinde görüşcü ekleme ve silme işlemleri yapılarak görüş düzenleme işlemi yapılır.

![ref211]: Kayıtlar filtrelenerek arama yapılır.

![ref212]: Veriler Excel’ e aktarılır.

![ref213]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref214]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref215]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Listede seçili “Görüş” aşamasındaki dokümanda ![ref220] butonu ile dokümanın görüntüleme işlemi, ![ref222] butonu ile personelin değiştirme işlemi , ![ref224]  butonu ile dokümanın silinme işlemi , ![ref230] butonu ile dokümanın yazdırma işlemi ve ![ref231] butonu ile de kapak yazdırma işlemleri statüsü saklanan dokümandaki gibidir.

Taslak Dokümanlar listesi ekranında durumu “Görüş” olan doküman seçili iken ![ref228] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1095.png)

Açılan Görüş Düzenleme ekranında pozisyon ve kullanıcı grubu listesinde görüşcü ekleme,  silme işlemleri yapılarak görüş düzenleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1096.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref72]: Listeye kullanıcı grubu eklenir.

![ref55] : Listeye pozisyon eklenir.

![ref56] :Listede seçili olan görüş pozisyonunu siler. 

Görüş Düzenleme  ekranında Görüş  matrisi sekmesinde görüş  matrisine görüşcü ekleme işlemi için ![ref22] butonu tıklanılır. Açılan sistemde tanımlı pozisyon listesinde pozisyon seçimi yapılarak ![ref71]  butonu tıklanarak yapılır

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1097.png)

Görüş Düzenleme ekranında görüşcü ekleme işleminden sonra devan politikasının düzenleme işlemi yapılarak ekranın sol üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1098.png) butonu tıklanarak görüş düzenleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1099.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1100.png)

Taslak Dokümanlar listesi ekranında durumu “Görüş” olan doküman seçili iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1101.png) butonu tıklanarak görüşten geri gönderilme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1102.png)

Sistem tarafından “Seçilen doküman görüşten geri gönderilmiştir.” mesajı verilerek dokümanın görüşten geri gönderilme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1103.png)

**Taslak doküman listesi menüsünde durum kısmı “Görüş Dönen” olan dokümanda yapılan işlemler;**

Taslak Doküman listesinde doküman arama sekmesinde arama ktriterlerinde “Görüş Dönen” durumundaki dokümanın kod bilgisi yazılarak ![ref219] (Ara) butonu tıklanarak doküman listesinde  dokümanın listede görüntülenmesi sağlanır. 

![ref229]

**Ekranda bulunan butonlar yardımıyla;**

![ref220]:Listede seçili dokümanın görüntüleme işlemi yapılır.

![ref221]:Listede seçili statüsü görüş aşamasındaki dokümandaki görüşcüleri verdiği görüşleri görüntüleme işlem yapılır.

![ref222]: Listede seçili dokümanın personeli değiştirilme işlemi yapılır. Bu butonun görüntülenmesi için kullanıcıların Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Yönetici Tanımlama menüsünde  Doküman Yönetimi Modülünde modül yöneticisi olarak tanımlı olması gerekmektedir.

![ref223]:Listede seçili dokümanda kullanıcı grubunun değiştirilme işlemi yapılır. Bu butonun görüntülenmesi için kullanıcıların Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Yönetici Tanımlama menüsünde  Doküman Yönetimi Modülünde modül yöneticisi olarak tanımlı olması gerekmektedir.

![ref224]:Listede seçili dokümanın silinme işlemi yapılır.Eğer yeni hazırlanan bir dokümansa taslak dokümanın silinmesine, eğer revizyonda olan bir dokümansa revizyon sürecinin silinip, dokümanın eski haline geri getirilmesine olanak sağlanır. Bu butonun görüntülenmesi için kullanıcıların Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Yönetici Tanımlama menüsünde  Doküman Yönetimi Modülünde modül yöneticisi olarak tanımlı olması gerekmektedir.

![ref225]:Listede seçili dokümanda kapak yazdırma işlemi yapılır.

![ref226]:Listede seçili dokümanın yazdırma işlemi yapılır.

![ref227]:Listede seçili görüş statüsündeki  dokümanın görüşten geri gönderme işlemi yapılır.Görüşten geri gönderilme işlemi yapılan dokümanın  durumu “Görüşten Dönen”statüsü olur.

![ref228]:Listede seçili görüş statüsündeki  dokümana pozisyon ve kullanıcı grubu listesinde görüşcü ekleme ve silme işlemleri yapılarak görüş düzenleme işlemi yapılır.

![ref211]: Kayıtlar filtrelenerek arama yapılır.

![ref212]: Veriler Excel’ e aktarılır.

![ref213]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref214]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref215]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Listede seçili “Görüş Dönen” aşamasındaki dokümanda ![ref220] butonu ile dokümanın görüntüleme işlemi, ![ref222] butonu ile personelin değiştirme işlemi , ![ref224]  butonu ile dokümanın silinme işlemi , ![ref230] butonu ile dokümanın yazdırma işlemi ve ![ref231] butonu ile de kapak yazdırma işlemleri statüsü saklanan dokümandaki gibidir.

Taslak Dokümanlar listesi ekranında durumu “Görüş Dönen” olan doküman seçili iken ![ref221] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1104.png)

Açılan Görüşler ekranında görüş sekmesinde atanan görüşcülerin görüşleri görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1105.png)

Taslak dokümanlar listesi ekranında doküman arama sekmesinde arama kriteri olan  Taslak Durumu alanında dokümanın statü seçilerek  doküman listesi sekmesinde ilgili kayıtların listelenerek ekrandaki butonlar kullanılarak işlem aşamaları bu şekilde yapılması sağlanır.
##### **6.2.12.11.Klasör Matris Raporu**
**Menü Adı**: Entegre Yönetim Sistemi/ Doküman Yönetimi/ Raporlar/ Klasör Matris Raporu

Klasör bazlı yetki, onay, dağıtım ve görüş matrisleri görüntülendiği ve Excel formatından raporunun alındığı menüdür. Klasör bazında kontrol eden bilgilerine ulaşılır. Klasördeki dokümanların, dağıtım matrisi ile kimlere okuma görevi olarak atandığı görülür. Klasör Matris Raporu ekranında doküman arama ve doküman listesi sekmesi olmak üzere iki sekme karşımıza çıkar. Doküman arama sekmesinde arama kriterlerine göre filtreleme işlemi yapılır. Doküman listesinde sekmesinde  ise bu arama kriterlerine göre filtreleme işlemine göre kayıtlar listelenir

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1106.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref211]: Kayıtlar filtrelenerek arama yapılır.

![ref212]: Veriler Excel’ e aktarılır.

![ref213]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref214]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref215]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Klasör Matris Raporu ekranında doküman arama sekmesinde filtre arama kriterleri olan “Klasör Kodu ” alanında ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1107.png)  butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1108.png)

Açılan sistemde tanımlı Doküman Klasörü listesinde Klasör seçim işlemi yapılarak ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1109.png) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1110.png)

Doküman Arama sekmesinde arama kriterlerine göre klasör seçim işlemi yapıldıktan sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1111.png) (Ara) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1112.png)

Klasör Matris Raporu ekranında doküman listesi sekmesinde  yapılan filtredeki  arama kriterlerine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1113.png)

Klasör Matris Raporu ekranında ![ref212] (Excel’e Aktar) butonu tıklanarak Klasör Matris Raporu Excel formatından raporu alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1114.png)
##### **6.2.12.12.Doküman Matris Raporu**
**Menü Adı**: Entegre Yönetim Sistemi/ Doküman Yönetimi/ Raporlar/ Doküman Matris Raporu

Doküman bazlı yetki, onay, dağıtım , süreç matrisleri görüntülendiği ve Excel formatından raporunun alındığı menüdür. Doküman Matris Raporu ekranında doküman arama ve doküman listesi sekmesi olmak üzere iki sekme karşımıza çıkar. Doküman arama sekmesinde arama kriterlerine göre filtreleme işlemi yapılır. Doküman listesinde sekmesinde  ise bu arama kriterlerine göre filtreleme işlemine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1115.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref32]: Kayıtlar filtrelenerek arama yapılır.

![ref3]: Veriler Excel’ e aktarılır.

![ref4]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref5]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref149]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama Doküman Matris Raporu ekranında doküman arama sekmesinde filtre arama kriterleri olan “Doküman Kodu ” alanında doküman kodu yazılarak  ![ref29] (Ara) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1116.png)

Doküman Matris Raporu ekranında doküman listesi sekmesinde  yapılan filtredeki  arama kriterlerine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1117.png)

Doküman Matris Raporu ekranında ![ref212] (Excel’e Aktar) butonu tıklanarak Doküman Matris Raporu Excel formatından raporu alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1118.png)
##### **6.2.12.13.Doküman Gözden Geçirme Listesi**
**Menü Adı**: Entegre Yönetim Sistemi/ Doküman Yönetimi/ Raporlar/ Doküman Gözden Geçirme Listesi

Dokümanların gözden geçirilip geçirilmediğinin takibinin yapıldığı ve Excel formatında raporunun alındığı menüdür. Doküman Gözden Geçirme Raporu ile klasörde/ dokümanda belirlenen gözden geçirme periyotlarına göre gözden geçirilme zamanı gelen dokümanların listesine ulaşılır. Doküman Gözden Geçirme Listesi ekranında kullanıcının modül yönetici olup, olmamasına göre ekrandaki butonlar değişmektedir. Bu menüde Modül Yöneticisi Doküman  Yönetimi modülünde Doküman Gözden Geçirme Listesi ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1119.png)butonu yardımıyla gözden geçirme sorumlu personeli değiştirebilir. Ayrıca Modül Yöneticisi Doküman Yönetimi modülünde Doküman Gözden Geçirme Listesi ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1120.png)butonu yardımıyla yönlendirme işlemini iptal edebilir. Doküman Gözden Geçirme Listesi ekranında doküman arama ve doküman listesi sekmesi olmak üzere iki sekme karşımıza çıkar. Doküman arama sekmesinde arama kriterlerine göre filtreleme işlemi yapılır. Doküman listesinde sekmesinde  ise bu arama kriterlerine göre filtreleme işlemine göre kayıtlar listelenir. Doküman arama sekmesinden “Gözden Geçirilen” veya “Gözden Geçirilmeyen” dokümanlar seçilerek listelenebilir

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1121.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref232] :Listede seçili doküman için gözden geçirme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1123.png) : Listede seçili dokümanın gözden geçirme sorumlu personeli değiştirilir. Bu butonun görüntülenmesi için kullanıcıların Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Yönetici Tanımlama menüsünde  Doküman Yönetimi modülünde modül yöneticisi olarak tanımlı olması gerekmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1124.png): Listede seçili dokümanın gözden geçirme işleminde yapılan yönlendirme işleminin iptal edilmesi yapılır. Bu butonun görüntülenmesi için kullanıcıların Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Yönetici Tanımlama menüsünde  Doküman Yönetimi modülünde modül yöneticisi olarak tanımlı olması gerekmektedir.

![ref184]: Kayıtlar filtrelenerek arama yapılır.

![ref176]: Veriler Excel’ e aktarılır.

![ref185]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref186]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref187]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1125.png): Listede seçili dokümanın gözden geçirme geçmişi aktarılır.

Doküman Gözden Geçirme Listesi ekranında doküman arama sekmesinde filtre arama kriterleri olan “Doküman Kodu ” alanında doküman kodu yazılarak  ![ref202] (Ara) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1126.png)

Doküman Gözden Geçirme Listesi ekranında doküman listesi sekmesinde  yapılan filtredeki  arama kriterlerine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1127.png)

Doküman Gözden Geçirme Listesi ekranında doküman listesinde doküman seçili iken ![ref232] butonu tıklanılır. Açılan   Doküman Gözden Geçirme ekranında dokümanın gözden geçirme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1128.png)

**Ekranda bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1129.png):Gözden geçirme işlemi uygun görülme işlemi yapılır.

![ref233]:Gözden geçirme işlemi öteleme işlemi ay bazında yapılır. Parametreye bağlı olarak görüntülenen bir butondur. Doküman Yönetimi parametrelerinde 347 numaralı “	Gözden geçirmede öteleme kullanılacak mı ?” parametresi değeri “Evet” seçilerek  parametre “Aktif” edilir. 

![ref234]

Parametre aktif edildikten sonra gözden geçirme ekranında  bu buton görüntülenerek gözden geçirme işlemi ay bazında öteleme işlemi yapılır.

![ref235]:Doküman gözden geçirme ekranında doküman görüntülenir.

![ref236]: Doküman gözden geçirme ekranında yapılan gözden geçirme sonucunda dokümanla ilgili revizyon başlatılır.

![ref237]: Doküman gözden geçirme ekranında gözden geçirme başka pozisyona yönlendirilir.

![ref238]: Doküman gözden geçirme ekranında dokümanla ilgili revizyon talebi yapılır.

![ref239]:Yapılan gözden geçirme sonucunda iptal işlemi başlatılır. 

Doküman Gözden Geçirme ekranın doküman geçirme ile ilgili açıklama  bilgisi, Gözden geçilerek mi? alanında gözden geçirilecek seçeneği seçilerek ve gözden geçirme periyotu ay bazında seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1137.png) butonu tıklanarak doküman gözden geçirme kayıt işlemi yapılır.

Doküman Gözden Geçirme ekranından ![ref233] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1138.png)

Açılan Gözden Geçirme Öteleme ekranında istenirse Öteleme süresi ay olarak seçim işlemi açılır listeden seçilerek   ekranın sol üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1139.png)buton tıklanılarak  gözden geçirme işlemi yapılır. Öteleme süresi Sistem Altyapı Tanımları/Doküman İşlemleri/ Gözden Geçirme Öteleme Süresi  Tanımlama menüsünde tanımlı seçeneklerin listesinde gelmektedir. Listeden ilgili seçenek seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1140.png)

Doküman Gözden Geçirme ekranından ![ref235] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1141.png)

Doküman Gözden Geçirme ekranından ![ref235] butonu tıklanıldıktan sonra dokümanın görüntüleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1142.png)

Doküman Gözden Geçirme ekranından ![ref237] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1143.png)

Doküman Gözden Geçirme  Yönlendirme ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1144.png)

Bu aşamada  kullanıcılar isterse açılan Doküman Gözden Geçirme Yönlendirme ekranında Yönlendirilecek alanında ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1145.png) butonu tıklanarak açılan sistemde tanımlı pozisyon listesinden yönlendirilecek pozisyondaki kişi seçilme işlemi  ve  doküman gözden geçirme yönlendirme işlemi notlar alanında varsa açıklama bilgisi yazarak gerekli alanlar ilgili bilgiler  girildikten sonra ekranın sol üst köşesindeki ![ref240]butonu tıklanarak  doküman gözden geçirme yönlendirme işlemi kayıt işlemi yapabilir. 

Doküman Gözden Geçirme ekranından ![ref238] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1147.png)

Doküman Revizyon Talebi ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1148.png)

Kullanıcılar isterlerse bu aşamada  Doküman revizyon Talebi ekranında  Talep açıklaması bilgisi yazarak ve varsa doküman  revizyon talebi  ile ilgili talep açıklama bilgisi yazılır. Doküman  revizyon talebi  ile ek dosya varsa yükleme işlemi yaparak gerekli alanlar ilgili bilgiler girerek ekranın sol üst köşesindeki ![ref240]butonu tıklayarak Doküman revizyon talebi kayıt işlemi yapabilir.

Doküman Gözden Geçirme ekranından ![ref239] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1149.png)

Sistem tarafından “Dokumanı İptal Etmek istediğinize emin misiniz?” mesajında “Tamam” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1150.png)

Kullanıcılar isterlerse açılan Doküman İptal ekranında  İptal nedeni alanında dokümanın iptal nedeni bilgisini yazarak ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1151.png) butonu tıklayarak onay matrisinde atanan kişinin iptal onayına doküman gönderilir. İptal işlemi Doküman iptal  menüsünün işlem aşamaları  aynı şekilde olmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1152.png)

Doküman Gözden Geçirme ekranından ![ref236] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1153.png)

Sistem tarafından “Doküman revizyon işlemlerini başlatmak istediğinizden emin misiniz?” mesajında “Tamam” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1154.png)

Açılan Doküman Revizyon ekranında sistem tarafından “**Doküman başarıyla kaydedildi. Revizyon işlemleri başlamıştır.” mesajı verilerek dokümanın revizyon işleminin başladığı belirtirilir.**

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1155.png)

Açılan Doküman Revizyon ekranında revizyon işlemi aynı doküman revizyon menüsünde yapılan işlem basamakları ile  aynı aşamalardan geçmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1156.png)

Doküman Gözden Geçirme ekranından listede doküman seçili iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1157.png) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1158.png)

Açılan sistemde tanımlı pozisyon listesinde değiştirilecek sorumlu olarak seçilecek pozisyondaki kişi seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1159.png) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1160.png)

Sorumlu değiştirme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1161.png)

Doküman Gözden Geçirme ekranından ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1162.png) butonu tıklanarak listede seçili dokümanın gözden geçirme işleminde yapılan yönlendirme işleminin iptal edilmesi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1163.png)

Yönlendirme işlemini iptal işleminin yapılması için Doküman Gözden Geçirme ekranında önceden yönlendirme işleminin yapılması gerekmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1164.png)

Doküman Gözden Geçirme Listesi ekranında ![ref176] (Excel’e Aktar) butonu  tıklanılır. ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1165.png)

“Doküman Gözden Geçirme Listesi Raporu” Excel formatında görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1166.png)

Doküman Gözden Geçirme Listesi ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1167.png) (Gözden Geçirme Geçmişi Aktar) butonu  tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1168.png)

“Doküman Gözden Geçirme Geçmişi ” Excel formatında görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1169.png)
##### **6.2.12.14.Doküman Yönetim Sistemi Listesi**
**Menü Adı**: Entegre Yönetim Sistemi/ Doküman Yönetimi/Raporlar/ Doküman Yönetim Sistemi Listesi

Dokümanlar ile ilişkilendiren standart madde numaralarının listesini görüntülendiği ve Excel formatından raporu alındığı menüdür. Doküman Yönetim Sistemi Listesi ekranında doküman arama ve doküman listesi sekmesi olmak üzere iki sekme karşımıza çıkar. Doküman Yönetim Sistemi Listesi ekranında Doküman arama sekmesinde arama kriterlerine göre filtreleme işlemi yapılır. Doküman listesinde sekmesinde  ise bu arama kriterlerine göre filtreleme işlemine göre kayıtlar listelenir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1170.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref184]: Kayıtlar filtrelenerek arama yapılır.

![ref176]: Veriler Excel’ e aktarılır.

![ref185]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref186]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref187]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip-gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Doküman Yönetim Sistemi Listesi ekranında doküman arama sekmesinde filtre arama kriterleri olan “Sistem ” alanında  ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1171.png) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1172.png)

Açılan Madde No Seçme ekranında filtre sekmesinde arama kriteri olan yönetim sistemi seçilerek ![ref241] (Ara) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1174.png)

Seçilen yönetim sistemi madde No listesinde seçim yapılarak ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1175.png) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1176.png)

Doküman Yönetim Sistemi Listesi ekranında doküman arama sekmesinde arama kriteri  Sistem alanında Standartın madde no seçim işleminden sonra ![ref241] (Ara) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1177.png)

Doküman Yönetim Sistemi Listesi ekranında doküman arama kriterlerine göre doküman listesinde ilgili kayıtlar görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1178.png)

Doküman Yönetim Sistemi Listesinde ![ref176] (Excel Aktar) butonu tıklanarak  Doküman Yönetim Sistemi Listesininde excel formatında raporu alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1179.png)
##### **6.2.12.15.Doküman Revizyon Talep Listesi**
**Menü Adı**: Entegre Yönetim Sistemi/ Doküman Yönetimi/ Raporlar/ Doküman Revizyon Talep Listesi

Revizyon talebi olan doküman listesi görüntülendiği ve Excel formatında raporunun alındığı menüdür. Doküman Revizyon Talep Listesi ekranında doküman arama ve doküman listesi sekmesi olmak üzere iki sekme karşımıza çıkar. Doküman Revizyon Talep Listesi ekranında doküman arama sekmesinde arama kriterlerine göre filtreleme işlemi yapılır. Doküman listesinde sekmesinde  ise bu arama kriterlerine göre filtreleme işlemine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1180.png)

**Ekranda bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1181.png): Listede seçili dokümanın revizyon telep bilgileri görüntülenir.

![ref184]: Kayıtlar filtrelenerek arama yapılır.

![ref176]: Veriler Excel’ e aktarılır.

![ref185]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref186]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref187]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip-gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Doküman Revizyon Talep Listesi ekranında doküman arama sekmesinde filtre arama kriterleri olan “Doküman Kodu ” alanında doküman kodu yazılarak  ![ref29] (Ara) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1182.png)

Doküman Revizyon Talep Listesi ekranında doküman listesi sekmesinde  yapılan filtredeki  arama kriterlerine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1183.png)

Doküman Revizyon Talep Listesi ekranında doküman arama sekmesinde listede doküman seçili iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1184.png) butonu tıklanarak dokümanın talep bilgisi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1185.png)

Doküman Revizyon Talep Listesi ekranında doküman listesinde doküman seçili iken ![ref176] (Excel Aktar) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1186.png)

Doküman Revizyon Talep Listesi ekranında Excel formatında Doküman Revizyon Talep Listesi raporu alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1187.png)
##### **6.2.12.16.Doküman Sayıları**
**Menü Adı**: Entegre Yönetim Sistemi/ Doküman Yönetimi/ Raporlar/ Doküman Sayıları

Hangi klasörde kaç doküman bulunduğu bilgisine ulaşıldığı ve Excel formatında raporunun alındığı menüdür.Ekranın sol tarafından klasör seçilerek o klasörde yer alan doküman listesine ulaşılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1188.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref184]: Kayıtlar filtrelenerek arama yapılır.

![ref176]: Veriler Excel’ e aktarılır.

![ref185]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref186]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref187]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip-gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Doküman Sayıları ekranın klasör seçili iken ![ref176] (Excel Aktar) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1189.png)

Doküman Sayıları Raporu ekranında “Doküman Sayıları” raporunun Excel formatında raporu alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1190.png)
##### **6.2.12.17.Referans Doküman Raporu**
Birbirlerine referans verilmiş dokümanlar listelendiği ve Excel formatında raporunun alındığı menüdür. Referans Doküman Raporu  ekranında doküman arama ve doküman listesi sekmesi olmak üzere iki sekme karşımıza çıkar. Doküman arama sekmesinde arama kriterlerine göre filtreleme işlemi yapılır. Doküman listesinde sekmesinde  ise bu arama kriterlerine göre filtreleme işlemine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1191.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref184]: Kayıtlar filtrelenerek arama yapılır.

![ref176]: Veriler Excel’ e aktarılır.

![ref185]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref186]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref187]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip-gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Sistem Doküman Referans Listesi ekranında doküman arama sekmesinde filtre arama kriterleri olan “Doküman Kodu ” alanında doküman kodu yazılarak  ![ref211] (Ara) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1192.png)

Sistem Doküman Referans Listesi ekranında doküman listesi sekmesinde  yapılan filtredeki  arama kriterlerine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1193.png)Sistem Doküman Referans Listesi ekranında  ![ref176] (Excel Aktar) butonu tıklanarak Excel formatında Sistem Doküman Referans listesi raporu alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1194.png)
##### **6.2.12.18.Doküman Onay Süreleri Raporu**
**Menü Adı**: Entegre Yönetim Sistemi/ Doküman Yönetimi/ Raporlar/ Doküman Onay Süreleri Raporu

Dokümana ait onay süreleri (gün), onay tarihleri ve onaycı bilgilerinin bulunduğu listesinin  alındığı ve Excel formatından raporunun alındığı menüdür. Doküman Onay Süreleri Raporu  ekranında doküman arama ve doküman listesi sekmesi olmak üzere iki sekme karşımıza çıkar. Doküman arama sekmesinde arama kriterlerine göre filtreleme işlemi yapılır. Doküman listesinde sekmesinde  ise bu arama kriterlerine göre filtreleme işlemine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1195.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref184]: Kayıtlar filtrelenerek arama yapılır.

![ref176] : Veriler Excel’ e aktarılır.

![ref185]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref186]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref187]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip-gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Doküman Onay Süreleri Raporu ekranında doküman arama sekmesinde filtre arama kriterleri olan “Doküman Kodu ” alanında doküman kodu yazılarak  ![ref211] (Ara) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1196.png)

Doküman Onay Süreleri Raporu ekranında doküman listesi sekmesinde  yapılan filtredeki  arama kriterlerine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1197.png)

Doküman Onay Süreleri Raporu ekranında ![ref176] (Excel Aktar) butonu tıklanılarak  Doküman Onay Süreleri Raporunun Excel formatında raporu alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1198.png)
##### **6.2.12.19.Gelişmiş Doküman İzleme Raporu**
**Menü Adı**: Entegre Yönetim Sistemi/ Doküman Yönetimi/ Raporlar/ Gelişmiş Doküman İzleme Raporu

Dokümanlar üzerinde yapılan tüm işlem bilgilerine, IP ve saat detaylarıyla ulaşılabildiği ve Excel formatında raporunun alındığı menüdür. Bu rapor log tutan bir rapordur. Kimin hangi saatte doküman ile ilgili hangi IP’den ne yaptığını detaylı bir şekilde çıkartabilir. Gelişmiş Doküman İzleme Raporu ekranında doküman arama ve doküman listesi sekmesi olmak üzere iki sekme karşımıza çıkar. Doküman Arama sekmesinde arama kriterlerine göre filtreleme işlemi yapılır. Doküman listesinde sekmesinde  ise bu arama kriterlerine göre filtreleme işlemine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1199.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref184]: Kayıtlar filtrelenerek arama yapılır.

![ref176]: Veriler Excel’ e aktarılır.

![ref185]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref186]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref187]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip-gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Gelişmiş Doküman İzleme Raporu ekranında doküman arama sekmesinde filtre arama kriterleri olan “Doküman Kodu ” alanında doküman kodu yazılarak ve işlem tipi alanında ilgili alanlar ilgili check box’lar seçilerek   ![ref211] (Ara) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1200.png)

Gelişmiş Doküman İzleme Raporu ekranında doküman listesi sekmesinde  yapılan filtredeki  arama kriterlerine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1201.png)

Gelişmiş Doküman İzleme Raporu ekranında Excel formatında Gelişmiş Doküman İzleme Raporu alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1202.png)
##### **6.2.12.20.Hazır Dokümanlar Listesi**
**Menü Adı**: Entegre Yönetim Sistemi/ Doküman Yönetimi/ Raporlar/ Hazır Dokümanlar Listesi

QDMS’ de tanımlı dokümanlar sistemde seçilenen kullanıcılara e-posta ile gönderildiği ve Excel formatından raporunun alındığı menüdür. Hazır Dokümanlar Listesi ekranında doküman arama ve doküman listesi sekmesi olmak üzere iki sekme karşımıza çıkar. Doküman arama sekmesinde arama kriterlerine göre filtreleme işlemi yapılır. Doküman listesinde sekmesinde  ise bu arama kriterlerine göre filtreleme işlemine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1203.png)

**Ekranda bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1204.png): Listede seçili dokümanın detay bilgisi görüntülenir.

![ref184]: Kayıtlar filtrelenerek arama yapılır.

![ref242] : Veriler Excel’ e aktarılır.

![ref185]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref186]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref187]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip-gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Hazır Dokümanlar Listesi ekranında doküman arama sekmesinde filtre arama kriterleri olan “Doküman Kodu ” alanında doküman kodu yazılarak  ![ref211] (Ara) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1206.png)

Hazır Dokümanlar Listesi ekranında doküman listesi sekmesinde  yapılan filtredeki  arama kriterlerine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1207.png)

Hazır Dokümanlar Listesi ekranında doküman listesinde doküman seçili iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1208.png) butonu tıklanılır

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1209.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref243]: Önceki ekrana geri dönülür.

![ref244]: Form bilgisayar indirilir.

![ref245]: Kontrollü Kopya hazırlanır.

![ref246]: İndirilen form  sisteme yüklenir

![ref247]: Mail gönderilecek kişilere mail gönderilir.

Hazır Dokümanlar ekranında ![ref244] butonu tıklanarak doküman kullanıcının bilgisayarına indirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1215.png) 

İndirilen Doküman Düzenlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1216.png)

Düzenlenen  Doküman  ![ref248]butonu ile Qdms sistemine geri yüklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1218.png)

Düzenlenen  Doküman ![ref249]butonu ile Qdms sistemine geri yüklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1220.png)

Dosya Ekle ekranında Gözat butonu tıklanarak doldurulan dosyanın seçim işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1221.png) Sistem tarafından “Dosya başarıyla aktarılmıştır” mesajı verilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1222.png)

Dosya aktarılma işleminde sonra mail  Gönderilecek kişiler alanında kullanıcı/kullanıcı grubu/ müşteri/tdarikçi alanlarında ve istenirse mailde mail adresi yazılarak  mail gönderilecek kişiler belirlenir. Hazır Doküman  Gönderme ekranında ![ref250]  butonu ile mail gönderilecek kişilere gönderilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1224.png)

Sistem tarafından “Dosya ilgili kişilere başarıyla gönderilmiştir.” mesajı verilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1225.png)

Hazır Dokümlar Listesi ekranında doküman arama sekmesinde doküman seçili iken  ![ref242] (Excel Aktar) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1226.png)

Hazır Dokümanlar Listesi ekranında Excel formatından Hazır Dokümanlar listesinin raporu alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1227.png)
##### **6.2.12.21.Doküman Parametrik Alan Raporu**
**Menü Adı**: Entegre Yönetim Sistemi/ Doküman Yönetimi/ Raporlar/ Doküman Parametrik Alan Raporu

Klasör bazında açılan parametrik alanların listesini görüntülendiği ve Excel formatında raporun alındığı menüdür. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1228.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref184]: Kayıtlar filtrelenerek arama yapılır.

![ref242] : Veriler Excel’ e aktarılır.

![ref185]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref186]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref187]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip-gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Açılan ekranda parametrik alanları görüntülenmek istenilen klasör seçilip, ileri butonuyla klasörün içerisine girilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1229.png)

Parametrik Alan  Raporu ekranında  gelişme arama kriterleri sekmesi tıklanarak tanımlanan parametrik alanları görüntülenmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1230.png)

Parametrik Alan Raporu ekranında listelenecek alanlar sekmesinden raporda görüntülenmek istenilen bilgiler seçilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1231.png)

Parametrik Alan Raporu ekranında ![ref184] (Ara) butonu ile rapor oluşturulur. İstenildiği takdirde arama kriterleri ya da gelişmiş arama kriterleri kullanılarak filtreleme işlemi ile rapor özelleştirilebilir

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1232.png)

Parametrik Alan Raporu ekranında Doküman Listesi ekranında ![ref242] (Excel Aktar) butonu tıklanarak Parametrik Alan Raporunun Excel formatından raporu alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1233.png)
##### **6.2.12.22.Kişi Bazında Doküman Okuma Sayısı Raporu**
**Menü Adı**: Entegre Yönetim Sistemi/ Doküman Yönetimi/ Raporlar/ Kişi Bazında Doküman Okuma Sayısı Raporu 

Personellerin okuması gereken doküman sayılarını gösteren ve Excel formatında raporunun alındığı menüdür. Bu menüde kişinin okuyacağı doküman sayısı raporu elde edilmiş olur. Kişi Bazında Doküman Okuma Sayası Raporu ekranında Filtre ve doküman listesi sekmesi olmak üzere iki sekme karşımıza çıkar. Filtre sekmesinde arama kriterlerine göre filtreleme işlemi yapılır. Doküman listesinde sekmesinde  ise bu arama kriterlerine göre filtreleme işlemine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1234.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref184]: Kayıtlar filtrelenerek arama yapılır.

![ref242] : Veriler Excel’ e aktarılır.

![ref185]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref186]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref187]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip-gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Kişi Bazında Doküman Okuma Sayısı Raporu ekranında filtre sekmesinde arama kriterleri olan “Okuyacak Kişi ” alanında sistemde tanımlı personel listesinden personel seçilerek   ![ref211] (Ara) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1235.png) Kişi Bazında Doküman Okuma Sayısı Raporu ekranında doküman listesi sekmesinde  yapılan filtredeki  arama kriterlerine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1236.png)

Kişi Bazında Doküman Okuma Sayısı Raporu ekranında ![ref176] (Excel Aktar) butonu tıklarak Kişi Bazında Okuma Sayısı Raporu  Excel formatında raporu alınır.          

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1237.png)
##### **6.2.12.23.Departman Bazında Okuma Sayısı Raporu**
**Menü Adı**: Entegre Yönetim Sistemi/ Doküman Yönetimi/ Raporlar/ Departman Bazında Okuma Sayısı Raporu

Departman bazlı olarak kullanıcıların okudukları dokümanların sayısını gösteren  ve Excel formatında raporunun alındığı menüdür. Departman Bazında Okuma Sayısı Raporu  ekranında filtre ve doküman listesi sekmesi olmak üzere iki sekme karşımıza çıkar. Filtre sekmesinde arama kriterlerine göre filtreleme işlemi yapılır. Doküman listesinde sekmesinde  ise bu arama kriterlerine göre filtreleme işlemine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1238.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref184]: Kayıtlar filtrelenerek arama yapılır.

![ref242] : Veriler Excel’ e aktarılır.

![ref185]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref186]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref187]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip-gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Departman Bazında Doküman Okuma Sayısı Raporu ekranında filtre sekmesinde arama kriterleri olan “Bölüm  ” alanında sistemde tanımlı departman listesinde departman seçilerek   ![ref211] (Ara) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1239.png)

Departman Bazında Doküman Okuma Sayısı Raporu ekranında doküman listesi sekmesinde  yapılan filtredeki  arama kriterlerine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1240.png)

Departman Bazında Okuma Raporu ekranında ![ref242] (Excel Aktar) butonu tıklanarak Excel formatından Departman Bazında Okuma Raporunu alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1241.png)
##### **6.2.12.24.Ek Doküman Raporu**
**Menü Adı**: Entegre Yönetim Sistemi/ Doküman Yönetimi/ Raporlar/ Ek Doküman Raporu

Dokümanlara ek olarak verilen dokümanların listesinin görüntülendiği  ve Excel formatından raporunun alındığı menüdür. Ek Doküman Raporu  ekranında doküman arama ve doküman listesi sekmesi olmak üzere iki sekme karşımıza çıkar. Doküman arama sekmesinde arama kriterlerine göre filtreleme işlemi yapılır. Doküman listesinde sekmesinde  ise bu arama kriterlerine göre filtreleme işlemine göre kayıtlar listelenir. Doküman arama sekmesinden “Ana Dokümana Göre” mi “Ek Dokümana Göre” mi rapor oluşturulacağı kriteri seçilerek rapor oluşturulur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1242.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref184]: Kayıtlar filtrelenerek arama yapılır.

![ref242] : Veriler Excel’ e aktarılır.

![ref185]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref186]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref187]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip-gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Ek Dokümanlar Listesi ekranında doküman arama sekmesinde filtre arama kriterleri olan “Doküman Kodu ” alanında doküman kodu yazılarak  ![ref251] (Ara) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1244.png)

Ek Dokümanlar Listesi ekranında doküman listesi sekmesinde  yapılan filtredeki  arama kriterlerine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1245.png)

Ek Dokümanlar Listesi ekranında ![ref242] (Excel Aktar)  butonu tıklanarak Excel formatında Ek Dokümanlar listesi raporu alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1246.png)
##### **6.2.12.25.Ürün Doküman Raporu**
**Menü Adı**: Entegre Yönetim Sistemi/ Doküman Yönetimi/ Raporlar/ Ürün Doküman Raporu

Dokümanlara bağlı ürünlerin gösterildiği ve Excel formatında raporunun alındığı menüdür. Ürün Doküman Raporu ekranında doküman arama ve doküman listesi sekmesi olmak üzere iki sekme karşımıza çıkar. Doküman arama sekmesinde arama kriterlerine göre filtreleme işlemi yapılır. Doküman listesinde sekmesinde  ise bu arama kriterlerine göre filtreleme işlemine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1247.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref184]: Kayıtlar filtrelenerek arama yapılır.

![ref242] : Veriler Excel’ e aktarılır.

![ref185]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref186]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref187]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip-gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Ürün Doküman Raporu  ekranında doküman arama sekmesinde filtre arama kriterleri olan “Doküman Kodu ” alanında doküman kodu yazılarak  ![ref251] (Ara) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1248.png)

Doküman Ürün Raporu ekranında Doküman Listesi sekmesinde  yapılan filtredeki  arama kriterlerine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1249.png)

Ürün Doküman Raporu ekranında ![ref242] (Excel Aktar)  butonu tıklanarak Excel formatında Ürün Doküman raporu alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1250.png)
##### **6.2.12.26.Doküman Hazırlama Talep Listesi**
**Menü Adı**: Entegre Yönetim Sistemi/ Doküman Yönetimi/ Raporlar/ Doküman Hazırlama Talep Listesi

Doküman görme menüsünde kullanıcıların yaptığı doküman hazırlama taleplerinin gösterildiği  ve Excel formatından raporunun alındığı menüdür. Doküman Hazırlama Talep Listesi   ekranında doküman arama ve doküman listesi sekmesi olmak üzere iki sekme karşımıza çıkar. Doküman arama ve doküman listesi sekmesi olmak üzere iki sekme karşımıza çıkar. Doküman arama sekmesinde arama kriterlerine göre filtreleme işlemi yapılır. Doküman listesinde sekmesinde  ise bu arama kriterlerine göre filtreleme işlemine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1251.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref184]: Kayıtlar filtrelenerek arama yapılır.

![ref242] : Veriler Excel’ e aktarılır.

![ref185]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref186]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref187]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip-gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Doküman Hazırlama Talep Listesi ekranında doküman arama sekmesinde filtre arama kriterleri olan “Bağlı Olduğu Klasör ” alanında doküman klasör listesinden klasör seçilerek   ![ref251] (Ara) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1252.png)

Doküman Hazırlama Talep Listesi ekranında doküman listesi sekmesinde  yapılan filtredeki  arama kriterlerine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1253.png)

Doküman Hazırlama Talep Listesi ekranında ![ref242] (Excel Aktar)  butonu tıklanarak Excel formatında Doküman Hazırlama Talep Listesinin raporu alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1254.png)
##### **6.2.12.27.Kontrollü Kopya Talep Raporu**
**Menü Adı**: Entegre Yönetim Sistemi/ Doküman Yönetimi/ Raporlar/ Kontrollü Kopya Talep Raporu

Doküman görme menüsünde yapılan kontrollü kopya taleplerinin listelendiği  ve Excel formatından raporunun alındığı menüdür. Kontrollü Kopya Talep Raporu ekranında doküman arama ve doküman listesi sekmesi olmak üzere iki sekme karşımıza çıkar. Doküman arama sekmesinde arama kriterlerine göre filtreleme işlemi yapılır. Doküman listesinde sekmesinde  ise bu arama kriterlerine göre filtreleme işlemine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1255.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref184]: Kayıtlar filtrelenerek arama yapılır.

![ref242] : Veriler Excel’ e aktarılır.

![ref185]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref186]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref187]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip-gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Kontrollü Kopya Talep Raporu ekranında doküman arama sekmesinde filtre arama kriterleri olan “Doküman Kodu ” alanında doküman kodu yazılarak  ![ref211] (Ara) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1256.png)

Kontrollü Kopya Talep Raporu ekranında doküman listesi sekmesinde  yapılan filtredeki  arama kriterlerine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1257.png)

Kontrollü Kopya Talep Raporu ekranında ![ref242] (Excel Aktar)  butonu tıklanarak Excel formatında Kontrollü Kopya Talep raporu alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1258.png)
##### **6.2.12.28. Kontrollü Kopya Toplama Raporu**
**Menü Adı**: Entegre Yönetim Sistemi/ Doküman Yönetimi/ Raporlar/ Kontrollü Kopya Toplama Raporu

Doküman revizyonu yada iptali sebebiyle daha önce sahaya dağıtılan kontrollü kopyaların geri toplama görevlerin listelendiği ve Excel formatında raporunun alındığı menüdür. Kontrollü Kopya Toplama Raporu ekranında doküman arama ve doküman listesi sekmesi olmak üzere iki sekme karşımıza çıkar. Doküman arama sekmesinde arama kriterlerine göre filtreleme işlemi yapılır. Doküman listesinde sekmesinde  ise bu arama kriterlerine göre filtreleme işlemine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1259.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref184]: Kayıtlar filtrelenerek arama yapılır.

![ref242] : Veriler Excel’ e aktarılır.

![ref185]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref186]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref187]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip-gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Kontrollü Kopya Toplama Raporu ekranında doküman arama sekmesinde filtre arama kriterleri olan “Doküman Kodu ” alanında doküman kodu yazılarak  ![ref251] (Ara) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1260.png)

Kontrollü Kopya Toplama Raporu ekranında doküman listesi sekmesinde  yapılan filtredeki  arama kriterlerine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1261.png)Kontrollü Kopya Toplama Raporu ekranında ![ref252] (Excel Aktar)  butonu tıklanarak Excel formatında Kontrollü Kopya Toplama raporu alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1263.png)
##### **6.2.12.29. Doküman Revizyon Listesi**
**Menü Adı**: Entegre Yönetim Sistemi/ Doküman Yönetimi/ Raporlar/Doküman Revizyon Listesi

Revizyon işlemi yapılan dokümanları listesinin görüntülendiği ve Excel formatından raporunun alındığı menüdür. Doküman Revizyon Listesi ekranında doküman arama ve doküman listesi sekmesi olmak üzere iki sekme karşımıza çıkar. Doküman arama sekmesinde arama kriterlerine göre filtreleme işlemi yapılır. Doküman listesinde sekmesinde  ise bu arama kriterlerine göre filtreleme işlemine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1264.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref184]: Kayıtlar filtrelenerek arama yapılır.

![ref242] : Veriler Excel’ e aktarılır.

![ref185]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref186]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref187]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip-gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Doküman Revizyon Listesi ekranında doküman arama sekmesinde filtre arama kriterleri olan “Doküman Kodu ” alanında doküman kodu yazılarak  ![ref251] (Ara) butonu tıklanılır.

![ref253]

Doküman Revizyon Listesi ekranında doküman listesi sekmesinde  yapılan filtredeki  arama kriterlerine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1266.png)Doküman Revizyon Listesi ekranında ![ref252] (Excel Aktar)  butonu tıklanarak Excel formatında Doküman Revizyon Listesi raporu alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1267.png)
##### **6.2.12.30.Doküman Çeviri Raporu**
**Menü Adı**: Entegre Yönetim Sistemi/ Doküman Yönetimi/ Raporlar/Doküman Çeviri Raporu

Doküman Yönetimi modülü  kapsamında çevirisi yapılan dokümanların kim tarafında çevirisi yapıldığı, çeviri yapılan dilin ne olduğu,  çevirinin başlama bitiş tarihi gibi çeviri ile ilgili bilgilerin görüntülendiği  ve Excel formatında raporunun alındığı menüdür. Doküman Çeviri Raporu ekranında doküman arama ve doküman listesi sekmesi olmak üzere iki sekme karşımıza çıkar. Doküman arama sekmesinde arama kriterlerine göre filtreleme işlemi yapılır. Doküman listesinde sekmesinde  ise bu arama kriterlerine göre filtreleme işlemine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1268.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref184]: Kayıtlar filtrelenerek arama yapılır.

![ref242] : Veriler Excel’ e aktarılır.

![ref185]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref186]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref187]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip-gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Doküman Çeviri Raporu ekranında doküman arama sekmesinde filtre arama kriterleri olan “Doküman Kodu ” alanında doküman kodu yazılarak  ![ref251] (Ara) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1269.png)

Doküman Çeviri Raporu ekranında doküman listesi sekmesinde  yapılan filtredeki  arama kriterlerine göre kayıtlar listelenir

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1270.png)

Doküman Çeviri Raporu ekranında ![ref254] (Excel Aktar)  butonu tıklanarak Excel formatında Doküman Çeviri Raporu alınır

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1272.png)
##### **6.2.12.31. Kontrollü  Kopya Dağıtım Görev Raporu**
**Menü Adı**: Entegre Yönetim Sistemi/ Doküman Yönetimi/ Raporlar/ Kontrollü  Kopya Dağıtım Görev Raporu

Kontrollü  kopya dağıtım görevlerinin görüntülendiği ve Excel formatında raporunun alındığı menüdür. Kontrollü  Kopya Dağıtım Görev Raporu ekranında doküman arama ve doküman listesi sekmesi olmak üzere iki sekme karşımıza çıkar. Doküman arama sekmesinde arama kriterlerine göre filtreleme işlemi yapılır. Doküman listesinde sekmesinde  ise bu arama kriterlerine göre filtreleme işlemine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1273.png)

**Ekranda bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1274.png):Listede seçili Kontrollü Kopya Dağıtım görevinin silinme işlemi yapılır.

![ref184]: Kayıtlar filtrelenerek arama yapılır.

![ref242] : Veriler Excel’ e aktarılır.

![ref185]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref186]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref187]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip-gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Kontrollü  Kopya Dağıtım Görev Raporu ekranında doküman arama sekmesinde filtre arama kriterleri olan “Doküman Kodu ” alanında doküman kodu yazılarak  ![ref251] (Ara) butonu tıklanılır.

![ref253]

Kontrollü  Kopya Dağıtım Görev Raporu ekranında doküman listesi sekmesinde  yapılan filtredeki  arama kriterlerine göre kayıtlar listelenir

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1275.png)

Kontrollü  Kopya Dağıtım Görev Raporu ekranında Doküman Listesi sekmesinde  Kontrollü  Kopya Dağıtım Görevi seçili iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1276.png)  butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1277.png)

Sistem tarafından “Seçili satırı silmek istediğinizden emin misiniz?” mesajında “Tamam” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1278.png)

Sistem tarafından “İşleminiz başarıyla gerçekleştirilmiştir” mesajı verilerek Kontrollü  Kopya Dağıtım görevinin silinme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1279.png)

Kontrollü  Kopya Dağıtım Görev Raporu ekranında Kontrollü  kopya dağıtım görevi  seçili iken  ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1280.png) (Excel Aktar) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1281.png)

Excel formatında Kontrollü  Kopya Dağıtım Görevi  raporu alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1282.png)
##### **6.2.12.32.Doküman İptal Onay Süreleri Raporu**
**Menü Adı**: Entegre Yönetim Sistemi/ Doküman Yönetimi/ Raporlar/Doküman İptal Onay Süreleri Raporu

Doküman İptal Onay Sürelerinin  görüntülendiği ve Excel formatında raporunun alındığı menüdür. Doküman İptal Onay Süreleri Raporu ekranında doküman arama ve doküman listesi sekmesi olmak üzere iki sekme karşımıza çıkar. Doküman arama sekmesinde arama kriterlerine göre filtreleme işlemi yapılır. Doküman listesinde sekmesinde  ise bu arama kriterlerine göre filtreleme işlemine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1283.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref184]: Kayıtlar filtrelenerek arama yapılır.

![ref242] : Veriler Excel’ e aktarılır.

![ref185]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref186]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref187]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip-gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Doküman İptal Onay Süreleri Raporu ekranında doküman arama sekmesinde filtre arama kriterleri olan “Doküman Kodu ” alanında doküman kodu yazılarak  ![ref251] (Ara) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1284.png)

Doküman İptal Onay Süreleri Raporu ekranında doküman listesi sekmesinde  yapılan filtredeki  arama kriterlerine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1285.png)

Doküman İptal Onay Süreleri Raporu ekranında ![ref252] (Excel Aktar)  butonu tıklanarak Excel formatında Doküman İptal Onay Süreleri Raporu alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1286.png)
##### **6.2.12.33.Doküman Statü Raporu**
**Menü Adı**: Entegre Yönetim Sistemi/ Doküman Yönetimi/ Raporlar/Doküman Statü Raporu

Doküman Yönetim Modülü kapsamında sistemde yüklü dokümanların hazırlanıyor, yayında, revizyonda gibi durum bilgileri ile görüşten dönen, saklanan , görüş gibi “taslak durum”olan statü bilgilerinin ulaşıldığı ve Excel formatında raporlarının alındığı menüdür. Doküman Statü Raporu ekranında doküman arama ve doküman listesi sekmesi olmak üzere iki sekme karşımıza çıkar. Doküman Arama sekmesinde arama kriterlerine göre filtreleme işlemi yapılır. Doküman listesinde sekmesinde  ise bu arama kriterlerine göre filtreleme işlemine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1287.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref184]: Kayıtlar filtrelenerek arama yapılır.

![ref242] : Veriler Excel’ e aktarılır.

![ref185]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref186]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref187]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip-gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Doküman Statü Raporu ekranında doküman arama sekmesinde filtre arama kriterleri olan “Doküman Kodu ” alanında doküman kodu yazılarak  ![ref251] (Ara) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1288.png)

Doküman Statü Raporu ekranında doküman listesi sekmesinde  yapılan filtredeki  arama kriterlerine göre kayıtlar listelenir

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1289.png)

Doküman Statü Raporu ekranında ![ref252] (Excel Aktar)  butonu tıklanarak Excel formatında Doküman Statü raporu alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1290.png)
##### **6.2.12.34.Görevi Düşen Dokümanlar Raporu**
**Menü Adı**: Entegre Yönetim Sistemi/ Doküman Yönetimi/ Raporlar/ Görevi Düşen Dokümanlar Raporu

Dokümanlar revize olduğunda ya da iptal olduğunda kullanıcılarda bekleyen okuma görevlerinin önceki revizyonlar ile birlikte kimlere düştüğünü göstererek listeleyen rapordur. Görevi Düşen Dokümanlar Raporu ekranında filtre ve doküman listesi sekmesi olmak üzere iki sekme karşımıza çıkar. Filtre sekmesinde arama kriterlerine göre filtreleme işlemi yapılır. Doküman listesinde sekmesinde  ise bu arama kriterlerine göre filtreleme işlemine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1291.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref255]:Görevi düşen doküman logları listelenir.

![ref184]: Kayıtlar filtrelenerek arama yapılır.

![ref242] : Veriler Excel’ e aktarılır.

![ref185]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref186]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref187]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip-gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Doküman Statü Raporu ekranında filtre sekmesinde arama kriterleri olan “Doküman Kodu ” alanında doküman kodu yazılarak  ![ref251] (Ara) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1293.png)

Görevi Düşen Dokümanlar Raporu ekranında doküman listesi sekmesinde  yapılan filtredeki  arama kriterlerine göre kayıtlar listelenir

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1294.png)

Görevi Düşen Dokümanlar Raporu ekranında Doküman listesinde doküman seçili iken ![ref255] butonu tıklanarak görevi düşen doküman loglarının listelenmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1295.png)
##### **6.2.12.35.Doküman Kullanım Yeri Listesi**
**Menü Adı**: Entegre Yönetim Sistemi/ Doküman Yönetimi/ Raporlar/ Doküman Kullanım Yeri Listesi

Dokümanlara ait kullanım yeri matrislerini gösteren  ve Excel formatında raporun alındığı menüdür. Doküman Kullanım Yeri Listesi ekranında doküman arama ve doküman listesi sekmesi olmak üzere iki sekme karşımıza çıkar. Doküman arama sekmesinde arama kriterlerine göre filtreleme işlemi yapılır. Doküman listesinde sekmesinde  ise bu arama kriterlerine göre filtreleme işlemine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1296.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref256]: Kayıtlar filtrelenerek arama yapılır.

![ref254] : Veriler Excel’ e aktarılır.

![ref257]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref258]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref259]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Doküman Kullanım Yeri Listesi ekranında doküman arama sekmesinde filtre arama kriterleri olan “Doküman Kodu ” alanında doküman kodu yazılarak  ![ref211] (Ara) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1301.png)

Doküman Kullanım Yeri Listesi ekranında doküman listesi sekmesinde  yapılan filtredeki  arama kriterlerine göre kayıtlar listelenir

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1302.png)

Doküman Kullanım Yeri Listesi ekranında ![ref254] (Excel Aktar)  butonu tıklanarak Excel formatında Doküman Kullanım Yeri Listesi raporu alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1303.png)
##### **6.2.12.36.Görevi Düşen Kişiler Raporu**
**Menü Adı**: Entegre Yönetim Sistemi/ Doküman Yönetimi/ Raporlar/ Görevi Düşen Kişiler Raporu

Görevi düşen kişiler raporu, görevi düşen dokümanlar raporu ile benzerdir. Kişi bazlı görevleri gösteren bir rapordur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1304.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref260]: Görevi Düşen Doküman kişi logları listeler.

![ref256]: Kayıtlar filtrelenerek arama yapılır.

![ref254] : Veriler Excel’ e aktarılır.

![ref257]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref258]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref259]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip-gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1306.png)

Görevi Düşen Kişiler Raporu ekranında ![ref260] butonu tıklanarak görevi düşen kişi logları  görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1307.png)
### **6.3.Sistem Altyapı Tanımları/ Doküman İşlemleri/ 2.Kısım**
#### **6.3.1.Doküman Sisteme Aktarım**
**Menü Adı**: Sistem Altyapı Tanımları/ Doküman İşlemleri/ Doküman Sisteme Aktarım

Daha önce onay ve dağıtım süreçlerini tamamlamış olan dokümanların, sistemde onay ve kontrole gitmeden hızlıca sisteme dahil edilebildiği menüdür. Doküman Hazırlama menüsünden tek farkı onay mekanizmalarının olmamasıdır. Doküman sisteme aktarımı sistem yöneticileri tarafından kullanılmaktadır.

Doküman Sisteme Aktarım menüsü tıklanılır.Açılan Doküman Sisteme Aktarım - Klasör Seçme ekranında  dokümanın aktarılacağı klasör seçilir ve  ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1308.png) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1309.png)

Açılan Doküman Sistem Aktarım ekranında Doküman bilgileri sekmesinde dokümanın bilgileri girilir. Dokümanın adı yazılarak,  hazırlama tarihi açılan takvim alanından seçilerek  detay bilgileri doldurulur.Bu işlemler, doküman hazırlama menüsündeki işlem basamakları aynı şekilde yapılmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1310.png)

Doküman Sisteme Aktarım ekranında doküman bilgileri sekmesinde dokümanın detay bilgileri girildikten sonra doküman sekmesi tıklanılır. Doküman sekmesinde Dokuman Dosyası Yükleme (Türkçe) alanında ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1311.png) butonu tıklanarak sisteme aktarılacak doküman yükleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1312.png)

Doküman Sisteme Aktarım ekranında  Dosya Ekle ekranında Gözat butonu tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1313.png)

Sistem aktarım işlemi yapılacak Doküman seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1314.png)

Sistem tarafından “Dosya başarıyla aktarılmıştır” mesajı verilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1315.png)

Doküman Sisteme Aktarım ekranında doküman bilgiler sekmesi tıklanarak doküman ilgili tüm bilgiler girildikten sonra ekranın sol üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1316.png) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1317.png)

Sistem tarafından “Doküman başarıyla kaydedilmiştir” mesajı verilerek dokümanın sisteme aktarılma işleminin yapıldığı belirtilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1318.png)
#### **6.3.2.Doküman Kayıt Bakım**
**Menü Adı:** Sistem Altyapı Tanımları/ Doküman İşlemleri/ Doküman Kayıt Bakım

Dokümanda revizyon gerektirmeyen küçük değişikliklerin yapılabildiği menüdür. Örneğin; doküman hazırlanış tarihi, doküman içerisindeki noktalama hataları gibi. Doküman kayıt bakım özelliği ile, revizyon numarası almadan, dokümanların revize edilmesi sağlanır. Doküman içinde bir şey değiştirilmek istenip, revizyon numarası alması istenmiyorsa bu menü kullanılır.

Doküman Kayıt Bakım menüsü tıklanılır.Açılan Doküman Kayıt Bakım-Klasör Seçme ekranında bilgileri düzenlenecek ilgili doküman bulunduğu klasör seçilir ve  ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1319.png)  butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1320.png)

Açılan Doküman Kayıt Bakım - Doküman Belirleme ekranında Doküman Listesinde bilgileri düzenlenecek ilgili doküman seçilir ve  ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1321.png)  butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1322.png)

İlgili dokümanın bilgilerinin bulunduğu sayfaya gelinir. Bu sayfada bulunan bilgiler istenildiği gibi düzenlenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1323.png)

Doküman Kayıt Bakım ekranında Doküman sekmesi tıklanılır. ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1324.png)(Dosya Görüntüle) butonu ile doküman kullanıcının bilgisayarına indirilir

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1325.png)

İndirilen doküman üzerinde yapı ve içerik kapsamında istenilen değişiklikler yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1326.png)

Doküman Kayıt Bakım ekranında Doküman sekmesinde ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1327.png)(Dosya Ekle) butonu tıklanarak yapı ve içeriği değiştirilen doküman sisteme yükleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1328.png)

Dosya Ekle ekranında Gözat butonu tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1329.png)

Yapı ve içeriği değiştirilen doküman seçilerek sisteme yüklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1330.png)

Sistem tarafından “Dosya başarıyla aktarılmıştır.” mesajı verilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1331.png)

Yapı ve içerik olarak değiştirilen dokümanın sisteme yüklenmesinden sonra Doküman Bilgileri sekmesi tıklanılır.Doküman Bilgileri sekmesinde “Mevcut Doküman Dosya Bilgileri Değiştirilsin” alanı ile ilgili check box işaretlenir. Bu alan ile ilgili check box işaretlenirse takdirde doküman bilgileri kısmında yapılan değişiklikler doküman şablonuna yansıyacak olup, doküman yeni bilgilerle görüntülenecektir. (Örneğin; doküman hazırlanma tarihi, hazırlayan, kontrol eden, onaycı bilgileri gibi). Doküman Kayıt Bakım ekranında doküman bilgileri sekmesindeki ekranında  sol üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1332.png) butonu yardımıyla yapılan değişiklikler kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1333.png)

Sistem tarafından” Doküman başarıyla kaydedilmiştir” mesajı verilerek Doküman kayıt bakım işleminin yapıldığı belirtilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1334.png)
#### **6.3.3.Taslak Doküman Ek Dosya Düzenleyici**
**Menü Adı**: Sistem Altyapı Tanımları/ Doküman İşlemleri/ Taslak Doküman Ek Dosya Düzenleyici

Doküman Yönetimi Modülü kapsamından taslak aşamasında dokümanların Ek Dosyalar sekmesinde yüklenen ek dosyaların görüntülenip, düzenlendiği, düzenlenen ek dosyaların sisteme tekrar yüklendiği veya farklı bir ek dosyanında bu aşamada yüklendiği menüdür. Doküman Ek Dosya Düzenleyici menüsü tıklanılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1335.png)

Açılan Ek Dosya Düzenleme ekranında listeden ek dosyaları düzenlenecek doküman seçilir ve ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1336.png)butonu ile ek dosyaların düzenleneceği ekrana gelinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1337.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref261]:Kayıt işlemi yapılır.

![ref262]:Dosya yüklenir.

![ref263]: Listede seçili olan dosya açılır.

![ref264]: Listede seçili olan dosya silinir.

Ek Dosya Düzenleme ekranında ![ref263]butonu tıklanarak listede seçili ek dosya sisteme indirilerek görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1342.png)

Bilgisayara indirilen taslak aşamasında eklenen Ek dosya düzenlendikten sonra   ![ref262] butonu ile sisteme tekrar yüklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1343.png)

Dosya Ekle  ekranında Gözat butonu tıklanır  ve dosya seçilerek düzenlenmiş şekli sistem yüklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1344.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1345.png)

Ek Dosya Düzenleme ekranında ![ref265]butonu tıklanarak sistemde yüklü Ek Dosyanın silinme işlemi yapılır. Ek Dosya Düzenleme ekranında listede sistemde yükle Ek Dosya seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1347.png)

Listede seçili Ek Dosya seçili iken ![ref265]butonu tıklanarak listede seçili Ek Dosyanın silinme işlemi yapılır ve ekranın sol üst köşesindeki ![ref266] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1349.png)

Ek Dosya Düzenleme ekranında Taslak aşamasında Ek Dosya sekmesinde yüklenen Ek dosyaların  ![ref267]butonu tıklanarak listesi görüntülenir. Açılan Ek Dosyaları Düzenleme ekranında ![ref267]yardımıyla listedeki Ek Dosyalar bilgisayara indirilir ve indirilen Ek dosyalar düzenleme işleminde sonra ![ref268]butonu ile bilgisayardan sisteme tekrar düzenlenmiş şekli yüklenir.  Ek Dosya Düzenleme ekranında Taslak aşamasında yüklenen dosyaların görüntülenip, düzenleme işlemi yapıldığı gibi bu ekranda bilgisayardaki bir dosyanında ![ref268] butonu ile sisteme yükleme işlemi yapılır. Bekleyen işlerimde “Saklanan dokümanlar” taskında taslak aşamasındaki doküman listede seçilerek doküman kodu tıklanır. Açılan Yeni Doküman ekranında Ek Dosyalar sekmesi tıklanarak Taslak Doküman Ek Dosya Düzenleyici menüsünde düzenlenen ve bilgisayardan yüklenen dosyaların listesi görüntülenir.
#### **6.3.4.Yayınlı Doküman Ek Dosya Düzenleyici**
**Menü Adı**: Sistem Altyapı Tanımları/ Doküman İşlemleri/ Yayınlı  Doküman Ek Dosya Düzenleyici

Doküman Yönetim kapsamında onaylama sürecinde, onay matrisindeki sıraya göre son onaydan geçen doküman yayınlanarak dağıtım matrisinde olan kişilere dağıtılır ve kullanıma açılır. Dağıtım matrisindeki ilgili kişilere sistem tarafından mail gönderilir ve dokümana artık yetkili kişiler tarafından ulaşılabilir.Yayınlanan doküman, dağıtım matrisinde bulunan yetkili kişilere okuma görevi olarak düşmektedir. Kişilerin “Bekleyen İşlerimde” sayfasında “Okunması Gereken Dokümanlar Listesi” olarak görüntülenir. Ayrıca Doküman Dağıtım Matrisinde “Önemli” check box’ı işaretli olan kullanıcı grupları ya da pozisyonlar için “Okunması Gereken Önemli Dokümanlar Listesi” adında bir okuma görevi de oluşur.  Bu şekilde yayınlanan dokümanların yayınlama aşamasında Ek Dosyalar sekmesinde yüklenen Ek dosyaların görüntülenip, düzenlendiği, düzenlenen ek dosyaların sisteme tekrar yüklendiği veya bilgisayardan  farklı bir ek dosyanında bu aşamada sisteme yüklendiği menüdür.  Açılan Yayınlı  Doküman Ek Dosya Düzenleyici ekranında Filtre ve  Liste sekmesi olmak üzere iki sekme karşımıza çıkar. Filtre sekmesinde arama kriterlerine göre filtreleme işlemi yapılarak liste sekmesinde kayıtların görüntülenmesi sağlanır.

Yayınlı Doküman Ek Dosya Düzenleyıci ekranında Filtre sekmesinde arama kriterleri olan “Doküman Kodu ” alanında doküman kodu yazılarak  ![ref29] (Ara) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1352.png)

Yayınlı Doküman Ek Dosya Düzenleyıci ekranında liste sekmesinde  yapılan filtredeki  arama kriterlerine göre kayıtlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1353.png)

Açılan Yayınlı Ek Dosya Düzenleme ekranında listeden ek dosyaları düzenlenecek doküman seçilir ve ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1354.png) butonu tıklanarak ek dosyaların düzenleneceği ekrana gelinir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1355.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref269]:Kayıt işlemi yapılır.

![ref270]:Dosya yüklenir.

![ref271]: Listede seçili olan dosya açılır.

![ref272]: Listede seçili olan dosya silinir.

Ek Dosya Düzenleme ekranında ![ref271]butonu tıklanarak listede seçili ek dosya sisteme indirilerek görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1360.png)

Bilgisayara indirilen Ek dosya düzenlendikten sonra   ![ref262] butonu ile sisteme tekrar yüklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1361.png)

Dosya Ekle ekranında Gözat butonu tıklanır  ve dosya seçilerek düzenlenmiş şekli sistem yüklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1362.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1363.png)

Ek Dosya Düzenleme ekranında ![ref265]butonu tıklanarak sistemde yüklü Ek Dosyanın silinme işlemi yapılır. Listede sistemde yükle Ek Dosya seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1364.png)

Listede seçili Ek Dosya seçili iken ![ref265]butonu tıklanarak listede seçili Ek Dosyanın silinme işlemi yapılır ve ekranın sol üst köşesindeki ![ref266] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1365.png)

Ek Dosya Düzenleme ekranında yayınlama aşaması bitmiş dokümanların Ek Dosya sekmesinde yüklenen Ek dosyaların  ![ref271]butonu tıklanarak  listesi görüntülenir. Açılan Ek Dosyaları Düzenleme ekranında ![ref271]yardımıyla listedeki Ek Dosyalar bilgisayara indirilir ve indirilen Ek dosyalar düzenleme işleminde sonra ![ref270]butonu ile bilgisayardan sisteme tekrar düzenlenmiş şekli yüklenir.  Ek Dosya Düzenleme ekranında yayınlanmış dokümanlarda yüklenen dosyaların görüntülenip, düzenleme işlemi yapıldığı gibi bu ekranda bilgisayardaki bir dosyanında ![ref270] butonu ile sisteme yükleme işlemi yapılır.
#### **6.3.5.Doküman Link**
**Menü Adı**: Sistem Altyapı Tanımları/ Doküman İşlemleri/ Doküman Link

Doküman Seç alanında seçilen dokümanın Qdms’deki linki alındığı ve  alınan link mail yoluyla paylaşıldığı menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1366.png)

**Ekranda bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1367.png):Doküman Linki ekranında seçilen dokümanın link alma işlemi yapılır.Qdms sisteminde doküman görme menüsünde dokümanın görüntüleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1368.png):Doküman Linki ekranında seçilen dokümanın yetkisiz link alma işlemi yapılır. Alınan link ile Qdms’e girmeden dokümana ulaşılır.

**Link Geçirlilik Süresi:** Doküman Linki ekranında link geçerlilik süresinin süreli ve süresiz olarak seçildiği alandır.

**Süreli:** Doküman Linki ekranında linkin geçerlilik süresinin belirli bir süreye bağlı olarak seçildiği alandır.Süreli seçeneği seçildiğinde ek bir alan olan Link geçerlilik Tarihi alanı görüntülenir. Bu alanda link geçerlilik tarihi bilgisi açılan Takvim alanında seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1369.png)

Doküman Link ekranında Doküman seç alanında ![ref273] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1371.png)

Açılan Doküman Seçme ekranında Filtre sekmesinde filtre arama kriterleri olan “Doküman Kodu ” alanında doküman kodu yazılarak  ![ref251] (Ara) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1372.png)

Liste sekmesinde yapılan filtredeki  arama kriterlerine göre kayıtlar listelenir .

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1373.png)

Doküman seçildiktende sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1374.png)  butonu tıklanarak doküman seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1375.png)

Doküman seçilme işleminden sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1376.png) butonu tıklanarak dokümanın link alma işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1377.png)

Bu link adresi ile sistemde tanımlı herhangi bir dokümana link verilebilir (microsoft linki kurma işlemi gibi) veya Qdms kullanıcısı olan bir personelle alınan link paylaşılabilir.Alınan link sağ tıkla/kopyala-yapıştır yöntemi ile yeni sekmede  Qdms sisteminde Doküman Görme menüsü açılarak görüntülenmesi ve Qdms kullanıcısı olan ilgili kişiler paylaşılması sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1378.png)

Doküman Linki ekranında Doküman Seç alanında doküman seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1379.png)

Doküman linki ekranında doküman seçildikten sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1380.png) butonu tıklanarak Qdms kullanıcısı olmayan personellerle ilgili link paylaşılırsa, Qdms ‘e girmeden dokümana ulaşılabilirler.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1381.png)

Alınan link sağ tıkla/kopyala -yapıştır yönetimi ile yeni sekmede Qdms sisteminde girmeden dokümanın görüntülenip ilgili kişiler ile paylaşımı sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1382.png)
#### **6.3.6.Doküman Kodu Değiştirici**
**Menü Adı:** Sistem Altyapı Tanımları/ Doküman İşlemleri/ Doküman Kodu Değiştirici

Doküman kodlarının değiştirildiği menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1383.png)

**Ekranda bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1384.png):Listede seçili dokümanın kodunun değiştirme işlemi yapılır.

Doküman Kodunu Değiştirme ekranında Doküman Seç alanında ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1385.png) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1386.png)

Açılan ekranda Doküman Seç ekranında Doküman listesinde, kodu değiştirilecek doküman seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1387.png) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1388.png)

Bu alanda dokümanın kodu değiştirilip ![ref274]butonuna basıldığında doküman kodu değişme işlemi yapılır. İstenirse “Yeni Doküman Adı” alanına da dokümana verilecek yeni isim girildikten sonra  ![ref274] butonu ile yapılan değişiklikler kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1390.png)

Sistem tarafından “Dokuman Kodunu değiştirmek istediğinize emin misiniz?” mesajında “Tamam” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1391.png)

Sistem tarafından “Dokuman Kodu veya Adı değiştirilmiştir.” mesajı verilerek doküman kodunun değiştirilme işleminin gerçekleştiği belirtirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1392.png)
#### **6.3.7.Doküman Matris Eşitleyici**
**Menü Adı:** Sistem Altyapı Tanımları/ Doküman İşlemleri/ Doküman Matris Eşitleyici

Bir klasörde yetki, dağıtım, onay, kontrollü kopya matrislerinde değişiklik yapıldığında ya da klasöre bağlı doküman sorumluları, kontrolle ilgili değişiklikler, hazırlayan, revize eden, gözden geçirecek, doküman türü, doküman tipi, gibi alanlarında değişiklik yapıldığında bu değişikliğin alt klasörlere ve dokümanlara yansıması için matris eşitleme yapılması gerekir.Bu menüden klasör matris eşitleme veya doküman matris eşitleme yapılabilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1393.png)

**Ekranda bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1394.png):Matris eşitleme işlemi ile ilgili log kayıtları görüntülenir.

![ref275]:Matris eşitleme işlemi yapılır.

**Doküman Matris Eşitleme için;**

Matris Eşitleyici ekranında Klasör Seç alanında ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1396.png) butonu tıklanarak Doküman Klasörü  listeden, istenen klasör seçilir.Matris Eşitleyici ekranında Matrisleri Eşitle seçeneği ile ilgili alanla ilgili check box işaretlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1397.png) Klasörü seçtikten sonra, klasörün kırılımına bağlı olan ilgili seçenek işaretlenir (Örneğin; Yalnızca seçili klasörün Dokümanları listele)

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1398.png)

Matris Eşitleyici ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1399.png)( Ara)  butonu ile dokümanların  filtreleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1400.png)

Matris Eşitleyici ekranında daha sonra değişiklik yapılacak dokümanlar seçilerek  belirlenir. İstenirse doküman Sorumlusu,  Kontrol Eden, Revize Eden ve Hazırlayan, İlgili bölüm, Doküman Türü, Doküman tipi  gibi alanlar da düzenlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1401.png)

Yetki-Dağıtım-Onay-Kontrollü Kopya-Görme Matrisi gibi değişiklik yapılacak matris ile ilgili cehck box işeretlenir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1402.png)

Yapılan değişikliklerin dokuman dosyası içerisindeki <...\> değişkenlerine de yansıması isteniyorsa “Doküman Dosya Bilgileri Değiştirilsin” check box’ı işaretlenir. Doküman matris eşitleme yapılırken revizyon işlemi devam eden dokümanlar için matris eşitleme işleminin gerçekleştirilmesi için “Revizyonu devam edenleride  Değiştir (Yetki ve Dağıtım)”  alanı ilgili check box işaretlenir.

Matris Eşitleyici ekranında doküman seçimi ve değişiklik yapılacak alanlar ilgili cehck box işaretlendikten sonra  ![ref275]butonu  tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1403.png)

Sistem tarafından “Matrisleri eşitlemek istediğinize emin misiniz?” mesajında “Tamam” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1404.png)

Matris Eşitleyici ekranında seçilen dokümanlar için matris eşitleme işleminin yapıldığının tamamlandığı görülür.

**Klasör Bilgileri Eşitle;**

Seçilen klasörün alt klasörleri listelenir. Alt klasörleri seçilerek seçilenen alt klasörlerin  seçilen klasörlerin  klasör ayarları ilgili bilgilerinin eşitleme işlemi yapılır. Bu işlemde seçilen alt klasörler seçilen klasör olan ana klasörün seçilen klasör ayarları bilgileri  göre değişmesi işlemi yapılmaktadır.Bu işlemin yapılması için öncelikle Klasör Seç alanında ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1405.png) butonu tıklanarak açılan Doküman Klasör listesinde Klasör seçilir. Matris Eşitleyici ekranında Klasör Bilgileri Eşitle seçeneği alanı ilgili check box işaretlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1406.png)

Matris Eşitleyici ekranında klasör seçilme işleminde ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1407.png)(Ara) butonu tıklanarak klasörün alt klasörlerin listelenmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1408.png)

Seçilen Klasörün listelen alt klasörleri seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1409.png)Seçilen Klasörün alt klasörlerin seçim işleminde sonra seçilen klasörün klasör ayarları ilgili bulunduğu alanlar ilgili check box’lar işaretlenir. Bu aşamada Ana klasör olan seçilen klasörün Klasör  ayarları ilgili alanlar seçilen alt klasörlere göre değişmesi istenilen alanların seçim işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1410.png)

Ana klasör olarak seçilen klasörün alt klasörde değişmesi istenilen alanların seçim işleminden sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1411.png) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1412.png)

Sistem tarafından “Matrisleri eşitlemek istediğinize emin misiniz?” meajında “Tamam” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1413.png)

Matris Eşitleyici ekranında seçilen alt klasörler için seçilen ana klasörün olan seçilen klasörün klasör  ayarları alanları ilgili bilgilerinin için matris eşitleme işleminin yapıldığının tamamlandığı görülür.

**Log Göster İşlemi;**

Matris Eşitleyici ekranında  ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1414.png) butonu tıklanarak matris eşitleme işlemi log kayıtları görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1415.png)

Filtre sekmesinde Revizyon Tarihi alanında açılan Takvim alanında seçim yapılarak arama kriterine göre liste sekmesinde Matris Eşitleme Log kayıtlarının detay bilgileri görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1416.png)
#### **6.3.8.Çoklu Doküman Kodu Değiştirici**
**Menü Adı:** Sistem Altyapı Tanımları/ Doküman İşlemleri/ Çoklu Doküman Kodu Değiştirici

Birden çok dokümanın kodunun aynı anda  toplu olarak değiştirmek için kullanıldığı menüdür.(Eski Doküman Kodu, Yeni Doküman Kodu şeklinde)  Bu işlemin yapılması için ![ref276]   butonu tıklanarak bilgisayara indirilen Çoklu  doküman Kodu Değiştirici şablonunda eski doküman  kod bilgisi alanında sistemde tanımlı eski doküman kod bilgileri yazılarak  ve  yeni doküman kod alanında değiştirilmek istenilen doküman kod bilgileri yeni doküman kod alanı yazılarak Çoklu Doküman Kodu Değitirici şablonu doldurulur. Çoklu Doküman Kodu Değitirici şablonda ilgili alanlar bilgiler yazıldıktan sonra ![ref277]  butonu tıklanarak Çoklu Doküman Kodu Değitirici şablonu Qdms sisteminde menüye yüklenir.Aktarılan veriler aktarım için uygunsa ![ref278]  butonu aracılığıyla aktarım gerçekleşmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1420.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref276] :Çoklu Doküman Kodu Değiştirici şablonu bilgisayara indirilir.

![ref277] :Doldurulan Çoklu Doküman Kodu Değiştirici şablon sisteme yüklenir.

![ref278]: Aktarım işlemi gerçekleştirilir.

![ref279]:Veriler Excel’e aktarılır.

![ref4]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref5]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref149]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip-gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.


Çoklu Doküman Kodu Değiştirme ekranında ![ref276]butonu tıklanarak Çoklu Doküman Kodu Değitirici şablonu bilgisayara indirilir. İndirilen Çoklu Doküman Kodu Değitirici şablonunda  ilgili alanlar ilgili bilgiler yazılarak doldurularak  ve bilgisayara kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1422.png)

Çoklu Doküman Kodu Değiştirme ekranında doldurulan Çoklu Doküman Kodu Değiştirici şablonu ![ref280] butonu tıklanarak sisteme yükleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1424.png)

Dosya Yükle ekranında “Gözat” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1425.png)

Açılan ekranda doldurulan Çoklu Doküman Kodu Değiştirici şablonu seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1426.png)

Çoklu Doküman Kodu Değiştirici ekranında 3. buton olan ![ref278]  tıklanarak  eski doküman kodlarının yeni doküman  kodları ile değiştirilerek sistem aktarılma işlemi yapılmasını sağlar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1427.png)

Sistem tarafından Çoklu Doküman Kodu Değiştirici ekranından doküman kodlarının değiştiği bilgisi Durum alanında verilir. Revizyon işlemi yapılan dokümanlarda doküman kodu değiştirme işlemi yapılmaz.Sistem tarafından durum alanında “Revizyonda, değiştirlimez” bilgisi verilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1428.png)
#### **6.3.9.Çoklu Klasör Kodu Değiştirici**
**Menü Adı:** Sistem Altyapı Tanımları/ Doküman İşlemleri/ Çoklu Klasör  Kodu Değiştirici

Birden çok klasörün  kodunun toplu olarak aynı anda değiştirmek için kullanıldığı menüdür.(Eski Klasör Kodu, Yeni Klasör Kodu şeklinde)  Bu işlemin yapılması için ![ref276]   butonu tıklanarak bilgisayara indirilen Çoklu  Klasör Kodu Değiştirici şablonunda eski klasör kod bilgisi alanında sistemde tanımlı eski klasör kod bilgileri yazılarak  ve  yeni klasör kod alanında değiştirilmek istenilen klasör kod  bilgileri yeni klasör kod alanı yazılarak Çoklu Klasör Kodu Değitirici şablonu doldurulur. Çoklu Klasör Kodu Değitirici şablonda ilgili alanlar bilgiler yazıldıktan sonra ![ref277]  butonu tıklanarak Çoklu Klasör Kodu Değitirici şablonu Qdms sisteminde menüye yüklenir.Aktarılan veriler aktarım için uygunsa ![ref278]  butonu aracılığıyla aktarım gerçekleşmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1429.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref276] : Çoklu Klasör Kodu Değiştirici şablonu bilgisayara indirilir.

![ref277] : Doldurulan Çoklu Klasör Kodu Değiştirici şablon sisteme yüklenir.

![ref278]: Aktarım işlemi gerçekleştirilir.

![ref279]:Veriler Excel’e aktarılır.

![ref4]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref5]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref149]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip-gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.


Çoklu Klasör Kodu Değiştirme ekranında ![ref276]butonu tıklanarak Çoklu Klasör Kodu Değitirici şablonu bilgisayara indirilir. İndirilen Çoklu Klasör Kodu Değitirici şablonunda  ilgili alanlar ilgili bilgiler yazılarak doldurularak  ve bilgisayara kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1430.png)

Çoklu Klasör Kodu Değiştirme ekranında doldurulan Çoklu Klasör Kodu Değiştirici  şablonu ![ref280] butonu tıklanarak sisteme yükleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1431.png)

Dosya Yükle ekranında “Gözat” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1432.png)

Açılan ekranda doldurulan Çoklu Klasör Kodu Değiştirici şablonu seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1433.png)

Çoklu Klasör Kodu Değiştirici ekranında 3. buton olan ![ref278]  tıklanarak  eski Klasör kodlarının yeni Klasör kodları ile değiştirilerek sistem aktarılma işlemi yapılmasını sağlar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1434.png)

Sistem tarafından Çoklu Klasör Kodu Değiştirici ekranından doküman kodlarının değiştiği bilgisi Durum alanında “İşlem Başarılı” bilgisi verilerek klasör kodlarının değiştiği bilgisi verilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1435.png)
#### **6.3.10.Doküman Kısayolu Tanımlama**
**Menü Adı:** Sistem Altyapı Tanımları/ Doküman İşlemleri/ Doküman Kısayolu Tanımlama

Qdms’de var olan bir dokümanın kısayol şeklinde başka bir klasöre kopyalanmasını sağlar. Kısayol olarak tanımlanan dokümanda revizyon işlemi yapılamaz. Dokümanın revize işlemleri asıl dokümanda yapılır. Doküman listesi ekranında kısayol olarak tanımlanan dokümanlar listelenmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1436.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref281]:Yeni bir kısayol tanımlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1438.png):Listede seçili kısayol bilgisi üzerinde değişiklik ve güncelleme işlemi yapılır.

Doküman Kısayolu eklemek için ekranın sol üst  köşesindeki ![ref281]butonu tıklanarak Doküman Kısayol Tanımlama/ Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1439.png)

Açılan ekranda kısayol olarak taşınacak doküman seçilir. Hangi klasöre kısayol tanımlanacağı belirtilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1440.png)

Ekranın sol tarafındaki klasör ağacından ise dokümanın hangi klasörlerin altında görüntüleneceği seçilir ve ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1441.png) butonu ile klasör seçim işlemi kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1442.png)

Doküman Kısa Yol Tanımlama ekranında ekranın sol üst köşesindeki  ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1443.png) butonuna tıklanarak doküman kısayol kayıt işlemi gerçekleştirilmiş olur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1444.png)
#### **6.3.11.Doküman Yetkileri Düzenleme**
**Menü Adı:** Sistem Altyapı Tanımları/ Doküman İşlemleri/ Doküman Yetkileri Düzenleme

Dokümanlarla ilgili yetkilendirme işlemi kolay ve hızlı bir şekilde düzenlendiği menüdür. Klasörlerin içindeki tüm dokümanlara yetki verilmek istenmediği durumlarda, sadece klasörün içindeki bazı dokümanlar için yetki verilmek istendiğinde veya yetki alınmak istendiğinde bu özellik kullanılabilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1445.png)

Doküman Yetkileri Düzenleme menüsüne tıklanılır. Filtre sekmesinde Bağlı olduğu Klasör alanından ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1446.png) butonu tıklanarak Doküman Klasörü listesinden Klasör seçilir. ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1447.png)

Doküman Yetkileri Düzenleme ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1448.png)(Ara) butonu tıklanarak  Klasör içerisindeki dokümanları listelenmesi sağlanır.Listelenen dokümanlarda yetkileri düzenlenecek dokümanlar seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1449.png)

Doküman Yetkileri Düzenleme ekranında Kullanıcı türü olarak personel ya da kullanıcı grubu belirlenir; ardından okuma, yazdırma, revize, eski revizyonları görme, silme alanları ile ilgili check box işaretlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1450.png)

Son olarak ekranın sol üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1451.png)butonuna tıklanarak toplu ve hızlıca yetki düzenlemesi işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1452.png)

Sistem tarafından “İşlemi gerçekleştirmek istediğinize emin misiniz?” mesajında “Tamam” butonu   tıklanılır

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1453.png)Sistem tarafından Pozisyon/kullanıcı grubu için yetkiler düzenlendiği ve yetkileri düzenlenen pozisyon/kullanıcı grubunun bilgisi verilir. Doküman bazında yetki verilebileceği gibi yetkiler de bu kısımdan kaldırılabilme işlemide yapılır. Bu menüde iptal edilmiş olan dokümanlar üzerinde de gerekli düzenlemeler yapılabilmektedir.
#### **6.3.12.Klasör Yetkileri Düzenleme**
**Menü Adı:** Sistem Altyapı Tanımları/ Doküman İşlemleri/ Klasör Yetkileri Düzenleme

Klasörlerle ilgili yetkilendirme işlemi kolay ve hızlı bir şekilde düzenlenebildiği menüdür. Yetkiler belirlenen klasör seçiminden sonra kullanıcı türü olarak personele ya da kullanıcı gruplarına  yetkiler verilebilmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1454.png)

Filtre sekmesinde Bağlı Olduğu Klasör alanından ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1455.png) butonu tıklanarak açılan sistemde tanımlı Doküman Klasör listesinde yetki verilecek Klasör seçim işlemi yapılarak  ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1456.png)(Ara) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1457.png)Filtre sekmesinde arama kriterlerine göre filtreleme işleminden sonra yetki verilecek klasör liste sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1458.png)

Ardından, yetki verilecek klasörler seçilir. Kullanıcı türü alanından personel ya da kullanıcı grubu olarak belirlenir, ardından okuma, yazdırma, revize, eski revizyonları görme, iptal alanları ile ilgili check box’lar işaretlenir. İşlem Tipi alanında yetkilerinin ekleme veya çıkarma işlemine göre ilgili seçenek olarak Ekle seçeneği seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1459.png)

Son olarak ekranın sol üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1460.png) butonuna tıklanarak hızlıca klasör yetki düzenlemesi işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1461.png)

Sistem tarafından “İşlemi gerçekleştirmek istediğinize emin misiniz?” mesajında “Tamam” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1462.png)

Sistem tarafından pozisyon/ kullanıcı grubu için yetkiler düzenlenme işlemi yapıldığı ve yetkilerin düzenleme işlemi yapılan pozisyon/kullanıcı grubu bilgisinin verildiği görülür. Klasör bazında yetki verilebileceği gibi yetkiler de bu kısımdan kaldırılabilme işlemide yapılır. Bu menüde İptal edilmiş olan klasörler  üzerinde de yetkilerle ilgili gerekli düzenlemeler yapılabilmektedir.
#### **6.3.13.Dokümanı İptalden Geri Getir.**
**Menü Adı:** Sistem Altyapı Tanımları/ Doküman İşlemleri/ Dokümanı İptalden Geri Getir

İptal edilmiş bir dokümanın iptalden geri çekilerek, tekrar kullanıma alınabildiği menüdür.

Dokümanı İptalden Geri Getir menüsüne gelinir. Filtre sekmesindeki Klasör Kodu, Doküman Kodu veya Doküman Adı gibi alanlar doldurulduktan sonra ![ref282] (Ara) butonu ile filtreleme işlemi gerçekleştirilerek, istenen kriterlere göre dokümanlar ekrana getirilir. Dokümanlarını seçim işleminde sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1464.png) butonu tıklanarak dokümanlarının iptalden geri getirme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1465.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref283]:Listede seçili iptal durumundaki dokümaların iptalden geri getirme işlemi yapılır.Listede seçili olan dokümanlar iptalden tekrar kullanıma geri döndürülür.

![ref257]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref258]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref259]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip-gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Dokümanı İptalden Geri Getir ekranında Doküman Arama sekmesinde Bağlı Olduğu Klasör alanında ![ref284] butonu tıklanarak Doküman Klasörü listesinde Klasör seçim işlemi yapılarak ![ref211] (Ara) butonu tıklanılır.  

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1468.png)

Liste sekmesinde  iptal işlemi  yapılan  dokümanların listelenmesi sağlanır. Dokümanı İptalden Geri Getir yapılacak dokümanlar listeden seçilir ve  ![ref283]butonu tıklanılarak dokümanların iptalden geri getirme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1469.png)

Sistem tarafından “İptalden geri döndürmek istediğinize emin misiniz? Bu işlem sonucunda dokumanın klasörü pasif ise Klasör de aktif edilecektir.” mesajında “Tamam” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1470.png)

Sistem tarafından “Seçilen dokuman(lar) başarıyla geri getirilmiştir.” mesajı verilerek seçilen dokümanların iptalden geri getirme işlemi yapılır. Dokümanlar iptal edilmeden önce hangi klasörün içinde bulunuyorsa yine aynı klasöre geri gitmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1471.png)
#### **6.3.14.Dokümanı Sil**
**Menü Adı:** Sistem Altyapı Tanımları/ Doküman İşlemleri/ Dokümanı Sil

Seçilen dokümanların sistemden tamamen silinmesi işleminin gerçekleştirildiği menüdür. Bu işlem sonrası dokümanlara bir daha ulaşılamaz ve sistem veri tabanında da bu doküman saklayamaz. Dokümanı Sil menüsüne gelinir. Filtre sekmesindeki Klasör Kodu, Doküman Kodu veya Doküman Adı gibi alanlar doldurulduktan sonra ![ref282] (Ara) butonu ile filtreleme işlemi gerçekleştirilerek, istenen kriterlere göre dokümanlar ekrana getirilir. Dokümanlarını seçim işleminde sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1472.png) butonu tıklanarak dokümanlarının silinme  işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1473.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref285]:Listede seçili dokümanın silinme işlemi yapılır.

![ref32]: Kayıtlar filtrelenerek arama yapılır.

![ref4]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref5]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref149]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip-gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Doküman Sil ekranında doküman arama sekmesinde filtre arama kriterleri olan “Doküman Kodu” alanında doküman kodu yazılarak  ![ref211] (Ara) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1475.png)

Doküman Sil  ekranında doküman listesi sekmesinde  yapılan filtredeki  arama kriterlerine göre kayıtlar listelenir.Doküman listesi sekmesinde listelenen doküman seçilerek ![ref286] butonu tıklanarak dokümanın silinme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1477.png)

Sistem tarafından “Seçili kaydı silmek istediğiniz emin misiniz?” mesajında “Tamam” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1478.png)

Sistem tarafından “Seçilen dokuman(lar) başarıyla silinmiştir” mesajın verilerek doküman silinme işleminin gerçekleştiği belirtilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1479.png)
#### **6.3.15.Taslak Dokümanı Sil**
**Menü Adı:** Sistem Altyapı Tanımları/ Doküman İşlemleri/Taslak Dokümanı Sil

Taslak durumu Görüş,Görüşten Dönen, İlk kontrol,İlk Kontrol Ret , İptal, Saklanan gibi statüsünde  bulunan dokümanların tamamen silinme işlemin gerçekleştiği menüdür. Bu işlem sonrası dokümanlara bir daha ulaşılamaz ve sistem veri tabanında da bu doküman saklanmaz. Taslak Dokümanı Sil menüsüne tıklanılır. Taslak Doküman Sil ekranında doküman listesi ve doküman arama sekmeleri karşımıza çıkar. Doküman arama sekmesinde arama kriterlerine göre filtreleme yapılarak Doküman listesinde bu arama kriterlerine göre ilgili kayıtlarının listelenmesi sağlanır.Listelenen kayıtlar seçilerek ![ref285] butonu tıklanarak taslak aşamasındaki dokümanların silinme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1480.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref285]:Listede seçili taslak durumundaki dokümanın silinme işlemi yapılır.

![ref32]: Kayıtlar filtrelenerek arama yapılır.

![ref4]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref5]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref149]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip-gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Taslak Doküman Sil ekranında doküman arama sekmesinde filtre arama kriterleri olan “Doküman Kodu ” alanında doküman kodu yazılarak  ![ref211] (Ara) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1481.png)

Taslak Doküman Sil  ekranında doküman listesi sekmesinde  yapılan filtredeki  arama kriterlerine göre kayıtlar listelenir.Doküman Listesi sekmesinde listelenen doküman seçilerek ![ref287] butonu tıklanarak statüsü “Saklanan” taslak aşamasındaki dokümanın silinme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1483.png)

Sistem tarafından “Seçili kaydı silmek istediğiniz emin misiniz?” mesajında “Tamam” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1484.png)

Sistem tarafından “Seçilen dokuman(lar) başarıyla silinmiştir” mesajın verilerek doküman silinme işleminin gerçekleştiği belirtilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1485.png)
#### **6.3.16.Kontrollü Kopya Dağıtım Görevi Sil**
**Menü Adı:** Sistem Altyapı Tanımları/ Doküman İşlemleri/ Kontrollü Kopya Dağıtım Görevi Sil

Kontrollü kopya dağıtım görevi silinme işlemin gerçekleştiği menüdür. Kontrollü kopya dağıtım görevi sil ekranında Doküman Listesi ve Doküman Arama sekmeleri karşımıza çıkar. Doküman Arama sekmesinde arama kriterlerine göre filtreleme yapılarak Doküman listesinde bu arama kriterlerine göre ilgili kayıtlarının listelenmesi sağlanır.Listelenen kayıtlar seçilerek ![ref285] butonu tıklanarak kontrollü kopya dağıtım görevlerin  silinme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1486.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref285]:Listede seçili kontrollü kopya dağıtım görevi silinme işlemi yapılır.

![ref32]: Kayıtlar filtrelenerek arama yapılır.

![ref4]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref5]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref149]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip-gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Kontrollü Kopya Dağıtım Görevi Sil ekranında doküman arama sekmesinde filtre arama kriterleri olan “Doküman Kodu ” alanında doküman kodu yazılarak  ![ref211] (Ara) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1487.png) Kontrollü Kopya Dağıtım Görevi Sil  ekranında doküman listesi sekmesinde  yapılan filtredeki  arama kriterlerine göre kayıtlar listelenir.Doküman Listesi sekmesinde listelenen doküman seçilerek ![ref286] butonu tıklanarak kontrollü kopya dağıtım görevlerinin  silinme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1488.png)

Sistem tarafından “Seçili kaydı silmek istediğiniz emin misiniz?” mesajında “Tamam” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1489.png)

Sistem tarafından “İşleminiz başarıyla gerçekleştirilmiştir.”mesajı verilerek kontrollü kopya dağıtım görevlerinin silinme işleminin gerçekleştiği bilgisi belirtilir.![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1490.png)
#### **6.3.17.Dokümanı Başka Klasöre Taşı**
**Menü Adı:** Sistem Altyapı Tanımları/ Doküman İşlemleri/ Dokümanı Başka Klasöre Taşı

Sistemde tanımlı olan bir dokümanın, bağlı olduğu klasör dışında başka bir klasöre taşınması işleminin yapıldığı menüdür.Dokümanı başka klasöre taşı ekranında  liste ve filtre sekmeleri karşımıza çıkar. Filtre sekmesinde arama kriterlerine göre filtreleme işlemi yapılır. Liste sekmesinde listelenen doküman seçilir. Seçilen dokümanlar Hedef klasör belirlenerek  ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1491.png) butonu tıklanarak hedef klasöre taşınma işlemi yapılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1492.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref288]:Listede seçili dokümanların hedef klasöre taşınma işlemi yapılır.

![ref32]: Kayıtlar filtrelenerek arama yapılır.

![ref4]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref5]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref149]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip-gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Dokümanı Başka klasöre Taşı ekranında doküman arama sekmesinde filtre arama kriterleri olan “Doküman Kodu ” alanında doküman kodu yazılarak  ![ref211] (Ara) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1494.png)

Dokümanı Başka klasöre Taşı ekranında doküman listesi sekmesinde  yapılan filtredeki  arama kriterlerine göre kayıtlar listelenir.Listen sekmesinde listelenen  dokümanın seçim işlemi yapılır.Listesi ekranında Hedef klasör alanında ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1495.png)  butonu tıklanarak açılan sistemde tanımlı Doküman klasör listesinde hedef klasör seçilir. Doküman listesinde doküman  ve taşınacak hedef klasör seçim işleminde sonra ![ref288] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1496.png)

Sistem tarafından “Seçili dokümanları taşımak istediğinizden emin misiniz” mesajında “Tamam” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1497.png)

Sistem tarafından “Seçilen dokuman(lar) başarıyla taşınmıştır.” mesajı verilerek seçilen doküman seçilen hedef klasöre taşınma işleminin gerçekleştiği belirtilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1498.png)
#### **6.3.18.Doküman Okundu Yapıcı**
**Menü Adı:** Sistem Altyapı Tanımları/ Doküman İşlemleri/ Doküman Okundu Yapıcı

Seçilen personel veya tüm personeller için belirlenen dokümanlar “okundu” statüsüne getirildiği menüdür. Açılan ekranda Klasör Kodu, Doküman Kodu ve Doküman Adı gibi çeşitli kriterlere göre filtreleme işlemi yapılarak doküman listesi açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1499.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref289]: Seçili olan dokümanlar seçili olan personel/kullanıcı grubu için “okundu” yapma işlemi yapılır.

![ref290]: Seçili olan dokümanlar, herkes için “okundu” yapma işlemi yapılır.

![ref29]: Kayıtlar filtrelenerek arama yapılır.

![ref291]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref292]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref293]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip-gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Doküman Okundu Yapıcı ekranında Filtre sekmesinde Bağlı Olduğu Klasör alanında ![ref294] butonu tıklanarak Doküman Klasörü listesinde Klasör seçim işlemi yapılarak ![ref29] (Ara) butonu tıklanılır.  

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1506.png)

Doküman Okundu Yapıcı ekranında liste sekmesinde arama kriterlerine göre dokümanlar listenir.Listelenen doküman listesinde seçim işlemi yapılır. Doküman Okundu Yapıcı ekranında Personel/ Kullanıcı Grubu seçim işlemi yapılır. Doküman Okundu Yapıcı ekranında ![ref289]butonu tıklanarak seçili olan dokümanlar seçili olan kullanıcı grubu personelleri  için “okundu” yapılma işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1507.png)

Sistem tarafından “Seçili Dokumanlar ilgili personel için Okundu yapılacak.Devam etmek istediğinize emin misiniz?” mesajında “Tamam” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1508.png)

Sistem tarafından “İşleminiz başarıyla gerçekleştirilmiştir.” mesajı verilerek seçili kullanıcı grubu personelleri için seçilen dokümanların “okundu” yapılma işlemi gerçekleştiği belirtilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1509.png)Eğer istenirse ![ref290] butonu yardımıyla seçili olan dokümanlar, herkes için “okundu” yapılabilir. “Önemlileri okundu yapma” seçeneği işaretlenirse önemli doküman olarak okuma görevi düşen dokümanlar “okundu” statüsüne getirilmez.
#### **6.3.19.Doküman Dağıtım Mailleri Oluşturma**
**Menü Adı:** Sistem Altyapı Tanımları/ Doküman İşlemleri/ Doküman Dağıtım Mailleri Oluşturma

Doküman hazırlanırken dağıtım matrisi ile oluşturulan okuma görevlerinin belirlenen personellere/ kullanıcı gruplarına tekrar düşmesini sağlandığı veya sisteme yeni tanımlanan kişilere okuma görevi atandığı menüdür. Doküman Dağıtım Mailleri oluşturma ekranında klasöre bağlı dokümanlar filtrasyon yardımı ile listelenir. Listelenen dokümanların seçim işleminde sonra ![ref295]/![ref296]/![ref297] butonları  tıklanarakTüm Kişilere/ Okumayan Kişilere/Seçilen kişiye doküman dağıtım maili gönderilme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1513.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref298]:Tüm kişilere dağıtım maili gönderilme işlemi yapılır.

![ref299]:Okunmayan kişilere dağıtım maili gönderilme işlemi yapılır.

![ref300]:Seçilen kişilere dağıtım maili gönderilme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1517.png):Okuyacak kişilere ekleme işlemi yapılır.

![ref32]: Kayıtlar filtrelenerek arama yapılır.

![ref4]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref5]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref149]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip-gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Doküman Dağıtım Mailleri oluşturma menüsüne tıklanılır. Klasör Seç alanında ![ref273] butonu tıklanarak açılan Doküman Klasörü listesinde klasör seçilir.Yalnızca seçili klasörün dokümanları listele seçeneği seçilerek  ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1518.png) (Ara) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1519.png)Dağıtım Mailleri Oluşturma ekranında  klasöre bağlı dokümanların filtrasyon yardımı ile listelenmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1520.png)

Dağıtım Mailleri Oluşturma ekranında listelenen dokümanların seçim işlemi yapılır. Önemli olarak okunacaklar maili gitsin istenirse ilgili check-box işaretlenir. Dokümanların seçim işleminde sonra ![ref298] butonu tıklanarak tüm kullanıcılara dağıtım maili gönderilme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1521.png)

Sistem tarafından “Doküman mailleri ilgili kişilere gönderilmiştir.” mesajı verilerek tüm kullanıcılara dağıtım maili gönderilme işleminin yapıldığı belirtilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1522.png)

Doküman dağıtım mailleri oluşturma ekranında seçilen kişiye mail gitmesi için okuyacak kişi alanına kişi atanma işlemi yapılarak doküman listesinde dokümanların seçim işlemi yapılarak ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1523.png)butonu tıklanarak  doküman dağıtım matrisine ilgili kişi atanma işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1524.png)

Doküman Dağıtım Mailleri Oluşturma ekranında durum alanında doküman dağıtım matrisine ilgili kişi atanma işleminin tamamlandığı bilgisi verilir.![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1525.png)
#### **6.3.20.Doküman Print Formatı Tanımlama**
**Menü Adı:** Sistem Altyapı Tanımları/ Doküman İşlemleri/ Doküman Print Formatı Tanımlama

Doküman şablonlarında yer alan alt bilgi/ üst bilgi alanlarının tanımlandığı menüdür. Daha sonra tanımlanan bu format klasör tanımlama menüsünden ilgili klasörü açıp klasör ayarları sekmesinde Doküman Print Formatı alanından  tanımlı doküman print formatı seçilerek klasör bazlı olarak tanımlanabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1526.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref301]:Yeni bir Doküman Print Format tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1528.png):Listede seçili Doküman Print Format bilgisi üzerinde değişiklik ve düzenleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1529.png): Listede seçili Doküman Print Format bilgisi

![ref4]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref5]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref149]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip-gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Doküman Print Format ekranında yeni bir Doküman Print Format tanımlamak için ![ref301] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1530.png)

Doküman Print formatı tanımlama menüsünden header(üst), footer(alt) ve sol-sağ-orta bölüm seçimi yaparak hangi alanların doküman görmede çıkacağı belirtilir ve ekranın sol üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1531.png) butonu tıklanarak Doküman Print Formatı tanımlama kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1532.png)

Entegre Yönetim Sistemi/ Doküman İşlemleri/ Klasör Tanımlama menüsü tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1533.png)

Klasör tanımlamada kayıt güncelleme botunu tıklanarak, klasör ayarlarında Doküman Print Format seçilerek kaydedilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1534.png)

Entegre Yönetim Sistemi/ Doküman İşlemleri/ Doküman Görme menüsünde tıklanılır. Açılan Doküman Görme ekranında klasör ağacı listesinde Doküman Print Formatı seçilen klasör seçilerek listelenen doküman listesinde doküman kodu tıklanarak dokümanın Doküman Print Formatının görüntüleme şekli görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1535.png)
#### **6.3.21.Toplu Doküman Gözden Geçirme**
**Menü Adı:** Sistem Altyapı Tanımları/ Doküman İşlemleri/ Toplu Doküman Gözden Geçirme

Qdms‘ e ilk toplu aktarım yapıldığında dokümanlar revizyon tarihine göre klasörde belirlenen gözden geçirme süresini geçtiyse Bekleyen İşlerim menüsüne çok fazla gözden geçirme görevleri düştüğü için, bu menü özelliği getirilmiştir. Toplu Gözden Geçirme menüsüne gelinir. Filtrasyon yardımı ile hangi dokümanların toplu bir şekilde gözden geçirileceği seçilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1536.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1537.png):Listede seçili dokümanları gözden geçirme işlemi yapılır.

![ref32]: Kayıtlar filtrelenerek arama yapılır.

![ref4]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref5]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref149]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip-gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Toplu Doküman Gözden Geçirme ekranında doküman arama sekmesinde Bağlı Olduğu Klasör alanında ![ref302] butonu tıklanarak doküman klasörü listesinde klasör seçim işlemi yapılarak ![ref32] (Ara) butonu tıklanılır.  

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1539.png)

Doküman listesinde gözden geçirme işlemi yapılacak dokümanların listelenmesi sağlanır.Gözden geçirme işlemi yapılacak dokümanlar listeden seçilir ve ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1540.png) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1541.png)

Sistem tarafından “Seçilen dokümanların gözden geçirme işlemi yapılacaktır, onaylıyor musunuz?” mesajında “Tamam” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1542.png)

Açılan ekranında Gözden Geçirme Tarihi alanında açılan Takvim alanında Gözden geçirme tarihi seçilir ve gözden geçirme işlemi ile açıklama bilgisi yazılarak ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1543.png) butonu tıklanarak toplu gözden geçirme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1544.png)

Sistem tarafından “Seçilen dokümanların gözden geçirme işlemi tamamlanmıştır.” mesajı verilerek toplu gözden geçirme işleminin yapıldığı belirtilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1545.png)
#### **6.3.22.Doküman Parametreleri**
**Menü Adı**: Sistem Altyapı Tanımları/ Doküman İşlemleri/ Doküman Parametreleri

Doküman Yönetimi Modülü için kullanıcıların istek ve ihtiyaçlarına göre çeşitli ayarlamalar yapabildiği ve bunlara göre parametreleri belirlediği (seçebildiği) menüdür. Filtre sekmesinde Modüller alanında Doküman İşlemleri Modülü seçili olarak gelir ve Liste sekmesinde  Doküman İşlemleri Modülü parametreleri listelenir. Seçili parametre bilgisi üzerinden  değişiklik yapmak için ![ref303]butonu kullanılır. Filtre sekmesinde parametre no ve parametre tanımı arama kriterlerine göre filtreleme işlemi yapıldığı gibi liste sekmesinde ise gridde parametre no ve tanım alanlara göre de arama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1547.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref303]:Listede seçili parametre üzerinde değişiklik ve düzenleme işlemi yapılır.

![ref32]: Kayıtlar filtrelenerek arama yapılır.

![ref4]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref5]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref149]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip-gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Parametreler ekranında liste sekmesinde 1 numaralı parametreler seçili iken ![ref303] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1548.png)

Açılan parametreler ekranında “Doküman Okuma Süresi” parametresinin parametre değeri bilgisi üzerinde değişiklik yapılır. İstenirse parametreler ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1549.png) butonu tıklanarak parametrenin parametre değeri ile ilgili varsayılan değeri bilgisinin gelmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1550.png)

Gerekli alanlar ilgili bilgiler girildikten sonra ekranın sol üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1551.png)butonu tıklanarak parametre kayıt güncelleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1552.png)

Parametreler ekranında ![ref303] butonu tıklanarak seçili pasif parametrenin parametre değeri “Evet”seçilerek parametreyi aktif etme, seçili aktif edilenen parametrenin parametre değeri “Hayır” seçilerek parametreyi pasif etme işlemi,  seçili parametrenin varsa değeri değiştirme işlemleri  ve seçili parametrenin varsayılan değeri seçme işlemleri yapılır.
#### **6.3.23.Toplu Doküman İptali**
**Menü Adı:** Sistem Altyapı Tanımları/ Doküman İşlemleri/ Toplu Doküman İptali

Dokümanların toplu şekilde iptal işleminin yapıldığı menüdür. Toplu Doküman İptali menüsüne gelinir. Filtrasyon yardımı ile hangi dokümanların toplu şekilde iptal edileceği seçilir.Doküman seçim işleminden sonra ![ref304] butonu tıklanarak dokümanların iptal etme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1554.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref304]:Listede seçili dokümanların iptal etme işlemi yapılır.

![ref32]: Kayıtlar filtrelenerek arama yapılır.

![ref4]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref5]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref149]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip-gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Toplu Doküman İptali ekranında doküman arama sekmesinde Bağlı Olduğu Klasör alanında ![ref302] butonu tıklanarak doküman klasörü listesinde klasör seçim işlemi yapılarak ![ref32] (Ara) butonu tıklanılır.  

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1555.png)

Doküman listesinde toplu doküman iptal işlemi  yapılacak dokümanların listelenmesi sağlanır. Toplu Doküman İptali işlemi yapılacak dokümanlar listeden seçilir ve  ![ref304]butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1556.png)

Açılan ekranda İptal eden kişi sistem giren olarak gelir ve  istenirse iptal eden alanında ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1557.png) butonu tıklanarak personel listesinden  iptal eden kişi bilgisi seçilir.İptal Nedeni alanında dokümanların neden iptal edildiği bilgisi yazılarak ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1558.png) butonu tıklanarak dokümanların toplu iptal işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1559.png)

Sistem tarafından “Seçili dokümanları iptal etmek istediğinize emin misiniz?” mesajında “Tamam” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1560.png)

Sistem tarafından “İptal işlemi tamamlandı, aşağıdaki dokümanlar revizyonda olduğundan iptal edilememiştir.” mesajı verilerek revizyon işleminde  olan dokümanın dışında dokümanın iptal işlemlerinin gerçekleştiği bilgisi verilir. Toplu Doküman İptal İşlemi yapılırken Revizyon işlemi devam eden dokümanlar için Toplu Doküman İptali işleminin gerçekleştirilemeyeceği göz önünde bulundurulmalıdır.


![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1561.png)
#### **6.3.24.Toplu Doküman Askıya Alma**
**Menü Adı:** Sistem Altyapı Tanımları/ Doküman İşlemleri/ Toplu Doküman Askıya Alma

Dokümanların toplu bir şekilde askıya alma işleminin gerçekleştiği menüdür. Askıya Alma menüsüne gidilir. Doküman Arama sekmesinde Doküman türü ve Bağlı Olduğu klasör seçilerek ![ref32] (Ara) butonunu tıklanarak dokümanlar listelenir.Doküman Listesi sekmesinde listenenen dokümanları seçim işlemi yapılarak ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1562.png) butonu tıklanarak toplu doküman askıya alma işlemi yapılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1563.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref305]:Listede seçili dokümanların askıya alma işlemi yapılır.

![ref32]: Kayıtlar filtrelenerek arama yapılır.

![ref4]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref5]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref149]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Toplu Doküman Askıya Alma ekranında doküman arama sekmesinde Bağlı Olduğu Klasör alanında ![ref302] butonu tıklanarak Doküman Klasörü listesinde Klasör seçim işlemi yapılarak ![ref32] (Ara) butonu tıklanılır.  

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1565.png)

Doküman listesinde toplu doküman askıya alma yapılacak dokümanların listelenmesi sağlanır. Toplu Doküman Askıya Alma işlemi yapılacak dokümanlar listeden seçilir ve  ![ref305]butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1566.png)

Sistem tarafından “Seçili dokümanları askıya almak istediğinize emin misiniz?” mesajında “Tamam” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1567.png)

Sistem tarafından “Seçili dokümanlar askıya alınmıştır.” mesajı verilerek seçilen dokümanlar için toplu doküman askıya alma işleminin yapıldığı belirtirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1568.png)
#### **6.3.25.E-Posta Ayarları**
**Menü Adı:** Sistem Altyapı Tanımları/ Doküman İşlemleri/ E-Posta Ayarları

E-Posta Ayarları ekranında, Doküman İşlemleri  süreçlerinin hangi aşamasında kimlere mail ve sms gönderimi yapılacağı belirlendiği menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1569.png)

**Ekranda bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1570.png): Listede seçili olan  E-postaları  değeri bilgisi üzerinde düzenleme/değişiklik/güncelleme işlemi yapılır.

![ref185]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref186]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref187]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip-gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

**E- Posta Ayarlarında SMS  bildirimi kullanılacak ise;** 

Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/ Parametreler menüsü tıklanılır. Açılan Parametreler ekranında listelenen Sistem Altyapı Tanımları  modülü parametrelerinde 102 numaralı “SMS bildirimi kullanıcak mı?” parametresinin parametreler ekranında Filtre sekmesinde parametre no alanına parametre numarası yazılarak ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1571.png) (Ara) butonu tıklanarak aratılarak seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1572.png)

Sistem Alyapı Tanımları modülü parametrelerinde 102 numaralı “SMS bildirimi kullanıcak mı?” parametresi seçildikten sonra ![ref306] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1574.png)

Açılan parametreler ekranın parametre değeri “Evet” seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1575.png)

Parametreler ekranında parametre değeri “Evet” seçildikten sonra ekranın sol üstte yer alan ![ref307] butonu tıklanarak parametreyi aktif etme kayıt işlemi  yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1577.png)

Parametre Aktif edildikten sonra E- Posta Ayarları ekranında SMS bildirimi kullanılması ile ilgili “SMS gitsin mi?” alanı ile ilgili check box görüntülenir.  İlgili check box işaretlenerek E-Posta ayarlarında SMS bildirimi kullanılır.

Hangi basamakta e-posta/ mesaj gitmesi isteniyorsa seçilir ve  ![ref306] butonu tıklanılır. 

Örn:E-Posta Ayarları ekranında “Görüş Bekleyen Dokümanlar “ basamağı seçilir ve ![ref308] butonu tıklanılır.  

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1579.png)

Açılan E-Posta Ayarları/ Görüş Bekleyen Dokümanlar ekranı görüntülenir. Roller kısmı, e-posta ve mesaj bildirimimin gideceği rolü yani kişiyi göstermektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1580.png)

E-Posta Ayarları/ Görüş Bekleyen Dokümanlar ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1581.png)  butonu tıklanarak açılan sistemde tanımlı Mesaj Gövdesi listesinde  gönderilecek mesaj gövdesi ilgili listeden seçilir. Yanlış eklenen bir mesaj gövdesini silmek içinse ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1582.png)  butonu kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1583.png)

Mesaj Gövdesi listesinde mesaj gövdesi seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1584.png) butonu tıklanarak  mesaj gövdesinin içeriği detaylı bir şekilde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1585.png)

İlgili roller için gidecek mesaj gövdeleri mesaj gövdesi listesinde  mesaj gövdesi seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1586.png) butonu tıklanarak seçilme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1587.png)

Kime E-Posta gitmesi isteniyorsa, o rolle ilgili “E-Posta Gitsin Mi/ SMS Gitsin Mi” check box ‘ı işaretlenir.Mesaj gitmesi için rolde tanımlı olan kişinin cep telefon numarası personel tanımlama ekranında tanımlı olmalıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1588.png)

E-Posta Ayarları/ Görüş Bekleyen Dokümanlar ekranında E-Posta gitmesi  rollerle  ilgili “E-Posta Gitsin Mi/ SMS Gitsin Mi” check box ‘ı işaretlendikten sonra ekranın sol üstte köşede yer alan ![ref309] (Kaydet) butonu tıklanarak E- Posta Ayarları kayıt işlemi gerçekleştirilir.
#### **6.3.26.Toplu Doküman Aktifleme**
**Menü Adı:** Sistem Altyapı Tanımları/ Doküman İşlemleri/ Toplu Doküman Aktifleme

Askıya alınan dokümanları toplu bir şekilde aktifleme işlemi yapıldığı menüdür.  Toplu Doküman Aktifleme menüsüne gelinir. Doküman Arama sekmesinde arama kriterlerinde  Doküman türü ve Bağlı Olduğu klasör seçilerek ![ref32] (Ara) butonunu tıklanarak Dokümanlar listelenir.Doküman Listesinde listelenen dokümanların seçim işlemi yapıldıktan sonra ![ref310] butonu tıklanarak toplu doküman aktifleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1591.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref310]:Listede seçili dokümanların aktifleme işlemi yapılır.

![ref311]: Kayıtlar filtrelenerek arama yapılır.

![ref312]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref313]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref314]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip-gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Toplu Doküman Aktifleme ekranında Doküman Arama sekmesinde Bağlı Olduğu Klasör alanında ![ref315] butonu tıklanarak Doküman Klasörü listesinde Klasör seçim işlemi yapılarak ![ref311] (Ara) butonu tıklanılır.  

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1597.png)

Doküman listesinde toplu doküman aktifleme yapılacak dokümanların listelenmesi sağlanır. Toplu Doküman aktifleme  yapılacak dokümanlar listeden seçilir ve  ![ref310]butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1598.png)

Sistem tarafından “Seçili dokümanları aktiflemek istediğinize emin misiniz?” mesajında “Tamam” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1599.png)

Sistem tarafından “Seçili dokümanlar aktiflenmiştir.” mesajı verilerek seçilen askıya alınan dokümanları toplu bir şekilde aktifleme işleminin yapıldığı belirtilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1600.png)
#### **6.3.27.Doküman Dağıtım Matrisi Düzenleme**
**Menü Adı:** Sistem Altyapı Tanımları/ Doküman İşlemleri/ Doküman Dağıtım Matrisi Düzenleme

Daha önce Klasörlerde dağıtım matrislerine eklenen kullanıcı grup ve pozisyonlar üzerinde değişiklikler yapmak için kullanılan bir menüdür. Dağıtım Matrisi Düzenleme menüsüne gelinir. Öncelikle filtre sekmesini kullanarak ilgili dokümanlar listelenir.Liste sekmesinde listesinde doküman dağıtım matrisi düzenleme işlemi yapılacak dokümanlar seçilir. Kullanıcı türü alanında kullanıcı grubu seçeneği seçildiğinde Kullanıcı grubu listesinde ve Pozisyon seçeneği seçildiğinde  Pozisyon listesinde seçim işlemleri yapılır. İşlem tipi alanında dağıtım matrisine seçilen kullanıcı grubu yada pozisyona göre ekleme ve çıkarma işlemi göre  yapılacak düzenleme göre uygun olan seçenek seçilir. Dağıtım matrisinde önemli doküman, okunması gereken dokümanlar olmasına ve dokümanda anket  tanımlamasına göre ilgili seçenekler ilgili check box’lar işaretlenerek ekranın sol üst köşesindeki  ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1601.png) butonu tıklanarak  doküman dağıtım matrisi düzenleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1602.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref316]:Listede seçili dokümaların dağıtım matrisi düzenleme kayıt işlemi yapılır.

Doküman Dağıtım Matrisi Düzenlem ekranında Doküman Arama sekmesinde Bağlı Olduğu Klasör alanında ![ref315] butonu tıklanarak Doküman Klasörü listesinde Klasör seçim işlemi yapılarak ![ref311] (Ara) butonu tıklanılır.  

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1604.png)

Doküman listesinde doküman dağıtım matrisi düzenleme işlemi yapılacak dokümanların listelenmesi sağlanır. Doküman dağıtım matrisi düzenleme işlemi yapılacak dokümanlar listeden seçilir.Kullanıcı Türü alanında Kullanıcı Grubu seçeneği seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1605.png) butonu tıklanarak açılan sistemde tanımlı kullanıcı grubu listesinde Kullanıcı grubu seçim işlemi yapılır.İşlem Tipi alanında Ekle seçeneği seçilir. Eklenecek dağıtım matrisi sekmesinde önemli doküman olması göre önemli alanı ve dokümanda anket tanımlama işlemini yapılması ise  anket ile ilgili check box’lar işaretlenerek ekranın sol üst köşesindeki ![ref316]butonu tıklanarak seçilen dokümanlar için doküman dağıtım matrisi düzenleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1606.png)

Sistem tarafından “İşlemi gerçekleştirmek istediğinize emin misiniz?” mesajında “Tamam” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1607.png)

Sistem tarafından “Aşağıdaki pozisyon/kullanıcı grubu için yetkiler düzenlenmiştir.” mesajı verilerek hangi pozisyon/kullanıcı grubunun için yetkilerin düzenliği bilgiside mesajda yer alır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1608.png)

Doküman bazında dağıtım matrisinde ilgili seçenekler ilgili yetki verilebileceği gibi ilgili seçeneklerde yetkiler de bu kısımdan kaldırılabilme işlemide yapılır. Bu menüde iptal edilmiş olan dokümanlar üzerinde de gerekli düzenlemeler yapılabilmektedir.
#### **6.3.28.Doküman Hazırlama/ Revizyon Türü Tanımlama**
**Menü Adı:** Sistem Altyapı Tanımları/ Doküman İşlemleri/ Doküman Hazırlama/Revizyon Türü Tanımlama

Yeni doküman, Yönetsel, Majör, Minör gibi doküman hazırlama/revizyon türünün tanımlama işleminin yapıldığı menüdür.Doküman Hazırlama, Doküman revizyon, Doküman Sisteme aktarma menüleri gibi ekranlarda Doküman bilgiler sekmesinde parametreye bağlı olarak görüntülenen Doküman Hazırlama/Revizyon Türü alanında bu menüden tanımlanan doküman hazırlama/revizyon türü seçeneklerinde seçim yapılır. Bu alan Doküman Yönetimi parametrelerinde 269 numaralı “Hazırlama/Revizyon Türü Kullanılacak mı?” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilerek görüntülenen bir alandır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1609.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref317]:Yeni bir doküman hazırlama/revizyon türü tanımlama işlemi yapılır.

![ref318]:Listede seçili doküman hazırlama/revizyon türü bilgisi üzerinde değişiklik ve güncelleme yapılır.

![ref319]:Listede seçili doküman hazırlama/revizyon türü bilgisi silinir.

Doküman Hazırlama/Revizyon Türü Tanımlama ekranında yeni bir Doküman Hazırlama/Revizyon Türü tanımlamak için ![ref317] butonu tıklanarak Doküman Hazırlama/Revizyon Türü Tanımlama - Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1613.png)

**Açılan ekranda ilgili alanlar tanımlanır;**

**Doküman Hazırlama/Revizyon Türü:** Doküman Hazırlama/Revizyon Türü-Yeni Kayıt ekranında doküman hazırlama/revizyon türünün tanım bilgisinin yazıldığı alandır.

**Eğitim Sorumlusu Boş Gelsin:** Doküman Hazırlama/Revizyon Türü-Yeni Kayıt ekranında tanımlı doküman hazırlama/revizyon türü ilgili check box işaretlenirse  ilgili alanda seçildiğinde eğitim sorumlu alanındaki kişi bilgisinin varsa boşalmasını sağlanır.

**Eğitim Sorumlusu Zorunlu:** Doküman Hazırlama/Revizyon Türü-Yeni Kayıt ekranında tanımlı doküman hazırlama/revziyon türü  ilgili check box işaretlenirse  ilgili alanda seçildiğinde eğitim sorumlu alanındaki kişi bilgisinin zorunlu olması sağlanır.	

**Durum:** Doküman Hazırlama/Revizyon Türü-Yeni Kayıt ekranında tanımlı doküman hazırlama/revziyon türünün aktif ve pasif seçeneklerinde seçim yapılarak durumunun belirlendiği alandır.

Doküman Hazırlama/Revizyon Türü-Yeni Kayıt ekranında Doküman Hazırlama/Revizyon Türünün tanım bilgisi yazılarak , Eğitim sorumlusu boş gelsin alanında ilgili check box işaretlenir. Durum kısmı aktif seçilir. Gerekli alanlar ilgili bilgiler girildikten sonra ekranın sol üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1614.png) buton tıklanarak Doküman Hazırlama/Revizyon Türü tanımlama kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1615.png)
#### **6.3.29.Doküman Ürün Aktarımı**
**Menü Adı:** Sistem Altyapı Tanımları/ Doküman İşlemleri/ Doküman Ürün Aktarımı

Dokümanla ilişkili ürünlerin Excel şablonu üzerinde toplu aktarımı için kullanılan menüdür. Sistemde yüklü olan dokümanlar  ve tanımlı ürünler  ile ilişkilendirilme işlemi yapılır. Bu işlemin yapılması için ![ref276]   butonu tıklanarak bilgisayara indirilen Ürün Doküman  şablonunda Doküman  kod bilgisi alanında sistemde yüklü doküman kod bilgileri yazılarak  ve  Ürün  kod alanında sistemde tanımlı Ürün  kod  bilgileri yazılırak Ürün Doküman  şablonu doldurulur. Ürün Doküman  şablonda ilgili alanlar bilgiler yazıldıktan sonra ![ref277]  butonu tıklanarak Ürün Doküman şablonu Qdms sisteminde menüye yüklenir.Aktarılan veriler aktarım için uygunsa ![ref278]  butonu aracılığıyla aktarım gerçekleşmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1616.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref276] : Ürün Doküman şablonu bilgisayara indirilir.

![ref277] : Doldurulan Ürün Doküman şablon sisteme yüklenir.

![ref278]: Aktarım işlemi gerçekleştirilir.

![ref279]:Veriler Excel’e aktarılır.

![ref4]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref5]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref149]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip-gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Doküman Ürün Aktarımı ekranında ![ref276]butonu tıklanarak Ürün Doküman şablonu bilgisayara indirilir. İndirilen Ürün Doküman şablonunda  ilgili alanlar ilgili bilgiler yazılarak doldurularak  ve bilgisayara kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1617.png)

Doküman Ürün Aktarımı ekranında doldurulan Ürün Doküman şablonu ![ref280] butonu tıklanarak sisteme yükleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1618.png)

Dosya Yükle ekranında “Gözat” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1619.png)

Açılan ekranda doldurulan Ürün Doküman şablonu seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1620.png)

Doküman Ürün Aktarımı ekranında görüntülenen 3. buton olan ![ref278]  tıklanarak Doküman Ürün Aktarım işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1621.png)

Doküman Ürün Aktarımı ekranında durum alanında Doküman Ürün Aktarımı işleminin yapıldığının bitti bilgisi verilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1622.png)

Doküman Ürün aktarım işlemi yapılan dokümanlarda  Doküman Görme menüsünde dokümanlar görüntülendiğinde  ürün sekmesi tıklanarak ilişkilendirme yapılan ürünlerin görüntülenmesi sağlanır.
#### **6.3.30.Kontrollü Kopya Matris Düzenleme**
**Menü Adı**: Sistem Altyapı Tanımları/ Doküman İşlemleri/ Kontrollü Kopya Matris Düzenleme

Doküman üzerinde kontrollü kopya matrislerini toplu olarak dağıtım yeri ekleme ve çıkarma işlemi için kullanılan menüdür. Kontrollü Kopya Matris Düzenleme menüsüne gelinir. Doküman Arama sekmesinden Klasör Kodu alanından Doküman Klasörü Seç Listesinden ilgili klasör seçilerek ![ref32] (Ara) butonu tıklanarak Dokümanlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1623.png)

Liste sekmesinde listelenen dokümanlarını seçim işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1624.png)

Dağıtım Yeri alanında ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1625.png) butonu tıklanarak sistemde tanımlı dağıtım yeri listesinde seçim işlemi yapılarak ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1626.png) butonu tıklanarak Dağıtım yerinin seçim işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1627.png)

Dağıtım yeri ve  doküman seçim işleminde sonra nusha alanında kaç nusha alınacağı bilgisi seçildikten sonra ekranın sol üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1628.png)butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1629.png)

Sistem tarafından “**Dağıtım yeri ilişkileri oluşturulmuştur” mesajı verilerek kontrollü kopya matris düzenleme işleminin yapıldığı belirtilir.**

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1630.png)
#### **6.3.31.Doküman Referans Aktarım**
**Menü Adı:** Sistem Altyapı Tanımları/ Doküman İşlemleri/ Doküman Referans Aktarım

Doküman Yönetim kapsamında birbirleriyle referans olacak dokümanların sistemde “toplu aktarım özelliği” yöntemi ile aktarılma işlemin tek seferde aynı anda yapıldığı menüdür.Birden çok dokümanın birbiriyle referansın tek seferde aktarılma işlemi yapılması için Doküman Referans Aktarım menüsü kullanılır. Bu menüde aktarılma işleminde ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1631.png)butonu ile şablon  bilgisayara indirilir. İndirilen şablona ana doküman kodu  ve İlişkilendirilecek Referans  Doküman kodu bilgileri girilir ve  bilgisayara kaydedilir. Doldurulma işlemi yapılan şablon ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1632.png)butonu ile sisteme yüklenir. Bu şablondaki doküman kodları bilgisi girilen dokümanların sistemde yüklü olması gerekmektedir.  Aksi takdirde  yüklü olmayan doküman kodları girilen dokümanlar için şablon yükleme işlemi yapıldıktan sonra “Doküman ve referans doküman kodu bulanamadı.”şeklinde sistem uyarı mesajını verir. O yüzden sistemde yüklü dokümanlar arasında aktarılma işlemi yapılır. Doküman Referans Aktarım ekranında şablon yükleme işleminde sonra veriler aktarıma uygunsa ![ref278] butonu görüntülenir ve ![ref278]butonu tıklanarak Referans doküman aktarılma işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1633.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref276] : Referans Doküman şablonu bilgisayara indirilir.

![ref277] : Doldurulan Referans Doküman şablon sisteme yüklenir.

![ref278]: Aktarım işlemi gerçekleştirilir.

![ref279]:Veriler Excel’e aktarılır.

![ref4]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref5]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref149]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip-gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Doküman Referans Aktarımı ekranında ![ref276]butonu tıklanarak Referans Doküman şablonu bilgisayara indirilir. İndirilen Referans Doküman şablonunda  ilgili alanlar ilgili bilgiler yazılarak doldurularak  ve bilgisayara kaydedilir. Eğer birden fazla referans doküman girilecek ise alt alta yazılması gerekmektedir.

Örnek: A dokümanına B ve C dokümanları refere edilecek.Excel'e;

A'nın doküman kodu=B'nin doküman kodu

A'nın doküman kodu=C'nin doküman kodu şeklinde şablona yazıılmalıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1634.png)

Doküman Referans Aktarımı ekranında doldurulan Referans Doküman şablonu ![ref280] butonu tıklanarak sisteme yükleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1635.png)

Dosya Yükle ekranında “Gözat” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1636.png)

Açılan ekranda doldurulan Referans Doküman şablonu seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1637.png)

Doküman Referans Aktarımı ekranında görüntülenen 3. buton olan ![ref278]  tıklanarak Doküman Referans Aktarım işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1638.png)

Doküman Referans Aktarımı ekranında durum alanında Doküman Referans Aktarım işleminin yapıldığının bitti bilgisi verilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1639.png)

Doküman Referans Aktarım işleminde sonra ana dokümana referans ilişkisi kurulan dokümanlar Doküman görme menüsünde görüntülenen dokümanın referans sekmesinde görüntülenir.
#### **6.3.32.Gözden Geçirme Öteleme Süresi Tanımlama** 
**Menü Adı:** Sistem Altyapı Tanımları/ Doküman İşlemleri/ Gözden Geçirme Öteleme Süresi Tanımlama

Gözden Geçirme öteleme süresi tanımlama işleminin yapıldığı menüdür.Tanımlanan Gözden Geçirme Öteleme Süresi Doküman Yönetim Modülü raporlarından Doküman Gözden Geçirme Listesi ekranında doküman listesinde doküman seçili iken ![ref232] butonu tıklanılır. Doküman Gözden Geçirme ekranı açılarak dokümanın gözden geçirme işlemi yapıldığı ekranda parametreye bağlı olarak ![ref233] butonu görüntülenir. Doküman Yönetimi parametrelerinde 347 numaralı “	Gözden geçirmede öteleme kullanılacak mı ?” parametresi değeri “Evet” seçilerek  parametre “Aktif” edilir. 

![ref234]

Parametre aktif edildikten sonra gözden geçirrme ekranında  bu buton görüntülenerek gözden geçirme işlemi ay bazında öteleme işlemi yapılır. Açılan ekranında Öteleme süresi(Ay) alanında bu menüde tanımlı Gözden Geçirme Öteleme Süresi  seçeneklerin listesi gelir. Bu alanda Gözden Geçirme Öteleme Süresi  seçeneklerin listesinden seçim yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1640.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref317]:Yeni bir gözden geçirme öteleme süresi  tanımlama işlemi yapılır.

![ref318]:Listede seçili Gözden Geçirme Öteleme Süresi bilgisi üzerinde değişiklik ve güncelleme yapılır.

![ref319]:Listede seçili gözden geçirme öteleme süresi  bilgisi silinir.

Gözden Geçirme Öteleme Süresi Tanımlama ekranında yeni bir Gözden Geçirme Öteleme Süresi Tanımlama için ![ref317] butonu tıklanarak Gözden Geçirme Öteleme Süresi Tanımlama - Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1641.png)

**Açılan ekranda ilgili alanlar tanımlanır;**

**Öteleme Tipi:** Gözden Geçirme Öteleme Süresi Tanımlama - Yeni Kayıt ekranında Öteleme Tipi tanım bilgisinin yazıldığı alandır.

**Öteleme Süresi(ay):** Gözden Geçirme Öteleme Süresi Tanımlama - Yeni Kayıt ekranında öteleme süresinin ay olarak bilgisinin yazıldığı alandır.

**Durum:** Gözden Geçirme Öteleme Süresi Tanımlama - Yeni Kayıt ekranında Gözden Geçirme Öteleme Süresi tanımın durum bilgisinin aktif ve pasif seçeenklerinde seçildiği alandır.

Gözden Geçirme Öteleme Süresi Tanımlama ekranında öteleme tipi tanım ve  öteleme süresi ay olarak bilgileri yazılır. Durum kısmında aktif ve pasif seçeneklerinde aktif olarak seçilir.Gerekli alanlar ilgili bilgiler girildikten sonra ekranın sol üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1642.png) butonu tıklanarak gözden geçirme öteleme süresi tanımlama kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1643.png)



[ref1]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_10.png
[ref2]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_14.png
[ref3]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_15.png
[ref4]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_16.png
[ref5]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_17.png
[ref6]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_22.png
[ref7]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_26.png
[ref8]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_27.png
[ref9]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_28.png
[ref10]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_30.png
[ref11]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_33.png
[ref12]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_34.png
[ref13]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_36.png
[ref14]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_37.png
[ref15]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_38.png
[ref16]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_39.png
[ref17]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_41.png
[ref18]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_46.png
[ref19]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_47.png
[ref20]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_48.png
[ref21]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_49.png
[ref22]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_51.png
[ref23]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_58.png
[ref24]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_65.png
[ref25]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_68.png
[ref26]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_69.png
[ref27]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_77.png
[ref28]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_82.png
[ref29]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_85.png
[ref30]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_86.png
[ref31]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_88.png
[ref32]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_91.png
[ref33]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_94.png
[ref34]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_104.png
[ref35]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_112.png
[ref36]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_114.png
[ref37]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_115.png
[ref38]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_123.png
[ref39]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_124.png
[ref40]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_125.png
[ref41]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_126.png
[ref42]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_127.png
[ref43]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_128.png
[ref44]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_129.png
[ref45]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_130.png
[ref46]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_131.png
[ref47]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_132.png
[ref48]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_133.png
[ref49]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_134.png
[ref50]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_135.png
[ref51]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_151.png
[ref52]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_159.png
[ref53]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_167.png
[ref54]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_175.png
[ref55]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_180.png
[ref56]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_181.png
[ref57]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_192.png
[ref58]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_200.png
[ref59]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_204.png
[ref60]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_208.png
[ref61]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_216.png
[ref62]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_220.png
[ref63]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_224.png
[ref64]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_229.png
[ref65]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_231.png
[ref66]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_243.png
[ref67]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_343.png
[ref68]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_353.png
[ref69]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_359.png
[ref70]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_368.png
[ref71]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_377.png
[ref72]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_381.png
[ref73]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_386.png
[ref74]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_387.png
[ref75]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_392.png
[ref76]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_395.png
[ref77]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_404.png
[ref78]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_415.png
[ref79]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_422.png
[ref80]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_434.png
[ref81]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_437.png
[ref82]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_440.png
[ref83]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_447.png
[ref84]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_449.png
[ref85]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_456.png
[ref86]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_482.png
[ref87]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_483.png
[ref88]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_484.png
[ref89]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_486.png
[ref90]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_489.png
[ref91]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_496.png
[ref92]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_497.png
[ref93]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_498.png
[ref94]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_499.png
[ref95]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_500.png
[ref96]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_501.png
[ref97]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_502.png
[ref98]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_503.png
[ref99]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_510.png
[ref100]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_535.png
[ref101]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_537.png
[ref102]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_538.png
[ref103]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_539.png
[ref104]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_542.png
[ref105]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_543.png
[ref106]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_561.png
[ref107]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_562.png
[ref108]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_563.png
[ref109]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_566.png
[ref110]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_567.png
[ref111]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_568.png
[ref112]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_569.png
[ref113]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_570.png
[ref114]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_571.png
[ref115]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_572.png
[ref116]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_573.png
[ref117]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_574.png
[ref118]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_575.png
[ref119]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_591.png
[ref120]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_593.png
[ref121]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_605.png
[ref122]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_616.png
[ref123]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_617.png
[ref124]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_618.png
[ref125]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_619.png
[ref126]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_621.png
[ref127]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_625.png
[ref128]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_632.png
[ref129]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_634.png
[ref130]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_639.png
[ref131]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_644.png
[ref132]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_652.png
[ref133]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_658.png
[ref134]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_662.png
[ref135]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_663.png
[ref136]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_673.png
[ref137]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_684.png
[ref138]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_755.png
[ref139]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_766.png
[ref140]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_769.png
[ref141]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_770.png
[ref142]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_771.png
[ref143]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_786.png
[ref144]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_794.png
[ref145]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_803.png
[ref146]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_805.png
[ref147]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_806.png
[ref148]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_807.png
[ref149]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_808.png
[ref150]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_811.png
[ref151]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_816.png
[ref152]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_836.png
[ref153]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_838.png
[ref154]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_840.png
[ref155]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_846.png
[ref156]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_863.png
[ref157]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_870.png
[ref158]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_871.png
[ref159]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_891.png
[ref160]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_892.png
[ref161]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_893.png
[ref162]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_897.png
[ref163]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_905.png
[ref164]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_906.png
[ref165]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_907.png
[ref166]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_908.png
[ref167]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_912.png
[ref168]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_927.png
[ref169]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_931.png
[ref170]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_933.png
[ref171]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_936.png
[ref172]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_937.png
[ref173]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_938.png
[ref174]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_939.png
[ref175]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_941.png
[ref176]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_945.png
[ref177]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_956.png
[ref178]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_957.png
[ref179]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_958.png
[ref180]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_959.png
[ref181]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_969.png
[ref182]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_970.png
[ref183]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_971.png
[ref184]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_972.png
[ref185]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_973.png
[ref186]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_974.png
[ref187]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_975.png
[ref188]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_978.png
[ref189]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_980.png
[ref190]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_981.png
[ref191]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_982.png
[ref192]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_983.png
[ref193]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_987.png
[ref194]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_998.png
[ref195]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_999.png
[ref196]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1004.png
[ref197]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1005.png
[ref198]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1006.png
[ref199]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1010.png
[ref200]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1014.png
[ref201]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1019.png
[ref202]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1020.png
[ref203]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1024.png
[ref204]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1025.png
[ref205]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1026.png
[ref206]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1027.png
[ref207]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1028.png
[ref208]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1031.png
[ref209]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1035.png
[ref210]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1038.png
[ref211]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1042.png
[ref212]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1043.png
[ref213]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1044.png
[ref214]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1045.png
[ref215]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1046.png
[ref216]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1051.png
[ref217]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1052.png
[ref218]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1053.png
[ref219]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1064.png
[ref220]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1066.png
[ref221]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1067.png
[ref222]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1068.png
[ref223]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1069.png
[ref224]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1070.png
[ref225]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1071.png
[ref226]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1072.png
[ref227]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1073.png
[ref228]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1074.png
[ref229]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1092.png
[ref230]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1093.png
[ref231]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1094.png
[ref232]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1122.png
[ref233]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1130.png
[ref234]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1131.png
[ref235]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1132.png
[ref236]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1133.png
[ref237]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1134.png
[ref238]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1135.png
[ref239]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1136.png
[ref240]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1146.png
[ref241]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1173.png
[ref242]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1205.png
[ref243]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1210.png
[ref244]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1211.png
[ref245]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1212.png
[ref246]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1213.png
[ref247]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1214.png
[ref248]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1217.png
[ref249]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1219.png
[ref250]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1223.png
[ref251]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1243.png
[ref252]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1262.png
[ref253]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1265.png
[ref254]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1271.png
[ref255]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1292.png
[ref256]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1297.png
[ref257]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1298.png
[ref258]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1299.png
[ref259]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1300.png
[ref260]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1305.png
[ref261]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1338.png
[ref262]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1339.png
[ref263]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1340.png
[ref264]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1341.png
[ref265]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1346.png
[ref266]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1348.png
[ref267]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1350.png
[ref268]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1351.png
[ref269]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1356.png
[ref270]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1357.png
[ref271]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1358.png
[ref272]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1359.png
[ref273]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1370.png
[ref274]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1389.png
[ref275]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1395.png
[ref276]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1417.png
[ref277]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1418.png
[ref278]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1419.png
[ref279]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1421.png
[ref280]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1423.png
[ref281]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1437.png
[ref282]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1463.png
[ref283]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1466.png
[ref284]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1467.png
[ref285]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1474.png
[ref286]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1476.png
[ref287]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1482.png
[ref288]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1493.png
[ref289]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1500.png
[ref290]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1501.png
[ref291]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1502.png
[ref292]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1503.png
[ref293]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1504.png
[ref294]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1505.png
[ref295]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1510.png
[ref296]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1511.png
[ref297]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1512.png
[ref298]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1514.png
[ref299]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1515.png
[ref300]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1516.png
[ref301]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1527.png
[ref302]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1538.png
[ref303]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1546.png
[ref304]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1553.png
[ref305]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1564.png
[ref306]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1573.png
[ref307]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1576.png
[ref308]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1578.png
[ref309]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1589.png
[ref310]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1590.png
[ref311]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1592.png
[ref312]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1593.png
[ref313]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1594.png
[ref314]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1595.png
[ref315]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1596.png
[ref316]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1603.png
[ref317]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1610.png
[ref318]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1611.png
[ref319]: https://docsbimser.blob.core.windows.net/imagecontainer/5225d54f-44a0-4f79-8137-3bbe832d981f_1612.png
