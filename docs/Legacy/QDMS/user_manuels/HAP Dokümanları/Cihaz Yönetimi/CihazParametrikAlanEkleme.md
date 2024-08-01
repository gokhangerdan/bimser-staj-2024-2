---
title: Parametrik Alan Tanımlama İşlemi
description: Parametrik Alan Tanımlama İşlemi Yardım Dokümanı
sidebar_position: 1
---

:::tip Bilgi

İlgili konu başlığına sağ tarafta bulunan navigasyon yardımıyla hızlı bir şekilde ulaşabilirsiniz.

:::


**Cihaz Yönetim Sistem Modülünde Dil Ayarları Menüsünde Parametrik Alan Tanımlama Kullanıcı Yardım Dokümanı**


## **1.Sistem Altyapı Tanımları**

Personel bilgilerinin tanımlandığı ve diğer modüller için gerekli olan altyapının kurgulanmasının yapıldığı menüdür.

## **1.1.Konfigürasyon Ayarları**

**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları

QDMS sisteminde özel ayarların yapıldığı menülerdir. Bu menülerde yapılan ayarlar tüm QDMS kullanıcıları için geçerli olan ortak ayarlardır.

### **1.1.1. Dil Ayarları**

**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları

Dil ayarları menüsünden QDMS üzerinde görülen menülerin isimleri, alanların isimleri değiştirilebilir. Modüllere yeni alanlar eklenebilir. Var olan alanların zorunluluk durumları düzenlenebilir. Alanların ekran üzerinde göründükleri sıralama değiştirilebilir.

### **1.1.1.1.Cihaz Yönetimi Sistemi Modülü Ortak Kullanım İçin Yeni Alan Oluşturma**

Cihaz Yönetimi Sistemi Modülünde Cihaz Tanımlama menüsünde için Diğer Bilgiler sekmesinde Cihaz Kategorileri/Ölçüm Sabitleri ve Kalibrasyon Raporu/Ölçüm Değerleri sekmesinde firmanın istemiş olduğu sistemde olmayan ekstradan alanlar tanımlanabilir. Tanımlanan bu alanlar tüm Cihaz Yönetimi Sistemi Modül kaynakları için geçerlidir. Sistem Altyapı Tanımları/BSAT/ Konfigürasyon Ayarları/Dil Ayarları menüsü tıklanılır. Açılan Dil Ayarları sayfasında Modül alanında “Cihaz Yönetim Sistemi” seçilir ve ekranda Cihaz Yönetimi Sistemi Modülü ile ilgili dil tanımları görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada23498b4-faa5-4626-b0b0-ac9bd59213f9)


Cihaz Yönetim Sistemi Modülünde Entegre Yönetim Sistemi\> Cihaz Yönetim Sistemi\>Cihaz Tanımlama menüsü baz alanılarak Diğer Bilgiler sekmesinde Dil ayarlarından parametrik alan tanımlaması yapılmaktadır.Cihaz Yönetim Sistemi Sistem Altyapı Tanımları\>BSAT\>Konfigürasyon Ayarları\>Dil Ayarlarında tanımlanan alanlar Cihaz Tanımlama menüsünde açılan Cihaz listesi ekranında yeni butonu tıklanarak açılan Cihaz Tanımlama sayfasında Diğer Bilgiler sekmesinde yer aldığı gibi bazı parametrik alanların tanımlamaları da Cihaz Kategorileri ve Kalibrasyon Raporu Tanımlama ekranlarında görüntülenmektedir. Cihaz Kategorileri menüsünde Ölçüm Sabitleri butonu tıklanarak açılan ölçüm sabitleri ekranında Yeni butonu tıklanarak açılan Ölçüm Sabitleri Tanımlama sayfasında tanımlanan dil ayarlarındaki parametrik alanlar görüntülenir. Kalibrasyon Raporu menüsünde ise İşlem Raporu ekranında Ölçüm Değerleri sekmesinde Yeni butonu tıklanarak açılan Ölçüm Değerleri Tanımlama sayfasında Dil ayarlarında tanımlanan parametrik alanlar görüntülenir.

**Cihaz Yönetim Sistemi Modülünde Tanımlanan Parametrik Tipli Alanlar ve Tanımları;**

**1-Tarih tipli**: Takvim alanı eklenilen parametrik alandır. Örnek Kısa Kod: lblDPARAM1(Cihaz Tanımlama/Diğer Bilgiler sekmesinde görüntülenir)

**2-Liste tipli**: Birden fazla liste elemanları arasından tek seçim yaptırılan parametrik alandır. Liste elemanları tanımlanarak, tanımlanan liste elemanlarında seçip yapılır. Örnek Kısa Kod: lblLPARAM1(Cihaz Tanımlama/Diğer Bilgiler sekmesinde görüntülenir), Örnek Kısa Kod: lblOS_LParam1 (Cihaz Kategorisi/Ölçüm Sabitleri Tanımlama ve Kalibrasyon Raporu/Ölçüm Değerleri Tanımlama ekranlarında görüntülenir.)

**3-Personel Tipli:** QDMS personel veri tabanından kişi seçilebilmesini sağlar. Sistem Altyapı Tanımları\>Bsat\>Tanımlama\>Personel Tanımlama menüsünde tanımlı olan Personellerin listesinde seçim yapılır. Örnek Kısa Kod: lblPPARAM1(Cihaz Tanımlama/Diğer Bilgiler sekmesinde görüntülenir)

**4-Metin Tipli**: Elle yazım imkanı veren metin kutucuğu ekleyen parametrik alandır. Örnek Kısa Kod: lblPARAM1(Cihaz Tanımlama/Diğer Bilgiler sekmesinde görüntülenir)

**5- Ölçü Birimi Tipli:** Ölçü olarak veri girişi yaptıran parametrik alandır. Tanımlanan parametrik alanın yanında Ölçü birimleri seçildiği alan çıkar. Ölçü birimleri seçim alanındaki ölçü Birimleri Sistem Altyapı Tanımları\>BSAT\>Tanımlar\>Ölçü Birimleri Tanımlama menüsünde tanımlı olan ölçü birimleridir. Örnek Kısa Kod: lblNPARAM1(Cihaz Tanımlama/Diğer Bilgiler sekmesinde görüntülenir)

**6-Doküman (Çoklu Seçim) Tipli:** QDMS doküman veri tabanından doküman bilgisi çoklu-tekli seçim seçilebilmesini sağlayan parametrik alandır. Örnek Kısa Kod: lblDOCPARAM1(Cihaz Tanımlama/Diğer Bilgiler sekmesinde görüntülenir)

**7- Metin (Çoklu Satır Tipli:** Elle yazım imkanı veren karakter sınırı olmayan çok satırlı metin kutucuğu eklenen parametrik alandır. Örnek Kısa Kod: lblMPARAM1((Cihaz Tanımlama/Diğer Bilgiler sekmesinde görüntülenir)

**8**-**Numerik Tipli:** Sayısal olarak veri girişi yaptıran parametrik alandır. Örnek Kısa Kod: lblOS_NParam1(Cihaz Kategorisi/Ölçüm Sabitleri Tanımlama ve Kalibrasyon Raporu/Ölçüm Değerleri Tanımlama ekranlarında görüntülenir.)

#### **1.1.1.1.1. Cihaz  Yönetimi Sistemi Modülünde Cihaz Tanımlama/Diğer Bilgiler Sekmesinde Parametrik Alan Tanımlama**

##### **1.1.1.1.1.1.Tarih Tipli Parametrik Alanların Listesi**

Cihaz Yönetimi Sistemi Modülünde Entegre Yönetim sistemi\>Cihaz Yönetim Sistemi \>Cihaz Tanımlama menüsünde Diğer Bilgiler sekmesinde Tarih tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Tarih yazarak Tarih tipli parametrik alanlar aratılır ve Tarih tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen tarih tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6cef13f8-1ac3-45f3-85d9-974942a4bea0)

##### **1.1.1.1.1.2.Tarih Tipli Parametrik Alan Tanımlama**

lblDPARAM1 Tarih tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload00108945-8e22-42b9-844c-0733c72b43c1) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload81614b22-cb1a-4921-9813-3cfe01c3fce4)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload26214067-2ea6-41d0-b86f-9c0954ebc18f)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6c6f707c-d02c-489c-9736-6e4b0ee5f3a3)(Kaydet) butonu tıklanarak tarih tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6d6db295-7f49-4929-86f3-877d4c9c4236)

Tanımlanan Tarih tipli parametik alan olan Cihazın Satın Alındığı Tarih alanı Entegre Yönetim Sistemi/Cihaz Yönetim Sistemi/Cihaz Tanımlama menüsünde Diğer Bilgiler Sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload07dee2fa-95ad-4f2a-9b6f-4c03e61d7b29)

##### **1.1.1.1.1.3.Liste Tipli Parametrik Alanların Listesi**

Cihaz Yönetimi Sistemi Modülünde Entegre Yönetim sistemi\>Cihaz Yönetim Sistemi \>Cihaz Tanımlama menüsünde Diğer Bilgiler sekmesinde Liste tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına liste yazarak liste tipli parametrik alanlar aratılır ve liste tipli parametrik alanların listesi Dil Ayarları menüsünde listenir. Listenen liste tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload794b889c-955d-47e5-8fa6-6b2058a6ea9e)

##### **1.1.1.1.1.4. Liste Tipli Parametrik Alan Tanımlama**

lblLPARAM1 Liste tipli parametrik seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload00108945-8e22-42b9-844c-0733c72b43c1) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf6b3e4e8-0c0d-4d79-82a5-cb7f6ffb2dae)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade745f014-ef0b-4fbc-b3bf-dbf79903aad4)

Liste tipli alanın liste değerlerini girmek için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddef0a015-0453-4513-bc34-33e8effe5b1a) (Yeni) butonuna tıklanır, liste değerleri yazılır ve kaydedilir. Liste eleman değeri 1 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada69b6e16-f99a-4ea9-9a18-050d4303b1c9)

Liste eleman değeri 2 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2ca7bc10-3167-4f06-aecc-d0d37d7029f8)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload90c27b34-4339-4531-a931-e15cbba1a329)

Alanın zorunlu olup, olmayacağı sıra no bilgisi ve liste elemanları tanımlanarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6c6f707c-d02c-489c-9736-6e4b0ee5f3a3)(kaydet) butonu tıklanarak liste tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3a0f2611-2dd5-401d-a064-6c5c22c68ce2)

Tanımlanan Liste tipli parametik alan olan Cihazın İşlem Yerleri liste alanı Entegre Yönetim Sistemi/Cihaz Yönetim Sistemi/Cihaz Tanımlama menüsünde Diğer Bilgiler Sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload78060171-475c-4ad8-b99f-6150cc2224a1)

##### **1.1.1.1.1.5.Personel Tipli Parametrik Alanların Listesi**

Cihaz Yönetimi Sistemi Modülünde Entegre Yönetim sistemi\>Cihaz Yönetim Sistemi \>Cihaz Tanımlama menüsünde Diğer Bilgiler sekmesinde Personel tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Personel yazarak Personel tipli parametrik alanlar aratılır ve Personel tipli parametrik alanların listesi Dil Ayarları menüsünde listenir. Listenen Personel tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4e156a85-d5ad-4f77-a7a1-cd218b170d42)

##### **1.1.1.1.1.6. Personel Tipli Parametrik Alan Tanımlama**

lblPPARAM1 Personel tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload00108945-8e22-42b9-844c-0733c72b43c1) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5f0cb311-7171-490f-b626-8e447b0dd1f1)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload466356ad-c348-48d2-9db8-b6519acce21c)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6c6f707c-d02c-489c-9736-6e4b0ee5f3a3)(kaydet) butonu tıklanarak Personel tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadecf7c8aa-4409-4e07-851f-d46e269c573f)

Tanımlanan Personel tipli parametik alan olan Cihazın Bakım Sorumlusu alanı Entegre Yönetim Sistemi/Cihaz Yönetim Sistemi/Cihaz Tanımlama menüsünde Diğer Bilgiler Sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5805d160-83ab-4761-9c52-0a3eaad0c304)

Cihazın Bakım Sorumlusu personel tipli parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada54c699f-77ff-4310-bb0f-05fde8360d3a)(seç) butonu tıklanıldığında sistemde tanımlı personel listesinde seçim yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbdde3ce9-bf07-4000-9fca-b9aefb5c6d4e)

##### **1.1.1.1.1.7. Metin Tipli Parametrik Alanların Listesi**

Cihaz Yönetimi Sistemi Modülünde Entegre Yönetim sistemi\>Cihaz Yönetim Sistemi \>Cihaz Tanımlama menüsünde Diğer Bilgiler sekmesinde Metin tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Metin yazarak Metin tipli parametrik alanlar aratılır ve Metin tipli parametrik alanların listesi Dil Ayarları menüsünde listenir. Listenen Metin tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload59fda62e-1d20-479b-878a-889f249c61f3)

##### **1.1.1.1.1.8. Metin Tipli Parametrik Alan Tanımlama**

lblPARAM1 Metin tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload00108945-8e22-42b9-844c-0733c72b43c1) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6917d158-54c6-434d-a94b-9b92ebb87b13)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade2ca20d1-5278-4cc2-b068-2943b9e0681b)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6c6f707c-d02c-489c-9736-6e4b0ee5f3a3)(kaydet) butonu tıklanarak Metin tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload347d2b22-fff0-4da2-8310-4549ee4cb6dd)

Tanımlanan Metin tipli parametik alan olan Cihaz Bakım Açıklaması alanı Entegre Yönetim Sistemi/Cihaz Yönetim Sistemi/Cihaz Tanımlama menüsünde Diğer Bilgiler Sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfe9b2b13-8357-4ebd-88d2-7cf27644571a)

##### **1.1.1.1.1.9.Ölçü Birimi Tipli Parametrik Alanların Listesi**

Cihaz Yönetimi Sistemi Modülünde Entegre Yönetim sistemi\>Cihaz Yönetim Sistemi \>Cihaz Tanımlama menüsünde Diğer Bilgiler sekmesinde Ölçü Birimi tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Ölçü Birimi yazarak Ölçü Birimi tipli parametrik alanlar aratılır ve Ölçü Birimi tipli parametrik alanların listesi Dil Ayarları menüsünde listenir. Listenen Ölçü Birimi tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload85e6fd15-f564-4d64-88f7-47f867f8c123)

##### **1.1.1.1.1.10. Ölçü Birimi Parametrik Alan Tanımlama**

lblNPARAM1 Ölçü Birimi tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload00108945-8e22-42b9-844c-0733c72b43c1) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada92bd5cd-c618-4251-8a17-6f5e67b8a8d6)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade6af2b98-440f-456c-b12a-29fc5a86dcaf)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6c6f707c-d02c-489c-9736-6e4b0ee5f3a3)(kaydet) butonu tıklanarak Ölçü Birimi tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload623789b3-ab6b-48b7-b62b-5c5dd4e5f17b)

Tanımlanan Ölçü Birimi tipli parametik zorunlu alan olan Cihazın Ölçü Birimi alanı Entegre Yönetim Sistemi/Cihaz Yönetim Sistemi/Cihaz Tanımlama menüsünde Diğer Bilgiler Sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2960da3b-deb3-4b6e-a26a-361d8edcd9b7)

##### **1.1.1.1.1.11. Doküman (Çoklu Secim) Tipli Parametrik Alanların Listesi**

Cihaz Yönetimi Sistemi Modülünde Entegre Yönetim sistemi\>Cihaz Yönetim Sistemi \>Cihaz Tanımlama menüsünde Diğer Bilgiler sekmesinde Doküman (Çoklu Secim) tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Doküman (Çoklu Secim) yazarak Doküman (Çoklu Secim) tipli parametrik alanlar aratılır ve Doküman (Çoklu Secim) tipli parametrik alanların listesi Dil Ayarları menüsünde listenir. Listenen Doküman (Çoklu Secim) tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd73961e7-7ba5-4fba-895c-6e2e73633752)

##### **1.1.1.1.1.12. Doküman (Çoklu Seçim) Tipli Parametrik Alan Tanımlama**

lblDOCPARAM1 Doküman (Çoklu Seçim) tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload00108945-8e22-42b9-844c-0733c72b43c1) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaf630ff7-5a9e-450b-aa29-136fa564c72c)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaff58cd2-5263-4914-90b8-dbb874a58eb7)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6c6f707c-d02c-489c-9736-6e4b0ee5f3a3)(kaydet) butonu tıklanarak Doküman (Çoklu Seçim) tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload17d07dda-f329-4c23-9423-83eb1cf863ca)

Tanımlanan Doküman (Çoklu Seçim) tipli parametik alan olan Dokümanlar alanı Entegre Yönetim Sistemi/Cihaz Yönetim Sistemi/Cihaz Tanımlama menüsünde Diğer Bilgiler Sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload36c2ac45-ee5b-4179-8832-ea1207e8bf7a)

Dil ayarlarında tanımlanan Doküman (Çoklu Seçim) alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada266db20-cee0-4fd2-a36d-f68538ecadf2) (ekle) butonu tıklanıldığında sistemde tanımlı doküman listesinden tekli ve çoklu seçim yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4c1da35f-bdfe-4cf5-aa8c-222ee21e2c88)

##### **1.1.1.1.1.13. Metin ( Çoklu Satır)Tipli Parametrik Alan Listesi**

Cihaz Yönetimi Sistemi Modülünde Entegre Yönetim sistemi\>Cihaz Yönetim Sistemi \>Cihaz Tanımlama menüsünde Diğer Bilgiler sekmesinde Metin (Çoklu Satır) tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Metin (Çoklu Satır) yazarak Metin (Çoklu Satır) tipli parametrik alanlar aratılır ve Metin (Çoklu Satır) tipli parametrik alanların listesi Dil Ayarları menüsünde listenir. Listenen Metin (Çoklu Satır) tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada8ed1faf-af8c-4d11-8dff-5d8174213d73)

##### **1.1.1.1.1.14. Metin (Çoklu Satır) Tipli Parametrik Alan Tanımlama**

lblMPARAM1 Metin (Çoklu Satır) tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload00108945-8e22-42b9-844c-0733c72b43c1) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload461d7329-41ef-45a7-b74c-dc0d1eb2b70a)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc39f4ac-10c4-4822-b846-e4e6d632d918)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6c6f707c-d02c-489c-9736-6e4b0ee5f3a3)(kaydet) butonu tıklanarak Metin (Çoklu Satır) tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5e2b656d-67e3-4797-9bc2-b86a6799a5b3)

Tanımlanan Metin (Çoklu Satır) tipli parametik alan olan Cihaz Bakım İşlemlerin Detayı alanı Entegre Yönetim Sistemi/Cihaz Yönetim Sistemi/Cihaz Tanımlama menüsünde Diğer Bilgiler Sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5456afae-b73c-49f5-b64e-c7aac33a9d90)

Cihaz Yönetim Sistemi Modülünde Cihaz Tanımlama/Diğer Bilgiler sekmeside Tanımlanan tüm parametrik Alanlar;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload733fdf24-b858-4d42-ae93-8c1c193c8bea)

#### **1.1.1.1.2. Cihaz Yönetim Sistemi Modülünde Cihaz Kategorisi ve İşlem Raporu Ekranlarında Parametrik Alan Tanımlama**

##### **1.1.1.1.2.1. Liste Tipli Parametrik Alanların Listesi**

Cihaz Yönetimi Sistemi Modülünde Sistem Altyapı Tanımları\>CihazYönetim Sistemi\>Cihaz Kategorileri menüsünde ölçüm Sabitleri butonu tıklanınca açılan Ölçüm Sabitleri ekranında ve Entegre Yönetim Sistemi\>Cihaz Yönetim Sistemi\>İşlem Gerçekleştirme menüsünde Kalibrasyon Raporu tıklanınca açılan İşlem Raporu ekranında Ölçüm Değerleri sekmesinde liste tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Liste yazarak Liste tipli parametrik alanlar aratılır ve Liste tipli parametrik alanların listesi Dil Ayarları menüsünde listenir. Listenen Liste tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5765247b-545f-48c3-bae7-f2f0bda9a3f8)

##### **1.1.1.1.2.2. Liste Tipli Parametrik Alan Tanımlama**

lblOS_LParam1 Liste tipli alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload00108945-8e22-42b9-844c-0733c72b43c1) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaf471890-0145-470e-beec-e4c466aca156)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload765bf2c0-766f-423f-ac2b-132037bd498c)

Liste tipli alanın liste değerlerini girmek için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddef0a015-0453-4513-bc34-33e8effe5b1a) (Yeni) butonuna tıklanır, liste değerleri yazılır ve kaydedilir. Liste elaman değeri 1 için liste elemanı tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf5032c6e-7668-4760-b90d-c1bf401becc5)

Liste eleman değeri 2 için liste elemanı tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload54ef6091-8486-4c9f-8d25-0b021127bd45)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload50d643c6-89e4-4ad1-aa9a-3cba597942c1)

Alanın zorunlu olup, olmayacağı sıra no bilgisi ve liste elemanların tanımlanarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6c6f707c-d02c-489c-9736-6e4b0ee5f3a3)(kaydet) butonu tıklanarak liste tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada44608ec-f480-4f42-b4a9-66510fdbd2a2)

Tanımlanan Liste tipli parametik alan olan Ölçüm değerleri alanı ilk olarak Sistem Altyapı Tanımları\>Cihaz Yönetim Sistemi\>Cihaz Kategorileri menüsünde ölçüm sabitleri butonu tıklatıldığında açılan ölçüm Sabitleri Tanımlama ekranında görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5495cb61-54d1-4ca9-8dbf-08aa1676f83a)

Tanımlanan Liste tipli parametik alan olan Ölçüm değerleri alanı ikinci olarak Entegre Yönetim Sistemi\>Cihaz Yönetim Sistemi\>İşlem Gerçekleştirme menüsünde Kalibrasyon Raporu tıklatıldığında açılan İşlem Raporunda ölçüm Değerleri sekmesinde açılan ölçüm Değerleri Tanımlama ekranında görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload06bfb72b-a3bf-41b7-b949-bce99ba9abb6)

##### **1.1.1.1.2.3. Nümerik Tipli Parametrik Alanların Listesi**

Cihaz Yönetimi Sistemi Modülünde Sistem Altyapı Tanımları\>CihazYönetim Sistemi\>Cihaz Kategorileri menüsünde ölçüm Sabitleri butonu tıklanınca açılan Ölçüm Sabitleri ekranında ve Entegre Yönetim Sistemi\>Cihaz Yönetim Sistemi\>İşlem Gerçekleştirme menüsünde İşlem Raporu tıklanınca açılan İşlem Raporu ekranında Ölçüm Değerleri sekmesinde Numerik tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Numerik yazarak Numerik tipli parametrik alanlar aratılır ve Numerik tipli parametrik alanların listesi Dil Ayarları menüsünde listenir. Listenen Numerik tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf45eb81a-abcd-4b8c-8f11-9fc62cbd001f)

##### **1.1.1.1.2.4. Numerik Tipli Parametrik Alan Tanımlama**

lblOS_NParam1 Numerik tipli parametrik alanı seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload00108945-8e22-42b9-844c-0733c72b43c1) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf5ff9a40-3ba0-400a-95cf-6f426c43290c)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1d45c64d-1c04-4404-add5-9c2e3846b694)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6c6f707c-d02c-489c-9736-6e4b0ee5f3a3)(kaydet) butonu tıklanarak numerik tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf2f9f754-95ed-414a-adca-cd8aa5d3ee51)

Tanımlanan Numerik tipli parametik alan olan Cihazın Seri Nosu alanı ilk olarak Sistem Altyapı Tanımları\>Cihaz Yönetim Sistemi\>Cihaz Kategorileri menüsünde ölçüm sabitleri butonu tıklanıldığında açılan ölçüm Sabitleri Tanımlama ekranında görüntülenir.

Ölçüm Sabitlerinde Tanımlanan Tüm Parametrik alanlar ;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6ef0ed38-1c79-4057-bc9c-21083bfbe1c1)

Tanımlanan Liste tipli parametik alan olan Ölçüm değerleri alanı ikinci olarak Entegre Yönetim Sistemi\>Cihaz Yönetim Sistemi\>İşlem Gerçekleştirme menüsünde Kalibrasyon Raporu tıklatıldığında açılan İşlem Raporunda ölçüm Değerleri sekmesinde açılan ölçüm Değerleri Tanımlama ekranında görüntülenir.

Ölçüm Değerlerinde Tanımlanan Tüm Parametrik alanlar ;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade2b5700a-2668-408c-b18e-18310a0a383b)

##### **1.1.1.1.1.3. Dil ayarlarında Tanımlan Parametrik Alan tipleri Görüntülen Ekrandan Kaldırma İşlemi**

1.Aşamada parametrik alanın bulunduğu ekran açılır. Örnekte Cihaz Tanımlama/Diğer bilgiler sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1164717f-2310-4266-84ba-03b18f025045)

2\. Aşamada Parametrik Alanın bulunduğu ekran görüntülendikten sonra örnekteki herhangi alan seçilerek, Sağ tıkla/Kopyala komutu ile parametrik alanın ismi kopyalanır. Örnek:Cihaz Bakım Sorumlusu personel tipli parametrik alan

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1c518e49-4ba5-4459-8720-e0fd8af9c251)

3\. Aşamada Sistem Altyapı Tanımları\>BSAT\>Konfigürasyon Ayarları\>Dil ayarları menüsü tıklanarak açılan ekranda Modül olarak Cihaz Yönetim Sistemi Modülü seçilir. Kopyalanan Dil ayarlarından tanımlanan Personel tipli parametrik alanı grid ekranında **TR** alanına sağ tıkla/yapıştır komutu ile alanın yapıştırma işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf25903ae-5e9d-44aa-81a9-1d394a0a770a)

4.aşamada Personel Tipli tipli parametrik alan seçilerek alanın içeriği görüntülemek için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload00108945-8e22-42b9-844c-0733c72b43c1) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf1cc99c4-8de4-42f8-9f40-2b7f38c3e02f)

5.Aşamada içeriği görüntülen personel tipli alanın değeri kısmı silerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6c6f707c-d02c-489c-9736-6e4b0ee5f3a3)(Kaydet) butonu tıklanarak Dil Ayarları menüsünde tanımlı personel tipli alanın kaldırma işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload05e60876-79c4-4218-8b74-678df2c19634)

Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarlarında tanımlanan diğer parametrik alan tiplerin dil ayarları menüsünde kaldırma işlemi aynı şekilde olmaktadır.

Entegre Yönetim Sistemi\>Cihaz Yönetim Sistem\>Cihaz Tanımlama menüsünde diğer bilgiler sekmesinde Cihaz Bakım Sorumlu Personel Tipli parametrik alanın kaldırılmış olduğu görülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload16a20be9-4893-4b47-87d1-ec81612df892)
