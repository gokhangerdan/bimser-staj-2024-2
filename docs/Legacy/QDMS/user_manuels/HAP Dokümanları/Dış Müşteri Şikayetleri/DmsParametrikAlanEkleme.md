---
title: Parametrik Alan Tanımlama İşlemi
description: Parametrik Alan Tanımlama İşlemi Yardım Dokümanı
sidebar_position: 1
---

:::tip Bilgi

İlgili konu başlığına sağ tarafta bulunan navigasyon yardımıyla hızlı bir şekilde ulaşabilirsiniz.

:::


**Dış Müşteri Şikayetleri Modülünde Dil Ayarları Menüsünde Parametrik Alan Tanımlama Kullanıcı Yardım Dokümanı**


## **1.Sistem Altyapı Tanımları**

Personel bilgilerinin tanımlandığı ve diğer modüller için gerekli olan altyapının kurgulanmasının yapıldığı menüdür.

## **1.1.Konfigürasyon Ayarları**

**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları

QDMS sisteminde özel ayarların yapıldığı menülerdir. Bu menülerde yapılan ayarlar tüm QDMS kullanıcıları için geçerli olan ortak ayarlardır.

### **1.1.1. Dil Ayarları**

**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları

Dil ayarları menüsünden QDMS üzerinde görülen menülerin isimleri, alanların isimleri değiştirilebilir. Modüllere yeni alanlar eklenebilir. Var olan alanların zorunluluk durumları düzenlenebilir. Alanların ekran üzerinde göründükleri sıralama değiştirilebilir.

### **1.1.1.1.Dış Müşteri Şikayetleri  Modülü Ortak Kullanım İçin Yeni Alan Oluşturma**

Dış Müşteri Şikayetleri Modülünde Şikayet Detayı Diğer Alanlar, Gelişme Raporu, Kök Nedenler, Aksiyonlar, Sonuç Raporu ve Kapatma sekmelerinde firmanın istemiş olduğu sistemde olmayan ekstradan alanlar tanımlanabilir. Tanımlanan bu alanlar tüm Dış Müşteri Şikayetleri Modül kaynakları için geçerlidir. Sistem Altyapı Tanımları/BSAT/ Konfigürasyon Ayarları/Dil Ayarları menüsü tıklanılır. Açılan Dil Ayarları sayfasında Modül alanında “Dış Müşteri Şikayetleri” seçilir ve ekranda Dış Müşteri Şikayetleri Modülü ile ilgili dil tanımları görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload63e77964-bde4-4ed9-8eec-db0a1335e63a)



Dış Müşteri Şikayetleri Modülünde Entegre Yönetim Sistemi\> Dış Müşteri Şikayetleri \> Dış Müşteri Şikayetleri İşlemleri menüsünde Yeni butonu tıklatıldığında açılan Şikayet Detay ekranında Şikayet Detayı Diğer Alanlar parametrik tipli alan tanımlaması Dil Ayarların menüsünde yapılmaktadır. Ayrıca Dış Müşteri Şikayetleri Modülünde Gelişme Raporu, Kök Neden Analizi, Aksiyonlar, Sonuç Raporu ve Kapatma aşamaların gerçekleştiği sekmelerde Dil Ayarları menüsünde parametrik tipli alan tanımlamasıda yapılmaktır. Bu aşamaların gerçekleştiği sekmelerde örneğin Gelişme Raporu ile ilgili parametrik tipli alan tanımlaması yapıldığında Gelişme Raporu sekmesinde, Kök Neden Analizi ilgili parametrik tipli alan tanımlaması yapıldığında Kök Neden Analizi sekmesinde tanımlanan parametrik alanlar görüntülenmektedir. Hangi sekmede parametrik tipli alan tanımlaması yapıldıysa ilgili sekmede parametrik tipli alanlar görüntülenmektedir. Bu aşamalarda parametrik tipli alanlarda kullanılan kısa kodlar bulunmaktadır. Hangi aşamada hangi kısa kodlar kullanılmış ayırt etmek mümkündür. Örneğin tanımlanan Metin Tipli parametrik tipli alanlarda hangi aşamada olduğunun ayırt etmek için aşağıdaki kısa kodların başlama kısımlarına dikkate etmek gerekir;

**Şikayet Detayı Diğer Alanlar:** lblPARAM1 kısa kodları genelde Şikayet Detayı Diğer Alanlar sekmesinde görüntülen parametrik alanları temsil eder.

**Gelişme Raporu:** lblG_Param1, lblG ile başlayan kısa kodları genelde Gelişme Rpaoru aşamasında görüntülenen parametrik tipli alanları temsil eder.

**Kök Nedenler:** lblKOKPARAM1, lblKOK ile başlayan kısa kodları genelde Kök Neden Analizi aşamasında görüntülenen parametrik tipli alanları temsil eder

**Aksiyonlar:** lblA_Param1, lblA kısa kodları ile başlayan genelde Aksiyonlar aşamasında görüntülenen parametrik tipli alanları temsil eder.

**Sonuç Raporu:** lblS_Param1, lblS kısa kodları ile başlayan genelde Sonuç Raporu aşamasında görüntülenen parametrik tipli alanları temsil eder.

**Kapatma:** lblK_Param1, lblK kısa kodları ile başlayan genelde Kapatma aşamasında görüntülenen parametrik tipli alanları temsil eder.

**Dış Müşteri Şikayetleri Modülünde Tanımlanan Parametrik Tipli Alanlar ve Tanımları;**

**1-Tarih tipli**: Takvim alanı eklenilen parametrik alandır. Örnek Kısa Kod: lblDPARAM1 (Şikayet Detayı Diğer Alanlar sekmesinde parametrik alan tipi görüntülenir.)

**2-Liste tipli**: Birden fazla liste elemanları arasından tek seçim yapılan parametrik alandır. Liste elemanları tanımlanarak, tanımlanan liste elemanlarında seçip yapılır. Örnek Kısa Kod: lblG_LParam2 (Gelişme Raporu sekmesinde parametrik alan tipi görüntülenir.)

**3-Personel Tipli:** QDMS personel veri tabanından kişi seçilebilmesini sağlayan parametrik alandır. Sistem Altyapı Tanımları\>Bsat\>Tanımlama\>Personel Tanımlama menüsünde tanımlı olan Personellerin listesinde seçim yapılır. Örnek Kısa Kod: lblG_PParam2 (Gelişme Raporu sekmesinde parametrik alan tipi görüntülenir.)

**4-Sorgu tipli:** QDMS/Ensemble veri tabanları içerisindeki ana verilerden seçim yapılabilmesi için tanımlanabilen alan türüdür. (Sadece Bimser Destek Ekibi tarafından tanımlanmalıdır) Tekli ve çoklu seçim yapılabilir. Örnek Kısa Kod: lblQPARAM1(Şikayet Detayı Diğer Alanlar sekmesinde parametrik alan tipi görüntülenir.)

**5-Metin tipli**: Elle yazım imkanı veren metin kutucuğu ekleyen parametrik alandır. Örnek Kısa Kod: lblKOKPARAM1(Kök Neden Analizi sekmesinde parametrik alan tipi görüntülenir.)

**6-Metin (Çoklu Satır) Tipli**: Elle yazım imkanı veren karakter sınırı olmayan çok satırlı metin kutucuğu eklenen parametrik alandır. Örnek Kısa Kod: lblPARAM16 (Şikayet Detayı Diğer Alanlar sekmesinde parametrik alan tipi görüntülenir.)

**7- Başlık Tipli:** Formlara koyu harflerle yazılacak başlık alanı ekleyen parametrik alandır. Örnek Kısa Kod: lblBaslikParam1(Şikayet Detayı Diğer Alanlar sekmesinde parametrik alan tipi görüntülenir.)

**8-Ürün Tipli:** QDMS ürün veri tabanından ürün bilgisinin seçilebilmesini sağlayan parametrik alandır. Sistem Altyapı Tanımları\>BSAT\>Tanımlar\>Ürün Tanımlama menüsünde tanımlı Ürün listesinden Ürün bilgisinin seçimi yapılır. Örnek Kısa Kod: lblUPARAM1 (Şikayet Detayı Diğer Alanlar sekmesinde parametrik alan tipi görüntülenir.)

**9**-**Parasal Tipli:** Parasal olarak veri girişi yaptıran parametrik alandır. Tanımlanan parametrik alanın yanında para birimleri seçildiği alan çıkar. Para birimleri seçim alanındaki para birimleri Sistem Altyapı Tanımları\>BSAT\>Tanımlar\>Para Birimleri Tanımlama menüsünde tanımlı olan para birimleridir. Örnek Kısa Kod: lblA_NParam1 (Aksiyonlar sekmesinde parametrik alan tipi görüntülenir)

**10- Ölçü Birimi Tipli:** Ölçü olarak veri girişi yaptıran parametrik alandır. Tanımlanan parametrik alanın yanında Ölçü birimleri seçildiği alan çıkar. Ölçü birimleri seçim alanındaki ölçü Birimleri Sistem Altyapı Tanımları\>BSAT\>Tanımlar\>Ölçü Birimleri Tanımlama menüsünde tanımlı olan ölçü birimleridir. Örnek Kısa Kod: lblS_NParam3 (Sonuç Raporu sekmesinde parametrik alan tipi görüntülenir.)

**11-Müşteri Tipli:** Qdms Müşteri veri tabanından Müşteri seçilebilmesini tekli ve çoklu seçim yapılmasını sağlayan parametrik alandır. Örnek Kısa Kod: lblMPARAM1 (Şikayet Detayı Diğer Alanlar sekmesinde parametrik alan tipi görüntülenir.)

### **1.1.1.1.1. Dış Müşteri Şikayetleri Modülünde Şikayet Detayı Diğer Alanlar Sekmesinde Parametrik Alan Tanımlaması**

Dış Müşteri Şikayetleri Modülünde Şikayet Detayı Diğer Alanlar sekmesinde tanımlanan parametrik alanların kısa kodları lblPARAM başlığı ile tanımlı kısa kodlardır. lblPARAM başlığındaki kısa kodlar olan tüm parametrik tipli alanlar tanımlandığında Dış Müşteri Şikayetleri Modülünde Şikayet Detayı Diğer Alanlar sekmesi ekranında görüntülenir.

### **1.1.1.1.1.1.Tarih Tipli Parametrik Alanların Listesi**

Dış Müşteri Şikayetleri Modülünde Entegre Yönetim Sistemi\> Dış Müşteri Şikayetleri \> Dış Müşteri Şikayetleri İşlemleri menüsünde Yeni butonu tıklatıldığında açılan Şikayet Detayı ekranında Şikayet Detayı Diğer Alanlar sekmesinde Tarih tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Tarih yazarak Tarih tipli parametrik alanlar aratılır ve Tarih tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen tarih tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7056a916-97b3-4e6e-9950-7f3dc5433055)

### **1.1.1.1.1.2.Tarih Tipli Parametrik Alan Tanımlama**

lblDPARAM1 Tarih tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb3deccc7-e055-4662-8e68-9791b0e27c06) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3321d913-b2c6-4ce4-986a-f9d052315401)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d3acb69-6832-4079-ad91-feecc05b6c88)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7cbf1f11-0a29-43b6-8256-93931e45ac92)(Kaydet) butonu tıklanarak tarih tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcaa4811c-0f97-4c4f-b2fe-fb763b15b849)

Tanımlanan Tarih tipli parametik alan Entegre Yönetim Sistemi\> Dış Müşteri Şikayetleri \> Dış Müşteri Şikayetleri İşlemleri menüsünde Yeni butonu tıklatıldığında açılan Şikayet Detayı ekranında Şikayet Detayı Diğer Alanlar sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4bcc6efe-6755-439b-b12e-b8a5c95133a9)

### **1.1.1.1.1.3.Liste Tipli Parametrik Alanların Listesi**

Dış Müşteri Şikayetleri Modülünde Entegre Yönetim Sistemi\> Dış Müşteri Şikayetleri \> Dış Müşteri Şikayetleri İşlemleri menüsünde Yeni butonu tıklatıldığında açılan Şikayet Detayı ekranında Şikayet Detayı Diğer Alanlar sekmesinde Liste tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Liste yazarak Liste tipli parametrik alanlar aratılır ve Liste tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Liste tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc96763f9-6306-4fac-94ae-077f4ae9466b)

### **1.1.1.1.1.4.Liste Tipli Parametrik Alan Tanımlama**

lblLPARAM5 Liste tipli parametrik seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb3deccc7-e055-4662-8e68-9791b0e27c06) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload433191e0-44b3-4d4c-ac55-5c99531d98cd)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload202b7813-34c5-4ac7-aea2-dad923191232)

Liste tipli alanın liste değerlerini girmek için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8fba83f5-4dbd-4b5e-b132-7bd5ea6319a1) (Yeni) butonuna tıklanır, liste değerleri yazılır ve kaydedilir. Liste eleman değeri 1 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc23bc398-1f9f-4439-af31-5364731e8169)

Liste eleman değeri 2 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0d3c4521-1af3-4f74-adc4-451b75d7ac48)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload21db9fdb-3043-4a37-ba47-b63ae98c1978)

Alanın zorunlu olup, olmayacağı sıra no bilgisi, liste elemanları tanımlanarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7cbf1f11-0a29-43b6-8256-93931e45ac92)(kaydet) butonu tıklanarak liste tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3c367e55-1919-4ec6-9797-805512eecd78)

Tanımlanan Liste Tipli parametik alan Entegre Yönetim Sistemi\> Dış Müşteri Şikayetleri \> Dış Müşteri Şikayetleri İşlemleri menüsünde Yeni butonu tıklatıldığında açılan Şikayet Detayı ekranında Şikayet Detayı Diğer Alanlar sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd254b1a6-902e-427d-aede-1dc6e9033b74)

### **1.1.1.1.1.5.Personel Tipli Parametrik Alanların Listesi**

Dış Müşteri Şikayetleri Modülünde Entegre Yönetim Sistemi\> Dış Müşteri Şikayetleri \> Dış Müşteri Şikayetleri İşlemleri menüsünde Yeni butonu tıklatıldığında açılan Şikayet Detayı ekranında Şikayet Detayı Diğer Alanlar sekmesinde Personel tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Personel yazarak Personel tipli parametrik alanlar aratılır ve Personel tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Personel tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf51b1cba-9979-4f22-b901-da5eafa893d8)

### **1.1.1.1.1.6.Personel Tipli Parametrik Alan Tanımlama**

lblPPARAM1 Personel tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb3deccc7-e055-4662-8e68-9791b0e27c06) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8d22c722-59b7-4242-95ed-8b0c91144ab1)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload598190f2-d929-4a97-9216-195cbb414c91)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7cbf1f11-0a29-43b6-8256-93931e45ac92)(kaydet) butonu tıklanarak Personel tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6cdd3382-ba28-4115-9a18-71f7eb6b4872)

Tanımlanan Personel Tipli parametik alan Entegre Yönetim Sistemi\> Dış Müşteri Şikayetleri \> Dış Müşteri Şikayetleri İşlemleri menüsünde Yeni butonu tıklatıldığında açılan Şikayet Detayı ekranında Şikayet Detayı Diğer Alanlar sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9977b75c-9d34-4323-8cb8-ecf08971b1bc)

Personel tipli parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb9d36d6-a59a-497a-bf4f-f7ec328993d8)(seç) butonu tıklanıldığında sistemde tanımlı personel listesinde seçim yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload098da642-43f7-47be-8167-357d8eaf142a)

### **1.1.1.1.1.7.Sorgu Tipli Parametrik Alanların Listesi**

Dış Müşteri Şikayetleri Modülünde Entegre Yönetim Sistemi\> Dış Müşteri Şikayetleri \> Dış Müşteri Şikayetleri İşlemleri menüsünde Yeni butonu tıklatıldığında açılan Şikayet Detayı ekranında Şikayet Detayı Diğer Alanlar sekmesinde Sorgu tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Sorgu yazarak Sorgu tipli parametrik alanlar aratılır ve Sorgu tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Sorgu tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7e478885-f53d-4c4e-a390-ecf49eb11a0d)

### **1.1.1.1.1.8.Sorgu Tipli Parametrik Alan Tanımlama**

lblQPARAM1 Sorgu tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb3deccc7-e055-4662-8e68-9791b0e27c06) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload73b0a94b-0fd5-4400-a16e-fd35939a27e0)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3ba0307d-a81a-42e8-bbbb-74b924cd8a12) Bimser Destek ekibinde yardım alınarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7cbf1f11-0a29-43b6-8256-93931e45ac92)(kaydet) butonu tıklanarak Sorgu tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload313d6910-3a7a-4584-8b7f-0910d8c2f27f)

Tanımlanan Sorgu Tipli parametrik alan Entegre Yönetim Sistemi\> Dış Müşteri Şikayetleri \> Dış Müşteri Şikayetleri İşlemleri menüsünde Yeni butonu tıklatıldığında açılan Şikayet Detayı ekranında Şikayet Detayı Diğer Alanlar sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd44612c8-602f-4fdb-87b3-e366507f3784)

Sorgu tipli parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2408cc34-5c0d-4cf0-b665-98e2dc6cbbc9) (Ekle) butonu tıklanıldığında sistemde tanımlı Ürün listesinde tekli ve çoklu seçim yapılarak ekleme işlemi sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2ac7d06d-b46e-4159-965c-bb7ae84c4e0a)

### **1.1.1.1.1.9.Metin Tipli Parametrik Alanların Listesi**

Dış Müşteri Şikayetleri Modülünde Entegre Yönetim Sistemi\> Dış Müşteri Şikayetleri \> Dış Müşteri Şikayetleri İşlemleri menüsünde Yeni butonu tıklatıldığında açılan Şikayet Detayı ekranında Şikayet Detayı Diğer Alanlar sekmesinde Metin tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Metin yazarak Metin tipli parametrik alanlar aratılır ve Metin tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Metin tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9b038ce4-b05f-4750-8aa7-124158b6c530)

### **1.1.1.1.1.10.Metin Tipli Parametrik Alan Tanımlama**

lblPARAM5 Metin tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb3deccc7-e055-4662-8e68-9791b0e27c06) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1454bcae-0f80-46e8-b2d6-5e79c556c875)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada6790437-ace7-4674-8eaa-4179518e4122)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7cbf1f11-0a29-43b6-8256-93931e45ac92)(kaydet) butonu tıklanarak Metin tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload011ec0fa-b19d-4408-b6ee-53d6e75c2801)

Tanımlanan Metin Tipli parametrik alan Entegre Yönetim Sistemi\> Dış Müşteri Şikayetleri \> Dış Müşteri Şikayetleri İşlemleri menüsünde Yeni butonu tıklatıldığında açılan Şikayet Detayı ekranında Şikayet Detayı Diğer Alanlar sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload260c8b05-2e6f-4c65-963e-c88ded8eba10)

### **1.1.1.1.1.11.Metin (Çoklu Satır) Tipli Parametrik Alanların Listesi**

Dış Müşteri Şikayetleri Modülünde Entegre Yönetim Sistemi\> Dış Müşteri Şikayetleri \> Dış Müşteri Şikayetleri İşlemleri menüsünde Yeni butonu tıklatıldığında açılan Şikayet Detayı ekranında Şikayet Detayı Diğer Alanlar sekmesinde Metin (Çoklu Satır)  tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Metin (Çoklu Satır) yazarak Metin (Çoklu Satır) tipli parametrik alanlar aratılır ve Metin (Çoklu Satır)  tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Metin (Çoklu Satır)  tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5408a94d-433b-4647-95be-9959dea1f370)

### **1.1.1.1.1.12.Metin (Çoklu Satır) Tipli Parametrik Alan Tanımlama**

lblPARAM16 Metin (Çoklu Satır) tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb3deccc7-e055-4662-8e68-9791b0e27c06) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0f56fca4-0faf-467a-9691-9f48e999b224)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6bb3bf18-71e9-409d-980c-8063225ad148)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7cbf1f11-0a29-43b6-8256-93931e45ac92)(kaydet) butonu tıklanarak Metin (Çoklu Satır) tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4fbaf627-3ccc-4b01-aaaa-18d41ad8e735)

Tanımlanan Metin (Çoklu Satır) Tipli parametrik alan Entegre Yönetim Sistemi\> Dış Müşteri Şikayetleri \> Dış Müşteri Şikayetleri İşlemleri menüsünde Yeni butonu tıklatıldığında açılan Şikayet Detayı ekranında Şikayet Detayı Diğer Alanlar sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd9969b99-11be-4349-b08a-7032e3c45e1d)

### **1.1.1.1.1.13.Ölçü Birimi Parametrik Alanların Listesi**

Dış Müşteri Şikayetleri Modülünde Entegre Yönetim Sistemi\> Dış Müşteri Şikayetleri \> Dış Müşteri Şikayetleri İşlemleri menüsünde Yeni butonu tıklatıldığında açılan Şikayet Detayı ekranında Şikayet Detayı Diğer Alanlar sekmesinde Ölçü Birimi tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Ölçü Birimi yazarak Ölçü Birimi tipli parametrik alanlar aratılır ve Ölçü Birimi tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Ölçü Birimi tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8fc93775-c70a-464a-ba9a-01535eb44704)

### **1.1.1.1.1.14.Ölçü Birimi Parametrik Alan Tanımlama**

lblNPARAM6 Ölçü birimi tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb3deccc7-e055-4662-8e68-9791b0e27c06) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade0a1d029-7eda-4986-b186-19c730fe724e)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada258158c-3eef-453e-ba12-3d0ca1898351)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7cbf1f11-0a29-43b6-8256-93931e45ac92)(Kaydet) butonu tıklanarak ölçü birimi tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb802796-c8f8-4e14-8b55-23a18a7fbc8d)

Tanımlanan ölçü birimi tipli parametrik alan Entegre Yönetim Sistemi\> Dış Müşteri Şikayetleri \> Dış Müşteri Şikayetleri İşlemleri menüsünde Yeni butonu tıklatıldığında açılan Şikayet Detayı ekranında Şikayet Detayı Diğer Alanlar sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d3dbe6b-34b1-42a5-9f4d-5d11f22fe2b9)

### **1.1.1.1.1.15.Parasal Tipli Parametrik Alanların Listesi**

Dış Müşteri Şikayetleri Modülünde Entegre Yönetim Sistemi\> Dış Müşteri Şikayetleri \> Dış Müşteri Şikayetleri İşlemleri menüsünde Yeni butonu tıklatıldığında açılan Şikayet Detayı ekranında Şikayet Detayı Diğer Alanlar sekmesinde Parasal tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Parasal yazarak Parasal tipli parametrik alanlar aratılır ve Parasal tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Parasal tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4c5f9d57-b2d9-4e8f-89d6-a7b56e8d62fa)

### **1.1.1.1.1.16.Parasal Tipli Parametrik Alan Tanımlama**

lblNPARAM1 Parasal tipli alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb3deccc7-e055-4662-8e68-9791b0e27c06) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1c2be5e9-580f-4369-a19f-5c5d2600b296)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb758898f-f13c-4d67-b4c4-459c304c4bed)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7cbf1f11-0a29-43b6-8256-93931e45ac92)(Kaydet ) butonu tıklanarak Parasal tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload61f4e8f2-7579-419b-8cb0-390d3b20a294)

Tanımlanan Parasal Tipli parametrik alan Entegre Yönetim Sistemi\> Dış Müşteri Şikayetleri \> Dış Müşteri Şikayetleri İşlemleri menüsünde Yeni butonu tıklatıldığında açılan Şikayet Detayı ekranında Şikayet Detayı Diğer Alanlar sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4130a7f6-2deb-4524-9687-dbaa3e22243d)

### **1.1.1.1.1.17.Başlık Tipli Parametrik Alanların Listesi**

Dış Müşteri Şikayetleri Modülünde Entegre Yönetim Sistemi\> Dış Müşteri Şikayetleri \> Dış Müşteri Şikayetleri İşlemleri menüsünde Yeni butonu tıklatıldığında açılan Şikayet Detayı ekranında Şikayet Detayı Diğer Alanlar sekmesinde Başlık tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Başlık yazarak Başlık tipli parametrik alanlar aratılır ve Başlık tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Başlık tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload19b907d6-60e0-48b2-a96e-99b5f20a0cc0)

### **1.1.1.1.1.18.Başlık Tipli Parametrik Alan Tanımlama**

lblBaslikParam1 Başlık tipli alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb3deccc7-e055-4662-8e68-9791b0e27c06) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0298cb47-c1cd-4c74-af13-0950e378af03)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2573a07c-81d1-4e86-aa9f-f9425d60d4b7)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7cbf1f11-0a29-43b6-8256-93931e45ac92)(Kaydet ) butonu tıklanarak Başlık tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload39a934dd-0848-4017-b9fc-6746970371a1)

Tanımlanan Başlık Tipli parametrik alan Entegre Yönetim Sistemi\> Dış Müşteri Şikayetleri \> Dış Müşteri Şikayetleri İşlemleri menüsünde Yeni butonu tıklatıldığında açılan Şikayet Detayı ekranında Şikayet Detayı Diğer Alanlar sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0442aba7-5629-4ef9-b13e-7703b72948b1)

### **1.1.1.1.1.19.Ürün Tipli Parametrik Alanların Listesi**

Dış Müşteri Şikayetleri Modülünde Entegre Yönetim Sistemi\> Dış Müşteri Şikayetleri \> Dış Müşteri Şikayetleri İşlemleri menüsünde Yeni butonu tıklatıldığında açılan Şikayet Detayı ekranında Şikayet Detayı Diğer Alanlar sekmesinde Ürün tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Ürün yazarak Ürün tipli parametrik alanlar aratılır ve Ürün tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Ürün tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd7809d12-6783-4e22-bcec-59ff36e16869)

### **1.1.1.1.1.20. Ürün Tipli Parametrik Alan Tanımlama**

lblUPARAM1 Ürün tipli alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb3deccc7-e055-4662-8e68-9791b0e27c06) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload778032d8-448e-49fb-887b-853192419779)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload38723620-c6ac-4d27-a467-c44a60ba5ecd)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7cbf1f11-0a29-43b6-8256-93931e45ac92)(Kaydet ) butonu tıklanarak Ürün tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf4b67441-0822-4c92-bdff-b1bae5a83d40)

Tanımlanan Ürün Tipli parametrik alan Entegre Yönetim Sistemi\> Dış Müşteri Şikayetleri \> Dış Müşteri Şikayetleri İşlemleri menüsünde Yeni butonu tıklatıldığında açılan Şikayet Detayı ekranında Şikayet Detayı Diğer Alanlar sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7397860d-7b33-4ed9-a736-b9f38a3346b4)

Ürün tipli parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadffe2d0d6-dda0-4d41-86d1-1a75b512c602)(Ekle) butonu tıklanıldığında sistemde tanımlı Ürün listesinde Ürün ekleme işlemi yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload01fc2c1c-43cd-4c19-b8c4-f03beefaca79)

### **1.1.1.1.1.21.Müşteri Tipli Parametrik Alanların Listesi**

Dış Müşteri Şikayetleri Modülünde Entegre Yönetim Sistemi\> Dış Müşteri Şikayetleri \> Dış Müşteri Şikayetleri İşlemleri menüsünde Yeni butonu tıklatıldığında açılan Şikayet Detayı ekranında Şikayet Detayı Diğer Alanlar sekmesinde Müşteri tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Müşteri yazarak Müşteri tipli parametrik alanlar aratılır ve Müşteri tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Müşteri tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6a6d6168-f89b-4643-8624-0f98d9e6cc3c)

### **1.1.1.1.1.22.Müşteri Tipli Parametrik Alan Tanımlama**

lblMPARAM1 Müşteri tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb3deccc7-e055-4662-8e68-9791b0e27c06) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb85925c7-424e-47cd-9355-84f6b8109ae4)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload214370bb-f29d-4829-8d18-29e48fd18cb1)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7cbf1f11-0a29-43b6-8256-93931e45ac92)(kaydet) butonu tıklanarak Müşteri parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload74ce4195-08ac-449d-8b72-c3e96db9a703)

Tanımlanan Müşteri tipli parametrik alan Entegre Yönetim Sistemi\> Dış Müşteri Şikayetleri \> Dış Müşteri Şikayetleri İşlemleri menüsünde Yeni butonu tıklatıldığında açılan Şikayet detayı ekranında Şikayet Detayı Diğer Alanlar sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0b450974-cbde-45cf-a4b2-130fd07016c6)

Müşteri parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadffe2d0d6-dda0-4d41-86d1-1a75b512c602)(Ekle) butonu tıklanıldığında sistemde tanımlı Müşteri listesinde Müşteri ekleme işlemi yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6e722eee-e533-4df9-9cad-f491dd1f16ee)

Entegre Yönetim Sistemi\> Dış Müşteri Şikayetleri \> Dış Müşteri Şikayetleri İşlemleri menüsünde Yeni butonu tıklatıldığında açılan Şikayet Detayı ekranında Şikayet Detayı Diğer Alanlar sekmesinde tanımlanan parametrik tipli tüm alanlar;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc4d18e87-60e9-4850-80f2-9f9d31e54de6)

#### **1.1.1.1.2.Dış Müşteri Şikayetleri Modülünde Gelişme Raporu Sekmesinde Parametrik Alan Tipi Tanımlaması**

Dış Müşteri Şikayetleri Modülünde Şikayet Detayı ekranında Gelişme Raporu sekmesinde tanımlanan parametrik alanların kısa kodları lblG\_ başlığı ile tanımlı kısa kodlardır. lblG\_ başlığındaki kısa kodlar olan tüm parametrik tipli alanlar tanımlandığında Dış Müşteri Şikayetleri Modülünde Şikayet Detayı ekranında Gelişme Raporu sekmesi ekranında görüntülenir.

### **1.1.1.1.2.1.Liste Tipli Parametrik Alanların Listesi**

Dış Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Gelişme Raporu sekmesinde Liste tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Liste yazarak Liste tipli parametrik alanlar aratılır ve Liste tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Liste tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload041dfbb6-bded-421d-9307-b5e690cce1cb)

### **1.1.1.1.2.2.Liste Tipli Parametrik Alan Tanımlama.**

lblG_LParam2 Liste tipli parametrik seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb3deccc7-e055-4662-8e68-9791b0e27c06) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4f869bfe-cc9f-4213-99b5-05f9a2db4d67)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcd6d539e-38d3-4c35-a5f2-29cc4f81effe)Liste tipli alanın liste değerlerini girmek için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8fba83f5-4dbd-4b5e-b132-7bd5ea6319a1) (Yeni) butonuna tıklanır, liste değerleri yazılır ve kaydedilir. Liste eleman değeri 1 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8577c650-48af-42b6-a663-92b993935389)

Liste eleman değeri 2 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadea36c46e-f865-4f6f-9fdf-e66559a0c7ff)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8aa7d131-12bc-4718-a684-84e903d10515)

Alanın zorunlu olup, olmayacağı sıra no bilgisi ve liste elemanları tanımlanarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7cbf1f11-0a29-43b6-8256-93931e45ac92)(kaydet) butonu tıklanarak liste tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf2ffb283-9859-4c12-a73b-bee16dbba6f1)

Tanımlanan liste tipli parametrik alan Dış Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Gelişme Raporu sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload99f1c269-5057-45a5-8ea5-b7d3ab145649)

### **1.1.1.1.2.3.Personel Tipli Parametrik Alanların Listesi**

Dış Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Gelişme Raporu sekmesinde Personel tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Personel yazarak Personel tipli parametrik alanlar aratılır ve Personel tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Personel tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload797e5627-899a-4b28-be56-017453d8dea0)

### **1.1.1.1.2.4.Personel Tipli Parametrik Alan Tanımlama**

lblG_PParam1 Personel tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb3deccc7-e055-4662-8e68-9791b0e27c06) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3fb3890f-4e9b-4732-ad66-84ac6e36fed4)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2a56a338-a172-4473-9880-22913b5ca2bd)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7cbf1f11-0a29-43b6-8256-93931e45ac92)(kaydet) butonu tıklanarak Personel tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb3c33faf-5a26-46cf-9d2b-0f7625a1ff52)

Tanımlanan Personel tipli parametrik alan Dış Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Gelişme Raporu sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload506681a9-d2a8-486a-9e8e-a7d7fc04c892)

Personel tipli parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb9d36d6-a59a-497a-bf4f-f7ec328993d8)(seç) butonu tıklanıldığında sistemde tanımlı personel listesinde seçim yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada0c99382-f49b-4d87-b850-f68dd4ddeabb)

### **1.1.1.1.2.5.Sorgu Tipli Parametrik Alanların Listesi**

Dış Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Gelişme Raporu sekmesinde Sorgu tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Sorgu yazarak Sorgu tipli parametrik alanlar aratılır ve Sorgu tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Sorgu tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfdb51264-99b0-4908-9d50-ac74f1b59322)

### **1.1.1.1.2.6.Sorgu Tipli Parametrik Alan Tanımlama**

lblG_QParam1 Sorgu tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb3deccc7-e055-4662-8e68-9791b0e27c06) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade49b12f7-cc88-4acf-b098-d457539be6e2)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbc23629a-dce0-4200-925e-0c51774df4f7)

Bimser Destek ekibi tarafından yardım alınarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7cbf1f11-0a29-43b6-8256-93931e45ac92)(kaydet) butonu tıklanarak Sorgu tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2b31f472-d579-4eae-b5af-f716cc52feb1)

Tanımlanan Sorgu tipli parametrik alan Dış Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Gelişme Raporu sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb78cbbed-2d78-40d7-8917-0d03a3a46c02)

Sorgu tipli parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb9d36d6-a59a-497a-bf4f-f7ec328993d8)(seç) butonu tıklanıldığında sistemde tanımlı Pozisyon listesinde seçim yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2a5d686f-d45b-4614-8747-fbc6f9620a5b)

### **1.1.1.1.2.7.Metin Tipli Parametrik Alanların Listesi**

Dış Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Gelişme Raporu sekmesinde Metin tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Metin yazarak Metin tipli parametrik alanlar aratılır ve Metin tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Metin tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade073c639-a35b-447d-93b1-ac8ae4eefb83)

### **1.1.1.1.2.8.Metin Tipli Parametrik Alan Tanımlama**

lblG_Param2 Metin tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb3deccc7-e055-4662-8e68-9791b0e27c06) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload32d621c8-0414-48c9-8ba4-73c61694d16f)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload05ed1370-5b80-4e6e-8507-1843efcd064d)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7cbf1f11-0a29-43b6-8256-93931e45ac92)(kaydet) butonu tıklanarak Metin tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload81adf231-7826-40d0-b434-74060738f668)

Tanımlanan Metin tipli parametrik alan Dış Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Gelişme Raporu sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload346c09a3-e317-47e3-84a2-16e1c48f88b7)

### **1.1.1.1.2.9.Ölçü Birimi Parametrik Alanların Listesi**

Dış Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Gelişme Raporu sekmesinde Ölçü Birimi tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Ölçü Birimi yazarak Ölçü Birimi tipli parametrik alanlar aratılır ve Ölçü Birimi tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Ölçü Birimi tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload04d4bc94-624e-42f4-bb37-46dc78e39717)

### **1.1.1.1.2.10.Ölçü Birimi Parametrik Alan Tanımlama**

lblG_NParam3 Ölçü birimi tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb3deccc7-e055-4662-8e68-9791b0e27c06) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade5d8d7c2-d79f-408f-b25a-529c64c42698)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2badde23-e462-42cf-a678-2a4017b6c131)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7cbf1f11-0a29-43b6-8256-93931e45ac92)(Kaydet) butonu tıklanarak ölçü birimi tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf1b5ad0a-1f4e-4c47-9f0c-9fe437b4eb19)

Tanımlanan ölçü birimi tipli parametrik alan Dış Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Gelişme Raporu sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload185301b3-b07a-4dc7-9425-c8482c780e49)

### **1.1.1.1.2.11.Parasal Tipli Parametrik Alanların Listesi**

Dış Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Gelişme Raporu sekmesinde Parasal tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Parasal yazarak Parasal tipli parametrik alanlar aratılır ve Parasal tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Parasal tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload45571ad6-4fb2-4730-8609-b3996545abf9)

### **1.1.1.1.2.12.Parasal Tipli Parametrik Alan Tanımlama**

lblG_NParam1 Parasal tipli alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb3deccc7-e055-4662-8e68-9791b0e27c06) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7faf4aba-584f-4214-9029-7bf522328c85)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload58fdb4a8-14d3-445e-adb4-109d9ff70e77)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7cbf1f11-0a29-43b6-8256-93931e45ac92)(Kaydet ) butonu tıklanarak Parasal tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc2805d63-2abc-44ff-b84c-63abc071f5e7)

Tanımlanan Parasal tipli parametrik alan Dış Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Gelişme Raporu sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc18f7cdb-fdb7-4b8e-9812-f45acb86e415)

Dış Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Gelişme Raporu sekmesinde Tanımlanan Tüm Parametrik Tipli Alanlar;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1d8a7bbc-4ab3-49dc-a1d8-43d5a8b598b0)

#### **1.1.1.1.3. Dış  Müşteri Şikayetleri Modülünde Modülünde Kök Neden Analizi Sekmesinde Parametrik Alan Tipi Tanımlaması**

Dış Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Kök Neden Analizi sekmesinde tanımlanan parametrik alanların kısa kodları lblKOK başlığı ile tanımlı kısa kodlardır. lblKOK başlığındaki kısa kodlar olan tüm parametrik tipli alanlar tanımlandığında Dış Müşteri Şikayetleri Modülünde Şikayet Detayı ekranında Kök Neden Analizi sekmesinde görüntülenir.

### **1.1.1.1.3.1.Tarih Tipli Parametrik Alanların Listesi**

Dış Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Kök Neden Analizi sekmesinde tarih tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına tarih yazarak tarih tipli parametrik alanlar aratılır ve tarih tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen tarih tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3011bcc6-501b-40db-a979-02a85d330160)

### **1.1.1.1.3.2.Tarih Tipli Parametrik Alan Tanımlama**

lblKOKDPARAM1 Tarih tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb3deccc7-e055-4662-8e68-9791b0e27c06) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload73ad2d51-2b23-49dd-8568-96a97713620d)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload64d5669a-4868-40e0-9005-23da4e8691b6)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7cbf1f11-0a29-43b6-8256-93931e45ac92)(Kaydet) butonu tıklanarak tarih tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload392c65a9-976d-4c25-af2b-348557fcef69)

Tanımlanan tarih tipli parametrik alan Dış Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Kök Neden Analizi sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf5a3558d-db1c-4c96-831c-806cc35e424e)

### **1.1.1.1.3.3.Liste Tipli Parametrik Alanların Listesi**

Dış Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Kök Neden Analizi sekmesinde liste tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına liste yazarak liste tipli parametrik alanlar aratılır ve liste tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen liste tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload45ff4c7f-cd3c-457c-9540-c744a3ddaa98)

### **1.1.1.1.3.4.Liste Tipli Parametrik Alan Tanımlama**

lblKOKLPARAM1 Liste tipli parametrik seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb3deccc7-e055-4662-8e68-9791b0e27c06) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadef944047-072a-46ee-9882-ff3196e975df)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2b584ea3-f0b5-4089-a7ce-46c497e62e7a)

Liste tipli alanın liste değerlerini girmek için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8fba83f5-4dbd-4b5e-b132-7bd5ea6319a1) (Yeni) butonuna tıklanır, liste değerleri yazılır ve kaydedilir. Liste eleman değeri 1 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd712f299-8f59-4a57-a89a-a722dff5245f)

Liste eleman değeri 2 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload978819b5-13ae-4863-9522-3f7eab5f6ac7)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload16c37011-3b45-4e39-aa1c-ac260a9efc07)

Alanın zorunlu olup, olmayacağı sıra no bilgisi ve liste elemanları tanımlanarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7cbf1f11-0a29-43b6-8256-93931e45ac92)(kaydet) butonu tıklanarak liste tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload66ae1252-db76-45b8-a899-04f57cf5d5ac)

Tanımlanan liste tipli parametrik alan Dış Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Kök Neden Analizi sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6aba1872-c9ba-43b3-8682-3c0b38936fd7)

### **1.1.1.1.3.5.Metin Tipli Parametrik Alanların Listesi**

Dış Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Kök Neden Analizi sekmesinde metin tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına metin yazarak Metin tipli parametrik alanlar aratılır ve metin tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen metin tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada4e60dbe-fffd-4d56-8d96-24f8378c1917)

### **1.1.1.1.3.6.Metin Tipli Parametrik Alan Tanımlama**

lblKOKPARAM1 Metin tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb3deccc7-e055-4662-8e68-9791b0e27c06) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaded3c6261-4813-4f18-b929-f0e48ce58510)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1f914da9-937a-4c4a-abb6-dc98d7eecaeb)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7cbf1f11-0a29-43b6-8256-93931e45ac92)(kaydet) butonu tıklanarak Metin tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d78c740-e6db-4afb-9f33-d71cc93adefa)

Tanımlanan Metin tipli parametrik alan Dış Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Kök Neden Analizi sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf904c7cd-df65-4510-93ee-f41fd63a8f56)

### **1.1.1.1.3.7.Ölçü Birimi Parametrik Alanların Listesi**

Dış Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Kök Neden Analizi sekmesinde ölçü Birimi tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına ölçü Birimi yazarak ölçü Birimi tipli parametrik alanlar aratılır ve ölçü Birimi tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen ölçü Birimi tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada26de3ab-10da-44ab-b787-b4b69a108ecc)

### **1.1.1.1.3.8.Ölçü Birimi Parametrik Alan Tanımlama**

lblKOKNAPARAM1 Ölçü birimi tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb3deccc7-e055-4662-8e68-9791b0e27c06) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload828e1ced-f29e-45a7-8e63-0cb4bf83bcbb)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload81db4d92-a0af-423e-85a3-53682be57b8c)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7cbf1f11-0a29-43b6-8256-93931e45ac92)(Kaydet) butonu tıklanarak ölçü birimi tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload917d0d4c-78ca-41d8-b553-b9c80d9e0486)

Tanımlanan ölçü birimi tipli parametrik alan Dış Müşteri Şikayetleri Modülünde Şikayet Detayı ekranında Kök Neden Analizi sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload67056e87-7e81-4cd6-94e1-bb9b7c73400b)

### **1.1.1.1.3.9.Parasal Tipli Parametrik Alanların Listesi**

Dış Müşteri Şikayetleri Modülünde Şikayet Detayı ekranında Kök Neden Analizi sekmesinde parasal tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına parasal yazarak parasal tipli parametrik alanlar aratılır ve parasal tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen parasal tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2dedc630-4b7d-47aa-9492-14877e43c581)

### **1.1.1.1.3.10.Parasal Tipli Parametrik Alan Tanımlama**

lblKOKNCPARAM1 Parasal tipli alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb3deccc7-e055-4662-8e68-9791b0e27c06) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload57445e8c-4d46-4333-b715-8a96b7f157ee)Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4e5063db-4fa3-4022-b20b-73ac13182752)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7cbf1f11-0a29-43b6-8256-93931e45ac92)(Kaydet ) butonu tıklanarak parasal tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0f26ad09-1bec-4c1d-9ea6-8dbec6c0683b)

Tanımlanan parasal tipli parametrik alan Dış Müşteri Şikayetleri Modülünde Şikayet Detayı ekranında Kök Neden Analizi sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddd3e38cf-44a6-4367-8e76-0f73b0bd7220)

### **1.1.1.1.3.11.Sorgu Tipli Parametrik Alanların Listesi**

Dış Müşteri Şikayetleri Modülünde Şikayet Detayı ekranında Kök Neden Analizi sekmesinde Sorgu tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Sorgu yazarak Sorgu tipli parametrik alanlar aratılır ve Sorgu tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Sorgu tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc2968222-5987-4aeb-9c5e-e5dc7d189326)

### **1.1.1.1.3.12.Sorgu Tipli Parametrik Alan Tanımlama**

lblKOK_QParam1 Sorgu tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb3deccc7-e055-4662-8e68-9791b0e27c06) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload60b65dd3-87e0-4ac8-a55c-43d002ad2e54)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddf1fe556-bcda-43b9-9279-8d1f06aac518)

Bimser destek ekibinde yardım alınarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7cbf1f11-0a29-43b6-8256-93931e45ac92)(kaydet) butonu tıklanarak Sorgu tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload85c1c06c-1066-465f-91cb-54ff5cb19dd1)

Tanımlanan Sorgu Tipli parametrik alan Dış Müşteri Şikayetleri Modülünde Şikayet Detayı ekranında Kök Neden Analizi sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade4ae49aa-82fd-48a2-9ff4-e2193815303c)

Sorgu tipli parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb9d36d6-a59a-497a-bf4f-f7ec328993d8)(seç) butonu tıklanıldığında sistemde tanımlı Pozisyon listesinde seçim yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6dc23d30-17f9-4253-b916-f10a92f63496)

### **1.1.1.1.3.13.Personel Tipli Parametrik Alanların Listesi**

Dış Müşteri Şikayetleri Modülünde Şikayet Detayı ekranında Kök Neden Analizi sekmesinde Personel tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Personel yazarak Personel tipli parametrik alanlar aratılır ve Personel tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Personel tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload83c29109-a400-4b16-85c1-d5d5b68e944d)

### **1.1.1.1.3.14.Personel Tipli Parametrik Alan Tanımlama**

lblKOK_PParam1 Personel tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb3deccc7-e055-4662-8e68-9791b0e27c06) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6c2b7375-37f7-427f-b6dc-341ce560a72f)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload938b494a-7b6a-4bbe-b8c2-44125399b78f)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7cbf1f11-0a29-43b6-8256-93931e45ac92)(kaydet) butonu tıklanarak Personel tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf17adfb1-e596-4a2a-8d11-7b621fd4f73e)

Tanımlanan Personel Tipli parametik alan Dış Müşteri Şikayetleri Modülünde Şikayet Detayı ekranında Kök Neden Analizi sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3cd6572e-a364-4307-8d00-0c6dbb7737c7)

Personel tipli parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb9d36d6-a59a-497a-bf4f-f7ec328993d8)(seç) butonu tıklanıldığında sistemde tanımlı personel listesinde seçim yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload148189d4-234a-4f79-b51d-c2c0decfc3c7)

Dış Müşteri Şikayetleri Modülünde Şikayet Detayı ekranında Kök Neden Analizi sekmesinde Tanımlanan Tüm Alanlar;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7e14fa61-3f05-4855-a0db-bab1ce119d51)

#### **1.1.1.1.4.Dış Müşteri Şikayetleri Modülünde Aksiyonlar Sekmesinde Parametrik Alan Tipi Tanımlaması**

Dış Müşteri Şikayetleri Modülünde Şikayet Detayı ekranında Aksiyonlar sekmesinde tanımlanan parametrik tipli alanların kısa kodları lblA\_ başlığı ile tanımlı kısa kodlardır. lblA \_ başlığındaki kısa kodlar olan tüm parametrik tipli alanlar tanımlandığında Dış Müşteri Şikayetleri Modülünde Şikayet Detayı ekranında Aksiyonlar sekmesinde görüntülenir.

### **1.1.1.1.4.1.Tarih Tipli Parametrik Alanların Listesi**

Dış Müşteri Şikayetleri Modülünde Şikayet Detayı ekranında Aksiyonlar sekmesinde tarih tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına tarih yazarak tarih tipli parametrik alanlar aratılır ve tarih tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen tarih tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload314c230a-186a-45a4-99e7-314f539ff6fe)

### **1.1.1.1.4.2.Tarih Tipli Parametrik Alan Tanımlama**

lblA_DParam1 Tarih tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb3deccc7-e055-4662-8e68-9791b0e27c06) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload350cf71e-1836-48c5-aaed-a3442d71cf6c)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload76d66c22-6ed0-49ac-9c0d-e1ac4d1ec6c5)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7cbf1f11-0a29-43b6-8256-93931e45ac92)(Kaydet) butonu tıklanarak tarih tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3ec967cd-7c0c-46a0-841c-69f3c0d490b8)

Tanımlanan tarih tipli parametrik alan Dış Müşteri Şikayetleri Modülünde Şikayet Detayı ekranında Aksiyonlar sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc141f460-29c6-4e7f-b063-adbe922677bf)

### **1.1.1.1.4.3.Liste Tipli Parametrik Alanların Listesi**

Dış Müşteri Şikayetleri Modülünde Şikayet Detayı ekranında Aksiyonlar sekmesinde liste tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına liste yazarak liste tipli parametrik alanlar aratılır ve liste tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen liste tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5caf09ea-7e25-4600-bde3-f66d76a68bbf)

### **1.1.1.1.4.4.Liste Tipli Parametrik Alan Tanımlama**

lblA_LParam1 Liste tipli parametrik seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb3deccc7-e055-4662-8e68-9791b0e27c06) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload60dca140-2c09-4d62-b44f-89d88306b1e8)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3393316c-f193-4ff9-8ec2-f20b940b9cde)

Liste tipli alanın liste değerlerini girmek için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8fba83f5-4dbd-4b5e-b132-7bd5ea6319a1) (Yeni) butonuna tıklanır, liste değerleri yazılır ve kaydedilir. Liste elaman değeri 1 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload95dd3c68-c5c7-4baf-9785-473988c626e6)

Liste eleman değeri 2 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2e95efd4-c163-43ea-8fc5-9b4c8d3a701c)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload52dff876-46b6-44ea-94cd-be41519047cd)

Alanın zorunlu olup, olmayacağı sıra no bilgisi ve liste elemanları tanımlanarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7cbf1f11-0a29-43b6-8256-93931e45ac92)(kaydet) butonu tıklanarak liste tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1638603a-c89c-4231-ad4b-f8db87224feb)

Tanımlanan liste tipli parametrik alan Dış Müşteri Şikayetleri Modülünde Şikayet Detayı ekranında Aksiyonlar sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadccc9289e-6824-41df-a594-0f8ee19041c2)

### **1.1.1.1.4.5.Sorgu Tipli Parametrik Alanların Listesi**

Dış Müşteri Şikayetleri Modülünde Şikayet Detayı ekranında Aksiyonlar sekmesinde sorgu tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına sorgu yazarak sorgu tipli parametrik alanlar aratılır ve sorgu tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen sorgu tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3c9bd5d7-eaf7-4ed0-8102-e2b66b92daf7)

### **1.1.1.1.4.6.Sorgu Tipli Parametrik Alan Tanımlama**

lblA_QPARAM1 Sorgu tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb3deccc7-e055-4662-8e68-9791b0e27c06) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload678df587-00e2-4608-a475-f344aad356b9)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb93515e5-83c6-412b-b584-37d7c1d91f93)

Bimser Destek ekibi tarafından yardım alınarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7cbf1f11-0a29-43b6-8256-93931e45ac92)(kaydet) butonu tıklanarak Sorgu tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload642a25fe-50c1-4b3a-8897-ca5f784b4f5c)

Tanımlanan sorgu tipli parametrik alan Dış Müşteri Şikayetleri Modülünde Şikayet Detayı ekranında Aksiyonlar sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc4b8eeed-9663-45ac-bdda-8e4d4addf153)

Sorgu tipli parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb9d36d6-a59a-497a-bf4f-f7ec328993d8)(seç) butonu tıklanıldığında sistemde tanımlı Pozisyon listesinde seçim yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload79c51a86-37cc-48df-b33a-4cdd7226af9b)

### **1.1.1.1.4.7.Metin Tipli Parametrik Alanların Listesi**

Dış Müşteri Şikayetleri Modülünde Şikayet Detayı ekranında Aksiyonlar sekmesinde metin tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına metin yazarak metin tipli parametrik alanlar aratılır ve metin tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen metin tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadeb755ca1-0f5c-4c1f-af49-a2ce7a2754b7)

### **1.1.1.1.4.8.Metin Tipli Parametrik Alan Tanımlama**

lblA_Param1 Metin tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb3deccc7-e055-4662-8e68-9791b0e27c06) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0defbd8f-1d7b-4ba3-94fa-6bd19b7c18b3)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc21e8c3f-100d-4b29-8884-ab8350d555da)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7cbf1f11-0a29-43b6-8256-93931e45ac92)(kaydet) butonu tıklanarak Metin tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8f0b8c18-45fa-48dd-8561-a2bc2350b838)

Tanımlanan metin tipli parametrik alan Dış Müşteri Şikayetleri Modülünde Şikayet Detayı ekranında Aksiyonlar sekmesinde görüntülenir

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadeadf4405-05b2-4f8b-8d61-695d09cd2e75)

### **1.1.1.1.4.9.Ölçü Birimi Parametrik Alanların Listesi**

Dış Müşteri Şikayetleri Modülünde Şikayet Detayı ekranında Aksiyonlar sekmesinde ölçü Birimi tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına ölçü Birimi yazarak ölçü Birimi tipli parametrik alanlar aratılır ve ölçü Birimi tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen ölçü Birimi tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade66a50f0-3992-4447-8a19-c224dc934cf3)

### **1.1.1.1.4.10.Ölçü Birimi Parametrik Alan Tanımlama**

lblA_NParam3 Ölçü birimi tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb3deccc7-e055-4662-8e68-9791b0e27c06) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbec69617-27c1-4b82-a71a-abaa25dc984c)Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5bcf6a5e-b4c4-48b3-ade0-900191318f05)Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7cbf1f11-0a29-43b6-8256-93931e45ac92)(Kaydet) butonu tıklanarak ölçü birimi tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8b8e7ad6-60b3-492a-a9ad-873fed2082a5)

Tanımlanan ölçü birimi tipli parametrik alan Dış Müşteri Şikayetleri Modülünde Şikayet Detayı ekranında Aksiyonlar sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload552639cf-415e-4ca8-9d8e-68fc0ab9b347)

### **1.1.1.1.4.11.Parasal Tipli Parametrik Alanların Listesi**

Dış Müşteri Şikayetleri Modülünde Şikayet Detayı ekranında Aksiyonlar sekmesinde parasal tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına parasal yazarak parasal tipli parametrik alanlar aratılır ve parasal tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen parasal tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload854fe4dc-4e96-4174-8c23-1cbec789c48a)

### **1.1.1.1.4.12.Parasal Tipli Parametrik Alan Tanımlama**

lblA_NParam1 Parasal tipli alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb3deccc7-e055-4662-8e68-9791b0e27c06) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddeee9743-772d-421c-9e31-ded17e31bfb3)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0a49b99b-cab1-43df-a25a-6aa77b2f592b)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7cbf1f11-0a29-43b6-8256-93931e45ac92)(Kaydet ) butonu tıklanarak parasal tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload26e18bd9-b6df-4151-ae69-f2a07ceda53f)

Tanımlanan parasal tipli parametrik alan Dış Müşteri Şikayetleri Modülünde Şikayet Detayı ekranında Aksiyonlar sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadabc213e1-1b59-4151-ae12-d25395728853)

### **1.1.1.1.4.13.Personel Tipli Parametrik Alanların Listesi**

Dış Müşteri Şikayetleri Modülünde Şikayet Detayı ekranında Aksiyonlar sekmesinde Personel tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Personel yazarak Personel tipli parametrik alanlar aratılır ve Personel tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Personel tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf8f58682-a22b-4f70-b6b4-8b9e8640cecb)

### **1.1.1.1.4.14.Personel Tipli Parametrik Alan Tanımlama**

lblA_PParam1 Personel tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb3deccc7-e055-4662-8e68-9791b0e27c06) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada1d3681d-83e4-4ac5-a34a-671216da5a9f)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3adafdc3-f9b9-4503-a25c-c1bf0acbab95)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7cbf1f11-0a29-43b6-8256-93931e45ac92)(kaydet) butonu tıklanarak Personel tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfc50ee32-d49f-48d8-9329-06221c6308ce)

Tanımlanan Personel Tipli parametik alan Dış Müşteri Şikayetleri Modülünde Şikayet Detayı ekranında Aksiyonlar sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7117f6f0-0cce-46e8-9bab-0be0b5947afb)

Personel tipli parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb9d36d6-a59a-497a-bf4f-f7ec328993d8)(seç) butonu tıklanıldığında sistemde tanımlı personel listesinde seçim yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada06028ab-86a2-437c-87ef-ee27a52dcfed)

Dış Müşteri Şikayetleri Modülünde Şikayet Detayı ekranında Aksiyonlar sekmesinde tanımlanan tüm parametrik alanlar;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d61e50b-221b-427e-982a-3e678757be7f)

#### **1.1.1.1.5.Dış Müşteri Şikayetleri Modülünde Sonuç Raporu Sekmesinde Parametrik Alan Tipi Tanımlaması**

Dış Müşteri Şikayetleri Modülünde Şikayet Detayı ekranında Sonuç Raporu sekmesinde tanımlanan parametrik alanların kısa kodları lblS\_ başlığı ile tanımlı kısa kodlardır. lblS\_ başlığındaki kısa kodlar olan tüm parametrik tipli alanlar tanımlandığında Dış Müşteri Şikayetleri Modülünde Şikayet Detayı ekranında Sonuç Raporu sekmesinde ekranında görüntülenir.

### **1.1.1.1.5.1.Liste Tipli Parametrik Alanların Listesi**

Dış Müşteri Şikayetleri Modülünde Şikayet Detayı ekranında Sonuç Raporu sekmesinde liste tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına liste yazarak liste tipli parametrik alanlar aratılır ve liste tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen liste tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade4b4719d-50eb-498f-af98-0e5b1b9cc7d5)

### **1.1.1.1.5.2.Liste Tipli Parametrik Alan Tanımlama**

lblS_LParam2 Liste tipli parametrik seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb3deccc7-e055-4662-8e68-9791b0e27c06) (değiştir) butonuna tıklanır

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadac1a3d95-092f-4bc3-8c92-4b9ca8280e19)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload92983be1-71da-4dc8-b794-5a21efaf82b3)Liste tipli alanın liste değerlerini girmek için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8fba83f5-4dbd-4b5e-b132-7bd5ea6319a1) (Yeni) butonuna tıklanır, liste değerleri yazılır ve kaydedilir. Liste eleman değeri 1 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada48eb768-8a1a-41fa-9c2a-0bc8fa6e7d6a)

Liste eleman değeri 2 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6d2c2be5-6fe8-40d7-a0c5-7898f29a565f)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9c9abc52-44db-4836-a48e-824b28b0ecd1)

Alanın zorunlu olup, olmayacağı sıra no bilgisi ve liste elemanları tanımlanarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7cbf1f11-0a29-43b6-8256-93931e45ac92)(kaydet) butonu tıklanarak liste tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd2ff31df-662b-4c00-a050-7a83c5089da1)

Tanımlanan liste tipli parametrik alan Dış Müşteri Şikayetleri Modülünde Şikayet Detayı ekranında Sonuç Raporu sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload681c5e11-b1cd-4a38-b76e-1a34f3ab0e8d)

### **1.1.1.1.5.3.Personel Tipli Parametrik Alanların Listesi**

Dış Müşteri Şikayetleri Modülünde Şikayet Detayı ekranında Sonuç Raporu sekmesinde personel tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına personel yazarak personel tipli parametrik alanlar aratılır ve personel tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen personel tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload836f4030-f730-4abc-8f0f-b90668f6d450)

### **1.1.1.1.5.4.Personel Tipli Parametrik Alan Tanımlama.**

lblS_PParam1 Personel tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb3deccc7-e055-4662-8e68-9791b0e27c06) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7b6b0fb2-4248-4178-8232-f6781b95f797)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1c8ae019-cb20-455a-93f6-a3f9c847cf21)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7cbf1f11-0a29-43b6-8256-93931e45ac92)(kaydet) butonu tıklanarak personel tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb0e8170e-6de5-49c3-945d-cc52901afe2f)

Tanımlanan personel tipli parametrik alan Dış Müşteri Şikayetleri Modülünde Şikayet Detayı ekranında Sonuç Raporu sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadae566568-9d78-43b7-93b6-eb117d22d17b)

Personel tipli parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb9d36d6-a59a-497a-bf4f-f7ec328993d8)(seç) butonu tıklanıldığında sistemde tanımlı personel listesinde seçim yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4e72322d-5439-432b-9a3e-b14ef895cc9f)

### **1.1.1.1.5.5.Sorgu Tipli Parametrik Alanların Listesi**

Dış Müşteri Şikayetleri Modülünde Şikayet Detayı ekranında Sonuç Raporu sekmesinde sorgu tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına sorgu yazarak sorgu tipli parametrik alanlar aratılır sorgu tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen sorgu tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4d242d1d-bfe6-42af-a0a0-a3346a7e850f)

### **1.1.1.1.5.6.Sorgu Tipli Parametrik Alan Tanımlama**

lblS_QParam1 Sorgu tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb3deccc7-e055-4662-8e68-9791b0e27c06) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload394b2a22-2368-42a8-88b9-e4a327e32553)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload132f898f-33ba-412c-9128-8c173bd213c7)

Bimser Destek ekibi tarafından yardım alınarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7cbf1f11-0a29-43b6-8256-93931e45ac92)(kaydet) butonu tıklanarak Sorgu tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0a8acf98-d93c-4187-85a7-c71fcce36267)

Tanımlanan sorgu tipli parametrik alan Dış Müşteri Şikayetleri Modülünde Şikayet Detayı ekranında Sonuç Raporu sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload48827b82-79a6-4bc3-b53d-781971bf96b1)

Sorgu tipli parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0dc5a330-435e-472a-9895-4dcba0f5eb07) (ekle) butonu tıklanıldığında sistemde tanımlı Departman listesinde tekli ve çoklu seçim yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1ccbd798-f40c-425a-8ac5-fe371e8aa3d4)

### **1.1.1.1.5.7.Metin Tipli Parametrik Alanların Listesi**

Dış Müşteri Şikayetleri Modülünde Şikayet Detayı ekranında Sonuç Raporu sekmesinde metin tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına metin yazarak metin tipli parametrik alanlar aratılır metin tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen metin tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload12c95a9a-53e7-46ce-984e-4fad312422e5)

### **1.1.1.1.5.8.Metin Tipli Parametrik Alan Tanımlama**

lblS_Param2 Metin tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb3deccc7-e055-4662-8e68-9791b0e27c06) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9a50fd67-fc74-4023-bb5f-449ff39507ff)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0a80149c-ba96-447d-a5d0-b1e553c75fbc)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7cbf1f11-0a29-43b6-8256-93931e45ac92)(kaydet) butonu tıklanarak metin tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8c16e0b3-80e9-409d-ac95-545117ca0a2c)

Tanımlanan metin tipli parametrik alan Dış Müşteri Şikayetleri Modülünde Şikayet Detayı ekranında Sonuç Raporu sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8c535c63-a1f2-4c19-a5f1-c8817a133d6e)

### **1.1.1.1.5.9.Ölçü Birimi Parametrik Alanların Listesi**

Dış Müşteri Şikayetleri Modülünde Şikayet Detayı ekranında Sonuç Raporu sekmesinde ölçü Birimi tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına ölçü Birimi yazarak ölçü Birimi tipli parametrik alanlar aratılır ölçü Birimi tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen ölçü Birimi tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb3eb9a20-eb92-443d-926f-74435c42ee32)

### **1.1.1.1.5.10.Ölçü Birimi Parametrik Alan Tanımlama**

lblS_NParam3 Ölçü birimi tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb3deccc7-e055-4662-8e68-9791b0e27c06) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6ee24436-d69e-4bbb-ba73-5642532ac663)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbd582bdd-5591-42c1-9d70-0342e9da6b68)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7cbf1f11-0a29-43b6-8256-93931e45ac92)(Kaydet) butonu tıklanarak ölçü birimi tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload034ddc78-e6d0-4824-9441-6167e07de774)

Tanımlanan ölçü birimi tipli parametrik alan Dış Müşteri Şikayetleri Modülünde Şikayet Detayı ekranında Sonuç Raporu sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf47c9961-56b5-4c64-af07-5329b8ae968b)

### **1.1.1.1.5.11.Parasal Tipli Parametrik Alanların Listesi**

Dış Müşteri Şikayetleri Modülünde Şikayet Detayı ekranında Sonuç Raporu sekmesinde parasal tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına parasal yazarak parasal tipli parametrik alanlar aratılır parasal tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen parasal tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7256cb39-464d-4b0a-9f74-13d3652999d3)

### **1.1.1.1.5.12.Parasal Tipli Parametrik Alan Tanımlama**

lblS_NParam1 Parasal tipli alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb3deccc7-e055-4662-8e68-9791b0e27c06) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4e7220d4-7815-40d3-82eb-e9a4931d228c)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc48f2e16-2e3c-4123-a50a-7d5b121e4446)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7cbf1f11-0a29-43b6-8256-93931e45ac92)(Kaydet ) butonu tıklanarak Parasal tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload409a5c49-70e5-42d4-bf78-2e5c20d6fe02)

Tanımlanan parasal tipli parametrik alan Dış Müşteri Şikayetleri Modülünde Şikayet Detayı ekranında Sonuç Raporu sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6123d0ff-60d0-46f2-ab62-b9497a055fb2)

Dış Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Sonuç Raporu sekmesinde tanımlanan tüm parametrik alanlar;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload60bab44a-1b0b-451c-a7d2-a196f1be60fc)

#### **1.1.1.1.6.Dış Müşteri Şikayetleri Modülünde Kapatma sekmesinde Parametrik Alan Tipi Tanımlaması**

Dış Müşteri Şikayetleri Modülünde Şikayet Detayı ekranında Kapatma sekmesinde tanımlanan parametrik alanların kısa kodları lblK\_ başlığı ile tanımlı kısa kodlardır. lblK\_ başlığındaki kısa kodlar olan tüm parametrik tipli alanlar tanımlandığında Dış Müşteri Şikayetleri Modülünde Şikayet Detayı ekranında Kapatma sekmesinde görüntülenir.

### **1.1.1.1.6.1.Liste Tipli Parametrik Alanların Listesi**

Dış Müşteri Şikayetleri Modülünde Şikayet Detayı ekranında Kapatma sekmesinde liste tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına liste yazarak liste tipli parametrik alanlar aratılır liste tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen liste tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload34bd84ee-8f68-486c-ab03-19e7ebbcded5)

### **1.1.1.1.6.2.Liste Tipli Parametrik Alan Tanımlama.**

lblK_LParam2 Liste tipli parametrik seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb3deccc7-e055-4662-8e68-9791b0e27c06) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload925d361f-35c1-496a-be16-fd0eff3b9166)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload658a88d4-bcd9-4766-97c8-2b5af5291f59)Liste tipli alanın liste değerlerini girmek için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8fba83f5-4dbd-4b5e-b132-7bd5ea6319a1) (Yeni) butonuna tıklanır, liste değerleri yazılır ve kaydedilir. Liste elaman değeri 1 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadeb749b31-231f-4097-ac9d-7c571e53a46b)

Liste eleman değeri 2 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade03a2919-15ff-4df0-9845-93c1c6dee661)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload874657db-1a1d-4b3f-8de2-0e165a15b1f9)

Alanın zorunlu olup, olmayacağı sıra no bilgisi ve liste elemanları tanımlanarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7cbf1f11-0a29-43b6-8256-93931e45ac92)(kaydet) butonu tıklanarak liste tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc27de758-77f1-41f4-836c-52142acc0aed)

Tanımlanan liste tipli parametrik alan Dış Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Kapatma sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload198240da-e554-45f2-b557-022fbfd83528)

### **1.1.1.1.6.3.Personel Tipli Parametrik Alanların Listesi**

Dış Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Kapatma sekmesinde personel tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına personel yazarak personel tipli parametrik alanlar aratılır personel tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen personel tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf0c00698-e697-4667-8262-58e4dfe634e9)

### **1.1.1.1.6.4.Personel Tipli Parametrik Alan Tanımlama**

lblK_PParam1 Personel tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb3deccc7-e055-4662-8e68-9791b0e27c06) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3dd3200b-be11-4295-9119-1fc938abca49)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload458c040f-5f5c-4708-99f6-2e3f97bfb4c3)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7cbf1f11-0a29-43b6-8256-93931e45ac92)(kaydet) butonu tıklanarak personel tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb8157e5e-6086-42be-a42d-3cc7062d797f)

Tanımlanan personel tipli parametrik alan Dış Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Kapatma sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddbbaa6c8-932e-46f8-9640-efa169b28e5c)

Personel tipli parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb9d36d6-a59a-497a-bf4f-f7ec328993d8)(seç) butonu tıklanıldığında sistemde tanımlı personel listesinde seçim yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload11426aaf-6aa5-433c-9a9e-dcc6d887da85)

### **1.1.1.1.6.5.Sorgu Tipli Parametrik Alanların Listesi**

Dış Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Kapatma sekmesinde sorgu tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına sorgu yazarak sorgu tipli parametrik alanlar aratılır sorgu tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen sorgu tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload28d0b988-68a8-4cbe-8b0a-b8de488fc970)

### **1.1.1.1.6.6.Sorgu Tipli Parametrik Alan Tanımlama**

lblK_QParam1 Sorgu tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb3deccc7-e055-4662-8e68-9791b0e27c06) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload77641fa1-e260-4467-91da-ebf270b78eaa)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb6641f49-4be3-4380-a2ab-5bc51a323e30)

Bimser Destek ekibi tarafından destek alınarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7cbf1f11-0a29-43b6-8256-93931e45ac92)(kaydet) butonu tıklanarak Sorgu tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload26b9e5f4-7ba3-4c00-9271-f0b3f12b2d86)

Tanımlanan sorgu tipli parametrik alan Dış Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Kapatma sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload95f382e1-b4a9-48a5-b813-760a11f3a233)

Sorgu tipli parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload115965c4-300d-4832-a20e-d7f3bf7b6498) (Ekle) butonu tıklanıldığında sistemde tanımlı Pozisyon listesinde tekli ve çoklu seçim yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload01f49def-f574-4d0a-aa47-013010283253)

### **1.1.1.1.6.7.Metin Tipli Parametrik Alanların Listesi**

Dış Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Kapatma sekmesinde metin tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına metin yazarak metin tipli parametrik alanlar aratılır metin tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen metin tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9794f4c9-cb67-4898-94f6-af397dd29741)

### **1.1.1.1.6.8.Metin Tipli Parametrik Alan Tanımlama**

lblK_Param2 Metin tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb3deccc7-e055-4662-8e68-9791b0e27c06) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade555687a-632b-4ca1-a6b7-0bf8cebec19c)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1dd56e04-fa24-474b-a875-b415d2d640a8)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7cbf1f11-0a29-43b6-8256-93931e45ac92)(kaydet) butonu tıklanarak metin tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadad7cdb38-0f5d-400b-8b55-10f361809a0c)

Tanımlanan metin tipli parametrik alan Dış Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Kapatma sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload440351d9-3f23-492b-b397-5f1e6d082d24)

### **1.1.1.1.6.9.Ölçü Birimi Parametrik Alanların Listesi**

Dış Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Kapatma sekmesinde ölçü Birimi tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına ölçü Birimi yazarak ölçü Birimi tipli parametrik alanlar aratılır ölçü Birimi tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen ölçü Birimi tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadec81c765-ffa8-43cf-9569-cf522196f772)

### **1.1.1.1.6.10.Ölçü Birimi Parametrik Alan Tanımlama**

lblK_NParam3 Ölçü birimi tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb3deccc7-e055-4662-8e68-9791b0e27c06) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb36f3626-23ed-4e45-8bfa-32da9fa3ff79)Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc9b59e12-3ab5-45bb-91fc-83e70acb2789)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7cbf1f11-0a29-43b6-8256-93931e45ac92)(Kaydet) butonu tıklanarak ölçü birimi tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload836d98e1-ddde-4de4-a2ea-ad68520f2b2c)

Tanımlanan ölçü birimi tipli parametrik alan Dış Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Kapatma sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload666e19c0-7a2c-4f6f-952c-ece7b574519c)

### **1.1.1.1.6.11.Parasal Tipli Parametrik Alanların Listesi**

Dış Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Kapatma sekmesinde parasal tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına parasal yazarak parasal tipli parametrik alanlar aratılır parasal tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen parasal tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf0d4f018-a4e8-482f-9720-ded007b37b61)

### **1.1.1.1.6.12.Parasal Tipli Parametrik Alan Tanımlama**

lblK_NParam2 Parasal tipli alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb3deccc7-e055-4662-8e68-9791b0e27c06) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada9c74cd4-2c69-4500-b367-2f863b1fc57d)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadee9b71b3-be23-4f25-91df-289c174a19f8)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7cbf1f11-0a29-43b6-8256-93931e45ac92)(Kaydet ) butonu tıklanarak parasal tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload36cac10a-196e-4cfb-9762-bda2b6671320)

Tanımlanan parasal tipli parametrik alan Dış Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Kapatma sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadeaa60cfc-9453-422d-b55a-1560ca02a428)

### **1.1.1.1.6.13.Tarih Tipli Parametrik Alanların Listesi**

Dış Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Kapatma sekmesinde tarih tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına tarih yazarak tarih tipli parametrik alanlar aratılır ve tarih tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen tarih tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload493f8133-5c99-4c6b-99c9-e7bacdeecc0d)

### **1.1.1.1.6.14.Tarih Tipli Parametrik Alan Tanımlama**

lblK_DParam1Tarih tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb3deccc7-e055-4662-8e68-9791b0e27c06) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd5db578a-1d76-4df1-a90e-cd9990c72285)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc3978407-d11d-4b8e-99a0-a6f1cee68365)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7cbf1f11-0a29-43b6-8256-93931e45ac92)(Kaydet) butonu tıklanarak tarih tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc472b661-6abf-421d-976a-db72f792222b)

Tanımlanan tarih tipli parametrik alan Dış Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Kapatma sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc4fcfbbe-3d72-4e4e-b12d-2e6ebdf023df)

Dış Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Kapatma sekmesinde tanımlanan tüm parametrik alanlar;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload218dce30-1d2a-4d22-95cd-4d307f8a77d2)

#### **1.1.1.1.7.Dil ayarlarında Tanımlan Parametrik Alan tipleri Görüntülen Ekrandan Kaldırma İşlemi**

1.Aşamada parametrik alanın bulunduğu ekran açılır. Dış Müşteri Şikayetleri Modülünde Şikayet Kaydı ekranında Kapatma sekmesinde görüntülenir

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2872fea3-6ca7-4342-b797-a5ee4c78970c)

2\. Aşamada Parametrik Alanın bulunduğu ekran görüntülendikten sonra örnekteki herhangi alan seçilerek, Sağ tıkla/Kopyala komutu ile parametrik alanın ismi kopyalanır. Örnek: İstenilen Tarih

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7e9413d6-8f9e-47b4-b34f-c6dac755c7fc)

3\. Aşamada Sistem Altyapı Tanımları\>BSAT\>Konfigürasyon Ayarları\>Dil ayarları menüsü tıklanarak açılan ekranda Modül olarak Dış Müşteri Şikayetleri Modülü seçilir. Kopyalanan Dil ayarlarından tanımlanan liste tipli parametrik alanı grid ekranında **TR** alanına sağ tıkla/yapıştır komutu ile alanın yapıştırma işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6b43507b-a001-4eee-94af-9eb4eda1a5b4)

4.Aşamada Tarih tipli parametrik alan seçilerek alanın içeriği görüntülemek için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb3deccc7-e055-4662-8e68-9791b0e27c06) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload52a361ec-2a1b-4ccb-ac91-85222ef4d0bb)

5.Aşamada içeriği görüntülen Tarih tipli alanın değeri silerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7cbf1f11-0a29-43b6-8256-93931e45ac92)(Kaydet) butonu tıklanarak Dil Ayarları menüsünde tanımlı Tarih tipli alanın kaldırma işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4afb8fc1-eb7d-4622-a1d2-2b5da8144cbc)

Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarlarında tanımlanan diğer parametrik alan tiplerin dil ayarları menüsünde kaldırma işlemi aynı şekilde olmaktadır. Dış Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Kapatma sekmesinde tanımlı Tarih Tipli alanın kaldırılmış olduğu görülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload275de0a5-5571-4d73-829a-4a09384034a3)
