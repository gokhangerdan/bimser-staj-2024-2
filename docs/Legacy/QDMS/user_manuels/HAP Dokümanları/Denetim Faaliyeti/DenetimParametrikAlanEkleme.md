---
title: Parametrik Alan Tanımlama İşlemi
description: Parametrik Alan Tanımlama İşlemi Yardım Dokümanı
sidebar_position: 1
---

:::tip Bilgi

İlgili konu başlığına sağ tarafta bulunan navigasyon yardımıyla hızlı bir şekilde ulaşabilirsiniz.

:::

**Denetim Faaliyeti Modülünde Dil Ayarları Menüsünde Parametrik Alan Tanımlama Kullanıcı Yardım Dokümanı**

## **1.Sistem Altyapı Tanımları**

Personel bilgilerinin tanımlandığı ve diğer modüller için gerekli olan altyapının kurgulanmasının yapıldığı menüdür.

## **1.1.Konfigürasyon Ayarları**


**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları

QDMS sisteminde özel ayarların yapıldığı menülerdir. Bu menülerde yapılan ayarlar tüm QDMS kullanıcıları için geçerli olan ortak ayarlardır.

### **1.1.1. Dil Ayarları**

**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları

Dil ayarları menüsünden QDMS üzerinde görülen menülerin isimleri, alanların isimleri değiştirilebilir. Modüllere yeni alanlar eklenebilir. Var olan alanların zorunluluk durumları düzenlenebilir. Alanların ekran üzerinde göründükleri sıralama değiştirilebilir.

### **1.1.1.1. Denetim Faaliyeti Modülü Ortak Kullanım İçin Yeni Alan Oluşturma**

Denetim Faaliyeti Modülünde için Denetim Planları menüsünde Denetim Planları-Denetimler-Yeni Kayıt ekranında , Bekleyen Denetimler ve Plansız Denetimler menülerinde bulunan Diğer Bilgiler-Bulgular sekmeleri ekranında firmanın istemiş olduğu sistemde olmayan ekstradan alanlar tanımlanabilir. Tanımlanan bu alanlar tüm Denetim Faaliyetleri Modül kaynakları için geçerlidir. Sistem Altyapı Tanımları/BSAT/ Konfigürasyon Ayarları/Dil Ayarları menüsü tıklanılır. Açılan Dil Ayarları sayfasında Modül alanında “Denetim Faaliyeti” seçilir ve ekranda Denetim Faaliyeti ile ilgili dil tanımları görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload10f71449-3ac7-4323-a037-7972f9e6d3d1)

Denetim Faaliyetleri Modülünde Entegre Yönetim Sistemi\>Denetim Faaliyeti\>Bekleyen Denetimler menüsünde Denetim gerçekleştir butonu tıklanıldığında diğer bilgiler sekmesinde ve Bulgular sekmesinde Yeni butonu tıklatıldığında bulgu tanımlama ekranında Dil ayarlarından parametrik alan tanımlaması yapılmaktadır. Entegre Yönetim Sistemi\>Denetim Faaliyeti\>Plansız Denetimler ileri butonu tıklatıldığında Denetim Gerçekleştir- Kayıt güncelleme Diğer bilgiler sekmesi ve Bulgular sekmesinde Yeni butonu tıklatıldığında bulgu tanımlama menüsünde Dil ayarlarından parametrik alan tanımlaması da yapılmaktadır. Ayrıca Dil ayarlarında yapılan parametrik alan tanımlamaları Entegre Yönetim Sistemi\>Denetim Faaliyeti\>Denetim Planları menüsünde Denetimler butonu tıklanıldığında açılan Denetim Planları-Denetimler ekranında Yeni butonu tıklanıldığında açılan Denetim Planları-Denetimler-Yeni Kayıt ekranında parametrik alanlar görüntülenip bu ekran için de parametrik alan tanımlamları yapılmaktadır. Kısaca Denetim Faaliyetleri Modülünde Bekleyen Denetimler, Plansız Denetimler için Diğer bilgiler ve Bulgu sekmelerinde, Denetim Planları menüsünde Denetimler -Yeni Kayıt ekranlarıda dil ayarlarında parametrik alan tipi tanımlamaları yapılmaktadır. Yapılan dil ayarlarında tanımlama menüler için ortak kullanımı sağlamaktadır.

**Denetim Faaliyeti Modülünde Tanımlanan Parametrik Tipli Alanlar ve Tanımları;**

**1-Tarih tipli**: Takvim alanı eklenilen parametrik alandır. Örnek Kısa Kod: lblD_DPARAM1(Bekleyen Denetimler -Plansız Denetimler menülerinin Denetim Gerçekleştir- Kayıt Güncelle ekranında Diğer bilgiler sekmesinde ve Denetim Planları menüsünde Denetim Planları-Denetimler-Yeni Kayıt ekranında görüntülenir.), lblB_DPARAM1(Bekleyen Denetimler ve Plansız Denetimler menülerinde Denetim Gerçekleştir- Kayıt Güncelle ekranında Bulgular sekmesinde Yeni butonu tıklanarak açılan Bulgu Tanımlama ekranında görüntülenir)

**2-Liste tipli**: Birden fazla liste elemanları arasından tek seçim yapılan parametrik alandır. Liste elemanları tanımlanarak, tanımlanan liste elemanlarında seçip yapılır. Örnek Kısa Kod: lblD_LPARAM1 (Bekleyen Denetimler -Plansız Denetimler menülerinin Denetim Gerçekleştir- Kayıt Güncelle ekranında Diğer bilgiler sekmesinde ve Denetim Planları menüsünde Denetim Planları-Denetimler-Yeni Kayıt ekranında görüntülenir.), lblL_LPARAM1(Bekleyen Denetimler ve Plansız Denetimler menülerinde Denetim Gerçekleştir- Kayıt Güncelle ekranında Bulgular sekmesinde Yeni butonu tıklanarak açılan Bulgu Tanımlama ekranında görüntülenir.)

**3-Metin tipli**: Elle yazım imkanı veren metin kutucuğu ekleyen parametrik alandır. Örnek Kısa Kod: lblD_PARAM3 (Bekleyen Denetimler -Plansız Denetimler menülerinin Denetim Gerçekleştir- Kayıt Güncelle ekranında Diğer bilgiler sekmesinde ve Denetim Planları menüsünde Denetim Planları-Denetimler-Yeni Kayıt ekranında görüntülenir.), lblT_TPARAM1(Bekleyen Denetimler ve Plansız Denetimler menülerinde Denetim Gerçekleştir- Kayıt Güncelle ekranında Bulgular sekmesinde Yeni butonu tıklanarak açılan Bulgu Tanımlama ekranında görüntülenir.)

**4-Metin (Çoklu Satır)Tipli** : Elle yazım imkanı veren karakter sınırı olmayan çok satırlı metin kutucuğu eklenen parametrik alandır. Örnek Kısa Kod: lblD_PARAM1(Bekleyen Denetimler -Plansız Denetimler menülerinin Denetim Gerçekleştir- Kayıt Güncelle ekranında Diğer bilgiler sekmesinde ve Denetim Planları menüsünde Denetim Planları-Denetimler-Yeni Kayıt ekranında görüntülenir.), lblT_TPARAM4 (Bekleyen Denetimler ve Plansız Denetimler menülerinde Denetim Gerçekleştir- Kayıt Güncelle ekranında Bulgular sekmesinde Yeni butonu tıklanarak açılan Bulgu Tanımlama ekranında görüntülenir.)

**5- Ölçü Birimi Tipli:** Ölçü olarak veri girişi yaptıran parametrik alandır. Tanımlanan parametrik alanın yanında Ölçü birimleri seçildiği alan çıkar. Ölçü birimleri seçim alanındaki ölçü Birimleri Sistem Altyapı Tanımları\>BSAT\>Tanımlar\>Ölçü Birimleri Tanımlama menüsünde tanımlı olan ölçü birimleridir. Örnek Kısa Kod: lblD_NPARAM1(Bekleyen Denetimler -Plansız Denetimler menülerinin Denetim Gerçekleştir- Kayıt Güncelle ekranında Diğer bilgiler sekmesinde ve Denetim Planları menüsünde Denetim Planları-Denetimler-Yeni Kayıt ekranında görüntülenir.), lblB_NPARAM1(Bekleyen Denetimler ve Plansız Denetimler menülerinde Denetim Gerçekleştir- Kayıt Güncelle ekranında Bulgular sekmesinde Yeni butonu tıklanarak açılan Bulgu Tanımlama ekranında görüntülenir.)

**6**-**Parasal Tipli:** Parasal olarak veri girişi yaptıran parametrik alandır.Tanımlanan parametrik alanın yanında para birimleri seçildiği alan çıkar. Para birimleri seçim alanındaki para birimleri Sistem Altyapı Tanımları\>BSAT\>Tanımlar\>Para Birimleri Tanımlama menüsünde tanımlı olan para birimleridir. Örnek Kısa Kod: lblD_NPARAM4 (Bekleyen Denetimler -Plansız Denetimler menülerinin Denetim Gerçekleştir- Kayıt Güncelle ekranında Diğer bilgiler sekmesinde ve Denetim Planları menüsünde Denetim Planları-Denetimler-Yeni Kayıt ekranında görüntülenir.), lblB_NPARAM4 (Bekleyen Denetimler ve Plansız Denetimler menülerinde Denetim Gerçekleştir- Kayıt Güncelle ekranında Bulgular sekmesinde Yeni butonu tıklanarak açılan Bulgu Tanımlama ekranında görüntülenir.)

### **1.1.1.1.1. Denetim Faaliyet Modülünde Bekleyen Denetimler-Plansız Denetimler (Diğer Bilgiler Sekmesi) ve Denetim Planları Menülerinde Parametrik Alan Tanımlama**

### **1.1.1.1.1.1.Tarih Tipli Parametrik Alanların Listesi**

Denetim Faaliyetleri Modülünde Bekleyen Denetimler -Plansız Denetimler menülerinin Denetim Gerçekleştir- Kayıt güncelleme ekranında Diğer bilgiler sekmesi ve Denetim Planları menüsünde Denetim Planları-Denetimler-Yeni Kayıt ekranında Tarih tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Tarih yazarak Tarih tipli parametrik alanlar aratılır ve Tarih tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen tarih tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb989b133-b1d4-4d5b-9705-08cf52e7b844)

### **1.1.1.1.1.2. Tarih Tipli Parametrik Alan Tanımlama**

lblD_DPARAM1 Tarih tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload18b1e179-380c-4af6-90c2-e5f6c9c33b2a) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb3dc04b3-8843-4400-bcb5-3e0a008feb9b)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload356238af-7aea-4a7b-85b2-0094911f7e7d)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload79bd4f84-d3ff-41f7-8f61-e774f9e4827a)(Kaydet) butonu tıklanarak tarih tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf0dbeda2-d871-4005-9c88-a369095c8463)

Tanımlanan Tarih tipli parametrik alan Entegre Yönetim Sistemi\>Denetim Faaliyeti\>Bekleyen Denetimler menüsünde Denetim Gerçekleştir butonu tıklanarak açılan Denetim Gerçekleştir-Kayıt Güncelle ekranında Diğer Bilgiler sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3a4640d2-a011-4504-99ad-d482c565f75b)

Tanımlanan Tarih tipli parametrik alan Entegre Yönetim Sistemi\>Denetim Faaliyeti\>Plansız Denetimler menüsünde İleri butonu tıklanarak açılan Denetim Gerçekleştir- Kayıt Güncelle ekranında Diğer bilgiler sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload35401f83-c364-43d7-85a9-fd667f19ba25)

Tanımlanan Tarih tipli parametrik alan Entegre Yönetim Sistemi\>Denetim Faaliyeti\>Denetim Planları menüsünde Denetim Planları-Denetimler-Yeni Kayıt ekranında görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc1e49700-879c-4b3a-8e55-db8887d0dadd)

### **1.1.1.1.1.3.Liste Tipli Parametrik Alanların Listesi**

Denetim Faaliyetleri Modülünde Bekleyen Denetimler -Plansız Denetimler menülerinin Denetim Gerçekleştir- Kayıt güncelleme ekranında Diğer bilgiler sekmesi ve Denetim Planları menüsünde Denetim Planları-Denetimler-Yeni Kayıt ekranında Liste tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Liste yazarak Liste tipli parametrik alanlar aratılır ve Liste tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Liste tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3ad76f2c-8760-43bf-a738-485005a5f2dc)

### **1.1.1.1.1.4.Liste Tipli Parametrik Alan Tanımlama.**

lblD_LPARAM1 Liste tipli parametrik seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload18b1e179-380c-4af6-90c2-e5f6c9c33b2a) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload65ccab69-66b7-431c-a1b9-27c05f0618be)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5803b13d-d004-4685-8e07-521707213e01)

Liste tipli alanın liste değerlerini girmek için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3da03dd1-2d83-45ab-91ff-df493b3de3ea) (Yeni) butonuna tıklanır, liste değerleri yazılır ve kaydedilir. Liste eleman değeri 1 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload888f2e6e-0349-41d7-a051-42f89b833022)

Liste eleman değeri 2 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4f6ec4d3-f95b-4beb-ad32-9bca939d7f9b)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload508f2441-a43b-4524-a674-db4d102ac969)

Alanın zorunlu olup, olmayacağı sıra no bilgisi ve liste elemanları tanımlanarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload79bd4f84-d3ff-41f7-8f61-e774f9e4827a)(kaydet) butonu tıklanarak liste tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1daaef5d-96d5-44b2-a481-107a27a75a43)

Tanımlanan Liste tipli parametrik alan Entegre Yönetim Sistemi\>Denetim Faaliyeti\>Bekleyen Denetimler menüsünde Denetim Gerçekleştir butonu tıklanarak açılan Denetim Gerçekleştir-Kayıt Güncelle ekranında Diğer Bilgiler sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfe8404ec-0fe9-4795-9bc2-79275c24f9fd)

Tanımlanan Liste tipli parametrik alan Entegre Yönetim Sistemi\>Denetim Faaliyeti\>Plansız Denetimler menüsünde İleri butonu tıklanarak açılan Denetim Gerçekleştir- Kayıt Güncelle ekranında Diğer bilgiler sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4d5b637d-f966-4ec1-bb06-d8c19c7f2e21)

Tanımlanan Liste tipli parametrik alan Entegre Yönetim Sistemi\>Denetim Faaliyeti\>Denetim Planları menüsünde Denetim Planları-Denetimler-Yeni Kayıt ekranında görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd59b17a6-1cdd-4794-8335-1a5202cad229)

### **1.1.1.1.1.5.Metin Tipli Parametrik Alanların Listesi**

Denetim Faaliyetleri Modülünde Bekleyen Denetimler -Plansız Denetimler menülerinin Denetim Gerçekleştir- Kayıt güncelleme ekranında Diğer bilgiler sekmesi ve Denetim Planları menüsünde Denetim Planları-Denetimler-Yeni Kayıt ekranında Metin tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Metin yazarak Metin tipli parametrik alanlar aratılır ve Metin tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Metin tipli parametrik alanların alan tanımlaması yapılır.

### **1.1.1.1.1.6. Metin Tipli Parametrik Alan Tanımlama**

lblD_PARAM3 Metin tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload18b1e179-380c-4af6-90c2-e5f6c9c33b2a) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4fea3425-9570-4dd6-af9c-f12f7e502530)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadebf407d8-051b-4882-a2a9-82d170e89346)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload79bd4f84-d3ff-41f7-8f61-e774f9e4827a)(kaydet) butonu tıklanarak Metin tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd2b4f69e-5f91-445b-8257-c42fe3111e69)

Tanımlanan Metin tipli parametrik alan Entegre Yönetim Sistemi\>Denetim Faaliyeti\>Bekleyen Denetimler menüsünde Denetim Gerçekleştir butonu tıklanarak açılan Denetim Gerçekleştir-Kayıt Güncelle ekranında Diğer Bilgiler sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9be01ace-053d-4a42-9a54-8fb55648b504)

Tanımlanan Metin tipli parametrik alan Entegre Yönetim Sistemi\>Denetim Faaliyeti\>Plansız Denetimler menüsünde İleri butonu tıklanarak açılan Denetim Gerçekleştir- Kayıt Güncelle ekranında Diğer bilgiler sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1608d0b2-a8e7-418d-a2af-b693195df272)

Tanımlanan Metin tipli parametrik alan Entegre Yönetim Sistemi\>Denetim Faaliyeti\>Denetim Planları menüsünde Denetim Planları-Denetimler-Yeni Kayıt ekranında görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4af379d3-075b-4118-8eee-dca19a94daf2)

### **1.1.1.1.1.7.Metin (Çoklu Satır) Tipli Parametrik Alanların Listesi**

Denetim Faaliyetleri Modülünde Bekleyen Denetimler -Plansız Denetimler menülerinin Denetim Gerçekleştir- Kayıt güncelleme ekranında Diğer bilgiler sekmesi ve Denetim Planları menüsünde Denetim Planları-Denetimler-Yeni Kayıt ekranında Metin(Çoklu Satır) tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Metin(Çoklu Satır) yazarak Metin(Çoklu Satır) tipli parametrik alanlar aratılır ve Metin(Çoklu Satır) tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Metin(Çoklu Satır) tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload25bfa09c-aa02-42d4-a77d-702595056acd)

### **1.1.1.1.1.8.Metin (Çoklu Satır)** **Tipli Parametrik Alan Tanımlama**

lblD_PARAM1 Metin (Çoklu Satır) tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload18b1e179-380c-4af6-90c2-e5f6c9c33b2a) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadac29a059-bad3-4a22-821e-bb0b84f25ee1)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload48413dae-352d-4985-8e8a-af748f4822aa)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload79bd4f84-d3ff-41f7-8f61-e774f9e4827a)(kaydet) butonu tıklanarak Metin (Çoklu Satır) tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaac092e9-06c6-4f78-830d-471813e3003d)

Tanımlanan Metin(Çoklu Satır) tipli parametrik alan Entegre Yönetim Sistemi\>Denetim Faaliyeti\>Bekleyen Denetimler menüsünde Denetim Gerçekleştir butonu tıklanarak açılan Denetim Gerçekleştir-Kayıt Güncelle ekranında Diğer Bilgiler sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd07a809d-a1d2-4153-a867-ff5eb4b70550)

Tanımlanan Metin(Çoklu Satır) parametrik alan Entegre Yönetim Sistemi\>Denetim Faaliyeti\>Plansız Denetimler menüsünde İleri butonu tıklanarak açılan Denetim Gerçekleştir- Kayıt Güncelle ekranında Diğer bilgiler sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload70c9c344-55c5-4cbd-b8b5-d0a5e0f06fef)

Tanımlanan Metin(Çoklu Satır) parametrik alan Entegre Yönetim Sistemi\>Denetim Faaliyeti\>Denetim Planları menüsünde Denetim Planları-Denetimler-Yeni Kayıt ekranında görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0aefe84c-3d64-4a73-bf86-dd2baff4497c)

### **1.1.1.1.1.9.Ölçü Birimi Tipli Parametrik Alanların Listesi**

Denetim Faaliyetleri Modülünde Bekleyen Denetimler -Plansız Denetimler menülerinin Denetim Gerçekleştir- Kayıt güncelleme ekranında Diğer bilgiler sekmesi ve Denetim Planları menüsünde Denetim Planları-Denetimler-Yeni Kayıt ekranında Ölçü Birimi tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Ölçü Birimi yazarak Ölçü Birimi tipli parametrik alanlar aratılır ve Ölçü Birimi tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Ölçü Birimi tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload65a35936-79d9-4c0c-999c-dc3daa411eda)

### **1.1.1.1.1.10. Ölçü Birimi Tipli Parametrik Alan Tanımlama**

lblD_NPARAM1 Ölçü birimi tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload18b1e179-380c-4af6-90c2-e5f6c9c33b2a) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9b971280-a787-4db0-b2a6-4f132f5a3d71)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6b961ae9-ca31-4a92-9635-7b2970243a67)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload79bd4f84-d3ff-41f7-8f61-e774f9e4827a)(Kaydet) butonu tıklanarak ölçü birimi tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload51f900b6-7b55-4190-80c6-a40856d877ac)

Tanımlanan Ölçü Birimi tipli parametrik alan Entegre Yönetim Sistemi\>Denetim Faaliyeti\>Bekleyen Denetimler menüsünde Denetim Gerçekleştir butonu tıklanarak açılan Denetim Gerçekleştir-Kayıt Güncelle ekranında Diğer Bilgiler sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada272edaf-faec-46af-aaa5-52cff1e41c31)

Tanımlanan Ölçü Birimi tipli parametrik alan Entegre Yönetim Sistemi\>Denetim Faaliyeti\>Plansız Denetimler menüsünde İleri butonu tıklanarak açılan Denetim Gerçekleştir- Kayıt Güncelle ekranında Diğer bilgiler sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1a10aed4-9375-4776-82fd-cf2de52a5dbc)

Tanımlanan Ölçü Birimi tipli parametrik alan Entegre Yönetim Sistemi\>Denetim Faaliyeti\>Denetim Planları menüsünde Denetim Planları-Denetimler-Yeni Kayıt ekranında görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3a3ce34f-0793-4af5-85f5-b68153f58efe)

### **1.1.1.1.1.11.Parasal Tipli Parametrik Alanların Listesi**

Denetim Faaliyetleri Modülünde Bekleyen Denetimler -Plansız Denetimler menülerinin Denetim Gerçekleştir- Kayıt güncelleme ekranında Diğer bilgiler sekmesi ve Denetim Planları menüsünde Denetim Planları-Denetimler-Yeni Kayıt ekranında Parasal tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Parasal yazarak Parasal tipli parametrik alanlar aratılır ve Parasal  tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Parasal tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb7198019-66e4-494d-878e-9438dedd20ac)

### **1.1.1.1.1.12.Parasal Tipli Parametrik Alan Tanımlama**

lblD_NPARAM4 Parasal tipli alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload18b1e179-380c-4af6-90c2-e5f6c9c33b2a) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8d81a0d4-bfa2-4921-adff-90fb70aa6bcf)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade4c44afa-7d82-493b-8219-c68a49491918)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload79bd4f84-d3ff-41f7-8f61-e774f9e4827a)(Kaydet ) butonu tıklanarak Parasal tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload37e10d7b-165c-4759-9147-a43fd54850d6)

Tanımlanan Parasal tipli parametrik alan Entegre Yönetim Sistemi\>Denetim Faaliyeti\>Bekleyen Denetimler menüsünde Denetim Gerçekleştir butonu tıklanarak açılan Denetim Gerçekleştir-Kayıt Güncelle ekranında Diğer Bilgiler sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload623c5e2e-40d2-4eeb-830d-a18137df42f5)

Tanımlanan Parasal tipli parametrik alan Entegre Yönetim Sistemi\>Denetim Faaliyeti\>Plansız Denetimler menüsünde İleri butonu tıklanarak açılan Denetim Gerçekleştir- Kayıt Güncelle Diğer bilgiler sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7ceb5e85-8942-47ff-946e-344c0dcd2119)

Tanımlanan Parasal tipli parametrik alan Entegre Yönetim Sistemi\>Denetim Faaliyeti\>Denetim Planları menüsünde Denetim Planları-Denetimler-Yeni Kayıt ekranında görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc832ecdc-35e8-46c3-9863-5293a9b335ea)

Denetim Gerçekleştir-Kayıt Güncelleme ekranında Dil ayarlarından tanımlanan tüm Parametrik Tipli alanlar;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2401907f-2ec2-48be-b7c0-da26eaf5ac5e)

### **1.1.1.1.2.Denetim Faaliyet Modülünde Bekleyen Denetimler ve Plansız Denetimler Menüsünde (Bulgular Sekmesinde) Parametrik Alan Tanımlama**

### **1.1.1.1.2.1.Tarih Tipli Parametrik Alanların Listesi**

Denetim Faaliyetleri Modülünde Bekleyen Denetimler ve Plansız Denetimler menülerinde Denetim Gerçekleştir- Kayıt Güncelle ekranında Bulgular sekmesinde Yeni butonu tıklanarak açılan Bulgu Tanımlama ekranında Tarih tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Tarih yazarak Tarih tipli parametrik alanlar aratılır ve Tarih tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen tarih tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadeb3f62ec-78c7-4594-bda0-81fcc86011dc)

### **1.1.1.1.2.2.Tarih Tipli Parametrik Alan Tanımlama**

lblB_DPARAM1 Tarih tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload18b1e179-380c-4af6-90c2-e5f6c9c33b2a) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfa6fac6f-6723-4491-b6cf-65212b119672)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5f0c57f5-ce27-45e3-937a-68d93116704e)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload79bd4f84-d3ff-41f7-8f61-e774f9e4827a)(Kaydet) butonu tıklanarak tarih tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada0f0381a-2bdd-4285-93ff-7e9cf233e337)

Tanımlanan Tarih tipli parametrik alan Entegre Yönetim Sistemi\>Denetim Faaliyeti\>Bekleyen Denetimler menüsünde Denetim Gerçekleştir- Kayıt Güncelle ekranında Bulgular sekmesinde Yeni butonu tıklanarak açılan Bulgu Tanımlama ekranında görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8fe1e0e6-4260-417d-9ff4-78768a784db3)

Tanımlanan Tarih tipli parametrik alan Entegre Yönetim Sistemi\>Denetim Faaliyeti\>Plansız Denetimler menüsünde Denetim Gerçekleştir- Kayıt Güncelle ekranında Bulgular sekmesinde Yeni butonu tıklanarak açılan Bulgu Tanımlama ekranında görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload914645b0-d166-4804-81fc-15c9c650606b)

### **1.1.1.1.2.3.Liste Tipli Parametrik Alanların Listesi**

Denetim Faaliyetleri Modülünde Bekleyen Denetimler ve Plansız Denetimler menülerinde Denetim Gerçekleştir- Kayıt Güncelle ekranında Bulgular sekmesinde Yeni butonu tıklanarak açılan Bulgu Tanımlama ekranında Liste tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Liste yazarak Liste tipli parametrik alanlar aratılır ve Liste tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Liste tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5deae75d-10c2-4dba-8afd-09620a4af6ba)

### **1.1.1.1.2.4.Liste Tipli Parametrik Alan Tanımlama.**

lblL_LPARAM1 Liste tipli parametrik seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload18b1e179-380c-4af6-90c2-e5f6c9c33b2a) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload45fe8497-e3a7-4b36-9b0a-db0bbf4b40c6)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload077148d0-1032-4ab8-9671-43e2c2a69f4e)

Liste tipli alanın liste değerlerini girmek için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3da03dd1-2d83-45ab-91ff-df493b3de3ea) (Yeni) butonuna tıklanır, liste değerleri yazılır ve kaydedilir. Liste elemanı değeri 1 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4d061258-7881-4d3b-b65d-4451e26fd80f)

Liste elemanı değeri 2 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc6c835c6-6e5c-491e-9131-573458d421b1)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload134167ad-84bd-4a55-9c7f-785d80cd051c)

Alanın zorunlu olup, olmayacağı sıra no bilgisi ve liste elemanları tanımlanarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload79bd4f84-d3ff-41f7-8f61-e774f9e4827a)(kaydet) butonu tıklanarak liste tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0996af8f-53b3-41fb-bdd0-03c303b810b5)

Tanımlanan Liste tipli parametrik alan Entegre Yönetim Sistemi\>Denetim Faaliyeti\>Bekleyen Denetimler menüsünde Denetim Gerçekleştir- Kayıt Güncelle ekranında Bulgular sekmesinde Yeni butonu tıklanarak açılan Bulgu Tanımlama ekranında görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfb6a30cb-6259-4818-a275-649d4e88388d)

Tanımlanan Liste tipli parametrik alan Entegre Yönetim Sistemi\>Denetim Faaliyeti\>Plansız Denetimler menüsünde Denetim Gerçekleştir- Kayıt Güncelle ekranında Bulgular sekmesinde Yeni butonu tıklanarak açılan Bulgu Tanımlama ekranında görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadac1af40d-7a03-4198-a4cf-9dd2411fe184)

### **1.1.1.1.2.5.Metin Tipli Parametrik Alanların Listesi**

Denetim Faaliyetleri Modülünde Bekleyen Denetimler ve Plansız Denetimler menülerinde Denetim Gerçekleştir- Kayıt Güncelle ekranında Bulgular sekmesinde Yeni butonu tıklanarak açılan Bulgu Tanımlama ekranında Metin tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Metin yazarak Metin tipli parametrik alanlar aratılır ve Metin tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Metin tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload06e21396-5807-4751-8120-0b83d81d2d03)

### **1.1.1.1.2.6.Metin Tipli Parametrik Alan Tanımlama**

lblT_TPARAM1 Metin tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload18b1e179-380c-4af6-90c2-e5f6c9c33b2a) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload44536741-25ec-4b1a-8b58-768a8b9ea897)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload619b7aa8-efc7-4d7a-8c73-ed639bb4abfd)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload79bd4f84-d3ff-41f7-8f61-e774f9e4827a)(kaydet) butonu tıklanarak Metin tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload67da0f15-5b70-4148-9b38-179566ea0eaf)

Tanımlanan Metin tipli parametrik alan Entegre Yönetim Sistemi\>Denetim Faaliyeti\>Bekleyen Denetimler menüsünde Denetim Gerçekleştir- Kayıt Güncelle ekranında Bulgular sekmesinde Yeni butonu tıklanarak açılan Bulgu Tanımlama ekranında görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3afb932a-0838-4c21-9a34-5f40a0849795)

Tanımlanan Metin tipli parametrik alan Entegre Yönetim Sistemi\>Denetim Faaliyeti\>Plansız Denetimler menüsünde Denetim Gerçekleştir- Kayıt Güncelle ekranında Bulgular sekmesinde Yeni butonu tıklanarak açılan Bulgu Tanımlama ekranında görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadca50e2aa-bc91-4c33-ae01-1172f6375d7a)

### **1.1.1.1.2.7.Metin (Çoklu Satır) Tipli Parametrik Alanların Listesi**

Denetim Faaliyetleri Modülünde Bekleyen Denetimler ve Plansız Denetimler menülerinde Denetim Gerçekleştir- Kayıt Güncelle ekranında Bulgular sekmesinde Yeni butonu tıklanarak açılan Bulgu Tanımlama ekranında Metin(Çoklu Satır) tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Metin(Çoklu Satır) yazarak Metin(Çoklu Satır) tipli parametrik alanlar aratılır ve Metin(Çoklu Satır) tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Metin(Çoklu Satır) tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload88d02af5-3c55-44c2-b094-f0fad832e1cf)

### **1.1.1.1.2.8.Metin (Çoklu Satır) Tipli Parametrik Alan Tanımlama**

lblT_TPARAM4 Metin (Çoklu Satır) tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload18b1e179-380c-4af6-90c2-e5f6c9c33b2a) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9a8c9eac-bbc4-4f5e-8a3a-700ac5cc05aa)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf01cc848-077a-45b0-809e-64ec9af8c7c4)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload79bd4f84-d3ff-41f7-8f61-e774f9e4827a)(kaydet) butonu tıklanarak Metin (Çoklu Satır) tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload60d41772-264f-4a22-a8f6-37f1768c058b)

Tanımlanan Metin(Çoklu Satır) tipli parametrik alan Entegre Yönetim Sistemi\>Denetim Faaliyeti\>Bekleyen Denetimler menüsünde Denetim Gerçekleştir- Kayıt Güncelle ekranında Bulgular sekmesinde Yeni butonu tıklanarak açılan Bulgu Tanımlama ekranında görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload26318296-7074-48d4-a639-7113ddfa9ee8)

Tanımlanan Metin(Çoklu Satır) parametrik alan Entegre Yönetim Sistemi\>Denetim Faaliyeti\>Plansız Denetimler menüsünde Denetim Gerçekleştir- Kayıt Güncelle ekranında Bulgular sekmesinde Yeni butonu tıklanarak açılan Bulgu Tanımlama ekranında görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade726179a-0863-48b6-97ac-f979a00f4946)

### **1.1.1.1.2.9.Ölçü Birimi Tipli Parametrik Alanların Listesi**

Denetim Faaliyetleri Modülünde Bekleyen Denetimler ve Plansız Denetimler menülerinde Denetim Gerçekleştir- Kayıt Güncelle ekranında Bulgular sekmesinde Yeni butonu tıklanarak açılan Bulgu Tanımlama ekranında Ölçü Birimi tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Ölçü Birimi yazarak Ölçü Birimi tipli parametrik alanlar aratılır ve Ölçü Birimi tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Ölçü Birimi tipli parametrik alanların alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9dc22587-0fbc-46c2-bf7f-d028c14331ed)

### **1.1.1.1.2.10.Ölçü Birimi Tipli Parametrik Alan Tanımlama**

lblB_NPARAM1 Ölçü birimi tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload18b1e179-380c-4af6-90c2-e5f6c9c33b2a) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb2be30e9-28b8-4926-96e0-d26b8785b348)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6071498a-6bff-442d-ae2b-0c6abad0c3b9)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload79bd4f84-d3ff-41f7-8f61-e774f9e4827a)(Kaydet) butonu tıklanarak ölçü birimi tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6213cafa-725c-48f7-b100-3b7040c82bd7)

Tanımlanan Ölçü Birimi tipli parametrik alan Entegre Yönetim Sistemi\>Denetim Faaliyeti\>Bekleyen Denetimler menüsünde Denetim Gerçekleştir- Kayıt Güncelle ekranında Bulgular sekmesinde Yeni butonu tıklanarak açılan Bulgu Tanımlama ekranında görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadccf1d52c-882d-44fb-be0b-f760b14c02ff)

Tanımlanan Ölçü Birimi tipli parametik alan Entegre Yönetim Sistemi\>Denetim Faaliyeti\>Plansız Denetimler menüsünde Denetim Gerçekleştir- Kayıt Güncelle ekranında Bulgular sekmesinde Yeni butonu tıklanarak açılan Bulgu Tanımlama ekranında görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload13b195a7-6597-429c-8b38-42ad6d813901)

### **1.1.1.1.2.11.Parasal Tipli Parametrik Alanların Listesi**

Denetim Faaliyetleri Modülünde Bekleyen Denetimler ve Plansız Denetimler menülerinde Denetim Gerçekleştir- Kayıt Güncelle ekranında Bulgular sekmesinde Yeni butonu tıklanarak açılan Bulgu Tanımlama ekranında Parasal Tipli tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına Parasal yazarak Parasal tipli parametrik alanlar aratılır ve Parasal tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen Parasal tipli parametrik alanlara alan tanımlaması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload47ff1adf-4bfa-42ba-8dc5-8b32a83ae616)

### **1.1.1.1.2.12.Parasal Tipli Parametrik Alan Tanımlama**

lblB_NPARAM4 Parasal tipli alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload18b1e179-380c-4af6-90c2-e5f6c9c33b2a) (değiştir) butonuna tıklanır

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6eea53ab-49b0-49b5-af3d-ef820f43238b)

Açılan ekranda değeri alanına görmek istediğimiz alan adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4de491c2-1b87-4f7b-911c-942207cf636e)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload79bd4f84-d3ff-41f7-8f61-e774f9e4827a)(Kaydet ) butonu tıklanarak Parasal tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7f26c12e-820c-4243-9776-d760f29fbcbc)

Tanımlanan Parasal tipli parametrik alan Entegre Yönetim Sistemi\>Denetim Faaliyeti\>Bekleyen Denetimler menüsünde Denetim Gerçekleştir- Kayıt Güncelle ekranında Bulgular sekmesinde Yeni butonu tıklanarak açılan Bulgu Tanımlama ekranında görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc7460655-8598-4af9-8909-71d648c41c15)

Tanımlanan Ölçü Birimi tipli parametrik alan Entegre Yönetim Sistemi\>Denetim Faaliyeti\>Plansız Denetimler menüsünde Denetim Gerçekleştir- Kayıt Güncelle ekranında Bulgular sekmesinde Yeni butonu tıklanarak açılan Bulgu Tanımlama ekranında görüntülenir.

T![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2b66ea07-c649-4369-be11-2297809e0d44)

Denetim Gerçekleştir- Kayıt güncelleme ekranında Dil Ayarlarından Tanımlanan Tüm Parametrik Tipli Alanlar;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbbb073d9-633d-4f1e-887a-87b29a68cffd)

**1.1.1.1.1.3. Dil ayarlarında Tanımlan Parametrik Alan tipleri Görüntülen Ekrandan Kaldırma İşlemi**

1.Aşamada parametrik alanın bulunduğu ekran açılır. Örnekte Entegre Yönetim Sistemi\>Denetim Faaliyeti\>Bekleyen Denetimler menüsünde Denetim Gerçekleştir butonu tıklanarak açılanan Denetim Gerçekleştir-Kayıt Güncelle ekranında Diğer Bilgiler sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5cbcfeb9-b073-46b8-bb4c-df6f821ca48a)

2\. Aşamada Parametrik Alanın bulunduğu ekran görüntülendikten sonra örnekteki herhangi alan seçilerek, Sağ tıkla/Kopyala komutu ile parametrik alanın ismi kopyalanır. Örnek:Denetimin Açıklaması

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload485f502f-e336-4ee9-a85b-9add58e873da)

3\. Aşamada Sistem Altyapı Tanımları\>BSAT\>Konfigürasyon Ayarları\>Dil ayarları menüsü tıklanarak açılan ekranda Modül olarak Denetim Faaliyeti Modülü seçilir. Kopyalanan Dil ayarlarından tanımlanan Metin tipli parametrik alanı grid ekranında **TR** alanına sağ tıkla/yapıştır komutu ile alanın yapıştırma işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload005ca4c9-2427-410d-8d7e-87f96d7a8063)

4.Aşamada Metin Tipli tipli parametrik alan seçilerek alanın içeriği görüntülemek için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload18b1e179-380c-4af6-90c2-e5f6c9c33b2a) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload754a5e8a-f1e3-4440-ac2a-866b71ce3cd3)

5.Aşamada içeriği görüntülen metin tipli alanın değeri kısmı silerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload79bd4f84-d3ff-41f7-8f61-e774f9e4827a)(Kaydet) butonu tıklanarak Dil Ayarları menüsünde tanımlı metin tipli alanın kaldırma işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadec4a0096-9a03-4100-be60-1aa7776d042a)

Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarlarında tanımlanan diğer parametrik alan tiplerin dil ayarları menüsünde kaldırma işlemi aynı şekilde olmaktadır. Entegre Yönetim Sistemi\>Denetim Faaliyeti\>Bekleyen Denetimler menüsünde Denetim Gerçekleştir butonu tıklanarak açılanan Denetim Gerçekleştir-Kayıt Güncelle ekranında Diğer Bilgiler sekmesinde tanımlı metin tipli alanın kaldırılmış olduğu görülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5bbcb4b6-c53d-4ce1-831c-8b2af5938ef0)
