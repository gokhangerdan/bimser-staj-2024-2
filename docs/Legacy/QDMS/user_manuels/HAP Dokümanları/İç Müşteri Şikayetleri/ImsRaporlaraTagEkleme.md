---
title: Raporlara Parametrik Alan Ekleme İşlemi ve Genel Tag Listesi
description: Raporlara Parametrik Alan Ekleme İşlemi ve Genel Tag Listesi Kullanıcı Yardım Dokümanı
sidebar_position: 2
---

:::tip Bilgi

İlgili konu başlığına sağ tarafta bulunan navigasyon yardımıyla hızlı bir şekilde ulaşabilirsiniz.

:::


**İç Müşteri Şikayetleri Modülünde Raporlara Parametrik Alan Ekleme İşlemi ve Genel Tag Listesi Kullanıcı Yardım Dokümanı**



# **1.İç Müşteri Şikayetleri Modülünde Raporlara Parametrik Alan Ekleme İşlemi ve Raporlarda Kullanılan Taglar**

İç Müşteri Şikayetleri Modülünde tüm raporlarına parametrik alan ekleme işlemi yapılmaktdır. İç Müşteri Şikayetleri Özet Raporuna parametrik alan ekleme işlem basamakları ve İç Müşteri Şikayetleri Modülünde kullanılan taglerin (kısa kodların) listesi bu yardım dokümanında yer almaktadır.

## **1.1.İç Müşteri Şikayetleri Modülünde Parametrik Alan Tiplerinin İç Müşteri Şikayetleri Özet Raporunda Gösterimi**

İç Müşteri Şikayetleri Modülü raporlarında İç Müşteri Şikayetleri Özet Listesi raporuna eklenen parametrik alanların raporda gösterilme işlemi için öncelikle dil ayarları menüsünde parametrik alan tiplerinin tanımlama işlemi yapmak gerekiyor. Dil ayarlarında metin, liste, gibi parametrik alan tiplerinin tanımlama işlemi yapılır. Bu tanımlanan parametrik alanlar Entegre Yönetim Sistemi\> İç Müşteri Şikayetleri \> İç Müşteri Şikayetleri İşlemleri menüsünde açılan bir Şikayet kaydı sekmelerinde görüntülenir. Bu sekmeler Şikayet Detayı Diğer Alanlar, Gelişme Raporu, Kök neden, Aksiyon, Sonuç Raporu ve Kapatma sekmelerindedir. Bu sekmelerde tanımlanan parametrik alan tiplerinin bilgisi girilir. Açılan Şikayet kaydında bu sekmelerin bilgi girişleri yapıldıktan sonra Rapor Formatları Düzenleme menüsüne gidilir. Rapor formatların düzenleme menüsünde İç Müşteri Şikayetleri Özet listesinin rapor format “IMS_OZET_RAPOR.xls” indirilir. İndirilenen “IMS_OZET_RAPOR.xls” dil ayarlarından tanımlanan parametrik alanların tag’leri yazılır. Örneğin: Şikayet kaydında Şikayet Detayı Diğer Alanlar sekmesine eklenen metin tipli parametrik alan tipi lblPARAM5 için \<PARAM5\> alan kodunun lbl olmadan tag içerisine yazılır. Bu şekilde Şikayet kaydı aşamalarına parametrik alan tipleri tag şeklinde Rapor formatına yazılır. Rapor formatına parametrik alanların tag şeklinde yazıldıktan Rapor format “IMS_OZET_RAPOR.xls” aynı isimde bilgisayara kaydedilir. Kaydedilen aynı isimde İç Müşteri Şikayetleri Özet Listesi Rapor formatı Rapor formatları düzenleme menüsünde tekrar sisteme yüklenir. İç Müşteri Şikayetleri Özet Listesi Rapor formatının yükleme işleminde sonra İç Müşteri Şikayetleri Raporlarında İç Müşteri Şikayetleri Özet Listesi Raporu menüsüne gidilir. Arama filtrelerinde kayıt no alanına Şikayetin kayıt no yazılırak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0fa8ad36-ffb7-40da-a8f8-a9f103231eac)(Excel aktar) butonu tıklanır. Excel format alınan raporda parametrik alanların taglerinin bulunduğu kısımda girilen Şikayet kaydının aşamalarında alan bilgilerinin geldiği ve taglerin çalıştığı görülür.

### **1.1.1. İç Müşteri Şikayetleri Modülünde Parametrik Alan Tanımlama**

İç Müşteri Şikayetleri Modülünde Şikayet Detayı Diğer Alanlar, Gelişme Raporu, Kök Nedenler, Aksiyonlar, Sonuç Raporu ve Kapatma sekmelerinde firmanın istemiş olduğu sistemde olmayan ekstradan alanlar tanımlanabilir. Tanımlanan bu alanlar tüm İç Müşteri Şikayetleri Modül kaynakları için geçerlidir. Sistem Altyapı Tanımları/BSAT/ Konfigürasyon Ayarları/Dil Ayarları menüsü tıklanılır. Açılan Dil Ayarları sayfasında Modül alanında “İç Müşteri Şikayetleri” seçilir ve ekranda İç Müşteri Şikayetleri Modülü ile ilgili dil tanımları görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload526348e6-149f-4552-8253-1080bb7b10b6)

İç Müşteri Şikayetleri Modülünde şikayet kaydının sekmelerinde tanımlanan parametrik alan tipleri tanımlanarak bu alanların tag şeklinde İç Müşteri Şikayetleri Özet raporunun formatına (IMS_OZET_RAPOR.xls) eklenerek İç Müşteri Şikayetleri özet raporuna bu parametrik alan tiplerinin bilgilerin basılması sağlanılır. İç Müşteri Şikayetleri Özet raporunun formatınan Aksiyon ve Kök Neden aşamalarında parametrik alan tiplerinin tag ekleme işlemi yapılmaktadır. Aksiyon ve Kök Neden tagleri Aksiyon raporlarının formatlarına eklenebiliyor.

### **1.1.1.1.İç Müşteri Şikayetleri Modülünde Şikayet Detayı Diğer Alanlar Sekmesinde Parametrik Alan Tanımlaması**

İç Müşteri Şikayetleri Modülünde Şikayet Detayı Diğer Alanlar sekmesinde tanımlanan parametrik alanların kısa kodları lblPARAM başlığı ile tanımlı kısa kodlardır. lblPARAM başlığındaki kısa kodlar olan tüm parametrik tipli alanlar tanımlandığında İç Müşteri Şikayetleri Modülünde Şikayet Detayı Diğer Alanlar sekmesi ekranında görüntülenir.

### **1.1.1.1.1.Metin Tipli Parametrik Alanların Listesi**

İç Müşteri Şikayetleri Modülünde Entegre Yönetim Sistemi\>İç Müşteri Şikayetleri \> İç Müşteri Şikayetleri İşlemleri menüsünde ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload35bc3ab4-2799-4720-a019-78fb4f82aadd) (Yeni) butonu tıklatıldığında açılan Şikayet Detayı ekranında Şikayet Detayı Diğer Alanlar sekmesinde Metin tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Metin yazarak Metin tipli parametrik alanlar aratılır ve Metin tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Metin tipli parametrik alanların alan tanımlaması yapılır. Bu metin tipli alanın daha sonra İç Müşteri Şikayetleri Özet listesinde gösterilme işleminde tag’ini kullanmak için tanımlama işlemi yapılacaktır. Bu alan tanımlaması yapılan Metin tipli parametrik alanları lbl kısa kodu kaldırarak:

\<PARAM1\>…\<PARAM15\> ve \<PARAM31\>…\<PARAM35\>şeklinde İç Müşteri Şikayetleri Özet Raporu formatına tag şeklinde eklendiğinde Şikayet Detayı ekranında Metin tipli alanların girilen değerleri bilgisi ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0fa9930f-ef84-49a3-880d-5b72c1b3e686)(Excel aktar) butonu tıklanarak alınan Excel formatındaki rapora basılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6a9b6f39-c1f4-4686-be00-686ef9e56a25)

### **1.1.1.1.2. Metin Tipli Parametrik Alan Tanımlama**

Rapor formatına eklenecek Metin tipli parametrik bir alan tanımlaması yapılır. lblPARAM5 Metin tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd768b4da-36a1-4ee5-859d-7bbdfd7cee59) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4a974ff5-44b1-482f-ace7-69832a25df41)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade18910e4-871c-4c80-bf0c-3e29ef3973d9)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1a4f2b2d-ab37-48b2-bb6d-683e20ad83c8)(kaydet) butonu tıklanarak Metin tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf11c3c8d-a28b-43cb-b0c5-48ee4b08c78e)

Tanımlanan Metin Tipli parametrik alan Entegre Yönetim Sistemi\> İç Müşteri Şikayetleri \> İç Müşteri Şikayetleri İşlemleri menüsünde ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload35bc3ab4-2799-4720-a019-78fb4f82aadd)(Yeni) butonu tıklatıldığında açılan Şikayet Detayı ekranında Şikayet Detayı Diğer Alanlar sekmesinde görüntülenir. Tanımlanan metin tipli parametrik alanın “lblPARAM5” lbl kısa kod kısmı kaldırrarak İç Müşteri Şikayetleri Özet Raporunun rapor formatına \<PARAM5\> tag şeklinde bilgisi yazılır. Şikayet Detayı tanımlama işleminde bu metin tipli alanın bilgisi girildiğinde İç Müşteri Şikayetleri Özet Raporu alındığında Metin tipli alanın girilen bilgileri rapora basılacaktır.

### **1.1.1.1.3.Metin (Çoklu Satır) Tipli Parametrik Alanların Listesi**

İç Müşteri Şikayetleri Modülünde Entegre Yönetim Sistemi\> İç Müşteri Şikayetleri \> İç Müşteri Şikayetleri İşlemleri menüsünde ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload35bc3ab4-2799-4720-a019-78fb4f82aadd) (Yeni) butonu tıklatıldığında açılan Şikayet Detayı ekranında Şikayet Detayı Diğer Alanlar sekmesinde Metin (Çoklu Satır)  tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Metin (Çoklu Satır) yazarak Metin (Çoklu Satır) tipli parametrik alanlar aratılır ve Metin (Çoklu Satır)  tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Metin (Çoklu Satır)  tipli parametrik alanların alan tanımlaması yapılır. Bu Metin (Çoklu Satır)  tipli alanın daha sonra İç Müşteri Şikayetleri Özet raporunda gösterilme işleminde tag’ini kullanmak için tanımlama işlemi yapılacaktır. Bu alan tanımlaması yapılan Metin (Çoklu Satır) tipli parametrik alanları lbl kısa kodu kaldırarak:

\<PARAM16\>,\<PARAM17\>…\<PARAM25\> şeklinde İç Müşteri Şikayetleri Özet Raporu formatına tag şeklinde eklendiğinde Şikayet Detayı ekranında Metin (Çoklu Satır) tipli alanların girilen değerleri bilgisi ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0fa9930f-ef84-49a3-880d-5b72c1b3e686)(Excel aktar) butonu tıklanarak alınan Excel formatındaki rapora basılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2fac6571-3d35-4d7d-9c8b-08881c2d2bd8)

### **1.1.1.1.4.Metin (Çoklu Satır) Tipli Parametrik Alan Tanımlama**

Rapor formatına eklenecek Metin (Çoklu Satır) tipli parametrik bir alan tanımlaması yapılır. lblPARAM16 Metin (Çoklu Satır) tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd768b4da-36a1-4ee5-859d-7bbdfd7cee59) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload86358969-3c43-4035-8bda-77cd6b24256f)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7f5b0787-3425-41e5-9eae-b526712e234c)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1a4f2b2d-ab37-48b2-bb6d-683e20ad83c8)(kaydet) butonu tıklanarak Metin (Çoklu Satır) tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadee9474f8-d6e1-4282-82a2-bb25ab6816a2)

Tanımlanan Metin (Çoklu Satır) Tipli parametrik alan Entegre Yönetim Sistemi\> İç Müşteri Şikayetleri \> İç Müşteri Şikayetleri İşlemleri menüsünde ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload35bc3ab4-2799-4720-a019-78fb4f82aadd)(Yeni) butonu tıklatıldığında açılan Şikayet Detayı ekranında Şikayet Detayı Diğer Alanlar sekmesinde görüntülenir. Tanımlanan Metin (Çoklu Satır) tipli parametrik alanın “lblPARAM16” lbl kısa kod kısmı kaldırrarak İç Müşteri Şikayetleri Özet Raporunun rapor formatına \<PARAM16\> tag şeklinde bilgisi yazılır. Şikayet Detayı tanımlama işleminde bu Metin (Çoklu Satır) tipli alanın bilgisi girildiğinde İç Müşteri Şikayetleri Özet Raporu alındığında Metin (Çoklu Satır) tipli alanın girilen bilgileri rapora basılacaktır.

### **1.1.1.1.5.Tarih Tipli Parametrik Alanların Listesi**

İç Müşteri Şikayetleri Modülünde Entegre Yönetim Sistemi\> İç Müşteri Şikayetleri \> İç Müşteri Şikayetleri İşlemleri menüsünde ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload35bc3ab4-2799-4720-a019-78fb4f82aadd) (Yeni) butonu tıklatıldığında açılan Şikayet Detayı ekranında Şikayet Detayı Diğer Alanlar sekmesinde Tarih tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Tarih yazarak Tarih tipli parametrik alanlar aratılır ve Tarih tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen tarih tipli parametrik alanların alan tanımlaması yapılır. Bu tarih tipli alanın daha sonra İç Müşteri Şikayetleri Özet raporunda gösterilme işleminde tag’ini kullanmak için tanımlama işlemi yapılacaktır. Bu alan tanımlaması yapılan tarih tipli parametrik alanları lbl kısa kodu kaldırarak:

\<DPARAM1\>,\<DPARAM2\>,….\<DPARAM5\> şeklinde İç Müşteri Şikayetleri Özet Raporu formatına tag şeklinde eklendiğinde Şikayet Detayı ekranında tarih tipli alanların girilen değerleri bilgisi ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0fa9930f-ef84-49a3-880d-5b72c1b3e686)(Excel aktar) butonu tıklanarak alınan Excel formatındaki rapora basılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload01923340-7e8d-40b1-a33c-da67abe54abf)

### **1.1.1.1.6.Tarih Tipli Parametrik Alan Tanımlama**

Rapor formatına eklenecek Tarih tipli parametrik bir alan tanımlaması yapılır. lblDPARAM1 Tarih tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd768b4da-36a1-4ee5-859d-7bbdfd7cee59) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9a1474ef-9f33-44d0-adb7-2c161ad536ba)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc72bd64-36b5-4a1d-bd69-93b3c82e4ce6)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1a4f2b2d-ab37-48b2-bb6d-683e20ad83c8)(Kaydet) butonu tıklanarak tarih tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9dbce69f-6048-4f11-9fd1-991f921dd844)

Tanımlanan Tarih tipli parametik alan Entegre Yönetim Sistemi\> İç Müşteri Şikayetleri \> İç Müşteri Şikayetleri İşlemleri menüsünde ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload35bc3ab4-2799-4720-a019-78fb4f82aadd)(Yeni) butonu tıklatıldığında açılan Şikayet Detayı ekranında Şikayet Detayı Diğer Alanlar sekmesinde görüntülenir. Tanımlanan Tarih tipli parametrik alanın “lblDPARAM1” lbl kısa kod kısmı kaldırrarak İç Müşteri Şikayetleri Özet Raporunun rapor formatına \<DPARAM1\> tag şeklinde bilgisi yazılır. Şikayet Detayı tanımlama işleminde bu Tarih tipli alanın bilgisi girildiğinde İç Müşteri Şikayetleri Özet Raporu alındığında Tarih tipli alanın girilen bilgileri rapora basılacaktır.

### **1.1.1.1.7.Liste Tipli Parametrik Alanların Listesi**

İç Müşteri Şikayetleri Modülünde Entegre Yönetim Sistemi\> İç Müşteri Şikayetleri \> İç Müşteri Şikayetleri İşlemleri menüsünde ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload35bc3ab4-2799-4720-a019-78fb4f82aadd) (Yeni) butonu tıklatıldığında açılan Şikayet Detayı ekranında Şikayet Detayı Diğer Alanlar sekmesinde Liste tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Liste yazarak Liste tipli parametrik alanlar aratılır ve Liste tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Liste tipli parametrik alanların alan tanımlaması yapılır. Bu Liste tipli alanın daha sonra İç Müşteri Şikayetleri Özet raporunda gösterilme işleminde tag’ini kullanmak için tanımlama işlemi yapılacaktır. Bu alan tanımlaması yapılan Liste tipli parametrik alanları lbl kısa kodu kaldırarak:

\<LPARAM1_VALUE\>,..\<LPARAM20_VALUE\>,ve\<LPARAM36_VALUE\>, …\<LPARAM40 \_VALUE \> şeklinde İç Müşteri Şikayetleri Özet Raporu formatına tag şeklinde eklendiğinde Şikayet Detayı ekranında Liste tipli alanların girilen değerleri bilgisi ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0fa9930f-ef84-49a3-880d-5b72c1b3e686)(Excel aktar )butonu tıklanarak alınan Excel formatındaki rapora basılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8cafd529-e4a5-43c7-8314-c32badad28ce)

### **1.1.1.1.8.Liste Tipli Parametrik Alan Tanımlama**

Rapor formatına eklenecek liste tipli parametrik bir alan tanımlaması yapılır. lblLPARAM5 Liste tipli parametrik seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd768b4da-36a1-4ee5-859d-7bbdfd7cee59) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5f38b895-8bcb-477b-9bf7-62086d36f3c4)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6a3d3edd-130e-4e91-a2fc-898d40348fd3)

Liste tipli alanın liste değerlerini girmek için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf8ca80e2-5e36-4a56-8132-e2a06d51a2ec) (Yeni) butonuna tıklanır, liste değerleri yazılır ve kaydedilir. Liste eleman değeri 1 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload53e5334c-0ad5-4e84-9e80-657e31190f7f)

Liste eleman değeri 2 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfdaa21a0-36f2-4486-9deb-f0c78c6d2f03)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload76a0a520-7601-4c03-aed5-6d23ae98b46b)

Alanın zorunlu olup, olmayacağı sıra no bilgisi, liste elemanları tanımlanarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1a4f2b2d-ab37-48b2-bb6d-683e20ad83c8)(kaydet) butonu tıklanarak liste tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload41c59bc3-54be-4b2c-8633-192175e19f47)

Tanımlanan Liste Tipli parametik alan Entegre Yönetim Sistemi\> İç Müşteri Şikayetleri \> İç Müşteri Şikayetleri İşlemleri menüsünde ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload35bc3ab4-2799-4720-a019-78fb4f82aadd) (Yeni) butonu tıklatıldığında açılan Şikayet Detayı ekranında Şikayet Detayı Diğer Alanlar sekmesinde görüntülenir. İç Müşteri Şikayetleri Özet Raporunun rapor formatına \<LPARAM5 \_VALUE \> tag şeklinde bilgisi yazılır. Şikayet Detayı tanımlama işleminde bu liste tipli alanın bilgisi girildiğinde İç Müşteri Şikayetleri Özet Raporu alındığında liste tipli alanın girilen bilgileri rapora basılacaktır.

### **1.1.1.1.9.Sorgu Tipli Parametrik Alanların Listesi**

İç Müşteri Şikayetleri Modülünde Entegre Yönetim Sistemi\> İç Müşteri Şikayetleri \> İç Müşteri Şikayetleri İşlemleri menüsünde ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload35bc3ab4-2799-4720-a019-78fb4f82aadd) (Yeni) butonu tıklatıldığında açılan Şikayet Detayı ekranında Şikayet Detayı Diğer Alanlar sekmesinde Sorgu tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Sorgu yazarak Sorgu tipli parametrik alanlar aratılır ve Sorgu tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Sorgu tipli parametrik alanların alan tanımlaması yapılır. Bu Sorgu tipli alanın daha sonra İç Müşteri Şikayetleri Özet raporunda gösterilme işleminde tag’ini kullanmak için tanımlama işlemi yapılacaktır. Bu alan tanımlaması yapılan Sorgu tipli parametrik alanları lbl kısa kodu kaldırarak:

\<QPARAM1\>,\<QPARAM2\>,….\<QPARAM5\> şeklinde İç Müşteri Şikayetleri Özet Raporu formatına tag şeklinde eklendiğinde Şikayet Detayı ekranında Sorgu tipli alanların girilen değerleri bilgisi ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0fa9930f-ef84-49a3-880d-5b72c1b3e686)(Excel aktar) butonu tıklanarak alınan Excel formatındaki rapora basılır

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload56741bcc-237c-486c-84f9-0413fc09df70)

### **1.1.1.1.10.Sorgu Tipli Parametrik Alan Tanımlama**

Rapor formatına eklenecek Sorgu tipli parametrik bir alan tanımlaması yapılır. lblQPARAM1 Sorgu tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd768b4da-36a1-4ee5-859d-7bbdfd7cee59) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadde0f3c36-60a5-4422-8502-c315abe6e66c)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfea72bb9-91f2-400c-abfc-8057f682e64e) Bimser Destek ekibinde yardım alınarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1a4f2b2d-ab37-48b2-bb6d-683e20ad83c8)(kaydet) butonu tıklanarak Sorgu tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload11950519-2213-414b-aa1e-1b46f4eaa096)

Tanımlanan Sorgu Tipli parametrik alan Entegre Yönetim Sistemi\> İç Müşteri Şikayetleri \> İç Müşteri Şikayetleri İşlemleri menüsünde ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload35bc3ab4-2799-4720-a019-78fb4f82aadd) (Yeni) butonu tıklatıldığında açılan Şikayet Detayı ekranında Şikayet Detayı Diğer Alanlar sekmesinde görüntülenir. İç Müşteri Şikayetleri Özet Raporunun rapor formatına \<QPARAM1\> tag şeklinde bilgisi yazılır. Şikayet Detayı tanımlama işleminde bu sorgu tipli alanın bilgisi girildiğinde İç Müşteri Şikayetleri Özet Raporu alındığında sorgu tipli alanın girilen bilgileri rapora basılacaktır.

### **1.1.1.1.11.Parasal Tipli Parametrik Alanların Listesi**

İç Müşteri Şikayetleri Modülünde Entegre Yönetim Sistemi\>İç Müşteri Şikayetleri \>İç Müşteri Şikayetleri İşlemleri menüsünde ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload35bc3ab4-2799-4720-a019-78fb4f82aadd) (Yeni) butonu tıklatıldığında açılan Şikayet Detayı ekranında Şikayet Detayı Diğer Alanlar sekmesinde Parasal tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Parasal yazarak Parasal tipli parametrik alanlar aratılır ve Parasal tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Parasal tipli parametrik alanların alan tanımlaması yapılır. Bu parasal tipli alanın daha sonra İç Müşteri Şikayetleri Özet raporunda gösterilme işleminde tag’ini kullanmak için tanımlama işlemi yapılacaktır. Bu alan tanımlaması yapılan parasal tipli parametrik alanları lbl kısa kodu kaldırarak:

\<NPARAM1_VALUE\>,..\<NPARAM5_VALUE\>,\<NPARAM21_VALUE\>…\<NPARAM30_VALUE\>, ve \<NPARAM46_VALUE\>,..\<NPARAM50_VALUE\> şeklinde İç Müşteri Şikayetleri Özet Raporu formatına tag şeklinde eklendiğinde Şikayet Detayı ekranında parasal tipli alanların girilen değerleri bilgisi ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0fa9930f-ef84-49a3-880d-5b72c1b3e686)(Excel aktar) butonu tıklanarak alınan Excel formatındaki rapora basılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb0f95def-bdd3-453b-ba5e-d9ed951ac079)

### **1.1.1.1.12.Parasal Tipli Parametrik Alan Tanımlama**

Rapor formatına eklenecek Parasal tipli parametrik bir alan tanımlaması yapılır. lblNPARAM1 Parasal tipli alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd768b4da-36a1-4ee5-859d-7bbdfd7cee59) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9c8bb5d5-93b9-4171-a9fe-1325da2beba6)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb23537b5-6033-4090-827d-4b298c2c2aff)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1a4f2b2d-ab37-48b2-bb6d-683e20ad83c8)(Kaydet ) butonu tıklanarak Parasal tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1285e322-40cf-4fdc-8e7f-31c4125f248f)

Tanımlanan Parasal Tipli parametrik alan Entegre Yönetim Sistemi\> İç Müşteri Şikayetleri \> İç Müşteri Şikayetleri İşlemleri menüsünde ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload35bc3ab4-2799-4720-a019-78fb4f82aadd) (Yeni) butonu tıklatıldığında açılan Şikayet Detayı ekranında Şikayet Detayı Diğer Alanlar sekmesinde görüntülenir. İç Müşteri Şikayetleri Özet Raporunun rapor formatına \<NPARAM21_VALUE\> tag şeklinde bilgisi yazılır. Şikayet Detayı tanımlama işleminde bu parasal tipli alanın bilgisi girildiğinde İç Müşteri Şikayetleri Özet Raporu alındığında parasal tipli alanın girilen bilgileri rapora basılacaktır.

### **1.1.1.2.İç Müşteri Şikayetleri Modülünde Gelişme Raporu Sekmesinde Parametrik Alan Tipi Tanımlaması**

İç Müşteri Şikayetleri Modülünde Şikayet Detayı ekranında Gelişme Raporu sekmesinde tanımlanan parametrik alanların kısa kodları lblG\_ başlığı ile tanımlı kısa kodlardır. lblG\_ başlığındaki kısa kodlar olan tüm parametrik tipli alanlar tanımlandığında İç Müşteri Şikayetleri Modülünde Şikayet Detayı ekranında Gelişme Raporu sekmesi ekranında görüntülenir.

### **1.1.1.2.1.Liste Tipli Parametrik Alanların Listesi**

İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Gelişme Raporu sekmesinde Liste tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Liste yazarak Liste tipli parametrik alanlar aratılır ve Liste tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Liste tipli parametrik alanların alan tanımlaması yapılır. Bu liste tipli alanın daha sonra İç Müşteri Şikayetleri Özet raporunda gösterilme işleminde tag’ini kullanmak için tanımlama işlemi yapılacaktır. Bu alan tanımlaması yapılan liste tipli parametrik alanları lblG kısa kodu kaldırarak:

\<GELISME_LPARAM1_VALUE\>… \<GELISME_LPARAM10_VALUE\> şeklinde İç Müşteri Şikayetleri Özet Raporu formatına tag şeklinde eklendiğinde Şikayet Detayı ekranında liste tipli alanların girilen değerleri bilgisi ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0fa9930f-ef84-49a3-880d-5b72c1b3e686)(Excel aktar) butonu tıklanarak alınan Excel formatındaki rapora basılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4d083ff5-20cc-4bb6-952a-c67c35cd9606)

### **1.1.1.2.2.Liste Tipli Parametrik Alan Tanımlama.**

Rapor formatına eklenecek liste tipli parametrik bir alan tanımlaması yapılır. lblG_LParam2 Liste tipli parametrik seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd768b4da-36a1-4ee5-859d-7bbdfd7cee59) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc226eb45-bb48-4de0-a97e-759a4d3c1977)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd90908f4-11cf-44e1-8c75-cbb8cd1637bd)Liste tipli alanın liste değerlerini girmek için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf8ca80e2-5e36-4a56-8132-e2a06d51a2ec) (Yeni) butonuna tıklanır, liste değerleri yazılır ve kaydedilir. Liste eleman değeri 1 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload50f88591-546b-49bd-861c-165dac66de99)

Liste eleman değeri 2 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9a846da9-8af7-489e-91ac-a539a6522fa0)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd119511c-674a-4c51-bc21-c8ee44eecdf8)

Alanın zorunlu olup, olmayacağı sıra no bilgisi ve liste elemanları tanımlanarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1a4f2b2d-ab37-48b2-bb6d-683e20ad83c8)(kaydet) butonu tıklanarak liste tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload88da75a8-704c-4d4e-97f1-e1050e7678f4)

Tanımlanan liste tipli parametrik alan İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Gelişme Raporu sekmesinde görüntülenir. İç Müşteri Şikayetleri Özet Raporunun rapor formatına \<GELISME_LPARAM2_VALUE\> tag şeklinde bilgisi yazılır. Şikayet Detayı tanımlama işleminde bu liste tipli alanın bilgisi girildiğinde İç Müşteri Şikayetleri Özet Raporu alındığında liste tipli alanın girilen bilgileri rapora basılacaktır.

### **1.1.1.2.3.Personel Tipli Parametrik Alanların Listesi**

İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Gelişme Raporu sekmesinde Personel tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Personel yazarak Personel tipli parametrik alanlar aratılır ve Personel tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Personel tipli parametrik alanların alan tanımlaması yapılır. Bu Personel tipli alanın daha sonra İç Müşteri Şikayetleri Özet raporunda gösterilme işleminde tag’ini kullanmak için tanımlama işlemi yapılacaktır Bu alan tanımlaması yapılan Personel tipli parametrik alanları lbG kısa kodu kaldırarak:

\<GELISME_PPARAM1_VALUE\>…\<GELISME_PPARAM5_VALUE\> şeklinde İç Müşteri Şikayetleri Özet Raporu formatına tag şeklinde eklendiğinde Şikayet Detayı ekranında Personel tipli alanların girilen değerleri bilgisi ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0fa9930f-ef84-49a3-880d-5b72c1b3e686)(Excel aktar) butonu tıklanarak alınan Excel formatındaki rapora basılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfb597b15-42a0-4ef6-90a6-4890e3d9bc1c)

### **1.1.1.2.4.Personel Tipli Parametrik Alan Tanımlama**

Rapor formatına eklenecek Personel tipli parametrik bir alan tanımlaması yapılır. lblG_PParam1 Personel tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd768b4da-36a1-4ee5-859d-7bbdfd7cee59) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc6dc9b55-b1a2-4045-a75b-0aef3dddf2a0)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4e22b816-6b40-4963-972f-09c9977c0be1)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1a4f2b2d-ab37-48b2-bb6d-683e20ad83c8)(kaydet) butonu tıklanarak Personel tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload869c9db0-6541-4c4c-97e3-3333b031a20e)

Tanımlanan Personel tipli parametrik alan İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Gelişme Raporu sekmesinde görüntülenir. İç Müşteri Şikayetleri Özet Raporunun rapor formatına \<GELISME_PPARAM1_VALUE\> tag şeklinde bilgisi yazılır. Şikayet Detayı tanımlama işleminde bu Personel tipli alanın bilgisi girildiğinde İç Müşteri Şikayetleri Özet Raporu alındığında Personel tipli alanın girilen bilgileri rapora basılacaktır.

### **1.1.1.2.5.Metin Tipli Parametrik Alanların Listesi**

İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Gelişme Raporu sekmesinde Metin tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Metin yazarak Metin tipli parametrik alanlar aratılır ve Metin tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Metin tipli parametrik alanların alan tanımlaması yapılır. Bu Metin tipli alanın daha sonra İç Müşteri Şikayetleri Özet raporunda gösterilme işleminde tag’ini kullanmak için tanımlama işlemi yapılacaktır Bu alan tanımlaması yapılan Metin tipli parametrik alanları lblG kısa kodu kaldırarak:

\<GELISME_PARAM1\>,.. \<GELISME_PARAM10\> şeklinde İç Müşteri Şikayetleri Özet Raporu formatına tag şeklinde eklendiğinde Şikayet Detayı ekranında Metin tipli alanların girilen değerleri bilgisi ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0fa9930f-ef84-49a3-880d-5b72c1b3e686) (Excel aktar) butonu tıklanarak alınan Excel formatındaki rapora basılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1e45fc6f-0d30-4897-b66f-a72fd590fa5b)

### **1.1.1.2.6.Metin Tipli Parametrik Alan Tanımlama**

Rapor formatına eklenecek Metin tipli parametrik bir alan tanımlaması yapılır. lblG_Param2 Metin tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd768b4da-36a1-4ee5-859d-7bbdfd7cee59) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload64580dac-50ee-409e-8f93-8a9c8536efcf)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload09c78456-e069-47ad-b7dd-35e64bed5447)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1a4f2b2d-ab37-48b2-bb6d-683e20ad83c8)(kaydet) butonu tıklanarak Metin tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload212816f9-0148-4055-9f97-ab0c6d4b3f21)

Tanımlanan Metin tipli parametrik alan İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Gelişme Raporu sekmesinde görüntülenir. İç Müşteri Şikayetleri Özet Raporunun rapor formatına \<GELISME_PARAM2\> tag şeklinde bilgisi yazılır. Şikayet Detayı tanımlama işleminde bu Metin tipli alanın bilgisi girildiğinde İç Müşteri Şikayetleri Özet Raporu alındığında Metin tipli alanın girilen bilgileri rapora basılacaktır.

### **1.1.1.3.İç Müşteri Şikayetleri Modülünde Sonuç Raporu Sekmesinde Parametrik Alan Tipi Tanımlaması**

İç Müşteri Şikayetleri Modülünde Şikayet Detayı ekranında Sonuç Raporu sekmesinde tanımlanan parametrik alanların kısa kodları lblS\_ başlığı ile tanımlı kısa kodlardır. lblS\_ başlığındaki kısa kodlar olan tüm parametrik tipli alanlar tanımlandığında İç Müşteri Şikayetleri Modülünde Şikayet Detayı ekranında Sonuç Raporu sekmesinde ekranında görüntülenir.

### **1.1.1.3.1.Metin Tipli Parametrik Alanların Listesi**

İç Müşteri Şikayetleri Modülünde Şikayet Detayı ekranında Sonuç Raporu sekmesinde metin tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına metin yazarak metin tipli parametrik alanlar aratılır metin tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen metin tipli parametrik alanların alan tanımlaması yapılır. Bu Metin tipli alanın daha sonra İç Müşteri Şikayetleri Özet raporunda gösterilme işleminde tag’ini kullanmak için tanımlama işlemi yapılacaktır Bu alan tanımlaması yapılan metin tipli parametrik alanları lblS\_ kısa kodu kaldırarak:

\<SONUC_PARAM1\>…\<SONUC_PARAM10\> şeklinde İç Müşteri Şikayetleri Özet Raporu formatına tag şeklinde eklendiğinde Şikayet Detayı ekranında metin tipli alanların girilen değerleri bilgisi ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0fa9930f-ef84-49a3-880d-5b72c1b3e686) (Excel aktar) butonu tıklanarak alınan Excel formatındaki rapora basılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3ee4b26a-ac6a-4cf9-9247-f77e39cf7aa8)

### **1.1.1.3.2.Metin Tipli Parametrik Alan Tanımlama**

Rapor formatına eklenecek Metin tipli parametrik bir alan tanımlaması yapılır. lblS_Param2 Metin tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd768b4da-36a1-4ee5-859d-7bbdfd7cee59) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3815bc1c-669a-4df1-8195-ef11c326893a)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadce66a6ab-8153-43bd-a43d-a790a3bf5b38)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1a4f2b2d-ab37-48b2-bb6d-683e20ad83c8)(kaydet) butonu tıklanarak metin tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2e9a5c65-38d0-41fd-bee3-44837872b187)

Tanımlanan metin tipli parametrik alan İç Müşteri Şikayetleri Modülünde Şikayet Detayı ekranında Sonuç Raporu sekmesinde görüntülenir. İç Müşteri Şikayetleri Özet Raporunun rapor formatına \<SONUC_PARAM2\> tag şeklinde bilgisi yazılır. Şikayet Detayı tanımlama işleminde bu Metin tipli alanın bilgisi girildiğinde İç Müşteri Şikayetleri Özet Raporu alındığında metin tipli alanın girilen bilgileri rapora basılacaktır.

### **1.1.1.4.İç Müşteri Şikayetleri Modülünde Kapatma sekmesinde Parametrik Alan Tipi Tanımlaması**

İç Müşteri Şikayetleri Modülünde Şikayet Detayı ekranında Kapatma sekmesinde tanımlanan parametrik alanların kısa kodları lblK\_ başlığı ile tanımlı kısa kodlardır. lblK\_ başlığındaki kısa kodlar olan tüm parametrik tipli alanlar tanımlandığında İç Müşteri Şikayetleri Modülünde Şikayet Detayı ekranında Kapatma sekmesinde görüntülenir.

### **1.1.1.4.1.Metin Tipli Parametrik Alanların Listesi**

İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Kapatma sekmesinde metin tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına metin yazarak metin tipli parametrik alanlar aratılır metin tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen metin tipli parametrik alanların alan tanımlaması yapılır. Bu metin tipli alanın daha sonra İç Müşteri Şikayetleri Özet raporunda gösterilme işleminde tag’ini kullanmak için tanımlama işlemi yapılacaktır. Bu alan tanımlaması yapılan metin tipli parametrik alanları lblK\_ kısa kodu kaldırarak:

\<KAPATMA_PARAM1\>…\<KAPATMA_PARAM10\> şeklinde İç Müşteri Şikayetleri Özet Raporu formatına tag şeklinde eklendiğinde Şikayet Detayı ekranında Metin tipli alanların girilen değerleri bilgisi ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0fa9930f-ef84-49a3-880d-5b72c1b3e686) (Excel aktar) butonu tıklanarak alınan Excel formatındaki rapora basılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0e133fa2-98be-4906-9a53-080b5e425842)

### **1.1.1.4.1.Metin Tipli Parametrik Alan Tanımlama**

Rapor formatına eklenecek Metin tipli parametrik bir alan tanımlaması yapılır. lblK_Param2 Metin tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd768b4da-36a1-4ee5-859d-7bbdfd7cee59) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload64a74fd8-5c31-44e9-bd53-30d0bd545be9)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload645d9292-383c-44de-adb0-19fe3e31a973)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1a4f2b2d-ab37-48b2-bb6d-683e20ad83c8)(kaydet) butonu tıklanarak metin tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload19a84837-a62e-4544-97f5-871a5579fde7)

Tanımlanan metin tipli parametrik alan İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Kapatma sekmesinde görüntülenir. İç Müşteri Şikayetleri Özet Raporunun rapor formatına \<KAPATMA_PARAM2\> tag şeklinde bilgisi yazılır. Şikayet Detayı tanımlama işleminde bu Metin tipli alanın bilgisi girildiğinde İç Müşteri Şikayetleri Özet Raporu alındığında Metin tipli alanın girilen bilgileri rapora basılacaktır.

### **1.1.2. İç Müşteri Şikayetleri Özet Raporu Formatına Tag Eklenecek Alanların Değerlerin Girilmesi**

İç Müşteri Şikayetleri Özet Raporu formatına tag eklenecek alanların dğerlerin girilmesi için İç Müşteri Şikayetleri Modülünde yeni bir Şikayet Detayı açılır. Açılan Şikayet Detayı tag eklenecek alanların bilgisi girilir. İç Müşteri Şikayetleri modülünde açılan Şikayet Detayı tanımlanan parametrik alanların tiplerini bilgisi girildikten sonra rapor formatına eklenen alanların tagleri ile rapora bu alanların bilgisinin basılma sağlanılır. Raporda tanımlanan alan değerlerin bilgisinin gelmesi için Şikayet Detayı ekranında alan bilgilerin girilmesi gerekmektedir

Entegre Yönetim Sistemi/ İç Müşteri Şikayetleri/ İç Müşteri Şikayet İşlemleri tıklanılır.

### **1.1.2.1.Şikayet Açma**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload35bc3ab4-2799-4720-a019-78fb4f82aadd) (yeni) butonuna tıklanarak yeni bir kayıt açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8afff982-69bf-42ff-88f6-2c0f53e39b8c) Açılan ekranda doldurulması gereken 3 sekme vardır. Şikayet detayı, çözüm ekibi, ek dosyalar sekmeleridir. Bu sekmeler dışında Dil ayarlarından parametrik alan tipi tanımlaması yapıldığı için 4. sekme olan Şikayet detayı diğer alanlar sekmeside kaydı açan tarafından bilgisi doldurulur.

Şikayet Detayı Sekmesinde Şikayetin hangi departmandan geldiği, şikayetin tanımı, detayı, şikayetin kategorisi gibi zorunlu alanlar girilir. İstenilirse şikayetin hangi işyeri, hangi ürün, hangi süreç ve yönetim sistemi ile alakalı olduğu da belirtilebilir. Şikayetle ilgili bilgi sahibi olması gereken kullanıcılar ise bilgilendirme alanından seçilebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload36fe3422-27ce-4165-9794-d7ae14f4a9c9)

Şikayet Detayı Diğer Alanlar Sekmesinde Firmanın özel istekleri doğrultusunda oluşturulmuş parametrik alanları içerdiği sekmedir. Bu sekmede dil ayarlarında tanımlanan parametrik alan tiplerinin bilgisi girilir. Bu parametrik alan tiplerinin tag’leri daha sonra rapor formatına eklenerek İç Müşteri Şikayetleri Özet raporuna bilgilerin basılması sağlanacaktır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaf796bdc-e7af-4e74-ae3a-9ffe95e4a4fd)

Çözüm Ekibi Sekmesinde gelen şikayetleri çözüme ulaştıracak, kök neden analizini yapacak ve kalıcı aksiyonları planlayacak olan ekip lideri ve ekip üyelerinin seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload86122f57-5f40-4eab-850d-17890f452cd2)

Ek Dosyalar sekmesine geçilerek istenirse şikayetle ilgili doküman, ses, görüntü vb. formatlarda istenen dosyaların eklenmesi gerçekleştirilebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc41141f5-7731-4faf-9db3-8b3429d35c82)

**![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0791f6dc-ca0c-4c21-b7b0-1fe428e5ee69)**(Kaydet) butonu ile kaydedildiğinde eğer Şikayet açma onayı için bir akış kurgulandıysa ilgili rolün onayına kurgulanmadıysa Ekip Liderine Gelişme Raporu yazılması için görev düşer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada8ea38ea-1f03-42c7-9c4b-ed24d109001e)

### **1.1.2.2.Gelişme Raporu**

**Şikayet kaydı gelişme raporu yazmak üzere Ekip Liderinin ve Ekip Üyesi** Bekleyen İşleri’ne “**Gelişme Raporu Yazılacak İç Müşteri Şikayetleri**” olarak iş düşer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload697bdf2c-16bb-4057-a3db-652d5b1a3569)

İlgili Şikayet kodu üzerine tıklayarak Şikayet bilgilerinin olduğu ekrana açılır. Gelişme Raporu sekmesinde bilgileri doldulur. Gelişme raporu aşamasındaki parametrik alan tiplerinin bilgi girişleri yapılır. Bu parametrik alan tiplerinin tag’leri daha sonra rapor formatına eklenerek İç Müşteri Şikayetleri Özet raporuna bilgilerin basılması sağlanacaktır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload566dbbf9-88eb-4839-985f-ed35e8e331d2)

Gelişme raporu sekmesi ile ilgili bilgilerin girişi tamamlanınca ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload47445d5a-ae4d-467f-907b-1887545038da) (kaydet) butonu ile kayıt edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8d9ace8a-5920-479e-980c-20df20d65a26)

### **1.1.2.3.Kök Neden Analizi**

Gelişme raporundan sonraki aşama kök neden analizinin yapılacağı sekmedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb40421bc-54d5-436a-a7a8-cf17df720647)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload23f71f48-c7b0-4c6d-b625-02a4ee6ce1c3) (Yeni) butonu tıklanarak kök neden ekleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada1d27c7e-27f5-42d6-ad3d-06c95d7d2d8e)

Açılan ekranda daha önceden tanımlanan kök nedenlerden istenenler seçilir, açıklama bilgisi girilir. Daha sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadae5d91bd-986e-4532-b0b3-e7a0f5dd1e94) (kaydet) butonu tıklanarak kök neden kaydedilerek Şikayet kaydı ile ilişkisi kurulmuş olur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload93387ca2-3909-40a3-b123-0a562639c60e)

### **1.1.2.4.Aksiyon Planlama**

Kök neden aşamasından sonraki sekme aksiyonları planlamaktır. Bu aksiyonlar kök nedenleri ortadan kaldırmak ve bir daha ortaya çıkmasını engellemek adına alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload69f7a267-cf73-4d78-848b-0597ccc1f74d)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade3ae684b-c559-4157-a0ce-e3b267a3a884) Yeni butonu tıklanarak Aksiyonlar-Yeni Kayıt ekranına gelinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0dd18b68-9f59-4eed-b300-fde267bc609d)

Açılan ekranda, aksiyonu takip edecek sorumlu, aksiyonu yapacak kişi, aksiyonun ne olduğunun açıklaması, aksiyonun planlanan bitiş tarihi, ilişkilendirilmek istenirse dokümanlar, ayrıca aksiyonun hangi kök nedenle alakalı olduğu alanları doldurulur. Bu alanlar girildikten sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload47445d5a-ae4d-467f-907b-1887545038da)(kaydet) butonuna tıklanarak aksiyon, yapacak kişiye görev olarak atanmış olacaktır.

Aksiyon açılması için onay kurgusu yapılmış ise; aksiyon işi yapacak kişiye düşmeden önce rolde tanımlanmış kişinin açılmaya onayına düşecektir. Onay verilirse işi yapacak kişiye aksiyon görevi düşer. Onay kurgusu yoksa aksiyon tanımlandıktan sonra direkt olarak işi yapacak kişiye görev olarak düşer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload099493aa-da62-4b57-bdc6-2a1fc266d5ee)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload860ba159-d8e2-4cc3-9ad3-ad2d4b513002)

### **1.1.2.5.Aksiyon Gerçekleştirme**

Aksiyon planlama işleminden sonra aksiyonu yapacak kişinin bekleyen işlerim menüsüne “**Gerçekleşecek İç Müşteri Şikayeti Aksiyonları**” olarak iş düşmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload38ce209b-229d-49ea-b33d-7127ed476483)

Aksiyonu yapacak kişi MS-Aksiyon No’sunu tıklayıp, aksiyonu gerçekleştireceği ekrana ulaşır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload71397371-9d22-49ea-906e-429cb80fa5b7)

Açılan ekranda yapılan aksiyon sonucunu yazmak için ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload462f3200-7f18-42ca-bb2a-1e9395ec2b56) (aksiyonu gerçekleştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8bbbb2d2-9ced-4c7b-8e95-f2fdf1fcf6c7)

Bu ekranda iken, yapılan aksiyon açıklaması girilir. Yapılan tarih belirtilir ve herhangi bir ek dosya varsa eklenir. Gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload47445d5a-ae4d-467f-907b-1887545038da) Kaydet butonu tıklanır. Aksiyon gerçekleştirilir. Eğer akışlarda aksiyon gerçekleştirme kapatma onayı kurgulanmışsa, aksiyon gerçekleştirildikten sonra onaycı role düşer. Onay işlemi gerçekleştirildikten sonra aksiyon kapalı konuma geçip, şikayet kaydı sonuç raporu yazılmak üzere ekibin bekleyen işlerine düşer. Aksiyon ret olursa, işi yapacak kişiye geri döner. Onay olmadığı durumda aksiyonlar gerçekleştirildikten sonra, şikayet kaydı sonuç raporu yazılmak üzere ekibin bekleyen işlerine düşer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf47aef89-e10b-46b3-b359-6246e4d9207b)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1c09309c-b584-48ba-a554-c90d8c4da100)

### **1.1.2.6.Sonuç Raporu**

Aksiyonların tamamı gerçekleştirildikten sonraki aşama, sonuç raporu yazma basamağıdır. Sonuç raporu sekmesinde ekip lideri tarafından aksiyonlar incelenerek yeterliliği araştırılır. Ekip lideri sonuç raporu yazarken, şikayetin bu aksiyonlar ile kapatılıp kapatılamayacağına dair kapatma onayındaki kişiye geri bildirim verir. Ekip lideri bekleyen işlerim menüsündeki “**Sonuç Raporu yazılacak İç Müşteri Şikayetleri**” iş olarak düşer. Şikayet kodu tıklanarak, sonuç raporun yazılacağı sayfaya ulaşılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8e5f82ef-154b-49dc-95ba-0bda3eb5e66e)

Sonuç raporu yazılarak, ek dosya var ise eklenir. Sonuç Raporu aşamasında dil ayarlarından tanımlanan parametrik alan tiplerinin bilgi girişi yapılır. Bu parametrik alan tiplerinin tagleri daha sonra rapor formatına eklenerek İç Müşteri Şikayetleri Özet raporuna bilgilerin basılması sağlanacaktır. Gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadae5d91bd-986e-4532-b0b3-e7a0f5dd1e94)(Kaydet) butonu tıklanarak kayıt işlemi gereçkleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8132666e-a250-4204-9db1-59ae9134325f)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1e6e3933-a49e-4d40-9fb9-2b2c26a2937d)

### **1.1.2.7.Şikayeti Kapatma**

Sonuç raporu yazıldıktan sonra, şikayet artık kapatılmak üzere onaya gitmektedir. Onaycı kişi, bekleyen işlerim menüsünden “**Kapatılacak İç Müşteri Şikayetleri Listesi**” olarak iş düşer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf65c9006-71a2-4b08-a97b-11f49c85e606)

Şikayet kodu tıklayarak “**Onay Bekleyen Şikayetler**”ekranına gelir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7a27a429-efb8-4bc1-a4b9-7cdcecd08933)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd595d02e-c270-4e9f-8907-ac1f771968fd): Şikayeti kapat butonu ile şikayeti kapatma aşamasına gelinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfc615d27-1b97-4d34-b0b2-485561613c50)

Kapatma sekmesinde yeterlilik bilgisi, onay notu yazılabilir ve ek dosya eklenebilir. Şikayet kategorisi bu aşamada değiştirilebilir. Kapatma aşamasındaki dil ayarlarında tanımlanan parametrik alanların bilgi girişi yapılır. Bu parametrik alan tiplerinin tagleri daha sonra rapor formatına eklenerek İç Müşteri Şikayetleri Özet raporuna bilgilerin basılması sağlanacaktır. Bilgiler girildikten sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload47445d5a-ae4d-467f-907b-1887545038da) (kaydet) butonu ile İç Müşteri Şikayet kaydı kapatılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5483685d-31b4-414f-9867-fac0f9577c0e)

### **1.1.3.İç Müşteri Şikayetleri Özet Rapor Formatına Tanımlanan Parametrik Alanların Taglerin Eklenmesi**

İç Müşteri Şikayetleri Özet Raporu tanımlanan parametrik alanların taglerin eklenmesi için SAT\>BSAT\> Konfigürasyon Ayarları\>Rapor Formatları Düzenleme menüsüne gidilir. Qdms tüm raporların yüklendiği menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2c470df7-9540-4ce8-a628-0d510b7c87cb)

**Ekranda bulanan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf67f8ef3-704d-4d61-bb3c-f659e7383765): Sisteme yeni bir rapor formatı yüklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade24c4d5b-d26c-487c-9aab-f9839204004a): Listede seçili olan rapor formatı görüntülenip, indirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload66edb6b6-c0e2-4bdf-924d-8c9a8fec358e): Listede seçili olan rapor formatı silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd6630a52-f080-44c4-89fa-6f72b652db46) (Görüntüle) butonu tıklanarak İç Müşteri Şikayetleri Özet Raporunun rapor format şablonu (IMS_OZET_RAPOR.xls) bilgisayara indirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadec77edc3-d450-47c3-b330-86314d0e2f4a)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload029eff01-9234-42d2-929c-fd4963611736)

Rapor formatına tanımlanan parametrik alanların alan tanımları ve tagleri ilgili bilgiler yazılırak rapor aynı isimde formatı bilgisayara kaydedilir. Örnekte İç Müşteri Şikayetleri Dosya Adı metin tipli parametrik alanın tagi \<PARAM5\> ve İç Müşteri Şikayetleri Dosya Detayı metin (Çoklu Satır) parametrik tipli alanın tagi \<PARAM16\> olacak şekilde rapor formatına yazılır. Diğer tanımlanan parametrik alan tiplerinin tagleri rapor formatınan eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload08793b05-9e18-44cf-b05e-396caa0790f0)

Bilgisayara kaydedilen aynı isimdeki Rapor format (IMS_OZET_RAPOR.xls) ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1262692e-6991-4f2b-8ca6-e3b73cfbb480) (Yeni) butonu ile tekrar rapor formatları menüsüne sisteme yüklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload65b1f6f0-a73b-4d4e-bf53-3f0841c4eb00)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1b619b9e-2540-4eb0-b9eb-ce5588b24995)

Rapor formatları menüsünde aynı isimde rapor format yükleme işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload334a396f-fc45-4f69-9ded-22b7673ffe04)

### **1.1.4. İç Müşteri Şikayetleri Özet Raporunun Rapor Formatına Eklenen Parametrik Alanların Gösterimi**

İç Müşteri Şikayetleri Özet Raporunun rapor formatına (IMS_OZET_RAPOR.xls) tag ekleme işlemi yapılan rapor format yükleme işleminde sonra Entegre Yönetim Sistemi\>İç Müşteri Şikayetleri \>Raporlar\>İç Müşteri Şikayetleri Özet Rapor menüsü tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfec038dc-4f90-40c1-868c-474cb46d4786)

İç Müşteri Şikayetleri Özet Raporu ekranında Şikayetin Tanımı ve Şikayetin ekip lideri yazılarak arama kriterlerine göre filtreler kullanılarak tanımlanıp kapatılan şikayet kaydının aratalarak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0fa8ad36-ffb7-40da-a8f8-a9f103231eac) (Excel’e Aktar) butonu tıklanılır. ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0fa8ad36-ffb7-40da-a8f8-a9f103231eac) (Excel’e Aktar) butonu ile “İç Müşteri Şikayetleri Özet Raporu” Excel formatında görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3e63a076-0cbd-4fec-9d45-07424978b777)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7c1ea4a8-05a9-43ae-a6ec-3b419e83b00f)

## **1.2. İç Müşteri Şikayetleri Modülünde Genel Replacement (Kısa Kodlar) Tag Tablosu**

İç Müşteri Şikayetleri Modülünde kullanılan genel taglerin listesi aşağıdaki tabloda yer almaktadır.

| **Kısaltma (Kısalmalar tag şeklinde \< \> isaretleri arasına yazılacaktır.)** | **Açıklama**                                             |
|-------------------------------------------------------------------------------|----------------------------------------------------------|
| MKOD                                                                          | Müşteri Kodu                                             |
| SKOD                                                                          | Şikayet Kodu                                             |
| MREF                                                                          | Denetimden açılan Müşteri şikayetleri için referans kodu |
| BILDIREN                                                                      | Bildiren kişi                                            |
| BILDIRIMT                                                                     | Bildirim Tarihi                                          |
| SIKAYETG                                                                      | Şikayet oluşturan sicil no                               |
| SISTEMEKT                                                                     | Sisteme ekleme tarihi                                    |
| SORUMLUD                                                                      | Sorumlu departman kodu                                   |
| SIKAYET                                                                       | Şikayet tanımı                                           |
| SIKAYETD                                                                      | Şikayet detayı                                           |
| URUN                                                                          | Ürün kodu                                                |
| SEVKIYATM                                                                     | Toplam geri dönüş miktarı                                |
| SIKAYETM                                                                      | Geri dönüş şikayet miktarı                               |
| GERIODEME                                                                     | Geri dönüş ödeme tutarı                                  |
| ACIKLAMA                                                                      | Açıklama                                                 |
| GELRAPY                                                                       | Planlanan gelisme raporu tarihi                          |
| DURUM                                                                         | Durum bilgisi                                            |
| GELISMEYT                                                                     | Gelişme raporu yazma tarihi                              |
| GELISMERP                                                                     | Gelişme raporu                                           |
| GELEQUSON                                                                     | Gelişme ve Sonuç Raporu Aynı Olsun                       |
| SONRAPY                                                                       | Planlanan sonuç raporu tarihi                            |
| SONRP                                                                         | Sonuç raporu                                             |
| LIDER                                                                         | Lider sicil numarası                                     |
| PARABIRIMI                                                                    | Para birimi                                              |
| GELKYTUSR                                                                     | Gelişme raporu yazan sicili                              |
| SONRAPYT                                                                      | Sonuç raporu yazma tarihi                                |
| SONKYTUSR                                                                     | Sonuç raporunu yazanın sicil numarası                    |
| KAPATAN                                                                       | Kapatan kişinin sicil numarası                           |
| KAPATMAT                                                                      | Kapatma tarihi                                           |
| ICDIS                                                                         | İç veya dış müşteri şikayeti durumu                      |
| SPARISNO                                                                      | Sipariş no                                               |
| IRSALIYENO                                                                    | İrsaliye no                                              |
| SEVKTARIHI                                                                    | Sevk tarihi                                              |
| BIRIMSIKAYETM                                                                 | Geri dönüş şikayet miktar birimi                         |
| BIRIMTOPLAM                                                                   | Toplam geri dönüş miktar birimi                          |
| YETERLILIK                                                                    | Yeterlilik Bilgisi                                       |
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
| REDNEDENI                                                                     | İptal nedeni                                             |
| ISYERI_KODU                                                                   | İş yeri kodu                                             |
| ILKCEV_PLANTAR                                                                | Planlanan ilk cevap tarihi                               |
| ILKCEV_GERTAR                                                                 | Gerçekleşen ilk cevap tarihi                             |
| ILKCEV_GECNED                                                                 | İlk gecikme nedeni                                       |
| SONCEV_PLANTAR                                                                | Planlanan son cevap tarihi                               |
| SONCEV_GERTAR                                                                 | Gerçekleşen son cevap tarihi                             |
| SONCEV_GECNED                                                                 | Son cevap gecikme nedeni                                 |
| PPM_HATALIMIKTAR                                                              | PPMe Yansıyacak Hatalı Miktar                            |
| CVPDA                                                                         | Cevap verme performansında dikkate alınması              |
| SAADA                                                                         | Şikayet adedi analizinde dikkate alınması                |
| MSH                                                                           | Müşteri şikayetinde haklıdır.                            |
| HATA_PER1                                                                     | Hata personel tipli parametrik alan                      |
| HATA_PER2                                                                     | Hata personel tipli parametrik alan                      |
| HATA_PER3                                                                     | Hata personel tipli parametrik alan                      |
| HATA_PER4                                                                     | Hata personel tipli parametrik alan                      |
| HATA_PER5                                                                     | Hata personel tipli parametrik alan                      |
| HATA_PER6                                                                     | Hata personel tipli parametrik alan                      |
| HATA_PER_ORAN1                                                                | Hata personel oranı parametrik alan                      |
| HATA_PER_ORAN2                                                                | Hata personel oranı parametrik alan                      |
| HATA_PER_ORAN3                                                                | Hata personel oranı parametrik alan                      |
| HATA_PER_ORAN4                                                                | Hata personel oranı parametrik alan                      |
| HATA_PER_ORAN5                                                                | Hata personel oranı parametrik alan                      |
| HATA_PER_ORAN6                                                                | Hata personel oranı parametrik alan                      |
| REDDEDEN                                                                      | Reddeden bilgisi                                         |
| SUREC_KODU                                                                    | Süreç kodu                                               |
| ANKET_REF                                                                     | Anket referans kodu                                      |
| GELISME_ALAN1                                                                 | Gelişme parametrik alan                                  |
| GELISME_ALAN2                                                                 | Gelişme parametrik alan                                  |
| GELISME_ALAN3                                                                 | Gelişme parametrik alan                                  |
| PARAM_MIKTAR1                                                                 | Parametrik alan                                          |
| PARAM_MIKTAR2                                                                 | Parametrik alan                                          |
| PARAM_BIRIM1                                                                  | Parametrik alan                                          |
| PARAM_BIRIM2                                                                  | Parametrik alan                                          |
| PARAM2                                                                        | Parametrik alan                                          |
| PARAM3                                                                        | Parametrik alan                                          |
| PARAM4                                                                        | Parametrik alan                                          |
| PARAM5                                                                        | Parametrik alan                                          |
| PARAM6                                                                        | Parametrik alan                                          |
| PARAM7                                                                        | Parametrik alan                                          |
| PARAM8                                                                        | Parametrik alan                                          |
| PARAM9                                                                        | Parametrik alan                                          |
| PARAM10                                                                       | Parametrik alan                                          |
| NPARAM1                                                                       | Nümerik tipli parametrik alan                            |
| NPARAM2                                                                       | Nümerik tipli parametrik alan                            |
| NPARAM3                                                                       | Nümerik tipli parametrik alan                            |
| NPARAM4                                                                       | Nümerik tipli parametrik alan                            |
| NPARAM5                                                                       | Nümerik tipli parametrik alan                            |
| NPARAM6                                                                       | Nümerik tipli parametrik alan                            |
| NPARAM7                                                                       | Nümerik tipli parametrik alan                            |
| NPARAM8                                                                       | Nümerik tipli parametrik alan                            |
| NPARAM9                                                                       | Nümerik tipli parametrik alan                            |
| NPARAM10                                                                      | Nümerik tipli parametrik alan                            |
| NPARAM1_BIRIM                                                                 | Nümerik birim tiplerine ait parametrik alan              |
| NPARAM2_BIRIM                                                                 | Nümerik birim tiplerine ait parametrik alan              |
| NPARAM3_BIRIM                                                                 | Nümerik birim tiplerine ait parametrik alan              |
| NPARAM4_BIRIM                                                                 | Nümerik birim tiplerine ait parametrik alan              |
| NPARAM5_BIRIM                                                                 | Nümerik birim tiplerine ait parametrik alan              |
| NPARAM6_BIRIM                                                                 | Nümerik birim tiplerine ait parametrik alan              |
| NPARAM7_BIRIM                                                                 | Nümerik birim tiplerine ait parametrik alan              |
| NPARAM8_BIRIM                                                                 | Nümerik birim tiplerine ait parametrik alan              |
| NPARAM9_BIRIM                                                                 | Nümerik birim tiplerine ait parametrik alan              |
| NPARAM10_BIRIM                                                                | Nümerik birim tiplerine ait parametrik alan              |
| DPARAM1                                                                       | Tarih tipli parametrik alan                              |
| DPARAM2                                                                       | Tarih tipli parametrik alan                              |
| DPARAM3                                                                       | Tarih tipli parametrik alan                              |
| DPARAM4                                                                       | Tarih tipli parametrik alan                              |
| DPARAM5                                                                       | Tarih tipli parametrik alan                              |
| PPARAM1                                                                       | Personel tipli parametrik alan                           |
| PPARAM2                                                                       | Personel tipli parametrik alan                           |
| PPARAM3                                                                       | Personel tipli parametrik alan                           |
| PPARAM4                                                                       | Personel tipli parametrik alan                           |
| PPARAM5                                                                       | Personel tipli parametrik alan                           |
| LPARAM1                                                                       | Liste tipli parametrik alan                              |
| LPARAM2                                                                       | Liste tipli parametrik alan                              |
| LPARAM3                                                                       | Liste tipli parametrik alan                              |
| LPARAM4                                                                       | Liste tipli parametrik alan                              |
| LPARAM5                                                                       | Liste tipli parametrik alan                              |
| SISTEM_KODU                                                                   | Yönetim sistemi kodu                                     |
| ONAY_DURUM                                                                    | Onay durumu                                              |
| AKSIYON_DURUM                                                                 | Aksiyon Durumu                                           |
| AKSIYON_SONUC_TARIHI                                                          | Aksiyon sonuç tarihi                                     |
| DOF_SONUC_TARIHI                                                              | DOF sonuç tarihi                                         |
| NERDEN                                                                        | Web servisten açılan kayıtlar için                       |
| NERDEN_KOD                                                                    | Web servisten açılan kayıtlar için                       |
| PARAM11                                                                       | Parametrik alan                                          |
| PARAM12                                                                       | Parametrik alan                                          |
| PARAM13                                                                       | Parametrik alan                                          |
| PARAM14                                                                       | Parametrik alan                                          |
| PARAM15                                                                       | Parametrik alan                                          |
| LPARAM6                                                                       | Liste tipli parametrik alan                              |
| LPARAM7                                                                       | Liste tipli parametrik alan                              |
| LPARAM8                                                                       | Liste tipli parametrik alan                              |
| LPARAM9                                                                       | Liste tipli parametrik alan                              |
| LPARAM10                                                                      | Liste tipli parametrik alan                              |
| KAPATMA_PARAM1                                                                | Kapatma Parametrik alan                                  |
| KAPATMA_PARAM3                                                                | Kapatma Parametrik alan                                  |
| KAPATMA_PARAM4                                                                | Kapatma Parametrik alan                                  |
| KAPATMA_PARAM5                                                                | Kapatma Parametrik alan                                  |
| KAPATMA_PARAM6                                                                | Kapatma Parametrik alan                                  |
| KAPATMA_PARAM7                                                                | Kapatma Parametrik alan                                  |
| KAPATMA_PARAM8                                                                | Kapatma Parametrik alan                                  |
| KAPATMA_PARAM9                                                                | Kapatma Parametrik alan                                  |
| KAPATMA_PARAM10                                                               | Kapatma Parametrik alan                                  |
| KAPATMA_LPARAM1                                                               | Kapatma Parametrik alan                                  |
| KAPATMA_LPARAM2                                                               | Kapatma Parametrik alan                                  |
| KAPATMA_LPARAM3                                                               | Kapatma Parametrik alan                                  |
| KAPATMA_LPARAM4                                                               | Kapatma Parametrik alan                                  |
| KAPATMA_LPARAM5                                                               | Kapatma Parametrik alan                                  |
| KAPATMA_LPARAM6                                                               | Kapatma Parametrik alan                                  |
| KAPATMA_LPARAM7                                                               | Kapatma Parametrik alan                                  |
| KAPATMA_LPARAM8                                                               | Kapatma Parametrik alan                                  |
| KAPATMA_LPARAM9                                                               | Kapatma Parametrik alan                                  |
| KAPATMA_LPARAM10                                                              | Kapatma Parametrik alan                                  |
| KAPATMA_NPARAM1                                                               | Kapatma Parametrik alan                                  |
| KAPATMA_NPARAM2                                                               | Kapatma Parametrik alan                                  |
| KAPATMA_NPARAM3                                                               | Kapatma Parametrik alan                                  |
| KAPATMA_NPARAM4                                                               | Kapatma Parametrik alan                                  |
| KAPATMA_NPARAM1_BIRIM                                                         | Kapatma Parametrik alan                                  |
| KAPATMA_NPARAM2_BIRIM                                                         | Kapatma Parametrik alan                                  |
| KAPATMA_NPARAM3_BIRIM                                                         | Kapatma Parametrik alan                                  |
| KAPATMA_NPARAM4_BIRIM                                                         | Kapatma Parametrik alan                                  |
| ESKI_DURUM                                                                    | Önceki durum                                             |
| ESKI_ONAY_DURUM                                                               | Önceki onay durumu                                       |
| ONAY_TARIHI                                                                   | Onay tarihi                                              |
| ARACEV_PLANTAR                                                                | Planlanan ara cevap tarihi                               |
| ARACEV_GERTAR                                                                 | Gerçekleşen ara cevap tarihi                             |
| ARACEV_GECNED                                                                 | Ara gecikme nedeni                                       |
| UPARAM1                                                                       | Ürün tipli parametrik alan                               |
| MPARAM1                                                                       | Müşteri tipli parametrik alan                            |
| TDPARAM1                                                                      | Tedarikçi tipli parametrik alan                          |
| RDFD_NO                                                                       | Risk kodu                                                |
| PARAM17                                                                       | Parametrik alan                                          |
| PARAM18                                                                       | Parametrik alan                                          |
| PARAM19                                                                       | Parametrik alan                                          |
| PARAM20                                                                       | Parametrik alan                                          |
| OTOMATIK_AKSIYON                                                              | Otomatik aksiyon durumu                                  |
| QPARAM1                                                                       | Sorgu tipli parametrik alan                              |
| QPARAM2                                                                       | Sorgu tipli parametrik alan                              |
| QPARAM3                                                                       | Sorgu tipli parametrik alan                              |
| QPARAM4                                                                       | Sorgu tipli parametrik alan                              |
| QPARAM5                                                                       | Sorgu tipli parametrik alan                              |
| LPARAM11                                                                      | Liste tipli parametrik alan                              |
| LPARAM12                                                                      | Liste tipli parametrik alan                              |
| LPARAM13                                                                      | Liste tipli parametrik alan                              |
| LPARAM14                                                                      | Liste tipli parametrik alan                              |
| LPARAM15                                                                      | Liste tipli parametrik alan                              |
| LPARAM16                                                                      | Liste tipli parametrik alan                              |
| LPARAM17                                                                      | Liste tipli parametrik alan                              |
| LPARAM18                                                                      | Liste tipli parametrik alan                              |
| LPARAM19                                                                      | Liste tipli parametrik alan                              |
| LPARAM20                                                                      | Liste tipli parametrik alan                              |
| NPARAM11                                                                      | Nümerik tipli parametrik alan                            |
| NPARAM12                                                                      | Nümerik tipli parametrik alan                            |
| NPARAM13                                                                      | Nümerik tipli parametrik alan                            |
| NPARAM14                                                                      | Nümerik tipli parametrik alan                            |
| NPARAM15                                                                      | Nümerik tipli parametrik alan                            |
| NPARAM16                                                                      | Nümerik tipli parametrik alan                            |
| NPARAM17                                                                      | Nümerik tipli parametrik alan                            |
| NPARAM18                                                                      | Nümerik tipli parametrik alan                            |
| NPARAM19                                                                      | Nümerik tipli parametrik alan                            |
| NPARAM20                                                                      | Nümerik tipli parametrik alan                            |
| NPARAM21                                                                      | Nümerik tipli parametrik alan                            |
| NPARAM22                                                                      | Nümerik tipli parametrik alan                            |
| NPARAM23                                                                      | Nümerik tipli parametrik alan                            |
| NPARAM24                                                                      | Nümerik tipli parametrik alan                            |
| NPARAM25                                                                      | Nümerik tipli parametrik alan                            |
| NPARAM26                                                                      | Nümerik tipli parametrik alan                            |
| NPARAM27                                                                      | Nümerik tipli parametrik alan                            |
| NPARAM28                                                                      | Nümerik tipli parametrik alan                            |
| NPARAM29                                                                      | Nümerik tipli parametrik alan                            |
| NPARAM30                                                                      | Nümerik tipli parametrik alan                            |
| NPARAM11_BIRIM                                                                | Nümerik birim tiplerine ait parametrik alan              |
| NPARAM12_BIRIM                                                                | Nümerik birim tiplerine ait parametrik alan              |
| NPARAM13_BIRIM                                                                | Nümerik birim tiplerine ait parametrik alan              |
| NPARAM14_BIRIM                                                                | Nümerik birim tiplerine ait parametrik alan              |
| NPARAM15_BIRIM                                                                | Nümerik birim tiplerine ait parametrik alan              |
| NPARAM16_BIRIM                                                                | Nümerik birim tiplerine ait parametrik alan              |
| NPARAM17_BIRIM                                                                | Nümerik birim tiplerine ait parametrik alan              |
| NPARAM18_BIRIM                                                                | Nümerik birim tiplerine ait parametrik alan              |
| NPARAM19_BIRIM                                                                | Nümerik birim tiplerine ait parametrik alan              |
| NPARAM20_BIRIM                                                                | Nümerik birim tiplerine ait parametrik alan              |
| NPARAM21_BIRIM                                                                | Nümerik birim tiplerine ait parametrik alan              |
| NPARAM22_BIRIM                                                                | Nümerik birim tiplerine ait parametrik alan              |
| NPARAM23_BIRIM                                                                | Nümerik birim tiplerine ait parametrik alan              |
| NPARAM24_BIRIM                                                                | Nümerik birim tiplerine ait parametrik alan              |
| NPARAM25_BIRIM                                                                | Nümerik birim tiplerine ait parametrik alan              |
| NPARAM26_BIRIM                                                                | Nümerik birim tiplerine ait parametrik alan              |
| NPARAM27_BIRIM                                                                | Nümerik birim tiplerine ait parametrik alan              |
| NPARAM28_BIRIM                                                                | Nümerik birim tiplerine ait parametrik alan              |
| NPARAM29_BIRIM                                                                | Nümerik birim tiplerine ait parametrik alan              |
| NPARAM30_BIRIM                                                                | Nümerik birim tiplerine ait parametrik alan              |
| PARAM21                                                                       | Parametrik alan                                          |
| PARAM22                                                                       | Parametrik alan                                          |
| PARAM23                                                                       | Parametrik alan                                          |
| PARAM24                                                                       | Parametrik alan                                          |
| PARAM25                                                                       | Parametrik alan                                          |
| PARAM31                                                                       | Parametrik alan                                          |
| PARAM32                                                                       | Parametrik alan                                          |
| PARAM33                                                                       | Parametrik alan                                          |
| PARAM34                                                                       | Parametrik alan                                          |
| PARAM35                                                                       | Parametrik alan                                          |
| LPARAM36                                                                      | Liste tipli parametrik alan                              |
| LPARAM37                                                                      | Liste tipli parametrik alan                              |
| LPARAM38                                                                      | Liste tipli parametrik alan                              |
| LPARAM39                                                                      | Liste tipli parametrik alan                              |
| LPARAM40                                                                      | Liste tipli parametrik alan                              |
| NPARAM41                                                                      | Nümerik tipli parametrik alan                            |
| NPARAM42                                                                      | Nümerik tipli parametrik alan                            |
| NPARAM43                                                                      | Nümerik tipli parametrik alan                            |
| NPARAM44                                                                      | Nümerik tipli parametrik alan                            |
| NPARAM45                                                                      | Nümerik tipli parametrik alan                            |
| NPARAM46                                                                      | Nümerik tipli parametrik alan                            |
| NPARAM47                                                                      | Nümerik tipli parametrik alan                            |
| NPARAM48                                                                      | Nümerik tipli parametrik alan                            |
| NPARAM49                                                                      | Nümerik tipli parametrik alan                            |
| NPARAM50                                                                      | Nümerik tipli parametrik alan                            |
| NPARAM41_BIRIM                                                                | Nümerik birim tiplerine ait parametrik alan              |
| NPARAM42_BIRIM                                                                | Nümerik birim tiplerine ait parametrik alan              |
| NPARAM43_BIRIM                                                                | Nümerik birim tiplerine ait parametrik alan              |
| NPARAM44_BIRIM                                                                | Nümerik birim tiplerine ait parametrik alan              |
| NPARAM45_BIRIM                                                                | Nümerik birim tiplerine ait parametrik alan              |
| NPARAM46_BIRIM                                                                | Nümerik birim tiplerine ait parametrik alan              |
| NPARAM47_BIRIM                                                                | Nümerik birim tiplerine ait parametrik alan              |
| NPARAM48_BIRIM                                                                | Nümerik birim tiplerine ait parametrik alan              |
| NPARAM49_BIRIM                                                                | Nümerik birim tiplerine ait parametrik alan              |
| NPARAM50_BIRIM                                                                | Nümerik birim tiplerine ait parametrik alan              |
| KAPATMA_NPARAM5                                                               | Kapatma Parametrik alan                                  |
| KAPATMA_NPARAM6                                                               | Kapatma Parametrik alan                                  |
| KAPATMA_NPARAM7                                                               | Kapatma Parametrik alan                                  |
| KAPATMA_NPARAM8                                                               | Kapatma Parametrik alan                                  |
| KAPATMA_NPARAM9                                                               | Kapatma Parametrik alan                                  |
| KAPATMA_NPARAM10                                                              | Kapatma Parametrik alan                                  |
| KAPATMA_NPARAM5_BIRIM                                                         | Kapatma Parametrik alan                                  |
| KAPATMA_NPARAM6_BIRIM                                                         | Kapatma Parametrik alan                                  |
| KAPATMA_NPARAM7_BIRIM                                                         | Kapatma Parametrik alan                                  |
| KAPATMA_NPARAM8_BIRIM                                                         | Kapatma Parametrik alan                                  |
| KAPATMA_NPARAM9_BIRIM                                                         | Kapatma Parametrik alan                                  |
| KAPATMA_NPARAM10_BIRIM                                                        | Kapatma Parametrik alan                                  |
| DOF_NO                                                                        | DOF no                                                   |
| DEGERLENDIRME                                                                 | Değerlendirme bilgisi                                    |
| DEGERLENDIRME_PUANI                                                           | Değerlendirme puanı bilgisi                              |
| RET_TIPI                                                                      | Ret tipi                                                 |
| TERMINTARIHI                                                                  | Termin Tarihi                                            |
| KAPATMA_DPARAM1                                                               | Kapatma Parametrik alan                                  |
| KAPATMA_DPARAM2                                                               | Kapatma Parametrik alan                                  |
| KAPATMA_DPARAM3                                                               | Kapatma Parametrik alan                                  |
| KAPATMA_DPARAM4                                                               | Kapatma Parametrik alan                                  |
| KAPATMA_DPARAM5                                                               | Kapatma Parametrik alan                                  |
| HATA1_BIRIM                                                                   | Hata tipli parametrik alan                               |
| HATA2_BIRIM                                                                   | Hata tipli parametrik alan                               |
| HATA3_BIRIM                                                                   | Hata tipli parametrik alan                               |
| HATA4_BIRIM                                                                   | Hata tipli parametrik alan                               |
| HATA5_BIRIM                                                                   | Hata tipli parametrik alan                               |
| HATA6_BIRIM                                                                   | Hata tipli parametrik alan                               |
| KAPATMA_PPARAM1                                                               | Kapatma personel tipli parametrik alan                   |
| KAPATMA_PPARAM2                                                               | Kapatma personel tipli parametrik alan                   |
| KAPATMA_PPARAM3                                                               | Kapatma personel tipli parametrik alan                   |
| KAPATMA_PPARAM4                                                               | Kapatma personel tipli parametrik alan                   |
| KAPATMA_PPARAM5                                                               | Kapatma personel tipli parametrik alan                   |
| KAPATMA_QPARAM1                                                               | Kapatma sorgu tipli parametrik alan                      |
| KAPATMA_QPARAM2                                                               | Kapatma sorgu tipli parametrik alan                      |
| KAPATMA_QPARAM3                                                               | Kapatma sorgu tipli parametrik alan                      |
| KAPATMA_QPARAM4                                                               | Kapatma sorgu tipli parametrik alan                      |
| KAPATMA_QPARAM5                                                               | Kapatma sorgu tipli parametrik alan                      |
| MALIYET                                                                       | Maliyet bilgisi                                          |
| MALIYET_BIRIM                                                                 | Maliyet birim bilgisi                                    |
| T2_ADI                                                                        | Müşteri veya Tedarikçi Adı                               |
| T3_ADISOYADI                                                                  | Aksiyon sorumlu adı soyadı                               |
| T4_DEPARTMAN_ADI                                                              | Sorumlu Departman adı                                    |
| T5_URUN_ADI                                                                   | Ürün adı                                                 |
| T6_ADISOYADI                                                                  | Ekip lideri adı soyadı                                   |
| T7_ADISOYADI                                                                  | Gelişme raporu yazan adı soyadı                          |
| T8_ADISOYADI                                                                  | Sonuç raporunu yazanın adı soyadı                        |
| T9_ADISOYADI                                                                  | Kapatan kişinin adı soyadı                               |
| T10_ISYERI_ADI                                                                | İş yeri adı                                              |
| T11_ACIKLAMA                                                                  | Yönetim sistemi                                          |
| MS_T12_URUN_ADI                                                               | Ürün Adı                                                 |
| MS_T12_SORUMLU                                                                | Sorumlu sicil no                                         |
| MS_T12_URUN_TIPI                                                              | Ürün tipi                                                |
| MS_T13_ADISOYADI                                                              | Sorumlu adı soyadı                                       |
| DURUM_ACK                                                                     | Durum açıklması                                          |
| ISLEM_SURESI                                                                  | İşlem süresi                                             |
| ILK_AKSIYON_TARIHI                                                            | İlk aksiyon tarihi                                       |
| T2_TEDARIKCI_ADI                                                              | Tedarikçi adı                                            |
| T2_MUSTERI_ADI                                                                | Müşteri adı                                              |
| URUN_TIPI                                                                     | Ürün tipi                                                |
| URUN_GRUP                                                                     | Ürün grubu                                               |
| IZLEME                                                                        | İzleme                                                   |
| YORUMLAR                                                                      | Yorumlar                                                 |
| KOK_TARIH                                                                     | Kök neden tarihi                                         |
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
| GELISME_PPARAM2_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_PPARAM3_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_PPARAM4_VALUE                                                         | Gelişme parametrik alan                                  |
| GELISME_PPARAM5_VALUE                                                         | Gelişme parametrik alan                                  |
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
| SONUC_PPARAM2_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_PPARAM3_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_PPARAM4_VALUE                                                           | Sonuç parametrik alan                                    |
| SONUC_PPARAM5_VALUE                                                           | Sonuç parametrik alan                                    |
| DEGERLENDIRME_KATEGORISI                                                      | Değerlendirme kategorisi                                 |
| DEGERLENDIRME_ALT_KATEGORISI                                                  | Derlendirme alt kategorisi                               |
| DEGERLENDIRME_TUTAR                                                           | Derlendirme tutar                                        |
| DEGERLENDIRME_TUTAR_BIRIM                                                     | Derlendirme tutar birim                                  |
| DEGERLENDIRME_TARIH                                                           | Derlendirme tarih                                        |
| DEGERLENDIRME_ACIKLAMA                                                        | Derlendirme açıklama                                     |
| DEGERLENDIRME_KATEGORILERI                                                    | Derlendirme kategorileri                                 |
| DEGERLENDIRME_SECENEK                                                         | Derlendirme seçenek                                      |
| DEGERLENDIRME_PUAN                                                            | Derlendirme puan                                         |
| DEGERLENDIRME_MIKTAR                                                          | Derlendirme miktar                                       |
| DEGERLENDIRME_BIRIM                                                           | Derlendirme birim                                        |
| DEGERLENDIRME_DEGERLENDIREN                                                   | Değerlendiren bilgisi                                    |
| DEGERLENDIRME_DEGERLENDIRMET                                                  | Değerlendirme Tarihi                                     |
| ULKE                                                                          | Ulke bilgisi                                             |
| IL                                                                            | İl bilgisi                                               |
| SIKAYET_ANA_KAT_KOD                                                           | Ana şikayet kategori kodu                                |
| SIKAYET_ANA_KAT                                                               | Ana şikayet kategorisi                                   |
| SIKAYET_ALT_KAT_KOD                                                           | Alt şikayet kategori kodu                                |
| SIKAYET_ALT_KAT                                                               | Alt şikayet kategorisi                                   |
| SIKAYET_KODLAR                                                                | Şikayet kodlarının bilgisi                               |
| MS_EKIP                                                                       | Ekip üyeleri                                             |
| MNPARAM1                                                                      | Madde no parametrik alan                                 |
| DOF_AKSIYON_TARIHI                                                            | DOF aksiyon tarihi                                       |
| KOK_NEDENLER                                                                  | Kök nedenler                                             |
| KOK_NEDEN_KIRILIM                                                             | Kök neden kırılımı                                       |
| IZLEME1                                                                       | İzleme parametrik alan                                   |
| SIKAYET_KAT1                                                                  | İzleme parametrik alan                                   |
| IZLEME2                                                                       | İzleme parametrik alan                                   |
| SIKAYET_KAT2                                                                  | İzleme parametrik alan                                   |
| IZLEME3                                                                       | İzleme parametrik alan                                   |
| SIKAYET_KAT3                                                                  | İzleme parametrik alan                                   |
| IZLEME4                                                                       | İzleme parametrik alan                                   |
| SIKAYET_KAT4                                                                  | İzleme parametrik alan                                   |
| IZLEME5                                                                       | İzleme parametrik alan                                   |
| SIKAYET_KAT5                                                                  | İzleme parametrik alan                                   |
| IZLEME6                                                                       | İzleme parametrik alan                                   |
| SIKAYET_KAT6                                                                  | İzleme parametrik alan                                   |
| IZLEME7                                                                       | İzleme parametrik alan                                   |
| SIKAYET_KAT7                                                                  | İzleme parametrik alan                                   |
| IZLEME8                                                                       | İzleme parametrik alan                                   |
| SIKAYET_KAT8                                                                  | İzleme parametrik alan                                   |
| IZLEME9                                                                       | İzleme parametrik alan                                   |
| SIKAYET_KAT9                                                                  | İzleme parametrik alan                                   |
| IZLEME10                                                                      | İzleme parametrik alan                                   |
| SIKAYET_KAT10                                                                 | İzleme parametrik alan                                   |
| IZLEME11                                                                      | İzleme parametrik alan                                   |
| SIKAYET_KAT11                                                                 | İzleme parametrik alan                                   |
| IZLEME12                                                                      | İzleme parametrik alan                                   |
| SIKAYET_KAT12                                                                 | İzleme parametrik alan                                   |
| IZLEME13                                                                      | İzleme parametrik alan                                   |
| SIKAYET_KAT13                                                                 | İzleme parametrik alan                                   |
| IZLEME14                                                                      | İzleme parametrik alan                                   |
| SIKAYET_KAT14                                                                 | İzleme parametrik alan                                   |
| IZLEME15                                                                      | İzleme parametrik alan                                   |
| SIKAYET_KAT15                                                                 | İzleme parametrik alan                                   |
| IZLEME16                                                                      | İzleme parametrik alan                                   |
| SIKAYET_KAT16                                                                 | İzleme parametrik alan                                   |
| IZLEME17                                                                      | İzleme parametrik alan                                   |
| SIKAYET_KAT17                                                                 | İzleme parametrik alan                                   |
| IZLEME18                                                                      | İzleme parametrik alan                                   |
| SIKAYET_KAT18                                                                 | İzleme parametrik alan                                   |
| IZLEME19                                                                      | İzleme parametrik alan                                   |
| SIKAYET_KAT19                                                                 | İzleme parametrik alan                                   |
| IZLEME20                                                                      | İzleme parametrik alan                                   |
| SIKAYET_KAT20                                                                 | İzleme parametrik alan                                   |
| IZLEME21                                                                      | İzleme parametrik alan                                   |
| SIKAYET_KAT21                                                                 | İzleme parametrik alan                                   |
| IZLEME22                                                                      | İzleme parametrik alan                                   |
| SIKAYET_KAT22                                                                 | İzleme parametrik alan                                   |
| IZLEME23                                                                      | İzleme parametrik alan                                   |
| SIKAYET_KAT23                                                                 | İzleme parametrik alan                                   |
| IZLEME24                                                                      | İzleme parametrik alan                                   |
| SIKAYET_KAT24                                                                 | İzleme parametrik alan                                   |
| IZLEME25                                                                      | İzleme parametrik alan                                   |
| SIKAYET_KAT25                                                                 | İzleme parametrik alan                                   |
| IZLEME26                                                                      | İzleme parametrik alan                                   |
| SIKAYET_KAT26                                                                 | İzleme parametrik alan                                   |
| IZLEME27                                                                      | İzleme parametrik alan                                   |
| SIKAYET_KAT27                                                                 | İzleme parametrik alan                                   |
| IZLEME28                                                                      | İzleme parametrik alan                                   |
| SIKAYET_KAT28                                                                 | İzleme parametrik alan                                   |
| IZLEME29                                                                      | İzleme parametrik alan                                   |
| SIKAYET_KAT29                                                                 | İzleme parametrik alan                                   |
| IZLEME30                                                                      | İzleme parametrik alan                                   |
| SIKAYET_KAT30                                                                 | İzleme parametrik alan                                   |
| IZLEME31                                                                      | İzleme parametrik alan                                   |
| SIKAYET_KAT31                                                                 | İzleme parametrik alan                                   |
| IZLEME32                                                                      | İzleme parametrik alan                                   |
| SIKAYET_KAT32                                                                 | İzleme parametrik alan                                   |
| IZLEME33                                                                      | İzleme parametrik alan                                   |
| SIKAYET_KAT33                                                                 | İzleme parametrik alan                                   |
| IZLEME34                                                                      | İzleme parametrik alan                                   |
| SIKAYET_KAT34                                                                 | İzleme parametrik alan                                   |
| IZLEME35                                                                      | İzleme parametrik alan                                   |
| SIKAYET_KAT35                                                                 | İzleme parametrik alan                                   |
| IZLEME36                                                                      | İzleme parametrik alan                                   |
| SIKAYET_KAT36                                                                 | İzleme parametrik alan                                   |
| IZLEME37                                                                      | İzleme parametrik alan                                   |
| SIKAYET_KAT37                                                                 | İzleme parametrik alan                                   |
| IZLEME38                                                                      | İzleme parametrik alan                                   |
| SIKAYET_KAT38                                                                 | İzleme parametrik alan                                   |
| IZLEME39                                                                      | İzleme parametrik alan                                   |
| SIKAYET_KAT39                                                                 | İzleme parametrik alan                                   |
| IZLEME40                                                                      | İzleme parametrik alan                                   |
| SIKAYET_KAT40                                                                 | İzleme parametrik alan                                   |
| IZLEME41                                                                      | İzleme parametrik alan                                   |
| SIKAYET_KAT41                                                                 | İzleme parametrik alan                                   |
| IZLEME42                                                                      | İzleme parametrik alan                                   |
| SIKAYET_KAT42                                                                 | İzleme parametrik alan                                   |
| IZLEME43                                                                      | İzleme parametrik alan                                   |
| SIKAYET_KAT43                                                                 | İzleme parametrik alan                                   |
| IZLEME44                                                                      | İzleme parametrik alan                                   |
| SIKAYET_KAT44                                                                 | İzleme parametrik alan                                   |
| IZLEME45                                                                      | İzleme parametrik alan                                   |
| SIKAYET_KAT45                                                                 | İzleme parametrik alan                                   |
| IZLEME46                                                                      | İzleme parametrik alan                                   |
| SIKAYET_KAT46                                                                 | İzleme parametrik alan                                   |
| IZLEME47                                                                      | İzleme parametrik alan                                   |
| SIKAYET_KAT47                                                                 | İzleme parametrik alan                                   |
| IZLEME48                                                                      | İzleme parametrik alan                                   |
| SIKAYET_KAT48                                                                 | İzleme parametrik alan                                   |
| IZLEME49                                                                      | İzleme parametrik alan                                   |
| SIKAYET_KAT49                                                                 | İzleme parametrik alan                                   |
| IZLEME50                                                                      | İzleme parametrik alan                                   |
| SIKAYET_KAT50                                                                 | İzleme parametrik alan                                   |
| RET_NEDENI                                                                    | Ret nedeni                                               |
| RET_TARIHI                                                                    | Ret tarihi                                               |
| URUN_KODU                                                                     | Ürün kodu                                                |
| SUREC_ADI                                                                     | Süreç Adı                                                |
| HATAMIKTARI                                                                   | Hata miktarı                                             |
| HATATUTARI                                                                    | Hata tutarı                                              |
| HATATUTARI1                                                                   | Hata tutarı parametrik alan                              |
| HATATUTARI2                                                                   | Hata tutarı parametrik alan                              |
| HATATUTARI3                                                                   | Hata tutarı parametrik alan                              |
| HATATUTARI4                                                                   | Hata tutarı parametrik alan                              |
| HATATUTARI5                                                                   | Hata tutarı parametrik alan                              |
| HATATUTARI6                                                                   | Hata tutarı parametrik alan                              |
| KAPATMAONAY_0                                                                 | Kapatma onaycıları ve tarihler(10' a kadar gidiyor)      |
| ACMAONAY_0                                                                    | Açma onaycıları ve tarihler(10' a kadar gidiyor)         |
| KAPATMAONAYTAR_0                                                              | Kapatma onay tarihi(10' a kadar gidiyor)                 |
| ACMAONAYTAR_0                                                                 | Açma onay tarihi(10' a kadar gidiyor)                    |
| ACMASURE_0                                                                    | Açma onay süresi(10' a kadar gidiyor)                    |
| KAPATMASURE_0                                                                 | Kapatma onay süresi(10' a kadar gidiyor)                 |
| ACMAONAYNOTU_0                                                                | Açma onay notu(10' a kadar gidiyor)                      |
| KAPATMAONAYNOTU_0                                                             | Kapatma onay notu(10' a kadar gidiyor)                   |
| ACMABASLAMATARIHI_0                                                           | Açma onayı başlama tarihi(10' a kadar gidiyor)           |
| TOPLAM_ACMASURE                                                               | Toplam açma onay süresi                                  |
| TOPLAM_KAPATMASURE                                                            | Toplam kapatma onay süresi                               |

## **1.3. İç Müşteri Şikayetleri Modülünde İç Müşteri Şikayetleri Aksiyon 3 Raporu Replacement (Kısa Kodlar) Tag Tablosu**

İç Müşteri Şikayetleri Modülünde kullanılan İç Müşteri Şikayetleri Aksiyon 3 Rapor taglerin listesi aşağıdaki tabloda yer almaktadır.

| **Kısaltma (Kısalmalar tag şeklinde \< \> isaretleri arasına yazılacaktır.)** | **Açıklama**                                        |
|-------------------------------------------------------------------------------|-----------------------------------------------------|
| SUREC_ADI                                                                     | Süreç adı                                           |
| KOK_NEDENLER                                                                  | Kök nedenler                                        |
| KOK_NEDEN_KIRILIM                                                             | Kök neden kırılımı                                  |
| KAPATMAT                                                                      | Kapatma tarihi                                      |
| T9_ADISOYADI                                                                  | Kapatan kişinin adı soyadı                          |
| T11_ACIKLAMA                                                                  | Yönetim sistemi                                     |
| T5_URUN_ADI                                                                   | Ürün adı                                            |
| T10_ISYERI_ADI                                                                | İş yeri adı                                         |
| T4_DEPARTMAN_ADI                                                              | Departman adı                                       |
| T6_ADISOYADI                                                                  | Ekip lideri adı soyadı                              |
| SISTEMEKT                                                                     | Sisteme ekleme tarihi                               |
| SIKAYETG                                                                      | Şikayet oluşturan sicil no                          |
| SIKAYETD                                                                      | Şikayet detayı                                      |
| SIKAYET_KAT                                                                   | Şikayet kategorisi                                  |
| SIKAYET                                                                       | Şikayet tanımı                                      |
| AKS_T5_MKOD                                                                   | Müşteri kodu                                        |
| AKS_T5_SKOD                                                                   | Şikayet kodu                                        |
| AKS_T5_ICDIS                                                                  | İç veya dış müşteri şikayeti durumu                 |
| AKS_T5_SIKAYET_TANIM                                                          | Şikayet Tanımı                                      |
| AKS_MS_DURUM                                                                  | Durum                                               |
| AKS_SIKAYETG                                                                  | Şikayet oluşturan sicil no                          |
| AKS_ROW_NUMBER                                                                | Satır no                                            |
| AKS_NO                                                                        | Aksiyon no                                          |
| AKS_AKSIYON                                                                   | Aksiyon bilgisi                                     |
| AKS_YAPACAK                                                                   | Yapacak sicil no                                    |
| AKS_SORUMLU                                                                   | Sorumlu sicil no                                    |
| AKS_PLANT                                                                     | Plan tarihi                                         |
| AKS_YAPILAN                                                                   | Yapılanların açıklaması                             |
| AKS_YAPT                                                                      | Yapılma tarihi                                      |
| AKS_STDNO                                                                     | Madde no                                            |
| AKS_DOCNO                                                                     | Doküman no                                          |
| AKS_SISTEMEGIREN                                                              | Sisteme giren sicil no                              |
| AKS_TIP                                                                       | Aksiyon tipi                                        |
| AKS_KAYITTARIHI                                                               | Kayıt tarihi                                        |
| AKS_REVPLANT                                                                  | Planlanan revizyon tarihi                           |
| AKS_GECIKMENEDENI                                                             | Gecikme nedeni                                      |
| AKS_GECIKTI                                                                   | Gecikme durumu                                      |
| AKS_YAPACAKD                                                                  | Yapacak departman                                   |
| AKS_MSKOD                                                                     | Müşteri şikayet kodu                                |
| AKS_ALAN1                                                                     | Parametrik alan                                     |
| AKS_ALAN2                                                                     | Parametrik alan                                     |
| AKS_ALAN3                                                                     | Parametrik alan                                     |
| AKS_ALAN4                                                                     | Parametrik alan                                     |
| AKS_ALAN5                                                                     | Parametrik alan                                     |
| AKS_NPARAM1                                                                   | Parametrik alan                                     |
| AKS_NPARAM2                                                                   | Parametrik alan                                     |
| AKS_NPARAM3                                                                   | Parametrik alan                                     |
| AKS_NPARAM4                                                                   | Parametrik alan                                     |
| AKS_NPARAM1_BIRIM                                                             | Parametrik alan                                     |
| AKS_NPARAM2_BIRIM                                                             | Parametrik alan                                     |
| AKS_NPARAM3_BIRIM                                                             | Parametrik alan                                     |
| AKS_NPARAM4_BIRIM                                                             | Parametrik alan                                     |
| AKS_LPARAM1                                                                   | Parametrik alan                                     |
| AKS_LPARAM2                                                                   | Parametrik alan                                     |
| AKS_LPARAM3                                                                   | Parametrik alan                                     |
| AKS_DURUM                                                                     | Durum                                               |
| AKS_ONAY_DURUM                                                                | Onay durumu                                         |
| AKS_YAYINLANDI                                                                | Yayınlanma durumu                                   |
| AKS_ACIKLAMA                                                                  | Açıklama                                            |
| AKS_QPARAM1                                                                   | Parametrik alan                                     |
| AKS_QPARAM2                                                                   | Parametrik alan                                     |
| AKS_QPARAM3                                                                   | Parametrik alan                                     |
| AKS_QPARAM4                                                                   | Parametrik alan                                     |
| AKS_QPARAM5                                                                   | Parametrik alan                                     |
| AKS_DPARAM1                                                                   | Parametrik alan                                     |
| AKS_DPARAM2                                                                   | Parametrik alan                                     |
| AKS_DPARAM3                                                                   | Parametrik alan                                     |
| AKS_RET_TIPI                                                                  | Ret tipi                                            |
| AKS_SIRA_NO                                                                   | Sıra no                                             |
| AKS_PPARAM1                                                                   | Parametrik alan                                     |
| AKS_PPARAM2                                                                   | Parametrik alan                                     |
| AKS_PPARAM3                                                                   | Parametrik alan                                     |
| AKS_PPARAM4                                                                   | Parametrik alan                                     |
| AKS_PPARAM5                                                                   | Parametrik alan                                     |
| AKS_T2_ADISOYADI                                                              | Aksiyon yapacak adı soyadı                          |
| AKS_T3_ADISOYADI                                                              | Aksiyon sorumlu adı soyadı                          |
| AKS_T4_ADISOYADI                                                              | Sisteme giren adı soyadı                            |
| AKS_T5_URUN                                                                   | Ürün tanımı                                         |
| AKS_T5_SIKAYET                                                                | Şikayet tanımı                                      |
| AKS_T5_SIKAYETD                                                               | Şikayet detayı                                      |
| AKS_T5_LIDER                                                                  | Lider sicil numarası                                |
| AKS_T5_KAPATAN                                                                | Kapatan kişinin sicil numarası                      |
| AKS_T5_KAPATMAT                                                               | Kapatma tarihi                                      |
| AKS_T5_SORUMLUD                                                               | Sorumlu departman kodu                              |
| AKS_T5_SISTEMEKT                                                              | Sisteme ekleme tarihi                               |
| AKS_T6_URUN_ADI                                                               | Ürün adı                                            |
| AKS_T6_URUN_GRUP                                                              | Ürün grubu                                          |
| AKS_T7_ADISOYADI                                                              | Lider adı soyadı                                    |
| AKS_T8_ADISOYADI                                                              | Kapatan adı soyadı                                  |
| AKS_T9_DEPARTMAN_ADI                                                          | Departman adı                                       |
| AKS_T10_URUN_ADI                                                              | Ürün adı                                            |
| AKS_T10_SORUMLU                                                               | Sorumlu sicil no                                    |
| AKS_T10_URUN_TIPI                                                             | Ürüm tipi                                           |
| AKS_T11_ADISOYADI                                                             | Sorumlu Adı soyadı                                  |
| AKS_MSKOD_TANIM                                                               | Müşteri şikayetleri kodu ve sikayet tanımı          |
| AKS_STATU                                                                     | Statü                                               |
| AKS_MSKOD_ROWNUMBER                                                           | Satır no                                            |
| AKS_SIKAYET_KAT                                                               | Şikayet kategorisi                                  |
| AKS_MD                                                                        | Müşteri kodu                                        |
| AKS_MSKOD_NO                                                                  | Satır no                                            |
| AKS_KAPATAN                                                                   | Kapatan adı soyadı                                  |
| AKS_KAPATMAONAY_0                                                             | Kapatma onaycıları ve tarihler(10' a kadar gidiyor) |
| AKS_ACMAONAY_0                                                                | Açma onaycıları ve tarihler(10' a kadar gidiyor)    |
| AKS_KAPATMAONAYTAR_0                                                          | Kapatma onaycıları ve tarihler(10' a kadar gidiyor) |
| AKS_ACMAONAYTAR_0                                                             | Açma onay tarihi(10' a kadar gidiyor)               |
| AKS_ACMASURE_0                                                                | Açma onay süresi(10' a kadar gidiyor)               |
| AKS_KAPATMASURE_0                                                             | Kapatma onay süresi(10' a kadar gidiyor)            |
| AKS_TOPLAM_ACMASURE                                                           | Toplam açma onay süresi                             |
| AKS_TOPLAM_KAPATMASURE                                                        | Toplam Kapatma onay süresi                          |
| AKS_REVIZYON_BITIS_TARIHI                                                     | Reviyon bitiş tarihi                                |
| AKS_GECIKME_NEDENI                                                            | Gecikme nedeni                                      |
| AKS_YAPACAK_DEPARTMAN_ADI                                                     | Aksiyon Yapacak departman adı                       |
| SIRA_NO                                                                       | Sıra no                                             |
| YAPACAK_DEPARTMAN_ADI                                                         | Departman adı                                       |
| GECIKME_NEDENI                                                                | Gecikme nedeni                                      |
| REVIZYON_BITIS_TARIHI                                                         | Revizyon bitiş tarihi                               |
| KAYITTARIHI                                                                   | Kayıt tarihi                                        |
| SISTEMEGIREN                                                                  | Sisteme giren adı soyadı                            |
| YAPT                                                                          | Yapılma tarihi                                      |
| YAPILAN                                                                       | Yapılanların açıklaması                             |
| REVPLANT                                                                      | Revizyon plan tarihi                                |
| PLANT                                                                         | Plan tarihi                                         |
| YAPACAK                                                                       | Yapacak sicil no                                    |
| SORUMLU                                                                       | Sorumlu sicil no                                    |
| STATU                                                                         | Statü                                               |
| AKSIYON                                                                       | Aksiyon bilgisi                                     |
| NO                                                                            | Aksiyon no                                          |
| MSKOD_NO                                                                      | Müşteri kod no                                      |

## **1.4. İç Müşteri Şikayetleri Modülünde Tekli Raporu Replacement (Kısa Kodlar) Tag Tablosu**

İç Müşteri Şikayetleri Modülünde kullanılan İç Müşteri Şikayetleri Modülünde Tekli Rapor taglerin listesi aşağıdaki tabloda yer almaktadır.

| **Kısaltma (Kısalmalar tag şeklinde \< \> isaretleri arasına yazılacaktır.)** | **Açıklama**                                            |
|-------------------------------------------------------------------------------|---------------------------------------------------------|
| MKOD                                                                          | Müşteri Kodu                                            |
| SKOD                                                                          | Şikayet Kodu                                            |
| MUSADI                                                                        | Müşteri adı                                             |
| DEPARTMAN                                                                     | Departman adı                                           |
| DOF_NO                                                                        | DOF no                                                  |
| DEGERLENDIRME_PUANI                                                           | Değerlendirme puanı                                     |
| SISTEMEKT                                                                     | Sisteme ekleme tarihi                                   |
| ACMA_TARIHI                                                                   | Açma tarihi                                             |
| ONAY_TARIHI                                                                   | Onay Tarihi                                             |
| SIKAYETG                                                                      | Şikayet oluşturan adı soyadı                            |
| ACAN                                                                          | Şikayet açan adı soyadı                                 |
| LIDER                                                                         | Lider sicil numarası                                    |
| SISTEM                                                                        | Yönetim sistemi                                         |
| MNPARAM1                                                                      | Madde no parametrik alan                                |
| ISYERI                                                                        | İş yeri adı bilgisi                                     |
| EKIP                                                                          | Ekip üyelerinin adı soyadı                              |
| SORUMLUD                                                                      | Sorumlu departman kodu                                  |
| URUN_KODU                                                                     | Ürün kodu                                               |
| URUN_TIPI                                                                     | Ürün tipi                                               |
| BILGILENDIRME                                                                 | Bilgilendirilecek kişinin adı soyadı                    |
| GELRAPY                                                                       | Planlanan gelisme raporu tarihi                         |
| SIKAYETKONUSU                                                                 | Şikayet konusu                                          |
| UYGKAT                                                                        | Uygulama kategorisi                                     |
| SIKAYETKATEGORISI                                                             | Şikayet kategorisi                                      |
| YORUMLAR                                                                      | Yorum yapanlar ve yorum bilgilerinin tamamı             |
| IZLEME                                                                        | İzlemeye iat bilgilerin tümü                            |
| ACMAONAY_0                                                                    | Açma onaycıları ve tarihler(10' a kadar gidiyor)        |
| ACMAONAY_TUMU_0                                                               | Açma onaycıları ve tarihler tümü(10' a kadar gidiyor)   |
| DEGERLENDIRME_KATEGORISI                                                      | Değerlendirme kategorisi                                |
| DEGERLENDIRME_BILGISI                                                         | Değerlendirme bilgisi                                   |
| DEGERLENDIRME_ALT_KATEGORISI                                                  | Değerlendirme alt kategorisi                            |
| DEGERLENDIRME_TUTAR                                                           | Değerlendirme tutar                                     |
| DEGERLENDIRME_TUTAR_BIRIM                                                     | Değerlendirme tutar birimi                              |
| DEGERLENDIRME_ACIKLAMA                                                        | Değerlendirme açıklama                                  |
| DEGERLENDIRME_TARIH                                                           | Değerlendirme tarihi                                    |
| DEGERLENDIRME_SECENEK                                                         | Değerlendirme seçenek                                   |
| DEGERLENDIRME_PUAN                                                            | Değerlendirme puanı                                     |
| DEGERLENDIRME_MIKTAR                                                          | Değerlendirme miktar                                    |
| DEGERLENDIRME_BIRIM                                                           | Değerlendirme birim                                     |
| DEGERLENDIRME_DEGERLENDIREN                                                   | Değerlendiren                                           |
| DEGERLENDIRME_DEGERLENDIRMET                                                  | Değerlendirme Tarihi                                    |
| DEGERLENDIRME_KATEGORILERI                                                    | Değerlendirme kategorileri                              |
| HATAMIKTARI1                                                                  | Hata parametrik alan                                    |
| HATAMIKTARI2                                                                  | Hata parametrik alan                                    |
| HATAMIKTARI3                                                                  | Hata parametrik alan                                    |
| HATAMIKTARI4                                                                  | Hata parametrik alan                                    |
| HATAMIKTARI5                                                                  | Hata parametrik alan                                    |
| HATAMIKTARI6                                                                  | Hata parametrik alan                                    |
| HATATUTARI1                                                                   | Hata parametrik alan                                    |
| HATATUTARI2                                                                   | Hata parametrik alan                                    |
| HATATUTARI3                                                                   | Hata parametrik alan                                    |
| HATATUTARI4                                                                   | Hata parametrik alan                                    |
| HATATUTARI5                                                                   | Hata parametrik alan                                    |
| HATATUTARI6                                                                   | Hata parametrik alan                                    |
| HATALIBOLUM1                                                                  | Hata parametrik alan                                    |
| HATALIBOLUM2                                                                  | Hata parametrik alan                                    |
| HATALIBOLUM3                                                                  | Hata parametrik alan                                    |
| HATALIBOLUM4                                                                  | Hata parametrik alan                                    |
| HATALIBOLUM5                                                                  | Hata parametrik alan                                    |
| HATALIBOLUM6                                                                  | Hata parametrik alan                                    |
| HATAORANI1                                                                    | Hata parametrik alan                                    |
| HATAORANI2                                                                    | Hata parametrik alan                                    |
| HATAORANI3                                                                    | Hata parametrik alan                                    |
| HATAORANI4                                                                    | Hata parametrik alan                                    |
| HATAORANI5                                                                    | Hata parametrik alan                                    |
| HATAORANI6                                                                    | Hata parametrik alan                                    |
| HATAMIKTARI                                                                   | Hata parametrik alan                                    |
| HATATUTARI                                                                    | Hata parametrik alan                                    |
| MALIYET_BIRIM                                                                 | Hata parametrik alan                                    |
| HATA_PER1                                                                     | Hata parametrik alan                                    |
| HATA_PER_ORAN1                                                                | Hata parametrik alan                                    |
| HATA_PER2                                                                     | Hata parametrik alan                                    |
| HATA_PER_ORAN2                                                                | Hata parametrik alan                                    |
| HATA_PER3                                                                     | Hata parametrik alan                                    |
| HATA_PER_ORAN3                                                                | Hata parametrik alan                                    |
| HATA_PER4                                                                     | Hata parametrik alan                                    |
| HATA_PER_ORAN4                                                                | Hata parametrik alan                                    |
| HATA_PER5                                                                     | Hata parametrik alan                                    |
| HATA_PER_ORAN5                                                                | Hata parametrik alan                                    |
| HATA_PER6                                                                     | Hata parametrik alan                                    |
| HATA_PER_ORAN6                                                                | Hata parametrik alan                                    |
| GERI_DONUSLER                                                                 | Geri dönüş bilgileri                                    |
| PPM_HATALIMIKTAR                                                              | PPMe Yansıyacak Hatalı Miktar                           |
| CVPDA                                                                         | Cevap verme performansında dikkate alınması             |
| SAADA                                                                         | Şikayet adedi analizinde dikkate alınması               |
| MSH                                                                           | Müşteri şikayetinde haklıdır.                           |
| KOKNEDEN                                                                      | Tüm kök neden analizlerine ait neden ve açıklamaları    |
| SIKAYET                                                                       | Şikayet tanımı                                          |
| SIKAYETD                                                                      | Şikayet detayı                                          |
| GELISMERP                                                                     | Gelişme raporu                                          |
| GELKYTUSR                                                                     | Gelişme raporu yazanın sicil numarası                   |
| GELISMEYT                                                                     | Gelişme raporu yazma tarihi                             |
| SONRAPY                                                                       | Planlanan sonuç raporu tarihi                           |
| SONRAPYT                                                                      | Sonuç raporu yazma tarihi                               |
| SONRP                                                                         | Sonuç raporu                                            |
| KAPALIMI                                                                      | Kapatma durumu                                          |
| KAPATMAT                                                                      | Kapatma tarihi                                          |
| KAPATAN                                                                       | Kapatan kişinin sicil numarası                          |
| SUREC_KODU                                                                    | Süreç kodu                                              |
| SUREC_ADI                                                                     | Süreç adı                                               |
| SUREC                                                                         | Süreç                                                   |
| YETERLILIK                                                                    | Yeterlilil                                              |
| GELISME_LPARAM1                                                               | Gelişme Liste tipli parametrik alan                     |
| GELISME_LPARAM10                                                              | Gelişme Liste tipli parametrik alan                     |
| GELISME_LPARAM2                                                               | Gelişme Liste tipli parametrik alan                     |
| GELISME_LPARAM3                                                               | Gelişme Liste tipli parametrik alan                     |
| GELISME_LPARAM4                                                               | Gelişme Liste tipli parametrik alan                     |
| GELISME_LPARAM5                                                               | Gelişme Liste tipli parametrik alan                     |
| GELISME_LPARAM6                                                               | Gelişme Liste tipli parametrik alan                     |
| GELISME_LPARAM7                                                               | Gelişme Liste tipli parametrik alan                     |
| GELISME_LPARAM8                                                               | Gelişme Liste tipli parametrik alan                     |
| GELISME_LPARAM9                                                               | Gelişme Liste tipli parametrik alan                     |
| GELISME_NPARAM1                                                               | Gelişme nümerik tipli parametrik alan                   |
| GELISME_NPARAM2                                                               | Gelişme nümerik tipli parametrik alan                   |
| GELISME_NPARAM3                                                               | Gelişme nümerik tipli parametrik alan                   |
| GELISME_NPARAM4                                                               | Gelişme nümerik tipli parametrik alan                   |
| GELISME_NPARAM5                                                               | Gelişme nümerik tipli parametrik alan                   |
| GELISME_PARAM1                                                                | Gelişme parametrik alan                                 |
| GELISME_PARAM10                                                               | Gelişme parametrik alan                                 |
| GELISME_PARAM2                                                                | Gelişme parametrik alan                                 |
| GELISME_PARAM3                                                                | Gelişme parametrik alan                                 |
| GELISME_PARAM4                                                                | Gelişme parametrik alan                                 |
| GELISME_PARAM5                                                                | Gelişme parametrik alan                                 |
| GELISME_PARAM6                                                                | Gelişme parametrik alan                                 |
| GELISME_PARAM7                                                                | Gelişme parametrik alan                                 |
| GELISME_PARAM8                                                                | Gelişme parametrik alan                                 |
| GELISME_PARAM9                                                                | Gelişme parametrik alan                                 |
| GELISME_PPARAM1                                                               | Gelişme personel tipli parametrik alan                  |
| GELISME_PPARAM2                                                               | Gelişme personel tipli parametrik alan                  |
| GELISME_PPARAM3                                                               | Gelişme personel tipli parametrik alan                  |
| GELISME_PPARAM4                                                               | Gelişme personel tipli parametrik alan                  |
| GELISME_PPARAM5                                                               | Gelişme personel tipli parametrik alan                  |
| GELISME_QPARAM1                                                               | Gelişme sorgu tipli parametrik alan                     |
| GELISME_QPARAM2                                                               | Gelişme sorgu tipli parametrik alan                     |
| GELISME_QPARAM3                                                               | Gelişme sorgu tipli parametrik alan                     |
| GELISME_QPARAM4                                                               | Gelişme sorgu tipli parametrik alan                     |
| GELISME_QPARAM5                                                               | Gelişme sorgu tipli parametrik alan                     |
| KAPATMA_PARAM2                                                                | Kapatma parametrik alan                                 |
| PARAM1                                                                        | Parametrik alan                                         |
| PARAM16                                                                       | Parametrik alan                                         |
| SONUC_LPARAM1                                                                 | Sonuç liste tipli parametrik alan                       |
| SONUC_LPARAM10                                                                | Sonuç liste tipli parametrik alan                       |
| SONUC_LPARAM2                                                                 | Sonuç liste tipli parametrik alan                       |
| SONUC_LPARAM3                                                                 | Sonuç liste tipli parametrik alan                       |
| SONUC_LPARAM4                                                                 | Sonuç liste tipli parametrik alan                       |
| SONUC_LPARAM5                                                                 | Sonuç liste tipli parametrik alan                       |
| SONUC_LPARAM6                                                                 | Sonuç liste tipli parametrik alan                       |
| SONUC_LPARAM7                                                                 | Sonuç liste tipli parametrik alan                       |
| SONUC_LPARAM8                                                                 | Sonuç liste tipli parametrik alan                       |
| SONUC_LPARAM9                                                                 | Sonuç liste tipli parametrik alan                       |
| SONUC_NPARAM1                                                                 | Sonuç nümerik tipli parametrik alan                     |
| SONUC_NPARAM2                                                                 | Sonuç nümerik tipli parametrik alan                     |
| SONUC_NPARAM3                                                                 | Sonuç nümerik tipli parametrik alan                     |
| SONUC_NPARAM4                                                                 | Sonuç nümerik tipli parametrik alan                     |
| SONUC_NPARAM5                                                                 | Sonuç nümerik tipli parametrik alan                     |
| SONUC_PARAM1                                                                  | Sonuç parametrik alan                                   |
| SONUC_PARAM10                                                                 | Sonuç parametrik alan                                   |
| SONUC_PARAM2                                                                  | Sonuç parametrik alan                                   |
| SONUC_PARAM3                                                                  | Sonuç parametrik alan                                   |
| SONUC_PARAM4                                                                  | Sonuç parametrik alan                                   |
| SONUC_PARAM5                                                                  | Sonuç parametrik alan                                   |
| SONUC_PARAM6                                                                  | Sonuç parametrik alan                                   |
| SONUC_PARAM7                                                                  | Sonuç parametrik alan                                   |
| SONUC_PARAM8                                                                  | Sonuç parametrik alan                                   |
| SONUC_PARAM9                                                                  | Sonuç parametrik alan                                   |
| SONUC_PPARAM1                                                                 | Sonuç personel tipli parametrik alan                    |
| SONUC_PPARAM2                                                                 | Sonuç personel tipli parametrik alan                    |
| SONUC_PPARAM3                                                                 | Sonuç personel tipli parametrik alan                    |
| SONUC_PPARAM4                                                                 | Sonuç personel tipli parametrik alan                    |
| SONUC_PPARAM5                                                                 | Sonuç personel tipli parametrik alan                    |
| SONUC_QPARAM1                                                                 | Sonuç sorgu tipli parametrik alan                       |
| SONUC_QPARAM2                                                                 | Sonuç sorgu tipli parametrik alan                       |
| SONUC_QPARAM3                                                                 | Sonuç sorgu tipli parametrik alan                       |
| SONUC_QPARAM4                                                                 | Sonuç sorgu tipli parametrik alan                       |
| SONUC_QPARAM5                                                                 | Sonuç sorgu tipli parametrik alan                       |
| DOSYALAR                                                                      | Ek dosya bilgileri                                      |
| RET_NEDENI                                                                    | Ret nedeni                                              |
| REDDEDEN                                                                      | Redden sicil numarası                                   |
| RET_TARIHI                                                                    | Reddedilme tarihi                                       |
| REDNEDENI                                                                     | İptal nedeni                                            |
| KOK_MSKOD                                                                     | Kök neden müşteri şikayet kodu                          |
| KOK_KOKNO                                                                     | Kök neden numarası                                      |
| KOK_ACIKLAMA                                                                  | Kök neden açıklama                                      |
| KOK_SISTEMG                                                                   | Kök nedeni sisteme giren sicil no                       |
| KOK_SISTEMG_TARIH                                                             | Kök neden sisteme giriş tarihi                          |
| KOK_PARAM1                                                                    | Parametrik alan                                         |
| KOK_PARAM2                                                                    | Parametrik alan                                         |
| KOK_PARAM3                                                                    | Parametrik alan                                         |
| KOK_DPARAM1                                                                   | Parametrik alan                                         |
| KOK_DPARAM2                                                                   | Parametrik alan                                         |
| KOK_DPARAM3                                                                   | Parametrik alan                                         |
| KOK_NAPARAM1                                                                  | Parametrik alan                                         |
| KOK_NAPARAM2                                                                  | Parametrik alan                                         |
| KOK_NAPARAM3                                                                  | Parametrik alan                                         |
| KOK_NCPARAM1                                                                  | Parametrik alan                                         |
| KOK_NCPARAM2                                                                  | Parametrik alan                                         |
| KOK_NCPARAM3                                                                  | Parametrik alan                                         |
| KOK_LPARAM1                                                                   | Parametrik alan                                         |
| KOK_LPARAM2                                                                   | Parametrik alan                                         |
| KOK_LPARAM3                                                                   | Parametrik alan                                         |
| KOK_NAPARAM1_BIRIM                                                            | Parametrik alan                                         |
| KOK_NAPARAM2_BIRIM                                                            | Parametrik alan                                         |
| KOK_NAPARAM3_BIRIM                                                            | Parametrik alan                                         |
| KOK_NCPARAM1_BIRIM                                                            | Parametrik alan                                         |
| KOK_NCPARAM2_BIRIM                                                            | Parametrik alan                                         |
| KOK_NCPARAM3_BIRIM                                                            | Parametrik alan                                         |
| KOK_KOK_PPARAM1                                                               | Parametrik alan                                         |
| KOK_KOK_PPARAM2                                                               | Parametrik alan                                         |
| KOK_KOK_PPARAM3                                                               | Parametrik alan                                         |
| KOK_KOK_PPARAM4                                                               | Parametrik alan                                         |
| KOK_KOK_PPARAM5                                                               | Parametrik alan                                         |
| KOK_KOK_QPARAM1                                                               | Parametrik alan                                         |
| KOK_KOK_QPARAM2                                                               | Parametrik alan                                         |
| KOK_KOK_QPARAM3                                                               | Parametrik alan                                         |
| KOK_KOK_QPARAM4                                                               | Parametrik alan                                         |
| KOK_KOK_QPARAM5                                                               | Parametrik alan                                         |
| KOK_T2_NEDEN                                                                  | Kök neden analizine ait neden                           |
| KOK_T3_ADISOYADI                                                              | Sisteme giren adı soyadı                                |
| KOK_LPARAM1_VALUE                                                             | Parametrik alan                                         |
| KOK_LPARAM2_VALUE                                                             | Parametrik alan                                         |
| KOK_LPARAM3_VALUE                                                             | Parametrik alan                                         |
| KOK_NAPARAM1_VALUE                                                            | Parametrik alan                                         |
| KOK_NAPARAM2_VALUE                                                            | Parametrik alan                                         |
| KOK_NAPARAM3_VALUE                                                            | Parametrik alan                                         |
| KOK_NCPARAM1_VALUE                                                            | Parametrik alan                                         |
| KOK_NCPARAM2_VALUE                                                            | Parametrik alan                                         |
| KOK_NCPARAM3_VALUE                                                            | Parametrik alan                                         |
| AKS_NO                                                                        | Aksiyon no                                              |
| AKS_AKSIYON                                                                   | Aksiyon bilgisi                                         |
| AKS_YAPACAK                                                                   | Yapacak sicil no                                        |
| AKS_SORUMLU                                                                   | Sorumlu sicil no                                        |
| AKS_PLANT                                                                     | Plan tarihi                                             |
| AKS_YAPILAN                                                                   | Yapılanların açıklaması                                 |
| AKS_YAPT                                                                      | Yapılma tarihi                                          |
| AKS_STDNO                                                                     | Madde no                                                |
| AKS_DOCNO                                                                     | Doküman no                                              |
| AKS_SISTEMEGIREN                                                              | Sisteme giren sicil no                                  |
| AKS_TIP                                                                       | Aksiyon tipi                                            |
| AKS_KAYITTARIHI                                                               | Kayıt tarihi                                            |
| AKS_REVPLANT                                                                  | Planlanan revizyon tarihi                               |
| AKS_GECIKMENEDENI                                                             | Gecikme nedeni                                          |
| AKS_GECIKTI                                                                   | Gecikme durumu                                          |
| AKS_ALAN1                                                                     | Parametrik alan                                         |
| AKS_ALAN2                                                                     | Parametrik alan                                         |
| AKS_ALAN3                                                                     | Parametrik alan                                         |
| AKS_ALAN4                                                                     | Parametrik alan                                         |
| AKS_ALAN5                                                                     | Parametrik alan                                         |
| AKS_NPARAM1                                                                   | Parametrik alan                                         |
| AKS_NPARAM2                                                                   | Parametrik alan                                         |
| AKS_NPARAM3                                                                   | Parametrik alan                                         |
| AKS_NPARAM4                                                                   | Parametrik alan                                         |
| AKS_NPARAM1_BIRIM                                                             | Parametrik alan                                         |
| AKS_NPARAM2_BIRIM                                                             | Parametrik alan                                         |
| AKS_NPARAM3_BIRIM                                                             | Parametrik alan                                         |
| AKS_NPARAM4_BIRIM                                                             | Parametrik alan                                         |
| AKS_LPARAM1                                                                   | Parametrik alan                                         |
| AKS_LPARAM2                                                                   | Parametrik alan                                         |
| AKS_LPARAM3                                                                   | Parametrik alan                                         |
| AKS_DURUM                                                                     | Durum                                                   |
| AKS_ONAY_DURUM                                                                | Onay durumu                                             |
| AKS_YAYINLANDI                                                                | Yayınlanma durumu                                       |
| AKS_ACIKLAMA                                                                  | Açıklama                                                |
| AKS_QPARAM1                                                                   | Parametrik alan                                         |
| AKS_QPARAM2                                                                   | Parametrik alan                                         |
| AKS_QPARAM3                                                                   | Parametrik alan                                         |
| AKS_QPARAM4                                                                   | Parametrik alan                                         |
| AKS_QPARAM5                                                                   | Parametrik alan                                         |
| AKS_DPARAM1                                                                   | Parametrik alan                                         |
| AKS_DPARAM2                                                                   | Parametrik alan                                         |
| AKS_DPARAM3                                                                   | Parametrik alan                                         |
| AKS_RET_TIPI                                                                  | Ret tipi                                                |
| AKS_SIRA_NO                                                                   | Sıra no                                                 |
| AKS_PPARAM1                                                                   | Parametrik alan                                         |
| AKS_PPARAM2                                                                   | Parametrik alan                                         |
| AKS_PPARAM3                                                                   | Parametrik alan                                         |
| AKS_PPARAM4                                                                   | Parametrik alan                                         |
| AKS_PPARAM5                                                                   | Parametrik alan                                         |
| AKS_T2_ADISOYADI                                                              | Aksiyon yapacak adı soyadı                              |
| AKS_T3_ADISOYADI                                                              | Aksiyon sorumlu adı soyadı                              |
| AKS_T4_ADISOYADI                                                              | Sisteme giren adı soyadı                                |
| AKS_T5_URUN                                                                   | Ürün kodu                                               |
| AKS_T5_SIKAYET                                                                | Şikayet kodu                                            |
| AKS_T5_SIKAYETD                                                               | Şikayet detayı                                          |
| AKS_T5_LIDER                                                                  | Lider sicil numarası                                    |
| AKS_T5_KAPATAN                                                                | Kapatan kişinin sicil numarası                          |
| AKS_T5_KAPATMAT                                                               | Kapatma tarihi                                          |
| AKS_T5_SORUMLUD                                                               | Sorumlu departman kodu                                  |
| AKS_T5_SISTEMEKT                                                              | Sisteme ekleme tarihi                                   |
| AKS_T6_URUN_ADI                                                               | Ürün adı                                                |
| AKS_T6_URUN_GRUP                                                              | Ürün grubu                                              |
| AKS_T7_ADISOYADI                                                              | Lider adı soyadı                                        |
| AKS_T8_ADISOYADI                                                              | Kapatan adı soyadı                                      |
| AKS_T9_DEPARTMAN_ADI                                                          | Departman adı                                           |
| AKS_T10_URUN_ADI                                                              | Ürün adı                                                |
| AKS_T10_SORUMLU                                                               | Sorumlu sicil no                                        |
| AKS_T10_URUN_TIPI                                                             | Ürüm tipi                                               |
| AKS_T11_ADISOYADI                                                             | Sorumlu Adı soyadı                                      |
| AKS_DURUM_ACK                                                                 | Durum açıklaması                                        |
| AKS_KOKNEDEN                                                                  | Kök neden bilgisi                                       |
| AKS_DOSYALAR                                                                  | Ek dosya bilgileri                                      |
| AKS_ACMAONAY_0                                                                | Açma onaycıları ve tarihler(10' a kadar gidiyor)        |
| AKS_GERCEKLESMEONAY_0                                                         | Gerçekleşme onaycıları ve tarihler(10' a kadar gidiyor) |
| AKS_GECIKTIRMEONAY_0                                                          | Geciktirme onaycıları ve tarihler(10' a kadar gidiyor)  |
| AKS_ACMAONAYTAR_0                                                             | Açma onay tarihi(10' a kadar gidiyor)                   |
| AKS_GERCEKLESMEONAYTAR_0                                                      | Gerçekleşme onay tarihi(10' a kadar gidiyor)            |
| AKS_GECIKTIRMEONAYTAR_0                                                       | Geciktirme onay tarihi(10' a kadar gidiyor)             |

## **1.5. İç Müşteri Şikayetleri Modülünde Aksiyon Raporu Replacement (Kısa Kodlar) Tag Tablosu**

İç Müşteri Şikayetleri Modülünde kullanılan İç Müşteri Şikayetleri Aksiyon Raporu taglerin listesi aşağıdaki tabloda yer almaktadır.

| **Kısaltma (Kısalmalar tag şeklinde \< \> isaretleri arasına yazılacaktır.)** | **Açıklama**                                             |
|-------------------------------------------------------------------------------|----------------------------------------------------------|
| NO                                                                            | Aksiyon no                                               |
| AKSIYON                                                                       | Aksiyon bilgisi                                          |
| YAPACAK                                                                       | Yapacak sicil no                                         |
| SORUMLU                                                                       | Sorumlu sicil no                                         |
| PLANT                                                                         | Plan tarihi                                              |
| YAPILAN                                                                       | Yapılanların açıklaması                                  |
| YAPT                                                                          | Yapılma tarihi                                           |
| STDNO                                                                         | Madde no                                                 |
| DOCNO                                                                         | Doküman no                                               |
| SISTEMEGIREN                                                                  | Sisteme giren sicil no                                   |
| TIP                                                                           | Aksiyon tipi                                             |
| KAYITTARIHI                                                                   | Kayıt tarihi                                             |
| REVPLANT                                                                      | Planlanan revizyon tarihi                                |
| GECIKMENEDENI                                                                 | Gecikme nedeni                                           |
| MSKOD                                                                         | Müşteri şikayet kodu                                     |
| ALAN1                                                                         | Parametrik alan                                          |
| ALAN2                                                                         | Parametrik alan                                          |
| ALAN3                                                                         | Parametrik alan                                          |
| ALAN4                                                                         | Parametrik alan                                          |
| ALAN5                                                                         | Parametrik alan                                          |
| NPARAM1                                                                       | Parametrik alan                                          |
| NPARAM2                                                                       | Parametrik alan                                          |
| NPARAM3                                                                       | Parametrik alan                                          |
| NPARAM4                                                                       | Parametrik alan                                          |
| NPARAM1_BIRIM                                                                 | Parametrik alan                                          |
| NPARAM2_BIRIM                                                                 | Parametrik alan                                          |
| NPARAM3_BIRIM                                                                 | Parametrik alan                                          |
| NPARAM4_BIRIM                                                                 | Parametrik alan                                          |
| LPARAM1                                                                       | Parametrik alan                                          |
| LPARAM2                                                                       | Parametrik alan                                          |
| LPARAM3                                                                       | Parametrik alan                                          |
| DURUM                                                                         | Durum                                                    |
| ONAY_DURUM                                                                    | Onay durumu                                              |
| YAYINLANDI                                                                    | Yayınlanma durumu                                        |
| ACIKLAMA                                                                      | Açıklama                                                 |
| QPARAM1                                                                       | Parametrik alan                                          |
| QPARAM2                                                                       | Parametrik alan                                          |
| QPARAM3                                                                       | Parametrik alan                                          |
| QPARAM4                                                                       | Parametrik alan                                          |
| QPARAM5                                                                       | Parametrik alan                                          |
| DPARAM1                                                                       | Parametrik alan                                          |
| DPARAM2                                                                       | Parametrik alan                                          |
| DPARAM3                                                                       | Parametrik alan                                          |
| RET_TIPI                                                                      | Ret tipi                                                 |
| SIRA_NO                                                                       | Sıra no                                                  |
| PPARAM1                                                                       | Parametrik alan                                          |
| PPARAM2                                                                       | Parametrik alan                                          |
| PPARAM3                                                                       | Parametrik alan                                          |
| PPARAM4                                                                       | Parametrik alan                                          |
| PPARAM5                                                                       | Parametrik alan                                          |
| T2_ADISOYADI                                                                  | Aksiyon yapacak adı soyadı                               |
| T3_ADISOYADI                                                                  | Aksiyon sorumlu adı soyadı                               |
| T4_ADISOYADI                                                                  | Sisteme giren adı soyadı                                 |
| T5_URUN                                                                       | Ürün tanımı                                              |
| T5_SIKAYET                                                                    | Şikayet tanımı                                           |
| T5_SIKAYETD                                                                   | Şikayet detayı                                           |
| T5_LIDER                                                                      | Lider sicil numarası                                     |
| T5_KAPATAN                                                                    | Kapatan kişinin sicil numarası                           |
| T5_KAPATMAT                                                                   | Kapatma tarihi                                           |
| T5_SORUMLUD                                                                   | Sorumlu departman kodu                                   |
| T5_SISTEMEKT                                                                  | Sisteme ekleme tarihi                                    |
| T6_URUN_ADI                                                                   | Ürün adı                                                 |
| T6_URUN_GRUP                                                                  | Ürün grubu                                               |
| T7_ADISOYADI                                                                  | Lider adı soyadı                                         |
| T8_ADISOYADI                                                                  | Kapatan adı soyadı                                       |
| T9_DEPARTMAN_ADI                                                              | Departman adı                                            |
| T10_URUN_ADI                                                                  | Ürün adı                                                 |
| T10_SORUMLU                                                                   | Sorumlu sicil no                                         |
| T10_URUN_TIPI                                                                 | Ürüm tipi                                                |
| T11_ADISOYADI                                                                 | Sorumlu Adı soyadı                                       |
| DURUM_ACK                                                                     | Durum açıklaması                                         |
| KOKNEDEN                                                                      | Kök neden bilgisi                                        |
| AKS_ACMAONAY_0                                                                | Açma onaycıları ve tarihler(10' a kadar gidiyor)         |
| AKS_GERCEKLESMEONAY_0                                                         | Gerçekleşme onaycıları ve tarihler(10' a kadar gidiyor)  |
| AKS_GECIKTIRMEONAY_0                                                          | Geciktirme onaycıları ve tarihler(10' a kadar gidiyor)   |
| AKS_ACMAONAYTAR_0                                                             | Açma onay tarihi(10' a kadar gidiyor)                    |
| AKS_GERCEKLESMEONAYTAR_0                                                      | Gerçekleşme onay tarihi(10' a kadar gidiyor)             |
| AKS_GECIKTIRMEONAYTAR_0                                                       | Geciktirme onay tarihi(10' a kadar gidiyor)              |
| AKS_ACMASURE_0                                                                | Açma onay süresi(10' a kadar gidiyor)                    |
| AKS_KAPATMASURE_0                                                             | Kapatma onay süresi(10' a kadar gidiyor)                 |
| KAPATMAONAYTAR_0                                                              | Kapatma onay tarihi(10' a kadar gidiyor)                 |
| ACMAONAYTAR_0                                                                 | Açma onay tarihi(10' a kadar gidiyor)                    |
| TOPLAM_AKS_ACMASURE                                                           | Toplam açma onay süresi                                  |
| TOPLAM_AKS_KAPATMASURE                                                        | Toplam kapatma onay süresi                               |
| REVIZYON_BITIS_TARIHI                                                         | Revizyon bitiş tarihi                                    |
| GECIKME_NEDENI                                                                | Gecikme nedeni                                           |
| AKS_YAPACAK_DEPARTMAN_ADI                                                     | Aksiyon yapacak departman adı                            |
| LPARAM1_VALUE                                                                 | Parametrik alan                                          |
| LPARAM2_VALUE                                                                 | Parametrik alan                                          |
| LPARAM3_VALUE                                                                 | Parametrik alan                                          |
| NPARAM1_VALUE                                                                 | Parametrik alan                                          |
| NPARAM2_VALUE                                                                 | Parametrik alan                                          |
| NPARAM3_VALUE                                                                 | Parametrik alan                                          |
| NPARAM4_VALUE                                                                 | Parametrik alan                                          |
| PPARAM1_VALUE                                                                 | Parametrik alan                                          |
| PPARAM2_VALUE                                                                 | Parametrik alan                                          |
| PPARAM3_VALUE                                                                 | Parametrik alan                                          |
| PPARAM4_VALUE                                                                 | Parametrik alan                                          |
| PPARAM5_VALUE                                                                 | Parametrik alan                                          |
| MS_MKOD                                                                       | Müşteri Kodu                                             |
| MS_SKOD                                                                       | Şikayet Kodu                                             |
| MS_MREF                                                                       | Denetimden açılan Müşteri şikayetleri için referans kodu |
| MS_BILDIREN                                                                   | Bildiren kişi                                            |
| MS_BILDIRIMT                                                                  | Bildirim Tarihi                                          |
| MS_BILDIRIMS                                                                  | Bildirim süresi                                          |
| MS_SIKAYETG                                                                   | Şikayet oluşturan sicil no                               |
| MS_SISTEMEKT                                                                  | Sisteme ekleme tarihi                                    |
| MS_SORUMLUD                                                                   | Sorumlu departman kodu                                   |
| MS_SIKAYET                                                                    | Şikayet tanımı                                           |
| MS_SIKAYETD                                                                   | Şikayet detayı                                           |
| MS_URUN                                                                       | Ürün kodu                                                |
| MS_SEVKIYATM                                                                  | Toplam geri dönüş miktarı                                |
| MS_SIKAYETM                                                                   | Geri dönüş şikayet miktarı                               |
| MS_GERIODEME                                                                  | Geri dönüş ödeme tutarı                                  |
| MS_ACIKLAMA                                                                   | Açıklama                                                 |
| MS_GELRAPY                                                                    | Planlanan gelisme raporu tarihi                          |
| MS_DURUM                                                                      | Durum bilgisi                                            |
| MS_GELISMEYT                                                                  | Gelişme raporu yazma tarihi                              |
| MS_GELISMERP                                                                  | Gelişme raporu                                           |
| MS_GELEQUSON                                                                  | Gelişme ve Sonuç Raporu Aynı Olsun                       |
| MS_SONRAPY                                                                    | Planlanan sonuç raporu tarihi                            |
| MS_SONRP                                                                      | Sonuç raporu                                             |
| MS_LIDER                                                                      | Lider sicil numarası                                     |
| MS_PARABIRIMI                                                                 | Para birimi                                              |
| MS_GELKYTUSR                                                                  | Gelişme raporu yazan sicili                              |
| MS_SONRAPYT                                                                   | Sonuç raporu yazma tarihi                                |
| MS_SONKYTUSR                                                                  | Sonuç raporunu yazanın sicil numarası                    |
| MS_KAPATAN                                                                    | Kapatan kişinin sicil numarası                           |
| MS_KAPATMAT                                                                   | Kapatma tarihi                                           |
| MS_ICDIS                                                                      | İç veya dış müşteri şikayeti durumu                      |
| MS_SPARISNO                                                                   | Sipariş no                                               |
| MS_IRSALIYENO                                                                 | İrsaliye no                                              |
| MS_SEVKTARIHI                                                                 | Sevk tarihi                                              |
| MS_BIRIMSIKAYETM                                                              | Geri dönüş şikayet miktar birimi                         |
| MS_BIRIMTOPLAM                                                                | Toplam geri dönüş miktar birimi                          |
| MS_YETERLILIK                                                                 | Yeterlilik Bilgisi                                       |
| MS_HATA6M                                                                     | Hata parametrik alan                                     |
| MS_HATA5M                                                                     | Hata parametrik alan                                     |
| MS_HATA4M                                                                     | Hata parametrik alan                                     |
| MS_HATA3M                                                                     | Hata parametrik alan                                     |
| MS_HATA2M                                                                     | Hata parametrik alan                                     |
| MS_HATA1M                                                                     | Hata parametrik alan                                     |
| MS_HATA6T                                                                     | Hata parametrik alan                                     |
| MS_HATA5T                                                                     | Hata parametrik alan                                     |
| MS_HATA4T                                                                     | Hata parametrik alan                                     |
| MS_HATA3T                                                                     | Hata parametrik alan                                     |
| MS_HATA2T                                                                     | Hata parametrik alan                                     |
| MS_HATA1T                                                                     | Hata parametrik alan                                     |
| MS_BOLUM1                                                                     | Hata parametrik alan                                     |
| MS_BOLUM2                                                                     | Hata parametrik alan                                     |
| MS_BOLUM3                                                                     | Hata parametrik alan                                     |
| MS_BOLUM4                                                                     | Hata parametrik alan                                     |
| MS_BOLUM5                                                                     | Hata parametrik alan                                     |
| MS_BOLUM6                                                                     | Hata parametrik alan                                     |
| MS_ORAN6                                                                      | Hata parametrik alan                                     |
| MS_ORAN5                                                                      | Hata parametrik alan                                     |
| MS_ORAN4                                                                      | Hata parametrik alan                                     |
| MS_ORAN3                                                                      | Hata parametrik alan                                     |
| MS_ORAN2                                                                      | Hata parametrik alan                                     |
| MS_ORAN1                                                                      | Hata parametrik alan                                     |
| MS_REDNEDENI                                                                  | İptal nedeni                                             |
| MS_ISYERI_KODU                                                                | İş yeri kodu                                             |
| MS_ILKCEV_PLANTAR                                                             | Planlanan ilk cevap tarihi                               |
| MS_ILKCEV_GERTAR                                                              | Gerçekleşen ilk cevap tarihi                             |
| MS_ILKCEV_GECNED                                                              | İlk gecikme nedeni                                       |
| MS_SONCEV_PLANTAR                                                             | Planlanan son cevap tarihi                               |
| MS_SONCEV_GERTAR                                                              | Gerçekleşen son cevap tarihi                             |
| MS_SONCEV_GECNED                                                              | Son cevap gecikme nedeni                                 |
| MS_PPM_HATALIMIKTAR                                                           | PPMe Yansıyacak Hatalı Miktar                            |
| MS_CVPDA                                                                      | Cevap verme performansında dikkate alınması              |
| MS_SAADA                                                                      | Şikayet adedi analizinde dikkate alınması                |
| MS_MSH                                                                        | Müşteri şikayetinde haklıdır.                            |
| MS_HATA_PER1                                                                  | Hata personel tipli parametrik alan                      |
| MS_HATA_PER2                                                                  | Hata personel tipli parametrik alan                      |
| MS_HATA_PER3                                                                  | Hata personel tipli parametrik alan                      |
| MS_HATA_PER4                                                                  | Hata personel tipli parametrik alan                      |
| MS_HATA_PER5                                                                  | Hata personel tipli parametrik alan                      |
| MS_HATA_PER6                                                                  | Hata personel tipli parametrik alan                      |
| MS_HATA_PER_ORAN1                                                             | Hata personel oranı parametrik alan                      |
| MS_HATA_PER_ORAN2                                                             | Hata personel oranı parametrik alan                      |
| MS_HATA_PER_ORAN3                                                             | Hata personel oranı parametrik alan                      |
| MS_HATA_PER_ORAN4                                                             | Hata personel oranı parametrik alan                      |
| MS_HATA_PER_ORAN5                                                             | Hata personel oranı parametrik alan                      |
| MS_HATA_PER_ORAN6                                                             | Hata personel oranı parametrik alan                      |
| MS_REDDEDEN                                                                   | Reddeden bilgisi                                         |
| MS_SUREC_KODU                                                                 | Süreç kodu                                               |
| MS_ANKET_REF                                                                  | Anket referans kodu                                      |
| MS_GELISME_ALAN1                                                              | Gelişme parametrik alan                                  |
| MS_GELISME_ALAN2                                                              | Gelişme parametrik alan                                  |
| MS_GELISME_ALAN3                                                              | Gelişme parametrik alan                                  |
| MS_PARAM_MIKTAR1                                                              | Parametrik alan                                          |
| MS_PARAM_MIKTAR2                                                              | Parametrik alan                                          |
| MS_PARAM_BIRIM1                                                               | Parametrik alan                                          |
| MS_PARAM_BIRIM2                                                               | Parametrik alan                                          |
| MS_PARAM1                                                                     | Parametrik alan                                          |
| MS_PARAM2                                                                     | Parametrik alan                                          |
| MS_PARAM3                                                                     | Parametrik alan                                          |
| MS_PARAM4                                                                     | Parametrik alan                                          |
| MS_PARAM5                                                                     | Parametrik alan                                          |
| MS_PARAM6                                                                     | Parametrik alan                                          |
| MS_PARAM7                                                                     | Parametrik alan                                          |
| MS_PARAM8                                                                     | Parametrik alan                                          |
| MS_PARAM9                                                                     | Parametrik alan                                          |
| MS_PARAM10                                                                    | Parametrik alan                                          |
| MS_NPARAM1                                                                    | Nümerik tipli parametrik alan                            |
| MS_NPARAM2                                                                    | Nümerik tipli parametrik alan                            |
| MS_NPARAM3                                                                    | Nümerik tipli parametrik alan                            |
| MS_NPARAM4                                                                    | Nümerik tipli parametrik alan                            |
| MS_NPARAM5                                                                    | Nümerik tipli parametrik alan                            |
| MS_NPARAM6                                                                    | Nümerik tipli parametrik alan                            |
| MS_NPARAM7                                                                    | Nümerik tipli parametrik alan                            |
| MS_NPARAM8                                                                    | Nümerik tipli parametrik alan                            |
| MS_NPARAM9                                                                    | Nümerik tipli parametrik alan                            |
| MS_NPARAM10                                                                   | Nümerik birim tiplerine ait parametrik alan              |
| MS_NPARAM1_BIRIM                                                              | Nümerik birim tiplerine ait parametrik alan              |
| MS_NPARAM2_BIRIM                                                              | Nümerik birim tiplerine ait parametrik alan              |
| MS_NPARAM3_BIRIM                                                              | Nümerik birim tiplerine ait parametrik alan              |
| MS_NPARAM4_BIRIM                                                              | Nümerik birim tiplerine ait parametrik alan              |
| MS_NPARAM5_BIRIM                                                              | Nümerik birim tiplerine ait parametrik alan              |
| MS_NPARAM6_BIRIM                                                              | Nümerik birim tiplerine ait parametrik alan              |
| MS_NPARAM7_BIRIM                                                              | Nümerik birim tiplerine ait parametrik alan              |
| MS_NPARAM8_BIRIM                                                              | Nümerik birim tiplerine ait parametrik alan              |
| MS_NPARAM9_BIRIM                                                              | Nümerik birim tiplerine ait parametrik alan              |
| MS_NPARAM10_BIRIM                                                             | Nümerik birim tiplerine ait parametrik alan              |
| MS_DPARAM1                                                                    | Tarih tipli parametrik alan                              |
| MS_DPARAM2                                                                    | Tarih tipli parametrik alan                              |
| MS_DPARAM3                                                                    | Tarih tipli parametrik alan                              |
| MS_DPARAM4                                                                    | Tarih tipli parametrik alan                              |
| MS_DPARAM5                                                                    | Tarih tipli parametrik alan                              |
| MS_PPARAM1                                                                    | Personel tipli parametrik alan                           |
| MS_PPARAM2                                                                    | Personel tipli parametrik alan                           |
| MS_PPARAM3                                                                    | Personel tipli parametrik alan                           |
| MS_PPARAM4                                                                    | Personel tipli parametrik alan                           |
| MS_PPARAM5                                                                    | Personel tipli parametrik alan                           |
| MS_LPARAM1                                                                    | Liste tipli parametrik alan                              |
| MS_LPARAM2                                                                    | Liste tipli parametrik alan                              |
| MS_LPARAM3                                                                    | Liste tipli parametrik alan                              |
| MS_LPARAM4                                                                    | Liste tipli parametrik alan                              |
| MS_LPARAM5                                                                    | Liste tipli parametrik alan                              |
| MS_SISTEM_KODU                                                                | Yönetim sistemi kodu                                     |
| MS_ONAY_DURUM                                                                 | Onay durumu                                              |
| MS_AKSIYON_DURUM                                                              | Aksiyon Durumu                                           |
| MS_AKSIYON_SONUC_TARIHI                                                       | Aksiyon sonuç tarihi                                     |
| MS_DOF_SONUC_TARIHI                                                           | DOF sonuç tarihi                                         |
| MS_GELISME_PARAM1                                                             | Gelişme parametrik alan                                  |
| MS_GELISME_PARAM2                                                             | Gelişme parametrik alan                                  |
| MS_GELISME_PARAM3                                                             | Gelişme parametrik alan                                  |
| MS_GELISME_PARAM4                                                             | Gelişme parametrik alan                                  |
| MS_GELISME_PARAM5                                                             | Gelişme parametrik alan                                  |
| MS_GELISME_PARAM6                                                             | Gelişme parametrik alan                                  |
| MS_GELISME_PARAM7                                                             | Gelişme parametrik alan                                  |
| MS_GELISME_PARAM8                                                             | Gelişme parametrik alan                                  |
| MS_GELISME_PARAM9                                                             | Gelişme parametrik alan                                  |
| MS_GELISME_PARAM10                                                            | Gelişme parametrik alan                                  |
| MS_GELISME_LPARAM1                                                            | Gelişme parametrik alan                                  |
| MS_GELISME_LPARAM2                                                            | Gelişme parametrik alan                                  |
| MS_GELISME_LPARAM3                                                            | Gelişme parametrik alan                                  |
| MS_GELISME_LPARAM4                                                            | Gelişme parametrik alan                                  |
| MS_GELISME_LPARAM5                                                            | Gelişme parametrik alan                                  |
| MS_GELISME_LPARAM6                                                            | Gelişme parametrik alan                                  |
| MS_GELISME_LPARAM7                                                            | Gelişme parametrik alan                                  |
| MS_GELISME_LPARAM8                                                            | Gelişme parametrik alan                                  |
| MS_GELISME_LPARAM9                                                            | Gelişme parametrik alan                                  |
| MS_GELISME_LPARAM10                                                           | Gelişme parametrik alan                                  |
| MS_GELISME_NPARAM1                                                            | Gelişme parametrik alan                                  |
| MS_GELISME_NPARAM2                                                            | Gelişme parametrik alan                                  |
| MS_GELISME_NPARAM3                                                            | Gelişme parametrik alan                                  |
| MS_GELISME_NPARAM4                                                            | Gelişme parametrik alan                                  |
| MS_GELISME_NPARAM5                                                            | Gelişme parametrik alan                                  |
| MS_GELISME_NPARAM1_BIRIM                                                      | Gelişme parametrik alan                                  |
| MS_GELISME_NPARAM2_BIRIM                                                      | Gelişme parametrik alan                                  |
| MS_GELISME_NPARAM3_BIRIM                                                      | Gelişme parametrik alan                                  |
| MS_GELISME_NPARAM4_BIRIM                                                      | Gelişme parametrik alan                                  |
| MS_GELISME_NPARAM5_BIRIM                                                      | Gelişme parametrik alan                                  |
| MS_NERDEN                                                                     | Web servisten açılan kayıtlar için                       |
| MS_NERDEN_KOD                                                                 | Web servisten açılan kayıtlar için                       |
| MS_PARAM11                                                                    | Parametrik alan                                          |
| MS_PARAM12                                                                    | Parametrik alan                                          |
| MS_PARAM13                                                                    | Parametrik alan                                          |
| MS_PARAM14                                                                    | Parametrik alan                                          |
| MS_PARAM15                                                                    | Parametrik alan                                          |
| MS_LPARAM6                                                                    | Liste tipli parametrik alan                              |
| MS_LPARAM7                                                                    | Liste tipli parametrik alan                              |
| MS_LPARAM8                                                                    | Liste tipli parametrik alan                              |
| MS_LPARAM9                                                                    | Liste tipli parametrik alan                              |
| MS_LPARAM10                                                                   | Liste tipli parametrik alan                              |
| MS_SONUC_PARAM1                                                               | Sonuç parametrik alan                                    |
| MS_SONUC_PARAM2                                                               | Sonuç parametrik alan                                    |
| MS_SONUC_PARAM3                                                               | Sonuç parametrik alan                                    |
| MS_SONUC_PARAM4                                                               | Sonuç parametrik alan                                    |
| MS_SONUC_PARAM5                                                               | Sonuç parametrik alan                                    |
| MS_SONUC_PARAM6                                                               | Sonuç parametrik alan                                    |
| MS_SONUC_PARAM7                                                               | Sonuç parametrik alan                                    |
| MS_SONUC_PARAM8                                                               | Sonuç parametrik alan                                    |
| MS_SONUC_PARAM9                                                               | Sonuç parametrik alan                                    |
| MS_SONUC_PARAM10                                                              | Sonuç parametrik alan                                    |
| MS_SONUC_LPARAM1                                                              | Sonuç parametrik alan                                    |
| MS_SONUC_LPARAM2                                                              | Sonuç parametrik alan                                    |
| MS_SONUC_LPARAM3                                                              | Sonuç parametrik alan                                    |
| MS_SONUC_LPARAM4                                                              | Sonuç parametrik alan                                    |
| MS_SONUC_LPARAM5                                                              | Sonuç parametrik alan                                    |
| MS_SONUC_LPARAM6                                                              | Sonuç parametrik alan                                    |
| MS_SONUC_LPARAM7                                                              | Sonuç parametrik alan                                    |
| MS_SONUC_LPARAM8                                                              | Sonuç parametrik alan                                    |
| MS_SONUC_LPARAM9                                                              | Sonuç parametrik alan                                    |
| MS_SONUC_LPARAM10                                                             | Sonuç parametrik alan                                    |
| MS_SONUC_NPARAM1                                                              | Sonuç parametrik alan                                    |
| MS_SONUC_NPARAM2                                                              | Sonuç parametrik alan                                    |
| MS_SONUC_NPARAM3                                                              | Sonuç parametrik alan                                    |
| MS_SONUC_NPARAM4                                                              | Sonuç parametrik alan                                    |
| MS_SONUC_NPARAM5                                                              | Sonuç parametrik alan                                    |
| MS_SONUC_NPARAM1_BIRIM                                                        | Sonuç parametrik alan                                    |
| MS_SONUC_NPARAM2_BIRIM                                                        | Sonuç parametrik alan                                    |
| MS_SONUC_NPARAM3_BIRIM                                                        | Sonuç parametrik alan                                    |
| MS_SONUC_NPARAM4_BIRIM                                                        | Sonuç parametrik alan                                    |
| MS_SONUC_NPARAM5_BIRIM                                                        | Sonuç parametrik alan                                    |
| MS_KAPATMA_PARAM1                                                             | Kapatma parametrik alan                                  |
| MS_KAPATMA_PARAM2                                                             | Kapatma parametrik alan                                  |
| MS_KAPATMA_PARAM3                                                             | Kapatma parametrik alan                                  |
| MS_KAPATMA_PARAM4                                                             | Kapatma parametrik alan                                  |
| MS_KAPATMA_PARAM5                                                             | Kapatma parametrik alan                                  |
| MS_KAPATMA_PARAM6                                                             | Kapatma parametrik alan                                  |
| MS_KAPATMA_PARAM7                                                             | Kapatma parametrik alan                                  |
| MS_KAPATMA_PARAM8                                                             | Kapatma parametrik alan                                  |
| MS_KAPATMA_PARAM9                                                             | Kapatma parametrik alan                                  |
| MS_KAPATMA_PARAM10                                                            | Kapatma parametrik alan                                  |
| MS_KAPATMA_LPARAM1                                                            | Kapatma parametrik alan                                  |
| MS_KAPATMA_LPARAM2                                                            | Kapatma parametrik alan                                  |
| MS_KAPATMA_LPARAM3                                                            | Kapatma parametrik alan                                  |
| MS_KAPATMA_LPARAM4                                                            | Kapatma parametrik alan                                  |
| MS_KAPATMA_LPARAM5                                                            | Kapatma parametrik alan                                  |
| MS_KAPATMA_LPARAM6                                                            | Kapatma parametrik alan                                  |
| MS_KAPATMA_LPARAM7                                                            | Kapatma parametrik alan                                  |
| MS_KAPATMA_LPARAM8                                                            | Kapatma parametrik alan                                  |
| MS_KAPATMA_LPARAM9                                                            | Kapatma parametrik alan                                  |
| MS_KAPATMA_LPARAM10                                                           | Kapatma parametrik alan                                  |
| MS_KAPATMA_NPARAM1                                                            | Kapatma parametrik alan                                  |
| MS_KAPATMA_NPARAM2                                                            | Kapatma parametrik alan                                  |
| MS_KAPATMA_NPARAM3                                                            | Kapatma parametrik alan                                  |
| MS_KAPATMA_NPARAM4                                                            | Kapatma parametrik alan                                  |
| MS_KAPATMA_NPARAM1_BIRIM                                                      | Kapatma parametrik alan                                  |
| MS_KAPATMA_NPARAM2_BIRIM                                                      | Kapatma parametrik alan                                  |
| MS_KAPATMA_NPARAM3_BIRIM                                                      | Kapatma parametrik alan                                  |
| MS_KAPATMA_NPARAM4_BIRIM                                                      | Kapatma parametrik alan                                  |
| MS_ESKI_DURUM                                                                 | Önceki durum                                             |
| MS_ESKI_ONAY_DURUM                                                            | Önceki onay durumu                                       |
| MS_ONAY_TARIHI                                                                | Onay tarihi                                              |
| MS_ARACEV_PLANTAR                                                             | Planlanan ara cevap tarihi                               |
| MS_ARACEV_GERTAR                                                              | Gerçekleşen ara cevap tarihi                             |
| MS_ARACEV_GECNED                                                              | Ara gecikme nedeni                                       |
| MS_UPARAM1                                                                    | Ürün tipli parametrik alan                               |
| MS_MPARAM1                                                                    | Müşteri tipli parametrik alan                            |
| MS_TDPARAM1                                                                   | Tedarikçi tipli parametrik alan                          |
| MS_RDFD_NO                                                                    | Risk kodu                                                |
| MS_PARAM16                                                                    | Parametrik alan                                          |
| MS_PARAM17                                                                    | Parametrik alan                                          |
| MS_PARAM18                                                                    | Parametrik alan                                          |
| MS_PARAM19                                                                    | Parametrik alan                                          |
| MS_PARAM20                                                                    | Parametrik alan                                          |
| MS_OTOMATIK_AKSIYON                                                           | Otomatik aksiyon durumu                                  |
| MS_QPARAM1                                                                    | Sorgu tipli parametrik alan                              |
| MS_QPARAM2                                                                    | Sorgu tipli parametrik alan                              |
| MS_QPARAM3                                                                    | Sorgu tipli parametrik alan                              |
| MS_QPARAM4                                                                    | Sorgu tipli parametrik alan                              |
| MS_QPARAM5                                                                    | Sorgu tipli parametrik alan                              |
| MS_LPARAM11                                                                   | Liste tipli parametrik alan                              |
| MS_LPARAM12                                                                   | Liste tipli parametrik alan                              |
| MS_LPARAM13                                                                   | Liste tipli parametrik alan                              |
| MS_LPARAM14                                                                   | Liste tipli parametrik alan                              |
| MS_LPARAM15                                                                   | Liste tipli parametrik alan                              |
| MS_LPARAM16                                                                   | Liste tipli parametrik alan                              |
| MS_LPARAM17                                                                   | Liste tipli parametrik alan                              |
| MS_LPARAM18                                                                   | Liste tipli parametrik alan                              |
| MS_LPARAM19                                                                   | Liste tipli parametrik alan                              |
| MS_LPARAM20                                                                   | Liste tipli parametrik alan                              |
| MS_NPARAM11                                                                   | Nümerik tipli parametrik alan                            |
| MS_NPARAM12                                                                   | Nümerik tipli parametrik alan                            |
| MS_NPARAM13                                                                   | Nümerik tipli parametrik alan                            |
| MS_NPARAM14                                                                   | Nümerik tipli parametrik alan                            |
| MS_NPARAM15                                                                   | Nümerik tipli parametrik alan                            |
| MS_NPARAM16                                                                   | Nümerik tipli parametrik alan                            |
| MS_NPARAM17                                                                   | Nümerik tipli parametrik alan                            |
| MS_NPARAM18                                                                   | Nümerik tipli parametrik alan                            |
| MS_NPARAM19                                                                   | Nümerik tipli parametrik alan                            |
| MS_NPARAM20                                                                   | Nümerik tipli parametrik alan                            |
| MS_NPARAM21                                                                   | Nümerik tipli parametrik alan                            |
| MS_NPARAM22                                                                   | Nümerik tipli parametrik alan                            |
| MS_NPARAM23                                                                   | Nümerik tipli parametrik alan                            |
| MS_NPARAM24                                                                   | Nümerik tipli parametrik alan                            |
| MS_NPARAM25                                                                   | Nümerik tipli parametrik alan                            |
| MS_NPARAM26                                                                   | Nümerik tipli parametrik alan                            |
| MS_NPARAM27                                                                   | Nümerik tipli parametrik alan                            |
| MS_NPARAM28                                                                   | Nümerik tipli parametrik alan                            |
| MS_NPARAM29                                                                   | Nümerik tipli parametrik alan                            |
| MS_NPARAM30                                                                   | Nümerik tipli parametrik alan                            |
| MS_NPARAM11_BIRIM                                                             | Nümerik birim tiplerine ait parametrik alan              |
| MS_NPARAM12_BIRIM                                                             | Nümerik birim tiplerine ait parametrik alan              |
| MS_NPARAM13_BIRIM                                                             | Nümerik birim tiplerine ait parametrik alan              |
| MS_NPARAM14_BIRIM                                                             | Nümerik birim tiplerine ait parametrik alan              |
| MS_NPARAM15_BIRIM                                                             | Nümerik birim tiplerine ait parametrik alan              |
| MS_NPARAM16_BIRIM                                                             | Nümerik birim tiplerine ait parametrik alan              |
| MS_NPARAM17_BIRIM                                                             | Nümerik birim tiplerine ait parametrik alan              |
| MS_NPARAM18_BIRIM                                                             | Nümerik birim tiplerine ait parametrik alan              |
| MS_NPARAM19_BIRIM                                                             | Nümerik birim tiplerine ait parametrik alan              |
| MS_NPARAM20_BIRIM                                                             | Nümerik birim tiplerine ait parametrik alan              |
| MS_NPARAM21_BIRIM                                                             | Nümerik birim tiplerine ait parametrik alan              |
| MS_NPARAM22_BIRIM                                                             | Nümerik birim tiplerine ait parametrik alan              |
| MS_NPARAM23_BIRIM                                                             | Nümerik birim tiplerine ait parametrik alan              |
| MS_NPARAM24_BIRIM                                                             | Nümerik birim tiplerine ait parametrik alan              |
| MS_NPARAM25_BIRIM                                                             | Nümerik birim tiplerine ait parametrik alan              |
| MS_NPARAM26_BIRIM                                                             | Nümerik birim tiplerine ait parametrik alan              |
| MS_NPARAM27_BIRIM                                                             | Nümerik birim tiplerine ait parametrik alan              |
| MS_NPARAM28_BIRIM                                                             | Nümerik birim tiplerine ait parametrik alan              |
| MS_NPARAM29_BIRIM                                                             | Nümerik birim tiplerine ait parametrik alan              |
| MS_NPARAM30_BIRIM                                                             | Nümerik birim tiplerine ait parametrik alan              |
| MS_PARAM21                                                                    | Parametrik alan                                          |
| MS_PARAM22                                                                    | Parametrik alan                                          |
| MS_PARAM23                                                                    | Parametrik alan                                          |
| MS_PARAM24                                                                    | Parametrik alan                                          |
| MS_PARAM25                                                                    | Parametrik alan                                          |
| MS_PARAM31                                                                    | Parametrik alan                                          |
| MS_PARAM32                                                                    | Parametrik alan                                          |
| MS_PARAM33                                                                    | Parametrik alan                                          |
| MS_PARAM34                                                                    | Parametrik alan                                          |
| MS_PARAM35                                                                    | Parametrik alan                                          |
| MS_LPARAM36                                                                   | Liste tipli parametrik alan                              |
| MS_LPARAM37                                                                   | Liste tipli parametrik alan                              |
| MS_LPARAM38                                                                   | Liste tipli parametrik alan                              |
| MS_LPARAM39                                                                   | Liste tipli parametrik alan                              |
| MS_LPARAM40                                                                   | Liste tipli parametrik alan                              |
| MS_NPARAM41                                                                   | Nümerik tipli parametrik alan                            |
| MS_NPARAM42                                                                   | Nümerik tipli parametrik alan                            |
| MS_NPARAM43                                                                   | Nümerik tipli parametrik alan                            |
| MS_NPARAM44                                                                   | Nümerik tipli parametrik alan                            |
| MS_NPARAM45                                                                   | Nümerik tipli parametrik alan                            |
| MS_NPARAM46                                                                   | Nümerik tipli parametrik alan                            |
| MS_NPARAM47                                                                   | Nümerik tipli parametrik alan                            |
| MS_NPARAM48                                                                   | Nümerik tipli parametrik alan                            |
| MS_NPARAM49                                                                   | Nümerik tipli parametrik alan                            |
| MS_NPARAM50                                                                   | Nümerik tipli parametrik alan                            |
| MS_NPARAM41_BIRIM                                                             | Nümerik birim tiplerine ait parametrik alan              |
| MS_NPARAM42_BIRIM                                                             | Nümerik birim tiplerine ait parametrik alan              |
| MS_NPARAM43_BIRIM                                                             | Nümerik birim tiplerine ait parametrik alan              |
| MS_NPARAM44_BIRIM                                                             | Nümerik birim tiplerine ait parametrik alan              |
| MS_NPARAM45_BIRIM                                                             | Nümerik birim tiplerine ait parametrik alan              |
| MS_NPARAM46_BIRIM                                                             | Nümerik birim tiplerine ait parametrik alan              |
| MS_NPARAM47_BIRIM                                                             | Nümerik birim tiplerine ait parametrik alan              |
| MS_NPARAM48_BIRIM                                                             | Nümerik birim tiplerine ait parametrik alan              |
| MS_NPARAM49_BIRIM                                                             | Nümerik birim tiplerine ait parametrik alan              |
| MS_NPARAM50_BIRIM                                                             | Nümerik birim tiplerine ait parametrik alan              |
| MS_KAPATMA_NPARAM5                                                            | Kapatma Parametrik alan                                  |
| MS_KAPATMA_NPARAM6                                                            | Kapatma Parametrik alan                                  |
| MS_KAPATMA_NPARAM7                                                            | Kapatma Parametrik alan                                  |
| MS_KAPATMA_NPARAM8                                                            | Kapatma Parametrik alan                                  |
| MS_KAPATMA_NPARAM9                                                            | Kapatma Parametrik alan                                  |
| MS_KAPATMA_NPARAM10                                                           | Kapatma Parametrik alan                                  |
| MS_KAPATMA_NPARAM5_BIRIM                                                      | Kapatma Parametrik alan                                  |
| MS_KAPATMA_NPARAM6_BIRIM                                                      | Kapatma Parametrik alan                                  |
| MS_KAPATMA_NPARAM7_BIRIM                                                      | Kapatma Parametrik alan                                  |
| MS_KAPATMA_NPARAM8_BIRIM                                                      | Kapatma Parametrik alan                                  |
| MS_KAPATMA_NPARAM9_BIRIM                                                      | Kapatma Parametrik alan                                  |
| MS_KAPATMA_NPARAM10_BIRIM                                                     | Kapatma Parametrik alan                                  |
| MS_DOF_NO                                                                     | DOF no                                                   |
| MS_DEGERLENDIRME                                                              | Değerlendirme bilgisi                                    |
| MS_DEGERLENDIRME_PUANI                                                        | Değerlendirme puanı bilgisi                              |
| MS_RET_TIPI                                                                   | Ret tipi                                                 |
| MS_TERMINTARIHI                                                               | Termin Tarihi                                            |
| MS_KAPATMA_DPARAM1                                                            | Kapatma Parametrik alan                                  |
| MS_KAPATMA_DPARAM2                                                            | Kapatma Parametrik alan                                  |
| MS_KAPATMA_DPARAM3                                                            | Kapatma Parametrik alan                                  |
| MS_KAPATMA_DPARAM4                                                            | Kapatma Parametrik alan                                  |
| MS_KAPATMA_DPARAM5                                                            | Kapatma Parametrik alan                                  |
| MS_HATA1_BIRIM                                                                | Hata tipli parametrik alan                               |
| MS_HATA2_BIRIM                                                                | Hata tipli parametrik alan                               |
| MS_HATA3_BIRIM                                                                | Hata tipli parametrik alan                               |
| MS_HATA4_BIRIM                                                                | Hata tipli parametrik alan                               |
| MS_HATA5_BIRIM                                                                | Hata tipli parametrik alan                               |
| MS_HATA6_BIRIM                                                                | Hata tipli parametrik alan                               |
| MS_GELISME_PPARAM1                                                            | Gelişme parametrik alan                                  |
| MS_GELISME_PPARAM2                                                            | Gelişme parametrik alan                                  |
| MS_GELISME_PPARAM3                                                            | Gelişme parametrik alan                                  |
| MS_GELISME_PPARAM4                                                            | Gelişme parametrik alan                                  |
| MS_GELISME_PPARAM5                                                            | Gelişme parametrik alan                                  |
| MS_SONUC_PPARAM1                                                              | Sonuç parametrik alan                                    |
| MS_SONUC_PPARAM2                                                              | Sonuç parametrik alan                                    |
| MS_SONUC_PPARAM3                                                              | Sonuç parametrik alan                                    |
| MS_SONUC_PPARAM4                                                              | Sonuç parametrik alan                                    |
| MS_SONUC_PPARAM5                                                              | Sonuç parametrik alan                                    |
| MS_KAPATMA_PPARAM1                                                            | Kapatma Parametrik alan                                  |
| MS_KAPATMA_PPARAM2                                                            | Kapatma Parametrik alan                                  |
| MS_KAPATMA_PPARAM3                                                            | Kapatma Parametrik alan                                  |
| MS_KAPATMA_PPARAM4                                                            | Kapatma Parametrik alan                                  |
| MS_KAPATMA_PPARAM5                                                            | Kapatma Parametrik alan                                  |
| MS_GELISME_QPARAM1                                                            | Gelişme parametrik alan                                  |
| MS_GELISME_QPARAM2                                                            | Gelişme parametrik alan                                  |
| MS_GELISME_QPARAM3                                                            | Gelişme parametrik alan                                  |
| MS_GELISME_QPARAM4                                                            | Gelişme parametrik alan                                  |
| MS_GELISME_QPARAM5                                                            | Gelişme parametrik alan                                  |
| MS_SONUC_QPARAM1                                                              | Sonuç parametrik alan                                    |
| MS_SONUC_QPARAM2                                                              | Sonuç parametrik alan                                    |
| MS_SONUC_QPARAM3                                                              | Sonuç parametrik alan                                    |
| MS_SONUC_QPARAM4                                                              | Sonuç parametrik alan                                    |
| MS_SONUC_QPARAM5                                                              | Sonuç parametrik alan                                    |
| MS_KAPATMA_QPARAM1                                                            | Kapatma Parametrik alan                                  |
| MS_KAPATMA_QPARAM2                                                            | Kapatma Parametrik alan                                  |
| MS_KAPATMA_QPARAM3                                                            | Kapatma Parametrik alan                                  |
| MS_KAPATMA_QPARAM4                                                            | Kapatma Parametrik alan                                  |
| MS_KAPATMA_QPARAM5                                                            | Kapatma Parametrik alan                                  |
| MS_MALIYET                                                                    | Maliyet                                                  |
| MS_MALIYET_BIRIM                                                              | Maliyet birimi                                           |
| MS_T2_ADI                                                                     | Müşteri veya Tedarikçi Adı                               |
| MS_T3_ADISOYADI                                                               | Aksiyon sorumlu adı soyadı                               |
| MS_T4_DEPARTMAN_ADI                                                           | Sorumlu Departman adı                                    |
| MS_T5_URUN_ADI                                                                | Ürün adı                                                 |
| MS_T6_ADISOYADI                                                               | Ekip lideri adı soyadı                                   |
| MS_T7_ADISOYADI                                                               | Gelişme raporu yazan adı soyadı                          |
| MS_T8_ADISOYADI                                                               | Sonuç raporunu yazanın adı soyadı                        |
| MS_T9_ADISOYADI                                                               | Kapatan kişinin adı soyadı                               |
| MS_T10_ISYERI_ADI                                                             | İş yeri adı                                              |
| MS_T11_ACIKLAMA                                                               | Yönetim sistemi                                          |
| MS_T12_URUN_ADI                                                               | Ürün Adı                                                 |
| MS_T12_SORUMLU                                                                | Sorumlu sicil no                                         |
| MS_T12_URUN_TIPI                                                              | Ürün tipi                                                |
| MS_T13_ADISOYADI                                                              | Sorumlu adı soyadı                                       |
| MS_DURUM_ACK                                                                  | Durum açıklması                                          |
| MS_MD                                                                         | İşlem süresi                                             |
| MS_ISLEM_SURESI                                                               | İlk aksiyon tarihi                                       |
| MS_ILK_AKSIYON_TARIHI                                                         | Tedarikçi adı                                            |
| MS_T2_TEDARIKCI_ADI                                                           | Müşteri adı                                              |
| MS_T2_MUSTERI_ADI                                                             | Ürün tipi                                                |
| MS_URUN_TIPI                                                                  | Ürün grubu                                               |
| MS_IZLEME                                                                     | İzleme                                                   |
| MS_GELISME_LPARAM1_VALUE                                                      | Gelişme parametrik alan                                  |
| MS_GELISME_LPARAM10_VALUE                                                     | Gelişme parametrik alan                                  |
| MS_GELISME_LPARAM2_VALUE                                                      | Gelişme parametrik alan                                  |
| MS_GELISME_LPARAM3_VALUE                                                      | Gelişme parametrik alan                                  |
| MS_GELISME_LPARAM4_VALUE                                                      | Gelişme parametrik alan                                  |
| MS_GELISME_LPARAM5_VALUE                                                      | Gelişme parametrik alan                                  |
| MS_GELISME_LPARAM6_VALUE                                                      | Gelişme parametrik alan                                  |
| MS_GELISME_LPARAM7_VALUE                                                      | Gelişme parametrik alan                                  |
| MS_GELISME_LPARAM8_VALUE                                                      | Gelişme parametrik alan                                  |
| MS_GELISME_LPARAM9_VALUE                                                      | Gelişme parametrik alan                                  |
| MS_GELISME_NPARAM1_VALUE                                                      | Gelişme parametrik alan                                  |
| MS_GELISME_NPARAM2_VALUE                                                      | Gelişme parametrik alan                                  |
| MS_GELISME_NPARAM3_VALUE                                                      | Gelişme parametrik alan                                  |
| MS_GELISME_NPARAM4_VALUE                                                      | Gelişme parametrik alan                                  |
| MS_GELISME_NPARAM5_VALUE                                                      | Gelişme parametrik alan                                  |
| MS_GELISME_PPARAM1_VALUE                                                      | Gelişme parametrik alan                                  |
| MS_GELISME_PPARAM2_VALUE                                                      | Gelişme parametrik alan                                  |
| MS_GELISME_PPARAM3_VALUE                                                      | Gelişme parametrik alan                                  |
| MS_GELISME_PPARAM4_VALUE                                                      | Gelişme parametrik alan                                  |
| MS_GELISME_PPARAM5_VALUE                                                      | Gelişme parametrik alan                                  |
| MS_PPARAM1_VALUE                                                              | Parametrik alan                                          |
| MS_SONUC_LPARAM1_VALUE                                                        | Sonuç parametrik alan                                    |
| MS_SONUC_LPARAM10_VALUE                                                       | Sonuç parametrik alan                                    |
| MS_SONUC_LPARAM2_VALUE                                                        | Sonuç parametrik alan                                    |
| MS_SONUC_LPARAM3_VALUE                                                        | Sonuç parametrik alan                                    |
| MS_SONUC_LPARAM4_VALUE                                                        | Sonuç parametrik alan                                    |
| MS_SONUC_LPARAM5_VALUE                                                        | Sonuç parametrik alan                                    |
| MS_SONUC_LPARAM6_VALUE                                                        | Sonuç parametrik alan                                    |
| MS_SONUC_LPARAM7_VALUE                                                        | Sonuç parametrik alan                                    |
| MS_SONUC_LPARAM8_VALUE                                                        | Sonuç parametrik alan                                    |
| MS_SONUC_LPARAM9_VALUE                                                        | Sonuç parametrik alan                                    |
| MS_SONUC_NPARAM1_VALUE                                                        | Sonuç parametrik alan                                    |
| MS_SONUC_NPARAM2_VALUE                                                        | Sonuç parametrik alan                                    |
| MS_SONUC_NPARAM3_VALUE                                                        | Sonuç parametrik alan                                    |
| MS_SONUC_NPARAM4_VALUE                                                        | Sonuç parametrik alan                                    |
| MS_SONUC_NPARAM5_VALUE                                                        | Sonuç parametrik alan                                    |
| MS_SONUC_PPARAM1_VALUE                                                        | Sonuç parametrik alan                                    |
| MS_SONUC_PPARAM2_VALUE                                                        | Sonuç parametrik alan                                    |
| MS_SONUC_PPARAM3_VALUE                                                        | Sonuç parametrik alan                                    |
| MS_SONUC_PPARAM4_VALUE                                                        | Sonuç parametrik alan                                    |
| MS_SONUC_PPARAM5_VALUE                                                        | Sonuç parametrik alan                                    |
| MS_DEGERLENDIRME_KATEGORISI                                                   | Değerlendirme kategorisi                                 |
| MS_DEGERLENDIRME_ALT_KATEGORISI                                               | Derlendirme alt kategorisi                               |
| MS_DEGERLENDIRME_TUTAR                                                        | Derlendirme tutar                                        |
| MS_DEGERLENDIRME_TARIH                                                        | Derlendirme tarih                                        |
| MS_DEGERLENDIRME_ACIKLAMA                                                     | Derlendirme açıklama                                     |
| MS_DEGERLENDIRME_KATEGORILERI                                                 | Derlendirme kategorileri                                 |
| MS_DEGERLENDIRME_SECENEK                                                      | Derlendirme seçenek                                      |
| MS_DEGERLENDIRME_PUAN                                                         | Derlendirme puan                                         |
| MS_DEGERLENDIRME_DEGERLENDIREN                                                | Değerlendiren bilgisi                                    |
| MS_DEGERLENDIRME_DEGERLENDIRMET                                               | Değerlendirme Tarihi                                     |
| MS_ULKE                                                                       | Ulke bilgisi                                             |
| MS_IL                                                                         | İl bilgisi                                               |
| MS_SIKAYET_ANA_KAT_KOD                                                        | Ana şikayet kategori kodu                                |
| MS_SIKAYET_ANA_KAT                                                            | Ana şikayet kategorisi                                   |
| MS_SIKAYET_ALT_KAT_KOD                                                        | Alt şikayet kategori kodu                                |
| MS_SIKAYET_ALT_KAT                                                            | Alt şikayet kategorisi                                   |
| MS_SIKAYET_KODLAR                                                             | Şikayet kodlarının bilgisi                               |
| MS_EKIP                                                                       | Ekip üyeleri                                             |
| MS_DOF_AKSIYON_TARIHI                                                         | DOF aksiyon tarihi                                       |
| MS_KOK_NEDENLER                                                               | Kök nedenler                                             |
| MS_KOK_NEDEN_KIRILIM                                                          | Kök neden kırılımı                                       |
| MS_IZLEME1                                                                    | İzleme parametrik alan                                   |
| MS_IZLEME2                                                                    | İzleme parametrik alan                                   |
| MS_IZLEME3                                                                    | İzleme parametrik alan                                   |
| MS_IZLEME4                                                                    | İzleme parametrik alan                                   |
| MS_IZLEME5                                                                    | İzleme parametrik alan                                   |
| MS_IZLEME6                                                                    | İzleme parametrik alan                                   |
| MS_IZLEME7                                                                    | İzleme parametrik alan                                   |
| MS_IZLEME8                                                                    | İzleme parametrik alan                                   |
| MS_IZLEME9                                                                    | İzleme parametrik alan                                   |
| MS_IZLEME10                                                                   | İzleme parametrik alan                                   |
| MS_RET_NEDENI                                                                 | Ret nedeni                                               |
| MS_RET_TARIHI                                                                 | Ret tarihi                                               |
| MS_SIKAYET_KAT1                                                               | Şikayet kategorisi1                                      |
| MS_SIKAYET_KAT2                                                               | Şikayet kategorisi2                                      |

## **1.6. İç Müşteri Şikayetleri Modülünde Özet Raporu Replacement (Kısa Kodlar) Tag Tablosu**

İç Müşteri Şikayetleri Modülünde kullanılan İç Müşteri Şikayetleri Özet Raporu taglerin listesi aşağıdaki tabloda yer almaktadır.

| **Kısaltma (Kısalmalar tag şeklinde  \< \> isaretleri arasına yazılacaktır.)** | **Açıklama**                                                          |
|--------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| MKOD                                                                           | Müşteri Kodu                                                          |
| SKOD                                                                           | Şikayet Kodu                                                          |
| MREF                                                                           | Denetimden açılan Müşteri şikayetleri için referans kodu              |
| BILDIREN                                                                       | Bildiren kişi                                                         |
| BILDIRIMT                                                                      | Bildirim Tarihi                                                       |
| SIKAYETG                                                                       | Şikayet oluşturan sicil no                                            |
| SISTEMEKT                                                                      | Sisteme ekleme tarihi                                                 |
| SORUMLUD                                                                       | Sorumlu departman kodu                                                |
| SIKAYET                                                                        | Şikayet tanımı                                                        |
| SIKAYETD                                                                       | Şikayet detayı                                                        |
| URUN                                                                           | Ürün kodu                                                             |
| SEVKIYATM                                                                      | Toplam geri dönüş miktarı                                             |
| SIKAYETM                                                                       | Geri dönüş şikayet miktarı                                            |
| GERIODEME                                                                      | Geri dönüş ödeme tutarı                                               |
| ACIKLAMA                                                                       | Açıklama                                                              |
| GELRAPY                                                                        | Planlanan gelisme raporu tarihi                                       |
| DURUM                                                                          | Durum bilgisi                                                         |
| GELISMEYT                                                                      | Gelişme raporu yazma tarihi                                           |
| GELISMERP                                                                      | Gelişme raporu                                                        |
| GELEQUSON                                                                      | Gelişme ve Sonuç Raporu Aynı Olsun                                    |
| SONRAPY                                                                        | Planlanan sonuç raporu tarihi                                         |
| SONRP                                                                          | Sonuç raporu                                                          |
| LIDER                                                                          | Lider sicil numarası                                                  |
| PARABIRIMI                                                                     | Para birimi                                                           |
| GELKYTUSR                                                                      | Gelişme raporu yazan sicili                                           |
| SONRAPYT                                                                       | Sonuç raporu yazma tarihi                                             |
| SONKYTUSR                                                                      | Sonuç raporunu yazanın sicil numarası                                 |
| KAPATAN                                                                        | Kapatan kişinin sicil numarası                                        |
| KAPATMAT                                                                       | Kapatma tarihi                                                        |
| ICDIS                                                                          | İç veya dış müşteri şikayeti durumu                                   |
| SPARISNO                                                                       | Sipariş no                                                            |
| IRSALIYENO                                                                     | İrsaliye no                                                           |
| SEVKTARIHI                                                                     | Sevk tarihi                                                           |
| BIRIMSIKAYETM                                                                  | Geri dönüş şikayet miktar birimi                                      |
| BIRIMTOPLAM                                                                    | Toplam geri dönüş miktar birimi                                       |
| YETERLILIK                                                                     | Yeterlilik Bilgisi                                                    |
| HATA6M                                                                         | Hata parametrik alan                                                  |
| HATA5M                                                                         | Hata parametrik alan                                                  |
| HATA4M                                                                         | Hata parametrik alan                                                  |
| HATA3M                                                                         | Hata parametrik alan                                                  |
| HATA2M                                                                         | Hata parametrik alan                                                  |
| HATA1M                                                                         | Hata parametrik alan                                                  |
| HATA6T                                                                         | Hata parametrik alan                                                  |
| HATA5T                                                                         | Hata parametrik alan                                                  |
| HATA4T                                                                         | Hata parametrik alan                                                  |
| HATA3T                                                                         | Hata parametrik alan                                                  |
| HATA2T                                                                         | Hata parametrik alan                                                  |
| HATA1T                                                                         | Hata parametrik alan                                                  |
| BOLUM1                                                                         | Hata parametrik alan                                                  |
| BOLUM2                                                                         | Hata parametrik alan                                                  |
| BOLUM3                                                                         | Hata parametrik alan                                                  |
| BOLUM4                                                                         | Hata parametrik alan                                                  |
| BOLUM5                                                                         | Hata parametrik alan                                                  |
| BOLUM6                                                                         | Hata parametrik alan                                                  |
| ORAN6                                                                          | Hata parametrik alan                                                  |
| ORAN5                                                                          | Hata parametrik alan                                                  |
| ORAN4                                                                          | Hata parametrik alan                                                  |
| ORAN3                                                                          | Hata parametrik alan                                                  |
| ORAN2                                                                          | Hata parametrik alan                                                  |
| ORAN1                                                                          | Hata parametrik alan                                                  |
| REDNEDENI                                                                      | İptal nedeni                                                          |
| ISYERI_KODU                                                                    | İş yeri kodu                                                          |
| ILKCEV_PLANTAR                                                                 | Planlanan ilk cevap tarihi                                            |
| ILKCEV_GERTAR                                                                  | Gerçekleşen ilk cevap tarihi                                          |
| ILKCEV_GECNED                                                                  | İlk gecikme nedeni                                                    |
| SONCEV_PLANTAR                                                                 | Planlanan son cevap tarihi                                            |
| SONCEV_GERTAR                                                                  | Gerçekleşen son cevap tarihi                                          |
| SONCEV_GECNED                                                                  | Son cevap gecikme nedeni                                              |
| PPM_HATALIMIKTAR                                                               | PPMe Yansıyacak Hatalı Miktar                                         |
| CVPDA                                                                          | Cevap verme performansında dikkate alınması                           |
| SAADA                                                                          | Şikayet adedi analizinde dikkate alınması                             |
| MSH                                                                            | Müşteri şikayetinde haklıdır.                                         |
| HATA_PER1                                                                      | Hata personel tipli parametrik alan                                   |
| HATA_PER2                                                                      | Hata personel tipli parametrik alan                                   |
| HATA_PER3                                                                      | Hata personel tipli parametrik alan                                   |
| HATA_PER4                                                                      | Hata personel tipli parametrik alan                                   |
| HATA_PER5                                                                      | Hata personel tipli parametrik alan                                   |
| HATA_PER6                                                                      | Hata personel tipli parametrik alan                                   |
| HATA_PER_ORAN1                                                                 | Hata personel oranı parametrik alan                                   |
| HATA_PER_ORAN2                                                                 | Hata personel oranı parametrik alan                                   |
| HATA_PER_ORAN3                                                                 | Hata personel oranı parametrik alan                                   |
| HATA_PER_ORAN4                                                                 | Hata personel oranı parametrik alan                                   |
| HATA_PER_ORAN5                                                                 | Hata personel oranı parametrik alan                                   |
| HATA_PER_ORAN6                                                                 | Hata personel oranı parametrik alan                                   |
| REDDEDEN                                                                       | Reddeden bilgisi                                                      |
| SUREC_KODU                                                                     | Süreç kodu                                                            |
| ANKET_REF                                                                      | Anket referans kodu                                                   |
| GELISME_ALAN1                                                                  | Gelişme parametrik alan                                               |
| GELISME_ALAN2                                                                  | Gelişme parametrik alan                                               |
| GELISME_ALAN3                                                                  | Gelişme parametrik alan                                               |
| PARAM_MIKTAR1                                                                  | Parametrik alan                                                       |
| PARAM_MIKTAR2                                                                  | Parametrik alan                                                       |
| PARAM_BIRIM1                                                                   | Parametrik alan                                                       |
| PARAM_BIRIM2                                                                   | Parametrik alan                                                       |
| PARAM2                                                                         | Parametrik alan                                                       |
| PARAM3                                                                         | Parametrik alan                                                       |
| PARAM4                                                                         | Parametrik alan                                                       |
| PARAM5                                                                         | Parametrik alan                                                       |
| PARAM6                                                                         | Parametrik alan                                                       |
| PARAM7                                                                         | Parametrik alan                                                       |
| PARAM8                                                                         | Parametrik alan                                                       |
| PARAM9                                                                         | Parametrik alan                                                       |
| PARAM10                                                                        | Parametrik alan                                                       |
| NPARAM1                                                                        | Nümerik tipli parametrik alan                                         |
| NPARAM2                                                                        | Nümerik tipli parametrik alan                                         |
| NPARAM3                                                                        | Nümerik tipli parametrik alan                                         |
| NPARAM4                                                                        | Nümerik tipli parametrik alan                                         |
| NPARAM5                                                                        | Nümerik tipli parametrik alan                                         |
| NPARAM6                                                                        | Nümerik tipli parametrik alan                                         |
| NPARAM7                                                                        | Nümerik tipli parametrik alan                                         |
| NPARAM8                                                                        | Nümerik tipli parametrik alan                                         |
| NPARAM9                                                                        | Nümerik tipli parametrik alan                                         |
| NPARAM10                                                                       | Nümerik tipli parametrik alan                                         |
| NPARAM1_BIRIM                                                                  | Nümerik birim tiplerine ait parametrik alan                           |
| NPARAM2_BIRIM                                                                  | Nümerik birim tiplerine ait parametrik alan                           |
| NPARAM3_BIRIM                                                                  | Nümerik birim tiplerine ait parametrik alan                           |
| NPARAM4_BIRIM                                                                  | Nümerik birim tiplerine ait parametrik alan                           |
| NPARAM5_BIRIM                                                                  | Nümerik birim tiplerine ait parametrik alan                           |
| NPARAM6_BIRIM                                                                  | Nümerik birim tiplerine ait parametrik alan                           |
| NPARAM7_BIRIM                                                                  | Nümerik birim tiplerine ait parametrik alan                           |
| NPARAM8_BIRIM                                                                  | Nümerik birim tiplerine ait parametrik alan                           |
| NPARAM9_BIRIM                                                                  | Nümerik birim tiplerine ait parametrik alan                           |
| NPARAM10_BIRIM                                                                 | Nümerik birim tiplerine ait parametrik alan                           |
| DPARAM1                                                                        | Tarih tipli parametrik alan                                           |
| DPARAM2                                                                        | Tarih tipli parametrik alan                                           |
| DPARAM3                                                                        | Tarih tipli parametrik alan                                           |
| DPARAM4                                                                        | Tarih tipli parametrik alan                                           |
| DPARAM5                                                                        | Tarih tipli parametrik alan                                           |
| PPARAM1                                                                        | Personel tipli parametrik alan                                        |
| PPARAM2                                                                        | Personel tipli parametrik alan                                        |
| PPARAM3                                                                        | Personel tipli parametrik alan                                        |
| PPARAM4                                                                        | Personel tipli parametrik alan                                        |
| PPARAM5                                                                        | Personel tipli parametrik alan                                        |
| LPARAM1                                                                        | Liste tipli parametrik alan                                           |
| LPARAM2                                                                        | Liste tipli parametrik alan                                           |
| LPARAM3                                                                        | Liste tipli parametrik alan                                           |
| LPARAM4                                                                        | Liste tipli parametrik alan                                           |
| LPARAM5                                                                        | Liste tipli parametrik alan                                           |
| SISTEM_KODU                                                                    | Yönetim sistemi kodu                                                  |
| ONAY_DURUM                                                                     | Onay durumu                                                           |
| AKSIYON_DURUM                                                                  | Aksiyon Durumu                                                        |
| AKSIYON_SONUC_TARIHI                                                           | Aksiyon sonuç tarihi                                                  |
| DOF_SONUC_TARIHI                                                               | DOF sonuç tarihi                                                      |
| NERDEN                                                                         | Web servisten açılan kayıtlar için                                    |
| NERDEN_KOD                                                                     | Web servisten açılan kayıtlar için                                    |
| PARAM11                                                                        | Parametrik alan                                                       |
| PARAM12                                                                        | Parametrik alan                                                       |
| PARAM13                                                                        | Parametrik alan                                                       |
| PARAM14                                                                        | Parametrik alan                                                       |
| PARAM15                                                                        | Parametrik alan                                                       |
| LPARAM6                                                                        | Liste tipli parametrik alan                                           |
| LPARAM7                                                                        | Liste tipli parametrik alan                                           |
| LPARAM8                                                                        | Liste tipli parametrik alan                                           |
| LPARAM9                                                                        | Liste tipli parametrik alan                                           |
| LPARAM10                                                                       | Liste tipli parametrik alan                                           |
| KAPATMA_PARAM1                                                                 | Kapatma Parametrik alan                                               |
| KAPATMA_PARAM3                                                                 | Kapatma Parametrik alan                                               |
| KAPATMA_PARAM4                                                                 | Kapatma Parametrik alan                                               |
| KAPATMA_PARAM5                                                                 | Kapatma Parametrik alan                                               |
| KAPATMA_PARAM6                                                                 | Kapatma Parametrik alan                                               |
| KAPATMA_PARAM7                                                                 | Kapatma Parametrik alan                                               |
| KAPATMA_PARAM8                                                                 | Kapatma Parametrik alan                                               |
| KAPATMA_PARAM9                                                                 | Kapatma Parametrik alan                                               |
| KAPATMA_PARAM10                                                                | Kapatma Parametrik alan                                               |
| KAPATMA_LPARAM1                                                                | Kapatma Parametrik alan                                               |
| KAPATMA_LPARAM2                                                                | Kapatma Parametrik alan                                               |
| KAPATMA_LPARAM3                                                                | Kapatma Parametrik alan                                               |
| KAPATMA_LPARAM4                                                                | Kapatma Parametrik alan                                               |
| KAPATMA_LPARAM5                                                                | Kapatma Parametrik alan                                               |
| KAPATMA_LPARAM6                                                                | Kapatma Parametrik alan                                               |
| KAPATMA_LPARAM7                                                                | Kapatma Parametrik alan                                               |
| KAPATMA_LPARAM8                                                                | Kapatma Parametrik alan                                               |
| KAPATMA_LPARAM9                                                                | Kapatma Parametrik alan                                               |
| KAPATMA_LPARAM10                                                               | Kapatma Parametrik alan                                               |
| KAPATMA_NPARAM1                                                                | Kapatma Parametrik alan                                               |
| KAPATMA_NPARAM2                                                                | Kapatma Parametrik alan                                               |
| KAPATMA_NPARAM3                                                                | Kapatma Parametrik alan                                               |
| KAPATMA_NPARAM4                                                                | Kapatma Parametrik alan                                               |
| KAPATMA_NPARAM1_BIRIM                                                          | Kapatma Parametrik alan                                               |
| KAPATMA_NPARAM2_BIRIM                                                          | Kapatma Parametrik alan                                               |
| KAPATMA_NPARAM3_BIRIM                                                          | Kapatma Parametrik alan                                               |
| KAPATMA_NPARAM4_BIRIM                                                          | Kapatma Parametrik alan                                               |
| ESKI_DURUM                                                                     | Önceki durum                                                          |
| ESKI_ONAY_DURUM                                                                | Önceki onay durumu                                                    |
| ONAY_TARIHI                                                                    | Onay tarihi                                                           |
| ARACEV_PLANTAR                                                                 | Planlanan ara cevap tarihi                                            |
| ARACEV_GERTAR                                                                  | Gerçekleşen ara cevap tarihi                                          |
| ARACEV_GECNED                                                                  | Ara gecikme nedeni                                                    |
| UPARAM1                                                                        | Ürün tipli parametrik alan                                            |
| MPARAM1                                                                        | Müşteri tipli parametrik alan                                         |
| TDPARAM1                                                                       | Tedarikçi tipli parametrik alan                                       |
| RDFD_NO                                                                        | Risk kodu                                                             |
| PARAM17                                                                        | Parametrik alan                                                       |
| PARAM18                                                                        | Parametrik alan                                                       |
| PARAM19                                                                        | Parametrik alan                                                       |
| PARAM20                                                                        | Parametrik alan                                                       |
| OTOMATIK_AKSIYON                                                               | Otomatik aksiyon durumu                                               |
| QPARAM1                                                                        | Sorgu tipli parametrik alan                                           |
| QPARAM2                                                                        | Sorgu tipli parametrik alan                                           |
| QPARAM3                                                                        | Sorgu tipli parametrik alan                                           |
| QPARAM4                                                                        | Sorgu tipli parametrik alan                                           |
| QPARAM5                                                                        | Sorgu tipli parametrik alan                                           |
| LPARAM11                                                                       | Liste tipli parametrik alan                                           |
| LPARAM12                                                                       | Liste tipli parametrik alan                                           |
| LPARAM13                                                                       | Liste tipli parametrik alan                                           |
| LPARAM14                                                                       | Liste tipli parametrik alan                                           |
| LPARAM15                                                                       | Liste tipli parametrik alan                                           |
| LPARAM16                                                                       | Liste tipli parametrik alan                                           |
| LPARAM17                                                                       | Liste tipli parametrik alan                                           |
| LPARAM18                                                                       | Liste tipli parametrik alan                                           |
| LPARAM19                                                                       | Liste tipli parametrik alan                                           |
| LPARAM20                                                                       | Liste tipli parametrik alan                                           |
| NPARAM11                                                                       | Nümerik tipli parametrik alan                                         |
| NPARAM12                                                                       | Nümerik tipli parametrik alan                                         |
| NPARAM13                                                                       | Nümerik tipli parametrik alan                                         |
| NPARAM14                                                                       | Nümerik tipli parametrik alan                                         |
| NPARAM15                                                                       | Nümerik tipli parametrik alan                                         |
| NPARAM16                                                                       | Nümerik tipli parametrik alan                                         |
| NPARAM17                                                                       | Nümerik tipli parametrik alan                                         |
| NPARAM18                                                                       | Nümerik tipli parametrik alan                                         |
| NPARAM19                                                                       | Nümerik tipli parametrik alan                                         |
| NPARAM20                                                                       | Nümerik tipli parametrik alan                                         |
| NPARAM21                                                                       | Nümerik tipli parametrik alan                                         |
| NPARAM22                                                                       | Nümerik tipli parametrik alan                                         |
| NPARAM23                                                                       | Nümerik tipli parametrik alan                                         |
| NPARAM24                                                                       | Nümerik tipli parametrik alan                                         |
| NPARAM25                                                                       | Nümerik tipli parametrik alan                                         |
| NPARAM26                                                                       | Nümerik tipli parametrik alan                                         |
| NPARAM27                                                                       | Nümerik tipli parametrik alan                                         |
| NPARAM28                                                                       | Nümerik tipli parametrik alan                                         |
| NPARAM29                                                                       | Nümerik tipli parametrik alan                                         |
| NPARAM30                                                                       | Nümerik tipli parametrik alan                                         |
| NPARAM11_BIRIM                                                                 | Nümerik birim tiplerine ait parametrik alan                           |
| NPARAM12_BIRIM                                                                 | Nümerik birim tiplerine ait parametrik alan                           |
| NPARAM13_BIRIM                                                                 | Nümerik birim tiplerine ait parametrik alan                           |
| NPARAM14_BIRIM                                                                 | Nümerik birim tiplerine ait parametrik alan                           |
| NPARAM15_BIRIM                                                                 | Nümerik birim tiplerine ait parametrik alan                           |
| NPARAM16_BIRIM                                                                 | Nümerik birim tiplerine ait parametrik alan                           |
| NPARAM17_BIRIM                                                                 | Nümerik birim tiplerine ait parametrik alan                           |
| NPARAM18_BIRIM                                                                 | Nümerik birim tiplerine ait parametrik alan                           |
| NPARAM19_BIRIM                                                                 | Nümerik birim tiplerine ait parametrik alan                           |
| NPARAM20_BIRIM                                                                 | Nümerik birim tiplerine ait parametrik alan                           |
| NPARAM21_BIRIM                                                                 | Nümerik birim tiplerine ait parametrik alan                           |
| NPARAM22_BIRIM                                                                 | Nümerik birim tiplerine ait parametrik alan                           |
| NPARAM23_BIRIM                                                                 | Nümerik birim tiplerine ait parametrik alan                           |
| NPARAM24_BIRIM                                                                 | Nümerik birim tiplerine ait parametrik alan                           |
| NPARAM25_BIRIM                                                                 | Nümerik birim tiplerine ait parametrik alan                           |
| NPARAM26_BIRIM                                                                 | Nümerik birim tiplerine ait parametrik alan                           |
| NPARAM27_BIRIM                                                                 | Nümerik birim tiplerine ait parametrik alan                           |
| NPARAM28_BIRIM                                                                 | Nümerik birim tiplerine ait parametrik alan                           |
| NPARAM29_BIRIM                                                                 | Nümerik birim tiplerine ait parametrik alan                           |
| NPARAM30_BIRIM                                                                 | Nümerik birim tiplerine ait parametrik alan                           |
| PARAM21                                                                        | Parametrik alan                                                       |
| PARAM22                                                                        | Parametrik alan                                                       |
| PARAM23                                                                        | Parametrik alan                                                       |
| PARAM24                                                                        | Parametrik alan                                                       |
| PARAM25                                                                        | Parametrik alan                                                       |
| PARAM31                                                                        | Parametrik alan                                                       |
| PARAM32                                                                        | Parametrik alan                                                       |
| PARAM33                                                                        | Parametrik alan                                                       |
| PARAM34                                                                        | Parametrik alan                                                       |
| PARAM35                                                                        | Parametrik alan                                                       |
| LPARAM36                                                                       | Liste tipli parametrik alan                                           |
| LPARAM37                                                                       | Liste tipli parametrik alan                                           |
| LPARAM38                                                                       | Liste tipli parametrik alan                                           |
| LPARAM39                                                                       | Liste tipli parametrik alan                                           |
| LPARAM40                                                                       | Liste tipli parametrik alan                                           |
| NPARAM41                                                                       | Nümerik tipli parametrik alan                                         |
| NPARAM42                                                                       | Nümerik tipli parametrik alan                                         |
| NPARAM43                                                                       | Nümerik tipli parametrik alan                                         |
| NPARAM44                                                                       | Nümerik tipli parametrik alan                                         |
| NPARAM45                                                                       | Nümerik tipli parametrik alan                                         |
| NPARAM46                                                                       | Nümerik tipli parametrik alan                                         |
| NPARAM47                                                                       | Nümerik tipli parametrik alan                                         |
| NPARAM48                                                                       | Nümerik tipli parametrik alan                                         |
| NPARAM49                                                                       | Nümerik tipli parametrik alan                                         |
| NPARAM50                                                                       | Nümerik tipli parametrik alan                                         |
| NPARAM41_BIRIM                                                                 | Nümerik birim tiplerine ait parametrik alan                           |
| NPARAM42_BIRIM                                                                 | Nümerik birim tiplerine ait parametrik alan                           |
| NPARAM43_BIRIM                                                                 | Nümerik birim tiplerine ait parametrik alan                           |
| NPARAM44_BIRIM                                                                 | Nümerik birim tiplerine ait parametrik alan                           |
| NPARAM45_BIRIM                                                                 | Nümerik birim tiplerine ait parametrik alan                           |
| NPARAM46_BIRIM                                                                 | Nümerik birim tiplerine ait parametrik alan                           |
| NPARAM47_BIRIM                                                                 | Nümerik birim tiplerine ait parametrik alan                           |
| NPARAM48_BIRIM                                                                 | Nümerik birim tiplerine ait parametrik alan                           |
| NPARAM49_BIRIM                                                                 | Nümerik birim tiplerine ait parametrik alan                           |
| NPARAM50_BIRIM                                                                 | Nümerik birim tiplerine ait parametrik alan                           |
| KAPATMA_NPARAM5                                                                | Kapatma Parametrik alan                                               |
| KAPATMA_NPARAM6                                                                | Kapatma Parametrik alan                                               |
| KAPATMA_NPARAM7                                                                | Kapatma Parametrik alan                                               |
| KAPATMA_NPARAM8                                                                | Kapatma Parametrik alan                                               |
| KAPATMA_NPARAM9                                                                | Kapatma Parametrik alan                                               |
| KAPATMA_NPARAM10                                                               | Kapatma Parametrik alan                                               |
| KAPATMA_NPARAM5_BIRIM                                                          | Kapatma Parametrik alan                                               |
| KAPATMA_NPARAM6_BIRIM                                                          | Kapatma Parametrik alan                                               |
| KAPATMA_NPARAM7_BIRIM                                                          | Kapatma Parametrik alan                                               |
| KAPATMA_NPARAM8_BIRIM                                                          | Kapatma Parametrik alan                                               |
| KAPATMA_NPARAM9_BIRIM                                                          | Kapatma Parametrik alan                                               |
| KAPATMA_NPARAM10_BIRIM                                                         | Kapatma Parametrik alan                                               |
| DOF_NO                                                                         | DOF no                                                                |
| DEGERLENDIRME                                                                  | Değerlendirme bilgisi                                                 |
| DEGERLENDIRME_PUANI                                                            | Değerlendirme puanı bilgisi                                           |
| RET_TIPI                                                                       | Ret tipi                                                              |
| TERMINTARIHI                                                                   | Termin Tarihi                                                         |
| KAPATMA_DPARAM1                                                                | Kapatma Parametrik alan                                               |
| KAPATMA_DPARAM2                                                                | Kapatma Parametrik alan                                               |
| KAPATMA_DPARAM3                                                                | Kapatma Parametrik alan                                               |
| KAPATMA_DPARAM4                                                                | Kapatma Parametrik alan                                               |
| KAPATMA_DPARAM5                                                                | Kapatma Parametrik alan                                               |
| HATA1_BIRIM                                                                    | Hata tipli parametrik alan                                            |
| HATA2_BIRIM                                                                    | Hata tipli parametrik alan                                            |
| HATA3_BIRIM                                                                    | Hata tipli parametrik alan                                            |
| HATA4_BIRIM                                                                    | Hata tipli parametrik alan                                            |
| HATA5_BIRIM                                                                    | Hata tipli parametrik alan                                            |
| HATA6_BIRIM                                                                    | Hata tipli parametrik alan                                            |
| KAPATMA_PPARAM1                                                                | Kapatma personel tipli parametrik alan                                |
| KAPATMA_PPARAM2                                                                | Kapatma personel tipli parametrik alan                                |
| KAPATMA_PPARAM3                                                                | Kapatma personel tipli parametrik alan                                |
| KAPATMA_PPARAM4                                                                | Kapatma personel tipli parametrik alan                                |
| KAPATMA_PPARAM5                                                                | Kapatma personel tipli parametrik alan                                |
| KAPATMA_QPARAM1                                                                | Kapatma sorgu tipli parametrik alan                                   |
| KAPATMA_QPARAM2                                                                | Kapatma sorgu tipli parametrik alan                                   |
| KAPATMA_QPARAM3                                                                | Kapatma sorgu tipli parametrik alan                                   |
| KAPATMA_QPARAM4                                                                | Kapatma sorgu tipli parametrik alan                                   |
| KAPATMA_QPARAM5                                                                | Kapatma sorgu tipli parametrik alan                                   |
| MALIYET                                                                        | Maliyet bilgisi                                                       |
| MALIYET_BIRIM                                                                  | Maliyet birim bilgisi                                                 |
| T2_ADI                                                                         | Müşteri veya Tedarikçi Adı                                            |
| T3_ADISOYADI                                                                   | Aksiyon sorumlu adı soyadı                                            |
| T4_DEPARTMAN_ADI                                                               | Sorumlu Departman adı                                                 |
| T5_URUN_ADI                                                                    | Ürün adı                                                              |
| T6_ADISOYADI                                                                   | Ekip lideri adı soyadı                                                |
| T7_ADISOYADI                                                                   | Gelişme raporu yazan adı soyadı                                       |
| T8_ADISOYADI                                                                   | Sonuç raporunu yazanın adı soyadı                                     |
| T9_ADISOYADI                                                                   | Kapatan kişinin adı soyadı                                            |
| T10_ISYERI_ADI                                                                 | İş yeri adı                                                           |
| T11_ACIKLAMA                                                                   | Yönetim sistemi                                                       |
| MS_T12_URUN_ADI                                                                | Ürün Adı                                                              |
| MS_T12_SORUMLU                                                                 | Sorumlu sicil no                                                      |
| MS_T12_URUN_TIPI                                                               | Ürün tipi                                                             |
| MS_T13_ADISOYADI                                                               | Sorumlu adı soyadı                                                    |
| DURUM_ACK                                                                      | Durum açıklması                                                       |
| ISLEM_SURESI                                                                   | İşlem süresi                                                          |
| ILK_AKSIYON_TARIHI                                                             | İlk aksiyon tarihi                                                    |
| T2_TEDARIKCI_ADI                                                               | Tedarikçi adı                                                         |
| T2_MUSTERI_ADI                                                                 | Müşteri adı                                                           |
| URUN_TIPI                                                                      | Ürün tipi                                                             |
| URUN_GRUP                                                                      | Ürün grubu                                                            |
| IZLEME                                                                         | İzleme                                                                |
| YORUMLAR                                                                       | Yorumlar                                                              |
| KOK_TARIH                                                                      | Kök neden tarihi                                                      |
| IZLGUNTOP                                                                      | İzleme toplamı (gün olarak)                                           |
| TRH1                                                                           | Gelişme raporu yazma tarihi ile sisteme ekleme tarihi arasındaki fark |
| TRH2                                                                           | Sonuç raporu yazma tarihi ile sisteme ekleme tarihi arasındaki fark   |
| TRH3                                                                           | Kapatma tarihi ile sisteme ekleme tarihi arasındaki fark              |
| ILK_AKS_TARIHI                                                                 | Kaydın açılma tarihi                                                  |
| AKS_ALMA_SURESI                                                                | Aksiyon alma süresi (Kayıt tarihi ve onay tarihi arasındaki fark)     |
| GELISME_LPARAM1_VALUE                                                          | Gelişme parametrik alan                                               |
| GELISME_LPARAM10_VALUE                                                         | Gelişme parametrik alan                                               |
| GELISME_LPARAM2_VALUE                                                          | Gelişme parametrik alan                                               |
| GELISME_LPARAM3_VALUE                                                          | Gelişme parametrik alan                                               |
| GELISME_LPARAM4_VALUE                                                          | Gelişme parametrik alan                                               |
| GELISME_LPARAM5_VALUE                                                          | Gelişme parametrik alan                                               |
| GELISME_LPARAM6_VALUE                                                          | Gelişme parametrik alan                                               |
| GELISME_LPARAM7_VALUE                                                          | Gelişme parametrik alan                                               |
| GELISME_LPARAM8_VALUE                                                          | Gelişme parametrik alan                                               |
| GELISME_LPARAM9_VALUE                                                          | Gelişme parametrik alan                                               |
| GELISME_NPARAM1_VALUE                                                          | Gelişme parametrik alan                                               |
| GELISME_NPARAM2_VALUE                                                          | Gelişme parametrik alan                                               |
| GELISME_NPARAM3_VALUE                                                          | Gelişme parametrik alan                                               |
| GELISME_NPARAM4_VALUE                                                          | Gelişme parametrik alan                                               |
| GELISME_NPARAM5_VALUE                                                          | Gelişme parametrik alan                                               |
| GELISME_PPARAM1_VALUE                                                          | Gelişme parametrik alan                                               |
| GELISME_PPARAM2_VALUE                                                          | Gelişme parametrik alan                                               |
| GELISME_PPARAM3_VALUE                                                          | Gelişme parametrik alan                                               |
| GELISME_PPARAM4_VALUE                                                          | Gelişme parametrik alan                                               |
| GELISME_PPARAM5_VALUE                                                          | Gelişme parametrik alan                                               |
| SONUC_LPARAM1_VALUE                                                            | Sonuç parametrik alan                                                 |
| SONUC_LPARAM10_VALUE                                                           | Sonuç parametrik alan                                                 |
| SONUC_LPARAM2_VALUE                                                            | Sonuç parametrik alan                                                 |
| SONUC_LPARAM3_VALUE                                                            | Sonuç parametrik alan                                                 |
| SONUC_LPARAM4_VALUE                                                            | Sonuç parametrik alan                                                 |
| SONUC_LPARAM5_VALUE                                                            | Sonuç parametrik alan                                                 |
| SONUC_LPARAM6_VALUE                                                            | Sonuç parametrik alan                                                 |
| SONUC_LPARAM7_VALUE                                                            | Sonuç parametrik alan                                                 |
| SONUC_LPARAM8_VALUE                                                            | Sonuç parametrik alan                                                 |
| SONUC_LPARAM9_VALUE                                                            | Sonuç parametrik alan                                                 |
| SONUC_NPARAM1_VALUE                                                            | Sonuç parametrik alan                                                 |
| SONUC_NPARAM2_VALUE                                                            | Sonuç parametrik alan                                                 |
| SONUC_NPARAM3_VALUE                                                            | Sonuç parametrik alan                                                 |
| SONUC_NPARAM4_VALUE                                                            | Sonuç parametrik alan                                                 |
| SONUC_NPARAM5_VALUE                                                            | Sonuç parametrik alan                                                 |
| SONUC_PPARAM1_VALUE                                                            | Sonuç parametrik alan                                                 |
| SONUC_PPARAM2_VALUE                                                            | Sonuç parametrik alan                                                 |
| SONUC_PPARAM3_VALUE                                                            | Sonuç parametrik alan                                                 |
| SONUC_PPARAM4_VALUE                                                            | Sonuç parametrik alan                                                 |
| SONUC_PPARAM5_VALUE                                                            | Sonuç parametrik alan                                                 |
| DEGERLENDIRME_KATEGORISI                                                       | Değerlendirme kategorisi                                              |
| DEGERLENDIRME_ALT_KATEGORISI                                                   | Derlendirme alt kategorisi                                            |
| DEGERLENDIRME_TUTAR                                                            | Derlendirme tutar                                                     |
| DEGERLENDIRME_TUTAR_BIRIM                                                      | Derlendirme tutar birim                                               |
| DEGERLENDIRME_TARIH                                                            | Derlendirme tarih                                                     |
| DEGERLENDIRME_ACIKLAMA                                                         | Derlendirme açıklama                                                  |
| DEGERLENDIRME_KATEGORILERI                                                     | Derlendirme kategorileri                                              |
| DEGERLENDIRME_SECENEK                                                          | Derlendirme seçenek                                                   |
| DEGERLENDIRME_PUAN                                                             | Derlendirme puan                                                      |
| DEGERLENDIRME_MIKTAR                                                           | Derlendirme miktar                                                    |
| DEGERLENDIRME_BIRIM                                                            | Derlendirme birim                                                     |
| DEGERLENDIRME_DEGERLENDIREN                                                    | Değerlendiren bilgisi                                                 |
| DEGERLENDIRME_DEGERLENDIRMET                                                   | Değerlendirme Tarihi                                                  |
| ULKE                                                                           | Ulke bilgisi                                                          |
| IL                                                                             | İl bilgisi                                                            |
| SIKAYET_ANA_KAT_KOD                                                            | Ana şikayet kategori kodu                                             |
| SIKAYET_ANA_KAT                                                                | Ana şikayet kategorisi                                                |
| SIKAYET_ALT_KAT_KOD                                                            | Alt şikayet kategori kodu                                             |
| SIKAYET_ALT_KAT                                                                | Alt şikayet kategorisi                                                |
| SIKAYET_KODLAR                                                                 | Şikayet kodlarının bilgisi                                            |
| MS_EKIP                                                                        | Ekip üyeleri                                                          |
| MNPARAM1                                                                       | Madde no parametrik alan                                              |
| DOF_AKSIYON_TARIHI                                                             | DOF aksiyon tarihi                                                    |
| KOK_NEDENLER                                                                   | Kök nedenler                                                          |
| KOK_NEDEN_KIRILIM                                                              | Kök neden kırılımı                                                    |
| IZLEME1                                                                        | İzleme parametrik alan                                                |
| SIKAYET_KAT1                                                                   | İzleme parametrik alan                                                |
| IZLEME2                                                                        | İzleme parametrik alan                                                |
| SIKAYET_KAT2                                                                   | İzleme parametrik alan                                                |
| IZLEME3                                                                        | İzleme parametrik alan                                                |
| SIKAYET_KAT3                                                                   | İzleme parametrik alan                                                |
| IZLEME4                                                                        | İzleme parametrik alan                                                |
| SIKAYET_KAT4                                                                   | İzleme parametrik alan                                                |
| IZLEME5                                                                        | İzleme parametrik alan                                                |
| SIKAYET_KAT5                                                                   | İzleme parametrik alan                                                |
| IZLEME6                                                                        | İzleme parametrik alan                                                |
| SIKAYET_KAT6                                                                   | İzleme parametrik alan                                                |
| IZLEME7                                                                        | İzleme parametrik alan                                                |
| SIKAYET_KAT7                                                                   | İzleme parametrik alan                                                |
| IZLEME8                                                                        | İzleme parametrik alan                                                |
| SIKAYET_KAT8                                                                   | İzleme parametrik alan                                                |
| IZLEME9                                                                        | İzleme parametrik alan                                                |
| SIKAYET_KAT9                                                                   | İzleme parametrik alan                                                |
| IZLEME10                                                                       | İzleme parametrik alan                                                |
| SIKAYET_KAT10                                                                  | İzleme parametrik alan                                                |
| IZLEME11                                                                       | İzleme parametrik alan                                                |
| SIKAYET_KAT11                                                                  | İzleme parametrik alan                                                |
| IZLEME12                                                                       | İzleme parametrik alan                                                |
| SIKAYET_KAT12                                                                  | İzleme parametrik alan                                                |
| IZLEME13                                                                       | İzleme parametrik alan                                                |
| SIKAYET_KAT13                                                                  | İzleme parametrik alan                                                |
| IZLEME14                                                                       | İzleme parametrik alan                                                |
| SIKAYET_KAT14                                                                  | İzleme parametrik alan                                                |
| IZLEME15                                                                       | İzleme parametrik alan                                                |
| SIKAYET_KAT15                                                                  | İzleme parametrik alan                                                |
| IZLEME16                                                                       | İzleme parametrik alan                                                |
| SIKAYET_KAT16                                                                  | İzleme parametrik alan                                                |
| IZLEME17                                                                       | İzleme parametrik alan                                                |
| SIKAYET_KAT17                                                                  | İzleme parametrik alan                                                |
| IZLEME18                                                                       | İzleme parametrik alan                                                |
| SIKAYET_KAT18                                                                  | İzleme parametrik alan                                                |
| IZLEME19                                                                       | İzleme parametrik alan                                                |
| SIKAYET_KAT19                                                                  | İzleme parametrik alan                                                |
| IZLEME20                                                                       | İzleme parametrik alan                                                |
| SIKAYET_KAT20                                                                  | İzleme parametrik alan                                                |
| IZLEME21                                                                       | İzleme parametrik alan                                                |
| SIKAYET_KAT21                                                                  | İzleme parametrik alan                                                |
| IZLEME22                                                                       | İzleme parametrik alan                                                |
| SIKAYET_KAT22                                                                  | İzleme parametrik alan                                                |
| IZLEME23                                                                       | İzleme parametrik alan                                                |
| SIKAYET_KAT23                                                                  | İzleme parametrik alan                                                |
| IZLEME24                                                                       | İzleme parametrik alan                                                |
| SIKAYET_KAT24                                                                  | İzleme parametrik alan                                                |
| IZLEME25                                                                       | İzleme parametrik alan                                                |
| SIKAYET_KAT25                                                                  | İzleme parametrik alan                                                |
| IZLEME26                                                                       | İzleme parametrik alan                                                |
| SIKAYET_KAT26                                                                  | İzleme parametrik alan                                                |
| IZLEME27                                                                       | İzleme parametrik alan                                                |
| SIKAYET_KAT27                                                                  | İzleme parametrik alan                                                |
| IZLEME28                                                                       | İzleme parametrik alan                                                |
| SIKAYET_KAT28                                                                  | İzleme parametrik alan                                                |
| IZLEME29                                                                       | İzleme parametrik alan                                                |
| SIKAYET_KAT29                                                                  | İzleme parametrik alan                                                |
| IZLEME30                                                                       | İzleme parametrik alan                                                |
| SIKAYET_KAT30                                                                  | İzleme parametrik alan                                                |
| IZLEME31                                                                       | İzleme parametrik alan                                                |
| SIKAYET_KAT31                                                                  | İzleme parametrik alan                                                |
| IZLEME32                                                                       | İzleme parametrik alan                                                |
| SIKAYET_KAT32                                                                  | İzleme parametrik alan                                                |
| IZLEME33                                                                       | İzleme parametrik alan                                                |
| SIKAYET_KAT33                                                                  | İzleme parametrik alan                                                |
| IZLEME34                                                                       | İzleme parametrik alan                                                |
| SIKAYET_KAT34                                                                  | İzleme parametrik alan                                                |
| IZLEME35                                                                       | İzleme parametrik alan                                                |
| SIKAYET_KAT35                                                                  | İzleme parametrik alan                                                |
| IZLEME36                                                                       | İzleme parametrik alan                                                |
| SIKAYET_KAT36                                                                  | İzleme parametrik alan                                                |
| IZLEME37                                                                       | İzleme parametrik alan                                                |
| SIKAYET_KAT37                                                                  | İzleme parametrik alan                                                |
| IZLEME38                                                                       | İzleme parametrik alan                                                |
| SIKAYET_KAT38                                                                  | İzleme parametrik alan                                                |
| IZLEME39                                                                       | İzleme parametrik alan                                                |
| SIKAYET_KAT39                                                                  | İzleme parametrik alan                                                |
| IZLEME40                                                                       | İzleme parametrik alan                                                |
| SIKAYET_KAT40                                                                  | İzleme parametrik alan                                                |
| IZLEME41                                                                       | İzleme parametrik alan                                                |
| SIKAYET_KAT41                                                                  | İzleme parametrik alan                                                |
| IZLEME42                                                                       | İzleme parametrik alan                                                |
| SIKAYET_KAT42                                                                  | İzleme parametrik alan                                                |
| IZLEME43                                                                       | İzleme parametrik alan                                                |
| SIKAYET_KAT43                                                                  | İzleme parametrik alan                                                |
| IZLEME44                                                                       | İzleme parametrik alan                                                |
| SIKAYET_KAT44                                                                  | İzleme parametrik alan                                                |
| IZLEME45                                                                       | İzleme parametrik alan                                                |
| SIKAYET_KAT45                                                                  | İzleme parametrik alan                                                |
| IZLEME46                                                                       | İzleme parametrik alan                                                |
| SIKAYET_KAT46                                                                  | İzleme parametrik alan                                                |
| IZLEME47                                                                       | İzleme parametrik alan                                                |
| SIKAYET_KAT47                                                                  | İzleme parametrik alan                                                |
| IZLEME48                                                                       | İzleme parametrik alan                                                |
| SIKAYET_KAT48                                                                  | İzleme parametrik alan                                                |
| IZLEME49                                                                       | İzleme parametrik alan                                                |
| SIKAYET_KAT49                                                                  | İzleme parametrik alan                                                |
| IZLEME50                                                                       | İzleme parametrik alan                                                |
| SIKAYET_KAT50                                                                  | İzleme parametrik alan                                                |
| RET_NEDENI                                                                     | Ret nedeni                                                            |
| RET_TARIHI                                                                     | Ret tarihi                                                            |
| URUN_KODU                                                                      | Ürün kodu                                                             |
| SUREC_ADI                                                                      | Süreç Adı                                                             |
| HATAMIKTARI                                                                    | Hata miktarı                                                          |
| HATATUTARI                                                                     | Hata tutarı                                                           |
| HATATUTARI1                                                                    | Hata tutarı parametrik alan                                           |
| HATATUTARI2                                                                    | Hata tutarı parametrik alan                                           |
| HATATUTARI3                                                                    | Hata tutarı parametrik alan                                           |
| HATATUTARI4                                                                    | Hata tutarı parametrik alan                                           |
| HATATUTARI5                                                                    | Hata tutarı parametrik alan                                           |
| HATATUTARI6                                                                    | Hata tutarı parametrik alan                                           |
| KAPATMAONAY_0                                                                  | Kapatma onaycıları ve tarihler(10' a kadar gidiyor)                   |
| ACMAONAY_0                                                                     | Açma onaycıları ve tarihler(10' a kadar gidiyor)                      |
| KAPATMAONAYTAR_0                                                               | Kapatma onay tarihi(10' a kadar gidiyor)                              |
| ACMAONAYTAR_0                                                                  | Açma onay tarihi(10' a kadar gidiyor)                                 |
| ACMASURE_0                                                                     | Açma onay süresi(10' a kadar gidiyor)                                 |
| KAPATMASURE_0                                                                  | Kapatma onay süresi(10' a kadar gidiyor)                              |
| ACMAONAYNOTU_0                                                                 | Açma onay notu(10' a kadar gidiyor)                                   |
| KAPATMAONAYNOTU_0                                                              | Kapatma onay notu(10' a kadar gidiyor)                                |
| ACMABASLAMATARIHI_0                                                            | Açma onayı başlama tarihi(10' a kadar gidiyor)                        |
| TOPLAM_ACMASURE                                                                | Toplam açma onay süresi                                               |
| TOPLAM_KAPATMASURE                                                             | Toplam kapatma onay süresi                                            |
