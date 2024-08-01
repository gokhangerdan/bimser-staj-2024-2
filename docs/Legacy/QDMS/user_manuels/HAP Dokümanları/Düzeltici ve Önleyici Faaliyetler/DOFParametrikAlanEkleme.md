---
title: Parametrik Alan Tanımlama İşlemi
description: Parametrik Alan Tanımlama İşlemi Yardım Dokümanı
sidebar_position: 1
---

:::tip Bilgi

İlgili konu başlığına sağ tarafta bulunan navigasyon yardımıyla hızlı bir şekilde ulaşabilirsiniz.

:::


**Düzeltici ve Önleyici Faaliyetler** **Modülünde Dil Ayarları Menüsünde Parametrik Alan Tanımlama Kullanıcı Yardım Dokümanı**


# **1.Sistem Altyapı Tanımları**

Personel bilgilerinin tanımlandığı ve diğer modüller için gerekli olan altyapının kurgulanmasının yapıldığı menüdür.

## **1.1.Konfigürasyon Ayarları**

**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları

QDMS sisteminde özel ayarların yapıldığı menülerdir. Bu menülerde yapılan ayarlar tüm QDMS kullanıcıları için geçerli olan ortak ayarlardır.

### **1.1.1. Dil Ayarları**

**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları

Dil ayarları menüsünden QDMS üzerinde görülen menülerin isimleri, alanların isimleri değiştirilebilir. Modüllere yeni alanlar eklenebilir. Var olan alanların zorunluluk durumları düzenlenebilir. Alanların ekran üzerinde göründükleri sıralama değiştirilebilir.

### **1.1.1.1.Düzeltici ve Önleyici Faaliyetler Modülü Ortak Kullanım İçin Yeni Alan Oluşturma**

Düzeltici ve Önleyici Faaliyetler Modülünde Detay Bilgiler, Gelişme Raporu,Kök Nedenler, Aksiyonlar, Sonuç Raporu ve Kapatma sekmelerinde firmanın istemiş olduğu sistemde olmayan ekstradan alanlar tanımlanabilir. Tanımlanan bu alanlar tüm Düzeltici ve Önleyici Faaliyetler Modül kaynakları için geçerlidir. Sistem Altyapı Tanımları/BSAT/ Konfigürasyon Ayarları/Dil Ayarları menüsü tıklanılır. Açılan Dil Ayarları sayfasında Modül alanında “Düzeltici ve Önleyici Faaliyetler” seçilir ve ekranda Düzeltici ve Önleyici Faaliyetler Modülü ile ilgili dil tanımları görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload93241fa2-f787-4f65-87b6-3d115c130b43)

Düzeltici ve Önleyici Faaliyetler Modülünde Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler \>DÖF işlemleri menüsünde Yeni butonu tıklatıldığında açılan -Yeni Kayıt ekranında Detay Bilgiler sekmesinde parametrik tipli alan tanımlaması Dil Ayarların menüsünde yapılmaktadır. Detay Bilgiler sekmesinde parametrik alan tanımlaması yapılırken görüntülecek işlem kaynağı seçimi ve Döf Türü seçeneklerinde seçim yapılır. Görüntülecek işlem kaynağı seçildiğinde tanımlanan alan görüntülecek işlem kaynağında seçim yapılan işlem kaynağına göre Detay bilgiler sekmesinde görüntülenir. Başka işlem kaynaklarında tanımlanan alan görüntülenmez. Döf Türü seçeneği için aynı durum söz konusudur. Seçim yapılan DÖF türüne göre tanımlanan alan Detay Bilgiler sekmesinde görüntülenir. Ayrıca Düzeltici ve Önleyici Faaliyetler Modülünde Gelişme Raporu, Kök Nedenler, Aksiyonlar, Sonuç Raporu ve Kapatma aşamaların gerçekleştiği sekmelerde Dil Ayarları menüsünde parametrik tipli alan tanımlamasıda yapılmaktır. Bu aşamaların gerçekleştiği sekmelerde örneğin Gelişme Raporu ile ilgili parametrik tipli alan tanımlaması yapıldığında Gelişme Raporu sekmesinde, Kök Nedenler ilgili parametrik tipli alan tanımlaması yapıldığında Kök Nedenler sekmesinde tanımlanan parametrik alanlar görüntülenmektedir. Hangi sekmede parametrik tipli alan tanımlaması yapıldıysa ilgili sekmede parametrik tipli alanlar görüntülenmektedir. Bu aşamalarda parametrik tipli alanlarda kullanılan kısa kodlar bulunmaktadır. Hangi aşamada hangi kısa kodlar kullanılmış ayırt etmek mümkündür. Örneğin tanımlanan Metin Tipli parametrik tipli alanlarda hangi aşamada olduğunun ayırt etmek için aşağıdaki kısa kodların başlama kısımlarına dikkate etmek gerekir;

**Detay  Bilgiler sekmesi:** lblPARAM1 kısa kodları genelde detay bilgiler sekmesinde görüntülen parametrik alanları temsil eder.

**Gelişme Raporu:** lblG_Param1, lblG ile başlayan kısa kodları genelde Gelişme aşamasında görüntülenen parametrik tipli alanları temsil eder.

**Kök Nedenler:** lblKOKPARAM1, lblKOK ile başlayan kısa kodları genelde Kök nedenler aşamasında görüntülenen parametrik tipli alanları temsil eder

**Aksiyonlar:** lblA_Param1, lblA kısa kodları ile başlayan genelde Aksiyonlar aşamasında görüntülenen parametrik tipli alanları temsil eder.

**Sonuç Raporu:** lblS_Param1, lblS kısa kodları ile başlayan genelde Sonuç Raporu aşamasında görüntülenen parametrik tipli alanları temsil eder.

**Kapatma:** lblK_Param1, lblK kısa kodları ile başlayan genelde Kapatma aşamasında görüntülenen parametrik tipli alanları temsil eder.

**Doküman Yönetimi Modülünde Tanımlanan Parametrik Tipli Alanlar ve Tanımları;**

**1-Tarih tipli**: Takvim alanı eklenilen parametrik alandır. Örnek Kısa Kod: lblDPARAM1(Detay Bilgiler sekmesinde parametrik alan tipi görüntülenir.)

**2-Liste tipli**: Birden fazla liste elemanları arasından tek seçim yapılan parametrik alandır. Liste elemanları tanımlanarak, tanımlanan liste elemanlarında seçip yapılır. Örnek Kısa Kod: lblG_LParam2 (Gelişme Raporu sekmesinde parametrik alan tipi görüntülenir.)

**3-Personel Tipli:** QDMS personel veri tabanından kişi seçilebilmesini sağlayan parametrik alandır. Sistem Altyapı Tanımları\>Bsat\>Tanımlama\>Personel Tanımlama menüsünde tanımlı olan Personellerin listesinde seçim yapılır. Örnek Kısa Kod: lblG_PParam2 (Gelişme Raporu sekmesinde parametrik alan tipi görüntülenir.)

**4-Sorgu tipli:** QDMS/Ensemble veri tabanları içerisindeki ana verilerden seçim yapılabilmesi için tanımlanabilen alan türüdür. (Sadece Bimser Destek Ekibi tarafından tanımlanmalıdır) Tekli ve çoklu seçim yapılabilir. Örnek Kısa Kod: blQPARAM1(Detay Bilgiler sekmesinde parametrik alan tipi görüntülenir.)

**5-Metin tipli**: Elle yazım imkanı veren metin kutucuğu ekleyen parametrik alandır. Örnek Kısa Kod: lblKOKPARAM1(Kök Nedenler sekmesinde parametrik alan tipi görüntülenir.)

**6-Metin (Çoklu Satır) Tipli**: Elle yazım imkanı veren karakter sınırı olmayan çok satırlı metin kutucuğu eklenen parametrik alandır. Örnek Kısa Kod: lblPARAM8(Detay Bilgiler sekmesinde parametrik alan tipi görüntülenir.)

**7- Başlık Tipli:** Formlara koyu harflerle yazılacak başlık alanı ekleyen parametrik alandır. Örnek Kısa Kod: lblBaslikParam1(Detay Bilgiler sekmesinde parametrik alan tipi görüntülenir.)

**8-Ürün Tipli:** QDMS ürün veri tabanından ürün bilgisinin seçilebilmesini sağlayan parametrik alandır. Sistem Altyapı Tanımları\>BSAT\>Tanımlar\>Ürün Tanımlama menüsünde tanımlı Ürün listesinden Ürün bilgisinin seçimi yapılır. Örnek Kısa Kod: lblUPARAM (Detay Bilgiler sekmesinde parametrik alan tipi görüntülenir.)

**9**-**Parasal Tipli:** Parasal olarak veri girişi yaptıran parametrik alandır. Tanımlanan parametrik alanın yanında para birimleri seçildiği alan çıkar. Para birimleri seçim alanındaki para birimleri Sistem Altyapı Tanımları\>BSAT\>Tanımlar\>Para Birimleri Tanımlama menüsünde tanımlı olan para birimleridir. Örnek Kısa Kod: lblA_NParam1(Aksiyonlar sekmesinde parametrik alan tipi görüntülenir)

**10- Ölçü Birimi Tipli:** Ölçü olarak veri girişi yaptıran parametrik alandır. Tanımlanan parametrik alanın yanında Ölçü birimleri seçildiği alan çıkar. Ölçü birimleri seçim alanındaki ölçü Birimleri Sistem Altyapı Tanımları\>BSAT\>Tanımlar\>Ölçü Birimleri Tanımlama menüsünde tanımlı olan ölçü birimleridir. Örnek Kısa Kod: lblS_NParam3 (Sonuç sekmesinde parametrik alan tipi görüntülenir.)

**11-Doküman (Çoklu Seçim) Tipli:** QDMS doküman veri tabanından doküman seçilebilmesini tekli ve çoklu seçim yapılmasını sağlayan parametrik alandır. Örnek Kısa Kod: lblDOCPARAM1(Detay bilgiler sekmesinde parametrik alan tipi görüntülenir.)

**12-Çoklu ListeTipli:** Birden fazla liste elemanları arasından tekli ve çoklu seçim yapılmasını parametrik alandır. Örnek Kısa Kod: lblS_LMParam2 (Sonuç sekmesinde parametrik alan tipi görüntülenir.)

### **1.1.1.1.1. Düzeltici ve Önleyici Faaliyetler Modülünde Detay Bilgiler Sekmesinde Parametrik Alan Tanımlaması**

Düzeltici ve Önleyici Faaliyetler Modülünde Detay Bilgiler sekmesinde tanımlanan parametrik alanların kısa kodları lblPARAM başlığı ile tanımlı kısa kodlardır. lblPARAM başlığındaki kısa kodlar olan tüm parametrik tipli alanlar tanımlandığında Düzeltici ve Önleyici Faaliyetler Modülünde Detay bilgiler sekmesi ekranında görüntülenir.

### **1.1.1.1.1.1.Tarih Tipli Parametrik Alanların Listesi**

DÖF Modülünde Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri menüsünde Detay Bilgiler sekmesinde Tarih tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Tarih yazarak Tarih tipli parametrik alanlar aratılır ve Tarih tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen tarih tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfa5fea49-1409-4c64-90b0-23e1f627473b)

### **1.1.1.1.1.2.Tarih Tipli Parametrik Alan Tanımlama.**

lblDPARAM1 Tarih tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb281623-1d3c-42f8-9520-b891d9c9d7e3) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd1969bad-290a-4b83-86fc-ed9007665794)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6254a481-18b7-43d7-bc02-58a7746f47d3)

Alanın zorunlu olup, olmayacağı sıra no bilgisi, hangi Döf türünde görüntülenmesi isteniyorsa ilgili seçenekler seçilerek gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d5e69d9-a38d-4f36-ae36-d5c8da9eb045)(Kaydet) butonu tıklanarak tarih tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload15321a57-00db-46ce-97de-f69fbc8b14ab)

Tanımlanan Tarih tipli parametik alan Entegre Yönetim Sistemi\>Düzeltici ve Önleyici Faaliyetler\>DÖf İşlemleri menüsünde Yeni butonu tıklanarak açılan DÖF işlemleri-Yeni Kayıt ekranında Detay Bilgiler sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload54757cce-5642-490e-aa55-bfcaa597bca6)

### **1.1.1.1.1.3.Liste Tipli Parametrik Alanların Listesi**

DÖF Modülünde Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri menüsünde Detay Bilgiler sekmesinde Liste tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Liste yazarak Liste tipli parametrik alanlar aratılır ve Liste tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Liste tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddeb9c89a-ec7a-4c77-b98c-c579ea400283)

### **1.1.1.1.1.4.Liste Tipli Parametrik Alan Tanımlama.**

lblLPARAM2 Liste tipli parametrik seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb281623-1d3c-42f8-9520-b891d9c9d7e3) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfeae54a1-03e6-4d46-94c4-1cda1dab4fb4)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload469d5caa-fa01-4093-b86a-4900d71f114f)

Liste tipli alanın liste değerlerini girmek için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload66f97ccb-fbe8-4710-a3b3-45eb91116899) (Yeni) butonuna tıklanır, liste değerleri yazılır ve kaydedilir. Liste eleman değeri 1 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb1e2c4c6-2c8a-42d1-8ac6-35a7a2bc5111)

Liste eleman değeri 2 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaebc3d72-751d-49bc-bcaf-b692986f8a14)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcc07ac58-76b8-4b7c-ab70-cbeb73d02ffb)

Alanın zorunlu olup, olmayacağı sıra no bilgisi, liste elemanları tanımlanarak Döf türü seçeneklerinde seçip yapılarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d5e69d9-a38d-4f36-ae36-d5c8da9eb045)(kaydet) butonu tıklanarak liste tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload233e67fa-3a6b-4812-bc58-d597b16d62c4)

Tanımlanan Liste Tipli parametik alan Entegre Yönetim Sistemi\>Düzeltici ve Önleyici Faaliyetler\>DÖf İşlemleri menüsünde Yeni butonu tıklanarak açılan DÖF işlemleri-Yeni Kayıt ekranında Detay Bilgiler sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada2d56b81-8e02-4934-868b-e20dd6419f9e)

### **1.1.1.1.1.5.Personel Tipli Parametrik Alanların Listesi**

DÖF Modülünde Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri menüsünde Detay Bilgiler sekmesinde Personel tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Personel yazarak Personel tipli parametrik alanlar aratılır ve Personel tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Personel tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload94791b55-8b25-40ff-bc7b-e70c5bc8b697)

### **1.1.1.1.1.6.Personel Tipli Parametrik Alan Tanımlama**

lblPPARAM1 Personel tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb281623-1d3c-42f8-9520-b891d9c9d7e3) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2495b0f1-49cb-4a5f-9e1e-8e65cb3f700c)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5cbc6c33-1802-49ca-a9ec-5f33761369b0)

Alanın zorunlu olup, olmayacağı sıra no bilgisi, DÖF türü seçeneklerinde seçim yapılarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d5e69d9-a38d-4f36-ae36-d5c8da9eb045)(kaydet) butonu tıklanarak Personel tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir. Varsayılan Değeri Getir check box işaretlendiğinde varsayılan personel bilgisini otomatik olarak sistem getirir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3bc66ea8-b7af-4026-8758-e77b0c4bb140)

Tanımlanan Personel Tipli parametik alan Entegre Yönetim Sistemi\>Düzeltici ve Önleyici Faaliyetler\>DÖf İşlemleri menüsünde Yeni butonu tıklanarak açılan DÖF işlemleri-Yeni Kayıt ekranında Detay Bilgiler sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0cea4697-d86c-4fff-8bc1-16dbdc26cda8)

Personel tipli parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1f8c0d89-b0d1-4792-8b16-36a05706ba2a)(seç) butonu tıklanıldığında sistemde tanımlı personel listesinde seçim yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb1e765d2-3f03-4806-a28e-7c7ed005accc)

### **1.1.1.1.1.7.Sorgu Tipli Parametrik Alanların Listesi**

DÖF Modülünde Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri menüsünde Detay Bilgiler sekmesinde Sorgu tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Sorgu yazarak Sorgu tipli parametrik alanlar aratılır ve Sorgu tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Sorgu tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload54d27578-a58d-48ea-a10c-38d6befeebcd)

### **1.1.1.1.1.8.Sorgu Tipli Parametrik Alan Tanımlama**

lblQPARAM1 Sorgu tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb281623-1d3c-42f8-9520-b891d9c9d7e3) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5f405457-189f-4262-8a21-69ebc442934d)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfa581ca9-0f9c-4a17-b5d2-4ba7813e4659)Bimser Destek ekibinde yardım alınarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d5e69d9-a38d-4f36-ae36-d5c8da9eb045)(kaydet) butonu tıklanarak Sorgu tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade5727398-07c1-4dd1-9c25-2674e2927ce9)

Tanımlanan Sorgu Tipli parametrik alan Entegre Yönetim Sistemi\>Düzeltici ve Önleyici Faaliyetler\>DÖf İşlemleri menüsünde Yeni butonu tıklanarak açılan DÖF işlemleri-Yeni Kayıt ekranında Detay Bilgiler sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0a450409-15a5-42b0-8915-4181b154c494)

Sorgu tipli parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1f8c0d89-b0d1-4792-8b16-36a05706ba2a)(seç) butonu tıklanıldığında sistemde tanımlı Departman listesinde seçim yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload85733ab9-ea57-4a94-869f-9e9a78d37870)

### **1.1.1.1.1.9. Metin Tipli Parametrik Alanların Listesi**

DÖF Modülünde Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri menüsünde Detay Bilgiler sekmesinde Metin tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Metin yazarak Metin tipli parametrik alanlar aratılır ve Metin tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Metin tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9734f737-5b69-49fd-a43a-52f63e6ed9d1)

### **1.1.1.1.1.10. Metin Tipli Parametrik Alan Tanımlama**

lblPARAM2 Metin tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb281623-1d3c-42f8-9520-b891d9c9d7e3) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4c8046bc-f2a5-4e31-85ed-4b3a89021500)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada991a826-e077-4ca8-98a7-b8964836d3e7)

Alanın zorunlu olup, olmayacağı sıra no bilgisi, Döf türü seçeneklerinde seçim yapılarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d5e69d9-a38d-4f36-ae36-d5c8da9eb045)(kaydet) butonu tıklanarak Metin tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd06e8e7e-0cb3-4032-b5e3-f78d058af276)

Tanımlanan Metin Tipli parametrik alan Entegre Yönetim Sistemi\>Düzeltici ve Önleyici Faaliyetler\>DÖf İşlemleri menüsünde Yeni butonu tıklanarak açılan DÖF işlemleri-Yeni Kayıt ekranında Detay Bilgiler sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5f67ac64-fa82-4100-96d5-c6d6d3d2b54e)

### **1.1.1.1.1.11.Metin (Çoklu Satır) Tipli Parametrik Alanların Listesi**

DÖF Modülünde Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri menüsünde Detay Bilgiler sekmesinde Metin (Çoklu Satır)  tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Metin (Çoklu Satır) yazarak Metin (Çoklu Satır) tipli parametrik alanlar aratılır ve Metin (Çoklu Satır)  tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Metin (Çoklu Satır)  tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6cf521d2-52b4-4161-a1fd-04b200227254)

### **1.1.1.1.1.12.Metin (Çoklu Satır) Tipli Parametrik Alan Tanımlama**

lblPARAM8 Metin (Çoklu Satır) tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb281623-1d3c-42f8-9520-b891d9c9d7e3) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3a2d3197-3d48-44fe-8143-a3b6d26fb35b)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload68d77e5d-1f93-4636-b53d-0bf57457d90d)

Alanın zorunlu olup, olmayacağı sıra no bilgisi, Döf türü bilgisi seçeneklerinden seçim yapılarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d5e69d9-a38d-4f36-ae36-d5c8da9eb045)(kaydet) butonu tıklanarak Metin (Çoklu Satır) tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc5a7967e-a2c2-4c0e-b693-2bda1d914cab)

Tanımlanan Metin (Çoklu Satır) Tipli parametrik alan Entegre Yönetim Sistemi\>Düzeltici ve Önleyici Faaliyetler\>DÖF İşlemleri menüsünde Yeni butonu tıklanarak açılan DÖF işlemleri-Yeni Kayıt ekranında Detay Bilgiler sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7d0cde4a-015a-4eba-a4b7-0fabbb39d56c)

### **1.1.1.1.1.13.Ölçü Birimi Parametrik Alanların Listesi**

DÖF Modülünde Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri menüsünde Detay Bilgiler sekmesinde Ölçü Birimi tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Ölçü Birimi yazarak Ölçü Birimi tipli parametrik alanlar aratılır ve Ölçü Birimi tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Ölçü Birimi tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2246a5b3-3fbf-4e3b-a665-b4355b00a7ff)

### **1.1.1.1.1.14. Ölçü Birimi Parametrik Alan Tanımlama**

lblNPARAM6 Ölçü birimi tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb281623-1d3c-42f8-9520-b891d9c9d7e3) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload070a6380-10f5-4ee6-80e5-2977c211a44f)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2f551e47-c23e-4137-8520-98b4fcd2bef6)

Alanın zorunlu olup, olmayacağı sıra no bilgisi, Döf Türü seçeneklerinde seçim yapılarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d5e69d9-a38d-4f36-ae36-d5c8da9eb045)(Kaydet) butonu tıklanarak ölçü birimi tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8b8b6da3-d169-494a-a3c0-7de59ae57a2e)

Tanımlanan ölçü birimi tipli parametrik alan Entegre Yönetim Sistemi\>Düzeltici ve Önleyici Faaliyetler\>DÖf İşlemleri menüsünde Yeni butonu tıklanarak açılan DÖF işlemleri-Yeni Kayıt ekranında Detay Bilgiler sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload497c437e-61de-4f1c-9074-e8c8c39a835c)

### **1.1.1.1.1.15.Parasal Tipli Parametrik Alanların Listesi**

DÖF Modülünde Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri menüsünde Detay Bilgiler sekmesinde Parasal tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Parasal yazarak Parasal tipli parametrik alanlar aratılır ve Parasal tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Parasal tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9f261c35-8846-4131-a80a-ccfd11a0ffc9)

### **1.1.1.1.1.16.Parasal Tipli Parametrik Alan Tanımlama**

lblNPARAM1 Parasal tipli alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb281623-1d3c-42f8-9520-b891d9c9d7e3) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload61348fea-8858-42f3-9851-c8d34549fa6b)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf73c6033-6f3e-48f2-a869-07db482e3414)

Alanın zorunlu olup, olmayacağı sıra no bilgisi, Döf türü seçeneklerinde seçim yapılarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d5e69d9-a38d-4f36-ae36-d5c8da9eb045)(Kaydet ) butonu tıklanarak Parasal tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload661059d4-af46-474b-9156-3715c9521d3c)

Tanımlanan Parasal Tipli parametrik alan Entegre Yönetim Sistemi\>Düzeltici ve Önleyici Faaliyetler\>DÖF İşlemleri menüsünde Yeni butonu tıklanarak açılan DÖF işlemleri-Yeni Kayıt ekranında Detay Bilgiler sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0f48feaa-0376-4195-a22c-7ef2a068005f)

### **1.1.1.1.1.17. Başlık Tipli Parametrik Alanların Listesi**

DÖF Modülünde Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri menüsünde Detay Bilgiler sekmesinde Başlık tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Başlık yazarak Başlık tipli parametrik alanlar aratılır ve Başlık tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Başlık tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload553bcb4b-124c-4ba7-8397-dd5a60f59b83)

### **1.1.1.1.1.18.Başlık Tipli Parametrik Alan Tanımlama**

lblBaslikParam1 Başlık tipli alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb281623-1d3c-42f8-9520-b891d9c9d7e3) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4143e780-0598-4eda-ae5f-058680e867fd)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4d524385-36ea-4851-b71e-4c6154a4c3fb)

Alanın zorunlu olup, olmayacağı sıra no bilgisi, Döf türü seçeneklerden seçim yapılarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d5e69d9-a38d-4f36-ae36-d5c8da9eb045)(Kaydet ) butonu tıklanarak Başlık tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfdb1f78c-b0cc-4012-a97b-d74c55493578)

Tanımlanan Başlık Tipli parametrik alan Entegre Yönetim Sistemi\>Düzeltici ve Önleyici Faaliyetler\>DÖf İşlemleri menüsünde Yeni butonu tıklanarak açılan DÖF işlemleri-Yeni Kayıt ekranında Detay Bilgiler sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcb67aa40-4024-4ce0-bd37-e90d75e90cc6)

### **1.1.1.1.1.19. ÜrünTipli Parametrik Alanların Listesi**

DÖF Modülünde Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri menüsünde Detay Bilgiler sekmesinde Ürün tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Ürün yazarak Ürün tipli parametrik alanlar aratılır ve Ürün tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Ürün tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadffa79f30-9787-472e-bb6c-8dc0588d71ac)

### **1.1.1.1.1.20. Ürün Tipli Parametrik Alan Tanımlama**

lblUPARAM Ürün tipli alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb281623-1d3c-42f8-9520-b891d9c9d7e3) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6306f8c7-ecf2-488e-bfe2-ceb43e5e79cf)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload315f6e55-b13e-466c-87e9-f34e1e5144ff)

Alanın zorunlu olup, olmayacağı sıra no bilgisi Döf türü seçeneklerinde seçim yapılarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d5e69d9-a38d-4f36-ae36-d5c8da9eb045)(Kaydet ) butonu tıklanarak Ürün tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6fa45674-06f8-47b2-9444-e9ba3669e735)

Tanımlanan Ürün Tipli parametrik alan Entegre Yönetim Sistemi\>Düzeltici ve Önleyici Faaliyetler\>DÖf İşlemleri menüsünde Yeni butonu tıklanarak açılan DÖF işlemleri-Yeni Kayıt ekranında Detay Bilgiler sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6e5a1b12-34e7-426d-a371-07648c4cb2ed)

Ürün tipli parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade4f5660a-df95-4834-a663-616c9822f97f)(Ekle) butonu tıklanıldığında sistemde tanımlı Ürün listesinde Ürün ekleme işlemi yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload08f46690-ca85-4634-a4e7-120df602f895)

### **1.1.1.1.1.21. Doküman (Çoklu Seçim) Tipli Parametrik Alanların Listesi**

DÖF Modülünde Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri menüsünde Detay Bilgiler sekmesinde Doküman (Çoklu Seçim) tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Doküman (Çoklu Seçim) yazarak Doküman (Çoklu Seçim) tipli parametrik alanlar aratılır ve Doküman (Çoklu Seçim) tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Doküman (Çoklu Seçim) tipli parametrik alanların alan tanımlaması yapılır.

### **1.1.1.1.1.22.Doküman (Çoklu Seçim) Tipli Parametrik Alan Tanımlama.**

lblDOCPARAM1 Doküman (Çoklu Seçim) tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb281623-1d3c-42f8-9520-b891d9c9d7e3) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd98c15d6-7ae7-4ad6-a6e9-1d04061cf4de)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbebf215f-b120-4fc4-b93b-c5c22b429873)

Alanın zorunlu olup, olmayacağı sıra no bilgisi Döf türü seçeneklerinde seçim yapılarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d5e69d9-a38d-4f36-ae36-d5c8da9eb045)(kaydet) butonu tıklanarak Doküman (Çoklu Seçim) parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd30f8c7e-350c-4935-ac04-6365996c3bf2)

Tanımlanan Doküman (Çoklu Seçim) tipli parametrik alan Entegre Yönetim Sistemi\>Düzeltici ve Önleyici Faaliyetler\>DÖF İşlemleri menüsünde Yeni butonu tıklanarak açılan DÖF işlemleri-Yeni Kayıt ekranında Detay Bilgiler sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaaef6539-a71a-4599-8213-0a0425139cdf)

Doküman (Çoklu Seçim) parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade4f5660a-df95-4834-a663-616c9822f97f)(Ekle) butonu tıklanıldığında sistemde tanımlı doküman listesinde doküman ekleme işlemi yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload342ccdae-51f0-4596-9287-2c035dc83830)

DÖF işlemleri-Yeni Kayıt ekranında Detay Bilgiler sekmesinde tanımlanan tüm parametrik alan tipleri ;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload67dc0515-a4d1-4f27-9e5d-0edb7c0a3a69)

### **1.1.1.1.2. Düzeltici ve Önleyici Faaliyetler Modülünde Gelişme Raporu Sekmesinde Parametrik Alan Tipi Tanımlaması**

Düzeltici ve Önleyici Faaliyetler Modülünde Gelişme Raporu sekmesinde tanımlanan parametrik alanların kısa kodları lblG\_ başlığı ile tanımlı kısa kodlardır. lblG\_ başlığındaki kısa kodlar olan tüm parametrik tipli alanlar tanımlandığında Düzeltici ve Önleyici Faaliyetler Modülünde Gelişme Raporu sekmesi ekranında görüntülenir.

### **1.1.1.1.2.1.Liste Tipli Parametrik Alanların Listesi**

DÖF Modülünde Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Gelişme Raporu sekmesinde Liste tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Liste yazarak Liste tipli parametrik alanlar aratılır ve Liste tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Liste tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload18a21634-a313-48b8-b66a-a76f56f0bd2a)

### **1.1.1.1.2.2.Liste Tipli Parametrik Alan Tanımlama.**

lblG_LParam2 Liste tipli parametrik seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb281623-1d3c-42f8-9520-b891d9c9d7e3) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade71266e5-9a46-4813-bc72-46ab99ba7661)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada192b853-d921-4729-ad6a-d702246f2b8c)

Liste tipli alanın liste değerlerini girmek için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload66f97ccb-fbe8-4710-a3b3-45eb91116899) (Yeni) butonuna tıklanır, liste değerleri yazılır ve kaydedilir. Liste eleman değeri 1 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade7bb9241-1027-41f5-9957-a5f9ea611020)

Liste eleman değeri 2 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0dc0470a-77bb-42d6-b7be-aa7af961008b)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2fb9c16f-75a9-4647-8497-f74788f10f73)

Alanın zorunlu olup, olmayacağı sıra no bilgisi ve liste elemanları tanımlanarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d5e69d9-a38d-4f36-ae36-d5c8da9eb045)(kaydet) butonu tıklanarak liste tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload095f9917-f747-43d4-a11e-a3cdffbe237d)

Tanımlanan liste tipli parametrik Alan Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Gelişme Raporu sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2e751241-baa2-456e-9045-2fe15bd287e0)

### **1.1.1.1.2.3.Personel Tipli Parametrik Alanların Listesi**

DÖF Modülünde Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Gelişme Raporu sekmesinde Personel tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Personel yazarak Personel tipli parametrik alanlar aratılır ve Personel tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Personel tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade4c43484-3a17-49ec-b296-c8e11c4f6afe)

### **1.1.1.1.2.4.Personel Tipli Parametrik Alan Tanımlama.**

lblG_PParam2 Personel tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb281623-1d3c-42f8-9520-b891d9c9d7e3) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9a580aaa-6e0a-4644-9f1c-6e8293139851)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0b3ddf63-e729-47d2-b33c-202f562406fe)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d5e69d9-a38d-4f36-ae36-d5c8da9eb045)(kaydet) butonu tıklanarak Personel tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload39353af9-fe2d-43f2-9fde-a1a8ba594f12)

Tanımlanan Personel tipli parametrik Alan Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Gelişme Raporu sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaaabc622-3305-4049-9dc3-6bece0c8b0f6)

Personel tipli parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1f8c0d89-b0d1-4792-8b16-36a05706ba2a)(seç) butonu tıklanıldığında sistemde tanımlı personel listesinde seçim yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload07bb38f8-87a1-4b27-8e75-c11fadb6aff1)

### **1.1.1.1.2.5.Sorgu Tipli Parametrik Alanların Listesi**

DÖF Modülünde Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Gelişme Raporu sekmesinde Sorgu tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Sorgu yazarak Sorgu tipli parametrik alanlar aratılır ve Sorgu tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Sorgu tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1256979b-fd2f-4a54-9c77-349093614a6e)

### **1.1.1.1.2.6.Sorgu Tipli Parametrik Alan Tanımlama**

lblG_QParam1 Sorgu tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb281623-1d3c-42f8-9520-b891d9c9d7e3) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0dbadcf9-e246-43c5-88b4-6e5e6e6a16e5)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload64719a2c-a175-4d6c-979a-ed90910b75ed)

Bimser Destek ekibi tarafından gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d5e69d9-a38d-4f36-ae36-d5c8da9eb045)(kaydet) butonu tıklanarak Sorgu tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0fff4b27-081b-4fca-afa5-c042fe25117a)

Tanımlanan Sorgu tipli parametrik Alan Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Gelişme Raporu sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0aa77f6c-eaec-48f3-9364-959a54573114)

Sorgu tipli parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1f8c0d89-b0d1-4792-8b16-36a05706ba2a)(seç) butonu tıklanıldığında sistemde tanımlı Pozisyon listesinde seçim yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload384c231c-332a-4962-84b1-4f40fd4ed2e5)

### **1.1.1.1.2.7.Metin Tipli Parametrik Alanların Listesi**

DÖF Modülünde Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Gelişme Raporu sekmesinde Metin tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Metin yazarak Metin tipli parametrik alanlar aratılır ve Metin tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Metin tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1c1a00fb-96f9-49c8-bc1c-8d9211182068)

### **1.1.1.1.2.8.Metin Tipli Parametrik Alan Tanımlama**

lblG_Param2 Metin tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb281623-1d3c-42f8-9520-b891d9c9d7e3) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf2968d1b-a63e-4737-bd96-6e245013d5d6)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2c81b758-f8a7-4618-9bf1-6c62141c3c8b)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d5e69d9-a38d-4f36-ae36-d5c8da9eb045)(kaydet) butonu tıklanarak Metin tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcdab1007-c2c9-4fc3-8613-dbabf0ecbcb0)

Tanımlanan Metin tipli parametrik Alan Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Gelişme Raporu sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8f22c8f5-c22a-4706-915f-c79096ac7b39)

### **1.1.1.1.2.9.Ölçü Birimi Parametrik Alanların Listesi**

DÖF Modülünde Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Gelişme Raporu sekmesinde Ölçü Birimi tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Ölçü Birimi yazarak Ölçü Birimi tipli parametrik alanlar aratılır ve Ölçü Birimi tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Ölçü Birimi tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadde3dd122-91cc-4340-a3bb-f47ef6fdc49c)

### **1.1.1.1.2.10.Ölçü Birimi Parametrik Alan Tanımlama**

lblG_NParam3 Ölçü birimi tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb281623-1d3c-42f8-9520-b891d9c9d7e3) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload00174f43-3f72-4885-9d34-b125b982d64f)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload877332e8-652e-4cd7-afe5-ace05098376f)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d5e69d9-a38d-4f36-ae36-d5c8da9eb045)(Kaydet) butonu tıklanarak ölçü birimi tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade6546509-1b3f-498e-b643-f6a0adfe7e66)

Tanımlanan ölçü birimi tipli parametrik Alan Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Gelişme Raporu sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload47cfae8f-a2ae-4bf7-b0d6-b184cb9fe455)

### **1.1.1.1.2.11.Parasal Tipli Parametrik Alanların Listesi**

DÖF Modülünde Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Gelişme Raporu sekmesinde Parasal tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Parasal yazarak Parasal tipli parametrik alanlar aratılır ve Parasal tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Parasal tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload998ff739-327d-4bc8-8372-bee7b467028e)

### **1.1.1.1.2.12.Parasal Tipli Parametrik Alan Tanımlama**

lblG_NParam1Parasal tipli alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb281623-1d3c-42f8-9520-b891d9c9d7e3) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf987fa8f-3752-4f37-bb7e-06824e49f7ef)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload80167277-41e5-424d-990e-588edb16c73b)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d5e69d9-a38d-4f36-ae36-d5c8da9eb045)(Kaydet ) butonu tıklanarak Parasal tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload19b00cab-78d4-46b5-899a-11e10f39611e)

Tanımlanan Parasal tipli parametrik Alan Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Gelişme Raporu sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload73622cd5-5559-4714-bab7-733608e5ae37)

Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Gelişme Raporu sekmesinde Tanımlanan Tüm Parametrik Tipli Alanlar;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload732e5a5f-0e53-4cd9-abf3-01934e3e8d48)

### **1.1.1.1.3. Düzeltici ve Önleyici Faaliyetler Modülünde Kök Nedenler Sekmesinde Parametrik Alan Tipi Tanımlaması**

Düzeltici ve Önleyici Faaliyetler Modülünde Kök Nedenler sekmesinde tanımlanan parametrik alanların kısa kodları lblKOK başlığı ile tanımlı kısa kodlardır. lblKOK başlığındaki kısa kodlar olan tüm parametrik tipli alanlar tanımlandığında Düzeltici ve Önleyici Faaliyetler Modülünde Kök Nedenler sekmesi ekranında görüntülenir.

### **1.1.1.1.3.1.Tarih Tipli Parametrik Alanların Listesi**

DÖF Modülünde Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Kök Nedenler sekmesinde tarih tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına tarih yazarak tarih tipli parametrik alanlar aratılır ve tarih tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen tarih tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8b344827-c27d-4c16-8ce5-94e655d8034b)

### **1.1.1.1.3.2.Tarih Tipli Parametrik Alan Tanımlama.**

lblKOKDPARAM1 Tarih tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb281623-1d3c-42f8-9520-b891d9c9d7e3) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload87988b63-e8f3-427d-a953-525f4ace43f0)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload815e28f2-b770-48c1-b5dd-dd9da69c0ec3)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d5e69d9-a38d-4f36-ae36-d5c8da9eb045)(Kaydet) butonu tıklanarak tarih tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc1ade1fc-f38a-4867-b55e-0d78ba41f751)

Tanımlanan tarih tipli parametrik Alan Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Kök Nedenler sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5d710757-9b8c-489f-b525-f1ce10bed35c)

### **1.1.1.1.3.3.Liste Tipli Parametrik Alanların Listesi**

DÖF Modülünde Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Kök Nedenler sekmesinde liste tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına liste yazarak liste tipli parametrik alanlar aratılır ve liste tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen liste tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4b6796e1-7dcf-4699-a408-33c9a2910535)

### **1.1.1.1.3.4.Liste Tipli Parametrik Alan Tanımlama**

lblKOKLPARAM1 Liste tipli parametrik seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb281623-1d3c-42f8-9520-b891d9c9d7e3) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7f9ca227-4748-48b1-b0aa-2d4b2c626215)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload857cdb92-51aa-455c-ba7d-2f2b5d2dc63a)

Liste tipli alanın liste değerlerini girmek için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload66f97ccb-fbe8-4710-a3b3-45eb91116899) (Yeni) butonuna tıklanır, liste değerleri yazılır ve kaydedilir. Liste eleman değeri 1 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0f0b45f1-7312-4980-9652-5ffc081277e7)

Liste eleman değeri 2 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaaff50ba-3080-4b9a-b482-1cae9dfa4572)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0e830ae2-0a55-4c6e-aedf-93b467dd36fe)

Alanın zorunlu olup, olmayacağı sıra no bilgisi ve liste elemanları tanımlanarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d5e69d9-a38d-4f36-ae36-d5c8da9eb045)(kaydet) butonu tıklanarak liste tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload317c3e24-058a-4371-916b-4e36f52f08bf)

Tanımlanan liste tipli parametrik Alan Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Kök Nedenler sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload199d2979-f5a0-4394-aefb-1c9458fcbbc1)

### **1.1.1.1.3.5.Metin Tipli Parametrik Alanların Listesi**

DÖF Modülünde Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Kök Nedenler sekmesinde metin tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına metin yazarak Metin tipli parametrik alanlar aratılır ve metin tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen metin tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7e20ac77-43c7-45ad-933f-de4a236e5cc8)

### **1.1.1.1.3.6. Metin Tipli Parametrik Alan Tanımlama**

lblKOKPARAM1 Metin tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb281623-1d3c-42f8-9520-b891d9c9d7e3) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd589ca40-2719-4b87-a69f-e6715b520e08)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload98c6bf8c-87ce-472f-aed6-773405c4204d)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d5e69d9-a38d-4f36-ae36-d5c8da9eb045)(kaydet) butonu tıklanarak Metin tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload55e1d1ad-169d-4504-a04a-ad9ad4c75f02)

Tanımlanan Metin tipli parametrik Alan Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Kök Nedenler sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc9491333-cd4b-445c-b856-a81bf8ed1e04)

### **1.1.1.1.3. 7.Ölçü Birimi Parametrik Alanların Listesi**

DÖF Modülünde Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Kök Nedenler sekmesinde ölçü Birimi tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına ölçü Birimi yazarak ölçü Birimi tipli parametrik alanlar aratılır ve ölçü Birimi tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen ölçü Birimi tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload14a1b08e-6337-4fa6-acfb-ca5b55919341)

### **1.1.1.1.3.8.Ölçü Birimi Parametrik Alan Tanımlama**

lblKOKNAPARAM1Ölçü birimi tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb281623-1d3c-42f8-9520-b891d9c9d7e3) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadeae84bc9-d74e-41e1-b96a-8c6166382b15)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade1c2a66f-a5c3-43bb-aac4-f76c27bb2d75)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d5e69d9-a38d-4f36-ae36-d5c8da9eb045)(Kaydet) butonu tıklanarak ölçü birimi tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd1503154-66cb-4e28-9eae-91925872dbe7)

Tanımlanan ölçü birimi tipli parametrik Alan Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Kök Nedenler sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada0c343b6-7eb0-43d7-9d66-725bca3d070f)

### **1.1.1.1.3. 9.Parasal Tipli Parametrik Alanların Listesi**

DÖF Modülünde Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Kök Nedenler sekmesinde parasal tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına parasal yazarak parasal tipli parametrik alanlar aratılır ve parasal tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen parasal tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0f258043-8957-4ad6-8269-ebf4a96d9603)

### **1.1.1.1.3. 10.Parasal Tipli Parametrik Alan Tanımlama**

lblKOKNCPARAM1 Parasal tipli alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb281623-1d3c-42f8-9520-b891d9c9d7e3) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc1f3a666-df0e-43d6-bff4-a407175f8a8a)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload389b7e78-077f-4db3-a106-2df5d697217d)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d5e69d9-a38d-4f36-ae36-d5c8da9eb045)(Kaydet ) butonu tıklanarak parasal tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload762fe713-fd4d-4f08-8aeb-d9b78617b864)

Tanımlanan parasal tipli parametrik alan Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Kök Nedenler sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload242aec58-d5b3-4076-ad5e-e08cb854c4db)

Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Kök Nedenler sekmesinde Tanımlanan Tüm Alanlar;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd03d2a37-7ee8-47c1-b57b-86821559cd5a)

### **1.1.1.1.4.Düzeltici ve Önleyici Faaliyetler Modülünde Aksiyonlar Sekmesinde Parametrik Alan Tipi Tanımlaması**

Düzeltici ve Önleyici Faaliyetler Modülünde Aksiyonlar sekmesinde tanımlanan parametrik tipli alanların kısa kodları lblA\_ başlığı ile tanımlı kısa kodlardır. lblA \_ başlığındaki kısa kodlar olan tüm parametrik tipli alanlar tanımlandığında Düzeltici ve Önleyici Faaliyetler Modülünde Aksiyonlar sekmesi ekranında görüntülenir.

### **1.1.1.1.4.1.Tarih Tipli Parametrik Alanların Listesi**

DÖF Modülünde Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Aksiyonlar sekmesinde tarih tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına tarih yazarak tarih tipli parametrik alanlar aratılır ve tarih tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen tarih tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload116a0a75-abba-4c23-a8e8-5b3736347dc1)

### **1.1.1.1.4.2.Tarih Tipli Parametrik Alan Tanımlama**

lblA_DParam1 Tarih tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb281623-1d3c-42f8-9520-b891d9c9d7e3) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc9d0de7c-e58d-4910-af05-98bcd7a7dc74)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada171c867-cafc-4221-8673-aa90569b2841)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d5e69d9-a38d-4f36-ae36-d5c8da9eb045)(Kaydet) butonu tıklanarak tarih tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd1a5b898-49fb-422d-b881-a713b739c3b0)

Tanımlanan tarih tipli parametrik alan Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Aksiyonlar sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6b47ea8e-73a4-47d1-9da0-57bd7d15449c)

### **1.1.1.1.4.3.Liste Tipli Parametrik Alanların Listesi**

DÖF Modülünde Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında **Aksiyonlar** sekmesinde liste tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına liste yazarak liste tipli parametrik alanlar aratılır ve liste tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen liste tipli parametrik alanların alan tanımlaması yapılır.

### **1.1.1.1.4.4.Liste Tipli Parametrik Alan Tanımlama**

lblA_LParam1 Liste tipli parametrik seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb281623-1d3c-42f8-9520-b891d9c9d7e3) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload28428e86-8644-47e0-b819-d1131c6e2358)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload46ea6d82-1de5-42ed-9755-5f8bdbc7bbee)

Liste tipli alanın liste değerlerini girmek için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload66f97ccb-fbe8-4710-a3b3-45eb91116899) (Yeni) butonuna tıklanır, liste değerleri yazılır ve kaydedilir. Liste elaman değeri 1 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc6b6f736-224b-4301-b04c-531a833e80f6)

Liste eleman değeri 2 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadceebb6e3-e01e-47b5-a8a9-69620b12f07f)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3d2ee02c-3fef-4e41-a043-cf758c81c82d)

Alanın zorunlu olup, olmayacağı sıra no bilgisi ve liste elemanları tanımlanarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d5e69d9-a38d-4f36-ae36-d5c8da9eb045)(kaydet) butonu tıklanarak liste tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4e82b4fa-6fdd-4b58-ae97-dc6a77bb4296)

Tanımlanan liste tipli parametrik alan Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Aksiyonlar sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc6fe5066-8d00-4a8e-b400-1062a1a5da51)

### **1.1.1.1.4.5.Sorgu Tipli Parametrik Alanların Listesi**

DÖF Modülünde Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Aksiyonlar sekmesinde sorgu tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına sorgu yazarak sorgu tipli parametrik alanlar aratılır ve sorgu tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen sorgu tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadea764d34-4f23-4e39-9056-d8cf8e93b6fe)

### **1.1.1.1.4.6.Sorgu Tipli Parametrik Alan Tanımlama**

lblA_QPARAM1 Sorgu tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb281623-1d3c-42f8-9520-b891d9c9d7e3) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc148c618-3e25-4e31-bd67-8ef32d96866d)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload079825f8-16c8-48d1-b54d-81ffe27429d8)

Bimser Destek ekibi tarafından gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d5e69d9-a38d-4f36-ae36-d5c8da9eb045)(kaydet) butonu tıklanarak Sorgu tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade9344395-2f80-4fc5-9688-019d2b3552cf)

Tanımlanan sorgu tipli parametrik Alan Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Aksiyonlar sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd365ee43-b842-41fc-b044-5b096cac201f)

Sorgu tipli parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1f8c0d89-b0d1-4792-8b16-36a05706ba2a)(seç) butonu tıklanıldığında sistemde tanımlı Pozisyon listesinde seçim yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd9889a02-76e3-46de-8c47-36eececed84c)

### **1.1.1.1.4.7.Metin Tipli Parametrik Alanların Listesi**

DÖF Modülünde Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Aksiyonlar sekmesinde metin tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına metin yazarak metin tipli parametrik alanlar aratılır ve metin tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen metin tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload752fbb8b-93c7-4b21-bd6c-1c710844d10f)

### **1.1.1.1.4.8.Metin Tipli Parametrik Alan Tanımlama**

lblA_Param2 Metin tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb281623-1d3c-42f8-9520-b891d9c9d7e3) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5af127ea-b79f-401e-aef7-dc53a0caf939)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbb4d54d5-f143-4120-861b-a1f55f693df4)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d5e69d9-a38d-4f36-ae36-d5c8da9eb045)(kaydet) butonu tıklanarak Metin tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload044d6161-bf9e-4d4e-a7f7-2efcfad2c7f1)

Tanımlanan metin tipli parametrik alan Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Aksiyonlar sekmesinde görüntülenir

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload362bf759-3ec5-4722-b8b4-daae5a9b4e27)

### **1.1.1.1.4.9.Metin (Çoklu Satır) Tipli Parametrik Alanların Listesi**

DÖF Modülünde Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Aksiyonlar sekmesinde Metin (Çoklu Satır) tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Metin (Çoklu Satır)  yazarak Metin (Çoklu Satır)  tipli parametrik alanlar aratılır ve Metin (Çoklu Satır)  tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Metin (Çoklu Satır) tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6797d170-1375-47b9-81b1-4cfa8f8d10f3)

### **1.1.1.1.4.10.Metin (Çoklu Satır) Tipli Parametrik Alan Tanımlama**

lblA_Param11 Metin (Çoklu Satır) tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb281623-1d3c-42f8-9520-b891d9c9d7e3) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9e48b243-f16f-457f-9389-702c4688cc32)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadda9b3eaa-98aa-45a5-a315-36ef64e48ab9)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d5e69d9-a38d-4f36-ae36-d5c8da9eb045)(kaydet) butonu tıklanarak Metin (Çoklu Satır) tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6fd50dba-5c5f-4190-bca7-95d9577787a6)

Tanımlanan Metin (Çoklu Satır) tipli parametrik alan Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Aksiyonlar sekmesinde görüntülenir

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9b57b0c7-9b32-4795-97df-0f33ed780ae2)

### **1.1.1.1.4.11.Ölçü Birimi Parametrik Alanların Listesi**

DÖF Modülünde Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Aksiyonlar sekmesinde ölçü Birimi tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına ölçü Birimi yazarak ölçü Birimi tipli parametrik alanlar aratılır ve ölçü Birimi tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen ölçü Birimi tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4d84141e-44b4-4f90-bee2-12e6e0a3dc94)

### **1.1.1.1.4.12.Ölçü Birimi Parametrik Alan Tanımlama**

lblA_NParam3 Ölçü birimi tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb281623-1d3c-42f8-9520-b891d9c9d7e3) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1b268fb5-a63a-4fee-b46a-826d61d9eade)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada53d950d-6b8d-45b8-8001-aabb844b1ebc)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d5e69d9-a38d-4f36-ae36-d5c8da9eb045)(Kaydet) butonu tıklanarak ölçü birimi tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5f863af6-eea5-40e2-80d3-de6fd5aca9db)

Tanımlanan ölçü birimi tipli parametrik alan Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Aksiyonlar sekmesinde görüntülenir

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddd726f80-e0eb-4d14-9af1-9ed5b12916c8)

### **1.1.1.1.4.13.Parasal Tipli Parametrik Alanların Listesi**

DÖF Modülünde Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Aksiyonlar sekmesinde parasal tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına parasal yazarak parasal tipli parametrik alanlar aratılır ve parasal tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen parasal tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaa6ddb1b-6b31-46c3-b791-3ef89bd0bece)

### **1.1.1.1.4.14.Parasal Tipli Parametrik Alan Tanımlama**

lblA_NParam1 Parasal tipli alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb281623-1d3c-42f8-9520-b891d9c9d7e3) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb24adfbf-cefb-474d-bd0e-b42266348316)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7f3ed271-241f-4fe8-aff0-cd67361d1f6e)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d5e69d9-a38d-4f36-ae36-d5c8da9eb045)(Kaydet ) butonu tıklanarak parasal tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6ca28547-aef1-47db-a895-bc5b89992145)

Tanımlanan parasal tipli parametrik alan Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Aksiyonlar sekmesinde görüntülenir

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6faa9967-7f49-4f1a-8097-05c39245e249)

Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Aksiyonlar sekmesinde tanımlanan tüm parametrik alanlar;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade098671d-f58b-4897-9cc9-23aafd6cb344)

### **1.1.1.1.5.Düzeltici ve Önleyici Faaliyetler Modülünde Sonuç Raporu Sekmesinde Parametrik Alan Tipi Tanımlaması.**

Düzeltici ve Önleyici Faaliyetler Modülünde Sonuç Raporu sekmesinde tanımlanan parametrik alanların kısa kodları lblS\_ başlığı ile tanımlı kısa kodlardır. lblS\_ başlığındaki kısa kodlar olan tüm parametrik tipli alanlar tanımlandığında Düzeltici ve Önleyici Faaliyetler Modülünde Sonuç Raporu sekmesi ekranında görüntülenir.

### **1.1.1.1.5.1.Liste Tipli Parametrik Alanların Listesi**

DÖF Modülünde Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Sonuç Raporu sekmesinde liste tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına liste yazarak liste tipli parametrik alanlar aratılır ve liste tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen liste tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9468a30c-ddf0-4136-a387-48d72444816a)

### **1.1.1.1.5.2.Liste Tipli Parametrik Alan Tanımlama.**

lblS_LParam2 Liste tipli parametrik seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb281623-1d3c-42f8-9520-b891d9c9d7e3) (değiştir) butonuna tıklanır

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload532ca7e6-bdc5-4e95-a090-92e3c64710f0)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb36bc894-26a0-425c-9865-63f06b956723)

Liste tipli alanın liste değerlerini girmek için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload66f97ccb-fbe8-4710-a3b3-45eb91116899) (Yeni) butonuna tıklanır, liste değerleri yazılır ve kaydedilir. Liste eleman değeri 1 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload916f8e95-c9b6-44eb-a9cb-0abb034de07f)

Liste eleman değeri 2 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload460e4765-56de-4b9f-9b7b-d40f13267924)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada5aa3931-c15d-46e6-9b0c-e49f189ae81a)

Alanın zorunlu olup, olmayacağı sıra no bilgisi ve liste elemanları tanımlanarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d5e69d9-a38d-4f36-ae36-d5c8da9eb045)(kaydet) butonu tıklanarak liste tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload46be6eee-dbf7-4150-a4ef-03bbab2aa9d8)

Tanımlanan liste tipli parametrik alan Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Sonuç Raporu sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload69f7ff07-4e69-4b2f-9536-47a1b8eae136)

### **1.1.1.1.5.3.Çoklu Liste Tipli Parametrik Alanların Listesi**

DÖF Modülünde Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Sonuç Raporu sekmesinde Çoklu liste tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Çoklu liste yazarak Çoklu liste tipli parametrik alanlar aratılır ve Çoklu liste tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Çoklu liste tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2af4ecda-2aa1-4d1f-974f-202594965775)

### **1.1.1.1.5.4.Çoklu Liste Tipli Parametrik Alan Tanımlama.**

lblS_LMParam2 Çoklu Liste tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb281623-1d3c-42f8-9520-b891d9c9d7e3) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddcbb1f76-bcd3-4862-a26f-4dbe4b820f78)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.Çoklu Liste tipli alanın liste değerlerini girmek için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload66f97ccb-fbe8-4710-a3b3-45eb91116899) (Yeni) butonuna tıklanır, liste değerleri yazılır ve kaydedilir.Liste elaman değeri 1 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload06a2d10e-909f-4adb-b9e2-c9f477ba87c6)

Liste eleman değeri 2 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload744798d6-1eb8-4e1a-acc0-7bd18bb78212)

Liste eleman değeri 3 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload799811b5-d9f7-4aad-8b0e-d01462a94f3f)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload24bde738-fdda-4e70-b588-48867e90300d)

Alanın zorunlu olup, olmayacağı sıra no bilgisi ve liste elemanları tanımlanarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d5e69d9-a38d-4f36-ae36-d5c8da9eb045)(kaydet) butonu tıklanarak Çoklu liste tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0a3587bb-a0e7-4086-8661-ee0b3d589329)

Tanımlanan Çoklu liste tipli parametrik alan Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Sonuç Raporu sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1b3101bf-6712-40e5-ab49-6d93cdc0dab6)

Çoklu liste tipli parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4b58dd96-1ac5-4a15-931b-fd4a30198c57) (Ekle) butonu tıklanıldığında sistemde tanımlı Kök Neden listesi elemanlarından tekli ve çoklu seçim yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc790db7f-0998-49fe-984a-a9ad3c5a7bd2)

### **1.1.1.1.5.5.Personel Tipli Parametrik Alanların Listesi**

DÖF Modülünde Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Sonuç Raporu personel tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına personel yazarak personel tipli parametrik alanlar aratılır ve personel tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen personel tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbdc8d26f-ef11-401d-a985-dd29965e36d1)

### **1.1.1.1.5.6.Personel Tipli Parametrik Alan Tanımlama.**

lblS_PParam2 Personel tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb281623-1d3c-42f8-9520-b891d9c9d7e3) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload511965a3-fa01-43e3-8969-ab982ec4aa3c)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload339d9ded-c8ca-4211-8436-a79ed9a556f2)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d5e69d9-a38d-4f36-ae36-d5c8da9eb045)(kaydet) butonu tıklanarak personel tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada3397b95-899c-4625-aa1f-b01237681ec4)

Tanımlanan personel tipli parametrik alan Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Sonuç Raporu sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd28cfde0-7b2d-45a1-ae53-4aedab069e4e)

Personel tipli parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1f8c0d89-b0d1-4792-8b16-36a05706ba2a)(seç) butonu tıklanıldığında sistemde tanımlı personel listesinde seçim yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2bdad3ed-a142-4dba-b109-ee5821320548)

### **1.1.1.1.5.7.Sorgu Tipli Parametrik Alanların Listesi**

DÖF Modülünde Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Sonuç Raporu sekmesinde sorgu tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına sorgu yazarak sorgu tipli parametrik alanlar aratılır sorgu tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen sorgu tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8bd46fc6-7303-47a8-9979-63bc9e9c15b7)

### **1.1.1.1.5.8.Sorgu Tipli Parametrik Alan Tanımlama**

lblS_QParam1 Sorgu tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb281623-1d3c-42f8-9520-b891d9c9d7e3) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9b871416-e4d5-4674-ad89-c696852f839a)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0ed8f7b8-832b-4d4f-b861-75da4b9881d4)

Bimser Destek ekibi tarafından gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d5e69d9-a38d-4f36-ae36-d5c8da9eb045)(kaydet) butonu tıklanarak Sorgu tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload49bfed7d-fc8b-4b58-aa56-2d278b5a0212)

Tanımlanan sorgu tipli parametrik Alan Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Sonuç Raporu sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4fb12ef1-b229-4937-acde-f5224899ffd6)

Sorgu tipli parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2bc51caf-987c-4d34-80e2-8fc7719a7cf2) (Ekle) butonu tıklanıldığında sistemde tanımlı Pozisyon listesinde tekli ve çoklu seçim yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd5792c53-793d-404b-937d-9ef42e43a1c0)

### **1.1.1.1.5.9.Metin Tipli Parametrik Alanların Listesi**

DÖF Modülünde Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Sonuç Raporu sekmesinde metin tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına metin yazarak metin tipli parametrik alanlar aratılır metin tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen metin tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadeb7b5cef-915b-4e0a-8757-bdacac16b5ad)

### **1.1.1.1.5.10.Metin Tipli Parametrik Alan Tanımlama**

lblS_Param2 Metin tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb281623-1d3c-42f8-9520-b891d9c9d7e3) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload27e27d0a-fad6-4e68-a6a2-a95c223df4f5)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7ff6ea2b-6410-4a21-a0c9-db908e2c76c9)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d5e69d9-a38d-4f36-ae36-d5c8da9eb045)(kaydet) butonu tıklanarak metin tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload35ae327d-4803-4cd4-91b1-9330035b79ab)

Tanımlanan metin tipli parametrik alan Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Sonuç Raporu sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload06f176f5-43aa-4508-9c83-1cca94e1da1a)

### **1.1.1.1.5.11.Ölçü Birimi Parametrik Alanların Listesi**

DÖF Modülünde Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Sonuç Raporu sekmesinde ölçü Birimi tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına ölçü Birimi yazarak ölçü Birimi tipli parametrik alanlar aratılır ölçü Birimi tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen ölçü Birimi tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadde06c4ce-2d7f-4d1d-8218-f483e31d7007)

### **1.1.1.1.5.12.Ölçü Birimi Parametrik Alan Tanımlama**

lblS_NParam3 Ölçü birimi tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb281623-1d3c-42f8-9520-b891d9c9d7e3) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9715f5b4-4d21-4400-a78c-27edeaa95a3b)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade913b56c-18cd-4f0a-8001-262637bf3e60)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d5e69d9-a38d-4f36-ae36-d5c8da9eb045)(Kaydet) butonu tıklanarak ölçü birimi tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7eec9445-11e4-4b3b-8dcf-3a50216a367e)

Tanımlanan ölçü birimi tipli parametrik alan Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Sonuç Raporu sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb505c6c3-582f-443d-a522-3ac3b5e90afe)

### **1.1.1.1.5.13.Parasal Tipli Parametrik Alanların Listesi**

DÖF Modülünde Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Sonuç Raporu sekmesinde parasal tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına parasal yazarak parasal tipli parametrik alanlar aratılır parasal tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen parasal tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload05b41e93-524d-4576-8b00-b64dba151024)

### **1.1.1.1.5.14.Parasal Tipli Parametrik Alan Tanımlama**

lblS_NParam1 Parasal tipli alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb281623-1d3c-42f8-9520-b891d9c9d7e3) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2366bad8-1557-4f8d-a966-f86996106120)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload336913e3-4460-4877-8b94-bcfd57e488d5)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d5e69d9-a38d-4f36-ae36-d5c8da9eb045)(Kaydet ) butonu tıklanarak Parasal tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3b4929bf-0740-47eb-97c0-d65e6f0ea133)

Tanımlanan parasal tipli parametrik alan Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Sonuç Raporu sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8286b6ea-c3c8-4ab4-b46e-117882f5ade4)

Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Sonuç Raporu sekmesinde

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade3c32973-b465-4402-b3fa-78ee3ed21d05)

### **1.1.1.1.6.Düzeltici ve Önleyici Faaliyetler Modülünde Kapatma Sekmesinde Parametrik Alan Tipi  Tanımlaması**

Düzeltici ve Önleyici Faaliyetler Modülünde Kapatma sekmesinde tanımlanan parametrik alanların kısa kodları lblK\_ başlığı ile tanımlı kısa kodlardır. lblK\_ başlığındaki kısa kodlar olan tüm parametrik tipli alanlar tanımlandığında Düzeltici ve Önleyici Faaliyetler Modülünde Kapatma sekmesi ekranında görüntülenir.

### **1.1.1.1.6.1.Liste Tipli Parametrik Alanların Listesi**

DÖF Modülünde Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Kapatma sekmesinde liste tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına liste yazarak liste tipli parametrik alanlar aratılır liste tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen liste tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8ec397a7-c6cd-4353-8cf6-b0241b4aec25)

### **1.1.1.1.6.2.Liste Tipli Parametrik Alan Tanımlama.**

lblK_LParam2 Liste tipli parametrik seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb281623-1d3c-42f8-9520-b891d9c9d7e3) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade3638b2d-0ce1-4308-a3dc-501428a843cb)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaf073bb4-4c3a-4c4f-bbd9-092f257661ca)

Liste tipli alanın liste değerlerini girmek için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload66f97ccb-fbe8-4710-a3b3-45eb91116899) (Yeni) butonuna tıklanır, liste değerleri yazılır ve kaydedilir. Liste elaman değeri 1 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4724c5b9-2362-4078-bdff-fe846e863266)

Liste eleman değeri 2 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload24db8921-71f4-41d2-a2f4-c9107f033c38)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb04677ef-0929-4e19-9fe1-d54b6d1eac75)

Alanın zorunlu olup, olmayacağı sıra no bilgisi ve liste elemanları tanımlanarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d5e69d9-a38d-4f36-ae36-d5c8da9eb045)(kaydet) butonu tıklanarak liste tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd29e981f-d5f8-4d28-b15a-57c1882be6c2)

Tanımlanan liste tipli parametrik alan Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Kapatma sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload75e7728f-b865-4017-a51d-db27e0aed0e5)

### **1.1.1.1.6.3.Personel Tipli Parametrik Alanların Listesi**

DÖF Modülünde Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Kapatma sekmesinde personel tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına personel yazarak personel tipli parametrik alanlar aratılır personel tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen personel tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2b0aff0a-6924-41af-8758-bd355c87d614)

### **1.1.1.1.6.4.Personel Tipli Parametrik Alan Tanımlama**

lblK_PParam2 Personel tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb281623-1d3c-42f8-9520-b891d9c9d7e3) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload37dd464d-ff01-4b18-a33f-b1b74fca30ef)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd1732313-4ee4-4e33-a58d-dd105153db84)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d5e69d9-a38d-4f36-ae36-d5c8da9eb045)(kaydet) butonu tıklanarak personel tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf5fc4d88-bf67-4a9d-ae23-8e7d0f431323)

Tanımlanan personel tipli parametrik alan Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Kapatma sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4c2e567a-eb3a-4bc5-80bc-a0bf21d516b0)

Personel tipli parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1f8c0d89-b0d1-4792-8b16-36a05706ba2a)(seç) butonu tıklanıldığında sistemde tanımlı personel listesinde seçim yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload42f18bcf-704a-4954-bf1f-7aeda29f03c0)

### **1.1.1.1.6.5.Sorgu Tipli Parametrik Alanların Listesi**

DÖF Modülünde Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Kapatma sekmesinde sorgu tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına sorgu yazarak sorgu tipli parametrik alanlar aratılır sorgu tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen sorgu tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadac380a9b-02cd-4656-a8d1-ee18c9be0240)

### **1.1.1.1.6.6.Sorgu Tipli Parametrik Alan Tanımlama**

lblK_QParam1 Sorgu tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb281623-1d3c-42f8-9520-b891d9c9d7e3) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc6a4e913-923c-43d5-a086-eea1b9cc4ccc)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddcfa43f0-b44b-4d07-80cd-c015d0925d4f)

Bimser Destek ekibi tarafından destek alınarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d5e69d9-a38d-4f36-ae36-d5c8da9eb045)(kaydet) butonu tıklanarak Sorgu tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0a096d20-e703-4077-93fc-f219b72048ce)

Tanımlanan sorgu tipli parametrik alan Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Kapatma sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload67c6f140-18c0-4501-b167-373eac9eb834)

Sorgu tipli parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1f8c0d89-b0d1-4792-8b16-36a05706ba2a)(seç) butonu tıklanıldığında sistemde tanımlı Departman listesinde seçim yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc22b5a2a-3f47-4808-8b9d-1d0db082bcac)

### **1.1.1.1.6.7.Metin Tipli Parametrik Alanların Listesi**

DÖF Modülünde Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Kapatma sekmesinde metin tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına metin yazarak metin tipli parametrik alanlar aratılır metin tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen metin tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload07c46fe9-316c-4c6c-a722-d488dfe860f8)

### **1.1.1.1.6.8.Metin Tipli Parametrik Alan Tanımlama**

lblK_Param2 Metin tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb281623-1d3c-42f8-9520-b891d9c9d7e3) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd24304d5-8452-41a4-a6ad-57d7addd2e8e)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf5be19b2-4f46-4f41-ab65-363383ed9270)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d5e69d9-a38d-4f36-ae36-d5c8da9eb045)(kaydet) butonu tıklanarak metin tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb96c9002-ae12-4c2a-877a-4d334fe09582)

Tanımlanan metin tipli parametrik alan Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Kapatma sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8f108957-72bc-4015-887c-a4d4de09fc9b)

### **1.1.1.1.6.9.Ölçü Birimi Parametrik Alanların Listesi**

DÖF Modülünde Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Kapatma sekmesinde ölçü Birimi tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına ölçü Birimi yazarak ölçü Birimi tipli parametrik alanlar aratılır ölçü Birimi tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen ölçü Birimi tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload22e2ccab-185e-4c20-80cd-e1b9689b0355)

### **1.1.1.1.6.10.Ölçü Birimi Parametrik Alan Tanımlama**

lblK_NParam3 Ölçü birimi tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb281623-1d3c-42f8-9520-b891d9c9d7e3) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload72245d5d-a15e-4b43-a97f-4659762d4036)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddf6dbed8-5656-4a58-8850-f1fed7bcbc93)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d5e69d9-a38d-4f36-ae36-d5c8da9eb045)(Kaydet) butonu tıklanarak ölçü birimi tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload90a6fabc-5753-498c-b29a-bef268cbaf47)

Tanımlanan ölçü birimi tipli parametrik Alan Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Kapatma sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada277d7e4-7936-4bd7-82b4-e33bde0d133b)

### **1.1.1.1.6.11.Parasal Tipli Parametrik Alanların Listesi**

DÖF Modülünde Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Kapatma sekmesinde parasal tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına parasal yazarak parasal tipli parametrik alanlar aratılır parasal tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen parasal tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9892c8ce-eb4a-41a1-951d-48ba13e24f8d)

### **1.1.1.1.6.12.Parasal Tipli Parametrik Alan Tanımlama**

lblK_NParam1 Parasal tipli alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb281623-1d3c-42f8-9520-b891d9c9d7e3) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload71fe5b57-9499-4e85-98cf-e0808ab69a19)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade205e0d4-e1a8-40c3-a13a-804e2f4fe8ef)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d5e69d9-a38d-4f36-ae36-d5c8da9eb045)(Kaydet ) butonu tıklanarak parasal tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload525b1935-d7df-4324-9210-44b18272df88)

Tanımlanan parasal tipli parametrik alan Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Kapatma sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload09137cc8-3ea5-46b6-8047-d4f71751751d)

Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Kapatma sekmesinde tanımlanan tüm parametrik alanlar;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadffd7b275-9ab1-4d3b-8cf7-d23c9279f212)

### **1.1.1.1.7. Dil ayarlarında Tanımlan Parametrik Alan tipleri Görüntülen Ekrandan Kaldırma İşlemi**

1.Aşamada parametrik alanın bulunduğu ekran açılır. DÖF Modülünde Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Kapatma sekmesinde görüntülenir

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload66705917-3abf-4e63-bb3b-be2ab191748b)

2\. Aşamada Parametrik Alanın bulunduğu ekran görüntülendikten sonra örnekteki herhangi alan seçilerek, Sağ tıkla/Kopyala komutu ile parametrik alanın ismi kopyalanır. Örnek:DÖF Kapama Dosya Türü.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9e024b99-bdd1-4295-b0e3-56543412a4a1)

3\. Aşamada Sistem Altyapı Tanımları\>BSAT\>Konfigürasyon Ayarları\>Dil ayarları menüsü tıklanarak açılan ekranda Modül olarak Düzeltici ve Önleyici Faaliyetler Modülü seçilir. Kopyalanan Dil ayarlarından tanımlanan liste tipli parametrik alanı grid ekranında **TR** alanına sağ tıkla/yapıştır komutu ile alanın yapıştırma işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload518d11ec-212b-4234-8e6d-127d3412097f)

4.Aşamada liste tipli tipli parametrik alan seçilerek alanın içeriği görüntülemek için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb281623-1d3c-42f8-9520-b891d9c9d7e3) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbcf98d41-1974-4f9f-972f-5e679be943d0)

5.Aşamada içeriği görüntülen liste tipli alanın değeri ve liste elemanları kısımları silerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d5e69d9-a38d-4f36-ae36-d5c8da9eb045)(Kaydet) butonu tıklanarak Dil Ayarları menüsünde tanımlı liste tipli alanın kaldırma işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7e772009-47ea-475b-b323-d4d0abe70b02)

Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarlarında tanımlanan diğer parametrik alan tiplerin dil ayarları menüsünde kaldırma işlemi aynı şekilde olmaktadır. DÖF Modülünde Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Kapatma sekmesinde tanımlı liste tipli alanın kaldırılmış olduğu görülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload60b45776-db8f-46c9-94d1-6c4ec6e28e7d)
