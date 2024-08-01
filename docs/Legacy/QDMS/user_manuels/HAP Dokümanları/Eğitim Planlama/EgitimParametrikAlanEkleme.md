---
title: Parametrik Alan Tanımlama İşlemi
description: Parametrik Alan Tanımlama İşlemi Yardım Dokümanı
sidebar_position: 1
---

:::tip Bilgi

İlgili konu başlığına sağ tarafta bulunan navigasyon yardımıyla hızlı bir şekilde ulaşabilirsiniz.

:::



**Eğitim Planlama Modülünde** **Dil Ayarları Menüsünde Parametrik Alan Tanımlama Kullanıcı Yardım Dokümanı**



# **1.Sistem Altyapı Tanımları**

Personel bilgilerinin tanımlandığı ve diğer modüller için gerekli olan altyapının kurgulanmasının yapıldığı menüdür.

## **1.1.Konfigürasyon Ayarları**

**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları

QDMS sisteminde özel ayarların yapıldığı menülerdir. Bu menülerde yapılan ayarlar tüm QDMS kullanıcıları için geçerli olan ortak ayarlardır.

### **1.1.1. Dil Ayarları**

**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları

Dil ayarları menüsünden QDMS üzerinde görülen menülerin isimleri, alanların isimleri değiştirilebilir. Modüllere yeni alanlar eklenebilir. Var olan alanların zorunluluk durumları düzenlenebilir. Alanların ekran üzerinde göründükleri sıralama değiştirilebilir.

### **1.1.1.1.Eğitim Planlama Modülü Ortak Kullanım İçin Yeni Alan Oluşturma**

Eğitim Planlama Modülünde menülerinde firmanın istemiş olduğu sistemde olmayan ekstradan alanlar tanımlanabilir. Tanımlanan bu alanlar tüm Eğitim Planlama Modülü kaynakları için geçerlidir. Sistem Altyapı Tanımları/BSAT/ Konfigürasyon Ayarları/Dil Ayarları menüsü tıklanılır. Açılan Dil Ayarları sayfasında Modül alanında “Eğitim Planlama” seçilir ve ekranda Eğitim Planlama Modülü ile ilgili dil tanımları görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload32fe50ce-c985-4969-a761-50a1b9b97abb)


Eğitim Planlama Modülünde Eğitim Tanımlama, Eğitim Talebi, Eğitim Etkinlik Değerlendirilmesi ve Puan Vereceğim Eğitimler menüsünde dil ayarlarında parametrik alan tipi tanımlama işlemleri yapılmaktadır. Eğitim Planlama menüsünde ise Detaylar butonu tıklatıldığında açılan Eğitim Detayı planlama ekranında bir Eğitim Detayı Planı tanımlarken Diğer Alanlar sekmesinde parametrik alan tipi tanımlaması yapılmaktadır. Bu menülerde parametrik tipli alanlarda kullanılan kısa kodlar bulunmaktadır. Hangi menüde hangi kısa kodlar kullanılmış ayırt etmek mümkündür. Parametrik tipli alanlarda hangi menüde olduğunun ayırt etmek için aşağıdaki kısa kodların başlama kısımlarına dikkate etmek gerekir;

**Eğitim Tanımlama:** lbl\_ kısa kodları genelde Entegre Yönetim Sistemi\>Eğitim Planlama \>Eğitim Tanımlama menüsünde açılan Eğitim Tanımlama ekranında görüntülen parametrik alan tipleri temsil eder.

**Eğitim Detay Planı:** lblO\_ kısa kodları genelde Entegre Yönetim Sistemi\>Eğitim Planlama \>Eğitim Planı menüsünde detaylar butonu tıklanıldığında açılan Eğitim Detay Planı menüsünde tanımlanan Eğitim Detay Planın ekranında Diğer alanlar sekmesinde görüntülen parametrik alan tipleri temsil eder.

**Eğitim Talebi:** lblT\_ kısa kodları genelde Entegre Yönetim Sistemi\>Eğitim Planlama \>Eğitim Talebi menüsünde görüntülen parametrik alan tipleri temsil eder.

**Eğitim Etkinlik Değerlendirmesi:** lblPARAM kısa kodları genelde Entegre Yönetim Sistemi\>Eğitim Planlama\>Eğitim Etkinlik Değerlendirmesi menüsünde görüntülen parametrik alan tipleri temsil eder.

**Puan Vereceğim Eğitimler:** lbl_K kısa kodları genelde Entegre Yönetim Sistemi\>Eğitim Planlama\>Puan Vereceğim Eğitimler menüsünde görüntülen parametrik alan tipleri temsil eder.

**Eğitim Planlama** **Modülünde Tanımlanan Parametrik Tipli Alanlar ve Tanımları;**

**1-Tarih tipli**: Takvim alanı eklenilen parametrik alandır. Örnek Kısa Kod: lbl_DPARAM1 (Eğitim Planlama Modülünde Eğitim Tanımlama menüsünde görüntülenir.)

**2-Liste tipli**: Birden fazla liste elemanları arasından tek seçim yapılan parametrik alandır. Liste elemanları tanımlanarak, tanımlanan liste elemanlarında seçip yapılır. Örnek Kısa Kod: lblO_LPARAM2 (Eğitim Modülünde Eğitim planı detayları ekranında diğer alanlar sekmesinde görüntülenir.)

**3-Personel Tipli:** QDMS personel veri tabanından kişi seçilebilmesini sağlayan parametrik alandır. Sistem Altyapı Tanımları\>Bsat\>Tanımlama\>Personel Tanımlama menüsünde tanımlı olan Personellerin listesinde seçim yapılır. Örnek Kısa Kod: lblO_PPARAM1 (Eğitim Modülünde Eğitim planı detayları ekranında diğer alanlar sekmesinde görüntülenir.)

**4- Metin (Çoklu Satır) Tipli**: Elle yazım imkanı veren karakter sınırı olmayan çok satırlı metin kutucuğu eklenen parametrik alandır. Örnek Kısa Kod: lbl_PARAM6 (Eğitim Planlama Modülünde Eğitim Tanımlama menüsünde görüntülenir.)

**5-Metin tipli**: Elle yazım imkanı veren metin kutucuğu ekleyen parametrik alandır. Örnek Kısa Kod: lblO_PARAM2 (Eğitim Modülünde Eğitim planı detayları ekranında diğer alanlar sekmesinde görüntülenir)

**6-Personel (Çoklu Satır) Tipli**: QDMS personel veri tabanından tekli ve çoklu kişi seçilebilmesini sağlayan parametrik alandır. Sistem Altyapı Tanımları\>Bsat\>Tanımlama\>Personel Tanımlama menüsünde tanımlı olan Personellerin listesinde seçim yapılır. Örnek Kısa Kod: lblT_PMPARAM1 (Eğitim Modülünde Eğitim Talebi menüsünde görüntülenir.)

**7- Departman Tipli:** QDMS departman veri tabanından departman bilgisi seçilebilmesini sağlar. Sistem Altyapı Tanımları\>Bsat\>Tanımlama\>Departman Tanımlama menüsünde tanımlı olan Departman listesinde seçim yapılır. Örnek Kısa Kod: lblT_DSPARAM1 (Eğitim Modülünde Eğitim Talebi menüsünde görüntülenir.)

**8- Departman(Çoklu Seçim):** QDMS departman veri tabanından departman bilgisi tekli ve çoklu seçilebilmesini sağlar. Sistem Altyapı Tanımları\>Bsat\>Tanımlama\>Departman Tanımlama menüsünde tanımlı olan Departman listesinde seçim yapılır. Örnek Kısa Kod: lbl_DMPARAM1 (Eğitim Planlama Modülünde Eğitim Tanımlama menüsünde görüntülenir.)

**9**-**Parasal Tipli:** Parasal olarak veri girişi yaptıran parametrik alandır. Tanımlanan parametrik alanın yanında para birimleri seçildiği alan çıkar. Para birimleri seçim alanındaki para birimleri Sistem Altyapı Tanımları\>BSAT\>Tanımlar\>Para Birimleri Tanımlama menüsünde tanımlı olan para birimleridir. Örnek Kısa Kod: lbl_NPARAM6 (Eğitim Planlama Modülünde Eğitim Tanımlama menüsünde görüntülenir.

**10- Ölçü Birimi Tipli:** Ölçü olarak veri girişi yaptıran parametrik alandır. Tanımlanan parametrik alanın yanında Ölçü birimleri seçildiği alan çıkar. Ölçü birimleri seçim alanındaki ölçü Birimleri Sistem Altyapı Tanımları\>BSAT\>Tanımlar\>Ölçü Birimleri Tanımlama menüsünde tanımlı olan ölçü birimleridir. Örnek Kısa Kod: lbl_KNPARAM1 (Eğitim Planlama Modülünde Puan Vereceğim Eğitimler menüsünde görüntülenir.)

### **1.1.1.1.1.Eğitim Planlama Modülünde Eğitim Tanımlama Menüsünde Parametrik Alan Tipi Tanımlaması**

Eğitim Modülünde Entegre Yönetim Sistemi \>Eğitim Planlama\>Eğitim Tanımlama menüsünde tanımlanan parametrik alanların kısa kodları lbl\_ başlığı ile tanımlı kısa kodlardır. lbl\_ başlığındaki kısa kodlar olan tüm parametrik tipli alanlar tanımlandığında Eğitim Planlama Modülünde Eğitim Tanımlama menüsünde görüntülenir.

##### **1.1.1.1.1.1.Tarih Tipli Parametrik Alanların Listesi**

Eğitim Planlama Modülünde Eğitim Tanımlama menüsünde Tarih tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Tarih yazarak Tarih tipli parametrik alanlar aratılır ve Tarih tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen tarih tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd3e011d1-1acc-4c73-a8e2-d0f2b564795e)

##### **1.1.1.1.1.2.Tarih Tipli Parametrik Alan Tanımlama**

lbl_DPARAM1 Tarih tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload399037b0-bd91-4dee-804b-6c5b92047c91) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcbb1ec11-ffff-4824-85c6-68a592e50b4a)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada6798295-f018-45c9-b17c-40035a1b6ae0)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada32aa19a-4aa8-4616-bf87-4148a32befcd)(Kaydet) butonu tıklanarak tarih tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload31eccf4f-30aa-4ffd-af8e-ca5a291e9c83)

Tanımlanan Tarih tipli parametik alan Eğitim Planlama Modülünde Eğitim Tanımlama ekranında görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb0fd6b3a-c620-4402-b378-0f48a8484011)

##### **1.1.1.1.1.3.Liste Tipli Parametrik Alanların Listesi**

Eğitim Planlama Modülünde Eğitim Tanımlama menüsünde Liste tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Liste yazarak Liste tipli parametrik alanlar aratılır ve Liste tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Liste tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3c853c0e-0605-480a-83ba-412b34637be0)

##### **1.1.1.1.1.4.Liste Tipli Parametrik Alan Tanımlama**

lbl_LPARAM1 Liste tipli parametrik seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload399037b0-bd91-4dee-804b-6c5b92047c91) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload41406ebf-104c-4714-95c0-072c1d605252)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8bcb7c90-b798-4d12-b066-4828c78cf37e)

Liste tipli alanın liste değerlerini girmek için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadac48c8a9-5528-48a6-99a3-3bcc6e064ea4) (Yeni) butonuna tıklanır, liste değerleri yazılır ve kaydedilir. Liste eleman değeri 1 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2e557207-3beb-4390-95bc-dc5f8ebbc788)

Liste eleman değeri 2 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5802f632-a646-4fcc-99ce-992cda67a5b9)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload52002209-a915-4353-b8f2-9b419c98b4e1)

Alanın zorunlu olup, olmayacağı sıra no bilgisi, liste elemanları tanımlanarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada32aa19a-4aa8-4616-bf87-4148a32befcd)(kaydet) butonu tıklanarak liste tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaded16adec-7343-4b71-be8c-84025b678cd0)

Tanımlanan Liste tipli parametik alan Eğitim Planlama Modülünde Eğitim Tanımlama ekranında görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd4c5bcc3-5582-4ba3-be55-d9ee47f11ebd)

##### **1.1.1.1.1.5.Metin Tipli Parametrik Alanların Listesi**

Eğitim Planlama Modülünde Eğitim Tanımlama menüsünde Metin tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Metin yazarak Metin tipli parametrik alanlar aratılır ve Metin tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Metin tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload31d314fe-f997-47a2-b31f-fcfacb089356)

##### **1.1.1.1.1.6.Metin Tipli Parametrik Alan Tanımlama**

lbl_PARAM2 Metin tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload399037b0-bd91-4dee-804b-6c5b92047c91) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada5650f61-c5b6-4980-98af-199b6e3ae8d0)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3b6496e9-d5a7-40e1-99f7-82def2239a9a)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada32aa19a-4aa8-4616-bf87-4148a32befcd)(kaydet) butonu tıklanarak Metin tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadedd01a10-90db-4b16-912d-b906ffd2bd28)

Tanımlanan Metin tipli parametik alan Eğitim Planlama Modülünde Eğitim Tanımlama ekranında görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadefb4d052-8f58-4763-a086-9162afda5ce6)

##### **1.1.1.1.1.7.Metin(Çoklu Satır) Tipli Parametrik Alanların Listesi**

Eğitim Planlama Modülünde Eğitim Tanımlama menüsünde Metin(Çoklu Satır) tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Metin(Çoklu Satır) yazarak Metin(Çoklu Satır) tipli parametrik alanlar aratılır ve Metin(Çoklu Satır) tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Metin(Çoklu Satır) tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7f6f3e97-b609-49da-abe4-3c38b43f98c9)

##### **1.1.1.1.1.8.Metin(Çoklu Satır) Tipli Parametrik Alan Tanımlama**

lbl_PARAM6 Metin(Çoklu Satır) tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload399037b0-bd91-4dee-804b-6c5b92047c91) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1115a849-509a-4e8d-a086-51ccd887b3ce)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbcd5ec40-cd93-4755-970d-77458dc4cec3)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada32aa19a-4aa8-4616-bf87-4148a32befcd)(kaydet) butonu tıklanarak Metin(Çoklu Satır) tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload562d99e0-7a56-40f0-b289-f6ab27b2de30)

Tanımlanan Metin(Çoklu Satır) tipli parametik alan Eğitim Planlama Modülünde Eğitim Tanımlama ekranında görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7776b9e0-ee6c-409c-b919-a9192b9a912b)

##### **1.1.1.1.1.9.Ölçü Birimi Parametrik Alanların Listesi**

Eğitim Planlama Modülünde Eğitim Tanımlama menüsünde Ölçü Birimi tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Ölçü Birimi yazarak Ölçü Birimi tipli parametrik alanlar aratılır ve Ölçü Birimi tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Ölçü Birimi tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc02d2452-8ea9-4491-97d0-26e40610dbf5)

##### **1.1.1.1.1.10.Ölçü Birimi Parametrik Alan Tanımlama**

lbl_NPARAM1 Ölçü birimi tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload399037b0-bd91-4dee-804b-6c5b92047c91) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcb9e5fe9-3215-4fb4-a167-a36b186886a4)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcf4c1a82-9dc3-41f3-ac6b-4918e49b308a)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada32aa19a-4aa8-4616-bf87-4148a32befcd)(Kaydet) butonu tıklanarak ölçü birimi tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc72f9f2e-0536-45ac-9adc-3c40de5fac2f)

Tanımlanan ölçü birimi tipli parametik alan Eğitim Planlama Modülünde Eğitim Tanımlama ekranında görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada959a576-fca2-4ff8-b5d8-6cb8997012b8)

##### **1.1.1.1.1.11.Parasal Tipli Parametrik Alanların Listesi**

Eğitim Planlama Modülünde Eğitim Tanımlama menüsünde Parasal tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Parasal yazarak Parasal tipli parametrik alanlar aratılır ve Parasal tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Parasal tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload31e83033-dffa-4dc2-85bd-8535324d5347)

##### **1.1.1.1.1.12.Parasal Tipli Parametrik Alan Tanımlama**

lbl_NPARAM6 Parasal tipli alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload399037b0-bd91-4dee-804b-6c5b92047c91) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload69e88802-ffc9-4684-862b-99bf2f21fa60)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload73031666-4dba-41ce-893e-eaf772401d99)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada32aa19a-4aa8-4616-bf87-4148a32befcd)(Kaydet ) butonu tıklanarak Parasal tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada990c1bf-139e-4b41-a6a8-2c911008fb02)

Tanımlanan Parasal tipli parametik alan Eğitim Planlama Modülünde Eğitim Tanımlama ekranında görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload09403d99-de1b-49d0-b33c-56cd2c273641)

##### **1.1.1.1.1.13.Departman Tipli Parametrik Alanların Listesi**

Eğitim Planlama Modülünde Eğitim Tanımlama menüsünde Departman tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Departman yazarak Departman tipli parametrik alanlar aratılır ve Departman tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Departman tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload47f82081-3131-4099-8567-c4e633470bbb)

##### **1.1.1.1.1.14.Departman Tipli Parametrik Alan Tanımlama**

lbl_DSPARAM1 Departman tipli alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload399037b0-bd91-4dee-804b-6c5b92047c91) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9102afe8-bf9b-42df-bc3f-a5e79ef1c5d3)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfe52bb65-f4ca-4b81-bf05-845312f22562)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada32aa19a-4aa8-4616-bf87-4148a32befcd)(Kaydet ) butonu tıklanarak Departman tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload640a10a4-b418-49f7-9bec-3ebb0f8502a8)

Tanımlanan Departman tipli parametik alan Eğitim Planlama Modülünde Eğitim Tanımlama ekranında görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbf1fc44f-5919-4754-9107-69aff271c4fd)

Departman tipli parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd9d88a1b-3774-4023-b1e2-c30ebd8fbed4)(seç) butonu tıklanıldığında sistemde tanımlı Departman listesinde seçim yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadae544ec9-0a7f-4347-aff6-c70c755bde1f)

##### **1.1.1.1.1.15.Departman(Çoklu Seçim) Tipli Parametrik Alanların Listesi**

Eğitim Planlama Modülünde Eğitim Tanımlama menüsünde Departman(Çoklu Seçim) tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Departman(Çoklu Seçim) yazarak Departman(Çoklu Seçim)l tipli parametrik alanlar aratılır ve Departman(Çoklu Seçim) tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Departman(Çoklu Seçim) tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7ce4324b-a948-4180-be7b-abf88a4ee8f3)

##### **1.1.1.1.1.16.Departman(Çoklu Seçim) Tipli Parametrik Alan Tanımlama**

lbl_DMPARAM1 Departman(Çoklu Seçim) tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload399037b0-bd91-4dee-804b-6c5b92047c91) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf35f6fd5-6b34-4622-94e9-02096263e2b5)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload62f11f1f-f61a-4e86-b12b-80732cdee749)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada32aa19a-4aa8-4616-bf87-4148a32befcd)(kaydet) butonu tıklanarak Departman(Çoklu Seçim) tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload380b0b9d-0ab3-4c2d-8311-614b1afd596a)

Tanımlanan Departman(Çoklu Seçim) tipli parametik alan Eğitim Planlama Modülünde Eğitim Tanımlama ekranında görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8d38972b-9f02-474b-9598-84a6e8312e40)

Departman(Çoklu Seçim) tipli parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4f15826a-92a7-4986-a7fa-76f3e7363515) (Ekle) butonu tıklanıldığında sistemde tanımlı departman listesinde tekli ve çoklu seçim yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2a14834d-d476-4276-b163-7ee6ba64484d)

##### **1.1.1.1.1.17.Personel Tipli Parametrik Alanların Listesi**

Eğitim Planlama Modülünde Eğitim Tanımlama menüsünde Personel tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Personel yazarak Personel tipli parametrik alanlar aratılır ve Personel tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Personel tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf70fc49e-1c44-4b0f-8968-686c302acbca)

##### **1.1.1.1.1.18.Personel Tipli Parametrik Alan Tanımlama**

lbl_PPARAM1 Personel tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload399037b0-bd91-4dee-804b-6c5b92047c91) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload161b73a7-3132-4e8a-ba7f-2a39dad9b455)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf6c52a2e-48d8-4f2e-8071-b22e58fdcd6a)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada32aa19a-4aa8-4616-bf87-4148a32befcd)(kaydet) butonu tıklanarak Personel tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb80cb7e6-bba5-4c7c-9e10-4030d2b8cd23)

Tanımlanan Personel tipli parametik alan Eğitim Planlama Modülünde Eğitim Tanımlama ekranında görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc6757d9f-3486-46d0-92eb-fc770942c739)

Personel tipli parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd9d88a1b-3774-4023-b1e2-c30ebd8fbed4)(seç) butonu tıklanıldığında sistemde tanımlı personel listesinde seçim yapılması sağlanılır

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8d6533c1-3357-4ebf-b4d4-98529880f9a4)

##### **1.1.1.1.1.19.Personel(Çoklu Seçim) Tipli Parametrik Alanların Listesi**

Eğitim Planlama Modülünde Eğitim Tanımlama menüsünde Personel(Çoklu Seçim) tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Personel(Çoklu Seçim) yazarak Personel(Çoklu Seçim) tipli parametrik alanlar aratılır ve Personel(Çoklu Seçim) tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Personel(Çoklu Seçim)  tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload787e5622-cff3-4d42-a472-3d70fc5995af)

##### **1.1.1.1.1.20.Personel (Çoklu Seçim) Tipli Parametrik Alan Tanımlama**

lbl_PMPARAM1 Personel(Çoklu Seçim) tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload399037b0-bd91-4dee-804b-6c5b92047c91) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb8cbb772-b19b-4d93-8493-94aa4b78b07f)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload96b226a9-00e4-49d5-af72-6a9172e34696)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada32aa19a-4aa8-4616-bf87-4148a32befcd)(kaydet) butonu tıklanarak Personel(Çoklu Seçim) tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada031a332-a39d-466d-9fa0-57da1d3f4ad3)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload380b0b9d-0ab3-4c2d-8311-614b1afd596a)

Tanımlanan Personel(Çoklu Seçim) tipli parametik alan Eğitim Planlama Modülünde Eğitim Tanımlama ekranında görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9a19810e-9144-43b8-a5da-3b5ec3c63073)

Personel(Çoklu Seçim) tipli parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload218d1ce9-e47b-49c3-a736-ee3f993c8dac)(Ekle) butonu tıklanıldığında sistemde tanımlı personel listesinde tekli ve çoklu seçim yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload861596c2-2cc8-4434-ae1a-92b3c94a18a2)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbae60b1f-81ee-442d-b255-ebe306c751e7)(Seç) butonu tıklanıldığında ise sistemde tanımlı kullanıcı Grubu listesinde seçim yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2f0b5c4b-ea12-406d-904d-93fc5a331541)

Eğitim Planlama Modülünde Eğitim Tanımlama menüsünde tanımlanan tüm alanlar;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload756c82f5-f4c8-4690-8b96-d145418a8d75)

#### **1.1.1.1.2.Eğitim Planlama Modülünde Eğitim Detay Planlama Ekranında Diğer Alanlar sekmesinde Parametrik Alan Tipi Tanımlaması**

Eğitim Planlama Modülünde Entegre Yönetim Sistemi\>Eğitim Planlama\>Eğitim Planı menüsünde detaylar butonu tıklanıldığında açılan Eğitim Detay Planlama sayfasında bir Eğitim Detay planı tanımlanırken Diğer alanlar sekmesinde dil ayarlarında tanımlanan parametrik alanların kısa kodları lblO\_ başlığı ile tanımlı kısa kodlardır. lblO\_ başlığındaki kısa kodlar olan tüm parametrik tipli alanlar tanımlandığında Eğitim Modülünde Eğitim Detay Planlama ekranında Diğer alanlar sekmesinde görüntülenir.

##### **1.1.1.1.2.1.Tarih Tipli Parametrik Alanların Listesi**

Eğitim Modülünde Eğitim Detay Planlama ekranında Diğer alanlar sekmesinde Tarih tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Tarih yazarak Tarih tipli parametrik alanlar aratılır ve Tarih tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen tarih tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb37a9d45-f866-4abf-a4ce-bd25d3ac20a3)

##### **1.1.1.1.2.2.Tarih Tipli Parametrik Alan Tanımlama**

lblO_DPARAM2 Tarih tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload399037b0-bd91-4dee-804b-6c5b92047c91) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4e91ae29-8f1e-4f9f-ad92-ef1c89ca8bd1)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8606cdee-2c0b-4102-8e6b-bf297ca52e7d)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada32aa19a-4aa8-4616-bf87-4148a32befcd)(Kaydet) butonu tıklanarak tarih tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4bd8a0ff-1f33-413f-be95-8b529fd52d9c)

Tanımlanan Tarih tipli parametik alan Eğitim Modülünde Eğitim Detay Planlama ekranında Diğer alanlar sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9c400d1d-d799-43cb-be02-94868010be23)

##### **1.1.1.1.2.3.Liste Tipli Parametrik Alanların Listesi**

Eğitim Modülünde Eğitim Detay Planlama ekranında Diğer alanlar sekmesinde Liste tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Liste yazarak Liste tipli parametrik alanlar aratılır ve Liste tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Liste tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2562b561-2bd0-4ff7-9f1f-edbeb2a66343)

##### **1.1.1.1.2.4.Liste Tipli Parametrik Alan Tanımlama**

lblO_LPARAM2 Liste tipli parametrik seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload399037b0-bd91-4dee-804b-6c5b92047c91) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload34bb0300-5d6e-4b12-9fb1-dc9d5d1aa6ee)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4c8d4206-362c-40b5-960d-d2ffffa51a83)

Liste tipli alanın liste değerlerini girmek için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadac48c8a9-5528-48a6-99a3-3bcc6e064ea4) (Yeni) butonuna tıklanır, liste değerleri yazılır ve kaydedilir. Liste eleman değeri 1 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2e557207-3beb-4390-95bc-dc5f8ebbc788)

Liste eleman değeri 2 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5802f632-a646-4fcc-99ce-992cda67a5b9)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd3233ed0-4179-482e-8287-8b613d803dd2)

Alanın zorunlu olup, olmayacağı sıra no bilgisi, liste elemanları tanımlanarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada32aa19a-4aa8-4616-bf87-4148a32befcd)(kaydet) butonu tıklanarak liste tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd6df9bd2-b753-40a7-8a9a-1aef1760e197)

Tanımlanan Liste tipli parametik alan Eğitim Modülünde Eğitim Detay Planlama ekranında Diğer alanlar sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf5f33fcc-6551-4da2-bd11-34b836be5c56)

##### **1.1.1.1.2.5.Personel Tipli Parametrik Alanların Listesi**

Eğitim Modülünde Eğitim Detay Planlama ekranında Diğer alanlar sekmesinde Personel tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Personel yazarak Personel tipli parametrik alanlar aratılır ve Personel tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Personel tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadccc33b2c-27aa-405b-ab34-18fb897ddc3f)

##### **1.1.1.1.2.6.Personel Tipli Parametrik Alan Tanımlama**

lblO_PPARAM1 Personel tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload399037b0-bd91-4dee-804b-6c5b92047c91) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload76981e66-e020-489d-a264-a361d9743fb5)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload311a20c6-c51b-432a-8103-18842a7a60cf)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada32aa19a-4aa8-4616-bf87-4148a32befcd)(kaydet) butonu tıklanarak Personel tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2e195b2b-15d7-4839-a474-8a3cfaa1f944)

Tanımlanan Personel tipli parametik alan Eğitim Modülünde Eğitim Detay Planlama ekranında Diğer alanlar sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6f5ffd5a-82aa-4ff5-9154-cd71821c5ed0)

Personel tipli parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd9d88a1b-3774-4023-b1e2-c30ebd8fbed4)(seç) butonu tıklanıldığında sistemde tanımlı personel listesinde seçim yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7793506c-b12e-4184-97e2-b99fe8ad5f49)

##### **1.1.1.1.2.7.Ölçü Birimi Parametrik Alanların Listesi**

Eğitim Modülünde Eğitim Detay Planlama ekranında Diğer alanlar sekmesinde Ölçü Birimi tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Ölçü Birimi yazarak Ölçü Birimi tipli parametrik alanlar aratılır ve Ölçü Birimi tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Ölçü Birimi tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfcd36b49-5b2e-4afe-a66a-022673b5f0c3)

##### **1.1.1.1.2.8.Ölçü Birimi Parametrik Alan Tanımlama**

lblO_NPARAM6 Ölçü birimi tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload399037b0-bd91-4dee-804b-6c5b92047c91) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadeab7c802-64b6-4f6f-bb16-5968af2e4f1f)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1d0f78e1-dc91-44d7-b039-bae9342222d3)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada32aa19a-4aa8-4616-bf87-4148a32befcd)(Kaydet) butonu tıklanarak ölçü birimi tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb9ed556e-4ce1-4884-965b-6d213c9e0b51)

Tanımlanan Ölçü Birimi tipli parametik alan Eğitim Modülünde Eğitim Detay Planlama ekranında Diğer alanlar sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload31331a1d-b58a-40cb-a1f0-70a9789958b0)

##### **1.1.1.1.2.9.Parasal Tipli Parametrik Alanların Listesi**

Eğitim Modülünde Eğitim Detay Planlama ekranında Diğer alanlar sekmesinde Parasal tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Parasal yazarak Parasal tipli parametrik alanlar aratılır ve Parasal tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Parasal tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload10fe5834-786d-4c1a-9332-9221099eddb4)

##### **1.1.1.1.2.10.Parasal Tipli Parametrik Alan Tanımlama**

lblO_NPARAM2 Parasal tipli alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload399037b0-bd91-4dee-804b-6c5b92047c91) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc85e9f6c-b1f7-4d75-9680-b518b86c8574)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade6187d40-8f0a-4d48-b9f7-54e7a55dfda3)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada32aa19a-4aa8-4616-bf87-4148a32befcd)(Kaydet ) butonu tıklanarak Parasal tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload75a165da-b094-455d-9be6-7f0c915c00d4)

Tanımlanan Parasal tipli parametik alan Eğitim Modülünde Eğitim Detay Planlama ekranında Diğer alanlar sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload71f07c02-bf77-431b-bb9d-f7868ee464ce)

##### **1.1.1.1.2.11.Departman Tipli Parametrik Alanların Listesi**

Eğitim Modülünde Eğitim Detay Planlama ekranında Diğer alanlar sekmesinde Departman tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Departman yazarak Departman tipli parametrik alanlar aratılır ve Departman tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Departman tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6650b2cf-3e28-49ed-b1a3-0bfb2808b252)

##### **1.1.1.1.2.12.Departman Tipli Parametrik Alan Tanımlama**

lblO_DSPARAM1 Departman tipli alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload399037b0-bd91-4dee-804b-6c5b92047c91) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd67542f4-6d25-482c-a90b-1accbb9fa465)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5435e641-b9a0-4ddc-a83c-c04f567f4de1)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada32aa19a-4aa8-4616-bf87-4148a32befcd)(Kaydet ) butonu tıklanarak Departman tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0b8e9f48-0e69-4bba-8831-10bcbb5e8993)

Tanımlanan Departman tipli parametik alan Eğitim Modülünde Eğitim Detay Planlama ekranında Diğer alanlar sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9fa9dc10-500b-4058-a828-13e8ed27674c)

Departman tipli parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd9d88a1b-3774-4023-b1e2-c30ebd8fbed4)(seç) butonu tıklanıldığında sistemde tanımlı Departman listesinde seçim yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload11203599-51ef-46bd-a96c-e528b9fa7a96)

##### **1.1.1.1.2.13.Departman(Çoklu Seçim) Tipli Parametrik Alanların Listesi**

Eğitim Modülünde Eğitim Detay Planlama ekranında Diğer alanlar sekmesinde Departman(Çoklu Seçim) tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Departman(Çoklu Seçim) yazarak Departman(Çoklu Seçim)l tipli parametrik alanlar aratılır ve Departman(Çoklu Seçim) tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Departman(Çoklu Seçim) tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload48fd7fc0-c893-4c4b-976a-359d9e79d30c)

##### **1.1.1.1.2.14.Departman(Çoklu Seçim) Tipli Parametrik Alan Tanımlama**

lblO_DMPARAM1 Departman(Çoklu Seçim) tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload399037b0-bd91-4dee-804b-6c5b92047c91) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload41f2e95a-eae2-4e4e-9fab-0c7fed35ae56)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload093eb836-2a74-45e6-ba4b-46767dd46173)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada32aa19a-4aa8-4616-bf87-4148a32befcd)(kaydet) butonu tıklanarak Departman(Çoklu Seçim) tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb5bd8235-c058-43f8-9e48-ef2054fece49)

Tanımlanan Departman(Çoklu Seçim) tipli parametik alan Eğitim Modülünde Eğitim Detay Planlama ekranında Diğer alanlar sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1094caee-594d-40f5-8221-4b8d19fb7c80)

Departman(Çoklu Seçim) tipli parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4f15826a-92a7-4986-a7fa-76f3e7363515) (Ekle) butonu tıklanıldığında sistemde tanımlı departman listesinde tekli ve çoklu seçim yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload45b6b328-4cf3-4ff3-8537-d937bb837bf8)

##### **1.1.1.1.2.15.Personel(Çoklu Seçim) Tipli Parametrik Alanların Listesi**

Eğitim Modülünde Eğitim Detay Planlama ekranında Diğer alanlar sekmesinde Personel(Çoklu Seçim) tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Personel(Çoklu Seçim) yazarak Personel(Çoklu Seçim) tipli parametrik alanlar aratılır ve Personel(Çoklu Seçim) tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Personel(Çoklu Seçim)  tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload82e3eed1-2d7a-4d0a-a122-0e6cde6c936c)

##### **1.1.1.1.2.16.Personel(Çoklu Seçim) Tipli Parametrik Alan Tanımlama**

lblO_PMPARAM1 Personel(Çoklu Seçim) tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload399037b0-bd91-4dee-804b-6c5b92047c91) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload159102d3-8f8b-4462-a925-64b530b7e95e)Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload105f3174-5282-49e0-9d4f-2c586260248c)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada32aa19a-4aa8-4616-bf87-4148a32befcd)(kaydet) butonu tıklanarak Personel(Çoklu Seçim) tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4078a143-9752-4aad-916c-50d628d0c62c)

Tanımlanan Personel(Çoklu Seçim) tipli parametik alan Eğitim Modülünde Eğitim Detay Planlama ekranında Diğer alanlar sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb5c8c976-c579-48ef-b424-249b49e522f9)

Personel(Çoklu Seçim) tipli parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload218d1ce9-e47b-49c3-a736-ee3f993c8dac)(Ekle) butonu tıklanıldığında sistemde tanımlı personel listesinde tekli ve çoklu seçim yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload403562af-16ce-4b83-a0c1-76dbfdd240bf)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbae60b1f-81ee-442d-b255-ebe306c751e7)(Seç) butonu tıklanıldığında ise sistemde tanımlı kullanıcı Grubu listesinde seçim yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload168109c8-37e0-4fa5-9c0f-aaf38e745fe0)

##### **1.1.1.1.2.17.Metin Tipli Parametrik Alanların Listesi**

Eğitim Modülünde Eğitim Detay Planlama ekranında Diğer alanlar sekmesinde Metin tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Metin yazarak Metin tipli parametrik alanlar aratılır ve Metin tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Metin tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada93337ed-155e-45d5-bcea-a5b3eebb524e)

##### **1.1.1.1.2.18.Metin Tipli Parametrik Alan Tanımlama**

lblO_PARAM2 Metin tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload399037b0-bd91-4dee-804b-6c5b92047c91) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd2504cfd-7500-48b8-81f5-54a49fdaf7d4)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5be1c7c9-a033-4da0-a6a7-b75a032c4472)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada32aa19a-4aa8-4616-bf87-4148a32befcd)(kaydet) butonu tıklanarak Metin tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload82bab0e5-2836-4e12-bb35-8b419a85bc7c)

Tanımlanan Metin tipli parametik alan Eğitim Modülünde Eğitim Detay Planlama ekranında Diğer alanlar sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadecc203b6-6cc0-472b-b46c-e1d9f5be8bdf)

##### **1.1.1.1.2.19.Metin(Çoklu Satır) Tipli Parametrik Alanların Listesi**

Eğitim Modülünde Eğitim Detay Planlama ekranında Diğer alanlar sekmesinde Metin(Çoklu Satır) tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Metin(Çoklu Satır) yazarak Metin(Çoklu Satır) tipli parametrik alanlar aratılır ve Metin(Çoklu Satır) tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Metin(Çoklu Satır) tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9f2bff17-a01d-427c-a6aa-8ef97da30780)

##### **1.1.1.1.2.20.Metin(Çoklu Satır) Tipli Parametrik Alan Tanımlama**

lblO_PARAM6 Metin(Çoklu Satır) tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload399037b0-bd91-4dee-804b-6c5b92047c91) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload876f6bf8-f27a-4c4f-adb2-1eed885262e1)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc6b7bc84-fcf7-40ed-9c42-d79aec6aac04)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada32aa19a-4aa8-4616-bf87-4148a32befcd)(kaydet) butonu tıklanarak Metin(Çoklu Satır) tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload939bce78-b767-426f-8678-a894903d429d)

Tanımlanan Metin(Çoklu Satır) tipli parametik alan Eğitim Modülünde Eğitim Detay Planlama ekranında Diğer alanlar sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6381e1c4-adc2-46aa-9fc9-155733b158dc)

Eğitim Modülünde Eğitim Detay Planlama ekranında Diğer alanlar sekmesinde tanımlanan tüm alanlar;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2f8e3ed4-7bcf-4dbf-ac2e-9b7385666564)

#### **1.1.1.1.3.Eğitim Modülünde Eğitim Talebi Menüsünde Parametrik Alan Tipi Tanımlaması**

Eğitim Planlama Modülünde Entegre Yönetim Sistemi\>Eğitim Planlama\>Eğitim Talebi menüsünde tıklanıldığında açılan Yeni Eğitim Talebi sayfasında dil ayarlarında tanımlanan parametrik alanların kısa kodları lblT\_ başlığı ile tanımlı kısa kodlardır. lblT\_ başlığındaki kısa kodlar olan tüm parametrik tipli alanlar tanımlandığında Eğitim Modülünde Eğitim Talebi menüsünde görüntülenir.

##### **1.1.1.1.3.1.Tarih Tipli Parametrik Alanların Listesi**

Eğitim Modülünde Eğitim Talebi menüsünde Tarih tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Tarih yazarak Tarih tipli parametrik alanlar aratılır ve Tarih tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen tarih tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada0d2ddfe-4db5-4db5-89a3-0e83046ee527)

##### **1.1.1.1.3.2.Tarih Tipli Parametrik Alan Tanımlama**

lblT_DPARAM2 Tarih tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload399037b0-bd91-4dee-804b-6c5b92047c91) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload672e8722-bf4a-448f-856a-e246900949e2)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload37776004-e945-458c-9f25-6c9b525532e8)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada32aa19a-4aa8-4616-bf87-4148a32befcd)(Kaydet) butonu tıklanarak tarih tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload87639642-ce8c-4024-a16d-a1e2ed5d2620)

Tanımlanan Tarih tipli parametik alan Eğitim Modülünde Yeni Eğitim Talebi ekranında görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade7d1670c-fd33-4197-969c-2d024138dd4d)

##### **1.1.1.1.3.3.Liste Tipli Parametrik Alanların Listesi**

Eğitim Modülünde Eğitim Talebi menüsünde Liste tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Liste yazarak Liste tipli parametrik alanlar aratılır ve Liste tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Liste tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbb45a353-e607-4fbd-91da-49ffe96d8707)

##### **1.1.1.1.3.4.Liste Tipli Parametrik Alan Tanımlama**

lblT_LPARAM2 Liste tipli parametrik seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload399037b0-bd91-4dee-804b-6c5b92047c91) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9b4e4409-f51b-4f9a-bc0a-3e627a6a4888)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload883f31f6-bbcc-4f9d-b93b-1971b1296e7d)

Liste tipli alanın liste değerlerini girmek için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadac48c8a9-5528-48a6-99a3-3bcc6e064ea4) (Yeni) butonuna tıklanır, liste değerleri yazılır ve kaydedilir. Liste eleman değeri 1 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2e557207-3beb-4390-95bc-dc5f8ebbc788)

Liste eleman değeri 2 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5802f632-a646-4fcc-99ce-992cda67a5b9)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7355ff71-fb18-4ddb-a58d-13d8083d81e3)

Alanın zorunlu olup, olmayacağı sıra no bilgisi, liste elemanları tanımlanarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada32aa19a-4aa8-4616-bf87-4148a32befcd)(kaydet) butonu tıklanarak liste tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb3523a33-9f9c-4e1e-8a2c-f53918372123)

Tanımlanan Liste tipli parametik alan Eğitim Modülünde Yeni Eğitim Talebi ekranında görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1d83c8b3-0585-46de-a4db-576a773e6d9e)

##### **1.1.1.1.3.5.Personel Tipli Parametrik Alanların Listesi**

Eğitim Modülünde Eğitim Talebi menüsünde Personel tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Personel yazarak Personel tipli parametrik alanlar aratılır ve Personel tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Personel tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5a4e1868-ee69-4ec6-8b3d-cd3f748f6aa8)

##### **1.1.1.1.3.6.Personel Tipli Parametrik Alan Tanımlama**

lblT_PPARAM1 Personel tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload399037b0-bd91-4dee-804b-6c5b92047c91) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcc4dc06e-bd87-4920-89d0-fcad1b495159)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload247f7b79-7992-45bd-a235-2a6d027a523a)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada32aa19a-4aa8-4616-bf87-4148a32befcd)(kaydet) butonu tıklanarak Personel tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload03a2983a-a91e-41d1-a541-40f8dec092ca)

Tanımlanan Personel tipli parametik alan Eğitim Modülünde Yeni Eğitim Talebi menüsünde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd4c96c6d-6141-4cf7-b98c-ca8f6262392b)

Personel tipli parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd9d88a1b-3774-4023-b1e2-c30ebd8fbed4)(seç) butonu tıklanıldığında sistemde tanımlı personel listesinde seçim yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload42044824-f0d2-44c8-ba00-5a13f99d89c3)

##### **1.1.1.1.3.7.Ölçü Birimi Parametrik Alanların Listesi**

Eğitim Modülünde Eğitim Talebi menüsünde Ölçü Birimi tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Ölçü Birimi yazarak Ölçü Birimi tipli parametrik alanlar aratılır ve Ölçü Birimi tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Ölçü Birimi tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade29f7205-c736-471b-8bab-8193789e6463)

##### **1.1.1.1.3.8.Ölçü Birimi Parametrik Alan Tanımlama**

lblT_NPARAM6 Ölçü birimi tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload399037b0-bd91-4dee-804b-6c5b92047c91) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload82e4914d-2cbd-4e1b-8140-553792fb95de)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddfbc2551-40a2-4d82-89a9-ab076257e45d)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada32aa19a-4aa8-4616-bf87-4148a32befcd)(Kaydet) butonu tıklanarak ölçü birimi tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload439e4e63-576f-4f2f-ac80-fce5e055867d)

Tanımlanan ölçü birimi tipli parametik alan Eğitim Yeni Eğitim Talebi ekranında görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadce6d5cb6-4f0a-41d2-9a16-2d4b7de855b6)

##### **1.1.1.1.3.9.Parasal Tipli Parametrik Alanların Listesi**

Eğitim Modülünde Eğitim Talebi menüsünde Parasal tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Parasal yazarak Parasal tipli parametrik alanlar aratılır ve Parasal tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Parasal tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcacb408b-abff-46c8-859f-4938b651267c)

##### **1.1.1.1.3.10.Parasal Tipli Parametrik Alan Tanımlama**

lblT_NPARAM1 Parasal tipli alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload399037b0-bd91-4dee-804b-6c5b92047c91) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload86c85eea-a519-4e0c-8f1c-127f5c868b83)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4ce84f29-0d1d-4f7a-aad3-73eb2ae5422a)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada32aa19a-4aa8-4616-bf87-4148a32befcd)(Kaydet ) butonu tıklanarak Parasal tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload70592ca6-c13c-4a9b-b9d6-77a9a698efee)

Tanımlanan Parasal tipli parametik alan Eğitim Modülünde Yeni Eğitim Talebi ekranında görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload87f33ccf-57cd-4e2d-9e40-7d880d5e0e5d)

##### **1.1.1.1.3.11.Departman Tipli Parametrik Alanların Listesi**

Eğitim Modülünde Eğitim Talebi menüsünde Departman tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Departman yazarak Departman tipli parametrik alanlar aratılır ve Departman tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Departman tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload80f6ea54-c96c-43e2-8a97-1e995c6ad2eb)

##### **1.1.1.1.3.12.Departman Tipli Parametrik Alan Tanımlama**

lblT_DSPARAM1 Departman tipli alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload399037b0-bd91-4dee-804b-6c5b92047c91) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf224b4fb-5b1f-4f3a-b893-ef9341446623)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7b88cf3b-ca93-4283-91d6-81ad153d22d2)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada32aa19a-4aa8-4616-bf87-4148a32befcd)(Kaydet ) butonu tıklanarak Departman tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload506cddda-b587-446e-a755-a537458b98cb)

Tanımlanan Departman tipli parametik alan Eğitim Modülünde Yeni Eğitim Talebi menüsünde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6cbb6349-fa4b-49e8-9c9b-cec19ab71467)

Departman tipli parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd9d88a1b-3774-4023-b1e2-c30ebd8fbed4)(seç) butonu tıklanıldığında sistemde tanımlı Departman listesinde seçim yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4d3c5e6c-4f3a-4ba3-b0a1-558a0e9a7fe5)

##### **1.1.1.1.3.13.Departman(Çoklu Seçim) Tipli Parametrik Alanların Listesi**

Eğitim Modülünde Eğitim Talebi menüsünde Departman(Çoklu Seçim) tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Departman(Çoklu Seçim) yazarak Departman(Çoklu Seçim)l tipli parametrik alanlar aratılır ve Departman(Çoklu Seçim) tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Departman(Çoklu Seçim) tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbd666942-2b22-46f9-8f3f-a2e605c9d2c8)

##### **1.1.1.1.3.14.Departman(Çoklu Seçim) Tipli Parametrik Alan Tanımlama**

lblT_DMPARAM1 Departman(Çoklu Seçim) tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload399037b0-bd91-4dee-804b-6c5b92047c91) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6e9965af-ba09-4d04-96be-25a71acdc277)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload00a55ff8-820f-49de-a25f-e0cdb53262b9)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada32aa19a-4aa8-4616-bf87-4148a32befcd)(kaydet) butonu tıklanarak Departman(Çoklu Seçim) tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadda4d44bb-a5c7-4185-8fbf-603f7826c9a0)

Tanımlanan Departman(Çoklu Seçim) tipli parametik alan Eğitim Modülünde Yeni Eğitim Talebi ekranında görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload08813fff-bb7e-4748-93b2-66ec056afcdf)

Departman(Çoklu Seçim) tipli parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4f15826a-92a7-4986-a7fa-76f3e7363515) (Ekle) butonu tıklanıldığında sistemde tanımlı departman listesinde tekli ve çoklu seçim yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddf7cefce-5b4e-46ef-be07-4b9be4023ad4)

##### **1.1.1.1.3.15.Personel(Çoklu Seçim) Tipli Parametrik Alanların Listesi**

Eğitim Modülünde Eğitim Talebi menüsünde Personel(Çoklu Seçim) tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Personel(Çoklu Seçim) yazarak Personel(Çoklu Seçim) tipli parametrik alanlar aratılır ve Personel(Çoklu Seçim) tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Personel(Çoklu Seçim)  tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload616ed75f-2b9c-4576-a406-f531f59df0da)

##### **1.1.1.1.3.16.Personel(Çoklu Seçim) Tipli Parametrik Alan Tanımlama**

lblT_PMPARAM1 Personel(Çoklu Seçim) tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload399037b0-bd91-4dee-804b-6c5b92047c91) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6dbfb477-12df-4a5b-b9f5-86c50799c5bc)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf50761df-8e6e-4cc2-b513-3913250362b0)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada32aa19a-4aa8-4616-bf87-4148a32befcd)(kaydet) butonu tıklanarak Personel(Çoklu Seçim) tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload51e52eea-c98b-4ccf-817d-9ca0e40dd715)

Tanımlanan Personel(Çoklu Seçim) tipli parametik alan Eğitim Modülünde Yeni Eğitim Talebi menüsünde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade662fe51-5bbe-4d87-94c0-6fbd24b08278)

Personel(Çoklu Seçim) tipli parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload218d1ce9-e47b-49c3-a736-ee3f993c8dac)(Ekle) butonu tıklanıldığında sistemde tanımlı personel listesinde tekli ve çoklu seçim yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade2d942a4-eadd-48fe-a5b0-a1a978464f70)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbae60b1f-81ee-442d-b255-ebe306c751e7)(Seç) butonu tıklanıldığında ise sistemde tanımlı kullanıcı Grubu listesinde seçim yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload25b8690d-c8ba-4a08-99be-065a59fef02a)

##### **1.1.1.1.3.17.Metin Tipli Parametrik Alanların Listesi**

Eğitim Modülünde Eğitim Talebi menüsünde Metin tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Metin yazarak Metin tipli parametrik alanlar aratılır ve Metin tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Metin tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5835983f-daf4-42a4-8a11-a4232ab7fc74)

##### **1.1.1.1.3.18.Metin Tipli Parametrik Alan Tanımlama**

lblT_PARAM1Metin tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload399037b0-bd91-4dee-804b-6c5b92047c91) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbfde5f51-f67a-4457-bc21-d785774aa7e7)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb000f4bd-45f8-4253-a618-e93b3fc773ab)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada32aa19a-4aa8-4616-bf87-4148a32befcd)(kaydet) butonu tıklanarak Metin tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload79324cea-bf27-49bc-a627-222cec44f403)

Tanımlanan Metin tipli parametik alan Eğitim Modülünde Yeni Eğitim Talebi ekranında görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3744dc00-fea5-4a5e-ab0a-2f61bd53c092)

##### **1.1.1.1.3.19.Metin(Çoklu Satır) Tipli Parametrik Alanların Listesi**

Eğitim Modülünde Eğitim Talebi menüsünde Metin(Çoklu Satır) tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Metin(Çoklu Satır) yazarak Metin(Çoklu Satır) tipli parametrik alanlar aratılır ve Metin(Çoklu Satır) tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Metin(Çoklu Satır) tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9cd0be4c-e15d-4191-9a77-92c0928f1c1b)

##### **1.1.1.1.3.20.Metin(Çoklu Satır) Tipli Parametrik Alan Tanımlama**

lblT_PARAM6 Metin(Çoklu Satır) tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload399037b0-bd91-4dee-804b-6c5b92047c91) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada2c6bb96-588f-42d6-8a61-b203cce0e4a3)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload87000ad6-0385-4994-a345-799e60f72e00)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada32aa19a-4aa8-4616-bf87-4148a32befcd)(kaydet) butonu tıklanarak Metin(Çoklu Satır) tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade48ddbf5-dcd0-4c35-bab6-9a8f8097b0d6)

Tanımlanan Metin(Çoklu Satır) tipli parametik alan Eğitim Modülünde Yeni Eğitim Talebi ekranında görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcb6e373f-fa77-49bd-ab22-be9ae9e55ab4)

Eğitim Modülünde Yeni Eğitim Talebi ekranında tanımlanan parametrik tipli tüm alanlar;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadac81c010-91cc-4756-8dbb-5978f9cae5dd)

#### **1.1.1.1.4.Eğitim Planlama Modülünde Eğitim Etkinlik Değerlendirmesi Menüsünde Parametrik Alan Tipi Tanımlama**

Eğitim Planlama Modülünde Entegre Yönetim Sistemi\>Eğitim Planlama\>Eğitim Etkinlik Değerlendirmesi menüsünde dil ayarlarında tanımlanan parametrik alanların kısa kodları lblPARAM başlığı ile tanımlı kısa kodlardır. lblPARAM başlığındaki kısa kodlar olan tüm parametrik tipli alanlar tanımlandığında Eğitim Planlama Modülünde Eğitim Etkinlik Değerlendirmesi menüsünde görüntülenir.

##### **1.1.1.1.4.1.Tarih Tipli Parametrik Alanların Listesi**

Eğitim Planlama Modülünde Eğitim Etkinlik Değerlendirmesi menüsünde Tarih tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Tarih yazarak Tarih tipli parametrik alanlar aratılır ve Tarih tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen tarih tipli parametrik alanların alan tanımlaması yapılır.

##### **1.1.1.1.4.2.Tarih Tipli Parametrik Alan Tanımlama**

lblDPARAM1 Tarih tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload399037b0-bd91-4dee-804b-6c5b92047c91) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload785cd4cb-e8f0-4fe9-89d2-9ba443b50a47)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf8029c42-4a03-42da-93b6-556cbd3d0c1d)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada32aa19a-4aa8-4616-bf87-4148a32befcd)(Kaydet) butonu tıklanarak tarih tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload26db7232-3d54-40e1-b573-accd66f05e84)

Tanımlanan Tarih tipli parametik alan Eğitim Planlama Modülünde Eğitim Etkinlik Değerlendirme ekranında görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6683fe6a-c6ae-48eb-a7dd-115c26b99130)

##### **1.1.1.1.4.3.Liste Tipli Parametrik Alanların Listesi**

Eğitim Planlama Modülünde Eğitim Etkinlik Değerlendirmesi menüsünde Liste tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Liste yazarak Liste tipli parametrik alanlar aratılır ve Liste tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Liste tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload43768afb-00f8-421b-862d-56bf1adce70f)

##### **1.1.1.1.4.4.Liste Tipli Parametrik Alan Tanımlama**

lblLPARAM1 Liste tipli parametrik seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload399037b0-bd91-4dee-804b-6c5b92047c91) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8ae773ec-a203-4561-a61c-b94eed980891)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6e0d5ca4-53f7-4f38-b26a-d5f098bd4949)

Liste tipli alanın liste değerlerini girmek için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadac48c8a9-5528-48a6-99a3-3bcc6e064ea4) (Yeni) butonuna tıklanır, liste değerleri yazılır ve kaydedilir. Liste eleman değeri 1 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2e557207-3beb-4390-95bc-dc5f8ebbc788)

Liste eleman değeri 2 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5802f632-a646-4fcc-99ce-992cda67a5b9)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9e41b80c-5576-4227-b7ad-b78a246f254a)

Alanın zorunlu olup, olmayacağı sıra no bilgisi, liste elemanları tanımlanarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada32aa19a-4aa8-4616-bf87-4148a32befcd)(kaydet) butonu tıklanarak liste tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9fcb0447-1b60-4fc6-876b-eb6026e52f5e)

Tanımlanan Liste tipli parametik alan Eğitim Planlama Modülünde Eğitim Etkinlik Değerlendirme ekranında görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload091e9cb9-aee9-474f-aece-73443d8d6f1f)

##### **1.1.1.1.4.5.Ölçü Birimi Parametrik Alanların Listesi**

Eğitim Planlama Modülünde Eğitim Etkinlik Değerlendirmesi menüsünde Ölçü Birimi tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Ölçü Birimi yazarak Ölçü Birimi tipli parametrik alanlar aratılır ve Ölçü Birimi tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Ölçü Birimi tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload309e8b4b-80d2-456e-a503-a0a714ef4a31)

##### **1.1.1.1.4.6.Ölçü Birimi Parametrik Alan Tanımlama**

lblNPARAM1 Ölçü birimi tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload399037b0-bd91-4dee-804b-6c5b92047c91) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb9327544-5b45-4f8c-a573-301366cb658f)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload30dcb373-dbc8-416f-813f-1459a7bdcb3a)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada32aa19a-4aa8-4616-bf87-4148a32befcd)(Kaydet) butonu tıklanarak ölçü birimi tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadca146d9f-b8c1-49bf-929c-094155a92309)

Tanımlanan ölçü birimi tipli parametik alan Eğitim Planlama Modülünde Eğitim Etkinlik Değerlendirme ekranında görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload091e3ed5-a41f-4b55-ba22-bbdc728dad6f)

##### **1.1.1.1.4.7.Parasal Tipli Parametrik Alanların Listesi**

Eğitim Planlama Modülünde Eğitim Etkinlik Değerlendirmesi menüsünde Parasal tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Parasal yazarak Parasal tipli parametrik alanlar aratılır ve Parasal tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Parasal tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadde30304e-811f-498f-89f8-89e055420e79)

##### **1.1.1.1.4.8.Parasal Tipli Parametrik Alan Tanımlama**

lblNPARAM6 Parasal tipli alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload399037b0-bd91-4dee-804b-6c5b92047c91) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload41d4b9ab-d197-4410-b608-c7a88642048e)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload73c0cb00-28e0-4b2e-9058-b645dee46c47)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada32aa19a-4aa8-4616-bf87-4148a32befcd)(Kaydet ) butonu tıklanarak Parasal tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6f9fa683-72f3-4c63-a4a7-06671cd57c97)

Tanımlanan Parasal tipli parametik alan Eğitim Planlama Modülünde Eğitim Etkinlik Değerlendirme ekranında görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload81332d75-09a1-4bef-9d5d-3565c983538a)

##### **1.1.1.1.4.9.Metin Tipli Parametrik Alanların Listesi**

Eğitim Planlama Modülünde Eğitim Etkinlik Değerlendirmesi menüsünde Metin tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Metin yazarak Metin tipli parametrik alanlar aratılır ve Metin tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Metin tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd68fb03a-4718-43f3-af83-9ba69d2a0aeb)

##### **1.1.1.1.4.10.Metin Tipli Parametrik Alan Tanımlama**

lblPARAM1 Metin tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload399037b0-bd91-4dee-804b-6c5b92047c91) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload032aec82-8f85-4f1b-9d47-875778870496)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload308989f3-f304-4fab-852f-41cd72f5567f)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada32aa19a-4aa8-4616-bf87-4148a32befcd)(kaydet) butonu tıklanarak Metin tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d0039ba-694c-4a9a-a98b-811794cab9c2)

Tanımlanan Metin tipli parametik alan Eğitim Planlama Modülünde Eğitim Etkinlik Değerlendirme ekranında görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddd264b99-77af-431e-8359-bf428a27a011)

Eğitim Planlama Modülünde Eğitim Etkinlik Değerlendirme ekranında tanımlanan tüm alanlar;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcb7f4dc3-c0d4-4d22-9bc4-f8738daaa118)

#### **1.1.1.1.5.Eğitim Planlama Modülünde Puan Vereceğim Eğitimler Menüsünde Parametrik Alan Tipi Tanımlaması**

Eğitim Planlama Modülünde Entegre Yönetim Sistemi\>Eğitim Planlama\>Puan Vereceğim Eğitimler menüsünde dil ayarlarında tanımlanan parametrik alanların kısa kodları lbl_K başlığı ile tanımlı kısa kodlardır. lbl_K başlığındaki kısa kodlar olan tüm parametrik tipli alanlar tanımlandığında Eğitim Planlama Modülünde Puan Vereceğim Eğitimler menüsünde görüntülenir.

##### **1.1.1.1.5.1.Tarih Tipli Parametrik Alanların Listesi**

Eğitim Planlama Modülünde Puan Vereceğim Eğitimler menüsünde Tarih tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Tarih yazarak Tarih tipli parametrik alanlar aratılır ve Tarih tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen tarih tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb1227a1e-6d8f-4e09-b1b9-612fce1b249b)

##### **1.1.1.1.5.2.Tarih Tipli Parametrik Alan Tanımlama**

lbl_KDPARAM1 Tarih tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload399037b0-bd91-4dee-804b-6c5b92047c91) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd92212de-e39a-493d-90c7-d19f5023fd41)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload37b94fd2-15ec-4a30-98ce-594259107d86)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada32aa19a-4aa8-4616-bf87-4148a32befcd)(Kaydet) butonu tıklanarak tarih tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddd582b0f-fc06-4320-9827-7170f0290a14)

Tanımlanan Tarih tipli parametik Eğitim Planlama Modülünde Eğitim Değerlendirme ekranında görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9297afa4-b519-4d52-9839-d89b41d21b13)

##### **1.1.1.1.5.3.Liste Tipli Parametrik Alanların Listesi**

Eğitim Planlama Modülünde Puan Vereceğim Eğitimler menüsünde Liste tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Liste yazarak Liste tipli parametrik alanlar aratılır ve Liste tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Liste tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc5d1a761-4c83-483e-995d-4d0cb719a810)

##### **1.1.1.1.5.4.Liste Tipli Parametrik Alan Tanımlama**

lbl_KLPARAM1 Liste tipli parametrik seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload399037b0-bd91-4dee-804b-6c5b92047c91) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8007525c-05dc-4c3b-b002-888093143307)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9734817a-4f22-4f7c-b4a0-6ae86b2bcdb3)

Liste tipli alanın liste değerlerini girmek için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadac48c8a9-5528-48a6-99a3-3bcc6e064ea4) (Yeni) butonuna tıklanır, liste değerleri yazılır ve kaydedilir. Liste eleman değeri 1 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2e557207-3beb-4390-95bc-dc5f8ebbc788)

Liste eleman değeri 2 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5802f632-a646-4fcc-99ce-992cda67a5b9)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf0792b32-1f82-4e17-bf39-4ccc5e7390f5)

Alanın zorunlu olup, olmayacağı sıra no bilgisi, liste elemanları tanımlanarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada32aa19a-4aa8-4616-bf87-4148a32befcd)(kaydet) butonu tıklanarak liste tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade5b5e43f-99b6-498a-8de8-03daec8a33b9)

Tanımlanan Liste tipli parametik Eğitim Planlama Modülünde Eğitim Değerlendirme ekranında görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload55570b93-cf39-4d3a-9fb9-eae6f35beb80)

##### **1.1.1.1.5.5.Ölçü Birimi Parametrik Alanların Listesi**

Eğitim Planlama Modülünde Puan Vereceğim Eğitimler menüsünde Ölçü Birimi tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Ölçü Birimi yazarak Ölçü Birimi tipli parametrik alanlar aratılır ve Ölçü Birimi tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Ölçü Birimi tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2cf689e6-46ff-4676-b857-2bac6c0dd346)

##### **1.1.1.1.5.6.Ölçü Birimi Parametrik Alan Tanımlama**

lbl_KNPARAM1 Ölçü birimi tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload399037b0-bd91-4dee-804b-6c5b92047c91) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaf541bb2-d920-4fa9-9282-30fe4caf267a)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4a89599d-e9ce-47e2-af82-e3a46f22a0e6)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada32aa19a-4aa8-4616-bf87-4148a32befcd)(Kaydet) butonu tıklanarak ölçü birimi tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5f3a7663-5669-4130-8fe0-54ffeb93a4ad)

Tanımlanan ölçü birimi tipli parametik Eğitim Planlama Modülünde Eğitim Değerlendirme ekranında görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfc092e20-65bb-467d-81bd-6307d5aaf134)

##### **1.1.1.1.5.7.Parasal Tipli Parametrik Alanların Listesi**

Eğitim Planlama Modülünde Puan Vereceğim Eğitimler menüsünde Parasal tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Parasal yazarak Parasal tipli parametrik alanlar aratılır ve Parasal tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Parasal tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada82054ed-48df-4442-b15d-48e4e0c714e3)

##### **1.1.1.1.5.8.Parasal Tipli Parametrik Alan Tanımlama**

lbl_KNPARAM6 Parasal tipli alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload399037b0-bd91-4dee-804b-6c5b92047c91) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4a5e839f-62c2-46bc-805f-357006b24401)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8547bbea-6569-4b9c-acf3-7a6e4aa13c28)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada32aa19a-4aa8-4616-bf87-4148a32befcd)(Kaydet ) butonu tıklanarak Parasal tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload11a60371-9a9b-47ae-8c0b-bfbee343320d)

Tanımlanan Parasal tipli parametik Eğitim Planlama Modülünde Eğitim Değerlendirme ekranında görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd65f5a5c-a1b6-426d-b6d8-d53465e5cc2d)

##### **1.1.1.1.5.9.Metin Tipli Parametrik Alanların Listesi**

Eğitim Planlama Modülünde Puan Vereceğim Eğitimler menüsünde Metin tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Metin yazarak Metin tipli parametrik alanlar aratılır ve Metin tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Metin tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0d8f829c-6ee0-40ee-971d-d06632452da5)

##### **1.1.1.1.5.10.Metin Tipli Parametrik Alan Tanımlama**

lbl_KPARAM1Metin tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload399037b0-bd91-4dee-804b-6c5b92047c91) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload27461d8a-94ac-472b-b1c8-ece9eb83d83b)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload205e6058-8060-4942-9943-5b3b3c780472)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada32aa19a-4aa8-4616-bf87-4148a32befcd)(kaydet) butonu tıklanarak Metin tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddf4305b7-800c-4088-b800-87e69540cff4)

Tanımlanan Metin tipli parametik Eğitim Planlama Modülünde Eğitim Değerlendirme ekranında görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc89b1d4d-61e4-4b78-beff-c11dd07ba8ee)

Eğitim Planlama Modülünde Puan Vereceğim Eğitimler menüsünde tanımlanan parametrik tipli tüm alanlar;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcba1c071-9eb0-4e15-93ab-b7103c0db57c)

#### **1.1.1.1.6.Dil ayarlarında Tanımlan Parametrik Alan Tipleri Görüntülen Ekrandan Kaldırma İşlemi**

1.Aşamada parametrik alanın bulunduğu ekran açılır. Eğitim Planlama Modülünde Puan Vereceğim Eğitimler menüsü görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada985e889-34d0-4d4b-ad4c-423a6d9a7449)

2\. Aşamada parametrik alanın bulunduğu ekran görüntülendikten sonra örnekteki herhangi alan seçilerek, Sağ tıkla/Kopyala komutu ile parametrik alanın ismi kopyalanır. Örnek: İstenilen Tarih

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1bd3fada-cacc-43de-9f28-a857546e932d)

3\. Aşamada Sistem Altyapı Tanımları\>BSAT\>Konfigürasyon Ayarları\>Dil ayarları menüsü tıklanarak açılan ekranda Modül olarak Eğitim Planlama Modülü seçilir. Kopyalanan Dil ayarlarından tanımlanan liste tipli parametrik alanı grid ekranında **TR** alanına sağ tıkla/yapıştır komutu ile alanın yapıştırma işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6ec3ddf4-bd5c-4f50-9897-50c47cfff56a)

4.Aşamada Tarih tipli parametrik alan seçilerek alanın içeriği görüntülemek için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload399037b0-bd91-4dee-804b-6c5b92047c91) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0d6c9da1-78ff-4aaa-836d-e7cc9942d06f)

5.Aşamada içeriği görüntülen Tarih tipli alanın değeri silerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada32aa19a-4aa8-4616-bf87-4148a32befcd)(Kaydet) butonu tıklanarak Dil Ayarları menüsünde tanımlı Tarih tipli alanın kaldırma işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfbb197c9-6891-4d97-870a-f8fa68fabf8b)

Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarlarında tanımlanan diğer parametrik alan tiplerin dil ayarları menüsünde kaldırma işlemi aynı şekilde olmaktadır. Eğitim Planlama Modülünde Puan Vereceğim Eğitimler menüsünde tanımlı Tarih Tipli alanın kaldırılmış olduğu görülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9e2861b9-fb5d-4931-a7f4-0e757179fc2d)
