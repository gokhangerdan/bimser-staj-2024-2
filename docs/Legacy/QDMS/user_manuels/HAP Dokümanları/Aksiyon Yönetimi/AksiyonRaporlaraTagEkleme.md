---
title: Raporlara Parametrik Alan Ekleme İşlemi ve Genel Tag Listesi
description: Raporlara Parametrik Alan Ekleme İşlemi ve Genel Tag Listesi Kullanıcı Yardım Dokümanı
sidebar_position: 2
---

:::tip Bilgi

İlgili konu başlığına sağ tarafta bulunan navigasyon yardımıyla hızlı bir şekilde ulaşabilirsiniz.

:::


**Aksiyon Yönetim Modülünde Raporlara Parametrik Alan Ekleme İşlemi ve Genel Tag Listesi Kullanıcı Yardım Dokümanı**


## **1.Aksiyon Yönetim Modülünde Raporlara Parametrik Alan Ekleme İşlemi ve Raporlarda Kullanılan Taglar**

Aksiyon Yönetimi Modülü raporlarından Kalemler Detayında raporunun rapor formatı olan “AKSIYON_YATAY_RAP.xls” formatına parametrik alan ekleme işlemi yapılmaktadır. Raporlara bu parametrik alan ekleme işlem basamakları ve Aksiyon Yönetimi Modülünde kullanılan taglerin (kısa kodların) listesi bu yardım dokümanında yer almaktadır.

## **1.1.Aksiyon Yönetimi Modülünde Dil Ayarlarında Tanımlanan Parametrik Alan Tiplerinin Aksiyon Kalemi Raporunda Gösterimi**

Aksiyon Yönetimi Modülü raporlarında Kalemler Detayında raporunun formatına eklenen parametrik alanların raporda gösterilme işlemi için öncelikle dil ayarları menüsünde parametrik alan tanımlama işlemi yapmak gerekiyor. Aksiyon Planlama ekranında Kalemler butonu tıklanarak açılan Aksiyon Kalemi Tanımlama ekranında Yeni butonu tıklanarak açılan Aksiyon Kalemi Planlama-Yeni Kayıt ekranında Dil ayarları menüsünde kalem bazında parametrik alan tanımlaması yapılmaktadır. Aksiyon Yönetimi Modülünde kısa kodlarda lblK-yani sonunda K olanlar- “Kalemler” sayfasında alan tanımlamada kullanılmaktadır ve bu sayfada gözükmektedir. Bu parametrik alan tiplerin Aksiyon Kalemi Planlama -Yeni Kayıt ekranında gözükmesi için Aksiyon parametrelerinden 30 numaralı “Aksiyon kaynağı bazında parametrik alan kullanılacak mı” parametrenin parametre değeri “Evet” seçilerek parametre aktif edilmelidir. Dil ayarlarında kalemler bazında metin, liste gibi parametrik alan tipleri tanımlama işlemi yapılır. Bu tanımlanan parametrik alan tipleri Aksiyon Yönetim Modülünde Aksiyon Kalemi Planlama ekranında görüntülenir. Bir Aksiyon kalemi planlama işleminde tanımlı olan bu parametrik alan tiplerinin bilgisi girilir. Aksiyon Kalemi Planlama işleminde sonra Rapor Formatları Düzenleme menüsüne gidilir. Rapor Formatları Düzenleme menüsünde Kalemler Detayında raporunun rapor format (AKSIYON_YATAY_RAP.xls) indirilir. İndirilen bu rapor formatına (AKSIYON_YATAY_RAP.xls) dil ayarlarında tanımlanan liste tipli alanların için örneğin “lblK_LALAN1” alan kodunun lblK olmadan <LALAN1\>tag içerisine yazılarak eklenir. Metin tipli alanlar için örneğin “lblK_ALAN1” alan kodunun lblK olmadan <ALAN1\> tag içerisine yazılarak rapor formatına eklenir. Bu şekilde kalem bazında dil ayarlarından tanımlanıp, Aksiyon Kalemi planlama ekranında görüntülen parametrik alanların Kalemler detayı rapor formatına tag şeklinde yazılır. Rapor formatına parametrik alanların tag şeklinde yazıldıktan Rapor format (AKSIYON_YATAY_RAP.xls) aynı isimde bilgisayara kaydedilir. Kaydedilen aynı isimde Kalemler detayında Rapor formatı Rapor Formatları Düzenleme menüsünde tekrar sisteme yüklenir. Kalemler Detayında Rapor formatının yükleme işleminde sonra Aksiyon Yönetimin Raporlarında Kalemler Detayında menüsüne gidilir. Açılan Aksiyon Kalemi Raporunda Aksiyon Kalemin bulunduğu Ana Aksiyon No bilgisi yazılarak Ara butonu tıklanarak tanımlanan Aksiyon Kalemi Planı görüntülenir. Aksiyon Planlama kalemi seçili iken Excel aktar butonu tıklanarak Excel format alınan raporda parametrik alanların taglerinin bulunduğu kısımda girilen alan bilgilerinin geldiği görülerek taglerin çalıştığı görülür.

## **1.2.Aksiyon Yönetim Modülünde Kaynak Bazlı Tanımlanan Parametrik Alan Tiplerini Aksiyon Kalemi Raporunda Gösterimi**


Kaynak Bazlı Parametrik Alanların Aksiyon Kalemi Raporunda gösterilme işleminde Aksiyon Parametrelerinde 30 numaralı “Aksiyon kaynağı bazında parametrik alan kullanılacak mı” parametresi aktif edilir. Parametre akif edildikten sonra Aksiyon Kaynağı tanımlama menüsünde ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload588ffbd2-7ffa-4a4d-8a93-58d4520b693c) (Alan Tanımlama) butonu görüntülenir. Alan tanımlama butonu tıklanıldığında açılan ekranda Kalemler sekmesinde kaynak bazlı parametrik alan tipi tanımlama işlemi yapılır. Kaynak bazlı alan tanımlama işleminde sonra Planlama menüsünde parametrik Alan tipleri tanımlaması yapılan Aksiyon kaynağı ile ilgili bir Ana Aksiyon Planı tanımlanır. Tanımlanan Ana aksiyon Planlama menüsünde Kalemler butonu tıklanarak açılan ekranda Yeni butonu ile yeni bir Aksiyon Kalemi Planlama işlemi yapılır. Bu aksiyon Kalemi Planlama ekranında tanımlanan kaynak bazlı parametrik alanların bilgi girişleri yapılır. Aksiyon Kalemi Planlama ekranda kaynak bazlı alanların bilgi girişleri yapıldıktan sonra Rapor Formatları düzenleme menüsü tıklanılır. Aksiyon Kalemi Rapor formatı görüntüle butonu ile bilgisayara indirilir. İndirilen Rapor formatına “<AKS_KAYNAK_PARAM\>” tag’i eklenir. Tag eklenen Rapor format aynı isimde Rapor Formatları Düzenleme menüsünde tekrar sisteme yüklenir. Rapor formatının sisteme yükleme işleminde sonra Entegre Yönetim Sistemi\>Aksiyon Yönetimi\>Raporlar\>Kalemler detayında menüsü tıklanılır. Açılan Aksiyon Kalemi Raporu ekranında "Aksiyon Arama" sekmesinde ilk olarak rapor çekmek istediğiniz aksiyon kaynağını seçilir ve en üstte bulunan "Kaynak bazında rapor al" alanını ilgili check box işaretlenir ve "Excele aktar" butonuna basılarak rapor alınır. Alınan raporda tek bir tag ile tanımlanan kaynak bazlı parametrik alanların tanımları ve bilgi girişlerinin geldiği görülür.

### **1.1.1.Aksiyon Yönetimi Modülünde Dil Ayarlarından Parametrik Alan Tipi Tanımlama**

Aksiyon Yönetimi Modülünde Parametrik ekleme işlemi için SAT\>BSAT\>Konfigürasyon Ayarları\>Dil ayarları menüsüne gidilir. Modüller alanında Aksiyon Yönetimi Modülü seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload98e8d76b-5670-43df-9f7c-c3356409b525)

Aksiyon Yönetimi Modülünü seçildikten sonra Liste geldikten sonra Başlıklar sekmesine tipi alanı parametrik alanın tipi yazılarak parametrik alanların listelenmesi sağlanılır. Kalemler bazında metin, metin(Çoklu Satır), tarih, personel, nümerik, ölçü, sorgu ve parasal tipli parametrik alan tanımlaması yapılır. Bu tanımlanan parametrik alan tipleri tagleri Aksiyon Modülü Kalemler detayında raporun formatına yazılarak alanların bilgisinin rapora basılması sağlanır.

### **1.1.1.1.Tarih Tipli Parametrik Alan Tipi Listesi**

Aksiyon Yönetimi Modülünde Aksiyon Planlama ekranında Kalemler butonu tıklanarak açılan Aksiyon Kalemi Tanımlama ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1882e68c-3493-484b-9f2d-3be7f7141edb)(Yeni) butonu tıklanarak açılan Aksiyon Kalemi Planlama-Yeni Kayıt ekranında Tarih tipli bir alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Tarih yazarak Tarih tipli parametrik alanlar aratılır ve Tarih tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Tarih tipli parametrik alanların alan tanımlaması yapılır. Bu alan tanımlaması yapılan tarih tipli parametrik alanları lblK\_ kısa kodu kaldırarak:

<DALAN1\>,<DALAN2\>,….<DALAN10\> şeklinde Aksiyon Kalemi Raporu formatına tag şeklinde eklendiğinde Aksiyon Kalemi Planlama ekranında tarih tipli alanların girilen değerleri bilgisi ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcc01ade1-45d9-4bd6-897e-5d02320a0d56)(Excel aktar) butonu tıklanarak alınan Excel formatındaki rapora basılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade1731eb0-4b14-429b-8223-e9f39c2d99ef)

### **1.1.1.2.Tarih Tipli Parametrik Alan Tipi Tanımlama**

Rapor formatına eklenecek Tarih tipli parametrik bir alan tanımlaması yapılır. lblK_DALAN2 Tarih tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload84d1f856-1f74-4079-82c1-1510d21f152d) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload99240092-b290-4299-bfa7-d47fefebd2f0)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload83243e6f-e0b0-4b08-854c-a9e3a09f3fac)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload69814fe9-142c-4b0b-99b3-0bbac2bea125)(Kaydet) butonu tıklanarak tarih tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload66f6d88d-e163-4b13-a710-c3a18b96e499)

Tanımlanan tarih tipli parametrik alan Aksiyon Planlama ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7258e64c-6bdb-47a2-8826-4c2ee905cceb)(Kalemler) butonu tıklanarak açılan Aksiyon Kalemi Tanımlama ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1882e68c-3493-484b-9f2d-3be7f7141edb)(Yeni) butonu tıklanarak açılan Aksiyon Kalemi Planlama-Yeni Kayıt ekranında görüntülenir. Tanımlanan tarih tipli parametrik alanın “lblK_DALAN2” lblK\_ kısa kod kısmı kaldırarak Aksiyon Kalemi Raporunun rapor formatına <DALAN2\> tag şeklinde bilgisi yazılır. Bir Aksiyon Kalemi Planlama işleminde bu tarih tipli alanın bilgisi girildiğinde Aksiyon Kaleminin Raporu alındığında tarih tipli alanın girilen bilgisi rapora basılacaktır.

### **1.1.1.3.Liste Tipli Parametrik Alan Tiplerin Listesi**

Aksiyon Yönetimi Modülünde Aksiyon Planlama ekranında Kalemler butonu tıklanarak açılan Aksiyon Kalemi Tanımlama ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1882e68c-3493-484b-9f2d-3be7f7141edb)(Yeni) butonu tıklanarak açılan Aksiyon Kalemi Planlama-Yeni Kayıt ekranında Liste tipli bir alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Liste yazarak Liste tipli parametrik alanlar aratılır ve Liste tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Liste tipli parametrik alanların alan tanımlaması yapılır. Bu alan tanımlaması yapılan Liste tipli parametrik alanları lblK\_ kısa kodu kaldırarak:

<LALAN1\>,<LALAN2\>,…<LALAN10\> şeklinde Aksiyon Kalemi Raporu formatına tag şeklinde eklendiğinde Aksiyon Kalemi Planlama ekranında Liste tipli alanların girilen değerleri bilgisi ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcc01ade1-45d9-4bd6-897e-5d02320a0d56)(Excel aktar )butonu tıklanarak alınan Excel formatındaki rapora basılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload96bafe5f-2862-4a64-be6d-08e755cee60a)

### **1.1.1.4. Liste Tipli Parametrik Alan Tipi Tanımlama**

Rapor formatına eklenecek liste tipli parametrik bir alan tanımlaması yapılır. lblK_LALAN2 Liste tipli parametrik seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload84d1f856-1f74-4079-82c1-1510d21f152d) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload371e15d1-7735-4ce3-8976-9f6b62749ebe)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadeacc65d9-ec68-4bd2-9216-4686cb07ea82)

Liste tipli alanın liste değerlerini girmek için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6040e345-42e6-46cd-9525-03f127aab8f6) (Yeni) butonuna tıklanır, liste değerleri yazılır ve kaydedilir. Liste eleman değeri 1 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade206cfee-3d96-4f40-90e2-6a7764584939)

Liste eleman değeri 2 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf485e52c-24cb-49e5-b424-f7a291f92d0b)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade8f70d86-8bf8-4db5-86be-74d02a9e6d4b)

Alanın zorunlu olup, olmayacağı sıra no bilgisi ve liste elemanları tanımlanarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload69814fe9-142c-4b0b-99b3-0bbac2bea125)(kaydet) butonu tıklanarak liste tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadce52a3c5-d311-4f81-b42b-3b4d0ec9a5ed)

Tanımlanan liste tipli parametrik alan Aksiyon Planlama ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7258e64c-6bdb-47a2-8826-4c2ee905cceb)(Kalemler) butonu tıklanarak açılan Aksiyon Kalemi Tanımlama ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1882e68c-3493-484b-9f2d-3be7f7141edb)(Yeni) butonu tıklanarak açılan Aksiyon Kalemi Planlama-Yeni Kayıt ekranında görüntülenir. Tanımlanan liste tipli parametrik alanın “lblK_LLAN2” lblK\_ kısa kod kısmı kaldırarak Aksiyon Kalemi Raporunun rapor formatına <LALAN2\> tag şeklinde bilgisi yazılır. Bir Aksiyon Kalemi Planlama işleminde bu liste tipli alanın bilgisi girildiğinde Aksiyon Kaleminin Raporu alındığında liste tipli alanın girilen bilgisi rapora basılacaktır.

### **1.1.1.5. Personel Tipli Parametrik Alan Tipleri Listesi**

Aksiyon Yönetimi Modülünde Aksiyon Planlama ekranında Kalemler butonu tıklanarak açılan Aksiyon Kalemi Tanımlama ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1882e68c-3493-484b-9f2d-3be7f7141edb)(Yeni) butonu tıklanarak açılan Aksiyon Kalemi Planlama-Yeni Kayıt ekranında Personel tipli bir alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Personel yazarak Personel tipli parametrik alanlar aratılır ve Personel tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Personel tipli parametrik alanların alan tanımlaması yapılır. Bu alan tanımlaması yapılan Personel tipli parametrik alanları lblK\_ kısa kodu kaldırarak:

<PALAN1\><PALAN2\>,…. <PALAN10\> şeklinde Aksiyon Kalemi Raporu formatına tag şeklinde eklendiğinde Aksiyon Kalemi Planlama ekranında Personel tipli alanların girilen değerleri bilgisi ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcc01ade1-45d9-4bd6-897e-5d02320a0d56)(Excel aktar) butonu tıklanarak alınan Excel formatındaki rapora basılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfa845f65-ca4e-4e0a-9ab1-38bce42746f9)

### **1.1.1.6. Personel Tipli Parametrik Alan Tipi Tanımlama.**

Rapor formatına eklenecek Personel tipli parametrik bir alan tanımlaması yapılır. lblK_PALAN2 Personel tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload84d1f856-1f74-4079-82c1-1510d21f152d) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadec041d8d-4cef-4f72-be1c-e88edd94c08c)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload841904d4-aa8f-4ddc-867d-75b7634e6ed7)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload69814fe9-142c-4b0b-99b3-0bbac2bea125)(kaydet) butonu tıklanarak Personel tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload64535a59-63bb-400a-a03c-c1f65c6d02cb)

Tanımlanan Personel tipli parametrik alan Aksiyon Planlama ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7258e64c-6bdb-47a2-8826-4c2ee905cceb)(Kalemler) butonu tıklanarak açılan Aksiyon Kalemi Tanımlama ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1882e68c-3493-484b-9f2d-3be7f7141edb)(Yeni) butonu tıklanarak açılan Aksiyon Kalemi Planlama-Yeni Kayıt ekranında görüntülenir. Tanımlanan Personel tipli parametrik alanın “lblK_PALAN2” lblK\_ kısa kod kısmı kaldırarak Aksiyon Kalemi Raporunun rapor formatına <PALAN2\> tag şeklinde bilgisi yazılır. Bir Aksiyon Kalemi Planlama işleminde bu Personel tipli alanın bilgisi girildiğinde Aksiyon Kaleminin raporu alındığında Personel tipli alanın girilen bilgisi rapora basılacaktır.

### **1.1.1.7. Sorgu Tipli Parametrik Alan Tipleri Listesi**

Aksiyon Yönetimi Modülünde Aksiyon Planlama ekranında Kalemler butonu tıklanarak açılan Aksiyon Kalemi Tanımlama ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1882e68c-3493-484b-9f2d-3be7f7141edb)(Yeni) butonu tıklanarak açılan Aksiyon Kalemi Planlama-Yeni Kayıt ekranında Sorgu tipli bir alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Sorgu yazarak Sorgu tipli parametrik alanlar aratılır ve Sorgu tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Sorgu tipli parametrik alanların alan tanımlaması yapılır. Bu alan tanımlaması yapılan Sorgu tipli parametrik alanları lblK\_ kısa kodu kaldırarak:

<QALAN1\>,<QALAN2\>,….<QALAN10\> şeklinde Aksiyon Kalemi Raporu formatına tag şeklinde eklendiğinde Aksiyon Kalemi Planlama ekranında Sorgu tipli alanların girilen değerleri bilgisi ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcc01ade1-45d9-4bd6-897e-5d02320a0d56)(Excel aktar) butonu tıklanarak alınan Excel formatındaki rapora basılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2c644c38-90fe-4e47-9cc6-e3a1601d77aa)

### **1.1.1.8. Sorgu Tipli Parametrik Alan Tipi Tanımlama**

Rapor formatına eklenecek Sorgu tipli parametrik bir alan tanımlaması yapılır. lblK_QPARAM2 Sorgu tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload84d1f856-1f74-4079-82c1-1510d21f152d) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2f6331ce-7e19-4837-88fb-e7303609d627)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4bb7f2cd-40a3-4a28-addf-889e5bb5447b)

Bimser Destek ekibi tarafından destek alınarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload69814fe9-142c-4b0b-99b3-0bbac2bea125)(kaydet) butonu tıklanarak Sorgu tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload02249815-3d7f-4d36-9070-a8bc9d2714db)

Tanımlanan Sorgu tipli parametrik alan Aksiyon Planlama ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7258e64c-6bdb-47a2-8826-4c2ee905cceb)(Kalemler) butonu tıklanarak açılan Aksiyon Kalemi Tanımlama ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1882e68c-3493-484b-9f2d-3be7f7141edb)(Yeni) butonu tıklanarak açılan Aksiyon Kalemi Planlama-Yeni Kayıt ekranında görüntülenir. Tanımlanan Sorgu tipli parametrik alanın “lblK_QALAN2” lblK\_ kısa kod kısmı kaldırarak Aksiyon Kalemi Raporunun rapor formatına <QALAN2\> tag şeklinde bilgisi yazılır. Bir Aksiyon Kalemi Planlama işleminde bu Sorgu tipli alanın bilgisi girildiğinde Aksiyon Kaleminin Raporu alındığında Sorgu tipli alanın girilen bilgisi rapora basılacaktır.

### **1.1.1.9. Metin Tipli Parametrik Alan Tipleri Listesi**

Aksiyon Yönetimi Modülünde Aksiyon Planlama ekranında Kalemler butonu tıklanarak açılan Aksiyon Kalemi Tanımlama ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1882e68c-3493-484b-9f2d-3be7f7141edb)(Yeni) butonu tıklanarak açılan Aksiyon Kalemi Planlama-Yeni Kayıt ekranında Metin tipli bir alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Metin yazarak Metin tipli parametrik alanlar aratılır ve Metin tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Metin tipli parametrik alanların alan tanımlaması yapılır. Bu alan tanımlaması yapılan Metin tipli parametrik alanları lblK\_ kısa kodu kaldırarak:

<ALAN1\>,<ALAN2\>,<ALAN3\>,<ALAN6\>,<ALAN7\>,<ALAN8\> şeklinde Aksiyon Kalemi Raporu formatına tag şeklinde eklendiğinde Aksiyon Kalemi Planlama ekranında Metin tipli alanların girilen değerleri bilgisi ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcc01ade1-45d9-4bd6-897e-5d02320a0d56)(Excel aktar) butonu tıklanarak alınan Excel formatındaki rapora basılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaded497984-ab57-4809-8d81-9437b8d944b1)

### **1.1.1.10. Metin Tipli Parametrik Alan Tipi Tanımlama**

Rapor formatına eklenecek Metin tipli parametrik bir alan tanımlaması yapılır. lblK_ALAN2 Metin tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload84d1f856-1f74-4079-82c1-1510d21f152d) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc32fe531-1d49-4dba-8aeb-65fab1d7a488)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb9878e78-899f-4ef0-a385-7b2c0eaa1370)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload69814fe9-142c-4b0b-99b3-0bbac2bea125)(kaydet) butonu tıklanarak Metin tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload256c0c07-44a9-4715-9590-7e04b8c0061c)

Tanımlanan Metin tipli parametrik alan Aksiyon Planlama ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7258e64c-6bdb-47a2-8826-4c2ee905cceb)(Kalemler) butonu tıklanarak açılan Aksiyon Kalemi Tanımlama ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1882e68c-3493-484b-9f2d-3be7f7141edb)Yeni butonu tıklanarak açılan Aksiyon Kalemi Planlama-Yeni Kayıt ekranında görüntülenir. Tanımlanan Metin tipli parametrik alanın “lblK_ALAN2” lblK\_ kısa kod kısmı kaldırarak Aksiyon Kalemi Raporunun rapor formatına <ALAN2\> tag şeklinde bilgisi yazılır. Bir Aksiyon Kalemi Planlama işleminde bu Metin tipli alanın bilgisi girildiğinde Aksiyon Kaleminin Raporu alındığında Metin tipli alanın girilen bilgisi rapora basılacaktır.

### **1.1.1.11. Metin (Çoklu Satır) Tipli Parametrik Alan Tiplerin Listesi**

Aksiyon Yönetimi Modülünde Aksiyon Planlama ekranında Kalemler butonu tıklanarak açılan Aksiyon Kalemi Tanımlama ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1882e68c-3493-484b-9f2d-3be7f7141edb)(Yeni) butonu tıklanarak açılan Aksiyon Kalemi Planlama-Yeni Kayıt ekranında Metin (Çoklu Satır) tipli bir alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Metin (Çoklu Satır) yazarak Metin (Çoklu Satır) tipli parametrik alanlar aratılır ve Metin (Çoklu Satır) tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Metin (Çoklu Satır) tipli parametrik alanların alan tanımlaması yapılır. Bu alan tanımlaması yapılan Metin (Çoklu Satır) tipli parametrik alanları lblK\_ kısa kodu kaldırarak:

 <ALAN4\>, <ALAN5\>, <ALAN9\>, <ALAN10\> şeklinde Aksiyon Kalemi Raporu formatına tag şeklinde eklendiğinde Aksiyon Kalemi Planlama ekranında Metin (Çoklu Satır) tipli alanların girilen değerleri bilgisi ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcc01ade1-45d9-4bd6-897e-5d02320a0d56)(Excel aktar) butonu tıklanarak alınan Excel formatındaki rapora basılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload359f18c2-8216-41a1-829b-54dc4a9dee7c)

### **1.1.1.12.Metin (Çoklu Satır) Tipli Parametrik Alan Tipi Tanımlama**

Rapor formatına eklenecek Metin (Çoklu Satır) tipli parametrik bir alan tanımlaması yapılır. lblK_ALAN4 Metin (Çoklu Satır) tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload84d1f856-1f74-4079-82c1-1510d21f152d) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb3fce359-c9ff-4489-82f5-b056c9b8040b)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade112f348-6960-4634-a107-232f18fda6cf)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload69814fe9-142c-4b0b-99b3-0bbac2bea125)(kaydet) butonu tıklanarak Metin (Çoklu Satır) tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada19ab436-6c1a-4e3d-b256-fe2c0d3f5df7)

Tanımlanan Metin (Çoklu Satır) tipli parametrik alan Aksiyon Planlama ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7258e64c-6bdb-47a2-8826-4c2ee905cceb)(Kalemler) butonu tıklanarak açılan Aksiyon Kalemi Tanımlama ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1882e68c-3493-484b-9f2d-3be7f7141edb)(Yeni) butonu tıklanarak açılan Aksiyon Kalemi Planlama-Yeni Kayıt ekranında görüntülenir. Tanımlanan Metin (Çoklu Satır) tipli parametrik alanın “lblK_ALAN4” lblK\_ kısa kod kısmı kaldırarak Aksiyon Kalemi Raporunun rapor formatına <ALAN4\> tag şeklinde bilgisi yazılır. Bir Aksiyon Kalemi Planlama işleminde bu Metin (Çoklu Satır) tipli alanın bilgisi girildiğinde Aksiyon Kaleminin raporu alındığında Metin (Çoklu Satır) tipli alanın girilen bilgisi rapora basılacaktır.

### **1.1.1.13. Numerik Tipli Parametrik Alan Tiplerin Listesi**

Aksiyon Yönetimi Modülünde Aksiyon Planlama ekranında Kalemler butonu tıklanarak açılan Aksiyon Kalemi Tanımlama ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1882e68c-3493-484b-9f2d-3be7f7141edb)(Yeni) butonu tıklanarak açılan Aksiyon Kalemi Planlama-Yeni Kayıt ekranında Numerik tipli bir alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Numerik yazarak Numerik tipli parametrik alanlar aratılır ve Numerik tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Numerik tipli parametrik alanların alan tanımlaması yapılır. Bu alan tanımlaması yapılan Numerik tipli parametrik alanları lblK\_ kısa kodu kaldırarak:

<NALAN1\>, <NALAN2\>… <NALAN10\> şeklinde Aksiyon Kalemi Raporu formatına tag şeklinde eklendiğinde Aksiyon Kalemi Planlama ekranında Numerik tipli alanların girilen değerleri bilgisi ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcc01ade1-45d9-4bd6-897e-5d02320a0d56)(Excel aktar) butonu tıklanarak alınan Excel formatındaki rapora basılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload12217ab9-755d-4c0d-b62c-fedb17500366)

### **1.1.1.14.Numerik Tipli Parametrik Alan Tipi Tanımlama**

Rapor formatına eklenecek Numerik tipli parametrik bir alan tanımlaması yapılır. lblK_NALAN2 Numerik tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload84d1f856-1f74-4079-82c1-1510d21f152d) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6b86a852-bd02-4ed4-b1db-7e22be2c5368)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload438ec0a5-5bd8-4e5a-b80a-b3632066b2dc)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload69814fe9-142c-4b0b-99b3-0bbac2bea125)(Kaydet) butonu tıklanarak Numerik tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc8a69bf5-4b87-47ec-b193-e68cb42c77b5)

Tanımlanan Numerik tipli parametrik alan Aksiyon Planlama ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7258e64c-6bdb-47a2-8826-4c2ee905cceb)(Kalemler) butonu tıklanarak açılan Aksiyon Kalemi Tanımlama ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1882e68c-3493-484b-9f2d-3be7f7141edb)(Yeni) butonu tıklanarak açılan Aksiyon Kalemi Planlama-Yeni Kayıt ekranında görüntülenir. Tanımlanan Numerik tipli parametrik alanın “lblK_NALAN2” lblK\_ kısa kod kısmı kaldırarak Aksiyon Kalemi Raporunun rapor formatına <NALAN2\> tag şeklinde bilgisi yazılır. Bir Aksiyon Kalemi Planlama işleminde bu Numerik tipli alanın bilgisi girildiğinde Aksiyon Kaleminin Raporu alındığında Numerik tipli alanın girilen bilgisi rapora basılacaktır.

### **1.1.3.Aksiyon Kalemi Raporu Formatına (Kalemler Detayında) Eklenecek Alanların Değerlerin Girilmesi**

Aksiyon Kalemi Raporu formatına eklenecek alanların dğerlerin girilmesi için Aksiyon Yönetimi Modülünde bir yeni bir Aksiyon Planı tanımlanır. Tanımlanan bu aksiyon planına ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7258e64c-6bdb-47a2-8826-4c2ee905cceb)(Kalemler) butonu ile Aksiyon Kalemi Planlama işlemi yapılır. Sistemde tanımlı Aksiyon Planı ve Aksiyon Kalemi Planlarıda kullanılabilir. Sistemde tanımlı Aksiyon Kalemi Planları ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload52f52e24-f767-4890-8db1-ba2e48efa859)(Değiştir) butonu ile içeriği görüntülenerek tanımlanan parametrik alanların bilgisi de girilebilir.Aksiyon Yönetimi modülünde tanımlanan parametrik alanların bilgisi girildikten sonra rapor formatına eklenen alanların tagleri ile rapora bu alanların bilgisinin basılması sağlanılır. Raporda tanımlanan alan değerlerin bilgisinin gelmesi için Aksiyon Kalemi Planlama ekranında alan bilgilerin girilmesi gerekmektedir

Entegre Yönetim Sistemi\>Aksiyon Yönetimi\>Planlama menüsüne tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbada560a-d0af-453b-b6ac-c6e890b37d92)

Aksiyon Planı oluşturmak için ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload663ebdcb-3b39-45a4-b974-ad9029b63a5b)(Yeni) butonuna tıklanarak Aksiyon Planlama/ Yeni Kayıt ekranı görüntülenir. Aksiyon Bilgileri sekmesinde Ana Aksiyon Planı ile ilgili genel bilgilerin tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload543ebf3c-1e2b-4970-ba38-820e2a132c56)

Ek Dosyalar sekmesinde tanımlanan aksiyon planı için resim, toplantı notu, karar tutanağı gibi ek belgeler varsa eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcaf6d746-876d-4a1b-9bec-8d35f9e7ca8f)

Gerekli bilgiler girildikten sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload308c0bb3-cb0a-4f2b-bf47-936447aa0f2a) (Kaydet) butonu ile “Ana Aksiyon Planı” kaydedilir ve listede görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddbe742ba-8bf7-4220-8a8b-517dba19f840)

Ana Aksiyon Planı oluşturulduktan sonra bu plana bağlı aksiyon kalemleri oluşturularak, görev atamaları gerçekleştirilir. Aksiyon Planlama sayfasındaki ilgili ana aksiyon planı seçilerek, sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada88e5a26-5cce-4b8b-a159-6c1292481480)(Kalemler) butonuna tıklanarak Aksiyon Kalemi Planlama ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload95dfce67-f1f2-42e2-9a21-7591ac64da85)

Ana Aksiyon Planının içerisine yeni bir Aksiyon Kalemi eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload663ebdcb-3b39-45a4-b974-ad9029b63a5b)(Yeni) butonu tıklanarak Aksiyon Kalemi Planlama/ Yeni Kayıt ekranı görüntülenir. Aksiyon Bilgiler sekmesinde Aksiyon Kalemi ile ilgili genel bilgilerin girilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7aca023c-e030-435b-b099-9adc3b95a813) ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1e8f9dd6-73a9-4164-8318-3906dc79e7d5)

Dil ayarlarında tanımlanan parametrik alan tiplerinin bilgisi girilir. Bu parametrik alan tiplerinin görüntülenmesi için Aksiyon Yönetimi parametrelerinde 30 numaralı “Aksiyon kaynağı bazında parametrik alan kullanılacak mı?” parametresinin parametre değeri “Hayır” seçeğini seçilerek pasif edilmesi gerekir.

Aksiyon Kalemi ile ilgili varsa fotoğraf, çizim, toplantı notu, karar tutanağı gibi ek belgeler/ kanıtlar Ek dosyalar sekmesinde yüklenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5619a342-f895-4a46-9c11-b6ec3ce857de)

Açılan aksiyon gerçekleştirilmesi işi iş yapacak kişi tarafından başka bir kişiye yönlendirildiyse yönlendirme tarihçesi sekmesi altında tüm yönlendirme bilgileri görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6ab6d751-760e-4d5a-bc78-ac312662050a)

Aksiyon Kalemi oluşturma aşamasında gerekli sekmeler ve alanlar doldurulduktan sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2b60df8c-3b30-4273-af33-d056a354ab83) (Kaydet) butonu kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1c933f92-0a90-4276-b1ee-6bb79902590c)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb8d6dfd7-78c9-4b97-8f0a-44de845e280d)

### **1.1.4.Aksiyon Kalemler Raporu (Kalemler Detayında) Rapor Formatına Tanımlanan Parametrik Alanların Taglerin Eklenmesi**

Aksiyon Kalemler Raporu tanımlanan parametrik alanların taglerin eklenmesi için SAT\>BSAT\> Konfigürasyon Ayarları\>Rapor Formatları Düzenleme menüsüne gidilir. Qdms tüm raporların yüklendiği menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload29ce48ae-83f6-46f7-b0bb-0677283f9df9)

**Ekranda bulanan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload728df651-748a-4d53-baa8-b90c590a1124): Sisteme yeni bir rapor formatı yüklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload77621cb6-eff2-44c8-a225-b0e3b72be6b9): Listede seçili olan rapor formatı görüntülenip, indirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0960c87d-d2de-4c1f-b6b9-a9a3e8deed68): Listede seçili olan rapor formatı silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload410add2c-a15e-438b-8ea1-8ca82b04078f) (Görüntüle) butonu tıklanarak Aksiyon Kalemi Raporunun rapor format şablonu (AKSIYON_YATAY_RAP.xls) bilgisayara indirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc81a75e6-260e-49af-bfd8-7c65c0e55ba5)

Rapor formatına tanımlanan parametrik alanların alan tanımları ve tagleri ilgili bilgiler yazılırak rapor aynı isimde formatı bilgisayara kaydedilir. Örnekte Aksiyon Dosyası Detayı metin (çoklu satır) parametrik alanın tag <ALAN4\>, ve Aksiyon Kalemi dosya Türü liste tipli parametrik alanın tagi <LALAN2\> olacak şekilde rapor formatına yazılır. Diğer tanımlanan alan tiplerinin tagleri rapor formatınan eklenir.

Bilgisayara kaydedilen aynı isimdeki Rapor format (AKSIYON_YATAY_RAP.xls) ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd9e079f2-1fc0-4c5f-8a76-4dd711cb5d8f) (Yeni) butonu ile tekrar rapor formatları menüsüne sisteme yüklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf1454417-f5ba-401a-a49f-4d773f58c266)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7ddc0446-ea78-43e7-af88-d333335c2e1b)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc37348ca-dde1-4aa7-8ee7-a5e879c5d4ac)

Rapor formatları menüsünde aynı isimde rapor format yükleme işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd504831f-2dd4-4b8d-b077-95fbca0ace99)

### **1.1.5.Aksiyon Kalemi Raporunun Rapor Formatına Eklenen Parametrik Alanların Gösterimi**

Aksiyon Kalemi Raporunun rapor formatına (AKSIYON_YATAY_RAP.xls) tag ekleme işlemi yapılan rapor format yükleme işleminde sonra Entegre Yönetim Sistemi\>Aksiyon Yönetimi\>Raporlar\>Kalemler Detayında menüsü tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd4cca174-001b-4875-8b8d-a77d7cc97378)

Açılan Aksiyon Kalemi Raporu ekranında Aksiyon Kalemi Planlanan Aksiyon Kalemin bulunduğu Ana aksiyon no’su Ana Aksiyon No alanına bilgisi yazılırak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload18003004-4b25-4d23-b264-9a72c89bc7bf)(Ara) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade1535e36-7276-4152-9bb0-4035c08074bb)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade264b0f6-0b80-42ba-ab13-6df4e5a66ca1) (Excel’e Aktar) butonu ile “Aksiyon Kalemi Raporu” Excel formatında görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload78a1e2c2-b726-4bdb-9ba1-58e485ac97e7)

Excel aktar butonu ile alınan Excel formatındaki rapordaki taglerin çalıştığı ve tanımlanan parametrik alanların bilgisinin raporda geldiği görülür.

### **1.2.1. Aksiyon Kaynağı Bazında Parametrik Alan Tipi Tanımlama İşlemi İlgili Parametrenin Aktif Edilmesi**

Aksiyon Kaynağı Bazında Parametrik Alan Tipi Tanımlama İşlemi için Aksiyon parametrelerinden 30 nolu parametre kontrol edilerek “Aksiyon kaynağı bazında parametrik alan kullanılacak m” parametresi düzenlenir. Sistem Altyapı tanımları/Aksiyon/Aksiyon Parametreleri menüsü tıklanılır. Parametre no alanına parametrenin numarası yazılarak görütülenir. Açılan ekranda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload52f52e24-f767-4890-8db1-ba2e48efa859)(değiştir) butonu tıklanarak parametrenin içeriği görüntülenir. Aksiyon kaynağı bazında parametrik alan kullanılması isteniyorsa parametre değeri “Hayır” seçili iken parametre değeri evet seçilerek parametre aktif hale getirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5faab5b7-fdb5-4ada-8fdf-87adeef8cd61)Parametre değeri “Evet” olduğunda Ana Aksiyon Planlama ve Aksiyon Kalemi oluşturma ekranlarına kaynak bazında alanlar tanımlanmasını sağlar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb2efbd4-99e9-4a6f-ae2a-0fcce4507958)

Dil ayarlarından yapılan ortak parametre tanımlamaları devre dışı kalıp, görüntülenmez. Eğer parametre değeri “Hayır” olarak seçilirse dil ayarlarında tanımlanan ortak parametreler kullanılır.

Kaynak bazında parametrik alan tanımlamak için Sistem Altyapı Tanımları/ Aksiyon Yönetimi/ Aksiyon Kaynağı Tanımlama menüsü görüntülenir. Tanımlanan bir aksiyon kaynağı için sadece o kaynakta gözükecek ekstra alanlar tanımlanabilir. Örneğin; Tanımlanan “Toplantı” aksiyon kaynağı için bir alan tanımlanmak istenebilir. Bu seçim alanının, sadece Toplantı kaynağında kullanıcının karşısına çıkması, diğer aksiyon kaynaklarında gözükmemesi isteniyorsa aksiyon kaynağına bağlı parametrik alan tipi tanımlamak gerekir. Bunun için; ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd9d6907e-372c-4728-8ea6-2a6911e1a733) (Alan Tanımlama) butonuna tıklanarak parametrik alan tanımlama menüsü açılır. Aksiyon Planlama Modülünde Planlama veya Kalemler bazında parametrik alan tanımlanabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload556a0af0-7f27-4864-8ede-50d2f4a30cd7)

Açılan ekranda tanımlanan Toplantı kaynağı seçili iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload50773dd7-2067-4c44-98f8-e27069e3d631) (Alan Tanımlama) butonu tıklanarak Alan Tanımlama menüsü görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5eb0a0b5-4f5b-492b-b48f-ed3cb3b04d98)

Sırasıyla Metin, liste, sayı, tarih, personel ve sorgu bazında alan tanımlamalar yapılabilir.

### **1.2.1.1.Metin Tipli Parametrik Alan Tipi Tanımlama**

Aksiyon Kaynağı Toplantı olan Kalemler menüsünde metin tipli bir parametrik Alan tanımlamak için Alan tanımlama menüsünde Kalemler sekmesinde ALAN1 verisi tanımlanacak alanın adı yazılır. Başlık Notu bilgisi, zorunlu bir alan olması isteniyorsa zorunlu check box işaretlenir. Kalemler bazında metin tipli alan tanımlarken açılışta gösterilme durumu, gerçekleştirme/gecikmede gösterilme durumu, gerçekleştirme/ gecikmede değiştirilme durumu, görüntülemede gösterilme durumu, onaylamada değiştirilebilme durumu, açılış onayında gösterilme durumu, kapanış onayında gösterilme durumu, gridde gösterilme durumu ve sıra numarası belirlenip kaydedilir. Eğer “onaylamada değiştirilsin mi” kutucuğu işaretlenirse aksiyon kalemi açma/ kapatma onaylarında onaycılar tarafından değiştirilebilir. Alan Tanımlama menüsünde Kalemler sekmesinde gerekli alanlar doldurultuktan sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2b60df8c-3b30-4273-af33-d056a354ab83) (Kaydet) tıklanarak Metin tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbc28a437-485e-4751-80e1-ad1cf1f00426)

### **1.2.1.2.Liste Tipli Parametrik Alan Tipi Tanımlama**

Aksiyon Kaynağı Toplantı olan Kalemler menüsünde liste tipli bir parametrik Alan tanımlamak için Alan tanımlama menüsünde Kalemler sekmesinde LALAN1 verisi tanımlanacak alanın adı yazılır. Başlık Notu bilgisi, zorunlu bir alan olması isteniyorsa zorunlu check box işaretlenir. Kalemler bazında liste tipli alan tanımlarken açılışta gösterilme durumu, gerçekleştirme/gecikmede gösterilme durumu, gerçekleştirme/ gecikmede değiştirilme durumu, görüntülemede gösterilme durumu, onaylamada değiştirilebilme durumu, açılış onayında gösterilme durumu, kapanış onayında gösterilme durumu, gridde gösterilme durumu ve sıra numarası belirlenip kaydedilir. Eğer “onaylamada değiştirilsin mi” kutucuğu işaretlenirse aksiyon kalemi açma/ kapatma onaylarında onaycılar tarafından değiştirilebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc1bff450-54ba-482b-b271-eefafea2142c)

Liste tipli parametrik alanın liste elemanları ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1882e68c-3493-484b-9f2d-3be7f7141edb) (Yeni) butonu tıklanarak tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1cacc6be-f87c-4351-967d-dcfc24832dc0)

Liste elemanları tanımlama ekranında liste elemanın ID’si ve Değer bilgisi girilerek liste elemanları tanımlama işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada8638ca8-17a9-4837-b1df-2e9fb836eb94)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4480aeb3-3a85-4782-afc6-b799d4d51b0f)

Kalemler sekmesinde liste tipli alanın liste elemanları tanımlandıktan sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2b60df8c-3b30-4273-af33-d056a354ab83) (Kaydet) tıklanarak Liste tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

### **1.2.1.3.Nümerik Tipli Parametrik Alan Tipi Tanımlama**

Aksiyon Kaynağı Toplantı olan Aksiyon Kalemi Planlama menüsünde nümerik tipli bir parametrik Alan tanımlamak için Alan tanımlama menüsünde Kalemler sekmesinde NALAN1 verisi tanımlanacak alanın adı yazılır. Başlık Notu bilgisi, zorunlu bir alan olması isteniyorsa zorunlu check box işaretlenerek sıra nosu girilir. Alan Tanımlama menüsünde Kalemler sekmesinde gerekli alanlar doldurultuktan sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2b60df8c-3b30-4273-af33-d056a354ab83) (Kaydet) tıklanarak Nümerik tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8397cd26-6717-46b4-ad1e-edd990927908)

Diğer parametrik tipli alanların tanımlama işlemi bu şekilde yapılır.

### **1.2.4.Aksiyon Kalemi Raporu Formatına (Kalemler Detayında) Eklenecek Kaynak Bazlı Alanların Değerlerin Girilmesi**

Aksiyon Yönetimi Modülünde Kaynak Bazlı alanların değerlerinin girilmesi için öncelikle Entegre Yönetim Sistemi\>Aksiyon Yönetimi\>Planlama menüsünde tanımlanan kaynağa bağlı bir Ana Aksiyon Planı Tanımlanır.

Entegre Yönetim Sistemi\>Aksiyon Yönetimi\>Planlama menüsüne tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbada560a-d0af-453b-b6ac-c6e890b37d92)

Aksiyon Planı oluşturmak için ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload663ebdcb-3b39-45a4-b974-ad9029b63a5b)(Yeni) butonuna tıklanarak Aksiyon Planlama/ Yeni Kayıt ekranı görüntülenir. Aksiyon Bilgileri sekmesinde Ana Aksiyon Planı ile ilgili genel bilgilerin tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada9709447-b3a8-4f68-a9c6-47af861630e6)

Ek Dosyalar sekmesinde tanımlanan aksiyon planı için resim, toplantı notu, karar tutanağı gibi ek belgeler varsa eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload73551349-fc86-440e-8b17-661d8665d30c)

Gerekli bilgiler girildikten sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload308c0bb3-cb0a-4f2b-bf47-936447aa0f2a) (Kaydet) butonu ile “Ana Aksiyon Planı” kaydedilir ve listede görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2d2cc81d-3be0-4770-b8f7-502553459578)

Ana Aksiyon Planı oluşturulduktan sonra bu plana bağlı aksiyon kalemleri oluşturularak, görev atamaları gerçekleştirilir. Aksiyon Planlama sayfasındaki ilgili ana aksiyon planı seçilerek, sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada88e5a26-5cce-4b8b-a159-6c1292481480) (Kalemler) butonuna tıklanarak Aksiyon Kalemi Planlama ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadda31ba79-e5d8-4826-8b01-56cf47ff3fa0)

Ana Aksiyon Planının içerisine yeni bir Aksiyon Kalemi eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload663ebdcb-3b39-45a4-b974-ad9029b63a5b)(Yeni) butonu tıklanarak Aksiyon Kalemi Planlama/ Yeni Kayıt ekranı görüntülenir. Aksiyon Bilgiler sekmesinde Aksiyon Kalemi ile ilgili genel bilgilerin girilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload52885207-b9d2-4bf4-b9fa-9ec9b9158d6a)![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb4b26c9d-a5db-4e09-abf8-45e7c9953599)

Bu parametrik alan tipleri Aksiyon Yönetimi 30 numaralı “Aksiyon kaynağı bazında parametrik alan kullanılacak mı?” parametresinin parametre değeri “Evet” seçilerek parametrenin aktif edilmesi görüntülenir.

Aksiyon Kalemi ile ilgili varsa fotoğraf, çizim, toplantı notu, karar tutanağı gibi ek belgeler/ kanıtlar Ek dosyalar sekmesinde yüklenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddd82ef60-5609-42a4-9bba-2d697b3c3ddf)

Açılan aksiyon gerçekleştirilmesi işi iş yapacak kişi tarafından başka bir kişiye yönlendirildiyse yönlendirme tarihçesi sekmesi altında tüm yönlendirme bilgileri görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9356a4d5-dc04-455e-9f85-ca082d19906e)

Aksiyon Kalemi oluşturma aşamasında gerekli sekmeler ve alanlar doldurulduktan sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2b60df8c-3b30-4273-af33-d056a354ab83) (Kaydet) butonu kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9fb20580-d849-4ff6-a30e-67be94dda428)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0431ea95-680c-4c52-8f0c-0aae39f90d35)

Kaynak bazlı alan tanımlaması yapılan parametrik tipli alanların Aksiyon Kalemi Planlama ekranında bilgi girişleri yapılma işlemi tanımlanır.

### **1.2.5.Aksiyon Kalem Raporun Rapor Formatına Tanımlanan Kaynak Bazlı Parametrik Alanlar İçin Tag Eklenmesi**

Aksiyon Kalemi Roporuna tanımlanan kaynak bazlı parametrik alanların tag’in eklenmesi için SAT\>BSAT\> Konfigürasyon Ayarları\>Rapor Formatlarının Düzenlenmesi menüsüne gidilir. Qdms tüm raporların yüklendiği menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload29ce48ae-83f6-46f7-b0bb-0677283f9df9)

**Ekranda bulanan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload728df651-748a-4d53-baa8-b90c590a1124): Sisteme yeni bir rapor formatı yüklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload77621cb6-eff2-44c8-a225-b0e3b72be6b9): Listede seçili olan rapor formatı görüntülenip, indirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0960c87d-d2de-4c1f-b6b9-a9a3e8deed68): Listede seçili olan rapor formatı silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload410add2c-a15e-438b-8ea1-8ca82b04078f) (Görüntüle) butonu tıklanarak Aksiyon Kalemi Raporunun rapor format şablonu (AKSIYON_YATAY_RAP.xls) bilgisayara indirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfcf1e079-4bfd-4fe1-8a99-04a90bbf2496)

Kaynak bazlı tanımlanan parametrik alanların alan tanımları ve bu alanlara girilen bilgilerin gelmesi için bu raporun formatının en sonuna <AKS_KAYNAK_PARAM\> tagını yerleştirilir ve bilgisayara kaydedilir.

Bilgisayara kaydedilen aynı isimdeki Rapor format (AKSIYON_YATAY_RAP.xls) ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd9e079f2-1fc0-4c5f-8a76-4dd711cb5d8f) (Yeni) butonu ile tekrar rapor formatları menüsünde sisteme yüklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd053a6a4-7711-42b8-8851-f2dc30d34728)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5ea8ba1e-8eb4-436e-8a6f-c170e911b466)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3e2844ae-7921-4dd9-9d4c-516fe129781c)

Rapor formatları menüsünde aynı isimde rapor format yükleme işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload516be8d2-4a42-4ced-9fcc-e7af8d51bd8a)

### **1.2.6.Aksiyon Kalemi Raporuna Rapor Formatına Eklenen Tag ile Kaynak Bazlı  Parametrik Alanların Gösterimi**

Aksiyon Kalemi Raporunun rapor formatına (AKSIYON_YATAY_RAP.xls) tag ekleme işlemi yapılan rapor format yükleme işleminde sonra Entegre Yönetim Sistemi\>Aksiyon Yönetimi\>Raporlar\>Kalemler Detayında menüsü tıklanılır. "Aksiyon Arama" sekmesinde ilk olarak rapor çekmek istediğiniz aksiyon kaynağını seçilir ve en üstte bulunan "Kaynak bazında rapor al" alanını ile ilgili check box işaretlenerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload18003004-4b25-4d23-b264-9a72c89bc7bf)(Ara) butonu tıklanılır

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf13b3be1-8ec1-4119-8150-0c3b83081756)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3567c9b4-5e9e-4394-83c5-21b6f9dc7767)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade264b0f6-0b80-42ba-ab13-6df4e5a66ca1) (Excel’e Aktar) butonu ile “Aksiyon Kalemi Raporu” Excel formatında görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload26f3216e-76ba-4891-a5ad-4a522ac24ed9)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcc01ade1-45d9-4bd6-897e-5d02320a0d56) (Excel aktar) butonu ile alınan Excel formatındaki rapordaki bu işlemin ardından sistem seçtiğiniz kaynak üzerine tanımlı olan alanları otomatik olarak rapora basıldığı görülür. Özetle tek bir TAG kullanarak bütün kaynaklar için parametrik alan tiplerinin rapora alan tanımları ve alan bilgi girişlerinin gelmesi sağlanılır.

## **1.3.Aksiyon Yönetimi Modülünde Replacement (Kısa Kodlar) Tag Tablosu**

Aksiyon Yönetimi Modülünde kullanılan taglerin listesi aşağıdaki tabloda yer almaktadır.

| Kısaltma                               | Açıklaması                                                   |
|----------------------------------------|--------------------------------------------------------------|
| <ID\>                                 | Ana Aksiyon No                                               |
| <SID\>                                | Kalem No                                                     |
| \<DURUM_\>                             | Durum                                                        |
| <GECIKTI\>                            | Gecikti                                                      |
| <ISYERI\>                             | İş yeri                                                      |
| <ISYERIADI\>                          | İş yeri adı                                                  |
| <ISYERI_TANIM\>                       | İş yeri tanım                                                |
| <TALEPEDEN\>                          | Talep Eden                                                   |
| <SORUMLU_ADISOYADI\>                  | Sorumlu Kişi                                                 |
| <YAPACAK_ADISOYADI\>                  | İşi Yapacak                                                  |
| <T4_DEPARTMAN_ADI\>                   | Sorumlu Birim                                                |
| <AKS_KAYNAGI\>                        | Aksiyon Kaynağı                                              |
| <MS_TIPI_\>                           | Ana Aksiyon Tipi                                             |
| <T5_TIP\>                             | Aksiyon Detay Tipi                                           |
| <TANIM\>                              | Aksiyon Detayı                                               |
| <GECIKMENEDENI\>                      | Gecikme Nedeni                                               |
| <REVBITISTARIHI\>                     | Revizyon Bitiş Tarihi                                        |
| <GERCEKLESMETARIHI\>                  | Gerçekleşme Tarihi                                           |
| <SGTARIH\>                            | Sisteme Giriş Tarihi                                         |
| <YAPILANIS\>                          | Yapılan İş                                                   |
| <BUTCE\>                              | Bütçe                                                        |
| <FIILI_BUTCE\>                        | Fiili Bitçe                                                  |
| <BASLAMATARIHI\>                      | Başlama Tarihi                                               |
| <BITISTARIHI\>                        | Bitiş Tarihi                                                 |
| <KAPANMA_TARIHI\>                     | Kapanma Tarihi                                               |
| (<KAPANMA_TARIHI\>-<BITISTARIHI\>)  | Aksiyon Kapanma Süresi                                       |
| <HESAP_E_H\>                          | Tamamlama Yüzdesi Hesaplama                                  |
| <T_YUZDESI\>                          | Tamamlama Yüzdesi                                            |
| <E_YUZDESI\>                          | Etki Yüzdesi                                                 |
| <PERIYODIK\>                          | Periyodiklik Bilgisi                                         |
| <AK_TEK_PER\>                         | Tekrar periyodu                                              |
| <T6_ADISOYADI\>                       | Aksiyon Sisteme Giren                                        |
| <SGTARIH\>                            | Sisteme giriş tarihi                                         |
| <ILISKILI_AKSIYON\>                   | İlişkili Aksiyon                                             |
| <ILGILI_ISYERI\>                      | İlgili İşyeri                                                |
| <ILGI\>                               | Tetkik                                                       |
| <AKS_KAYNAK_PARAM\>                   | Kaynak Bazlı Parametrik Alan Tiplerini Rapor formatına basar |
| <MEASURE_CODE\>                       | Gösterge Kodları                                             |
| <MEASURE\>                            | Gösterge Kodu-Gösterge Adları                                |
| <ISYERI_TANIM\>                       | Aksiyon Kalemi üzerindeki iş yeri                            |

## **1.4.Aksiyon Yönetimi Modülünde Aksiyon Çizelge Raporunda Kullanılan Tagler (Kısa Kodlar)**

Aksiyon Yönetimi Modülünde Aksiyon Çizelge Raporu için kullanılan taglerin listesi aşağıdaki tabloda yer almaktadır.

| Kısaltma              | Açıklaması         |
|-----------------------|--------------------|
| <ANA_AKSIYON_TANIM\> | Ana Aksiyon Tanımı |
| <TANIM\>             | Aksiyon Kalemleri  |
| <BASLAMATARIHI\>     | Başlangıç Tarihi   |
| <BITISTARIHI\>       | Bitiş Tarihi       |
| <SURE\>              | Sure               |
| <DURUM_\>            | Durum              |
| <YAPACAK_ADISOYADI\> | Yapacak            |
| <SORUMLU_ADISOYADI\> | Sorumlu            |
| <TARIHLER\>          | Tarihler           |

## **1.5.Aksiyon Yönetimi Modülünde Aksiyon Yorum Raporunda Kullanılan Tagler (Kısa Kodlar)**

Aksiyon Yönetimi Modülünde Aksiyon Yorum Raporu için kullanılan taglerin listesi aşağıdaki tabloda yer almaktadır.

| Kısaltma                | Açıklaması           |
|-------------------------|----------------------|
| <ILGI\>                | Açıklama             |
| <AKS_KODU\>            | Aksiyon Kaynağı      |
| <TALEPEDEN\>           | Talep Eden           |
| <SGIREN\>              | Sisteme Giren        |
| <SGTARIH\>             | Sisteme Giriş Tarihi |
| <ISYERI\>              | İş Yeri              |
| <K_ID\>                | ID                   |
| <K_SID\>               | SID                  |
| <K_TANIM\>             | Tanım                |
| <K_YAPACAK\>           | Yapacak              |
| <K_SORUMLU\>           | Sorumlu              |
| <K_YAPILANIS\>         | Yapılan İş           |
| <K_BASLAMATARIHI\>     | Başlama Tarihi       |
| <K_BITISTARIHI\>       | Bitiş Tarihi         |
| <K_STATU\>             | Statü                |
| <K_GERCEKLESMETARIHI\> | Gerçekleşme Tarihi   |
| <K_YORUM\>             | Yorum                |
| <K_YORUMYAPAN\>        | Yorum Yapan          |
| <K_GECIKTI\>           | Gecikti Mi?          |
| <K_GECIKMENEDENI\>     | Gecikme Nedeni       |
| <K_REVBITISTARIHI\>    | Revizyon Bit. Tar.   |
