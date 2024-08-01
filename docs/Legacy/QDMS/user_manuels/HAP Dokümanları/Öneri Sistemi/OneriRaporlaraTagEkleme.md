---
title: Raporlara Parametrik Alan Ekleme İşlemi ve Genel Tag Listesi
description: Raporlara Parametrik Alan Ekleme İşlemi ve Genel Tag Listesi Kullanıcı Yardım Dokümanı
sidebar_position: 2
---

:::tip Bilgi

İlgili konu başlığına sağ tarafta bulunan navigasyon yardımıyla hızlı bir şekilde ulaşabilirsiniz.

:::



**Öneri Sistemi Modülünde Raporlara Parametrik Alan Ekleme İşlemi ve Öneri Durum Raporu Tag Listesi Kullanıcı Yardım Dokümanı**



# **1.Öneri Sistemi Modülünde Raporlara Parametrik Alan Ekleme İşlemi ve Raporlarda Kullanılan Taglar**

Öneri Sistemi Modülünde Öneri durum raporuna parametrik alan ekleme işlemi yapılmaktadır. Öneri Durum Raporuna parametrik alan ekleme işlem basamakları ve Öneri Yönetim Sistemi Modülünde kullanılan taglerin (kısa kodların) listesi bu yardım dokümanında yer almaktadır.

## **1.1. Öneri Sistemi Modülünde Parametrik Alan Tiplerinin Öneri Durum Raporunda Gösterimi**

Öneri Sistemi Modülü raporlarında Öneri Durum raporuna eklenen parametrik alanların raporda gösterilme işlemi için öncelikle dil ayarları menüsünde parametrik alan tiplerinin tanımlama işlemi yapmak gerekiyor. Dil ayarlarında metin, liste, tarih gibi parametrik alan tiplerinin tanımlama işlemi yapılır. Bu tanımlanan parametrik alanlar Entegre Yönetim Sistemi\> Öneri Sistemi \> Öneri Girişi menüsü açılan Öneri tanımlama ekranında Öneri bilgileri sekmesinde görüntülenir. Bu sekmede tanımlanan parametrik alan tiplerinin bilgisi girilir. Açılan Öneri Bilgiler sekmesinde tanımlanan alanların bilgi girişleri yapıldıktan sonra Rapor Formatları Düzenleme menüsüne gidilir. Rapor Formatların Düzenleme menüsünde Öneri Durum Raporun Rapor formatı “oneridurumRaporu.xls” indirilir. İndirilenen “oneridurumRaporu.xls” dil ayarlarından tanımlanan parametrik alanların tag’leri yazılır. Örneğin: Öneri Girişi menüsü açılan Öneri tanımlama ekranında Öneri bilgileri sekmesinde eklenen tarih tipli parametrik alan tipi lblDPARAM1 için <DPARAM1\> alan kodunun lbl olmadan tag içerisine yazılır. Bu şekilde Öneri Girişi menüsü açılan Öneri tanımlama ekranında Öneri bilgileri sekmesinde parametrik alan tipleri tag şeklinde Rapor formatına yazılır. Rapor formatına parametrik alanların tag şeklinde yazıldıktan Rapor formatı “oneridurumRaporu.xls” aynı isimde bilgisayara kaydedilir. Kaydedilen aynı isimde Öneri Durum Rapor formatı Rapor Formatları Düzenleme menüsünde tekrar sisteme yüklenir. Öneri Durum Rapor formatının yükleme işleminde sonra Entegre Yönetim Sistemi\> Öneri Sistemi\>Raporlar\> Öneri Durum Raporu menüsüne gidilir. Açılan Öneri Durum Raporu ekranında arama filtrelerinde Öneri No alanına Önerinin Nosu yazılırak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload657d6c17-45ba-4525-a136-3fa7d2642043)(Excel aktar) butonu tıklanır. Excel format alınan raporda parametrik alanların taglerinin bulunduğu kısımda Öneri Sistemi Modülünde Öneri Girişi menüsü açılan Öneri tanımlama ekranında Öneri Bilgileri sekmesinde alan bilgilerinin geldiği ve taglerin çalıştığı görülür.

### **1.1.1.Öneri Sistemi Modülünde Parametrik Alan Tanımlama**

Öneri Sistemi Modülünde Öneri Girişi menüsü, Öneri Uzman Değerlendirme ve Kazanç Maliyet aşamalarında firmanın istemiş olduğu sistemde olmayan ekstradan alanlar tanımlanabilir. Tanımlanan bu alanlar tüm Öneri Sistemi Modülü kaynakları için geçerlidir. Sistem Altyapı Tanımları/BSAT/ Konfigürasyon Ayarları/Dil Ayarları menüsü tıklanılır. Açılan Dil Ayarları sayfasında Modül alanında “Öneri Sistemi ” seçilir ve ekranda Öneri Sistemi Modülü ile ilgili dil tanımları görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada60993ce-eea7-4e89-a821-8381069b5064)



Öneri Sistemi Modülünde Öneri Sistemi Modülünde Öneri Girişi menüsü açılan Öneri Tanımlama ekranında Öneri Bilgileri sekmesinde tanımlanan parametrik alan tipleri tanımlanarak bu alanların tag şeklinde Öneri Durum raporunun formatına (oneridurumRaporu.xls) eklenerek Öneri Durum raporuna bu parametrik alan tiplerinin bilgilerin basılması sağlanılır. Parametrik alan tiplerinin tagleri Rapor Formatları düzenleme menüsünde indirilen rapor format şablonuna eklenir.

### **1.1.1.1. Öneri Sistemi Modülünde Öneri Girişi Menüsü Açılan Öneri Tanımlama ekranında Öneri Bilgileri Sekmesinde Parametrik Alan Tanımlama**

Öneri Sistemi modülünde dil ayarları menüsünde Öneri Girişi menüsü açılan Öneri Tanımlama ekranında Öneri Bilgileri sekmesi için parametrik alan tanımlama işlemi yapılır. Aşağıdaki tabloda Öneri Tanımlama ekranında Öneri Bilgileri eklenecek parametrik alan tiplerinin ve rapor formatına eklenecek tag ‘lerin listesi yer almaktadır.

| **Parametrik Alan**      | **Parametrik Alan Tipi** | **Parametrik Alanların Tag’leri** |
|--------------------------|--------------------------|-----------------------------------|
| lblDPARAM1… lblDPARAM5   | Tarih                    | <DPARAM1\>… \<DPARAM5\>          |
| lblLPARAM1…lblLPARAM10   | Liste                    | <LPARAM1\>…\<LPARAM10\>          |
| lblPPARAM1…lblPPARAM5    | Personel                 | <PPARAM1\>…\<PPARAM5\>           |
| lblNPARAM6…lblNPARAM10   | Ölçü Birimi              | <NPARAM6\>…\<NPARAM10\>          |
| lblNPARAM1…lblNPARAM5    | Parasal                  | <NPARAM1\>…\<NPARAM5\>           |
| lblDSPARAM1… lblDSPARAM5 | Departman                | <DSPARAM1\>… \<DSPARAM5\>        |
| lblDMPARAM1… lblDMPARAM5 | Departman(Çoklu Seçim)   | <DMPARAM1\>… \<DMPARAM5\>        |
| lblPMPARAM1…lblPMPARAM5  | Personel(Çoklu Seçim)    | <PMPARAM1\>…\<PMPARAM5\>         |

### **1.1.1.1.1.Tarih Tipli Parametrik Alanların Listesi**

Öneri Sistemi Modülünde Öneri Girişi menüsünde açılan Öneri tanımlama ekranında Öneri bilgileri sekmesinde tarih tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına tarih yazarak tarih tipli parametrik alanlar aratılır ve tarih tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen tarih tipli parametrik alanların alan tanımlaması yapılır. Bu tarih tipli alanın daha sonra Öneri Durum raporunda gösterilme işleminde tag’ini kullanmak için tanımlama işlemi yapılacaktır. Bu alan tanımlaması yapılan tarih tipli parametrik alanları lbl kısa kodu kaldırarak:

<DPARAM1\>…<PARAM5\> şeklinde Öneri Durum raporu formatına tag şeklinde eklendiğinde Öneri girişi menüsünde açılan Öneri tanımlama ekranında Öneri bilgileri sekmesinde tarih tipli alanların girilen değerleri bilgisi ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf4318973-71e4-470a-9509-8d13c928bb27)(Excel aktar) butonu tıklanarak alınan Excel formatındaki rapora basılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd4d5f3c0-763c-49e0-9a76-cc87bbcc25c5)

### **1.1.1.1.2.Tarih Tipli Parametrik Alan Tanımlama**

Rapor formatına eklenecek tarih tipli parametrik bir alan tanımlaması yapılır. lblDPARAM1 tarih tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5806ecef-cfe7-4e9f-adf7-379084fac0dc) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8598c06c-89b4-46d6-9b49-7f955dbedc86)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload92b532a5-391c-4419-ba79-bdcfeea9913f)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc651ec7c-6d81-4be4-8340-7291394f72a4)(Kaydet) butonu tıklanarak tarih tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload714ace98-51a9-48f4-9a8b-3d026e7426c8)

Tanımlanan tarih tipli parametrik alan Entegre Yönetim Sistemi\> Öneri Sistemi\> Öneri Girişi menüsünde açılan Öneri tanımlama ekranında Öneri bilgiler sekmesinde görüntülenir. Tanımlanan tarih tipli parametrik alanın “lblDPARAM1” lbl kısa kod kısmı kaldırılarak Öneri Durum Raporunun rapor formatına <DPARAM1\> tag şeklinde bilgisi yazılır. Öneri Girişi menüsünde açılan Öneri Tanımlama ekranında Öneri bilgiler sekmesinde bu tarih tipli alanın bilgisi girildiğinde Öneri Durum raporu alındığında tarih tipli alanın girilen bilgilerin rapora basıldığı görülür.

### **1.1.1.1.3.Liste Tipli Parametrik Alanların Listesi**

Öneri Sistemi Modülünde Öneri Girişi menüsünde açılan Öneri tanımlama ekranında Öneri bilgileri sekmesinde liste tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına liste yazarak liste tipli parametrik alanlar aratılır ve liste tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen liste tipli parametrik alanların alan tanımlaması yapılır. Bu liste tipli alanın daha sonra Öneri Durum raporunda gösterilme işleminde tag’ini kullanmak için tanımlama işlemi yapılacaktır. Bu alan tanımlaması yapılan liste tipli parametrik alanları lbl kısa kodu kaldırarak:

<LPARAM1\>…<LPARAM10\> şeklinde Öneri Durum raporu formatına tag şeklinde eklendiğinde Öneri girişi menüsünde açılan Öneri tanımlama ekranında Öneri bilgileri sekmesinde liste tipli alanların girilen değerleri bilgisi ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf4318973-71e4-470a-9509-8d13c928bb27)(Excel aktar) butonu tıklanarak alınan Excel formatındaki rapora basılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8847c9f0-5d63-43bf-8ef0-a73fbb4444eb)

### **1.1.1.1.4.Liste Tipli Parametrik Alan Tanımlama**

Rapor formatına eklenecek liste tipli parametrik bir alan tanımlaması yapılır. lblLPARAM2 liste tipli parametrik seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5806ecef-cfe7-4e9f-adf7-379084fac0dc) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0d1eff28-f5db-4eb0-967f-691c21947217)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2c521814-156c-47b8-bc3f-5a967c542c07)

Liste tipli alanın liste değerlerini girmek için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0617fea8-c68f-4749-ab5f-6d46d8646316) (Yeni) butonuna tıklanır, liste değerleri yazılır ve kaydedilir. Liste eleman değeri 1 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload204cc5f0-ed3a-409d-90a3-f3d55d9d8c61)

Liste eleman değeri 2 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd7c157ee-2660-47ce-a31d-4fbb7ca1e91b)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload77276a23-3b76-4fe4-b974-4cd328046b72)

Alanın zorunlu olup, olmayacağı sıra no bilgisi, liste elemanları tanımlanarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc651ec7c-6d81-4be4-8340-7291394f72a4)(kaydet) butonu tıklanarak liste tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfd771528-a08f-4217-88ac-8dbe97293673)

Tanımlanan liste tipli parametrik alan Entegre Yönetim Sistemi\> Öneri Sistemi\> Öneri Girişi menüsünde açılan Öneri tanımlama ekranında Öneri bilgiler sekmesinde görüntülenir. Tanımlanan liste tipli parametrik alanın “lblLPARAM2” lbl kısa kod kısmı kaldırılarak Öneri Durum raporunun rapor formatına <LPARAM2\> tag şeklinde bilgisi yazılır. Öneri Girişi menüsünde açılan Öneri tanımlama ekranında Öneri bilgiler sekmesinde bu liste tipli alanın bilgisi girildiğinde Öneri Durum raporu alındığında liste tipli alanın girilen bilgilerin rapora basıldığı görülür.

### **1.1.1.1.5.Personel Tipli Parametrik Alanların Listesi**

Öneri Sistemi Modülünde Öneri girişi menüsünde açılan Öneri tanımlama ekranında Öneri bilgileri sekmesinde personel tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına personel yazarak personel tipli parametrik alanlar aratılır ve personel tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen personel tipli parametrik alanların alan tanımlaması yapılır. Bu personel tipli alanın daha sonra Öneri Durum raporunda gösterilme işleminde tag’ini kullanmak için tanımlama işlemi yapılacaktır. Bu alan tanımlaması yapılan personel tipli parametrik alanları lbl kısa kodu kaldırarak:

<PPARAM1\>…<PPARAM5\> şeklinde Öneri Durum raporu formatına tag şeklinde eklendiğinde Öneri Girişi menüsünde açılan Öneri tanımlama ekranında Öneri bilgileri sekmesinde personel tipli alanların girilen değerleri bilgisi ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf4318973-71e4-470a-9509-8d13c928bb27)(Excel aktar) butonu tıklanarak alınan Excel formatındaki rapora basılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade9a6dce8-fc91-4b27-b201-4d63a6776c08)

### **1.1.1.1.6.Personel Tipli Parametrik Alan Tanımlama**

Rapor formatına eklenecek personel tipli parametrik bir alan tanımlaması yapılır. lblPPARAM1 personel tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5806ecef-cfe7-4e9f-adf7-379084fac0dc) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade79a8b5b-847c-4863-8e5f-b7197ff06123)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload46295d72-0147-4493-9646-cc82d8464ad2)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc651ec7c-6d81-4be4-8340-7291394f72a4)(kaydet) butonu tıklanarak Personel tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload46c99329-3a15-47a0-ac58-4fca9a7d0b18)

Tanımlanan personel tipli parametrik alan Entegre Yönetim Sistemi\> Öneri Sistemi\> Öneri Girişi menüsünde açılan Öneri tanımlama ekranında Öneri bilgiler sekmesinde görüntülenir. Tanımlanan personel tipli parametrik alanın “lblPPARAM1” lbl kısa kod kısmı kaldırılarak Öneri Durum raporunun rapor formatına <PPARAM1\> tag şeklinde bilgisi yazılır. Öneri Girişi menüsünde açılan Öneri tanımlama ekranında Öneri bilgiler sekmesinde bu personel tipli alanın bilgisi girildiğinde Öneri Durum raporu alındığında personel tipli alanın girilen bilgilerin rapora basıldığı görülür.

### **1.1.1.1.7.Ölçü Birimi Parametrik Alanların Listesi**

Öneri Sistemi Modülünde Öneri girişi menüsünde açılan Öneri tanımlama ekranında Öneri bilgileri sekmesinde ölçü birimi tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına ölçü birimi yazarak ölçü birimi tipli parametrik alanlar aratılır ve ölçü birimi tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen ölçü birimi tipli parametrik alanların alan tanımlaması yapılır. Bu ölçü birimi tipli alanın daha sonra Öneri Durum raporunda gösterilme işleminde tag’ini kullanmak için tanımlama işlemi yapılacaktır. Bu alan tanımlaması yapılan ölçü birimi tipli parametrik alanları lbl kısa kodu kaldırarak:

<NPARAM6\>…<NPARAM10\> şeklinde Öneri Durum Raporu formatına tag şeklinde eklendiğinde Öneri girişi menüsünde açılan Öneri tanımlama ekranında Öneri bilgileri sekmesinde ölçü birimi tipli alanların girilen değerleri bilgisi ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf4318973-71e4-470a-9509-8d13c928bb27)(Excel aktar) butonu tıklanarak alınan Excel formatındaki rapora basılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6014af66-f179-4dd5-8877-13ed082f40b3)

### **1.1.1.1.8.Ölçü Birimi Parametrik Alan Tanımlama**

Rapor formatına eklenecek ölçü birimi tipli parametrik bir alan tanımlaması yapılır. lblNPARAM6 ölçü birimi tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5806ecef-cfe7-4e9f-adf7-379084fac0dc) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd4d88c25-9802-4f04-b051-0693b8d6b6ad)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf7fc2d12-6786-41f1-9d8a-939604c85227)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc651ec7c-6d81-4be4-8340-7291394f72a4)(Kaydet) butonu tıklanarak ölçü birimi tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4d60e838-7247-40a3-be32-97bd8ba1d86d)

Tanımlanan ölçü birimi Tipli parametrik alan Entegre Yönetim Sistemi\> Öneri Sistemi\> Öneri girişi menüsünde açılan Öneri tanımlama ekranında Öneri bilgiler sekmesinde görüntülenir. Tanımlanan ölçü birimi tipli parametrik alanın “lblNPARAM6” lbl kısa kod kısmı kaldırılarak Öneri Durum raporunun rapor formatına <NPARAM6\> tag şeklinde bilgisi yazılır. Öneri Girişi menüsünde açılan Öneri tanımlama ekranında Öneri bilgiler sekmesinde bu ölçü birimi tipli alanın bilgisi girildiğinde Öneri Durum raporu alındığında ölçü birimi tipli alanın girilen bilgilerin rapora basıldığı görülür.

Diğer parametrik alan tiplerinin aynı şekilde tanımlama işlemi yapılır.

\-Parasal parametrik alan tipi “**Tutar**” lblNPARAM1 dil ayarlarında label koduna tanımlanır. Rapor formatında eklenecek tag bilgisi için <NPARAM1\> şeklinde olacaktır.

\-Departman parametrik alan tipi “**Sorumlu Kişinin Bağlı Bulunduğu Departman**” lblDSPARAM1 dil ayarlarında label koduna tanımlanır. Rapor formatında eklenecek tag bilgisi için <DSPARAM1\> şeklinde olacaktır.

\-Departman(Çoklu Seçim) parametrik alan tipi “**İlgili Departmanlar**” lblDMPARAM1 dil ayarlarında label koduna tanımlanır. Rapor formatında eklenecek tag bilgisi için <DMPARAM1\> şeklinde olacaktır.

\-Personel(Çoklu Seçim) parametrik alan tipi “**İlgili Personeller**” lblPMPARAM1 dil ayarlarında label koduna tanımlanır. Rapor formatında eklenecek tag bilgisi için <PMPARAM1\> şeklinde olacaktır.

### **1.1.2. Öneri Sistemi Öneri Durum Raporu Formatına Tag Eklenecek Alanların Değerlerin Girilmesi**

Öneri Sistemi Öneri Durum raporu formatına tag eklenecek alanların değerlerin girilmesi için Öneri Sistemi Modülünde Öneri girişi menüsünde yeni bir Öneri girişi işlemi yapılır. Entegre Yönetim Sistemi\> Öneri Sistemi\> Öneri Girişi menüsünde açılan Öneri tanımlama ekranında Öneri bilgiler sekmesinde tag eklenecek alanların bilgisi girilir. Öneri Sistemi modülünde açılan Öneri Girişi menüsünde açılan Öneri tanımlama ekranında Öneri bilgiler sekmesinde tanımlanan parametrik alanların tiplerini bilgisi girildikten sonra rapor formatına eklenen alanların tagleri ile rapora bu alanların bilgisinin basılma sağlanılır. Raporda tanımlanan alan değerlerin bilgisinin gelmesi için Öneri girişi menüsünde açılan Öneri tanımlama ekranında Öneri bilgiler sekmesinde alan bilgilerin girilmesi gerekmektedir

Entegre Yönetim Sistemi/ Öneri Sistemi / Öneri Girişi menüsü tıklanılır.

Sisteme öneri girişinin yapıldığı menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload38a583b9-1156-4d66-875e-5a46bb0dbd92) ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload32dbee00-d041-4970-a2ee-03d632b9bde4)

Öneri bilgiler sekmesi tıklanarak Sistem Altyapı Tanımları\>BSAT\>Konfigürasyon Ayarları\>Dil Ayarlarında Modüller kısmında Öneri Sistemi seçilerek tanımlanan parametrik alanların görüntülenir ve bilgisi girilir. Bilgisi girilen bu parametrik alanların tagleri daha sonra rapor formatına eklenerek Öneri Durum raporuna bilgilerin basılması sağlanacaktır.

Öneri ile ilgili eklenmek istenen doküman, resim vb. dosya varsa “Ek Dosyalar” sekmesinden sisteme yüklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfc4a37b6-1cda-4d6f-8918-8d50cd4cf246)

Öneri giriş ekranında gerekli alanların bilgi girişi yapıldıktan sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd176c566-cfb1-406d-b34b-946d1a004e08) (Kaydet/ Onay Gönder) butonu ile öneri uzman değerlendirme aşaması yapılmak üzere sistemde tanımlanan uzman değerlendirmeci rolüne gönderilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd330b368-fdd4-4406-a533-c0df1f7da717) ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7934aa6e-e19a-4f55-bb1d-a38b8fde9aa6)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload09dc4b29-a0e9-4ae4-93be-89a5814196c8)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload71dca533-3688-48e4-8305-89d1feb1cad2)

### **1.1.3. Öneri Durum Rapor Formatına Tanımlanan Parametrik Alanların Taglerin Eklenmesi**

Öneri Durum Raporu tanımlanan parametrik alanların taglerin eklenmesi için Sistem Altyapı Tanımları\>BSAT\> Konfigürasyon Ayarları\>Rapor Formatları Düzenleme menüsüne gidilir. Qdms tüm raporların yüklendiği menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2c2fca39-298e-4b58-86f7-570ff9eeade1)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade660ca4c-b8d2-4908-8b91-f2e0edf67b82) (Görüntüle) butonu tıklanarak Öneri Durum Raporunun rapor format şablonu (oneridurumRaporu.xls) bilgisayara indirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfdf71e20-0bfb-4ec1-a17d-120c23e22e08)

Rapor formatına tanımlanan parametrik alanların alan tanımları ve tagleri ilgili bilgiler yazılırak rapor aynı isimde formatı bilgisayara kaydedilir. Örnekte “İstenilen Tarih” tarih tipli parametrik alanın tagi <DPARAM1\> ve “Öneri Dosya Türü” liste tipli parametrik tipli alanın tagi <LPARAM2\> olacak şekilde rapor formatına yazılır. Diğer tanımlanan parametrik alan tiplerinin tagleri rapor formatınan eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload459308f0-e8e9-43ca-9e1f-a0be1df12673)

Tag ekleme işlemi gerçekleştirilen ve bilgisayara kaydedilen aynı isimdeki Rapor format (oneridurumRaporu.xls) ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload251a5c90-eec4-46a9-b408-371efd336e85) (Yeni) butonu ile tekrar Rapor Formatları Düzenleme menüsüne sisteme yüklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0a946db3-9d18-43e7-bbbd-4b736fe378ec)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5bd52f50-5b07-496e-888e-7dc9bdd37fdb)

Rapor Formatları Düzenleme menüsünde aynı isimde rapor format yükleme işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9117d30a-bdbb-4c95-82ae-a8e0df6bfc22)

### **1.1.4. Öneri Durum Raporunun Rapor Formatına Eklenen Parametrik Alanların Gösterimi**

Raporunun rapor formatına (oneridurumRaporu.xls) tag ekleme işlemi yapılan rapor format yükleme işleminde sonra Entegre Yönetim Sistemi\>Öneri Sistemi \>Raporlar\>Öneri Durum Raporu menüsü tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2a3b7d3a-043f-422b-b399-0c837975d829)

Açılan Öneri Durum Raporu ekranında iki sekme karşımıza çıkar. Filtre sekmesi tıklanarak Öneri girişi menüsünde tanımlanan önerinin Öneri No alanına Öneri No bilgisi girilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4294403f-5165-444c-a29a-218dd6ab9d24)(Ara) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0604c06c-6414-4d6f-90a6-0dc80d31f9f5)

Liste sekmesi tıklanarak arama kriterlerine göre aratılan Öneri görüntülenir. Listede görüntülen Öneri seçilerek Excel’e aktar butonu tıklanır. ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload657d6c17-45ba-4525-a136-3fa7d2642043) (Excel’e Aktar) butonu ile “Öneri Durum Raporu” Excel formatında görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload96cd5946-01d5-4f00-81d8-771ca0bf9231)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2861e72c-8583-4e6c-b361-eecef0d6839b)

Dil ayarlarında tanımlanan parametirk alan tiplerinin değerlerinin bilgisinin rapora geldiği ve tanımlanan bu parametrik alan tiplerinin taglerinin çalıştığı görülür.

### **1.1.5.Öneri Sistemi Modülünde Öneri Durum Raporu Replacement (Kısa Kodlar) Tag Tablosu**

Öneri Sistemi Modülünde kullanılan Öneri Durum Raporu taglerin listesi aşağıdaki tabloda yer almaktadır.

|**Kısaltma**                       | **Açıklaması**                                    |
|-----------------------------------|---------------------------------------------------|
| <ONERI_NO\>                       | Öneri No Bilgisi                                  |
| <KAMPANYA_ONERI_MI\>              | Kampanya Bilgisi                                  |
| <ONERI_OZETI\>                    | Öneri Özeti Bilgisi                               |
| <PROBLEM_TANIMI\>                 | Problem Tanımı Bilgisi                            |
| <COZUM_TANIMI\>                   | Çözüm Tanımı Bilgisi                              |
| <DURUM\>                          | Öneri Durumu Bilgisi                              |
| <TIP\>                            | Tip Bilgisi                                       |
| <KIMDE\>                          | Öneri Kimde Bilgisi                               |
| <DEPARTMAN_ADI\>                  | İlgili Departman Bilgisi                          |
| <TARIH\>                          | Sisteme Ekleme Tarihi Bilgisi                     |
| <ISYERI_ADI\>                     | İş Yeri Bilgisi                                   |
| <ONERI_KAYNAK\>                   | Öneri Kaynağı Bilgisi                             |
| <SADI\>                           | Süreç Bilgisi                                     |
| <SISTEME_EKLEYEN\>                | Sisteme Ekleyen Bilgisi                           |
| <SISTEME_EKLEYEN_SICIL_NO\>       | Sisteme Ekleyen Sicil No Bilgisi                  |
| <PUAN\>                           | Puan Bilgisi                                      |
| <URUN\>                           | Ürün Bilgisi                                      |
| <KAZANC_KATEGORISI\>              | Kazanç Kategorisi Bilgisi                         |
| <KM_BRUT_KAZANC\>                 | Brüt Kazanç Bilgisi                               |
| <KM_MALIYET\>                     | Maliyet Bilgisi                                   |
| <KM_NET_KAZANC\>                  | Net Kazanç Bilgisi                                |
| <KM_YILLIK_ACIKLAMA\>             | Yıllık Açıklama Bilgisi                           |
| <KM_MALIYET_ACIKLAMA\>            | Maliyet Açıklama Bilgisi                          |
| <KM_TANIM\>                       | Kazanç Tanımı Bilgisi                             |
| <KM_BASKA_BOL_UYG\>               | Başka Bölümde Uygulanabilirlik Bilgisi            |
| <KM_BASKA_ISY_UYG\>               | Başka İşyerinde Uygulanabilirlik Bilgisi          |
| <ONERI_VERENLER\>                 | Öneri Verenler Bilgisi                            |
| <ONERI_VERENLERIN_DEPARTMANLARI\> | Öneri Verenlerin Departmanları Bilgisi            |
| <ONERI_VERENLER_SICIL_NO\>        | Öneri Verenler Sicil No Bilgisi                   |
| <OD_SON_DEGERLENDIRME_TAR\>       | Öneri Koordinatörü Değerlendirme Tarihi Bilgisi   |
| <PLANLANAN_KAPATMA_TARIHI\>       | termin 1 Bilgisi                                  |
| <PLANLANAN_KAPATMA_TAR\>          | termin 2 Bilgisi                                  |
| <KABUL\>                          | Kabul Kriteri Bilgisi                             |
| <UD_SON_DEGERLENDIRME_TAR\>       | Uzman Değerlendirici Değerlendirme Tarihi Bilgisi |
| <UZMAN_DEGERLENDIRME\>            | Uzman Değerlendirici Bilgisi                      |
| <KAPATMA_TAR\>                    | Kapatma Tarihi Bilgisi                            |
| <RET_NEDENI\>                     | Son Ön Değerlendirmeci Bilgisi                    |
|**Aksiyon Bilgileri**              |                                                   |
| <AKS_SAYISI\>                     | Aksiyon Sayısı Bilgisi                            |
| <ID\>                             | Aksiyon No Bilgisi                                |
| <SID\>                            | Kalem No Bilgisi                                  |
| <AKSIYON_TIPI\>                   | Aksiyon Tipi Bilgisi                              |
| <SORUMLU_ADSOYAD\>                | Sorumlu Bilgisi                                   |
| <YAPACAK_ADSOYAD\>                | Yapacak Bilgisi                                   |
| <DEPARTMAN_ADI2\>                 | Sorumlu Departman Bilgisi                         |
| <TANIM\>                          | Tanım Bilgisi                                     |
| <BITISTARIHI\>                    | Bitiş Tarihi Bilgisi                              |
| <DURUM_\>                         | Aksiyon Durumu Bilgisi                            |
| <GECIKTI\>                        | Gecikti mi? Bilgisi                               |
