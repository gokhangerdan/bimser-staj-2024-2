---
title: Parametrik Alan Tanımlama İşlemi
description: Parametrik Alan Tanımlama İşlemi Yardım Dokümanı
sidebar_position: 1
---

:::tip Bilgi

İlgili konu başlığına sağ tarafta bulunan navigasyon yardımıyla hızlı bir şekilde ulaşabilirsiniz.

:::


**Öneri Sistemi Modülünde** **Dil Ayarları Menüsünde Parametrik Alan Tanımlama Kullanıcı Yardım Dokümanı**


# **1.Sistem Altyapı Tanımları**

Personel bilgilerinin tanımlandığı ve diğer modüller için gerekli olan altyapının kurgulanmasının yapıldığı menüdür.

## **1.1.Konfigürasyon Ayarları**

**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları

QDMS sisteminde özel ayarların yapıldığı menülerdir. Bu menülerde yapılan ayarlar tüm QDMS kullanıcıları için geçerli olan ortak ayarlardır.

### **1.1.1. Dil Ayarları**

**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları

Dil ayarları menüsünden QDMS üzerinde görülen menülerin isimleri, alanların isimleri değiştirilebilir. Modüllere yeni alanlar eklenebilir. Var olan alanların zorunluluk durumları düzenlenebilir. Alanların ekran üzerinde göründükleri sıralama değiştirilebilir.

### **1.1.1.1.Öneri Sistemi Modülü Ortak Kullanım İçin Yeni Alan Oluşturma**

Öneri Sistemi Modülünde Öneri Girişi menüsü, Öneri Uzman Değerlendirme ve Kazanç Maliyet aşamalarında firmanın istemiş olduğu sistemde olmayan ekstradan alanlar tanımlanabilir. Tanımlanan bu alanlar tüm Öneri Sistemi Modülü kaynakları için geçerlidir. Sistem Altyapı Tanımları/BSAT/ Konfigürasyon Ayarları/Dil Ayarları menüsü tıklanılır. Açılan Dil Ayarları sayfasında Modül alanında “Öneri Sistemi ” seçilir ve ekranda Öneri Sistemi Modülü ile ilgili dil tanımları görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc8f5d94e-468a-4f4c-b7a2-ce31f8f31ca7)

Öneri Sistemi Modülünde Entegre Yönetim Sistemi\>Öneri Sistemi\>Öneri Girişi menüsü tıklatıldığında açılan Öneri Tanımlama ekranında Öneri bilgileri sekmesinde parametrik tipli alanların tanımlanması Dil ayarları menüsünden yapılmaktadır. Öneri girişi menüsünde Dil ayarlarında tanımlanan bu alanların Tarih, Liste, Parasal ve Ölçü Birimi parametrik alan tipleri Öneri Uzman Değerlendirme aşamasında açılan ekranda görüntülenmektedir. Öneri Girişi menüsü ile ortak tanımlanan parametrik alan tipleridir. Metin tipli alan tanımlaması sadece Öneri Uzman Değerlendirme aşaması için Dil ayarlarında ayrı bir şekilde yapılmaktadır. Öneri Modülün Kazanç- Maliyet aşamasında dil ayarlarında parametrik alan tipleri tanımlaması ayrı bir şekilde yapılmaktadır. Kazanç/Maliyet aşaması için tanımlanan parametrik alanlar açılan Kazanç /Maliyet Tanımları ekranında Diğer alanlar sekmesinde görüntülenir. Bu aşamalarda parametrik tipli alanlarda kullanılan kısa kodlar bulunmaktadır. Hangi aşamada hangi kısa kodlar kullanılmış ayırt etmek mümkündür. Parametrik tipli alanlarda hangi aşamada olduğunun ayırt etmek için aşağıdaki kısa kodların başlama kısımlarına dikkate etmek gerekir;

**Öneri Girişi:** lblPARAM1 kısa kodları genelde Entegre Yönetim Sistemi\>Öneri Sistemi\>Öneri Girişi menüsünde açılan Öneri Tanımlama ekranında Öneri Bilgileri sekmesinde görüntülen parametrik alanları temsil eder.

**Uzman Değerlendirme :** lblPARAM1 kısa kodları genelde Öneri Uzman Değerlendirme aşamasında görüntülen parametrik alanları temsil eder. Bu aşamada Tarih, Liste, Parasal, Ölçü ve Metin tipli parametrik alanlar dil ayarlarında tanımlanarak görüntülenir.

**Kazanç/Maliyet:** lblKM_PARAM1, lblKM\_ ile başlayan kısa kodları genelde önerin Kazanç/Maliyet aşamasında açılan Kazanç/Maliyet Tanımları ekranında Diğer Alanlar sekmesinde görüntülen parametrik alanları temsil eder.

**Öneri Sistemi Modülünde Tanımlanan Parametrik Tipli Alanlar ve Tanımları;**

**1-Tarih tipli**: Takvim alanı eklenilen parametrik alandır. Örnek Kısa Kod: lblDPARAM1(Öneri Girişi menüsünde açılan Öneri Tanımlama ekranında Öneri Bilgileri sekmesinde görüntülenir.), (Öneri Uzman Değerlendirme aşaması ekranında Öneri Onayı sekmesinde görüntülenir)

**2-Liste tipli**: Birden fazla liste elemanları arasından tek seçim yapılan parametrik alandır. Liste elemanları tanımlanarak, tanımlanan liste elemanlarında seçip yapılır. Örnek Kısa Kod: lblLPARAM2 (Öneri Girişi menüsünde açılan Öneri Tanımlama ekranında Öneri Bilgileri sekmesinde görüntülenir.), (Öneri Uzman Değerlendirme aşaması ekranında Öneri Onayı sekmesinde görüntülenir)

**3-Personel Tipli:** QDMS personel veri tabanından kişi seçilebilmesini sağlayan parametrik alandır. Sistem Altyapı Tanımları\>Bsat\>Tanımlama\>Personel Tanımlama menüsünde tanımlı olan Personellerin listesinde seçim yapılır. Örnek Kısa Kod: lblPPARAM1(Öneri Girişi menüsünde açılan Öneri Tanımlama ekranında Öneri Bilgileri sekmesinde görüntülenir.)

**4-Sorgu tipli:** QDMS/Ensemble veri tabanları içerisindeki ana verilerden seçim yapılabilmesi için tanımlanabilen alan türüdür. (Sadece Bimser Destek Ekibi tarafından tanımlanmalıdır) Tekli ve çoklu seçim yapılabilir. Örnek Kısa Kod: lbl_QPARAM1 (Öneri Girişi menüsünde açılan Öneri Tanımlama ekranında Öneri Bilgileri sekmesinde görüntülenir.)

**5-Metin tipli**: Elle yazım imkanı veren metin kutucuğu ekleyen parametrik alandır. Örnek Kısa Kod: lblPARAM2 (Öneri Uzman Değerlendirme aşaması ekranında Öneri Onayı sekmesinde görüntülenir)

**6-Personel (Çoklu Satır) Tipli**: QDMS personel veri tabanından tekli ve çoklu kişi seçilebilmesini sağlayan parametrik alandır. Sistem Altyapı Tanımları\>Bsat\>Tanımlama\>Personel Tanımlama menüsünde tanımlı olan Personellerin listesinde seçim yapılır. Örnek Kısa Kod: lblPMPARAM1(Öneri Girişi menüsünde açılan Öneri Tanımlama ekranında Öneri Bilgileri sekmesinde görüntülenir.)

**7- Departman Tipli:** QDMS departman veri tabanından departman bilgisi seçilebilmesini sağlar. Sistem Altyapı Tanımları\>Bsat\>Tanımlama\>Departman Tanımlama menüsünde tanımlı olan Departman listesinde seçim yapılır. Örnek Kısa Kod: lblDSPARAM1(Öneri Girişi menüsünde açılan Öneri Tanımlama ekranında Öneri Bilgileri sekmesinde görüntülenir.)

**8- Departman(Çoklu Seçim):** QDMS departman veri tabanından departman bilgisi tekli ve çoklu seçilebilmesini sağlar. Sistem Altyapı Tanımları\>Bsat\>Tanımlama\>Departman Tanımlama menüsünde tanımlı olan Departman listesinde seçim yapılır. Örnek Kısa Kod: lblDMPARAM1 (Öneri Girişi menüsünde açılan Öneri Tanımlama ekranında Öneri Bilgileri sekmesinde görüntülenir.)

**9**-**Parasal Tipli:** Parasal olarak veri girişi yaptıran parametrik alandır. Tanımlanan parametrik alanın yanında para birimleri seçildiği alan çıkar. Para birimleri seçim alanındaki para birimleri Sistem Altyapı Tanımları\>BSAT\>Tanımlar\>Para Birimleri Tanımlama menüsünde tanımlı olan para birimleridir. Örnek Kısa Kod: lblNPARAM1(Öneri Girişi menüsünde açılan Öneri Tanımlama ekranında Öneri Bilgileri sekmesinde görüntülenir.), (Öneri Uzman Değerlendirme aşaması ekranında Öneri Onayı sekmesinde görüntülenir)

**10- Ölçü Birimi Tipli:** Ölçü olarak veri girişi yaptıran parametrik alandır. Tanımlanan parametrik alanın yanında Ölçü birimleri seçildiği alan çıkar. Ölçü birimleri seçim alanındaki ölçü Birimleri Sistem Altyapı Tanımları\>BSAT\>Tanımlar\>Ölçü Birimleri Tanımlama menüsünde tanımlı olan ölçü birimleridir. Örnek Kısa Kod: lblNPARAM6 (Öneri Girişi menüsünde açılan Öneri Tanımlama ekranında Öneri Bilgileri sekmesinde görüntülenir.), (Öneri Uzman Değerlendirme aşaması ekranında Öneri Onayı sekmesinde görüntülenir)

### **1.1.1.1.1. Öneri Sistemi  Modülünde Öneri Girişi Menüsü ve Öneri Uzman Değerlendirme Aşamasında Parametrik Alan Tanımlaması**

Öneri Sistemi Modülünde Öneri Girişi Menüsü açılan Öneri Tanımlama ekranında Öneri Bilgileri sekmesinde ve Öneri uzman Değerlendirme aşamasında Öneri Onayı sekmesinde tanımlanan parametrik alanların kısa kodları lblPARAM başlığı ile tanımlı kısa kodlardır. lblPARAM başlığındaki kısa kodlar olan tüm parametrik tipli alanlar tanımlandığında Öneri Sistemi Modülünde Öneri Tanımlama ekranında Öneri Bilgileri sekmesinde görüntülenir. Öneri Uzman Değerlendirme aşamasında Öneri Girişi ile ortak olarak Tarih, Liste, Parasal ve ölçü tipi parametrik alanlar dil ayarları menüsünde tanımlanır. Metin tipli parametrik alan sadece Öneri Uzman Değerlendirme aşaması için Dil Ayarlarında tanımlanan ortak alan değildir.

#### **1.1.1.1.1.1.Tarih Tipli Parametrik Alanların Listesi**

Öneri Sistemi Modülünde Öneri Girişi menüsünde açılan Öneri Tanımlama ekranında Öneri Bilgileri sekmesinde Tarih tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Tarih yazarak Tarih tipli parametrik alanlar aratılır ve Tarih tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen tarih tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4602703d-454a-47dd-8346-9eb6096871b9)

#### **1.1.1.1.1.2.Tarih Tipli Parametrik Alan Tanımlama**

lblDPARAM1 Tarih tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload824e1f9c-4e7f-4f5e-a883-311cd629857a) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfea97e47-81ff-4bcd-98a4-57c024456a27)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload63159f96-44e6-4783-b731-1c351f3520e7)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadca9b6a36-8811-49eb-969f-c1c40557abc7)(Kaydet) butonu tıklanarak tarih tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0b61eae5-35da-4460-9536-2929a47202c0)

Tanımlanan Tarih tipli parametik alan Öneri Sistemi Modülünde Öneri Girişi Menüsü açılan Öneri Tanımlama ekranında Öneri Bilgileri sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf4e46efa-8f08-4942-9192-c899b053205e)

#### **1.1.1.1.1.3.Liste Tipli Parametrik Alanların Listesi**

Öneri Sistemi Modülünde Öneri Girişi menüsünde açılan Öneri Tanımlama ekranında Öneri Bilgileri sekmesinde Liste tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Liste yazarak Liste tipli parametrik alanlar aratılır ve Liste tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Liste tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3c54567d-0fcc-44d8-bda3-bf129acacb00)

#### **1.1.1.1.1.4.Liste Tipli Parametrik Alan Tanımlama**

lblLPARAM2 Liste tipli parametrik seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload824e1f9c-4e7f-4f5e-a883-311cd629857a) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload74dadcf6-d6a3-4db0-9484-1302cf694cf4)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload04db5a00-eb32-433f-998b-5e316cc960b5)

Liste tipli alanın liste değerlerini girmek için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1160d295-2b0a-4ae7-82aa-f685f95633a6) (Yeni) butonuna tıklanır, liste değerleri yazılır ve kaydedilir. Liste eleman değeri 1 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc31ed8f6-5e88-4102-9a18-f632e3760631)

Liste eleman değeri 2 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3a7129e0-028b-4c49-9976-086440a06b96)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload721dc416-def0-46cc-a4be-568b07a0f821)

Alanın zorunlu olup, olmayacağı sıra no bilgisi, liste elemanları tanımlanarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadca9b6a36-8811-49eb-969f-c1c40557abc7)(kaydet) butonu tıklanarak liste tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9ca1ef12-035a-4109-9f6b-50f1c89a788e)

Tanımlanan Liste tipli parametik alan Öneri Sistemi Modülünde Öneri Girişi Menüsü açılan Öneri Tanımlama ekranında Öneri Bilgileri sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2facb9c9-f0c3-4755-a32d-9bca2c941ed7)

#### **1.1.1.1.1.5.Personel Tipli Parametrik Alanların Listesi**

Öneri Sistemi Modülünde Öneri Girişi menüsünde açılan Öneri Tanımlama ekranında Öneri Bilgileri sekmesinde Personel tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Personel yazarak Personel tipli parametrik alanlar aratılır ve Personel tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Personel tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload42934275-e39a-475d-93d5-e2335a70b39c)

#### **1.1.1.1.1.6.Personel Tipli Parametrik Alan Tanımlama**

lblPPARAM1 Personel tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload824e1f9c-4e7f-4f5e-a883-311cd629857a) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd37496ac-f997-400f-9cd9-17bf049d9f80)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadde614e75-ffd4-4359-bc77-ff62d16c3c48)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadca9b6a36-8811-49eb-969f-c1c40557abc7)(kaydet) butonu tıklanarak Personel tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2e0dfcac-0b56-4cd4-b8b7-ddc06a930e61)

Tanımlanan Personel tipli parametik alan Öneri Sistemi Modülünde Öneri Girişi Menüsü açılan Öneri Tanımlama ekranında Öneri Bilgileri sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2a9bcbd1-fe91-4837-947d-c6a66d2878de)

Personel tipli parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload34ebaa9f-c31f-4932-8e9c-bfeca35f9c30)(seç) butonu tıklanıldığında sistemde tanımlı personel listesinde seçim yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8127e427-d768-44af-8c0d-8eb4df87ddd0)

#### **1.1.1.1.1.7.Sorgu Tipli Parametrik Alanların Listesi**

Öneri Sistemi Modülünde Öneri Girişi menüsünde açılan Öneri Tanımlama ekranında Öneri Bilgileri sekmesinde Sorgu tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Sorgu yazarak Sorgu tipli parametrik alanlar aratılır ve Sorgu tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Sorgu tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadda78d658-b8c1-4eb7-aa3a-ac22e609846b)

#### **1.1.1.1.1.8.Sorgu Tipli Parametrik Alan Tanımlama**

lbl_QPARAM1 Sorgu tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload824e1f9c-4e7f-4f5e-a883-311cd629857a) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb76a9365-770d-42ea-9ace-7cb63de9b43b)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade8e94836-c635-4aab-90cb-712932009ab0)

Bimser Destek ekibinde yardım alınarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadca9b6a36-8811-49eb-969f-c1c40557abc7)(kaydet) butonu tıklanarak Sorgu tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload42117a51-e209-43dd-bb67-edecf7617d83)

Tanımlanan Sorgu tipli parametik alan Öneri Sistemi Modülünde Öneri Girişi Menüsü açılan Öneri Tanımlama ekranında Öneri Bilgileri sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada12b2d81-850e-4df0-ac59-5edb1b51b2ba)

Sorgu tipli parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload53760b36-b738-495c-8cd5-f86a5e031de2) (Seç) butonu tıklanıldığında sistemde tanımlı Pozisyon listesinde seçim yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb774bf1-49a2-4c57-8db4-a3441d1a8b49)

#### **1.1.1.1.1.9.Ölçü Birimi Parametrik Alanların Listesi**

Öneri Sistemi Modülünde Öneri Girişi menüsünde açılan Öneri Tanımlama ekranında Öneri Bilgileri sekmesinde Ölçü Birimi tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Ölçü Birimi yazarak Ölçü Birimi tipli parametrik alanlar aratılır ve Ölçü Birimi tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Ölçü Birimi tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload527456a0-37a7-4979-b09a-231419ada943)

#### **1.1.1.1.1.10.Ölçü Birimi Parametrik Alan Tanımlama**

lblNPARAM6 Ölçü birimi tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload824e1f9c-4e7f-4f5e-a883-311cd629857a) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd8075d44-246d-4555-a79b-5887578e7851)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc33b7a58-b038-4024-9ca2-b4cf8010b50f)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadca9b6a36-8811-49eb-969f-c1c40557abc7)(Kaydet) butonu tıklanarak ölçü birimi tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf8d342fd-bc2a-4d28-b09d-0c463782ab36)

Tanımlanan Ölçü birimi tipli parametik alan Öneri Sistemi Modülünde Öneri Girişi Menüsü açılan Öneri Tanımlama ekranında Öneri Bilgileri sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5d6a139c-9eba-42bc-b8a1-b6fa3f5a2414)

#### **1.1.1.1.1.11.Parasal Tipli Parametrik Alanların Listesi**

Öneri Sistemi Modülünde Öneri Girişi menüsünde açılan Öneri Tanımlama ekranında Öneri Bilgileri sekmesinde Parasal tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Parasal yazarak Parasal tipli parametrik alanlar aratılır ve Parasal tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Parasal tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload832b8968-1ac1-4e13-99c4-d5492d470811)

#### **1.1.1.1.1.12.Parasal Tipli Parametrik Alan Tanımlama**

lblNPARAM1 Parasal tipli alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload824e1f9c-4e7f-4f5e-a883-311cd629857a) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0cca1359-1d55-4918-aacb-dee491da5005)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada1643d36-aebe-4606-90fb-421bd22d8a04)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadca9b6a36-8811-49eb-969f-c1c40557abc7)(Kaydet ) butonu tıklanarak Parasal tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload872b6112-e34f-4022-9838-312da59e4f23) Tanımlanan Parasal tipli parametik alan Öneri Sistemi Modülünde Öneri Girişi Menüsü açılan Öneri Tanımlama ekranında Öneri Bilgileri sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0f33603b-3573-4e29-af88-dd6dbc0fe705)

#### **1.1.1.1.1.13.Departman Tipli Parametrik Alanların Listesi**

Öneri Sistemi Modülünde Öneri Girişi menüsünde açılan Öneri Tanımlama ekranında Öneri Bilgileri sekmesinde Departman tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Departman yazarak Departman tipli parametrik alanlar aratılır ve Departman tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Departman tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload216a8d67-6c9b-42f3-a268-a2dbf7925fae)

#### **1.1.1.1.1.14.Departman Tipli Parametrik Alan Tanımlama**

lblDSPARAM1 Departman tipli alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload824e1f9c-4e7f-4f5e-a883-311cd629857a) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddfe78b95-8032-4929-9c5c-0bdaa82bba99)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload42dc93f1-28e2-43fc-ac05-f02d7c365f0b)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadca9b6a36-8811-49eb-969f-c1c40557abc7)(Kaydet ) butonu tıklanarak Departman tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf08e233a-f2f7-4b5b-a6db-2c36ef36d7d4)

Tanımlanan Departman tipli parametik alan Öneri Sistemi Modülünde Öneri Girişi Menüsü açılan Öneri Tanımlama ekranında Öneri Bilgileri sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade8b1c138-da5c-48f6-9f11-930b1857da4d)

Departman tipli parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload34ebaa9f-c31f-4932-8e9c-bfeca35f9c30)(seç) butonu tıklanıldığında sistemde tanımlı Departman listesinde seçim yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4bac1c6f-605f-42a9-8be3-e776f414f72b)

#### **1.1.1.1.1.15. Departman(Çoklu Seçim) Tipli Parametrik Alanların Listesi**

Öneri Sistemi Modülünde Öneri Girişi menüsünde açılan Öneri Tanımlama ekranında Öneri Bilgileri sekmesinde Departman(Çoklu Seçim) tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Departman(Çoklu Seçim) yazarak Departman(Çoklu Seçim)l tipli parametrik alanlar aratılır ve Departman(Çoklu Seçim) tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Departman(Çoklu Seçim) tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7152b401-ca0e-4346-aae2-78777ba1fbb4)

#### **1.1.1.1.1.16.Departman(Çoklu Seçim) Tipli Parametrik Alan Tanımlama**

lblDMPARAM1 Departman(Çoklu Seçim) tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload824e1f9c-4e7f-4f5e-a883-311cd629857a) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload49ceb1ca-b1cc-4ef3-914c-6fb03619e7b2)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload130b41ab-de39-4afd-b391-587ad1ed2464)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadca9b6a36-8811-49eb-969f-c1c40557abc7)(kaydet) butonu tıklanarak Departman(Çoklu Seçim) tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload333d6e30-b43b-4397-b550-36baebce4f16)

Tanımlanan Departman(Çoklu Seçim) tipli parametik alan Öneri Sistemi Modülünde Öneri Girişi Menüsü açılan Öneri Tanımlama ekranında Öneri Bilgileri sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7f6f6912-8dc5-45ce-885e-f0049fcf4e14)

Departman(Çoklu Seçim) tipli parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9848c5b2-b19c-4810-80dd-c02d24c19593) (Ekle) butonu tıklanıldığında sistemde tanımlı departman listesinde tekli ve çoklu seçim yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1d88db99-d03e-4c26-b253-2132cb1ef40f)

#### **1.1.1.1.1.17.Personel(Çoklu Seçim) Tipli Parametrik Alanların Listesi**

Öneri Sistemi Modülünde Öneri Girişi menüsünde açılan Öneri Tanımlama ekranında Öneri Bilgileri sekmesinde Personel(Çoklu Seçim) tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Personel(Çoklu Seçim) yazarak Personel(Çoklu Seçim) tipli parametrik alanlar aratılır ve Personel(Çoklu Seçim) tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Personel(Çoklu Seçim)  tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload72be84ab-4b68-44ae-88a9-05cb23160ed5)

#### **1.1.1.1.1.18.Personel(Çoklu Seçim) Tipli Parametrik Alan Tanımlama**

lblPMPARAM1 Personel(Çoklu Seçim) tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload824e1f9c-4e7f-4f5e-a883-311cd629857a) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5e00a114-56ec-43c3-abb7-f28965754419)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3e8fc748-c0cd-454b-8824-66c81c8c805a)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadca9b6a36-8811-49eb-969f-c1c40557abc7)(kaydet) butonu tıklanarak Personel(Çoklu Seçim) tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8818aa1b-9074-46ba-8aeb-63349533ecb5)

Tanımlanan Personel(Çoklu Seçim) tipli parametik alan Öneri Sistemi Modülünde Öneri Girişi Menüsü açılan Öneri Tanımlama ekranında Öneri Bilgileri sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3d3088ee-54ee-4776-bed4-1dde40aea259)

Personel(Çoklu Seçim) tipli parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbf7f7c86-0a1c-4e26-b805-3eb1f7fdaacf)(Ekle) butonu tıklanıldığında sistemde tanımlı personel listesinde tekli ve çoklu seçim yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6ac72aa2-f6d5-452e-acf8-e6b8353af076)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload95fe576d-7b30-4e85-a209-27a8a880365e)(Seç) butonu tıklanıldığında ise sistemde tanımlı kullanıcı Grubu listesinde seçim yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbcc58c32-9450-4881-85d5-90ad1eae2f88)

Öneri Sistemi Modülünde Öneri Girişi Menüsü açılan Öneri Tanımlama ekranında Öneri Bilgileri sekmesinde tanımlanan tüm alanlar;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf4720806-12ba-402c-8988-6c160c88a4af)

Dil ayarlarında tanımlanan bu alanların Tarih, Liste, Parasal ve Ölçü Birimi parametrik alan tipleri ayrıca Öneri Uzman Değerlendirme aşamasında açılan ekranda görüntülenmektedir. Ortak Tanımlanan parametrik alan tipleridir.Metin Tipli Alan tanımlaması sadece Öneri Uzman Değerlendirme aşaması için Dil ayarlarında ayrı bir şekilde yapılmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfd87b15f-20b9-46e5-bfa5-a6b6a7bfd003)

### **1.1.1.1.2.Öneri Sistemi Modülünde Kazanç /Maliyet aşamasında Diğer Alanlar sekmesinde Parametrik Alan Tipi Tanımlaması**

Öneri Sistemi Modülünde Önerinin Kazanç Maliyet aşamasında iken Kazanç /Maliyet Tanımları ekranında Diğer alanlar sekmesinde dil ayarlarında tanımlanan parametrik alanların kısa kodları lblKM\_ başlığı ile tanımlı kısa kodlardır. lblKM\_ başlığındaki kısa kodlar olan tüm parametrik tipli alanlar tanımlandığında Öneri Sistemi Modülünde Önerinin Kazanç Maliyet aşamasında iken Kazanç /Maliyet Tanımları ekranında Diğer Alanlar sekmesinde ekranında görüntülenir.

#### **1.1.1.1.2.1.Tarih Tipli Parametrik Alanların Listesi**

Öneri Sistemi Modülünde Önerinin Kazanç Maliyet aşamasında iken Kazanç /Maliyet Tanımları ekranında Diğer Alanlar sekmesinde Tarih tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Tarih yazarak Tarih tipli parametrik alanlar aratılır ve Tarih tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen tarih tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload73f16f3c-1826-4c31-84b4-0074d80863a1)

#### **1.1.1.1.2.2.Tarih Tipli Parametrik Alan Tanımlama**

lblKM_DPARAM1 Tarih tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload824e1f9c-4e7f-4f5e-a883-311cd629857a) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload73eb0a38-da2b-4e82-ab15-5195df9cdf3a)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload569cd4ad-674c-4e0c-b0b2-0f49e90cae03)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadca9b6a36-8811-49eb-969f-c1c40557abc7)(Kaydet) butonu tıklanarak tarih tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6c423362-a2a4-4b1b-ac03-78e37c5db653)

Tanımlanan Tarih tipli parametik alan Öneri Sistemi Modülünde Önerinin Kazanç Maliyet aşamasında iken Kazanç /Maliyet Tanımları ekranında Diğer Alanlar sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4f7ab2eb-ddd0-445b-92cd-26763f9fc02d)

#### **1.1.1.1.2.3.Liste Tipli Parametrik Alanların Listesi**

Öneri Sistemi Modülünde Önerinin Kazanç Maliyet aşamasında iken Kazanç /Maliyet Tanımları ekranında Diğer Alanlar sekmesinde Liste tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Liste yazarak Liste tipli parametrik alanlar aratılır ve Liste tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Liste tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload56fde25b-5688-4205-8392-5d34f153edff)

#### **1.1.1.1.2.4.Liste Tipli Parametrik Alan Tanımlama**

lblKM_LPARAM2 Liste tipli parametrik seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload824e1f9c-4e7f-4f5e-a883-311cd629857a) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadff6cfc9e-0bba-42ce-9710-7c9e90fd3c4b)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8e2f2dd1-e6a2-427d-91a7-f8d8dc82d850)

Liste tipli alanın liste değerlerini girmek için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1160d295-2b0a-4ae7-82aa-f685f95633a6) (Yeni) butonuna tıklanır, liste değerleri yazılır ve kaydedilir. Liste eleman değeri 1 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc31ed8f6-5e88-4102-9a18-f632e3760631)

Liste eleman değeri 2 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3a7129e0-028b-4c49-9976-086440a06b96)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb6fddee-9fbe-4af8-82c5-3123ff287391)

Alanın zorunlu olup, olmayacağı sıra no bilgisi, liste elemanları tanımlanarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadca9b6a36-8811-49eb-969f-c1c40557abc7)(kaydet) butonu tıklanarak liste tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade8f2ccf9-77ac-4117-8602-43b3d2080111)

Tanımlanan Liste tipli parametik alan Öneri Sistemi Modülünde Önerinin Kazanç Maliyet aşamasında iken Kazanç /Maliyet Tanımları ekranında Diğer Alanlar sekmesinde görüntülenir

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4b4ead58-90b8-4f42-be2a-62aefce97de5)

#### **1.1.1.1.2.5.Personel Tipli Parametrik Alanların Listesi**

Öneri Sistemi Modülünde Önerinin Kazanç Maliyet aşamasında iken Kazanç /Maliyet Tanımları ekranında Diğer Alanlar sekmesinde Personel tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Personel yazarak Personel tipli parametrik alanlar aratılır ve Personel tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Personel tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadadcbe0cc-3ef0-4dc7-a09d-df1a610fc7e5)

#### **1.1.1.1.2.6.Personel Tipli Parametrik Alan Tanımlama**

lblKM_PPARAM1 Personel tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload824e1f9c-4e7f-4f5e-a883-311cd629857a) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload661169c5-ce3f-4f5e-8721-d34f52776766)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1ec27e93-4e1c-4140-842c-a59af33e29ff)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadca9b6a36-8811-49eb-969f-c1c40557abc7)(kaydet) butonu tıklanarak Personel tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6a3a5f54-f5c3-49ce-b790-bc3c2c397d36)

Tanımlanan Personel tipli parametik alan Öneri Sistemi Modülünde Önerinin Kazanç Maliyet aşamasında iken Kazanç /Maliyet Tanımları ekranında Diğer Alanlar sekmesinde görüntülenir

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0756c981-f66b-4a73-8ea3-cb846eebe221)

Personel tipli parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload34ebaa9f-c31f-4932-8e9c-bfeca35f9c30)(seç) butonu tıklanıldığında sistemde tanımlı personel listesinde seçim yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload13f199b0-964a-4df9-9507-55da9700e293)

#### **1.1.1.1.2.7.Personel(Çoklu Seçim) Parametrik Alanların Listesi**

Öneri Sistemi Modülünde Önerinin Kazanç Maliyet aşamasında iken Kazanç /Maliyet Tanımları ekranında Diğer Alanlar sekmesinde Personel(Çoklu Seçim) tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Personel(Çoklu Seçim) yazarak Personel(Çoklu Seçim) tipli parametrik alanlar aratılır ve Personel(Çoklu Seçim) tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Personel(Çoklu Seçim) tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload851fa19e-da08-42ea-b8c5-4369d1bbde91)

#### **1.1.1.1.2.8.Personel(Çoklu Seçim) Parametrik Alan Tanımlama**

lblKM_PMPARAM1 Personel(Çoklu Seçim) tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload824e1f9c-4e7f-4f5e-a883-311cd629857a) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload97097b82-ee5a-4e36-abb6-8cdead5735fd)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4a82cf99-8a37-43e4-8831-4bc679b5a30c)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadca9b6a36-8811-49eb-969f-c1c40557abc7)(kaydet) butonu tıklanarak Personel(Çoklu Seçim) tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcbb25eb4-1d44-415a-813b-571e249b15df)

Tanımlanan Personel (Çoklu Seçim) tipli parametik alan Öneri Sistemi Modülünde Önerinin Kazanç Maliyet aşamasında iken Kazanç /Maliyet Tanımları ekranında Diğer Alanlar sekmesinde görüntülenir

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfd54bb17-1c7a-4324-9e65-116a63ac91bf)

Personel(Çoklu Seçim) tipli parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbf7f7c86-0a1c-4e26-b805-3eb1f7fdaacf)(Ekle) butonu tıklanıldığında sistemde tanımlı personel listesinde tekli ve çoklu seçim yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada97d4be3-8906-42ed-a734-39bfd3437e90)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload95fe576d-7b30-4e85-a209-27a8a880365e)(Seç) butonu tıklanıldığında ise sistemde tanımlı kullanıcı Grubu listesinde tekli ve çoklu seçim yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3a30fea0-3cae-4d16-be98-aee9bd7bd4c2)

#### **1.1.1.1.2.9.Metin Tipli Parametrik Alanların Listesi**

Öneri Sistemi Modülünde Önerinin Kazanç Maliyet aşamasında iken Kazanç /Maliyet Tanımları ekranında Diğer Alanlar sekmesinde Metin tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Metin yazarak Metin tipli parametrik alanlar aratılır ve Metin tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Metin tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb5e0905-3cee-4012-9b99-e384cc2c103e)

#### **1.1.1.1.2.10.Metin Tipli Parametrik Alan Tanımlama**

lblKM_PARAM1 Metin tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload824e1f9c-4e7f-4f5e-a883-311cd629857a) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb1cfe7a9-a803-42f4-a716-d0e65147bd2d)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3079a8f9-c7ca-41b4-9f94-cfe245df9145)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadca9b6a36-8811-49eb-969f-c1c40557abc7)(kaydet) butonu tıklanarak Metin tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbbc26fe5-2def-42e0-8f60-4ef6e325f439)

Tanımlanan Metin tipli parametik alan Öneri Sistemi Modülünde Önerinin Kazanç Maliyet aşamasında iken Kazanç /Maliyet Tanımları ekranında Diğer Alanlar sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc091bb8e-5097-4269-ad5c-58e88759da6e)

#### **1.1.1.1.2.11.Parasal Tipli Parametrik Alanların Listesi**

Öneri Sistemi Modülünde Önerinin Kazanç Maliyet aşamasında iken Kazanç /Maliyet Tanımları ekranında Diğer Alanlar sekmesinde Parasal tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Parasal yazarak Parasal tipli parametrik alanlar aratılır ve Parasal tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Parasal tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload236ceb2b-8d52-4970-81a5-32e4454f979a)

#### **1.1.1.1.2.12.Parasal Tipli Parametrik Alan Tanımlama**

lblKM_NPARAM1 Parasal tipli alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload824e1f9c-4e7f-4f5e-a883-311cd629857a) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload85fd5395-d464-44e1-93d8-dd1763bbf66c)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload18e2f9de-399d-4cad-a5bf-e1cc0b4a0299)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadca9b6a36-8811-49eb-969f-c1c40557abc7)(Kaydet ) butonu tıklanarak Parasal tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0ecac890-d601-40af-8207-3b6f7d2d965e)

Tanımlanan Parasal tipli parametik alan Öneri Sistemi Modülünde Önerinin Kazanç Maliyet aşamasında iken Kazanç /Maliyet Tanımları ekranında Diğer Alanlar sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb4f415a1-784f-402f-9ca4-099061a3813b)

#### **1.1.1.1.2.13.Departman Tipli Parametrik Alanların Listesi**

Öneri Sistemi Modülünde Önerinin Kazanç Maliyet aşamasında iken Kazanç /Maliyet Tanımları ekranında Diğer Alanlar sekmesinde Departman tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Departman yazarak Departman tipli parametrik alanlar aratılır ve Departman tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Departman tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload275b10ef-5004-44d4-b85d-5c8d2a4946a0)

#### **1.1.1.1.2.14.Departman Tipli Parametrik Alan Tanımlama**

lblKM_DSPARAM1 Departman tipli alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload824e1f9c-4e7f-4f5e-a883-311cd629857a) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4165f6f1-4251-4fd1-bc30-b1d732655daf)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada4fa4d05-d4d2-4e46-ba65-3143cd233f64)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadca9b6a36-8811-49eb-969f-c1c40557abc7)(Kaydet ) butonu tıklanarak Departman tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb0deb76d-2a70-4d5a-a157-621b803025bc)

Tanımlanan Departman tipli parametik alan Öneri Sistemi Modülünde Önerinin Kazanç Maliyet aşamasında iken Kazanç /Maliyet Tanımları ekranında Diğer Alanlar sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6a6ebf1f-c6d5-48f7-9b4b-d26a08ccd19f)

Departman tipli parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload34ebaa9f-c31f-4932-8e9c-bfeca35f9c30)(seç) butonu tıklanıldığında sistemde tanımlı Departman listesinde seçim yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6e6bb0a7-331c-48c8-a74c-4bfa6baa258b)

#### **1.1.1.1.2.15.Departman(Çoklu Seçim) Tipli Parametrik Alanların Listesi**

Öneri Sistemi Modülünde Önerinin Kazanç Maliyet aşamasında iken Kazanç /Maliyet Tanımları ekranında Diğer Alanlar sekmesinde Departman(Çoklu Seçim) tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Departman(Çoklu Seçim) yazarak Departman(Çoklu Seçim) tipli parametrik alanlar aratılır ve Departman(Çoklu Seçim) tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Departman(Çoklu Seçim) tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaaac778a-73c9-4580-a0d2-228115e90de1)

#### **1.1.1.1.2.16.Departman(Çoklu Seçim) Tipli Parametrik Alan Tanımlama**

lblKM_DMPARAM1 Departman(Çoklu Seçim) tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload824e1f9c-4e7f-4f5e-a883-311cd629857a) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd8e8cfa1-96c9-428b-8240-32e814cb3f0f)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3c0b0738-da3d-49b5-9a4a-77066754ce06)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadca9b6a36-8811-49eb-969f-c1c40557abc7)(kaydet) butonu tıklanarak Departman(Çoklu Seçim) tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8d6b46eb-1347-4657-8574-addbfda348c0)

Tanımlanan Departman(Çoklu Seçim) tipli parametik alan Öneri Sistemi Modülünde Önerinin Kazanç Maliyet aşamasında iken Kazanç /Maliyet Tanımları ekranında Diğer Alanlar sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade007629c-9fcd-49ce-8823-8e1e583ae5e1)

Departman(Çoklu Seçim) tipli parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9848c5b2-b19c-4810-80dd-c02d24c19593) (Ekle) butonu tıklanıldığında sistemde tanımlı departman listesinde tekli ve çoklu seçim yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload22de13c8-f2db-4d9f-bd91-3ab63acb9762)

Öneri Sistemi Modülünde Önerinin Kazanç Maliyet aşamasında iken Kazanç /Maliyet Tanımları ekranında Diğer Alanlar sekmesinde tanımlanan parametrik tipli tüm alanlar;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3c03fbb6-3d0b-42ff-9e40-773d23ae1ccd)

### **1.1.1.1.3.Dil ayarlarında Tanımlan Parametrik Alan tipleri Görüntülen Ekrandan Kaldırma İşlemi**

1.Aşamada parametrik alanın bulunduğu ekran açılır. Öneri Sistemi Modülünde Önerinin Kazanç Maliyet aşamasında iken Kazanç /Maliyet Tanımları ekranında Diğer Alanlar sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc9710829-a424-47f1-8b60-0a8a640cdf56)

2\. Aşamada parametrik alanın bulunduğu ekran görüntülendikten sonra örnekteki herhangi alan seçilerek, Sağ tıkla/Kopyala komutu ile parametrik alanın ismi kopyalanır. Örnek: İstenilen Tarih

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc7c04757-7d24-4b47-8263-51c3bded5dba)

3\. Aşamada Sistem Altyapı Tanımları\>BSAT\>Konfigürasyon Ayarları\>Dil ayarları menüsü tıklanarak açılan ekranda Modül olarak Öneri Sistemi Modülü seçilir. Kopyalanan Dil ayarlarından tanımlanan liste tipli parametrik alanı grid ekranında **TR** alanına sağ tıkla/yapıştır komutu ile alanın yapıştırma işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9ae96e53-cc7b-4f1f-9025-0e1987a1556a)

4.Aşamada Tarih tipli parametrik alan seçilerek alanın içeriği görüntülemek için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload824e1f9c-4e7f-4f5e-a883-311cd629857a) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8bb9e716-22a8-4de9-b657-72466b438498)

5.Aşamada içeriği görüntülen Tarih tipli alanın değeri silerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadca9b6a36-8811-49eb-969f-c1c40557abc7)(Kaydet) butonu tıklanarak Dil Ayarları menüsünde tanımlı Tarih tipli alanın kaldırma işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3b2d030f-d9de-45aa-8c3c-0cd1d351b40a)

Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarlarında tanımlanan diğer parametrik alan tiplerin dil ayarları menüsünde kaldırma işlemi aynı şekilde olmaktadır. Öneri Sistemi Modülünde Önerinin Kazanç Maliyet aşamasında iken Kazanç /Maliyet Tanımları ekranında Diğer Alanlar sekmesinde tanımlı Tarih Tipli alanın kaldırılmış olduğu görülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd6fd5ea9-b489-4996-9de3-03447fd49aff)
