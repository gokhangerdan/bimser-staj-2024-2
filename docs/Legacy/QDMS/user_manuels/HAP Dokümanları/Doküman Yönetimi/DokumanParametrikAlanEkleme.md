---
title: Parametrik Alan Tanımlama İşlemi
description: Parametrik Alan Tanımlama İşlemi Yardım Dokümanı
sidebar_position: 3
---

:::tip Bilgi

İlgili konu başlığına sağ tarafta bulunan navigasyon yardımıyla hızlı bir şekilde ulaşabilirsiniz.

:::


**Doküman Yönetimi Modülünde Dil Ayarları Menüsünde Parametrik Alan Tanımlama Kullanıcı Yardım Dokümanı**

# **1.Sistem Altyapı Tanımları**

Personel bilgilerinin tanımlandığı ve diğer modüller için gerekli olan altyapının kurgulanmasının yapıldığı menüdür.

## **1.1.Konfigürasyon Ayarları**

**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları

QDMS sisteminde özel ayarların yapıldığı menülerdir. Bu menülerde yapılan ayarlar tüm QDMS kullanıcıları için geçerli olan ortak ayarlardır.

### **1.1.1. Dil Ayarları**

**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları

Dil ayarları menüsünden QDMS üzerinde görülen menülerin isimleri, alanların isimleri değiştirilebilir. Modüllere yeni alanlar eklenebilir. Var olan alanların zorunluluk durumları düzenlenebilir. Alanların ekran üzerinde göründükleri sıralama değiştirilebilir.

### **1.1.1.1.Doküman Yönetimi Modülü Ortak Kullanım İçin Yeni Alan Oluşturma**

Doküman Yönetimi Modülünde Doküman için Diğer Bilgiler sekmesinde ve Kalite Kaydı için Kalite Kaydı/Kayıt Görüntüleme sekmesinde firmanın istemiş olduğu sistemde olmayan ekstradan alanlar tanımlanabilir. Tanımlanan bu alanlar tüm Doküman Yönetimi Modül kaynakları için geçerlidir. Sistem Altyapı Tanımları/BSAT/ Konfigürasyon Ayarları/Dil Ayarları menüsü tıklanılır. Açılan Dil Ayarları sayfasında Modül alanında “Doküman Yönetimi” seçilir ve ekranda Doküman Yönetimi Modülü ile ilgili dil tanımları görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8f9fb32d-e659-438d-b341-ea4b3e54bcff)

Doküman Yönetimi Modülünde Entegre Yönetim Sistemi\>Doküman İşlemleri \>Doküman Hazırlama menüsü baz alanılarak Diğer Bilgiler sekmesinde Dil ayarlarından parametrik alan tanımlaması yapılmaktadır. Sistem Altyapı Tanımları\>BSAT\>Konfigürasyon Ayarlar\>Dil Ayarları menüsünde tanımlanan parametrik alanlar Doküman Yönetimi Modülünde Diğer bilgiler sekmesinde diğer menülerde de yer almaktadır. Doküman Yönetimi Modülünde ayrıca Entegre Yönetim Sistemi\>Doküman işlemleri\>Kalite Kaydı\>Kalite Kaydı İşlemleri menüsünde listesinde Kalite Kaydının bulunduğu Klasör seçilerek Kalite kaydı görüntülendikten sonra açılan ekranda Yeni butonu tıklanarak açılan Kalite Kaydı sayfasında Kayıt Görüntüleme sekmesinde dil ayarları menüsünde tanımlanan parametrik alanlar görüntülenir. Kısaca Dil ayarlarında Doküman Yönetimi Modülü için tanımlanan parametrik alanlar Doküman için Diğer Bilgiler sekmesinde, Kalite kaydı içinde Kayıt Görüntüleme sekmesinde görüntülenir.

**Doküman Yönetimi Modülünde Tanımlanan Parametrik Tipli Alanlar ve Tanımları;**

**1-Tarih tipli**: Takvim alanı eklenilen parametrik alandır. Örnek Kısa Kod: lblDALAN1(Doküman için Diğer Bilgiler sekmesinde görüntülenir), lblKK_DPARAM1((Kalite Kaydı için Kayıt Görüntüleme Sekmesinde görüntülenir.)

**2-Liste tipli**: Birden fazla liste elemanları arasından tek seçim yapılan parametrik alandır. Liste elemanları tanımlanarak, tanımlanan liste elemanlarında seçip yapılır. Örnek Kısa Kod: lblALAN10 (Doküman için Diğer Bilgiler sekmesinde görüntülenir), lblKK_LPARAM1(Kalite Kaydı için Kayıt Görüntüleme Sekmesinde görüntülenir.)

**3-Personel Tipli:** QDMS personel veri tabanından kişi seçilebilmesini sağlayan parametrik alandır. Sistem Altyapı Tanımları\>Bsat\>Tanımlama\>Personel Tanımlama menüsünde tanımlı olan Personellerin listesinde seçim yapılır. Örnek Kısa Kod: lblPALAN1(Doküman için Diğer Bilgiler sekmesinde görüntülenir)

**4-Sorgu tipli:**QDMS/Ensemble veri tabanları içerisindeki ana verilerden seçim yapılabilmesi için tanımlanabilen alan türüdür. (Sadece Bimser Destek Ekibi tarafından tanımlanmalıdır) Tekli ve çoklu seçim yapılabilir. Örnek Kısa Kod: lblQALAN1(Doküman için Diğer Bilgiler sekmesinde görüntülenir)

**5-Metin tipli**: Elle yazım imkanı veren metin kutucuğu ekleyen parametrik alandır. Örnek Kısa Kod: lblALAN2 (Doküman için Diğer Bilgiler sekmesinde görüntülenir), lblKK_PARAM1(Kalite Kaydı için Kayıt Görüntüleme Sekmesinde görüntülenir.)

**6-Metin (Çoklu Satır)Tipli** : Elle yazım imkanı veren karakter sınırı olmayan çok satırlı metin kutucuğu eklenen parametrik alandır. Örnek Kısa Kod: lblMALAN1(Doküman için Diğer Bilgiler sekmesinde görüntülenir), lblKK_PARAM9 (Kalite Kaydı için Kayıt Görüntüleme Sekmesinde görüntülenir.)

**7- Departman Tipli:** QDMS departman veri tabanından departman bilgisi seçilebilmesini sağlayan parametrik alandır. Sistem Altyapı Tanımları\>BSAT\>Tanımlar\>Departman Tanımlama menüsünde tanımlı departman listesinden departman bilgisinin seçimi yapılır. Örnek Kısa Kod: lblKK_DSPARAM1(Kalite Kaydı için Kayıt Görüntüleme Sekmesinde görüntülenir.)

**8-Departman (Çoklu Seçim) Tipli:** QDMS departman veri tabanından departman bilgisi çoklu-tekli seçim seçilebilmesini sağlayan parametrik alandır. Sistem Altyapı Tanımları\>BSAT\>Tanımlar\>Departman Tanımlama menüsünde tanımlı departman listesinden departman bilgisinin seçimi yapılır. Örnek Kısa Kod: lblKK_DMPARAM1 (Kalite Kaydı için Kayıt Görüntüleme Sekmesinde görüntülenir.)

**9**-**Parasal Tipli:** Parasal olarak veri girişi yaptıran parametrik alandır.Tanımlanan parametrik alanın yanında para birimleri seçildiği alan çıkar. Para birimleri seçim alanındaki para birimleri Sistem Altyapı Tanımları\>BSAT\>Tanımlar\>Para Birimleri Tanımlama menüsünde tanımlı olan para birimleridir. Örnek Kısa Kod: lblKK_NPARAM1 (Kalite Kaydı için Kayıt Görüntüleme Sekmesinde görüntülenir.)

**10- Ölçü Birimi Tipli:** Ölçü olarak veri girişi yaptıran parametrik alandır. Tanımlanan parametrik alanın yanında Ölçü birimleri seçildiği alan çıkar. Ölçü birimleri seçim alanındaki ölçü Birimleri Sistem Altyapı Tanımları\>BSAT\>Tanımlar\>Ölçü Birimleri Tanımlama menüsünde tanımlı olan ölçü birimleridir. Örnek Kısa Kod: lblKK_NPARAM6 (Kalite Kaydı için Kayıt Görüntüleme Sekmesinde görüntülenir.)

#### **1.1.1.1.1.Doküman Yönetimi Modülünde Doküman İçin Diğer Bilgiler Sekmesinde Parametrik Alan Tanımlama**

### **1.1.1.1.1.1.Tarih Tipli Parametrik Alanların Listesi**

Doküman Yönetimi Modülünde Entegre Yönetim Sistemi\>Doküman İşlemleri\> Doküman Hazırlama menüsünde Diğer Bilgiler sekmesinde Tarih tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Tarih yazarak Tarih tipli parametrik alanlar aratılır ve Tarih tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen tarih tipli parametrik alanlara alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd38cd077-0343-473e-a134-accbf0821307)

### **1.1.1.1.1.2. Tarih Tipli Parametrik Alan Tanımlama.**

lblDALAN1 Tarih tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload06837354-764b-4943-b552-401929d4eb60) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7bd308cd-5268-4f3f-a833-9648f4b6a472)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2fc95fae-f546-45da-8673-f9a9a7499cfb)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1e3d9e46-d2d2-4af0-b674-2fef334a7cfe)(Kaydet) butonu tıklanarak tarih tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3ecf0b1c-4956-4234-a137-c400b3ed25ba)

Tanımlanan Tarih tipli parametik alan olan Gözden Geçirme Tarihi alanı Entegre Yönetim Sistemi/Doküman İşlemleri/Doküman Hazırlama menüsünde Diğer Bilgiler Sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9e53b1a6-1546-4c96-9025-958bfb829301)

### **1.1.1.1.1.3.Liste Tipli Parametrik Alanların Listesi**

Doküman Yönetimi Modülünde Entegre Yönetim Sistemi\>Doküman İşlemleri\> Doküman Hazırlama menüsünde Diğer Bilgiler sekmesinde Liste tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına liste yazarak liste tipli parametrik alanlar aratılır ve liste tipli parametrik alanların listesi Dil Ayarları menüsünde listenir. Listenen liste tipli parametrik alanlara alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2f63fbc4-1c92-42f4-9e20-dbe90f93ebff)

### **1.1.1.1.1.4.Liste Tipli Parametrik Alan Tanımlama.**

lblALAN10 Liste tipli parametrik seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload06837354-764b-4943-b552-401929d4eb60) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7244905e-b726-4764-9a4e-7ccb8433cd70)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada1961a9e-e5ee-4cd0-b254-27ab33ca93c7)

Liste tipli alanın liste değerlerini girmek için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbbbf0474-b1d4-4ffc-bfca-eeb97160f723) (Yeni) butonuna tıklanır, liste değerleri yazılır ve kaydedilir.

Liste değeri 1 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd668bf22-ef73-422d-9da5-9ca2e8043781)

Liste değeri 2 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8f5c3a82-783a-4956-9f4f-d0e8a69509a1)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9256e060-fd40-4b98-8c01-156192d84743)

Alanın zorunlu olup, olmayacağı sıra no bilgisi ve liste elemanları tanımlanarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1e3d9e46-d2d2-4af0-b674-2fef334a7cfe)(kaydet) butonu tıklanarak liste tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaa61d3bf-7948-406d-a697-a79c3b0d9a0c)

Entegre Yönetim Sistemi/Doküman İşlemleri/Doküman Hazırlama menüsünde Diğer alanlar sekmesinde tanımladığımız liste tipli parametrik alan olan Doküman Türü alanı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcab463f4-718c-4a32-a8c8-b752c4189905)

### **1.1.1.1.1.5. Personel Tipli Parametrik Alanların Listesi**

Doküman Yönetimi Modülünde Entegre Yönetim Sistemi\>Doküman İşlemleri\> Doküman Hazırlama menüsünde Diğer Bilgiler sekmesinde Personel tipli bir alan parametrik tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Personel yazarak Personel tipli parametrik alanlar aratılır ve Personel tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Personel tipli parametrik alanlara alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload75021cd7-ec64-4e75-8622-e3f84ec86706)

### **1.1.1.1.1.6. Personel Tipli Parametrik Alan Tanımlama.**

lblPALAN1 Personel tipli parametrik alan seçilerek alanın veri girişi için alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload06837354-764b-4943-b552-401929d4eb60) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd246295c-e14b-487e-9bb0-2cbdca6f2f3f)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada11920a8-6c8c-41be-9cd3-80eeeb5e4c70)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1e3d9e46-d2d2-4af0-b674-2fef334a7cfe)(kaydet) butonu tıklanarak Personel tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2bea86de-0f85-42a8-906f-c37fcccdbe9e)

Entegre Yönetim Sistemi/Doküman İşlemleri/Doküman Hazırlama menüsünde Diğer alanlar sekmesinde tanımladığımız Personel tipli parametrik alan olan Doküman Sorumlu alan görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6c7774dc-185a-45e5-89fd-bd69e2ca7f07)

Doküman sorumlusu personel tipli parametrik alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaded3a0ae3-8111-476a-b745-1dca2a4c9eb7)(seç) butonu tıklanıldığında sistemde tanımlı personel listesinde seçim yapılması sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload24d966f1-ac01-477c-82ae-e7cdc9cecc17)

### **1.1.1.1.1.7. Sorgu Tipli Parametrik Alanların Listesi**

Doküman Yönetimi Modülünde Entegre Yönetim Sistemi\>Doküman İşlemleri\> Doküman Hazırlama menüsünde Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Sorgu yazarak sorgu tipli parametrik alanlar listesi aratılır ve Sorgu tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen sorgu tipli parametrik alanlara alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload05543188-3c20-49e9-a459-0e4a56975f93)

Sistemde tanımlı olan sorgu tipinin içeriği ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload06837354-764b-4943-b552-401929d4eb60)(Değiştir) butonu tıklanarak içeriği görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf643495e-b709-4493-9a97-b47e424a7150)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload64d0aa56-5199-4666-be49-51d0cd73d2bd)

Entegre Yönetim Sistemi/Doküman İşlemleri/Doküman Hazırlama menüsünde Diğer alanlar sekmesinde tanımladığımız Sorgu tipli parametrik alan görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload69c696df-e45d-462e-a211-6d52138c128a)

### **1.1.1.1.1.8. Metin Tipli Parametrik Alanların Listesi**

Doküman Yönetimi Modülünde Entegre Yönetim Sistemi\>Doküman İşlemleri\> Doküman Hazırlama menüsünde Diğer Bilgiler sekmesinde Metin tipli bir alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Metin yazarak Metin tipli parametrik alanlar aratılır ve Metin tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen metin tipli parametrik alanlara alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload229ea05a-823f-41aa-a231-2d56fbfdf6c0)

### **1.1.1.1.1.9. Metin Tipli Parametrik Alan Tanımlama**

lblALAN2 Metin tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload06837354-764b-4943-b552-401929d4eb60) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada0b40016-3dec-4910-8d3e-df277e4aa735)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload49a34a5c-2b32-443b-ab4b-5468ac8cf453)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1e3d9e46-d2d2-4af0-b674-2fef334a7cfe)(kaydet) butonu tıklanarak Metin tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload515bec2e-a9aa-41d2-8113-55884f29fc76)

Entegre Yönetim Sistemi/Doküman İşlemleri/Doküman Hazırlama menüsünde Diğer alanlar sekmesinde tanımladığımız Metin tipli parametrik alan olan Doküman Açıklaması alan görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade2368ac0-ee93-4a7f-8ee1-68d2de3c8f56)

### **1.1.1.1.1.10. Metin (Çoklu Satır) Tipli Parametrik Alanların Listesi**

Doküman Yönetimi Modülünde Entegre Yönetim Sistemi\>Doküman İşlemleri\> Doküman Hazırlama menüsünde Diğer Bilgiler sekmesinde Metin (Çoklu Satır) tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip Metin (Çoklu Satır) alanına yazarak Metin (Çoklu Satır) tipli parametrik alanlar aratılır ve Metin (Çoklu Satır) tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Metin (Çoklu Satır) tipli parametrik alanlara alan tanımlaması yapılır.

**![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf880ed52-5042-44be-8486-59d1fbab6377)**

### **1.1.1.1.1.11.Metin (Çoklu Satır) Tipli Parametrik Alan Tanımlama**

lblMALAN1 Metin (Çoklu Satır) tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload06837354-764b-4943-b552-401929d4eb60) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6caf1635-19e5-42e9-bcd9-7e6df89c3640)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload249bd69c-f78e-4385-9fe6-4ac674bb9ef4)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1e3d9e46-d2d2-4af0-b674-2fef334a7cfe)(kaydet) butonu tıklanarak Metin (Çoklu Satır) tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8ee1f6a8-2fed-439f-ad12-8a646ffedc0a)

Entegre Yönetim Sistemi/Doküman İşlemleri/Doküman Hazırlama menüsünde Diğer alanlar sekmesinde tanımladığımız Metin (Çoklu Satır) parametrik alan olan Doküman Detayı alanı görüntülenir. Doküman için Tanımlanan tüm Parametrik tipli alanları Doküman Hazırlama/Diğer Bilgiler sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd875be36-01e6-4688-b1e6-7eb8bbfeb6ad)

#### **1.1.1.1.2. Doküman Yönetimi Modülünde Kalite Kaydı İçin Kayıt Görüntüleme Sekmesinde Parametrik Alan Tanımlama**

### **1.1.1.1.2.1.Metin Tipli Parametrik Alanlar Listesi**

Doküman Yönetimi Modülünde Kalite Kaydı/Kayıt Görüntüleme sekmesinde Metin tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Metin yazarak Metin tipli parametrik alanlar aratılır ve Metin tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen metin tipli parametrik alanlara alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload253a7841-8101-4652-a13e-6bedce199f5e)

### **1.1.1.1.2.2.Metin Tipli Parametrik Alan Tanımlama.**

lblKK_PARAM1 Metin tipli parametrik alanı seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload06837354-764b-4943-b552-401929d4eb60) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadafcc5671-4287-4ec4-90b1-26e1d54a4ffc)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload341ed6a2-a6d8-4f2f-b17c-a512e27cdc92)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1e3d9e46-d2d2-4af0-b674-2fef334a7cfe)(Kaydet) butonu tıklanarak metin tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadad100b65-6a8e-4bc7-b794-7a5f2163a662)

Kalite Kaydı için tanımlanan metin tipli tipli parametrik alan Kalite Kaydı Açıklaması alanı Kalite Kaydı\> Kayıt Görüntüleme sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfae69cd8-0068-4ccc-83b6-5ade3a146809)

### **1.1.1.1.2.3.Metin (Çoklu Satır) Parametrik Alanlar Listesi**

Doküman Yönetimi Modülünde Kalite Kaydı/Kayıt Görüntüleme sekmesinde Metin (Çoklu Satır**)** tipli bir alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Metin (Çoklu Satır) yazarak Metin (Çoklu Satır) tipli parametrik alanlar aratılır ve Metin (Çoklu Satır) tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Metin (Çoklu Satır) tipli parametrik alanlara alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc88566d1-8d38-43eb-877e-896107812e1d)

### **1.1.1.1.2.4.Metin (Çoklu Satır) Tipli Parametrik Alan Tanımlama**

lblKK_PARAM9 Metin (Çoklu Satır) tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload06837354-764b-4943-b552-401929d4eb60) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadde6e8fdd-7612-46ac-9a7f-915adecef6c3)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload95cc55e9-a41c-492c-bc73-265e4508db8b)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1e3d9e46-d2d2-4af0-b674-2fef334a7cfe)(kaydet) butonu tıklanarak Metin (Çoklu Satır) tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload45a380b4-0be5-46b2-a62d-9a0aa2b406fa)

Kalite Kaydı için tanımlanan Metin (Çoklu Satır) tipli parametrik alan olan Kalite Kaydı Detayı Kalite Kaydı\> Kayıt Görüntüleme sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf966b1c7-4c94-440c-9052-21628607f352)

### **1.1.1.1.2.5. Liste Tipli Parametrik Alanların Listesi**

Doküman Yönetimi Modülünde Kalite Kaydı/Kayıt Görüntüleme sekmesinde Liste tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Liste yazarak liste tipli parametrik alanlar aratılır ve liste tipli parametrik alanların listesi Dil ayarları menüsünde listelenir. Listenen Liste tipli parametrik alanlara alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload98be6859-d1c4-4571-b566-54dffc47e39c)

### **1.1.1.1.2.6. Liste Tipli Parametrik Alan Tanımlama**

lblKK_LPARAM1 Liste tipli alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload06837354-764b-4943-b552-401929d4eb60) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada1243f87-4c3e-45a6-9ce5-d0ecfc950d40)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9a208a37-56d8-49a8-8a22-d9ce83e4ba10)

Liste tipli alanın liste değerlerini girmek için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbbbf0474-b1d4-4ffc-bfca-eeb97160f723) (Yeni) butonuna tıklanır, liste değerleri yazılır ve kaydedilir.

Liste değeri 1 için liste elemanı tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf7909f89-6a48-463c-bcb9-4337be8ce1d8)

Liste değeri 2 için liste elemanı tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4a23d8bb-e3e9-4ec4-af8e-2807b495e385)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4f6e07bc-78ab-4b09-a1e8-c18dcfd9f4f5)

Alanın zorunlu olup, olmayacağı sıra no bilgisi ve liste elemanların tanımlanarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1e3d9e46-d2d2-4af0-b674-2fef334a7cfe)(kaydet) butonu tıklanarak liste tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadae200163-5209-4c10-b03b-a43e639ff690)

Kalite Kaydı için tanımlanan liste tipli parametrik alan olan Kalite Kaydı Türü alanı Kalite Kaydı\> Kayıt Görüntüleme sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf496f6c0-fe13-455a-bf9c-34b8afd387c4)

### **1.1.1.1.2.7. Tarih Tipli Parametrik Alanların Listesi**

Doküman Yönetimi Modülünde Kalite Kaydı/Kayıt görüntüleme sekmesinde Tarih tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Tarih yazarak Tarih tipli parametrik alanlar aratılır ve Tarih tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen tarih tipli parametrik alanlara alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload76f2a1df-e633-4a81-8f2d-5e51262f28dc)

### **1.1.1.1.2.8. Tarih Tipli Parametrik Alan Tanımlama**

lblKK_DPARAM1 Tarih tipli parametrik alanı seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload06837354-764b-4943-b552-401929d4eb60) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload53eaeb54-500f-4553-8de0-6dae5270a20f)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7d86d091-e8e8-46cf-823f-70e2433e3e4f)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1e3d9e46-d2d2-4af0-b674-2fef334a7cfe)(kaydet) butonu tıklanarak tarih tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadafb51635-aa85-4cec-8136-03dfd12af586)

Kalite Kaydı için tanımlanan tarih tipli parametrik alan olan Gözden Geçierme Tarihi alanı Kalite Kaydı\> Kayıt Görüntüleme sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3d3ba4e7-6d9a-4502-a9be-663eb4a69fdf)

### **1.1.1.1.2.9.Departman Tipli Parametrik Alanların Listesi**

Doküman Yönetimi Modülünde Kalite Kaydı/Kayıt Görüntüleme sekmesinde Departman tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Departman yazarak Departman tipli parametrik alanlar aratılır ve Departman tipli parametrik alanların listesi Dil ayarları menüsünde listelenir. Listenen Departman tipli parametrik alanlara alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload19cebbd8-3780-4367-a802-5bf2ac1eb1cc)

### **1.1.1.1.2.10. Departman Tipli Parametrik Alan Tanımlama**

lblKK_DSPARAM1 Departman tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload06837354-764b-4943-b552-401929d4eb60) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8a409fb4-6408-41f5-b731-94db7d3dfbf7)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload625edb2a-1984-4996-9999-44a3b2146237)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1e3d9e46-d2d2-4af0-b674-2fef334a7cfe)(kaydet) butonu tıklanarak Departman tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade06dc2e9-4ee1-4ab8-b289-4b0a79e84822)

Kalite Kaydı için tanımlanan Departman tipli parametrik alan Departman alanı Kalite Kaydı\> Kayıt Görüntüleme sekmesinde görüntülenir.

.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload45870030-acc9-4ff9-9e83-ca6d3279d05c)

Dil ayarlarında tanımlanan Departman tipli alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload539bd9b9-0e55-4f0f-9787-a4cc3e7959bc)(seç) butonu tıklanıldığında sistemde tanımlı departman listesine ulaşılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload25eb3eba-779f-4fd1-b23f-7d849dfd3cb1)

### **1.1.1.1.2.11.Departman (Çoklu Seçim)  Tipli Parametrik Alan Listesi**

Doküman Yönetimi Modülünde Kalite Kaydı/Kayıt Görüntüleme sekmesinde Departman (Çoklu Seçim) tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Departman (Çoklu Seçim)  yazarak Departman (Çoklu Seçim**)** tipli parametrik alanlar aratılır ve Departman(Çoklu Seçim) parametrik tipli parametrik alanların listesi Dil ayarları menüsünde listelenir. Listenen Departman(Çoklu Seçim) tipli parametrik alanlara alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload48a59562-2505-4917-9c79-ea4c229b9999)

### **1.1.1.1.2.12. Departman (Çoklu Seçim)  Tipli Parametrik Alan Tanımlama**

lblKK_DMPARAM1 Departman (Çoklu Seçim) tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload06837354-764b-4943-b552-401929d4eb60) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbc5e053a-bcec-4715-9500-0fde7ae5f281)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5cb729b6-1e79-41a3-93d8-53fb6eb917a6)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1e3d9e46-d2d2-4af0-b674-2fef334a7cfe)(kaydet) butonu tıklanarak Departman (Çoklu Seçim) tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload86e3fdf6-8030-4cb5-af0b-680a1d45f964)

Kalite Kaydı için tanımlanan Departman (Çoklu Seçim) tipli parametrik alan olan ilgili Departmanlar Kalite Kaydı\> Kayıt Görüntüleme sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadddbb1f93-c2f5-400d-8394-9960f2752b7f)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddf04d816-6d31-4fda-9b91-ed4bfabf5eff)

Dil ayarlarında tanımlanan Departman (Çoklu Seçim) alanda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0b7ad5ef-b2dd-4c8f-9448-d394be346733)(ekle) butonu tıklanıldığında sistemde tanımlı departman listesinden tekli ve çoklu seçim yapılır.

### **1.1.1.1.2.13. Ölçü Birimi Parametrik Alanların Listesi**

Doküman Yönetimi Modülünde Kalite Kaydı/Kayıt Görüntüleme sekmesinde Ölçü Birimi tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Ölçü Birimi yazarak Ölçü Birimi tipli parametrik alanlar aratılır ve ölçü birimi parametrik tipli alanların listesi Dil ayarları menüsünde listelenir. Listenen ölçü birimi tipli parametrik alanlara alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc0362c91-7862-4f5b-987d-2516922f0a45)

### **1.1.1.1.2.14. Ölçü Birimi Parametrik Alan Tanımlama**

lblKK_NPARAM6 Ölçü birimi tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload06837354-764b-4943-b552-401929d4eb60) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3b22f3d2-edc6-4c3c-a398-9f574b638a79)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload576a38e2-e5b2-45d5-966f-f6c6eccd0c74)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1e3d9e46-d2d2-4af0-b674-2fef334a7cfe)(Kaydet) butonu tıklanarak ölçü birimi tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd680acd7-a59b-4440-a701-1dd0a55adee6)

Kalite Kaydı için tanımlanan ölçü Birimi tipli parametrik alan olan Ölçü birimi Kalite Kaydı\> Kayıt Görüntüleme sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd432f23b-466d-48ed-95d3-74da0f64e116)

### **1.1.1.1.2.15. Parasal Tipli Parametrik Alanların Listesi**

Doküman Yönetimi Modülünde Kalite Kaydı/Kayıt Görüntüleme Parasal tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Parasal yazarak liste tipli parametrik alanlar aratılır ve Parasal tipli parametrik alanların listesi Dil ayarları menüsünde listelenir. Listenen Parasal tipli parametrik alanlara alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8cf71629-89c6-4882-b93e-1d66463ee8b3)

### **1.1.1.1.2.16. Parasal Tipli Parametrik Alan Tanımlama**

lblKK_NPARAM1 Parasal tipli alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload06837354-764b-4943-b552-401929d4eb60) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload17eb04a8-965a-4bfd-93c4-5c91cfaca181)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc4e9bef8-f313-476a-8f5f-7789e2cbdf14)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1e3d9e46-d2d2-4af0-b674-2fef334a7cfe)(Kaydet ) butonu tıklanarak Parasal tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3b10f8a4-bf06-4a66-83ff-0104a81469fc)

Kalite Kaydı için tanımlanan Parasal tipli parametrik alan olan Tutar alanı Kalite Kaydı\> Kayıt Görüntüleme sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4fb93516-0d47-4197-a7fa-8c8c28cd1b07)

Kalite Kaydı için Tanımlanan tüm Parametrik tipli alanları Kalite Kaydı \>Kayıt Görüntüleme sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload46c82e47-0ebf-430c-ae8a-907aae1252a7)
