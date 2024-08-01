---
title: Raporlara Parametrik Alan Ekleme İşlemi ve Genel Tag Listesi
description: Raporlara Parametrik Alan Ekleme İşlemi ve Genel Tag Listesi Kullanıcı Yardım Dokümanı
sidebar_position: 2
---

:::tip Bilgi

İlgili konu başlığına sağ tarafta bulunan navigasyon yardımıyla hızlı bir şekilde ulaşabilirsiniz.

:::


**Düzeltici ve Önleyici Faaliyetler Modülünde Raporlara Parametrik Alan Ekleme İşlemi ve Genel Tag Listesi Kullanıcı Yardım Dokümanı**

# **1.Düzeltici ve Önleyici Faaliyetler Modülünde Raporlara Parametrik Alan Ekleme İşlemi ve Raporlarda Kullanılan Taglar**

Düzeltici ve Önleyici Faaliyetler Modülünde tüm raporlarına parametrik alan ekleme işlemi yapılmaktdır. Bu modülde parametrik alan ekleme işlemi için DÖF Özet Raporuna bu parametrik alan ekleme işlem basamakları ve DÖF Modülünde kullanılan taglerin (kısa kodların) listesi bu yardım dokümanında yer almaktadır.

## **1.1.Düzeltici ve Önleyici Faaliyetler Modülünde Parametrik Alanların DÖF Özet Raporunda Gösterimi**

DÖF Modülü raporlarında DÖF Özet Listesi raporuna eklenen parametrik alanların raporda gösterilme işlemi için öncelikle dil ayarları menüsünde parametrik alan tiplerinin tanımlama işlemi yapmak gerekiyor. Dil ayarlarında metin, liste, gibi parametrik alan tiplerinin tanımlama işlemi yapılır. Bu tanımlanan parametrik alanlar Entegre Yönetim Sistemi\>Düzeltici ve Önleyici Faaliyetler\>DÖF İşlemler menüsünde açılan bir DÖF kaydının sekmelerinde görüntülenir. Bu sekmeler Detay bilgiler, Gelişme Raporu, Kök neden, Aksiyon, Sonuç Raporu ve Kapatma sekmelerindedir. Bu sekmelerde tanımlanan parametrik alan tiplerinin bilgisi girilir. Açılan DÖF kaydında bu sekmelerin bilgi girişleri yapıldıktan sonra Rapor Formatları Düzenleme menüsüne gidilir. Rapor formatların düzenleme menüsünde DÖF Özet listesinin rapor format “DOF_OZET_RAPOR.xls” indirilir. İndirilenen “DOF_OZET_RAPOR.xls” dil ayarlarından tanımlanan parametrik alanların tag leri yazılır. Örneğin: DÖF kaydının detay bilgiler sekmesine eklenen metin tipli parametrik alan tipi lblPARAM1 için <PARAM1\> alan kodunun lbl olmadan tag içerisine yazılır. Bu şekilde DÖF kaydının aşamalarına parametrik alan tipleri tag şeklinde Rapor formatına yazılır. Rapor formatına parametrik alanların tag şeklinde yazıldıktan Rapor format “DOF_OZET_RAPOR.xls” aynı isimde bilgisayara kaydedilir. Kaydedilen aynı isimde DÖF Özet Listesi Rapor formatı Rapor formatları düzenleme menüsünde tekrar sisteme yüklenir. DÖF Özet Listesi Rapor formatının yükleme işleminde sonra DÖF Raporlarında DÖF Özet Listesi Raporu menüsüne gidilir. Arama filtrelerinde DÖF kodu alanına DÖF kaydının kodu yazılırak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcd83eacf-5cba-4670-b04c-27688614570e)(Ara) butonu tıklanarak DÖF kaydının liste sekmesine gelmesi sağlanılır. Listede görüntülenen DÖF kaydın sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc2d605ee-fff6-48c3-99cd-11b080eeae5e)(Excel aktar) butonu tıklanır. Excel format alınan raporda parametrik alanların taglerinin bulunduğu kısımda girilen DÖF kaydının aşamalarında alan bilgilerinin geldiği görülerek taglerin çalıştığı görülür.

### **1.1.1.Düzeltici ve Önleyici Faaliyetler Modülünde Parametrik Alan Tanımlama**

Düzeltici ve Önleyici Faaliyetler Modülünde Detay Bilgiler, Gelişme Raporu,Kök Nedenler, Aksiyonlar, Sonuç Raporu ve Kapatma sekmelerinde firmanın istemiş olduğu sistemde olmayan ekstradan alanlar tanımlanabilir. Tanımlanan bu alanlar tüm Düzeltici ve Önleyici Faaliyetler Modül kaynakları için geçerlidir. Sistem Altyapı Tanımları/BSAT/ Konfigürasyon Ayarları/Dil Ayarları menüsü tıklanılır. Açılan Dil Ayarları sayfasında Modül alanında “Düzeltici ve Önleyici Faaliyetler” seçilir ve ekranda Düzeltici ve Önleyici Faaliyetler Modülü ile ilgili dil tanımları görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfac52067-517b-4b2d-a223-c97ab2798f35)

Düzeltici ve Önleyici Faaliyetler Modülünde sekmelerinde tanımlanan parametrik alan tipleri tanımlanarak bu alanların tag şeklinde DÖF Özet raporunun formatına (DOF_OZET_RAPOR.xls) eklenerek DÖF özet raporuna bu parametrik alan tiplerinin bilgilerin basılması sağlanılır. DÖF özet raporunun formatınan Aksiyon ve Kök Neden aşamalarında parametrik alan tiplerinin tag ekleme işlemi yapılmaktadır. Aksiyon ve Kök Neden tagleri Aksiyon raporlarının formatlarına eklenebiliyor.

### **1.1.1.1.Düzeltici ve Önleyici Faaliyetler Modülünde Detay Bilgiler Sekmesinde Parametrik Alan Tanımlaması**

Düzeltici ve Önleyici Faaliyetler Modülünde Detay Bilgiler sekmesinde tanımlanan parametrik alanların kısa kodları lblPARAM başlığı ile tanımlı kısa kodlardır. lblPARAM başlığındaki kısa kodlar olan tüm parametrik tipli alanlar tanımlandığında Düzeltici ve Önleyici Faaliyetler Modülünde Detay bilgiler sekmesi ekranında görüntülenir.

#### **1.1.1.1.1.Metin Tipli Parametrik Alanların Listesi**

DÖF Modülünde Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri menüsünde Detay Bilgiler sekmesinde Metin tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Metin yazarak Metin tipli parametrik alanlar aratılır ve Metin tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Metin tipli parametrik alanların alan tanımlaması yapılır. Bu metin tipli alanın daha sonra DÖF Özet raporunda gösterilme işleminde tag’ini kullanmak için tanımlama işlemi yapılacaktır. Bu alan tanımlaması yapılan Metin tipli parametrik alanları lbl kısa kodu kaldırarak:

<PARAM2\>…<PARAM7\> ve <PARAM31\>…<PARAM35\>şeklinde DÖF Özet Raporu formatına tag şeklinde eklendiğinde DÖF kaydının ekranında Metin tipli alanların girilen değerleri bilgisi ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload00d134af-80dc-4220-ae10-fd5d09b60c9f)(Excel aktar) butonu tıklanarak alınan Excel formatındaki rapora basılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddfdf7e59-92b6-4500-81db-4ed8b441df94)

#### **1.1.1.1.2.Metin Tipli Parametrik Alan Tanımlama**

Rapor formatına eklenecek Metin tipli parametrik bir alan tanımlaması yapılır. lblPARAM2 Metin tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload722bdf4d-1181-42e1-884c-a75b26f3452a) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0bb842ec-d027-4e0d-8b28-653f5bd9df18)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0ec8be18-db83-42c6-b807-2b546aea6096)

Alanın zorunlu olup, olmayacağı sıra no, görüntülecek işlem kaynağı bilgisi ve Döf türü seçeneklerinde seçim yapılarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd2790dd7-6d23-4df2-8bb8-cf76e9f61066)(kaydet) butonu tıklanarak Metin tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload30fe05c9-07f9-46fe-b555-9d99d298c1df)

Tanımlanan Metin Tipli parametrik alan Entegre Yönetim Sistemi\>Düzeltici ve Önleyici Faaliyetler\>DÖF İşlemleri menüsünde ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload754ae0e2-aa30-4dac-8366-a79d6b297a26)(Yeni) butonu tıklanarak açılan DÖF işlemleri-Yeni Kayıt ekranında Detay Bilgiler sekmesinde görüntülenir. Tanımlanan metin tipli parametrik alanın “lblPARAM2” lbl kısa kod kısmı kaldırrarak DÖF Özet Raporunun rapor formatına <PARAM2\> tag şeklinde bilgisi yazılır. DÖF kaydı tanımlama işleminde bu metin tipli alanın bilgisi girildiğinde DÖF Özet Raporu alındığında Metin tipli alanın girilen bilgileri rapora basılacaktır.

#### **1.1.1.1.3.Metin (Çoklu Satır) Tipli Parametrik Alanların Listesi**

DÖF Modülünde Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri menüsünde Detay Bilgiler sekmesinde Metin (Çoklu Satır)  tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Metin (Çoklu Satır) yazarak Metin (Çoklu Satır) tipli parametrik alanlar aratılır ve Metin (Çoklu Satır)  tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Metin (Çoklu Satır)  tipli parametrik alanların alan tanımlaması yapılır. Bu Metin (Çoklu Satır)  tipli alanın daha sonra DÖF Özet raporunda gösterilme işleminde tag’ini kullanmak için tanımlama işlemi yapılacaktır. Bu alan tanımlaması yapılan Metin (Çoklu Satır) tipli parametrik alanları lbl kısa kodu kaldırarak:

<PARAM8\>,<PARAM9\>…<PARAM15\> şeklinde DÖF Özet Raporu formatına tag şeklinde eklendiğinde DÖF kaydının ekranında Metin (Çoklu Satır) tipli alanların girilen değerleri bilgisi ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload00d134af-80dc-4220-ae10-fd5d09b60c9f)(Excel aktar) butonu tıklanarak alınan Excel formatındaki rapora basılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload18e6c4b5-60ae-466e-9abf-dc36814fb9b0)

#### **1.1.1.1.4. Metin (Çoklu Satır) Tipli Parametrik Alan Tanımlama**

Rapor formatına eklenecek Metin (Çoklu Satır) tipli parametrik bir alan tanımlaması yapılır. lblPARAM8 Metin (Çoklu Satır) tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload722bdf4d-1181-42e1-884c-a75b26f3452a) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf157e5e6-d7db-4548-bc25-f560ee187bdf)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb6dfd14-d6be-4c1b-99e0-5e562c8b84dd)

Alanın zorunlu olup, olmayacağı sıra no, görüntülecek işlem kaynağı bilgisi ve DÖF türü bilgisi seçeneklerinden seçim yapılarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd2790dd7-6d23-4df2-8bb8-cf76e9f61066)(kaydet) butonu tıklanarak Metin (Çoklu Satır) tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload89118292-5c6a-48e1-9314-4b2e8e0819b1)

Tanımlanan Metin (Çoklu Satır) Tipli parametrik alan Entegre Yönetim Sistemi\>Düzeltici ve Önleyici Faaliyetler\>DÖF İşlemleri menüsünde ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload754ae0e2-aa30-4dac-8366-a79d6b297a26)(Yeni) butonu tıklanarak açılan DÖF işlemleri-Yeni Kayıt ekranında Detay Bilgiler sekmesinde görüntülenir. Tanımlanan Metin (Çoklu Satır) tipli parametrik alanın “lblPARAM8” lbl kısa kod kısmı kaldırrarak DÖF Özet Raporunun rapor formatına <PARAM8\> tag şeklinde bilgisi yazılır. DÖF kaydı tanımlama işleminde bu Metin (Çoklu Satır) tipli alanın bilgisi girildiğinde DÖF Özet Raporu alındığında Metin (Çoklu Satır) tipli alanın girilen bilgileri rapora basılacaktır.

#### **1.1.1.1.5.Tarih Tipli Parametrik Alanların Listesi**

DÖF Modülünde Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri menüsünde Detay Bilgiler sekmesinde Tarih tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Tarih yazarak Tarih tipli parametrik alanlar aratılır ve Tarih tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen tarih tipli parametrik alanların alan tanımlaması yapılır. Bu tarih tipli alanın daha sonra DÖF Özet raporunda gösterilme işleminde tag’ini kullanmak için tanımlama işlemi yapılacaktır. Bu alan tanımlaması yapılan tarih tipli parametrik alanları lbl kısa kodu kaldırarak:

<DPARAM1\>,<DPARAM2\>,….<DPARAM5\> şeklinde DÖF Özet Raporu formatına tag şeklinde eklendiğinde DÖF kaydı ekranında tarih tipli alanların girilen değerleri bilgisi ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload00d134af-80dc-4220-ae10-fd5d09b60c9f)(Excel aktar) butonu tıklanarak alınan Excel formatındaki rapora basılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade4c9c131-efb4-4d6a-89fb-e157b970ed2f)

#### **1.1.1.1.6.Tarih Tipli Parametrik Alan Tanımlama**

Rapor formatına eklenecek Tarih tipli parametrik bir alan tanımlaması yapılır. lblDPARAM1 Tarih tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload722bdf4d-1181-42e1-884c-a75b26f3452a) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload90f79cb7-04f6-49f2-a135-c1e0ff1bfd23)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1e03811d-0916-4490-8142-cedb3a0ac418)

Alanın zorunlu olup, olmayacağı sıra no, görüntülenecek işlem kaynağı bilgisi ve hangi DÖF türünde görüntülenmesi isteniyorsa ilgili seçenekler seçilerek gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd2790dd7-6d23-4df2-8bb8-cf76e9f61066)(Kaydet) butonu tıklanarak tarih tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada18b040d-40f2-4e28-abc5-10957ef8eb72)

Tanımlanan Tarih tipli parametik alan Entegre Yönetim Sistemi\>Düzeltici ve Önleyici Faaliyetler\>DÖF İşlemleri menüsünde ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload754ae0e2-aa30-4dac-8366-a79d6b297a26)(Yeni) butonu tıklanarak açılan DÖF işlemleri-Yeni Kayıt ekranında Detay Bilgiler sekmesinde görüntülenir. Tanımlanan Tarih tipli parametrik alanın “lblDPARAM1” lbl kısa kod kısmı kaldırrarak DÖF Özet Raporunun rapor formatına <DPARAM1\> tag şeklinde bilgisi yazılır. DÖF kaydı tanımlama işleminde bu Tarih tipli alanın bilgisi girildiğinde DÖF Özet Raporu alındığında Tarih tipli alanın girilen bilgileri rapora basılacaktır.

#### **1.1.1.1.7.Liste Tipli Parametrik Alanların Listesi**

DÖF Modülünde Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri menüsünde Detay Bilgiler sekmesinde Liste tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Liste yazarak Liste tipli parametrik alanlar aratılır ve Liste tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Liste tipli parametrik alanların alan tanımlaması yapılır. Bu Liste tipli alanın daha sonra DÖF Özet raporunda gösterilme işleminde tag’ini kullanmak için tanımlama işlemi yapılacaktır. Bu alan tanımlaması yapılan Liste tipli parametrik alanları lbl kısa kodu kaldırarak:

<LPARAM1_VALUE\>,..<LPARAM10_VALUE\>,ve <LPARAM36_VALUE\>, …<LPARAM40 \_VALUE \> şeklinde DÖF Özet Raporu formatına tag şeklinde eklendiğinde DÖF kaydı ekranında Liste tipli alanların girilen değerleri bilgisi ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload00d134af-80dc-4220-ae10-fd5d09b60c9f)(Excel aktar )butonu tıklanarak alınan Excel formatındaki rapora basılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload428a728b-dd4c-4dac-aa20-34dc5cedf71c)

#### **1.1.1.1.8.Liste Tipli Parametrik Alan Tanımlama**

Rapor formatına eklenecek liste tipli parametrik bir alan tanımlaması yapılır. lblLPARAM2 Liste tipli parametrik seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload722bdf4d-1181-42e1-884c-a75b26f3452a) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload696d5ed9-325a-410f-956a-05cf352d5fb9)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6fbb7269-14a1-4e95-8e92-7251e36d7529)

Liste tipli alanın liste değerlerini girmek için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4c9c612e-d770-4ce2-9e51-1b761a01dda4) (Yeni) butonuna tıklanır, liste değerleri yazılır ve kaydedilir. Liste eleman değeri 1 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5081a4dd-afb0-45a8-9d50-7cdc8a283acc)

Liste eleman değeri 2 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6fa84372-b0c6-40a7-b1a5-747ebb608169)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada9d24897-8e8c-4f87-a48c-a2d266902caf)

Alanın zorunlu olup, olmayacağı sıra no, liste elemanları tanımlanarak görüntülenecek işlem kaynağı ve DÖF türü seçeneklerinde seçip yapılarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd2790dd7-6d23-4df2-8bb8-cf76e9f61066)(kaydet) butonu tıklanarak liste tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade875a53f-bf58-48f6-ab63-da8edafebbc0)

Tanımlanan Liste Tipli parametik alan Entegre Yönetim Sistemi\>Düzeltici ve Önleyici Faaliyetler\>DÖF İşlemleri menüsünde ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload754ae0e2-aa30-4dac-8366-a79d6b297a26)(Yeni) butonu tıklanarak açılan DÖF işlemleri-Yeni Kayıt ekranında Detay Bilgiler sekmesinde görüntülenir. DÖF Özet Raporunun rapor formatına <LPARAM2 \_VALUE \> tag şeklinde bilgisi yazılır. DÖF kaydı tanımlama işleminde bu liste tipli alanın bilgisi girildiğinde DÖF Özet Raporu alındığında liste tipli alanın girilen bilgileri rapora basılacaktır.

#### **1.1.1.1.9.Sorgu Tipli Parametrik Alanların Listesi**

DÖF Modülünde Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri menüsünde Detay Bilgiler sekmesinde Sorgu tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Sorgu yazarak Sorgu tipli parametrik alanlar aratılır ve Sorgu tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Sorgu tipli parametrik alanların alan tanımlaması yapılır. Bu Sorgu tipli alanın daha sonra DÖF Özet raporunda gösterilme işleminde tag’ini kullanmak için tanımlama işlemi yapılacaktır. Bu alan tanımlaması yapılan Sorgu tipli parametrik alanları lbl kısa kodu kaldırarak:

<QPARAM1\>,<QPARAM2\>,….<QPARAM5\> şeklinde DÖF Özet Raporu formatına tag şeklinde eklendiğinde DÖF kaydı ekranında Sorgu tipli alanların girilen değerleri bilgisi ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload00d134af-80dc-4220-ae10-fd5d09b60c9f)(Excel aktar) butonu tıklanarak alınan Excel formatındaki rapora basılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload22a805f8-07f9-4b8b-90b2-1fb939d3faeb)

#### **1.1.1.1.10.Sorgu Tipli Parametrik Alan Tanımlama**

Rapor formatına eklenecek Sorgu tipli parametrik bir alan tanımlaması yapılır. lblQPARAM1 Sorgu tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload722bdf4d-1181-42e1-884c-a75b26f3452a) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload43e2d819-1310-4ba0-9b1c-39f60230c530)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc24ad1e2-7ab7-40e6-ad99-2aac8729c09f)Bimser Destek ekibinde yardım alınarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd2790dd7-6d23-4df2-8bb8-cf76e9f61066)(kaydet) butonu tıklanarak Sorgu tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9a8d3b7a-2809-4c99-9fc0-99b266b5104d)

Tanımlanan Sorgu Tipli parametrik alan Entegre Yönetim Sistemi\>Düzeltici ve Önleyici Faaliyetler\>DÖF İşlemleri menüsünde ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload754ae0e2-aa30-4dac-8366-a79d6b297a26)(Yeni) butonu tıklanarak açılan DÖF işlemleri-Yeni Kayıt ekranında Detay Bilgiler sekmesinde görüntülenir. DÖF Özet Raporunun rapor formatına <QPARAM1\> tag şeklinde bilgisi yazılır. DÖF kaydı tanımlama işleminde bu sorgu tipli alanın bilgisi girildiğinde DÖF Özet Raporu alındığında sorgu tipli alanın girilen bilgileri rapora basılacaktır.

#### **1.1.1.1.11.Parasal Tipli Parametrik Alanların Listesi**

DÖF Modülünde Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri menüsünde Detay Bilgiler sekmesinde Parasal tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Parasal yazarak Parasal tipli parametrik alanlar aratılır ve Parasal tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Parasal tipli parametrik alanların alan tanımlaması yapılır. Bu Parasal tipli alanın daha sonra DÖF Özet raporunda gösterilme işleminde tag’ini kullanmak için tanımlama işlemi yapılacaktır. Bu alan tanımlaması yapılan Parasal tipli parametrik alanları lbl kısa kodu kaldırarak:

<NPARAM1_VALUE\>,..<NPARAM5_VALUE\>ve <NPARAM46_VALUE\>… <NPARAM50_VALUE\>,şeklinde DÖF Özet Raporu formatına tag şeklinde eklendiğinde DÖF kaydı ekranında parasal tipli alanların girilen değerleri bilgisi ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload00d134af-80dc-4220-ae10-fd5d09b60c9f)(Excel aktar) butonu tıklanarak alınan Excel formatındaki rapora basılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload866a5713-1d1c-4e4c-8b06-22b8a80a3c70)

#### **1.1.1.1.12.Parasal Tipli Parametrik Alan Tanımlama**

Rapor formatına eklenecek Parasal tipli parametrik bir alan tanımlaması yapılır. lblNPARAM1 Parasal tipli alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload722bdf4d-1181-42e1-884c-a75b26f3452a) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload653cfe61-93ce-4cdb-976c-b5fbd613c02f)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5a7866fe-a63d-4ce5-83d8-a0f677aecc6c)

Alanın zorunlu olup, olmayacağı sıra no bilgisi, görüntülenecek işlem kaynağı bilgisi ve DÖF türü seçeneklerinde seçim yapılarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd2790dd7-6d23-4df2-8bb8-cf76e9f61066)(Kaydet ) butonu tıklanarak Parasal tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb73c63b1-77f6-4cf9-9740-cb794a0db54f)

Tanımlanan Parasal Tipli parametrik alan Entegre Yönetim Sistemi\>Düzeltici ve Önleyici Faaliyetler\>DÖF İşlemleri menüsünde ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload754ae0e2-aa30-4dac-8366-a79d6b297a26)(Yeni) butonu tıklanarak açılan DÖF işlemleri-Yeni Kayıt ekranında Detay Bilgiler sekmesinde görüntülenir. DÖF Özet Raporunun rapor formatına <NPARAM1_VALUE\> tag şeklinde bilgisi yazılır. DÖF kaydı tanımlama işleminde bu parasal tipli alanın bilgisi girildiğinde DÖF Özet Raporu alındığında parasal tipli alanın girilen bilgileri rapora basılacaktır.

### **1.1.1.2. Düzeltici ve Önleyici Faaliyetler Modülünde Gelişme Raporu Sekmesinde Parametrik Alan Tipi Tanımlaması**

Düzeltici ve Önleyici Faaliyetler Modülünde Gelişme Raporu sekmesinde tanımlanan parametrik alanların kısa kodları lblG\_ başlığı ile tanımlı kısa kodlardır. lblG\_ başlığındaki kısa kodlar olan tüm parametrik tipli alanlar tanımlandığında Düzeltici ve Önleyici Faaliyetler Modülünde Gelişme Raporu sekmesi ekranında görüntülenir.

#### **1.1.1.2.1.Liste Tipli Parametrik Alanların Listesi**

DÖF Modülünde Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Gelişme Raporu sekmesinde liste tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına liste yazarak liste tipli parametrik alanlar aratılır ve liste tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Liste tipli parametrik alanların alan tanımlaması yapılır. Bu liste tipli alanın daha sonra DÖF Özet raporunda gösterilme işleminde tag’ini kullanmak için tanımlama işlemi yapılacaktır. Bu alan tanımlaması yapılan liste tipli parametrik alanları lblG kısa kodu kaldırarak:

<GELISME_LPARAM1_VALUE\>… <GELISME_LPARAM10_VALUE\> şeklinde DÖF Özet Raporu formatına tag şeklinde eklendiğinde DÖF kaydı ekranında liste tipli alanların girilen değerleri bilgisi ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload00d134af-80dc-4220-ae10-fd5d09b60c9f)(Excel aktar) butonu tıklanarak alınan Excel formatındaki rapora basılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb769aacb-c77b-4c08-8cce-e1c53c0a67ed)

#### **1.1.1.2.2.Liste Tipli Parametrik Alan Tanımlama**

Rapor formatına eklenecek liste tipli parametrik bir alan tanımlaması yapılır. lblG_LParam2 Liste tipli parametrik seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload722bdf4d-1181-42e1-884c-a75b26f3452a) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade7c94879-da14-4e37-aa78-a89c4b30e013)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload63d26e78-c865-4a13-a21b-db3839b4e460)

Liste tipli alanın liste değerlerini girmek için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4c9c612e-d770-4ce2-9e51-1b761a01dda4) (Yeni) butonuna tıklanır, liste değerleri yazılır ve kaydedilir. Liste eleman değeri 1 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1a11f433-6245-4bf2-a082-90dbc195ebae)

Liste eleman değeri 2 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb9fb3b88-2577-47ff-b6d6-c1c801fb5e37)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload755cce09-34f7-4e82-a639-8e66645daaff)

Alanın zorunlu olup, olmayacağı sıra no bilgisi ve liste elemanları tanımlanarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd2790dd7-6d23-4df2-8bb8-cf76e9f61066)(kaydet) butonu tıklanarak liste tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload93f3e1f0-ac03-48bd-979c-486e9c26ed56)

Tanımlanan liste tipli parametrik Alan Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Gelişme Raporu sekmesinde görüntülenir. DÖF Özet Raporunun rapor formatına <GELISME_LPARAM2_VALUE\> tag şeklinde bilgisi yazılır. DÖF kaydı tanımlama işleminde bu liste tipli alanın bilgisi girildiğinde DÖF Özet Raporu alındığında liste tipli alanın girilen bilgileri rapora basılacaktır.

#### **1.1.1.2.3.Personel Tipli Parametrik Alanların Listesi**

DÖF Modülünde Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Gelişme Raporu sekmesinde Personel tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Personel yazarak Personel tipli parametrik alanlar aratılır ve Personel tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Personel tipli parametrik alanların alan tanımlaması yapılır. Bu Personel tipli alanın daha sonra DÖF Özet raporunda gösterilme işleminde tag’ini kullanmak için tanımlama işlemi yapılacaktır Bu alan tanımlaması yapılan Personel tipli parametrik alanları lbG kısa kodu kaldırarak:

<GELISME_PPARAM1_VALUE\>…<GELISME_PPARAM10_VALUE\> şeklinde DÖF Özet Raporu formatına tag şeklinde eklendiğinde DÖF kaydı ekranında Personel tipli alanların girilen değerleri bilgisi ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload00d134af-80dc-4220-ae10-fd5d09b60c9f)(Excel aktar) butonu tıklanarak alınan Excel formatındaki rapora basılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4865dee9-58e1-4342-a66f-cc7dd9d1150a)

#### **1.1.1.2.4.Personel Tipli Parametrik Alan Tanımlama.**

Rapor formatına eklenecek Personel tipli parametrik bir alan tanımlaması yapılır. lblG_PParam2 Personel tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload722bdf4d-1181-42e1-884c-a75b26f3452a) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3c3d4c7f-2193-4b4d-a289-534e55b6cf68)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload45909f91-37e6-45d9-9388-8609d499614c)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd2790dd7-6d23-4df2-8bb8-cf76e9f61066)(kaydet) butonu tıklanarak Personel tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2ac4a5c2-d254-46ba-b796-617f68b7f94d)

Tanımlanan Personel tipli parametrik Alan Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Gelişme Raporu sekmesinde görüntülenir. DÖF Özet Raporunun rapor formatına <GELISME_PPARAM2_VALUE\> tag şeklinde bilgisi yazılır. DÖF kaydı tanımlama işleminde bu Personel tipli alanın bilgisi girildiğinde DÖF Özet Raporu alındığında Personel tipli alanın girilen bilgileri rapora basılacaktır.

#### **1.1.1.2.5.Metin Tipli Parametrik Alanların Listesi**

DÖF Modülünde Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Gelişme Raporu sekmesinde Metin tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Metin yazarak Metin tipli parametrik alanlar aratılır ve Metin tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Metin tipli parametrik alanların alan tanımlaması yapılır. Bu Metin tipli alanın daha sonra DÖF Özet raporunda gösterilme işleminde tag’ini kullanmak için tanımlama işlemi yapılacaktır Bu alan tanımlaması yapılan Metin tipli parametrik alanları lblG kısa kodu kaldırarak:

<GELISME_PARAM1\>,.. <GELISME_PARAM12\> şeklinde DÖF Özet Raporu formatına tag şeklinde eklendiğinde DÖF kaydı ekranında Metin tipli alanların girilen değerleri bilgisi ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload00d134af-80dc-4220-ae10-fd5d09b60c9f) (Excel aktar) butonu tıklanarak alınan Excel formatındaki rapora basılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada24cda48-a1b5-4271-a4a3-a3715a449cc5)

#### **1.1.1.2.6.Metin Tipli Parametrik Alan Tanımlama**

Rapor formatına eklenecek Metin tipli parametrik bir alan tanımlaması yapılır. lblG_Param2 Metin tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload722bdf4d-1181-42e1-884c-a75b26f3452a) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb7d7ed7f-5f15-46c1-97a2-44be3089e764)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadedbd3a81-ee85-4867-a5cb-1cbffe725dae)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd2790dd7-6d23-4df2-8bb8-cf76e9f61066)(kaydet) butonu tıklanarak Metin tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf84dd1f6-9eef-43cf-9f41-f5a6caff1331)

Tanımlanan Metin tipli parametrik Alan Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Gelişme Raporu sekmesinde görüntülenir. DÖF Özet Raporunun rapor formatına <GELISME_PARAM1\> tag şeklinde bilgisi yazılır. DÖF kaydı tanımlama işleminde bu Metin tipli alanın bilgisi girildiğinde DÖF Özet Raporu alındığında Metin tipli alanın girilen bilgileri rapora basılacaktır.

### **1.1.1.3.Düzeltici ve Önleyici Faaliyetler Modülünde Sonuç Raporu Sekmesinde Parametrik Alan Tipi Tanımlaması.**

Düzeltici ve Önleyici Faaliyetler Modülünde Sonuç Raporu sekmesinde tanımlanan parametrik alanların kısa kodları lblS\_ başlığı ile tanımlı kısa kodlardır. lblS\_ başlığındaki kısa kodlar olan tüm parametrik tipli alanlar tanımlandığında Düzeltici ve Önleyici Faaliyetler Modülünde Sonuç Raporu sekmesi ekranında görüntülenir.

#### **1.1.1.3.1.Metin Tipli Parametrik Alanların Listesi**

DÖF Modülünde Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Sonuç Raporu sekmesinde metin tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına metin yazarak metin tipli parametrik alanlar aratılır metin tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen metin tipli parametrik alanların alan tanımlaması yapılır. Bu Metin tipli alanın daha sonra DÖF Özet raporunda gösterilme işleminde tag’ini kullanmak için tanımlama işlemi yapılacaktır Bu alan tanımlaması yapılan metin tipli parametrik alanları lblS\_ kısa kodu kaldırarak:

<SONUC_PARAM1\>…<SONUC_PARAM10\> şeklinde DÖF Özet Raporu formatına tag şeklinde eklendiğinde DÖF kaydı ekranında metin tipli alanların girilen değerleri bilgisi ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload00d134af-80dc-4220-ae10-fd5d09b60c9f) (Excel aktar) butonu tıklanarak alınan Excel formatındaki rapora basılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload91f152dc-98aa-43ae-8c98-ce7748f8ec84)

#### **1.1.1.3.2.Metin Tipli Parametrik Alan Tanımlama**

Rapor formatına eklenecek Metin tipli parametrik bir alan tanımlaması yapılır. lblS_Param2 Metin tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload722bdf4d-1181-42e1-884c-a75b26f3452a) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload933612a5-76c4-448b-a8f6-b4a45c1e12e3)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload50fc3742-0c5d-4455-940a-2993da494ff3)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd2790dd7-6d23-4df2-8bb8-cf76e9f61066)(kaydet) butonu tıklanarak metin tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcf522d13-ae73-4b4f-8577-2d093803f9b5)

Tanımlanan metin tipli parametrik alan Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Sonuç Raporu sekmesinde görüntülenir. DÖF Özet Raporunun rapor formatına <SONUC_PARAM2\> tag şeklinde bilgisi yazılır. DÖF kaydı tanımlama işleminde bu Metin tipli alanın bilgisi girildiğinde DÖF Özet Raporu alındığında parasal tipli alanın girilen bilgileri rapora basılacaktır.

### **1.1.1.4.Düzeltici ve Önleyici Faaliyetler Modülünde Kapatma Sekmesinde Parametrik Alan Tipi Tanımlaması**

Düzeltici ve Önleyici Faaliyetler Modülünde Kapatma sekmesinde tanımlanan parametrik alanların kısa kodları lblK\_ başlığı ile tanımlı kısa kodlardır. lblK\_ başlığındaki kısa kodlar olan tüm parametrik tipli alanlar tanımlandığında Düzeltici ve Önleyici Faaliyetler Modülünde Kapatma sekmesi ekranında görüntülenir.

#### **1.1.1.4.1. Metin Tipli Parametrik Alanların Listesi**

DÖF Modülünde Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Kapatma sekmesinde metin tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına metin yazarak metin tipli parametrik alanlar aratılır metin tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen metin tipli parametrik alanların alan tanımlaması yapılır. Bu metin tipli alanın daha sonra DÖF Özet raporunda gösterilme işleminde tag’ini kullanmak için tanımlama işlemi yapılacaktır Bu alan tanımlaması yapılan metin tipli parametrik alanları lblK\_ kısa kodu kaldırarak:

<KAPATMA_PARAM1\>…<KAPATMA_PARAM10\> şeklinde DÖF Özet Raporu formatına tag şeklinde eklendiğinde DÖF kaydı ekranında Metin tipli alanların girilen değerleri bilgisi ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload00d134af-80dc-4220-ae10-fd5d09b60c9f) (Excel aktar) butonu tıklanarak alınan Excel formatındaki rapora basılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload36978803-d579-49c7-be81-21b7992ebad7)

#### **1.1.1.4.2.Metin Tipli Parametrik Alan Tanımlama**

Rapor formatına eklenecek Metin tipli parametrik bir alan tanımlaması yapılır. lblK_Param2 Metin tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload722bdf4d-1181-42e1-884c-a75b26f3452a) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8ff2b0fa-be71-4662-a5a5-fdc0596025d5)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4c87817c-5082-40e2-ac45-bfe8f93ce12b)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd2790dd7-6d23-4df2-8bb8-cf76e9f61066)(kaydet) butonu tıklanarak metin tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload08f68e0b-c8dd-4e68-987b-5d57b016ced7)

Tanımlanan metin tipli parametrik alan Entegre Yönetim Sistemi\> Düzeltici ve Önleyici Faaliyetler\> DÖF İşlemleri -Kayıt Güncelleme ekranında Kapatma sekmesinde görüntülenir.DÖF Özet Raporunun rapor formatına <KAPATMA_PARAM2\> tag şeklinde bilgisi yazılır. DÖF kaydı tanımlama işleminde bu Metin tipli alanın bilgisi girildiğinde DÖF Özet Raporu alındığında Metin tipli alanın girilen bilgileri rapora basılacaktır.

### **1.1.2.DÖF Özet Raporu Formatına Tag Eklenecek Alanların Değerlerin Girilmesi**

DÖF Özet Raporu formatına tag eklenecek alanların değerlerin girilmesi için DÖF Modülünde yeni bir DÖF kaydı açılır. Açılan DÖF kaydına tag eklenecek alanların bilgisi girilir. DÖF modülünde açılan DÖF kaydına tanımlanan parametrik alanların tiplerini bilgisi girildikten sonra rapor formatına eklenen alanların tagleri ile rapora bu alanların bilgisinin basılma sağlanılır. Raporda tanımlanan alan değerlerin bilgisinin gelmesi için DÖF kaydı ekranında alan bilgilerin girilmesi gerekmektedir.

### **1.1.2.1.DÖF Açma**

Entegre Yönetim Sistemi/ Düzeltici Faaliyetler/ DÖF İşlemleri menüsü tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload62f5a255-ce52-4208-8a92-99a48b7e4c34)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload754ae0e2-aa30-4dac-8366-a79d6b297a26) Yeni butonu ile DÖF İşlemleri / Yeni Kayıt ekranına gelinir. DÖF sekmesinde DÖF ile ilgili genel bilgilerin girişi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbf7db83a-2db6-4eba-9972-0a13c1ea8501)

Detay Bilgiler sekmesinde dil ayarlarında tanımlanmış parametrik alanların bilgi girişi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload103a7010-d6d6-4777-8f42-9d46cdefec1b)

Çözüm Ekibi sekmesi tıklanarak DÖF Çözüm Ekibi tanımlanır. DÖF Çözüm Ekibi ekranında çözüm ekibi lideri ve sorumlu departman seçilir. Ekip üyeleri, personel listesinden seçilir. Ayrıca Gelişme Raporu’nun yazılacağı son tarih belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0997dbdc-3bb8-4f45-b98c-856efaca8718)

Ek Dosyalar sekmesine geçilerek istenirse DÖF kaydına doküman, ses, görüntü vb. formatlarda istenen dosyaların eklenmesi gerçekleştirilebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9e3a0487-2971-40df-9b57-d3a19f386d81)

**![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload58bd0aed-9493-4a88-885b-21074f9d41a4)**(Kaydet) butonu ile kaydedildiğinde eğer DÖF açma onayı için bir akış kurgulandıysa ilgili rolün onayına kurgulanmadıysa Ekip Liderine Gelişme Raporu yazılması için görev düşer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf72adf67-e5e3-4203-89d5-ec413af0af9b)

### **1.1.2.2.Gelişme Raporu**

**DÖF kaydı gelişme raporu yazmak üzere Ekip Liderinin ve Ekip Üyesi atanan kişilerin  bekleyen işlerine iş olarak düşer.** Bekleyen İşleri’ne “**Gelişme Raporu Yazılacak DÖF’ler Listesi**” olarak iş düşer. İlgili DÖF no’su üzerine tıklayarak DÖF bilgilerinin olduğu ekrana açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload47ca5894-2424-4a7d-a71f-e1c940aaaa79)

Gelişme Raporu sekmesinde bilgileri doldulur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload736596f8-212b-42e0-841f-7aa7022ebb1d)

**Ekip lideri Acil aldığı önlemleri ve DÖF çalışmasının gidişatını Gelişme raporunda belirtir. DÖF Sonuçlandırma süresini, Ekibini varsa ek dosyasını ekleyerek kaydet butonunu tıklar ise bir sonra ki aşamaya geçilir. ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload599f24d7-72d8-4cef-be89-58051529b276) (**Kaydet) butonuyla Gelişme Raporu kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadff47fe96-67eb-4320-ad82-4a54a5b6f1de)

### **1.1.2.3.Kök Neden Analizi ve Aksiyon Planlama**

Gelişme Raporu aşamasında sonra “**“Kök Neden Analizi Yapılacak/Aksiyon Planlanacak DÖF’ler Listesi**” olarak iş düşer. DÖF no’su üzerine tıklayarak DÖF bilgilerinin olduğu ekrana açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1a99de03-0d6c-492a-8f5d-07dde8513a31)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc21e189-3720-45d7-851e-cb535bafc751) (Yeni) butonu tıklanarak kök neden ekleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload103b8cc0-257b-4c6b-a117-c5ee32cf86ac)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf1c36b15-24e7-4e51-83da-266ecbb1cf4e)

Açılan ekranda daha önceden tanımlanan kök nedenlerden istenenler seçilir, açıklama bilgisi girilir. Daha sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbe88c4d4-596f-4bb0-92e2-598b23d86ec1) kaydet butonu tıklanarak kök neden kaydedilerek DÖF ile ilişkisi kurulmuş olur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadeddeb92d-2c2b-4b16-a46d-1dc640c5c27d)

### **1.1.2.4.Aksiyonlar**

Kök Nedenler belirlendikten sonra süreç, DÖF Aksiyonlarının planlanması ile devam eder. Aksiyonlar sekmesine gelinir. Burada DÖF ile ilgili oluşturulacak aksiyonlar planlanır ve iş olarak atanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbe031a81-ee16-4c85-b1c0-7ffec4428c29)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3c39eb67-4eed-4085-9191-f6d28bbfb1d1) Yeni butonu tıklanarak Aksiyonlar-Yeni Kayıt ekranına gelinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload195d2433-766c-4313-9459-ca3b2b1d0e78)

Açılan ekranda Aksiyondan sorumlu kişi ve aksiyonu yapacak kişi listeden seçilir, aksiyon bilgisi girilir, aksiyonun planlanan bitiş tarihi belirlenir, aksiyon ile ilgili standart madde numaraları eklenebilir, aksiyon ile ilgili varsa referans dokümanlar ve kök nedenler eklenir. Yine istenirse Ek Dosyalar kısmından, Aksiyon ile alakalı ek dosya, doküman vb. eklenebilir.

Aksiyon bilgileri girildikten sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2d9728ed-830c-432c-ba52-52ba0197dbca) (kaydet) butonuyla aksiyon planlanmış olur ve işi yapacak kişiye bilgilendirme olarak mail yoluyla gönderilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6033a291-aa40-4848-b8f2-cec46c327ac3)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload67142aa3-805a-40b9-b413-7c067227d7d7)

Aksiyon listesinde görüntülenir ve aksiyonu gerçekleştirecek kişinin Bekleyen İşleri’nde “**Gerçekleştirilecek DÖF Aksiyonları”** listesi altında belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6097026f-fa16-47cf-917e-e53bd783deae)

Bekleyen İşleri’nden “**Gerçekleştirilecek DÖF Aksiyonlar Listesi**” nde DÖF-Aksiyon No üzerine tıklanır. DÖF bilgileri ekranına ulaşılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb7a95868-caa9-4bf9-b7d2-f6a55d59932c)

Aksiyon Gerçekleştirme ekranında, aksiyonun gerçekleştirme bilgisi ve gerçekleştirme tarihi girilir. Ayrıca istenirse aksiyonun gerçekleştirme aşamasına ek dosya eklenebilir. Yapılan iş ve varsa ek dosya eklendikten sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2d9728ed-830c-432c-ba52-52ba0197dbca)(kaydet) butonunu tıkladığımızda aksiyon gerçekleştirilmiş olur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb597a0e8-1004-4988-ac08-ef23d42bc6db)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf67a83fe-6e42-4b73-a66c-00ac006522a5)

### **1.1.2.5.Sonuç Raporu**

Aksiyonlar planlanıp gerçekleştirildikten sonra süreç, sonuç raporunun yazılmasıyla devam eder. Ekip Lideri/ Üyesi, Bekleyen İşleri’ne gelerek “**Sonuç Raporu Yazılacak DÖF’ler Listesi** sekmesinin altında ilgili DÖF’ü görür ve DÖF no’suna tıklayarak DÖF bilgilerinin olduğu ekrana açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada57e16af-2aab-445c-a911-0484596645ba)

Sonuç raporu, DÖF ile ilgili alınan nihai önlemleri, çözüm önerilerini içeren bir rapordur. DÖF İşlemleri sırasında yapılan tüm işlemlerin özeti niteliğinde, Kapatma onayı verecek kişi için hazırlanan sonuç raporudur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6e2e17ba-657d-45d9-b2a9-6e00318a6784)

Açılan ekranda Sonuç Raporu yazılır. Sonuç Raporu’na eklenmek istenen ek dosyalar, eklenebilir. Daha sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2d9728ed-830c-432c-ba52-52ba0197dbca) (kaydet) butonuyla Sonuç Raporu kaydedilir ve DÖF kapatma onayına gider.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload86f67dfa-45da-40d7-842e-67943612cb0f)

Sonuç raporu yazılma işlemi kaydedildikten sonra, önceden belirlenen DÖF kapatma sorumlusuna **“Kapatılacak DÖF’ler Listesi”** olarak bekleyen işlerine düşecektir.

### **1.12.6.Kapatma**

**“Kapatılacak DÖF’ler Listesi** “ nde ilgili DÖF nosu tıklanarak DÖF kapatma sekmesi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload07ee1ae8-4fd1-4d26-a45a-c550bddb4e25)

DÖF no’su üzerine tıklayarak “**Onay Bekleyen DÖF’ler**”ekranına gelir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7b5b43e0-674e-4d0f-8141-6c4d76e6cd61)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4ff9a546-9cb5-4aa7-8c38-5efb998d33dc) (Kapatma) butonu tıklanarak DÖF’ü Kapatma aşaması görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9b5e1b13-f9fa-4d12-8078-01e99151d888)

Açılan ekranda yeterlilik bilgisi girilir. Ayrıca istenirse uygunsuzluk kategorisi alanına eklemeler yapılabilir. Yine istenirse kapatma aşamasına ek dosya eklenebilir. Gerekli alanlar doldurulduktan sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload01d426f2-4850-4db0-85c7-eae897c0c360) (kaydet) butonu tıklanarak bilgiler kaydedilir ve DÖF kapatılmış olur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc671f994-3eb1-4f24-a998-35cfe7858db7)

### **1.1.3.DÖF Özet  Rapor Formatına Tanımlanan Parametrik Alanların Taglerin Eklenmesi**

DÖF Özet Raporu tanımlanan parametrik alanların taglerin eklenmesi için SAT\>BSAT\> Konfigürasyon Ayarları\>Rapor Formatları Düzenleme menüsüne gidilir. Qdms tüm raporların yüklendiği menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf78247ce-c57c-4be1-98bd-ea1ca27e4373)

**Ekranda bulanan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf4e2f7b4-3d94-4efb-9837-16fce4bf3202): Sisteme yeni bir rapor formatı yüklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3c785927-c406-4b26-99b0-726d65837bf8): Listede seçili olan rapor formatı görüntülenip, indirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade7156e36-4b72-4c6a-9d7a-dba25dc1fc15): Listede seçili olan rapor formatı silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload34fa440f-f4e3-4dc0-be29-d5ca2a8770b6) (Görüntüle) butonu tıklanarak DÖF Özet Raporunun rapor format şablonu (DOF_OZET_RAPOR.xls) bilgisayara indirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload264a9945-1853-4ef8-950c-94ce4d01199f)

Rapor formatına tanımlanan parametrik alanların alan tanımları ve tagleri ilgili bilgiler yazılırak rapor aynı isimde formatı bilgisayara kaydedilir. Örnekte DÖF Dosya Adı metin parametrik alanın tag <PARAM2\> ve DÖF Dosya Detayı metin (Çoklu Satır) parametrik alanın tagi <PARAM8\> olacak şekilde rapor formatına yazılır. Diğer tanımlanan alan tiplerinin tagleri rapor formatınan eklenir.

Bilgisayara kaydedilen aynı isimdeki Rapor format (DOF_OZET_RAPOR.xls) ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadba6e2e9d-eedc-42dc-b713-9e9dd4a49e0e) (Yeni) butonu ile tekrar rapor formatları menüsüne sisteme yüklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada431138e-e4df-4538-ba53-489940a6e2b3)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8213fb84-09c6-415e-b8cf-f195b26a6a72)

Rapor formatları menüsünde aynı isimde rapor format yükleme işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload95c264ea-9c17-4ca7-b740-68dfd32f5cb4)

### **1.1.4. DÖF Özet Raporunun Rapor Formatına Eklenen Parametrik Alanların Gösterimi**

DÖF Özet Raporunun rapor formatına (DOF_OZET_RAPOR.xls) tag ekleme işlemi yapılan rapor format yükleme işleminde sonra Entegre Yönetim Sistemi\>Düzeltici ve Önleyici Faaliyetler \>Raporlar\>DÖF Özet Rapor menüsü tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload36908c58-4948-4b19-ad53-c22675ed2d1b)

Düzeltici ve Önleyici Faaliyetler Özet Raporu ekranında DÖF kodu alanına açılıp kapatılan DÖF kaydının kodu ve işlem kaynağı bilgisi yazılarak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcd83eacf-5cba-4670-b04c-27688614570e)(Ara) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4316d559-3b40-49a4-b062-c48089297252)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc2d605ee-fff6-48c3-99cd-11b080eeae5e) (Excel’e Aktar) butonu ile “DÖF Özet Raporu” Excel formatında görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9889c976-30fe-463c-8f0e-39901d2d44f8)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcb7eb0f8-ec1a-4aea-8472-00cfe171621a)

## **1.2. Düzeltici ve Önleyici Faaliyetler Modülünde Genel Replacement (Kısa Kodlar) Tag Tablosu**

Düzeltici ve Önleyici Modülünde kullanılan genel taglerin listesi aşağıdaki tabloda yer almaktadır.

| **Kısaltma (Kısalmalar tag şeklinde < \> isaretleri arasına yazılacaktır.)** | **Açıklama**                                             |
|-------------------------------------------------------------------------------|----------------------------------------------------------|
| DKOD                                                                          | DOF kodu                                                 |
| KAYNAK                                                                        | DOF kaynağı                                              |
| SISTEMEKT                                                                     | Sisteme ekleme tarihi                                    |
| MREF                                                                          | Denetimden açılan Müşteri şikayetleri için referans kodu |
| BILDIREN                                                                      | Bildiren kişi                                            |
| BILDIRIMT                                                                     | Bildirim Tarihi                                          |
| BILDIRIMS                                                                     | Bildirim şekli                                           |
| SIKAYETG                                                                      | Şikayet oluşturan sicil no                               |
| LIDER                                                                         | Lider sicil numarası                                     |
| SORUMLUD                                                                      | Sorumlu departman kodu                                   |
| UYGT                                                                          | DOF Uygunsuzluk tanımı                                   |
| UYGDT                                                                         | DOF Uygunsuzluk detayı                                   |
| URUN                                                                          | Ürün kodu                                                |
| GELRAPY                                                                       | Planlanan gelisme raporu tarihi                          |
| DURUM                                                                         | Durum bilgisi                                            |
| GELISMEYT                                                                     | Gelişme raporu yazma tarihi                              |
| GELISMERP                                                                     | Gelişme raporu                                           |
| SONRAPY                                                                       | Planlanan sonuç raporu tarihi                            |
| GELKYTUSR                                                                     | Gelişme raporu yazan sicili                              |
| NOTLAR                                                                        | Notlar                                                   |
| KAPATAN                                                                       | Kapatan kişinin sicil numarası                           |
| KAPATMAT                                                                      | Kapatma tarihi                                           |
| MKOD                                                                          | Müşteri kodu                                             |
| YETERLILIK                                                                    | Yeterlilik                                               |
| HATA6M                                                                        | Hata parametrik alan                                     |
| HATA5M                                                                        | Hata parametrik alan                                     |
| HATA4M                                                                        | Hata parametrik alan                                     |
| HATA3M                                                                        | Hata parametrik alan                                     |
| HATA2M                                                                        | Hata parametrik alan                                     |
| HATA1M                                                                        | Hata parametrik alan                                     |
| HATA6T                                                                        | Hata parametrik alan                                     |
| HATA5T                                                                        | Hata parametrik alan                                     |
| HATA4T                                                                        | Hata parametrik alan                                     |
| HATA3T                                                                        | Hata parametrik alan                                     |
| HATA2T                                                                        | Hata parametrik alan                                     |
| HATA1T                                                                        | Hata parametrik alan                                     |
| BOLUM1                                                                        | Hata parametrik alan                                     |
| BOLUM2                                                                        | Hata parametrik alan                                     |
| BOLUM3                                                                        | Hata parametrik alan                                     |
| BOLUM4                                                                        | Hata parametrik alan                                     |
| BOLUM5                                                                        | Hata parametrik alan                                     |
| BOLUM6                                                                        | Hata parametrik alan                                     |
| ORAN6                                                                         | Hata parametrik alan                                     |
| ORAN5                                                                         | Hata parametrik alan                                     |
| ORAN4                                                                         | Hata parametrik alan                                     |
| ORAN3                                                                         | Hata parametrik alan                                     |
| ORAN2                                                                         | Hata parametrik alan                                     |
| ORAN1                                                                         | Hata parametrik alan                                     |
| ONAY                                                                          | Onay                                                     |
| REDNEDENI                                                                     | Ret nedeni                                               |
| ISYERI_KODU                                                                   | iş yeri kodu                                             |
| SISTEM_KODU                                                                   | sistem kodu                                              |
| GELISMERP_ETKINLIK                                                            | Gelişme raporuna ait etkinlik                            |
| HATA_PER1                                                                     | Hata parametrik alan                                     |
| HATA_PER2                                                                     | Hata parametrik alan                                     |
| HATA_PER3                                                                     | Hata parametrik alan                                     |
| HATA_PER4                                                                     | Hata parametrik alan                                     |
| HATA_PER5                                                                     | Hata parametrik alan                                     |
| HATA_PER6                                                                     | Hata parametrik alan                                     |
| HATA_PER_ORAN1                                                                | Hata parametrik alan                                     |
| HATA_PER_ORAN2                                                                | Hata parametrik alan                                     |
| HATA_PER_ORAN3                                                                | Hata parametrik alan                                     |
| HATA_PER_ORAN4                                                                | Hata parametrik alan                                     |
| HATA_PER_ORAN5                                                                | Hata parametrik alan                                     |
| HATA_PER_ORAN6                                                                | Hata parametrik alan                                     |
| REDDEDEN                                                                      | Reddeden sicil                                           |
| PARAM2                                                                        | Parametrik alan                                          |
| PARAM3                                                                        | Parametrik alan                                          |
| PARAM4                                                                        | Parametrik alan                                          |
| PARAM5                                                                        | Parametrik alan                                          |
| SUREC_KODU                                                                    | Süreç kodu                                               |
| MALIYET                                                                       | Maliyet                                                  |
| PARAM6                                                                        | Parametrik alan                                          |
| PARAM7                                                                        | Parametrik alan                                          |
| PARAM9                                                                        | Parametrik alan                                          |
| NPARAM2                                                                       | Parametrik alan                                          |
| NPARAM4                                                                       | Parametrik alan                                          |
| NPARAM5                                                                       | Parametrik alan                                          |
| NPARAM6                                                                       | Parametrik alan                                          |
| NPARAM7                                                                       | Parametrik alan                                          |
| NPARAM8                                                                       | Parametrik alan                                          |
| NPARAM9                                                                       | Parametrik alan                                          |
| NPARAM10                                                                      | Parametrik alan                                          |
| NPARAM2_BIRIM                                                                 | Parametrik alan                                          |
| NPARAM4_BIRIM                                                                 | Parametrik alan                                          |
| NPARAM5_BIRIM                                                                 | Parametrik alan                                          |
| NPARAM6_BIRIM                                                                 | Parametrik alan                                          |
| NPARAM7_BIRIM                                                                 | Parametrik alan                                          |
| NPARAM8_BIRIM                                                                 | Parametrik alan                                          |
| NPARAM9_BIRIM                                                                 | Parametrik alan                                          |
| NPARAM10_BIRIM                                                                | Parametrik alan                                          |
| DPARAM1                                                                       | Parametrik alan                                          |
| LPARAM1                                                                       | Parametrik alan                                          |
| LPARAM10                                                                      | Parametrik alan                                          |
| LPARAM2                                                                       | Parametrik alan                                          |
| LPARAM3                                                                       | Parametrik alan                                          |
| NPARAM1                                                                       | Parametrik alan                                          |
| NPARAM1_BIRIM                                                                 | Parametrik alan                                          |
| NPARAM3                                                                       | Parametrik alan                                          |
| NPARAM3_BIRIM                                                                 | Parametrik alan                                          |
| PARAM1                                                                        | Parametrik alan                                          |
| PARAM10                                                                       | Parametrik alan                                          |
| PARAM8                                                                        | Parametrik alan                                          |
| PPARAM1                                                                       | Parametrik alan                                          |
| QPARAM1                                                                       | Parametrik alan                                          |
| QPARAM2                                                                       | Parametrik alan                                          |
| DPARAM2                                                                       | Parametrik alan                                          |
| DPARAM3                                                                       | Parametrik alan                                          |
| DPARAM4                                                                       | Parametrik alan                                          |
| DPARAM5                                                                       | Parametrik alan                                          |
| PPARAM2                                                                       | Parametrik alan                                          |
| PPARAM3                                                                       | Parametrik alan                                          |
| PPARAM4                                                                       | Parametrik alan                                          |
| PPARAM5                                                                       | Parametrik alan                                          |
| LPARAM4                                                                       | Parametrik alan                                          |
| DPARAM1                                                                       | Parametrik alan                                          |
| LPARAM1                                                                       | Parametrik alan                                          |
| LPARAM10                                                                      | Parametrik alan                                          |
| LPARAM2                                                                       | Parametrik alan                                          |
| LPARAM3                                                                       | Parametrik alan                                          |
| LPARAM5                                                                       | Parametrik alan                                          |
| NPARAM1                                                                       | Parametrik alan                                          |
| NPARAM1_BIRIM                                                                 | Parametrik alan                                          |
| NPARAM3                                                                       | Parametrik alan                                          |
| NPARAM3_BIRIM                                                                 | Parametrik alan                                          |
| PARAM1                                                                        | Parametrik alan                                          |
| PARAM10                                                                       | Parametrik alan                                          |
| PARAM8                                                                        | Parametrik alan                                          |
| PPARAM1                                                                       | Parametrik alan                                          |
| QPARAM1                                                                       | Parametrik alan                                          |
| QPARAM2                                                                       | Parametrik alan                                          |
| GELISME_PARAM1                                                                | Gelişme parametrik alan                                  |
| GELISME_PARAM2                                                                | Gelişme parametrik alan                                  |
| GELISME_PARAM3                                                                | Gelişme parametrik alan                                  |
| GELISME_LPARAM1                                                               | Gelişme parametrik alan                                  |
| GELISME_LPARAM2                                                               | Gelişme parametrik alan                                  |
| GELISME_LPARAM3                                                               | Gelişme parametrik alan                                  |
| GELISME_NPARAM1                                                               | Gelişme parametrik alan                                  |
| GELISME_NPARAM2                                                               | Gelişme parametrik alan                                  |
| GELISME_NPARAM3                                                               | Gelişme parametrik alan                                  |
| GELISME_NPARAM4                                                               | Gelişme parametrik alan                                  |
| GELISME_NPARAM5                                                               | Gelişme parametrik alan                                  |
| GELISME_NPARAM1_BIRIM                                                         | Gelişme parametrik alan                                  |
| GELISME_NPARAM2_BIRIM                                                         | Gelişme parametrik alan                                  |
| GELISME_NPARAM3_BIRIM                                                         | Gelişme parametrik alan                                  |
| GELISME_NPARAM4_BIRIM                                                         | Gelişme parametrik alan                                  |
| GELISME_NPARAM5_BIRIM                                                         | Gelişme parametrik alan                                  |
| ONAY_DURUM                                                                    | Onay durumu                                              |
| SONUCRP                                                                       | Sonuç raporu                                             |
| SONUCRPYT                                                                     | Sonuç raporu yazma tarihi                                |
| SONUCRPKYTUSR                                                                 | Sonuç raporunu yazanın sicil numarası                    |
| AKSIYON_DURUM                                                                 | Aksiyon durumu                                           |
| AKSIYON_SONUC_TARIHI                                                          | Aksiyon sonuç tarihi                                     |
| DOF_SONUC_TARIHI                                                              | DOF sonuç tarihi                                         |
| DUZELTICIONLEYICI                                                             | Düzeltici mi önleyici mi durumu                          |
| REF_MODULE                                                                    | Referans modül                                           |
| REF_MODULE_CODE                                                               | Referans modül kodu                                      |
| PARAM11                                                                       | Parametrik alan                                          |
| PARAM12                                                                       | Parametrik alan                                          |
| PARAM13                                                                       | Parametrik alan                                          |
| PARAM14                                                                       | Parametrik alan                                          |
| PARAM15                                                                       | Parametrik alan                                          |
| LPARAM6                                                                       | Parametrik alan                                          |
| LPARAM7                                                                       | Parametrik alan                                          |
| LPARAM8                                                                       | Parametrik alan                                          |
| LPARAM9                                                                       | Parametrik alan                                          |
| ETKINLIK                                                                      | Etkinlik                                                 |
| ETKINLIK_PUANI                                                                | Etkinlik puanı                                           |
| ESKI_DURUM                                                                    | Eski durum                                               |
| ESKI_ONAY_DURUM                                                               | Eski onay durumu                                         |
| SONUC_PARAM1                                                                  | Sonuç parametrik alan                                    |
| SONUC_PARAM2                                                                  | Sonuç parametrik alan                                    |
| SONUC_PARAM3                                                                  | Sonuç parametrik alan                                    |
| SONUC_PARAM4                                                                  | Sonuç parametrik alan                                    |
| SONUC_PARAM5                                                                  | Sonuç parametrik alan                                    |
| SONUC_PARAM6                                                                  | Sonuç parametrik alan                                    |
| SONUC_PARAM7                                                                  | Sonuç parametrik alan                                    |
| SONUC_PARAM8                                                                  | Sonuç parametrik alan                                    |
| SONUC_PARAM9                                                                  | Sonuç parametrik alan                                    |
| SONUC_PARAM10                                                                 | Sonuç parametrik alan                                    |
| SONUC_LPARAM1                                                                 | Sonuç parametrik alan                                    |
| SONUC_LPARAM2                                                                 | Sonuç parametrik alan                                    |
| SONUC_LPARAM3                                                                 | Sonuç parametrik alan                                    |
| SONUC_LPARAM4                                                                 | Sonuç parametrik alan                                    |
| SONUC_LPARAM5                                                                 | Sonuç parametrik alan                                    |
| SONUC_LPARAM6                                                                 | Sonuç parametrik alan                                    |
| SONUC_LPARAM7                                                                 | Sonuç parametrik alan                                    |
| SONUC_LPARAM8                                                                 | Sonuç parametrik alan                                    |
| SONUC_LPARAM9                                                                 | Sonuç parametrik alan                                    |
| SONUC_LPARAM10                                                                | Sonuç parametrik alan                                    |
| SONUC_NPARAM1                                                                 | Sonuç parametrik alan                                    |
| SONUC_NPARAM2                                                                 | Sonuç parametrik alan                                    |
| SONUC_NPARAM3                                                                 | Sonuç parametrik alan                                    |
| SONUC_NPARAM4                                                                 | Sonuç parametrik alan                                    |
| SONUC_NPARAM5                                                                 | Sonuç parametrik alan                                    |
| SONUC_NPARAM1_BIRIM                                                           | Sonuç parametrik alan                                    |
| SONUC_NPARAM2_BIRIM                                                           | Sonuç parametrik alan                                    |
| SONUC_NPARAM3_BIRIM                                                           | Sonuç parametrik alan                                    |
| SONUC_NPARAM4_BIRIM                                                           | Sonuç parametrik alan                                    |
| SONUC_NPARAM5_BIRIM                                                           | Sonuç parametrik alan                                    |
| SONUC_LMPARAM1                                                                | Sonuç parametrik alan                                    |
| SONUC_LMPARAM2                                                                | Sonuç parametrik alan                                    |
| SONUC_LMPARAM3                                                                | Sonuç parametrik alan                                    |
| SONUC_LMPARAM4                                                                | Sonuç parametrik alan                                    |
| SONUC_LMPARAM5                                                                | Sonuç parametrik alan                                    |
| SONUC_LMPARAM6                                                                | Sonuç parametrik alan                                    |
| SONUC_LMPARAM7                                                                | Sonuç parametrik alan                                    |
| SONUC_LMPARAM8                                                                | Sonuç parametrik alan                                    |
| SONUC_LMPARAM9                                                                | Sonuç parametrik alan                                    |
| SONUC_LMPARAM10                                                               | Sonuç parametrik alan                                    |
| KAPATMA_PARAM1                                                                | Kapatma parametrik alan                                  |
| KAPATMA_PARAM2                                                                | Kapatma parametrik alan                                  |
| KAPATMA_PARAM3                                                                | Kapatma parametrik alan                                  |
| KAPATMA_PARAM4                                                                | Kapatma parametrik alan                                  |
| KAPATMA_PARAM5                                                                | Kapatma parametrik alan                                  |
| KAPATMA_PARAM6                                                                | Kapatma parametrik alan                                  |
| KAPATMA_PARAM7                                                                | Kapatma parametrik alan                                  |
| KAPATMA_PARAM8                                                                | Kapatma parametrik alan                                  |
| KAPATMA_PARAM9                                                                | Kapatma parametrik alan                                  |
| KAPATMA_PARAM10                                                               | Kapatma parametrik alan                                  |
| KAPATMA_LPARAM1                                                               | Kapatma parametrik alan                                  |
| KAPATMA_LPARAM2                                                               | Kapatma parametrik alan                                  |
| KAPATMA_LPARAM3                                                               | Kapatma parametrik alan                                  |
| KAPATMA_LPARAM4                                                               | Kapatma parametrik alan                                  |
| KAPATMA_LPARAM5                                                               | Kapatma parametrik alan                                  |
| KAPATMA_LPARAM6                                                               | Kapatma parametrik alan                                  |
| KAPATMA_LPARAM7                                                               | Kapatma parametrik alan                                  |
| KAPATMA_LPARAM8                                                               | Kapatma parametrik alan                                  |
| KAPATMA_LPARAM9                                                               | Kapatma parametrik alan                                  |
| KAPATMA_LPARAM10                                                              | Kapatma parametrik alan                                  |
| KAPATMA_NPARAM1                                                               | Kapatma parametrik alan                                  |
| KAPATMA_NPARAM2                                                               | Kapatma parametrik alan                                  |
| KAPATMA_NPARAM3                                                               | Kapatma parametrik alan                                  |
| KAPATMA_NPARAM4                                                               | Kapatma parametrik alan                                  |
| KAPATMA_NPARAM5                                                               | Kapatma parametrik alan                                  |
| KAPATMA_NPARAM1_BIRIM                                                         | Kapatma parametrik alan                                  |
| KAPATMA_NPARAM2_BIRIM                                                         | Kapatma parametrik alan                                  |
| KAPATMA_NPARAM3_BIRIM                                                         | Kapatma parametrik alan                                  |
| KAPATMA_NPARAM4_BIRIM                                                         | Kapatma parametrik alan                                  |
| KAPATMA_NPARAM5_BIRIM                                                         | Kapatma parametrik alan                                  |
| ONAY_TARIHI                                                                   | Onay tarihi                                              |
| TERMIN_TARIHI                                                                 | Termin tarihi                                            |
| ILK_TERMIN_TARIHI                                                             | İlk termin tarihi                                        |
| OTOMATIK_AKSIYON                                                              | Otomatik aksiyon                                         |
| QPARAM3                                                                       | Sorgu tipli parametrik alan                              |
| QPARAM4                                                                       | Sorgu tipli parametrik alan                              |
| QPARAM5                                                                       | Sorgu tipli parametrik alan                              |
| MALIYET_BIRIM                                                                 | Maliyet birimi                                           |
| PARAM31                                                                       | Parametrik alan                                          |
| PARAM32                                                                       | Parametrik alan                                          |
| PARAM33                                                                       | Parametrik alan                                          |
| PARAM34                                                                       | Parametrik alan                                          |
| PARAM35                                                                       | Parametrik alan                                          |
| LPARAM36                                                                      | Parametrik alan                                          |
| LPARAM37                                                                      | Parametrik alan                                          |
| LPARAM38                                                                      | Parametrik alan                                          |
| LPARAM39                                                                      | Parametrik alan                                          |
| LPARAM40                                                                      | Parametrik alan                                          |
| NPARAM41                                                                      | Parametrik alan                                          |
| NPARAM42                                                                      | Parametrik alan                                          |
| NPARAM43                                                                      | Parametrik alan                                          |
| NPARAM44                                                                      | Parametrik alan                                          |
| NPARAM45                                                                      | Parametrik alan                                          |
| NPARAM46                                                                      | Parametrik alan                                          |
| NPARAM47                                                                      | Parametrik alan                                          |
| NPARAM48                                                                      | Parametrik alan                                          |
| NPARAM49                                                                      | Parametrik alan                                          |
| NPARAM50                                                                      | Parametrik alan                                          |
| NPARAM41_BIRIM                                                                | Parametrik alan                                          |
| NPARAM42_BIRIM                                                                | Parametrik alan                                          |
| NPARAM43_BIRIM                                                                | Parametrik alan                                          |
| NPARAM44_BIRIM                                                                | Parametrik alan                                          |
| NPARAM45_BIRIM                                                                | Parametrik alan                                          |
| NPARAM46_BIRIM                                                                | Parametrik alan                                          |
| NPARAM47_BIRIM                                                                | Parametrik alan                                          |
| NPARAM48_BIRIM                                                                | Parametrik alan                                          |
| NPARAM49_BIRIM                                                                | Parametrik alan                                          |
| NPARAM50_BIRIM                                                                | Parametrik alan                                          |
| DOCPARAM1                                                                     | Parametrik alan                                          |
| RET_TIPI                                                                      | Ret tipi                                                 |
| HATA1_BIRIM                                                                   | Hata parametrik alan                                     |
| HATA2_BIRIM                                                                   | Hata parametrik alan                                     |
| HATA3_BIRIM                                                                   | Hata parametrik alan                                     |
| HATA4_BIRIM                                                                   | Hata parametrik alan                                     |
| HATA5_BIRIM                                                                   | Hata parametrik alan                                     |
| HATA6_BIRIM                                                                   | Hata parametrik alan                                     |
| REF_DKOD                                                                      | Referans DOF kodu                                        |
| GELISME_PARAM4                                                                | Gelişme parametrik alan                                  |
| GELISME_PARAM5                                                                | Gelişme parametrik alan                                  |
| GELISME_PARAM6                                                                | Gelişme parametrik alan                                  |
| GELISME_PARAM7                                                                | Gelişme parametrik alan                                  |
| GELISME_PARAM8                                                                | Gelişme parametrik alan                                  |
| GELISME_PARAM9                                                                | Gelişme parametrik alan                                  |
| GELISME_PARAM10                                                               | Gelişme parametrik alan                                  |
| GELISME_PARAM11                                                               | Gelişme parametrik alan                                  |
| GELISME_PARAM12                                                               | Gelişme parametrik alan                                  |
| GELISME_LPARAM4                                                               | Gelişme parametrik alan                                  |
| GELISME_LPARAM5                                                               | Gelişme parametrik alan                                  |
| GELISME_LPARAM6                                                               | Gelişme parametrik alan                                  |
| GELISME_LPARAM7                                                               | Gelişme parametrik alan                                  |
| GELISME_LPARAM8                                                               | Gelişme parametrik alan                                  |
| GELISME_LPARAM9                                                               | Gelişme parametrik alan                                  |
| GELISME_LPARAM10                                                              | Gelişme parametrik alan                                  |
| GELISME_QPARAM1                                                               | Gelişme parametrik alan                                  |
| GELISME_QPARAM2                                                               | Gelişme parametrik alan                                  |
| GELISME_QPARAM3                                                               | Gelişme parametrik alan                                  |
| GELISME_QPARAM4                                                               | Gelişme parametrik alan                                  |
| GELISME_QPARAM5                                                               | Gelişme parametrik alan                                  |
| SONUC_QPARAM1                                                                 | Sonuç parametrik alan                                    |
| SONUC_QPARAM2                                                                 | Sonuç parametrik alan                                    |
| SONUC_QPARAM3                                                                 | Sonuç parametrik alan                                    |
| SONUC_QPARAM4                                                                 | Sonuç parametrik alan                                    |
| SONUC_QPARAM5                                                                 | Sonuç parametrik alan                                    |
| KAPATMA_QPARAM1                                                               | Kapatma parametrik alan                                  |
| KAPATMA_QPARAM2                                                               | Kapatma parametrik alan                                  |
| KAPATMA_QPARAM3                                                               | Kapatma parametrik alan                                  |
| KAPATMA_QPARAM4                                                               | Kapatma parametrik alan                                  |
| KAPATMA_QPARAM5                                                               | Kapatma parametrik alan                                  |
| GELISME_PPARAM1                                                               | Gelişme parametrik alan                                  |
| GELISME_PPARAM2                                                               | Gelişme parametrik alan                                  |
| GELISME_PPARAM3                                                               | Gelişme parametrik alan                                  |
| GELISME_PPARAM4                                                               | Gelişme parametrik alan                                  |
| GELISME_PPARAM5                                                               | Gelişme parametrik alan                                  |
| GELISME_PPARAM6                                                               | Gelişme parametrik alan                                  |
| GELISME_PPARAM7                                                               | Gelişme parametrik alan                                  |
| GELISME_PPARAM8                                                               | Gelişme parametrik alan                                  |
| GELISME_PPARAM9                                                               | Gelişme parametrik alan                                  |
| GELISME_PPARAM10                                                              | Gelişme parametrik alan                                  |
| SONUC_PPARAM1                                                                 | Sonuç parametrik alan                                    |
| SONUC_PPARAM2                                                                 | Sonuç parametrik alan                                    |
| SONUC_PPARAM3                                                                 | Sonuç parametrik alan                                    |
| SONUC_PPARAM4                                                                 | Sonuç parametrik alan                                    |
| SONUC_PPARAM5                                                                 | Sonuç parametrik alan                                    |
| SONUC_PPARAM6                                                                 | Sonuç parametrik alan                                    |
| SONUC_PPARAM7                                                                 | Sonuç parametrik alan                                    |
| SONUC_PPARAM8                                                                 | Sonuç parametrik alan                                    |
| SONUC_PPARAM9                                                                 | Sonuç parametrik alan                                    |
| SONUC_PPARAM10                                                                | Sonuç parametrik alan                                    |
| KAPATMA_PPARAM1                                                               | Kapatma parametrik alan                                  |
| KAPATMA_PPARAM2                                                               | Kapatma parametrik alan                                  |
| KAPATMA_PPARAM3                                                               | Kapatma parametrik alan                                  |
| KAPATMA_PPARAM4                                                               | Kapatma parametrik alan                                  |
| KAPATMA_PPARAM5                                                               | Kapatma parametrik alan                                  |
| KAPATMA_PPARAM6                                                               | Kapatma parametrik alan                                  |
| KAPATMA_PPARAM7                                                               | Kapatma parametrik alan                                  |
| KAPATMA_PPARAM8                                                               | Kapatma parametrik alan                                  |
| KAPATMA_PPARAM9                                                               | Kapatma parametrik alan                                  |
| KAPATMA_PPARAM10                                                              | Kapatma parametrik alan                                  |
| T2_ACIKLAMA                                                                   | Kaynak açıklaması                                        |
| T2_ICDIS                                                                      | İç veya dış müşteri şikayeti durumu                      |
| T3_ADISOYADI                                                                  | Bildiren adı soyadı                                      |
| T4_ADISOYADI                                                                  | Şikayet oluşturan kişinin adı soyadı                     |
| T5_ADISOYADI                                                                  | Lider adı soyadı                                         |
| T6_DEPARTMAN_ADI                                                              | Sorumlu departman adı                                    |
| T7_URUN_ADI                                                                   | Ürün adı                                                 |
| T8_ADISOYADI                                                                  | Gelişme raporu yazan adı soyadı                          |
| T9_ADISOYADI                                                                  | Kapatan adı soyadı                                       |
| T10_ISYERI_ADI                                                                | İş yeri adı                                              |
| T11_ACIKLAMA                                                                  | Sistem açıklaması                                        |
| T12_ADISOYADI                                                                 | Sonuç raporunu yazanın adı soyadı                        |
| T13_VALUE                                                                     | Düzeltici mi önleyici mi durumunun açıklaması            |
| ALAN1                                                                         | DOF parametrik alan                                      |
| ALAN1_ACK                                                                     | DOF parametrik alan                                      |
| ALAN1_DESC                                                                    | DOF parametrik alan                                      |
| ALAN2                                                                         | DOF parametrik alan                                      |
| ALAN2_ACK                                                                     | DOF parametrik alan                                      |
| ALAN2_DESC                                                                    | DOF parametrik alan                                      |
| ALAN3                                                                         | DOF parametrik alan                                      |
| ALAN4                                                                         | DOF parametrik alan                                      |
| ALAN4_ACK                                                                     | DOF parametrik alan                                      |
| ALAN6                                                                         | DOF parametrik alan                                      |
| ALAN7                                                                         | DOF parametrik alan                                      |
| ALAN7_ACK                                                                     | DOF parametrik alan                                      |
| ALAN8                                                                         | DOF parametrik alan                                      |
| ALAN9                                                                         | DOF parametrik alan                                      |
| ALAN10                                                                        | DOF parametrik alan                                      |
| ALAN10_ACK                                                                    | DOF parametrik alan                                      |
| ALAN10_DESC                                                                   | DOF parametrik alan                                      |
| ALAN11                                                                        | DOF parametrik alan                                      |
| MTB                                                                           | Müşteri adı veya departman adı                           |
| DURUM_ACK                                                                     | Durum açıklaması                                         |
| DOF_ACAN_DEPT                                                                 | DOF açan departman                                       |
| DOF_LIDERAMIRI                                                                | DOF lider amiri                                          |
| ISLEM_SURESI                                                                  | İşlem süresi                                             |
| DUZELTICIONLEYICI_ACK                                                         | Düzeltici mi önleyici mi durumunun açıklaması            |
| EKIP                                                                          | Ekip bilgisi                                             |
| BILGILENDIRME                                                                 | Bilgilendirme                                            |
| KOK_NEDENLER                                                                  | Kök nedenler                                             |
| KOKNEDEN_DETAYI                                                               | Kök neden detayı                                         |
| KOK_TARIH                                                                     | Kök neden tarihi                                         |
| MNPARAM                                                                       | Parametrik alan                                          |
| URUN_TIPI                                                                     | Ürün tipi                                                |
| SUREC_ADI                                                                     | Sürec adı                                                |
| SUREC                                                                         | Süreç kodu - süreç adı                                   |
| DENETIM_KODU                                                                  | Denetim kodu                                             |
| DENETIM_TANIMI                                                                | Denetim tanımı                                           |
| DENETIM_TIPI                                                                  | Denetim tipi                                             |
| UYG_KAT1                                                                      | Uygunsuzluk kategorisi                                   |
| UYG_KAT2                                                                      | Uygunsuzluk kategorisi                                   |
| UYG_KAT3                                                                      | Uygunsuzluk kategorisi                                   |
| UYG_KAT4                                                                      | Uygunsuzluk kategorisi                                   |
| UYG_KAT5                                                                      | Uygunsuzluk kategorisi                                   |
| GELISME_LPARAM1_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_LPARAM10_VALUE                                                        | Gelişme parametrik alan                                  |
| GELISME_LPARAM2_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_LPARAM3_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_LPARAM4_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_LPARAM5_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_LPARAM6_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_LPARAM7_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_LPARAM8_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_LPARAM9_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_NPARAM1_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_NPARAM2_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_NPARAM3_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_NPARAM4_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_NPARAM5_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_PPARAM1_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_PPARAM10_VALUE                                                        | Gelişme parametrik alan                                  |
| GELISME_PPARAM2_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_PPARAM3_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_PPARAM4_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_PPARAM5_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_PPARAM6_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_PPARAM7_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_PPARAM8_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_PPARAM9_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_QPARAM1_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_QPARAM1_KOD                                                           | Gelişme parametrik alan                                  |
| GELISME_QPARAM2_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_QPARAM2_KOD                                                           | Gelişme parametrik alan                                  |
| GELISME_QPARAM3_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_QPARAM3_KOD                                                           | Gelişme parametrik alan                                  |
| GELISME_QPARAM4_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_QPARAM4_KOD                                                           | Gelişme parametrik alan                                  |
| GELISME_QPARAM5_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_QPARAM5_KOD                                                           | Gelişme parametrik alan                                  |
| KAPATMA_LPARAM1_VALUE                                                         | Gelişme parametrik alan                                  |
| KAPATMA_QPARAM2_VALUE                                                         | Gelişme parametrik alan                                  |
| KAPATMA_QPARAM2_KOD                                                           | Gelişme parametrik alan                                  |
| LPARAM1_VALUE                                                                 | Parametrik alan                                          |
| LPARAM10_VALUE                                                                | Parametrik alan                                          |
| LPARAM2_VALUE                                                                 | Parametrik alan                                          |
| LPARAM3_VALUE                                                                 | Parametrik alan                                          |
| NPARAM1_VALUE                                                                 | Parametrik alan                                          |
| NPARAM3_VALUE                                                                 | Parametrik alan                                          |
| PPARAM1_VALUE                                                                 | Parametrik alan                                          |
| QPARAM1_VALUE                                                                 | Parametrik alan                                          |
| QPARAM1_KOD                                                                   | Parametrik alan                                          |
| QPARAM2_VALUE                                                                 | Parametrik alan                                          |
| QPARAM2_KOD                                                                   | Parametrik alan                                          |
| SONUC_LMPARAM1_VALUE                                                          | Sonuç parametrik alan                                    |
| SONUC_LMPARAM10_VALUE                                                         | Sonuç parametrik alan                                    |
| SONUC_LMPARAM2_VALUE                                                          | Sonuç parametrik alan                                    |
| SONUC_LMPARAM3_VALUE                                                          | Sonuç parametrik alan                                    |
| SONUC_LMPARAM4_VALUE                                                          | Sonuç parametrik alan                                    |
| SONUC_LMPARAM5_VALUE                                                          | Sonuç parametrik alan                                    |
| SONUC_LMPARAM6_VALUE                                                          | Sonuç parametrik alan                                    |
| SONUC_LMPARAM7_VALUE                                                          | Sonuç parametrik alan                                    |
| SONUC_LMPARAM8_VALUE                                                          | Sonuç parametrik alan                                    |
| SONUC_LMPARAM9_VALUE                                                          | Sonuç parametrik alan                                    |
| SONUC_LPARAM1_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_LPARAM10_VALUE                                                          | Sonuç parametrik alan                                    |
| SONUC_LPARAM2_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_LPARAM3_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_LPARAM4_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_LPARAM5_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_LPARAM6_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_LPARAM7_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_LPARAM8_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_LPARAM9_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_NPARAM1_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_NPARAM2_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_NPARAM3_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_NPARAM4_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_NPARAM5_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_PPARAM1_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_PPARAM10_VALUE                                                          | Sonuç parametrik alan                                    |
| SONUC_PPARAM2_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_PPARAM3_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_PPARAM4_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_PPARAM5_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_PPARAM6_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_PPARAM7_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_PPARAM8_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_PPARAM9_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_QPARAM1_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_QPARAM1_KOD                                                             | Sonuç parametrik alan                                    |
| SONUC_QPARAM2_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_QPARAM2_KOD                                                             | Sonuç parametrik alan                                    |
| SONUC_QPARAM3_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_QPARAM3_KOD                                                             | Sonuç parametrik alan                                    |
| SONUC_QPARAM4_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_QPARAM4_KOD                                                             | Sonuç parametrik alan                                    |
| SONUC_QPARAM5_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_QPARAM5_KOD                                                             | Sonuç parametrik alan                                    |
| YORUM                                                                         | Yorum                                                    |
| ACIK_STATUSUNE_DONDURME                                                       | Açık statüsü bilgisi(Adı soyadı-tarih-açıklama)          |
| KAPATMAONAY_0                                                                 | Kapatma onaycıları ve tarihler(10' a kadar gidiyor)      |
| ACMAONAY_0                                                                    | Açma onaycıları ve tarihler(10' a kadar gidiyor)         |
| GELISMEONAY_0                                                                 | Gelişme onaycıları ve tarihler(10' a kadar gidiyor)      |
| KAPATMAONAYTAR_0                                                              | Kapatma onay tarihleri(10' a kadar gidiyor)              |
| ACMAONAYTAR_0                                                                 | Açma onay tarihleri(10' a kadar gidiyor)                 |
| GELISMEONAYTAR_0                                                              | Gelişme onay tarihleri(10' a kadar gidiyor)              |
| ACMASURE_0                                                                    | Açma onay süresi(10' a kadar gidiyor)                    |
| KAPATMASURE_0                                                                 | Kapatma onay süresi(10' a kadar gidiyor)                 |
| GELISMESURE_0                                                                 | Gelişme onay süresi(10' a kadar gidiyor)                 |
| AKS_PLANONAY_TAR_0                                                            | Aksiyon plan onaycıları ve tarihler(3' e kadar gidiyor)  |
| AKS_PLANONAY_0                                                                | Aksiyon plan onay tarihleri(3' e kadar gidiyor)          |
| TOPLAM_ACMASURE                                                               | Toplam açma onay süresi                                  |
| TOPLAM_KAPATMASURE                                                            | Toplam Kapatma onay süresi                               |
| AKS_PLANONAY_TAR                                                              | Aksiyon plan onay tarihi                                 |
| AKS_PLANONAY_BASTAR                                                           | Aksiyon plan onay başlangıç tarihi                       |
| AKS_PLANONAY_RETTAR                                                           | Aksiyon plan onay ret tarihi                             |
| RET_NEDENI                                                                    | Ret nedeni                                               |
| RET_TARIHI                                                                    | Ret tarihi                                               |
| IZLEME                                                                        | İzleme                                                   |
| UPARAM                                                                        | Parametrik alan                                          |
| IZLEME1                                                                       | İzleme bilgisi(10' a kadar gidiyor)                      |
| IZLEME1_BASLANGIC_TARIHI                                                      | İzleme başlangıç tarihi(10' a kadar gidiyor)             |
| IZLEME1_SORUMLUSU                                                             | İzleme sorumlusu(10' a kadar gidiyor)                    |

## **1.3. DÖF Aksiyon 3 Raporu Replacement (Kısa Kodlar) Tag Tablosu**

Düzeltici ve Önleyici Modülünde kullanılan DÖF Aksiyon 3 Rapor taglerin listesi aşağıdaki tabloda yer almaktadır.

| **Kısaltma (Kısalmalar tag şeklinde < \> isaretleri arasına yazılacaktır.)** | **Açıklama**                                             |
|-------------------------------------------------------------------------------|----------------------------------------------------------|
| DKOD                                                                          | DOF kodu                                                 |
| KAYNAK                                                                        | DOF kaynağı                                              |
| SISTEMEKT                                                                     | Sisteme ekleme tarihi                                    |
| MREF                                                                          | Denetimden açılan Müşteri şikayetleri için referans kodu |
| BILDIREN                                                                      | Bildiren kişi                                            |
| BILDIRIMT                                                                     | Bildirim Tarihi                                          |
| BILDIRIMS                                                                     | Bildirim şekli                                           |
| SIKAYETG                                                                      | Şikayet oluşturan sicil no                               |
| LIDER                                                                         | Lider sicil numarası                                     |
| SORUMLUD                                                                      | Sorumlu departman kodu                                   |
| UYGT                                                                          | DOF Uygunsuzluk tanımı                                   |
| UYGDT                                                                         | DOF Uygunsuzluk detayı                                   |
| URUN                                                                          | Ürün kodu                                                |
| GELRAPY                                                                       | Planlanan gelisme raporu tarihi                          |
| DURUM                                                                         | Durum bilgisi                                            |
| GELISMEYT                                                                     | Gelişme raporu yazma tarihi                              |
| GELISMERP                                                                     | Gelişme raporu                                           |
| SONRAPY                                                                       | Planlanan sonuç raporu tarihi                            |
| GELKYTUSR                                                                     | Gelişme raporu yazan sicili                              |
| NOTLAR                                                                        | Notlar                                                   |
| KAPATAN                                                                       | Kapatan kişinin sicil numarası                           |
| KAPATMAT                                                                      | Kapatma tarihi                                           |
| MKOD                                                                          | Müşteri kodu                                             |
| YETERLILIK                                                                    | Yeterlilik                                               |
| HATA6M                                                                        | Hata parametrik alan                                     |
| HATA5M                                                                        | Hata parametrik alan                                     |
| HATA4M                                                                        | Hata parametrik alan                                     |
| HATA3M                                                                        | Hata parametrik alan                                     |
| HATA2M                                                                        | Hata parametrik alan                                     |
| HATA1M                                                                        | Hata parametrik alan                                     |
| HATA6T                                                                        | Hata parametrik alan                                     |
| HATA5T                                                                        | Hata parametrik alan                                     |
| HATA4T                                                                        | Hata parametrik alan                                     |
| HATA3T                                                                        | Hata parametrik alan                                     |
| HATA2T                                                                        | Hata parametrik alan                                     |
| HATA1T                                                                        | Hata parametrik alan                                     |
| BOLUM1                                                                        | Hata parametrik alan                                     |
| BOLUM2                                                                        | Hata parametrik alan                                     |
| BOLUM3                                                                        | Hata parametrik alan                                     |
| BOLUM4                                                                        | Hata parametrik alan                                     |
| BOLUM5                                                                        | Hata parametrik alan                                     |
| BOLUM6                                                                        | Hata parametrik alan                                     |
| ORAN6                                                                         | Hata parametrik alan                                     |
| ORAN5                                                                         | Hata parametrik alan                                     |
| ORAN4                                                                         | Hata parametrik alan                                     |
| ORAN3                                                                         | Hata parametrik alan                                     |
| ORAN2                                                                         | Hata parametrik alan                                     |
| ORAN1                                                                         | Hata parametrik alan                                     |
| ONAY                                                                          | Onay                                                     |
| REDNEDENI                                                                     | Red nedeni                                               |
| ISYERI_KODU                                                                   | İş yeri kodu                                             |
| SISTEM_KODU                                                                   | Sistem kodu                                              |
| GELISMERP_ETKINLIK                                                            | Gelişme raporuna ait etkinlik                            |
| HATA_PER1                                                                     | Hata parametrik alan                                     |
| HATA_PER2                                                                     | Hata parametrik alan                                     |
| HATA_PER3                                                                     | Hata parametrik alan                                     |
| HATA_PER4                                                                     | Hata parametrik alan                                     |
| HATA_PER5                                                                     | Hata parametrik alan                                     |
| HATA_PER6                                                                     | Hata parametrik alan                                     |
| HATA_PER_ORAN1                                                                | Hata parametrik alan                                     |
| HATA_PER_ORAN2                                                                | Hata parametrik alan                                     |
| HATA_PER_ORAN3                                                                | Hata parametrik alan                                     |
| HATA_PER_ORAN4                                                                | Hata parametrik alan                                     |
| HATA_PER_ORAN5                                                                | Hata parametrik alan                                     |
| HATA_PER_ORAN6                                                                | Hata parametrik alan                                     |
| REDDEDEN                                                                      | Reddeden sicil                                           |
| PARAM2                                                                        | Parametrik alan                                          |
| PARAM3                                                                        | Parametrik alan                                          |
| PARAM4                                                                        | Parametrik alan                                          |
| PARAM5                                                                        | Parametrik alan                                          |
| SUREC_KODU                                                                    | Süreç kodu                                               |
| MALIYET                                                                       | Maliyet                                                  |
| PARAM6                                                                        | Parametrik alan                                          |
| PARAM7                                                                        | Parametrik alan                                          |
| PARAM9                                                                        | Parametrik alan                                          |
| NPARAM2                                                                       | Parametrik alan                                          |
| NPARAM4                                                                       | Parametrik alan                                          |
| NPARAM5                                                                       | Parametrik alan                                          |
| NPARAM6                                                                       | Parametrik alan                                          |
| NPARAM7                                                                       | Parametrik alan                                          |
| NPARAM8                                                                       | Parametrik alan                                          |
| NPARAM9                                                                       | Parametrik alan                                          |
| NPARAM10                                                                      | Parametrik alan                                          |
| NPARAM2_BIRIM                                                                 | Parametrik alan                                          |
| NPARAM4_BIRIM                                                                 | Parametrik alan                                          |
| NPARAM5_BIRIM                                                                 | Parametrik alan                                          |
| NPARAM6_BIRIM                                                                 | Parametrik alan                                          |
| NPARAM7_BIRIM                                                                 | Parametrik alan                                          |
| NPARAM8_BIRIM                                                                 | Parametrik alan                                          |
| NPARAM9_BIRIM                                                                 | Parametrik alan                                          |
| NPARAM10_BIRIM                                                                | Parametrik alan                                          |
| DPARAM2                                                                       | Parametrik alan                                          |
| DPARAM3                                                                       | Parametrik alan                                          |
| DPARAM4                                                                       | Parametrik alan                                          |
| DPARAM5                                                                       | Parametrik alan                                          |
| PPARAM2                                                                       | Parametrik alan                                          |
| PPARAM3                                                                       | Parametrik alan                                          |
| PPARAM4                                                                       | Parametrik alan                                          |
| PPARAM5                                                                       | Parametrik alan                                          |
| LPARAM4                                                                       | Parametrik alan                                          |
| LPARAM5                                                                       | Parametrik alan                                          |
| GELISME_PARAM1                                                                | Gelişme parametrik alan                                  |
| GELISME_PARAM2                                                                | Gelişme parametrik alan                                  |
| GELISME_PARAM3                                                                | Gelişme parametrik alan                                  |
| GELISME_LPARAM1                                                               | Gelişme parametrik alan                                  |
| GELISME_LPARAM2                                                               | Gelişme parametrik alan                                  |
| GELISME_LPARAM3                                                               | Gelişme parametrik alan                                  |
| GELISME_NPARAM1                                                               | Gelişme parametrik alan                                  |
| GELISME_NPARAM2                                                               | Gelişme parametrik alan                                  |
| GELISME_NPARAM3                                                               | Gelişme parametrik alan                                  |
| GELISME_NPARAM4                                                               | Gelişme parametrik alan                                  |
| GELISME_NPARAM5                                                               | Gelişme parametrik alan                                  |
| GELISME_NPARAM1_BIRIM                                                         | Gelişme parametrik alan                                  |
| GELISME_NPARAM2_BIRIM                                                         | Gelişme parametrik alan                                  |
| GELISME_NPARAM3_BIRIM                                                         | Gelişme parametrik alan                                  |
| GELISME_NPARAM4_BIRIM                                                         | Gelişme parametrik alan                                  |
| GELISME_NPARAM5_BIRIM                                                         | Gelişme parametrik alan                                  |
| ONAY_DURUM                                                                    | Onay durum                                               |
| SONUCRP                                                                       | Sonuç raporu                                             |
| SONUCRPYT                                                                     | Sonuç raporu yazma tarihi                                |
| SONUCRPKYTUSR                                                                 | Sonuç raporunu yazanın sicil numarası                    |
| AKSIYON_DURUM                                                                 | Aksiyon durumu                                           |
| AKSIYON_SONUC_TARIHI                                                          | Aksiyon sonuç tarihi                                     |
| DOF_SONUC_TARIHI                                                              | DOF sonuç tarihi                                         |
| DUZELTICIONLEYICI                                                             | Düzeltici mi önleyici mi durumu                          |
| REF_MODULE                                                                    | Referans modül                                           |
| REF_MODULE_CODE                                                               | Referans modül kodu                                      |
| PARAM11                                                                       | Parametrik alan                                          |
| PARAM12                                                                       | Parametrik alan                                          |
| PARAM13                                                                       | Parametrik alan                                          |
| PARAM14                                                                       | Parametrik alan                                          |
| PARAM15                                                                       | Parametrik alan                                          |
| LPARAM6                                                                       | Parametrik alan                                          |
| LPARAM7                                                                       | Parametrik alan                                          |
| LPARAM8                                                                       | Parametrik alan                                          |
| LPARAM9                                                                       | Parametrik alan                                          |
| ETKINLIK                                                                      | Etkinlik                                                 |
| ETKINLIK_PUANI                                                                | Etkinlik puanı                                           |
| ESKI_DURUM                                                                    | Eski durum                                               |
| ESKI_ONAY_DURUM                                                               | Eski onay durumu                                         |
| SONUC_PARAM1                                                                  | Sonuç parametrik alan                                    |
| SONUC_PARAM2                                                                  | Sonuç parametrik alan                                    |
| SONUC_PARAM3                                                                  | Sonuç parametrik alan                                    |
| SONUC_PARAM4                                                                  | Sonuç parametrik alan                                    |
| SONUC_PARAM5                                                                  | Sonuç parametrik alan                                    |
| SONUC_PARAM6                                                                  | Sonuç parametrik alan                                    |
| SONUC_PARAM7                                                                  | Sonuç parametrik alan                                    |
| SONUC_PARAM8                                                                  | Sonuç parametrik alan                                    |
| SONUC_PARAM9                                                                  | Sonuç parametrik alan                                    |
| SONUC_PARAM10                                                                 | Sonuç parametrik alan                                    |
| SONUC_LPARAM1                                                                 | Sonuç parametrik alan                                    |
| SONUC_LPARAM2                                                                 | Sonuç parametrik alan                                    |
| SONUC_LPARAM3                                                                 | Sonuç parametrik alan                                    |
| SONUC_LPARAM4                                                                 | Sonuç parametrik alan                                    |
| SONUC_LPARAM5                                                                 | Sonuç parametrik alan                                    |
| SONUC_LPARAM6                                                                 | Sonuç parametrik alan                                    |
| SONUC_LPARAM7                                                                 | Sonuç parametrik alan                                    |
| SONUC_LPARAM8                                                                 | Sonuç parametrik alan                                    |
| SONUC_LPARAM9                                                                 | Sonuç parametrik alan                                    |
| SONUC_LPARAM10                                                                | Sonuç parametrik alan                                    |
| SONUC_NPARAM1                                                                 | Sonuç parametrik alan                                    |
| SONUC_NPARAM2                                                                 | Sonuç parametrik alan                                    |
| SONUC_NPARAM3                                                                 | Sonuç parametrik alan                                    |
| SONUC_NPARAM4                                                                 | Sonuç parametrik alan                                    |
| SONUC_NPARAM5                                                                 | Sonuç parametrik alan                                    |
| SONUC_NPARAM1_BIRIM                                                           | Sonuç parametrik alan                                    |
| SONUC_NPARAM2_BIRIM                                                           | Sonuç parametrik alan                                    |
| SONUC_NPARAM3_BIRIM                                                           | Sonuç parametrik alan                                    |
| SONUC_NPARAM4_BIRIM                                                           | Sonuç parametrik alan                                    |
| SONUC_NPARAM5_BIRIM                                                           | Sonuç parametrik alan                                    |
| SONUC_LMPARAM1                                                                | Sonuç parametrik alan                                    |
| SONUC_LMPARAM2                                                                | Sonuç parametrik alan                                    |
| SONUC_LMPARAM3                                                                | Sonuç parametrik alan                                    |
| SONUC_LMPARAM4                                                                | Sonuç parametrik alan                                    |
| SONUC_LMPARAM5                                                                | Sonuç parametrik alan                                    |
| SONUC_LMPARAM6                                                                | Sonuç parametrik alan                                    |
| SONUC_LMPARAM7                                                                | Sonuç parametrik alan                                    |
| SONUC_LMPARAM8                                                                | Sonuç parametrik alan                                    |
| SONUC_LMPARAM9                                                                | Sonuç parametrik alan                                    |
| SONUC_LMPARAM10                                                               | Sonuç parametrik alan                                    |
| KAPATMA_PARAM1                                                                | Kapatma parametrik alan                                  |
| KAPATMA_PARAM2                                                                | Kapatma parametrik alan                                  |
| KAPATMA_PARAM3                                                                | Kapatma parametrik alan                                  |
| KAPATMA_PARAM4                                                                | Kapatma parametrik alan                                  |
| KAPATMA_PARAM5                                                                | Kapatma parametrik alan                                  |
| KAPATMA_PARAM6                                                                | Kapatma parametrik alan                                  |
| KAPATMA_PARAM7                                                                | Kapatma parametrik alan                                  |
| KAPATMA_PARAM8                                                                | Kapatma parametrik alan                                  |
| KAPATMA_PARAM9                                                                | Kapatma parametrik alan                                  |
| KAPATMA_PARAM10                                                               | Kapatma parametrik alan                                  |
| KAPATMA_LPARAM1                                                               | Kapatma parametrik alan                                  |
| KAPATMA_LPARAM2                                                               | Kapatma parametrik alan                                  |
| KAPATMA_LPARAM3                                                               | Kapatma parametrik alan                                  |
| KAPATMA_LPARAM4                                                               | Kapatma parametrik alan                                  |
| KAPATMA_LPARAM5                                                               | Kapatma parametrik alan                                  |
| KAPATMA_LPARAM6                                                               | Kapatma parametrik alan                                  |
| KAPATMA_LPARAM7                                                               | Kapatma parametrik alan                                  |
| KAPATMA_LPARAM8                                                               | Kapatma parametrik alan                                  |
| KAPATMA_LPARAM9                                                               | Kapatma parametrik alan                                  |
| KAPATMA_LPARAM10                                                              | Kapatma parametrik alan                                  |
| KAPATMA_NPARAM1                                                               | Kapatma parametrik alan                                  |
| KAPATMA_NPARAM2                                                               | Kapatma parametrik alan                                  |
| KAPATMA_NPARAM3                                                               | Kapatma parametrik alan                                  |
| KAPATMA_NPARAM4                                                               | Kapatma parametrik alan                                  |
| KAPATMA_NPARAM5                                                               | Kapatma parametrik alan                                  |
| KAPATMA_NPARAM1_BIRIM                                                         | Kapatma parametrik alan                                  |
| KAPATMA_NPARAM2_BIRIM                                                         | Kapatma parametrik alan                                  |
| KAPATMA_NPARAM3_BIRIM                                                         | Kapatma parametrik alan                                  |
| KAPATMA_NPARAM4_BIRIM                                                         | Kapatma parametrik alan                                  |
| KAPATMA_NPARAM5_BIRIM                                                         | Kapatma parametrik alan                                  |
| ONAY_TARIHI                                                                   | Onay tarihi                                              |
| TERMIN_TARIHI                                                                 | Termin tarihi                                            |
| ILK_TERMIN_TARIHI                                                             | İlk termin tarihi                                        |
| OTOMATIK_AKSIYON                                                              | Otomatik aksiyon                                         |
| DPARAM1                                                                       | Parametrik alan                                          |
| LPARAM1                                                                       | Parametrik alan                                          |
| LPARAM10                                                                      | Parametrik alan                                          |
| LPARAM2                                                                       | Parametrik alan                                          |
| LPARAM3                                                                       | Parametrik alan                                          |
| NPARAM1                                                                       | Parametrik alan                                          |
| NPARAM1_BIRIM                                                                 | Parametrik alan                                          |
| NPARAM3                                                                       | Parametrik alan                                          |
| NPARAM3_BIRIM                                                                 | Parametrik alan                                          |
| PARAM1                                                                        | Parametrik alan                                          |
| PARAM10                                                                       | Parametrik alan                                          |
| PARAM8                                                                        | Parametrik alan                                          |
| PPARAM1                                                                       | Parametrik alan                                          |
| QPARAM1                                                                       | Parametrik alan                                          |
| QPARAM2                                                                       | Parametrik alan                                          |
| NPARAM42                                                                      | Parametrik alan                                          |
| NPARAM43                                                                      | Parametrik alan                                          |
| NPARAM44                                                                      | Parametrik alan                                          |
| NPARAM45                                                                      | Parametrik alan                                          |
| NPARAM46                                                                      | Parametrik alan                                          |
| NPARAM47                                                                      | Parametrik alan                                          |
| NPARAM48                                                                      | Parametrik alan                                          |
| NPARAM49                                                                      | Parametrik alan                                          |
| NPARAM50                                                                      | Parametrik alan                                          |
| NPARAM41_BIRIM                                                                | Parametrik alan                                          |
| NPARAM42_BIRIM                                                                | Parametrik alan                                          |
| NPARAM43_BIRIM                                                                | Parametrik alan                                          |
| NPARAM44_BIRIM                                                                | Parametrik alan                                          |
| NPARAM45_BIRIM                                                                | Parametrik alan                                          |
| NPARAM46_BIRIM                                                                | Parametrik alan                                          |
| NPARAM47_BIRIM                                                                | Parametrik alan                                          |
| NPARAM48_BIRIM                                                                | Parametrik alan                                          |
| NPARAM49_BIRIM                                                                | Parametrik alan                                          |
| NPARAM50_BIRIM                                                                | Parametrik alan                                          |
| DOCPARAM1                                                                     | Parametrik alan                                          |
| RET_TIPI                                                                      | Ret tipi                                                 |
| HATA1_BIRIM                                                                   | Hata parametrik alan                                     |
| HATA2_BIRIM                                                                   | Hata parametrik alan                                     |
| HATA3_BIRIM                                                                   | Hata parametrik alan                                     |
| HATA4_BIRIM                                                                   | Hata parametrik alan                                     |
| HATA5_BIRIM                                                                   | Hata parametrik alan                                     |
| HATA6_BIRIM                                                                   | Hata parametrik alan                                     |
| REF_DKOD                                                                      | Referans DOF kodu                                        |
| GELISME_PARAM4                                                                | Gelişme parametrik alan                                  |
| GELISME_PARAM5                                                                | Gelişme parametrik alan                                  |
| GELISME_PARAM6                                                                | Gelişme parametrik alan                                  |
| GELISME_PARAM7                                                                | Gelişme parametrik alan                                  |
| GELISME_PARAM8                                                                | Gelişme parametrik alan                                  |
| GELISME_PARAM9                                                                | Gelişme parametrik alan                                  |
| GELISME_PARAM10                                                               | Gelişme parametrik alan                                  |
| GELISME_PARAM11                                                               | Gelişme parametrik alan                                  |
| GELISME_PARAM12                                                               | Gelişme parametrik alan                                  |
| GELISME_LPARAM4                                                               | Gelişme parametrik alan                                  |
| GELISME_LPARAM5                                                               | Gelişme parametrik alan                                  |
| GELISME_LPARAM6                                                               | Gelişme parametrik alan                                  |
| GELISME_LPARAM7                                                               | Gelişme parametrik alan                                  |
| GELISME_LPARAM8                                                               | Gelişme parametrik alan                                  |
| GELISME_LPARAM9                                                               | Gelişme parametrik alan                                  |
| GELISME_LPARAM10                                                              | Gelişme parametrik alan                                  |
| GELISME_QPARAM1                                                               | Gelişme parametrik alan                                  |
| GELISME_QPARAM2                                                               | Gelişme parametrik alan                                  |
| GELISME_QPARAM3                                                               | Gelişme parametrik alan                                  |
| GELISME_QPARAM4                                                               | Gelişme parametrik alan                                  |
| GELISME_QPARAM5                                                               | Gelişme parametrik alan                                  |
| SONUC_QPARAM1                                                                 | Sonuç parametrik alan                                    |
| SONUC_QPARAM2                                                                 | Sonuç parametrik alan                                    |
| SONUC_QPARAM3                                                                 | Sonuç parametrik alan                                    |
| SONUC_QPARAM4                                                                 | Sonuç parametrik alan                                    |
| SONUC_QPARAM5                                                                 | Sonuç parametrik alan                                    |
| KAPATMA_QPARAM1                                                               | Kapatma parametrik alan                                  |
| KAPATMA_QPARAM2                                                               | Kapatma parametrik alan                                  |
| KAPATMA_QPARAM3                                                               | Kapatma parametrik alan                                  |
| KAPATMA_QPARAM4                                                               | Kapatma parametrik alan                                  |
| KAPATMA_QPARAM5                                                               | Kapatma parametrik alan                                  |
| GELISME_PPARAM1                                                               | Gelişme parametrik alan                                  |
| GELISME_PPARAM2                                                               | Gelişme parametrik alan                                  |
| GELISME_PPARAM3                                                               | Gelişme parametrik alan                                  |
| GELISME_PPARAM4                                                               | Gelişme parametrik alan                                  |
| GELISME_PPARAM5                                                               | Gelişme parametrik alan                                  |
| GELISME_PPARAM6                                                               | Gelişme parametrik alan                                  |
| GELISME_PPARAM7                                                               | Gelişme parametrik alan                                  |
| GELISME_PPARAM8                                                               | Gelişme parametrik alan                                  |
| GELISME_PPARAM9                                                               | Gelişme parametrik alan                                  |
| GELISME_PPARAM10                                                              | Gelişme parametrik alan                                  |
| SONUC_PPARAM1                                                                 | Sonuç parametrik alan                                    |
| SONUC_PPARAM2                                                                 | Sonuç parametrik alan                                    |
| SONUC_PPARAM3                                                                 | Sonuç parametrik alan                                    |
| SONUC_PPARAM4                                                                 | Sonuç parametrik alan                                    |
| SONUC_PPARAM5                                                                 | Sonuç parametrik alan                                    |
| SONUC_PPARAM6                                                                 | Sonuç parametrik alan                                    |
| SONUC_PPARAM7                                                                 | Sonuç parametrik alan                                    |
| SONUC_PPARAM8                                                                 | Sonuç parametrik alan                                    |
| SONUC_PPARAM9                                                                 | Sonuç parametrik alan                                    |
| SONUC_PPARAM10                                                                | Sonuç parametrik alan                                    |
| KAPATMA_PPARAM1                                                               | Kapatma parametrik alan                                  |
| KAPATMA_PPARAM2                                                               | Kapatma parametrik alan                                  |
| KAPATMA_PPARAM3                                                               | Kapatma parametrik alan                                  |
| KAPATMA_PPARAM4                                                               | Kapatma parametrik alan                                  |
| KAPATMA_PPARAM5                                                               | Kapatma parametrik alan                                  |
| KAPATMA_PPARAM6                                                               | Kapatma parametrik alan                                  |
| KAPATMA_PPARAM7                                                               | Kapatma parametrik alan                                  |
| KAPATMA_PPARAM8                                                               | Kapatma parametrik alan                                  |
| KAPATMA_PPARAM9                                                               | Kapatma parametrik alan                                  |
| KAPATMA_PPARAM10                                                              | Kapatma parametrik alan                                  |
| T2_ACIKLAMA                                                                   | Kaynak açıklaması                                        |
| T2_ICDIS                                                                      | İç veya dış müşteri şikayeti durumu                      |
| T3_ADISOYADI                                                                  | Bildiren adı soyadı                                      |
| T4_ADISOYADI                                                                  | Şikayet oluşturan kişinin adı soyadı                     |
| T5_ADISOYADI                                                                  | Lider adı soyadı                                         |
| T6_DEPARTMAN_ADI                                                              | Sorumlu departman adı                                    |
| T7_URUN_ADI                                                                   | Ürün adı                                                 |
| T8_ADISOYADI                                                                  | Gelişme raporu yazan adı soyadı                          |
| T9_ADISOYADI                                                                  | Kapatan adı soyadı                                       |
| T10_ISYERI_ADI                                                                | İş yeri adı                                              |
| T11_ACIKLAMA                                                                  | Sistem açıklaması                                        |
| T12_ADISOYADI                                                                 | Sonuç raporunu yazanın adı soyadı                        |
| T13_VALUE                                                                     | Düzeltici mi önleyici mi durumunun açıklaması            |
| KAPATMAONAY_0                                                                 | Kapatma onaycıları ve tarihler(10' a kadar gidiyor)      |
| ACMAONAY_0                                                                    | Açma onaycıları ve tarihler(10' a kadar gidiyor)         |
| GELISMEONAY_0                                                                 | Gelişme onaycıları ve tarihler(10' a kadar gidiyor)      |
| KAPATMAONAYTAR_0                                                              | Kapatma onaycıları ve tarihler(10' a kadar gidiyor)      |
| ACMAONAYTAR_0                                                                 | Açma onaycıları ve tarihler(10' a kadar gidiyor)         |
| GELISMEONAYTAR_0                                                              | Gelişme onaycıları ve tarihler(10' a kadar gidiyor)      |
| ACMASURE_0                                                                    | Açma onay süresi(10' a kadar gidiyor)                    |
| KAPATMASURE_0                                                                 | Kapatma onay süresi(10' a kadar gidiyor)                 |
| GELISMESURE_0                                                                 | Gelişme onay süresi(10' a kadar gidiyor)                 |
| TOPLAM_ACMASURE                                                               | Toplam açma onay süresi                                  |
| TOPLAM_KAPATMASURE                                                            | Toplam Kapatma onay süresi                               |
| SUREC_ADI                                                                     | Süreç adı                                                |
| SUREC                                                                         | Süreç kodu - süreç adı                                   |
| KOK_NEDENLER                                                                  | Kök nedenler                                             |
| KOKNEDEN_DETAYI                                                               | Kök neden detayı                                         |
| BILGILENDIRME                                                                 | Bilgilendirme                                            |
| MTB                                                                           | Müşteri adı veya departman adı                           |
| DURUM_ACK                                                                     | Durum açıklaması                                         |
| UYG_KAT                                                                       | Uygunluk kategorisi                                      |
| DOCPARAM1_VALUE                                                               | Parametrik alan                                          |
| GELISME_LPARAM1_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_LPARAM10_VALUE                                                        | Gelişme parametrik alan                                  |
| GELISME_LPARAM2_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_LPARAM3_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_LPARAM4_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_LPARAM5_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_LPARAM6_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_LPARAM7_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_LPARAM8_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_LPARAM9_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_NPARAM1_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_NPARAM2_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_NPARAM3_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_NPARAM4_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_NPARAM5_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_PPARAM1_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_PPARAM10_VALUE                                                        | Gelişme parametrik alan                                  |
| GELISME_PPARAM2_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_PPARAM3_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_PPARAM4_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_PPARAM5_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_PPARAM6_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_PPARAM7_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_PPARAM8_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_PPARAM9_VALUE                                                         | Gelişme parametrik alan                                  |
| KAPATMA_LPARAM1_VALUE                                                         | Kapatma parametrik alan                                  |
| LPARAM1_VALUE                                                                 | Parametrik alan                                          |
| LPARAM10_VALUE                                                                | Parametrik alan                                          |
| LPARAM2_VALUE                                                                 | Parametrik alan                                          |
| LPARAM3_VALUE                                                                 | Parametrik alan                                          |
| NPARAM1_VALUE                                                                 | Parametrik alan                                          |
| NPARAM3_VALUE                                                                 | Parametrik alan                                          |
| PPARAM1_VALUE                                                                 | Parametrik alan                                          |
| SONUC_LPARAM1_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_LPARAM10_VALUE                                                          | Sonuç parametrik alan                                    |
| SONUC_LPARAM2_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_LPARAM3_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_LPARAM4_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_LPARAM5_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_LPARAM6_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_LPARAM7_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_LPARAM8_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_LPARAM9_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_NPARAM1_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_NPARAM2_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_NPARAM3_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_NPARAM4_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_NPARAM5_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_PPARAM1_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_PPARAM10_VALUE                                                          | Sonuç parametrik alan                                    |
| SONUC_PPARAM2_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_PPARAM3_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_PPARAM4_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_PPARAM5_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_PPARAM6_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_PPARAM7_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_PPARAM8_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_PPARAM9_VALUE                                                           | Sonuç parametrik alan                                    |
| DEGISTIRMET                                                                   | Değiştirme tarihi                                        |
| SON_DEGISTIREN                                                                | Son değişiklik yapan sicil                               |
| GECIKMENEDENI                                                                 | Gecikme nedeni                                           |
| KAYITTARIHI                                                                   | Kayıt tarihi                                             |
| T5_KAPATMAT                                                                   | Kapatma tarihi                                           |
| SISTEMEGIREN                                                                  | Sisteme giren adı soyadı                                 |
| YAPT                                                                          | Yapılma tarihi                                           |
| YAPILAN                                                                       | Yapılanların açıklaması                                  |
| REVPLANT                                                                      | Revizyon plan tarihi                                     |
| PLANT                                                                         | Plan tarihi                                              |
| YAPACAK                                                                       | Yapacak sicil no                                         |
| SORUMLU                                                                       | Sorumlu sicil no                                         |
| AKSIYON                                                                       | Aksiyon bilgisi                                          |
| NO                                                                            | Aksiyon no                                               |
| DKOD_NO                                                                       | DOF kod no                                               |

## **1.4. DÖF Tekli Raporu Replacement (Kısa Kodlar) Tag Tablosu**

Düzeltici ve Önleyici Modülünde kullanılan DÖF Tekli Rapor taglerin listesi aşağıdaki tabloda yer almaktadır.

| **Kısaltma (Kısalmalar tag şeklinde < \> isaretleri arasına yazılacaktır.)** | **Açıklama**                                             |
|-------------------------------------------------------------------------------|----------------------------------------------------------|
| DKOD                                                                          | DOF kodu                                                 |
| KAYNAK                                                                        | DOF kaynağı                                              |
| SISTEMEKT                                                                     | Sisteme ekleme tarihi                                    |
| MREF                                                                          | Denetimden açılan Müşteri şikayetleri için referans kodu |
| BILDIREN                                                                      | Bildiren kişi                                            |
| BILDIRIMT                                                                     | Bildirim Tarihi                                          |
| BILDIRIMS                                                                     | Bildirim şekli                                           |
| SIKAYETG                                                                      | Şikayet oluşturan sicil no                               |
| LIDER                                                                         | Lider sicil numarası                                     |
| SORUMLUD                                                                      | Sorumlu departman kodu                                   |
| UYGT                                                                          | DOF Uygunsuzluk tanımı                                   |
| UYGDT                                                                         | DOF Uygunsuzluk detayı                                   |
| URUN                                                                          | Ürün kodu                                                |
| GELRAPY                                                                       | Planlanan gelisme raporu tarihi                          |
| DURUM                                                                         | Durum bilgisi                                            |
| GELISMEYT                                                                     | Gelişme raporu yazma tarihi                              |
| GELISMERP                                                                     | Gelişme raporu                                           |
| SONRAPY                                                                       | Planlanan sonuç raporu tarihi                            |
| GELKYTUSR                                                                     | Gelişme raporu yazan sicili                              |
| NOTLAR                                                                        | Notlar                                                   |
| KAPATAN                                                                       | Kapatan kişinin sicil numarası                           |
| KAPATMAT                                                                      | Kapatma tarihi                                           |
| MKOD                                                                          | Müşteri kodu                                             |
| YETERLILIK                                                                    | Yeterlilik                                               |
| HATA6M                                                                        | Hata parametrik alan                                     |
| HATA5M                                                                        | Hata parametrik alan                                     |
| HATA4M                                                                        | Hata parametrik alan                                     |
| HATA3M                                                                        | Hata parametrik alan                                     |
| HATA2M                                                                        | Hata parametrik alan                                     |
| HATA1M                                                                        | Hata parametrik alan                                     |
| HATA6T                                                                        | Hata parametrik alan                                     |
| HATA5T                                                                        | Hata parametrik alan                                     |
| HATA4T                                                                        | Hata parametrik alan                                     |
| HATA3T                                                                        | Hata parametrik alan                                     |
| HATA2T                                                                        | Hata parametrik alan                                     |
| HATA1T                                                                        | Hata parametrik alan                                     |
| BOLUM1                                                                        | Hata parametrik alan                                     |
| BOLUM2                                                                        | Hata parametrik alan                                     |
| BOLUM3                                                                        | Hata parametrik alan                                     |
| BOLUM4                                                                        | Hata parametrik alan                                     |
| BOLUM5                                                                        | Hata parametrik alan                                     |
| BOLUM6                                                                        | Hata parametrik alan                                     |
| ORAN6                                                                         | Hata parametrik alan                                     |
| ORAN5                                                                         | Hata parametrik alan                                     |
| ORAN4                                                                         | Hata parametrik alan                                     |
| ORAN3                                                                         | Hata parametrik alan                                     |
| ORAN2                                                                         | Hata parametrik alan                                     |
| ORAN1                                                                         | Hata parametrik alan                                     |
| ONAY                                                                          | Onay                                                     |
| REDNEDENI                                                                     | Ret nedeni                                               |
| ISYERI_KODU                                                                   | iş yeri kodu                                             |
| SISTEM_KODU                                                                   | sistem kodu                                              |
| GELISMERP_ETKINLIK                                                            | Gelişme raporuna ait etkinlik                            |
| HATA_PER1                                                                     | Hata parametrik alan                                     |
| HATA_PER2                                                                     | Hata parametrik alan                                     |
| HATA_PER3                                                                     | Hata parametrik alan                                     |
| HATA_PER4                                                                     | Hata parametrik alan                                     |
| HATA_PER5                                                                     | Hata parametrik alan                                     |
| HATA_PER6                                                                     | Hata parametrik alan                                     |
| HATA_PER_ORAN1                                                                | Hata parametrik alan                                     |
| HATA_PER_ORAN2                                                                | Hata parametrik alan                                     |
| HATA_PER_ORAN3                                                                | Hata parametrik alan                                     |
| HATA_PER_ORAN4                                                                | Hata parametrik alan                                     |
| HATA_PER_ORAN5                                                                | Hata parametrik alan                                     |
| HATA_PER_ORAN6                                                                | Hata parametrik alan                                     |
| REDDEDEN                                                                      | Reddeden sicil                                           |
| PARAM1                                                                        | Parametrik alan                                          |
| PARAM2                                                                        | Parametrik alan                                          |
| PARAM3                                                                        | Parametrik alan                                          |
| PARAM4                                                                        | Parametrik alan                                          |
| PARAM5                                                                        | Parametrik alan                                          |
| SUREC_KODU                                                                    | Süreç kodu                                               |
| MALIYET                                                                       | Maliyet                                                  |
| PARAM6                                                                        | Parametrik alan                                          |
| PARAM7                                                                        | Parametrik alan                                          |
| PARAM8                                                                        | Parametrik alan                                          |
| PARAM9                                                                        | Süreç kodu                                               |
| PARAM10                                                                       | Maliyet                                                  |
| NPARAM1                                                                       | Parametrik alan                                          |
| NPARAM2                                                                       | Parametrik alan                                          |
| NPARAM3                                                                       | Parametrik alan                                          |
| NPARAM4                                                                       | Süreç kodu                                               |
| NPARAM5                                                                       | Maliyet                                                  |
| NPARAM6                                                                       | Parametrik alan                                          |
| NPARAM7                                                                       | Parametrik alan                                          |
| NPARAM8                                                                       | Parametrik alan                                          |
| NPARAM9                                                                       | Süreç kodu                                               |
| NPARAM10                                                                      | Maliyet                                                  |
| NPARAM1_BIRIM                                                                 | Parametrik alan                                          |
| NPARAM2_BIRIM                                                                 | Parametrik alan                                          |
| NPARAM3_BIRIM                                                                 | Parametrik alan                                          |
| NPARAM4_BIRIM                                                                 | Süreç kodu                                               |
| NPARAM5_BIRIM                                                                 | Maliyet                                                  |
| NPARAM6_BIRIM                                                                 | Parametrik alan                                          |
| NPARAM7_BIRIM                                                                 | Parametrik alan                                          |
| NPARAM8_BIRIM                                                                 | Parametrik alan                                          |
| NPARAM9_BIRIM                                                                 | Süreç kodu                                               |
| NPARAM10_BIRIM                                                                | Maliyet                                                  |
| DPARAM1                                                                       | Parametrik alan                                          |
| DPARAM2                                                                       | Parametrik alan                                          |
| DPARAM3                                                                       | Parametrik alan                                          |
| DPARAM4                                                                       | Süreç kodu                                               |
| DPARAM5                                                                       | Maliyet                                                  |
| PPARAM1                                                                       | Parametrik alan                                          |
| PPARAM2                                                                       | Parametrik alan                                          |
| PPARAM3                                                                       | Parametrik alan                                          |
| PPARAM4                                                                       | Süreç kodu                                               |
| PPARAM5                                                                       | Maliyet                                                  |
| LPARAM1                                                                       | Parametrik alan                                          |
| LPARAM2                                                                       | Parametrik alan                                          |
| LPARAM3                                                                       | Parametrik alan                                          |
| LPARAM4                                                                       | Süreç kodu                                               |
| LPARAM5                                                                       | Maliyet                                                  |
| GELISME_PARAM1                                                                | Gelişme parametrik alan                                  |
| GELISME_PARAM2                                                                | Gelişme parametrik alan                                  |
| GELISME_PARAM3                                                                | Gelişme parametrik alan                                  |
| GELISME_LPARAM1                                                               | Gelişme parametrik alan                                  |
| GELISME_LPARAM2                                                               | Gelişme parametrik alan                                  |
| GELISME_LPARAM3                                                               | Gelişme parametrik alan                                  |
| GELISME_NPARAM1                                                               | Gelişme parametrik alan                                  |
| GELISME_NPARAM2                                                               | Gelişme parametrik alan                                  |
| GELISME_NPARAM3                                                               | Gelişme parametrik alan                                  |
| GELISME_NPARAM4                                                               | Gelişme parametrik alan                                  |
| GELISME_NPARAM5                                                               | Gelişme parametrik alan                                  |
| GELISME_NPARAM1_BIRIM                                                         | Gelişme parametrik alan                                  |
| GELISME_NPARAM2_BIRIM                                                         | Gelişme parametrik alan                                  |
| GELISME_NPARAM3_BIRIM                                                         | Gelişme parametrik alan                                  |
| GELISME_NPARAM4_BIRIM                                                         | Gelişme parametrik alan                                  |
| GELISME_NPARAM5_BIRIM                                                         | Gelişme parametrik alan                                  |
| ONAY_DURUM                                                                    | Onay durumu                                              |
| SONUCRP                                                                       | Sonuç raporu                                             |
| SONUCRPYT                                                                     | Sonuç raporu yazma tarihi                                |
| SONUCRPKYTUSR                                                                 | Sonuç raporunu yazanın sicil numarası                    |
| AKSIYON_DURUM                                                                 | Aksiyon durumu                                           |
| AKSIYON_SONUC_TARIHI                                                          | Aksiyon sonuç tarihi                                     |
| DOF_SONUC_TARIHI                                                              | DOF sonuç tarihi                                         |
| DUZELTICIONLEYICI                                                             | Düzeltici mi önleyici mi durumu                          |
| REF_MODULE                                                                    | Referans modül                                           |
| REF_MODULE_CODE                                                               | Referans modül kodu                                      |
| PARAM11                                                                       | Parametrik alan                                          |
| PARAM12                                                                       | Parametrik alan                                          |
| PARAM13                                                                       | Parametrik alan                                          |
| PARAM14                                                                       | Parametrik alan                                          |
| PARAM15                                                                       | Parametrik alan                                          |
| LPARAM6                                                                       | Parametrik alan                                          |
| LPARAM7                                                                       | Parametrik alan                                          |
| LPARAM8                                                                       | Parametrik alan                                          |
| LPARAM9                                                                       | Parametrik alan                                          |
| LPARAM10                                                                      | Parametrik alan                                          |
| ETKINLIK                                                                      | Etkinlik                                                 |
| ETKINLIK_PUANI                                                                | Etkinlik puanı                                           |
| ESKI_DURUM                                                                    | Eski durum                                               |
| ESKI_ONAY_DURUM                                                               | Eski onay durumu                                         |
| SONUC_PARAM1                                                                  | Sonuç parametrik alan                                    |
| SONUC_PARAM2                                                                  | Sonuç parametrik alan                                    |
| SONUC_PARAM3                                                                  | Sonuç parametrik alan                                    |
| SONUC_PARAM4                                                                  | Sonuç parametrik alan                                    |
| SONUC_PARAM5                                                                  | Sonuç parametrik alan                                    |
| SONUC_PARAM6                                                                  | Sonuç parametrik alan                                    |
| SONUC_PARAM7                                                                  | Sonuç parametrik alan                                    |
| SONUC_PARAM8                                                                  | Sonuç parametrik alan                                    |
| SONUC_PARAM9                                                                  | Sonuç parametrik alan                                    |
| SONUC_PARAM10                                                                 | Sonuç parametrik alan                                    |
| SONUC_LPARAM1                                                                 | Sonuç parametrik alan                                    |
| SONUC_LPARAM2                                                                 | Sonuç parametrik alan                                    |
| SONUC_LPARAM3                                                                 | Sonuç parametrik alan                                    |
| SONUC_LPARAM4                                                                 | Sonuç parametrik alan                                    |
| SONUC_LPARAM5                                                                 | Sonuç parametrik alan                                    |
| SONUC_LPARAM6                                                                 | Sonuç parametrik alan                                    |
| SONUC_LPARAM7                                                                 | Sonuç parametrik alan                                    |
| SONUC_LPARAM8                                                                 | Sonuç parametrik alan                                    |
| SONUC_LPARAM9                                                                 | Sonuç parametrik alan                                    |
| SONUC_LPARAM10                                                                | Sonuç parametrik alan                                    |
| SONUC_NPARAM1                                                                 | Sonuç parametrik alan                                    |
| SONUC_NPARAM2                                                                 | Sonuç parametrik alan                                    |
| SONUC_NPARAM3                                                                 | Sonuç parametrik alan                                    |
| SONUC_NPARAM4                                                                 | Sonuç parametrik alan                                    |
| SONUC_NPARAM5                                                                 | Sonuç parametrik alan                                    |
| SONUC_NPARAM1_BIRIM                                                           | Sonuç parametrik alan                                    |
| SONUC_NPARAM2_BIRIM                                                           | Sonuç parametrik alan                                    |
| SONUC_NPARAM3_BIRIM                                                           | Sonuç parametrik alan                                    |
| SONUC_NPARAM4_BIRIM                                                           | Sonuç parametrik alan                                    |
| SONUC_NPARAM5_BIRIM                                                           | Sonuç parametrik alan                                    |
| SONUC_LMPARAM1                                                                | Sonuç parametrik alan                                    |
| SONUC_LMPARAM2                                                                | Sonuç parametrik alan                                    |
| SONUC_LMPARAM3                                                                | Sonuç parametrik alan                                    |
| SONUC_LMPARAM4                                                                | Sonuç parametrik alan                                    |
| SONUC_LMPARAM5                                                                | Sonuç parametrik alan                                    |
| SONUC_LMPARAM6                                                                | Sonuç parametrik alan                                    |
| SONUC_LMPARAM7                                                                | Sonuç parametrik alan                                    |
| SONUC_LMPARAM8                                                                | Sonuç parametrik alan                                    |
| SONUC_LMPARAM9                                                                | Sonuç parametrik alan                                    |
| SONUC_LMPARAM10                                                               | Sonuç parametrik alan                                    |
| KAPATMA_PARAM1                                                                | Kapatma parametrik alan                                  |
| KAPATMA_PARAM2                                                                | Kapatma parametrik alan                                  |
| KAPATMA_PARAM3                                                                | Kapatma parametrik alan                                  |
| KAPATMA_PARAM4                                                                | Kapatma parametrik alan                                  |
| KAPATMA_PARAM5                                                                | Kapatma parametrik alan                                  |
| KAPATMA_PARAM6                                                                | Kapatma parametrik alan                                  |
| KAPATMA_PARAM7                                                                | Kapatma parametrik alan                                  |
| KAPATMA_PARAM8                                                                | Kapatma parametrik alan                                  |
| KAPATMA_PARAM9                                                                | Kapatma parametrik alan                                  |
| KAPATMA_PARAM10                                                               | Kapatma parametrik alan                                  |
| KAPATMA_LPARAM1                                                               | Kapatma parametrik alan                                  |
| KAPATMA_LPARAM2                                                               | Kapatma parametrik alan                                  |
| KAPATMA_LPARAM3                                                               | Kapatma parametrik alan                                  |
| KAPATMA_LPARAM4                                                               | Kapatma parametrik alan                                  |
| KAPATMA_LPARAM5                                                               | Kapatma parametrik alan                                  |
| KAPATMA_LPARAM6                                                               | Kapatma parametrik alan                                  |
| KAPATMA_LPARAM7                                                               | Kapatma parametrik alan                                  |
| KAPATMA_LPARAM8                                                               | Kapatma parametrik alan                                  |
| KAPATMA_LPARAM9                                                               | Kapatma parametrik alan                                  |
| KAPATMA_LPARAM10                                                              | Kapatma parametrik alan                                  |
| KAPATMA_NPARAM1                                                               | Kapatma parametrik alan                                  |
| KAPATMA_NPARAM2                                                               | Kapatma parametrik alan                                  |
| KAPATMA_NPARAM3                                                               | Kapatma parametrik alan                                  |
| KAPATMA_NPARAM4                                                               | Kapatma parametrik alan                                  |
| KAPATMA_NPARAM5                                                               | Kapatma parametrik alan                                  |
| KAPATMA_NPARAM1_BIRIM                                                         | Kapatma parametrik alan                                  |
| KAPATMA_NPARAM2_BIRIM                                                         | Kapatma parametrik alan                                  |
| KAPATMA_NPARAM3_BIRIM                                                         | Kapatma parametrik alan                                  |
| KAPATMA_NPARAM4_BIRIM                                                         | Kapatma parametrik alan                                  |
| KAPATMA_NPARAM5_BIRIM                                                         | Kapatma parametrik alan                                  |
| ONAY_TARIHI                                                                   | Onay tarihi                                              |
| TERMIN_TARIHI                                                                 | Termin tarihi                                            |
| ILK_TERMIN_TARIHI                                                             | İlk termin tarihi                                        |
| OTOMATIK_AKSIYON                                                              | Otomatik aksiyon                                         |
| QPARAM1                                                                       | Sorgu tipli parametrik alan                              |
| QPARAM2                                                                       | Sorgu tipli parametrik alan                              |
| QPARAM3                                                                       | Sorgu tipli parametrik alan                              |
| QPARAM4                                                                       | Sorgu tipli parametrik alan                              |
| QPARAM5                                                                       | Sorgu tipli parametrik alan                              |
| MALIYET_BIRIM                                                                 | Maliyet birimi                                           |
| PARAM31                                                                       | Parametrik alan                                          |
| PARAM32                                                                       | Parametrik alan                                          |
| PARAM33                                                                       | Parametrik alan                                          |
| PARAM34                                                                       | Parametrik alan                                          |
| PARAM35                                                                       | Parametrik alan                                          |
| LPARAM36                                                                      | Parametrik alan                                          |
| LPARAM37                                                                      | Parametrik alan                                          |
| LPARAM38                                                                      | Parametrik alan                                          |
| LPARAM39                                                                      | Parametrik alan                                          |
| LPARAM40                                                                      | Parametrik alan                                          |
| NPARAM41                                                                      | Parametrik alan                                          |
| NPARAM42                                                                      | Parametrik alan                                          |
| NPARAM43                                                                      | Parametrik alan                                          |
| NPARAM44                                                                      | Parametrik alan                                          |
| NPARAM45                                                                      | Parametrik alan                                          |
| NPARAM46                                                                      | Parametrik alan                                          |
| NPARAM47                                                                      | Parametrik alan                                          |
| NPARAM48                                                                      | Parametrik alan                                          |
| NPARAM49                                                                      | Parametrik alan                                          |
| NPARAM50                                                                      | Parametrik alan                                          |
| NPARAM41_BIRIM                                                                | Parametrik alan                                          |
| NPARAM42_BIRIM                                                                | Parametrik alan                                          |
| NPARAM43_BIRIM                                                                | Parametrik alan                                          |
| NPARAM44_BIRIM                                                                | Parametrik alan                                          |
| NPARAM45_BIRIM                                                                | Parametrik alan                                          |
| NPARAM46_BIRIM                                                                | Parametrik alan                                          |
| NPARAM47_BIRIM                                                                | Parametrik alan                                          |
| NPARAM48_BIRIM                                                                | Parametrik alan                                          |
| NPARAM49_BIRIM                                                                | Parametrik alan                                          |
| NPARAM50_BIRIM                                                                | Parametrik alan                                          |
| DOCPARAM1                                                                     | Parametrik alan                                          |
| RET_TIPI                                                                      | Ret tipi                                                 |
| HATA1_BIRIM                                                                   | Hata parametrik alan                                     |
| HATA2_BIRIM                                                                   | Hata parametrik alan                                     |
| HATA3_BIRIM                                                                   | Hata parametrik alan                                     |
| HATA4_BIRIM                                                                   | Hata parametrik alan                                     |
| HATA5_BIRIM                                                                   | Hata parametrik alan                                     |
| HATA6_BIRIM                                                                   | Hata parametrik alan                                     |
| REF_DKOD                                                                      | Referans DOF kodu                                        |
| GELISME_PARAM4                                                                | Gelişme parametrik alan                                  |
| GELISME_PARAM5                                                                | Gelişme parametrik alan                                  |
| GELISME_PARAM6                                                                | Gelişme parametrik alan                                  |
| GELISME_PARAM7                                                                | Gelişme parametrik alan                                  |
| GELISME_PARAM8                                                                | Gelişme parametrik alan                                  |
| GELISME_PARAM9                                                                | Gelişme parametrik alan                                  |
| GELISME_PARAM10                                                               | Gelişme parametrik alan                                  |
| GELISME_PARAM11                                                               | Gelişme parametrik alan                                  |
| GELISME_PARAM12                                                               | Gelişme parametrik alan                                  |
| GELISME_LPARAM4                                                               | Gelişme parametrik alan                                  |
| GELISME_LPARAM5                                                               | Gelişme parametrik alan                                  |
| GELISME_LPARAM6                                                               | Gelişme parametrik alan                                  |
| GELISME_LPARAM7                                                               | Gelişme parametrik alan                                  |
| GELISME_LPARAM8                                                               | Gelişme parametrik alan                                  |
| GELISME_LPARAM9                                                               | Gelişme parametrik alan                                  |
| GELISME_LPARAM10                                                              | Gelişme parametrik alan                                  |
| GELISME_QPARAM1                                                               | Gelişme parametrik alan                                  |
| GELISME_QPARAM2                                                               | Gelişme parametrik alan                                  |
| GELISME_QPARAM3                                                               | Gelişme parametrik alan                                  |
| GELISME_QPARAM4                                                               | Gelişme parametrik alan                                  |
| GELISME_QPARAM5                                                               | Gelişme parametrik alan                                  |
| SONUC_QPARAM1                                                                 | Sonuç parametrik alan                                    |
| SONUC_QPARAM2                                                                 | Sonuç parametrik alan                                    |
| SONUC_QPARAM3                                                                 | Sonuç parametrik alan                                    |
| SONUC_QPARAM4                                                                 | Sonuç parametrik alan                                    |
| SONUC_QPARAM5                                                                 | Sonuç parametrik alan                                    |
| KAPATMA_QPARAM1                                                               | Kapatma parametrik alan                                  |
| KAPATMA_QPARAM2                                                               | Kapatma parametrik alan                                  |
| KAPATMA_QPARAM3                                                               | Kapatma parametrik alan                                  |
| KAPATMA_QPARAM4                                                               | Kapatma parametrik alan                                  |
| KAPATMA_QPARAM5                                                               | Kapatma parametrik alan                                  |
| GELISME_PPARAM1                                                               | Gelişme parametrik alan                                  |
| GELISME_PPARAM2                                                               | Gelişme parametrik alan                                  |
| GELISME_PPARAM3                                                               | Gelişme parametrik alan                                  |
| GELISME_PPARAM4                                                               | Gelişme parametrik alan                                  |
| GELISME_PPARAM5                                                               | Gelişme parametrik alan                                  |
| GELISME_PPARAM6                                                               | Gelişme parametrik alan                                  |
| GELISME_PPARAM7                                                               | Gelişme parametrik alan                                  |
| GELISME_PPARAM8                                                               | Gelişme parametrik alan                                  |
| GELISME_PPARAM9                                                               | Gelişme parametrik alan                                  |
| GELISME_PPARAM10                                                              | Gelişme parametrik alan                                  |
| SONUC_PPARAM1                                                                 | Sonuç parametrik alan                                    |
| SONUC_PPARAM2                                                                 | Sonuç parametrik alan                                    |
| SONUC_PPARAM3                                                                 | Sonuç parametrik alan                                    |
| SONUC_PPARAM4                                                                 | Sonuç parametrik alan                                    |
| SONUC_PPARAM5                                                                 | Sonuç parametrik alan                                    |
| SONUC_PPARAM6                                                                 | Sonuç parametrik alan                                    |
| SONUC_PPARAM7                                                                 | Sonuç parametrik alan                                    |
| SONUC_PPARAM8                                                                 | Sonuç parametrik alan                                    |
| SONUC_PPARAM9                                                                 | Sonuç parametrik alan                                    |
| SONUC_PPARAM10                                                                | Sonuç parametrik alan                                    |
| KAPATMA_PPARAM1                                                               | Kapatma parametrik alan                                  |
| KAPATMA_PPARAM2                                                               | Kapatma parametrik alan                                  |
| KAPATMA_PPARAM3                                                               | Kapatma parametrik alan                                  |
| KAPATMA_PPARAM4                                                               | Kapatma parametrik alan                                  |
| KAPATMA_PPARAM5                                                               | Kapatma parametrik alan                                  |
| KAPATMA_PPARAM6                                                               | Kapatma parametrik alan                                  |
| KAPATMA_PPARAM7                                                               | Kapatma parametrik alan                                  |
| KAPATMA_PPARAM8                                                               | Kapatma parametrik alan                                  |
| KAPATMA_PPARAM9                                                               | Kapatma parametrik alan                                  |
| KAPATMA_PPARAM10                                                              | Kapatma parametrik alan                                  |
| T2_ACIKLAMA                                                                   | Kaynak açıklaması                                        |
| T2_ICDIS                                                                      | İç veya dış müşteri şikayeti durumu                      |
| T3_ADISOYADI                                                                  | Bildiren adı soyadı                                      |
| T4_ADISOYADI                                                                  | Şikayet oluşturan kişinin adı soyadı                     |
| T5_ADISOYADI                                                                  | Lider adı soyadı                                         |
| T6_DEPARTMAN_ADI                                                              | Sorumlu departman adı                                    |
| T7_URUN_ADI                                                                   | Ürün adı                                                 |
| T8_ADISOYADI                                                                  | Gelişme raporu yazan adı soyadı                          |
| T9_ADISOYADI                                                                  | Kapatan adı soyadı                                       |
| T10_ISYERI_ADI                                                                | İş yeri adı                                              |
| T11_ACIKLAMA                                                                  | Sistem açıklaması                                        |
| T12_ADISOYADI                                                                 | Sonuç raporunu yazanın adı soyadı                        |
| T13_VALUE                                                                     | Düzeltici mi önleyici mi durumunun açıklaması            |
| URUN_TIPI                                                                     | Ürün tipi                                                |
| KAPATMAONAY_TUMU_0                                                            | Kapatma onaycısı, onay notu ve zamanı (1-10)             |
| KOK_DKOD                                                                      | DOF kodu                                                 |
| KOK_KOKNO                                                                     | Kök neden kodu                                           |
| KOK_ACIKLAMA                                                                  | Kök neden açıklaması                                     |
| KOK_NO                                                                        | Kök no                                                   |
| KOK_VERIFICATION                                                              | Uyarı kontrolü                                           |
| KOK_CONTRIBUTION                                                              | Uyarı kontrolü                                           |
| KOK_SISTEMG                                                                   | Sisteme giren sicil no                                   |
| KOK_SISTEMG_TARIH                                                             | Sisteme girme tarihi                                     |
| KOK_KOKNEDEN_DETAYI                                                           | Kök neden detayı                                         |
| KOK_PARAM1                                                                    | Kök neden parametrik alan                                |
| KOK_PARAM2                                                                    | Kök neden parametrik alan                                |
| KOK_PARAM3                                                                    | Kök neden parametrik alan                                |
| KOK_DPARAM1                                                                   | Kök neden parametrik alan                                |
| KOK_DPARAM2                                                                   | Kök neden parametrik alan                                |
| KOK_DPARAM3                                                                   | Kök neden parametrik alan                                |
| KOK_NAPARAM1                                                                  | Kök neden parametrik alan                                |
| KOK_NAPARAM2                                                                  | Kök neden parametrik alan                                |
| KOK_NAPARAM3                                                                  | Kök neden parametrik alan                                |
| KOK_NCPARAM1                                                                  | Kök neden parametrik alan                                |
| KOK_NCPARAM2                                                                  | Kök neden parametrik alan                                |
| KOK_NCPARAM3                                                                  | Kök neden parametrik alan                                |
| KOK_LPARAM1                                                                   | Kök neden parametrik alan                                |
| KOK_LPARAM2                                                                   | Kök neden parametrik alan                                |
| KOK_LPARAM3                                                                   | Kök neden parametrik alan                                |
| KOK_NAPARAM1_BIRIM                                                            | Kök neden parametrik alan                                |
| KOK_NAPARAM2_BIRIM                                                            | Kök neden parametrik alan                                |
| KOK_NAPARAM3_BIRIM                                                            | Kök neden parametrik alan                                |
| KOK_NCPARAM1_BIRIM                                                            | Kök neden parametrik alan                                |
| KOK_NCPARAM2_BIRIM                                                            | Kök neden parametrik alan                                |
| KOK_NCPARAM3_BIRIM                                                            | Kök neden parametrik alan                                |
| KOK_T2_NEDEN                                                                  | Kök neden parametrik alan                                |
| KOK_T3_ADISOYADI                                                              | Kök neden parametrik alan                                |
| KOK_LPARAM1_VALUE                                                             | Kök neden parametrik alan                                |
| KOK_LPARAM2_VALUE                                                             | Kök neden parametrik alan                                |
| KOK_LPARAM3_VALUE                                                             | Kök neden parametrik alan                                |
| KOK_NAPARAM1_VALUE                                                            | Kök neden parametrik alan                                |
| KOK_NAPARAM2_VALUE                                                            | Kök neden parametrik alan                                |
| KOK_NAPARAM3_VALUE                                                            | Kök neden parametrik alan                                |
| KOK_NCPARAM1_VALUE                                                            | Kök neden parametrik alan                                |
| KOK_NCPARAM2_VALUE                                                            | Kök neden parametrik alan                                |
| KOK_NCPARAM3_VALUE                                                            | Kök neden parametrik alan                                |
| AKS_NO                                                                        | Aksiyon no                                               |
| AKS_AKSIYON                                                                   | Aksiyon bilgisi                                          |
| AKS_YAPACAK                                                                   | Yapacak sicil no                                         |
| AKS_SORUMLU                                                                   | Sorumlu sicil no                                         |
| AKS_PLANT                                                                     | Plan tarihi                                              |
| AKS_YAPILAN                                                                   | Yapılanların açıklaması                                  |
| AKS_YAPT                                                                      | Yapılma tarihi                                           |
| AKS_STDNO                                                                     | Madde no                                                 |
| AKS_DOCNO                                                                     | Doküman no                                               |
| AKS_SISTEMEGIREN                                                              | Sisteme giren sicil no                                   |
| AKS_TIP                                                                       | Aksiyon tipi                                             |
| AKS_KAYITTARIHI                                                               | Kayıt tarihi                                             |
| AKS_FAALTUR                                                                   | Faaliyet türü                                            |
| AKS_VERIFICATION                                                              | Uyarı kontrolü                                           |
| AKS_EFFECTIVE                                                                 | Uyarı kontrolü                                           |
| AKS_VALIDATION                                                                | Uyarı kontrolü                                           |
| AKS_REVPLANT                                                                  | Planlanan revizyon tarihi                                |
| AKS_GECIKMENEDENI                                                             | Gecikme nedeni                                           |
| AKS_GECIKTI                                                                   | Gecikme durumu                                           |
| AKS_YAPACAKD                                                                  | Yapacak departman                                        |
| AKS_ALAN1                                                                     | Aksiyon parametrik alan                                  |
| AKS_ALAN2                                                                     | Aksiyon parametrik alan                                  |
| AKS_ALAN3                                                                     | Aksiyon parametrik alan                                  |
| AKS_ALAN4                                                                     | Aksiyon parametrik alan                                  |
| AKS_ALAN5                                                                     | Aksiyon parametrik alan                                  |
| AKS_NPARAM1                                                                   | Aksiyon parametrik alan                                  |
| AKS_NPARAM2                                                                   | Aksiyon parametrik alan                                  |
| AKS_NPARAM3                                                                   | Aksiyon parametrik alan                                  |
| AKS_NPARAM4                                                                   | Aksiyon parametrik alan                                  |
| AKS_NPARAM1_BIRIM                                                             | Aksiyon parametrik alan                                  |
| AKS_NPARAM2_BIRIM                                                             | Aksiyon parametrik alan                                  |
| AKS_NPARAM3_BIRIM                                                             | Aksiyon parametrik alan                                  |
| AKS_NPARAM4_BIRIM                                                             | Aksiyon parametrik alan                                  |
| AKS_LPARAM1                                                                   | Aksiyon parametrik alan                                  |
| AKS_LPARAM2                                                                   | Aksiyon parametrik alan                                  |
| AKS_LPARAM3                                                                   | Aksiyon parametrik alan                                  |
| AKS_DURUM                                                                     | Durum                                                    |
| AKS_ONAY_DURUM                                                                | Onay durumu                                              |
| AKS_DKOD                                                                      | DOF kodu                                                 |
| AKS_SON_DEGISTIREN                                                            | Son değişiklik yapan sicil no                            |
| AKS_DEGISTIRMET                                                               | Değiştirme Tarihi                                        |
| AKS_YAYINLANDI                                                                | Yayınlanma durumu                                        |
| AKS_ACIKLAMA                                                                  | Açıklama                                                 |
| AKS_QPARAM1                                                                   | Aksiyon parametrik alan                                  |
| AKS_QPARAM2                                                                   | Aksiyon parametrik alan                                  |
| AKS_QPARAM3                                                                   | Aksiyon parametrik alan                                  |
| AKS_QPARAM4                                                                   | Aksiyon parametrik alan                                  |
| AKS_QPARAM5                                                                   | Aksiyon parametrik alan                                  |
| AKS_DPARAM1                                                                   | Aksiyon parametrik alan                                  |
| AKS_DPARAM2                                                                   | Aksiyon parametrik alan                                  |
| AKS_DPARAM3                                                                   | Aksiyon parametrik alan                                  |
| AKS_RET_TIPI                                                                  | Ret tipi                                                 |
| AKS_SIRA_NO                                                                   | Sıra no                                                  |
| AKS_ALAN6                                                                     | Aksiyon parametrik alan                                  |
| AKS_ALAN7                                                                     | Aksiyon parametrik alan                                  |
| AKS_ALAN8                                                                     | Aksiyon parametrik alan                                  |
| AKS_ALAN9                                                                     | Aksiyon parametrik alan                                  |
| AKS_ALAN10                                                                    | Aksiyon parametrik alan                                  |
| AKS_ALAN11                                                                    | Aksiyon parametrik alan                                  |
| AKS_ALAN12                                                                    | Aksiyon parametrik alan                                  |
| AKS_ALAN13                                                                    | Aksiyon parametrik alan                                  |
| AKS_ALAN14                                                                    | Aksiyon parametrik alan                                  |
| AKS_ALAN15                                                                    | Aksiyon parametrik alan                                  |
| AKS_T2_ADISOYADI                                                              | Aksiyon yapacak adı soyadı                               |
| AKS_T3_ADISOYADI                                                              | Aksiyon sorumlu adı soyadı                               |
| AKS_T4_ADISOYADI                                                              | Sisteme giren adı soyadı                                 |
| AKS_T5_KAYNAK                                                                 | DOF kaynağı                                              |
| AKS_T5_URUN                                                                   | DOF ürün bilgisi                                         |
| AKS_T5_UYGT                                                                   | DOF Uygunsuzluk tanımı                                   |
| AKS_T5_UYGDT                                                                  | DOF Uygunsuzluk detayı                                   |
| AKS_T5_LIDER                                                                  | DOF Lider adı soyadı                                     |
| AKS_T5_BILDIREN                                                               | DOF Bildiren adı soyadı                                  |
| AKS_T5_KAPATAN                                                                | DOF Kapatan adı soyadı                                   |
| AKS_T5_KAPATMAT                                                               | DOF Kapatma tarihi                                       |
| AKS_T5_SORUMLUD                                                               | DOF Sorumlu departman                                    |
| AKS_T5_SISTEMEKT                                                              | DOF Sisteme ekleme tarihi                                |
| AKS_T5_TERMIN_TARIHI                                                          | DOF Termin tarihi                                        |
| AKS_T5_DURUM                                                                  | DOF durum                                                |
| AKS_T6_ADISOYADI                                                              | Son değişiklik yapan adı soyadı                          |
| AKS_T7_ACIKLAMA                                                               | Kaynak açıklaması                                        |
| AKS_T7_ICDIS                                                                  | Şikayet tipi                                             |
| AKS_T8_URUN_ADI                                                               | Ürün adı                                                 |
| AKS_T9_ADISOYADI                                                              | Lider adı soyadı                                         |
| AKS_T10_ADISOYADI                                                             | Bildiren adı soyadı                                      |
| AKS_T11_ADISOYADI                                                             | Kapatan adı soyadı                                       |
| AKS_T12_DEPARTMAN_ADI                                                         | Sorumlu departman adı                                    |
| AKS_LPARAM1_VALUE                                                             | Aksiyon parametrik alan                                  |
| AKS_LPARAM2_VALUE                                                             | Aksiyon parametrik alan                                  |
| AKS_LPARAM3_VALUE                                                             | Aksiyon parametrik alan                                  |
| AKS_NPARAM1_VALUE                                                             | Aksiyon parametrik alan                                  |
| AKS_NPARAM2_VALUE                                                             | Aksiyon parametrik alan                                  |
| AKS_NPARAM3_VALUE                                                             | Aksiyon parametrik alan                                  |
| AKS_NPARAM4_VALUE                                                             | Aksiyon parametrik alan                                  |
| AKS_ACAN_DEPT                                                                 | Aksiyon açan departman                                   |
| AKS_ACMAONAY_0                                                                | Açma onaycıları ve tarihler(10' a kadar gidiyor)         |
| AKS_GERCEKLESMEONAY_0                                                         | Gerçekleşme onaycıları ve tarihler(10' a kadar gidiyor)  |
| AKS_GECIKTIRMEONAY_0                                                          | Geciktirme onaycıları ve tarihler(10' a kadar gidiyor)   |
| AKS_ACMAONAYTAR_0                                                             | Açma onay tarihi(10' a kadar gidiyor)                    |
| AKS_GERCEKLESMEONAYTAR_0                                                      | Gerçekleşme onay tarihi(10' a kadar gidiyor)             |
| AKS_GECIKTIRMEONAYTAR_0                                                       | Geciktirme onay tarihi(10' a kadar gidiyor)              |
| AKS_KOKNEDEN                                                                  | Tüm kök neden bilgisi                                    |
| AKS_DOC_ADI                                                                   | Doküman adı                                              |
| AKS_DOC_HAZ_KISI                                                              | Doküman hazırlayan kişi                                  |
| AKS_DURUM_ACK                                                                 | Durum açıklaması                                         |
| AKS_DOSYALAR                                                                  | Dosyalar                                                 |
| **Düzeltici Aksiyon**                                                         |                                                          |
| AKS_D_NO                                                                      | Aksiyon no                                               |
| AKS_D_AKSIYON                                                                 | Aksiyon bilgisi                                          |
| AKS_D_YAPACAK                                                                 | Yapacak sicil no                                         |
| AKS_D_SORUMLU                                                                 | Sorumlu sicil no                                         |
| AKS_D_PLANT                                                                   | Plan tarihi                                              |
| AKS_D_YAPILAN                                                                 | Yapılanların açıklaması                                  |
| AKS_D_YAPT                                                                    | Yapılma tarihi                                           |
| AKS_D_STDNO                                                                   | Madde no                                                 |
| AKS_D_DOCNO                                                                   | Doküman no                                               |
| AKS_D_SISTEMEGIREN                                                            | Sisteme giren sicil no                                   |
| AKS_D_TIP                                                                     | Aksiyon tipi                                             |
| AKS_D_KAYITTARIHI                                                             | Kayıt tarihi                                             |
| AKS_D_FAALTUR                                                                 | Faaliyet türü                                            |
| AKS_D_VERIFICATION                                                            | Uyarı kontrolü                                           |
| AKS_D_EFFECTIVE                                                               | Uyarı kontrolü                                           |
| AKS_D_VALIDATION                                                              | Uyarı kontrolü                                           |
| AKS_D_REVPLANT                                                                | Planlanan revizyon tarihi                                |
| AKS_D_GECIKMENEDENI                                                           | Gecikme nedeni                                           |
| AKS_D_GECIKTI                                                                 | Gecikme durumu                                           |
| AKS_D_YAPACAKD                                                                | Yapacak departman                                        |
| AKS_D_ALAN1                                                                   | Parametrik alan                                          |
| AKS_D_ALAN2                                                                   | Parametrik alan                                          |
| AKS_D_ALAN3                                                                   | Parametrik alan                                          |
| AKS_D_ALAN4                                                                   | Parametrik alan                                          |
| AKS_D_ALAN5                                                                   | Parametrik alan                                          |
| AKS_D_NPARAM1                                                                 | Parametrik alan                                          |
| AKS_D_NPARAM2                                                                 | Parametrik alan                                          |
| AKS_D_NPARAM3                                                                 | Parametrik alan                                          |
| AKS_D_NPARAM4                                                                 | Parametrik alan                                          |
| AKS_D_NPARAM1_BIRIM                                                           | Parametrik alan                                          |
| AKS_D_NPARAM2_BIRIM                                                           | Parametrik alan                                          |
| AKS_D_NPARAM3_BIRIM                                                           | Parametrik alan                                          |
| AKS_D_NPARAM4_BIRIM                                                           | Parametrik alan                                          |
| AKS_D_LPARAM1                                                                 | Parametrik alan                                          |
| AKS_D_LPARAM2                                                                 | Parametrik alan                                          |
| AKS_D_LPARAM3                                                                 | Parametrik alan                                          |
| AKS_D_DURUM                                                                   | Durum                                                    |
| AKS_D_ONAY_DURUM                                                              | Onay durumu                                              |
| AKS_D_DKOD                                                                    | DOF kodu                                                 |
| AKS_D_SON_DEGISTIREN                                                          | Son değişiklik yapan sicil no                            |
| AKS_D_DEGISTIRMET                                                             | Değiştirme Tarihi                                        |
| AKS_D_YAYINLANDI                                                              | Yayınlanma durumu                                        |
| AKS_D_ACIKLAMA                                                                | Açıklama                                                 |
| AKS_D_QPARAM1                                                                 | Parametrik alan                                          |
| AKS_D_QPARAM2                                                                 | Parametrik alan                                          |
| AKS_D_QPARAM3                                                                 | Parametrik alan                                          |
| AKS_D_QPARAM4                                                                 | Parametrik alan                                          |
| AKS_D_QPARAM5                                                                 | Parametrik alan                                          |
| AKS_D_DPARAM1                                                                 | Parametrik alan                                          |
| AKS_D_DPARAM2                                                                 | Parametrik alan                                          |
| AKS_D_DPARAM3                                                                 | Parametrik alan                                          |
| AKS_D_RET_TIPI                                                                | Ret tipi                                                 |
| AKS_D_SIRA_NO                                                                 | Sıra no                                                  |
| AKS_D_ALAN6                                                                   | Parametrik alan                                          |
| AKS_D_ALAN7                                                                   | Parametrik alan                                          |
| AKS_D_ALAN8                                                                   | Parametrik alan                                          |
| AKS_D_ALAN9                                                                   | Parametrik alan                                          |
| AKS_D_ALAN10                                                                  | Parametrik alan                                          |
| AKS_D_ALAN11                                                                  | Parametrik alan                                          |
| AKS_D_ALAN12                                                                  | Parametrik alan                                          |
| AKS_D_ALAN13                                                                  | Parametrik alan                                          |
| AKS_D_ALAN14                                                                  | Parametrik alan                                          |
| AKS_D_ALAN15                                                                  | Parametrik alan                                          |
| AKS_D_T2_ADISOYADI                                                            | Aksiyon yapacak adı soyadı                               |
| AKS_D_T3_ADISOYADI                                                            | Aksiyon sorumlu adı soyadı                               |
| AKS_D_T4_ADISOYADI                                                            | Sisteme giren adı soyadı                                 |
| AKS_D_T5_KAYNAK                                                               | DOF kaynağı                                              |
| AKS_D_T5_URUN                                                                 | DOF ürün bilgisi                                         |
| AKS_D_T5_UYGT                                                                 | DOF Uygunsuzluk tanımı                                   |
| AKS_D_T5_UYGDT                                                                | DOF Uygunsuzluk detayı                                   |
| AKS_D_T5_LIDER                                                                | DOF Lider adı soyadı                                     |
| AKS_D_T5_BILDIREN                                                             | DOF Bildiren adı soyadı                                  |
| AKS_D_T5_KAPATAN                                                              | DOF Kapatan adı soyadı                                   |
| AKS_D_T5_KAPATMAT                                                             | DOF Kapatma tarihi                                       |
| AKS_D_T5_SORUMLUD                                                             | DOF Sorumlu departman                                    |
| AKS_D_T5_SISTEMEKT                                                            | DOF Sisteme ekleme tarihi                                |
| AKS_D_T5_TERMIN_TARIHI                                                        | DOF Termin tarihi                                        |
| AKS_D_T5_DURUM                                                                | DOF durum                                                |
| AKS_D_T6_ADISOYADI                                                            | Son değişiklik yapan adı soyadı                          |
| AKS_D_T7_ACIKLAMA                                                             | Kaynak açıklaması                                        |
| AKS_D_T7_ICDIS                                                                | Şikayet tipi                                             |
| AKS_D_T8_URUN_ADI                                                             | Ürün adı                                                 |
| AKS_D_T9_ADISOYADI                                                            | Lider adı soyadı                                         |
| AKS_D_T10_ADISOYADI                                                           | Bildiren adı soyadı                                      |
| AKS_D_T11_ADISOYADI                                                           | Kapatan adı soyadı                                       |
| AKS_D_T12_DEPARTMAN_ADI                                                       | Sorumlu departman adı                                    |
| AKS_D_LPARAM1_VALUE                                                           | Parametrik alan                                          |
| AKS_D_LPARAM2_VALUE                                                           | Parametrik alan                                          |
| AKS_D_LPARAM3_VALUE                                                           | Parametrik alan                                          |
| AKS_D_NPARAM1_VALUE                                                           | Parametrik alan                                          |
| AKS_D_NPARAM2_VALUE                                                           | Parametrik alan                                          |
| AKS_D_NPARAM3_VALUE                                                           | Parametrik alan                                          |
| AKS_D_NPARAM4_VALUE                                                           | Parametrik alan                                          |
| AKS_D_ACAN_DEPT                                                               | Aksiyon açan departman                                   |
| AKS_D_ACMAONAY_0                                                              | Açma onaycıları ve tarihler(10' a kadar gidiyor)         |
| AKS_D_GERCEKLESMEONAY_0                                                       | Gerçekleşme onaycıları ve tarihler(10' a kadar gidiyor)  |
| AKS_D_GECIKTIRMEONAY_0                                                        | Geciktirme onaycıları ve tarihler(10' a kadar gidiyor)   |
| AKS_D_ACMAONAYTAR_0                                                           | Açma onay tarihi(10' a kadar gidiyor)                    |
| AKS_D_GERCEKLESMEONAYTAR_0                                                    | Gerçekleşme onay tarihi(10' a kadar gidiyor)             |
| AKS_D_GECIKTIRMEONAYTAR_0                                                     | Geciktirme onay tarihi(10' a kadar gidiyor)              |
| AKS_D_KOKNEDEN                                                                | Tüm kök neden bilgisi                                    |
| AKS_D_SON_PLANT                                                               | Son plan tarihi                                          |
| AKS_D_DURUM_ACK                                                               | Durum açıklaması                                         |
| AKS_D_DOSYALAR                                                                | Dosyalar                                                 |
| **Gerçekleşen Düzeltici Aksiyonlar**                                          |                                                          |
| AKS_DG_NO                                                                     | Aksiyon no                                               |
| AKS_DG_AKSIYON                                                                | Aksiyon bilgisi                                          |
| AKS_DG_YAPACAK                                                                | Yapacak sicil no                                         |
| AKS_DG_SORUMLU                                                                | Sorumlu sicil no                                         |
| AKS_DG_PLANT                                                                  | Plan tarihi                                              |
| AKS_DG_YAPILAN                                                                | Yapılanların açıklaması                                  |
| AKS_DG_YAPT                                                                   | Yapılma tarihi                                           |
| AKS_DG_STDNO                                                                  | Madde no                                                 |
| AKS_DG_DOCNO                                                                  | Doküman no                                               |
| AKS_DG_SISTEMEGIREN                                                           | Sisteme giren sicil no                                   |
| AKS_DG_TIP                                                                    | Aksiyon tipi                                             |
| AKS_DG_KAYITTARIHI                                                            | Kayıt tarihi                                             |
| AKS_DG_FAALTUR                                                                | Faaliyet türü                                            |
| AKS_DG_VERIFICATION                                                           | Uyarı kontrolü                                           |
| AKS_DG_EFFECTIVE                                                              | Uyarı kontrolü                                           |
| AKS_DG_VALIDATION                                                             | Uyarı kontrolü                                           |
| AKS_DG_REVPLANT                                                               | Planlanan revizyon tarihi                                |
| AKS_DG_GECIKMENEDENI                                                          | Gecikme nedeni                                           |
| AKS_DG_GECIKTI                                                                | Gecikme durumu                                           |
| AKS_DG_YAPACAKD                                                               | Yapacak departman                                        |
| AKS_DG_ALAN1                                                                  | Parametrik alan                                          |
| AKS_DG_ALAN2                                                                  | Parametrik alan                                          |
| AKS_DG_ALAN3                                                                  | Parametrik alan                                          |
| AKS_DG_ALAN4                                                                  | Parametrik alan                                          |
| AKS_DG_ALAN5                                                                  | Parametrik alan                                          |
| AKS_DG_NPARAM1                                                                | Parametrik alan                                          |
| AKS_DG_NPARAM2                                                                | Parametrik alan                                          |
| AKS_DG_NPARAM3                                                                | Parametrik alan                                          |
| AKS_DG_NPARAM4                                                                | Parametrik alan                                          |
| AKS_DG_NPARAM1_BIRIM                                                          | Parametrik alan                                          |
| AKS_DG_NPARAM2_BIRIM                                                          | Parametrik alan                                          |
| AKS_DG_NPARAM3_BIRIM                                                          | Parametrik alan                                          |
| AKS_DG_NPARAM4_BIRIM                                                          | Parametrik alan                                          |
| AKS_DG_LPARAM1                                                                | Parametrik alan                                          |
| AKS_DG_LPARAM2                                                                | Parametrik alan                                          |
| AKS_DG_LPARAM3                                                                | Parametrik alan                                          |
| AKS_DG_DURUM                                                                  | Durum                                                    |
| AKS_DG_ONAY_DURUM                                                             | Onay durumu                                              |
| AKS_DG_DKOD                                                                   | DOF kodu                                                 |
| AKS_DG_SON_DEGISTIREN                                                         | Son değişiklik yapan sicil no                            |
| AKS_DG_DEGISTIRMET                                                            | Değiştirme Tarihi                                        |
| AKS_DG_YAYINLANDI                                                             | Yayınlanma durumu                                        |
| AKS_DG_ACIKLAMA                                                               | Açıklama                                                 |
| AKS_DG_QPARAM1                                                                | Parametrik alan                                          |
| AKS_DG_QPARAM2                                                                | Parametrik alan                                          |
| AKS_DG_QPARAM3                                                                | Parametrik alan                                          |
| AKS_DG_QPARAM4                                                                | Parametrik alan                                          |
| AKS_DG_QPARAM5                                                                | Parametrik alan                                          |
| AKS_DG_DPARAM1                                                                | Parametrik alan                                          |
| AKS_DG_DPARAM2                                                                | Parametrik alan                                          |
| AKS_DG_DPARAM3                                                                | Parametrik alan                                          |
| AKS_DG_RET_TIPI                                                               | Ret tipi                                                 |
| AKS_DG_SIRA_NO                                                                | Sıra no                                                  |
| AKS_DG_ALAN6                                                                  | Parametrik alan                                          |
| AKS_DG_ALAN7                                                                  | Parametrik alan                                          |
| AKS_DG_ALAN8                                                                  | Parametrik alan                                          |
| AKS_DG_ALAN9                                                                  | Parametrik alan                                          |
| AKS_DG_ALAN10                                                                 | Parametrik alan                                          |
| AKS_DG_ALAN11                                                                 | Parametrik alan                                          |
| AKS_DG_ALAN12                                                                 | Parametrik alan                                          |
| AKS_DG_ALAN13                                                                 | Parametrik alan                                          |
| AKS_DG_ALAN14                                                                 | Parametrik alan                                          |
| AKS_DG_ALAN15                                                                 | Parametrik alan                                          |
| AKS_DG_T2_ADISOYADI                                                           | Aksiyon yapacak adı soyadı                               |
| AKS_DG_T3_ADISOYADI                                                           | Aksiyon sorumlu adı soyadı                               |
| AKS_DG_T4_ADISOYADI                                                           | Sisteme giren adı soyadı                                 |
| AKS_DG_T5_KAYNAK                                                              | DOF kaynağı                                              |
| AKS_DG_T5_URUN                                                                | DOF ürün bilgisi                                         |
| AKS_DG_T5_UYGT                                                                | DOF Uygunsuzluk tanımı                                   |
| AKS_DG_T5_UYGDT                                                               | DOF Uygunsuzluk detayı                                   |
| AKS_DG_T5_LIDER                                                               | DOF Lider adı soyadı                                     |
| AKS_DG_T5_BILDIREN                                                            | DOF Bildiren adı soyadı                                  |
| AKS_DG_T5_KAPATAN                                                             | DOF Kapatan adı soyadı                                   |
| AKS_DG_T5_KAPATMAT                                                            | DOF Kapatma tarihi                                       |
| AKS_DG_T5_SORUMLUD                                                            | DOF Sorumlu departman                                    |
| AKS_DG_T5_SISTEMEKT                                                           | DOF Sisteme ekleme tarihi                                |
| AKS_DG_T5_TERMIN_TARIHI                                                       | DOF Termin tarihi                                        |
| AKS_DG_T5_DURUM                                                               | DOF durum                                                |
| AKS_DG_T6_ADISOYADI                                                           | Son değişiklik yapan adı soyadı                          |
| AKS_DG_T7_ACIKLAMA                                                            | Kaynak açıklaması                                        |
| AKS_DG_T7_ICDIS                                                               | Şikayet tipi                                             |
| AKS_DG_T8_URUN_ADI                                                            | Ürün adı                                                 |
| AKS_DG_T9_ADISOYADI                                                           | Lider adı soyadı                                         |
| AKS_DG_T10_ADISOYADI                                                          | Bildiren adı soyadı                                      |
| AKS_DG_T11_ADISOYADI                                                          | Kapatan adı soyadı                                       |
| AKS_DG_T12_DEPARTMAN_ADI                                                      | Sorumlu departman adı                                    |
| AKS_DG_LPARAM1_VALUE                                                          | Parametrik alan                                          |
| AKS_DG_LPARAM2_VALUE                                                          | Parametrik alan                                          |
| AKS_DG_LPARAM3_VALUE                                                          | Parametrik alan                                          |
| AKS_DG_NPARAM1_VALUE                                                          | Parametrik alan                                          |
| AKS_DG_NPARAM2_VALUE                                                          | Parametrik alan                                          |
| AKS_DG_NPARAM3_VALUE                                                          | Parametrik alan                                          |
| AKS_DG_NPARAM4_VALUE                                                          | Parametrik alan                                          |
| AKS_DG_ACAN_DEPT                                                              | Aksiyon açan departman                                   |
| AKS_DG_ACMAONAY_0                                                             | Açma onaycıları ve tarihler(10' a kadar gidiyor)         |
| AKS_DG_GERCEKLESMEONAY_0                                                      | Gerçekleşme onaycıları ve tarihler(10' a kadar gidiyor)  |
| AKS_DG_GECIKTIRMEONAY_0                                                       | Geciktirme onaycıları ve tarihler(10' a kadar gidiyor)   |
| AKS_DG_ACMAONAYTAR_0                                                          | Açma onay tarihi(10' a kadar gidiyor)                    |
| AKS_DG_GERCEKLESMEONAYTAR_0                                                   | Gerçekleşme onay tarihi(10' a kadar gidiyor)             |
| AKS_DG_GECIKTIRMEONAYTAR_0                                                    | Geciktirme onay tarihi(10' a kadar gidiyor)              |
| AKS_DG_KOKNEDEN                                                               | Tüm kök neden bilgisi                                    |
| AKS_DG_DURUM_ACK                                                              | Durum açıklaması                                         |
| AKS_DG_DOSYALAR                                                               | Dosyalar                                                 |
| **Önleyici Aksiyonlar**                                                       |                                                          |
| AKS_O_NO                                                                      | Aksiyon no                                               |
| AKS_O_AKSIYON                                                                 | Aksiyon bilgisi                                          |
| AKS_O_YAPACAK                                                                 | Yapacak sicil no                                         |
| AKS_O_SORUMLU                                                                 | Sorumlu sicil no                                         |
| AKS_O_PLANT                                                                   | Plan tarihi                                              |
| AKS_O_YAPILAN                                                                 | Yapılanların açıklaması                                  |
| AKS_O_YAPT                                                                    | Yapılma tarihi                                           |
| AKS_O_STDNO                                                                   | Madde no                                                 |
| AKS_O_DOCNO                                                                   | Doküman no                                               |
| AKS_O_SISTEMEGIREN                                                            | Sisteme giren sicil no                                   |
| AKS_O_TIP                                                                     | Aksiyon tipi                                             |
| AKS_O_KAYITTARIHI                                                             | Kayıt tarihi                                             |
| AKS_O_FAALTUR                                                                 | Faaliyet türü                                            |
| AKS_O_VERIFICATION                                                            | Uyarı kontrolü                                           |
| AKS_O_EFFECTIVE                                                               | Uyarı kontrolü                                           |
| AKS_O_VALIDATION                                                              | Uyarı kontrolü                                           |
| AKS_O_REVPLANT                                                                | Planlanan revizyon tarihi                                |
| AKS_O_GECIKMENEDENI                                                           | Gecikme nedeni                                           |
| AKS_O_GECIKTI                                                                 | Gecikme durumu                                           |
| AKS_O_YAPACAKD                                                                | Yapacak departman                                        |
| AKS_O_ALAN1                                                                   | Parametrik alan                                          |
| AKS_O_ALAN2                                                                   | Parametrik alan                                          |
| AKS_O_ALAN3                                                                   | Parametrik alan                                          |
| AKS_O_ALAN4                                                                   | Parametrik alan                                          |
| AKS_O_ALAN5                                                                   | Parametrik alan                                          |
| AKS_O_NPARAM1                                                                 | Parametrik alan                                          |
| AKS_O_NPARAM2                                                                 | Parametrik alan                                          |
| AKS_O_NPARAM3                                                                 | Parametrik alan                                          |
| AKS_O_NPARAM4                                                                 | Parametrik alan                                          |
| AKS_O_NPARAM1_BIRIM                                                           | Parametrik alan                                          |
| AKS_O_NPARAM2_BIRIM                                                           | Parametrik alan                                          |
| AKS_O_NPARAM3_BIRIM                                                           | Parametrik alan                                          |
| AKS_O_NPARAM4_BIRIM                                                           | Parametrik alan                                          |
| AKS_O_LPARAM1                                                                 | Parametrik alan                                          |
| AKS_O_LPARAM2                                                                 | Parametrik alan                                          |
| AKS_O_LPARAM3                                                                 | Parametrik alan                                          |
| AKS_O_DURUM                                                                   | Durum                                                    |
| AKS_O_ONAY_DURUM                                                              | Onay durumu                                              |
| AKS_O_DKOD                                                                    | DOF kodu                                                 |
| AKS_O_SON_DEGISTIREN                                                          | Son değişiklik yapan sicil no                            |
| AKS_O_DEGISTIRMET                                                             | Değiştirme Tarihi                                        |
| AKS_O_YAYINLANDI                                                              | Yayınlanma durumu                                        |
| AKS_O_ACIKLAMA                                                                | Açıklama                                                 |
| AKS_O_QPARAM1                                                                 | Parametrik alan                                          |
| AKS_O_QPARAM2                                                                 | Parametrik alan                                          |
| AKS_O_QPARAM3                                                                 | Parametrik alan                                          |
| AKS_O_QPARAM4                                                                 | Parametrik alan                                          |
| AKS_O_QPARAM5                                                                 | Parametrik alan                                          |
| AKS_O_DPARAM1                                                                 | Parametrik alan                                          |
| AKS_O_DPARAM2                                                                 | Parametrik alan                                          |
| AKS_O_DPARAM3                                                                 | Parametrik alan                                          |
| AKS_O_RET_TIPI                                                                | Ret tipi                                                 |
| AKS_O_SIRA_NO                                                                 | Sıra no                                                  |
| AKS_O_ALAN6                                                                   | Parametrik alan                                          |
| AKS_O_ALAN7                                                                   | Parametrik alan                                          |
| AKS_O_ALAN8                                                                   | Parametrik alan                                          |
| AKS_O_ALAN9                                                                   | Parametrik alan                                          |
| AKS_O_ALAN10                                                                  | Parametrik alan                                          |
| AKS_O_ALAN11                                                                  | Parametrik alan                                          |
| AKS_O_ALAN12                                                                  | Parametrik alan                                          |
| AKS_O_ALAN13                                                                  | Parametrik alan                                          |
| AKS_O_ALAN14                                                                  | Parametrik alan                                          |
| AKS_O_ALAN15                                                                  | Parametrik alan                                          |
| AKS_O_T2_ADISOYADI                                                            | Aksiyon yapacak adı soyadı                               |
| AKS_O_T3_ADISOYADI                                                            | Aksiyon sorumlu adı soyadı                               |
| AKS_O_T4_ADISOYADI                                                            | Sisteme giren adı soyadı                                 |
| AKS_O_T5_KAYNAK                                                               | DOF kaynağı                                              |
| AKS_O_T5_URUN                                                                 | DOF ürün bilgisi                                         |
| AKS_O_T5_UYGT                                                                 | DOF Uygunsuzluk tanımı                                   |
| AKS_O_T5_UYGDT                                                                | DOF Uygunsuzluk detayı                                   |
| AKS_O_T5_LIDER                                                                | DOF Lider adı soyadı                                     |
| AKS_O_T5_BILDIREN                                                             | DOF Bildiren adı soyadı                                  |
| AKS_O_T5_KAPATAN                                                              | DOF Kapatan adı soyadı                                   |
| AKS_O_T5_KAPATMAT                                                             | DOF Kapatma tarihi                                       |
| AKS_O_T5_SORUMLUD                                                             | DOF Sorumlu departman                                    |
| AKS_O_T5_SISTEMEKT                                                            | DOF Sisteme ekleme tarihi                                |
| AKS_O_T5_TERMIN_TARIHI                                                        | DOF Termin tarihi                                        |
| AKS_O_T5_DURUM                                                                | DOF durum                                                |
| AKS_O_T6_ADISOYADI                                                            | Son değişiklik yapan adı soyadı                          |
| AKS_O_T7_ACIKLAMA                                                             | Kaynak açıklaması                                        |
| AKS_O_T7_ICDIS                                                                | Şikayet tipi                                             |
| AKS_O_T8_URUN_ADI                                                             | Ürün adı                                                 |
| AKS_O_T9_ADISOYADI                                                            | Lider adı soyadı                                         |
| AKS_O_T10_ADISOYADI                                                           | Bildiren adı soyadı                                      |
| AKS_O_T11_ADISOYADI                                                           | Kapatan adı soyadı                                       |
| AKS_O_T12_DEPARTMAN_ADI                                                       | Sorumlu departman adı                                    |
| AKS_O_LPARAM1_VALUE                                                           | Parametrik alan                                          |
| AKS_O_LPARAM2_VALUE                                                           | Parametrik alan                                          |
| AKS_O_LPARAM3_VALUE                                                           | Parametrik alan                                          |
| AKS_O_NPARAM1_VALUE                                                           | Parametrik alan                                          |
| AKS_O_NPARAM2_VALUE                                                           | Parametrik alan                                          |
| AKS_O_NPARAM3_VALUE                                                           | Parametrik alan                                          |
| AKS_O_NPARAM4_VALUE                                                           | Parametrik alan                                          |
| AKS_O_ACAN_DEPT                                                               | Aksiyon açan departman                                   |
| AKS_O_ACMAONAY_0                                                              | Açma onaycıları ve tarihler(10' a kadar gidiyor)         |
| AKS_O_GERCEKLESMEONAY_0                                                       | Gerçekleşme onaycıları ve tarihler(10' a kadar gidiyor)  |
| AKS_O_GECIKTIRMEONAY_0                                                        | Geciktirme onaycıları ve tarihler(10' a kadar gidiyor)   |
| AKS_O_ACMAONAYTAR_0                                                           | Açma onay tarihi(10' a kadar gidiyor)                    |
| AKS_O_GERCEKLESMEONAYTAR_0                                                    | Gerçekleşme onay tarihi(10' a kadar gidiyor)             |
| AKS_O_GECIKTIRMEONAYTAR_0                                                     | Geciktirme onay tarihi(10' a kadar gidiyor)              |
| AKS_O_KOKNEDEN                                                                | Tüm kök neden bilgisi                                    |
| AKS_O_DURUM_ACK                                                               | Durum açıklaması                                         |
| AKS_O_SON_PLANT                                                               | Son plan tarihi                                          |
| AKS_O_DOSYALAR                                                                | Dosyalar                                                 |

## **1.5. DÖF Aksiyon Raporu Replacement (Kısa Kodlar) Tag Tablosu**

Düzeltici ve Önleyici Modülünde kullanılan DÖF Aksiyon Raporu taglerin listesi aşağıdaki tabloda yer almaktadır.

| **Kısaltma (Kısalmalar tag şeklinde < \> isaretleri arasına yazılacaktır.)** | **Açıklama**                                            |
|-------------------------------------------------------------------------------|---------------------------------------------------------|
| NO                                                                            | Aksiyon no                                              |
| AKSIYON                                                                       | Aksiyon bilgisi                                         |
| YAPACAK                                                                       | Yapacak sicil no                                        |
| SORUMLU                                                                       | Sorumlu sicil no                                        |
| PLANT                                                                         | Plan tarihi                                             |
| YAPILAN                                                                       | Yapılanların açıklaması                                 |
| YAPT                                                                          | Yapılma tarihi                                          |
| STDNO                                                                         | Madde no                                                |
| DOCNO                                                                         | Doküman no                                              |
| SISTEMEGIREN                                                                  | Sisteme giren sicil no                                  |
| TIP                                                                           | Aksiyon tipi                                            |
| KAYITTARIHI                                                                   | Kayıt tarihi                                            |
| FAALTUR                                                                       | Faaliyet türü                                           |
| VERIFICATION                                                                  | Uyarı kontrolü                                          |
| EFFECTIVE                                                                     | Uyarı kontrolü                                          |
| VALIDATION                                                                    | Uyarı kontrolü                                          |
| REVPLANT                                                                      | Planlanan revizyon tarihi                               |
| GECIKMENEDENI                                                                 | Gecikme nedeni                                          |
| GECIKTI                                                                       | Müşteri şikayet kodu                                    |
| YAPACAKD                                                                      | Yapacak departman                                       |
| ALAN1                                                                         | Parametrik alan                                         |
| ALAN2                                                                         | Parametrik alan                                         |
| ALAN3                                                                         | Parametrik alan                                         |
| ALAN4                                                                         | Parametrik alan                                         |
| ALAN5                                                                         | Parametrik alan                                         |
| NPARAM1                                                                       | Parametrik alan                                         |
| NPARAM2                                                                       | Parametrik alan                                         |
| NPARAM3                                                                       | Parametrik alan                                         |
| NPARAM4                                                                       | Parametrik alan                                         |
| NPARAM1_BIRIM                                                                 | Parametrik alan                                         |
| NPARAM2_BIRIM                                                                 | Parametrik alan                                         |
| NPARAM3_BIRIM                                                                 | Parametrik alan                                         |
| NPARAM4_BIRIM                                                                 | Parametrik alan                                         |
| LPARAM1                                                                       | Parametrik alan                                         |
| LPARAM2                                                                       | Parametrik alan                                         |
| LPARAM3                                                                       | Parametrik alan                                         |
| DURUM                                                                         | Durum                                                   |
| ONAY_DURUM                                                                    | Onay durumu                                             |
| DKOD                                                                          | DOF kodu                                                |
| SON_DEGISTIREN                                                                | Son değişiklik yapan sicil no                           |
| DEGISTIRMET                                                                   | Değiştirme Tarihi                                       |
| YAYINLANDI                                                                    | Yayınlanma durumu                                       |
| ACIKLAMA                                                                      | Açıklama                                                |
| QPARAM1                                                                       | Sorgu tipli parametrik alan                             |
| QPARAM2                                                                       | Sorgu tipli parametrik alan                             |
| QPARAM3                                                                       | Sorgu tipli parametrik alan                             |
| QPARAM4                                                                       | Sorgu tipli parametrik alan                             |
| QPARAM5                                                                       | Sorgu tipli parametrik alan                             |
| DPARAM1                                                                       | Tarhi tipli parametrik alan                             |
| DPARAM2                                                                       | Tarhi tipli parametrik alan                             |
| DPARAM3                                                                       | Tarhi tipli parametrik alan                             |
| RET_TIPI                                                                      | Ret tipi                                                |
| SIRA_NO                                                                       | Sıra no                                                 |
| ALAN6                                                                         | Parametrik alan                                         |
| ALAN7                                                                         | Parametrik alan                                         |
| ALAN8                                                                         | Parametrik alan                                         |
| ALAN9                                                                         | Parametrik alan                                         |
| ALAN10                                                                        | Parametrik alan                                         |
| ALAN11                                                                        | Parametrik alan                                         |
| ALAN12                                                                        | Parametrik alan                                         |
| ALAN13                                                                        | Parametrik alan                                         |
| ALAN14                                                                        | Parametrik alan                                         |
| ALAN15                                                                        | Parametrik alan                                         |
| T2_ADISOYADI                                                                  | Aksiyon yapacak adı soyadı                              |
| T3_ADISOYADI                                                                  | Aksiyon sorumlu adı soyadı                              |
| T4_ADISOYADI                                                                  | Sisteme giren adı soyadı                                |
| T5_KAYNAK                                                                     | DOF kaynağı                                             |
| T5_URUN                                                                       | DOF ürün bilgisi                                        |
| T5_UYGT                                                                       | DOF Uygunsuzluk tanımı                                  |
| T5_UYGDT                                                                      | DOF Uygunsuzluk detayı                                  |
| T5_LIDER                                                                      | DOF Lider adı soyadı                                    |
| T5_BILDIREN                                                                   | DOF Bildiren adı soyadı                                 |
| T5_KAPATAN                                                                    | DOF Kapatan adı soyadı                                  |
| T5_KAPATMAT                                                                   | DOF Kapatma tarihi                                      |
| T5_SORUMLUD                                                                   | DOF Sorumlu departman                                   |
| T5_SISTEMEKT                                                                  | DOF Sisteme ekleme tarihi                               |
| T5_TERMIN_TARIHI                                                              | DOF Termin tarihi                                       |
| T5_DURUM                                                                      | DOF durum                                               |
| T6_ADISOYADI                                                                  | Son değişiklik yapan adı soyadı                         |
| T7_ACIKLAMA                                                                   | Kaynak açıklaması                                       |
| T7_ICDIS                                                                      | Şikayet tipi                                            |
| T8_URUN_ADI                                                                   | Ürün adı                                                |
| T9_ADISOYADI                                                                  | Lider adı soyadı                                        |
| T10_ADISOYADI                                                                 | Bildiren adı soyadı                                     |
| T11_ADISOYADI                                                                 | Kapatan adı soyadı                                      |
| T12_DEPARTMAN_ADI                                                             | Sorumlu departman adı                                   |
| LPARAM1_VALUE                                                                 | Liste tipli parametrik alan                             |
| LPARAM2_VALUE                                                                 | Liste tipli parametrik alan                             |
| LPARAM3_VALUE                                                                 | Liste tipli parametrik alan                             |
| NPARAM1_VALUE                                                                 | Nümerik tipli parametrik alan                           |
| NPARAM2_VALUE                                                                 | Nümerik tipli parametrik alan                           |
| NPARAM3_VALUE                                                                 | Nümerik tipli parametrik alan                           |
| NPARAM4_VALUE                                                                 | Nümerik tipli parametrik alan                           |
| QPARAM1_VALUE                                                                 | Sorgu tipli parametrik alan                             |
| QPARAM1_KOD                                                                   | Sorgu tipli parametrik alan                             |
| QPARAM2_VALUE                                                                 | Sorgu tipli parametrik alan                             |
| QPARAM2_KOD                                                                   | Sorgu tipli parametrik alan                             |
| QPARAM3_VALUE                                                                 | Sorgu tipli parametrik alan                             |
| QPARAM3_KOD                                                                   | Sorgu tipli parametrik alan                             |
| QPARAM4_VALUE                                                                 | Sorgu tipli parametrik alan                             |
| QPARAM4_KOD                                                                   | Sorgu tipli parametrik alan                             |
| QPARAM5_VALUE                                                                 | Sorgu tipli parametrik alan                             |
| QPARAM5_KOD                                                                   | Sorgu tipli parametrik alan                             |
| AKSIYON_ACAN_DEPT                                                             | Aksiyon açan departman                                  |
| AKS_ACMAONAY_0                                                                | Açma onaycıları ve tarihler(10' a kadar gidiyor)        |
| AKS_GERCEKLESMEONAY_0                                                         | Gerçekleşme onaycıları ve tarihler(10' a kadar gidiyor) |
| AKS_GECIKTIRMEONAY_0                                                          | Geciktirme onaycıları ve tarihler(10' a kadar gidiyor)  |
| AKS_ACMAONAYTAR_0                                                             | Açma onay tarihi(10' a kadar gidiyor)                   |
| AKS_GERCEKLESMEONAYTAR_0                                                      | Gerçekleşme onay tarihi(10' a kadar gidiyor)            |
| AKS_GECIKTIRMEONAYTAR_0                                                       | Geciktirme onay tarihi(10' a kadar gidiyor)             |
| KOKNEDEN                                                                      | Tüm kök neden bilgisi                                   |
| DURUM_ACK                                                                     | Durum açıklaması                                        |
| SORUMLU_DEP                                                                   | Sorumlu departman adı                                   |
| YAPACAK_DEP                                                                   | Yapacak departman adı                                   |
| REVIZYON_BITIS_TARIHI                                                         | Revizyon bitiş tarihi                                   |
| GECIKME_NEDENI                                                                | Gecikme nedeni                                          |

## **1.6. DÖF Detay Raporu Replacement (Kısa Kodlar) Tag Tablosu**

Düzeltici ve Önleyici Modülünde kullanılan DÖF Detay Raporu taglerin listesi aşağıdaki tabloda yer almaktadır.

| **Kısaltma (Kısalmalar tag şeklinde < \> isaretleri arasına yazılacaktır.)** | **Açıklama**                                             |
|-------------------------------------------------------------------------------|----------------------------------------------------------|
| DKOD                                                                          | DOF kodu                                                 |
| KAYNAK                                                                        | DOF kaynağı                                              |
| SISTEMEKT                                                                     | Sisteme ekleme tarihi                                    |
| MREF                                                                          | Denetimden açılan Müşteri şikayetleri için referans kodu |
| BILDIREN                                                                      | Bildiren kişi                                            |
| BILDIRIMT                                                                     | Bildirim Tarihi                                          |
| BILDIRIMS                                                                     | Bildirim şekli                                           |
| SIKAYETG                                                                      | Şikayet oluşturan sicil no                               |
| LIDER                                                                         | Lider sicil numarası                                     |
| SORUMLUD                                                                      | Sorumlu departman kodu                                   |
| UYGT                                                                          | DOF Uygunsuzluk tanımı                                   |
| UYGDT                                                                         | DOF Uygunsuzluk detayı                                   |
| URUN                                                                          | Ürün kodu                                                |
| GELRAPY                                                                       | Planlanan gelisme raporu tarihi                          |
| DURUM                                                                         | Durum bilgisi                                            |
| GELISMEYT                                                                     | Gelişme raporu yazma tarihi                              |
| GELISMERP                                                                     | Gelişme raporu                                           |
| SONRAPY                                                                       | Planlanan sonuç raporu tarihi                            |
| GELKYTUSR                                                                     | Gelişme raporu yazan sicili                              |
| NOTLAR                                                                        | Notlar                                                   |
| KAPATAN                                                                       | Kapatan kişinin sicil numarası                           |
| KAPATMAT                                                                      | Kapatma tarihi                                           |
| MKOD                                                                          | Müşteri kodu                                             |
| YETERLILIK                                                                    | Yeterlilik                                               |
| HATA6M                                                                        | Hata parametrik alan                                     |
| HATA5M                                                                        | Hata parametrik alan                                     |
| HATA4M                                                                        | Hata parametrik alan                                     |
| HATA3M                                                                        | Hata parametrik alan                                     |
| HATA2M                                                                        | Hata parametrik alan                                     |
| HATA1M                                                                        | Hata parametrik alan                                     |
| HATA6T                                                                        | Hata parametrik alan                                     |
| HATA5T                                                                        | Hata parametrik alan                                     |
| HATA4T                                                                        | Hata parametrik alan                                     |
| HATA3T                                                                        | Hata parametrik alan                                     |
| HATA2T                                                                        | Hata parametrik alan                                     |
| HATA1T                                                                        | Hata parametrik alan                                     |
| BOLUM1                                                                        | Hata parametrik alan                                     |
| BOLUM2                                                                        | Hata parametrik alan                                     |
| BOLUM3                                                                        | Hata parametrik alan                                     |
| BOLUM4                                                                        | Hata parametrik alan                                     |
| BOLUM5                                                                        | Hata parametrik alan                                     |
| BOLUM6                                                                        | Hata parametrik alan                                     |
| ORAN6                                                                         | Hata parametrik alan                                     |
| ORAN5                                                                         | Hata parametrik alan                                     |
| ORAN4                                                                         | Hata parametrik alan                                     |
| ORAN3                                                                         | Hata parametrik alan                                     |
| ORAN2                                                                         | Hata parametrik alan                                     |
| ORAN1                                                                         | Hata parametrik alan                                     |
| ONAY                                                                          | Onay                                                     |
| REDNEDENI                                                                     | Ret nedeni                                               |
| ISYERI_KODU                                                                   | iş yeri kodu                                             |
| SISTEM_KODU                                                                   | sistem kodu                                              |
| GELISMERP_ETKINLIK                                                            | Gelişme raporuna ait etkinlik                            |
| HATA_PER1                                                                     | Hata parametrik alan                                     |
| HATA_PER2                                                                     | Hata parametrik alan                                     |
| HATA_PER3                                                                     | Hata parametrik alan                                     |
| HATA_PER4                                                                     | Hata parametrik alan                                     |
| HATA_PER5                                                                     | Hata parametrik alan                                     |
| HATA_PER6                                                                     | Hata parametrik alan                                     |
| HATA_PER_ORAN1                                                                | Hata parametrik alan                                     |
| HATA_PER_ORAN2                                                                | Hata parametrik alan                                     |
| HATA_PER_ORAN3                                                                | Hata parametrik alan                                     |
| HATA_PER_ORAN4                                                                | Hata parametrik alan                                     |
| HATA_PER_ORAN5                                                                | Hata parametrik alan                                     |
| HATA_PER_ORAN6                                                                | Hata parametrik alan                                     |
| REDDEDEN                                                                      | Reddeden sicil                                           |
| PARAM2                                                                        | Parametrik alan                                          |
| PARAM3                                                                        | Parametrik alan                                          |
| PARAM4                                                                        | Parametrik alan                                          |
| PARAM5                                                                        | Parametrik alan                                          |
| SUREC_KODU                                                                    | Süreç kodu                                               |
| MALIYET                                                                       | Maliyet                                                  |
| PARAM6                                                                        | Parametrik alan                                          |
| PARAM7                                                                        | Parametrik alan                                          |
| PARAM9                                                                        | Parametrik alan                                          |
| NPARAM2                                                                       | Parametrik alan                                          |
| NPARAM4                                                                       | Parametrik alan                                          |
| NPARAM5                                                                       | Parametrik alan                                          |
| NPARAM6                                                                       | Parametrik alan                                          |
| NPARAM7                                                                       | Parametrik alan                                          |
| NPARAM8                                                                       | Parametrik alan                                          |
| NPARAM9                                                                       | Parametrik alan                                          |
| NPARAM10                                                                      | Parametrik alan                                          |
| NPARAM2_BIRIM                                                                 | Parametrik alan                                          |
| NPARAM4_BIRIM                                                                 | Parametrik alan                                          |
| NPARAM5_BIRIM                                                                 | Parametrik alan                                          |
| NPARAM6_BIRIM                                                                 | Parametrik alan                                          |
| NPARAM7_BIRIM                                                                 | Parametrik alan                                          |
| NPARAM8_BIRIM                                                                 | Parametrik alan                                          |
| NPARAM9_BIRIM                                                                 | Parametrik alan                                          |
| NPARAM10_BIRIM                                                                | Parametrik alan                                          |
| DPARAM1                                                                       | Parametrik alan                                          |
| DPARAM2                                                                       | Parametrik alan                                          |
| DPARAM3                                                                       | Parametrik alan                                          |
| DPARAM4                                                                       | Parametrik alan                                          |
| DPARAM5                                                                       | Parametrik alan                                          |
| LPARAM1                                                                       | Parametrik alan                                          |
| LPARAM10                                                                      | Parametrik alan                                          |
| LPARAM2                                                                       | Parametrik alan                                          |
| LPARAM3                                                                       | Parametrik alan                                          |
| NPARAM1                                                                       | Parametrik alan                                          |
| NPARAM1_BIRIM                                                                 | Parametrik alan                                          |
| NPARAM3                                                                       | Parametrik alan                                          |
| NPARAM3_BIRIM                                                                 | Parametrik alan                                          |
| PARAM1                                                                        | Parametrik alan                                          |
| PARAM10                                                                       | Parametrik alan                                          |
| PARAM8                                                                        | Parametrik alan                                          |
| PPARAM1                                                                       | Parametrik alan                                          |
| QPARAM1                                                                       | Parametrik alan                                          |
| QPARAM2                                                                       | Parametrik alan                                          |
| PPARAM2                                                                       | Parametrik alan                                          |
| PPARAM3                                                                       | Parametrik alan                                          |
| PPARAM4                                                                       | Parametrik alan                                          |
| PPARAM5                                                                       | Parametrik alan                                          |
| LPARAM4                                                                       | Parametrik alan                                          |
| LPARAM5                                                                       | Parametrik alan                                          |
| GELISME_PARAM1                                                                | Gelişme parametrik alan                                  |
| GELISME_PARAM2                                                                | Gelişme parametrik alan                                  |
| GELISME_PARAM3                                                                | Gelişme parametrik alan                                  |
| GELISME_LPARAM1                                                               | Gelişme parametrik alan                                  |
| GELISME_LPARAM2                                                               | Gelişme parametrik alan                                  |
| GELISME_LPARAM3                                                               | Gelişme parametrik alan                                  |
| GELISME_NPARAM1                                                               | Gelişme parametrik alan                                  |
| GELISME_NPARAM2                                                               | Gelişme parametrik alan                                  |
| GELISME_NPARAM3                                                               | Gelişme parametrik alan                                  |
| GELISME_NPARAM4                                                               | Gelişme parametrik alan                                  |
| GELISME_NPARAM5                                                               | Gelişme parametrik alan                                  |
| GELISME_NPARAM1_BIRIM                                                         | Gelişme parametrik alan                                  |
| GELISME_NPARAM2_BIRIM                                                         | Gelişme parametrik alan                                  |
| GELISME_NPARAM3_BIRIM                                                         | Gelişme parametrik alan                                  |
| GELISME_NPARAM4_BIRIM                                                         | Gelişme parametrik alan                                  |
| GELISME_NPARAM5_BIRIM                                                         | Gelişme parametrik alan                                  |
| ONAY_DURUM                                                                    | Onay durum                                               |
| SONUCRP                                                                       | Sonuç raporu                                             |
| SONUCRPYT                                                                     | Sonuç raporu yazma tarihi                                |
| SONUCRPKYTUSR                                                                 | Sonuç raporunu yazanın sicil numarası                    |
| AKSIYON_DURUM                                                                 | Aksiyon durumu                                           |
| AKSIYON_SONUC_TARIHI                                                          | Aksiyon sonuç tarihi                                     |
| DOF_SONUC_TARIHI                                                              | DOF sonuç tarihi                                         |
| DUZELTICIONLEYICI                                                             | Düzeltici mi önleyici mi durumu                          |
| REF_MODULE                                                                    | Referans modül                                           |
| REF_MODULE_CODE                                                               | Referans modül kodu                                      |
| PARAM11                                                                       | Parametrik alan                                          |
| PARAM12                                                                       | Parametrik alan                                          |
| PARAM13                                                                       | Parametrik alan                                          |
| PARAM14                                                                       | Parametrik alan                                          |
| PARAM15                                                                       | Parametrik alan                                          |
| LPARAM6                                                                       | Parametrik alan                                          |
| LPARAM7                                                                       | Parametrik alan                                          |
| LPARAM8                                                                       | Parametrik alan                                          |
| LPARAM9                                                                       | Parametrik alan                                          |
| ETKINLIK                                                                      | Etkinlik                                                 |
| ETKINLIK_PUANI                                                                | Etkinlik puanı                                           |
| ESKI_DURUM                                                                    | Eski durum                                               |
| ESKI_ONAY_DURUM                                                               | Eski onay durumu                                         |
| SONUC_PARAM1                                                                  | Sonuç parametrik alan                                    |
| SONUC_PARAM2                                                                  | Sonuç parametrik alan                                    |
| SONUC_PARAM3                                                                  | Sonuç parametrik alan                                    |
| SONUC_PARAM4                                                                  | Sonuç parametrik alan                                    |
| SONUC_PARAM5                                                                  | Sonuç parametrik alan                                    |
| SONUC_PARAM6                                                                  | Sonuç parametrik alan                                    |
| SONUC_PARAM7                                                                  | Sonuç parametrik alan                                    |
| SONUC_PARAM8                                                                  | Sonuç parametrik alan                                    |
| SONUC_PARAM9                                                                  | Sonuç parametrik alan                                    |
| SONUC_PARAM10                                                                 | Sonuç parametrik alan                                    |
| SONUC_LPARAM1                                                                 | Sonuç parametrik alan                                    |
| SONUC_LPARAM2                                                                 | Sonuç parametrik alan                                    |
| SONUC_LPARAM3                                                                 | Sonuç parametrik alan                                    |
| SONUC_LPARAM4                                                                 | Sonuç parametrik alan                                    |
| SONUC_LPARAM5                                                                 | Sonuç parametrik alan                                    |
| SONUC_LPARAM6                                                                 | Sonuç parametrik alan                                    |
| SONUC_LPARAM7                                                                 | Sonuç parametrik alan                                    |
| SONUC_LPARAM8                                                                 | Sonuç parametrik alan                                    |
| SONUC_LPARAM9                                                                 | Sonuç parametrik alan                                    |
| SONUC_LPARAM10                                                                | Sonuç parametrik alan                                    |
| SONUC_NPARAM1                                                                 | Sonuç parametrik alan                                    |
| SONUC_NPARAM2                                                                 | Sonuç parametrik alan                                    |
| SONUC_NPARAM3                                                                 | Sonuç parametrik alan                                    |
| SONUC_NPARAM4                                                                 | Sonuç parametrik alan                                    |
| SONUC_NPARAM5                                                                 | Sonuç parametrik alan                                    |
| SONUC_NPARAM1_BIRIM                                                           | Sonuç parametrik alan                                    |
| SONUC_NPARAM2_BIRIM                                                           | Sonuç parametrik alan                                    |
| SONUC_NPARAM3_BIRIM                                                           | Sonuç parametrik alan                                    |
| SONUC_NPARAM4_BIRIM                                                           | Sonuç parametrik alan                                    |
| SONUC_NPARAM5_BIRIM                                                           | Sonuç parametrik alan                                    |
| SONUC_LMPARAM1                                                                | Sonuç parametrik alan                                    |
| SONUC_LMPARAM2                                                                | Sonuç parametrik alan                                    |
| SONUC_LMPARAM3                                                                | Sonuç parametrik alan                                    |
| SONUC_LMPARAM4                                                                | Sonuç parametrik alan                                    |
| SONUC_LMPARAM5                                                                | Sonuç parametrik alan                                    |
| SONUC_LMPARAM6                                                                | Sonuç parametrik alan                                    |
| SONUC_LMPARAM7                                                                | Sonuç parametrik alan                                    |
| SONUC_LMPARAM8                                                                | Sonuç parametrik alan                                    |
| SONUC_LMPARAM9                                                                | Sonuç parametrik alan                                    |
| SONUC_LMPARAM10                                                               | Sonuç parametrik alan                                    |
| KAPATMA_PARAM1                                                                | Kapatma parametrik alan                                  |
| KAPATMA_PARAM2                                                                | Kapatma parametrik alan                                  |
| KAPATMA_PARAM3                                                                | Kapatma parametrik alan                                  |
| KAPATMA_PARAM4                                                                | Kapatma parametrik alan                                  |
| KAPATMA_PARAM5                                                                | Kapatma parametrik alan                                  |
| KAPATMA_PARAM6                                                                | Kapatma parametrik alan                                  |
| KAPATMA_PARAM7                                                                | Kapatma parametrik alan                                  |
| KAPATMA_PARAM8                                                                | Kapatma parametrik alan                                  |
| KAPATMA_PARAM9                                                                | Kapatma parametrik alan                                  |
| KAPATMA_PARAM10                                                               | Kapatma parametrik alan                                  |
| KAPATMA_LPARAM1                                                               | Kapatma parametrik alan                                  |
| KAPATMA_LPARAM2                                                               | Kapatma parametrik alan                                  |
| KAPATMA_LPARAM3                                                               | Kapatma parametrik alan                                  |
| KAPATMA_LPARAM4                                                               | Kapatma parametrik alan                                  |
| KAPATMA_LPARAM5                                                               | Kapatma parametrik alan                                  |
| KAPATMA_LPARAM6                                                               | Kapatma parametrik alan                                  |
| KAPATMA_LPARAM7                                                               | Kapatma parametrik alan                                  |
| KAPATMA_LPARAM8                                                               | Kapatma parametrik alan                                  |
| KAPATMA_LPARAM9                                                               | Kapatma parametrik alan                                  |
| KAPATMA_LPARAM10                                                              | Kapatma parametrik alan                                  |
| KAPATMA_NPARAM1                                                               | Kapatma parametrik alan                                  |
| KAPATMA_NPARAM2                                                               | Kapatma parametrik alan                                  |
| KAPATMA_NPARAM3                                                               | Kapatma parametrik alan                                  |
| KAPATMA_NPARAM4                                                               | Kapatma parametrik alan                                  |
| KAPATMA_NPARAM5                                                               | Kapatma parametrik alan                                  |
| KAPATMA_NPARAM1_BIRIM                                                         | Kapatma parametrik alan                                  |
| KAPATMA_NPARAM2_BIRIM                                                         | Kapatma parametrik alan                                  |
| KAPATMA_NPARAM3_BIRIM                                                         | Kapatma parametrik alan                                  |
| KAPATMA_NPARAM4_BIRIM                                                         | Kapatma parametrik alan                                  |
| KAPATMA_NPARAM5_BIRIM                                                         | Kapatma parametrik alan                                  |
| ONAY_TARIHI                                                                   | Onay tarihi                                              |
| TERMIN_TARIHI                                                                 | Termin tarihi                                            |
| ILK_TERMIN_TARIHI                                                             | İlk termin tarihi                                        |
| OTOMATIK_AKSIYON                                                              | Otomatik aksiyon                                         |
| QPARAM3                                                                       | Sorgu tipli parametrik alan                              |
| QPARAM4                                                                       | Sorgu tipli parametrik alan                              |
| QPARAM5                                                                       | Sorgu tipli parametrik alan                              |
| MALIYET_BIRIM                                                                 | Maliyet birimi                                           |
| PARAM31                                                                       | Parametrik alan                                          |
| PARAM32                                                                       | Parametrik alan                                          |
| PARAM33                                                                       | Parametrik alan                                          |
| PARAM34                                                                       | Parametrik alan                                          |
| PARAM35                                                                       | Parametrik alan                                          |
| LPARAM36                                                                      | Parametrik alan                                          |
| LPARAM37                                                                      | Parametrik alan                                          |
| LPARAM38                                                                      | Parametrik alan                                          |
| LPARAM39                                                                      | Parametrik alan                                          |
| LPARAM40                                                                      | Parametrik alan                                          |
| NPARAM41                                                                      | Parametrik alan                                          |
| NPARAM42                                                                      | Parametrik alan                                          |
| NPARAM43                                                                      | Parametrik alan                                          |
| NPARAM44                                                                      | Parametrik alan                                          |
| NPARAM45                                                                      | Parametrik alan                                          |
| NPARAM46                                                                      | Parametrik alan                                          |
| NPARAM47                                                                      | Parametrik alan                                          |
| NPARAM48                                                                      | Parametrik alan                                          |
| NPARAM49                                                                      | Parametrik alan                                          |
| NPARAM50                                                                      | Parametrik alan                                          |
| NPARAM41_BIRIM                                                                | Parametrik alan                                          |
| NPARAM42_BIRIM                                                                | Parametrik alan                                          |
| NPARAM43_BIRIM                                                                | Parametrik alan                                          |
| NPARAM44_BIRIM                                                                | Parametrik alan                                          |
| NPARAM45_BIRIM                                                                | Parametrik alan                                          |
| NPARAM46_BIRIM                                                                | Parametrik alan                                          |
| NPARAM47_BIRIM                                                                | Parametrik alan                                          |
| NPARAM48_BIRIM                                                                | Parametrik alan                                          |
| NPARAM49_BIRIM                                                                | Parametrik alan                                          |
| NPARAM50_BIRIM                                                                | Parametrik alan                                          |
| DOCPARAM1                                                                     | Parametrik alan                                          |
| RET_TIPI                                                                      | Ret tipi                                                 |
| HATA1_BIRIM                                                                   | Hata parametrik alan                                     |
| HATA2_BIRIM                                                                   | Hata parametrik alan                                     |
| HATA3_BIRIM                                                                   | Hata parametrik alan                                     |
| HATA4_BIRIM                                                                   | Hata parametrik alan                                     |
| HATA5_BIRIM                                                                   | Hata parametrik alan                                     |
| HATA6_BIRIM                                                                   | Hata parametrik alan                                     |
| REF_DKOD                                                                      | Referans DOF kodu                                        |
| GELISME_PARAM4                                                                | Gelişme parametrik alan                                  |
| GELISME_PARAM5                                                                | Gelişme parametrik alan                                  |
| GELISME_PARAM6                                                                | Gelişme parametrik alan                                  |
| GELISME_PARAM7                                                                | Gelişme parametrik alan                                  |
| GELISME_PARAM8                                                                | Gelişme parametrik alan                                  |
| GELISME_PARAM9                                                                | Gelişme parametrik alan                                  |
| GELISME_PARAM10                                                               | Gelişme parametrik alan                                  |
| GELISME_PARAM11                                                               | Gelişme parametrik alan                                  |
| GELISME_PARAM12                                                               | Gelişme parametrik alan                                  |
| GELISME_LPARAM4                                                               | Gelişme parametrik alan                                  |
| GELISME_LPARAM5                                                               | Gelişme parametrik alan                                  |
| GELISME_LPARAM6                                                               | Gelişme parametrik alan                                  |
| GELISME_LPARAM7                                                               | Gelişme parametrik alan                                  |
| GELISME_LPARAM8                                                               | Gelişme parametrik alan                                  |
| GELISME_LPARAM9                                                               | Gelişme parametrik alan                                  |
| GELISME_LPARAM10                                                              | Gelişme parametrik alan                                  |
| GELISME_QPARAM1                                                               | Gelişme parametrik alan                                  |
| GELISME_QPARAM2                                                               | Gelişme parametrik alan                                  |
| GELISME_QPARAM3                                                               | Gelişme parametrik alan                                  |
| GELISME_QPARAM4                                                               | Gelişme parametrik alan                                  |
| GELISME_QPARAM5                                                               | Gelişme parametrik alan                                  |
| SONUC_QPARAM1                                                                 | Sonuç parametrik alan                                    |
| SONUC_QPARAM2                                                                 | Sonuç parametrik alan                                    |
| SONUC_QPARAM3                                                                 | Sonuç parametrik alan                                    |
| SONUC_QPARAM4                                                                 | Sonuç parametrik alan                                    |
| SONUC_QPARAM5                                                                 | Sonuç parametrik alan                                    |
| KAPATMA_QPARAM1                                                               | Kapatma parametrik alan                                  |
| KAPATMA_QPARAM2                                                               | Kapatma parametrik alan                                  |
| KAPATMA_QPARAM3                                                               | Kapatma parametrik alan                                  |
| KAPATMA_QPARAM4                                                               | Kapatma parametrik alan                                  |
| KAPATMA_QPARAM5                                                               | Kapatma parametrik alan                                  |
| GELISME_PPARAM1                                                               | Gelişme parametrik alan                                  |
| GELISME_PPARAM2                                                               | Gelişme parametrik alan                                  |
| GELISME_PPARAM3                                                               | Gelişme parametrik alan                                  |
| GELISME_PPARAM4                                                               | Gelişme parametrik alan                                  |
| GELISME_PPARAM5                                                               | Gelişme parametrik alan                                  |
| GELISME_PPARAM6                                                               | Gelişme parametrik alan                                  |
| GELISME_PPARAM7                                                               | Gelişme parametrik alan                                  |
| GELISME_PPARAM8                                                               | Gelişme parametrik alan                                  |
| GELISME_PPARAM9                                                               | Gelişme parametrik alan                                  |
| GELISME_PPARAM10                                                              | Gelişme parametrik alan                                  |
| SONUC_PPARAM1                                                                 | Sonuç parametrik alan                                    |
| SONUC_PPARAM2                                                                 | Sonuç parametrik alan                                    |
| SONUC_PPARAM3                                                                 | Sonuç parametrik alan                                    |
| SONUC_PPARAM4                                                                 | Sonuç parametrik alan                                    |
| SONUC_PPARAM5                                                                 | Sonuç parametrik alan                                    |
| SONUC_PPARAM6                                                                 | Sonuç parametrik alan                                    |
| SONUC_PPARAM7                                                                 | Sonuç parametrik alan                                    |
| SONUC_PPARAM8                                                                 | Sonuç parametrik alan                                    |
| SONUC_PPARAM9                                                                 | Sonuç parametrik alan                                    |
| SONUC_PPARAM10                                                                | Sonuç parametrik alan                                    |
| KAPATMA_PPARAM1                                                               | Kapatma parametrik alan                                  |
| KAPATMA_PPARAM2                                                               | Kapatma parametrik alan                                  |
| KAPATMA_PPARAM3                                                               | Kapatma parametrik alan                                  |
| KAPATMA_PPARAM4                                                               | Kapatma parametrik alan                                  |
| KAPATMA_PPARAM5                                                               | Kapatma parametrik alan                                  |
| KAPATMA_PPARAM6                                                               | Kapatma parametrik alan                                  |
| KAPATMA_PPARAM7                                                               | Kapatma parametrik alan                                  |
| KAPATMA_PPARAM8                                                               | Kapatma parametrik alan                                  |
| KAPATMA_PPARAM9                                                               | Kapatma parametrik alan                                  |
| KAPATMA_PPARAM10                                                              | Kapatma parametrik alan                                  |
| T2_ACIKLAMA                                                                   | Kaynak açıklaması                                        |
| T2_ICDIS                                                                      | İç veya dış müşteri şikayeti durumu                      |
| T3_ADISOYADI                                                                  | Bildiren adı soyadı                                      |
| T4_ADISOYADI                                                                  | Şikayet oluşturan kişinin adı soyadı                     |
| T5_ADISOYADI                                                                  | Lider adı soyadı                                         |
| T6_DEPARTMAN_ADI                                                              | Sorumlu departman adı                                    |
| T7_URUN_ADI                                                                   | Ürün adı                                                 |
| T8_ADISOYADI                                                                  | Gelişme raporu yazan adı soyadı                          |
| T9_ADISOYADI                                                                  | Kapatan adı soyadı                                       |
| T10_ISYERI_ADI                                                                | İş yeri adı                                              |
| T11_ACIKLAMA                                                                  | Sistem açıklaması                                        |
| T12_ADISOYADI                                                                 | Sonuç raporunu yazanın adı soyadı                        |
| T13_VALUE                                                                     | Düzeltici mi önleyici mi durumunun açıklaması            |
| ALAN1                                                                         | DOF parametrik alan                                      |
| ALAN1_ACK                                                                     | DOF parametrik alan                                      |
| ALAN1_DESC                                                                    | DOF parametrik alan                                      |
| ALAN2                                                                         | DOF parametrik alan                                      |
| ALAN2_ACK                                                                     | DOF parametrik alan                                      |
| ALAN2_DESC                                                                    | DOF parametrik alan                                      |
| ALAN3                                                                         | DOF parametrik alan                                      |
| ALAN4                                                                         | DOF parametrik alan                                      |
| ALAN4_ACK                                                                     | DOF parametrik alan                                      |
| ALAN6                                                                         | DOF parametrik alan                                      |
| ALAN7                                                                         | DOF parametrik alan                                      |
| ALAN7_ACK                                                                     | DOF parametrik alan                                      |
| ALAN8                                                                         | DOF parametrik alan                                      |
| ALAN9                                                                         | DOF parametrik alan                                      |
| ALAN10                                                                        | DOF parametrik alan                                      |
| ALAN10_ACK                                                                    | DOF parametrik alan                                      |
| ALAN10_DESC                                                                   | DOF parametrik alan                                      |
| ALAN11                                                                        | DOF parametrik alan                                      |
| MTB                                                                           | Müşteri adı veya departman adı                           |
| DURUM_ACK                                                                     | Durum açıklaması                                         |
| DOF_ACAN_DEPT                                                                 | DOF açan departman                                       |
| ISLEM_SURESI                                                                  | İşlem süresi                                             |
| DUZELTICIONLEYICI_ACK                                                         | Düzeltici mi önleyici mi durumunun açıklaması            |
| EKIP                                                                          | Ekip bilgisi                                             |
| KOK_NEDENLER                                                                  | Kök nedenler                                             |
| KOKNEDEN_DETAYI                                                               | Kök neden detayı                                         |
| MNPARAM                                                                       | Parametrik alan                                          |
| URUN_TIPI                                                                     | Ürün tipi                                                |
| DENETIM_KODU                                                                  | Denetim kodu                                             |
| DENETIM_TANIMI                                                                | Denetim tanımı                                           |
| DENETIM_TIPI                                                                  | Denetim tipi                                             |
| UYG_KAT1                                                                      | Uygunsuzluk kategorisi                                   |
| UYG_KAT2                                                                      | Uygunsuzluk kategorisi                                   |
| UYG_KAT3                                                                      | Uygunsuzluk kategorisi                                   |
| UYG_KAT4                                                                      | Uygunsuzluk kategorisi                                   |
| UYG_KAT5                                                                      | Uygunsuzluk kategorisi                                   |
| UYG_ANA_KAT_KOD                                                               | Uygunsuzluk kategorisi ana kategori kodu                 |
| UYG_ANA_KAT                                                                   | Uygunsuzluk kategorisi ana kategori tanımı               |
| UYG_ALT_KAT_KOD                                                               | Uygunsuzluk kategorisi alt kategori kodu                 |
| UYG_ALT_KAT                                                                   | Uygunsuzluk alt kategori tanımı                          |
| UYG_KODLAR                                                                    | Uygunsuzluk kodları                                      |
| GELISME_LPARAM1_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_LPARAM10_VALUE                                                        | Gelişme parametrik alan                                  |
| GELISME_LPARAM2_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_LPARAM3_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_LPARAM4_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_LPARAM5_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_LPARAM6_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_LPARAM7_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_LPARAM8_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_LPARAM9_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_NPARAM1_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_NPARAM2_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_NPARAM3_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_NPARAM4_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_NPARAM5_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_PPARAM1_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_PPARAM10_VALUE                                                        | Gelişme parametrik alan                                  |
| GELISME_PPARAM2_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_PPARAM3_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_PPARAM4_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_PPARAM5_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_PPARAM6_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_PPARAM7_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_PPARAM8_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_PPARAM9_VALUE                                                         | Gelişme parametrik alan                                  |
| KAPATMA_LPARAM1_VALUE                                                         | Gelişme parametrik alan                                  |
| LPARAM1_VALUE                                                                 | Parametrik alan                                          |
| LPARAM10_VALUE                                                                | Parametrik alan                                          |
| LPARAM2_VALUE                                                                 | Parametrik alan                                          |
| LPARAM3_VALUE                                                                 | Parametrik alan                                          |
| NPARAM1_VALUE                                                                 | Parametrik alan                                          |
| NPARAM3_VALUE                                                                 | Parametrik alan                                          |
| PPARAM1_VALUE                                                                 | Parametrik alan                                          |
| SONUC_LMPARAM1_VALUE                                                          | Sonuç parametrik alan                                    |
| SONUC_LMPARAM10_VALUE                                                         | Sonuç parametrik alan                                    |
| SONUC_LMPARAM2_VALUE                                                          | Sonuç parametrik alan                                    |
| SONUC_LMPARAM3_VALUE                                                          | Sonuç parametrik alan                                    |
| SONUC_LMPARAM4_VALUE                                                          | Sonuç parametrik alan                                    |
| SONUC_LMPARAM5_VALUE                                                          | Sonuç parametrik alan                                    |
| SONUC_LMPARAM6_VALUE                                                          | Sonuç parametrik alan                                    |
| SONUC_LMPARAM7_VALUE                                                          | Sonuç parametrik alan                                    |
| SONUC_LMPARAM8_VALUE                                                          | Sonuç parametrik alan                                    |
| SONUC_LMPARAM9_VALUE                                                          | Sonuç parametrik alan                                    |
| SONUC_LPARAM1_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_LPARAM10_VALUE                                                          | Sonuç parametrik alan                                    |
| SONUC_LPARAM2_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_LPARAM3_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_LPARAM4_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_LPARAM5_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_LPARAM6_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_LPARAM7_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_LPARAM8_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_LPARAM9_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_NPARAM1_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_NPARAM2_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_NPARAM3_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_NPARAM4_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_NPARAM5_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_PPARAM1_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_PPARAM10_VALUE                                                          | Sonuç parametrik alan                                    |
| SONUC_PPARAM2_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_PPARAM3_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_PPARAM4_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_PPARAM5_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_PPARAM6_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_PPARAM7_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_PPARAM8_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_PPARAM9_VALUE                                                           | Sonuç parametrik alan                                    |
| YORUM                                                                         | Yorum                                                    |
| ACIK_STATUSUNE_DONDURME                                                       | Açık statüsü bilgisi(Adı soyadı-tarih-açıklama)          |
| SUREC_ADI                                                                     | Sürec adı                                                |
| SUREC                                                                         | Süreç kodu - süreç adı                                   |
| KAPATMAONAY_0                                                                 | Kapatma onaycıları ve tarihler(10' a kadar gidiyor)      |
| ACMAONAY_0                                                                    | Açma onaycıları ve tarihler(10' a kadar gidiyor)         |
| GELISMEONAY_0                                                                 | Gelişme onaycıları ve tarihler(10' a kadar gidiyor)      |
| KAPATMAONAYTAR_0                                                              | Kapatma onay tarihleri(10' a kadar gidiyor)              |
| ACMAONAYTAR_0                                                                 | Açma onay tarihleri(10' a kadar gidiyor)                 |
| GELISMEONAYTAR_0                                                              | Gelişme onay tarihleri(10' a kadar gidiyor)              |
| ACMASURE_0                                                                    | Açma onay süresi(10' a kadar gidiyor)                    |
| KAPATMASURE_0                                                                 | Kapatma onay süresi(10' a kadar gidiyor)                 |
| GELISMESURE_0                                                                 | Gelişme onay süresi(10' a kadar gidiyor)                 |
| AKS_PLANONAY_TAR_0                                                            | Aksiyon plan onaycıları ve tarihler(3' e kadar gidiyor)  |
| AKS_PLANONAY_0                                                                | Aksiyon plan onay tarihleri(3' e kadar gidiyor)          |
| TOPLAM_ACMASURE                                                               | Toplam açma onay süresi                                  |
| TOPLAM_KAPATMASURE                                                            | Toplam Kapatma onay süresi                               |
| AKS_PLANONAY_TAR                                                              | Aksiyon plan onay tarihi                                 |
| RET_NEDENI                                                                    | Ret nedeni                                               |
| RET_TARIHI                                                                    | Ret tarihi                                               |
| IZLEME                                                                        | İzleme                                                   |
| UPARAM                                                                        | Parametrik alan                                          |
| ACAN_DEPT                                                                     | Şikayet açan departman adı                               |
| T12_SADI                                                                      | Süreç adı                                                |
| IZLEME1                                                                       | İzleme bilgisi(10' a kadar gidiyor)                      |
| BILGILENDIRME                                                                 | Bilgilendirme                                            |

## **1.7. DÖF Özet Raporu Replacement (Kısa Kodlar) Tag Tablosu**

Düzeltici ve Önleyici Modülünde kullanılan DÖF Özet Raporu taglerin listesi aşağıdaki tabloda yer almaktadır.

| **Kısaltma (Kısalmalar tag şeklinde \< \> isaretleri arasına yazılacaktır.)** | **Açıklama**                                                          |
|-------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| DKOD                                                                          | DOF kodu                                                              |
| KAYNAK                                                                        | DOF kaynağı                                                           |
| SISTEMEKT                                                                     | Sisteme ekleme tarihi                                                 |
| MREF                                                                          | Denetimden açılan Müşteri şikayetleri için referans kodu              |
| BILDIREN                                                                      | Bildiren kişi                                                         |
| BILDIRIMT                                                                     | Bildirim Tarihi                                                       |
| BILDIRIMS                                                                     | Bildirim şekli                                                        |
| SIKAYETG                                                                      | Şikayet oluşturan sicil no                                            |
| LIDER                                                                         | Lider sicil numarası                                                  |
| SORUMLUD                                                                      | Sorumlu departman kodu                                                |
| UYGT                                                                          | DOF Uygunsuzluk tanımı                                                |
| UYGDT                                                                         | DOF Uygunsuzluk detayı                                                |
| URUN                                                                          | Ürün kodu                                                             |
| GELRAPY                                                                       | Planlanan gelisme raporu tarihi                                       |
| DURUM                                                                         | Durum bilgisi                                                         |
| GELISMEYT                                                                     | Gelişme raporu yazma tarihi                                           |
| GELISMERP                                                                     | Gelişme raporu                                                        |
| SONRAPY                                                                       | Planlanan sonuç raporu tarihi                                         |
| GELKYTUSR                                                                     | Gelişme raporu yazan sicili                                           |
| NOTLAR                                                                        | Notlar                                                                |
| KAPATAN                                                                       | Kapatan kişinin sicil numarası                                        |
| KAPATMAT                                                                      | Kapatma tarihi                                                        |
| MKOD                                                                          | Müşteri kodu                                                          |
| YETERLILIK                                                                    | Yeterlilik                                                            |
| HATA6M                                                                        | Hata parametrik alan                                                  |
| HATA5M                                                                        | Hata parametrik alan                                                  |
| HATA4M                                                                        | Hata parametrik alan                                                  |
| HATA3M                                                                        | Hata parametrik alan                                                  |
| HATA2M                                                                        | Hata parametrik alan                                                  |
| HATA1M                                                                        | Hata parametrik alan                                                  |
| HATA6T                                                                        | Hata parametrik alan                                                  |
| HATA5T                                                                        | Hata parametrik alan                                                  |
| HATA4T                                                                        | Hata parametrik alan                                                  |
| HATA3T                                                                        | Hata parametrik alan                                                  |
| HATA2T                                                                        | Hata parametrik alan                                                  |
| HATA1T                                                                        | Hata parametrik alan                                                  |
| BOLUM1                                                                        | Hata parametrik alan                                                  |
| BOLUM2                                                                        | Hata parametrik alan                                                  |
| BOLUM3                                                                        | Hata parametrik alan                                                  |
| BOLUM4                                                                        | Hata parametrik alan                                                  |
| BOLUM5                                                                        | Hata parametrik alan                                                  |
| BOLUM6                                                                        | Hata parametrik alan                                                  |
| ORAN6                                                                         | Hata parametrik alan                                                  |
| ORAN5                                                                         | Hata parametrik alan                                                  |
| ORAN4                                                                         | Hata parametrik alan                                                  |
| ORAN3                                                                         | Hata parametrik alan                                                  |
| ORAN2                                                                         | Hata parametrik alan                                                  |
| ORAN1                                                                         | Hata parametrik alan                                                  |
| ONAY                                                                          | Onay                                                                  |
| REDNEDENI                                                                     | Ret nedeni                                                            |
| ISYERI_KODU                                                                   | iş yeri kodu                                                          |
| SISTEM_KODU                                                                   | sistem kodu                                                           |
| GELISMERP_ETKINLIK                                                            | Gelişme raporuna ait etkinlik                                         |
| HATA_PER1                                                                     | Hata parametrik alan                                                  |
| HATA_PER2                                                                     | Hata parametrik alan                                                  |
| HATA_PER3                                                                     | Hata parametrik alan                                                  |
| HATA_PER4                                                                     | Hata parametrik alan                                                  |
| HATA_PER5                                                                     | Hata parametrik alan                                                  |
| HATA_PER6                                                                     | Hata parametrik alan                                                  |
| HATA_PER_ORAN1                                                                | Hata parametrik alan                                                  |
| HATA_PER_ORAN2                                                                | Hata parametrik alan                                                  |
| HATA_PER_ORAN3                                                                | Hata parametrik alan                                                  |
| HATA_PER_ORAN4                                                                | Hata parametrik alan                                                  |
| HATA_PER_ORAN5                                                                | Hata parametrik alan                                                  |
| HATA_PER_ORAN6                                                                | Hata parametrik alan                                                  |
| REDDEDEN                                                                      | Reddeden sicil                                                        |
| PARAM2                                                                        | Parametrik alan                                                       |
| PARAM3                                                                        | Parametrik alan                                                       |
| PARAM4                                                                        | Parametrik alan                                                       |
| PARAM5                                                                        | Parametrik alan                                                       |
| SUREC_KODU                                                                    | Süreç kodu                                                            |
| MALIYET                                                                       | Maliyet                                                               |
| PARAM6                                                                        | Parametrik alan                                                       |
| PARAM7                                                                        | Parametrik alan                                                       |
| PARAM9                                                                        | Parametrik alan                                                       |
| NPARAM2                                                                       | Parametrik alan                                                       |
| NPARAM4                                                                       | Parametrik alan                                                       |
| NPARAM5                                                                       | Parametrik alan                                                       |
| NPARAM6                                                                       | Parametrik alan                                                       |
| NPARAM7                                                                       | Parametrik alan                                                       |
| NPARAM8                                                                       | Parametrik alan                                                       |
| NPARAM9                                                                       | Parametrik alan                                                       |
| NPARAM10                                                                      | Parametrik alan                                                       |
| NPARAM2_BIRIM                                                                 | Parametrik alan                                                       |
| NPARAM4_BIRIM                                                                 | Parametrik alan                                                       |
| NPARAM5_BIRIM                                                                 | Parametrik alan                                                       |
| NPARAM6_BIRIM                                                                 | Parametrik alan                                                       |
| NPARAM7_BIRIM                                                                 | Parametrik alan                                                       |
| NPARAM8_BIRIM                                                                 | Parametrik alan                                                       |
| NPARAM9_BIRIM                                                                 | Parametrik alan                                                       |
| NPARAM10_BIRIM                                                                | Parametrik alan                                                       |
| DPARAM1                                                                       | Parametrik alan                                                       |
| LPARAM1                                                                       | Parametrik alan                                                       |
| LPARAM10                                                                      | Parametrik alan                                                       |
| LPARAM2                                                                       | Parametrik alan                                                       |
| LPARAM3                                                                       | Parametrik alan                                                       |
| NPARAM1                                                                       | Parametrik alan                                                       |
| NPARAM1_BIRIM                                                                 | Parametrik alan                                                       |
| NPARAM3                                                                       | Parametrik alan                                                       |
| NPARAM3_BIRIM                                                                 | Parametrik alan                                                       |
| PARAM1                                                                        | Parametrik alan                                                       |
| PARAM10                                                                       | Parametrik alan                                                       |
| PARAM8                                                                        | Parametrik alan                                                       |
| PPARAM1                                                                       | Parametrik alan                                                       |
| QPARAM1                                                                       | Parametrik alan                                                       |
| QPARAM2                                                                       | Parametrik alan                                                       |
| DPARAM2                                                                       | Parametrik alan                                                       |
| DPARAM3                                                                       | Parametrik alan                                                       |
| DPARAM4                                                                       | Parametrik alan                                                       |
| DPARAM5                                                                       | Parametrik alan                                                       |
| PPARAM2                                                                       | Parametrik alan                                                       |
| PPARAM3                                                                       | Parametrik alan                                                       |
| PPARAM4                                                                       | Parametrik alan                                                       |
| PPARAM5                                                                       | Parametrik alan                                                       |
| LPARAM4                                                                       | Parametrik alan                                                       |
| DPARAM1                                                                       | Parametrik alan                                                       |
| LPARAM1                                                                       | Parametrik alan                                                       |
| LPARAM10                                                                      | Parametrik alan                                                       |
| LPARAM2                                                                       | Parametrik alan                                                       |
| LPARAM3                                                                       | Parametrik alan                                                       |
| LPARAM5                                                                       | Parametrik alan                                                       |
| NPARAM1                                                                       | Parametrik alan                                                       |
| NPARAM1_BIRIM                                                                 | Parametrik alan                                                       |
| NPARAM3                                                                       | Parametrik alan                                                       |
| NPARAM3_BIRIM                                                                 | Parametrik alan                                                       |
| PARAM1                                                                        | Parametrik alan                                                       |
| PARAM10                                                                       | Parametrik alan                                                       |
| PARAM8                                                                        | Parametrik alan                                                       |
| PPARAM1                                                                       | Parametrik alan                                                       |
| QPARAM1                                                                       | Parametrik alan                                                       |
| QPARAM2                                                                       | Parametrik alan                                                       |
| GELISME_PARAM1                                                                | Gelişme parametrik alan                                               |
| GELISME_PARAM2                                                                | Gelişme parametrik alan                                               |
| GELISME_PARAM3                                                                | Gelişme parametrik alan                                               |
| GELISME_LPARAM1                                                               | Gelişme parametrik alan                                               |
| GELISME_LPARAM2                                                               | Gelişme parametrik alan                                               |
| GELISME_LPARAM3                                                               | Gelişme parametrik alan                                               |
| GELISME_NPARAM1                                                               | Gelişme parametrik alan                                               |
| GELISME_NPARAM2                                                               | Gelişme parametrik alan                                               |
| GELISME_NPARAM3                                                               | Gelişme parametrik alan                                               |
| GELISME_NPARAM4                                                               | Gelişme parametrik alan                                               |
| GELISME_NPARAM5                                                               | Gelişme parametrik alan                                               |
| GELISME_NPARAM1_BIRIM                                                         | Gelişme parametrik alan                                               |
| GELISME_NPARAM2_BIRIM                                                         | Gelişme parametrik alan                                               |
| GELISME_NPARAM3_BIRIM                                                         | Gelişme parametrik alan                                               |
| GELISME_NPARAM4_BIRIM                                                         | Gelişme parametrik alan                                               |
| GELISME_NPARAM5_BIRIM                                                         | Gelişme parametrik alan                                               |
| ONAY_DURUM                                                                    | Onay durumu                                                           |
| SONUCRP                                                                       | Sonuç raporu                                                          |
| SONUCRPYT                                                                     | Sonuç raporu yazma tarihi                                             |
| SONUCRPKYTUSR                                                                 | Sonuç raporunu yazanın sicil numarası                                 |
| AKSIYON_DURUM                                                                 | Aksiyon durumu                                                        |
| AKSIYON_SONUC_TARIHI                                                          | Aksiyon sonuç tarihi                                                  |
| DOF_SONUC_TARIHI                                                              | DOF sonuç tarihi                                                      |
| DUZELTICIONLEYICI                                                             | Düzeltici mi önleyici mi durumu                                       |
| REF_MODULE                                                                    | Referans modül                                                        |
| REF_MODULE_CODE                                                               | Referans modül kodu                                                   |
| PARAM11                                                                       | Parametrik alan                                                       |
| PARAM12                                                                       | Parametrik alan                                                       |
| PARAM13                                                                       | Parametrik alan                                                       |
| PARAM14                                                                       | Parametrik alan                                                       |
| PARAM15                                                                       | Parametrik alan                                                       |
| LPARAM6                                                                       | Parametrik alan                                                       |
| LPARAM7                                                                       | Parametrik alan                                                       |
| LPARAM8                                                                       | Parametrik alan                                                       |
| LPARAM9                                                                       | Parametrik alan                                                       |
| ETKINLIK                                                                      | Etkinlik                                                              |
| ETKINLIK_PUANI                                                                | Etkinlik puanı                                                        |
| ESKI_DURUM                                                                    | Eski durum                                                            |
| ESKI_ONAY_DURUM                                                               | Eski onay durumu                                                      |
| SONUC_PARAM1                                                                  | Sonuç parametrik alan                                                 |
| SONUC_PARAM2                                                                  | Sonuç parametrik alan                                                 |
| SONUC_PARAM3                                                                  | Sonuç parametrik alan                                                 |
| SONUC_PARAM4                                                                  | Sonuç parametrik alan                                                 |
| SONUC_PARAM5                                                                  | Sonuç parametrik alan                                                 |
| SONUC_PARAM6                                                                  | Sonuç parametrik alan                                                 |
| SONUC_PARAM7                                                                  | Sonuç parametrik alan                                                 |
| SONUC_PARAM8                                                                  | Sonuç parametrik alan                                                 |
| SONUC_PARAM9                                                                  | Sonuç parametrik alan                                                 |
| SONUC_PARAM10                                                                 | Sonuç parametrik alan                                                 |
| SONUC_LPARAM1                                                                 | Sonuç parametrik alan                                                 |
| SONUC_LPARAM2                                                                 | Sonuç parametrik alan                                                 |
| SONUC_LPARAM3                                                                 | Sonuç parametrik alan                                                 |
| SONUC_LPARAM4                                                                 | Sonuç parametrik alan                                                 |
| SONUC_LPARAM5                                                                 | Sonuç parametrik alan                                                 |
| SONUC_LPARAM6                                                                 | Sonuç parametrik alan                                                 |
| SONUC_LPARAM7                                                                 | Sonuç parametrik alan                                                 |
| SONUC_LPARAM8                                                                 | Sonuç parametrik alan                                                 |
| SONUC_LPARAM9                                                                 | Sonuç parametrik alan                                                 |
| SONUC_LPARAM10                                                                | Sonuç parametrik alan                                                 |
| SONUC_NPARAM1                                                                 | Sonuç parametrik alan                                                 |
| SONUC_NPARAM2                                                                 | Sonuç parametrik alan                                                 |
| SONUC_NPARAM3                                                                 | Sonuç parametrik alan                                                 |
| SONUC_NPARAM4                                                                 | Sonuç parametrik alan                                                 |
| SONUC_NPARAM5                                                                 | Sonuç parametrik alan                                                 |
| SONUC_NPARAM1_BIRIM                                                           | Sonuç parametrik alan                                                 |
| SONUC_NPARAM2_BIRIM                                                           | Sonuç parametrik alan                                                 |
| SONUC_NPARAM3_BIRIM                                                           | Sonuç parametrik alan                                                 |
| SONUC_NPARAM4_BIRIM                                                           | Sonuç parametrik alan                                                 |
| SONUC_NPARAM5_BIRIM                                                           | Sonuç parametrik alan                                                 |
| SONUC_LMPARAM1                                                                | Sonuç parametrik alan                                                 |
| SONUC_LMPARAM2                                                                | Sonuç parametrik alan                                                 |
| SONUC_LMPARAM3                                                                | Sonuç parametrik alan                                                 |
| SONUC_LMPARAM4                                                                | Sonuç parametrik alan                                                 |
| SONUC_LMPARAM5                                                                | Sonuç parametrik alan                                                 |
| SONUC_LMPARAM6                                                                | Sonuç parametrik alan                                                 |
| SONUC_LMPARAM7                                                                | Sonuç parametrik alan                                                 |
| SONUC_LMPARAM8                                                                | Sonuç parametrik alan                                                 |
| SONUC_LMPARAM9                                                                | Sonuç parametrik alan                                                 |
| SONUC_LMPARAM10                                                               | Sonuç parametrik alan                                                 |
| KAPATMA_PARAM1                                                                | Kapatma parametrik alan                                               |
| KAPATMA_PARAM2                                                                | Kapatma parametrik alan                                               |
| KAPATMA_PARAM3                                                                | Kapatma parametrik alan                                               |
| KAPATMA_PARAM4                                                                | Kapatma parametrik alan                                               |
| KAPATMA_PARAM5                                                                | Kapatma parametrik alan                                               |
| KAPATMA_PARAM6                                                                | Kapatma parametrik alan                                               |
| KAPATMA_PARAM7                                                                | Kapatma parametrik alan                                               |
| KAPATMA_PARAM8                                                                | Kapatma parametrik alan                                               |
| KAPATMA_PARAM9                                                                | Kapatma parametrik alan                                               |
| KAPATMA_PARAM10                                                               | Kapatma parametrik alan                                               |
| KAPATMA_LPARAM1                                                               | Kapatma parametrik alan                                               |
| KAPATMA_LPARAM2                                                               | Kapatma parametrik alan                                               |
| KAPATMA_LPARAM3                                                               | Kapatma parametrik alan                                               |
| KAPATMA_LPARAM4                                                               | Kapatma parametrik alan                                               |
| KAPATMA_LPARAM5                                                               | Kapatma parametrik alan                                               |
| KAPATMA_LPARAM6                                                               | Kapatma parametrik alan                                               |
| KAPATMA_LPARAM7                                                               | Kapatma parametrik alan                                               |
| KAPATMA_LPARAM8                                                               | Kapatma parametrik alan                                               |
| KAPATMA_LPARAM9                                                               | Kapatma parametrik alan                                               |
| KAPATMA_LPARAM10                                                              | Kapatma parametrik alan                                               |
| KAPATMA_NPARAM1                                                               | Kapatma parametrik alan                                               |
| KAPATMA_NPARAM2                                                               | Kapatma parametrik alan                                               |
| KAPATMA_NPARAM3                                                               | Kapatma parametrik alan                                               |
| KAPATMA_NPARAM4                                                               | Kapatma parametrik alan                                               |
| KAPATMA_NPARAM5                                                               | Kapatma parametrik alan                                               |
| KAPATMA_NPARAM1_BIRIM                                                         | Kapatma parametrik alan                                               |
| KAPATMA_NPARAM2_BIRIM                                                         | Kapatma parametrik alan                                               |
| KAPATMA_NPARAM3_BIRIM                                                         | Kapatma parametrik alan                                               |
| KAPATMA_NPARAM4_BIRIM                                                         | Kapatma parametrik alan                                               |
| KAPATMA_NPARAM5_BIRIM                                                         | Kapatma parametrik alan                                               |
| ONAY_TARIHI                                                                   | Onay tarihi                                                           |
| TERMIN_TARIHI                                                                 | Termin tarihi                                                         |
| ILK_TERMIN_TARIHI                                                             | İlk termin tarihi                                                     |
| OTOMATIK_AKSIYON                                                              | Otomatik aksiyon                                                      |
| QPARAM3                                                                       | Sorgu tipli parametrik alan                                           |
| QPARAM4                                                                       | Sorgu tipli parametrik alan                                           |
| QPARAM5                                                                       | Sorgu tipli parametrik alan                                           |
| MALIYET_BIRIM                                                                 | Maliyet birimi                                                        |
| PARAM31                                                                       | Parametrik alan                                                       |
| PARAM32                                                                       | Parametrik alan                                                       |
| PARAM33                                                                       | Parametrik alan                                                       |
| PARAM34                                                                       | Parametrik alan                                                       |
| PARAM35                                                                       | Parametrik alan                                                       |
| LPARAM36                                                                      | Parametrik alan                                                       |
| LPARAM37                                                                      | Parametrik alan                                                       |
| LPARAM38                                                                      | Parametrik alan                                                       |
| LPARAM39                                                                      | Parametrik alan                                                       |
| LPARAM40                                                                      | Parametrik alan                                                       |
| NPARAM41                                                                      | Parametrik alan                                                       |
| NPARAM42                                                                      | Parametrik alan                                                       |
| NPARAM43                                                                      | Parametrik alan                                                       |
| NPARAM44                                                                      | Parametrik alan                                                       |
| NPARAM45                                                                      | Parametrik alan                                                       |
| NPARAM46                                                                      | Parametrik alan                                                       |
| NPARAM47                                                                      | Parametrik alan                                                       |
| NPARAM48                                                                      | Parametrik alan                                                       |
| NPARAM49                                                                      | Parametrik alan                                                       |
| NPARAM50                                                                      | Parametrik alan                                                       |
| NPARAM41_BIRIM                                                                | Parametrik alan                                                       |
| NPARAM42_BIRIM                                                                | Parametrik alan                                                       |
| NPARAM43_BIRIM                                                                | Parametrik alan                                                       |
| NPARAM44_BIRIM                                                                | Parametrik alan                                                       |
| NPARAM45_BIRIM                                                                | Parametrik alan                                                       |
| NPARAM46_BIRIM                                                                | Parametrik alan                                                       |
| NPARAM47_BIRIM                                                                | Parametrik alan                                                       |
| NPARAM48_BIRIM                                                                | Parametrik alan                                                       |
| NPARAM49_BIRIM                                                                | Parametrik alan                                                       |
| NPARAM50_BIRIM                                                                | Parametrik alan                                                       |
| DOCPARAM1                                                                     | Parametrik alan                                                       |
| RET_TIPI                                                                      | Ret tipi                                                              |
| HATA1_BIRIM                                                                   | Hata parametrik alan                                                  |
| HATA2_BIRIM                                                                   | Hata parametrik alan                                                  |
| HATA3_BIRIM                                                                   | Hata parametrik alan                                                  |
| HATA4_BIRIM                                                                   | Hata parametrik alan                                                  |
| HATA5_BIRIM                                                                   | Hata parametrik alan                                                  |
| HATA6_BIRIM                                                                   | Hata parametrik alan                                                  |
| REF_DKOD                                                                      | Referans DOF kodu                                                     |
| GELISME_PARAM4                                                                | Gelişme parametrik alan                                               |
| GELISME_PARAM5                                                                | Gelişme parametrik alan                                               |
| GELISME_PARAM6                                                                | Gelişme parametrik alan                                               |
| GELISME_PARAM7                                                                | Gelişme parametrik alan                                               |
| GELISME_PARAM8                                                                | Gelişme parametrik alan                                               |
| GELISME_PARAM9                                                                | Gelişme parametrik alan                                               |
| GELISME_PARAM10                                                               | Gelişme parametrik alan                                               |
| GELISME_PARAM11                                                               | Gelişme parametrik alan                                               |
| GELISME_PARAM12                                                               | Gelişme parametrik alan                                               |
| GELISME_LPARAM4                                                               | Gelişme parametrik alan                                               |
| GELISME_LPARAM5                                                               | Gelişme parametrik alan                                               |
| GELISME_LPARAM6                                                               | Gelişme parametrik alan                                               |
| GELISME_LPARAM7                                                               | Gelişme parametrik alan                                               |
| GELISME_LPARAM8                                                               | Gelişme parametrik alan                                               |
| GELISME_LPARAM9                                                               | Gelişme parametrik alan                                               |
| GELISME_LPARAM10                                                              | Gelişme parametrik alan                                               |
| GELISME_QPARAM1                                                               | Gelişme parametrik alan                                               |
| GELISME_QPARAM2                                                               | Gelişme parametrik alan                                               |
| GELISME_QPARAM3                                                               | Gelişme parametrik alan                                               |
| GELISME_QPARAM4                                                               | Gelişme parametrik alan                                               |
| GELISME_QPARAM5                                                               | Gelişme parametrik alan                                               |
| SONUC_QPARAM1                                                                 | Sonuç parametrik alan                                                 |
| SONUC_QPARAM2                                                                 | Sonuç parametrik alan                                                 |
| SONUC_QPARAM3                                                                 | Sonuç parametrik alan                                                 |
| SONUC_QPARAM4                                                                 | Sonuç parametrik alan                                                 |
| SONUC_QPARAM5                                                                 | Sonuç parametrik alan                                                 |
| KAPATMA_QPARAM1                                                               | Kapatma parametrik alan                                               |
| KAPATMA_QPARAM2                                                               | Kapatma parametrik alan                                               |
| KAPATMA_QPARAM3                                                               | Kapatma parametrik alan                                               |
| KAPATMA_QPARAM4                                                               | Kapatma parametrik alan                                               |
| KAPATMA_QPARAM5                                                               | Kapatma parametrik alan                                               |
| GELISME_PPARAM1                                                               | Gelişme parametrik alan                                               |
| GELISME_PPARAM2                                                               | Gelişme parametrik alan                                               |
| GELISME_PPARAM3                                                               | Gelişme parametrik alan                                               |
| GELISME_PPARAM4                                                               | Gelişme parametrik alan                                               |
| GELISME_PPARAM5                                                               | Gelişme parametrik alan                                               |
| GELISME_PPARAM6                                                               | Gelişme parametrik alan                                               |
| GELISME_PPARAM7                                                               | Gelişme parametrik alan                                               |
| GELISME_PPARAM8                                                               | Gelişme parametrik alan                                               |
| GELISME_PPARAM9                                                               | Gelişme parametrik alan                                               |
| GELISME_PPARAM10                                                              | Gelişme parametrik alan                                               |
| SONUC_PPARAM1                                                                 | Sonuç parametrik alan                                                 |
| SONUC_PPARAM2                                                                 | Sonuç parametrik alan                                                 |
| SONUC_PPARAM3                                                                 | Sonuç parametrik alan                                                 |
| SONUC_PPARAM4                                                                 | Sonuç parametrik alan                                                 |
| SONUC_PPARAM5                                                                 | Sonuç parametrik alan                                                 |
| SONUC_PPARAM6                                                                 | Sonuç parametrik alan                                                 |
| SONUC_PPARAM7                                                                 | Sonuç parametrik alan                                                 |
| SONUC_PPARAM8                                                                 | Sonuç parametrik alan                                                 |
| SONUC_PPARAM9                                                                 | Sonuç parametrik alan                                                 |
| SONUC_PPARAM10                                                                | Sonuç parametrik alan                                                 |
| KAPATMA_PPARAM1                                                               | Kapatma parametrik alan                                               |
| KAPATMA_PPARAM2                                                               | Kapatma parametrik alan                                               |
| KAPATMA_PPARAM3                                                               | Kapatma parametrik alan                                               |
| KAPATMA_PPARAM4                                                               | Kapatma parametrik alan                                               |
| KAPATMA_PPARAM5                                                               | Kapatma parametrik alan                                               |
| KAPATMA_PPARAM6                                                               | Kapatma parametrik alan                                               |
| KAPATMA_PPARAM7                                                               | Kapatma parametrik alan                                               |
| KAPATMA_PPARAM8                                                               | Kapatma parametrik alan                                               |
| KAPATMA_PPARAM9                                                               | Kapatma parametrik alan                                               |
| KAPATMA_PPARAM10                                                              | Kapatma parametrik alan                                               |
| T2_ACIKLAMA                                                                   | Kaynak açıklaması                                                     |
| T2_ICDIS                                                                      | İç veya dış müşteri şikayeti durumu                                   |
| T3_ADISOYADI                                                                  | Bildiren adı soyadı                                                   |
| T4_ADISOYADI                                                                  | Şikayet oluşturan kişinin adı soyadı                                  |
| T5_ADISOYADI                                                                  | Lider adı soyadı                                                      |
| T6_DEPARTMAN_ADI                                                              | Sorumlu departman adı                                                 |
| T7_URUN_ADI                                                                   | Ürün adı                                                              |
| T8_ADISOYADI                                                                  | Gelişme raporu yazan adı soyadı                                       |
| T9_ADISOYADI                                                                  | Kapatan adı soyadı                                                    |
| T10_ISYERI_ADI                                                                | İş yeri adı                                                           |
| T11_ACIKLAMA                                                                  | Sistem açıklaması                                                     |
| T12_ADISOYADI                                                                 | Sonuç raporunu yazanın adı soyadı                                     |
| T13_VALUE                                                                     | Düzeltici mi önleyici mi durumunun açıklaması                         |
| ALAN1                                                                         | DOF parametrik alan                                                   |
| ALAN1_ACK                                                                     | DOF parametrik alan                                                   |
| ALAN1_DESC                                                                    | DOF parametrik alan                                                   |
| ALAN2                                                                         | DOF parametrik alan                                                   |
| ALAN2_ACK                                                                     | DOF parametrik alan                                                   |
| ALAN2_DESC                                                                    | DOF parametrik alan                                                   |
| ALAN3                                                                         | DOF parametrik alan                                                   |
| ALAN4                                                                         | DOF parametrik alan                                                   |
| ALAN4_ACK                                                                     | DOF parametrik alan                                                   |
| ALAN6                                                                         | DOF parametrik alan                                                   |
| ALAN7                                                                         | DOF parametrik alan                                                   |
| ALAN7_ACK                                                                     | DOF parametrik alan                                                   |
| ALAN8                                                                         | DOF parametrik alan                                                   |
| ALAN9                                                                         | DOF parametrik alan                                                   |
| ALAN10                                                                        | DOF parametrik alan                                                   |
| ALAN10_ACK                                                                    | DOF parametrik alan                                                   |
| ALAN10_DESC                                                                   | DOF parametrik alan                                                   |
| ALAN11                                                                        | DOF parametrik alan                                                   |
| MTB                                                                           | Müşteri adı veya departman adı                                        |
| DURUM_ACK                                                                     | Durum açıklaması                                                      |
| DOF_ACAN_DEPT                                                                 | DOF açan departman                                                    |
| DOF_LIDERAMIRI                                                                | DOF lider amiri                                                       |
| ISLEM_SURESI                                                                  | İşlem süresi                                                          |
| DUZELTICIONLEYICI_ACK                                                         | Düzeltici mi önleyici mi durumunun açıklaması                         |
| EKIP                                                                          | Ekip bilgisi                                                          |
| BILGILENDIRME                                                                 | Bilgilendirme                                                         |
| KOK_NEDENLER                                                                  | Kök nedenler                                                          |
| KOKNEDEN_DETAYI                                                               | Kök neden detayı                                                      |
| KOK_TARIH                                                                     | Kök neden tarihi                                                      |
| MNPARAM                                                                       | Parametrik alan                                                       |
| URUN_TIPI                                                                     | Ürün tipi                                                             |
| SUREC_ADI                                                                     | Sürec adı                                                             |
| SUREC                                                                         | Süreç kodu - süreç adı                                                |
| DENETIM_KODU                                                                  | Denetim kodu                                                          |
| DENETIM_TANIMI                                                                | Denetim tanımı                                                        |
| DENETIM_TIPI                                                                  | Denetim tipi                                                          |
| UYG_KAT1                                                                      | Uygunsuzluk kategorisi                                                |
| UYG_KAT2                                                                      | Uygunsuzluk kategorisi                                                |
| UYG_KAT3                                                                      | Uygunsuzluk kategorisi                                                |
| UYG_KAT4                                                                      | Uygunsuzluk kategorisi                                                |
| UYG_KAT5                                                                      | Uygunsuzluk kategorisi                                                |
| GELISME_LPARAM1_VALUE                                                         | Gelişme parametrik alan                                               |
| GELISME_LPARAM10_VALUE                                                        | Gelişme parametrik alan                                               |
| GELISME_LPARAM2_VALUE                                                         | Gelişme parametrik alan                                               |
| GELISME_LPARAM3_VALUE                                                         | Gelişme parametrik alan                                               |
| GELISME_LPARAM4_VALUE                                                         | Gelişme parametrik alan                                               |
| GELISME_LPARAM5_VALUE                                                         | Gelişme parametrik alan                                               |
| GELISME_LPARAM6_VALUE                                                         | Gelişme parametrik alan                                               |
| GELISME_LPARAM7_VALUE                                                         | Gelişme parametrik alan                                               |
| GELISME_LPARAM8_VALUE                                                         | Gelişme parametrik alan                                               |
| GELISME_LPARAM9_VALUE                                                         | Gelişme parametrik alan                                               |
| GELISME_NPARAM1_VALUE                                                         | Gelişme parametrik alan                                               |
| GELISME_NPARAM2_VALUE                                                         | Gelişme parametrik alan                                               |
| GELISME_NPARAM3_VALUE                                                         | Gelişme parametrik alan                                               |
| GELISME_NPARAM4_VALUE                                                         | Gelişme parametrik alan                                               |
| GELISME_NPARAM5_VALUE                                                         | Gelişme parametrik alan                                               |
| GELISME_PPARAM1_VALUE                                                         | Gelişme parametrik alan                                               |
| GELISME_PPARAM10_VALUE                                                        | Gelişme parametrik alan                                               |
| GELISME_PPARAM2_VALUE                                                         | Gelişme parametrik alan                                               |
| GELISME_PPARAM3_VALUE                                                         | Gelişme parametrik alan                                               |
| GELISME_PPARAM4_VALUE                                                         | Gelişme parametrik alan                                               |
| GELISME_PPARAM5_VALUE                                                         | Gelişme parametrik alan                                               |
| GELISME_PPARAM6_VALUE                                                         | Gelişme parametrik alan                                               |
| GELISME_PPARAM7_VALUE                                                         | Gelişme parametrik alan                                               |
| GELISME_PPARAM8_VALUE                                                         | Gelişme parametrik alan                                               |
| GELISME_PPARAM9_VALUE                                                         | Gelişme parametrik alan                                               |
| GELISME_QPARAM1_VALUE                                                         | Gelişme parametrik alan                                               |
| GELISME_QPARAM1_KOD                                                           | Gelişme parametrik alan                                               |
| GELISME_QPARAM2_VALUE                                                         | Gelişme parametrik alan                                               |
| GELISME_QPARAM2_KOD                                                           | Gelişme parametrik alan                                               |
| GELISME_QPARAM3_VALUE                                                         | Gelişme parametrik alan                                               |
| GELISME_QPARAM3_KOD                                                           | Gelişme parametrik alan                                               |
| GELISME_QPARAM4_VALUE                                                         | Gelişme parametrik alan                                               |
| GELISME_QPARAM4_KOD                                                           | Gelişme parametrik alan                                               |
| GELISME_QPARAM5_VALUE                                                         | Gelişme parametrik alan                                               |
| GELISME_QPARAM5_KOD                                                           | Gelişme parametrik alan                                               |
| KAPATMA_LPARAM1_VALUE                                                         | Gelişme parametrik alan                                               |
| KAPATMA_QPARAM2_VALUE                                                         | Gelişme parametrik alan                                               |
| KAPATMA_QPARAM2_KOD                                                           | Gelişme parametrik alan                                               |
| LPARAM1_VALUE                                                                 | Parametrik alan                                                       |
| LPARAM10_VALUE                                                                | Parametrik alan                                                       |
| LPARAM2_VALUE                                                                 | Parametrik alan                                                       |
| LPARAM3_VALUE                                                                 | Parametrik alan                                                       |
| NPARAM1_VALUE                                                                 | Parametrik alan                                                       |
| NPARAM3_VALUE                                                                 | Parametrik alan                                                       |
| PPARAM1_VALUE                                                                 | Parametrik alan                                                       |
| QPARAM1_VALUE                                                                 | Parametrik alan                                                       |
| QPARAM1_KOD                                                                   | Parametrik alan                                                       |
| QPARAM2_VALUE                                                                 | Parametrik alan                                                       |
| QPARAM2_KOD                                                                   | Parametrik alan                                                       |
| SONUC_LMPARAM1_VALUE                                                          | Sonuç parametrik alan                                                 |
| SONUC_LMPARAM10_VALUE                                                         | Sonuç parametrik alan                                                 |
| SONUC_LMPARAM2_VALUE                                                          | Sonuç parametrik alan                                                 |
| SONUC_LMPARAM3_VALUE                                                          | Sonuç parametrik alan                                                 |
| SONUC_LMPARAM4_VALUE                                                          | Sonuç parametrik alan                                                 |
| SONUC_LMPARAM5_VALUE                                                          | Sonuç parametrik alan                                                 |
| SONUC_LMPARAM6_VALUE                                                          | Sonuç parametrik alan                                                 |
| SONUC_LMPARAM7_VALUE                                                          | Sonuç parametrik alan                                                 |
| SONUC_LMPARAM8_VALUE                                                          | Sonuç parametrik alan                                                 |
| SONUC_LMPARAM9_VALUE                                                          | Sonuç parametrik alan                                                 |
| SONUC_LPARAM1_VALUE                                                           | Sonuç parametrik alan                                                 |
| SONUC_LPARAM10_VALUE                                                          | Sonuç parametrik alan                                                 |
| SONUC_LPARAM2_VALUE                                                           | Sonuç parametrik alan                                                 |
| SONUC_LPARAM3_VALUE                                                           | Sonuç parametrik alan                                                 |
| SONUC_LPARAM4_VALUE                                                           | Sonuç parametrik alan                                                 |
| SONUC_LPARAM5_VALUE                                                           | Sonuç parametrik alan                                                 |
| SONUC_LPARAM6_VALUE                                                           | Sonuç parametrik alan                                                 |
| SONUC_LPARAM7_VALUE                                                           | Sonuç parametrik alan                                                 |
| SONUC_LPARAM8_VALUE                                                           | Sonuç parametrik alan                                                 |
| SONUC_LPARAM9_VALUE                                                           | Sonuç parametrik alan                                                 |
| SONUC_NPARAM1_VALUE                                                           | Sonuç parametrik alan                                                 |
| SONUC_NPARAM2_VALUE                                                           | Sonuç parametrik alan                                                 |
| SONUC_NPARAM3_VALUE                                                           | Sonuç parametrik alan                                                 |
| SONUC_NPARAM4_VALUE                                                           | Sonuç parametrik alan                                                 |
| SONUC_NPARAM5_VALUE                                                           | Sonuç parametrik alan                                                 |
| SONUC_PPARAM1_VALUE                                                           | Sonuç parametrik alan                                                 |
| SONUC_PPARAM10_VALUE                                                          | Sonuç parametrik alan                                                 |
| SONUC_PPARAM2_VALUE                                                           | Sonuç parametrik alan                                                 |
| SONUC_PPARAM3_VALUE                                                           | Sonuç parametrik alan                                                 |
| SONUC_PPARAM4_VALUE                                                           | Sonuç parametrik alan                                                 |
| SONUC_PPARAM5_VALUE                                                           | Sonuç parametrik alan                                                 |
| SONUC_PPARAM6_VALUE                                                           | Sonuç parametrik alan                                                 |
| SONUC_PPARAM7_VALUE                                                           | Sonuç parametrik alan                                                 |
| SONUC_PPARAM8_VALUE                                                           | Sonuç parametrik alan                                                 |
| SONUC_PPARAM9_VALUE                                                           | Sonuç parametrik alan                                                 |
| SONUC_QPARAM1_VALUE                                                           | Sonuç parametrik alan                                                 |
| SONUC_QPARAM1_KOD                                                             | Sonuç parametrik alan                                                 |
| SONUC_QPARAM2_VALUE                                                           | Sonuç parametrik alan                                                 |
| SONUC_QPARAM2_KOD                                                             | Sonuç parametrik alan                                                 |
| SONUC_QPARAM3_VALUE                                                           | Sonuç parametrik alan                                                 |
| SONUC_QPARAM3_KOD                                                             | Sonuç parametrik alan                                                 |
| SONUC_QPARAM4_VALUE                                                           | Sonuç parametrik alan                                                 |
| SONUC_QPARAM4_KOD                                                             | Sonuç parametrik alan                                                 |
| SONUC_QPARAM5_VALUE                                                           | Sonuç parametrik alan                                                 |
| SONUC_QPARAM5_KOD                                                             | Sonuç parametrik alan                                                 |
| YORUM                                                                         | Yorum                                                                 |
| ACIK_STATUSUNE_DONDURME                                                       | Açık statüsü bilgisi(Adı soyadı-tarih-açıklama)                       |
| IZLGUNTOP                                                                     | İzleme toplamı (gün olarak)                                           |
| TRH1                                                                          | Gelişme raporu yazma tarihi ile sisteme ekleme tarihi arasındaki fark |
| TRH2                                                                          | Sonuç raporu yazma tarihi ile sisteme ekleme tarihi arasındaki fark   |
| TRH3                                                                          | Kapatma tarihi ile sisteme ekleme tarihi arasındaki fark              |
| ILK_AKS_TARIHI                                                                | Kaydın açılma tarihi                                                  |
| AKS_ALMA_SURESI                                                               | Aksiyon alma süresi (Kayıt tarihi ve onay tarihi arasındaki fark)     |
| KAPATMAONAY_0                                                                 | Kapatma onaycıları ve tarihler(10' a kadar gidiyor)                   |
| ACMAONAY_0                                                                    | Açma onaycıları ve tarihler(10' a kadar gidiyor)                      |
| GELISMEONAY_0                                                                 | Gelişme onaycıları ve tarihler(10' a kadar gidiyor)                   |
| KAPATMAONAYTAR_0                                                              | Kapatma onay tarihleri(10' a kadar gidiyor)                           |
| ACMAONAYTAR_0                                                                 | Açma onay tarihleri(10' a kadar gidiyor)                              |
| GELISMEONAYTAR_0                                                              | Gelişme onay tarihleri(10' a kadar gidiyor)                           |
| ACMASURE_0                                                                    | Açma onay süresi(10' a kadar gidiyor)                                 |
| KAPATMASURE_0                                                                 | Kapatma onay süresi(10' a kadar gidiyor)                              |
| GELISMESURE_0                                                                 | Gelişme onay süresi(10' a kadar gidiyor)                              |
| AKS_PLANONAY_TAR_0                                                            | Aksiyon plan onaycıları ve tarihler(3' e kadar gidiyor)               |
| AKS_PLANONAY_0                                                                | Aksiyon plan onay tarihleri(3' e kadar gidiyor)                       |
| TOPLAM_ACMASURE                                                               | Toplam açma onay süresi                                               |
| TOPLAM_KAPATMASURE                                                            | Toplam Kapatma onay süresi                                            |
| AKS_PLANONAY_TAR                                                              | Aksiyon plan onay tarihi                                              |
| AKS_PLANONAY_BASTAR                                                           | Aksiyon plan onay başlangıç tarihi                                    |
| AKS_PLANONAY_RETTAR                                                           | Aksiyon plan onay ret tarihi                                          |
| RET_NEDENI                                                                    | Ret nedeni                                                            |
| RET_TARIHI                                                                    | Ret tarihi                                                            |
| IZLEME                                                                        | İzleme                                                                |
| UPARAM                                                                        | Parametrik alan                                                       |
| IZLEME1                                                                       | İzleme bilgisi(10' a kadar gidiyor)                                   |
| IZLEME1_BASLANGIC_TARIHI                                                      | İzleme başlangıç tarihi(10' a kadar gidiyor)                          |
| IZLEME1_SORUMLUSU                                                             | İzleme sorumlusu(10' a kadar gidiyor)                                 |
