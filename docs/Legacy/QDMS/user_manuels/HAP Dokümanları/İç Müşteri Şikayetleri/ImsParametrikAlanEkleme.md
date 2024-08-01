---
title: Parametrik Alan Tanımlama İşlemi
description: Parametrik Alan Tanımlama İşlemi Yardım Dokümanı
sidebar_position: 1
---

:::tip Bilgi

İlgili konu başlığına sağ tarafta bulunan navigasyon yardımıyla hızlı bir şekilde ulaşabilirsiniz.

:::


**İç Müşteri Şikayetleri Modülünde Dil Ayarları Menüsünde Parametrik Alan Tanımlama Kullanıcı Yardım Dokümanı**


# **1.Sistem Altyapı Tanımları**

Personel bilgilerinin tanımlandığı ve diğer modüller için gerekli olan altyapının kurgulanmasının yapıldığı menüdür.

## **1.1.Konfigürasyon Ayarları**

**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları

QDMS sisteminde özel ayarların yapıldığı menülerdir. Bu menülerde yapılan ayarlar tüm QDMS kullanıcıları için geçerli olan ortak ayarlardır.

### **1.1.1. Dil Ayarları**

**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları

Dil ayarları menüsünden QDMS üzerinde görülen menülerin isimleri, alanların isimleri değiştirilebilir. Modüllere yeni alanlar eklenebilir. Var olan alanların zorunluluk durumları düzenlenebilir. Alanların ekran üzerinde göründükleri sıralama değiştirilebilir.

### **1.1.1.1.İç Müşteri Şikayetleri  Modülü Ortak Kullanım İçin Yeni Alan Oluşturma**

İç Müşteri Şikayetleri Modülünde Şikayet Detayı Diğer Alanlar, Gelişme Raporu, Kök Neden Analizi, Aksiyonlar, Sonuç Raporu ve Kapatma sekmelerinde firmanın istemiş olduğu sistemde olmayan ekstradan alanlar tanımlanabilir. Tanımlanan bu alanlar tüm İç Müşteri Şikayetleri Modül kaynakları için geçerlidir. Sistem Altyapı Tanımları/BSAT/ Konfigürasyon Ayarları/Dil Ayarları menüsü tıklanılır. Açılan Dil Ayarları sayfasında Modül alanında “İç Müşteri Şikayetleri” seçilir ve ekranda İç Müşteri Şikayetleri Modülü ile ilgili dil tanımları görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada70428ff-84f7-4392-81a2-11746afcd228)


İç Müşteri Şikayetleri Modülünde Entegre Yönetim Sistemi\> İç Müşteri Şikayetleri \>İç Müşteri Şikayetleri İşlemleri menüsünde Yeni butonu tıklatıldığında açılan Şikayet Detay ekranında Şikayet Detayı Diğer Alanlar parametrik tipli alan tanımlaması Dil Ayarların menüsünde yapılmaktadır. Ayrıca İç Müşteri Şikayetleri Modülünde Gelişme Raporu, Kök Neden Analizi, Aksiyonlar, Sonuç Raporu ve Kapatma aşamaların gerçekleştiği sekmelerde Dil Ayarları menüsünde parametrik tipli alan tanımlamasıda yapılmaktır. Bu aşamaların gerçekleştiği sekmelerde örneğin Gelişme Raporu ile ilgili parametrik tipli alan tanımlaması yapıldığında Gelişme Raporu sekmesinde, Kök Neden Analizi ile ilgili parametrik tipli alan tanımlaması yapıldığında Kök Neden Analizi sekmesinde tanımlanan parametrik alanlar görüntülenmektedir. Hangi sekmede parametrik tipli alan tanımlaması yapıldıysa ilgili sekmede parametrik tipli alanlar görüntülenmektedir. Bu aşamalarda parametrik tipli alanlarda kullanılan kısa kodlar bulunmaktadır. Hangi aşamada hangi kısa kodlar kullanılmış ayırt etmek mümkündür. Örneğin tanımlanan Metin Tipli parametrik tipli alanlarda hangi aşamada olduğunun ayırt etmek için aşağıdaki kısa kodların başlama kısımlarına dikkate etmek gerekir;

**Şikayet Detayı Diğer Alanlar:** lblPARAM1 kısa kodları genelde Şikayet Detayı Diğer Alanlar sekmesinde görüntülen parametrik alanları temsil eder.

**Gelişme Raporu:** lblG_Param1, lblG ile başlayan kısa kodları genelde Gelişme Raporu aşamasında görüntülenen parametrik tipli alanları temsil eder.

**Kök Neden Analizi:** lblKOKPARAM1, lblKOK ile başlayan kısa kodları genelde Kök Neden Analizi aşamasında görüntülenen parametrik tipli alanları temsil eder

**Aksiyonlar:** lblA_Param1, lblA kısa kodları ile başlayan genelde Aksiyonlar aşamasında görüntülenen parametrik tipli alanları temsil eder.

**Sonuç Raporu:** lblS_Param1, lblS kısa kodları ile başlayan genelde Sonuç Raporu aşamasında görüntülenen parametrik tipli alanları temsil eder.

**Kapatma:** lblK_Param1, lblK kısa kodları ile başlayan genelde Kapatma aşamasında görüntülenen parametrik tipli alanları temsil eder.

**İç Müşteri Şikayetleri Modülünde Tanımlanan Parametrik Tipli Alanlar ve Tanımları;**

**1-Tarih tipli**: Takvim alanı eklenilen parametrik alandır. Örnek Kısa Kod: lblDPARAM1 (Şikayet Detayı Diğer Alanlar sekmesinde parametrik alan tipi görüntülenir.)

**2-Liste tipli**: Birden fazla liste elemanları arasından tek seçim yapılan parametrik alandır. Liste elemanları tanımlanarak, tanımlanan liste elemanlarında seçip yapılır. Örnek Kısa Kod: lblG_LParam2 (Gelişme Raporu sekmesinde parametrik alan tipi görüntülenir.)

**3-Personel Tipli:** QDMS personel veri tabanından kişi seçilebilmesini sağlayan parametrik alandır. Sistem Altyapı Tanımları\>Bsat\>Tanımlama\>Personel Tanımlama menüsünde tanımlı olan Personellerin listesinde seçim yapılır. Örnek Kısa Kod: lblG_PParam2 (Gelişme Raporu sekmesinde parametrik alan tipi görüntülenir.)

**4-Sorgu tipli:** QDMS/Ensemble veri tabanları içerisindeki ana verilerden seçim yapılabilmesi için tanımlanabilen alan türüdür. (Sadece Bimser Destek Ekibi tarafından tanımlanmalıdır) Tekli ve çoklu seçim yapılabilir. Örnek Kısa Kod: lblQPARAM1 (Şikayet Detayı Diğer Alanlar sekmesinde parametrik alan tipi görüntülenir.)

**5-Metin tipli**: Elle yazım imkanı veren metin kutucuğu ekleyen parametrik alandır. Örnek Kısa Kod: lblKOKPARAM1(Kök Neden Analizi sekmesinde parametrik alan tipi görüntülenir.)

**6-Metin (Çoklu Satır) Tipli**: Elle yazım imkanı veren karakter sınırı olmayan çok satırlı metin kutucuğu eklenen parametrik alandır. Örnek Kısa Kod: lblPARAM16 (Şikayet Detayı Diğer Alanlar sekmesinde parametrik alan tipi görüntülenir.)

**7- Başlık Tipli:** Formlara koyu harflerle yazılacak başlık alanı ekleyen parametrik alandır. Örnek Kısa Kod: lblBaslikParam1(Şikayet Detayı Diğer Alanlar sekmesinde parametrik alan tipi görüntülenir.)

**8-Ürün Tipli:** QDMS ürün veri tabanından ürün bilgisinin seçilebilmesini sağlayan parametrik alandır. Sistem Altyapı Tanımları\>BSAT\>Tanımlar\>Ürün Tanımlama menüsünde tanımlı Ürün listesinden Ürün bilgisinin seçimi yapılır. Örnek Kısa Kod: lblUPARAM1 (Şikayet Detayı Diğer Alanlar sekmesinde parametrik alan tipi görüntülenir.)

**9**-**Parasal Tipli:** Parasal olarak veri girişi yaptıran parametrik alandır. Tanımlanan parametrik alanın yanında para birimleri seçildiği alan çıkar. Para birimleri seçim alanındaki para birimleri Sistem Altyapı Tanımları\>BSAT\>Tanımlar\>Para Birimleri Tanımlama menüsünde tanımlı olan para birimleridir. Örnek Kısa Kod: lblA_NParam1 (Aksiyonlar sekmesinde parametrik alan tipi görüntülenir)

**10- Ölçü Birimi Tipli:** Ölçü olarak veri girişi yaptıran parametrik alandır. Tanımlanan parametrik alanın yanında Ölçü birimleri seçildiği alan çıkar. Ölçü birimleri seçim alanındaki ölçü Birimleri Sistem Altyapı Tanımları\>BSAT\>Tanımlar\>Ölçü Birimleri Tanımlama menüsünde tanımlı olan ölçü birimleridir. Örnek Kısa Kod: lblS_NParam3 (Sonuç Raporu sekmesinde parametrik alan tipi görüntülenir.)

**11-Müşteri Tipli:** Qdms Müşteri veri tabanından Müşteri seçilebilmesini tekli ve çoklu seçim yapılmasını sağlayan parametrik alandır. Örnek Kısa Kod: lblMPARAM1 (Şikayet Detayı Diğer Alanlar sekmesinde parametrik alan tipi görüntülenir.)

#### **1.1.1.1.1. İç Müşteri Şikayetleri Modülünde Şikayet Detayı Diğer Alanlar Sekmesinde Parametrik Alan Tanımlaması**

İç Müşteri Şikayetleri Modülünde Şikayet Detayı Diğer Alanlar sekmesinde tanımlanan parametrik alanların kısa kodları lblPARAM başlığı ile tanımlı kısa kodlardır. lblPARAM başlığındaki kısa kodlar olan tüm parametrik tipli alanlar tanımlandığında İç Müşteri Şikayetleri Modülünde Şikayet Detayı Diğer Alanlar sekmesi ekranında görüntülenir.

##### **1.1.1.1.1.1.Tarih Tipli Parametrik Alanların Listesi**

İç Müşteri Şikayetleri Modülünde Entegre Yönetim Sistemi\> İç Müşteri Şikayetleri \> İç Müşteri Şikayetleri İşlemleri menüsünde Yeni butonu tıklatıldığında açılan Şikayet Detayı ekranında Şikayet Detayı Diğer Alanlar sekmesinde Tarih tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Tarih yazarak Tarih tipli parametrik alanlar aratılır ve Tarih tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen tarih tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5263f224-0c6c-462b-a7b7-b93508f280f5)

##### **1.1.1.1.1.2.Tarih Tipli Parametrik Alan Tanımlama.**

lblDPARAM1 Tarih tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc58c94f-dff5-4b5d-96ae-346a21b6539b) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd3450117-4147-451e-9a4b-546313434779)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc1e27dda-d692-4f8c-b8b5-c51966dd89b2)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4cc2ef13-5ccf-4b1b-9cab-fecd054c5f49)(Kaydet) butonu tıklanarak tarih tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6b169583-38ac-4ea5-97d3-e10a3d95251b)

Tanımlanan Tarih tipli parametik alan Entegre Yönetim Sistemi\> İç Müşteri Şikayetleri \> İç Müşteri Şikayetleri İşlemleri menüsünde Yeni butonu tıklatıldığında açılan Şikayet Detayı ekranında Şikayet Detayı Diğer Alanlar sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2246a229-9710-4abf-882c-05df51d7b736)

##### **1.1.1.1.1.3.Liste Tipli Parametrik Alanların Listesi**

İç Müşteri Şikayetleri Modülünde Entegre Yönetim Sistemi\> İç Müşteri Şikayetleri \> İç Müşteri Şikayetleri İşlemleri menüsünde Yeni butonu tıklatıldığında açılan Şikayet Detayı ekranında Şikayet Detayı Diğer Alanlar sekmesinde Liste tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Liste yazarak Liste tipli parametrik alanlar aratılır ve Liste tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Liste tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadeb53fd12-b0a6-434a-bbc4-033a65ef2f23)

##### **1.1.1.1.1.4.Liste Tipli Parametrik Alan Tanımlama.**

lblLPARAM5 Liste tipli parametrik seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc58c94f-dff5-4b5d-96ae-346a21b6539b) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4a17ebe5-262d-4879-b4a2-5e7b660e0f92)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaded99428b-1907-446a-830f-fc12c6fb138d)

Liste tipli alanın liste değerlerini girmek için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade75a24a8-38e7-435e-ae69-25434a4527d1) (Yeni) butonuna tıklanır, liste değerleri yazılır ve kaydedilir. Liste eleman değeri 1 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload657051dc-6b22-4177-a239-60adda5b2368)

Liste eleman değeri 2 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload32445847-60dd-429c-8c62-4cd9296ffd69)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9bfe261c-9241-4eb6-b548-e858a9517ead)

Alanın zorunlu olup, olmayacağı sıra no bilgisi, liste elemanları tanımlanarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4cc2ef13-5ccf-4b1b-9cab-fecd054c5f49)(kaydet) butonu tıklanarak liste tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb13e9fc7-4019-44ff-a4e5-d8fa596723dc)

Tanımlanan Liste Tipli parametik alan Entegre Yönetim Sistemi\> İç Müşteri Şikayetleri \> İç Müşteri Şikayetleri İşlemleri menüsünde Yeni butonu tıklatıldığında açılan Şikayet Detayı ekranında Şikayet Detayı Diğer Alanlar sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload777047c6-fe8c-4f36-a444-af7a707da06c)

##### **1.1.1.1.1.5.Personel Tipli Parametrik Alanların Listesi**

İç Müşteri Şikayetleri Modülünde Entegre Yönetim Sistemi\> İç Müşteri Şikayetleri \> İç Müşteri Şikayetleri İşlemleri menüsünde Yeni butonu tıklatıldığında açılan Şikayet Detayı ekranında Şikayet Detayı Diğer Alanlar sekmesinde Personel tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Personel yazarak Personel tipli parametrik alanlar aratılır ve Personel tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Personel tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload82bd5ff6-6770-450d-99ec-6a51ac99e38a)

##### **1.1.1.1.1.6.Personel Tipli Parametrik Alan Tanımlama**

lblPPARAM1 Personel tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc58c94f-dff5-4b5d-96ae-346a21b6539b) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf5ddcb22-49ef-4fb5-ae40-a29988690baf)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload76d10378-fef7-4339-bd1b-1d4c7a01523c)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4cc2ef13-5ccf-4b1b-9cab-fecd054c5f49)(kaydet) butonu tıklanarak Personel tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload934e4311-0c9c-4c16-82bc-42c51b42127f)

Tanımlanan Personel Tipli parametik alan Entegre Yönetim Sistemi\> İç Müşteri Şikayetleri \> İç Müşteri Şikayetleri İşlemleri menüsünde Yeni butonu tıklatıldığında açılan Şikayet Detayı ekranında Şikayet Detayı Diğer Alanlar sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbf5050ed-59ea-4c0c-af33-3c7f2b9604fc)

Personel tipli parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload25faf77d-8dee-4776-919a-11fee2b1f76a)(seç) butonu tıklanıldığında sistemde tanımlı personel listesinde seçim yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload05c8c364-b515-48af-b96b-bc77927f4254)

##### **1.1.1.1.1.7.Sorgu Tipli Parametrik Alanların Listesi**

İç Müşteri Şikayetleri Modülünde Entegre Yönetim Sistemi\> İç Müşteri Şikayetleri \> İç Müşteri Şikayetleri İşlemleri menüsünde Yeni butonu tıklatıldığında açılan Şikayet Detayı ekranında Şikayet Detayı Diğer Alanlar sekmesinde Sorgu tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Sorgu yazarak Sorgu tipli parametrik alanlar aratılır ve Sorgu tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Sorgu tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaa70185c-d61c-4b83-8cb4-8a6a576459c5)

##### **1.1.1.1.1.8.Sorgu Tipli Parametrik Alan Tanımlama**

lblQPARAM1 Sorgu tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc58c94f-dff5-4b5d-96ae-346a21b6539b) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload28b57d6a-0f12-464d-bbe0-ec7991835ac4)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4a547f09-d27d-47b5-901b-124341971e9a) Bimser Destek ekibinde yardım alınarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4cc2ef13-5ccf-4b1b-9cab-fecd054c5f49)(kaydet) butonu tıklanarak Sorgu tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd178b0e7-bc61-43d4-9bbf-1848fa2ca7e5)

Tanımlanan Sorgu Tipli parametrik alan Entegre Yönetim Sistemi\> İç Müşteri Şikayetleri \> İç Müşteri Şikayetleri İşlemleri menüsünde Yeni butonu tıklatıldığında açılan Şikayet Detayı ekranında Şikayet Detayı Diğer Alanlar sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7d8aba96-9ce9-4c6e-96d9-6e04f209fe33)

Sorgu tipli parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload25faf77d-8dee-4776-919a-11fee2b1f76a)(seç) butonu tıklanıldığında sistemde tanımlı Departman listesinde seçim yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada1dd77a2-af3b-483d-9333-599e95db3794)

##### **1.1.1.1.1.9.Metin Tipli Parametrik Alanların Listesi**

İç Müşteri Şikayetleri Modülünde Entegre Yönetim Sistemi\> İç Müşteri Şikayetleri \> İç Müşteri Şikayetleri İşlemleri menüsünde Yeni butonu tıklatıldığında açılan Şikayet Detayı ekranında Şikayet Detayı Diğer Alanlar sekmesinde Metin tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Metin yazarak Metin tipli parametrik alanlar aratılır ve Metin tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Metin tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadffc366ec-f21b-44d7-9675-0a00fd05efd8)

##### **1.1.1.1.1.10.Metin Tipli Parametrik Alan Tanımlama**

lblPARAM5 Metin tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc58c94f-dff5-4b5d-96ae-346a21b6539b) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc6fefa8d-3754-446f-9db6-9d39d019ce57)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload75c730f5-d10d-4f7c-a457-9c90661fb77c)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4cc2ef13-5ccf-4b1b-9cab-fecd054c5f49)(kaydet) butonu tıklanarak Metin tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd085dd7d-e7f2-483f-a041-ea1f933b8607)

Tanımlanan Metin Tipli parametrik alan Entegre Yönetim Sistemi\> İç Müşteri Şikayetleri \> İç Müşteri Şikayetleri İşlemleri menüsünde Yeni butonu tıklatıldığında açılan Şikayet Detayı ekranında Şikayet Detayı Diğer Alanlar sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload079a7c51-01da-49c0-b472-8684eb5f8f89)

##### **1.1.1.1.1.11.Metin (Çoklu Satır) Tipli Parametrik Alanların Listesi**

İç Müşteri Şikayetleri Modülünde Entegre Yönetim Sistemi\> İç Müşteri Şikayetleri \> İç Müşteri Şikayetleri İşlemleri menüsünde Yeni butonu tıklatıldığında açılan Şikayet Detayı ekranında Şikayet Detayı Diğer Alanlar sekmesinde Metin (Çoklu Satır)  tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Metin (Çoklu Satır) yazarak Metin (Çoklu Satır) tipli parametrik alanlar aratılır ve Metin (Çoklu Satır)  tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Metin (Çoklu Satır)  tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8b6dbdf4-1615-4b34-b6aa-09986b7cc1f4)

##### **1.1.1.1.1.12.Metin (Çoklu Satır) Tipli Parametrik Alan Tanımlama**

lblPARAM16 Metin (Çoklu Satır) tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc58c94f-dff5-4b5d-96ae-346a21b6539b) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0fdafcba-9c10-4f3c-ab34-4415a1fbba19)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb10743d7-acea-4dc4-93ae-d3034c0b8118)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4cc2ef13-5ccf-4b1b-9cab-fecd054c5f49)(kaydet) butonu tıklanarak Metin (Çoklu Satır) tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9c0b7d46-7e52-481d-93e9-32e66de8c8b0)

Tanımlanan Metin (Çoklu Satır) Tipli parametrik alan Entegre Yönetim Sistemi\> İç Müşteri Şikayetleri \> İç Müşteri Şikayetleri İşlemleri menüsünde Yeni butonu tıklatıldığında açılan Şikayet Detayı ekranında Şikayet Detayı Diğer Alanlar sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0345a2dd-e0b4-40f2-b43f-1b6a343ac461)

##### **1.1.1.1.1.13.Ölçü Birimi Parametrik Alanların Listesi**

İç Müşteri Şikayetleri Modülünde Entegre Yönetim Sistemi\> İç Müşteri Şikayetleri \> İç Müşteri Şikayetleri İşlemleri menüsünde Yeni butonu tıklatıldığında açılan Şikayet Detayı ekranında Şikayet Detayı Diğer Alanlar sekmesinde Ölçü Birimi tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Ölçü Birimi yazarak Ölçü Birimi tipli parametrik alanlar aratılır ve Ölçü Birimi tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Ölçü Birimi tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbcc0eeb6-a666-437e-be64-46b5624aa1c2)

##### **1.1.1.1.1.14.Ölçü Birimi Parametrik Alan Tanımlama**

lblNPARAM6 Ölçü birimi tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc58c94f-dff5-4b5d-96ae-346a21b6539b) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload536ae8b7-e769-4376-b593-757438729c34)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9eca591e-519c-4c75-a8cd-6e7b03e2b255)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4cc2ef13-5ccf-4b1b-9cab-fecd054c5f49)(Kaydet) butonu tıklanarak ölçü birimi tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload540e8835-2f03-4ae3-89b9-205f48fc7ecd)

Tanımlanan ölçü birimi tipli parametrik alan Entegre Yönetim Sistemi\> İç Müşteri Şikayetleri \> İç Müşteri Şikayetleri İşlemleri menüsünde Yeni butonu tıklatıldığında açılan Şikayet Detayı ekranında Şikayet Detayı Diğer Alanlar sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload40f65e8e-1b7f-4573-a7b5-a0520177a057)

##### **1.1.1.1.1.15.Parasal Tipli Parametrik Alanların Listesi**

İç Müşteri Şikayetleri Modülünde Entegre Yönetim Sistemi\> İç Müşteri Şikayetleri \> İç Müşteri Şikayetleri İşlemleri menüsünde Yeni butonu tıklatıldığında açılan Şikayet Detayı ekranında Şikayet Detayı Diğer Alanlar sekmesinde Parasal tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Parasal yazarak Parasal tipli parametrik alanlar aratılır ve Parasal tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Parasal tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload80788596-4885-4168-bdb3-072247d00276)

##### **1.1.1.1.1.16.Parasal Tipli Parametrik Alan Tanımlama**

lblNPARAM21 Parasal tipli alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc58c94f-dff5-4b5d-96ae-346a21b6539b) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8be59931-a805-4a6d-9041-8c7c93fe1695)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9a255522-9f25-4d60-905c-9eb46b5ef642)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4cc2ef13-5ccf-4b1b-9cab-fecd054c5f49)(Kaydet ) butonu tıklanarak Parasal tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc818c8af-d0e7-46a4-b75e-6fe35759d281)

Tanımlanan Parasal Tipli parametrik alan Entegre Yönetim Sistemi\> İç Müşteri Şikayetleri \> İç Müşteri Şikayetleri İşlemleri menüsünde Yeni butonu tıklatıldığında açılan Şikayet Detayı ekranında Şikayet Detayı Diğer Alanlar sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1b925f72-24f9-4379-8780-84e57386eb77)

##### **1.1.1.1.1.17.Başlık Tipli Parametrik Alanların Listesi**

İç Müşteri Şikayetleri Modülünde Entegre Yönetim Sistemi\> İç Müşteri Şikayetleri \> İç Müşteri Şikayetleri İşlemleri menüsünde Yeni butonu tıklatıldığında açılan Şikayet Detayı ekranında Şikayet Detayı Diğer Alanlar sekmesinde Başlık tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Başlık yazarak Başlık tipli parametrik alanlar aratılır ve Başlık tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Başlık tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc8bdd271-b9d1-4b65-9ef2-9bac73851813)

##### **1.1.1.1.1.18.Başlık Tipli Parametrik Alan Tanımlama**

lblBaslikParam1 Başlık tipli alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc58c94f-dff5-4b5d-96ae-346a21b6539b) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3c8d7619-0555-4994-b032-94d2103d1077)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload332e5309-bdf5-4344-abf5-5d93a929e759)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4cc2ef13-5ccf-4b1b-9cab-fecd054c5f49)(Kaydet ) butonu tıklanarak Başlık tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload08e1dcc2-d620-4d3e-b5c1-e5bf4515d730)

Tanımlanan Başlık Tipli parametrik alan Entegre Yönetim Sistemi\> İç Müşteri Şikayetleri \> İç Müşteri Şikayetleri İşlemleri menüsünde Yeni butonu tıklatıldığında açılan Şikayet Detayı ekranında Şikayet Detayı Diğer Alanlar sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb8a86da0-e705-42cb-af5d-c8655f52647e)

##### **1.1.1.1.1.19.ÜrünTipli Parametrik Alanların Listesi**

İç Müşteri Şikayetleri Modülünde Entegre Yönetim Sistemi\> İç Müşteri Şikayetleri \> İç Müşteri Şikayetleri İşlemleri menüsünde Yeni butonu tıklatıldığında açılan Şikayet Detayı ekranında Şikayet Detayı Diğer Alanlar sekmesinde Ürün tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Ürün yazarak Ürün tipli parametrik alanlar aratılır ve Ürün tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Ürün tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload89c276cb-edf4-4bcb-a916-ec18c75bac80)

##### **1.1.1.1.1.20.Ürün Tipli Parametrik Alan Tanımlama**

lblUPARAM1 Ürün tipli alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc58c94f-dff5-4b5d-96ae-346a21b6539b) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade60da6c2-79d3-40b5-ac6e-cec47e0d789f)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload60650a63-4e49-4d16-a8ce-98a5308c4189)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4cc2ef13-5ccf-4b1b-9cab-fecd054c5f49)(Kaydet ) butonu tıklanarak Ürün tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaab46099-32cd-4a5c-9f9d-a9b8e216414c)

Tanımlanan Ürün Tipli parametrik alan Entegre Yönetim Sistemi\> İç Müşteri Şikayetleri \> İç Müşteri Şikayetleri İşlemleri menüsünde Yeni butonu tıklatıldığında açılan Şikayet Detayı ekranında Şikayet Detayı Diğer Alanlar sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6d82e5ab-766d-4941-9d0d-c2e5953b08bb)

Ürün tipli parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4d845a43-52bd-4e04-b33c-24d8ebc5a04d)(Ekle) butonu tıklanıldığında sistemde tanımlı Ürün listesinde Ürün ekleme işlemi yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadec4ba6a4-41a0-4f89-b766-7040fb3a22d2)

##### **1.1.1.1.1.21.Müşteri Tipli Parametrik Alanların Listesi**

İç Müşteri Şikayetleri Modülünde Entegre Yönetim Sistemi\> İç Müşteri Şikayetleri \> İç Müşteri Şikayetleri İşlemleri menüsünde Yeni butonu tıklatıldığında açılan Şikayet Detayı ekranında Şikayet Detayı Diğer Alanlar sekmesinde Müşteri tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Müşteri yazarak Müşteri tipli parametrik alanlar aratılır ve Müşteri tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Müşteri tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2005316a-6292-412e-a7b0-f5d50a9313ce)

##### **1.1.1.1.1.22.Müşteri Tipli Parametrik Alan Tanımlama.**

lblMPARAM1 Müşteri tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc58c94f-dff5-4b5d-96ae-346a21b6539b) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload90d88c04-b6c2-4bf4-955a-3b980f18c679)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9c3370b0-fd6e-4ab3-a387-7958ccb0ec07)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4cc2ef13-5ccf-4b1b-9cab-fecd054c5f49)(kaydet) butonu tıklanarak Müşteri parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3cf23b5f-70b6-437e-9cb9-e05a6d83a12c)

Tanımlanan Müşteri tipli parametrik alan Entegre Yönetim Sistemi\> İç Müşteri Şikayetleri \> İç Müşteri Şikayetleri İşlemleri menüsünde Yeni butonu tıklatıldığında açılan Şikayet Detayı ekranında Şikayet Detayı Diğer Alanlar sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7886323e-ee95-4608-b3d5-6f8630d96d2d)

Müşteri tipli parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4d845a43-52bd-4e04-b33c-24d8ebc5a04d)(Ekle) butonu tıklanıldığında sistemde tanımlı Müşteri listesinde Müşteri ekleme işlemi yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload83622003-2618-4d54-a9fb-d5d71df962a5)

Entegre Yönetim Sistemi\> İç Müşteri Şikayetleri \> İç Müşteri Şikayetleri İşlemleri menüsünde Yeni butonu tıklatıldığında açılan Şikayet Detayı ekranında Şikayet Detayı Diğer Alanlar sekmesinde tanımlanan parametrik tipli tüm alanlar;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf2b87b0f-cb35-44d0-b436-b69cf8ad8915)

#### **1.1.1.1.2.İç Müşteri Şikayetleri Modülünde Gelişme Raporu Sekmesinde Parametrik Alan Tipi Tanımlaması**

İç Müşteri Şikayetleri Modülünde Gelişme Raporu sekmesinde tanımlanan parametrik alanların kısa kodları lblG\_ başlığı ile tanımlı kısa kodlardır. lblG\_ başlığındaki kısa kodlar olan tüm parametrik tipli alanlar tanımlandığında İç Müşteri Şikayetleri Modülünde Gelişme Raporu sekmesi ekranında görüntülenir.

##### **1.1.1.1.2.1.Liste Tipli Parametrik Alanların Listesi**

İç Müşteri Şikayetleri Modülünde Şikayet Detayı ekranında Gelişme Raporu sekmesinde Liste tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Liste yazarak Liste tipli parametrik alanlar aratılır ve Liste tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Liste tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd01321d7-3457-43f3-a6b0-544a0f4a0e3b)

##### **1.1.1.1.2.2.Liste Tipli Parametrik Alan Tanımlama.**

lblG_LParam2 Liste tipli parametrik seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc58c94f-dff5-4b5d-96ae-346a21b6539b) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3f0c9b84-a184-41bc-8154-00830a73df44)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload60a76ce2-5b23-4bb5-8ea3-2c69696f4fbd)

Liste tipli alanın liste değerlerini girmek için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade75a24a8-38e7-435e-ae69-25434a4527d1) (Yeni) butonuna tıklanır, liste değerleri yazılır ve kaydedilir. Liste eleman değeri 1 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade580500d-d151-436c-9f2c-3fecf183d124)

Liste eleman değeri 2 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6521c5c2-547f-451b-bb42-f3aef54345b6)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfbd34354-e593-4acb-b703-62e13188bd47)

Alanın zorunlu olup, olmayacağı sıra no bilgisi ve liste elemanları tanımlanarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4cc2ef13-5ccf-4b1b-9cab-fecd054c5f49)(kaydet) butonu tıklanarak liste tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5ff2c3b8-b6f4-43b9-ba27-75ea734848d4)

Tanımlanan liste tipli parametrik alan İç Müşteri Şikayetleri Modülünde Şikayet Detayı ekranında Gelişme Raporu sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7faa591c-0692-4f78-a0e0-f454a2105458)

##### **1.1.1.1.2.3.Personel Tipli Parametrik Alanların Listesi**

İç Müşteri Şikayetleri Modülünde Şikayet Detayı ekranında Gelişme Raporu sekmesinde Personel tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Personel yazarak Personel tipli parametrik alanlar aratılır ve Personel tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Personel tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8c4e04d1-8a9b-4504-b388-6ae709722766)

##### **1.1.1.1.2.4.Personel Tipli Parametrik Alan Tanımlama.**

lblG_PParam1 Personel tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc58c94f-dff5-4b5d-96ae-346a21b6539b) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd92d6eaa-a03f-4393-b7a6-a7e6289ebd72)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada945c07c-4685-4d91-b999-5b3dcfaf9458)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4cc2ef13-5ccf-4b1b-9cab-fecd054c5f49)(kaydet) butonu tıklanarak Personel tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload684c86cb-bc00-4bf8-8a63-8cdf7d583482)

Tanımlanan Personel tipli parametrik Alan İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Gelişme Raporu sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9cbaf75b-868b-47ea-a143-8994c90aedef)

Personel tipli parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload25faf77d-8dee-4776-919a-11fee2b1f76a)(seç) butonu tıklanıldığında sistemde tanımlı personel listesinde seçim yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload690cbd11-6319-4dbf-8199-bbc6b502b46d)

##### **1.1.1.1.2.5.Sorgu Tipli Parametrik Alanların Listesi**

İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Gelişme Raporu sekmesinde Sorgu tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Sorgu yazarak Sorgu tipli parametrik alanlar aratılır ve Sorgu tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Sorgu tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload34449fd0-6cb1-4973-b6c5-b7d8f5c3db52)

##### **1.1.1.1.2.6.Sorgu Tipli Parametrik Alan Tanımlama**

lblG_QParam1 Sorgu tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc58c94f-dff5-4b5d-96ae-346a21b6539b) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload758ff52e-546c-4701-8ef1-6c0af31a3cff)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload785a7950-0535-40f8-847a-6edcbdf6fe68)

Bimser Destek ekibi tarafından yardım alınarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4cc2ef13-5ccf-4b1b-9cab-fecd054c5f49)(kaydet) butonu tıklanarak Sorgu tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload402ef142-6433-4e33-8006-f9ac21203788)

Tanımlanan Sorgu tipli parametrik Alan İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Gelişme Raporu sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb0539dea-75b9-4c38-9897-2c23ab6ff9d4)

Sorgu tipli parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload25faf77d-8dee-4776-919a-11fee2b1f76a)(seç) butonu tıklanıldığında sistemde tanımlı Pozisyon listesinde seçim yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade45742b7-fa99-4abd-a5fc-9a99cb7c1c85)

##### **1.1.1.1.2.7.Metin Tipli Parametrik Alanların Listesi**

İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Gelişme Raporu sekmesinde Metin tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Metin yazarak Metin tipli parametrik alanlar aratılır ve Metin tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Metin tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload46c95b1b-150a-459d-82c8-17fde8405f7b)

##### **1.1.1.1.2.8.Metin Tipli Parametrik Alan Tanımlama**

lblG_Param2 Metin tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc58c94f-dff5-4b5d-96ae-346a21b6539b) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc7f564fa-ae7c-4e6c-9bde-e2ca25084125)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5fb5db5c-bd5e-4737-b8df-e248ad375c98)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4cc2ef13-5ccf-4b1b-9cab-fecd054c5f49)(kaydet) butonu tıklanarak Metin tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5a46bbe6-107a-4493-aa9f-3b8b85466505)

Tanımlanan Metin tipli parametrik Alan İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Gelişme Raporu sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload278af3a7-9143-495b-9d59-a4face6e75b9)

##### **1.1.1.1.2.9.Ölçü Birimi Parametrik Alanların Listesi**

İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Gelişme Raporu sekmesinde Ölçü Birimi tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Ölçü Birimi yazarak Ölçü Birimi tipli parametrik alanlar aratılır ve Ölçü Birimi tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Ölçü Birimi tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3ea5b9b2-eae7-4184-9cd2-6d67dcfe8dae)

##### **1.1.1.1.2.10.Ölçü Birimi Parametrik Alan Tanımlama**

lblG_NParam3 Ölçü birimi tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc58c94f-dff5-4b5d-96ae-346a21b6539b) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade8d02b95-4c94-4783-82a1-f358444875ca)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc043f5ff-7df8-445f-ada8-f2509281c180)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4cc2ef13-5ccf-4b1b-9cab-fecd054c5f49)(Kaydet) butonu tıklanarak ölçü birimi tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcd5e489a-7466-4dce-9503-979c6166e600)

Tanımlanan ölçü birimi tipli parametrik alan İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Gelişme Raporu sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf9a7ca4d-3f0c-4193-8553-09aec8f79d37)

##### **1.1.1.1.2.11.Parasal Tipli Parametrik Alanların Listesi**

İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Gelişme Raporu sekmesinde Parasal tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Parasal yazarak Parasal tipli parametrik alanlar aratılır ve Parasal tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Parasal tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload95eb863a-a046-468b-a63c-5d54baddf0d9)

##### **1.1.1.1.2.12.Parasal Tipli Parametrik Alan Tanımlama**

lblG_NParam1 Parasal tipli alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc58c94f-dff5-4b5d-96ae-346a21b6539b) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload748e9145-85ca-4628-96b6-ef854b60bb68)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8e1ab8b8-a74b-40fb-93ac-07f581e6edf0)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4cc2ef13-5ccf-4b1b-9cab-fecd054c5f49)(Kaydet ) butonu tıklanarak Parasal tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2729796d-ed43-4985-acf4-67239fcb5f09)

Tanımlanan Parasal tipli parametrik alan İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Gelişme Raporu sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb4b750dc-cfcc-4ea9-a61b-936971cf77eb)

##### **1.1.1.1.2.13.Metin (Çoklu Satır) Tipli Parametrik Alanların Listesi**

İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Gelişme Raporu sekmesinde Metin (Çoklu Satır)  tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Metin (Çoklu Satır) yazarak Metin (Çoklu Satır) tipli parametrik alanlar aratılır ve Metin (Çoklu Satır)  tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Metin (Çoklu Satır)  tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9a30376d-d5a9-43c1-8519-0f126e88d5d9)

##### **1.1.1.1.2.14.Metin (Çoklu Satır) Tipli Parametrik Alan Tanımlama**

lblG_PARAM11 Metin (Çoklu Satır) tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc58c94f-dff5-4b5d-96ae-346a21b6539b) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadceb2e9a7-91af-4bf3-8f91-40e24d36b2db)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8caf0191-42cb-4bee-bf6e-c3fc6e0a62be)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4cc2ef13-5ccf-4b1b-9cab-fecd054c5f49)(kaydet) butonu tıklanarak Metin (Çoklu Satır) tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload11ea47a7-8511-4952-8712-fbfd1876c5f8)

Tanımlanan Metin (Çoklu Satır) Tipli parametrik alan İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Gelişme Raporu sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9aef9374-e17b-4e09-9a1b-c04a5d63952b)

İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Gelişme Raporu sekmesinde Tanımlanan Tüm Parametrik Tipli Alanlar;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload65797242-66ab-4202-8f18-2a34bcbf120e)

#### **1.1.1.1.3.İç Müşteri Şikayetleri Modülünde Modülünde Kök Neden Analizi Sekmesinde Parametrik Alan Tipi Tanımlaması**

İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Kök Neden Analizi sekmesinde tanımlanan parametrik alanların kısa kodları lblKOK başlığı ile tanımlı kısa kodlardır. lblKOK başlığındaki kısa kodlar olan tüm parametrik tipli alanlar tanımlandığında İç Müşteri Şikayetleri Modülünde Kök Neden Analizi sekmesi ekranında görüntülenir.

##### **1.1.1.1.3.1.Tarih Tipli Parametrik Alanların Listesi**

İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Kök Neden Analizi sekmesinde tarih tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına tarih yazarak tarih tipli parametrik alanlar aratılır ve tarih tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen tarih tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8c0b0e39-ea9e-414e-88f1-dbd44e059cee)

##### **1.1.1.1.3.2.Tarih Tipli Parametrik Alan Tanımlama.**

lblKOKDPARAM1 Tarih tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc58c94f-dff5-4b5d-96ae-346a21b6539b) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadecd4ba03-42d4-432b-9009-8407ba42a029)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload81f12592-d918-4e28-b15f-d39f9872e090)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4cc2ef13-5ccf-4b1b-9cab-fecd054c5f49)(Kaydet) butonu tıklanarak tarih tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2ccc6fdb-c149-4bc4-a1a4-bbde3f038e4f)

Tanımlanan tarih tipli parametrik Alan İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Kök Neden Analizi sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload143191f2-d10c-4166-a303-af8987d3391e)

##### **1.1.1.1.3.3.Liste Tipli Parametrik Alanların Listesi**

İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Kök Neden Analizi sekmesinde liste tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına liste yazarak liste tipli parametrik alanlar aratılır ve liste tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen liste tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5f2c8bcf-51ab-41e4-b8d3-55f9c16bf853)

##### **1.1.1.1.3.4.Liste Tipli Parametrik Alan Tanımlama**

lblKOKLPARAM1 Liste tipli parametrik seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc58c94f-dff5-4b5d-96ae-346a21b6539b) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb9a04733-5ef4-40b1-a68a-11fa9e4cb97a)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadee2f5309-31c4-4df8-95f6-466486006655)

Liste tipli alanın liste değerlerini girmek için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade75a24a8-38e7-435e-ae69-25434a4527d1) (Yeni) butonuna tıklanır, liste değerleri yazılır ve kaydedilir. Liste eleman değeri 1 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload96315248-3cff-4b0f-b64a-be0f58cfd3b0)

Liste eleman değeri 2 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5d7ae171-60db-4cb9-853c-2fb0d1a0a8ad)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfebdecad-4924-4c57-864f-13ffca189385)

Alanın zorunlu olup, olmayacağı sıra no bilgisi ve liste elemanları tanımlanarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4cc2ef13-5ccf-4b1b-9cab-fecd054c5f49)(kaydet) butonu tıklanarak liste tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8578b41c-ede4-4b5d-8c36-735c55bea1f8)

Tanımlanan liste tipli parametrik Alan İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Kök Neden Analizi sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9da8e2fc-e578-4414-9718-cd67b6505405)

##### **1.1.1.1.3.5.Metin Tipli Parametrik Alanların Listesi**

İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Kök Neden Analizi sekmesinde metin tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına metin yazarak Metin tipli parametrik alanlar aratılır ve metin tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen metin tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadce5a0558-44f6-4a2f-947d-3fed465147ca)

##### **1.1.1.1.3.6.Metin Tipli Parametrik Alan Tanımlama**

lblKOKPARAM1 Metin tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc58c94f-dff5-4b5d-96ae-346a21b6539b) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6403bd47-b3c1-4aa6-bd90-722594ef88a3)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc933a306-b3e3-418c-a974-4d4f225a9809)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4cc2ef13-5ccf-4b1b-9cab-fecd054c5f49)(kaydet) butonu tıklanarak Metin tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1d455d22-f1e7-460e-bae0-bf669820763a)

Tanımlanan Metin tipli parametrik Alan İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Kök Neden Analizi sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbdc9cafc-2e1d-4731-8b3b-6ed36f526ad8)

##### **1.1.1.1.3.7.Ölçü Birimi Parametrik Alanların Listesi**

İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Kök Neden Analizi sekmesinde ölçü Birimi tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına ölçü Birimi yazarak ölçü Birimi tipli parametrik alanlar aratılır ve ölçü Birimi tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen ölçü Birimi tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc68db859-ea73-43d7-84aa-54da62d856b1)

##### **1.1.1.1.3.8.Ölçü Birimi Parametrik Alan Tanımlama**

lblKOKNAPARAM1 Ölçü birimi tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc58c94f-dff5-4b5d-96ae-346a21b6539b) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload87afca0f-aaa1-4d77-809f-a537efca8d0a)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload08073afe-a346-4912-a657-993a414d9917)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4cc2ef13-5ccf-4b1b-9cab-fecd054c5f49)(Kaydet) butonu tıklanarak ölçü birimi tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf8e043b7-5bdf-43d2-9904-5f3e77ce95d7)

Tanımlanan ölçü birimi tipli parametrik alan İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Kök Neden Analizi sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9e1fa8ad-b6ac-4b11-ab7d-ab020262d7de)

##### **1.1.1.1.3.9.Parasal Tipli Parametrik Alanların Listesi**

İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Kök Neden Analizi sekmesinde parasal tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına parasal yazarak parasal tipli parametrik alanlar aratılır ve parasal tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen parasal tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6640ec6e-9109-4f04-89d8-8dbf842a94d9)

##### **1.1.1.1.3.10.Parasal Tipli Parametrik Alan Tanımlama**

lblKOKNCPARAM1 Parasal tipli alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc58c94f-dff5-4b5d-96ae-346a21b6539b) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload26cba385-9539-408c-af30-90e302eafd87)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4c5be20d-62d2-4cea-a401-025aae327d61)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4cc2ef13-5ccf-4b1b-9cab-fecd054c5f49)(Kaydet ) butonu tıklanarak parasal tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaabe407d-3185-4090-9809-29e91451bb67)

Tanımlanan parasal tipli parametrik alan İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Kök Neden Analizi sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload605e5ac5-feed-4651-99aa-103f9d60154a)

##### **1.1.1.1.3.11.Sorgu Tipli Parametrik Alanların Listesi**

İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Kök Neden Analizi sekmesinde Sorgu tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Sorgu yazarak Sorgu tipli parametrik alanlar aratılır ve Sorgu tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Sorgu tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8576cc53-a7c1-4890-a856-aa93b77d28c3)

##### **1.1.1.1.3.12.Sorgu Tipli Parametrik Alan Tanımlama**

lblKOK_QParam1 Sorgu tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc58c94f-dff5-4b5d-96ae-346a21b6539b) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb2de2532-3112-4451-b6da-fe0a0c3dc417)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada42e33a7-462a-4af9-a133-3dd42a6ba1be)

Bimser destek ekibinde yardım alınarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4cc2ef13-5ccf-4b1b-9cab-fecd054c5f49)(kaydet) butonu tıklanarak Sorgu tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd2c480b5-e0ea-4665-aa6c-33f2a60ae3cb)

Tanımlanan Sorgu Tipli parametrik alan İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Kök Neden Analizi sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfacdab50-6722-4171-af42-edc3ad7a7acc)

Sorgu tipli parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload25faf77d-8dee-4776-919a-11fee2b1f76a)(seç) butonu tıklanıldığında sistemde tanımlı Departman listesinde seçim yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload21c1f31d-42cd-452c-b5e1-a74c417c643b)

##### **1.1.1.1.3.13.Personel Tipli Parametrik Alanların Listesi**

İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Kök Neden Analizi sekmesinde Personel tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Personel yazarak Personel tipli parametrik alanlar aratılır ve Personel tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Personel tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload808e3ca4-18fe-4884-841e-5957e2f49602)

##### **1.1.1.1.3.14.Personel Tipli Parametrik Alan Tanımlama**

lblKOK_PParam1 Personel tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc58c94f-dff5-4b5d-96ae-346a21b6539b) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3d8bbade-8e77-4699-9250-8401c441cf7b)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade0ce787c-9f51-47f8-87d2-5161b6e9cbe0)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4cc2ef13-5ccf-4b1b-9cab-fecd054c5f49)(kaydet) butonu tıklanarak Personel tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload670c448a-f6ee-4721-a746-eace45ca6e03)

Tanımlanan Personel Tipli parametik alan İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Kök Neden Analizi sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaa45feb1-47ae-4918-a7f8-e6de60625bda)

Personel tipli parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload25faf77d-8dee-4776-919a-11fee2b1f76a)(seç) butonu tıklanıldığında sistemde tanımlı personel listesinde seçim yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5dada6d2-57ed-431b-81c6-2996d5fd7071)

##### **1.1.1.1.3.15.Metin (Çoklu Satır) Tipli Parametrik Alanların Listesi**

İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Kök Neden Analizi sekmesinde Metin (Çoklu Satır)  tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Metin (Çoklu Satır) yazarak Metin (Çoklu Satır) tipli parametrik alanlar aratılır ve Metin (Çoklu Satır)  tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Metin (Çoklu Satır)  tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload53f3be92-8a0c-4a96-8ea2-422c90693674)

##### **1.1.1.1.3.16.Metin (Çoklu Satır) Tipli Parametrik Alan Tanımlama**

lblKOKPARAM4 Metin (Çoklu Satır) tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc58c94f-dff5-4b5d-96ae-346a21b6539b) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload47c41ca6-be39-4257-b7bd-b1f4026a8945)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9b0d711a-9d73-4e34-9315-822df9e42662)

Alanın zorunlu olup, olmayacağı sıra no bilgisi, gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4cc2ef13-5ccf-4b1b-9cab-fecd054c5f49)(kaydet) butonu tıklanarak Metin (Çoklu Satır) tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload84f27f6b-5643-493e-8511-356c316b6bcb)

Tanımlanan Metin (Çoklu Satır) Tipli parametrik alan İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Kök Neden Analizi sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload713cb2ee-15dc-40d7-8dac-5de420d9b77e)

İç Müşteri Şikayetleri Modülünde Şikayet Kaydı ekranında Kök Neden Analizi sekmesinde Tanımlanan Tüm Alanlar;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc8d79520-267e-4783-a736-3421aa440da1)

#### **1.1.1.1.4.İç Müşteri Şikayetleri Modülünde Aksiyonlar Sekmesinde Parametrik Alan Tipi Tanımlaması**

İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Aksiyonlar sekmesinde tanımlanan parametrik tipli alanların kısa kodları lblA\_ başlığı ile tanımlı kısa kodlardır. lblA \_ başlığındaki kısa kodlar olan tüm parametrik tipli alanlar tanımlandığında İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Aksiyonlar sekmesi ekranında görüntülenir.

##### **1.1.1.1.4.1.Tarih Tipli Parametrik Alanların Listesi**

İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Aksiyonlar sekmesinde tarih tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına tarih yazarak tarih tipli parametrik alanlar aratılır ve tarih tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen tarih tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload646c8b35-a70b-4dc4-8c36-f5f4011fe571)

##### **1.1.1.1.4.2.Tarih Tipli Parametrik Alan Tanımlama**

lblA_DParam1 Tarih tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc58c94f-dff5-4b5d-96ae-346a21b6539b) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd6c9aea9-9c8d-4d48-a468-03c63a6b2b1b)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade8a746c9-048e-486c-b134-79c938dcac06)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4cc2ef13-5ccf-4b1b-9cab-fecd054c5f49)(Kaydet) butonu tıklanarak tarih tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc804f4cc-2229-4ddb-8866-fdc7f5ef7a31)

Tanımlanan tarih tipli parametrik alan İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Aksiyonlar sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada7981d8a-7083-4a58-88d4-8c32dec72703)

##### **1.1.1.1.4.3.Liste Tipli Parametrik Alanların Listesi**

İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Aksiyonlar sekmesinde liste tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına liste yazarak liste tipli parametrik alanlar aratılır ve liste tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen liste tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload999b4eae-0ef5-40ac-bdd3-fc424f7fb113)

##### **1.1.1.1.4.4.Liste Tipli Parametrik Alan Tanımlama**

lblA_LParam1 Liste tipli parametrik seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc58c94f-dff5-4b5d-96ae-346a21b6539b) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload09bb2cd0-13aa-472a-a27a-2b2f6a062dfd)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6c1efa21-8d77-4a60-98ec-9504ab9914d7)

Liste tipli alanın liste değerlerini girmek için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade75a24a8-38e7-435e-ae69-25434a4527d1) (Yeni) butonuna tıklanır, liste değerleri yazılır ve kaydedilir. Liste elaman değeri 1 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2b0e2176-0036-4b30-ba4f-e5a7cb9b9412)

Liste eleman değeri 2 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload01d50075-f8e0-45f6-83ae-4974642a4b49)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcc04cae9-4496-49af-9184-d190bb1982a5)

Alanın zorunlu olup, olmayacağı sıra no bilgisi ve liste elemanları tanımlanarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4cc2ef13-5ccf-4b1b-9cab-fecd054c5f49)(kaydet) butonu tıklanarak liste tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf61e977e-7602-4f6e-9b01-bf099bff1de4)

Tanımlanan liste tipli parametrik alan İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Aksiyonlar sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade55264a0-dd7f-46dd-b441-253108d5e17c)

##### **1.1.1.1.4.5.Sorgu Tipli Parametrik Alanların Listesi**

İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Aksiyonlar sekmesinde sorgu tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına sorgu yazarak sorgu tipli parametrik alanlar aratılır ve sorgu tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen sorgu tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8686a2ca-4709-4595-bc64-7ffd0c877306)

##### **1.1.1.1.4.6.Sorgu Tipli Parametrik Alan Tanımlama**

lblA_QPARAM1 Sorgu tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc58c94f-dff5-4b5d-96ae-346a21b6539b) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadae747eed-033c-40d3-9da1-4194df2b198e)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade93d04bd-ef7b-4c95-b456-53d11f26343e)

Bimser Destek ekibi tarafından gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4cc2ef13-5ccf-4b1b-9cab-fecd054c5f49)(kaydet) butonu tıklanarak Sorgu tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload58fb4dd6-f646-4499-b86a-369824000f77)

Tanımlanan sorgu tipli parametrik alan İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Aksiyonlar sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload45934aec-e804-426e-9c64-3c47d8bbdb42)

Sorgu tipli parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload25faf77d-8dee-4776-919a-11fee2b1f76a)(seç) butonu tıklanıldığında sistemde tanımlı Pozisyon listesinde seçim yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2f9d9608-571d-43ee-ba93-ce9d551982d0)

##### **1.1.1.1.4.7.Metin Tipli Parametrik Alanların Listesi**

İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Aksiyonlar sekmesinde metin tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına metin yazarak metin tipli parametrik alanlar aratılır ve metin tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen metin tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload730cbc64-d9c5-4a78-8915-0a8ee7e23bc1)

##### **1.1.1.1.4.8.Metin Tipli Parametrik Alan Tanımlama**

lblA_Param1 Metin tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc58c94f-dff5-4b5d-96ae-346a21b6539b) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf95c5fdf-78ba-4adc-a9b6-d8f02475a8f8)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5279ed01-3d82-480a-b071-0a1e061e2372)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4cc2ef13-5ccf-4b1b-9cab-fecd054c5f49)(kaydet) butonu tıklanarak Metin tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadacb334a1-9ddb-4f98-a928-b7ef8861cc8f)

Tanımlanan metin tipli parametrik alan İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Aksiyonlar sekmesinde görüntülenir

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6c946938-3688-49cf-b24b-28cac29ea32e)

##### **1.1.1.1.4.9.Ölçü Birimi Parametrik Alanların Listesi**

İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Aksiyonlar sekmesinde ölçü Birimi tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına ölçü Birimi yazarak ölçü Birimi tipli parametrik alanlar aratılır ve ölçü Birimi tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen ölçü Birimi tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2e66f3a5-4896-4ae1-87e1-58757ee300f7)

##### **1.1.1.1.4.10.Ölçü Birimi Parametrik Alan Tanımlama**

lblA_NParam3 Ölçü birimi tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc58c94f-dff5-4b5d-96ae-346a21b6539b) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf70afc6e-e006-45ba-a544-f3fabd8152fa)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada730deef-ade3-4294-af0e-86d894257095)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4cc2ef13-5ccf-4b1b-9cab-fecd054c5f49)(Kaydet) butonu tıklanarak ölçü birimi tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8a748922-c27c-40d4-a3c1-29ffc92422ae)

Tanımlanan ölçü birimi tipli parametrik alan İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Aksiyonlar sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload958210d3-7dc0-45d0-bf50-c46f42f7e26d)

##### **1.1.1.1.4.11.Parasal Tipli Parametrik Alanların Listesi**

İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Aksiyonlar sekmesinde parasal tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına parasal yazarak parasal tipli parametrik alanlar aratılır ve parasal tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen parasal tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1bafb303-38f4-4600-9deb-00d22e387080)

##### **1.1.1.1.4.12.Parasal Tipli Parametrik Alan Tanımlama**

lblA_NParam1 Parasal tipli alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc58c94f-dff5-4b5d-96ae-346a21b6539b) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadad73eb7d-1dbf-4dc9-a1d3-00ac56c9991e)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload86400d5c-e893-487c-890e-601ab71f946d)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4cc2ef13-5ccf-4b1b-9cab-fecd054c5f49)(Kaydet ) butonu tıklanarak parasal tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload681d95e8-be94-4ba8-a16b-d56261858001)

Tanımlanan parasal tipli parametrik alan İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Aksiyonlar sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9bb374d0-89e7-4d42-ae14-50f013b80a20)

##### **1.1.1.1.4.13.Personel Tipli Parametrik Alanların Listesi**

İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Aksiyonlar sekmesinde Personel tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Personel yazarak Personel tipli parametrik alanlar aratılır ve Personel tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Personel tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3db817f8-b7fe-432b-9e08-e1d437fb0449)

##### **1.1.1.1.4.14.Personel Tipli Parametrik Alan Tanımlama**

lblA_PParam1 Personel tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc58c94f-dff5-4b5d-96ae-346a21b6539b) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2494ebfe-36a7-49c9-8381-ad67230c55aa)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload938d6f1d-951e-4409-9ab0-704b7a68cc0e)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4cc2ef13-5ccf-4b1b-9cab-fecd054c5f49)(kaydet) butonu tıklanarak Personel tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadca10858a-6055-4aa4-b457-84c401d54cc6)

Tanımlanan Personel Tipli parametik alan İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Aksiyonlar sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd8dda938-6ccd-40b2-8290-6399218a9345)

Personel tipli parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload25faf77d-8dee-4776-919a-11fee2b1f76a)(seç) butonu tıklanıldığında sistemde tanımlı personel listesinde seçim yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3ac05ea8-cfa6-4998-8756-0ed32f7616e2)

İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Aksiyonlar sekmesinde tanımlanan tüm parametrik alanlar;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb6204426-cadb-4ff2-887a-5c4168b1c7db)

#### **1.1.1.1.5.İç Müşteri Şikayetleri Modülünde Sonuç Raporu Sekmesinde Parametrik Alan Tipi Tanımlaması**

İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Sonuç Raporu sekmesinde tanımlanan parametrik alanların kısa kodları lblS\_ başlığı ile tanımlı kısa kodlardır. lblS\_ başlığındaki kısa kodlar olan tüm parametrik tipli alanlar tanımlandığında İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Sonuç Raporu sekmesinde ekranında görüntülenir.

##### **1.1.1.1.5.1.Liste Tipli Parametrik Alanların Listesi**

İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Sonuç Raporu sekmesinde liste tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına liste yazarak liste tipli parametrik alanlar aratılır ve liste tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen liste tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload08c4eccc-d454-4dc5-9746-72e67a566b51)

##### **1.1.1.1.5.2.Liste Tipli Parametrik Alan Tanımlama.**

lblS_LParam2 Liste tipli parametrik seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc58c94f-dff5-4b5d-96ae-346a21b6539b) (değiştir) butonuna tıklanır

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfa372142-b693-4dd2-a30b-0494b0617a7d)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload884be4ab-0609-416c-b124-9db17aa7bfec)

Liste tipli alanın liste değerlerini girmek için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade75a24a8-38e7-435e-ae69-25434a4527d1) (Yeni) butonuna tıklanır, liste değerleri yazılır ve kaydedilir. Liste eleman değeri 1 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload10fbb28c-34a9-40b8-8dc0-c5a14b4bf34f)

Liste eleman değeri 2 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload152453bf-ca5e-469b-b91a-031af5480110)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadee008fe9-687d-453d-b420-8f1c650dc5d8)

Alanın zorunlu olup, olmayacağı sıra no bilgisi ve liste elemanları tanımlanarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4cc2ef13-5ccf-4b1b-9cab-fecd054c5f49)(kaydet) butonu tıklanarak liste tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0af85258-7870-4d42-9175-a47398ef51ae)

Tanımlanan liste tipli parametrik alan İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Sonuç Raporu sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadebd050b9-d455-47db-9b62-66ebfbf16a81)

##### **1.1.1.1.5.3.Personel Tipli Parametrik Alanların Listesi**

İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Sonuç Raporu sekmesinde personel tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına personel yazarak personel tipli parametrik alanlar aratılır ve personel tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen personel tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload99977e91-af88-4917-9170-289af589dfb5)

##### **1.1.1.1.5.4.Personel Tipli Parametrik Alan Tanımlama.**

lblS_PParam1 Personel tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc58c94f-dff5-4b5d-96ae-346a21b6539b) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbcd99eb2-cf2f-47e6-997a-50519f3d655e)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload64038e58-6be3-4f7f-afaf-b4ebc0eca1a6)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4cc2ef13-5ccf-4b1b-9cab-fecd054c5f49)(kaydet) butonu tıklanarak personel tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload42edab68-6ba3-4def-96ed-9efd85741682)

Tanımlanan personel tipli parametrik alan İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Sonuç Raporu sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload82713841-e1ea-4213-b53c-6f7595ebc295)

Personel tipli parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload25faf77d-8dee-4776-919a-11fee2b1f76a)(seç) butonu tıklanıldığında sistemde tanımlı personel listesinde seçim yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload75d26f10-1aa7-45f0-b24c-12c0cafe11b5)

##### **1.1.1.1.5.5.Sorgu Tipli Parametrik Alanların Listesi**

İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Sonuç Raporu sekmesinde sorgu tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına sorgu yazarak sorgu tipli parametrik alanlar aratılır sorgu tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen sorgu tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadac710d71-d2d3-46c8-a7df-8b58bcded057)

##### **1.1.1.1.5.6.Sorgu Tipli Parametrik Alan Tanımlama**

lblS_QParam1 Sorgu tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc58c94f-dff5-4b5d-96ae-346a21b6539b) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd71083dd-c04f-403b-b11d-bc11238efdcb)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd6934715-674c-41e7-804a-d1dd85449624)

Bimser Destek ekibi tarafından yardım alınarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4cc2ef13-5ccf-4b1b-9cab-fecd054c5f49)(kaydet) butonu tıklanarak Sorgu tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload13eb5182-8f04-4de8-8bb3-9b4af8ef648d)

Tanımlanan sorgu tipli parametrik Alan İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Sonuç Raporu sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload624772e4-a84d-4758-92cc-f5d9b00bf460)

Sorgu tipli parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd2d34306-f7fc-4567-8caf-ef1f26e0806b) (Seç) butonu tıklanıldığında sistemde tanımlı Pozisyon listesinde tekli ve çoklu seçim yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddbdf17d3-cdfb-4146-ab92-7dd9dbd05891)

##### **1.1.1.1.5.7.Metin Tipli Parametrik Alanların Listesi**

İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Sonuç Raporu sekmesinde metin tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına metin yazarak metin tipli parametrik alanlar aratılır metin tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen metin tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8dea7eb0-3f06-4eee-9b37-5d1ecefbbb89)

##### **1.1.1.1.5.8.Metin Tipli Parametrik Alan Tanımlama**

lblS_Param2 Metin tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc58c94f-dff5-4b5d-96ae-346a21b6539b) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfa492720-09d2-42af-8ad0-31ada676aab8)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload05610c8d-4ad4-4c41-a333-f6a2d9b25e11)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4cc2ef13-5ccf-4b1b-9cab-fecd054c5f49)(kaydet) butonu tıklanarak metin tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfa298447-4622-45e7-ac4c-ad6f32b71252)

Tanımlanan metin tipli parametrik alan İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Sonuç Raporu sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3da205e3-e3a9-4ab7-a55c-98fdf7bca15e)

##### **1.1.1.1.5.9.Ölçü Birimi Parametrik Alanların Listesi**

İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Sonuç Raporu sekmesinde ölçü Birimi tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına ölçü Birimi yazarak ölçü Birimi tipli parametrik alanlar aratılır ölçü Birimi tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen ölçü Birimi tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4e03e1ef-c83a-4b69-bd90-158baf6118fe)

##### **1.1.1.1.5.10.Ölçü Birimi Parametrik Alan Tanımlama**

lblS_NParam3 Ölçü birimi tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc58c94f-dff5-4b5d-96ae-346a21b6539b) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload998c0075-80e4-48ee-8a11-b7ab9fd6dcfe)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaded26f386-ee6f-4f68-a8b2-c644bdf98dfb)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4cc2ef13-5ccf-4b1b-9cab-fecd054c5f49)(Kaydet) butonu tıklanarak ölçü birimi tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8d20131f-edb2-4750-b9dd-e686d48f1240)

Tanımlanan ölçü birimi tipli parametrik alan İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Sonuç Raporu sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload704e7eeb-86eb-4cb4-bc12-870e14975bbd)

##### **1.1.1.1.5.11.Parasal Tipli Parametrik Alanların Listesi**

İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Sonuç Raporu sekmesinde parasal tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına parasal yazarak parasal tipli parametrik alanlar aratılır parasal tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen parasal tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada487eebb-6ccf-4c3f-84b0-52e1564d97c9)

##### **1.1.1.1.5.12.Parasal Tipli Parametrik Alan Tanımlama**

lblS_NParam1 Parasal tipli alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc58c94f-dff5-4b5d-96ae-346a21b6539b) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload70b9cc84-d85b-4062-99d0-596c3e322a6a)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6d1630a3-d408-4b47-943d-05b75719a3df)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4cc2ef13-5ccf-4b1b-9cab-fecd054c5f49)(Kaydet ) butonu tıklanarak Parasal tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload221de5db-7b55-4ec2-b4bd-dd8c12947bc0)

Tanımlanan parasal tipli parametrik alan İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Sonuç Raporu sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3089277e-bc1c-43b0-84ff-2a64a8813f9e)

İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Sonuç Raporu sekmesinde tanımlanan tüm parametrik alanlar;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload30822213-1226-4943-9eff-4efc59f00dcb)

#### **1.1.1.1.6.İç Müşteri Şikayetleri Modülünde Kapatma sekmesinde Parametrik Alan Tipi Tanımlaması**

İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Kapatma sekmesinde tanımlanan parametrik alanların kısa kodları lblK\_ başlığı ile tanımlı kısa kodlardır. lblK\_ başlığındaki kısa kodlar olan tüm parametrik tipli alanlar tanımlandığında İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Kapatma sekmesinde ekranında görüntülenir.

##### **1.1.1.1.6.1.Liste Tipli Parametrik Alanların Listesi**

İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Kapatma sekmesinde liste tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına liste yazarak liste tipli parametrik alanlar aratılır liste tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen liste tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload62bd68d5-1bc0-48d3-a2e4-89f22abbd67b)

##### **1.1.1.1.6.2.Liste Tipli Parametrik Alan Tanımlama.**

lblK_LParam2 Liste tipli parametrik seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc58c94f-dff5-4b5d-96ae-346a21b6539b) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload87c68e44-6c06-4632-9c13-bf600d02f80e)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload850d0ba7-33a6-4925-b260-093cb02be942)

Liste tipli alanın liste değerlerini girmek için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade75a24a8-38e7-435e-ae69-25434a4527d1) (Yeni) butonuna tıklanır, liste değerleri yazılır ve kaydedilir. Liste elaman değeri 1 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload336698be-c89e-4aa0-9ff5-8995f2c98879)

Liste eleman değeri 2 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddf19150e-8474-45a0-a33d-b254ee139383)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9cf8d5ce-935d-45fc-ae16-75b4edf87b76)

Alanın zorunlu olup, olmayacağı sıra no bilgisi ve liste elemanları tanımlanarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4cc2ef13-5ccf-4b1b-9cab-fecd054c5f49)(kaydet) butonu tıklanarak liste tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadff391631-bb8d-4eec-8b88-19c520c4b731)

Tanımlanan liste tipli parametrik alan İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Kapatma sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfe22e6de-9c99-4d5f-a86f-9283dde83f9a)

##### **1.1.1.1.6.3.Personel Tipli Parametrik Alanların Listesi**

İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Kapatma sekmesinde personel tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına personel yazarak personel tipli parametrik alanlar aratılır personel tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen personel tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfdf815f9-b264-490d-8bf8-f72b677e5943)

##### **1.1.1.1.6.4.Personel Tipli Parametrik Alan Tanımlama**

lblK_PParam1 Personel tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc58c94f-dff5-4b5d-96ae-346a21b6539b) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade630d4e5-5809-4ee4-ba3f-52bca0ec1e5e)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload33499ce5-7d69-4dab-b2e0-2c25f5239405)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4cc2ef13-5ccf-4b1b-9cab-fecd054c5f49)(kaydet) butonu tıklanarak personel tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0a0fe108-fcb6-4f10-8318-72d3f648782a)

Tanımlanan personel tipli parametrik alan İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Kapatma sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaf3686f3-c1a7-4222-93e4-5272a5c028e3)

Personel tipli parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload25faf77d-8dee-4776-919a-11fee2b1f76a)(seç) butonu tıklanıldığında sistemde tanımlı personel listesinde seçim yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6fe96718-39a9-47a5-b965-0d9da07bfc19)

##### **1.1.1.1.6.5.Sorgu Tipli Parametrik Alanların Listesi**

İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Kapatma sekmesinde sorgu tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına sorgu yazarak sorgu tipli parametrik alanlar aratılır sorgu tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen sorgu tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload75166e8d-428d-4176-98e2-0efc331f2c5f)

##### **1.1.1.1.6.6.Sorgu Tipli Parametrik Alan Tanımlama**

lblK_QParam1 Sorgu tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc58c94f-dff5-4b5d-96ae-346a21b6539b) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade834de02-7da5-42e8-8128-28374034085c)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6a26771d-91c7-4ce5-b3f2-2406bc5482cd)

Bimser Destek ekibi tarafından destek alınarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4cc2ef13-5ccf-4b1b-9cab-fecd054c5f49)(kaydet) butonu tıklanarak Sorgu tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbe5f37f5-9859-4796-ac86-67b807b43674)

Tanımlanan sorgu tipli parametrik alan İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Kapatma sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload79495454-db81-40fa-a6b1-3f75a245bd19)

Sorgu tipli parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload25faf77d-8dee-4776-919a-11fee2b1f76a)(seç) butonu tıklanıldığında sistemde tanımlı Departman listesinde seçim yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7f22399b-f175-4f20-89c9-f74f21bee2e9)

##### **1.1.1.1.6.7.Metin Tipli Parametrik Alanların Listesi**

İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Kapatma sekmesinde metin tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına metin yazarak metin tipli parametrik alanlar aratılır metin tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen metin tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload33c83ea4-d97b-4111-8cca-80e8cef24a1c)

##### **1.1.1.1.6.8.Metin Tipli Parametrik Alan Tanımlama**

lblK_Param2 Metin tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc58c94f-dff5-4b5d-96ae-346a21b6539b) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade6f51660-3764-4962-8043-d17c75b2af34)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7ff35b10-d435-4e2a-aa0e-cb23ec03af01)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4cc2ef13-5ccf-4b1b-9cab-fecd054c5f49)(kaydet) butonu tıklanarak metin tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadacd1a01e-0832-478c-8251-a1da738d7d5c)

Tanımlanan metin tipli parametrik alan İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Kapatma sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload78077be1-db37-4079-baab-f072c3a7d3f8)

##### **1.1.1.1.6.9.Ölçü Birimi Parametrik Alanların Listesi**

İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Kapatma sekmesinde ölçü Birimi tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına ölçü Birimi yazarak ölçü Birimi tipli parametrik alanlar aratılır ölçü Birimi tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen ölçü Birimi tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload29bd9e10-cbd8-4523-b101-fda7a5a8a699)

##### **1.1.1.1.6.10.Ölçü Birimi Parametrik Alan Tanımlama**

lblK_NParam3 Ölçü birimi tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc58c94f-dff5-4b5d-96ae-346a21b6539b) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2636baff-792b-44c4-83fd-6fb7a8a20da7)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload38d1231c-a144-4a6f-b023-45c7dab6a1ac)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4cc2ef13-5ccf-4b1b-9cab-fecd054c5f49)(Kaydet) butonu tıklanarak ölçü birimi tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload87c7f7fc-9cae-400e-a066-c8c4ce52c307)

Tanımlanan ölçü birimi tipli parametrik Alan İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Kapatma sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2ebbd3a8-a9f5-4222-9178-975441d3eba2)

##### **1.1.1.1.6.11.Parasal Tipli Parametrik Alanların Listesi**

İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Kapatma sekmesinde parasal tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına parasal yazarak parasal tipli parametrik alanlar aratılır parasal tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen parasal tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd69aded2-619e-436b-aaa4-fbf66b8529e4)

##### **1.1.1.1.6.12.Parasal Tipli Parametrik Alan Tanımlama**

lblK_NParam2 Parasal tipli alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc58c94f-dff5-4b5d-96ae-346a21b6539b) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload75e01c69-6e08-41cd-8a84-f3215a69c07a)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7b9c57fa-0fe7-4cc1-a045-8b09f185affd)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4cc2ef13-5ccf-4b1b-9cab-fecd054c5f49)(Kaydet ) butonu tıklanarak parasal tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddca45005-1732-437d-918a-fe71c1579f37)

Tanımlanan parasal tipli parametrik alan İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Kapatma sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload66231ddb-e90a-4fbc-8e9a-a8a1f4a0e276)

##### **1.1.1.1.6.13.Tarih Tipli Parametrik Alanların Listesi**

İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Kapatma sekmesinde tarih tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına tarih yazarak tarih tipli parametrik alanlar aratılır ve tarih tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen tarih tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc0f2b5c6-77b7-4af3-925e-64378f09ce4f)

##### **1.1.1.1.6.14.Tarih Tipli Parametrik Alan Tanımlama**

lblK_DParam1Tarih tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc58c94f-dff5-4b5d-96ae-346a21b6539b) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload87d32387-879a-475f-bbd9-a907454de364)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb59fc714-e083-4937-b167-9a99811a1edd)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4cc2ef13-5ccf-4b1b-9cab-fecd054c5f49)(Kaydet) butonu tıklanarak tarih tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7d6ee1cc-21eb-4039-aba5-f360e13ec3bf)

Tanımlanan tarih tipli parametrik alan İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Kapatma sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada80aab39-4d0f-4b9f-9a16-ee515464e135)

İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Kapatma sekmesinde tanımlanan tüm parametrik alanlar;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf2aa93e0-67f3-49d1-b624-232077a81234)

#### **1.1.1.1.7.Dil ayarlarında Tanımlan Parametrik Alan tipleri Görüntülen Ekrandan Kaldırma İşlemi**

1.Aşamada parametrik alanın bulunduğu ekran açılır. İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Kapatma sekmesinde görüntülenir

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload633a4cfa-a0c4-4499-bf11-a860a0bbacff)

2\. Aşamada Parametrik Alanın bulunduğu ekran görüntülendikten sonra örnekteki herhangi alan seçilerek, Sağ tıkla/Kopyala komutu ile parametrik alanın ismi kopyalanır. Örnek: İstenilen Tarih

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb29000da-90c4-4842-963b-be79518afbc2)

3\. Aşamada Sistem Altyapı Tanımları\>BSAT\>Konfigürasyon Ayarları\>Dil ayarları menüsü tıklanarak açılan ekranda Modül olarak İç Müşteri Şikayetleri Modülü seçilir. Kopyalanan Dil ayarlarından tanımlanan liste tipli parametrik alanı grid ekranında **TR** alanına sağ tıkla/yapıştır komutu ile alanın yapıştırma işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload16308c5f-6aa9-411d-9348-9fbc4c819c6f)

4.Aşamada liste tipli tipli parametrik alan seçilerek alanın içeriği görüntülemek için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc58c94f-dff5-4b5d-96ae-346a21b6539b) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload095abb37-d8ea-4c1f-ba2a-1315b4cb771c)

5.Aşamada içeriği görüntülen liste tipli alanın değeri silerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4cc2ef13-5ccf-4b1b-9cab-fecd054c5f49)(Kaydet) butonu tıklanarak Dil Ayarları menüsünde tanımlıTarih tipli alanın kaldırma işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6f15fa34-b5c3-4253-9581-cb302e2b8aff)

Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarlarında tanımlanan diğer parametrik alan tiplerin dil ayarları menüsünde kaldırma işlemi aynı şekilde olmaktadır. İç Müşteri Şikayetleri Modülünde Şikayet detayı ekranında Kapatma sekmesinde tanımlı liste tipli alanın kaldırılmış olduğu görülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd4deb8ae-cbdb-4d84-a830-18c2a2be9648)
