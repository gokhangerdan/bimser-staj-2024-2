---
title: Raporlara Parametrik Alan Ekleme İşlemi ve Genel Tag Listesi
description: Raporlara Parametrik Alan Ekleme İşlemi ve Genel Tag Listesi Kullanıcı Yardım Dokümanı
sidebar_position: 2
---

:::tip Bilgi

İlgili konu başlığına sağ tarafta bulunan navigasyon yardımıyla hızlı bir şekilde ulaşabilirsiniz.

:::


**Cihaz Yönetim Sistemi Modülünde Raporlara Parametrik Alan Ekleme İşlemi ve Genel Tag Listesi Kullanıcı Yardım Dokümanı**


## **1.Cihaz Yönetim Sistemi Modülünde Raporlara Parametrik Alan Ekleme İşlemi ve Raporlarda Kullanılan Taglar**

Cihaz Yönetim Sistemi Modülünde tüm raporlarına parametrik alan ekleme işlemi yapılmaktdır. Planlanan İşlemler Raporuna parametrik alan ekleme işlem basamakları ve Cihaz Yönetim Sistemi Modülünde kullanılan taglerin (kısa kodların) listesi bu yardım dokümanında yer almaktadır.

## **1.1. Cihaz Yönetim Sistemi Modülünde Parametrik Alan Tiplerinin Planlanan İşlemler Raporunda Gösterimi**

Cihaz Yönetim Sistemi Modülü raporlarında Planlanan İşlemler raporuna eklenen parametrik alanların raporda gösterilme işlemi için öncelikle dil ayarları menüsünde parametrik alan tiplerinin tanımlama işlemi yapmak gerekiyor. Dil ayarlarında metin, liste, tarih gibi parametrik alan tiplerinin tanımlama işlemi yapılır. Bu tanımlanan parametrik alanlar Entegre Yönetim Sistemi\> Cihaz Yönetim Sistemi \>Cihaz Tanımlama menüsünde açılan Cihaz listesi ekranında Diğer bilgiler sekmelerinde görüntülenir. Bu sekmede tanımlanan parametrik alan tiplerinin bilgisi girilir. Açılan diğer bilgiler sekmesinde tanımlanan alanların bilgi girişleri yapıldıktan sonra Rapor Formatları Düzenleme menüsüne gidilir. Rapor formatların düzenleme menüsünde Planlanan İşlemler raporun Rapor formatı “PLAN_ISLEM_RAPORU.xls” indirilir. İndirilenen “PLAN_ISLEM_RAPORU.xls” dil ayarlarından tanımlanan parametrik alanların tag’leri yazılır. Örneğin: Cihaz Tanımlama ekranında Diğer bilgiler sekmesine eklenen metin tipli parametrik alan tipi lblPARAM1 için <PARAM1\> alan kodunun lbl olmadan tag içerisine yazılır. Bu şekilde Cihaz Tanımlama Diğer bilgiler sekmesindeki parametrik alan tipleri tag şeklinde Rapor formatına yazılır. Rapor formatına parametrik alanların tag şeklinde yazıldıktan Rapor format “PLAN_ISLEM_RAPORU.xls” aynı isimde bilgisayara kaydedilir. Kaydedilen aynı isimde Planlanan İşlemler Rapor formatı Rapor formatları düzenleme menüsünde tekrar sisteme yüklenir. Planlanan İşlemler Rapor formatının yükleme işleminde sonra Entegre Yönetim Sistemi\>Cihaz Yönetim Sistemi\>Raporlar\> Planlanan İşlemler Raporu menüsüne gidilir. Açılan Planlanan Kalibrasyonlar Raporu ekranında arama filtrelerinde Cihaz Kodu alanına Cihazın kodu yazılırak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcc09736f-5c0c-4ae6-9edd-aa10dd634ff5)(Excel aktar) butonu tıklanır. Excel format alınan raporda parametrik alanların taglerinin bulunduğu kısımda girilen Cihaz Tanımlama ekranında Diğer bilgiler sekmesinde alan bilgilerinin geldiği ve taglerin çalıştığı görülür.

### **Cihaz Yönetim Sistemi Modülünde Parametrik Alan Tanımlama**

Cihaz Yönetimi Sistemi Modülünde Cihaz Tanımlama menüsünde için Diğer Bilgiler sekmesinde Cihaz Kategorileri/Ölçüm Sabitleri ve Kalibrasyon Raporu/Ölçüm Değerleri sekmesinde firmanın istemiş olduğu sistemde olmayan ekstradan alanlar tanımlanabilir. Tanımlanan bu alanlar tüm Cihaz Yönetimi Sistemi Modül kaynakları için geçerlidir. Sistem Altyapı Tanımları/BSAT/ Konfigürasyon Ayarları/Dil Ayarları menüsü tıklanılır. Açılan Dil Ayarları sayfasında Modül alanında “Cihaz Yönetim Sistemi” seçilir ve ekranda Cihaz Yönetimi Sistemi Modülü ile ilgili dil tanımları görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf375097e-14be-4df2-9b6b-eaa231b27c2d)

Cihaz Yönetim Sistemi Modülünde diğer bilgiler sekmelerinde tanımlanan parametrik alan tipleri tanımlanarak bu alanların tag şeklinde Planlanan İşlemler raporunun formatına (PLAN_ISLEM_RAPORU.xls) eklenerek Planlanan İşlemler raporuna bu parametrik alan tiplerinin bilgilerin basılması sağlanılır. Parametrik alan tiplerinin tagleri Rapor Formatları düzenleme menüsünde indirilen rapor format şablonuna eklenir. Aynı şekilde diğer Raporları düzenlemek için ise;

Sistem Altyapı Tanımları\> BSAT \> KONFİGÜRASYON AYARLARI \> Rapor Formatları Düzenleme menüsüne tıklanılır.

1-Entegre Yönetim Sistemi \> Cihaz Yönetim Sistemi\> İşlem Gerçekleştirme \> Rapor Hazırla butonu ile alınan "KAL_RAP" isimli rapor formatı şablonu

2.Entegre Yönetim Sistemi \> Cihaz Yönetim Sistemi \> Cihaz Tanımlama \> Excel’e Aktar ile alınan Cihaz listesi için "CIHAZ_RAP" isimli rapor formatı şablonunu

3-Entegre Yönetim Sistemi \> Cihaz Yönetim Sistemi \> Raporlar \> İşemri Raporu için; KAL_ISEMRI_RAP.xls isimli rapor formatı şablonu

4-Entegre Yönetim Sistemi \> Cihaz Yönetim Sistemi \> Raporlar \> İşemri Detay Raporu için; KAL_ISEMRI_RAP_DETAY.xls isimli rapor formatı şablonu

5-Entegre Yönetim Sistemi \> Cihaz Yönetim Sistemi \> Raporlar \> Maliyet Raporu için; KAL_MALIYET_RAP.xls isimli rapor formatı şablonu

Belirtilen rapor formatları şablonlarını bilgisayarınıza indirerek düzenleyebilirsiniz. Bu düzenleme dil ayarlarında tanımlanan parametrik alan tiplerinin alan tagleri eklenir. Düzenlemenin ardından Rapor Formatları Düzenleme menüsünden aynı isimle sistem rapor formatları şablonları aktarılır. Düzenleme sırasında fazlalık olan sütunları şablondan silebilir. Cihaz Yönetim Sisteminde düzenlenen rapor formatları şablonların raporları alındığında eklenen parametrik alan tiplerinin tagleri çalıştığı ve parametrik alan tiplerinin değerlerin rapora basıldığı görülür.

### **1.1.1.1.Cihaz Yönetimi Sistemi Modülünde Cihaz Tanımlama/Diğer Bilgiler Sekmesinde Parametrik Alan Tanımlama**

Cihaz Yönetim Sistemi modülünde dil ayarları menüsünde Cihaz Tanımlama ekranında Diğer bilgiler sekmesi için parametrik alan tanımlama işlemi yapılır. Aşağıdaki tabloda Cihaz tanımlama ekranında Diğer bilgiler sekmesinde eklenecek parametrik alan tiplerinin ve rapor formatına eklenecek tag ‘lerin listesi yer almaktadır.

| **Parametrik Alan**     | **Parametrik Alan Tipi** | **Parametrik Alanların Tag’leri**            |
|-------------------------|--------------------------|----------------------------------------------|
|  lblPARAM1...lblPARAM10 |  Metin                   |  <PARAM1\>...<PARAM10\>                    |
|  lblMPARAM1…lblMPARAM2  | Metin(Çoklu Satır)       |  <MPARAM1\>…<MPARAM2\>                     |
|  lblLPARAM1…lblLPARAM8  |  Liste                   |  <LPARAM1\>…<LPARAM8\>                     |
|  lblDPARAM1…lblDAPAM3   |  Tarih                   |  <DATETIME1\>…<\<DATETIME3\>               |
|  lblPPARAM1… lblPPARAM3 |  Personel                |  \<PPARAM1\>… <PPARAM3\>                    |
|  lblNPARAM1… lblNPARAM4 | Ölçü Birimi              |  <\<NPARAM1_BIRIM\>\>… <\<NPARAM1_BIRIM4\> |

#### **1.1.1.1.1.Metin Tipli Parametrik Alanların Listesi**

Cihaz Yönetimi Sistemi Modülünde Entegre Yönetim sistemi\>Cihaz Yönetim Sistemi \>Cihaz Tanımlama menüsünde Diğer Bilgiler sekmesinde Metin tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Metin yazarak Metin tipli parametrik alanlar aratılır ve Metin tipli parametrik alanların listesi Dil Ayarları menüsünde listenir. Listenen Metin tipli parametrik alanların alan tanımlaması yapılır. Bu metin tipli alanın daha sonra Planlanan İşlemler raporunda gösterilme işleminde tag’ini kullanmak için tanımlama işlemi yapılacaktır. Bu alan tanımlaması yapılan Metin tipli parametrik alanları lbl kısa kodu kaldırarak:

<PARAM1\>…<PARAM10\> şeklinde Planlanan İşlemler Raporu formatına tag şeklinde eklendiğinde Cihaz Tanımlama ekranında Diğer bilgiler sekmesinde Metin tipli alanların girilen değerleri bilgisi ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcee3feb9-8573-407c-a77e-1567dd3783f2)(Excel aktar) butonu tıklanarak alınan Excel formatındaki rapora basılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload36e97638-7167-4fd3-83f4-2ac6493a883e)

#### **1.1.1.1.2. Metin Tipli Parametrik Alan Tanımlama**

Rapor formatına eklenecek Metin tipli parametrik bir alan tanımlaması yapılır. lblPARAM2 Metin tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7fe4df0a-c37f-4052-9a50-cee0be537901) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload409a2875-4e96-4e3f-9aa9-aa11a7a3fa6e)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload637770a0-983e-4867-9b09-8c75c231d077)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6e40d7f8-040a-441d-81f4-adff831620ba)(kaydet) butonu tıklanarak Metin tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9e90d0bd-4615-4b53-81bf-49d71f2148f1)

Tanımlanan Metin Tipli parametrik alan Entegre Yönetim Sistemi\> Cihaz Yönetim Sistemi\> Cihaz Tanımlama menüsünde açılan Cihaz Listesi ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload031d5991-437d-46d3-b67c-42e48a2609d9)(Yeni) butonu tıklatıldığında açılan Cihaz tanımlama ekranında Diğer bilgiler sekmesinde görüntülenir. Tanımlanan metin tipli parametrik alanın “lblPARAM2” lbl kısa kod kısmı kaldırılarak Planlanan İşlemler Raporunun rapor formatına <PARAM2\> tag şeklinde bilgisi yazılır. Cihaz tanımlama işleminde bu metin tipli alanın bilgisi girildiğinde Planlanan İşlemler alındığında Metin tipli alanın girilen bilgileri rapora basılacaktır.

#### **1.1.1.1.3.Liste Tipli Parametrik Alanların Listesi**

Cihaz Yönetimi Sistemi Modülünde Entegre Yönetim sistemi\>Cihaz Yönetim Sistemi \>Cihaz Tanımlama menüsünde Diğer Bilgiler sekmesinde liste tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına liste yazarak liste tipli parametrik alanlar aratılır ve liste tipli parametrik alanların listesi Dil Ayarları menüsünde listenir. Listenen liste tipli parametrik alanların alan tanımlaması yapılır. Bu liste tipli alanın daha sonra Planlanan İşlemler raporunda gösterilme işleminde tag’ini kullanmak için tanımlama işlemi yapılacaktır. Bu alan tanımlaması yapılan liste tipli parametrik alanları lbl kısa kodu kaldırarak:

<LPARAM1\>…<LPARAM8\> şeklinde Planlanan İşlemler Raporu formatına tag şeklinde eklendiğinde Cihaz Tanımlama ekranında Diğer bilgiler sekmesinde liste tipli alanların girilen değerleri bilgisi ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcee3feb9-8573-407c-a77e-1567dd3783f2)(Excel aktar) butonu tıklanarak alınan Excel formatındaki rapora basılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload33725f9a-0d8b-4b75-bc1d-1fcab753822b)

#### **1.1.1.1.4. Liste Tipli Parametrik Alan Tanımlama**

Rapor formatına eklenecek liste tipli parametrik bir alan tanımlaması yapılır. lblLPARAM1 Liste tipli parametrik seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7fe4df0a-c37f-4052-9a50-cee0be537901) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd11fbbca-4037-47f5-b1ac-f91cc7adb699)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload00cf6bb9-27b5-41af-82a4-41be3656f7c4)

Liste tipli alanın liste değerlerini girmek için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada1460bd4-86bc-45e7-96ed-3b8e51bed356) (Yeni) butonuna tıklanır, liste değerleri yazılır ve kaydedilir. Liste eleman değeri 1 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8938be1c-3a75-4b12-8411-a213f918b60e)

Liste eleman değeri 2 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload324f9699-ecec-4198-a0fa-868274df5374)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb574a24b-345d-4b4d-a556-c3348bd01c86)

Alanın zorunlu olup, olmayacağı sıra no bilgisi ve liste elemanları tanımlanarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6e40d7f8-040a-441d-81f4-adff831620ba)(kaydet) butonu tıklanarak liste tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcaad21d3-3046-4185-9a18-193df2ccf855)

Tanımlanan Liste Tipli parametrik alan Entegre Yönetim Sistemi\> Cihaz Yönetim Sistemi\> Cihaz Tanımlama menüsünde açılan Cihaz Listesi ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload031d5991-437d-46d3-b67c-42e48a2609d9)(Yeni) butonu tıklatıldığında açılan Cihaz tanımlama ekranında Diğer bilgiler sekmesinde görüntülenir. Tanımlanan liste tipli parametrik alanın “lblLPARAM1” lbl kısa kod kısmı kaldırrarak Planlanan İşlemler Raporunun rapor formatına <LPARAM1\> tag şeklinde bilgisi yazılır. Cihaz tanımlama işleminde bu liste tipli alanın bilgisi girildiğinde Planlanan İşlemler alındığında liste tipli alanın girilen bilgileri rapora basılacaktır.

#### **1.1.1.1.5.Personel Tipli Parametrik Alanların Listesi**

Cihaz Yönetimi Sistemi Modülünde Entegre Yönetim sistemi\>Cihaz Yönetim Sistemi \>Cihaz Tanımlama menüsünde Diğer Bilgiler sekmesinde Personel tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Personel yazarak Personel tipli parametrik alanlar aratılır ve Personel tipli parametrik alanların listesi Dil Ayarları menüsünde listenir. Listenen Personel tipli parametrik alanların alan tanımlaması yapılır. Bu Personel tipli alanın daha sonra Planlanan İşlemler raporunda gösterilme işleminde tag’ini kullanmak için tanımlama işlemi yapılacaktır. Bu alan tanımlaması yapılan Personel tipli parametrik alanları lbl kısa kodu kaldırarak:

<PPARAM1\>…<PPARAM3\> şeklinde Planlanan İşlemler Raporu formatına tag şeklinde eklendiğinde Cihaz Tanımlama ekranında Diğer bilgiler sekmesinde Personel tipli alanların girilen değerleri bilgisi ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcee3feb9-8573-407c-a77e-1567dd3783f2)(Excel aktar) butonu tıklanarak alınan Excel formatındaki rapora basılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload988ed890-22d4-4545-82b5-57c78a84bfbb)

#### **1.1.1.1.6. Personel Tipli Parametrik Alan Tanımlama**

Rapor formatına eklenecek liste tipli parametrik bir alan tanımlaması yapılır. lblPPARAM1 Personel tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7fe4df0a-c37f-4052-9a50-cee0be537901) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9badb8f0-794d-44ea-a1c7-009f944f81e5)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb597a5a-2511-475b-8806-c9561043012c)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6e40d7f8-040a-441d-81f4-adff831620ba)(kaydet) butonu tıklanarak Personel tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf5b422c7-431d-4635-b03f-eb07f6ea196f)

Tanımlanan Personel Tipli parametrik alan Entegre Yönetim Sistemi\> Cihaz Yönetim Sistemi\> Cihaz Tanımlama menüsünde açılan Cihaz Listesi ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload031d5991-437d-46d3-b67c-42e48a2609d9)(Yeni) butonu tıklatıldığında açılan Cihaz tanımlama ekranında Diğer bilgiler sekmesinde görüntülenir. Tanımlanan Personel tipli parametrik alanın “lbPPARAM1” lbl kısa kod kısmı kaldırılarak Planlanan İşlemler Raporunun rapor formatına <PPARAM1\> tag şeklinde bilgisi yazılır. Cihaz tanımlama işleminde bu Personel tipli alanın bilgisi girildiğinde Planlanan İşlemler alındığında Personel tipli alanın girilen bilgileri rapora basılacaktır.

#### **1.1.1.1.7.Tarih Tipli Parametrik Alanların Listesi**

Cihaz Yönetimi Sistemi Modülünde Entegre Yönetim sistemi\>Cihaz Yönetim Sistemi \>Cihaz Tanımlama menüsünde Diğer Bilgiler sekmesinde Tarih tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Tarih yazarak Tarih tipli parametrik alanlar aratılır ve Tarih tipli parametrik alanların listesi Dil Ayarları menüsünde listenir. Listenen Tarih tipli parametrik alanların alan tanımlaması yapılır. Bu Tarih tipli alanın daha sonra Planlanan İşlemler raporunda gösterilme işleminde tag’ini kullanmak için tanımlama işlemi yapılacaktır. Bu alan tanımlaması yapılan Tarih tipli parametrik alanları:

<DATETIME1\>…<DATETIME3\> şeklinde Planlanan İşlemler Raporu formatına tag şeklinde eklendiğinde Cihaz Tanımlama ekranında Diğer bilgiler sekmesinde Tarih tipli alanların girilen değerleri bilgisi ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcee3feb9-8573-407c-a77e-1567dd3783f2)(Excel aktar) butonu tıklanarak alınan Excel formatındaki rapora basılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload30b35088-68a1-46a9-9a80-802b3aad317e)

#### **1.1.1.1.8.Tarih Tipli Parametrik Alan Tanımlama**

Rapor formatına eklenecek liste tipli parametrik bir alan tanımlaması yapılır. lblDPARAM1 Tarih tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7fe4df0a-c37f-4052-9a50-cee0be537901) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload180827c4-762c-42a1-a2e0-89ac9aa216a2)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload02dd5d8e-7b23-47e5-b5d2-3cb16d975382)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6e40d7f8-040a-441d-81f4-adff831620ba)(Kaydet) butonu tıklanarak tarih tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload77701270-0860-4a8c-bb61-5180a325cc3c)

Tanımlanan Tarih Tipli parametrik alan Entegre Yönetim Sistemi\> Cihaz Yönetim Sistemi\> Cihaz Tanımlama menüsünde açılan Cihaz Listesi ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload031d5991-437d-46d3-b67c-42e48a2609d9)(Yeni) butonu tıklatıldığında açılan Cihaz tanımlama ekranında Diğer bilgiler sekmesinde görüntülenir. Tanımlanan Tarih tipli parametrik alanın “lblDPARAM1” için Planlanan İşlemler Raporunun rapor formatına <DATETIME1\> tag şeklinde bilgisi yazılır. Cihaz tanımlama işleminde bu Tarih tipli alanın bilgisi girildiğinde Planlanan İşlemler alındığında Tarih tipli alanın girilen bilgileri rapora basılacaktır.

Diğer parametrik alan tiplerinin aynı şekilde tanımlama işlemi yapılır.

\-Metin (çoklu Satır) parametrik alan “Cihaz Bakım işlemleri Detayı” lblMPARAM1 dil ayarlarında label koduna tanımlanır. Rapor formatında eklenecek tag bilgisi lbl kısmı kaldırılarak <MPARAM1\> şeklinde olacaktır.

\-Ölçü Birimi parametrik alan tipi “Cihazın Ölçü Birimi” lblNPARAM1 dil ayarlarında label koduna tanımlanır. Rapor formatında eklenecek tag bilgisi için \<NPARAM1_BIRIM\> şeklinde olacaktır.

### **1.1.2. Cihaz Yönetim Sistemi Planlanan İşlemler Raporu Formatına Tag Eklenecek Alanların Değerlerin Girilmesi**

Cihaz Yönetim Sistemi Planlanan İşlemler Raporu formatına tag eklenecek alanların değerlerin girilmesi için Cihaz Yönetim Sistemi Modülünde Cihaz Tanımlama menüsünde yeni bir cihaz Tanımlama işlemi ve yapılacak işlem ataması yapılır. Cihaz Tanımlama menüsünde diğer bilgiler sekmesinde tag eklenecek alanların bilgisi girilir. Cihaz Yönetim Sistemi modülünde açılan Cihaz tanımlama ekranında Diğer bilgiler sekmesinde tanımlanan parametrik alanların tiplerini bilgisi girildikten sonra rapor formatına eklenen alanların tagleri ile rapora bu alanların bilgisinin basılma sağlanılır. Raporda tanımlanan alan değerlerin bilgisinin gelmesi için Cihaz Tanımlama ekranında Diğer bilgiler sekmesinde alan bilgilerin girilmesi gerekmektedir

Entegre Yönetim Sistemi/ Cihaz Yönetim Sistemi / Cihaz Tanımlama menüsü tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb4d6cc73-b385-413a-a271-6dc4412ccc65)

Listeye yeni bir cihaz eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload031d5991-437d-46d3-b67c-42e48a2609d9) (yeni) butonu tıklanarak Cihaz Tanımlama/ Yeni Kayıt ekranı görüntülenir. İlk olarak Cihaz bilgileri sekmesindeki ilgili alanlar bilgisi girilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload575cec78-34b9-4877-bc81-1ea68ea6a45d)

Diğer bilgiler sekmesi tıklanarak Sistem Altyapı Tanımları\>BSAT\>Konfigürasyon Ayarları\>Dil Ayarlarında Modüller kısmında Cihaz Yönetim Sistemi seçilerek tanımlanan parametrik alanların görüntülenir ve bilgisi girilir. Bilgisi girilen bu parametrik alanların tagleri daha sonra rapor formatına eklenerek Planlanan İşlemler raporuna bilgilerin basılması sağlanacaktır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5d901ebe-14f3-4ee3-ace3-94b5355ebd07)

Ek Dosyalar sekmesinde Cihaz ile ilgili eklenmek istenen doküman, resim vb. dosya varsa eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf1d61c36-41a2-4699-b227-abf64a5ba3ec)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd8ce1a8f-9d85-4c2c-b6d5-29a709bdb416)

Gerekli tüm alan bilgileri girildikten sonra, ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc15169f3-3ecf-479c-a74d-2ad579c6fa37) (Kaydet) butonu tıklanarak Cihaz Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload06f8745d-1a84-4b74-bd9f-1450562daea5)

Cihaz listesi ekranındaki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3fe0fe46-e11a-42e2-8140-602a6840dd39) (işlem tipleri) butonuyla tanımlanmış işlem tiplerinden biri ya da birkaçı seçilen cihaza atanabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada1f2670a-cf9c-4318-a476-2790063137ba)

Açılan ekranda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload446c83be-40af-4d32-963c-9688e605681e) (Yeni) butonuna basılarak cihaza yeni işlem tipi tanımlanabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfb9d4583-35aa-4dc9-8da8-23952070318b)

Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0f7c9dcd-6bf9-4702-9563-9eda7f6476b6) (kaydet) butonu tıklanarak Cihaza Ait İşlem Tipleri Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload479a0615-5c7e-42a5-9816-1488f3cb1f03)

### **1.1.3. Planlanan İşlemler Rapor Formatına Tanımlanan Parametrik Alanların Taglerin Eklenmesi**

Planlanan İşlemler Raporu tanımlanan parametrik alanların taglerin eklenmesi için Sistem Altyapı Tanımları\>BSAT\> Konfigürasyon Ayarları\>Rapor Formatları Düzenleme menüsüne gidilir. Qdms tüm raporların yüklendiği menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9915c926-230b-4952-821d-76ce5a35652f)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload998f460f-3c0c-4ee6-a0c6-89a8600a7940) (Görüntüle) butonu tıklanarak Planlanan İşlemler Raporunun rapor format şablonu (PLAN_ISLEM_RAPORU.xls) bilgisayara indirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7949e4a5-b7bc-4372-a4b5-9c01f480d192)

Rapor formatına tanımlanan parametrik alanların alan tanımları ve tagleri ilgili bilgiler yazılırak rapor aynı isimde formatı bilgisayara kaydedilir. Örnekte “Cihaz Bakım Açıklaması” metin tipli parametrik alanın tagi <PARAM2\> ve “Cihazın Bakım İşlemleri Detayı” metin (Çoklu Satır) parametrik tipli alanın tagi \<MPARAM1\> olacak şekilde rapor formatına yazılır. Diğer tanımlanan parametrik alan tiplerinin tagleri rapor formatınan eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf2692cee-be4d-4ed6-b703-a904a166bb75)

Tag ekleme işlemi gerçekleştirilen ve bilgisayara kaydedilen aynı isimdeki Rapor format (PLAN_ISLEM_RAPORU.xls) ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf01a2e2d-6398-4577-bdc2-5cb221121652) (Yeni) butonu ile tekrar rapor formatları Düzenleme menüsüne sisteme yüklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0e8c24e2-dad4-4293-a4a3-7620bbd365ef)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4d1958ba-04d0-4b9e-9942-33c2e7e48835)

Rapor formatları menüsünde aynı isimde rapor format yükleme işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload335b36e5-5a01-4824-9ff5-67ac58e61bbf)

### **1.1.4. Planlanmış İşlemler Raporunun Rapor Formatına Eklenen Parametrik Alanların Gösterimi**

Raporunun rapor formatına (PLAN_ISLEM_RAPORU.xls) tag ekleme işlemi yapılan rapor format yükleme işleminde sonra Entegre Yönetim Sistemi\>Cihaz Yönetim Sistemi \>Raporlar\>Planlanmış İşlemler Raporu menüsü tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload74a5451d-a387-47e4-aee1-40ccecd8b96d)

Açılan Planlanan Kalibrasyonlar Raporu ekranında iki sekme karşımıza çıkar. Ara sekmesi tıklanarak Cihaz Tanımlama menüsünde tanımlanan ve işlemi gerçekleştirilen cihazın adı bilgisi girilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade78dde2d-3ac2-4625-a7dd-99ce345d519b)(ara) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2b24f9cf-1205-4007-8057-f9e946d03a7b)

Liste sekmesi tıklanarak arama kriterlerine göre aratılan cihaz görüntülenir. Listede görüntülen Cihaz seçilerek Excel’e aktar butonu tıklanır. ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcc09736f-5c0c-4ae6-9edd-aa10dd634ff5) (Excel’e Aktar) butonu ile “Planlanmış İşlemler Raporu” Excel formatında görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4cd67594-f401-4abb-9234-a7acea9f4e04)

## **1.2.Cihaz Yönetim Sistemi Modülünde Genel Replacement (Kısa Kodlar) Tag Tablosu**

Aşağıdaki tabloda Cihaz Yönetim Sisteminde kullanılan genel Tag’lerin listesi bulunmaktadır.

| **RAPLECEMENTLER (KISA KODLAR)** |                          |
|----------------------------------|--------------------------|
| **TİPİ**                         | **KODU**                 |
| Cihaz Kodu                       | <CIHAZ_KODU\>           |
| Cihaz Adı                        | <ADI\>                  |
| Kategorisi                       | <KATEGORI\>             |
| Marka                            | <MARKA\>                |
| Model                            | <MODEL\>                |
| Seri No                          | <SERI_NO\>              |
| Periyot                          | <PERIYOD\>              |
| İşlem Tipi                       | <ISLEM_TIPI\>           |
| İş Emri no                       | <ISEMRI_NO\>            |
| Cihazın Sorumlusu                | <CIHAZ_SOR\>            |
| Bulunduğu yer                    | <BUL_YER\>              |
| Son İşlem Tarihi                 | <SON_ISLEM_TAR\>        |
| Gelecek İşlem Tarihi             | <GEL_ISLEM_TAR\>        |
| İşlem Sorumlusu                  | <KAL_SOR\>              |
| Cihazın Maliyeti                 | <CIHAZ_MALIYETI\>       |
| Cihaza Yönelik İşlem             | <CIHAZ_ISLEM\>          |
| Açıklama                         | <CIHAZ_ISLEM_ACK\>      |
| Kalibrasyonu Yapan               | <KAL_SOR\>              |
| Onaylayan                        | <ONAYLAYANLAR\>         |
| İş Emri Tarihi                   | <ISEMRI_TARIHI\>        |
| İşlem Yeri                       | <KAL_YERI_TANIMI\>      |
| Bulunduğu Yer Açıklaması         | <BUL_YER_ACK\>          |
| Durum                            | <DURUM\>                |
| Notlar                           | <NOTLAR\>               |
| Referans değer                   | <REFERANS_DEGER\>       |
| Standart değer                   | <STANDART_DEGER\>       |
| Ölçülen Değer                    | <OLCULEN_DEGER\>        |
| Sapma                            | <SAPMA\>                |
| Hata Oranı                       | <HATA_ORANI\>           |
| Kabul Aralığı Alt                | <KABUL_ARA_ALT\>        |
| Kabul Aralığı Üst                | <KABUL_ARA_UST\>        |
| İşlem Maliyet                    | <ISLEM_MALIYETI\>       |
| İşlem Maliyet Birimi             | <ISLEM_MALIYETI_BIRIM\> |
| Cihaz Maliyet Birimi             | <CIHAZ_MALIYETI_BIRIM\> |
| Bulunduğu Ful Yer                | <FUL_YER\>              |
| Param1(metin)                    | <PARAM1\>               |
| Param2(Metin)                    | <PARAM2\>               |
| Param3(Metin)                    | <PARAM3\>               |
| Param4(Metin)                    | <PARAM4\>               |
| Param5(Metin)                    | <PARAM5\>               |
| Param6(Metin)                    | <PARAM6\>               |
| Param7(Metin)                    | <PARAM7\>               |
| Param8(Metin)                    | <PARAM8\>               |
| Param9(Metin)                    | <PARAM9\>               |
| Param10(Metin)                   | <PARAM10\>              |
| LParam1(Liste)                   | <LPARAM1\>              |
| LParam2(Liste)                   | <LPARAM2\>              |
| LParam3(Liste)                   | <LPARAM3\>              |
| LParam4(Liste)                   | <LPARAM4\>              |
| LParam5(Liste)                   | <LPARAM5\>              |
| LParam6(Liste)                   | <LPARAM6\>              |
| LParam7(Liste)                   | <LPARAM7\>              |
| LParam8(Liste)                   | <LPARAM8\>              |
| NParam1(Ölçü Birimi)             | <NPARAM1_BIRIM\>        |
| NParam2(Ölçü Birimi)             | <NPARAM2_BIRIM\>        |
| NParam3(Ölçü Birimi)             | <NPARAM3_BIRIM\>        |
| NParam4(Ölçü Birimi)             | <NPARAM4_BIRIM\>        |
| PParam1(Personel)                | <PPARAM1\>              |
| PParam2(Personel)                | <PPARAM2\>              |
| PParam3(Personel)                | <PPARAM3\>              |
| DParam1(Tarih)                   | <DATETIME1\>            |
| DParam2(Tarih)                   | <DATETIME2\>            |
| DParam3(Tarih)                   | <DATETIME3\>            |
| MParam1(Metin (Çoklu Satır)      | <MPARAM1\>              |
| MParam2(Metin (Çoklu Satır)      | <MPARAM2\>              |
